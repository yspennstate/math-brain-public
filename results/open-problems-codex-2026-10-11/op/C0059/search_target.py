import requests,pathlib,concurrent.futures,json,xml.etree.ElementTree as E
jobs=[('arxiv_target','https://export.arxiv.org/api/query',{'search_query':'all:"planar" AND all:"transience"','max_results':60,'sortBy':'submittedDate','sortOrder':'descending'}),('arxiv_cauchy','https://export.arxiv.org/api/query',{'search_query':'all:"Cauchy" AND all:"maps"','max_results':30,'sortBy':'submittedDate','sortOrder':'descending'}),('oa_retry','https://api.openalex.org/works',{'search':'Peeling random planar maps','per_page':5}),('crossref_target','https://api.crossref.org/works',{'query.title':'Boltzmann planar maps','rows':30}),('semantic_target','https://api.semanticscholar.org/graph/v1/paper/search',{'query':'"planar maps" "transience"','limit':30,'fields':'title,authors,year,abstract,externalIds'})]
def run(t):
 name,url,p=t
 try:
  r=requests.get(url,params=p,timeout=45);pathlib.Path('search_'+name+'.txt').write_text(r.text,encoding='utf8');
  with open('LITERATURE.md','a',encoding='utf8') as f:f.write('\n- 2026-10-12 '+name+': '+r.url+' HTTP '+str(r.status_code)+' raw search_'+name+'.txt\n')
  if name.startswith('arxiv'):
   ns={'a':'http://www.w3.org/2005/Atom'};return name,[(e.findtext('a:title',namespaces=ns),e.findtext('a:id',namespaces=ns)) for e in E.fromstring(r.text).findall('a:entry',ns)]
  j=r.json()
  if name.startswith('oa'):return name,j if 'results' not in j else [(x['id'],x['title'],x.get('doi'),x.get('cited_by_count')) for x in j['results']]
  if name.startswith('cross'):return name,[(x.get('title'),x.get('DOI')) for x in j.get('message',{}).get('items',[])]
  return name,[(x['title'],x.get('externalIds')) for x in j.get('data',[])] if 'data' in j else j
 except Exception as e:return name,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 for r in ex.map(run,jobs):print(json.dumps(r,ensure_ascii=False))
