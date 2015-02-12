# -*- coding: utf-8 -*-
import ConfigParser


def dict2ini(data_dict, filepath=None):
    config = ConfigParser.SafeConfigParser()
    if filepath:
        h = open(filename, 'w+')
        config.read(h)
    for section, data in data_dict.iteritems():
        config.add_section(section)
        for key, value in data.iteritems():
            config.set(section, key, value)
    if filepath:
        config.write(h)
    return config
