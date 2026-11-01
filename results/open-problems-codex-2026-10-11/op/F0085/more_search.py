exec(open('search.py',encoding='utf-8-sig').read().split('with concurrent')[0])
urls={
'openalex_citing':'https://api.openalex.org/works?filter=cites:W2161642397&per-page=100',
'openalex_doi':'https://api.openalex.org/works?filter=doi:https://doi.org/10.1214/009117906000000098&per-page=1',
'semantic_source_citing':'https://api.semanticscholar.org/graph/v1/paper/DOI:10.1214/009117906000000098/citations?fields=title,year,externalIds&limit=100',
'crossref_unclaimed':'https://api.crossref.org/works?query='+urllib.parse.quote('stable marriage unclaimed percolation')+'&rows=30',
'random_appetites':'https://arxiv.org/pdf/0909.5325'}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: results=list(ex.map(lambda kv:fetch(*kv),urls.items()))
old=json.loads((P/'search_log.json').read_text(encoding='utf8'));(P/'search_log.json').write_text(json.dumps(old+results,indent=2),encoding='utf8')
for r in results:print(r)
import pymupdf
d=pymupdf.open('random_appetites.json');(P/'random_appetites.txt').write_text('\n'.join('--- PDF PAGE '+str(i+1)+' ---\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
