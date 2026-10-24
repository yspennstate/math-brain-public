from pathlib import Path
import urllib.request,urllib.parse,concurrent.futures,json
qs=[('dg_publisher','https://www.sciencedirect.com/science/article/pii/S0304414900000302'),('wetting_metadata','https://api.openalex.org/works/W1970562499'),('bl_pdf','https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S0305004102006552/S0305004102006552a.pdf/on-stochastic-domination-in-the-brascamp-lieb-framework.pdf'),('dg_lpsmraw','https://www.lpsm.paris/_export/raw/pageperso/giacomin/index'),('arxiv_wetting_query','https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'ti:"Wetting of gradient fields"','max_results':5})),('crossref_max','https://api.crossref.org/works?'+urllib.parse.urlencode({'query.title':'Maximum of the Ginzburg Landau fields','rows':3}))]
def run(pair):
 n,u=pair
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'F0073 research'}),timeout=35) as r:b=r.read()
  ext='.pdf' if b[:4]==b'%PDF' else '.json' if b[:1]==b'{' else '.xml' if 'arxiv' in n else '.html'
  Path(n+ext).write_bytes(b);s='OK '+str(len(b))
  if ext=='.pdf':
   import pymupdf
   d=pymupdf.open(n+ext);Path(n+'.txt').write_text('\n'.join('\nPAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
 except Exception as e:s=repr(e)
 with Path('LITERATURE.md').open('a',encoding='utf8') as f:f.write(f'\n- 2026-10-12 | {n} | `{u}` | {s}\n')
 print(n,s)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:list(ex.map(run,qs))
