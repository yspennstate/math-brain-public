import requests,pathlib,concurrent.futures,xml.etree.ElementTree as E,json
jobs=[('arxiv_maps','https://export.arxiv.org/api/query',{'search_query':'ti:Boltzmann AND ti:maps','max_results':100,'sortBy':'submittedDate','sortOrder':'descending'}),('arxiv_dual','https://export.arxiv.org/api/query',{'search_query':'all:"dual" AND all:"planar maps"','max_results':80,'sortBy':'submittedDate','sortOrder':'descending'}),('crossref_book','https://api.crossref.org/works',{'query.bibliographic':'Nicolas Curien Peeling Random Planar Maps','rows':5}),('semantic_book','https://api.semanticscholar.org/graph/v1/paper/search',{'query':'Peeling random planar maps','limit':5,'fields':'title,authors,year,externalIds'}),('oa_citing','https://api.openalex.org/works',{'filter':'cites:https://doi.org/10.1007/978-3-031-36854-7','per-page':50})]
def run(t):
 name,u,p=t
 try:
  r=requests.get(u,params=p,timeout=40);pathlib.Path('search_'+name+'.txt').write_text(r.text,encoding='utf8')
  with open('LITERATURE.md','a',encoding='utf8') as f:f.write('\n- 2026-10-12 '+name+': '+r.url+' HTTP '+str(r.status_code)+' raw search_'+name+'.txt\n')
  if name.startswith('arxiv'):
   ns={'a':'http://www.w3.org/2005/Atom'};return name,[(e.findtext('a:title',namespaces=ns),e.findtext('a:id',namespaces=ns)) for e in E.fromstring(r.text).findall('a:entry',ns)]
  if name.startswith('cross'):return name,[(x.get('title'),x.get('DOI')) for x in r.json().get('message',{}).get('items',[])]
  return name,r.json()
 except Exception as e:return name,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 for r in ex.map(run,jobs):print(json.dumps(r,ensure_ascii=False))
