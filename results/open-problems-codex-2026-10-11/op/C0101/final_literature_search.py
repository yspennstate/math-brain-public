import requests,json,concurrent.futures
from pathlib import Path
R=Path(__file__).parent
jobs=[
 ('openalex_correct_source','https://api.openalex.org/works/https://doi.org/10.1090/bull/1573',{}),
 ('openalex_citing_source','https://api.openalex.org/works',{'filter':'cites:https://doi.org/10.1090/bull/1573','per-page':100}),
 ('semantic_citing_lps','https://api.semanticscholar.org/graph/v1/paper/ARXIV:1309.3267/citations',{'limit':100,'fields':'title,year,authors,externalIds,abstract'}),
 ('arxiv_superharmonic_dimension','https://export.arxiv.org/api/query',{'search_query':'all:superharmonic AND (all:sandpile OR all:"integer-valued") AND (all:dimension OR all:matrices)','max_results':80}),
 ('f_lattice_retry','https://arxiv.org/pdf/2110.07556v2',{})]
def run(job):
 name,url,params=job;rec={'date':'2026-10-12','service':name,'url':url,'query':params}
 try:
  res=requests.get(url,params=params,timeout=40);rec.update(status=res.status_code,request_url=res.url)
  if name=='f_lattice_retry' and res.status_code==200:
   import pymupdf
   (R/'f_lattice.pdf').write_bytes(res.content);doc=pymupdf.open(stream=res.content,filetype='pdf')
   (R/'f_lattice.txt').write_text('\n'.join('PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
  else:(R/(name+'.txt')).write_text(res.text,encoding='utf-8')
  print(name,res.status_code,flush=True)
 except Exception as e:rec['error']=str(e)
 return rec
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as p:out=list(p.map(run,jobs))
(R/'final_search_log.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
with (R/'LITERATURE.md').open('a',encoding='utf-8') as f:
 f.write('\n## Final follow-up searches, 2026-10-12\n')
 for x in out:f.write('- '+json.dumps(x)+'\n')
