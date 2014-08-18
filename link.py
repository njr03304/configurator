#!/bin/python3

import os, yaml

project_dir = os.path.dirname(os.path.abspath(__file__))
manifest = yaml.load(open('manifest.yml', 'r'))

for directory in manifest['directories']:
    path = manifest['directories'][directory]['path']
    if path[0] == '~':
        path = path.replace('~', os.environ['HOME'])

    os.symlink(path, project_dir + '/configs/' + directory)
