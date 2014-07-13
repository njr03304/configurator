Configuration Deployer
======================

Deploy a set of configuration files
------------------------------------
    python3 deploy.py config.tgz

`config.tgz` is assumed to be an archived copy of configuration files stored in a single directory called `config`.  The files must be in `manifest.yml`.


To archive the current configuations
-------------------------------------
    mv configs config; tar -h -czf config.tgz config; mv config configs;


To add a new config file to the list
-------------------------------------
Add a reference to `manifest.yml`.

Create a symlink to the file or directory in `configs`

Archive the current config (see above)
