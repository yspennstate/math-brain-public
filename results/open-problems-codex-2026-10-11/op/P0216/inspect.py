from pathlib import Path
import json,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parent
for file in ['crossref.raw','crossref_specific.raw']:
 d=json.loads((R/file).read_bytes())
 for x in d['message']['items']:
  if any(t in ' '.join(x.get('title',[])).lower() for t in ['models of random partial','box-spaces','concentration','largest planar','common subtree']):
   print(json.dumps({k:x.get(k) for k in ['title','author','DOI','published','container-title']},ensure_ascii=False))
for file in ['arxiv.raw','arxiv_specific.raw']:
 root=ET.fromstring((R/file).read_bytes());ns={'a':'http://www.w3.org/2005/Atom'}
 for e in root.findall('a:entry',ns):
  if 'poset metric' in e.findtext('a:title',default='',namespaces=ns):
   print(e.findtext('a:title',namespaces=ns),[a.findtext('a:name',namespaces=ns) for a in e.findall('a:author',ns)],e.findtext('a:summary',namespaces=ns))
print('CHECKS', (R/'checks.json').read_text() if (R/'checks.json').exists() else 'pending')
