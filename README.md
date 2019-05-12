# GitHub Helpers
Some handy little friends that make using GitHub a little easier.

## Known Hosts Helper
`ssh_helper.py` is a simple Python script that prints valid `known_hosts`
entries to STDOUT based on the IP ranges listed in the `git` block at the
GitHub API's `/meta` endpoint.

It is a pretty stupid program as of now, but it does work.  Eventually I will
try to consolidate `/24` subnets into globs, where possible.  For now, feast on
your new >6000 line `known_hosts` file!

### DEPENDENCIES
I have not added a `requirements` file or a `setup.py` file yet, but there is
only a single dependency as of now: [ipcalc](https://github.com/tehmaze/ipcalc).

You can grab it with this one-liner (you may need to use `sudo` here):
```
you@yourbox $ pip3 install ipcalc
```

### USAGE
```
you@yourbox $ ./ssh_helper.py
```
