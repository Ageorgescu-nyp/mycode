#!/usr/bin/env python3
import shutil
import os
import os
os.chdir('/home/student/mycode/')
#move a file
shutil.move('raynor.obj', 'ceph_storage/')
xname = input('What is the new name for kerrigan.obj? ')
#move and rename
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

