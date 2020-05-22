## Author: Alex Payne 
## Date: 2020.05.21
## <https://stackabuse.com/reading-and-writing-yaml-to-a-file-in-python/>
import yaml, argparse
from pymol import cmd, stored

with open(r'selections.yml') as file:
    proteins = yaml.full_load(file)

def domain_selection(protein, pdbid, selections):
    for name, resi in selections.items():
        cmd.select(f'{protein}_{pdbid}_{name}', f'{pdbid} and resi {resi}')
        

def domain_autoselect():
    for protein, info in proteins.items():
        for structure in info['structures']:
            domain_selection(protein, structure, info['selections'])

cmd.extend('domain_selection', domain_selection)
cmd.extend('das', domain_autoselect)