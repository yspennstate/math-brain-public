from pathlib import Path
import fitz,json,xml.etree.ElementTree as ET
p=Path('.')
for name in ['source','improved','lindeberg']:
 if p.joinpath(name+'.pdf').exists():
  d=fitz.open(name+'.pdf');p.joinpath(name+'.txt').write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+x.get_text() for i,x in enumerate(d)),encoding='utf-8')
  print('PAPER',name,'PAGES',len(d),d[0].get_text()[:4500])
  if name!='source':
   for i in range(min(5,len(d))):
    t=d[i].get_text()
    if 'Theorem 1.' in t:print('THEOREM PAGE',i+1,t[:10000])
ns={'a':'http://www.w3.org/2005/Atom'}
for fn in ['arxiv.xml','arxiv_kpz.xml']:
 for e in ET.parse(fn).getroot().findall('a:entry',ns):
  if any(z in e.findtext('a:title',namespaces=ns).lower() for z in ['universality bounds','high temperature','heavy-tail','heavy tail','entropy-controlled']):
   print('REFERENCE',e.findtext('a:title',namespaces=ns),[x.findtext('a:name',namespaces=ns) for x in e.findall('a:author',ns)],e.findtext('a:id',namespaces=ns))
if p.joinpath('crossref_source.json').exists():
 for x in json.loads(p.joinpath('crossref_source.json').read_text())['message']['items']:print('SOURCE CROSSREF',x.get('title'),x.get('DOI'))
