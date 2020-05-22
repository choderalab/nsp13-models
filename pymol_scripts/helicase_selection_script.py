#!/usr/bin/env python3
## Author: Alex Payne 
## Date: 2020.05.21
## <https://stackabuse.com/reading-and-writing-yaml-to-a-file-in-python/>
import yaml, argparse
from pymol import cmd, stored

with open(r'selections_chainA.yaml') as file:
    proteins = yaml.full_load(file)

def domain_selection(protein, pdbid, selections = False):
    if not selections:
        selections = proteins[protein]['selections']
    for name, selection in selections.items():
        cmd.select(f'{protein}_{pdbid}_{name}', f'{pdbid} and {selection}')
        

def domain_autoselect():
    for protein, info in proteins.items():
        for structure in info['structures']:
            if structure in cmd.get_object_list():
                domain_selection(protein, structure, info['selections'])

cmd.extend('domain_selection', domain_selection)
cmd.extend('domain_autoselect', domain_autoselect)