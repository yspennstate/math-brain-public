import requests, pathlib, json, concurrent.futures, xml.etree.ElementTree as E
urls={
'arxiv_boundary':'https://export.arxiv.org/api/query?search_query=au:Okada%20AND%20(all:boundary%20OR%20all:annulus)&max_results=30&sortBy=submittedDate&sortOrder=descending',
'arxiv_covered':'https://export.arxiv.org/api/query?search_query=all:%22random%20walk%22%20AND%20all:%22covered%20disc%22&max_results=15&sortBy=submittedDate&sortOrder=descending',
'crossref_thick':'https://api.crossref.org/works?query.title=Thick%20points%20for%20planar%20Brownian%20motion%20and%20the%20Erdos%20Taylor%20conjecture%20on%20random%20walk&rows=3'}
def fetch(k,u):
 try:
  r=requests.get(u,timeout=40);r.raise_for_status();pathlib.Path(k+'.txt').write_text(r.text,encoding='utf8')
  if k.startswith('arxiv'):
   ns={'a':'http://www.w3.org/2005/Atom'};root=E.fromstring(r.text)
   print(k,[(e.find('a:id',ns).text,e.find('a:title',ns).text) for e in root.findall('a:entry',ns)],flush=True)
  else:
   print(k,[(i.get('title'),i.get('DOI'),i.get('link')) for i in r.json()['message']['items']],flush=True)
  return {'key':k,'url':u,'status':r.status_code}
 except Exception as e: print(k,str(e),flush=True);return {'key':k,'url':u,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool: results=list(pool.map(lambda kv:fetch(*kv),urls.items()))
pathlib.Path('additional_fetch_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
