from pathlib import Path
import hashlib,json
from datetime import datetime,timezone
RUN=Path(__file__).resolve().parents[1];OWN=RUN.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
report=(RUN/'REPORT.md').read_text()
sentence='Here H_k=eta((1-delta)^2)+(2^(k+1)-1)delta^2(2k); its main term is<4delta by -(1-epsilon)ln(1-epsilon)<=epsilon and ln2>1/2, and its small terms sum to<4kdelta. Physical edges give the displayed influence. '
report=report.replace(sentence+sentence,sentence)
report=report.replace('no proof result changed. Jobs expected','no proof result changed. The first persistence attempt used a raw-text source hash comparison; inspection of A020 code/persist.py line12 established its compact sorted statement-and-hypotheses JSON convention, which then verified exactly. out/SOURCE_HASH_BINDING.json records both conventions; no source hash or statement was altered. Jobs expected')
(RUN/'REPORT.md').write_text(report,encoding='utf8')
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text())
progress=json.loads((RUN/'PROGRESS.json').read_text());claims=json.loads((RUN/'CLAIMS.json').read_text())
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
for c in claims:assert set(c)==set(protocol['required_per_run']['claim_fields'])
assert hashlib.sha256(claims[1]['exact_statement'].encode()).hexdigest()==claims[1]['statement_sha256']
assert hashlib.sha256(json.dumps(dict(statement=claims[0]['exact_statement'],hypotheses=claims[0]['hypotheses']),sort_keys=True,separators=(',',':')).encode()).hexdigest()==claims[0]['statement_sha256']
assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
assert report.rsplit('\n## ',1)[1].startswith('Universal bridge\n')
assert len((OWN/'STATUS.md').read_text().splitlines())==2
receipt=json.loads((RUN/'out/PERSISTENCE.json').read_text());receipt['artifacts']=[]
for p in sorted(RUN.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  assert p.stat().st_size<20_000_000
  if p.suffix=='.json':json.loads(p.read_text())
  receipt['artifacts'].append({'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)})
receipt['final_audit_at_utc']=datetime.now(timezone.utc).isoformat();receipt['source_canonical_hash']='PASS';receipt['own_raw_statement_hash']='PASS'
(RUN/'out/PERSISTENCE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
print(json.dumps({'schema':'PASS','source_canonical_hash':'PASS','own_claim_hash':'PASS','artifacts':len(receipt['artifacts']),'final_assertions':receipt['total_final_exact_assertions'],'full_FEI':'OPEN'}))
