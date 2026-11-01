import json,xml.etree.ElementTree as E
r=E.parse('arxiv.txt'); ns={'a':'http://www.w3.org/2005/Atom'}
for e in r.findall('a:entry',ns): print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),e.findtext('a:published',namespaces=ns),e.findtext('a:summary',namespaces=ns))
j=json.load(open('crossref.txt',encoding='utf8'))
for e in j['message']['items']: print(e.get('title'),e.get('DOI'),e.get('published'))
