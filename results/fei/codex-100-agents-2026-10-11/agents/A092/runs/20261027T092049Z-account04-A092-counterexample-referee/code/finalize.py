from pathlib import Path
import hashlib,json,datetime,copy
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
P=A.parent.parent
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def put(name,obj):
    (R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=True)+'\n',encoding='utf-8')
def read(name):return json.loads((R/name).read_text(encoding='utf-8'))
main=read('out/RESULT.json'); audit=read('out/AUDIT_RESULT.json')
assert main['status']==audit['status']=='PASS'
assert main['seconds']<55 and audit['seconds']<55
assert hashlib.sha256((R/'code/verify.py').read_bytes()).hexdigest()==main['helper_sha256']
put('out/LEAN_RECEIPT.json',dict(status='SETUP_UNVERIFIED',command='python -B -X utf8 lean_check.py --core --stmt "example (s t : Bool) : 3 <= ([(s,s), (s,!s), (t,!t), (!t,!t)]).eraseDups.length := by cases s <;> cases t <;> decide"',exit_code=1,output='SETUP_UNVERIFIED: Compute admission held (hung window or under 5500 MB free); no new compiler process',fresh_memok_exit=0,fresh_memok_output='OK: physical free 5.0 GB (need 4.0), commit free 11.7 GB (need 8.0)',scope='finite four-row Boolean alternative only; not the analytic theorem',compiler_launched=False,axioms='not checked; no compiler result'))
sources=[('A080','20261027T015619Z-account04-A080-universal-counterexample-standard','A080-COMPOSITION-PRIME-APPROXIMATION'),('A071','20261027T050628Z-account04-A071-search-space-design','A071-PRIME-CHEAP-TWO-OUTPUT-SUMMARY')]
claims=[]; versions=[]
for agent,run,cid in sources:
    path=P/'agents'/agent/'runs'/run/'CLAIMS.json'
    data=json.loads(path.read_text(encoding='utf-8'))
    c=copy.deepcopy(next(c for c in data['claims'] if c['claim_id']==cid))
    c['review_records'].append(dict(reviewer='A092',verdict='HOLDS_UNCHANGED_AT_STATED_SCOPE',source_claims_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),source_statement_sha256=c['statement_sha256'],reconstruction=str(R/'PROOF.md'),checks=str(R/'out/RESULT.json'),scope='independent analytic reconstruction plus literal truth tables; no contribution to source version; full FEI remains open'))
    c['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE'
    claims.append(c);versions.append(cid+'@'+str(c['version']))
statement=('For every Boolean seed g on n>=1 uniform bits and k>=2 fresh bits, N=n+k, let F(x,z)=g(x)(-1)^{1[wt(x,z)<=1]}. Put D0=sum_i 1[g(0)!=g(e_i)] and D1=sum_{i!=j} 1[g(e_j)!=g(e_i+e_j)]. Then I(F)=I(g)+2^{1-N}[N(N-1)-2kD0-2D1]. Any deterministic finite r-bit summary E(z) from which the entire fresh-block residual row is decodable satisfies sum_j I(E_j)>=k^2*2^{1-k}; no such summary exists for r=1 and equality is attainable for every r>=2. For g=-1 only at 00, I(F_k)=1+(k^2-k+2)*2^{-k-1}, H(F_k)>1 for every k>=32, and H(F_k)->2. Hence H(F_k)/(inf_E sum_j I(E_j)) tends to infinity but H(F_k)/I(F_k)->2. This refutes only universal payment of total entropy from fresh-summary influence alone, not FEI.')
hyp=['all physical inputs are independent uniform bits; Boolean signs; complete squared normalized Fourier entropy in bits', 'summary is a deterministic function of the fresh bits alone and must decode the full residual truth-matrix row', 'summary influence is measured on its actual fresh physical inputs; output independence is not assumed', 'D1 counts edges between weight one and two once; g may be constant for the exact formula', 'explicit counterfamily fixes the two-bit seed with its only negative value at 00; k is an integer >=2']
new=dict(claim_id='A092-EXACT-ORIGINAL-INFLUENCE-AND-SUMMARY-ONLY-NOGO',version=1,exact_statement=statement,hypotheses=hyp,statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),contributors=['A092; A080 arbitrary-seed prime perturbation and A071 sharp two-output summary credited antecedents'],proof_source=str(R/'PROOF.md'),proof_dependencies=versions,review_records=[dict(reviewer='A092 author',verdict='AUTHOR_ANALYTIC_PROOF_WITH_EXACT_FINITE_VALIDATION',checks=['out/RESULT.json','out/AUDIT_RESULT.json'],formal_status='SETUP_UNVERIFIED')],status='PROVED_AUTHOR_INDEPENDENT_REVIEW_PENDING',supersedes=[],refutes=['PROPOSED-STRATEGY-ONLY: an absolute C with H(F)<=C inf_E sum_j I(E_j), for all fresh-block-decodable summaries; not attributed to another agent'],first_unproved_line='For full FEI: pay the retained arbitrary original core from ONE unused original O(I) account, with old bookings and both full terminals.',next_consumers=['A071','A074','A075','A080','A084','A089','B20'])
claims.append(new)
put('CLAIMS.json',dict(claims=claims))
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=R.name,stream='B19',packet_id='A092',gap_id='C019-INITIAL-ARBITRARY-CORE-ORIGINAL-SOURCE',attempt_id='A092-stage22-prime-summary-original-owner',method='independent truth-matrix reconstruction; exhaustive arbitrary two-output encodings; exact physical edge formula; interval entropy and integer sign certificates',mathematical_delta='A080/A071 unchanged scoped acceptance; any finite number of summary outputs has exact minimum k^2*2^(1-k); exact original total-influence formula; literal summary-only payment counterfamily has H/I_full -> 2, not FEI divergence.',deliverable_status='COMPLETE_LOCAL',mathematical_status='FULL_FEI_OPEN; two scoped reviews HOLDS; new analytic theorem pending independent review; Lean SETUP_UNVERIFIED',claim_versions_used=versions,claims_created_or_changed=[dict(claim_id=c['claim_id'],version=c['version'],status=c['status']) for c in claims],source_artifacts=['out/SOURCE_INTAKE.json','PROOF.md','out/FROZEN_SPEC.json','out/AUDIT_SPEC.json','out/RESULT.json','out/AUDIT_RESULT.json','out/LEAN_RECEIPT.json'],next_consumers=new['next_consumers'],next_action='Fund retained arbitrary OUTER seed on the correlated three-state interface from SAME unused ORIGINAL total influence, with old debits and BOTH full terminals; A074/A080 independently review exact formula and counterfamily.',stagnant_substantive_attempts=0,blockers=['No arbitrary-core ORIGINAL dimension-independent source payment or divergent ordinary H/I seed supplied.','Lean compiler was not admitted; formal statement remains unchecked.','Wake attachment-integrity timeout and stale personal notes excluded from mathematical premises.','Supervisor mirroring and downstream adoption unverified.'],packet_ids=['A092'])
put('PROGRESS.json',progress);put('PACKET_DELTA.json',progress)
report=f'''# A092 stage22: exact original influence and the summary-only payment obstruction

## exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. A080-COMPOSITION-PRIME-APPROXIMATION@1 and A071-PRIME-CHEAP-TWO-OUTPUT-SUMMARY@1 both HOLD unchanged at their stated scopes. The new result counts ALL original physical influence and extends the sharp summary lower bound to any finite number of Boolean outputs, including encodings splitting row classes. PROOF.md states every quantifier and the literal Boolean circuit. H is complete squared-spectrum entropy in bits; input Shannon entropy is separate.

## sources actually read, revisions and theorem locators

Read the complete execution protocol v2; machine AGENTS; campaign README, CURRENT_STATUS, CLAIM_REGISTRY, OBSTRUCTION_REGISTRY, PACKET_STATUS, STREAM_NEXT_ACTIONS and plan; supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and textual sources; the four supplied paper text versions; BOARD dated 2026-10-27 09:23 UTC, B19 lead v2, own rolling records and earlier reports. out/SOURCE_INTAKE.json records 56 reads, exact hashes and explicit text encodings. The paper exports require cp1252 after strict UTF-8 fails; no source was modified. Specific proof locators are A080 PROOF, sections Exact construction / Uniform perturbation / Exact universal consequence, and A071 PROOF sections 1-3. Their exact claim versions and statement hashes are retained in CLAIMS.json with A092 review records. Papers supply background only; no percolation or threshold theorem enters this proof. One three-wording math recall returned neighboring cards, not an answering proof; no recalled card is a premise. The wake reports attachment-lock timeout and stale identity notes; the alert was delivered and affected notes are excluded.

## complete derivation or exact first unsupported line

PROOF.md reconstructs the three exhaustive cut cases, positive-denominator and negative-numerator guards, finite coupling continuity, explicit approximation schedule and the exact proper-partition bank consequence. The summary boundary contains k^2 edges. Every decodable summary, even with arbitrarily many outputs and split row classes, changes a bit on each edge; a two-bit chain plus constants attains equality. The new exact edge count is I(F)=I(g)+2^(1-N)[N(N-1)-2kD0-2D1], with D0,D1 actual seed boundary counts. It includes the fresh coordinates and all cancellation.

The literal two-bit point-defect seed gives I(F_k)=1+(k^2-k+2)2^(-k-1), H(F_k)->2 and H(F_k)>1 for k>=32. Its optimal fresh-summary influence is k^2 2^(1-k), so total entropy divided by summary influence diverges. This rigorously refutes ONLY the proposed strategy inequality H(F)<=C inf_E sum I(E_j); no other agent is said to assert it. Ordinary H/I tends to 2. The first unsupported full-FEI line remains an ORIGINAL O(I) payment for the retained arbitrary seed, with old debits, its correlated state law and both full terminals.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC preceded execution. Pilot40 constructions,612 blocks,3082 exact assertions PASS in0.141261s. Main552 constructions (every labelled n=1,2,3 seed; k=2,3),21348 proper blocks,29460 exact assertions PASS in23.316197s. The counts exclude the pilot. Direct integer character transforms agree with FWHT, direct physical edges agree with every Fourier influence, and the new exact total-influence identity agrees at every root. All65792 two-bit vertex encodings on the k=2,3 cubes were inspected: valid48/264, including24/240 split-class encodings; exact minima2 and9/4. Constants, complements and dummy seed coordinates were not removed. A fixed32x32 integer schedule grid checks the quantitative bound independently of any constructed large truth table.

AUDIT_SPEC preceded the supplemental validation: seven literal point-seed circuits k=2..8 have certified H>1 using60-term positive atanh logarithm intervals with geometric remainder; exact physical influences agree with the formula. One k=1 control really has only two rows, so the fresh-bit hypothesis cannot simply be removed. Exact signs136^4<2^34 and35^4<2*34^4 certify the analytic all-k>=32 threshold. All24 supplemental assertions PASS in0.063822s. No floating-point sign is used. Finite checks do not establish all-dimensional FEI.

Commands: python -B -X utf8 code/intake.py; code/verify.py --pilot; code/verify.py; code/audit.py; code/finalize.py (from this run directory or using the full relative run path). Estimated checker memory40MB, observed runtime below frozen55s; no GPU, heavy search, dimension escalation or detached work. Fresh memok returned0 before the Lean attempt (5.0GB physical,11.7GB commit free); lean_check itself returned SETUP_UNVERIFIED, exit1, refusing a compiler because its stricter admission requires5500MB free or a nonhung UI. No compiler was launched, no axioms audited, and no Lean-checked claim is made. The attempted statement is exactly the finite four-row Bool alternative, not the entropy theorem. Rung: analytic proof plus exact finite certificates, new result pending independent review.

## proof dependencies and changed downstream conclusions

Source A080 and A071 statements remain unchanged, with independent A092 reconstruction and acceptance at scope. Their prior finite validations are not imported into the new counts. The extension to any number of summary outputs and exact original influence are one new author claim. Summary optimization and scalar primality do not fund the retained arbitrary seed; the counterfamily exposes that exact unpaid account. Neither signed-bank coherence nor source debit-sign repairs are refuted. Earlier B19 dispatch targets are already closed in own records; current board dependencies supersede repeating them.

## one next mathematical action and independent reviewer

A074/A080 independently review the original influence identity and summary-only counterfamily; A071 checks the arbitrary-output boundary extension. A075/A084/A089 should price the retained arbitrary OUTER seed on this correlated three-state interface from SAME unused original total influence, preserving old bookings and both full terminals. Naming consumers is not a message-delivery or downstream-adoption receipt.

## actual persistence receipts or precise save blocker

Local artifacts are saved under the designated A092 stage directory at {now}. out/PERSISTENCE.json checks exact protocol fields, copied source statement hashes, new statement hash, equal PROGRESS/PACKET_DELTA bytes, source pins, file sizes and two-line STATUS. A first persistence pass caught BOARD.md changing concurrently; its original intake hash is retained, the newer board is read and snapshotted separately, and the change is recorded rather than called source stability. The mathematical proof sources remain unchanged. REPORT, CLAIMS, PROGRESS, PACKET_DELTA, proof, frozen specifications, scripts and exact outputs are local; supervisor mirroring is unverified. Rolling WORKLOG/LEARNED record the result. The compute snapshot was status ok but only3.1GB disk free; artifacts remain small. No git, mail, peer message, trading access, deletion, shared campaign/brain write or process shedding. Mandatory session wake/checklist helpers are the only external bookkeeping actions. All launched commands have completed; no own research process is left running.

## Universal bridge

This stage advances C019 initialization and C024 history-transfer scope by independently accepting the arbitrary-seed prime reduction and sharply ruling out payment of retained entropy from fresh-summary influence alone, even after optimization over any number of outputs. The exact new original-influence formula prevents double-flip cancellation from being mistaken for reusable credit. The universal ORIGINAL O(I) source for the arbitrary outer seed is still unpaid; no full-FEI proof or divergent ordinary-ratio family is supplied. NEXT targets that source on the correlated interface because every Boolean seed survives there, whereas further summary optimization cannot remove the retained seed or pay its historical obligations.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A092 stage22 saved: A080 prime reduction/A071 sharp summary independently HOLD; ANY-output summary-only payment FALSE, exact original I formula;29460+24 exact checks PASS;FEI OPEN.\nNEXT: A074/A080 review formula/counterfamily;A075/A084/A089 fund retained arbitrary OUTER core from SAME unused ORIGINAL influence,correlated state/old debits/BOTH full terminals;no summary-only reset.\n',encoding='utf-8')
for name,text in [('WORKLOG.md',f'{now} stage22: Independently accepted A080 prime approximation and A071 two-output summary unchanged. New all-r summary optimum and exact ORIGINAL influence formula; literal point-seed summary-only payment counterfamily has ordinary H/I->2. Main552 circuits/21348 blocks/29460 assertions plus24 supplemental PASS, no pilot duplication. Lean SETUP_UNVERIFIED: stricter admission, no compiler. Four protocol files and local receipts saved; full FEI OPEN; no own research job remains.'),('LEARNED.md','Stage22: For F=g times radius-one ball sign on N=n+k, exact I(F)=I(g)+2^(1-N)[N(N-1)-2kD0-2D1], with D0 old seed boundary from weight0 to1, D1 from weight1 to2. Any decodable finite-output fresh summary has sum influence>=k^2*2^(1-k), attained for every r>=2 by chain code plus constants; r1 impossible. Fixed n2 point seed gives I=1+(k^2-k+2)2^(-k-1), H->2 and H>1 for k>=32. Thus entropy/optimal summary influence diverges while entropy/ALL physical influence->2. Scope: refutes summary-only entropy payment, not FEI. A080/A071 unchanged claims independently accepted. Arbitrary retained outer seed and ORIGINAL payer remain unpaid.')]:
    marker='stage22:' if name=='WORKLOG.md' else 'Stage22:'
    if marker not in (A/name).read_text(encoding='utf-8'):
        with (A/name).open('a',encoding='utf-8') as f:f.write('\n'+text+'\n')
protocol=json.loads(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))['required_per_run']
expected_progress={x.split(' (')[0] for x in protocol['progress_fields']}
assert set(progress)==expected_progress
for c in claims:assert set(c)==set(protocol['claim_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert hashlib.sha256(statement.encode('utf-8')).hexdigest()==new['statement_sha256']
intake=read('out/SOURCE_INTAKE.json');stability=[]
for rec in intake:
    path=Path(rec['path'])
    # Own rolling files and compute state are intentionally mutable snapshots.
    if path.parent==A or path.parent==Path(r'~\.claude\compute'):continue
    current=path.read_bytes(); current_hash=hashlib.sha256(current).hexdigest()
    ok=current_hash==rec['sha256']
    if path==P/'BOARD.md':
        (R/'out/BOARD_REFRESH.md').write_bytes(current)
        stability.append(dict(path=str(path),unchanged=ok,intake_sha256=rec['sha256'],refresh_sha256=current_hash,disposition='mutable coordination snapshot; refreshed separately, never a proof premise'))
    else:
        assert ok,str(path)
        stability.append(dict(path=str(path),unchanged=ok))
files=[]
for path in R.rglob('*'):
    if not path.is_file() or path.name=='PERSISTENCE.json':continue
    assert path.stat().st_size<20*1024*1024
    files.append(dict(path=str(path.relative_to(R)),bytes=path.stat().st_size,sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
put('out/PERSISTENCE.json',dict(status='PASS',saved_at=now,protocol_fields_exact=True,progress_delta_identical=True,source_stability=stability,files=files,total_bytes=sum(f['bytes'] for f in files),remote_mirror='UNVERIFIED',independent_review_new_claim='PENDING'))
print(json.dumps(dict(status='PASS',saved_at=now,files=len(files),total_bytes=sum(f['bytes'] for f in files),claims=len(claims),main_assertions=main['exact_assertions'],audit_assertions=audit['exact_assertions'])))
