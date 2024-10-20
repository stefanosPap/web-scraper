import sys 
sys.path.append("/home/stefanos/web-scraper")
from .. import dummy  
import pytest  

@pytest.mark.parametrize(
        ('input_n', 'expected'),
        (
            (5, 25),
            (3., 9.),
            (1., 1.),
            (2., 4.),
            (6., 36.)
        )
)



def test_square(input_n, expected):
    assert dummy.square(input_n) == expected 

# @pytest.mark.great
# def test_square(input_value):
#     assert dummy.square(input_value) == 9 

