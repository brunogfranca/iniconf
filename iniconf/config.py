# -*- coding: utf-8 -*-
from os import listdir
from os.path import isdir, isfile, join
from iniconf.libs import utils
from iniconf.base import BaseParser


class Config:
    def __init__(self, config_paths):
        self.config_paths = config_paths
        self._get_config_files()
        self._load_config()

    def _get_config_files(self):
        self.config_files = []
        for path in self.config_paths:
            if isfile(path):
                self.config_files.append(path)
            elif isdir(path):
                files = [f for f in listdir(path) if isfile(join(path, f)) and f.lower().endswith('.ini')]
                files.sort()
                self.config_files += files

    def _load_config(self):
        self.config = {}
        for f in self.config_files:
            cfg = BaseParser(f)
            utils.deepUpdate(self.config, cfg.config)