"""Fetch a paper and convert entirely in memory; only plain text reaches disk."""
import argparse, hashlib, io, json, subprocess, urllib.request
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('url'); p.add_argument('out'); a=p.parse_args()
r=urllib.request.urlopen(urllib.request.Request(a.url,headers={'User-Agent':'G0010 literature research contact via arXiv'}),timeout=90)
b=r.read()
if b[:4]==b'%PDF':
    q=subprocess.run(['pdftotext','-layout','-','-'],input=b,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
    s=q.stdout.decode('utf-8')
else:
    s=b.decode('utf-8')
Path(a.out).write_text(s)
print(json.dumps({'url':a.url,'out':a.out,'download_bytes':len(b),'text_chars':len(s),'sha256_download':hashlib.sha256(b).hexdigest(),'pages':s.count('\f')}))
