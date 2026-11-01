import pathlib,json
s=pathlib.Path('source.txt').read_text(encoding='utf8')
for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18]:
 p=s.split('=== PDF PAGE ')[i];
 if i in [1,2,15,18] or any(w in p for w in ['compound Poisson','Kanda','Question 4']): print(p[:16000])
for fn in ['openalex_source.raw','openalex_search.raw','semantic_citations.raw','crossref.raw']:
 d=json.loads(pathlib.Path(fn).read_text(encoding='utf8')); print('\nFILE',fn)
 rows=d.get('results',d.get('data',d.get('message',{}).get('items',[])))
 for r in rows:
  r=r.get('citingPaper',r);title=r.get('title');
  if fn!='crossref.raw' or 'hunt' in str(title).lower():print(r.get('id'),title,r.get('publication_year',r.get('year',r.get('published'))),r.get('doi',r.get('DOI',r.get('externalIds'))))
