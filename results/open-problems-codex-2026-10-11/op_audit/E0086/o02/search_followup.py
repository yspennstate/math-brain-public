from pathlib import Path
ROOT=Path(__file__).resolve().parent
import concurrent.futures,json
jobs=[('focused_arxiv','https://export.arxiv.org/api/query?search_query=all:%22random%20walk%22+AND+(all:%22favorite%20sites%22+OR+all:%22generalized%20boundary%22)&max_results=30&sortBy=submittedDate&sortOrder=descending'),('favorite2024','https://arxiv.org/pdf/2409.00995'),('crossref_original','https://api.crossref.org/works?query.title=Thick%20points%20for%20planar%20Brownian%20motion%20and%20the%20Erdos%20Taylor%20conjecture%20on%20random%20walk&rows=3')]
def run(job):
 import requests,pymupdf,xml.etree.ElementTree as ET
 name,url=job
 try:
  r=requests.get(url,timeout=45); rec={'name':name,'url':url,'status':r.status_code}
  if r.ok:
   if name=='favorite2024':
    (ROOT/(name+'.pdf')).write_bytes(r.content); doc=pymupdf.open(stream=r.content,filetype='pdf')
    (ROOT/(name+'.txt')).write_text('\n'.join('PDF PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
   else:
    (ROOT/(name+'.txt')).write_text(r.text,encoding='utf8')
    if name=='focused_arxiv':
     ns={'a':'http://www.w3.org/2005/Atom'}
     entries=[{'title':e.findtext('a:title',namespaces=ns),'id':e.findtext('a:id',namespaces=ns),'summary':e.findtext('a:summary',namespaces=ns)} for e in ET.fromstring(r.text).findall('a:entry',ns)]
     rec['entries']=entries
    else:rec['entries']=[{'title':x.get('title'),'doi':x.get('DOI'),'links':x.get('link')} for x in r.json()['message']['items']]
  return rec
 except Exception as e:return {'name':name,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as p: results=list(p.map(run,jobs))
(ROOT/'followup_log.json').write_text(json.dumps(results,indent=2,ensure_ascii=False),encoding='utf8')
for r in results:
 print(r['name'],r.get('status',r.get('error')))
 for x in r.get('entries',[]):print(x.get('id',x.get('doi')),x['title'],x.get('links',''))
