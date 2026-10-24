import pathlib,subprocess
root=pathlib.Path('~/<private-repo>/06_math_research')
for d in list(root.glob('probability_1000_intake_*'))+[root/'codex_pool_2026_10_10']:
 r=subprocess.run(['rg','-n','--glob','*.jsonl','D0047',str(d)],capture_output=True,text=True,encoding='utf8',errors='replace'); print(r.stdout[:14000])
r=subprocess.run(['git','-C','~/math-open-problems','ls-tree','-r','--name-only','origin/master'],capture_output=True,text=True,encoding='utf8',errors='replace'); matches=[x for x in r.stdout.splitlines() if any(w in x.lower() for w in ['d0047','carousel','virag'])];print('\n'.join(matches[:40])); pathlib.Path('prior_paths.txt').write_text('\n'.join(matches),encoding='utf8')
