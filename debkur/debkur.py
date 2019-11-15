#!/usr/bin/env python3
import os,sys

if os.geteuid() != 0:
  print("\33[91mYou must be root for run this program")
else:
    args = ""
    for arg in sys.argv[1:]:
        args += arg+" "
    if len(args) > 0:
        os.system("dpkg -i {}".format(args))
    else:
        print("\33[32m==> debkur.py [*.deb]")
