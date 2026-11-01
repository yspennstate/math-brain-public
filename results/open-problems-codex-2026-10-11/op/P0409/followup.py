import pathlib,json,urllib.request,urllib.parse,concurrent.futures
p=pathlib.Path('.')
queries={'openalex_citing_arxiv':'https://api.openalex.org/works?filter=cites:W4361807156&per-page=100','openalex_citing_journal':'https://api.openalex.org/works?filter=cites:W7131653980&per-page=100','arxiv_focused':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"Voronoi" AND (all:"neighboring" OR all:"Palm" OR all:"Laguerre")')+'&max_results=50','semantic_search':'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('ideal Voronoi neighboring vertices')+'&limit=20&fields=title,authors,year,externalIds'}
def fetch(k,u):
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'P0409-research/1.0'}),timeout=45) as r:s=r.read().decode()
  p.joinpath('search_'+k+'.txt').write_text(s,encoding='utf-8');return k,u,'OK'
 except Exception as e:return k,u,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:out=list(ex.map(lambda z:fetch(*z),queries.items()))
with p.joinpath('LITERATURE.md').open('a',encoding='utf-8') as f:
 for k,u,s in out:f.write(f'\n- {k}: `{u}` — {s}\n')
print(out)
ss=json.loads(p.joinpath('search_semantic.txt').read_text(encoding='utf-8'))
for a in ss['data']:
 a=a['citingPaper']
 if any(w in a['title'] for w in ['Laguerre','Face volume','polyhedra','Convergence']): print(a)
j=json.loads(p.joinpath('search_openalex.txt').read_text(encoding='utf-8'))
for a in j['results'][:8]:print(a['title'],[(z['author']['display_name']) for z in a['authorships']],a['primary_location'].get('landing_page_url'),a.get('doi'))
