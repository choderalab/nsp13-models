#!/usr/bin/env python3
## Author: Alex Payne 
## Date: 2020.05.21
from pymol import cmd, stored
from startup_pkg import align_all as aa
run 'startup_pkg/align_all.py'

chainA_list = [sel for sel in cmd.get_object_list() if 'chainA' in sel]

align_all 6jyt
#print(cmd.get_object_list())
#cmd.select('chain A')
#cmd.hide('everything')
#cmd.show('cartoon', 'chain A')