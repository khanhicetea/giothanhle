import requests
import json
from bs4 import BeautifulSoup
import urllib.parse as urlparse


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""

def get_location_map(element):
    if element:
        url = element['href'] if element else None
        parsed_url = urlparse.urlparse(url)
        ll = urlparse.parse_qs(parsed_url.query)['ll'][0].split(',')
        return dict(lat=ll[0], long=ll[1])
    return dict(lat=0, long=0)

def get_mass_times(element):
    items = [i.text for i in element.find_all('div')]
    return [i.replace('.', ':').strip() for i in items]


def hcm_crawler():
    page_url = 'http://tgpsaigon.net/giole-timgx?page={}'
    data = []
    for page in range(0, 1):
        url = page_url.format(page)
        res = requests.get(url)
        body = find_between(res.text, '<tbody>', '</tbody>')
        soup = BeautifulSoup(body, "html.parser")
        for row in soup.find_all('tr'):
            cols = row.find_all('td')
            church = dict(masses=dict())
            church['name'] = cols[0].find('a').text
            church['address'] = cols[1].find(text=True, recursive=False).strip()
            church['district'] = cols[2].find(text=True, recursive=False).strip()
            church['location'] = get_location_map(cols[10].find('a'))
            church['address'] = cols[1].find(text=True, recursive=False).strip()
            for w in range(0, 7):
                church['masses'][w] = get_mass_times(cols[w + 3])
            data.append(church)
    return data

if __name__ == '__main__':
    crawl_data = hcm_crawler()
    print(json.dumps(crawl_data))
