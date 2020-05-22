## Author: Alex Payne 
## Date: 2020.05.21
## <https://stackabuse.com/reading-and-writing-yaml-to-a-file-in-python/>
import yaml, argparse
from pymol import cmd, stored

with open(r'selections.yml') as file:
    proteins = yaml.full_load(file)
    print(proteins['selections']) 

def domain_selection(protein, pdbid):
    for name, resi in proteins['selections'].items():
        cmd.select(f'{protein}_{name}', f'resi {resi}')

cmd.extend('domain_selection', domain_selection)