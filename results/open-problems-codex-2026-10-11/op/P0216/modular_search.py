import urllib.request,urllib.parse,pathlib,concurrent.futures,json,xml.etree.ElementTree as ET
R=pathlib.Path(__file__).resolve().parent
queries={
 'arxiv_modular':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"permutation graphs" AND all:"modular decomposition"')+'&max_results=20',
 'arxiv_substitution':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"simple permutations" AND all:"substitution decomposition"')+'&max_results=15',
 'crossref_gallai':'https://api.crossref.org/works?query='+urllib.parse.quote('Gallai transitiv orientierbare Graphen')+'&rows=5',
 'arxiv_orient':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"transitive orientations" AND all:"prime"')+'&max_results=15',
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'MathResearch/1.0'})
  data=urllib.request.urlopen(req,timeout=40).read();(R/(name+'.raw')).write_bytes(data)
  return {'name':name,'url':url,'status':'ok','bytes':len(data)}
 except Exception as e:return {'name':name,'url':url,'status':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:log=list(pool.map(fetch,queries.items()))
(R/'modular_search_log.json').write_text(json.dumps(log,indent=2),encoding='utf8')
for x in log:print(json.dumps(x))
ns={'a':'http://www.w3.org/2005/Atom'}
for name in ['arxiv_modular','arxiv_substitution','arxiv_orient']:
 p=R/(name+'.raw')
 if p.exists():
  root=ET.fromstring(p.read_bytes())
  for e in root.findall('a:entry',ns):print(name,e.findtext('a:id',namespaces=ns),' '.join(e.findtext('a:title',namespaces=ns).split()),' '.join(e.findtext('a:summary',namespaces=ns).split())[:1500])
