from pathlib import Path
import xml.etree.ElementTree as ET,json
R=Path(__file__).resolve().parent; ns={'a':'http://www.w3.org/2005/Atom'}
for name in ['arxiv_leads','arxiv_continuous']:
 p=R/(name+'.json'); print('\n',name)
 root=ET.fromstring(p.read_bytes())
 for e in root.findall('a:entry',ns):
  title=e.findtext('a:title',namespaces=ns)
  if name=='arxiv_leads' or any(s in title.lower() for s in ['surface','interface','repulsion']):
   print(e.findtext('a:id',namespaces=ns),title)
   print(e.findtext('a:summary',namespaces=ns))
for name in ['middle_pdf','degenerate_pdf']:
 p=R/(name+'.txt'); s=p.read_text(encoding='utf8');print('\n',name, s[:15000])
 for term in ['Velenik','continuous SOS','absolute value','entropic repulsion','Theorem 1.1']:
  starts=[]; k=0
  while True:
   k=s.find(term,k)
   if k<0 or len(starts)>=4: break
   starts.append(k);k+=len(term)
  for k in starts: print('TERM',term,s[max(0,k-400):k+1500])
p=R/'source.txt';s=p.read_text(encoding='utf8')
for page in [5,6,19,20,21,22]:
 start=s.find(f'=== PDF PAGE {page} ===');end=s.find('=== PDF PAGE',start+20)
 print(s[start:end])
