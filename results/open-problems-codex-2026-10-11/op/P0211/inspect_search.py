import json,xml.etree.ElementTree as E,pathlib
r=E.parse('arxiv.xml').getroot(); ns={'a':'http://www.w3.org/2005/Atom'}
for e in r.findall('a:entry',ns): print(e.find('a:id',ns).text,e.find('a:title',ns).text.strip(),e.find('a:summary',ns).text.strip()[:1800])
r=json.load(open('crossref.json',encoding='utf8'))
for e in r['message']['items']: print(e.get('title'),e.get('DOI'),e.get('published',{}).get('date-parts'))
print('GITHUB')
for e in json.load(open('github.json',encoding='utf8'))['items']: print(e['full_name'],e['description'])
