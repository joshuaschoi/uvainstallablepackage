import sys
sys.path.append('.')
import shared as sh
import pytest

def test_clean_string():
    test_str = " This! is      a ,test string  "

    assert "This is a test string" == sh.clean_string(test_str), "String <{}> not cleaned as expected".format(test_str)

## https://docs.pytest.org/en/7.1.x/how-to/skipping.html

# Working Function
space_compressor_data = [
    ('word  word  word', 'word word word')
]

@pytest.mark.parametrize("input, expected", space_compressor_data)

def test_space_compressor(input, expected):
    assert sh.space_compress(input) == expected

# Failing Function
space_compressor_data_with_failure = [
    pytest.param('word  word  word  ', 'wordwordword', marks=pytest.mark.xfail)
]

@pytest.mark.parametrize("input, expected", space_compressor_data_with_failure)

def test_space_compressor_failure(input, expected):
    assert sh.space_compress(input) == expected

# Skipping Function
@pytest.mark.skip(reason="According to the instruction, this function is skipped.")
def test_skip():
    assert 1 == 12

@pytest.mark.skipif(sys.platform == 'darwin', reason = "Test only for darwins")
def test_os():
    print("My Plaform is ", sys.platform)
    assert 1 == 12
