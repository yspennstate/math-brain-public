from search import fetch,P
import json,urllib.parse,concurrent.futures
queries=[('arxiv_jacka','https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'au:Jacka AND au:Windridge','max_results':15})),('crossref_jacka','https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'Jacka Warren Windridge Boolean expected cost','rows':5})),('arxiv_uniform','https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"iterated majority"','max_results':50}))]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:results=list(ex.map(fetch,queries))
(P/'search_jacka_log.json').write_text(json.dumps(results,indent=2),encoding='utf8');print(json.dumps(results,indent=2))
import xml.etree.ElementTree as E
ns={'a':'http://www.w3.org/2005/Atom'}
for name in ['arxiv_jacka','arxiv_uniform']:
 try:
  r=E.parse(P/(name+'.json'))
  for e in r.findall('a:entry',ns):print(name,e.find('a:title',ns).text,e.find('a:id',ns).text,e.find('a:summary',ns).text)
 except Exception as e:print(repr(e))
