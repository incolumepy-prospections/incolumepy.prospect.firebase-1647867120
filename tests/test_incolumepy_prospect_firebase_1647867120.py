from incolumepy.prospect.firebase_1647867120 import __version__
import pytest
import re


@pytest.mark.parametrize(
    ['version', 'expected'],
    [
        (__version__, True),
        ('1111.0.0', True),
        ('0.111111.0', True),
        ('0.0.111111111', True),
        ('0.0.111-a.9999', True),
        ('0.0.111.a.9999', False),
        ('0.1.0-dev.0', True),
        ('0.111111.0-alpha.11', True),
        ('0.1.1111110-beta.111', True),
        ('10.1.0-rc.111', True),
        ('10.1.0-a-111', False),
        ('0.1.0-a1', False),
        ('0.1', False),
        ('1', False),
        ('0.1.0_a1', False),
    ],
)
def test_version(version, expected):
    regex = r'\d+(\.\d+){2}(-\w+\.\d+)?'
    assert bool(re.compile(regex).fullmatch(version)) == expected
