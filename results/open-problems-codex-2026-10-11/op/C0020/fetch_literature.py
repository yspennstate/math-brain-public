from pathlib import Path
import urllib.request, urllib.parse, concurrent.futures, json, datetime
ROOT=Path(__file__).resolve().parent
queries={
'source_pdf':'https://arxiv.org/pdf/1102.5761',
'arxiv':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:percolation AND (all:algorithm OR all:"query complexity" OR all:revealment)','start':0,'max_results':60,'sortBy':'submittedDate','sortOrder':'descending'}),
'openalex_source':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Noise Sensitivity of Boolean Functions and Percolation','per-page':8}),
'openalex_search':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'percolation crossing randomized algorithm complexity','per-page':40}),
'crossref':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'percolation crossing randomized algorithm complexity','rows':40}),
'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?'+urllib.parse.urlencode({'query':'percolation randomized algorithm complexity','limit':40,'fields':'title,authors,year,abstract,url,externalIds'}),
'github':'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'percolation crossing algorithm','per_page':30})}
def fetch(k,u):
    try:
        req=urllib.request.Request(u,headers={'User-Agent':'C0020-mathematical-research/1.0'})
        with urllib.request.urlopen(req,timeout=65) as r: b=r.read(); status=r.status
        (ROOT/(k+('.pdf' if k=='source_pdf' else '.response'))).write_bytes(b)
        return {'service':k,'url':u,'date':'2026-10-12','status':status,'bytes':len(b)}
    except Exception as e:return {'service':k,'url':u,'date':'2026-10-12','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
    rows=list(ex.map(lambda kv:fetch(*kv),queries.items()))
(ROOT/'search_log.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in rows),encoding='utf8')
for x in rows: print(json.dumps(x))
try:
 import pymupdf
 doc=pymupdf.open(ROOT/'source_pdf.pdf')
 (ROOT/'source.txt').write_text('\n'.join('=== PDF PAGE '+str(i+1)+' ===\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
 print('PDF extracted',len(doc))
except Exception as e: print('PDF extraction',repr(e))
