#!/usr/bin/env python3

import os
import sys
from pathlib import Path
import pytest

# @pytest.fixture()
# def addpath():
#     sys.path.append(".")

@pytest.fixture()
def test_init():
    sys.path.append("./py")
    pass

if __name__  == "__main__":
    test_init()
