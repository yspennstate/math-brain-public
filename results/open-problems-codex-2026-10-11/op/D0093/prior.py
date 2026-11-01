import pathlib,subprocess,json
base=pathlib.Path('~/<private-repo>/06_math_research')
for folder in list(base.glob('probability_1000_intake_*'))+[base/'codex_pool_2026_10_10']:
 for p in folder.rglob('*.jsonl'):
  for line in p.open(encoding='utf8',errors='replace'):
   if 'D0093' in line: print(str(p),line[:9000])
r=subprocess.run(['git','-C','~/math-open-problems','ls-tree','-r','--name-only','origin/master'],capture_output=True,text=True,encoding='utf8')
paths=[s for s in r.stdout.splitlines() if 'D0093' in s.upper()]; print('REPO PATHS',paths[:40]);pathlib.Path('repo_paths.json').write_text(json.dumps(paths),encoding='utf8')
