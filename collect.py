"""Collect all the themes and export to a given directory."""

import sys
import os
import shutil

if len(sys.argv) < 2:
    print("Target directory required.")
    sys.exit(1)

directory = os.path.join(sys.argv[1], 'bootswatch_css')

themes = [
    'cerulean', 'cosmo', 'cyborg', 'darkly',
    'flatly', 'journal', 'lumen', 'paper',
    'readable', 'sandstone', 'simplex', 'slate',
    'spacelab', 'superhero', 'united', 'yeti'
]

os.mkdir(directory)
for theme in themes:
    shutil.copyfile(
        os.path.join(theme, 'bootstrap.min.css'),
        os.path.join(directory, 'bootstrap-{:s}.min.css'.format(theme)))
    
    