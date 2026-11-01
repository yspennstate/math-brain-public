import pathlib,xml.etree.ElementTree as E,json
ns={'a':'http://www.w3.org/2005/Atom'}
for fn in ['second_broman_arxiv.txt','second_noise_arxiv.txt']:
 p=pathlib.Path(fn)
 if p.exists():
  print(fn)
  for e in E.parse(p).findall('a:entry',ns):print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),e.findtext('a:summary',namespaces=ns))
p=pathlib.Path('second_broman_crossref.txt')
if p.exists():
 for w in json.loads(p.read_text())['message']['items']:print(w.get('title'),w.get('DOI'))
