import requests,pathlib,json,concurrent.futures
qs=[('openalex_citing','https://api.openalex.org/works',{'filter':'cites:doi:10.1214/11-PS186','per-page':50}),('crossref_zhang','https://api.crossref.org/works',{'query.title':'A singularity at the criticality for the free energy in percolation','rows':3}),('crossref_ziff','https://api.crossref.org/works',{'query.title':'Universal features of cluster numbers in percolation','rows':3})]
def f(x):
 n,u,p=x
 try:
  r=requests.get(u,params=p,timeout=35);pathlib.Path(n+'.response').write_text(r.text,encoding='utf-8');return dict(service=n,url=r.url,status=r.status_code,date='2026-10-12',file=n+'.response')
 except Exception as e:return dict(service=n,url=u,params=p,error=str(e),date='2026-10-12')
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:rs=list(ex.map(f,qs))
a=json.loads(pathlib.Path('search_log.json').read_text());a+=rs;pathlib.Path('search_log.json').write_text(json.dumps(a,indent=2),encoding='utf-8');print(rs)
for n in ['crossref_zhang','crossref_ziff']:
 try:
  for x in json.loads(pathlib.Path(n+'.response').read_text())['message']['items']:print(x.get('title'),x.get('DOI'),x.get('author'),x.get('published'),x.get('container-title'),x.get('volume'),x.get('page'))
 except Exception as e:print(e)
