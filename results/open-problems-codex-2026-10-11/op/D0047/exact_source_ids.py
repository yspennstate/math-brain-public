import pathlib,urllib.request,json
p=pathlib.Path('.')
u='https://api.semanticscholar.org/graph/v1/paper/ARXIV:1804.06953?fields=title,externalIds,citationCount'
qs={'semantic_source_ids':u};rs=[]
try:
 b=urllib.request.urlopen(u,timeout=30).read();(p/'semantic_source_ids.json').write_bytes(b);d=json.loads(b);print(d);rs.append(['semantic_source_ids','OK'])
 mag=d.get('externalIds',{}).get('MAG')
 if mag:
  v='https://api.openalex.org/works?filter=cites:W'+str(mag)+'&per-page=100';qs['openalex_verified_source_citing']=v
  try:
   b=urllib.request.urlopen(v,timeout=30).read();(p/'openalex_verified_source_citing.json').write_bytes(b);rs.append(['openalex_verified_source_citing','OK'])
  except Exception as e:rs.append(['openalex_verified_source_citing',str(e)])
except Exception as e:rs.append(['semantic_source_ids',str(e)])
(p/'search_log_5.json').write_text(json.dumps({'date':'2026-10-12','queries':qs,'results':rs},indent=2));print(rs)
