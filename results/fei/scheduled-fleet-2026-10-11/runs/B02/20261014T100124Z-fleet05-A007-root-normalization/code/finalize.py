from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,copy
root=Path(__file__).resolve().parents[1]; agent=root.parents[1]; workers=agent.parents[1]
reports=Path(r'~\mop_fei100\reports\fei-2026-10-11')
other=workers/'agents/A015/runs/20261014T062347Z-fleet05-A015-minterm-barrier-analysis'
prior=agent/'runs/20261014T043228Z-fleet05-A007-root-normalization'
lift=agent/'runs/20261014T014217Z-fleet05-A007-root-normalization'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,o): Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
stamp=datetime.now(timezone.utc).isoformat()
sources=[reports/'EXECUTION_PROTOCOL.json',workers/'BOARD.md',workers/'claude/B02/STREAM_NOTES.md',
 other/'REPORT.md',other/'CLAIMS.json',other/'SCOPE_AND_CREDITS.md',other/'REVIEW_A007.md',prior/'GENERAL_BUDGET.md',prior/'CLAIMS.json',
 agent/'runs/20261013T220854Z-fleet05-A007-root-normalization/code/check_lift.py']
save(root/'out/SOURCES.json',[{'path':str(p),'sha256':sha(p),'scope':'read this stage'} for p in sources]+[
 {'path':str(lift/'DISTRIBUTED_LIFT.md'),'sha256':sha(lift/'DISTRIBUTED_LIFT.md'),'scope':'inherited accepted proof interface; not newly reread in full'}])
