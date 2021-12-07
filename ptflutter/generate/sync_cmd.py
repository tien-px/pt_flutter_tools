# coding=utf-8

from .generate_stream_debug import GenerateStreamDebugCommand
from .generate_image_cmd import GenerateImageCommand
from .generate_localization_cmd import GenerateLocalizationCommand
from .generate_object_mapper_cmd import GenerateObjectMapperCommand
from ..core.command import Command
import os


class SyncCommand(Command):
    def __init__(self):
        super(SyncCommand, self).__init__()

    def run(self):
        GenerateImageCommand().run()
        GenerateLocalizationCommand().run()
        GenerateObjectMapperCommand().run()
        # GenerateStreamDebugCommand().run()