import json,xml.etree.ElementTree as E,pathlib
P=pathlib.Path(__file__).parent
r=E.parse(P/'arxiv_electric.json');ns={'a':'http://www.w3.org/2005/Atom'}
for e in r.findall('a:entry',ns):print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),'\n',e.findtext('a:summary',namespaces=ns))
j=json.loads((P/'crossref.json').read_text());print('\nCROSSREF')
for w in j['message']['items']:print(w.get('title'),w.get('DOI'),w.get('published'))
