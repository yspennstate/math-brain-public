#!/usr/bin/env python3
import json, pathlib, re
root=pathlib.Path(__file__).resolve().parents[1]
lines=['D0046 primary-source text index','Fetched 2026-11-13. PDF bytes were transient memory only; no PDFs retained.','Page numbers below are one-based original PDF pages, delimited by form feeds.','']
for meta in sorted((root/'sources').glob('*.metadata.txt')):
    d=json.loads(meta.read_text());name=meta.name.replace('.metadata.txt','.txt')
    lines += [name,d['url'],f"pages={d['pages']} text_sha256={d['text_sha256']}"]
    pages=(root/'sources'/name).read_text().split('\f')
    for i,p in enumerate(pages,1):
        if len(pages)>200 and i>40:break
        for line in p.splitlines():
            if re.match(r'^\s*(Theorem|THEOREM|Corollary|Question|Problem)\s+(?:[A-Z]|[0-9]+(?:\.[0-9]+)*)[ .(:]',line):
                lines.append(f'  PDF p.{i}: {line.strip()[:155]}')
    lines.append('')
(root/'sources'/'INDEX.txt').write_text('\n'.join(lines)+'\n')
print('Indexed',len(list((root/'sources').glob('*.metadata.txt'))),'source texts')
