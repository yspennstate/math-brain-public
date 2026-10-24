import pathlib,json
s=pathlib.Path('rolla.txt').read_text(encoding='utf8')
a=s.find('Theorem 6.1'); print(s[max(0,a-4000):a+10500])
for fn in ['openalex_search.json','openalex_source.json','crossref.json','semantic.json']:
 p=pathlib.Path(fn)
 if not p.exists(): continue
 x=json.loads(p.read_text(encoding='utf8')); works=x.get('results',x.get('data',x.get('message',{}).get('items',[])))
 print('\nFILE',fn)
 for w in works: print(w.get('id',w.get('DOI','')), w.get('publication_year',w.get('year','')), w.get('title'),w.get('doi',''))
