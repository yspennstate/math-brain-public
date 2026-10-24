import pathlib,xml.etree.ElementTree as E
r=E.fromstring(pathlib.Path('arxiv.response').read_bytes());ns={'a':'http://www.w3.org/2005/Atom'}
for e in r.findall('a:entry',ns): print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),e.findtext('a:summary',namespaces=ns))
