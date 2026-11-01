import research,json,concurrent.futures,xml.etree.ElementTree as E
q={
 'transport_retry_pdf':'https://arxiv.org/pdf/1504.02965',
 'random_retry_pdf':'https://arxiv.org/pdf/0911.1429',
 'semantic_tails_retry':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:math/0507324?fields=title,year,citations.title,citations.year,citations.externalIds',
 'arxiv_tail':'https://export.arxiv.org/api/query?search_query=all:stable%20AND%20all:Poisson%20AND%20all:critical%20AND%20all:tail&max_results=50',
 'openalex_citing_retry':'https://api.openalex.org/works?filter=cites:https://doi.org/10.1214/009117906000000098&per-page=100',
}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 out=list(ex.map(lambda kv:research.fetch(*kv),q.items()))
p=research.ROOT/'search_log.json';p.write_text(json.dumps(json.loads(p.read_text())+out,indent=2))
print(json.dumps(out,indent=2))
import pymupdf
for k in ['transport_retry','random_retry']:
 try:
  doc=pymupdf.open(research.ROOT/(k+'_pdf.pdf'))
  (research.ROOT/(k+'.txt')).write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+x.get_text() for i,x in enumerate(doc)),encoding='utf8')
 except Exception as e: print(k,e)
