import json,xml.etree.ElementTree as E
x=json.load(open('semantic_citations.json'));print('CITATIONS',len(x.get('data',[])),'NEXT',x.get('next'))
for a in x.get('data',[]):
 p=a['citingPaper']; print(p['year'],p['title'])
print('ARXIV BROAD')
ns={'a':'http://www.w3.org/2005/Atom'}
for e in E.parse('arxiv_tail.xml').findall('a:entry',ns):
 title=e.findtext('a:title',namespaces=ns); summary=e.findtext('a:summary',namespaces=ns)
 if any(w in title.lower() for w in ['matching','stable','allocation']):print(e.findtext('a:id',namespaces=ns),title)
print('CROSSREF SOURCE')
for a in json.load(open('crossref_source.json'))['message']['items']:print(a.get('title'),a.get('DOI'),a.get('published'),a.get('author'))
