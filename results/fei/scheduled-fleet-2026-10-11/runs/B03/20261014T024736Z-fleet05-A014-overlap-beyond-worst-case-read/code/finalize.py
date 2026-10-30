from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,data):(R/name).write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
check=json.loads((R/'out/check.json').read_text());pilot=json.loads((R/'out/pilot.json').read_text())
assert check['stats']['cases']==6561 and check['helper']=='A014-shared-blocker-v1.2'
assert check['elapsed_seconds']<300 and pilot['elapsed_seconds']<60
receipt=(f"Pilot PASS: {pilot['assertions']:,} assertions, {pilot['elapsed_seconds']:.6f} seconds. "
         f"Full PASS: {check['assertions']:,} assertions, {check['elapsed_seconds']:.6f} seconds. "
         f"Full census includes {check['stats']['nonzero_blockers']:,} nonzero blockers, "
         f"{check['stats']['zero_blockers']} constant-zero blockers, "
         f"{check['stats']['positive_private_monotone_cases']} positive-private monotone combinations, "
         f"and {check['stats']['nontrivial_shared_bit']:,} functions with positive shared influence.")
report=R/'REPORT.md';report.write_text(report.read_text(encoding='utf-8').replace('VALIDATION_RECEIPT_PENDING',receipt),encoding='utf-8')
previous=A/'runs/20261013T235200Z-fleet05-A014-overlap-beyond-worst-case-read/CLAIMS.json'
old=json.loads(previous.read_text(encoding='utf-8'))[0]
addition=(' For any finite disjoint private cubes Y,Z and Boolean indicators h1<=h0,k1<=k0, '
 'f=1-2 h_x k_x has the exact terminal-inclusive influence and signed entropy ledger in DERIVATION equations (1)-(5). '
 'With a_i=E h_i,b_i=E k_i,A_i=a_i*b_i,s=(A0+A1)/2, lambda_i=A_i/(2s), '
 'normalized component references Q_hi,Q_ki positive on their blocker spectra give R=sum_i lambda_i Q_hi Q_ki, '
 'Q_C(T,xi)=R(T)/2 and, for 0<s<1, Q_f(empty)=1-v,Q_f(A)=v Q_C(A)/(1-q_e) for nonempty A, '
 'where v=4s(1-s),q_e=Q_C(empty). These are normalized whole-set references with complete '
 'CE(f,Q_f)=h2(v)+4s[CE(P_C,Q_C)-s log2(1/q_e)+(1-s)log2(1-q_e)]. '
 'The exact excess is v KL(P_C conditioned nonempty || Q_C conditioned nonempty). '
 'Zero branch masses are omitted and constant outputs use an empty point mass. No universal influence bound on this excess is claimed.')
claim=dict(old);claim.update(version=3,exact_statement=old['exact_statement']+addition,
 statement_sha256=hashlib.sha256((old['exact_statement']+addition).encode()).hexdigest(),
 proof_source={'prior_version_source':str(previous),'prior_version_sha256':digest(previous),'new_proof':str(R/'DERIVATION.md'),'new_proof_sha256':digest(R/'DERIVATION.md'),'locators':['equations (1)-(10)','First unsupported line and downstream use']},
 proof_dependencies=[{'claim_id':old['claim_id'],'version':2,'scope_used':'Unchanged inherited statements; author-proved pending independent review'}, {'claim_id':'ELEMENTARY-PARSEVAL-PRODUCT-ENTROPY-LOGSUM','version':'standard','scope_used':'Self-contained new interface/reference proof'}],
 review_records=[],status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',supersedes=[{'claim_id':old['claim_id'],'version':2}],
 first_unproved_line='Pay complete reference excess and terminal conversions by one dimension-independent physical influence account, iterably through overlapping blockers.',
 next_consumers=['A008','A009','A006','A015','B03','A086','A094'])
