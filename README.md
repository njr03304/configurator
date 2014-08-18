Configuration Deployer
======================
Deploy various configuration files through the magic of symlinks.

Basic Usage
------------------------------------
- Build Symlinks
- Push Config changes through symlinks with rsync
- Retrieve changes to config files and push them somewhere else

Dependencies
------------------------------------
    sudo yum install python3-PyYAML

Build the Symlinks
------------------------------------
    ./link.py

Deploy a set of configuration files
------------------------------------
    ./deploy.py config/config

`config/config` is assumed to be a directory containing configuration files.  This would ideally be a git repo.  The files must be in `manifest.yml`.

Retrieve a set of configurationj files
-------------------------------------
    ./retrieve.py config/config

`config/config` is assumed to be a directory containing configuration files.  This would ideally be a git repo.  The files must be in `manifest.yml`.

To add a new config file to the list
-------------------------------------
Add a reference to `manifest.yml`.

Re-build symlinks

Deploy and Retrieve as you desire
