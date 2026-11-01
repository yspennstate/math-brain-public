import urllib.request, urllib.parse, concurrent.futures, pathlib, json, datetime
root=pathlib.Path('.')
queries={
 'cerf_pdf':'https://arxiv.org/pdf/2608.23661',
 'cerf_abs':'https://arxiv.org/abs/2608.23661',
 'arxiv':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"percolation" AND (all:"finite cluster" OR all:"Cerf")','start':0,'max_results':30,'sortBy':'submittedDate','sortOrder':'descending'}),
 'openalex':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Cerf theta percolation critical','per-page':20}),
 'crossref':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'Cerf percolation finite cluster stretched exponential','rows':20}),
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2608.23661?fields=title,authors,year,citations.title,citations.year,citations.externalIds',
 'github':'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'percolation criticality','per_page':20}),
}
def fetch(pair):
 k,u=pair
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'MathematicalResearch/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read();status=r.status
  name=k+('.pdf' if k.endswith('pdf') else '.txt');(root/name).write_bytes(data)
  return {'service':k,'url':u,'date':'2026-10-11','status':status,'bytes':len(data),'file':name}
 except Exception as e:return {'service':k,'url':u,'date':'2026-10-11','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
 results=list(ex.map(fetch,queries.items()))
(root/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
(root/'LITERATURE.md').write_text('# Literature audit — 2026-10-11\n\nNo solution in print verified.\n\n'+''.join('Query: '+x['service']+'\nURL: '+x['url']+'\nResult: '+str(x)+'\n\n' for x in results),encoding='utf8')
for x in results:print(x)
try:
 import pymupdf
 doc=pymupdf.open('cerf_pdf.pdf')
 (root/'cerf_source.txt').write_text('\n'.join(f'\n[PDF PAGE {i+1}]\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
 print('PDF pages',len(doc)); print('\n'.join(doc[i].get_text() for i in range(min(4,len(doc)))))
except Exception as e:print('PDF extraction:',e)
