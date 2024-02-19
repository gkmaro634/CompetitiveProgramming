
import pytest
import os
import sys
import io
from pathlib import Path

data_dir = Path(__file__).parent / "data"

@pytest.fixture()
def setup(test_init):
    fpath = os.path.join(data_dir, 'test_handinput.txt')
    with open(fpath, 'r') as f:
        content = f.read()
    sys.stdin = io.StringIO(content)

def test_script(setup):
    import script

    r = script.execute()
    assert r == "665683269"
