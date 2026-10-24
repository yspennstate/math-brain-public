from pathlib import Path
import hashlib,json,datetime,subprocess
ROOT=Path(__file__).resolve().parents[1]
HOME=Path('~')
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
# This boundary was identified during the proof audit, after the primary run.
spec={'helper_version':'A082-boundary-v1','family':'a=1,b=0,r=1 negative-cell edit','domain':'one fixed Boolean truth table and its source','case_count':1,'symmetry':'none','arithmetic':'exact Fraction and power-of-two logs','memory_estimate_mb':60,'max_runtime_seconds':10}
dump(ROOT/'out/BOUNDARY_SPEC.json',spec)
import check as C
f=C.truth(1,0,1);P=C.spectrum(f);Pg=C.spectrum(C.source(1,0))
B=C.sub(C.ent(P),C.ent(C.marginal(P,0)))
Bg=C.sub(C.ent(Pg),C.ent(C.marginal(Pg,0)))
assert B==(1,1) and Bg==(0,0)
dump(ROOT/'out/BOUNDARY.json',{'status':'PASS','truth_table':f,'edited_erasure':1,'source_erasure':0,'conclusion':'a>=2 erasure hypothesis is essential; final active query needs separate point-law reset'})
source=HOME/'brain_workers/FEI100_20261011/agents/A096/runs/20261021T210221Z-account03-A096-live-gap-ledger/CLAIMS.json'
claims=json.loads(source.read_text(encoding='utf-8-sig'))
assert len(claims)==1
cl=claims[0]
observed=hashlib.sha256(cl['exact_statement'].encode('utf-8')).hexdigest()
assert observed==cl['statement_sha256']
cl['review_records'].append({'reviewer':'A082','timestamp':now,'verdict':'INDEPENDENT_SCOPED_RECONSTRUCTION_HOLDS','method':'Analytic reconstruction of scalar endpoint/SOS certificate and envelope induction; independent direct-character, physical-edge, rational-log implementation','substantive_repair_contributed':False,'scope':'Exact unchanged source statement, retaining A097 complete-floor premise and original source price; no independent acceptance of entire A097 dependency','evidence':['REVIEW.md','code/check.py','out/CHECK.json','out/BOUNDARY.json'],'source_file_sha256':digest(source)})
cl['status']='INDEPENDENT_SCOPED_RECONSTRUCTION_HOLDS_BASELINE_FLOOR_RETAINED'
dump(ROOT/'CLAIMS.json',claims)
protocol=json.loads((HOME/'mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=ROOT.name,stream='B17',packet_id='A082',gap_id='G-R-MISMATCH-C024-PRESCRIBED-RESET',attempt_id='A082-stage17-independent-active-reset',method='Independent scalar rational/SOS certificate, physical spectral replay and all-tree analytic induction',mathematical_delta='A096 canonical active-reset theorem independently holds at unchanged rate 2C0+10 with complete off-cell cost; 24 roots/228 resets/26553 assertions PASS, 507 scalar fixtures and exact a=1 countercheck. Universal FEI remains OPEN.',deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='SCOPED_INDEPENDENT_ACCEPTANCE_FULL_FEI_OPEN',claim_versions_used=[dict(claim_id=cl['claim_id'],version=cl['version'],statement_sha256=observed)]+cl['proof_dependencies'],claims_created_or_changed=[dict(claim_id=cl['claim_id'],version=cl['version'],change='A082 independent acceptance record; source statement unchanged')],source_artifacts=['REPORT.md','REVIEW.md','CLAIMS.json','code/check.py','out/CHECK.json','out/FROZEN_SPEC.json','out/SOURCE_RECEIPTS.json','out/BOUNDARY.json','out/FORMAL_RECEIPT.json'],next_consumers=['A096','A097','A094','A085','A081','A090','B20'],next_action='Pay one dummy-data/control query and prescribed reset after a spent active prefix from SAME original remaining envelope, retaining old debit and both complete terminals.',stagnant_substantive_attempts=0,blockers=['Arbitrary source-reference construction and non-active/interleaved reset payment remain unproved; supervisor adoption/mirror/second review unverified.'],packet_ids=['A082'])
expected=protocol['required_per_run']['progress_fields'];expected=[x.split(' (')[0] for x in expected]
assert set(progress)==set(expected)
assert set(cl)==set(protocol['required_per_run']['claim_fields'])
dump(ROOT/'PROGRESS.json',progress);dump(ROOT/'PACKET_DELTA.json',progress)
lean=(ROOT/'out/LEAN.txt').read_text(encoding='utf-8') if (ROOT/'out/LEAN.txt').exists() else 'No Lean compilation attempted: admission blocked.'
print('FORMAL RESULT',lean[:4000])
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
report=report.replace('Formal-check admission and any resulting narrow Lean receipt are recorded separately in out/MEMOK.txt, out/FORMAL_RECEIPT.json and out/LEAN.txt when present. Compilation is never used as a certificate for the full theorem.','Formal-check admission and its narrow polynomial-identity attempt are recorded in out/MEMOK.txt, out/FORMAL_RECEIPT.json and out/LEAN.txt. The helper exits 2; no Lean certificate is claimed. The full theorem is an analytic proof conditional on the baseline floor, with exact finite validation. The supplemental one-table boundary check proves B_j(F)=1>B_j(g)=0 at a=1, justifying the separate final rule.')
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
base=ROOT.parents[1]
(base/'STATUS.md').write_text('STATE: Stage17 complete: A096 active-reset theorem independently HOLDS at unchanged rate18; 26553 exact assertions and a1 boundary PASS; full FEI OPEN.\nNEXT: A096/A097 pay one non-active query/reset after spent active history from SAME remaining source envelope; retain both terminals; A094/A085 review.\n',encoding='utf-8')
with (base/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+now+': Stage17 independently reconstructed A096 canonical active-reset theorem unchanged, keeping A097 floor premise. Direct character/Fraction replay:24 roots,156 active-prefix nodes,228 reset calls,16 positive complementary debts,507 scalar fixtures,26553 assertions PASS in5.393s. Exact a1 boundary refutes extending erasure comparison. Scalar endpoint and SOS argument, not finite sampling, cover unbounded parameter/reference domain. Lean helper exits2; no formal certificate. Full FEI OPEN.\n')
with (base/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n'+now+': Active canonical reset payment can retain the same 2C0+10 ancestor quota. Arbitrary source profiles reduce exactly to v=R({j}) in the constant-sibling likelihood, whose worst endpoint obeys qmax>=27/52 by a rational SOS certificate; hence signed complementary excess<18e. Envelope surcharge releases10e and half that sibling excess costs<9e, leaving>=e. The a>=2 erasure comparison fails at a1 (edited erasure1, source0); final explicit point-law reset is essential. Active-only geometry does not pay non-active/interleaved reset or construct an arbitrary cheap root reference.\n')
receipts=[]
for p in ROOT.rglob('*'):
 if p.is_file() and p.name!='RECEIPTS.json':
  assert p.stat().st_size<20_000_000
  receipts.append(dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=digest(p)))
dump(ROOT/'out/RECEIPTS.json',dict(at=now,files=receipts,remote_mirror_verified=False))
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert len((base/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert report.rstrip().split('\n\n')[-1].startswith('C024 history transfer')
print('FINALIZED',len(receipts),'files; exact protocol schemas and hashes PASS; statement hash',observed)
