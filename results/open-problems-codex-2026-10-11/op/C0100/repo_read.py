from pathlib import Path
import subprocess
p=subprocess.run(['git','-C','~/math-open-problems','ls-tree','-r','--name-only','origin/master'],capture_output=True,text=True,encoding='utf8')
paths=[x for x in p.stdout.splitlines() if 'C0100' in x or 'c0100' in x];print('\n'.join(paths[:50]));Path('repository_paths.txt').write_text('\n'.join(paths),encoding='utf8')
for x in paths[:8]:
 r=subprocess.run(['git','-C','~/math-open-problems','show','origin/master:'+x],capture_output=True,text=True,encoding='utf8');print('\nPATH',x,'\n',r.stdout[:5000])
