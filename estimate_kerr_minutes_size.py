import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://legacy.co.kerr.tx.us/commcrt/minutes/"
START_YEAR = 2008
END_YEAR = datetime.now().year

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

def get_txt_files_and_sizes(year):
    url = f"{BASE_URL}{year}/"
    try:
        resp = requests.get(url, verify=False)
        resp.raise_for_status()
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return []
    soup = BeautifulSoup(resp.text, 'html.parser')
    files = []
    # Find all table rows
    for row in soup.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) >= 4:
            link = cols[1].find('a', href=True)
            if link and link['href'].endswith('.txt'):
                fname = link['href']
                size_str = cols[3].get_text()
                size = parse_size(size_str)
                files.append((fname, size))
    return files

def main():
    total_size = 0
    file_count = 0
    for year in range(START_YEAR, END_YEAR + 1):
        print(f"Checking {year}...")
        files = get_txt_files_and_sizes(year)
        for fname, size in files:
            if size is not None:
                total_size += size
            file_count += 1
    print(f"\nTotal files: {file_count}")
    print(f"Total size: {total_size} bytes")
    print(f"Total size: {total_size / 1024:.2f} KB")
    print(f"Total size: {total_size / (1024*1024):.2f} MB")
    print(f"Total size: {total_size / (1024*1024*1024):.4f} GB")

if __name__ == "__main__":
    main() 