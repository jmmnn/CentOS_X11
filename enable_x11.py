#!/usr/bin/env python
__author__ = 'jmmnn'

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

