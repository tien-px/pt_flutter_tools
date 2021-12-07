# PYTHON_ARGCOMPLETE_OK

import sys
from arghandler import subcmd, ArgumentHandler

from .usecase.usecase_cmd import UseCaseCommand
from .figma.generate_text import FigmaGenerateTextCommand
from .config.config_cmd import ConfigCommand
from .generate.generate_image_cmd import GenerateImageCommand
from .generate.generate_localization_cmd import GenerateLocalizationCommand
from .generate.generate_object_mapper_cmd import GenerateObjectMapperCommand
from .generate.generate_stream_debug import GenerateStreamDebugCommand
from .generate.sync_cmd import SyncCommand
from .create.create_cmd import CreateCommand
from .rename.rename_cmd import RenameCommand
from .template.template_cmd import TemplateCommand
from .utils.intellij import Intellij
from . import __version__

# @subcmd("create", help="")
# def cmd_create(parser, context, args):
#     parser.description = ""
#     CreateCommand().create_app()


# @subcmd("rename", help="")
# def cmd_rename(parser, context, args):
#     parser.description = ""
#     args = parser.parse_args(args)
#     RenameCommand().rename_app()


# @subcmd("template", help="")
# def cmd_template(parser, context, args):
#     parser.description = "."
#     parser.add_argument("type", nargs=1, choices=["base"], help="template type")
#     parser.add_argument("name", nargs=1, help="scene name")
#     parser.add_argument(
#         "--mock", required=False, action="store_true", help="Include mock file."
#     )
#     parser.add_argument(
#         "--test", required=False, action="store_true", help="Include unit test file."
#     )
#     parser.add_argument(
#         "--navigator", required=False, action="store_true", help=""
#     )
#     args = parser.parse_args(args)
#     template_name = args.type[0]
#     scene_name = args.name[0]
#     options = {
#         "mock": args.mock,
#         "test": args.test,
#         "navigator": args.navigator
#     }
#     TemplateCommand(template_name, scene_name, options).create_files()


@subcmd("gen", help="code generator")
def cmd_generate(parser, context, args):
    parser.description = "code generator"
    parser.add_argument(
        "type",
        nargs=1,
        choices=["image", "localization", "rx_debug", "tuples", "object_mapper"],
        help="type",
    )
    args = parser.parse_args(args)
    type = args.type[0]
    if type == "image":
        GenerateImageCommand().run()
    elif type == "localization":
        GenerateLocalizationCommand().run()
    elif type == "rx_debug":
        GenerateStreamDebugCommand().run()
    elif type == "tuples":
        print()
    elif type == "object_mapper":
        GenerateObjectMapperCommand().run()
    else:
        print("Invalid command")

# @subcmd("sync", help="")
# def cmd_template(parser, context, args):
#     parser.description = ""
#     SyncCommand().run()

# @subcmd("usecase", help="usecase")
# def cmd_template(parser, context, args):
#     parser.description = "usecase."
#     parser.add_argument("type", nargs=1, choices=["list", "add", "remove"], help="type")
#     parser.add_argument("-path", nargs=1, help="usecase path", required=True)
#     parser.add_argument("-func", nargs="+", help="functions", required=False)
#     args = parser.parse_args(args)
#     path = args.path[0]
#     type = args.type[0]
#     functions = args.func
#     if type == "list" and functions is None:
#         UseCaseCommand(path).list()
#     elif type == "add" and functions is not None:
#         UseCaseCommand(path).add(functions)
#     elif type == "remove" and functions is not None:
#         UseCaseCommand(path).remove(functions)
#     else:
#         print("Invalid command")


# @subcmd("figma", help="create template files for a scene")
# def cmd_figma(parser, context, args):
#     parser.description = "Create template files for a scene."
#     parser.add_argument(
#         "type",
#         nargs=1,
#         choices=["text"],
#         help="type",
#     )
#     parser.add_argument("input", nargs=1, help="input text")
#     args = parser.parse_args(args)
#     type = args.type[0]
#     input = args.input[0]
#     if type == "text":
#         FigmaGenerateTextCommand(input).run()
#     else:
#         print("Invalid command")


# @subcmd("config", help="project")
# def cmd_config(parser, context, args):
#     parser.description = "image"
#     parser.add_argument("key", nargs="?", help="configuration key")
#     args = parser.parse_args(args)
#     key = args.key
#     cmd = ConfigCommand()
#     if key is None:
#         cmd.info()
#     elif key == "project":
#         cmd.create_config()
#     else:
#         print("Invalid command")


def exit_handler():
    Intellij.getInstance().to_file()

def main():
    handler = ArgumentHandler(
        use_subcommand_help=True,
        enable_autocompletion=True,
        epilog="Get help on a subcommand: ptflutter subcommand -h",
    )
    handler.add_argument(
        "-v",
        "--version",
        action="version",
        version=__version__,
        help="show the version number",
    )
    if len(sys.argv) == 1:
        handler.run(["-h"])
    else:
        handler.run()
    exit_handler()

if __name__ == "__main__":
    main()
