#!/usr/bin/python
#Jeremy Galloway

import sys
import iptools #https://github.com/bd808/python-iptools

with open(sys.argv[1], 'r') as f:
	iplist = [line.strip() for line in f]
print "\nValid IPv6 Addresses contained within the file include:\n"
for line in iplist:
	if iptools.ipv6.validate_ip(line):
		print line