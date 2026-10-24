import pathlib,json,xml.etree.ElementTree as ET
r=ET.fromstring(pathlib.Path('arxiv.response').read_bytes());ns={'a':'http://www.w3.org/2005/Atom'}
for e in r.findall('a:entry',ns):
 title=' '.join(e.findtext('a:title','',ns).split());summary=' '.join(e.findtext('a:summary','',ns).split())
 print(e.findtext('a:id','',ns),title,summary[:400])
c=json.loads(pathlib.Path('crossref.response').read_bytes())
for x in c['message']['items'][:20]:print('CROSSREF',x.get('title'),x.get('DOI'))
