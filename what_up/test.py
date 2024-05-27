#!/usr/bin/env python3
"""tests for what_up.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './what_up.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_runnable():
    """Runs using python3"""

    out = getoutput(f'python3 {prg}')
    assert out.strip() == 'What up, humanoid!'


# --------------------------------------------------
def test_executable():
    """Says 'What up, everyone!' by default"""

    out = getoutput(prg)
    assert out.strip() == 'What up, humanoid!'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_input():
    """test for input"""

    for val in ['Buddy', 'Homeslice']:
        for option in ['-n', '--name']:
            rv, out = getstatusoutput(f'{prg} {option} {val}')
            assert rv == 0
            assert out.strip() == f'What up, {val}!'