accepted=copy.deepcopy(json.loads((other/'CLAIMS.json').read_text(encoding='utf-8-sig'))[0])
old=next(c for c in json.loads((prior/'CLAIMS.json').read_text(encoding='utf-8-sig')) if c['claim_id']==accepted['claim_id'])
assert old['exact_statement']==accepted['exact_statement'] and old['statement_sha256']==accepted['statement_sha256']
statement=('For gamma=6/5, every actual old partition forest rho with used gates V, roots R, c=|R|, owned sizes s_l and selected intersections kappa_l has the following exact rank-stripped common-core distributed-lift multiplier for each integer u>=1. Let a(l) be its actual tree-component root, pi_a its old rarity and f_l(z)=sum_{v=0}^u [((s_l+v)/(kappa_l+u))^(gamma(s_l+v))/(s_l/kappa_l)^(gamma*s_l)] z^v/v!. If c=1, G_rho(u)=beta^|V| u! [z^u]prod_l f_l. If c>=2, G_rho(u)=beta^|V|(u+1)_(c-2)u!/[prod_R pi] [z^u]sum_l pi_a(l) z f_l\' prod_{h!=l}f_h. Under the SAME original conditional surrogate posterior J_dist,U(T)=E_eta_T G_rho(|U|). These are selected-family equalities, not complete activated mass or queue probability. At u=1 the root average is weighted by susceptibility t_l=(s_l+1)^(gamma(s_l+1))/(s_l^(gamma*s_l)(kappa_l+1)^gamma), not owned sizes. The actual overlapping two-prime Boolean OR with supports {0,1,4},{2,3,4,5}, selected T={0,1,2}, lambda=(1/2,1/2), beta=1 has forced old ownership (2,1), root rarities (1/8,1/16), ghat(T)=-1/32, and susceptibility-weighted root mean strictly below the owned-size mean 5/48. Thus replacing susceptibility by the owned-size mean in the lower refund is false. Nevertheless its exact J=16*2^(-6/5)+8*(4/9)^(6/5)>8, while one-core conditioning D\'/(pD)=97/98. The complete signed all-sector budget and inherited pR_g remain unpaid universally.')
new={'claim_id':'A007-EXACT-ROOT-TILTED-OCCUPATION','version':1,'exact_statement':statement,
 'hypotheses':['fixed positive feasible fractional weights and globally fixed beta with beta sum lambda<=1',
 'nonempty selected data T; every used gate has positive owned size and s_l<=kappa_l',
 'actual old chronological partition forests, not separate SCC moment factors; pi_a>0',
 'fresh positive common conjunction core; gamma=6/5; logs bits; rising factorial convention',
 'surrogate and rank-stripped selected lift distinguished from full mass and actual queue output'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A007'],
 'proof_source':{'path':str(root/'JOINT_OCCUPATION.md'),'certificate':str(root/'out/EXACT_CHECK.json'),'witness':str(root/'out/WITNESS.json')},
 'proof_dependencies':[{'claim_id':'A007-DISTRIBUTED-CORE-COMPONENT-LIFT','version':1,'statement_sha256':'d098009e6a0d306a1a627bc12cf92d8dcc345befadb682bb4e8c7072aa318c6b','status':'A015_NO_REPAIR_ACCEPTANCE_CONSUMED_PREVIOUS_STAGE','proof_source':str(lift/'DISTRIBUTED_LIFT.md')}],
 'review_records':[],'status':'AUTHOR_PROVED_EXACTLY_CHECKED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':[{'statement':'Replace sum_l pi_a(l)t_l/sum_h t_h by sum_l pi_a(l)s_l/s in the u=1 lower root refund','scope':'additional shortcut, no existing registered claim refuted','witness':str(root/'out/WITNESS.json')}],
 'first_unproved_line':None,'next_consumers':['A015','A006','A008','A009','A010','A086','A094','B02','B03','B20']}
claims=[accepted,new]; save(root/'CLAIMS.json',claims)
check=json.loads((root/'out/EXACT_CHECK.json').read_text()); pilot=json.loads((root/'out/PILOT.json').read_text())
total=check['counts']['assertions']+check['helper_assertions']; assert total==1458 and check['status']=='PASS'
nextaction='Pay the exact root-tilted occupation coefficient under the SAME old determinant/factorial posterior on mixed-width shared/leafless incidence; retain all r+1 sectors, signed normalizer and inherited pR_g. A015/A008 independently review the transform and factorization falsifier; A086 audit root-component scope.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':root.name,'stream':'B02','packet_id':'A007','gap_id':'C020/PI-J-JOINT-COST','attempt_id':'A007-stage6-root-tilted-coefficient',
 'method':'Independent whole A015 diagnostic review; exact labelled occupation coefficient and root-marked convolution; independently enumerated chronological component trees; actual overlapping Boolean countercertificate',
 'mathematical_delta':'Exact all-support distributed occupation/root numerator, O(|V|u^2) per old forest. Owned-size root factorization refuted by actual shared-prime witness; exact coupled J>8 and signed Dprime/(pD)=97/98. 1458 full exact assertions PASS; A015 downstream acceptance consumed. No universal constant changed.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'EXACT_INTERFACE_AND_NARROW_REFUND_CLOSED_UNIVERSAL_PIJ_FEI_OPEN',
 'claim_versions_used':[{'claim_id':accepted['claim_id'],'version':1,'statement_sha256':accepted['statement_sha256'],'status':accepted['status']},new['proof_dependencies'][0],
 {'source':str(other/'SCOPE_AND_CREDITS.md'),'sha256':sha(other/'SCOPE_AND_CREDITS.md'),'status':'A007_INDEPENDENT_WHOLE_ARTIFACT_HOLDS_NO_REPAIR'}],
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'status':c['status']} for c in claims],
 'source_artifacts':['REPORT.md','JOINT_OCCUPATION.md','REVIEW_A015.md','FROZEN_SPEC.json','code/check.py','code/finalize.py','out/PILOT.json','out/EXACT_CHECK.json','out/WITNESS.json','out/PILOT_REPAIR.md','out/SOURCES.json','out/RECEIPTS.json'],
 'next_consumers':new['next_consumers'],'next_action':nextaction,'stagnant_substantive_attempts':0,
 'blockers':['universal influence payment of the complete signed spectral ledger and inherited base residual remains open','new exact transform/refund pending independent review','shared registry adoption and supervisor remote copy unverified'], 'packet_ids':['A007']}
