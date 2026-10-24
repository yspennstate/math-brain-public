import pathlib, json, urllib.request, urllib.parse, concurrent.futures, xml.etree.ElementTree as E
ROOT=pathlib.Path(__file__).resolve().parent
def fetch(name,url):
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'ProbabilityResearch/1.0'})
        with urllib.request.urlopen(req,timeout=40) as r: data=r.read(); code=r.status
        (ROOT/(name+'.raw')).write_bytes(data)
        out={'date':'2026-10-12','name':name,'url':url,'status':code,'bytes':len(data)}
    except Exception as e: out={'date':'2026-10-12','name':name,'url':url,'error':str(e)}
    with (ROOT/'search_log.jsonl').open('a',encoding='utf8') as f: f.write(json.dumps(out)+'\n')
    print(json.dumps(out),flush=True)
q=urllib.parse.quote
tasks=[
('arxiv_tree','https://export.arxiv.org/api/query?search_query='+q('all:Potts AND (all:tree OR all:trees) AND all:reconstruction')+'&max_results=100&sortBy=submittedDate&sortOrder=descending'),
('arxiv_monotone','https://export.arxiv.org/api/query?search_query='+q('all:reconstruction AND (all:monotonicity OR all:monotone) AND (all:Potts OR all:Mossel)')+'&max_results=50'),
('openalex_retry','https://api.openalex.org/works?search='+q('Information flow on trees')+'&per_page=5'),
('semantic_source','https://api.semanticscholar.org/graph/v1/paper/ARXIV:math/0406446?fields=title,year,externalIds,citations.title,citations.year,citations.externalIds'),
('sly_pdf','https://arxiv.org/pdf/0811.1208'),
('gu_polyanskiy_pdf','https://arxiv.org/pdf/2005.05444'),
('crossref_tree','https://api.crossref.org/works?query='+q('Potts reconstruction trees threshold')+'&rows=35'),
('github_monotone','https://api.github.com/search/repositories?q='+q('Potts monotonicity')+'&per_page=20')]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: list(pool.map(lambda t:fetch(*t),tasks))
import pymupdf
for name in ['sly','gu_polyanskiy']:
    if (ROOT/(name+'_pdf.raw')).exists():
        doc=pymupdf.open(ROOT/(name+'_pdf.raw'))
        (ROOT/(name+'.txt')).write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
for name in ['arxiv_tree','arxiv_monotone']:
    if (ROOT/(name+'.raw')).exists():
        root=E.parse(ROOT/(name+'.raw')).getroot(); ns={'a':'http://www.w3.org/2005/Atom'}
        records=[{key:e.find('a:'+key,ns).text for key in ['id','title','summary','published']} for e in root.findall('a:entry',ns)]
        (ROOT/(name+'_summary.json')).write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf8')
        for rec in records: print(rec['id'],rec['title'],flush=True)
