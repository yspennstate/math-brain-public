#!/usr/bin/env python3
"""Independent pdftotext extraction of decisive pages, without storing PDF bytes."""
import hashlib, subprocess, urllib.request
from pathlib import Path
root=Path(__file__).resolve().parents[1]
items=[
 ('bandeira_eth_key_pages','https://people.math.ethz.ch/~abandeira/TenLecturesFortyTwoProblems.pdf',132,134),
 ('zhong_boumal_key_pages','https://arxiv.org/pdf/1703.06605v1',11,12),
 ('gao_zhang_key_pages','https://andersonyezhang.github.io/PDF/Phase_Minimax.pdf',3,4),
]
for name,url,first,last in items:
    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
    with urllib.request.urlopen(req,timeout=45) as r: blob=r.read(35_000_000)
    if not blob.startswith(b'%PDF'): raise ValueError('not PDF')
    result=subprocess.run(['pdftotext','-f',str(first),'-l',str(last),'-layout','-','-'],input=blob,capture_output=True,check=True,timeout=45)
    header=f'SOURCE URL: {url}\nPDF SHA256: {hashlib.sha256(blob).hexdigest()}\nIndependent extraction: pdftotext -layout, one-based PDF pages {first} through {last}; form feeds separate pages.\n\n'
    (root/'sources'/f'{name}.txt').write_text(header+result.stdout.decode('utf-8'))
    print(f'{name}: {len(result.stdout)} text bytes')
