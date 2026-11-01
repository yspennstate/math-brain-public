import json,pathlib,urllib.request,concurrent.futures
x=json.loads(pathlib.Path('site_proof_tree.txt').read_text());paths=[y['path'] for y in x['tree'] if y['path'].startswith('docs/') or any(z in y['path'] for z in ['SiteCriticality','LatticeSite','CriticalProbability','FinalCriticality'])]
print('\n'.join(paths))
qs={
'site_manuscript_tex':'https://raw.githubusercontent.com/nitromannitol/percolation-after-anthropic/main/docs/kn-results.tex',
'site_comparator_challenge':'https://raw.githubusercontent.com/nitromannitol/percolation-after-anthropic/main/PercolationAudit/SiteCriticality/Challenge.lean',
'site_comparator_solution':'https://raw.githubusercontent.com/nitromannitol/percolation-after-anthropic/main/PercolationAudit/SiteCriticality/Solution.lean',
'site_repo_actions':'https://api.github.com/repos/nitromannitol/percolation-after-anthropic/actions/runs?per_page=5',
}
def f(x):
 k,u=x
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'MathResearch/1.0'}),timeout=30) as r:d=r.read()
  pathlib.Path(k+'.txt').write_bytes(d);res={'service':k,'url':u,'bytes':len(d)}
 except Exception as e:res={'service':k,'url':u,'error':str(e)}
 with open('followup_log.jsonl','a',encoding='utf8') as out:out.write(json.dumps({'date':'2026-10-11',**res})+'\n')
 print(res,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:list(ex.map(f,qs.items()))
