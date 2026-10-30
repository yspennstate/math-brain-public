from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n{now}: Final persistence check caught CRLF-vs-LF decision hashing. Explicit LF output and one justified replay preserved all329427 assertions, n4 counts and logical hash; saved-byte hash/readback passed. Final replay runtime1.1517426s, n4 runtime1.1306401s. All24 stage artifacts below20MB.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nFor streamed certificate hashes on Windows, set newline="\\n" explicitly or hash saved bytes; default text-mode newline translation changes the persisted digest.\n')
manifest=[]
for path in ROOT.rglob('*'):
 if path.is_file() and path.name!='manifest.json':
  data=path.read_bytes();assert len(data)<20*1024*1024
  manifest.append({'path':str(path.relative_to(ROOT)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(ROOT/'out/manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'receipts_refreshed':len(manifest),'files_under_20MB':True}))
