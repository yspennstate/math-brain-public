from pathlib import Path
import urllib.request, urllib.parse, json
P=Path(__file__).resolve().parent
queries=[('arxiv_cancelation_random','https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('(all:"cancelation" OR all:"cancellation" OR all:"conjugation-invariant") AND (all:"drift" OR all:"random")')+'&max_results=40'),('crossref_norm','https://api.crossref.org/works?query.title='+urllib.parse.quote('cancelation norm random walks biinvariant metrics')+'&rows=15')]
log=[]
for name,url in queries:
 try:
  data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'E0072 research'}),timeout=35).read()
  (P/(name+'.txt')).write_bytes(data)
  log.append([name,url,'OK',len(data)])
 except Exception as e:log.append([name,url,'ERROR',str(e)])
(P/'extra_search_log.json').write_text(json.dumps(log,indent=2),encoding='utf-8')
print(json.dumps(log),flush=True)
import xml.etree.ElementTree as E
try:
 root=E.fromstring((P/'arxiv_cancelation_random.txt').read_text()); ns={'a':'http://www.w3.org/2005/Atom'}
 print([(e.findtext('a:title',namespaces=ns),e.findtext('a:id',namespaces=ns),e.findtext('a:summary',namespaces=ns)) for e in root.findall('a:entry',ns)],flush=True)
except Exception as e:print(str(e))
