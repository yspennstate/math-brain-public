from pathlib import Path
import urllib.request, urllib.parse, concurrent.futures, json, datetime
base=Path('.')
queries={
 'source_pdf':'https://arxiv.org/pdf/1908.06825',
 'arxiv':'http://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"Hunt hypothesis" OR all:"Hunt\'s hypothesis"','start':0,'max_results':50,'sortBy':'submittedDate','sortOrder':'descending'}),
 'openalex':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':"Hunt hypothesis",'per-page':50}),
 'openalex_source':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':"Hunt's hypothesis (H) for Markov processes: survey and beyond",'per-page':5}),
 'crossref':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':"Hunt hypothesis Levy sum",'rows':30}),
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?'+urllib.parse.urlencode({'query':"Hunt hypothesis",'limit':50,'fields':'title,authors,year,externalIds,url,abstract'}),
 'github':'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'"Hunt hypothesis"','per_page':30})}
def fetch(item):
 key,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'ProbabilityResearch/1.0','Accept':'*/*'})
  with urllib.request.urlopen(req,timeout=45) as f: data=f.read(); status=f.status
  suffix='.pdf' if key=='source_pdf' else '.json' if key not in ('arxiv',) else '.xml'
  base.joinpath(key+suffix).write_bytes(data)
  info={'service':key,'query_url':url,'date':'2026-10-12','http_status':status,'bytes':len(data),'file':key+suffix}
 except Exception as e: info={'service':key,'query_url':url,'date':'2026-10-12','error':str(e)}
 with base.joinpath('search_log.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps(info)+'\n')
 return info
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
 for r in ex.map(fetch,queries.items()): print(json.dumps(r))
try:
 import pymupdf
 doc=pymupdf.open('source_pdf.pdf')
 base.joinpath('source.txt').write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
 print('Extracted',len(doc),'pages')
except Exception as e: print('PDF extract:',e)
