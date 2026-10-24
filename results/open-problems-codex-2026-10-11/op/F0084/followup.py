import research, json, concurrent.futures, pathlib
q={
 'tails_pdf':'https://arxiv.org/pdf/math/0507324',
 'transport_pdf':'https://arxiv.org/pdf/1504.02965',
 'random_pdf':'https://arxiv.org/pdf/0911.1429',
 'arxiv_critical':'https://export.arxiv.org/api/query?search_query=all:%22stable%20allocation%22%20AND%20all:critical&max_results=40',
 'openalex_source':'https://api.openalex.org/works/https://doi.org/10.1214/009117906000000098',
 'semantic_tails':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:math/0507324?fields=title,year,citations.title,citations.year,citations.externalIds',
}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 out=list(ex.map(lambda kv:research.fetch(*kv),q.items()))
p=research.ROOT/'search_log.json'; old=json.loads(p.read_text()); p.write_text(json.dumps(old+out,indent=2))
print(json.dumps(out,indent=2))
import pymupdf
for k in ['tails','transport','random']:
 try:
  doc=pymupdf.open(research.ROOT/(k+'_pdf.pdf'))
  (research.ROOT/(k+'.txt')).write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+x.get_text() for i,x in enumerate(doc)),encoding='utf8')
 except Exception as e: print(k,e)
# OpenAlex citation query, if the source lookup succeeded.
lookup=research.ROOT/'openalex_source.xml'
try:
 data=json.loads(lookup.read_text()); wid=data['id'].split('/')[-1]
 r=research.fetch('openalex_citing','https://api.openalex.org/works?filter=cites:'+wid+'&per-page=100')
 old=json.loads(p.read_text());p.write_text(json.dumps(old+[r],indent=2));print(r)
except Exception as e:
 r=research.fetch('openalex_citing_doi','https://api.openalex.org/works?filter=cites:https://doi.org/10.1214/009117906000000098&per-page=100')
 old=json.loads(p.read_text());p.write_text(json.dumps(old+[r],indent=2));print(r)
