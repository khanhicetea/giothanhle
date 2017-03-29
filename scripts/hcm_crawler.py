import requests
import json
from bs4 import BeautifulSoup
import urllib.parse as urlparse
from areas import vn_areas
from helpers import noAccentVietnamese
from fuzzywuzzy import process


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


def district_detect(district):
    nomalized = noAccentVietnamese(district)
    hcm_districts = [item for key, item in vn_areas.items() if int(item['parent_id']) == 30]
    hcm_slugs = [item['slug'] for item in hcm_districts]
    fuzzy = process.extractOne(nomalized, hcm_slugs)
    slug = fuzzy[0]
    for d in hcm_districts:
        if slug == d['slug']:
            return d['id']
    return 30


def hcm_crawler():
    page_url = 'http://tgpsaigon.net/giole-timgx?page={}'
    data = []
    for page in range(0, 10):
        url = page_url.format(page)
        res = requests.get(url)
        body = find_between(res.text, '<tbody>', '</tbody>')
        soup = BeautifulSoup(body, "html.parser")
        for row in soup.find_all('tr'):
            cols = row.find_all('td')
            church = dict(masses=dict())
            church['name'] = cols[0].find('a').text
            church['address'] = cols[1].find(text=True, recursive=False).strip()
            church['district_text'] = cols[2].find(text=True, recursive=False).strip()
            church['district_id'] = district_detect(church['district_text'])
            church['location'] = get_location_map(cols[10].find('a'))
            church['address'] = cols[1].find(text=True, recursive=False).strip()
            for w in range(0, 7):
                church['masses'][w] = get_mass_times(cols[w + 3])
            data.append(church)
    return data

if __name__ == '__main__':
    crawl_data = hcm_crawler()
    fixture_data = []
    cpk = 0
    mtpk = 0
    for church in crawl_data:
        cpk += 1
        row = {
            "model": "backend.church",
            "pk": int(cpk),
            "fields": {
                "name": church['name'],
                "address": church['address'],
                "area": church['district_id'],
                "location": '{},{}'.format(church['location']['lat'], church['location']['long']),
                "website": ""
            }
        }
        fixture_data.append(row)
        for dow, masses in church['masses'].items():
            for mass in masses:
                if len(mass) == 4 or len(mass) == 5:
                    mtpk += 1
                    mt_row = {
                        "model": "backend.masstime",
                        "pk": int(mtpk),
                        "fields": {
                            "church": cpk,
                            "day_of_week": int(dow) + 2,
                            "time": '{}:00'.format(mass),
                        }
                    }
                    fixture_data.append(mt_row)

    print(json.dumps(fixture_data, indent=4))