save(root/'PROGRESS.json',progress); save(root/'PACKET_DELTA.json',progress)
report='''# A007 stage 6: roots and occupation stay coupled

## exact target, quantifiers, hypotheses and units

C020 whole-set witness cost, B02 PI-J. For every actual old partition forest under one fixed feasible prime reference and every integer selected core size u>=1, derive its exact rank-stripped distributed occupation numerator with old root rarity and chronological tree credit summed together. Gamma=6/5, costs in bits. This is an algebraic interface and a checked overlapping-sector cancellation, not a new broad FEI candidate. The inherited base residual and universal conjecture remain open.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-14 09:53 UTC with follow-up chunks, B02 lead STREAM_NOTES.md v2 2026-10-11 23:35 UTC and own STATUS. Full EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2 reread. Read A015 stage-5 REPORT, SCOPE_AND_CREDITS, REVIEW_A007 and CLAIMS, and own preceding GENERAL_BUDGET. Own earlier independent event helper was read/compiled. out/SOURCES.json hashes read sources separately from the inherited accepted distributed-lift proof; earlier campaign/paper/source baseline is inherited, not advertised as newly reread. No external literature or brain query is needed for this finite algebraic continuation.

The lead's original A009 review/activation target is already completed. Its review-first direction is followed by reconstructing A015's complete new diagnostic before this narrow interface. A006/A008/A009 board work already prices full stars, connected two-scale families and private leaves; those proofs are not assumed or repeated. The new target is the mixed root/occupation correlation hidden by uniform-root families, including shared and leafless selected graphs in the finite check.

## complete derivation or exact first unsupported line

JOINT_OCCUPATION.md proves the exact marked exponential-generating coefficient for each old actual forest. Each gate series contains its exact new/old congestion ratio; labelled core ownership supplies u!/prod v!. A root-marked derivative supplies component core count u_a before multiplying by pi_a/prod_R pi and the exact chronological factor (u+1)_(c-2). For c=1 the root ratio and tree count are one; it is treated separately. Two-register truncated convolution computes the coefficient in O(|V|u^2) arithmetic and O(u) storage for a GIVEN old forest, without claiming efficient posterior summation. Taking the original eta_T expectation gives exactly J_dist. No entropy/K envelope or separate root averaging is required.

At u=1 the correct root average is tilted by occupation susceptibility t_l. An actual overlapping two-clause prime table refutes replacement of this average by the owned-size law. Its forced positive-spectral record has sizes (2,1), rarities (1/8,1/16), Fourier coefficient -1/32 and t0/t1=(9/8)^(6/5)<2. Thus the exact weighted mean is below the owned-size mean 5/48. The minimum-root lower bound remains sound. This is a falsifier of an additional shortcut, not a refutation of an existing registered theorem or FEI.

On the SAME fixed lambda=(1/2,1/2), beta=1 and one-core activation, the exact multiplier is 16*2^(-6/5)+8*(4/9)^(6/5)>8: old rare-root removal pays occupation loss and leaves over three bits of credit. Exact conditioning is Dprime/(pD)=97/98<1. Both contributions remain in the signed ledger; they are not separately optimized or assumed to pay unrelated sectors. The witness has actual shared coordinate 4 outside its selected T; selected overlap/leafless cases are separately covered by the all-n<=3 enumeration. No private-to-shared full-family payment is inferred from this one record.

REVIEW_A015.md reconstructs the entire preceding arbitrary-support tail obstruction, nearly sharp K charge, star surrogate and ACTUAL queue probability without repair. Its downstream acceptance of our full-support tail/general budget is consumed at unchanged statement/hash, with A015's upstream-authorship disclosure intact. This is not our self-review.

The exact ledger retains p Var(g)log[Dprime/(pD)], empty-core L0, all nonempty selected core sizes, original posterior and inherited pR_g. The first unsupported universal line is still a dimension-independent influence payment of this complete signed spectral expectation together with inherited base residual, using an appropriate once-fixed reference. Exact occupation coefficients remove one approximation; they do not establish that payment.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded the pilot. The final full run used all 22 labelled nonempty monotone prime antichains on n=2,3; every covered nonempty T, every eligible owner map, every old chronological forest; core size u=1,2,3. It checked 123 assignments, 127 old forests and 384 occupation cases (including the three fixed mixed-root witness cases). Direct labelled maps were compared to a two-register formal coefficient implementation. Independent component parent/attachment/child-permutation enumeration checked 514 tree records for u<=2,c<=3. Original physical integer Walsh spectra and flip influences were checked for each small table. The fixed six-coordinate witness additionally exhausts all 3^6 ternary literal lists to confirm its full signed prime table, its nonzero coefficient and exact integer refund/factorization signs.

Arithmetic is integer/Fraction and formal positive rational bases raised to 6/5; no floating sign is used. Equal formal sums are sufficient exact certificates despite not claiming a canonical basis for all algebraic identities. The all-u coefficient theorem is analytic, not extrapolated from u<=3. This stage supplies no numerical whole-ledger influence bound.

The initial pilot exposed a draft Fourier expectation 3/32; direct product expansion gives -1/32. Proof and checker were corrected before repeating it; out/PILOT_REPAIR.md preserves the failure. No successful totals include that failed run or superseded pilot. Final pilot passed 58 direct+16 helper assertions in 0.012844 seconds. Final full passed 1204 direct+254 helper assertions, total 1458, in 0.049092 seconds; pilot overlap is reported separately. Commands from A007:

    python -X utf8 runs/20261014T100124Z-fleet05-A007-root-normalization/code/check.py --pilot
    python -X utf8 runs/20261014T100124Z-fleet05-A007-root-normalization/code/check.py
    python -X utf8 runs/20261014T100124Z-fleet05-A007-root-normalization/code/finalize.py

Frozen memory estimate is 100 MB, not a measured peak, so the >300 MB preflight trigger does not apply. Jobs ran sequentially below 60 seconds, with no automatic dimension increase, GPU, background process or window. No other agent files were modified or author checker imported.

## proof dependencies and changed downstream conclusions

The accepted distributed-lift theorem supplies actual component-tree counts and the injective old-event recovery. The new coefficient proof is direct labelled combinatorics; no other graph cost theorem is a premise. The earlier full-support tail/general budget is locally adopted with A015's unchanged review record. Its valid min-root lower credit is strengthened to an exact occupation-weighted root numerator; an attempted owned-size replacement is rejected. The original negative normalization and full inherited residual stay available for downstream payment. New claim is narrowly author-proved/exactly-checked and pending independent review. Universal constant is unchanged.

## one next mathematical action and independent reviewer

Pay the exact root-tilted coefficient under the SAME old determinant/factorial posterior on mixed-width shared/leafless incidences, retaining all core-size sectors and inherited pR_g. A015/A008 should independently reconstruct the marked coefficient, one-control tilt and actual factorization falsifier; A086 should challenge use of actual tree-component roots versus source SCCs. This replaces the invalid independent root/ownership averaging shortcut with the exact quantity that a universal payment must bound. No messages were sent.

## actual persistence receipts or precise save blocker

All four protocol files, complete proof/review, frozen spec, independent checker, exact outputs, pilot correction and rolling files are saved only under A007. out/RECEIPTS.json records SHA256/size receipts and checks exact protocol fields, unchanged accepted statement/hash, PROGRESS/PACKET_DELTA equality and 20 MB caps. STATUS has two lines; WORKLOG/LEARNED are appended. Local save is complete; independent review of the new result, shared registry adoption and supervisor mirror copy remain unobserved.

## Universal bridge

C020 whole-set witness cost moves from a separate ownership/K upper bill and minimum-root credit to an exact all-support occupation/root coefficient for every original forest and selected core size, with a concrete overlapping-sector refund exceeding three bits and a retained negative normalization 97/98. An actual Boolean mixed-width prime family rules out independently averaging root rarity under owned-set proportions, closing that proposed shortcut before it enters a universal proof. No full-FEI constant changes: the same-posterior all-sector expectation and inherited physical-location/base cost remain unpaid. NEXT prices that exact coupled numerator on shared/leafless incidence because it targets the surviving universal witness mechanism, rather than another class entropy calibration.
'''
(root/'REPORT.md').write_text(report,encoding='utf-8')
(agent/'STATUS.md').write_text('STATE: A007 stage 6 complete: exact all-support root-tilted occupation coefficient; actual overlapping root-average shortcut refuted; same-record J>8 and signed ratio97/98;1458 full exact checks PASS; FEI OPEN.\nNEXT: Pay exact mixed-root occupation coefficient under SAME old determinant/factorial posterior on shared/leafless incidence with all core sectors and inherited pR_g; A015/A008/A086 review transform and falsifier.\n',encoding='utf-8')
entry='''
### 2026-10-14 stage6 10:01 UTC — root-tilted occupation
Consumed A015 no-repair downstream tail acceptance and independently reconstructed its entire OR scope/queue diagnostic. Derived an exact all-u root-marked occupation coefficient, verified 384 cases and 514 chronological component-tree records; full 1458 assertions PASS. Mixed-width overlapping prime witness rejects owned-size root averaging; correct same-reference J>8 and Dprime/(pD)=97/98. Initial wrong Fourier expectation repaired to -1/32 and preserved. Universal signed spectral/base payment remains open; next exact numerator pricing, no separate posterior credits.
'''
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f: f.write(entry)
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f: f.write('''
### Stage6 durable facts — exact occupation/root tilt
- Exact distributed multiplier per old forest is a marked exponential coefficient: c>=2 uses pi_a(l) z f_l' and (u+1)_(c-2)u!/prod pi; c=1 uses u!prod f. Actual TREE components are required. This does not make old forest summation efficient or pay universal cost.
- One-control susceptibility t_l=(s_l+1)^(gamma(s_l+1))/(s_l^(gamma*s_l)(kappa_l+1)^gamma) determines the root mean. Owned-size proportions cannot replace this tilt: supports {0,1,4},{2,3,4,5}, T={0,1,2}, lambda=.5 each give pi(1/8,1/16), forced sizes(2,1), ghat=-1/32, exact root mean<5/48. Valid min-root credit survives.
- Same overlapping record has J=16*2^(-6/5)+8*(4/9)^(6/5)>8 and one-core Dprime/(pD)=97/98. Preserve that signed normalizer, all other spectral sectors and inherited pR_g; one refund is not universal payment.
''')
protocol=json.loads((reports/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert all(set(c)==set(protocol['required_per_run']['claim_fields']) for c in claims)
for c in claims: assert hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256']
assert json.loads((root/'PROGRESS.json').read_text())==json.loads((root/'PACKET_DELTA.json').read_text())
assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
assert report.rstrip().split('## Universal bridge\n')[1].count('\n')==1
files=[p for p in root.rglob('*') if p.is_file() and p.name!='RECEIPTS.json']+[agent/s for s in ['STATUS.md','WORKLOG.md','LEARNED.md']]
receipts=[]
for p in sorted(files):
    assert p.stat().st_size<20*1024*1024
    receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
save(root/'out/RECEIPTS.json',{'timestamp_utc':stamp,'local_only':True,'protocol_schema':'PASS','files':receipts})
for item in receipts: assert sha(item['path'])==item['sha256']
print(json.dumps({'status':'PASS','full_checks':total,'receipt_files':len(receipts),'claims':len(claims),'full_fei':'OPEN'}))
