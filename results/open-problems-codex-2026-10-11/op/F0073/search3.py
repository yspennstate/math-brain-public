import urllib.request,urllib.parse,concurrent.futures,json
from pathlib import Path
qs=[('maximum2016','https://arxiv.org/pdf/1610.04195'),('maximum2024','https://arxiv.org/pdf/2403.11500'),('wetting','https://arxiv.org/pdf/math/0604175'),('dg_oa','https://api.openalex.org/works/https://doi.org/10.1016/S0304-4149(00)00030-2'),('bl_crossref','https://api.crossref.org/works?'+urllib.parse.urlencode({'query.title':'On stochastic domination in the Brascamp Lieb framework','rows':3})),('dg_author','https://www.lpsm.paris/pageperso/giacomin/')]
def f(pair):
 n,u=pair
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'F0073 research'}),timeout=40) as r:b=r.read()
  ext='.pdf' if b[:4]==b'%PDF' else '.json' if b[:1]==b'{' else '.html'
  Path(n+ext).write_bytes(b);s='OK '+str(len(b))
  if ext=='.pdf':
   import pymupdf
   d=pymupdf.open(n+ext);Path(n+'.txt').write_text('\n'.join('\nPAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
 except Exception as e:s=repr(e)
 with Path('LITERATURE.md').open('a',encoding='utf8') as out:out.write(f'\n- 2026-10-12 | {n} | `{u}` | {s}\n')
 print(n,s)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:list(ex.map(f,qs))

