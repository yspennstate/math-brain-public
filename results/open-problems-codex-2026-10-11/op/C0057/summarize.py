import pathlib,json,xml.etree.ElementTree as E
root=E.parse('arxiv.txt').getroot();ns={'a':'http://www.w3.org/2005/Atom'}
for x in root.findall('a:entry',ns):print(x.find('a:id',ns).text, x.find('a:title',ns).text.replace('\n',' '), x.find('a:published',ns).text);print(x.find('a:summary',ns).text[:900])
d=json.loads(pathlib.Path('crossref.txt').read_text())
for x in d['message']['items']: print(x.get('title'),x.get('DOI'),x.get('published'))
