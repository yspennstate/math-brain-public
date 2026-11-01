import pathlib,json,subprocess
R=pathlib.Path(__file__).resolve().parent
base=pathlib.Path('~/<private-repo>/06_math_research')
records=[]
for d in list(base.glob('probability_1000_intake_*'))+[base/'codex_pool_2026_10_10']:
 for name in ['problems.jsonl','attempts.jsonl','sources.jsonl']:
  for p in d.rglob(name):
   with p.open(encoding='utf8') as f:
    for line in f:
     if 'P0216' in line:
      try:x=json.loads(line)
      except ValueError:continue
      records.append({'file':str(p),'record':x})
(R/'prior_records.json').write_text(json.dumps(records,indent=2,ensure_ascii=False),encoding='utf8')
print('Prior rows',len(records))
for rec in records:
 x=rec['record'];print(rec['file'],json.dumps(x,ensure_ascii=False)[:2500])
p=subprocess.run(['git','-C','~/math-open-problems','ls-tree','-r','--name-only','origin/master'],capture_output=True,text=True,timeout=60)
paths=[x for x in p.stdout.splitlines() if 'P0216' in x or 'p0216' in x]
print('matching git paths',paths)
for path in paths[:5]:
 p=subprocess.run(['git','-C','~/math-open-problems','show','origin/master:'+path],capture_output=True,text=True,encoding='utf8',timeout=60)
 (R/('prior_git_'+str(paths.index(path))+'.txt')).write_text(p.stdout,encoding='utf8')
 print(path,p.stdout[:3000])
