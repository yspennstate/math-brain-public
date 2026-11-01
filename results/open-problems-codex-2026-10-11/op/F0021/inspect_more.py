import pathlib,json,xml.etree.ElementTree as ET,fitz
p=pathlib.Path('.')
ns={'a':'http://www.w3.org/2005/Atom'}
for fn in ['arxiv_kpz.xml','arxiv_fixed.xml']:
 print('\nSEARCH',fn)
 for e in ET.parse(fn).getroot().findall('a:entry',ns):
  print(e.findtext('a:id',namespaces=ns),e.findtext('a:published',namespaces=ns),e.findtext('a:title',namespaces=ns))
  s=e.findtext('a:summary',namespaces=ns)
  if any(w in s.lower() for w in ['universality','heavy','fixed']): print(s[:2200])
for fn in ['newchaos','physics']:
 d=fitz.open(fn+'.pdf');p.joinpath(fn+'.txt').write_text('\n'.join(f'\n=== PAGE {i+1} ===\n'+x.get_text() for i,x in enumerate(d)),encoding='utf-8')
 print('\nPAPER',fn,d[0].get_text()[:4500])
print('\nCROSSREF LATER')
for x in json.loads(p.joinpath('crossref_kpz.json').read_text())['message']['items']:
 print(x.get('title'),x.get('DOI'),x.get('published',{}).get('date-parts'))
