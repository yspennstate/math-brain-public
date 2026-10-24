from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request, urllib.parse, json
import pymupdf
ROOT=Path(__file__).resolve().parent
jobs={
 'source':'https://arxiv.org/pdf/0801.3306',
 'pegden':'https://arxiv.org/pdf/1105.0111',
 'random':'https://arxiv.org/pdf/1909.07849',
 'search_arxiv':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:sandpile AND (all:polygon OR all:holes OR all:corner)','max_results':35,'sortBy':'relevance'}),
 'search_openalex':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'sandpile holes polygon limiting shape','per-page':15}),
}
def fetch(item):
 name,url=item
 try:
  with urllib.request.urlopen(url,timeout=45) as r: data=r.read(); status=r.status
  (ROOT/(name+('.pdf' if name in ['source','pegden','random'] else '.txt'))).write_bytes(data)
  if name in ['source','pegden','random']:
   doc=pymupdf.open(stream=data,filetype='pdf')
   pages=[p.get_text() for p in doc]
   (ROOT/(name+'.txt')).write_text('\n'.join('PAGE '+str(i+1)+'\n'+p for i,p in enumerate(pages)),encoding='utf-8')
   needles={'source':['Question 6.2','Theorem 6.3','Theorem 6.1'],'pegden':['Theorem 4.2','Theorem 1.1'],'random':['Theorem 9.2','ηmin','stationary']}[name]
   for i,p in enumerate(pages):
    if any(n in p for n in needles): print(name,'PAGE',i+1,p,flush=True)
  elif name=='search_arxiv':
   import xml.etree.ElementTree as ET
   tree=ET.fromstring(data); ns={'a':'http://www.w3.org/2005/Atom'}
   print([(e.find('a:id',ns).text,e.find('a:title',ns).text) for e in tree.findall('a:entry',ns)],flush=True)
  else: print(name,data[:400],flush=True)
  return {'name':name,'url':url,'status':status,'bytes':len(data)}
 except Exception as e: return {'name':name,'url':url,'error':str(e)}
with ThreadPoolExecutor(max_workers=5) as ex: results=list(ex.map(fetch,jobs.items()))
(ROOT/'fetch_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(results,flush=True)
