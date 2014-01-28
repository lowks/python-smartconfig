#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def config_from_file(path):
    class SmartConfig:
        try:
            execfile(path)
        except Exception, e:
            sys.exit("E: Config load error: %s" % e)
    return SmartConfig


def config(**kwargs):
    if kwargs.has_key("local"):
        if os.path.exists(kwargs["local"]):
            return config_from_file(kwargs["local"])

    if kwargs.has_key("user"):
        if os.environ.has_key("HOME"):
            path = os.path.join(os.environ.get("HOME"), kwargs["user"])
            if os.path.exists(path):
                return config_from_file(path)

    if kwargs.has_key("system"):
        path = os.path.join("/etc", kwargs["system"])
        if os.path.exists(path):
            return config_from_file(path)

    sys.exit("E: Can't find config file")
