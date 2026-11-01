import requests, pathlib, json, concurrent.futures
items={
 'diffusions_2021_pdf':'https://arxiv.org/pdf/2107.06163',
 'concentration_2023_pdf':'https://arxiv.org/pdf/2310.03471',
 'oa_further':'https://api.openalex.org/works?search=%22Further%20study%20on%20Hunt%22&per-page=20',
 'oa_newresults':'https://api.openalex.org/works?search=%22New%20results%20on%20Hunt%22&per-page=20',
 'crossref_filtered':'https://api.crossref.org/works?query.bibliographic=Hunt%20hypothesis%20Levy%20Getoor&rows=100',
 'semantic_retry':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1908.06825?fields=title,year,citations.title,citations.year,citations.externalIds',
}
def fetch(pair):
 name,url=pair
 try:
  r=requests.get(url,timeout=50)
  ext='.pdf' if name.endswith('_pdf') else '.json'
  pathlib.Path(name+ext).write_bytes(r.content)
  if ext=='.pdf' and r.status_code==200:
   import pymupdf
   doc=pymupdf.open(stream=r.content,filetype='pdf')
   pathlib.Path(name+'.txt').write_text('\n'.join('PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
  out={'name':name,'url':url,'date':'2026-10-12','status':r.status_code,'bytes':len(r.content)}
 except Exception as e: out={'name':name,'url':url,'error':str(e)}
 print(json.dumps(out),flush=True); return out
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as p: results=list(p.map(fetch,items.items()))
pathlib.Path('leads_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
