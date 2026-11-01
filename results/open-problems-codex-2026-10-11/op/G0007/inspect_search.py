import json,xml.etree.ElementTree as ET
ns={'a':'http://www.w3.org/2005/Atom'}
t=ET.parse('arxiv.txt')
for e in t.findall('a:entry',ns):print(e.findtext('a:id',namespaces=ns),e.findtext('a:published',namespaces=ns),e.findtext('a:title',namespaces=ns))
x=json.load(open('crossref.txt',encoding='utf8'))
for w in x['message']['items']:print(w.get('title'),w.get('DOI'),w.get('published'))
