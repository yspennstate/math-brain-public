import urllib.request,urllib.parse,concurrent.futures,json,pathlib,xml.etree.ElementTree as E
qs={'local_clt':'all:"random regular" AND (all:"local statistics" OR all:"central limit")','peeling':'all:"k-core" AND (all:"critical" OR all:"peeling")','dependency':'ti:"A central limit theorem by differential calculus"','simple':'ti:"The probability that a random multigraph is simple"'}
def f(k,q):
 u='https://export.arxiv.org/api/query?search_query='+urllib.parse.quote(q)+'&max_results=20'
 try:
  b=urllib.request.urlopen(u,timeout=40).read();pathlib.Path('second_'+k+'.xml').write_bytes(b);r=E.fromstring(b);ns={'a':'http://www.w3.org/2005/Atom'}
  print(k,[(x.find('a:id',ns).text,x.find('a:title',ns).text) for x in r.findall('a:entry',ns)])
  return [k,q,u,'OK']
 except Exception as e:return[k,q,u,str(e)]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:r=list(ex.map(lambda kv:f(*kv),qs.items()))
pathlib.Path('second_search_log.json').write_text(json.dumps(r,indent=2),encoding='utf8')
