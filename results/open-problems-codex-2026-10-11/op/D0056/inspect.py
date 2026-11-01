import xml.etree.ElementTree as ET,json
ns={'a':'http://www.w3.org/2005/Atom'}
r=ET.parse('arxiv.xml')
for e in r.findall('a:entry',ns):
 print(e.find('a:id',ns).text, e.find('a:title',ns).text.strip());print(e.find('a:summary',ns).text.strip())
d=json.load(open('crossref.json',encoding='utf8'))
for x in d['message']['items']:
 t=' '.join(x.get('title',[]))
 if any(w in t.lower() for w in ['retaux','rétaux','recursive','depinning']): print('CROSSREF',t,x.get('DOI'),x.get('published',{}))
