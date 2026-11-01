import pathlib,urllib.request,concurrent.futures,json
queries=[('budd','https://arxiv.org/pdf/1506.01590'),('conditioned','https://arxiv.org/pdf/math/0602306'),('research_page','https://www.imo.universite-paris-saclay.fr/~nicolas.curien/recherche.html'),('openalex_cites','https://api.openalex.org/works?filter=cites:W4386255711&per-page=30')]
def f(x):
 n,u=x
 try:
  d=urllib.request.urlopen(u,timeout=40).read();pathlib.Path(n+('.pdf' if n in ['budd','conditioned'] else '.txt')).write_bytes(d);return n,u,'OK '+str(len(d))
 except Exception as e:return n,u,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:r=list(e.map(f,queries))
p=pathlib.Path('search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+r,indent=2),encoding='utf8');print(r)
import pymupdf
for n in ['budd','conditioned']:
 if pathlib.Path(n+'.pdf').exists():
  d=pymupdf.open(n+'.pdf');pathlib.Path(n+'.txt').write_text('\n'.join('PDF PAGE '+str(i+1)+'\n'+x.get_text() for i,x in enumerate(d)),encoding='utf8')
