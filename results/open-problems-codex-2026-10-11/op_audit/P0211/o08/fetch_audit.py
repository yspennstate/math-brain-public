from pathlib import Path
import urllib.request, urllib.parse, json, concurrent.futures
import fitz

ROOT=Path(__file__).resolve().parent
queries={
 'source.html':'https://www.stat.berkeley.edu/~aldous/Research/OP/coag_frag.html',
 'source.pdf':'https://www.stat.berkeley.edu/~aldous/Research/OP/coag_frag_mix.pdf',
 'arxiv.xml':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:coagulation AND (all:"spectral gap" OR all:relaxation OR all:"mixing time")','max_results':40}),
 'openalex.json':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'linear polymer coagulation fragmentation relaxation','per_page':20}),
 'crossref.json':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'coagulation fragmentation spectral gap relaxation Aldous','rows':20}),
 'hoze.pdf':'https://arxiv.org/pdf/1611.06493',
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Independent mathematical audit/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  (ROOT/name).write_bytes(data)
  if name.endswith('.pdf'):
   doc=fitz.open(stream=data,filetype='pdf')
   (ROOT/(name+'.txt')).write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
  return {'file':name,'url':url,'status':'OK','bytes':len(data)}
 except Exception as e: return {'file':name,'url':url,'status':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(fetch,queries.items()))
(ROOT/'fetch_results.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
