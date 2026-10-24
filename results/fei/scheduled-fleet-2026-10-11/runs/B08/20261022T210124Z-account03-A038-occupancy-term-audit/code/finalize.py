import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];A=R.parents[1];B=A.parents[1]
stamp=datetime.now(timezone.utc).isoformat()
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def receipt(p):return {'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
C=read(R/'out/MIXED_CHECK.json');assert C['status']=='PASS'
def bounds(key):return tuple(F(x) for x in C[key])
def small(key):
 a,b=bounds(key);g=10**9
 return '['+str(F((a*g).__floor__(),g))+', '+str(F((b*g).__ceil__(),g))+']'
rows=C['rows'];allnegative=all(F(x['incremental_conversion'][1])<0 for x in rows)
assert C['reference_only_rows_second_query']>0
proof=f'''# Inherited occupancy reference through a non-flat data exposure

All information is in bits. The physical input bits x,a,b,y0,y1,y2 are independent and uniform. Put v(y)=(-1)^y2*(1-2*1[y0=y1=0]). Define F=(-1)^a on x=0; on x=1 put F=v when b=1 and F=+1 otherwise. This is the actual priority descendant after the essential original u0=0 exposure of u=(-1,-1,-1,+1). Query a, then y0 in both a children. The four terminal functions are all nonconstant. A039 already covers this three-bit core; the present result is an independently implemented fixed-substatement reproduction, not a new class theorem.

## Exact original reference

For P(S)=Fhat(S)^2 let z=1-P(empty)=15/16 and r=(8/15,8/15,4/15,2/15,2/15,4/15). Let c be the unique positive root of 1-c=(1-8c/15)^2(1-4c/15)^2(1-2c/15)^2. The source-defined nonempty law Q_r is product Bernoulli(c r_i) conditioned on nonempty. Complete it once as M(empty)=1-z and M(S)=z Q_r(S) for nonempty S. Thus A=D(P||M)=z K_occ. No child reference or projection is substituted into M.

The 42-step rational bracket for c is in MAJORITY_CHECK. Its endpoints have opposite polynomial signs. On [3/4,1], the positive terms in the derivative of the product decrease, and their sum at 3/4 is strictly below 1 (checked rationally). Hence the polynomial is strictly decreasing on that interval and the bracket selects its only root there. Source maximum-entropy uniqueness identifies this as the canonical positive root. Direct interval sums enclose normalization 1 and each original spectral marginal.

## Physical kernel, including all reference-only rows

At a node, write u=Fhat(T), w=Fhat(T+i). The source row mass is u^2+w^2. If nonzero, set k_s(T)=(u+(-1)^s w)^2/[2(u^2+w^2)]; otherwise set both k_s(T)=1/2. Push an incoming JOINT reference m by m_s(T)=[m(T)+m(T+i)]k_s(T). No row is dropped. In particular a source-zero row with positive reference mass still contributes. The kernel is stochastic by (u+w)^2+(u-w)^2=2(u^2+w^2), and its push of the source is exactly one half of the actual physical child spectrum. The checker verifies this identity atom by atom at both levels, independently comparing direct child Fourier sums and physical edge influences.

Let q_s=sum_T m_s(T), Q_s=m_s/q_s. Actual physical outcomes are fair at both levels, including conditional on the first outcome. All reference prefix masses used as denominators are strictly positive. Write O1=D(Unif2||q_a) and O_s=D(Unif2||q_(y0|a=s)). The second-stage reference is the SAME pushed m_s; reference-only rows have fair fallback even after conditioning. There are {C['reference_only_rows_second_query']} source-zero erased rows across the second-level nodes.

## Debit and ownership

TC(g)=sum_j h2(Inf_j(g))-H(g). With g_s=F restricted at a=s and g_st further restricted at y0=t, define

    D1 = O1 + (TC(g_0)+TC(g_1))/2 - A,
    d_s = O_s + (TC(g_s0)+TC(g_s1))/2 - TC(g_s),
    W = [D1]_+ + ([d_0]_+ + [d_1]_+)/2.

The KL chain rule on the actual history probabilities gives O_history=O1+(O_0+O_1)/2. Therefore

    D1+(d_0+d_1)/2 = O_history+average_(s,t) TC(g_st)-A.

This is a potential comparison against the original transported reference. Intermediate TC is the booked comparison potential; its Bayes KL is never reintroduced as a new spendable bank. Positive bookings W dominate the net signed conversion even if negative terms are left unspent. The original occupancy account A is subtracted only once. This is NOT a procedure that physically resets to products at the first level and then claims to carry the old Bayes law.

Dedicate the original actual mean child certificate S0=average_s[4I(g_s)-H(g_s)]. Independently retain Sfinal=average_st[4I(g_st)-H(g_st)]. No FEI premise is used: all these are exact finite Boolean laws. The outward rational certificate gives

    D1 in {small('first_conversion_D1')},
    W in {small('positive_bookings')},
    S0 in {small('original_mean_child_surplus')},
    Sfinal in {small('final_mean_surplus')},
    S0-W in {small('remaining_original_bank')},
    Sfinal-W in {small('remaining_final_surplus')}.

The strict certificate W<min(S0,Sfinal) pays this specified conversion from one original certified account, retaining every terminal entropy. Both second-level signed increments are strictly negative: {allnegative}. Their full rational intervals and conditional outcome bills are in MAJORITY_CHECK. These signed savings are not called extra influence or renewed reserves.

## Exact certificate and scope

code/check.py enumerates this single 64-point truth table, 2 children and 4 terminals. Fourier coefficients and influence are exact rational numbers. Each logarithm uses range reduction into [1,2] and 24 terms of ln(q)=2 sum t^(2j+1)/(2j+1), with t=(q-1)/(q+1) in [0,1/3] and remainder at most 2t^49/[49(1-t^2)]. ln(2) has a positive enclosure and division reverses the denominator endpoints as required. Every interval operation rounds outward on denominator 10^24. All strict signs compare rational endpoints, never floating values. The transcript is the finite certificate; its {C['assertions']} assertions and {C['runtime_seconds']:.8f} second runtime cover only the frozen domains. This is an author-checked exact certificate, independent review pending.

The first unsupported universal step is preserving such positive inherited-reference payment and terminal eligibility for an arbitrary Boolean signed core and a genuinely general next query, with already spent budgets. This fixed non-flat coherent query does not establish that step or full FEI. The already archived K_occ-for-K_full substitutions remain refuted.
'''
(R/'PROOF.md').write_text(proof,encoding='utf-8')
statement='For the fixed uniform six-bit Boolean priority descendant F=(-1)^a when x=0, and F=Maj3(y0,y1,y2) when x=1,b=1, otherwise +1, transport the original completed canonical occupancy reference M through query a followed by y0 in both children, using the actual signed coherent kernel and fair zero-source-row fallback. Put A=D(P||M)=15 K_occ/16, D1=O_a+mean TC(child)-A, d_s=O_y|a=s+mean TC(grandchild|s)-TC(child_s), and W=[D1]_++mean[d_s]_+. Then W<min(mean_child(4I-H),mean_grandchild(4I-H)). Both complete terminal laws in each branch are retained; no reference is renewed and the original occupancy credit is subtracted only once. The exact intervals, root bracket, all physical spectra and reference-only rows are certified in out/MAJORITY_CHECK.json. This is a finite specified-source certificate; full FEI and arbitrary-core ownership remain open.'
hyp=['Exactly the stated actual six-bit truth table and physical query tree; independent uniform coordinates; bits.','Completed canonical root reference specified in PROOF; positive root bracket in the certificate.','Every source-zero/reference-positive row uses fair fallback at both queries.','Intermediate product TC is a comparison potential, not a physical reset followed by reuse of an old reference.','One dedicated previously unused original mean child S4 account; all four actual terminal entropy bills remain.']
claim={'claim_id':'A038-NONFLAT-INHERITED-REFERENCE-TWO-QUERY','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),'contributors':['A038'],'proof_source':{'run':R.name,'path':'PROOF.md','certificate':'out/MAJORITY_CHECK.json','code':'code/check.py'},'proof_dependencies':['Canonical nonempty maximum-entropy reference, account02/B15 Theorem 2.1, source checkpoint 2bf247373576eb406ca91bb3ea5f3ce5e5ab8588; exact source copy in A038 stage1.','Finite KL chain rule and actual signed physical row kernel reconstructed here.','Direct integer Fourier and physical edge enumeration; no universal FEI or arbitrary child slack premise.'],'review_records':[],'status':'EXACT_FINITE_CERTIFICATE_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A039','A047','A050','A088','A094','B20']}
save(R/'CLAIMS.json',[claim])
next_action='A039/A047/A050 replace this certified inherited profile by an unequal signed core where a positive next-query conversion survives; retain original Q, first booked debit, both terminals and unused S4. A088/A094 independently reconstruct the exact finite certificate.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B08','packet_id':'A038','gap_id':'G-A038-OWNED-SELECTOR-RESET-TRANSFER','attempt_id':'A038-owned-selector-transfer-4','method':'Source-exact canonical occupancy reference; complete actual two-query finite tree with reference-only rows and one unchanged original terminal surplus account','mathematical_delta':'One explicit non-flat coherent data query is certified with the SAME inherited canonical reference and all four nonconstant terminals. Exact positive bookings fit both original and final actual S4 certificates; all reference-only rows retained. No universal constant changes.','deliverable_status':'COMPLETE_LOCAL_EXACT_FINITE_CERTIFICATE','mathematical_status':'FINITE_SOURCE_INTERFACE_CLOSED_UNIVERSAL_OWNERSHIP_OPEN','claim_versions_used':['Canonical K_occ account02/B15 Theorem 2.1 at checkpoint 2bf247373576eb406ca91bb3ea5f3ce5e5ab8588','A038 stage5 original child-surplus ownership interface, scoped continuation only'],'claims_created_or_changed':[claim['claim_id']+'@1'],'source_artifacts':['REPORT.md','PROOF.md','CLAIMS.json','code/check.py','code/finalize.py','out/FROZEN_SPEC.json','out/SUPPLEMENT_SPEC.json','out/CHECK.json','out/MAJORITY_CHECK.json'],'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Arbitrary inherited non-flat signed core payment is unsupported.','Exact current Brain recall did not return the definition; original source-exact checkpoint was re-read; fresh remote-current-definition verification is not claimed.','New independent review, supervisor copying and mirror verification are unobserved.'],'packet_ids':['A038']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

Close the saved next-data ownership test on one actual non-flat core, carrying the same original canonical occupancy reference, including reference-only rows and both full terminal laws. Uniform independent Boolean physical inputs; all entropy and KL in bits. The exact target, tree, debit and original surplus account are in PROOF. The finite certificate gives W<min(S0,Sfinal), with W in {small('positive_bookings')}; all four terminals are nonconstant. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Read full EXECUTION_PROTOCOL revision 2026-10-11-execution-v2, machine AGENTS and current scheduled FEI owner control. Current user deadline 2026-10-23 14:49 UTC supersedes old October 21 dates in campaign snapshots. Read BOARD snapshot 2026-10-22 21:06 UTC, unchanged B08 lead v2, own STATUS/LEARNED/WORKLOG, and populated A038 stage1 through stage5 reports; inspect exact stage5 proof and checker. Later account05 directories contained only markers; they are not counted as completed mathematics. Campaign README/CURRENT_STATUS, relevant registry/packet/next-action entries, plan and supplement CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING were inspected. Paper text interfaces are orientation, not new proof premises; no whole-paper re-audit is asserted.

The math recall returned no answering occupancy card (WEAK MATCH). Main Brain recall likewise returned no exact formula and reported an unsuccessful internal refresh spawn. No authored Brain write or refresh is performed. The exact source is re-read from A038 stage1 OCCUPANCY_TARGET_SOURCE and archived K_OCC_DEFINITION: original account02/B15 Theorem 2.1 and Section 4, checkpoint 2bf247373576eb406ca91bb3ea5f3ce5e5ab8588, blob 5ce14eaaec34f0d91f2d430dba576e19dddc6894. K_occ=Hmax(r)-H(P_nonempty)=D(P_nonempty||Q_r) is retained exactly. Fresh default-branch retrieval is unverified and not claimed. Neither full product TC nor a newly invented occupancy candidate is substituted.

# complete derivation or exact first unsupported line

PROOF gives the actual truth table, exact root marginals, canonical positive-root characterization, rowwise common kernel with fair zero-source extension, history KL chain rule and nonrenewed debit telescope. It distinguishes the intermediate TC comparison potential from an actual reset of the transported reference. The original account A appears only once. Exact finite terminal laws independently certify S0 and Sfinal; no FEI premise is used. First unsupported universal line: the same ownership/terminal eligibility under arbitrary inherited signed cores and further already-spent histories. No universal FEI constant or quantifier is improved.

# executed validation with domain, arithmetic, commands and outputs

Frozen FROZEN_SPEC precedes the five-bit point-defect fixture. It passed 34 assertions in 3.05384930s, but its signed bookings vanish and its second-query source-zero rows are absent. That weak test is retained in CHECK, not presented as the desired support test. SUPPLEMENT_SPEC then freezes a separate fixed six-bit Maj3 fixture, with no automatic dimension escalation. Final command: python -X utf8 -B code/check.py --majority. Output: {C['status']}, {C['assertions']} exact assertions, {C['runtime_seconds']:.8f}s. All {C['reference_only_rows_second_query']} second-level reference-only rows and all four nonconstant terminal functions are retained.

Direct integer character sums, Fraction influence counts, exact polynomial bisection, and outward rational log intervals certify the signs. Checks include root uniqueness on the bracket, reference normalization/marginals, exact physical source push at both levels, terminal entropy and signed history telescope. No floating comparison proves a sign. Frozen memory estimate 60MB; no large search, GPU, detached worker or >300MB certificate job. Lean is a separate limited row-algebra check if its tool receipt succeeds; no Lean certification of the full information statement is claimed without that receipt.

# proof dependencies and changed downstream conclusions

The original canonical projection definition, elementary finite probability/KL algebra and actual finite Boolean spectra suffice. Prior parity payment is a scoped interface, not an arbitrary-core premise. Existing source-complete claims are not overwritten. This is a scoped repair/certificate of that pending reference-support interface, not another broad universal candidate. A039/A047/A050 may consume this explicit original-reference continuation; A088/A094 should reconstruct it independently. Shared-index adoption and downstream use are unobserved.

# one next mathematical action and independent reviewer

{next_action} The next test must force a positive additional inherited-reference bill; repeating a negative-reset example would not test the remaining payment mechanism.

# actual persistence receipts or precise save blocker

All required run files, code, frozen domains and exact outputs are local under the authorized A038 directory. STATUS is two lines; WORKLOG and LEARNED append this result. out/RECEIPTS records observed readback hashes, schema checks and compatibility equality. No git, other-agent write, shared-index write, authored Brain write, mail or publication occurs. Supervisor copying, remote mirror verification and independent review are pending. Session wake warned that owner-context notes were stale; the conversational alert was delivered before relying on them.

Universal bridge: This stage moves the C024 history-transfer/C019 terminal-ownership interface by certifying one complete non-flat two-query continuation under the SAME original occupancy reference, with reference-only rows and all four nonconstant terminal entropy bills, using no renewed KL or surplus bank. It changes no universal FEI constant. Arbitrary signed inherited profiles and positive further conversion costs remain unpaid; the shortest NEXT is a prescribed next query with a strictly positive additional inherited-reference bill, since another negative-reset class test cannot resolve that universal ownership obstruction.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text(f'STATE: A038 stage6 local exact non-flat inherited-reference certificate saved; {C["assertions"]} checks; reference-only rows and all four terminals retained; FEI OPEN, review pending.\nNEXT: A039/A047/A050 force a positive next-query inherited-reference conversion from SAME unused original S4 with first booking and both terminals; A088/A094 review.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+' '+R.name+': read current board, source-exact occupancy checkpoint and populated prior stages; later marker-only stages not treated as results. Five-bit fixture passed but had zero positive debit and no reference-only rows. Separately froze fixed Maj3 six-bit non-flat continuation; original reference never reset, all four nonconstant terminals and reference-only rows retained. '+str(C['assertions'])+' exact assertions in '+str(C['runtime_seconds'])+'s; complete positive bookings fit original and final certified child surplus. Universal ownership remains open; independent review pending.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n## Stage 6: inherited reference through a non-flat physical query\n\n- Carry original completed M through both a and y0 kernels. Intermediate product TC is a comparison potential, not an actual reset followed by reuse of the old reference.\n- Exact telescope: D1+mean d_s=O(history)+mean TC(final)-original A; positive bookings W=[D1]+ +mean[d_s]+ must fit the SAME original certified account and retained final terminal surplus.\n- Maj3 priority fixture in PROOF certifies this complete interface with reference-only rows and all four terminals nonconstant. Full rational bills are in out/MAJORITY_CHECK.json. No arbitrary-core or universal FEI conclusion follows.\n- The earlier point-defect fixture had zero positive bookings and no second-query reference-only rows; it does not validate a positive-debt payment mechanism. The next useful target must force a positive additional inherited-reference bill.\n')
protocol=read(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
pf=set(protocol['required_per_run']['progress_fields']);pf.remove('packet_ids (one primary ID, for compatibility)');pf.add('packet_ids')
assert set(progress)==pf and set(claim)==set(protocol['required_per_run']['claim_fields'])
assert all(x in report for x in protocol['required_per_run']['report_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[p for p in R.rglob('*') if p.is_file() and p.name!='RECEIPTS.json']
assert all(p.stat().st_size<20*1024**2 for p in files)
source=[B/'BOARD.md',B/'claude/B08/STREAM_NOTES.md',A/'runs/20261011T221733Z-account05-A038-occupancy-term-audit/OCCUPANCY_TARGET_SOURCE.md',A/'runs/20261014T051947Z-account05-A038-occupancy-term-audit/PROOF.md',Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')]
save(R/'out/RECEIPTS.json',{'schema_status':'PASS','saved_at_utc':stamp,'progress_delta_identical':True,'field_sets_exact':True,'all_files_under_20MB':True,'rung':'exact finite certificate; independent review pending','artifact_receipts':[receipt(p) for p in files],'source_receipts':[receipt(p) for p in source],'rolling_receipts':[receipt(A/p) for p in ['STATUS.md','WORKLOG.md','LEARNED.md']]})
print(json.dumps({'status':'PASS','artifact_count':len(files),'checks':C['assertions'],'claim':claim['claim_id'],'all_second_increments_negative':allnegative}))
