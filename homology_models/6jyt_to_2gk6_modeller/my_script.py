# Comparative modeling with multiple templates
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the automodel class

log.verbose()    # request verbose output
env = environ()  # create a new MODELLER environment to build this model in

# directories for input atom files
env.io.atom_files_directory = ['.', '../../deposited_structures']

a = automodel(env,
              alnfile  = '../../alignment_files/6jyt_to_2gk6_alignment_chainA_for_swiss.fasta', # alignment filename
              knowns   = ('2gk6'),     # codes of the templates
              sequence = '6jyt')               # code of the target
a.starting_model= 1                 # index of the first model
a.ending_model  = 1                 # index of the last model
                                    # (determines how many models to calculate)
a.make()                            # do the actual comparative modeling
