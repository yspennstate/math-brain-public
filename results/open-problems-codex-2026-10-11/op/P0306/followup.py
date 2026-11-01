import pathlib,json,urllib.parse,concurrent.futures,urllib.request
ROOT=pathlib.Path(__file__).resolve().parent
q=urllib.parse.quote
exec((ROOT/'fetch_literature.py').read_text(encoding='utf-8').split('q = urllib.parse.quote')[0])
jobs=[
 ('arxiv_recent','https://export.arxiv.org/api/query?search_query='+q('all:"quantum gravity" AND (all:geodesic OR all:boundary) AND submittedDate:[20260609 TO 20261011]')+'&max_results=100&sortBy=submittedDate&sortOrder=descending'),
 ('arxiv_stars','https://export.arxiv.org/api/query?search_query='+q('all:"Liouville quantum gravity" AND all:geodesic')+'&max_results=60&sortBy=submittedDate&sortOrder=descending'),
 ('openalex_lookup','https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2606.10496'),
 ('openalex_retry','https://api.openalex.org/works?search='+q('"Dimension lower bounds in random geometry via Lipschitz functions"')+'&per_page=5'),
 ('semantic_retry','https://api.semanticscholar.org/graph/v1/paper/search/bulk?query='+q('"Liouville quantum gravity" +boundary +geodesic')+'&fields=title,year,externalIds'),
 ('semantic_citations','https://api.semanticscholar.org/graph/v1/paper/ARXIV:2606.10496/citations?fields=title,year,externalIds&limit=100'),
 ('github_stars','https://api.github.com/search/repositories?q='+q('"LQG" "geodesic"')+'&per_page=30'),
]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:
    for r in p.map(lambda j:fetch(*j),jobs): print(json.dumps(r),flush=True)
try:
    rec=json.loads((ROOT/'openalex_lookup.txt').read_text())
    if rec.get('id'):
        print(json.dumps(fetch('openalex_citing','https://api.openalex.org/works?filter=cites:'+rec['id'].rsplit('/',1)[-1]+'&per_page=100')),flush=True)
except Exception as e: print('OpenAlex citation lookup not available:',str(e))
