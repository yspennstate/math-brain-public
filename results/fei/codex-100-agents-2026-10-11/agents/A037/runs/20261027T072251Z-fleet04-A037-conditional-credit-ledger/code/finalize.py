from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parents[1];own=r.parents[1]
for name in ['PROGRESS.json','PACKET_DELTA.json']:
 p=r/name;d=json.loads(p.read_text(encoding='utf-8'))
 d['blockers']=[s.replace('Full ordered-pair n3 census exceeded55s; reduced domain explicitly frozen before rerun','BOTH full and reduced n3 prime-log domains exceeded55s; only n<=2 main is complete, independent rational-product audit completed all n<=3 tables') for s in d['blockers']]
 p.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
for name in ['WORKLOG.md','LEARNED.md']:
 with (own/name).open('a',encoding='utf-8') as f:f.write('\n2026-10-27 stage22 final coverage: BOTH n3 prime-log attempts timed out55s. Main COMPLETE is272 references on20 tables n<=2 (25601 assertions); independent multiplicative audit COMPLETE is552 full trees on276 tables n<=3 (149649 assertions). The reduced4112-reference spec is an unfinished domain, not a completed certificate. Do not retry prime factorization; use rational likelihood products for this ledger.\n')
receipt=r/'out/RECEIPTS.json';d=json.loads(receipt.read_text(encoding='utf-8'));manifest=[]
for p in sorted(r.rglob('*')):
 if p.is_file() and p!=receipt:
  raw=p.read_bytes();assert len(raw)<20*1024*1024;manifest.append({'path':str(p.relative_to(r)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
d['files']=manifest;receipt.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
assert (r/'PROGRESS.json').read_bytes()==(r/'PACKET_DELTA.json').read_bytes()
assert len((own/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
print('Final coverage and receipts verified:',len(manifest),'files; FEI OPEN')
