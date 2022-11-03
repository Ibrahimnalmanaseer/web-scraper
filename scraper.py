from bs4 import BeautifulSoup
import requests


def get_citations_needed_count(url):

    '''
    params: website url 
    return: the amount of the needed citation in the web page.
    '''

    response=requests.get(url)

    web_page=response.text

    soup=BeautifulSoup(web_page,'html.parser')

    citation_count=len(soup.find_all(title='Wikipedia:Citation needed'))
    print (f'({citation_count}) Citation needed')


def get_citations_needed_report(url):

    '''
    params: website url 
    return: all paragraphs of the article the needed to citation
    '''

    response=requests.get(url)

    web_page=response.text

    soup=BeautifulSoup(web_page,'html.parser')

    for i in soup.findAll(name='p'):

        if i.find(title='Wikipedia:Citation needed'):
            with open('needed_citation.txt','a') as f:
                f.write(i.text +'\n')


get_citations_needed_count('https://en.wikipedia.org/wiki/Michelangelo')

get_citations_needed_report('https://en.wikipedia.org/wiki/Michelangelo')