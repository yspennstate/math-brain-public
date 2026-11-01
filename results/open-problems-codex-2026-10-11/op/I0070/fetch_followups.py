import requests,subprocess,pathlib,json,concurrent.futures
R=pathlib.Path(__file__).parent
Q={
 'recent_abstracts':'https://export.arxiv.org/api/query?id_list=2607.13341,2602.00895,2608.20266,2608.21014,2606.07417,2609.24789',
 'rough_data':'https://arxiv.org/pdf/2607.13341',
 'critical_perturbations':'https://arxiv.org/pdf/2602.00895',
 'cahn_hilliard':'https://arxiv.org/pdf/2608.21014',
}
def fetch(it):
 k,url=it
 try:
  r=requests.get(url,timeout=40);(R/(k+('.pdf' if '/pdf/' in url else '.xml'))).write_bytes(r.content)
  result={'service':'arxiv','query':url,'date':'2026-10-12','status':r.status_code,'bytes':len(r.content)}
  if r.content.startswith(b'%PDF'):
   import pymupdf
   d=pymupdf.open(stream=r.content,filetype='pdf');(R/(k+'.txt')).write_text('\n'.join(f'\nPAGE {i+1}\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
 except Exception as e:result={'service':'arxiv','query':url,'date':'2026-10-12','error':str(e)}
 return result
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:log=list(ex.map(fetch,Q.items()))
for k,url in [('openalex_curl','https://api.openalex.org/works/https://doi.org/10.1007/s00030-025-01090-2'),('github_curl','https://api.github.com/search/repositories?q=Agresti+Veraar+regularity')]:
 try:
  p=subprocess.run(['curl.exe','-L','--max-time','40','-sS',url],capture_output=True,timeout=50)
  (R/(k+'.json')).write_bytes(p.stdout);log.append({'service':k,'query':url,'date':'2026-10-12','exit':p.returncode,'bytes':len(p.stdout),'stderr':p.stderr.decode(errors='replace')[:500]})
  if k=='openalex_curl' and p.returncode==0:
   try:
    wid=json.loads(p.stdout)['id'].split('/')[-1]
    cu=f'https://api.openalex.org/works?filter=cites:{wid}&per-page=100'
    cp=subprocess.run(['curl.exe','-L','--max-time','40','-sS',cu],capture_output=True,timeout=50)
    (R/'openalex_citing_curl.json').write_bytes(cp.stdout);log.append({'service':'openalex_citations','query':cu,'date':'2026-10-12','exit':cp.returncode,'bytes':len(cp.stdout),'stderr':cp.stderr.decode(errors='replace')[:500]})
   except Exception as e:log.append({'service':'openalex_citations','error':str(e),'date':'2026-10-12'})
 except Exception as e:log.append({'service':k,'query':url,'date':'2026-10-12','error':str(e)})
(R/'followup_log.json').write_text(json.dumps(log,indent=2),encoding='utf8')
print(json.dumps(log,indent=2))
