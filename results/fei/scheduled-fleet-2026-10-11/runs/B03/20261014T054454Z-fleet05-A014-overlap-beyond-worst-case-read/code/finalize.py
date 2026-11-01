from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,data):(R/name).write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
check=json.loads((R/'out/check.json').read_text());pilot=json.loads((R/'out/pilot.json').read_text())
assert check['selected_graphs']==521 and check['labelled_candidates']==1096
assert check['elapsed_seconds']<300 and pilot['elapsed_seconds']<60
rows=check['rows'];improved=[r for r in rows if F(r['mixture_CE_over_I'][1])<F(r['product_CE_over_I'][0])]
assert len(improved)==132
assert all(F(r['occupation_CE_over_I'][1])<F(7,2) and F(r['product_CE_over_I'][1])<3 and F(r['mixture_CE_over_I'][1])<3 for r in rows)
summary={'domain':'all 521 connected labelled cut-vertex graphs on 3,4,5 vertices at fixed lambda=1/Delta','strict_product_beats_occupation':check['wins']['product'],'strict_half_mixture_improves_product':len(improved),'max_certified_upper_ratios':{k:str(max(F(r[k][1]) for r in rows)) for k in ['product_excess_over_I','product_CE_over_I','occupation_CE_over_I','mixture_CE_over_I']},'finite_bounds':'occupation CE<7I/2; product and mixture CE<3I; not universal or raw occupation cost bounds','first_mixture_gain':improved[0]}
save('out/COMPARISON.json',summary)
previous=A/'runs/20261014T024736Z-fleet05-A014-overlap-beyond-worst-case-read/CLAIMS.json'
old=json.loads(previous.read_text(encoding='utf-8'))[0]
addition=(' In the one-shared-bit nested blocker interface, using exact normalized component spectra as terminal references, '
 'the full normalized product reference obeys 0<=CE(f,Q_prod)-H(f)<=2I(f) in every private dimension, '
 'with constants handled by the empty point mass. This retains H(f) and every terminal/gate cost and is not an FEI bound. '
 'For any fixed nonempty output subprobability M positive on actual spectrum, Z=sum M in (0,1], '
 'Q_occ(empty)=1-v and Q_occ(A)=v*M(A)/Z are normalized; complete CE=h2(v)+sum_nonempty p_f log2(1/M)+v log2 Z. '
 'The induced blocker law has empty mass s and nonempty mass (1-s)*M/Z, matching the same output activation exactly. '
 'A fixed half-half nonempty prior mixture pays at most v<=I for reference choice. '
 'For all 521 connected labelled graphs with a cut vertex on n=3,4,5 at lambda_e=1/Delta and corrected complete occupation factors, '
 'normalized occupation CE<7I/2 and product/mixture CE<3I; product beats occupation separately on all 521, '
 'but their fixed half-half mixture strictly improves product CE on 132 certified graphs. '
 'Universal occupation expectation and inherited component reference debts remain unpaid.')
claim=dict(old);claim.update(version=4,exact_statement=old['exact_statement']+addition,
 statement_sha256=hashlib.sha256((old['exact_statement']+addition).encode()).hexdigest(),
 proof_source={'prior_version_source':str(previous),'prior_version_sha256':digest(previous),'new_proof':str(R/'DERIVATION.md'),'new_proof_sha256':digest(R/'DERIVATION.md'),'finite_certificate':str(R/'out/check.json'),'finite_certificate_sha256':digest(R/'out/check.json'),'locators':['A separator conversion, (11)-(12)','B occupation matching, (13)-(15)','C exact graph implementation']},
 proof_dependencies=[{'claim_id':old['claim_id'],'version':3,'scope_used':'Unchanged prior statements and exact interface/reference definition; pending independent review'},
 {'claim_id':'A008-MATCHING-OCCUPATION-MASS-COLLISION-CREDIT','version':1,'scope_used':'Corrected full mass formula and complete-queue subprobability premise; two reconstructions reported by A008, finite implementation independently checked here'},
 {'claim_id':'A006-MAXIMAL-MATCHING-STAR-COMPLETE-MASS','version':1,'scope_used':'Source-bound queue event positivity/complete interpretation through A008 occupation proof'}],
 review_records=[],status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',supersedes=[{'claim_id':old['claim_id'],'version':3}],
 first_unproved_line='Pay the full occupation expectation and inherited terminal component reference debts on arbitrary overlapping components with one influence budget.',
 next_consumers=['A008','A009','A006','A015','B03','A086','A094'])
