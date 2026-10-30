from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
# The first assembly stopped only because source statement hashes use a
# different documented convention. Preserve source hash; remove duplicate
# exact stage lines appended by the successful assembly retry.
for name,marker in (('WORKLOG.md','2026-10-14 03:26 UTC stage4:'),('LEARNED.md','2026-10-14 stage4: for shared-phase point surgery')):
 p=AGENT/name;lines=p.read_text(encoding='utf8').splitlines(keepends=True);seen=set();out=[]
 for line in lines:
  if line.startswith(marker):
   if line in seen:continue
   seen.add(line)
  out.append(line)
 p.write_text(''.join(out),encoding='utf8')
(ROOT/'out'/'HASH_CONVENTIONS.json').write_text(json.dumps(dict(source_claim_hash='SHA256(canonical compact sorted JSON of statement+hypotheses), independently checked; unchanged source hash preserved',new_claim_hash='SHA256(exact statement UTF-8)',first_assembly='local schema assertion repaired for source hash convention; mathematical assertions unchanged'),indent=2),encoding='utf8')
files=[p for p in ROOT.rglob('*') if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json']+[AGENT/n for n in ('STATUS.md','WORKLOG.md','LEARNED.md')]
assert all(p.stat().st_size<20*1024**2 for p in files)
receipts=dict(local_only=True,mirror_verified=False,new_claim_review='PENDING',artifacts=[dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in files])
(ROOT/'out'/'ARTIFACT_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf8')
assert all(hashlib.sha256(Path(r['path']).read_bytes()).hexdigest()==r['sha256'] for r in receipts['artifacts'])
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
print(json.dumps(dict(persistence='PASS',artifacts=len(files),progress_delta='IDENTICAL',rolling_status_lines=2,full_FEI='OPEN')))
