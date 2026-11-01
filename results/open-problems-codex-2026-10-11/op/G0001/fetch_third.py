import urllib.request,urllib.parse,concurrent.futures,pathlib,json
qs={
'openalex_source_direct':'https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2608.23661',
'openalex_citing':'https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:doi:10.48550/arXiv.2608.23661','per-page':20}),
'site_locality_abs':'https://arxiv.org/abs/2609.07026',
'site_counter_abs':'https://arxiv.org/abs/2608.29940',
'supercritical_abs':'https://arxiv.org/abs/2603.03257',
'crossref_recent':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'site percolation critical finite cluster Cerf','filter':'from-pub-date:2026-08-24','rows':20}),
}
def f(x):
 k,u=x
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'MathResearch/1.0'}),timeout=25) as r:d=r.read()
  pathlib.Path(k+'.txt').write_bytes(d);res={'service':k,'url':u,'bytes':len(d)}
 except Exception as e:res={'service':k,'url':u,'error':str(e)}
 with open('followup_log.jsonl','a',encoding='utf8') as out:out.write(json.dumps({'date':'2026-10-11',**res})+'\n')
 print(res,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:list(ex.map(f,qs.items()))
