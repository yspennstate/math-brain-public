from pathlib import Path
import subprocess,json
base=Path('~/<private-repo>/06_math_research')
roots=list(base.glob('probability_1000_intake_*'))+[base/'codex_pool_2026_10_10']
for root in roots:
 r=subprocess.run(['rg','-n','-l','--glob','*.jsonl','G0008',str(root)],capture_output=True,text=True,encoding='utf8')
 print('ROOT',root,'MATCHES',r.stdout[:4000])
 for file in r.stdout.splitlines():
  for line in Path(file).read_text(encoding='utf8').splitlines():
   if 'G0008' in line: print(file,line[:6000])
r=subprocess.run(['git','-C','~/math-open-problems','ls-tree','-r','--name-only','origin/master'],capture_output=True,text=True,encoding='utf8')
files=[s for s in r.stdout.splitlines() if 'G0008' in s]
Path('prior_paths.txt').write_text('\n'.join(files),encoding='utf8');print('GIT MATCHES',files[:40])
