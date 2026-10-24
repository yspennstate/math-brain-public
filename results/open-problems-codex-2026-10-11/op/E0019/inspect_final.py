import xml.etree.ElementTree as E
from pathlib import Path
n={'a':'http://www.w3.org/2005/Atom'}
for f in ['arxiv_targeted.json','general_regular.json']:
 print('FILE',f)
 for e in E.parse(f).findall('a:entry',n):
  title=e.find('a:title',n).text.replace('\n',' ')
  if f.startswith('arxiv_') or any(s in title.lower() for s in ['switch','piecewise','pdmp']):
   print(e.find('a:id',n).text,title, '; '.join(a.find('a:name',n).text for a in e.findall('a:author',n)))
for f in ['fast2022.txt','feller2023.txt']:
 s=Path(f).read_text(encoding='utf8');print('FILE',f,s[:5000]);
 for token in ['Theorem 1.1','Theorem 1.2','Theorem 4.15','Example 4.18']:
  i=s.find(token)
  if i>=0:print(s[max(0,i-300):i+2200])
