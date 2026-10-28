from pathlib import Path
import json, hashlib, datetime

run=Path(__file__).resolve().parents[1]
root=run.parents[1]
def put(name,value):
    p=run/name
    p.write_text(value if isinstance(value,str) else json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

checks=json.loads((run/'out'/'CHECKS.json').read_text(encoding='utf-8'))
assert checks['status']=='PASS' and checks['assertions']==1160
source_paths=[
 Path(r'~\AGENTS.md'),
 Path(r'BOARD.md'),
 Path(r'claude\B09\STREAM_NOTES.md')]
campaign=Path(r'math-open-problems/reports\fei-2026-10-11')
source_paths += [campaign/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
supp=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
source_paths += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
for agent,stamp in [('A041','20261014T083216Z-account05-A041-weighted-threshold-fei'),('A043','20261014T052009Z-account05-A043-prime-gate-decomposition'),('A044','20261014T055346Z-account05-A044-non-symmetric-gate-classes')]:
 source_paths.append(root.parent/agent/'runs'/stamp/'REPORT.md')
receipts=json.loads((run/'out'/'SOURCE_RECEIPTS.json').read_text(encoding='utf-8'))
receipts += [{'path':str(p),'sha256':digest(p),'scope':'campaign instruction, navigation or specifically read report'} for p in source_paths]
put('out/SOURCE_RECEIPTS.json',receipts)
put('out/LEAN_ATTEMPT.json',{'command':'python -X utf8 lean_check.py --stmt "example (z : Int) : 0 <= z * (z - 1) := by by_cases h : z <= 0; exact mul_nonneg_of_nonpos_of_nonpos h (by omega); exact mul_nonneg (by omega) (by omega)"','exit_code':1,'output':'RUNTIME_UNVERIFIED in 122.8s; source_sha256: aeb8afb4c2198fd4874a4662a11ba036d4106afdb162fe3b3e8a87d456b59dab; Translation fidelity: UNVERIFIED','rung':'not Lean-checked','scope':'integer scalar kernel only; no certificate and no assumption audit available','followup':'no retry or heavy job; analytic proof and exact finite checks retained'})
put('out/VALIDATION_HISTORY.json',{'initial_checker_assertions':1158,'final_checker_assertions':1160,'reason_for_change':'added two phase-independent Boolean-mean admission checks; no family or parameter change','source_read_repair':'PDF text exports are cp1252; initial strict UTF8 read failed without modifying any source; explicit original encoding then used','draft_arithmetic_repair':'reused-wire independent mean corrected to -41/45 and mass1681/2025 to match the exact executed checker before final save','lean_attempt':'runtime unverified; excluded from mathematical certification'})

statement=('For every d>=3 and independent Bernoulli biases p_i in (0,1), the Boolean gate f=2 product_i X_i-1 has integer cofactor profiles Z_[d]\\{i}=X_i. If integer-valued W_i retain mean p_i and variance [4^(d-2)/v_[d]\\{i}] lambda_i P([d]) for nonnegative allocations lambda_i, then every lambda_i>=1 and their sum>=d. Thus exclusive strict-superset allocation cannot preserve all inherited integer profiles. This owner count is compatible with O(degree deficit), since d/(d-1)<=3/2. For fair AND3, deleting the triple Fourier packet and normalizing yields empty mass3/5 and is not the spectrum of any Boolean gate on the inherited fair cube, for any choice of phases.')
claim={
 'claim_id':'A045-EXCLUSIVE-PROFILE-OWNERSHIP-ADMISSION-OBSTRUCTION','version':1,
 'exact_statement':statement,
 'hypotheses':['actual AND sign on distinct independent physical inputs','interior biases; deterministic inputs contract first','preserve inherited cofactor means and integer-valued profiles','variance funded only by allocated strict-superset mass via exact Parseval scaling','nonnegative allocations; normalized-deletion clause uses the original fair three-bit cube'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A045/account03'], 'proof_source':{'path':'PROOF.md','sha256':digest(run/'PROOF.md'),'checks':'out/CHECKS.json'},
 'proof_dependencies':[], 'review_records':[], 'status':'ANALYTIC_PROOF_EXACT_CHECKS_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[], 'refutes':['unregistered exclusive packet splitting that retains every inherited integer profile','Boolean admission of the normalized fair-AND3 spectrum after deleting its triple packet'],
 'first_unproved_line':None, 'next_consumers':['A044','A043','A041','A090','A091']}
put('CLAIMS.json',[claim])
progress={
 'protocol_revision':'2026-10-11-execution-v2', 'run_id':run.name, 'stream':'B09','packet_id':'A045',
 'gap_id':'G-BIASED-PROFILE-OWNERSHIP','attempt_id':'A045-stage6-exclusive-profile-admission',
 'method':'analytic integer-moment admission audit plus independent exact Fraction product spectra and cofactor checks',
 'mathematical_delta':'An all-d AND witness forces every codimension-one integer profile to retain the full top-packet variance. Exclusive splitting fails already at AND3; its normalized triple deletion fails Boolean admission for all phases. Linear degree-weighted ownership remains viable.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'SCOPED_ANALYTIC_OBSTRUCTION_PENDING_REVIEW_FULL_FEI_OPEN',
 'claim_versions_used':['A044-INTEGER-MIXED-PROFILE-PACKET-PAYMENT@1 (previously accepted context; all needed scaling rederived here)'],
 'claims_created_or_changed':[claim['claim_id']+'@1'],
 'source_artifacts':['PROOF.md','out/FROZEN_SPEC.json','code/check.py','out/CHECKS.json','out/CASES.json','out/SOURCE_RECEIPTS.json','out/LEAN_ATTEMPT.json'],
 'next_consumers':['A044','A043','A041','A090','A091'],
 'next_action':'Use a complete merged quadratic reference or degree-weighted shared profile funding, and prove its actual signed cross-entropy payment without assuming selected fragments retain Boolean/integer admission; retain full terminal cost.',
 'stagnant_substantive_attempts':0,
 'blockers':['Universal complete-reference cross-entropy payment remains open.','Independent review and supervisor copy/mirror receipts pending.','Lean helper returned RUNTIME_UNVERIFIED; no formal certification claimed.'],
 'packet_ids':['A045']}
put('PROGRESS.json',progress);put('PACKET_DELTA.json',progress)

report=f'''# exact target, quantifiers, hypotheses and units

Audit the next step after the nonzero-mean all-pairs congestion obstruction: can one allocate strict-superset Fourier packets exclusively while retaining the actual integer cofactor profiles used in A044's local bound? For every d>=3 and every interior product law, actual AND_d forces each codimension-one profile to retain the entire top-packet variance. Exclusive ownership fails. On the fair three-bit instance, deleting that packet and normalizing is not Boolean-realizable for any phases. This is a mechanism obstruction, not an FEI disproof. Natural logarithms are used for the small residual calculation; P is the normalized squared orthonormal product Fourier law.

Crucial limit: d required owners versus degree-deficit weight d-1 is bounded by3/2. The example does NOT refute a general O(Delta) shared funding rule or the complete-reference approach. It tells the consumers which admission hypothesis they lose when splitting packets.

# sources actually read, revisions and theorem locators

Read execution-v2 protocol in full, the listed campaign README/status/claim/obstruction/packet/next-action files, campaign-plan product-bias/realizability passages and supplement CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING; listed supplement sources. Current user deadline23 October14:49UTC takes precedence over the older campaign indices'21 October deadline. Read BOARD's B09 and neighboring consumer reports, B09 STREAM_NOTES v2, own STATUS/LEARNED, and actual prior completed report20261014T063646Z (later account05 run directories have no REPORT.md). The latest board names the same saved mathematics; no completed-stage claims are inferred from empty run directories.

Read A041 report20261014T083216Z sections on the max quadratic reference and terminal-cost scope, A043 report20261014T052009Z on coherent pair/triple funding, and A044 report/PROOF20261014T055346Z sections1 and3 on exact integer scaling and congestion. Prior A045 stage5 accepted A044's local claim; that accepted scope is retained, not re-certified as new work. No other agent code is executed or copied. Relevant normalization/composition/spectral-sample passages of all four supplied paper versions were inspected; the PDF text exports use cp1252, recorded explicitly after an initial UTF8 decoding failure. Percolation's distinct spectral/pivotal laws supply context only, no premise. Exact source bytes and locators are in out/SOURCE_RECEIPTS.json. No internet fact or novelty claim is used.

# complete derivation or exact first unsupported line

PROOF.md gives the complete all-d argument. Integer W obeys E[W(W-1)]>=0, so mean m in(0,1) forces Var(W)>=m(1-m). Actual AND_d has cofactor Z_[d]\\{{i}}=X_i, mean p_i and variance p_i(1-p_i). Its sole strict-superset packet satisfies4^(d-2)P([d])/v_[d]\\{{i}}=p_i(1-p_i). Allocating fraction lambda_i of that packet while retaining the inherited integer profile therefore forces lambda_i>=1 for every i. Already for AND3, three pair profiles cannot share one exclusive packet.

At fair AND3, removing the triple leaves total mass15/16 and empty mass9/16. After normalization the empty mass is3/5. Every Boolean sign on the same cube has mean(j-4)/4, j=0,...,8; no squared mean equals3/5. This excludes every possible Fourier phase choice, not only the inherited signs. Physical restriction instead gives a constant or AND2, with its complete transformed spectrum. Repeated inputs AND(X,X,Y) contract to AND2 and have empty mass121/225 at p_X=1/3,p_Y=2/5; fictitious independent wires give1681/2025. Deterministic inputs contract before any zero-variance division.

The checkable failure tests are: retain interior denominators; retain the physical cofactor mean; keep integer admission; compare variance after allocation; normalize the full proposed law; test Boolean mean quantization independently of signs; distinguish physical restriction and spectral conditioning; identify repeated variables. Dropping integer admission permits the constant real profile m. Dropping the inherited mean permits integer constants. Allowing degree-weighted sharing avoids the exclusive-owner contradiction. These establish the stated scope and prevent a stronger false conclusion.

Exact first unsupported universal line: bound the complete merged-reference cross-entropy, or its signed ordinary-KL remainder with the proper mass-normalizer term, by a dimension-independent multiple of root deficit while retaining all omitted coefficients and terminals. A041's complete max-reference remains a valid reference even if its selected parts are not Boolean; no individual integer-profile payment may be imported after selection without a new admission proof.

# executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json precedes the checker. Command from A045: `python -X utf8 runs/{run.name}/code/check.py`. Fixed41 cases:27 labeled interior product laws on AND3 with p_i in{{1/4,1/2,3/4}}, eight deterministic corners, and six deterministic faces with remaining biases1/3. No symmetry reduction or dimension escalation. All81 interior pair profiles and five prescribed allocation fractions are checked by independent alternating cofactor sums and centered-moment Fourier transforms, using exact Fraction arithmetic. Corner/face transforms contract deterministic coordinates and verify Parseval. Positive residuals use the rational lower bound ln(1/m)>=2(1-m)/(1+m)>0, obtained from the positive atanh series for m in(0,1). All-dimensional conclusions use the analytic argument, not these finite checks.

Final PASS:41 cases,81 interior pair profiles,1160 assertions in{checks['runtime_seconds']:.6f}s. The earlier1158-assertion run omitted two extra phase-independent mean-admission checks; the new count reflects those additions, not a changed search domain. The complete source for the necessary integer kernel was submitted to lean_check.py; it returned RUNTIME_UNVERIFIED in122.8s, exit1, with translation fidelity UNVERIFIED. There is no Lean certificate, no compiler/axiom acceptance and no retry. Rung: analytic proof with exact supporting checks, pending independent review. Frozen memory estimate40MB; no job expected above300MB, no GPU, heavy search, background worker or automatic n increase. Compute snapshot status ok, available RAM about10GB, free disk8.9GB; no workload was stopped. The formal-helper wall duration is recorded separately from the bounded exact search.

# proof dependencies and changed downstream conclusions

The proof is self-contained from integer moments, actual Boolean truth tables and product Fourier expansion. A044's valid original local inequality is preserved. A041's complete normalized max-reference and A043's coherent pair/triple payment are not refuted. There is no new broad FEI candidate or claimed independent acceptance of those whole bundles. One source-complete scoped admission objection replaces an unjustified exclusive-splitting continuation.

A044/A043/A041 must either keep the original full integer profiles with explicitly degree-weighted shared funding, or use a merged complete reference and prove its new logarithmic cost directly. A conditional reference need not be Boolean; applying a Boolean/profile theorem to it does require admission. The no-go is not a lower bound on H/I and does not contradict the earlier band-selector obstruction or any accepted FEI class bound.

# one next mathematical action and independent reviewer

NEXT: retain A041's complete max quadratic reference and seek a signed cross-entropy payment using both actual physical profiles, allowing O(|T|-1) shared owner capacity per packet. Do not demand an exclusive partition that preserves every local integer profile, and do not identify selected spectral fragments with physical restrictions. A090/A091 should independently reconstruct the all-d minimum-variance obstruction and the phase-independent AND3 rejection; A044/A043 can check compatibility with their local scaling and degree ledger. These are intended consumers, not completed reviews.

# actual persistence receipts or precise save blocker

The four protocol files, proof, frozen spec, code, exact case/check outputs, source receipts, validation history and unverified Lean attempt are saved in this A045 run. STATUS has exactly two current lines; WORKLOG/LEARNED are appended. Local schema/hash/size and progress-copy checks are in out/SCHEMA_VALIDATION.json; artifact receipts are in out/PERSISTENCE_RECEIPTS.json. No source tree, other agent folder, shared board/index, brain, trading folder or git state is changed. Independent review, supervisor adoption, private copy and mirror verification remain pending. No local save blocker.

Universal bridge: This stage moves B09's C020 whole-set witness-cost bridge by separating valid complete-reference selection from invalid exclusive integer-profile splitting. The all-d AND gate proves that preserving every inherited cofactor mean and quantized profile forces d owners of its top packet, while the fair AND3 spectral deletion fails Boolean admission even after normalization and arbitrary phase changes. It gains no FEI constant and explicitly leaves linear degree-weighted sharing viable. The unpaid step remains the complete signed cross-entropy and terminal cost; NEXT attacks that actual quantitative payment with a valid normalized reference instead of treating spectral ownership as a physical restriction or opening another isolated class census.
'''
put('REPORT.md',report)
status='STATE: Stage6 complete: exclusive packet splitting fails inherited integer-profile admission on all-d AND; normalized AND3 triple deletion is non-Boolean for any phases;1160 exact checks PASS;FEI OPEN.\nNEXT: A041/A044/A043 use one complete merged reference or degree-weighted shared funding and pay its signed cross-entropy plus terminal costs; A090/A091 review admission obstruction.\n'
(root/'STATUS.md').write_text(status,encoding='utf-8',newline='')
for name,text in [
 ('WORKLOG.md','\n2026-10-21 stage6/account03: Read current B09 board and actual prior completed sources (later account05 directories empty). Audited proposed exclusive strict-superset allocation: actual AND_d has Bernoulli codimension-one profiles, so every inherited integer profile needs the whole top-packet variance; owner fractions sum>=d. This is compatible with degree-weighted O(Delta), not a universal FEI obstruction. Fair AND3 normalized triple deletion has empty mass3/5 and fails Boolean admission for every phase. Exact41 cases/81 profiles/1160 assertions PASS in0.222s. Lean kernel attempt RUNTIME_UNVERIFIED122.8s, no certification. Next pay complete merged-reference signed cross-entropy with terminal costs; saved all stage artifacts.\n'),
 ('LEARNED.md','\nStage6: For actual AND_d=2prod X_i-1 at every interior product law, Z_[d]\\{i}=X_i, so integer-valued mean p_i forces variance>=p_i(1-p_i). Its sole strict-superset packet already attains this minimum; retaining only fraction lambda_i while preserving means and integer admission forces lambda_i>=1 for every i. Exclusive splitting is impossible, but d owners cost only O(d-1) degree deficit and do not refute linear shared funding. Fair AND3 triple deletion normalized by15/16 has empty mass3/5, impossible for any Boolean phases on the same fair cube. Normalization and phase changes cannot repair this admission. A complete non-Boolean reference remains valid; it simply cannot inherit a physical integer-profile bound without proof.\n')]:
 p=root/name
 with p.open('a',encoding='utf-8',newline='') as f:f.write(text)

protocol=json.loads((campaign/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
pf=[s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(pf)
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert all(s in report for s in protocol['required_per_run']['report_fields'])
assert len((root/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert report.rstrip().split('\n\n')[-1].startswith('Universal bridge:')
assert all(p.stat().st_size<20*1024*1024 for p in run.rglob('*') if p.is_file())
put('out/SCHEMA_VALIDATION.json',{'status':'PASS','claim_fields_exact':True,'progress_fields_exact':True,'progress_copy_identical':True,'report_fields_present':True,'statement_hash_matches':True,'status_two_lines':True,'all_files_under_20MB':True,'universal_bridge_last':True})
manifest=[{'path':str(p.relative_to(run)),'sha256':digest(p),'bytes':p.stat().st_size} for p in sorted(run.rglob('*')) if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']
put('out/PERSISTENCE_RECEIPTS.json',{'scope':'local artifacts only; no remote or review receipt','files':manifest})
print(json.dumps({'status':'SAVED_AND_VALIDATED','run':str(run),'artifacts':len(manifest)+1,'assertions':checks['assertions'],'full_fei':'OPEN','review':'PENDING'}))
