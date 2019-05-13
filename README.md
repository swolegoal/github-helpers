# GitHub Helpers
Some handy little helper scripts that make automating and using GitHub easier.

## Known Hosts Helper

### INTRODUCTION
Over the course of automating more of the things I do with GitHub+SSH, I quickly
realized that a single entry in your `known_hosts` file isn't going to cut the
mustard.  As it turns out, GitHub has been ramping up their load balancers for
SSH, too.  What this means is that Git and SSH are going to complain a *lot*.
SSH-based automation will break whenever the load balancer hands you an IP
address that your computer has not seen before (a very likely event, given that
there are a staggering 6000+ Git IPs).

To get around this, I have designed a tool that automatically generates entries
you can use in your `~/.ssh/known_hosts` file.

### DESCRIPTION
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

`ssh_helper` takes no arguments; it simply queries GitHub's API for a current
list of Git servers and barfs out entries in the SSH `known_hosts` file format.

You can add the new entries to your SSH `known_hosts` file by redirecting
`ssh_helper`'s output like so:

```
you@yourbox $ ./ssh_helper.py >> ~/.ssh/known_hosts
```
