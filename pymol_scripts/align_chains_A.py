#!/usr/bin/env python3
## Author: Alex Payne 
## Date: 2020.05.21
from pymol import cmd, stored
import align_all
print(cmd.get_object_list())
cmd.select('chain A')
cmd.hide('everything')
cmd.show('cartoon', 'chain A')