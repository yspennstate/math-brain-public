import requests,json,pathlib,concurrent.futures,datetime
queries=[('arxiv','https://export.arxiv.org/api/query',{'search_query':'all:"Boltzmann" AND (all:"transience" OR all:"random walk")','max_results':40}),('openalex','https://api.openalex.org/works',{'search':'Boltzmann maps random walk transience','per-page':30}),('openalex_source','https://api.openalex.org/works',{'search':'Peeling random planar maps','per-page':8}),('crossref','https://api.crossref.org/works',{'query':'Boltzmann maps transience random walk','rows':25}),('semantic','https://api.semanticscholar.org/graph/v1/paper/search',{'query':'Boltzmann maps transience','limit':30,'fields':'title,authors,year,abstract,url,externalIds'}),('github','https://api.github.com/search/repositories',{'q':'Boltzmann maps transience','per_page':20})]
def run(t):
 name,url,params=t
 try:
  r=requests.get(url,params=params,timeout=45,headers={'User-Agent':'C0059-mathematical-research/1.0'}); pathlib.Path('search_'+name+'.txt').write_text(r.text,encoding='utf8')
  with pathlib.Path('LITERATURE.md').open('a',encoding='utf8') as f:f.write('\n- 2026-10-12 '+name+': '+r.url+'; HTTP '+str(r.status_code)+'; raw: search_'+name+'.txt\n')
  if name=='arxiv':
   import xml.etree.ElementTree as ET
   root=ET.fromstring(r.text);ns={'a':'http://www.w3.org/2005/Atom'};return name,[(e.findtext('a:title',namespaces=ns),e.findtext('a:id',namespaces=ns),e.findtext('a:summary',namespaces=ns)) for e in root.findall('a:entry',ns)]
  j=r.json()
  if name.startswith('openalex'):return name,[(x['id'],x['title'],x.get('publication_year'),x.get('doi')) for x in j.get('results',[])]
  if name=='crossref':return name,[(x.get('title'),x.get('DOI')) for x in j.get('message',{}).get('items',[])]
  if name=='semantic':return name,j
  return name,[(x['full_name'],x.get('description')) for x in j.get('items',[])]
 except Exception as e:return name,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 for res in ex.map(run,queries):print(json.dumps(res,ensure_ascii=False))
