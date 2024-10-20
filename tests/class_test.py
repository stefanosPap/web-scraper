import sys 
sys.path.append("/home/stefanos/web-scraper")
import pytest 
from dummy import C 


@pytest.mark.great
def test_f(input_value):
    c = C()
    assert c.f(input_value) == 6

@pytest.mark.great
def test_g(input_value):
    c = C()
    assert c.g(input_value) == 9 