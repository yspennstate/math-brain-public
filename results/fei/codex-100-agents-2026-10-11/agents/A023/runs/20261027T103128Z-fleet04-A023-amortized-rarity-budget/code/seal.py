from pathlib import Path
import datetime as dt
import hashlib
import json

RUN=Path(__file__).resolve().parents[1]
AGENT=RUN.parents[1]
ROOT=Path('~')
PROTO=ROOT/'mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'
protocol=json.loads(PROTO.read_text(encoding='utf-8'))
prev=AGENT/'runs/20261023T144354Z-fleet03-A023-amortized-rarity-budget'
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def save(p,obj): p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
main=load(RUN/'out/validation.json'); audit=load(RUN/'out/audit.json'); lean=load(RUN/'out/lean.json')
assert main['status']==audit['status']=='PASS'
old=load(prev/'CLAIMS.json')[0]
claim={k:old[k] for k in protocol['required_per_run']['claim_fields']}
claim['version']=11
addition=(' ADDITIONAL JOINT ORIGINAL-INFLUENCE ACCOUNT: For EVERY Boolean f and finite adaptive physical restriction tree T with one prefix-free persistent first-mark antichain, every marked history uses q=(1-e)P+e*u with e=min(1/2,I/4), q=P at I=0. Against ANY normalized old reference finite on spectral support, keep full D=KL(P||q)-KL(P||r), charge D at first marking and signed realized differences thereafter. With C its expected total, Q total reach-weighted queried influence, L_M and L_U marked/unmarked terminal influence, B_M=sum firstmark reach*I_mark and Q_post query influence inside marked subtrees, C<=L_M, B_M=Q_post+L_M and Q+C<=I_root-L_U. Every actual subtree is finite with fair physical branch reaches; both terminal classes remain. The one original coefficient jointly pays query INFLUENCE and signed conversion; arbitrary physical-query KL and initial source CE are NOT included. For f_n=1-2*1{x=0}, n>=2, query x1, mark only x1=0, query x2 there and stop: Q=4*2^-n and L_M=2(n-2)*2^-n. All preceding scoped statements remain unchanged. Full FEI and arbitrary-core original source admission remain OPEN.')
claim['exact_statement']=old['exact_statement']+addition
claim['statement_sha256']=hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
claim['contributors']=old['contributors']+['A023 stage23 (fleet04 session): joint original influence account and exact audits']
claim['proof_source']={'path':str(RUN/'PROOF.md'),'validation':str(RUN/'out/validation.json'),'audit':str(RUN/'out/audit.json'),'previous_scopes':str(prev/'CLAIMS.json')}
claim['proof_dependencies']=[{'claim_id':old['claim_id'],'version':10,'scope':'previous statements retained; smoothing lemma reconstructed in new proof'}]
claim['review_records']=[]
claim['status']='AUTHOR_PROOF_EXACT_FINITE_CHECKS; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN'
claim['supersedes']=[{'claim_id':old['claim_id'],'version':10}]
claim['refutes']=[]
claim['first_unproved_line']='A noncircular original O(I) INITIAL complete reference source and any required physical-query excess beyond influence, after old invoices and both terminal laws.'
claim['next_consumers']=['A028','A029','A030','A087','A094','B05','B20']
save(RUN/'CLAIMS.json',[claim])
progress=dict(protocol_revision=protocol['revision'],run_id=RUN.name,stream='B05',packet_id='A023',
 gap_id='G-R-MISMATCH-FIRST-REVELATION',attempt_id='A023-23-joint-original-influence-query-conversion',
 method='Finite subtree influence partition, prefix-free marked ownership, full signed KL telescope; exact rational and independent physical-edge checks',
 mathematical_delta='Q+C<=I_root-L_U universally; conversion uses ONLY remaining marked terminal influence L_M, not a separate root-I coefficient. 3480 main and23615 audit checks PASS; Lean runtime unverified. Initial source and queryKL excess remain unpaid.',
 deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='AUTHOR_PROOF; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 claim_versions_used=[{'claim_id':old['claim_id'],'version':10,'source':str(prev/'PROOF.md'),'status':'self-contained smoothing reconstruction; prior scopes retained'}],
 claims_created_or_changed=[{'claim_id':old['claim_id'],'version':11}],
 source_artifacts=['REPORT.md','PROOF.md','CLAIMS.json','code/check.py','code/audit.py','code/OwnerBudget.lean','code/seal.py','out/FROZEN_SPEC.json','out/AUDIT_SPEC.json','out/validation.json','out/audit.json','out/lean.json','out/PERSISTENCE_RECEIPTS.json'],
 next_consumers=claim['next_consumers'],
 next_action='Fund a REQUIRED arbitrary-core initial complete reference and physical-query excess from SAME unused original influence, old bills and BOTH terminals retained; no further conversion-only iteration. A087/A094 audit joint account.',
 stagnant_substantive_attempts=0,
 blockers=['Full FEI and noncircular original source remain open.','QueryKL above influence has no generic payer.','Independent-person review, supervisor mirror and adoption unverified.','Brain wake attachment lock and stale identity notes; contract mutation classification unresolved; reversible local writes only.','Lean arithmetic check RUNTIME_UNVERIFIED, no certificate.'],packet_ids=['A023'])
