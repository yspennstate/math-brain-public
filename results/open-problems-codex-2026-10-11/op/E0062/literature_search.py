import urllib.request, urllib.parse, json, pathlib, concurrent.futures, datetime
ROOT=pathlib.Path(__file__).resolve().parent
queries=['Volterra quadratic stochastic operators ergodic theorem','Volterra quadratic stochastic operators transitive ergodicity','Volterra operators Ulam ergodic necessary sufficient']
jobs=[]
for i,q in enumerate(queries):
    enc=urllib.parse.quote(q)
    jobs += [(f'openalex_{i}', 'OpenAlex',q,f'https://api.openalex.org/works?search={enc}&per-page=30'),
             (f'crossref_{i}','Crossref',q,f'https://api.crossref.org/works?query={enc}&rows=15'),
             (f'semantic_{i}','Semantic Scholar',q,f'https://api.semanticscholar.org/graph/v1/paper/search?query={enc}&limit=20&fields=title,authors,year,url,abstract,externalIds'),
             (f'github_{i}','GitHub',q,f'https://api.github.com/search/repositories?q={enc}&per_page=10')]
aq='all:Volterra AND (all:ergodic OR all:ergodicity)'
jobs.append(('arxiv','arXiv',aq,'http://export.arxiv.org/api/query?search_query='+urllib.parse.quote(aq)+'&start=0&max_results=50'))
jobs.append(('arxiv_https','arXiv',aq,'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote(aq)+'&start=0&max_results=50'))
jobs.append(('source_lookup','OpenAlex','Quadratic stochastic operators results and open problems','https://api.openalex.org/works?search=Quadratic%20stochastic%20operators%20results%20and%20open%20problems&per-page=10'))
def fetch(job):
    name,svc,q,url=job
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'MathematicalResearch/1.0','Accept':'application/json,application/atom+xml,*/*'})
        with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
        (ROOT/(name+'.response')).write_bytes(data)
        outcome=f'OK {len(data)} bytes; saved {name}.response'
    except Exception as e: outcome=f'ERROR {type(e).__name__}: {e}'
    return dict(service=svc,query=q,url=url,date='2026-10-12',outcome=outcome)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
    results=list(ex.map(fetch,jobs))
(ROOT/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
with (ROOT/'LITERATURE.md').open('a',encoding='utf-8') as f:
    f.write('\n## API searches, 2026-10-12\n')
    for r in results: f.write(f"\n- {r['service']}; query: `{r['query']}`; URL: {r['url']}; {r['outcome']}\n")
for r in results: print(r['service'],r['query'],r['outcome'],flush=True)
for name,svc,q,url in jobs:
    p=ROOT/(name+'.response')
    if not p.exists(): continue
    try: d=json.loads(p.read_text(encoding='utf-8'))
    except Exception: continue
    if svc=='OpenAlex': items=d.get('results',[])
    elif svc=='Crossref': items=d.get('message',{}).get('items',[])
    elif svc=='Semantic Scholar': items=d.get('data',[])
    else: items=d.get('items',[])
    print('\nRESULTS',name)
    for w in items:
        print(json.dumps({k:w.get(k) for k in ['id','title','publication_year','year','DOI','doi','url','html_url','cited_by_count','authorships','authors','open_access','primary_location'] if k in w},ensure_ascii=False))
