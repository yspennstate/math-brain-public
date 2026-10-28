from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parents[1]; a=r.parents[1]
raw=(r/'out/LEAN_RAW.txt').read_text(encoding='utf-8-sig')
assert 'RUNTIME_UNVERIFIED' in raw
receipt={'status':'RUNTIME_UNVERIFIED','compiler_reported_seconds':123.9,
 'source_sha256':'7e323d683b65c1456a8600fb1702bcf0653f7c3b46019f96ba45d80c1fe73b32',
 'target':'example (s x y : Real) (h : x+y=2*s) : x*y <= s^2',
 'scope':'AM-GM algebra only; no named reviewed target, no compilation/proof certification, translation UNVERIFIED',
 'admission':'memok exit0: physical7.4GB free, commit17.7GB free',
 'resource_limitation':'Wrapper source inspected after launch documents typical Mathlib commit about4.1GB, exceeding packet1.5GB job target. Actual peak was not measured. No further compiler launched; original attempt completed with RUNTIME_UNVERIFIED. Future packet formal checks must use core-only or separately proven memory-bounded route.'}
(r/'out/LEAN_RECEIPT.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
p=r/'REPORT.md'; text=p.read_text(encoding='utf-8').replace('Formal rung: NOT_RUN_PENDING_ADMISSION.','Formal rung: RUNTIME_UNVERIFIED after123.9s; no formal certificate. The admitted wrapper later disclosed a typical4.1GB Mathlib commit, above the packet1.5GB target; actual peak unmeasured. No second compiler was launched; future formal checks require a memory-bounded route.')
text=text.replace('Main estimate80MB, runtime cap120s, no >300MB search.','Main estimate80MB, runtime cap120s, no >300MB search. Separate exact POSTFLIGHT controls retain the nonBoolean child-mass failure, actual parity2 ghost normalizer product35/36 and terminal mass1/2; their fixture counts are not added to MAIN.')
p.write_text(text,encoding='utf-8')
with (a/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\nStage22 final audit: formal AM-GM attempt returned RUNTIME_UNVERIFIED after123.9s, no Lean certificate. memok admitted it, but wrapper source subsequently disclosed typical Mathlib commit4.1GB above packet1.5GB target; actual peak unmeasured, no retry. Future formal checks must use memory-bounded/core route. Report and receipts updated; primary mathematics/checker unchanged.\n')
with (a/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nPacket resource lesson: memok passing does not establish a compiler fits this packet\'s1.5GB job cap. lean_check Mathlib imports document about4.1GB typical commit. Inspect resource needs BEFORE launching; use a memory-bounded/core route here. Stage22 attempt remained RUNTIME_UNVERIFIED, never a proof certificate.\n')
proto=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
claim=json.loads((r/'CLAIMS.json').read_text(encoding='utf-8'))[0]
assert set(claim)==set(proto['required_per_run']['claim_fields'])
assert hashlib.sha256(claim['exact_statement'].encode()).hexdigest()==claim['statement_sha256']
progress=json.loads((r/'PROGRESS.json').read_text(encoding='utf-8'))
assert set(progress)=={x.split(' (')[0] for x in proto['required_per_run']['progress_fields']}
assert (r/'PROGRESS.json').read_bytes()==(r/'PACKET_DELTA.json').read_bytes()
assert json.loads((r/'out/POSTFLIGHT.json').read_text(encoding='utf-8'))['status']=='PASS'
assert hashlib.sha256((r/'code/check.py').read_bytes()).hexdigest()==json.loads((r/'out/MAIN.json').read_text(encoding='utf-8'))['helper_sha256']
assert len((a/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[p for p in r.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json']
saved=[]
for p in files:
 b=p.read_bytes(); assert len(b)<20*1024**2
 saved.append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
out={'status':'PASS','exact_schema_keys':True,'statement_hash_unchanged':True,'progress_delta_identical':True,'report_readback':True,'full_FEI':'OPEN','files':saved}
(r/'out/PERSISTENCE_RECEIPT.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':'PASS','files':len(saved),'formal':'RUNTIME_UNVERIFIED','FEI':'OPEN'}))
