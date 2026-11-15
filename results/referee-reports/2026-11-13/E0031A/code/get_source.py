#!/usr/bin/env python3
"""Fetch papers into memory and retain page-labelled plain text only."""
import argparse, datetime, hashlib, io, os, urllib.request
if os.getpriority(os.PRIO_PROCESS,0)<10:
 os.setpriority(os.PRIO_PROCESS,0,10)
assert os.getpriority(os.PRIO_PROCESS,0)>=10
from pypdf import PdfReader
p=argparse.ArgumentParser()
p.add_argument('url'); p.add_argument('output'); a=p.parse_args()
r=urllib.request.urlopen(urllib.request.Request(a.url,headers={'User-Agent':'Research source verification contact via arxiv'}),timeout=90)
b=r.read()
if len(b)>40_000_000: raise ValueError('source too large')
pdf=PdfReader(io.BytesIO(b))
with open(a.output,'w') as f:
 f.write(f'SOURCE: {a.url}\nFETCHED UTC: {datetime.datetime.now(datetime.timezone.utc).isoformat()}\nPDF SHA256 (in-memory download; PDF not saved): {hashlib.sha256(b).hexdigest()}\nPAGES: {len(pdf.pages)}\n')
 for i,page in enumerate(pdf.pages,1):
  f.write(f'\n\n===== PDF PAGE {i} =====\n\n'+page.extract_text().replace('\x00','')+'\n')
print(a.output, len(pdf.pages),'pages',len(b),'bytes fetched; PDF discarded')
