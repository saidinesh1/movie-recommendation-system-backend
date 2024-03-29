import requests
from bs4 import BeautifulSoup
import json
import re

def GetYtVideo(name):
    r = requests.get('https://www.youtube.com/results?search_query={0}+official+trailer'.format(name))
    soup = BeautifulSoup(r.content, 'html.parser')
    script_tags = soup.find_all('script')
    ytInitialData_json = None
    for script_tag in script_tags:
        if 'ytInitialData' in script_tag.text:
            match = re.search(r'ytInitialData\s*=\s*({.*?});', script_tag.text)
            if match:
                ytInitialData_json = json.loads(match.group(1))
                break

    with open('lover.txt', 'w', encoding='utf-8') as file:
        json.dump(ytInitialData_json.get('contents'),file, indent=4)
    if ytInitialData_json:
        return ytInitialData_json.get('contents')
    else:
        return "No data"
