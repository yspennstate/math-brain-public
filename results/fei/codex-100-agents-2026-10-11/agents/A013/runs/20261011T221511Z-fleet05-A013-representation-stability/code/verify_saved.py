from pathlib import Path
import hashlib,json,datetime
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1]
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n'+datetime.datetime.now(datetime.timezone.utc).isoformat()+' — Late B03 lead v1 consumed: all three queue helper expectations fail pointwise restriction monotonicity on the exact r=10 two-gate activation; physical child weight 1/1024 retained. Same-selector multiplexer d=1..4 ledger checked, 147 further assertions in 0.001505s, total 52,513. NEXT is averaged queue transport retaining actual child probabilities and root normalizers.\n')
report=RUN/'REPORT.md';s=report.read_text(encoding='utf-8')
s=s.replace('NEXT is the shortest route toward full FEI because it directly removes the live A011/A012 bottleneck in a valid full reference and probes the next unpaid overlap term rather than treating rare activation as a new easy class.','NEXT is the shortest route toward full FEI because the explicit pointwise counterexample identifies the actual rare-child weight that an averaged queue transport must retain, while the full projected activation repair demonstrates how to erase latent labels without hiding the core cost. This joins C020 to a nonreusing physical stopping-tree ledger rather than asserting another isolated class admission.')
report.write_text(s,encoding='utf-8')
claim=json.loads((RUN/'CLAIMS.json').read_text(encoding='utf-8'))[0]
assert claim['proof_source']['sha256']==hashlib.sha256((RUN/'COVER_STABILITY.tex').read_bytes()).hexdigest()
assert claim['statement_sha256']==hashlib.sha256(claim['exact_statement'].encode()).hexdigest()
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
for p in RUN.rglob('*.json'):json.loads(p.read_text(encoding='utf-8'))
receipts={'saved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'local_schema_check':'PASS','claim_count':1,'files':[],'remote_mirror':'not performed; supervisor-owned'}
for p in RUN.rglob('*'):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
  assert p.stat().st_size<20*1024*1024
  receipts['files'].append({'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(RUN/'out/PERSISTENCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
assert len((ROOT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
print('Final proof/statement hashes, JSON, identical deltas, artifact sizes, receipts and two-line status: PASS')
