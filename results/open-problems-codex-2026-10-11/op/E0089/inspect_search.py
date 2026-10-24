from pathlib import Path
import json,xml.etree.ElementTree as E
p=Path('arxiv_regular.data')
if p.exists():
 ns={'a':'http://www.w3.org/2005/Atom'}
 for e in E.fromstring(p.read_bytes()).findall('a:entry',ns):print(e.find('a:id',ns).text,e.find('a:title',ns).text)
p=Path('oa_retry.data')
if p.exists():
 d=json.loads(p.read_text());print('OA',[(w['id'],w['title']) for w in d.get('results',[])])
p=Path('crossref_regular.data')
if p.exists():
 d=json.loads(p.read_text());print('CR',[(w.get('title'),w.get('DOI')) for w in d['message']['items']])
