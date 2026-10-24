import concurrent.futures, json, pathlib, urllib.request, urllib.parse, time
BASE=pathlib.Path(__file__).resolve().parent
requests={
 'source.pdf':'https://www.imo.universite-paris-saclay.fr/~nicolas.curien/cours/peccot.pdf',
 'budd.pdf':'https://arxiv.org/pdf/1506.01590',
 'conditioned.pdf':'https://arxiv.org/pdf/math/0602306',
 'arxiv_search.xml':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"peeling" AND (all:"exhaustion" OR all:"critical weight" OR all:"Boltzmann")','max_results':40,'sortBy':'submittedDate','sortOrder':'descending'}),
 'openalex_search.json':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'filled peeling critical Boltzmann maps','per-page':20}),
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Independent mathematical audit/1.0'})
  with urllib.request.urlopen(req,timeout=75) as r: data=r.read()
  (BASE/name).write_bytes(data)
  return {'file':name,'url':url,'bytes':len(data),'status':'OK'}
 except Exception as e: return {'file':name,'url':url,'status':repr(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
 results=list(pool.map(fetch,requests.items()))
(BASE/'fetch_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
print(json.dumps(results,indent=2))
try:
 import pymupdf
 for name in ['source','budd','conditioned']:
  p=BASE/(name+'.pdf')
  if p.exists():
   doc=pymupdf.open(p)
   (BASE/(name+'.txt')).write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+page.get_text() for i,page in enumerate(doc)),encoding='utf8')
except ImportError:
 import pypdf
 for name in ['source','budd','conditioned']:
  p=BASE/(name+'.pdf')
  if p.exists():
   doc=pypdf.PdfReader(p)
   (BASE/(name+'.txt')).write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+page.extract_text() for i,page in enumerate(doc.pages)),encoding='utf8')
