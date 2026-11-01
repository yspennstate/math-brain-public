from pathlib import Path
import subprocess,json
R=Path(__file__).resolve().parent
jobs=[('math_recall',['python','-X','utf8','~/.claude/dreaming/math_recall.py','continuous SOS entropic repulsion Velenik']),('memory_topic',['python','-X','utf8','~/.claude/dreaming/brain.py','recall','entropic repulsion']),('memory_mistakes',['python','-X','utf8','~/.claude/dreaming/brain.py','recall','entropic repulsion mistakes'])]
for name,args in jobs:
 try:
  x=subprocess.run(args,capture_output=True,text=True,encoding='utf8',timeout=90)
  (R/(name+'.txt')).write_text(x.stdout+'\nSTDERR\n'+x.stderr,encoding='utf8')
  print(name,x.stdout[:10000],flush=True)
 except Exception as e: print(name,repr(e),flush=True)
base=Path('~/<private-repo>/06_math_research')
matches=[]
for folder in list(base.glob('probability_1000_intake_*'))+[base/'codex_pool_2026_10_10']:
 if folder.exists():
  for file in folder.rglob('*'):
   if file.is_file() and file.suffix in ['.jsonl','.md','.json','.txt']:
    try:
     for line in file.read_text(encoding='utf8').splitlines():
      if 'F0072' in line: matches.append(str(file)+': '+line)
    except (OSError,UnicodeError): pass
(R/'prior_records.txt').write_text('\n'.join(matches),encoding='utf8')
print('Prior records', '\n'.join(matches)[:20000],flush=True)
x=subprocess.run(['git','-C','~/math-open-problems','ls-tree','-r','--name-only','origin/master'],capture_output=True,text=True,encoding='utf8',timeout=60)
paths=[p for p in x.stdout.splitlines() if 'F0072' in p]
for p in paths:
 x=subprocess.run(['git','-C','~/math-open-problems','show','origin/master:'+p],capture_output=True,text=True,encoding='utf8',timeout=60)
 matches.append('REPOSITORY '+p+'\n'+x.stdout)
(R/'prior_records.txt').write_text('\n'.join(matches),encoding='utf8')
print('Repository matching paths',paths,flush=True)
