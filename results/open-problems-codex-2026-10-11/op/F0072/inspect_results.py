from pathlib import Path
import json,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parent
for name in ['openalex_source','openalex_sos','openalex_laplace','crossref_sos']:
 p=R/(name+'.json')
 if not p.exists(): continue
 d=json.loads(p.read_text(encoding='utf8'))
 print('\nSERVICE',name)
 for x in d.get('results',d.get('message',{}).get('items',[])):
  print(x.get('id',x.get('DOI','')),x.get('publication_year',''),x.get('title'),x.get('doi',''))
for name in ['arxiv_sos','arxiv_absolute']:
 p=R/(name+'.json')
 if not p.exists(): continue
 print('\nSERVICE',name)
 root=ET.fromstring(p.read_bytes()); ns={'a':'http://www.w3.org/2005/Atom'}
 for e in root.findall('a:entry',ns):
  print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),e.findtext('a:summary',namespaces=ns))
p=R/'source.txt'
if p.exists():
 text=p.read_text(encoding='utf8')
 for term in ['Open Problem 5','(20)','3.2 Entropic','3.2. Entropic']:
  start=text.find(term); print('\nSOURCE',term, '\n',text[max(0,start-1200):start+3500])
