import pathlib,urllib.request,urllib.parse,json,concurrent.futures
R=pathlib.Path(__file__).parent
jobs=[('crossref_source','https://api.crossref.org/works/10.1214/11-PS183'),('crossref_title','https://api.crossref.org/works?'+urllib.parse.urlencode({'query.title':'Spectrum of non-Hermitian heavy tailed random matrices','rows':10})),('crossref_as_title','https://api.crossref.org/works?'+urllib.parse.urlencode({'query.bibliographic':'almost sure convergence heavy tailed circular law random matrices','rows':20}))]
def go(x):
 name,url=x
 try:
  with urllib.request.urlopen(url,timeout=40) as f:b=f.read()
  (R/(name+'.json')).write_bytes(b)
  d=json.loads(b)['message'];items=[d] if 'items' not in d else d['items']
  for e in items:print(name,e.get('title'),e.get('DOI'),e.get('container-title'),e.get('volume'),e.get('page'),flush=True)
  status='OK'
 except Exception as e:status=str(e)
 return {'url':url,'date':'2026-10-11','status':status}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:log=list(ex.map(go,jobs))
(R/'bibliography_log.json').write_text(json.dumps(log,indent=2),encoding='utf8')
