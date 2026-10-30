from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

run=Path(__file__).resolve().parents[1]
agent=run.parents[1]
now=datetime.now(timezone.utc).isoformat()
def save(name,obj):
    (run/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()

protocol_dir=Path(r'~\mop_fei100\reports\fei-2026-10-11')
context=Path(r'~\brain_workers\FEI100_20261011\context')
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
potential=Path(r'~\brain_workers\FEI100_20261011\agents\A046\runs\20261011T214251Z-fleet05-A046-current-candidate-intake\FROZEN_POTENTIAL.json')
sources=[]
for name in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','AGENT_ASSIGNMENTS.json','FEI_100_agent_research_plan.tex']:
    p=protocol_dir/name
    sources.append(dict(path=str(p),sha256=digest(p),read_scope='protocol fully read; status/registries and A076 contract/plan sections consulted; long outputs may have been truncated'))
for p in (protocol_dir/'runs').rglob('REPORT.md'):
    sources.append(dict(path=str(p),sha256=digest(p),read_scope='earlier-run report consulted; no pending theorem used as proof dependency'))
for name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']:
    p=supp/name
    sources.append(dict(path=str(p),sha256=digest(p),read_scope='campaign supplement consulted; standard controls not claimed novel'))
for name in ['ADDENDUM_11_26_CRITICAL_RARE_MOMENT.md','ADDENDUM_11_44_COMPONENT_ENTROPY_COUNTEREXAMPLE.md','ERASURE_RIGIDITY.md']:
    p=supp/'sources'/name
    sources.append(dict(path=str(p),sha256=digest(p),read_scope='complete source note read; not a proof dependency of new formulas'))
for name in ['threshold_paper_38pp.txt','threshold_paper_29pp_earlier_version.txt','percolation_spectral_pivotal_entropy_30pp.txt','percolation_spectral_pivotal_entropy_31pp_other_version.txt']:
    p=context/name
    sources.append(dict(path=str(p),sha256=digest(p),read_scope='introductions and selected theorem/composition sections; current threshold Proposition 7.1, eqs 67-70 and Corollary 7.8; percolation Theorems 1.1-1.6 only background; earlier abstracts for supersession'))
board=agent.parents[1]/'BOARD.md'
sources.append(dict(path=str(board),sha256=digest(board),read_scope='complete board read at stage start; snapshot 2026-10-11 21:45 UTC'))
sources.append(dict(path=str(potential),sha256=digest(potential),read_scope='complete intake A046-1 read; used definitions only, no pending helper assumed'))
save('SOURCE_MANIFEST.json',dict(saved_at_utc=now,sources=sources,missing_source='claude/B16/STREAM_NOTES.md absent at start and recheck; B16/runs contains no REPORT.md'))

consumers=['A015','A046','A092','A088','B16','B20']
statements=[
 ('A076-STRUCTURED-SPECTRA',
  'On independent uniform physical bits, threshold f_(n,r)=2*1_{|b|>=r}-1 has coefficient a_k=2^-n sum_(j=0..k,l=0..n-k)(2*1_{j+l>=r}-1)(-1)^j binom(k,j)binom(n-k,l), with multiplicity binom(n,k), and I=n*2^-(n-1)*binom(n-1,r-1) for 1<=r<=n (zero for constant endpoints). For disjoint t tribes of width w, q=2^-w,b=1-q,a=b^t, f=1-2 prod(1-A_j), the empty coefficient is 1-2a and a nonempty set meeting k tribes has coefficient -2*(-q)^k*b^(t-k), with multiplicity binom(t,k)*(2^w-1)^k. I=2twq*b^(t-1) and H=phi((1-2a)^2)+8wtqa-8t(ba-a^2)log2(b)-8(a-a^2). Balanced disjoint substitution has H(F)=H(g)+sum_i Inf_i(g)H(f_i), I(F)=sum_i Inf_i(g)I(f_i). Recursive majority3 depth ell has I=(3/2)^ell, H=4*((3/2)^ell-1), and degree PGF R_ell=(3/4)R_(ell-1)+(1/4)R_(ell-1)^3, R_0=z.',
  ['n>=1,0<=r<=n+1 integers; w,t>=1 integers; ell>=0 integer','entropy in bits; phi(u)=u log2(1/u), phi(0)=0','original inputs uniform; all composing physical blocks disjoint; child outputs balanced for balanced substitution'],
  [],[], 'STRUCTURED_CONTROLS.tex equations (1)-(23)'),
 ('A076-TRIBES-PAYMENT-DISCRIMINATION',
  'Fix lambda>0, q=2^-w,t=floor(lambda/q),a=(1-q)^t and use the preceding uniform tribes. H=8lambda*exp(-lambda)*w+O_lambda(1), I=2lambda*exp(-lambda)*w+O_lambda(wq), hence H/I->4. For A one entire tribe, c=1-4a+4a^2/(1-q),u=4qa^2/((1-q)c), M_A=c*h2(u)+(1-c)*h2(q)+4qa*log2(2^w-1), I_A=2wq*(1-q)^(t-1), L_A=H_(w,t)-(1-q)H_(w,t-1), J_A=L_A-M_A and Delta_A=0. If lambda!=ln2, M_A/I_A->4,J_A/I_A->0,L_A/I_A->4. If lambda=ln2, M_A/I_A->3,J_A/I_A->1,L_A/I_A->4. Thus universal M_A<=K I_A or L_A<=K I_A requires K>=4. Additionally the marginal code M=sum_i h2(Inf_i) obeys M/I=w-1+(lambda+1)log2(e)+O_lambda(q), whereas H(|S|)=O_lambda(log w) and H(S||S|)/I->4. Recursive majority3 gives M/I=ell+log2(e)+O(2^-ell), H(|S|)=O(ell), H/I->4 and H/(I-Var)=4 for ell>=1. These refute only a dimension-free payment of the independent-marginal code and any universal H<=C[H(|S|)+Var], not FEI or the B09 helper.',
  ['lambda fixed positive, w->infinity integers; t=floor(lambda*2^w)>=1','original inputs uniform and all tribes disjoint','M_A denotes conditional spectral block entropy, J_A actual physical-restriction mutual information; H(S||S|) means H(S conditional on |S|)','all influence includes every physical input'],
  ['A076-STRUCTURED-SPECTRA@1'],['M(f)<=K I(f) for a universal finite K, with M=sum_i h2(Inf_i(f))','H(f)<=C[H(|S|)+Var(f)] for a universal finite C'],
  'STRUCTURED_CONTROLS.tex equations (11)-(17),(20)-(22),(24)-(29)')
]
claims=[]
for cid,statement,hyp,deps,refutes,locator in statements:
    claims.append(dict(claim_id=cid,version=1,exact_statement=statement,hypotheses=hyp,
      statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['A076'],
      proof_source=dict(path=str(run/'STRUCTURED_CONTROLS.tex'),locator=locator,validation=str(run/'out'/'VALIDATION.json')),
      proof_dependencies=deps,review_records=[],status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=refutes,
      first_unproved_line=None,next_consumers=consumers))
save('CLAIMS.json',claims)

discrimination=dict(candidate=dict(candidate_id='B09-BIASED-BLOCK-UNCERTAINTY',candidate_version=1,intake_version='A046-1',source_path=str(potential),source_sha256=digest(potential),formula='P_A=M_A+Delta_A',source_status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',source_used_as='definitions only'),
  controls=[dict(family='tribes t=floor(lambda*2^w),lambda!=ln2, A one tribe',P_A_over_I_A_limit=4,J_A_over_I_A_limit=0,L_A_over_I_A_limit=4,Delta_A=0),dict(family='tribes t=floor(ln2*2^w), A one tribe',P_A_over_I_A_limit=3,J_A_over_I_A_limit=1,L_A_over_I_A_limit=4,Delta_A=0),dict(family='recursive-majority3 depth ell',H_exact='4*((3/2)^ell-1)',I_exact='(3/2)^ell',marginal_code_over_I='ell+log2(e)+O(2^-ell)',size_entropy_upper_bound='log2((3/2)^ell+1)+log2(e)')],
  downstream_conclusions=['Whole-tribe local potential payment P_A<=K I_A needs K>=4; balanced-only tribes force K>=3.','Actual entropy-drop payment L_A<=K I_A needs K>=4.','The B09 helper is not refuted or independently accepted.','Independent-coordinate marginal coding has a divergent excess; cardinality-only coding leaves asymptotically all full entropy unpaid.','No full-FEI conclusion follows.'],proof_locator='STRUCTURED_CONTROLS.tex equations (24)-(29)',independent_review='pending A092; alternate A088')
save('CONTROL_DISCRIMINATION.json',discrimination)
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=run.name,stream='B16',packet_id='A076',gap_id='FEI-B16-A076-INITIAL',attempt_id='A076-controls-stage1',method='Exact combinatorial spectra, disjoint spectral substitution, analytic asymptotic error bounds, and independent truth-table/Fraction implementation',mathematical_delta='Exact control ledger plus full-tribe evaluation of the live A046/B09 potential: necessary local payment constant 4, balanced potential ratio 3 and channel ratio 1; marginal overpayment and cardinality underpayment separated.',deliverable_status='COMPLETE_LOCAL_PENDING_INDEPENDENT_REVIEW',mathematical_status='RESTRICTED_CONTROL_TARGET_AUTHOR_PROVED; FULL_FEI_OPEN',claim_versions_used=['A076-STRUCTURED-SPECTRA@1'],claims_created_or_changed=[c['claim_id']+'@1' for c in claims],source_artifacts=['STRUCTURED_CONTROLS.tex','CONTROL_DISCRIMINATION.json','SOURCE_MANIFEST.json','code/check_controls.py','out/FROZEN_SPEC.json','out/BLOCK_VALIDATION_SPEC.json','out/VALIDATION.json'],next_consumers=consumers,next_action='A092 independently reconstruct equations (24)-(29), especially the balanced empty-residual fiber; A046 use K>=4 when freezing a whole-block influence payment.',stagnant_substantive_attempts=0,blockers=['B16 STREAM_NOTES.md absent; no obstacle to independent packet work','Independent review, supervisor ingestion, mirror verification and downstream use not yet observed'],packet_ids=['A076'])
save('PROGRESS.json',progress); save('PACKET_DELTA.json',progress)
validation=json.loads((run/'out'/'VALIDATION.json').read_text())
report=f'''# A076 / B16: threshold and tribes control ledger

## exact target, quantifiers, hypotheses and units

For finite uniform Boolean signs derive exact threshold, tribes and disjoint threshold-composition spectra, including every physical input in influence. Entropy is Shannon entropy in bits. The packet is locally complete with author proofs; full FEI remains OPEN and independent acceptance is pending.

The current intake actually tested is A046-1, `B09-BIASED-BLOCK-UNCERTAINTY@1`, with P_A=M_A+Delta_A. A is one entire tribe and original inputs are uniform, so Delta_A=0. Definitions are reused; the pending helper itself is not assumed.

## sources actually read, revisions and theorem locators

The execution protocol revision is 2026-10-11-execution-v2. The campaign README/status, registries, packet status, stream next actions, A076 assignment, relevant plan sections, earlier B05/B09/B19 reports and supplement CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING were consulted. The board snapshot is 2026-10-11 21:45 UTC; no earlier A076 result appears. B16 STREAM_NOTES.md was absent at start and recheck; no B16 lead report was available.

The current 38-page threshold text, Proposition 7.1 (67)-(70) and Corollary 7.8, was read for the exact composition interface. Introductions and selected theorem sections of all four supplied paper texts were consulted; older abstracts identify superseded versions. Percolation Theorems 1.1-1.6 are background only. Full-paper review and acceptance are not claimed. Three relevant supplemental source notes were read in full. Exact file hashes/read scopes are in SOURCE_MANIFEST.json. A046's complete frozen intake was consumed when it became available during this stage.

## complete derivation or exact first unsupported line

STRUCTURED_CONTROLS.tex is the complete derivation. Equations (1)-(4) give all symmetric-threshold coefficients and odd-majority closed forms. Equations (5)-(10) give exact tribes multiplicities, degree PGF, influence and entropy. Equations (11)-(12) give explicit all-large-w error bounds, yielding H/I->4. Equations (18)-(23) reconstruct balanced disjoint substitution and recursive/mixed majority controls without assuming a biased weighted-threshold theorem.

The new live-candidate substitution is (24)-(29): the full-tribe conditional spectrum yields the exact M_A. Physical restriction is constant with probability q and leaves t-1 tribes otherwise, giving exact L_A and J_A. For t=floor(lambda*2^w), unbalanced lambda!=ln2 gives M_A/I_A->4,J_A/I_A->0,L_A/I_A->4. At lambda=ln2 the three limits are 3,1,4. This forces K>=4 in any universal whole-block M_A<=K I_A or L_A<=K I_A, without establishing that such a finite K exists. The empty residual fiber is exceptional at balance and is treated separately rather than taking a nonuniform limit through lambda=ln2.

Independent marginal coding costs M/I~w for tribes and ~ell for recursive majority, although H/I->4. Spectral-size entropy is only O(log w) or O(ell), so H(S conditional on |S|) retains asymptotically the whole entropy. These are explicitly scoped payment obstructions, not a conjecture disproof. The first still unsupported universal line is a dimension-free, nonreusing payment of actual conditional block cost plus terminal entropy for arbitrary Boolean functions; this run does not assert it.

## executed validation with domain, arithmetic, commands and outputs

Before each validation extension, out/FROZEN_SPEC.json and out/BLOCK_VALIDATION_SPEC.json froze the helpers, domains, counts, arithmetic, symmetry, memory estimate and <=60-second runtime. Command:

`python -X utf8 runs\\{run.name}\\code\\check_controls.py`

The final execution checks {validation['case_count']} actual truth tables: 63 symmetric thresholds (n=1..9, every r=0..n+1), 15 tribes (w,t=1..4,wt<=12), recursive majority3 depths 1 and 2, and majority3-of-majority5 on 15 bits. Integer FWHT and Fraction coefficients independently check every predicted coefficient, Parseval, spectral versus physical-edge influence, closed odd-majority coefficients, active-block multiplicities and all conditional Fourier fibers for the first tribe. Exact recursive-majority entropy is checked using powers-of-two denominators.

Result: **{validation['exact_assertions']} exact assertions passed**, observed helper runtime **{validation['elapsed_seconds']:.3f} seconds**. Floating entropy/channel values are diagnostics, not sign certificates; all infinite-family statements use the analytic bounds in the derivation. The estimate was 30 MB; no >300 MB/heavy job or dimension escalation was used. This is author validation in a different representation, not external independent review.

## proof dependencies and changed downstream conclusions

The spectra are derived directly from Walsh expansion, pivotal counting and elementary probability. Claim A076-TRIBES-PAYMENT-DISCRIMINATION@1 depends on A076-STRUCTURED-SPECTRA@1. A046/B09 contributes definitions only, so rejection of the pending B09 upper bound would not invalidate the derived M_A,J_A,L_A formulas. No upstream unproved inequality is used.

A046 receives an explicit whole-tribe constant obstruction K>=4 and the balanced channel signature (3,1,4). A015 receives an exact ledger showing how whole-set entropy differs from independent-coordinate descriptions. These are handoff recommendations: downstream use has not been observed. Two complete author-proved claims are left for review, respecting the stream's unreviewed-claim cap.

## one next mathematical action and independent reviewer

A092 should independently reconstruct (24)-(29), concentrating on the empty-residual fiber at lambda=ln2; A088 is the alternate reviewer. A046 can substitute these formulas when freezing a nonreusing whole-block payment. Review and subsequent adoption are separate from local artifact completion.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json with packet_ids=[A076], STRUCTURED_CONTROLS.tex, CONTROL_DISCRIMINATION.json, SOURCE_MANIFEST.json, both frozen specs, code and validation output are saved in this assigned run folder. STATUS.md, WORKLOG.md and LEARNED.md are updated only in A076. out/PERSISTENCE_RECEIPTS.json records readback hashes. No git operation, external message, shared-ledger mutation, supervisor upload or mirror receipt is claimed. All files are below 20 MB.
'''
(run/'REPORT.md').write_text(report,encoding='utf-8')
(agent/'STATUS.md').write_text('STATE: A076 local packet complete: exact spectra and whole-tribe live-potential limits (4,0,4) or balanced (3,1,4); 62,798 exact checks; FEI OPEN, independent review pending.\nNEXT: A092/A088 reconstruct balanced empty-residual fiber; A046 apply necessary K>=4 to whole-block payment before any universal claim.\n',encoding='utf-8')
if not (agent/'WORKLOG.md').exists() or 'Stage 1: read protocol, board' not in (agent/'WORKLOG.md').read_text(encoding='utf-8'):
    with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
        f.write(f'\n{now} — Stage 1: read protocol, board and campaign sources; B16 notes missing. Derived exact threshold/tribes/recursive-majority spectra and explicit tribes asymptotic errors. Initial 81-case Walsh validation passed; odd-majority and conditional-block extensions completed with 62,798 exact assertions. Consumed newly available A046-1 intake and derived whole-tribe M_A/I_A,J_A/I_A,L_A/I_A limits: (4,0,4) off balance and (3,1,4) at lambda=ln2. Marginal coding diverges relative to influence; cardinality-only coding underpays. Saved two author-proved claims, external review pending; no FEI solution claimed.\n')
(agent/'LEARNED.md').write_text('''# A076 durable control facts

All entropy units are bits. Physical original inputs are uniform; t=floor(lambda*2^w) balances output by circuit size, not by input bias.

- Threshold coefficients are finite Krawtchouk sums with binomial multiplicities; odd-majority coefficients are exact central-slice binomial ratios. See STRUCTURED_CONTROLS.tex (1)-(4).
- Disjoint tribes have nonempty coefficient -2*(-q)^k*b^(t-k), multiplicity binom(t,k)*(2^w-1)^k, with q=2^-w,b=1-q. I=2twq*b^(t-1); exact H is (9). Fixed lambda=tq asymptotically gives H/I->4 with explicit errors (11)-(12).
- Recursive majority3 on disjoint uniform leaves has I=(3/2)^ell,H=4(I-1),Var=1, and leaf influence 2^-ell. Balanced disjoint substitution is valid; reused physical blocks need a new proof.
- Coordinatewise marginal code sum h2(Inf_i) is an entropy upper bound but its cost/influence grows like w for tribes and ell for recursive majority3. Spectral cardinality entropy is logarithmic in influence and leaves essentially all full entropy conditional within levels.
- Actual A046/B09 potential on A=one whole tribe: Delta_A=0; M_A=c*h2(u)+(1-c)*h2(q)+4qa*log2(2^w-1), c=1-4a+4a^2/b,u=4qa^2/(bc). At fixed lambda!=ln2, (M_A,J_A,L_A)/I_A -> (4,0,4). At lambda=ln2 the limit is (3,1,4). The empty-residual fiber changes order at balance: c~q rather than a positive constant. Do not use the off-balance expansion there.
- Thus local universal M_A<=K I_A and L_A<=K I_A require K>=4. This is necessary only; B09 helper and full FEI are not refuted or accepted by this calculation.
- Exact checks use integer Walsh transforms and Fraction probabilities. Floating entropy output is diagnostic; analytic bounds supply infinite-family comparisons. External independent review remains pending.

Source-complete proof and exact checker: runs/20261011T214703Z-fleet05-A076-threshold-and-tribes-controls/.
''',encoding='utf-8')

protocol=json.loads((protocol_dir/'EXECUTION_PROTOCOL.json').read_text())['required_per_run']
for c in claims: assert set(c)==set(protocol['claim_fields'])
# The protocol annotates this last field as "packet_ids (one primary ID, for compatibility)";
# its compatibility instructions and the owner's explicit requested key are packet_ids.
assert set(progress)=={s.split(' (')[0] for s in protocol['progress_fields']}
assert json.loads((run/'PACKET_DELTA.json').read_text())==json.loads((run/'PROGRESS.json').read_text())
assert all(field in report for field in protocol['report_fields'])
receipts=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        assert p.stat().st_size<20*1024*1024
        receipts.append(dict(path=str(p.relative_to(run)),size_bytes=p.stat().st_size,sha256=digest(p)))
save('out/PERSISTENCE_RECEIPTS.json',dict(saved_at_utc=now,files=receipts,rolling_files=[dict(path=str(agent/name),sha256=digest(agent/name)) for name in ['STATUS.md','WORKLOG.md','LEARNED.md']],schema_check='PASS',external_mirror='NOT_OBSERVED',independent_review='PENDING'))
print(json.dumps(dict(saved_at_utc=now,files=len(receipts),schema_check='PASS',claims=len(claims),exact_assertions=validation['exact_assertions'],run=str(run)),indent=2))
