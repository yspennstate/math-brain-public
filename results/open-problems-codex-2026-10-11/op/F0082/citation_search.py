import pathlib,urllib.request,json,concurrent.futures
p=pathlib.Path('.')
q={
'openalex_correct_source':'https://api.openalex.org/works/https://doi.org/10.1214/08-AIHP170',
'semantic_citations':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:0712.1867/citations?fields=title,year,externalIds&limit=100',
'crossref_planar':'https://api.crossref.org/works?query=translation%20invariant%20planar%20Poisson%20matching&rows=30'}
def f(kv):
 k,u=kv
 try:
  b=urllib.request.urlopen(u,timeout=35).read();p.joinpath(k+'.json').write_bytes(b);s=f'OK {len(b)} bytes'
 except Exception as e:s=str(e)
 return k,u,s
r=list(concurrent.futures.ThreadPoolExecutor(max_workers=3).map(f,q.items()));print(r)
with open('LITERATURE.md','a',encoding='utf8') as o:
 for k,u,s in r:o.write(f'- 2026-10-11 {k}: {u} — {s}.\n')
if p.joinpath('openalex_correct_source.json').exists():
 d=json.load(open('openalex_correct_source.json',encoding='utf8'));u='https://api.openalex.org/works?filter=cites:'+d['id'].split('/')[-1]+'&per-page=200'
 r=f(('openalex_citations',u));print(r)
 with open('LITERATURE.md','a',encoding='utf8') as o:o.write(f'- 2026-10-11 OpenAlex citing works: {u} — {r[2]}.\n')
else:
 with open('LITERATURE.md','a',encoding='utf8') as o:o.write('OpenAlex citing-works enumeration could not be run: source-ID resolution is rate-limited. No successful citation graph audit is claimed. The earlier DOI 08-AIHP185 query was incorrect; corrected to 08-AIHP170 here.\n')
