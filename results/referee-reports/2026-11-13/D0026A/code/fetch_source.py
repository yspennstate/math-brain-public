#!/usr/bin/env python3
"""Fetch documents into RAM; retain only extracted plain text, never PDFs."""
import argparse, hashlib, io, json, urllib.request, datetime
from pathlib import Path
from pypdf import PdfReader
p=argparse.ArgumentParser(); p.add_argument('url'); p.add_argument('name'); a=p.parse_args()
r=urllib.request.urlopen(urllib.request.Request(a.url,headers={'User-Agent':'D0026 literature research'}),timeout=90)
b=r.read()
if b.startswith(b'%PDF'):
    pages=PdfReader(io.BytesIO(b)).pages
    txt='\n'.join(f'\n===== PDF PAGE {i+1} =====\n'+page.extract_text(extraction_mode='layout') for i,page in enumerate(pages))
else:
    txt=b.decode('utf-8')
    if '<html' in txt[:2000].lower() or '<!doctype html' in txt[:2000].lower():
        from html.parser import HTMLParser
        class Extract(HTMLParser):
            def __init__(self): super().__init__(); self.parts=[]; self.skip=0
            def handle_starttag(self,tag,attrs):
                if tag in ('script','style'): self.skip+=1
                if tag in ('p','div','section','h1','h2','h3','h4','li'): self.parts.append('\n')
            def handle_endtag(self,tag):
                if tag in ('script','style'): self.skip=max(0,self.skip-1)
            def handle_data(self,data):
                if not self.skip: self.parts.append(data)
        e=Extract(); e.feed(txt); txt=''.join(e.parts)
    txt=txt.replace('\x00','')
Path('sources',a.name+'.txt').write_text(txt.replace('\x00',''))
rec={'url':a.url,'name':a.name,'download_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sha256_download':hashlib.sha256(b).hexdigest(),'bytes':len(b),'retained':'plain text only'}
with open('sources/manifest.jsonl','a') as f: f.write(json.dumps(rec)+'\n')
print(json.dumps(rec))
