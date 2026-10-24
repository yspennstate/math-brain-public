import json,xml.etree.ElementTree as E
ns={'a':'http://www.w3.org/2005/Atom'}
r=E.parse('arxiv_target.response').getroot()
for e in r.findall('a:entry',ns):
 t=' '.join(e.findtext('a:title',namespaces=ns).split()); a=' '.join(e.findtext('a:summary',namespaces=ns).split())
 if any(w in (t+' '+a).lower() for w in ['revealment','decision tree','noise sensitiv','randomized algorithm','randomised algorithm','query complexity']):
  print(e.findtext('a:id',namespaces=ns),t); print(a[:1300])
d=json.load(open('semantic_source.response',encoding='utf8'));print('CITATIONS',d.get('citationCount'))
for c in d.get('citations',[]):
 if any(w in c['title'].lower() for w in ['algorithm','complex','decision','noise','spectral','percolation']):print(c)
print('SOURCE CROSSREF')
for x in json.load(open('crossref_source.response',encoding='utf8'))['message']['items']:print(x.get('title'),x['DOI'])
