#!/usr/bin/env python3

import os, sys, io

def replace_stdin(fpath):
    """
    標準入力を指定されたファイルの内容に置き換える
    """
    with open(fpath, 'r') as f:
        content = f.read()
    sys.stdin = io.StringIO(content)

