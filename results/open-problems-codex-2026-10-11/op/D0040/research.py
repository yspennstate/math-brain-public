import urllib.request, urllib.parse, json, datetime, pathlib, concurrent.futures
ROOT=pathlib.Path(__file__).resolve().parent
queries={
 'arxiv': 'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"beta ensembles" AND all:"minors"')+'&max_results=20',
 'openalex_search':'https://api.openalex.org/works?search='+urllib.parse.quote('tridiagonal beta ensembles nested')+'&per-page=15',
 'openalex_source':'https://api.openalex.org/works?filter=locations.source.id:s4306400194&search='+urllib.parse.quote('Operator limits of random matrices')+'&per-page=5',
 'crossref':'https://api.crossref.org/works?query='+urllib.parse.quote('nested tridiagonal beta ensembles')+'&rows=15',
 'semantic_scholar':'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('nested tridiagonal beta ensembles')+'&limit=15&fields=title,year,authors,url,abstract',
 'github':'https://api.github.com/search/repositories?q='+urllib.parse.quote('tridiagonal beta ensembles'),
 'source':'https://arxiv.org/pdf/1804.06953',
 'dumitriu_edelman':'https://arxiv.org/pdf/math-ph/0206043',
}
def get(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'D0040-mathematical-research/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  path=ROOT/(name+('.pdf' if name in ('source','dumitriu_edelman') else '.response'))
  path.write_bytes(data)
  result='OK '+str(len(data))+' bytes; '+path.name
 except Exception as e: result='ERROR '+repr(e)
 with (ROOT/'search_log.jsonl').open('a',encoding='utf-8') as f:
  f.write(json.dumps({'date':datetime.datetime.now().isoformat(),'service':name,'url':url,'result':result})+'\n')
 print(name,result,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: list(ex.map(get,queries.items()))
for name in ['source','dumitriu_edelman']:
 try:
  import pymupdf
  doc=pymupdf.open(ROOT/(name+'.pdf'))
  (ROOT/(name+'.txt')).write_text('\n'.join('PDF PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
 except Exception as e: print('extract',name,repr(e),flush=True)
