import json,xml.etree.ElementTree as E
r=E.parse('arxiv.xml').getroot();ns={'a':'http://www.w3.org/2005/Atom'}
for e in r.findall('a:entry',ns):
 print(e.findtext('a:id',namespaces=ns),e.findtext('a:published',namespaces=ns),e.findtext('a:title',namespaces=ns).replace('\n',' '))
 print(e.findtext('a:summary',namespaces=ns).replace('\n',' ')[:1000])
j=json.load(open('crossref.json',encoding='utf8'))
print('\nCROSSREF')
for e in j['message']['items']: print(e.get('title'),e.get('DOI'),e.get('published',{}))
print('\nGITHUB')
for e in json.load(open('github.json'))['items']:print(e['full_name'],e['description'])
