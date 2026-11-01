import fitz, pathlib,xml.etree.ElementTree as ET,json
p=pathlib.Path('.')
d=fitz.open('source.pdf');p.joinpath('source.txt').write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+x.get_text() for i,x in enumerate(d)),encoding='utf-8')
for i,x in enumerate(d):
 t=x.get_text()
 if 'Question 5' in t or 'Assumption 3' in t: print('PAGE',i+1,t)
root=ET.parse('arxiv.xml').getroot();ns={'a':'http://www.w3.org/2005/Atom'}
for e in root.findall('a:entry',ns):print('ARXIV',e.findtext('a:id',namespaces=ns),e.findtext('a:published',namespaces=ns),e.findtext('a:title',namespaces=ns))
j=json.loads(p.joinpath('crossref.json').read_text())
for x in j['message']['items']:print('CROSSREF',x.get('title'),x.get('DOI'),x.get('published',{}).get('date-parts'))
