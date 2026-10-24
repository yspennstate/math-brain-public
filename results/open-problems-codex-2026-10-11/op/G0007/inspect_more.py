import json,pathlib,xml.etree.ElementTree as ET
for n in ['openalex_doi','openalex_retry','semantic_search','github_retry']:
 p=pathlib.Path(n+'.txt')
 if p.exists():print(n,p.read_text()[:1500])
p=pathlib.Path('arxiv_exact.txt')
if p.exists():
 try:
  ns={'a':'http://www.w3.org/2005/Atom'}
  for e in ET.fromstring(p.read_bytes()).findall('a:entry',ns): print(e.findtext('a:id',namespaces=ns),e.findtext('a:published',namespaces=ns),e.findtext('a:title',namespaces=ns))
 except Exception as e:print(e)
p=pathlib.Path('crossref_since.txt')
if p.exists():
 try:
  for w in json.loads(p.read_bytes())['message']['items']:print(w.get('title'),w.get('DOI'),w.get('published'))
 except Exception as e: print(e)
