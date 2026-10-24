import urllib.request,urllib.parse,pathlib,xml.etree.ElementTree as E,json
b=pathlib.Path(__file__).resolve().parent
queries={'arxiv_free_broad':{'search_query':'all:"free Brownian" AND (all:mode OR all:maximum OR all:location)','max_results':50,'sortBy':'lastUpdatedDate','sortOrder':'descending'},'arxiv_ho':{'id_list':'2007.06100'}}
for name,query in queries.items():
 u='https://export.arxiv.org/api/query?'+urllib.parse.urlencode(query)
 try:
  data=urllib.request.urlopen(u,timeout=45).read(); (b/(name+'.xml')).write_bytes(data)
  root=E.fromstring(data); ns={'a':'http://www.w3.org/2005/Atom'}
  out=[{'title':e.findtext('a:title',namespaces=ns),'id':e.findtext('a:id',namespaces=ns),'abstract':e.findtext('a:summary',namespaces=ns)} for e in root.findall('a:entry',ns)]
  (b/(name+'.json')).write_text(json.dumps({'url':u,'results':out},indent=2),encoding='utf8'); print(name,json.dumps(out,indent=2))
 except Exception as e: print(name,repr(e))
