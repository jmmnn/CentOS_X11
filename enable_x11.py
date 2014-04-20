#!/usr/bin/env python
__author__ = 'jmmnn'
# this script sets up the RHEL or CentOS server for X11 and Gui access

import subprocess
import sys

# Read the file
filedata = 'a'
with open('/etc/inittab', 'r') as file:
  filedata = file.read()
  print 'original content'
  print filedata + '\n'

# Replace the target string
filedata2 = filedata.replace('id:3:initdefault', 'id:5:initdefault')
print 'new content'
print filedata2 + '\n'
# Write the file out again
with open('/etc/inittab', 'w') as file2:
  file2.write(filedata2)



#List bash commands to execute here.

# desktop, firewall, clock, reboot
XWINDOWS = "yum groupinstall 'X Window System' Desktop"
NTPD = "sudo chkconfig ntpd on"
IPTABLES_OFF = "sudo chkconfig iptables off"
IPTABLES_STOP = "sudo /etc/init.d/iptables stop"
NTPD_START = "sudo service ntpd start"
REBOOT = "sudo chkconfig iptables off"

#order commands in sequence
cmds = [XWINDOWS, NTPD, IPTABLES_OFF, IPTABLES_STOP, NTPD_START, REBOOT]

#Iterates over list, running statements for each item in the list
count=0
for cmd in cmds:
    count+=1
    print "Running Command Number %s" % count
    subprocess.call(cmd, shell=True)