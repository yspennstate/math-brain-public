import pathlib,urllib.request,json,concurrent.futures
ROOT=pathlib.Path(__file__).resolve().parent
def fetch(name,url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'ProbabilityResearch/1.0'}),timeout=35) as r: data=r.read(); code=r.status
        (ROOT/(name+'.raw')).write_bytes(data)
        rec={'date':'2026-10-12','name':name,'url':url,'status':code,'bytes':len(data)}
    except Exception as e: rec={'date':'2026-10-12','name':name,'url':url,'error':str(e)}
    with (ROOT/'search_log.jsonl').open('a',encoding='utf8') as f: f.write(json.dumps(rec)+'\n')
    print(json.dumps(rec),flush=True)
    return rec
tasks=[
('mss_pdf','https://arxiv.org/pdf/2212.03362'),
('openalex_doi','https://api.openalex.org/works/https://doi.org/10.1090/dimacs/063/12'),
('semantic_doi','https://api.semanticscholar.org/graph/v1/paper/DOI:10.1090/dimacs/063/12?fields=title,year,externalIds,citations.title,citations.year,citations.externalIds'),
('mp_pdf','https://arxiv.org/pdf/math/0107033')]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: list(pool.map(lambda t:fetch(*t),tasks))
if (ROOT/'openalex_doi.raw').exists():
    work=json.loads((ROOT/'openalex_doi.raw').read_text(encoding='utf8'))
    fetch('openalex_citing','https://api.openalex.org/works?filter=cites:'+work['id'].split('/')[-1]+'&per-page=100')
else:
    with (ROOT/'search_log.jsonl').open('a',encoding='utf8') as f: f.write(json.dumps({'date':'2026-10-12','name':'openalex_citing','status':'BLOCKED','reason':'All source lookup requests rate-limited; cannot obtain a verified OpenAlex work ID for cites filter.'})+'\n')
import pymupdf
for name in ['mss','mp']:
    path=ROOT/(name+'_pdf.raw')
    if path.exists():
        doc=pymupdf.open(path)
        (ROOT/(name+'.txt')).write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
