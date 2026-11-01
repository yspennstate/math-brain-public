from pathlib import Path
import subprocess
repo='~/math-open-problems'
r=subprocess.run(['git','-C',repo,'ls-tree','-r','--name-only','origin/master'],capture_output=True,text=True,encoding='utf-8')
hits=[x for x in r.stdout.splitlines() if 'p0286' in x.lower()]
Path('previous_paths.txt').write_text('\n'.join(hits),encoding='utf-8')
for i,path in enumerate(hits[:12]):
 rr=subprocess.run(['git','-C',repo,'show','origin/master:'+path],capture_output=True)
 Path('prior_repo_'+str(i)+'.txt').write_bytes(rr.stdout)
print('Case-insensitive P0286 paths:',hits)
root=Path('~/<private-repo>/06_math_research')
print('Intake directories:',[str(p) for p in root.glob('probability_1000_intake_*')])
