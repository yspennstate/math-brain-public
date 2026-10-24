from pathlib import Path
import json, hashlib, datetime

R=Path(__file__).resolve().parents[1]
A=R.parents[1]
B=A.parents[1]
run=R.name
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
protocol_path=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8'))
check=json.loads((R/'out/CHECK.json').read_text(encoding='utf-8'))
assert check['status']=='PASS'
def write(p,s):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(s,encoding='utf-8')
def js(p,d): write(p,json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

sources=[protocol_path,B/'BOARD.md',B/'claude/B09/STREAM_NOTES.md',
 A/'runs/20261014T055346Z-account05-A044-non-symmetric-gate-classes/PROOF.md',
 B/'agents/A043/runs/20261022T210449Z-account03-A043-prime-gate-decomposition/PROOF.md',
 B/'agents/A042/runs/20261021T221439Z-account03-A042-bias-endpoint-certificates/PROOF.md',
 B/'agents/A045/runs/20261021T165712Z-account03-A045-biased-realizability-referee/PROOF.md',
 B/'context/threshold_paper_38pp.txt',B/'context/threshold_paper_29pp_earlier_version.txt',
 B/'context/percolation_spectral_pivotal_entropy_30pp.txt',B/'context/percolation_spectral_pivotal_entropy_31pp_other_version.txt']
js(R/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'size_bytes':p.stat().st_size} for p in sources])
js(R/'out/FORMAL_CHECK.json',{
 'rung':'NOT_RUN_ADMISSION_HELD','memok_exit_code':1,
 'memok_output':'WAIT: physical free 2.7 GB (need 4.0), commit free 24.5 GB (need 8.0)',
 'source':'code/tail_band.lean','source_sha256':sha(R/'code/tail_band.lean'),
 'planned_target':'A044_tail_band','compiler_started':False,
 'reason':'Campaign admission forbids starting a >300 MB job while memok exits 1. lean_check.py states approximately 4.1 GB compile commitment. No admission override and no Lean certification.'})

statement=('For every integer r>=1, the actual Boolean f_r(x)=(-1)^(sum_{j=1}^r x_(2j-1)x_(2j)) on 2r independent fair bits has P(S)=4^(-r), H_bits=2r, I=r and Delta=r-1+4^(-r). For integer m>=0, applying A043 scalar reserve truncation phi_m separately to every actual integer mixed profile with |mean|<=1, retaining exact h at |mean|>1, has error D_(r,m)=sum_{k=1}^r binom(2r,k)4^(1-k)(phi(t_k)-phi_m(t_k)), t_k=2^(k-1-r). This error is at least 2^(-m-1)(9/8)^r/((m+1)(m+2))-2^(-m-r)/((m+1)(m+2)), and for fixed m is asymptotic to 4(9/8)^r/(m+1). Hence no dimension-independent K_m bounds D_(r,m) by K_m Delta. If r is a positive multiple of four and m+1<=2^(r/4-1), D_(r,m)>=[(9/8)^r/18-2^(-r-1)]/(m+1). The complete uniform reference Q=P instead has ordinary KL zero and full cross entropy 2I. This refutes only the all-profile approximation extension, not A043 singleton theorem or FEI.')
hyp=['Physical independent fair bits; no repeated wires.','r is an integer >=1 and m is an integer >=0.','h(t)=t^2 ln(1/t^2), continuous zero at t=0; phi=2t(1-t)-h(t); phi_m=t(1-t)sum_{j=1}^m 2(1-t)^j/[j(j+1)] on [0,1].','All cofactor profiles and packets come from the SAME Boolean function.','Growing-order clause requires r divisible by four and m+1<=2^(r/4-1).','Natural units for residuals and approximation error; H_bits explicitly uses log base two.']
cid='A044-ALL-PROFILE-TRUNCATION-BENT-OBSTRUCTION'
claim={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hyp,
 'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest(),
 'contributors':['A044/account03'],'proof_source':{'run':run,'path':'PROOF.md','sha256':sha(R/'PROOF.md')},
 'proof_dependencies':['Direct two-bit Walsh tensorization, physical mixed-profile Parseval, positive log series and finite tail telescope; reconstructed in PROOF.md.'],
 'review_records':[],'status':'AUTHOR_PROOF_WITH_EXACT_FINITE_VALIDATION_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':['Unsupported dimension-independent error extension of fixed-order singleton hierarchy to all mixed profiles, even with exact zero-mean refunds and all negative higher-mean terms retained.'],
 'first_unproved_line':None,'next_consumers':['A043','A042','A045','A090','A091','A094']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
js(R/'CLAIMS.json',[claim])
next_action='Construct one complete merged/conditional reference before approximating local reserves; test it on full-support bent tensors and AND admission controls, retaining normalizer, ordinary KL, exact signed refunds, degree-weighted owners and both full terminal laws. A043/A090/A091 independently reconstruct the new truncation obstruction.'
progress={'protocol_revision':protocol['revision'],'run_id':run,'stream':'B09','packet_id':'A044',
 'gap_id':'A044-SIGNED-PROFILE-BOUNDED-CONGESTION','attempt_id':'substantive6-all-profile-truncation',
 'method':'Consume A043 hierarchy and A042/A045 endpoint/admission objections; explicit Boolean tensor stress family; analytic all-dimensional lower bound plus integer Walsh/Fraction checks.',
 'mathematical_delta':'Fixed all-profile reserve truncation has exponential error ~4(9/8)^r/(m+1) on explicit bent tensors with H_bits=2I. Growing-order lower bound and complete uniform-reference calibration isolate approximation congestion even when no means vanish and negative refunds are retained.',
 'deliverable_status':'COMPLETE_LOCAL_PENDING_INDEPENDENT_REVIEW','mathematical_status':'UNIVERSAL_FEI_OPEN; NARROW_OBSTRUCTION_AUTHOR_PROOF',
 'claim_versions_used':['A044 stage5 physical mixed-profile scaling (reconstructed)','A043 stage17 reserve hierarchy scalar identity (reconstructed)','A042 stage7 endpoint certificates and A045 stage6 admission obstruction (consumed as scope constraints, not premises of obstruction)'],
 'claims_created_or_changed':[cid+'@1'],'source_artifacts':['PROOF.md','out/CHECK.json','out/PILOT_FAILURE.json','out/SOURCE_RECEIPTS.json','out/FORMAL_CHECK.json'],
 'next_consumers':['A043','A042','A045','A090','A091','A094'],
 'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Universal complete-reference payment remains unproved.','Lean compilation not started because memok returned 1.','Independent review, supervisor adoption, brain ingestion and remote mirror verification not observed.'],
 'packet_ids':['A044']}
