import search_literature as s, urllib.parse as u, concurrent.futures, pathlib, xml.etree.ElementTree as E, json
q=[
('openalex_doi','https://api.openalex.org/works/https://doi.org/10.1007/978-3-319-18585-9_4'),
('arxiv_targeted','http://export.arxiv.org/api/query?'+u.urlencode({'search_query':'cat:math.PR AND (all:"patterns" AND all:"waiting")','max_results':100})),
('arxiv_pitman_tang','http://export.arxiv.org/api/query?'+u.urlencode({'search_query':'all:"Pitman" AND all:"Tang" AND all:"patterns"','max_results':100})),
('crossref_targeted','https://api.crossref.org/works?'+u.urlencode({'query':'pattern waiting times Pitman Tang','rows':40})),
('s2_search','https://api.semanticscholar.org/graph/v1/paper/search?'+u.urlencode({'query':'patterns random walks Brownian motion','limit':10,'fields':'title,year,externalIds'})),
]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p: list(p.map(s.fetch,q))
p=pathlib.Path('openalex_doi.response')
if p.exists():
 d=json.loads(p.read_text()); ident=d['id'].split('/')[-1]
 s.fetch(('openalex_citing','https://api.openalex.org/works?'+u.urlencode({'filter':'cites:'+ident,'per-page':100})))
else:
 s.fetch(('openalex_citing_attempt','https://api.openalex.org/works?'+u.urlencode({'filter':'cites:doi:10.1007/978-3-319-18585-9_4','per-page':100})))
ns={'a':'http://www.w3.org/2005/Atom'}
for name,_ in q:
 f=pathlib.Path(name+'.response')
 if not f.exists(): continue
 if name.startswith('arxiv'):
  entries=E.fromstring(f.read_bytes()).findall('a:entry',ns)
  rows=[{'id':x.find('a:id',ns).text,'title':x.find('a:title',ns).text,'summary':x.find('a:summary',ns).text} for x in entries]
  pathlib.Path(name+'.summary.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
  for x in rows: print(x['id'],x['title'].replace('\n',' '),flush=True)
