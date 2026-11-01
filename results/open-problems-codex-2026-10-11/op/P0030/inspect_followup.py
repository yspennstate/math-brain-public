import pathlib,json,xml.etree.ElementTree as E
ns={'a':'http://www.w3.org/2005/Atom'}
for name in ['arxiv_decomp','arxiv_authors']:
 print('\n'+name)
 root=E.fromstring(pathlib.Path('search_'+name+'.txt').read_text())
 for e in root.findall('a:entry',ns):
  print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns)); print(e.findtext('a:summary',namespaces=ns)[:1800])
for name in ['github_decomp','crossref_compat']:
 d=json.loads(pathlib.Path('search_'+name+'.txt').read_text());print('\n'+name)
 if name.startswith('github'):print('count',d['total_count']);print([(x['full_name'],x.get('description')) for x in d['items']])
 else:
  for x in d['message']['items']:print(x.get('title'),x.get('DOI'))
