#!/usr/bin/env python3
"""Save arXiv listing text, retaining no HTML/PDF file."""
import argparse
import datetime
import html.parser
import urllib.request
from pathlib import Path
class Extract(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.skip=0
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style'): self.skip+=1
        if tag in ('p','div','h1','h2','h3','dt','dd','li','br','tr'): self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script','style'): self.skip-=1
    def handle_data(self, data):
        if not self.skip: self.parts.append(data)
p=argparse.ArgumentParser();p.add_argument('id');a=p.parse_args()
url='https://arxiv.org/abs/'+a.id
with urllib.request.urlopen(url,timeout=45) as f: raw=f.read().decode()
e=Extract();e.feed(raw)
lines=[' '.join(line.split()) for line in ''.join(e.parts).splitlines()]
Path('sources/'+a.id+'-listing.txt').write_text('URL: '+url+'\nRetrieved UTC: '+datetime.datetime.now(datetime.timezone.utc).isoformat()+'\n\n'+'\n'.join(x for x in lines if x)+'\n')
print(a.id, 'listing saved')