save(RUN/'PROGRESS.json',progress)
(RUN/'PACKET_DELTA.json').write_bytes((RUN/'PROGRESS.json').read_bytes())
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
keys=[k.split(' (')[0] for k in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(keys)
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
status=('STATE: A023 stage23 saved: ONE original I pays all query influence plus full signed first-mark conversion, refund unmarked terminal I; 3480+23615 exact checks PASS; review/FEI OPEN; Lean runtime unverified.\n'
 'NEXT: Fund REQUIRED arbitrary-core INITIAL complete reference and queryKL excess from SAME unused original influence after old bills/BOTH terminals; no further conversion-only iteration; A087/A094 review.\n')
(AGENT/'STATUS.md').write_text(status,encoding='utf-8')
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
stamp=dt.datetime.now(dt.timezone.utc).isoformat()
entry=('\n'+stamp+' stage23: reconstructed v10 smoothing and derived exact joint-account Q+C<=I_root-L_U via marked antichain subtree partition. Main3480 and independent physical-edge23615 exact checks PASS (7870 policies). Four guard failures retained; point-defect2 queryKL=1>queryI=1/2. Lean initial saved-byte hash mismatch launched nothing; corrected-byte retry RUNTIME_UNVERIFIED, no certificate. Initial source remains unpaid; next targets required source/query excess. All outputs local; no external writes or publication.\n')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f: f.write(entry)
lesson=('\n2026-10-27 stage23: For every finite adapted physical tree and persistent prefix-free first mark, Iroot=Qpre+Bmark+Lunmarked, Bmark=Qpost+Lmarked. With full signed current-vs-supplied-old KL conversion C<=Lmarked, ONE original coefficient pays Q+C<=Iroot-Lunmarked. This sharpens separate C<=Iroot without funding initial CE or queryKL excess. QueryKL need not be <=query influence: actual point-defect2 has1 vs1/2. Discarding negative conversion increments fails on point-defect3 at a complete constant frontier (positive first mark, signed total0); renewed parity2 grants3 against original I2; normalized old law is necessary. Main exact3480/audit23615 assertions PASS; independent-person review pending; Lean runtime unverified. Source digests must hash saved bytes (Windows newline conversion changed the first Lean hash). Next: initial source and REQUIRED full query invoices, not another conversion theorem.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f: f.write(lesson)
sources=[PROTO,prev/'PROOF.md',ROOT/'brain_workers/FEI100_20261011/BOARD.md',ROOT/'brain_workers/FEI100_20261011/claude/B05/STREAM_NOTES.md']
source_dir=ROOT/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
sources.extend(source_dir/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md','sources/ERASURE_REDUCTION.md','sources/LOG_ALLOCATION_CURATED.md'])
sources.extend((ROOT/'brain_workers/FEI100_20261011/context').glob('*.txt'))
files=[p for p in RUN.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']
assert all(p.stat().st_size<20_000_000 for p in files)
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
assert all(('# '+k) in report for k in protocol['required_per_run']['report_fields'])
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
receipt=dict(saved_at_utc=stamp,status='LOCAL_SCHEMA_AND_HASH_CHECKS_PASS',
 source_hashes={str(p):sha(p) for p in sources},
 artifact_hashes={str(p.relative_to(RUN)):sha(p) for p in files},
 rolling_hashes={p.name:sha(p) for p in [AGENT/'STATUS.md',AGENT/'WORKLOG.md',AGENT/'LEARNED.md']},
 schema_fields_exact=True,compatibility_bytes_equal=True,status_lines=2,
 full_FEI='OPEN',independent_person_review='PENDING',mirror='UNVERIFIED',lean='RUNTIME_UNVERIFIED')
save(RUN/'out/PERSISTENCE_RECEIPTS.json',receipt)
print(json.dumps({'status':receipt['status'],'artifacts':len(files),'claim_version':11,'main_checks':main['counts']['assertions'],'audit_checks':audit['assertions'],'lean':receipt['lean']}))
