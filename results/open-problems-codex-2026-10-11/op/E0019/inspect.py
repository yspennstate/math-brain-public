import json,xml.etree.ElementTree as E
from pathlib import Path
p=Path('.')
s=p.joinpath('source.txt').read_text(encoding='utf8')
a=s.index('--- PDF PAGE 9 ---'); b=s.index('--- PDF PAGE 14 ---');print(s[a:b])
n={'a':'http://www.w3.org/2005/Atom'}
r=E.parse('arxiv.json')
for e in r.findall('a:entry',n):print(e.find('a:id',n).text,e.find('a:title',n).text,e.find('a:summary',n).text)
r=json.load(open('crossref.json',encoding='utf8'))
for x in r['message']['items']:print(x.get('title'),x.get('DOI'),x.get('published'),x.get('author'))
