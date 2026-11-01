from pathlib import Path
import re,json,xml.etree.ElementTree as E
for p in sorted(Path('.').glob('lead_*.txt')):
 s=p.read_text(encoding='utf8'); print('\nLEAD',p.name)
 for term in ['rectangle','Problem 4','empirical optimal transport plan','separated','selected','non-degenerate']:
  hits=list(re.finditer(re.escape(term),s,re.I));print(term,len(hits))
  for m in hits[:2]: print(s[max(0,m.start()-180):m.start()+500].replace('\n',' '))
x=E.fromstring(Path('arxiv_specific.txt').read_text());n={'a':'http://www.w3.org/2005/Atom'}
for e in x.findall('a:entry',n):print('SPECIFIC',e.findtext('a:published',namespaces=n),e.findtext('a:title',namespaces=n).replace('\n',' '),e.findtext('a:id',namespaces=n))
