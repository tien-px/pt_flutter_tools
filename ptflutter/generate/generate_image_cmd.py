# coding=utf-8

from ..core.command import Command
from jinja2 import Environment, PackageLoader
from ..utils.str_helpers import snake_to_camel, plural_to_singular
from ..utils.file_helpers import create_file
import os

class ImageFile(object):
        def __init__(self, image_name, image_file):
            self.image_name = image_name
            self.image_file = image_file

class GenerateImageCommand(Command):
    def __init__(self):
        super(GenerateImageCommand, self).__init__()

    def run(self):
        image_path = "lib/assets/images"
        path = "%s/%s" % (os.getcwd(), image_path)
        list_image_files = []
        for file in os.listdir(path):
            if file.endswith(".png") or file.endswith(".jpg"):
                file_name = os.path.splitext(file)[0].replace("-","_")
                list_image_files.append(ImageFile(snake_to_camel(file_name), file))
        env = Environment(
            loader=PackageLoader('ptflutter_templates', 'gen'),
            trim_blocks=True,
            lstrip_blocks=True
        )
        template = env.get_template("images.dart")
        content = template.render(
            image_folder=image_path,
            files=list_image_files
        )
        create_file(content, "images", "g.dart", "lib/generated")