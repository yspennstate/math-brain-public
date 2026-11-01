import json,xml.etree.ElementTree as E
r=E.parse('arxiv.xml').getroot(); ns={'a':'http://www.w3.org/2005/Atom'}
for e in r.findall('a:entry',ns):print(e.find('a:id',ns).text,e.find('a:title',ns).text,e.find('a:summary',ns).text)
for e in json.load(open('crossref.json',encoding='utf8'))['message']['items']:print(e.get('title'),e.get('DOI'))
