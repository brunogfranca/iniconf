# -*- coding: utf-8 -*-
import collections


def deepUpdate(d, u):
    for k, v in u.iteritems():
        if isinstance(v, collections.Mapping):
            r = deepUpdate(d.get(k, {}), v)
            d[k] = r
        else:
            d[k] = u[k]
    return d


def get_inner_key(_dict, path, default=None):
    return reduce(lambda obj, key: obj.get(key, {}), path.split('.'), _dict) or default