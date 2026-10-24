from pathlib import Path
import json
p=Path('.')
f=p/'search_log_5.json'
if f.exists():
 d=json.loads(f.read_text());rs={x[0]:x[1:] for x in d['results']}
 with (p/'LITERATURE.md').open('a',encoding='utf8') as out:
  out.write('\n\n## Final exact-ID lookup request\n\n')
  for k,u in d['queries'].items():out.write(f'- {d["date"]}: {k}: `{u}`; result {rs.get(k)}.\n')
  out.write('\nThe source-ID lookup was rate-limited, so no verified OpenAlex citing-source request could be constructed. The successful Semantic Scholar citations request remains the actual source-citation screen.\n')
print('Files present:',', '.join(x.name for x in p.glob('*.md')))
print('Lean output currently:',(p/'lean_check.txt').read_text(encoding='utf8')[:700])
