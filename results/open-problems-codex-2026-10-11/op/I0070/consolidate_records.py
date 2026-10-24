from pathlib import Path
import json
R=Path(__file__).parent
logs=[]
for name in ['search_log.json','search_more_log.json','followup_log.json','curl_followup_log.json']:
 p=R/name
 if p.exists():
  for x in json.loads(p.read_text(encoding='utf8')):
   logs.append((name,x))
lines=['\n## Exact machine-recorded request ledger\n','Each entry below was run on 2026-10-12. Raw responses remain in the folder.\n']
for name,x in logs:
 url=x.get('url',x.get('query'))
 if url:
  lines.append(f"- {x.get('service')}: `{url}`; outcome: {x.get('status',x.get('http_status',x.get('exit','failed')))}; bytes: {x.get('bytes','unknown')}." + (f" Error: {x['error']}" if 'error' in x else ''))
 if 'citation_search' in x:
  c=x['citation_search'];lines.append(f"- OpenAlex citing works: `{c['url']}`; HTTP {c['status']}; bytes {c['bytes']}.")
p=R/'LITERATURE.md'
s=p.read_text(encoding='utf8')
marker='\n## Exact machine-recorded request ledger\n'
if marker in s:s=s.split(marker)[0]
p.write_text(s+'\n'.join(lines)+'\n',encoding='utf8')
claims=[json.loads(x) for x in (R/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines() if x.strip()]
print('Validated claims:',len(claims))
print('Recorded request entries:',sum(bool(x.get('url',x.get('query'))) for _,x in logs))
print('Files:',[(p.name,p.stat().st_size) for p in R.iterdir() if p.is_file() and p.suffix in ['.md','.lean','.jsonl']])
