# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser


class BaseParser:
    def __init__(self, path):
        self.config = {}
        self.config_file = path
        self._load_config()

    def _load_config(self):
        self.raw_config = SafeConfigParser()
        self.raw_config.read(self.config_file)
        self._parse_config()

    def _parse_config(self):
        for section in self.raw_config.sections():
            self.config[section.lower()] = {}
            for k, v in self.raw_config.items(section):
                self.config[section.lower()][k] = v.isdigit() and int(v) or v
