from search_literature import fetch
from pathlib import Path
import json, urllib.parse, concurrent.futures
q={
'openalex_doi':'https://api.openalex.org/works/https://doi.org/10.1017/S0269964821000115',
'crossref_endless':'https://api.crossref.org/works/10.1080/07468342.2023.2201150',
'semantic_search':'https://api.semanticscholar.org/graph/v1/paper/search?'+urllib.parse.urlencode({'query':'nearest unvisited vertex','limit':20,'fields':'title,year,externalIds,abstract'}),
'arxiv_greedy':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"greedy walk" OR all:"nearest neighbor algorithm"','max_results':50}),
}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: results=list(pool.map(fetch,q.items()))
p=Path('search_log.json'); old=json.loads(p.read_text());p.write_text(json.dumps(old+results,indent=2))
for r in results:print(r)
p=Path('search_openalex_doi.txt')
if p.exists():
 d=json.loads(p.read_text()); print('OPENALEX',d.get('id'),d.get('title'),d.get('cited_by_count'))
 if 'id' in d:
  r=fetch(('openalex_citing','https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:'+d['id'].split('/')[-1],'per-page':100})))
  old=json.loads(Path('search_log.json').read_text());Path('search_log.json').write_text(json.dumps(old+[r],indent=2)); print(r)
p=Path('search_openalex_citing.txt')
if p.exists():
 for x in json.loads(p.read_text()).get('results',[]):print(x['title'],x['publication_year'],x.get('doi'))
p=Path('search_crossref_endless.txt')
if p.exists():
 d=json.loads(p.read_text())['message'];print('ENDLESS',d.get('author'),d.get('abstract'),d.get('link'))
