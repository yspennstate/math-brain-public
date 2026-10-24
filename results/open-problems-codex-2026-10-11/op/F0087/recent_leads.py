import pathlib,json,xml.etree.ElementTree as E
P=pathlib.Path('.')
for fn in ['semantic_dubedat_citations.json','semantic_kenyon_citations2.json']:
 J=json.loads((P/fn).read_text());print('FILE',fn,'next',J.get('next'),'count',len(J.get('data',[])))
 for c in J.get('data',[]):
  w=c['citingPaper'];t=w['title']
  if fn.startswith('semantic_dubedat') or any(s in t.lower() for s in ['electric','boson','cauchy','torsion','chaos','free field']):print(w['year'],t,w.get('externalIds'))
N={'a':'http://www.w3.org/2005/Atom'};R=E.parse('arxiv_targeted_alt.json')
for e in R.findall('a:entry',N):
 t=e.findtext('a:title',namespaces=N)
 if any(s in t.lower() for s in ['dimer','cauchy','boson','height']):print(e.findtext('a:id',namespaces=N),t,e.findtext('a:summary',namespaces=N))
for w in json.loads((P/'crossref_pinson.json').read_text())['message']['items']:print(w.get('title'),w.get('DOI'),w.get('volume'),w.get('page'))
