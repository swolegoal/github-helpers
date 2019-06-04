#!/usr/bin/env python3

import requests
import ipcalc

# This is GitHub's public RSA host key.
gh_pubkey  = 'ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa' \
           + '+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJ' \
           + 'NlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5Q' \
           + 'lWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaas' \
           + 'XVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua' \
           + '2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ=='

# GitHub provides a list of their Git servers via their API's /meta endpoint.
req = requests.get('https://api.github.com/meta')
gitnets = req.json()['git']

for net in gitnets:
  for ip in ipcalc.Network(net):
    gitservers = ['*.github.com']
    gitservers.append(ip.to_compressed())
    s_gitservers = ','.join(gitservers)
    print(s_gitservers + ' ' + gh_pubkey)
