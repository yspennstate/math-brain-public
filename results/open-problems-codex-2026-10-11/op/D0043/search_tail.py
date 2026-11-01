from pathlib import Path
import urllib.request,urllib.parse,xml.etree.ElementTree as E,json,concurrent.futures
r=Path(__file__).resolve().parent
qs={
'arxiv_nonregular':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'(cat:math.PR OR cat:math-ph) AND (all:nonregular OR all:"higher-order") AND (all:tridiagonal OR all:"stochastic Airy")','max_results':40,'sortBy':'submittedDate','sortOrder':'descending'}),
'arxiv_exotic_math':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'cat:math.PR AND all:exotic AND all:operator','max_results':30}),
'crossref_tail':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query.bibliographic':'exotic stochastic edge operator higher order tail','rows':10}),
}
ns={'a':'http://www.w3.org/2005/Atom'}
def get(pair):
 name,url=pair
 try:
  with urllib.request.urlopen(url,timeout=30) as x:data=x.read(12000000)
  (r/(name+('.xml' if name.startswith('arxiv') else '.json'))).write_bytes(data)
  result=f'{len(data)} bytes'
  if name.startswith('arxiv'):
   for e in E.fromstring(data).findall('a:entry',ns):
    print(name,e.find('a:id',ns).text,e.find('a:title',ns).text,e.find('a:published',ns).text,flush=True)
    print(e.find('a:summary',ns).text,flush=True)
  else:
   for e in json.loads(data)['message']['items']:print(name,e.get('title'),e.get('DOI'),flush=True)
 except Exception as e:result=str(e)
 return {'date':'2026-10-12','service':name,'url':url,'result':result}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as p:results=list(p.map(get,qs.items()))
(r/'tail_search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
with (r/'LITERATURE.md').open('a',encoding='utf8') as f:
 f.write('\n## Final targeted status/novelty search\n\n')
 for x in results:f.write(f"- {x['date']}: {x['service']}: {x['url']} — {x['result']}\n")
