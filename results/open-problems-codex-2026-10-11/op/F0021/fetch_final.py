import pathlib,urllib.request,concurrent.futures,json
p=pathlib.Path('.')
qs=[('finite_moments','https://arxiv.org/pdf/2609.08308'),('high_temp','https://arxiv.org/pdf/2503.20192'),('openalex_doi','https://api.openalex.org/works/https://doi.org/10.1016/j.spa.2024.104431')]
with p.joinpath('LITERATURE.md').open('a',encoding='utf-8') as f:
 for n,u in qs:f.write(f'- {n}: `{u}` (2026-10-12).\n')
def get(z):
 n,u=z
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'math-research'}),timeout=45) as r:data=r.read()
  p.joinpath(n+('.json' if n=='openalex_doi' else '.pdf')).write_bytes(data);return n,len(data)
 except Exception as e:p.joinpath(n+'_error.txt').write_text(str(e));return n,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for r in ex.map(get,qs):print(r)
if p.joinpath('openalex_doi.json').exists():
 j=json.loads(p.joinpath('openalex_doi.json').read_text());u='https://api.openalex.org/works?filter=cites:'+j['id']+'&per_page=100'
 with p.joinpath('LITERATURE.md').open('a',encoding='utf-8') as f:f.write(f'- OpenAlex works citing resolved source: `{u}` (2026-10-12).\n')
 print(get(('openalex_cites_resolved',u)))
