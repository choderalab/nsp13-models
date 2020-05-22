#!/usr/bin/env python3
## Author: Alex Payne 
## Date: 2020.05.21
## <https://stackabuse.com/reading-and-writing-yaml-to-a-file-in-python/>
import yaml, argparse
from pymol import cmd, stored

with open(r'selections_chainA.yaml') as file:
    proteins = yaml.full_load(file)

def domain_selection(protein, pdbid, sel_keys:list = False, selections:dict = False):
    DEFAULT_SEL = proteins[protein]['selections']
    for name, selection in DEFAULT_SEL.items():
        if sel_keys: 
            if selections and not name in selections:
                break
        cmd.select(f'{protein}_{pdbid}_{name}', f'{pdbid} and {selection}')
        

def domain_selecttype(protein_sel:str = False, pdbid_sel:str = False, sel_keys:list = False):
    for protein, info in proteins.items():
        print(protein, info)
        if protein_sel and not protein_sel == protein:
            break
            
        for structure in info['structures']:
            print(structure)
            if pdbid_sel and not pdbid_sel == structure:
                break
            if not structure in cmd.get_object_list():
                break
                
            sel_dict = info['selections']
            
            if not sel_keys:
                selections = sel_dict.keys()
            else:
                selections = sel_keys
            print(selections)    
            for name in selections:
                selection = sel_dict[name]
                cmd.select(f'{protein}_{structure}_{name}', f'{structure} and {selection}')

def domain_autoselect():
    for protein, info in proteins.items():
        for structure in info['structures']:
            if structure in cmd.get_object_list():
                domain_selection(protein, structure, info['selections'])

cmd.extend('domain_selection', domain_selection)
cmd.extend('domain_autoselect', domain_autoselect)
cmd.extend('domain_selecttype', domain_selecttype)