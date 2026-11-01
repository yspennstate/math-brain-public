import requests,pathlib,concurrent.futures,pymupdf,json
qs={'saburov2016':'https://iopscience.iop.org/article/10.1088/1742-6596/697/1/012014/pdf','abdulghafor2016':'https://www.degruyterbrill.com/document/doi/10.1515/math-2016-0045/pdf','abdulghafor_meta':'https://api.openalex.org/works/https://doi.org/10.1515/math-2016-0045','saburov_meta':'https://api.openalex.org/works/https://doi.org/10.1088/1742-6596/697/1/012014'}
def f(k,u):
 try:
  r=requests.get(u,timeout=45); pathlib.Path(k+('.pdf' if 'meta' not in k else '.json')).write_bytes(r.content)
  if r.content.startswith(b'%PDF'):
   d=pymupdf.open(stream=r.content,filetype='pdf'); pathlib.Path(k+'.txt').write_text('\n'.join(f'\nPAGE {i+1}\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
  return k,u,r.status_code,len(r.content)
 except Exception as e:return k,u,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: out=list(ex.map(lambda kv:f(*kv),qs.items()))
pathlib.Path('papers_log.json').write_text(json.dumps(out,indent=2),encoding='utf8'); print(out)
for k in ['citing_source','citing_survey']:
 d=json.loads(pathlib.Path(k+'.txt').read_text(encoding='utf8'))
 print(k); [print(x['title'],x['publication_year'],x.get('doi'),x.get('open_access',{}).get('oa_url')) for x in d['results']]
