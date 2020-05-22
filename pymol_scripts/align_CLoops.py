#!/usr/bin/env python3
## Author: Alex Payne 
## Date: 2020.05.21
from pymol import cmd, stored

cmd.run('helicase_selection_script.py')
pymol.domain_autoselect()

chainA_list = [sel for sel in cmd.get_names('selections') if 'CLoop' in sel]
chainA_list.remove('SARS_nsp13_6jyt_CLoop')
print(chainA_list)

for selection in chainA_list:
    cmd.align(selection, 'SARS_nsp13_6jyt_CLoop')
#cmd.align('SARS_nsp13_6jyt_chainA', chainA_list)
cmd.select('chain A')
cmd.hide('everything')
cmd.show('cartoon', 'chain A')
cmd.center('SARS_nsp13_6jyt_CLoop')