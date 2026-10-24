import requests,pathlib,json,concurrent.futures,xml.etree.ElementTree as E
queries=[('arxiv_specific','https://export.arxiv.org/api/query',{'search_query':'all:percolation AND (all:"cluster density" OR all:"number of clusters" OR all:"free energy")','max_results':60}),('crossref_specific','https://api.crossref.org/works',{'query':'percolation free energy differentiability cluster density Zhang','rows':20}),('openalex_retry','https://api.openalex.org/works',{'search':'percolation cluster density','per_page':10}),('openalex_doi','https://api.openalex.org/works/https://doi.org/10.1214/11-PS186',{}),('semantic_retry','https://api.semanticscholar.org/graph/v1/paper/ARXIV:1107.0158',{'fields':'title,year,citations.title,citations.year,citations.externalIds'})]
def run(q):
 n,u,p=q
 try:
  r=requests.get(u,params=p,timeout=40);pathlib.Path(n+'.response').write_text(r.text,encoding='utf-8');return dict(service=n,url=r.url,status=r.status_code,date='2026-10-12',file=n+'.response')
 except Exception as e:return dict(service=n,url=u,params=p,error=str(e),date='2026-10-12')
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: rs=list(ex.map(run,queries))
old=json.loads(pathlib.Path('search_log.json').read_text());old+=rs;pathlib.Path('search_log.json').write_text(json.dumps(old,indent=2),encoding='utf-8')
for r in rs:print(r)
try:
 ns={'a':'http://www.w3.org/2005/Atom'};t=E.parse('arxiv_specific.response')
 for e in t.findall('a:entry',ns):print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),e.findtext('a:summary',namespaces=ns)[:1800])
except Exception as e:print(e)
try:
 for x in json.loads(pathlib.Path('crossref_specific.response').read_text())['message']['items']: print(x.get('title'),x.get('author'),x.get('DOI'),x.get('published'))
except Exception as e:print(e)
