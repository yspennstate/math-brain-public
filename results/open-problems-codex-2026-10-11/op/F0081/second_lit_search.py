import urllib.request,json
from pathlib import Path
u='https://export.arxiv.org/api/query?search_query=all:%22stable%20matching%22%20AND%20all:Poisson%20AND%20(all:variance%20OR%20all:Poincare%20OR%20all:exponent)&max_results=50'
a={'date':'2026-10-11','service':'arxiv_second_attempt','url':u}
try:
 with urllib.request.urlopen(u,timeout=35) as r:b=r.read()
 Path('second_arxiv.xml').write_bytes(b);a.update(file='second_arxiv.xml',bytes=len(b))
 import xml.etree.ElementTree as E
 ns={'a':'http://www.w3.org/2005/Atom'}
 entries=E.fromstring(b).findall('a:entry',ns)
 for e in entries:print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns))
 a['entries']=len(entries)
except Exception as e:a['error']=repr(e)
p=Path('search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+[a],indent=2));print(a)
