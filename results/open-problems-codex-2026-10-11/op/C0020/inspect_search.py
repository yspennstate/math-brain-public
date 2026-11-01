import json, xml.etree.ElementTree as ET
from pathlib import Path
p=Path('.')
r=ET.parse('arxiv.response').getroot(); ns={'a':'http://www.w3.org/2005/Atom'}
for e in r.findall('a:entry',ns):
 print(e.findtext('a:id',namespaces=ns),e.findtext('a:published',namespaces=ns), ' '.join(e.findtext('a:title',namespaces=ns).split()))
 print(' '.join(e.findtext('a:summary',namespaces=ns).split())[:450])
d=json.load(open('crossref.response',encoding='utf8'))
print('\nCROSSREF')
for x in d['message']['items']:print(x.get('title'),x.get('DOI'),x.get('published',{}))
print('\nGITHUB',json.load(open('github.response',encoding='utf8'))['total_count'])
