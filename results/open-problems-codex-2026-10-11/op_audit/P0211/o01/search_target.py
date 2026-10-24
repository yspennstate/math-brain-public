import urllib.request, urllib.parse, pathlib, json, concurrent.futures, xml.etree.ElementTree as E
ROOT=pathlib.Path(__file__).resolve().parent
qs=[('arxiv_math.xml','(cat:math.PR OR cat:math-ph) AND all:"coagulation" AND (all:"fragmentation" OR all:"relaxation" OR all:"mixing")'),('arxiv_polymer.xml','all:"polymer" AND (all:"coagulation" OR all:"fragmentation")')]
def fetch(pair):
 name,q=pair
 url='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':q,'max_results':60})
 try:
  with urllib.request.urlopen(url,timeout=40) as resp: data=resp.read()
  (ROOT/name).write_bytes(data)
  ns={'a':'http://www.w3.org/2005/Atom'}
  entries=[{'id':e.find('a:id',ns).text,'title':e.find('a:title',ns).text,'abstract':e.find('a:summary',ns).text} for e in E.fromstring(data).findall('a:entry',ns)]
  return {'file':name,'url':url,'entries':entries}
 except Exception as e: return {'file':name,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex: results=list(ex.map(fetch,qs))
(ROOT/'target_search.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
for r in results:
 print(r['file'],r.get('error','OK'))
 for e in r.get('entries',[]): print(e['id'],e['title'].replace('\n',' '),e['abstract'].replace('\n',' ')[:650])
