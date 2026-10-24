import subprocess,pathlib
path='proofnet24/NM13-12/runs/2026-09-18/2026-09-18T08-59-30Z__e0086-two-trap-green-upper-bound.md'
s=subprocess.run(['git','-C','~/math-open-problems','show','origin/master:'+path],capture_output=True,text=True,encoding='utf-8',check=True).stdout
start=s.find('## 3.');end=s.find('## 9.',start)
part=s[start:end];pathlib.Path('prior_two_trap_excerpt.md').write_text(part,encoding='utf-8');print(part)
