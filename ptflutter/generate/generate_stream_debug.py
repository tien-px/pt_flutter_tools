# coding=utf-8

import glob
import re
from ..core.command import Command
from jinja2 import Environment, PackageLoader
from ..utils.file_helpers import *
from ..utils.utils import *


class ViewModelDebug:
    def __init__(self, method_name, output_class_name,  inputs, outputs):
        self.method_name = method_name
        self.output_class_name = output_class_name
        self.inputs = inputs
        self.outputs = outputs

    def __str__(self):
            return f"ViewModelDebug: {self.method_name} - {self.inputs} - {self.outputs}"


class GenerateStreamDebugCommand(Command):
    def __init__(self):
        super(GenerateStreamDebugCommand, self).__init__()

    def run(self):
        import_files = []
        items = []
        # Find all view model files
        for file in glob.glob("lib/**/*_viewmodel.dart", recursive=True):
            with open(file, "r+", encoding="utf8") as f:
                reg_exp = r"RxDebug.(.*)\(\[(.*|\n([^\]]*))\]\,"
                vmo_reg_exp = r"^class (.*)VMO {((?:.|\n)*)}";
                output_reg_exp = r"(?:.*) (.*) =(?:.*).obs";
                content = f.read()
                result = re.findall(reg_exp, content, re.MULTILINE)
                if result:
                    import_files.append(file)
                    method_name = result[0][0]
                    vmo = re.findall(vmo_reg_exp, content, re.MULTILINE)
                    output_class_name = vmo[0][0]
                    try:
                        input = list(map(lambda t: t.strip(), result[0][1].strip('\t\n\r').split(",")))
                        output = list(map(lambda t: t.strip(), re.findall(output_reg_exp, vmo[0][1], re.MULTILINE)))
                        items.append(ViewModelDebug(method_name, output_class_name, input, output))
                    except Exception as e:
                        items.append(ViewModelDebug(method_name, output_class_name, [], []))
        package_name = get_current_dart_package_name()
        import_files = list(dict.fromkeys(import_files))
        import_files = list(map(lambda x: x.replace("lib\\", 'package:%s/' % package_name).replace('\\','/'), import_files))
        env = Environment(
            loader=PackageLoader('ptflutter_templates', 'gen'),
            trim_blocks=True,
            lstrip_blocks=True
        )
        template = env.get_template("rx_debug.dart")
        content = template.render(
            import_files = import_files,
            items=items,
        )
        output_file = create_file(content, "rx_debug", "g.dart", "lib/generated")
        log("[Updated] {}".format(output_file))
