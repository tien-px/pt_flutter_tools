# coding=utf-8

import os
from datetime import datetime
from jinja2 import Environment, PackageLoader

from ..utils.utils import *
from ..utils.str_helpers import upper_first_letter, lower_first_letter
from ..utils.file_helpers import create_file
import re

class ProjectInfo:

    def __init__(self, project, developer, company, project_id):
        self.project = project
        self.developer = developer
        self.company = company
        self.project_id = project_id


class Template(object):

    class TemplateType:
        BASE = 'base'

    # =============== BaseTemplate ===============

    class BaseTemplate(object):
        def __init__(self, options, name, package_name):
            self.name = name
            self.short_name = self.create_file_name(self.name)
            self.package_name = package_name
            self.include_mock = options.mock
            self.include_test = options.test
            self.include_navigator = options.navigator
            self.output_path = '.'

            self.env = Environment(
                loader=PackageLoader('ptflutter_templates', 'base'),
                trim_blocks=True,
                lstrip_blocks=True
            )

            self.file_header_env = Environment(
                loader=PackageLoader('ptflutter_templates', 'commands'),
                trim_blocks=True,
                lstrip_blocks=True
            )

        def create_files(self):
            # Register
            log('Successfully created files:')
            # Base
            self._create_assembler()
            self._create_view()
            self._create_navigator()
            self._create_use_case()
            self._create_view_model()
            # Mock
            if self.include_mock:
                self._create_use_case_scene_mock()
            # Test
            if self.include_test:
                self._create_view_model_tests()
                self._create_use_case_mock()
                self._create_navigator_mock()
            # if self.include_navigator:
            #     self._register_navigator()

        def _make_dirs(self, path):
            current_directory = os.getcwd() if self.output_path == '.' else self.output_path
            self._make_dir(current_directory, path)

        def _make_dir(self, current_directory, new_directory_name):
            directory = os.path.join(current_directory,
                                     r'{}'.format(new_directory_name))
            try:
                os.makedirs(directory)
            except Exception as e:
                # print(e)
                pass
            return directory

        def _create_file_from_template(self,
                                       class_name,
                                       file_extension="dart",
                                       template_file=None,
                                       include_root_folder=True,
                                       output_path=None):
            if template_file is None:
                if file_extension:
                    template_file = '{}.{}'.format(class_name, file_extension)
                else:
                    template_file = class_name[len(self.short_name):]

            file_name = '{}.{}'.format(class_name, file_extension) \
                if file_extension is not None else class_name

            template = self.env.get_template(template_file)
            content = self._content_from_template(template)

            if output_path is None:
                output_path = './'

            if output_path.endswith('/'):
                output_path = output_path[:-1]

            if include_root_folder:
                folder = './{}/{}'.format(output_path, self.short_name)
            else:
                folder = './{}'.format(output_path)

            file_path = create_file(
                content=content,
                file_name=class_name,
                file_extension=file_extension,
                folder=folder
            )

            if file_path is not None:
                log('    {}'.format(file_path))
        
        def is_camel_case(self, s):
            return s != s.lower() and s != s.upper() and "_" not in s

        def create_file_name(self, class_name):
            if self.is_camel_case(class_name):
                upper_case_letters = re.findall('[A-Z][^A-Z]*', class_name)
                return '_'.join(upper_case_letters).lower()
            else:
                logError('Invalid filename. Filename need to be camel string.\nFor example: MyCamelCase')
                exit(1)

        def _content_from_template(self, template):
            return template.render(
                name=self.name,
                name_lower=self.short_name,
                package_name=self.package_name,
                include_mock=self.include_mock,
                include_test=self.include_test,
            )

        def _create_view_model(self):
            scene_name = 'viewmodel'
            self._create_file_from_template(
                class_name=self.short_name + '_' + scene_name,
                template_file='{}.dart'.format(scene_name),
                output_path='lib/scenes'
            )

        def _create_navigator(self):
            scene_name = 'navigator'
            self._create_file_from_template(
                class_name=self.short_name + '_' + scene_name,
                template_file='{}.dart'.format(scene_name),
                output_path='lib/scenes'
            )

        def _create_use_case(self):
            scene_name = 'usecase'
            self._create_file_from_template(
                class_name=self.short_name + '_' + scene_name,
                template_file='{}.dart'.format(scene_name),
                output_path='lib/scenes'
            )

        def _create_binding(self):
            scene_name = 'binding'
            self._create_file_from_template(
                class_name=self.short_name + '_' + scene_name,
                template_file='{}.dart'.format(scene_name),
                output_path='lib/scenes'
            )

        def _create_assembler(self):
            scene_name = 'assembler'
            self._create_file_from_template(
                class_name=self.short_name + '_' + scene_name,
                template_file='{}.dart'.format(scene_name),
                output_path='lib/scenes'
            )

        def _create_view(self):
            scene_name = 'view'
            self._create_file_from_template(
                class_name=self.short_name + '_' + scene_name,
                template_file='{}.dart'.format(scene_name),
                output_path='lib/scenes'
            )

        # =============== Mock ===============

        def _create_use_case_scene_mock(self):
            scene_name = 'usecase_mock'
            self._create_file_from_template(
                class_name=self.short_name + '_' + scene_name,
                template_file='{}.dart'.format(scene_name),
                include_root_folder=False,
                output_path='lib/mock'
            )

        # =============== UnitTests ===============

        def _create_view_model_tests(self):
            scene_name = 'viewmodel_test'
            self._create_file_from_template(
                class_name=self.short_name + '_' + scene_name,
                template_file='{}.dart'.format(scene_name),
                output_path='test/unit_test'
            )

        def _create_use_case_mock(self):
            scene_name = 'usecase_mock'
            self._create_file_from_template(
                class_name=self.short_name + '_' + scene_name,
                template_file='{}.dart'.format(scene_name),
                output_path='test/unit_test'
            )

        def _create_navigator_mock(self):
            scene_name = 'navigator_mock'
            self._create_file_from_template(
                class_name=self.short_name + '_' + scene_name,
                template_file='{}.dart'.format(scene_name),
                output_path='test/unit_test'
            )

        # =============== Other ===============

        def _register_assembler(self):
            try:
                path = 'lib/assembler.dart'
                with open(path, 'r') as file :
                    filedata = file.read()
                import_file = "import 'package:{}/scenes/{}/{}_assembler.dart';\n".format(self.package_name, self.short_name, self.short_name)
                filedata =  import_file + filedata
                if 'with' in filedata:
                    filedata = filedata.replace(' {}', ', {}Assembler {{}}'.format(self.name))
                else:
                    filedata = filedata.replace(' {}', 'with {}Assembler {{}}'.format(self.name))
                with open(path, 'w') as file:
                    file.write(filedata)
                print('    ./lib/assembler.dart')
            except (IOError, OSError) as e:
                print("Can't find assembler.dart")
                exit(1)

        def _register_navigator(self):
            log('Successfully updated files:')
            name = self.short_name
            try:
                path = './lib/scenes/app/app_pages.dart'
                import_reg_exp = r"import ('(.*)';|\"(.*)\";)"
                route_reg_exp = r"class Routes \{\n([^\]]*)\}"
                pages_reg_exp = r"static final pages = \[\n([^\]]*)\]"
                with open(path, 'r+', encoding='utf8') as f :
                    content = f.read()
                    # Import
                    imports = re.findall(import_reg_exp, content, re.MULTILINE)[-1][0]
                    package_name = get_current_dart_package_name()
                    import_1 = "\nimport 'package:%s/scenes/%s/%s_binding.dart';" %(package_name, name, name)
                    import_2 = "\nimport 'package:%s/scenes/%s/%s_view.dart';" %(package_name, name, name)
                    content = content.replace(imports, imports + import_1 + import_2)
                    # Routes
                    routes = re.findall(route_reg_exp, content, re.MULTILINE)[0]
                    route = "  static const %s = '/%s';\n" % (name.upper(), name.lower())
                    content = content.replace(routes, routes + route)
                    # Pages
                    match = re.findall(pages_reg_exp, content, re.MULTILINE)[0]
                    if match.strip()[-1] != ",":
                        content = content.replace(match, "    %s,\n" % match.strip())
                    pages = re.findall(pages_reg_exp, content, re.MULTILINE)[0]
                    name_title = name.title().replace("_", "")
                    page = "    GetPage(name: Routes.%s, page: () => %sView(), binding: %sBinding()),\n" % (name.upper(), name_title, name_title)
                    content = content.replace(pages, pages + page)
                    # Write to file
                    f.seek(0)
                    f.write(content)
                    f.truncate()
                    f.close()
                    log('    {}'.format(path))
            except (IOError, OSError) as e:
                print("Can't find app_pages.dart")
                exit(1)
            except Exception as e:
                print(e)
                exit(1)
            try:
                path = './lib/scenes/base/base_navigator.dart'
                abstract_func_reg_exp = r"(void (.*)();)"
                func_reg_exp = r"class BaseNavigator (?:.*) \{\n([^\]]*)\}"
                with open(path, 'r+', encoding='utf8') as f :
                    content = f.read()
                    name_title = name.title().replace("_", "")
                    # Abstract functions
                    abstract_funcs = re.findall(abstract_func_reg_exp, content, re.MULTILINE)[-1][0]
                    abstract_func = "\n  void to%s();" % (name_title)
                    content = content.replace(abstract_funcs, abstract_funcs + abstract_func)
                    # Functions
                    functions = re.findall(func_reg_exp, content, re.MULTILINE)[0]
                    function = "\n  @override\n  void to%s() {\n    Get.toNamed(Routes.%s);\n  }\n" % (name_title, name.upper())
                    content = content.replace(functions, functions + function)
                    # Write to file
                    f.seek(0)
                    f.write(content)
                    f.truncate()
                    f.close()
                    log('    {}'.format(path))
            except (IOError, OSError) as e:
                print("Can't find base_navigator.dart")
                exit(1)
            except Exception as e:
                print(e)
                exit(1)