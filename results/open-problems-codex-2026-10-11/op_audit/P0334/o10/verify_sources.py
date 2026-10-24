from pathlib import Path
import concurrent.futures, requests, pymupdf, json
ROOT=Path(__file__).resolve().parent
sources={
 'bl':'https://perso.math.univ-toulouse.fr/ledoux/files/2016/12/MEMO.pdf',
 'bk':'https://arxiv.org/pdf/2502.01254',
 'source':'https://arxiv.org/pdf/2505.19104',
 'arxiv_search':'https://export.arxiv.org/api/query?search_query=all:%22quantile%20process%22&sortBy=lastUpdatedDate&sortOrder=descending&max_results=40',
 'openalex_search':'https://api.openalex.org/works?search=quantile%20process%20Lp&per-page=10',
}
def get(item):
 name,url=item
 try:
  r=requests.get(url,timeout=55)
  meta={'name':name,'url':url,'status':r.status_code}
  if r.status_code==200 and r.content.startswith(b'%PDF'):
   (ROOT/(name+'.pdf')).write_bytes(r.content)
   doc=pymupdf.open(stream=r.content,filetype='pdf')
   (ROOT/(name+'.txt')).write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
   meta['pages']=len(doc)
  else:
   (ROOT/(name+'.response.txt')).write_text(r.text,encoding='utf-8')
  return meta
 except Exception as e: return {'name':name,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
 results=list(pool.map(get,sources.items()))
(ROOT/'source_fetch_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
