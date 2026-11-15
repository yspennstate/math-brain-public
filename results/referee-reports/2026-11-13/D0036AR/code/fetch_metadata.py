#!/usr/bin/env python3
"""Retain publisher/catalog HTML as readable plain text, never binary files."""
from pathlib import Path
from html.parser import HTMLParser
import requests,os
if os.getpriority(os.PRIO_PROCESS,0)<10:os.nice(10-os.getpriority(os.PRIO_PROCESS,0))
ROOT=Path(__file__).resolve().parents[1]
class Plain(HTMLParser):
    def __init__(self):super().__init__();self.skip=0;self.out=[]
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'):self.skip+=1
        if tag in ('p','h1','h2','h3','div','li','br','tr'):self.out.append('\n')
    def handle_endtag(self,tag):
        if tag in ('script','style'):self.skip=max(0,self.skip-1)
    def handle_data(self,data):
        if not self.skip:self.out.append(data)
items=[
('bradley_books_publisher','https://kendrick.press/Richard-Bradley-Introduction-to-Strong-Mixing-Conditions.htm'),
('peller_book_publisher','https://link.springer.com/book/10.1007/978-0-387-21681-2'),
('ibragimov_rozanov_publisher','https://link.springer.com/book/10.1007/978-1-4612-6275-6'),
('miller_1994_abstract','https://link.springer.com/article/10.1007/BF02214377'),
('bradley_1992_abstract','https://link.springer.com/article/10.1007/BF01046741'),
('bradley_2002_access','https://projecteuclid.org/journals/bernoulli/volume-8/issue-2/On-positive-spectral-density-functions/bj/1078866866.full'),
('helson_sarason_publisher','https://journals.msp.org/mscand/article/view/2485'),
]
for name,url in items:
    try:
        r=requests.get(url,timeout=25)
        parser=Plain();parser.feed(r.text)
        lines=[' '.join(x.split()) for x in ''.join(parser.out).splitlines()]
        text='\n'.join(x for x in lines if x)
        (ROOT/'sources'/f'{name}.txt').write_text(f'URL: {url}\nHTTP: {r.status_code}\n\n{text}\n')
        print(name,r.status_code,len(text),flush=True)
    except Exception as exc:
        with (ROOT/'sources'/'FETCH_LEDGER.txt').open('a') as f:f.write(f'FAILED {name} {url} {type(exc).__name__}: {exc}\n')
        print(name,type(exc).__name__,flush=True)
