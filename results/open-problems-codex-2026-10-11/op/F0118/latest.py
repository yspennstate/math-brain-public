import pathlib,urllib.request,urllib.parse,json,concurrent.futures,xml.etree.ElementTree as E
ROOT=pathlib.Path(__file__).resolve().parent
def fetch(name,url):
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'ProbabilityResearch/1.0','Accept':'application/json' if 'openalex' in url else '*/*'})
        with urllib.request.urlopen(req,timeout=35) as r: data=r.read(); status=r.status
        (ROOT/(name+'.raw')).write_bytes(data)
        rec={'date':'2026-10-12','name':name,'url':url,'status':status,'bytes':len(data)}
    except Exception as e: rec={'date':'2026-10-12','name':name,'url':url,'error':str(e)}
    with (ROOT/'search_log.jsonl').open('a',encoding='utf8') as f: f.write(json.dumps(rec)+'\n')
    print(json.dumps(rec),flush=True)
q=urllib.parse.quote
tasks=[
('growing_pdf','https://arxiv.org/pdf/2609.33263'),
('bp_pdf','https://arxiv.org/pdf/2303.14688'),
('arxiv_mss','https://export.arxiv.org/api/query?search_query='+q('au:Mossel AND au:Sohn AND (all:Potts OR all:reconstruction)')+'&max_results=20'),
('crossref_source','https://api.crossref.org/works?query.title='+q('Survey Information flow on trees')+'&rows=5'),
('openalex_title','https://api.openalex.org/works?filter='+q('title.search:Information flow on trees')+'&per-page=10'),
('semantic_retry','https://api.semanticscholar.org/graph/v1/paper/search?query='+q('Information flow on trees Mossel')+'&limit=5&fields=title,externalIds,year,paperId')]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: list(pool.map(lambda x:fetch(*x),tasks))
import pymupdf
for name in ['growing','bp']:
    path=ROOT/(name+'_pdf.raw')
    if path.exists():
        doc=pymupdf.open(path)
        (ROOT/(name+'.txt')).write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
if (ROOT/'arxiv_mss.raw').exists():
    root=E.parse(ROOT/'arxiv_mss.raw').getroot(); ns={'a':'http://www.w3.org/2005/Atom'}
    for e in root.findall('a:entry',ns): print(e.find('a:id',ns).text,e.find('a:title',ns).text,e.find('a:summary',ns).text,flush=True)
