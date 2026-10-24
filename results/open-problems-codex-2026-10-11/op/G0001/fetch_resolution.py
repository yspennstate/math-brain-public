import urllib.request,concurrent.futures,pathlib,json
qs={
'bourabee_home':'https://nitromannitol.github.io/',
'site_proof_page':'https://nitromannitol.github.io/site-percolation-7d3f2/',
'site_proof_repo':'https://api.github.com/repos/nitromannitol/percolation-after-anthropic',
'site_proof_readme':'https://raw.githubusercontent.com/nitromannitol/percolation-after-anthropic/main/README.md',
'site_proof_final':'https://raw.githubusercontent.com/nitromannitol/percolation-after-anthropic/main/Hypergraph/FinalCriticality.lean',
'site_proof_verify':'https://raw.githubusercontent.com/nitromannitol/percolation-after-anthropic/main/VERIFICATION.md',
'site_proof_tree':'https://api.github.com/repos/nitromannitol/percolation-after-anthropic/git/trees/main?recursive=1',
}
def f(x):
 k,u=x
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'MathResearch/1.0'}),timeout=35) as r:d=r.read()
  pathlib.Path(k+'.txt').write_bytes(d);res={'service':k,'url':u,'bytes':len(d)}
 except Exception as e:res={'service':k,'url':u,'error':str(e)}
 with open('followup_log.jsonl','a',encoding='utf8') as out:out.write(json.dumps({'date':'2026-10-11',**res})+'\n')
 print(res,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:list(ex.map(f,qs.items()))
