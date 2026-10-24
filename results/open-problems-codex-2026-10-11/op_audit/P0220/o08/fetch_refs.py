from pathlib import Path
import concurrent.futures, requests, json, xml.etree.ElementTree as ET
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parent
urls={
 'aldous.html':'https://www.stat.berkeley.edu/~aldous/Research/OP/left_Hamm.html',
 'notes1993.pdf':'https://www.stat.berkeley.edu/~aldous/Research/OP/patience.pdf',
 'borodin_rains.pdf':'https://arxiv.org/pdf/math-ph/0409059',
 'arxiv.xml':'https://export.arxiv.org/api/query?search_query=all%3AHammersley%20AND%20%28all%3Adrift%20OR%20all%3Astationary%20OR%20all%3Aleftmost%29&max_results=30',
 'openalex.json':'https://api.openalex.org/works?search=Hammersley%20drift%20stationary&per-page=20',
 'crossref.json':'https://api.crossref.org/works?query=Hammersley%20Plancherel%20joint%20stationary%20drift&rows=15',
}
def fetch(pair):
 name,url=pair
 try:
  r=requests.get(url,timeout=55)
  (ROOT/name).write_bytes(r.content)
  result={'file':name,'url':url,'status':r.status_code,'bytes':len(r.content)}
  if r.ok and name.endswith('.pdf'):
   reader=PdfReader(ROOT/name)
   (ROOT/name.replace('.pdf','.txt')).write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.extract_text() for i,p in enumerate(reader.pages)),encoding='utf-8')
  if r.ok and name=='arxiv.xml':
   ns={'a':'http://www.w3.org/2005/Atom'}
   result['records']=[{'title':e.findtext('a:title',namespaces=ns),'id':e.findtext('a:id',namespaces=ns),'summary':e.findtext('a:summary',namespaces=ns)} for e in ET.fromstring(r.content).findall('a:entry',ns)]
  if r.ok and name=='openalex.json':
   result['records']=[{'title':e['title'],'doi':e.get('doi'),'year':e.get('publication_year')} for e in r.json()['results']]
  if r.ok and name=='crossref.json':
   result['records']=[{'title':e.get('title'),'doi':e.get('DOI')} for e in r.json()['message']['items']]
  return result
 except Exception as e:return {'file':name,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
 results=list(pool.map(fetch,urls.items()))
(ROOT/'literature_fetch.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
for r in results:
 print(json.dumps(r,ensure_ascii=False))
