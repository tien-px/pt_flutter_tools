# coding=utf-8

import json
from sys import path
from ..utils.utils import *
from ..utils.dart_helpers import *
from ..utils.file_helpers import *
from ..core.command import Command
import re


class UseCaseCommand(Command):
    def __init__(self, usecase_path):
        super(UseCaseCommand, self).__init__()
        self.usecase_path = usecase_path

    def list(self):
        try:
            class_reg_exp = r"abstract class (.*)Type \{\n([^\]]*?)\}"
            dict = {"all": [], "selected": []}
            for dart_file in find_dart_files("lib/domain/usecase"):
                (file, content) = read_dart_file(dart_file)
                matches = re.findall(class_reg_exp, content, re.MULTILINE)
                for match in matches:
                    class_name = match[0]
                    content = match[1]
                    methods = get_abstract_methods_from_string(content)
                    dict["all"].append(
                        {
                            "name": class_name,
                            "functions": methods,
                            "path": file.name.replace("\\", "/"),
                        }
                    )
            methods = get_abstract_methods_from_path(self.usecase_path)
            dict["selected"].append(methods)
            output_json = json.dumps(dict, sort_keys=True, indent=4)
            logResult(output_json)
        except Exception as e:
            logError(e)
            exit(1)

    def add(self, functions):
        # Find file location of function
        try:
            new_usecase_class = []
            new_import_files = []
            # Read current usecase file
            (current_file, current_content) = read_dart_file(path=self.usecase_path)
            # Get current class name
            current_class_name = get_dart_class_name(current_content)
            current_abstract_methods = get_abstract_methods_from_string(current_content)
            new_abstract_methods = list(set(functions) - set(current_abstract_methods))
            # Find location of new methods
            for new_method in new_abstract_methods:
                for domain_usecase_file_path in find_dart_files("lib/domain/usecase"):
                    (usecase_file, usecase_content) = read_dart_file(
                        path=domain_usecase_file_path
                    )
                    if new_method in usecase_content:
                        path = get_path_from_file(usecase_file)
                        # Load all import
                        class_name = get_dart_class_name(usecase_content)
                        import_for_current_file = "import 'package:{}/{}';".format(
                            get_current_dart_package_name(),
                            path.replace("lib/", ""),
                        )
                        imports = get_imports_from_string(usecase_content)
                        new_usecase_class.append(class_name)
                        new_import_files.append(import_for_current_file)
                        new_import_files += imports
            # Remove duplicate for new data
            new_usecase_class = list(dict.fromkeys(new_usecase_class))
            new_import_files = list(dict.fromkeys(new_import_files))
            # Skip if no change
            if not new_usecase_class:
                log("No Change")
                return
            # Insert new import files for current usecase file
            insert_dart_imports(self.usecase_path, new_import_files)
            # Insert new methods for current usecase file
            insert_dart_abstract_methods(self.usecase_path, new_abstract_methods)
            # Extend mixin
            insert_dart_class_mixin(self.usecase_path, new_usecase_class)
            # Case: Mock file
            self.sync_usecase_to_mock_file(new_abstract_methods)
            # Format file
            format_dart_file_code(self.usecase_path)
            # Print
            current_path = get_path_from_file(current_file)
            log("[Updated] {}".format(current_path))
            logAndOpenfile(current_path)
            # logAndCommand("code_insight.optimize_imports")
        except Exception as e:
            logError(str(e))

    def sync_usecase_to_mock_file(self, new_methods=None):
        if new_methods is None:
            print("New_methods is None")
        else:
            print("New_methods is not None")
        (current_file, _) = read_dart_file(path=self.usecase_path)
        current_path = get_path_from_file(current_file)
        current_file_name_without_extension = os.path.splitext(
            os.path.basename(current_path)
        )[0]
        mock_file_path = "lib\mock\{}_mock.dart".format(
            current_file_name_without_extension
        )
        # Check if mock file exist
        if is_file_path_exist(mock_file_path) and new_methods:
            (_, mock_file_content) = read_dart_file(mock_file_path)
            new_mock_methods = list(
                map(
                    lambda x: "@override\n  "
                    + x.replace(");", ") { throw UnimplementedError(); }"),
                    new_methods,
                )
            )
            insert_dart_class_methods(mock_file_path, new_mock_methods)
            current_working_dictionary = (
                os.path.abspath(os.getcwd()).replace("\\", "/") + "/lib/"
            )
            import_usecase = "import 'package:{}/{}';".format(
                get_current_dart_package_name(),
                current_path.replace(current_working_dictionary, ""),
            )
            # Read new file changed
            # Remove all import
            (_, mock_file_content) = read_dart_file(mock_file_path)
            current_mock_imports = get_imports_from_string(mock_file_content)
            output_mock_content = mock_file_content.replace(
                "".join(current_mock_imports),
                "",
            )
            write_dart_file(mock_file_path, output_mock_content)
            # Replace import from usecase
            current_imports = get_imports_from_path(self.usecase_path)
            insert_dart_imports(mock_file_path, [import_usecase] + current_imports)
            # Format and log
            format_dart_file_code(mock_file_path)
            log("[Updated] {}".format(mock_file_path))

    def remove(self, functions):
        print("Remove")
