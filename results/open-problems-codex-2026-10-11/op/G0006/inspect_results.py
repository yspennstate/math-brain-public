from pathlib import Path
import xml.etree.ElementTree as E
ns={'a':'http://www.w3.org/2005/Atom'}
for fn in ['arxiv_since.txt','arxiv_exact.txt','rath_search.txt']:
 print('\nFILE',fn)
 for x in E.parse(fn).findall('a:entry',ns):
  title=' '.join(x.findtext('a:title',namespaces=ns).split())
  if fn!='arxiv_exact.txt' or any(w in title.lower() for w in ['percolation','invariant','stochastic domination']):
   print(x.findtext('a:published',namespaces=ns),x.findtext('a:id',namespaces=ns),title)
   if fn=='arxiv_since.txt': print(' '.join(x.findtext('a:summary',namespaces=ns).split()))
s=Path('source_text.txt').read_text(encoding='utf8')
for term in ['Theorem 2.1(a)','Teorem 2.1(a)','Proposition 4.','Lemma 4.','Proof of Teorem 2.1(a)']:
 start=s.find(term); print('\nEXCERPT',term,start); print(s[max(0,start-100):start+4800] if start>=0 else '')
s=Path('liggett_pdf_text.txt').read_text(encoding='utf8'); print('\nLIGGETT\n',s[:6500]);
