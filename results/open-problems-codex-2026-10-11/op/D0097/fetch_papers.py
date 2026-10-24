import requests,concurrent.futures,json,pymupdf
urls={
'afg':'https://projecteuclid.org/journals/annals-of-probability/volume-52/issue-5/The-critical-density-for-activated-random-walks-is-always-less/10.1214/23-AOP1674.pdf',
'diffusive':'https://alea.impa.br/articles/v19/19-17.pdf',
'hu':'https://arxiv.org/pdf/2203.14406',
'asymptotic':'https://arxiv.org/pdf/2512.00720'}
def f(kv):
 k,u=kv
 try:
  r=requests.get(u,timeout=80)
  with open('search_log.jsonl','a',encoding='utf8') as f:f.write(json.dumps({'date':'2026-10-12','service':'primary_pdf','url':u,'http_status':r.status_code})+'\n')
  r.raise_for_status();open(k+'.pdf','wb').write(r.content);d=pymupdf.open(k+'.pdf');s='\n'.join('PDF PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(d));open(k+'.txt','w',encoding='utf8').write(s);print(k,len(d),s[:15000],flush=True)
 except Exception as e:print(k,repr(e),flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:list(ex.map(f,urls.items()))
