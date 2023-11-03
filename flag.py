import time
from pathlib import Path
from typing import Callable

import httpx

POP = ('CN IN RU FR').split()
base_url = 'https://www.fluentpython.com/data/flags'
dest = Path('downloaded')

def save_flag(img,filename):
    (dest / filename).write_bytes(img)

def get_flag(cc):
    url = f'{base_url}/{cc}/{cc}.gif'.lower()
    resp = httpx.get(url,timeout=6.1,follow_redirects=True)
    resp.raise_for_status()
    return resp.content

def download_many(cc_list):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        save_flag(image,f'{cc}.gif')
        print(f'{cc} done')
    return len(cc_list)

def main(downloader):
    dest.mkdir(exist_ok=True)
    print(dest.cwd())
    t0= time.perf_counter()
    count = downloader(POP)
    elapsed = time.perf_counter()
    print(f'time {elapsed-t0}')

if __name__ == '__main__':
    main(download_many)