#!/usr/bin/env python3

import os, sys, io

def replace_stdin(fpath):
    with open(fpath, 'r') as f:
        content = f.read()
    sys.stdin = io.StringIO(content)

def read_string():
    return input()

def read_value():
    return int(input())

def read_two_values():
    a, b = list(map(int, input().split()))
    return a, b

def read_values():
    return list(map(int, input().split()))