import pathlib,subprocess,json,xml.etree.ElementTree as ET
base=pathlib.Path('~/<private-repo>/06_math_research')
out=[]
for d in list(base.glob('probability_1000_intake_*'))+[base/'codex_pool_2026_10_10']:
 if d.exists():
  r=subprocess.run(['rg','-n','--glob','*.jsonl','F0022',str(d)],capture_output=True,text=True,encoding='utf-8'); out.append(r.stdout)
pathlib.Path('prior_ledger_hits.txt').write_text('\n'.join(out),encoding='utf-8'); print('\n'.join(out)[:16000])
r=subprocess.run(['git','-C','~/math-open-problems','ls-tree','-r','--name-only','origin/master'],capture_output=True,text=True,encoding='utf-8'); hits=[x for x in r.stdout.splitlines() if 'F0022' in x]; pathlib.Path('prior_git_paths.txt').write_text('\n'.join(hits),encoding='utf-8'); print('GIT PATHS',hits[:40])
for x in hits:
 if x.endswith(('STATUS.md','ATTEMPT.md','LITERATURE.md')):
  q=subprocess.run(['git','-C','~/math-open-problems','show','origin/master:'+x],capture_output=True,text=True,encoding='utf-8'); pathlib.Path('git_'+str(hits.index(x))+'.txt').write_text(q.stdout,encoding='utf-8'); print(x,q.stdout[:6000])
t=ET.parse('arxiv.response'); ns={'a':'http://www.w3.org/2005/Atom'}
for e in t.findall('a:entry',ns): print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),e.findtext('a:summary',namespaces=ns)[:1400])
