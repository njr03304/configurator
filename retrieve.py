#!/bin/python3

import os, yaml, subprocess, sys

archive = sys.argv[1]

project_dir = os.path.dirname(os.path.abspath(__file__))
manifest = yaml.load(open('manifest.yml', 'r'))

for package in manifest['packages']:
    package_directory = manifest['packages'][package]['directory']
    package_name = manifest['packages'][package]['package']
    if package_directory[0] == '~':
        package_directory = package_directory.replace('~', os.environ['HOME'])

    print('Retrieving ' + package_name)
    subprocess.call(["rsync", "-r", "--copy-links", project_dir + '/configs/' + package_directory + '/' + package_name, archive])
