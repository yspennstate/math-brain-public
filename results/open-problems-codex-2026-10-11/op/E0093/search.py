import concurrent.futures, json, pathlib, urllib.request, urllib.parse, datetime
ROOT=pathlib.Path(__file__).resolve().parent
def fetch(item):
    name,url=item
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'E0093-mathematical-literature-check/1.0'})
        with urllib.request.urlopen(req,timeout=45) as r:
            data=r.read(); status=r.status
        (ROOT/(name+'.raw')).write_bytes(data)
        result={'name':name,'url':url,'status':status,'bytes':len(data),'date':'2026-10-12'}
    except Exception as e: result={'name':name,'url':url,'error':str(e),'date':'2026-10-12'}
    print(json.dumps(result),flush=True)
    return result
q=urllib.parse.quote
jobs=[
 ('diaconis_pdf','https://arxiv.org/pdf/1309.7754'),
 ('arxiv','http://export.arxiv.org/api/query?search_query='+q('all:"random Cayley" AND all:mixing')+'&start=0&max_results=40'),
 ('arxiv_https','https://export.arxiv.org/api/query?search_query='+q('all:"random Cayley" AND all:mixing')+'&start=0&max_results=40'),
 ('openalex','https://api.openalex.org/works?search='+q('random Cayley graphs mixing')+'&per-page=40'),
 ('openalex_source','https://api.openalex.org/works?search='+q('Some things we have learned about Markov chain Monte Carlo')+'&per-page=5'),
 ('crossref','https://api.crossref.org/works?query='+q('random Cayley graphs mixing')+'&rows=30'),
 ('semantic','https://api.semanticscholar.org/graph/v1/paper/search?query='+q('random Cayley graphs mixing')+'&limit=30&fields=title,authors,year,externalIds,url,abstract'),
 ('github','https://api.github.com/search/repositories?q='+q('random Cayley mixing')+'&per_page=20')]
if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        results=list(pool.map(fetch,jobs))
    (ROOT/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
    try:
        import pymupdf
        doc=pymupdf.open(ROOT/'diaconis_pdf.raw')
        (ROOT/'diaconis.txt').write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
    except Exception as e: print('PDF extraction:',repr(e))
