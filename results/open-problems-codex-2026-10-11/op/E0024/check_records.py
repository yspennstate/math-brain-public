import pathlib,subprocess,json
base=pathlib.Path('~/<private-repo>/06_math_research')
out=[]
for folder in list(base.glob('probability_1000_intake_*'))+[base/'codex_pool_2026_10_10']:
 for f in folder.rglob('*.jsonl'):
  if f.name not in ['problems.jsonl','attempts.jsonl','sources.jsonl']:continue
  with f.open(encoding='utf8',errors='replace') as h:
   for line in h:
    if 'E0024' in line:out.append({'file':str(f),'record':line.strip()})
pathlib.Path('earlier_records.json').write_text(json.dumps(out,indent=2),encoding='utf8')
for r in out: print(r['file'],r['record'][:3000])
p=subprocess.run(['git','-C','~/math-open-problems','ls-tree','-r','--name-only','origin/master'],capture_output=True,text=True,encoding='utf8')
paths=[v for v in p.stdout.splitlines() if 'e0024' in v.lower() or 'hunt' in v.lower()]
pathlib.Path('published_paths.txt').write_text('\n'.join(paths),encoding='utf8');print('Relevant repo paths:',paths[:40])
s=pathlib.Path('source.txt').read_text(encoding='utf8')
for i in [19,20,25,26,27]:print(s.split('=== PDF PAGE ')[i])
