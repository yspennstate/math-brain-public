#!/usr/bin/env python3
"""Fetch sources, converting PDF bytes through pipes; retain only plain text."""
import os
if os.getpriority(os.PRIO_PROCESS,0)<10:
    os.nice(10-os.getpriority(os.PRIO_PROCESS,0))
from pathlib import Path
import requests, subprocess, hashlib, datetime
ROOT=Path(__file__).resolve().parents[1]
def fetch(name,url):
    response=requests.get(url,timeout=75)
    response.raise_for_status()
    raw=response.content
    if raw.startswith(b'%PDF'):
        out=subprocess.run(['pdftotext','-layout','-','-'],input=raw,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True).stdout.decode('utf-8')
    else:
        out=response.text
    if '\x00' in out: raise ValueError('not plain text')
    (ROOT/'sources'/f'{name}.txt').write_text(out)
    with (ROOT/'sources'/'FETCH_LEDGER.txt').open('a') as f:
        f.write(f'{datetime.datetime.now().isoformat()} {name}\nURL: {url}\nHTTP: {response.status_code}; bytes fetched: {len(raw)}; text SHA256: {hashlib.sha256(out.encode()).hexdigest()}\n\n')
    print(name,len(out))
if __name__=='__main__':
    import sys
    fetch(sys.argv[1],sys.argv[2])
