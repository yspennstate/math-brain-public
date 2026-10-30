from pathlib import Path
import hashlib,json,datetime
R=Path(__file__).resolve().parents[1];OWN=R.parents[1]
def save(path,text):
    path.write_text(text,encoding='utf-8',newline='\n')
def js(path,obj):save(path,json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def read(path):return json.loads(path.read_text(encoding='utf-8'))
main=read(R/'out/CHECK.json');ind=read(R/'out/INDEPENDENT.json');pilot=read(R/'out/PILOT.json')
assert main['status']==ind['status']==pilot['status']=='PASS'
assert main['source_tables']==278 and main['fixtures']==279 and main['assertions']==11439 and ind['assertions']==37
protocol_path=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=read(protocol_path)
source_root=OWN.parent
source_runs={
 'A002':'20261023T010524Z-fleet03-A002-hardness-preserving-transformations',
 'A051':'20261023T002518Z-fleet03-A051-near-extremizer-definition',
 'A052':'20261023T014825Z-fleet03-A052-critical-source-structure',
 'A055':'20261022T233657Z-fleet03-A055-extremal-obstruction-referee'}
proofs={'A002':'RESET_LEDGER.md','A051':'RESET_BUDGET.md','A052':'RANK_PAIR_PROOF.md','A055':'PROOF.md'}
sources=[protocol_path,OWN.parent.parent/'BOARD.md',OWN.parent.parent/'claude/B01/STREAM_NOTES.md']
for a,run in source_runs.items():
    d=source_root/a/'runs'/run
    sources.extend([d/'REPORT.md',d/proofs[a]])
    if a!='A055':sources.append(d/'CLAIMS.json')
sources.append(OWN/'runs/20261022T231421Z-fleet03-A005-noncircular-endpoint-referee/REPORT.md')
js(R/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'role':'read-only observed source; mutable paths are not immutable revisions'} for p in sources])
review="""# Scoped independent reconstructions

A002-ACTIVATED-FULL-AFFINE-RESET-LEDGER@1: HOLDS at RESET_LEDGER Sections1--2 equations1--5. DERIVATION Section1 reconstructs the mixed-basis optimum by threshold ranks and physical directional disagreements, then applies it to every original terminal and subtracts exact scalar entropy profiles. k>=2 is essential. Deferred control redemption equations7--8 and the source census are read context, outside this acceptance. No substantive repair supplied; A005 remains an independent reviewer at this scope.

A052-RANK-RELEASE-ORIGINAL-PAIR-PAYMENT@1: HOLDS at RANK_PAIR_PROOF Sections1--2 rank ownership and exact bank. Integrating above-threshold basis counts proves both inequalities and greedy equality, with ties and rank0. Independent actual even-hyperplane guards d3,d5 reproduce one gain of1/2, versus false dependent-swap totals3/2,5/2. Source Sections3--5 all-k curvature and original15/4 payment are used as motivation and explicitly re-instantiated by our different tensor-before-activation construction, not accepted here as a whole claim. No repair supplied.

A051 current quantitative upper budgets and A055 latest weak hidden-pair reduction were read as context, not newly independently accepted. Earlier accepted affine-basis characterization is consumed. No source finite-check totals are added to A005 totals. Independent.py uses separate direct characters and physical substitution; it is different-implementation replay by A005, not independent-agent acceptance of the new theorem.
"""
save(R/'REVIEW.md',review)
statement="""For every fixed K>16/5 and epsilon>0, FEI(K) on finite uniform Boolean functions that have full affine Fourier span, minimize influence over their full affine spectral orbit, have I<epsilon, and have an original proper physical pair paid at K by an executable non-character linear reset implies full FEI(K) at the SAME K; the converse is immediate. More explicitly, for any positive-entropy seed f choose an affine-minimal compressed g with H(g)=H(f), q=I(g)<=I(f), mu=Eg with abs(mu)<1. Let Q=(-1)^(ab+ac+bc+za), G_t=Q times t disjoint copies of g, k=max(2,ceil(sqrt(t))), p=2^-k, and F=1+1[controls=0](G_t-1). F is full-span affine minimal; I=p[tq+2+k(1-mu^t/4)] tends to0 and H(F)/I(F) tends to H(g)/q. Query original pair(a,b) and shear only the character-weight-two branch, with all four terminals retained: I_pair=p, expected reset release=p/4, and abs(L_pair/p-4)<=(13+6k)abs(mu)^t, hence the explicit pair price tends to16/5 and is eventually strictly paid at K. Character-only child release is zero. If H(g)-Kq>0, all four complete reset terminals and their full-affine optima still violate K for sufficiently large t; the exact same-bank identity D_K(F)+S_pair^reset=L_pair-5Kp/4 gives a negative inherited bank. The eight-bit point defect with t100000000,k10000,K15/4 gives exact paid margin/p>7633553/12500016 and all four terminal deficits/p>862405/4, certified without evaluating its large truth table."""
deps=['A051-AFFINE-MINIMUM-BASIS-CRITICAL-REDUCTION@1: previously reviewed finite affine parity-basis characterization; canonical compression reconstructed',
      'A002-ACTIVATED-FULL-AFFINE-RESET-LEDGER@1: equations1--5 independently reconstructed at scoped extent in REVIEW.md',
      'A052-RANK-RELEASE-ORIGINAL-PAIR-PAYMENT@1: Sections1--2 rank ownership independently reconstructed; Q and shear directly verified',
      'Elementary finite Walsh, physical restriction, tensor product and rational logarithm identities; no FEI premise']
