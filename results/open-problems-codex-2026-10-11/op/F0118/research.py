import urllib.request, urllib.parse, json, pathlib, concurrent.futures, datetime
ROOT = pathlib.Path(__file__).resolve().parent
def fetch(name,url):
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'ProbabilityResearch/1.0'})
        with urllib.request.urlopen(req,timeout=45) as r:
            data=r.read(); status=r.status
        (ROOT/(name+'.raw')).write_bytes(data)
        out={'name':name,'url':url,'status':status,'bytes':len(data)}
    except Exception as e: out={'name':name,'url':url,'error':str(e)}
    with (ROOT/'search_log.jsonl').open('a',encoding='utf8') as f: f.write(json.dumps({'date':'2026-10-12',**out})+'\n')
    print(json.dumps(out),flush=True)
    return out
q=urllib.parse.quote
tasks=[
('mossel_pdf','https://arxiv.org/pdf/math/0406446'),
('arxiv_http','http://export.arxiv.org/api/query?search_query='+q('all:Potts AND all:reconstruction')+'&max_results=40'),
('arxiv_https','https://export.arxiv.org/api/query?search_query='+q('all:Potts AND all:reconstruction')+'&max_results=40'),
('openalex_search','https://api.openalex.org/works?search='+q('Potts reconstruction monotonicity')+'&per-page=30'),
('openalex_source','https://api.openalex.org/works?search='+q('Survey Information flow on trees')+'&per-page=5'),
('crossref','https://api.crossref.org/works?query='+q('Potts reconstruction monotonicity')+'&rows=25'),
('semantic','https://api.semanticscholar.org/graph/v1/paper/search?query='+q('Potts reconstruction')+'&limit=30&fields=title,authors,year,externalIds,url,abstract'),
('github','https://api.github.com/search/repositories?q='+q('Potts reconstruction')+'&per_page=20')]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: list(pool.map(lambda t:fetch(*t),tasks))
try:
    import pymupdf
    doc=pymupdf.open(ROOT/'mossel_pdf.raw')
    (ROOT/'mossel.txt').write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
    print('pdf converted',flush=True)
except Exception as e: print('pdf conversion:',str(e),flush=True)
