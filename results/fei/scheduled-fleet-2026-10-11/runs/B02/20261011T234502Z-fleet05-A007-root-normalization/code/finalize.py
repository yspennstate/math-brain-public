from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

run=Path(__file__).resolve().parents[1]; agent=run.parents[1]
root=Path('~/brain_workers/FEI100_20261011')
reports=Path('~/mop_fei100/reports/fei-2026-10-11')
a009=root/'agents/A009/runs/20261011T223308Z-fleet05-A009-fractional-incidence-optimization'
a094=root/'agents/A094/runs/20261011T224936Z-fleet05-A094-proof-chain-challenger'
prior=agent/'runs/20261011T215236Z-fleet05-A007-root-normalization'
seed=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents/SEED_LEMMAS.md')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,obj): p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
protocol=json.loads((reports/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
baseline=[{'source':str(reports/'source_material/reductions/paper/forests.tex'),
           'locator':'eq:forestconditioning, eq:forestcost, thm:posteriorforest',
           'sha256':sha(reports/'source_material/reductions/paper/forests.tex'),'status':'source-complete baseline reconstructed'},
          {'source':str(seed),'locator':'Section 2','sha256':sha(seed),'status':'source-complete complete-reference mixture baseline'}]
review_statement=('The assertions in hash-pinned A009 INCIDENCE_OPTIMIZATION.tex hold at their exact scopes: '
 'for fixed actual-run posterior laws with nonempty gate supports and positive root parameters, '
 'F(t)=v ln(product_l(1+pi_l exp(t_l))-1)-sum_l c_l t_l is convex under '
 'sum_{l:j in R_l}exp(t_l)<=1. The stated Gibbs/Lagrangian dual L(nu,y) is a lower certificate '
 'when b_l=c_l-v Pr_nu(l in R)>=0 and its scalar infima are finite; normalized root nu, '
 'b_l=lambda_l sum_{j in R_l}y_j and complementary slackness certify equality. '
 'Joint posterior optimization is nonconvex: duplicate dictators have residual '
 'ln(1+lambda_1 lambda_2/(2(lambda_1+lambda_2))), with second derivative -1/17 '
 'at lambda_l=1/4 on the exp(t+-s) path. All r,m>=1 singleton-petal activations '
 'have the specified actual-law residual <=8I and paid prior <=10I. Geometric sunflower '
 'weights lambda_l=2^-l give positive outer pressure <41I. For all prime powers Q>=16, '
 'the affine-plane OR-of-line-conjunctions positive coordinatewise pressure is '
 '>=7I log2((Q+1)/2) for every feasible lambda and every pivotal tie decomposition; '
 'uniform weights give <=7I log2(Q+1). These are not lower bounds for PI-J or FEI.')
review=dict(claim_id='A007-INDEPENDENT-REVIEW-A009-INCIDENCE',version=1,exact_statement=review_statement,
 hypotheses=['original A009 scopes preserved','fixed-law and optimized-law objectives distinguished',
             'uniform Boolean cube where asserted; other KKT examples abstract','bits except natural-unit primal and dual'],
 statement_sha256=hashlib.sha256(review_statement.encode()).hexdigest(),contributors=['A009 original artifact'],
 proof_source={'original':str(a009/'INCIDENCE_OPTIMIZATION.tex'),'source_sha256':sha(a009/'INCIDENCE_OPTIMIZATION.tex'),
               'independent_reconstruction':str(run/'REVIEW_A009.md')},
 proof_dependencies=baseline,
 review_records=[{'reviewer':'A007','verdict':'ACCEPT_AT_STATED_SCOPE','supplied_substantive_repair':False,
                 'method':'independent analytic reconstruction, physical boundary/geometry census, integer Walsh and exact rational certificates',
                 'source_claim_registry_empty':True,'review_source':str(run/'REVIEW_A009.md')}],
 status='INDEPENDENTLY_RECONSTRUCTED_ACCEPTED_LOCALLY',supersedes=[],refutes=[],first_unproved_line=None,
 next_consumers=['A009','A010','A085','A086','A094','B20'])

new_statement=('For every r,w>=1, m=2^w, F=2 A_r OR_{l=1}^m A_w^(l)-1 on a fresh uniform core '
 'and disjoint private conjunction blocks, its complete conditioned posterior residual '
 'for all m prime implicants, lambda_l=1/m, M_l=1 and core-first orders admits '
 'actual partition-forest laws with R<=26 I(F)/5. R includes v(Lambda+log2 Z), '
 'all labels once per used gate, root rarity, subset congestion, rank discrepancy and '
 'minus entropy of actual chronological runs. A fixed prior w_j=1/((j+1)(j+2)) '
 'on complete references with lambda^(j)=2^-j/m costs v for globally selecting j=0 '
 'and gives R+prior<=36 I(F)/5. Separately, for every prime power q>=16, '
 'the affine-plane line-conjunction Boolean family, every feasible positive incidence '
 'vector and every pivotal tie decomposition satisfy '
 'P+v log2 Z>=[7 log2((q+1)/2)-5] I, where '
 'P=(48/5)sum_j alpha_j log2(sum_{l through j}sqrt(q_{j,l})lambda_l^(-11/48)), '
 'pi_l=2^-q, Z=1-product_l(1+lambda_l pi_l)^(-1), and v=Var(f). '
 'Thus negative normalization cannot rescue this coordinatewise fractional bound. '
 'This does not lower-bound the optimized whole-set residual or disprove PI-J or FEI.')
new=dict(claim_id='A007-PIJ-ACTIVATION-CLOSURE-AND-NORMALIZER-DIAGNOSTIC',version=1,
 exact_statement=new_statement,
 hypotheses=['uniform finite Boolean cubes','activated tribes: r,w>=1, disjoint width-w petals, m=2^w',
             'specified fixed generator, lambda and orders; actual finite partition runs',
             'affine-plane part: prime-power q>=16, all positive feasible weights and arbitrary pivotal tie decomposition',
             'entropy and residual in bits; gamma=6/5'],
 statement_sha256=hashlib.sha256(new_statement.encode()).hexdigest(),contributors=['A007'],
 proof_source={'path':str(run/'REPORT.md'),'locators':'Derivation A2 and B-F'},
 proof_dependencies=baseline+[{'source':str(run/'REVIEW_A009.md'),'locator':'affine-plane mass cap',
                               'status':'independent reconstruction completed in this stage'}],
 review_records=[],status='AUTHOR_PROVED_EXACTLY_CHECKED_PENDING_INDEPENDENT_REVIEW',
 supersedes=[],refutes=['all-weight coordinatewise affine-plane fractional pressure payment even with retained v log Z'],
 first_unproved_line=None,next_consumers=['A006','A008','A009','A010','A085','A086','A094','B20'])

accepted=next(c for c in json.loads((a094/'CLAIMS.json').read_text()) if c['claim_id']=='A007-SHARED-CORE-ROOT-CANCELLATION')
original=json.loads((prior/'CLAIMS.json').read_text())[0]
assert accepted['exact_statement']==original['exact_statement']
assert accepted['statement_sha256']==original['statement_sha256']
accepted['proof_source']['path']=str(prior/'REPORT.md')
accepted['proof_source']['companion']=str(prior/'ROOT_NORMALIZATION.tex')
claims=[accepted,review,new]
for claim in claims: assert set(claim)==set(protocol['required_per_run']['claim_fields'])
save(run/'CLAIMS.json',claims)

checks=json.loads((run/'out/CHECK.json').read_text())
extra=json.loads((run/'out/NORMALIZER_CHECK.json').read_text())
total=checks['assertions_passed']+extra['assertions_passed']
progress=dict(protocol_revision=protocol['revision'],run_id=run.name,stream='B02',packet_id='A007',gap_id='C020/PI-J-JOINT-COST',
 attempt_id='A007-stage2-review-and-activation',method='independent whole-artifact review; root-normalized PI-J activation ledger and all-weight affine diagnostic',
 mathematical_delta='A009 independently reconstructed; prior A007 acceptance consumed; full activated-tribes R<=26I/5, paid prior<=36I/5; affine P+v log Z>=[7log((q+1)/2)-5]I for all weights.',
 deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='SCOPED_PROOFS_AND_REVIEW_COMPLETE_FULL_FEI_OPEN',
 claim_versions_used=[{'claim_id':accepted['claim_id'],'version':1,'status':'A094 independently accepted'},
                     {'source':str(a009/'INCIDENCE_OPTIMIZATION.tex'),'sha256':sha(a009/'INCIDENCE_OPTIMIZATION.tex'),'status':'A007 whole-artifact acceptance at stated scopes'},
                     {'source':'forests.tex thm:posteriorforest','sha256':baseline[0]['sha256']}],
 claims_created_or_changed=[{'claim_id':c['claim_id'],'version':c['version'],'status':c['status']} for c in claims],
 source_artifacts=['REPORT.md','REVIEW_A009.md','FROZEN_SPEC.json','NORMALIZER_FROZEN_SPEC.json','code/check.py','code/normalizer_check.py','out/CHECK.json','out/NORMALIZER_CHECK.json','out/SOURCES.json','out/RECEIPTS.json'],
 next_consumers=new['next_consumers'],
 next_action='Derive data-witness-preserving root transfer for overlapping PI-J forests; A009 apply it to the affine-plane joint label/rank cost, avoiding the refuted coordinatewise payment.',
 stagnant_substantive_attempts=0,blockers=['new continuation awaits A086/A094 review','arbitrary overlapping PI-J rank/occupancy law remains unpaid'],
 packet_ids=['A007'])
assert set(progress)==set(x.split(' (')[0] for x in protocol['required_per_run']['progress_fields'])
save(run/'PROGRESS.json',progress);save(run/'PACKET_DELTA.json',progress)
sources=[root/'BOARD.md',root/'claude/B02/STREAM_NOTES.md',reports/'EXECUTION_PROTOCOL.json',
         reports/'source_material/reductions/paper/forests.tex',a009/'INCIDENCE_OPTIMIZATION.tex',a009/'REPORT.md',
         a009/'WEIGHT_CERTIFICATE.json',a009/'CLAIMS.json',a094/'AUDIT.md',a094/'CLAIMS.json',prior/'CLAIMS.json',prior/'REPORT.md',seed]
save(run/'out/SOURCES.json',[dict(path=str(p),sha256=sha(p),size_bytes=p.stat().st_size) for p in sources])
now=datetime.now(timezone.utc).isoformat()
(agent/'STATUS.md').write_text(f'STATE: A007 stage 2 complete: A009 independently accepted; activated-tribes full R<=26I/5; affine normalization rescue refuted; {total:,} exact assertions; new proof review pending; FEI OPEN.\nNEXT: A086/A094 review full closure and normalizer diagnostic; derive data-witness-preserving root transfer for affine-plane joint PI-J labels/ranks rather than another coordinatewise bound.\n',encoding='utf8')
with (agent/'WORKLOG.md').open('a',encoding='utf8') as f:
 f.write(f'\n{now} — Stage 2: consumed B02 v2 direction and A094 acceptance of A007 v1. Independently reconstructed A009 whole artifact with no repair. Proved complete activated-tribes residual <=26I/5 (36I/5 with paid prior), and retained-normalizer affine pressure lower bound >=[7log((q+1)/2)-5]I for every weight. {total:,} exact assertions; {checks["actual_constructed_partition_traces"]:,} actual traces; main pilot {checks["elapsed_seconds"]:.3f}s. Full PI-J remains open; all files saved locally.\n')
with (agent/'LEARNED.md').open('a',encoding='utf8') as f:
 f.write('''
## Stage 2 durable additions

- A094 independently accepted original A007 root component at its exact scope. A007 independently reconstructed the entire A009 incidence artifact; fixed-law convexity cannot be transferred to the jointly optimized posterior.
- For activated tribes m=2^w, the prime-implicant star code pays all residual terms by 26I/5. Root remainder <=2I_data+log2(e)I_core; private/core rank <=(6/5)I; congestion <=(6/5)log2(e)I_core; labels minus actual-run entropy <=2I_data. The fixed paid prior adds <=2I.
- The congestion payment uses s log2(1+u/s)<=u log2(e), E u=r/2 on nonempty-data spectra, and Q m rho<=1-Q. Do not charge a log(r+1) factor per private coordinate when the shared core can pay occupancy jointly.
- Every selected private coordinate of a disjoint conjunction petal sees binomial predecessors on its core-first support. This exact conditional law is unpaid for arbitrary overlapping gates.
- Affine-plane pressure retains its row mass: P>=7I log2((q+1)/2)+(11/5)I log2(q/u), u=sum lambda<=q. Root normalization obeys log2 Z>=-q+log2 u-log2(1+q2^-q), and v/I<=4/q. Thus P+v log2 Z>=[7log2((q+1)/2)-5]I for all weights. Sending u to zero cannot rescue the coordinatewise bound, because its log-u coefficient is negative. This is not a PI-J or FEI disproof.
- The shortest unresolved task is the actual joint label/rank cost on growing overlapping prime implicants, with the negative normalizer retained and a data-witness-preserving decoder; further read-once calibration does not replace it.
''')
report=(run/'REPORT.md').read_text()
for field in protocol['required_per_run']['report_fields']: assert '## '+field in report,field
assert '## Universal bridge\n\n' in report
receipts=[]
for p in sorted(run.rglob('*')):
 if p.is_file() and p.name!='RECEIPTS.json':
  assert p.stat().st_size<20_000_000
  receipts.append(dict(path=str(p.relative_to(run)),size_bytes=p.stat().st_size,sha256=sha(p)))
for p in [agent/'STATUS.md',agent/'WORKLOG.md',agent/'LEARNED.md']:
 receipts.append(dict(path=str(p),size_bytes=p.stat().st_size,sha256=sha(p)))
save(run/'out/RECEIPTS.json',dict(saved_at=now,scope='local persistence; mirror and independent review of new proof pending',files=receipts))
print(json.dumps(dict(claims=len(claims),total_exact_assertions=total,persistence_files=len(receipts),protocol_fields_checked=True)))
