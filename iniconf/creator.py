# -*- coding: utf-8 -*-
import collections
import getpass
from os.path import join
from copy import deepcopy
from ConfigParser import RawConfigParser
from iniconf.libs import utils
from iniconf.base import BaseParser


class IniCreator:
    def __init__(self, template_path, destination_path):
        self.template_path = template_path
        self.destination_path = destination_path

    def _get_config(self, key, value, path=''):
        if path:
            path = '.'.join([path,key])
        else:
            path = key
        if isinstance(value, collections.Mapping):
            for k, v in value.iteritems():
                self._get_config(k, v, path)
        else:
            curr_value = utils.get_inner_key(self.current_config, path)
            change = 'Y'
            if curr_value:
                old_value = curr_value
                if 'password' in path:
                    old_value = 'OLD PASSWORD'
                change_question = 'Do you want to change the current value for %s? (%s) [y/N]' %(path, old_value)
                change = raw_input(change_question)
                if change == '':
                    change = 'N'
                while change.lower() not in ['y', 'n']:
                    change = raw_input(change_question)
                    if change == '':
                        change = 'N'
            new_value = ''
            if change.lower() == 'y':
                question = 'Set the value of %s' %path
                if 'password' in path:
                    new_value = getpass.getpass(question+": ")
                else:
                    question = '%s - DEFAULT "%s":' %(question, value)
                    new_value = raw_input(question)
                if not new_value:
                    new_value = value
                self.config[path] = new_value
            else:
                self.config[path] = curr_value

    def generate_file(self, reset_file=False):
        self.template_config = BaseParser(self.template_path).config
        self.current_config = BaseParser(self.destination_path).config
        if not reset_file:
            template_config = deepcopy(self.current_config)
            utils.deepUpdate(template_config, self.template_config)
            self.template_config = template_config
        self.config = {}
        for k, v in self.template_config.iteritems():
            self._get_config(k, v)

        self._create_file()

    def _create_file(self):
        cfg = RawConfigParser()
        sections = []
        for item, value in self.config.iteritems():
            section, key = item.split('.')
            if section not in sections:
                cfg.add_section(section)
                sections.append(section)
            cfg.set(section, key, value)
        with open(self.destination_path, 'wb') as configfile:
            cfg.write(configfile)