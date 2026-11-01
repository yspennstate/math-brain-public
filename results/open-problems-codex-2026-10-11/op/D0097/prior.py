from pathlib import Path
import subprocess
root=Path('~/<private-repo>/06_math_research')
for p in list(root.glob('probability_1000_intake_*'))+[root/'codex_pool_2026_10_10']:
 if p.exists():
  r=subprocess.run(['rg','-n','D0097',str(p)],capture_output=True,text=True,encoding='utf8',errors='replace'); print(r.stdout)
r=subprocess.run(['git','-C','~/math-open-problems','ls-tree','-r','--name-only','origin/master'],capture_output=True,text=True); paths=[p for p in r.stdout.splitlines() if 'D0097' in p or 'd0097' in p];print('PUBLISHED PATHS',paths)
for p in paths:
 r=subprocess.run(['git','-C','~/math-open-problems','show','origin/master:'+p],capture_output=True,text=True,encoding='utf8',errors='replace');print(r.stdout)
