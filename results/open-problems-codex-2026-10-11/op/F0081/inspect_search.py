import json,xml.etree.ElementTree as E
root=E.parse('arxiv.xml'); ns={'a':'http://www.w3.org/2005/Atom'}
for e in root.findall('a:entry',ns):
 print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns)); print(e.findtext('a:summary',namespaces=ns))
print('\nCROSSREF')
for x in json.load(open('crossref.json'))['message']['items']: print(x.get('title'),x.get('DOI'))
