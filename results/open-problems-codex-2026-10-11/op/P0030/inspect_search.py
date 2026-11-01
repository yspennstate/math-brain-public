import pathlib,json,xml.etree.ElementTree as E
for name in ['arxiv_http','openalex_title','openalex_compat','crossref','semantic','github']:
 print('\nSERVICE',name)
 t=pathlib.Path('search_'+name+'.txt').read_text(encoding='utf8')
 if name=='arxiv_http':
  root=E.fromstring(t); ns={'a':'http://www.w3.org/2005/Atom'}
  for e in root.findall('a:entry',ns):print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),e.findtext('a:summary',namespaces=ns))
 elif name=='crossref':
  for x in json.loads(t)['message']['items']: print(x.get('title'),x.get('DOI'),x.get('published'),x.get('author'))
 else: print(t[:3000])
