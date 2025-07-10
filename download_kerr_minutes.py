import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://legacy.co.kerr.tx.us/commcrt/minutes/"
START_YEAR = 2025
END_YEAR = datetime.now().year
DOWNLOAD_DIR = "minutes"

def parse_size(size_str):
    match = re.match(r"(\d+[\.,]?\d*)\s*([KMG]?)", size_str.strip(), re.I)
    if not match:
        return None
    num = float(match.group(1).replace(',', ''))
    unit = match.group(2).upper()
    if unit == 'K':
        return int(num * 1024)
    elif unit == 'M':
        return int(num * 1024 * 1024)
    elif unit == 'G':
        return int(num * 1024 * 1024 * 1024)
    else:
        return int(num)

def get_txt_files(year):
    url = f"{BASE_URL}{year}/"
    try:
        resp = requests.get(url, verify=False)
        resp.raise_for_status()
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return []
    soup = BeautifulSoup(resp.text, 'html.parser')
    files = []
    for row in soup.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) >= 4:
            link = cols[1].find('a', href=True)
            if link and link['href'].lower().endswith(('.txt', '.pdf')):
                fname = link['href']
                files.append(fname)
    return files

def download_file(year, fname):
    url = f"{BASE_URL}{year}/{fname}"
    year_dir = os.path.join(DOWNLOAD_DIR, str(year))
    os.makedirs(year_dir, exist_ok=True)
    local_path = os.path.join(year_dir, fname)
    if os.path.exists(local_path):
        print(f"Already exists: {local_path}")
        return
    try:
        resp = requests.get(url, verify=False)
        resp.raise_for_status()
        with open(local_path, 'wb') as f:
            f.write(resp.content)
        print(f"Downloaded: {local_path}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def main():
    for year in range(START_YEAR, END_YEAR + 1):
        print(f"Processing {year}...")
        files = get_txt_files(year)
        for fname in files:
            download_file(year, fname)

if __name__ == "__main__":
    main() 