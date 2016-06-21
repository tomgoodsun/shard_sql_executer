# -*- coding: utf-8 -*-

import ConfigParser, os, sys

config = ConfigParser.SafeConfigParser()
config.read('./default_settings.ini')
sections = config.sections()
cmds = []
for section in sections:
    cmd = 'mysql '
    labels = config.options(section) 
    for label in labels:
        if label == 'options':
            cmd += config.get(section, label) + ' '
        else:
            cmd += label + '=' + config.get(section, label) + ' '
    cmds.append(cmd)

for cmd in cmds:
    print cmd

