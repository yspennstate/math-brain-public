from pathlib import Path
import requests, pymupdf, json, concurrent.futures, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parent
jobs=[('source','https://arxiv.org/pdf/1606.03787'),('covered','https://arxiv.org/pdf/math/0503139'),('kernel','https://www.math.uchicago.edu/~lawler/srwbook.pdf'),('arxiv_search','https://export.arxiv.org/api/query?search_query=au:Okada+AND+(all:boundary+OR+all:favorite)&max_results=30&sortBy=submittedDate&sortOrder=descending'),('openalex_search','https://api.openalex.org/works?search=random%20walk%20moving%20boundary%20local%20time%20Okada&per_page=10')]
def fetch(job):
 name,url=job
 try:
  r=requests.get(url,timeout=50)
  record={'name':name,'url':url,'status':r.status_code,'bytes':len(r.content)}
  if r.ok:
   if name in ['source','covered','kernel']:
    (ROOT/(name+'.pdf')).write_bytes(r.content)
    doc=pymupdf.open(stream=r.content,filetype='pdf')
    (ROOT/(name+'.txt')).write_text('\n'.join('PDF PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
   else:
    (ROOT/(name+'.txt')).write_text(r.text,encoding='utf8')
    if name=='arxiv_search':
     ns={'a':'http://www.w3.org/2005/Atom'}
     record['entries']=[{'title':e.findtext('a:title',namespaces=ns),'id':e.findtext('a:id',namespaces=ns),'summary':e.findtext('a:summary',namespaces=ns)} for e in ET.fromstring(r.text).findall('a:entry',ns)]
    elif name=='openalex_search':
     record['entries']=[{'title':x.get('title'),'doi':x.get('doi')} for x in r.json().get('results',[])]
  return record
 except Exception as e:return {'name':name,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: results=list(pool.map(fetch,jobs))
(ROOT/'fetch_log.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(results,ensure_ascii=False,indent=2))
