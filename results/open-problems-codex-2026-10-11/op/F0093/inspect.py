import json,xml.etree.ElementTree as E
from pathlib import Path
r=E.parse('arxiv.response').getroot();ns={'a':'http://www.w3.org/2005/Atom'}
for e in r.findall('a:entry',ns):
 t=e.findtext('a:title',namespaces=ns);s=e.findtext('a:summary',namespaces=ns)
 print(e.findtext('a:id',namespaces=ns),t,s[:2500])
c=json.loads(Path('crossref.response').read_text())
for x in c['message']['items'][:12]:print('CR',x.get('title'),x.get('DOI'),x.get('published'))
t=Path('kalai.txt').read_text(encoding='utf8');i=t.find('Consider n steps');print('SOURCE',t[i-500:i+4500])
