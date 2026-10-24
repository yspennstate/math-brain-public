import urllib.request, urllib.parse, concurrent.futures, pathlib, json, xml.etree.ElementTree as ET
BASE=pathlib.Path(__file__).resolve().parent
urls={
 'published.pdf':'https://alea.math.cnrs.fr/articles/v15/15-15.pdf',
 'arxiv.xml':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:unimodality AND all:Brownian','max_results':50,'sortBy':'lastUpdatedDate','sortOrder':'descending'}),
 'arxiv_modes.xml':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"mode" AND all:"free Brownian"','max_results':30}),
 'openalex.json':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Brownian mode location unimodality','per_page':30}),
}
def fetch(k,u):
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'Independent-mathematical-audit/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  (BASE/k).write_bytes(data)
  if k.endswith('.xml'):
   root=ET.fromstring(data); ns={'a':'http://www.w3.org/2005/Atom'}
   entries=[{'title':e.findtext('a:title',namespaces=ns),'id':e.findtext('a:id',namespaces=ns),'abstract':e.findtext('a:summary',namespaces=ns)} for e in root.findall('a:entry',ns)]
   return {'url':u,'file':k,'entries':entries}
  if k.endswith('.json'):
   obj=json.loads(data)
   return {'url':u,'file':k,'works':[{'title':w['title'],'doi':w.get('doi'),'id':w['id']} for w in obj.get('results',[])]}
  return {'url':u,'file':k,'bytes':len(data)}
 except Exception as e: return {'url':u,'file':k,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: results=list(ex.map(lambda kv:fetch(*kv),urls.items()))
(BASE/'source_search_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
for r in results:
 print(r['file'],r.get('error',r.get('bytes','OK')))
 for e in r.get('entries',[]): print(e['id'],e['title'].replace('\n',' '))
 for e in r.get('works',[]): print(e['title'],e['doi'])
try:
 import pymupdf
 doc=pymupdf.open(BASE/'published.pdf')
 text='\n'.join(f'PDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc))
 (BASE/'published.txt').write_text(text,encoding='utf8')
 for needle in ['Problem 4.6','Theorem 4.3','(2.9)','(2.14)','Proposition 3.4']:
  start=text.find(needle); print('\nEXCERPT',needle,'\n',text[max(0,start-250):start+2100])
except Exception as e: print('PDF extraction:',repr(e))
