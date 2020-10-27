#!/usr/bin/env python3
import shutil
import os
#starts in home dir
os.chdir('/home/student/mycode/')
#copy file
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')
#copy dir tree
shutil.copytree('5g_research/', '5g_research_backup/')

