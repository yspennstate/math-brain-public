import pathlib,json,xml.etree.ElementTree as E
print(pathlib.Path('hingant_yvinec.txt').read_text(encoding='utf8')[:4800])
ns={'a':'http://www.w3.org/2005/Atom'}
for e in E.parse('arxiv_target.xml').getroot().findall('a:entry',ns):
 print(e.find('a:id',ns).text,e.find('a:title',ns).text.strip()); print(e.find('a:summary',ns).text.strip()[:1200])
for e in json.load(open('crossref_target.json',encoding='utf8'))['message']['items']: print(e.get('title'),e.get('DOI'))