claim={'claim_id':'A005-PAID-PAIR-WEAK-AFFINE-CORE-HARDNESS','version':1,
 'exact_statement':statement,
 'hypotheses':['Uniform finite cubes, Boolean signs, normalized real Walsh coefficients, H in bits; zero entropy terms continuous',
               'K>16/5 fixed and epsilon>0; ratios for positive-entropy seeds only',
               'Canonical representative may improve the original seed ratio; SAME-K reduction uses H(g)=H(f), I(g)<=I(f)',
               'Whole-product activation; query pair remains original physical(a,b); one explicit conditional linear shear, every branch retained',
               'Explicit reset release is a lower bound on full-affine release, not claimed to be the full optimum',
               'All limits choose k=max(2,ceil(sqrt(t))); finite scalar example uses t100000000,k10000',
               'Critical child nonviolation is NOT asserted; conditional negative-bank conclusion assumes positive seed K-deficit'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['fleet03/A005'],
 'proof_source':['DERIVATION.md Sections1--6','REVIEW.md','code/check.py','code/independent.py','out/CHECK.json','out/INDEPENDENT.json'],
 'proof_dependencies':deps,'review_records':[],
 'status':'AUTHOR_PROOF_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['A002','A051','A052','A055','A090','A094','B20']}
js(R/'CLAIMS.json',[claim])
next_action='A051/A052 exploit nonnegative complete smaller-child affine reserves to force one paid ORIGINAL proper pair, retaining mixed T and the SAME unused bank; A002/A055 independently review the tensor-before-activation endpoint and explicit shear.'
progress={
 'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B01','packet_id':'A005',
 'gap_id':'C019-CRITICAL-ORIGINAL-PAIR-LOWER-FUNDING','attempt_id':'A005-stage18-paid-pair-core-admission',
 'method':'Consume A002/A052 dependencies; independent scoped reconstructions; tensor core BEFORE activation; exact physical shear; mean-profile Lipschitz bound; finite-to-infinite SAME-K reduction',
 'mathematical_delta':'Even a genuinely paid original non-character pair inside weak full-span affine minima is SAME-K FEI-hard for every K>16/5. Explicit price tends16/5 while full terminal debts remain; concrete rational negative-bank certificate. Universal constant gain0.',
 'deliverable_status':'COMPLETE_LOCAL_VERIFIED','mathematical_status':'FULL_FEI_OPEN; new scoped theorem author-proved, independent-agent review pending',
 'claim_versions_used':deps,
 'claims_created_or_changed':[claim['claim_id']+'@1'],
 'source_artifacts':['out/SOURCE_RECEIPTS.json','DERIVATION.md','REVIEW.md','out/FROZEN_SPEC.json','out/CHECK.json','out/INDEPENDENT.json'],
 'next_consumers':claim['next_consumers'],'next_action':next_action,
 'stagnant_substantive_attempts':0,
 'blockers':['Universal critical pair lower-funding/selection remains unproved; paid local endpoint does not imply nonnegative terminal reserves',
             'New theorem independent-agent acceptance, registry adoption, supervisor copying and brain ingestion unverified',
             'Brain self-care degraded: owner-model/state personal context stale; current owner instructions and source-bound mathematics used'],
 'packet_ids':['A005']}
js(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
report="""# exact target, quantifiers, hypotheses and units

A005/B01 stage18 audits the new paid original-pair endpoint after A002 exact activation transport and A052 rank lower-funding. Uniform finite Boolean signs, normalized real Walsh coefficients, entropy bits. For EACH fixed K>16/5 and epsilon>0, decide whether full-span affine minima with I<epsilon and one genuinely paid non-character original pair still admit arbitrary seeds at SAME K. They do. Genuine smaller-child nonviolation remains the precise excluded hypothesis. Full FEI remains OPEN; owner deadline23October2026 14:49UTC supersedes the old protocol clock.

# sources actually read, revisions and theorem locators

Current BOARD header23October03:54UTC, B01 STREAM_NOTESv1, own STATUS, machine AGENTS and protocol2026-10-11-execution-v2 read. Fresh substantive sources: A00223October01:05 REPORT/RESET_LEDGER Sections1--5; A05100:25 REPORT/RESET_BUDGET Sections1--5; A05201:48 REPORT/RANK_PAIR_PROOF Sections1--5; A05522October23:36 REPORT/PROOF Sections1--7. Current A002/A051/A052 claim identifiers inspected. Source paths/observed byte hashes are pinned in out/SOURCE_RECEIPTS. Earlier baseline campaign, registries and four manuscript reads are retained from preceding stages, not represented as fresh audits. One read-only two-wording math recall supplied background and no matching new reset theorem; no novelty or external-paper premise is used.

The unchanged lead's old weak-influence assignment was closed earlier; protocol dispatch consumes the new paid-pair dependency. Brain self-care remains degraded/unverified because owner-model and state-of-mind personal-context notes are stale. Current explicit instructions and proof sources govern; mathematical verification here does not repair that personal-context degradation.

# complete derivation or exact first unsupported line

DERIVATION Sections1--6 give the complete argument. Put Q=(-1)^(ab+ac+bc+za), tensor with t copies of a canonical seed FIRST, then activate the whole product. The original(a,b) pair queries p influence. Its unique weight-two character branch admits an explicit physical shear, releasing p at original reach1/4, while every terminal retains the ENTIRE t-copy seed core. No character-only refund is available. Root full affine minimality and full span survive, and total influence tends to0.

The exact four child means are mu^t,0,0,0; the root mean before activation is mu^t/4. Retain the complete activation scalar profile R_k. Its derivative bound yields abs(L_pair/p-4)<=(13+6k)abs(mu)^t. Thus explicit pair query/reset price tends16/5 and is eventually paid at each fixed K>16/5. Choosing k=ceil(sqrt(t)) preserves the canonical seed ratio, with I tending0. This extends local paid-fragment hardness through rare activation without illegally scaling away either mean or translation correction.

An ACTUAL finite Boolean certificate uses the eight-bit point-defect seed, t100000000,k10000,K15/4. Rational source entropy gives deficit>1/256; Bernoulli bounds the mean power without computing it. Pair margin divided by p is>7633553/12500016, while all four reset terminal deficits divided by p are>862405/4. No large truth table is constructed. This is a fixed-constant obstruction, not a full FEI counterfamily.

FIRST UNSUPPORTED LINE: at a genuine least-essential-dimensional positive fixed-K witness, force one paid original proper pair from NONNEGATIVE complete smaller-child affine reserves and the SAME unused signed bank, retaining mixed T. The embedding fails exactly that eligibility: if its seed violates K, all four complete optimized terminals still violate. A paid local pair alone does not pay their inherited debt. No universal constant improves.

# executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC preceded computation. From A005 execute python -B -X utf8 runs/20261023T035753Z-fleet03-A005-noncircular-endpoint-referee/code/check.py --pilot, then without --pilot; execute code/independent.py under that run. Pilot:22 labelled seeds,902 assertions PASS in0.902s. Full:all278 labelled seeds n0..3,279 actual activated roots including a named t2 fixture,1116 physical pair terminals and1116 explicit reset terminals;11439 exact assertions PASS in44.060s. Canonical reduction is verified against EVERY independent source parity basis through3bits; it is a checked transform, not a symmetry counting shortcut.

Main arithmetic: integer FWHT, exact Fraction directional/physical influences, prime-log entropy vectors, full root affine-minimum inequalities and affine-span ranks, actual entropy-preserving shear permutations, exact signed banks at K0,16/5,15/4,8. Separate replay uses direct characters and independently evaluated physical exponents/substitution on point2 and literal fixtures. It also reconstructs even-hyperplane rank guards d3,d5 and the rational scalar negative-bank certificate:37 assertions PASS in0.084s. Combined final full total11476; pilot excluded. Different implementation by A005 is not independent-agent acceptance.

The all-t bridge and derivative/rank arguments are analytic proofs; finite domains do not establish them by extrapolation. Exact atanh tails enclose logarithms for the source-deficit sign. Zero coefficients, constants, negative means, ties, rank0 and all reaches are retained. Jobs had55s caps, estimated90MB, no dimension escalation, GPU, detached jobs or heavy search. Compute snapshot reported status ok,3.3GB physical free,88.2percent commit used. No existing work changed. No new Lean attempt or formal certification is claimed.

# proof dependencies and changed downstream conclusions

REVIEW independently reconstructs A002 reset optimum/child correction at equations1--5 and A052 rank ownership/complete bank at Sections1--2, unchanged and without repair. Source all-k curvature, deferred-control telescope and census totals are not newly independently accepted. Previously reviewed A051 finite affine-basis criterion is consumed. The new paid-pair weak-affine endpoint is author-proved with exact checks, pending independent-agent review. No source theorem is refuted. The downstream guard strengthens: even an already-paid original pair does not make a weak affine endpoint easier; the unused signed terminal bank must enter the next universal claim explicitly.

# one next mathematical action and independent reviewer

A051/A052 use nonnegative reserves of ALL smaller Boolean affine images to force an adequate quotient-rank increment at one ORIGINAL proper pair, with SAME unused bank, mixed T and complete terminals. A002/A055 should independently reconstruct tensor-before-activation, the four means and Lipschitz finite-to-infinite bridge; A090/A094 should challenge shear ownership and the rational negative-bank certificate. This is a source-bound saved handoff, not a sent message.

# actual persistence receipts or precise save blocker

All four protocol files, DERIVATION, REVIEW, frozen spec, scripts and exact outputs saved only under A005. Finalizer verifies exact protocol field sets, statement SHA256, byte-identical PROGRESS/PACKET_DELTA, required headings, two-line STATUS and20MB cap; persistence receipt hashes each run artifact and all rolling files, then reopens and verifies every hash. Local save is verified. Independent-agent acceptance, registry adoption, supervisor repository copying and brain ingestion remain unverified. No git or brain/shared-source writes were performed. No stage job remains running and no existing work was stopped.

## Universal bridge

C019 stopping-tree payment through critical original-pair selection gains a SAME-K hardness guard for a stronger endpoint: a real non-character original pair is already paid, full affine span/minimality and arbitrarily weak total influence are preserved, and arbitrary core ratio survives. The explicit local price tends16/5, with a rational finite negative-bank witness at15/4; universal constant gain is0. What remains is selection using the nonnegative unused reserve of genuine smaller Boolean affine children, not merely a paid fragment or root geometry. NEXT targets that precise excluded hypothesis and lower-funding direction, so it addresses the universal unpaid implication rather than another isolated class that still contains arbitrary seed entropy.
"""
save(R/'REPORT.md',report)
save(OWN/'STATUS.md','STATE: A005 stage18 saved: paid original non-character pair inside weak full-span affine minima is SAME-K FEI-hard for K>16/5;11476 exact checks PASS; FEI OPEN.\nNEXT: A051/A052 force pair funding from NONNEGATIVE smaller-child affine reserves and SAME unused bank/mixed T; A002/A055 review whole-activation paid-pair embedding.\n')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
for name,text in [
 ('WORKLOG.md',f'\n{stamp} stage18: Consumed new A002/A051/A052/A055 dependencies. Scoped independent rank/activation reconstructions HOLD. Tensor-before-activation preserves a paid original non-character pair and arbitrary canonical seed ratio inside weak full-span affine minima, SAME K>16/5. Pilot902; full11439+independent37=11476 exact assertions PASS. Fixed point8 t1e8/k10000 certificate has positive pair margin but all4 negative terminal reserves. Full FEI/open critical selection unchanged; no jobs left, no shared writes.\n'),
 ('LEARNED.md','\nStage18 durable fact: Q=(-1)^(ab+ac+bc+za) times g^t, THEN whole point activation, has I_pair=p and explicit shear release p/4 on original(a,b). All4 terminal cores persist. Exact L_pair=4p+R_k(mu^t/4)-[R_k(mu^t)+3R_k(0)]/4; abs(L_pair/p-4)<=(13+6k)|mu|^t. With k=ceil(sqrt(t)), explicit pair price tends16/5 while H/I tends canonical seed ratio and I->0. Hence paid-pair full-span affine-minimal weak-I endpoint remains SAME-K FEI-hard for every K>16/5. Genuine smaller-child nonviolation excludes positive-core members: all4 affine-optimized terminals still violate. Never confuse an already-paid local fragment with its unpaid complete terminal bank. Fixed point8/t1e8/k10000/K15/4 certificate: pair margin/p>7633553/12500016; each terminal deficit/p>862405/4. A002 equations1--5 and A052 rank/complete bank Sections1--2 scoped independent HOLDS; no complete source-claim acceptance implied.\n')]:
    with (OWN/name).open('a',encoding='utf-8',newline='\n') as f:f.write(text)
required=protocol['required_per_run']
assert set(claim)==set(required['claim_fields'])
pf=[x if not x.startswith('packet_ids ') else 'packet_ids' for x in required['progress_fields']]
assert set(progress)==set(pf)
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert hashlib.sha256(read(R/'CLAIMS.json')[0]['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
assert all('# '+x in (R/'REPORT.md').read_text(encoding='utf-8') for x in required['report_fields'])
assert len((OWN/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
paths=sorted([p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json'])+[OWN/x for x in ['STATUS.md','WORKLOG.md','LEARNED.md']]
assert all(p.stat().st_size<20*1024*1024 for p in paths)
receipt={'status':'LOCAL_READBACK_VERIFIED','utc':stamp,'remote_copy':'UNVERIFIED; supervisor responsibility','files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in paths]}
js(R/'out/PERSISTENCE_RECEIPT.json',receipt)
for entry in read(R/'out/PERSISTENCE_RECEIPT.json')['files']:
    assert sha(Path(entry['path']))==entry['sha256']
print(json.dumps({'status':'PASS','hashes_verified':len(paths),'exact_assertions':main['assertions']+ind['assertions'],'claim':claim['claim_id'],'full_fei':'OPEN'}))
