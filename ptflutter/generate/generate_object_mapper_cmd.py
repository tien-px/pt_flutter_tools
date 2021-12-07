# coding=utf-8

import glob
import re
from ..core.command import Command
from jinja2 import Environment, PackageLoader
from ..utils.file_helpers import *
from ..utils.utils import *

class GenerateObjectMapperCommand(Command):
    def __init__(self):
        super(GenerateObjectMapperCommand, self).__init__()

    def run(self):
        import_files = []
        classes = []
        for f in glob.glob('lib/**/*.dart', recursive=True):
            textfile = open(f, 'r')
            reg = re.compile("class (.*) (?:with Mappable|extends BaseAPIOutput|extends APIOutput)")
            for line in textfile:
                for match in reg.findall(line):
                    import_files.append(f)
                    classes.append(match)
            textfile.close()
        classes = list(dict.fromkeys(classes))
        import_files = list(dict.fromkeys(import_files))
        if not classes:
            log("Can't find any mapper file")
            return
        package_name = get_current_dart_package_name()
        import_files = list(map(lambda x: x.replace("lib\\", 'package:%s/' % package_name).replace('\\','/'), import_files))
        env = Environment(
            loader=PackageLoader('ptflutter_templates', 'gen'),
            trim_blocks=True,
            lstrip_blocks=True
        )
        template = env.get_template("entities.dart")
        content = template.render(
            import_files=import_files,
            classes=classes
        )
        output_file = create_file(content, "entities", "g.dart", "lib/generated")
        log("[Updated] {}".format(output_file))