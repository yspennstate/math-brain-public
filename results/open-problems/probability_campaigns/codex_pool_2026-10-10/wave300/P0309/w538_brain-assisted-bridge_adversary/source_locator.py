import pathlib,json,sqlite3
w=pathlib.Path('~/brain_workers/w538')
p=pathlib.Path('~/math-brain-inbox/claude-probability-1000-continue-0907/bundle_010.json')
if p.is_file():
 d=json.loads(p.read_text(encoding='utf-8-sig'))
 rows=[r for r in d.get('entries',[]) if r.get('key')=='op-p0309']
 (w/'p0309_exact_intake.json').write_text(json.dumps({'path':str(p),'entries':rows},ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps(rows,ensure_ascii=False))
else: print('Intake draft locator unavailable:',p)
print('w537 named proof artifacts:')
pair=pathlib.Path('~/brain_workers/w537')
print([p.name for p in pair.iterdir() if p.is_file()] if pair.is_dir() else 'folder absent')
print('canonical math brain candidate paths:')
for base in [pathlib.Path('~'),pathlib.Path('~/<private-repo>/06_math_research')]:
 print([str(p) for p in base.glob('*math*brain*') if p.is_dir()])
