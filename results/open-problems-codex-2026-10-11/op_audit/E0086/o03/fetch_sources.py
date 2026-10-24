import requests, pathlib, json, concurrent.futures, xml.etree.ElementTree as ET
from pypdf import PdfReader
root=pathlib.Path.cwd()
urls={
'source':'https://arxiv.org/pdf/1606.03787',
'covered':'https://arxiv.org/pdf/math/0503139',
'arxiv_search':'https://export.arxiv.org/api/query?search_query=all:%22random%20walk%22%20AND%20(all:%22generalized%20boundary%22%20OR%20all:%22favorite%20sites%22)&max_results=25&sortBy=submittedDate&sortOrder=descending',
'openalex':'https://api.openalex.org/works?search=random%20walk%20moving%20boundary%20local%20time&per_page=10',
'book':'https://www.math.uchicago.edu/~lawler/srwbook.pdf'}
def get(k,u):
 try:
  r=requests.get(u,timeout=70); r.raise_for_status()
  ext='pdf' if k in ['source','covered','book'] else 'txt'
  (root/(k+'.'+ext)).write_bytes(r.content)
  if ext=='pdf':
   reader=PdfReader(root/(k+'.pdf'))
   text='\n'.join('PDF PAGE '+str(i+1)+'\n'+p.extract_text() for i,p in enumerate(reader.pages))
   (root/(k+'.txt')).write_text(text,encoding='utf8')
   print(k, 'pages',len(reader.pages),flush=True)
  else: print(k,r.status_code,len(r.content),flush=True)
  return {'key':k,'url':u,'status':r.status_code,'bytes':len(r.content)}
 except Exception as e:
  print(k,str(e),flush=True); return {'key':k,'url':u,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
 records=list(pool.map(lambda kv:get(*kv),urls.items()))
(root/'fetch_log.json').write_text(json.dumps(records,indent=2),encoding='utf8')
