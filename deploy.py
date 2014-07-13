#!/bin/python3

import os, shutil, yaml, subprocess, sys

subprocess.call(['tar', '-xf', sys.argv[1]]);

project_dir = os.path.dirname(os.path.abspath(__file__))
manifest = yaml.load(open('manifest.yml', 'r'))

subprocess.call(project_dir + '/xfce4-shutdown')

for package in manifest['packages']:
    package_base_path = manifest['packages'][package]['base_path']
    package_name = manifest['packages'][package]['package']
    if package_base_path[0] == '~':
        package_base_path = package_base_path.replace('~', os.environ['HOME'])

    os.symlink(package_base_path + package_name, project_dir + '/configs/' + package_name)

    subprocess.call(["rsync", "-rk", "config/" + package_name, project_dir + '/configs/' + package_name])

subprocess.call(project_dir + '/xfce4-startup')
