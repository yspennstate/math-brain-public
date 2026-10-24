from pathlib import Path
import pymupdf, urllib.request, urllib.parse, json, concurrent.futures
ROOT=Path(__file__).resolve().parent
doc=pymupdf.open(ROOT/'source_independent.pdf')
pages=[269,373,391,394,398,448,449,450,451,452,453,708]
text='\n\n'.join('PDF PAGE '+str(p)+'\n'+doc[p-1].get_text() for p in pages)
(ROOT/'source_verified.txt').write_text(text,encoding='utf-8')
print('Downloaded source pages:',len(doc))
for p in [373,391,394,398]:
    print('PDF PAGE',p,doc[p-1].get_text()[:2500])
queries={
 'arxiv_pivotal': 'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"second order" AND all:pivotal','start':0,'max_results':20}),
 'arxiv_cerf': 'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'au:Cerf AND (all:pivotal OR all:"2608.23661")','start':0,'max_results':20}),
 'openalex': 'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'second order pivotal Cerf','per-page':10}),
 'crossref': 'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'second order pivotal Cerf','rows':10}),
}
def get(item):
    name,url=item
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'G0002-independent-referee/1.0'})
        with urllib.request.urlopen(req,timeout=25) as res: raw=res.read(); status=res.status
        (ROOT/(name+'_response.txt')).write_bytes(raw)
        return dict(name=name,url=url,status=status,bytes=len(raw))
    except Exception as e:
        return dict(name=name,url=url,error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    results=list(pool.map(get,queries.items()))
(ROOT/'independent_search_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
