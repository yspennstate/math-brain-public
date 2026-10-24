import json,pathlib,xml.etree.ElementTree as E
j=json.loads(pathlib.Path('semantic_retry.txt').read_text());print(j['title']);
for x in j.get('citations',[]):print(x)
r=E.parse('arxiv_exhaust.txt').getroot(); ns={'a':'http://www.w3.org/2005/Atom'}
for x in r.findall('a:entry',ns):print(x.find('a:id',ns).text,x.find('a:title',ns).text)