claim['hypotheses']=old['hypotheses']+['New interface: finite disjoint private cubes, one shared bit, nested Boolean blocker branches; component reference support positivity; all bits uniform']
save('CLAIMS.json',[claim])
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=R.name,stream='B03',packet_id='A014',
 gap_id='B03-WHOLE-SET-BLOCKER-PAYMENT',attempt_id='A014-stage4-one-bit-reference',
 method='Exact signed block-product entropy ledger and normalized whole-output reference; exhaustive symbolic logarithm certificates',
 mathematical_delta='Closed one-shared-bit whole-set reference construction and complete empty/terminal/signed cost identities; not the influence payment. Full 6561-case certificate passed.',
 deliverable_status='COMPLETE_LOCAL',mathematical_status='SCOPED_INTERFACE_PROVED_PENDING_REVIEW; FULL_FEI_AND_ALL_DENSITY_LINEAR_HYPERGRAPHS_OPEN',
 claim_versions_used=[old['claim_id']+'@2'],claims_created_or_changed=[old['claim_id']+'@3'],
 source_artifacts=['DERIVATION.md','REPORT.md','FROZEN_SPEC.json','code/check.py','out/pilot.json','out/check.json','out/checkpoint.json'],
 next_consumers=claim['next_consumers'],
 next_action='Compare an occupation-based R with the complete mixture ledger on the first overlapping graph blocker component, preserving actual row law, terminal references and empty refund.',
 stagnant_substantive_attempts=0,blockers=['General influence-paid conditional KL and terminal conversion costs unproved','No independent reconstruction or downstream adoption yet'],packet_ids=['A014'])
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
stamp=datetime.now(timezone.utc).isoformat()
(A/'STATUS.md').write_text(f"STATE: A014 stage 4 complete locally: normalized one-shared-bit blocker reference and exact terminal/signed ledger proved; {check['assertions']:,} full exact assertions PASS; review pending; FEI OPEN.\nNEXT: Compare occupation-based R with complete mixture cost on an overlapping graph blocker, retaining actual row law, terminal references and empty-spectrum refund.\n",encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n'+stamp+' stage 20261014T024736Z: read updated BOARD/B03 and A008 corrected occupation report. Derived one-shared-bit nested blocker influence/entropy law and explicit normalized whole-set reference with exact empty normalization/refund and conditional KL debt. Initial lexicographic pilot had only zero blockers; preserved it, froze diagonal pilot repair before full search. '+receipt+' General influence payment remains open; no new broad FEI candidate or messages.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nStage 4: C=h_x(Y)k_x(Z), nested blockers on disjoint private cubes. Physical Ix=A0-A1, private I=sum_i[b_i I(1-2h_i)+a_i I(1-2k_i)]/2. Normalized blocker entropy = weighted terminal blocker entropies + h2(lambda1)-erased-label entropy L+signed separator entropy J. Whole output H=h2(v)+4s[H(P_C)-h2(s)],v=4s(1-s). Mixture component reference with uniform separator gives normalized Q_C; conditioned nonempty reference Q_f has complete CE=h2(v)+4s[CE_C-s log(1/q_e)+(1-s)log(1-q_e)]. Exact excess=v conditional KL. Retain both empty terms: constant outputs cancel the blocker reference bill. Reference existence does not pay its influence cost; terminal entropies and same physical budget remain required. Rational prime-log coefficient vectors give exact entropy-identity checks without numeric logs.\n')
sources=[Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'),Path('~/brain_workers/FEI100_20261011/claude/B03/STREAM_NOTES.md'),Path('~/brain_workers/FEI100_20261011/agents/A008/runs/20261014T021605Z-fleet05-A008-gate-label-compression/REPORT.md'),previous]
save('out/SOURCES.json',[{'path':str(p),'sha256':digest(p)} for p in sources])
protocol=json.loads(sources[0].read_text())
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert json.loads((R/'PACKET_DELTA.json').read_text())==progress
assert len((A/'STATUS.md').read_text().splitlines())==2
receipts=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='RECEIPTS.json':
  assert p.stat().st_size<20_000_000
  receipts.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':digest(p)})
save('out/RECEIPTS.json',{'created_utc':stamp,'protocol_field_sets':'PASS','progress_delta_equality':'PASS','scope':'Local persistence only; independent review/mirror unverified','files':receipts})
print(json.dumps({'schema':'PASS','files_hashed':len(receipts),'full_assertions':check['assertions'],'full_fei':'OPEN'}))
