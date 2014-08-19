#!/bin/python3

import os, yaml, subprocess, sys

archive = sys.argv[1]

project_dir = os.path.dirname(os.path.abspath(__file__))
manifest = yaml.load(open('manifest.yml', 'r'))

subprocess.call(project_dir + '/xfce4-shutdown')

for package in manifest['packages']:
    manifest_element = manifest['packages'][package]
    package_directory = manifest_element['directory']
    package_name = manifest_element['package']
    if package_directory[0] == '~':
        package_directory = package_directory.replace('~', os.environ['HOME'])

    print('Deploying ' + package_name)
    call = ["rsync", "-rK", archive + "/" + package_name, project_dir + '/configs/' + package_directory]
    if 'use_sudo' in manifest_element and manifest_element['use_sudo']:
        call.insert(0, 'sudo')

    subprocess.call(call)

subprocess.call(project_dir + '/xfce4-startup')
