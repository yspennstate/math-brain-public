import pathlib, json, xml.etree.ElementTree as E
r=pathlib.Path('.')
print((r/'source_text.txt').read_text(encoding='utf8')[:2000])
x=E.fromstring((r/'arxiv.txt').read_text(encoding='utf8')); ns={'a':'http://www.w3.org/2005/Atom'}
for e in x.findall('a:entry',ns): print('ARXIV',e.findtext('a:title',namespaces=ns),e.findtext('a:id',namespaces=ns),e.findtext('a:published',namespaces=ns))
z=json.loads((r/'crossref.txt').read_text())
for v in z['message']['items']: print('CROSSREF',v.get('title'),v.get('DOI'),v.get('published'))
