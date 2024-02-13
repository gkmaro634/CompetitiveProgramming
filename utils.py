#!/usr/bin/env python3

import os, sys, io

def replace_stdin(fpath):
    with open(fpath, 'r') as f:
        content = f.read()
    sys.stdin = io.StringIO(content)
