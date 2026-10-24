import urllib.request,urllib.parse,pathlib,concurrent.futures,json
Q=[('openalex_source','https://api.openalex.org/works/https://doi.org/10.1007/978-3-031-36854-7'),('openalex_retry','https://api.openalex.org/works?search=Peeling%20Random%20Planar%20Maps&per_page=5'),('semantic_retry','https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/978-3-031-36854-7?fields=title,year,citations.title,citations.year,citations.externalIds'),('arxiv_exhaust','http://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"peeling" AND (all:"exhaustion" OR all:"critical weight")')+'&max_results=30'),('simple_pdf','https://arxiv.org/pdf/1909.10217'),('markov_pdf','https://arxiv.org/pdf/2505.05447'),('curien_page','https://www.imo.universite-paris-saclay.fr/~nicolas.curien/')]
def run(x):
 name,u=x
 try:
  b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Research/1.0'}),timeout=45).read();pathlib.Path(name+('.pdf' if name.endswith('pdf') else '.txt')).write_bytes(b);return name,u,'OK '+str(len(b))
 except Exception as e:return name,u,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:r=list(ex.map(run,Q))
p=pathlib.Path('search_log.json');old=json.loads(p.read_text());p.write_text(json.dumps(old+r,indent=2),encoding='utf8')
print(*r,sep='\n')
import pymupdf
for name in ['simple_pdf','markov_pdf']:
 p=pathlib.Path(name+'.pdf')
 if p.exists():
  d=pymupdf.open(p);pathlib.Path(name+'.txt').write_text('\n'.join('PDF PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
