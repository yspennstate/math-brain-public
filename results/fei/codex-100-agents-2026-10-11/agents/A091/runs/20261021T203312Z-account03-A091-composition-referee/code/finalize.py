from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parent.parent
BASE=Path('~/brain_workers/FEI100_20261011')
REPORTS=Path('math-open-problems/reports/fei-2026-10-11')
OLD=A/'runs/20261014T094139Z-account05-A091-composition-referee'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def digest(b):return hashlib.sha256(b).hexdigest()
def read(p):
    b=p.read_bytes()
    return b.decode('utf-16' if b.startswith((b'\xff\xfe',b'\xfe\xff')) else 'utf-8-sig').replace('\r\n','\n')
def write(p,s):
    assert p.resolve().is_relative_to(A.resolve())
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(s,encoding='utf-8')
def dump(p,obj):write(p,json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
protocol=json.loads(read(REPORTS/'EXECUTION_PROTOCOL.json'))
main=json.loads(read(R/'out/CHECK_0_3072.json'))
pilot=json.loads(read(R/'out/CHECK_0_2.json'))
repro=json.loads(read(R/'out/REPRODUCE.json'))
lean=json.loads(read(R/'out/LEAN.json'))
dump(R/'out/LEAN.json',lean)
assert main['status']==repro['status']==pilot['status']=='PASS'
assert main['cases']==3086 and repro['cases']==256
sources=[REPORTS/p for p in ('EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','STREAM_NEXT_ACTIONS.json')]
sources += [BASE/'BOARD.md',BASE/'claude/B19/STREAM_NOTES.md']
sources += [OLD/p for p in ('REPORT.md','PROOF.md','NEXT_IDENTITY.md','code/exact.py','code/check.py','code/next_query.py')]
supp=Path('math-open-problems/research_pushes/2026-10-11-full-fei-100-agents')
sources += [supp/p for p in ('CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md')]
dump(R/'out/SOURCE_RECEIPTS.json',{'captured_at':now,'note':'Capture-time byte hashes of sources consulted; paper baselines remain previously audited imports, not a new literature audit. Some source display batches were truncated; no whole-file rereview is inferred.','sources':[{'path':str(p),'bytes':p.stat().st_size,'sha256':digest(p.read_bytes())} for p in sources if p.exists()]})
statement='For F=(1-Y)G+Y[A*u+(1-A)*(B*v+(1-B)*G)] on finite uniform independent physical blocks, with A a point event of r>=1 bits, B any indicator, u,v,G arbitrary Boolean signs on mutually disjoint data blocks, and one actual G, every A-coordinate i satisfies B_i(F)<=12 Inf_i(F) and H(F)-(H(F_i=0)+H(F_i=1))/2 <= (12+2/ln(2)) Inf_i(F). In the original physically merged fine U/R account, U is harmonic and kappa=R-E R_child>=0, hence the same bound holds for the H-U-R decrement with both complete terminals retained.'
hyp=['Entropy in bits; signs +/-1; actual physical fair-coordinate restriction.', 'Y is fresh and fair; A, B and all selected-data blocks are independent.', 'A is one current point event; r>=1, q=2^(-r)<=1/2; B may be empty or certain.', 'u, v and the actual G have disjoint physical blocks; internal private G selectors are allowed.', 'Prior data exposure must preserve these independent-block hypotheses; all means in [-1,1], including constant cores.', 'No later B-query claim, arbitrary earlier live priorities, generic data overlap or universal inherited-account funding is asserted.']
claim={'claim_id':'A091-FIRST-PRIVATE-BEFORE-Y-REPEATED-FALLBACK','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':digest(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode('utf-8')),'contributors':['A091/account03 analytic grouping and tests; prior A091/account05 exact interface and scalar lemma'],'proof_source':{'path':str(R/'PROOF.md'),'sha256':digest((R/'PROOF.md').read_bytes()),'locators':['Exact grouped identity (1)','Bounds (2)-(5)','Original account decrement (6)']},'proof_dependencies':['C005 physical entropy decrement/channel bound J_i<=2 Inf_i/ln2; previously audited baseline','A091 stage6 PROOF.md scalar Phi(a^2,b^2)<=2|ab| and NEXT_IDENTITY.md equations (1),(2); direct grouping supplied in this version'],'review_records':[{'reviewer':'A091 author self-audit, not independent acceptance','verdict':'GROUPED_IDENTITY_REPRODUCED_WITH_DIRECT_CHARACTER_SUMS','source':'out/REPRODUCE.json','cases':256},{'reviewer':'Lean helper','verdict':lean['result']['status'],'source':'out/LEAN.json','scope':'fallback variance ownership only; no formal verification obtained'}],'status':'AUTHOR_ANALYTIC_PROOF_EXACT_CHECKS_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A059','A087','A090','A094','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
dump(R/'CLAIMS.json',[claim])
next_action='Price a later B point-coordinate while earlier A and shared Y remain unexposed, from SAME merged reserve and unused original owner, preserving both full H-U-R terminals; A059/A087 review new first-A grouping and A090 audits ownership.'
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B19','packet_id':'A091','gap_id':'G-LOWSEL-COLLISION','attempt_id':'A091-stage17-first-private-before-Y','method':'Disjoint physical Fourier-sector grouping, scalar entropy packet inequality, variance ownership, exact FWHT and independent direct-character reconstruction.','mathematical_delta':'Saved NEXT_IDENTITY first-A interface now has B_i<=12 Inf_i and full decrement rate12+2/ln2 without additional reserve spending; both actual terminals retained.','deliverable_status':'COMPLETE_LOCAL_PENDING_SUPERVISOR_COPY','mathematical_status':'SCOPED_AUTHOR_PROOF_PENDING_EXTERNAL_REVIEW; FULL_FEI_OPEN; LEAN_RUNTIME_UNVERIFIED','claim_versions_used':['C005 baseline','A091-SHARED-ACTIVATION-REPEATED-FALLBACK-PAYMENT@1 scalar lemma only','A091 stage6 NEXT_IDENTITY equations(1),(2)'],'claims_created_or_changed':['A091-FIRST-PRIVATE-BEFORE-Y-REPEATED-FALLBACK@1'],'source_artifacts':['PROOF.md','SPEC.json','code/private_query.py','code/reproduce.py','code/Ownership.lean','out/CHECK_0_2.json','out/CHECK_0_3072.json','out/REPRODUCE.json','out/LEAN.json','out/SOURCE_RECEIPTS.json'],'next_consumers':['A059','A087','A090','A094','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Lean returned RUNTIME_UNVERIFIED after timeout, no target or axiom certificate.','External review, adoption, mirror verification and supervisor copying unobserved.','Later B query and generic inherited account funding remain unpaid.','Brain wake warning: owner model59.2h and state of mind43.8h stale; owner alerted; current task instructions used.'],'packet_ids':['A091']}
fields=[f.split(' (')[0] for f in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(fields)
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
report='''# A091 composition referee stage17

## exact target, quantifiers, hypotheses and units

Close the stage6 NEXT_IDENTITY first-private-point-query payment while shared Y remains unexposed and ONE actual nonconstant fallback G survives both Y histories. Finite uniform cubes; entropy in bits; arbitrary selected-core biases, including constants. A is a point event, B any independent indicator; u,v,G have independent disjoint physical blocks. Prior actual core-data restrictions are allowed when this geometry survives. Theorem: B_i<=12 Inf_i and D_i<= (12+2/ln2)Inf_i <15Inf_i for an A coordinate. Full FEI remains OPEN; external review pending.

## sources actually read, revisions and theorem locators

Execution protocol2026-10-11-execution-v2 read in full; BOARD, B19 v2 notes, own STATUS/LEARNED and saved stage6 report/proof/NEXT_IDENTITY/code consulted. Current registry, obstruction, README, next-action and supplemental campaign/claims/counterexamples/seed/mapping navigation consulted. Capture-time source hashes are in out/SOURCE_RECEIPTS.json; some large display batches were truncated, so no whole-source rereview is claimed. Earlier threshold/percolation and biased-composition audits are retired baselines, not new results here. Stage6 NEXT_IDENTITY equations(1),(2), stage6 PROOF scalar lemma, and C005 are the mathematical dependencies. Later named stage directories lack a REPORT/code locally; the rolling status matches saved stage6. Current owner deadline2026-10-23T14:49Z supersedes stale October11 protocol endpoints; no schedule is changed.

## complete derivation or exact first unsupported line

PROOF.md reconstructs every frequency sector of the exact B_i identity. Nonempty u gives q²Vu; the v and nonconstant-B sectors give S Phi((1-q)²,q²)/2, S=VH-(1-p)²VG; empty-B/nonempty-G gives VG RG; the empty-data frequency gives R0. Point geometry supplies the remaining (q-2q²)(1-mh). The four grouped contributions are bounded by2d,4d,4d,2d. In particular fallback variance ownership (1-p)VG<=VH avoids an unpaired L2 square-root loss. The original merged reserve release is nonnegative and U harmonic, so D-kappa is paid without restarting any bank. No division by tiny d is used. All constants, p=0/1, r=1, arbitrary r, and zero-influence cases are covered analytically.

This is an analytic proof with exact finite validation, NOT Lean-checked. The first unsupported extension is the later B query with earlier A and Y unresolved: the direct-selected-u frequency grouping is then unavailable. No arbitrary-order shared-controller theorem or universal inherited U/R funding is inferred. Both exact terminal H-U-R debts remain in the account.

## executed validation with domain, arithmetic, commands and outputs

SPEC.json and helper source were frozen before execution. Main family: all64 one-bit sign-core triples, all16 two-bit B events, A widths1,2,3, plus14 signed AND2/actual restriction fixtures. Pilot: `python -B -X utf8 code/private_query.py 0 2 --pilot`,2 cases/26 exact assertions,0.00454s. Main: `python -B -X utf8 code/private_query.py 0 3072 --supplement`,3086 cases,132 zero-influence cases,40118 exact assertions,24.026s, PASS. Integer FWHT, Fraction physical edge counts and spectra, prime-log identity, and outward rational atanh enclosures check the grouped identity, each separate majorization, full-D rational rate15, and original merged reserve drift. Helper arithmetic is the previously audited stage6 implementation, loaded read-only with bytecode disabled.

Separate reproduction: `python -B -X utf8 code/reproduce.py`,256 cases/512 exact assertions,2.040s, PASS; explicit128-entry physical tables and direct character sums, with no imported FWHT/compose/local/formula implementation. Main plus reproduction are3342 cases/40630 assertions; adding the separate2-case pilot gives3344/40656. These are this stage's counts, not a revision of stage6 counts.

Before the potentially>300MB Lean job, memok exited0 (physical14.7GB, commit21.4GB free). lean_check used fresh admission, one thread, source/hash/target pinned,45s timeout and output root inside this run. out/LEAN.json returned RUNTIME_UNVERIFIED in51.344s, no compiler output/target/axiom evidence; no retry and no formal pass claimed. code/Ownership.lean states only the fallback variance inequality; prose fidelity is explicitly limited to that step. Mathematical jobs stayed below their55s watchdogs; estimated memory180MB, observed peak not measured. No GPU, dimension escalation, detached process or Git.

## proof dependencies and changed downstream conclusions

A091-FIRST-PRIVATE-BEFORE-Y-REPEATED-FALLBACK@1 has a source-complete author analytic proof, pending A059/A087 independent review and A090 ownership audit. It consumes C005 and the previously reconstructed scalar packet lemma. The saved first-A interface is paid; the stage6 shared-Y reveal and A059 priority results are unchanged. The available original rate<17 accommodates this node locally, but grafting arbitrary later private queries remains a separate proof obligation. No full-FEI status changes.

## one next mathematical action and independent reviewer

Price a later B point-coordinate while earlier A and shared Y remain unexposed, retaining the SAME original fine merged reserve, all previous debits, and both exact terminals; A059/A087 reconstruct the new first-A grouping, A090 checks reserve/ancestry, A094 challenges endpoints. This is the remaining adjacent interface rather than another gate-width census.

## actual persistence receipts or precise save blocker

Four protocol files, analytic proof, frozen spec, code, output certificates, failed formal receipt and capture-time source receipts saved locally under A091 only. Finalizer checks exact protocol fields, identical progress/delta, statement hash, output PASS values, two-line STATUS, final Universal bridge, and file sizes. WORKLOG is appended and LEARNED extended. Supervisor copy, mirror, external acceptance, downstream adoption and publication are unverified. Session wake completed with required stale-owner-model/state warning, reported to the owner; stale notes were not used as task authority. Tool startup/reads were slow; no existing work was stopped to relieve load.

## Universal bridge

This stage advances C019 stopping-tree payment and C024 actual history transfer by paying exactly the saved first-private-A query before shared-Y exposure, after actual core-data restrictions preserving independent blocks, at12+2/ln2 with no additional original reserve spending and both full terminals retained. The new ingredient is explicit fallback variance ownership in a complete physical Fourier-sector partition. What remains is the later B query under the earlier live A/Y history, then general histories and universal inherited core/reference funding. NEXT targets that adjacent unpaid physical transfer because it extends the SAME account across the next genuine overlap, rather than certifying an unrelated class or silently restarting the budget.
'''
write(R/'REPORT.md',report)
write(A/'STATUS.md','STATE: Stage17 saved: first private A before shared Y with one actual fallback paid at12+2/ln2;3086+256 exact cases PASS;analytic proof pending review;Lean runtime unverified;FEI OPEN.\nNEXT: Pay later B query while A/Y remain live from SAME merged reserve with both terminals;A059/A087 review first-A grouping,A090 ownership,A094 endpoints.\n')
if 'stage17/account03:' not in read(A/'WORKLOG.md'):
    with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
        f.write('\n'+now+' stage17/account03: resumed saved stage6 NEXT_IDENTITY after slow tool access. Grouped u/v/G/B spectra; first-A B<=12d, D<=12+2/ln2 d; original kappa>=0; all bias endpoints and both terminals retained. Main3086/40118 plus independent direct-Walsh256/512 and pilot2/26 PASS. Lean ownership lemma attempted after memok0, timed out RUNTIME_UNVERIFIED; no formal pass. Later B query remains next. Saved '+R.name+'; external review/copy unverified.\n')
if '\nStage17:' not in read(A/'LEARNED.md'):
    with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
        f.write('\nStage17: For F=(1-Y)G+Y[A u+(1-A)(Bv+(1-B)G)] with fresh fairY, point A probabilityq<=1/2, arbitrary independent eventB probabilityp, disjoint sign cores and ONE physicalG, an A-coordinate has B_i<=12Inf_i and D_i<= (12+2/ln2)Inf_i. Complete grouping uses S=VH-(1-p)^2VG and (1-p)VG<=VH; root mean packet paid via |m-h|<=1-mh. Original merged reserve release nonnegative, so no additional surplus consumed; retain both H-U-R terminals. All data restrictions preserving disjoint blocks and all constant/empty/certain endpoints included. Author analytic proof, external review pending; main3086 plus direct-character256 exact cases PASS; Lean key algebra timed out, NOT formal-certified. Does not apply to a later B query with A/Y unresolved.\n')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len(read(A/'STATUS.md').splitlines())==2
assert read(R/'REPORT.md').strip().split('\n\n')[-1].startswith('This stage advances C019')
files=[p for p in R.rglob('*') if p.is_file()]
assert all(p.stat().st_size<20_000_000 for p in files)
receipts={'status':'PASS','saved_at':now,'protocol_claim_fields_exact':True,'protocol_progress_fields_exact':True,'progress_delta_identical':True,'status_lines':2,'proof_rung':'ANALYTIC_PROOF_PENDING_INDEPENDENT_REVIEW','lean_rung':lean['result']['status'],'main_cases':main['cases'],'reproduction_cases':repro['cases'],'files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':digest(p.read_bytes())} for p in files]}
dump(R/'out/RECEIPTS.json',receipts)
print(json.dumps({'status':'PASS','run':str(R),'claim':claim['claim_id'],'main_cases':main['cases'],'reproduction_cases':repro['cases'],'lean':lean['result']['status'],'file_count':len(files)+1}))
