#!/usr/bin/env python

import os
import argparse
import sys
import time
import apt


parser = argparse.ArgumentParser(description='Check difference between urls')

parser.add_argument('-u', help='Pass urls. Ex: -u http://url.com?asdasdS:http://url.com')

args = parser.parse_args()
keys = ['u']
params = {}
diff_tool = 'diff'
cache = apt.Cache()
script_path = os.path.dirname(os.path.realpath(sys.argv[0]))

for k in keys:
    if args.__getattribute__(k):
        params[k] = args.__getattribute__(k)

if len(params) == 0:
    parser.print_usage()
    sys.exit()

if cache['colordiff'].is_installed:
    diff_tool = 'colordiff'
else:
    print 'You should install colordiff. apt-get install colordiff\n'

if '::' in args.u:
    urls = args.u.split('::')

    os.system('curl "%s" > %s/page1.log | curl "%s" > %s/page2.log' % (urls[0], script_path, urls[1], script_path))

    os.system('%s %s/page1.log %s/page2.log' % (diff_tool, script_path, script_path))
