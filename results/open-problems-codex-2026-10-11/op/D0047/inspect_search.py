import pathlib,xml.etree.ElementTree as E,json
p=pathlib.Path('.')
for fn in ['arxiv_gap.json']:
 root=E.fromstring((p/fn).read_bytes()); ns={'a':'http://www.w3.org/2005/Atom'}
 for e in root.findall('a:entry',ns):
  print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),e.findtext('a:published',namespaces=ns)); print(e.findtext('a:summary',namespaces=ns))
