from pathlib import Path
import xml.etree.ElementTree as E
N={'a':'http://www.w3.org/2005/Atom'}
for e in E.parse('arxiv_electric.json').findall('a:entry',N):
 if '2301.09665' in e.findtext('a:id',namespaces=N):print([a.findtext('a:name',namespaces=N) for a in e.findall('a:author',N)])
l=Path('jsw.txt').read_text(encoding='utf8').splitlines()
for i,t in enumerate(l):
 if 'Proposition 3.6' in t or 'Lemma 3.4' in t or 'Proposition 3.5' in t:
  print('\n'.join(l[max(0,i-2):i+20]))
