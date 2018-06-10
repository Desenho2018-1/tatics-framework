import configparser
import io
import os


class Configuration(object):

    def __init__(self):
        self.IMAGE_ASSETS_PATH = ''
        self.AUDIO_ASSETS_PATH = ''
        self.paths_section = 'paths'
        self.image_assets_path = 'image_assets'
        self.audio_assets_path = 'audio_assets'

        self.load_file()
        self.load_config()
        self.correct_paths()

    def load_file(self):
        dirname = os.path.dirname(__file__)
        self.config = configparser.ConfigParser()
        self.config.read(dirname + '/config.ini')

    def load_config(self):
        self.AUDIO_ASSETS_PATH = (
            (self.config[self.paths_section][self.audio_assets_path]))

        self.AUDIO_ASSETS_PATH = self.AUDIO_ASSETS_PATH.strip("'")

        self.IMAGE_ASSETS_PATH = (
            (self.config[self.paths_section][self.image_assets_path]))

        self.IMAGE_ASSETS_PATH = self.IMAGE_ASSETS_PATH.strip("'")