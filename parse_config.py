# -*- coding: utf-8 -*-

import ConfigParser, os, sys, getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "c:e:f:", ["command=", "exec=", "config="])
except getopt.GetoptError, err:
    print str(err)
    sys.exit(2)

sql = None
mysql_command = "mysql"
config_file = sys.argv[0] + "/default_settings.ini"
for o, a in opts:
    if o in ("-e", "--exec"):
        sql = a
    elif o in ("-c", "--command"):
        mysql_command = a
    elif o in ("-f", "--config"):
        config_file = a
    else:
        raise Exception("error")

if not os.path.exists(config_file):
    print "No config file '" + config_file + "'"
    sys.exit(2)

config = ConfigParser.SafeConfigParser()
#config.read('./default_settings.ini')
config.read(config_file)
sections = config.sections()
cmds = []
for section in sections:
    cmd = mysql_command
    labels = config.options(section) 
    for label in labels:
        if label == "options":
            if mysql_command == "mysql":
                cmd += " " + config.get(section, label)
        else:
            cmd += " --" + label + "=" + config.get(section, label)
    if sql is not None:
        cmd += " -e \"" + sql + "\""
    cmds.append(cmd)

for cmd in cmds:
    print cmd

# vim: set et ts=4 sts=4 sw=4 :
