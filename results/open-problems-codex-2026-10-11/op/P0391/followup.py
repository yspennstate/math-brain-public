import pathlib,json,urllib.request,concurrent.futures,xml.etree.ElementTree as ET
root=pathlib.Path(__file__).resolve().parent
queries={
'openalex_doi':'https://api.openalex.org/works/https://doi.org/10.1007/s11134-022-09746-x',
'openalex_citing':'https://api.openalex.org/works?filter=cites:doi:10.1007/s11134-022-09746-x&per-page=100',
'semantic_retry':'https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s11134-022-09746-x/citations?fields=title,year,externalIds&limit=100',
'arxiv_broad':'https://export.arxiv.org/api/query?search_query=all:%22symmetric%20queue%22%20OR%20(all:%22service%20disciplines%22%20AND%20all:%22heavy%20traffic%22)&max_results=50',
'crossref_fr alix'.replace(' ',''):'https://api.crossref.org/works?query.title=Time-dependent%20properties%20of%20symmetric%20queues&rows=3'}
def get(pair):
 name,url=pair
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Research-check/1.0'}),timeout=40) as f: data=f.read()
  (root/(name+'.txt')).write_bytes(data)
  return dict(service=name,query=url,date='2026-10-11',result='saved',bytes=len(data))
 except Exception as e:return dict(service=name,query=url,date='2026-10-11',result=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: res=list(ex.map(get,queries.items()))
(root/'followup_log.json').write_text(json.dumps(res,indent=2),encoding='utf-8')
print(json.dumps(res,indent=2))
base=pathlib.Path('~/<private-repo>/06_math_research')
matches=[]
for directory in list(base.glob('probability_1000_intake_*'))+[base/'codex_pool_2026_10_10']:
 for file in directory.rglob('*.jsonl'):
  try:
   for line in file.read_text(encoding='utf-8').splitlines():
    if 'P0391' in line:matches.append(str(file)+'\n'+line)
  except (OSError,UnicodeError):pass
(root/'prior_records.txt').write_text('\n'.join(matches),encoding='utf-8')
print('PRIOR RECORDS\n'+'\n'.join(matches)[:22000])
