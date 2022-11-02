import pytest
from bs4 import BeautifulSoup
import requests


from scraper import get_citations_needed_count



def test_get_citations_needed_count():

    

    actual=get_citations_needed_count('https://en.wikipedia.org/wiki/Michelangelo')
    expect=4
    assert actual==expect