assert set(progress)=={k.split(' (')[0] for k in protocol['required_per_run']['progress_fields']}
js(R/'PROGRESS.json',progress);js(R/'PACKET_DELTA.json',progress)

sample=next(x for x in check['rows'] if x['r']==256 and x['m']==16)
ratio=float(__import__('fractions').Fraction(sample['D_over_Delta_lower']))
report=f'''# A044 stage17 / substantive6: all-profile truncation obstruction

## exact target, quantifiers, hypotheses and units

Full uniform-cube FEI remains OPEN. This stage tests a precise candidate extension of A043's finite singleton reserve hierarchy to every actual integer mixed cofactor profile. For every r>=1 use the explicit fair-input Boolean bent tensor f_r=(-1)^(sum x_(2j-1)x_(2j)); for every fixed finite order m>=0 the summed approximation error divided by Delta tends to infinity. Natural logarithms measure error; the true spectral entropy in bits is exactly H=2r=2I. PROOF.md gives all formulas, a quantitative lower bound, the exact fixed-order asymptotic 4(9/8)^r/(m+1), and a growing-order bound. This is a narrow universal-route obstruction, not a new FEI counterfamily or a broad class claim.

## sources actually read, revisions and theorem locators

Read execution-v2 in full, README/CURRENT_STATUS, claim and obstruction registries, the A044 packet and B09 dispatch entries, B09 campaign-plan locators, supplemental campaign/claims/controls/seed/mapping context, current BOARD snapshot2026-10-22 22:38UTC, B09 STREAM_NOTES v2 dated2026-10-11, and own STATUS/WORKLOG/LEARNED and substantive stage5 proof. The original common-mean task is already retired; later account05 marker directories supplied no new mathematical report. Current owner FULL-FEI-ONLY control and this invocation's later campaign endpoint govern rather than the older protocol endpoint.

Read current original PROOF.md files from A043 run20261022T210449Z (singleton hierarchy and fixed-order prime corner), A042 run20261021T221439Z (uniform zero/unit endpoints), and A045 run20261021T165712Z (exclusive inherited-profile admission failure). This stage keeps those source claims unchanged. Read relevant threshold paper Section7 Proposition7.1/Corollary7.2 composition formulas, version locators of the 29pp predecessor, and percolation abstract/scope and product-measure pivotal-entropy theorem with earlier-version locators; neither percolation entropy nor the old composition theorem is a premise of the new obstruction. The threshold txt is cp1252, not UTF-8: an initial strict UTF-8 read failed and was retried explicitly with cp1252, without modifying the source. Source byte hashes are in out/SOURCE_RECEIPTS.json. Math recall returned general FEI/chain-budget warnings and no answer to the new truncation target; none is a premise.

## complete derivation or exact first unsupported line

Every two-bit factor has four Walsh coefficients of magnitude1/2, so the tensor has full support P(S)=4^(-r), H_bits=2r, I=r and Delta=r-1+4^(-r). For each degree k actual integer mixed profiles have absolute mean t_k=2^(k-1-r) and second moment2^(k-2). Their exact local reserve is2Var-h(t)=2(EZ^2-t)+phi(t) for t<=1. Keeping exact h when t>1 and replacing phi by its finite positive hierarchy at every remaining profile produces the exact error D in PROOF.md equation(2). All means are nonzero, so an exact zero-mean refund cannot remove it.

The first omitted scalar tail term plus a paired binomial sum proves D>=[2^(-m-1)/((m+1)(m+2))](9/8)^r-2^(-m-r)/((m+1)(m+2)). Delta<=r proves divergence at each fixed m. A binomial change of measure with an explicit Chebyshev event split gives the exact asymptotic; the proof states the boundedness and exceptional-event probabilities before taking the limit. A finite telescoping band and Markov bound give the growing-order lower bound. All cases r>=1 and m=0 are retained, and t=0,1 carry no quotient. The separate complete uniform reference Q=P is normalized, has KL0 and costs2I exactly, including the empty atom.

The first unsupported universal line is a complete merged/conditional-reference inequality with O(Delta) payment from the same unused owner. Applying the singleton error theorem after summing all submasks is now refuted; preserving negative large-mean charges and zero-mean refunds does not rescue this finite-order approximation. No claim is made that every joint reference, adaptive hierarchy or degree-weighted allocation fails. A043's valid singleton hierarchy is not refuted.

## executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json precedes the pilot. Command from A044: `python -X utf8 runs/{run}/code/check_stage.py`. First pilot failed the signed-mean comparison because Walsh characters were written as(-1)^x whereas physical mixed differences use2x-1; the required(-1)^k was missing. out/PILOT_FAILURE.json preserves the failure and exact reconstruction diff. Repair changes the checker convention, not the absolute-mean mathematics.

Repaired pilot PASS: {check['exact_assertions']} exact assertions; all physical spectra at n=2,4,6 and all81 nonempty profiles;120 closed-form cases with frozen r and m domains; boundary/monotonicity/telescope checks. Runtime {check['runtime_seconds']:.6f}s. Integer Walsh and Fraction calculations independently check physical profile means, second moments and strict-superset Parseval. The scalar error is an exact rational-plus-rational-times-ln2 expression;64 atanh terms enclose ln2 with tail<=2(1/3)^129/[129(1-1/9)]. Both fixed/growing lower-bound signs are rigorous interval comparisons, not float evidence. Example r=256,m=16 has certified D/Delta>{ratio:.3g}; this diagnostic is derived from its saved rational lower endpoint. Finite cases supplement the all-r proof and do not establish full FEI.

Estimated memory100MB, observed peak unmeasured; no heavy/GPU/detached process or dimension escalation. For the requested Lean check, memok returned1: physical free2.7GB below4.0GB. No compiler was started. code/tail_band.lean records the scalar target; out/FORMAL_CHECK.json records admission. Mathematical rung: author proof with exact finite validation, pending independent review; NOT Lean-checked. The singleton series identity itself is proved analytically, not by that uncompiled scalar file.

## proof dependencies and changed downstream conclusions

Critical steps use explicit Boolean tensor realizability, physical mixed-profile Parseval, a positive summable logarithm series, finite binomial pairing, Bernoulli/Markov/Chebyshev bounds. They are derived in PROOF.md. A043 motivates the attempted extension but its statement is not altered. A042/A045 are consumed to retain endpoint/sign/admission boundaries; exclusive fragment realizability is never assumed. This stage closes only the finite-order all-profile approximation route. It supplies a full-support stress test that is stronger than stage5's zero-mean parity control. No universal FEI constant improves.

## one next mathematical action and independent reviewer

{next_action} The next proof must sum or condition the complete reference before approximating individual reserves; repeating fixed-order all-submask approximation is ruled out by this actual Boolean family. Review assignments are handoffs recorded here, not claims that another agent has read or accepted them.

## actual persistence receipts or precise save blocker

The four protocol files, PROOF.md, frozen spec, failed-pilot record, checker and PASS output, source hashes and formal admission record are saved locally in this run. CLAIMS and PROGRESS use exactly the protocol field sets, and PACKET_DELTA is byte-identical to PROGRESS. The saver checks schemas, statement/proof hashes, file sizes and the final bridge. Rolling STATUS has two lines; WORKLOG and LEARNED are updated. No git, messages, shared source edits, brain writes or external publication is performed. Supervisor copy, durable brain ingestion and remote mirror verification remain unobserved. The wake warned about stale owner-model/state-of-mind notes; this was disclosed and those notes were not mathematical premises.

**Universal bridge:** This stage advances C020 whole-set witness cost through B09's signed mixed-profile interface by ruling out a specific unpaid extension: finite local polynomial reserves have exponentially growing summed error even on full-support Boolean bent tensors with a complete normalized reference costing exactly2I. It adds an explicit lower bound and a growing-order constraint, while preserving the singleton theorem and all endpoint/admission conditions. The remaining step is to construct and pay one merged or conditional complete reference with bounded degree-weighted ownership and both terminal laws. Testing that step against this obstruction and AND admission is the shortest route forward because another isolated gate inequality or fixed-order reserve grid cannot address the proven all-submask approximation failure.
'''
write(R/'REPORT.md',report)
write(A/'STATUS.md','STATE: A044 substantive6 saved: fixed all-profile reserve truncation error grows as4(9/8)^r/(m+1) on actual full-support bent tensors with H=2I;1591 exact checks PASS; review pending; FEI OPEN.\nNEXT: A043/A042/A045/A090/A091 review; sum one complete merged reference BEFORE local approximation, preserving signed refunds, ordinary KL/normalizer, degree owners and both full terminals.\n')
for name,line in [
 ('WORKLOG.md',f'{now}: Substantive6 consumed A043 hierarchy/A042 endpoints/A045 admission. Proved explicit bent-tensor all-profile truncation obstruction and exact exponential asymptotic; complete uniform reference still costs2I. First pilot sign-convention error preserved/repaired;1591 exact assertions/120 formula cases/81 actual profiles PASS in{check["runtime_seconds"]:.6f}s. memok1 held Lean; no compiler started. Full protocol bundle saved locally; independent review/mirrors pending; FEI OPEN.\n'),
 ('LEARNED.md','Substantive6: Singleton reserve error does NOT extend to all mixed profiles. On fair bent f_r=(-1)^(sum pair products), P(S)=4^-r,H_bits=2r,I=r,Delta=r-1+4^-r; every nonempty profile has |mean|=2^(|S|-1-r)>0 and E Z^2=2^(|S|-2). Replacing scalar phi by fixed-order phi_m at all |mean|<=1, retaining exact negative larger-mean terms, has summed error D~4(9/8)^r/(m+1), hence no O(Delta) fixed-order bound. An explicit all-r lower bound and growing-order bound are in this run/PROOF.md. Zero-mean refunds alone miss this full-support control. The complete uniform reference Q=P has KL0 and cost2I: sum/merge the whole reference BEFORE local approximation. A043 singleton hierarchy remains valid; this is no FEI counterexample.\n')]:
    p=A/name
    with p.open('a',encoding='utf-8') as f:f.write('\n'+line)

assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert set(json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'))[0])==set(protocol['required_per_run']['claim_fields'])
assert sha(R/'code/check_stage.py')==check['helper_sha256']
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
files=[p for p in R.rglob('*') if p.is_file()]
assert all(p.stat().st_size<20_000_000 for p in files)
js(R/'out/SAVE_RECEIPT.json',{'saved_at_utc':now,'status':'PASS','files':[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files],'independent_review':'PENDING','brain_ingestion':'UNVERIFIED','remote_mirror':'UNVERIFIED','schema_checks':'PASS','full_FEI':'OPEN'})
print(json.dumps({'status':'SAVED','run_id':run,'files':len(files)+1,'exact_assertions':check['exact_assertions'],'full_FEI':'OPEN'}))
