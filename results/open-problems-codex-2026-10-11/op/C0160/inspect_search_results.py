from pathlib import Path
import json, xml.etree.ElementTree as ET
for name in ['arxiv','arxiv_https','arxiv_endpoint']:
 p=Path(name+'.txt')
 if p.exists():
  try:
   root=ET.fromstring(p.read_text(encoding='utf-8'))
   ns={'a':'http://www.w3.org/2005/Atom'}
   for e in root.findall('a:entry',ns): print(name,e.findtext('a:title',namespaces=ns),e.findtext('a:id',namespaces=ns),e.findtext('a:published',namespaces=ns),e.findtext('a:summary',namespaces=ns))
  except Exception as e: print(name,e)
p=Path('crossref.txt')
if p.exists():
 try:
  for x in json.loads(p.read_text(encoding='utf-8'))['message']['items']: print('CROSSREF',x.get('title'),x.get('DOI'),x.get('published'),x.get('author'))
 except Exception as e: print(e)
for name in ['source.txt']:
 p=Path(name)
 if p.exists(): print(p.read_text(encoding='utf-8'))