claim['hypotheses']=old['hypotheses']+['2I excess bound uses exact component blocker spectra, not arbitrary cost-free child references','Finite graph conclusions restricted to all labelled connected cut-vertex graphs n=3,4,5 with globally fixed lambda=1/Delta and ideal normalized reference costs','Mixture prior is globally fixed; optional physical prefix rounding not included']
save('CLAIMS.json',[claim])
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=R.name,stream='B03',packet_id='A014',gap_id='B03-WHOLE-SET-BLOCKER-PAYMENT',attempt_id='A014-stage5-paid-excess-occupation-match',
 method='Prove paid exact-component separator conversion; match complete occupation law at same spectrum/activation; independently compare convolution and neighbor enumeration',
 mathematical_delta='Closed separator reference excess<=2I and occupation normalization mismatch; optional prior cost<=I. Certified 521 graph costs, including 132 strict mixture gains. General occupation/terminal payment open.',
 deliverable_status='COMPLETE_LOCAL',mathematical_status='SCOPED_CONVERSION_PROVED_PENDING_REVIEW; FULL_FEI_AND_ARBITRARY_DENSITY_OVERLAP_OPEN',
 claim_versions_used=[old['claim_id']+'@3','A008-MATCHING-OCCUPATION-MASS-COLLISION-CREDIT@1','A006-MAXIMAL-MATCHING-STAR-COMPLETE-MASS@1'],claims_created_or_changed=[old['claim_id']+'@4'],
 source_artifacts=['DERIVATION.md','PREVIOUS_INTERFACE.md','REPORT.md','FROZEN_SPEC.json','code/check.py','out/check.json','out/COMPARISON.json'],next_consumers=claim['next_consumers'],
 next_action='Remove one-bit separator factorization: test a genuinely overlapping graph blocker signed-row KL against the same normalized complete occupation law with all actual terminal reference debts.',
 stagnant_substantive_attempts=0,blockers=['Uniform influence payment of full occupation expectation and inherited component KL still open','Independent reconstruction and downstream adoption pending'],packet_ids=['A014'])
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
stamp=datetime.now(timezone.utc).isoformat()
(A/'STATUS.md').write_text('STATE: A014 stage 5 complete: exact-component separator reference excess<=2I proved; 521 graph certificates, 132 fixed-mixture gains, 148738 full exact assertions PASS; review pending; FEI OPEN.\nNEXT: Test non-separator overlapping graph blocker row-KL against the same normalized occupation law, retaining full terminal/reference debts and one influence account.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n'+stamp+' stage 20261014T054454Z: read updated BOARD/B03 and A008 occupation/corrected connected-scale source. Proved exact-component separator reference excess<=2I using log concavity and self-contained cube isoperimetry. Matched normalized complete occupation law to same blocker/output activation and empty refund; fixed prior switch costs <=I. Pilot 3 graphs/255 checks, full 521 labelled cut graphs/15631 sets/148738 assertions PASS in 45.428758 sec. Product has smaller CE on all 521 but half-mixture improves product on132; finite occupation CE<7I/2, product/mix<3I. This is not a universal occupation or FEI bound; all terminal debts retained.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nStage 5: exact component spectra make stage-4 row mixture equal actual row law. Empty reference mass q_e=(A0^2+A1^2)/(4s)>=s/2; actual blocker spectrum <=2Q_C. Complete normalized output reference excess <=v log((2-s)/(1-s))<=2I via isoperimetry of the complement, with no terminal entropy removed. A complete output subprobability M must be compared as Q_occ(A)=v M(A)/Z and Q_occ(empty)=1-v; cost retains +v log Z. Induced blocker law has empty mass s and nonempty (1-s)M/Z. Fixed conditional-nonempty half-mixture costs at most v<=I for choosing a reference once. A worse individual reference can improve mixture CE (132/521 certified graphs), so pointwise/posterior changes cannot be conflated with comparing scalar CE. Uniform degree weights are not universally safe per A008; finite separator results do not cover non-separator overlap or inherited arbitrary component KL.\n')
sources=[Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'),Path('~/brain_workers/FEI100_20261011/claude/B03/STREAM_NOTES.md'),Path('~/brain_workers/FEI100_20261011/agents/A008/runs/20261014T021605Z-fleet05-A008-gate-label-compression/OCCUPATION_MASS.md'),Path('~/brain_workers/FEI100_20261011/agents/A008/runs/20261014T021605Z-fleet05-A008-gate-label-compression/CLAIMS.json'),Path('~/brain_workers/FEI100_20261011/agents/A008/runs/20261014T050954Z-fleet05-A008-gate-label-compression/REPORT.md'),previous]
save('out/SOURCES.json',[{'path':str(p),'sha256':digest(p)} for p in sources])
protocol=json.loads(sources[0].read_text());assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert json.loads((R/'PACKET_DELTA.json').read_text())==progress
assert len((A/'STATUS.md').read_text().splitlines())==2
receipts=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='RECEIPTS.json':
  assert p.stat().st_size<20_000_000
  receipts.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':digest(p)})
save('out/RECEIPTS.json',{'created_utc':stamp,'protocol_fields':'PASS','progress_delta_equality':'PASS','scope':'Local persistence only','files':receipts})
print(json.dumps({'schema':'PASS','files_hashed':len(receipts),'full_assertions':check['assertions'],'mixture_gains':len(improved),'full_fei':'OPEN'}))
