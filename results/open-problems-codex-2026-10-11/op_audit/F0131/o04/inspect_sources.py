from pathlib import Path
import xml.etree.ElementTree as ET
import json
for name,term in [('pegden','Theorem 4.2'),('random','Theorem 9.2'),('source','Theorem 6.3')]:
    t=Path(name+'.txt').read_text(encoding='utf-8'); p=t.find(term); print('\n'+name+' '+term+'\n'+t[max(0,p-1000):p+5500])
ns={'a':'http://www.w3.org/2005/Atom'}
r=ET.fromstring(Path('arxiv_search.response').read_bytes())
for e in r.findall('a:entry',ns):
    print('SEARCH:',e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns))
    s=e.findtext('a:summary',namespaces=ns)
    if any(x in s.lower() for x in ('hole','polygon','background','limit shape')): print(s)
print('BOX CHECK TOTAL',sum(r['box_checks'] for r in json.loads(Path('independent_checks.json').read_text())['runs']))
