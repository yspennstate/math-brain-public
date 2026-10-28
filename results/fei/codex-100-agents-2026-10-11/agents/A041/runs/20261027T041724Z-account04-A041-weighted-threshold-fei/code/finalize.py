from pathlib import Path
from datetime import datetime, timezone
import hashlib,json

R=Path(__file__).resolve().parents[1];OWN=R.parents[1]
RUN=R.name;STAMP=datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
main=read(R/'out/CHECKS.json');pilot=read(R/'out/PILOT.json');review=read(R/'out/A045_CHECKS.json');adv=read(R/'out/ADVERSARIAL.json')
assert all(x['status']=='PASS' for x in [main,pilot,review,adv])
assert (main['checks'],review['checks'],adv['checks'])==(2084,330,14)
src=OWN.parent/'A045/runs/20261027T005611Z-account04-A045-biased-realizability-referee'
old=read(src/'CLAIMS.json')[1]
assert sha(src/'PROOF.md')=='f8d7501f6ab31569160bae0cd28af6bf006619e6cd72794559246a1bf91156e7'
assert old['statement_sha256']=='9d6a1705eeee9f23e3ba41ec07db7e7878ac49ca87594362371c881b79bf6c56'
reviewtext='''# A045 prime rare-boundary claim: scoped independent reconstruction

Verdict: HOLDS for the new A045-PRIME-RARE-BOUNDARY-RESERVE-OBSTRUCTION@1.
Original statement hash:9d6a1705eeee9f23e3ba41ec07db7e7878ac49ca87594362371c881b79bf6c56.
Original proof hash:f8d7501f6ab31569160bae0cd28af6bf006619e6cd72794559246a1bf91156e7.

Three count rows0,1,2 on any proper block of size at least2 and outside
counts0,1 give three different cofactor rows. Thus the T2 gate is prime.
Its core derivatives are(q0+q1)/2; its core-pair coefficient is(q0-q1)/2.
Union bounds give t>1/4, c12>=3/8 and both scales exactly1. A rare
derivative is(1/2)q'_0+(1/4)q'_1<=1/2, so I<=1+2m epsilon.
The mean stays in[-1/2,-1/4], hence Var>=3/4. With
a=binom(m,2)epsilon^2, J1/ln4>=1/2-a. Discarding only nonnegative L1
gives D=(Bstar+ln4R)/ln4<=4m epsilon+a<=5m epsilon.
The nonzero top coefficient gives R>0; Bstar>=0 is the already supplied
joint singleton premise. Since Jhi/ln4>=9/64, division by positive D
gives the stated9/(320m epsilon) bound, for every n>=3 and allowed epsilon.
The choice of epsilon after n is legitimate for the existential
counterfamily. No supremum or limiting interchange is used.

The independent checker uses A041's own exact centered transform, explicit
all-block cofactor rows and rational log intervals:12 cases,330 assertions.
No source checker is run or copied. The source's exception for all symmetric
thresholds remains valid. A041's previous singleton source is a dependency
authored by this reviewer; this review does NOT claim an independent
reacceptance of that upstream premise or of the entire universal FEI chain.
No repair is supplied to the reviewed version. The new nonsymmetric
extension is separated in PROOF.md and has no independent acceptance yet.
'''
(R/'REVIEW.md').write_text(reviewtext,encoding='utf-8')
rr={'reviewer':'A041/account04','outcome':'HOLDS_NEW_OBSTRUCTION_AT_STATED_SCOPE',
    'source_statement_sha256':old['statement_sha256'],'source_proof_sha256':sha(src/'PROOF.md'),
    'repair_supplied':False,'scope':'New prime rare-boundary theorem only; not independent reacceptance of A041-authored upstream singleton premise',
    'proof':'REVIEW.md','checks':'out/A045_CHECKS.json','source_checker_run':False}
old['review_records'].append(rr);old['status']='SCOPED_INDEPENDENT_OBSTRUCTION_RECONSTRUCTION_HOLDS'
statement=('For every m>=3 and 0<epsilon<=1/(8m), the actual Boolean sign F=+1 iff '
'3b1+3b2+2 sum_(i=3)^(m+2) b_i>=5 at independent biases(1/2,1/2,epsilon,...,epsilon) '
'is essential, nonsymmetric and prime under proper disjoint Boolean single-wire substitutions. '
'With the actual centered product spectrum and upper dyadic scales, natural units, '
'Jhi>=9 ln4/64 and0<Bstar+ln4 R<=5 ln4 m epsilon, hence '
'Jhi/(Bstar+ln4R)>=9/(320m epsilon). The same truth table has core weight w, rare weight1 '
'and threshold w+1 for every real1<w<2. Therefore no finite K pays Jhi from Bstar or '
'Bstar+ln4R after excluding ALL symmetric gates and every fixed finite arity cutoff. '
'This refutes only those diminished-source suppliers, not corrected FEI+, spectral erasure '
'or full FEI; all old imports/carries and both complete terminal laws retain their owners.')
claim={'claim_id':'A041-NONSYMMETRIC-TWO-WEIGHT-PRIME-BOUNDARY','version':1,
'exact_statement':statement,'hypotheses':[
'm>=3, actual finite Boolean sign, independent interior physical biases and 0<epsilon<=1/(8m)',
'Disjoint one-wire Boolean primeness; no affine or overlapping-variable primeness asserted',
'P(S)=v_S c_S^2, Delta=I-Var, R=sum_high (|S|-2)P(S); upper dyadic convention1/2<2^j|c|<=1',
'Bstar=ln4(2Delta-R)-J1-ln2 L1, with natural logarithms and all old charges retained',
'Finite-cutoff and symmetric exceptions only; separately paying this family or nondegenerate-bias restrictions not refuted'],
'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),
'contributors':['A041/account04'],'proof_source':{'path':str(R/'PROOF.md'),'sha256':sha(R/'PROOF.md'),'exact_checks':['out/CHECKS.json','out/PILOT.json','out/ADVERSARIAL.json']},
'proof_dependencies':[{'claim_id':'A041-SHARP-JOINT-SINGLETON-SOURCE','version':1,'statement_sha256':'858bf303c4d23127fd913d7bc8c6e670e56b44a2ac6db09f682328ce51ed371f','used_scope':'Bstar>=0; scalar proof restated'},'Exact cofactor-row obstruction, Boolean derivative identities and finite union bounds; A045 boundary construction motivates the extension but supplies no unverified new premise'],
'review_records':[],'status':'ANALYTIC_PROOF_EXACT_CHECKS_PENDING_INDEPENDENT_REVIEW','supersedes':[],
'refutes':['Unregistered Jhi<=K Bstar or K(Bstar+ln4R) supplier restricted to nonsymmetric primes beyond a finite arity cutoff'],
'first_unproved_line':None,'next_consumers':['A045','A044','A043','A091','B09 lead']}
save(R/'CLAIMS.json',[old,claim]);save(R/'out/A045_REVIEW.json',rr)
progress={
'protocol_revision':'2026-10-11-execution-v2','run_id':RUN,'stream':'B09','packet_id':'A041',
'gap_id':'G-BIASED-LTF-ORIGINAL-HIGH-SECTOR-SUPPLIER',
'attempt_id':'A041-stage22-nonsymmetric-prime-rare-boundary',
'method':'Consume A045 new boundary obstruction; independent reconstruction and nonsymmetric two-weight prime extension; exact product-spectrum certificates',
'mathematical_delta':'Closes all-symmetric-exception loophole: diminished singleton reserve(+degree refund) cannot pay high scale on nonsymmetric primes at unbounded arity. Original core high bill must survive rare-input transfer.',
'deliverable_status':'COMPLETE_LOCAL_PENDING_SUPERVISOR_COPY',
'mathematical_status':'RESTRICTED_OBSTRUCTION_PROVED_PENDING_INDEPENDENT_REVIEW; FULL_FEI_OPEN',
'claim_versions_used':[{'claim_id':old['claim_id'],'version':1,'statement_sha256':old['statement_sha256']},{'claim_id':'A041-SHARP-JOINT-SINGLETON-SOURCE','version':1,'statement_sha256':'858bf303c4d23127fd913d7bc8c6e670e56b44a2ac6db09f682328ce51ed371f'}],
'claims_created_or_changed':[{'claim_id':old['claim_id'],'version':1,'change':'scoped new-obstruction review added locally'},{'claim_id':claim['claim_id'],'version':1,'change':'new narrowed obstruction'}],
'source_artifacts':[str(src/'PROOF.md'),str(src/'CLAIMS.json'),'PROOF.md','REVIEW.md','out/CHECKS.json','out/A045_CHECKS.json','out/ADVERSARIAL.json'],
'next_consumers':['A045','A044','A043','A091','B09 lead'],
'next_action':'Construct an original rare-input/core high-sector transfer that retains the boundary core bill and pays the perturbation from SAME unused original influence after all singleton/import/carry and full terminal charges.',
'stagnant_substantive_attempts':0,
'blockers':['Universal arbitrary-prime high-sector payment unpaid','New nonsymmetric obstruction pending independent review','Lean attempt RUNTIME_UNVERIFIED; no formal certification','Supervisor copy, mirror and brain ingestion unobserved'],
'packet_ids':['A041']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
report='''# exact target, quantifiers, hypotheses and units

Test the remaining singleton reserve as a complete high-sector supplier after
excluding symmetric thresholds and every fixed finite arity cutoff. The exact
new family is F_m=+1 iff3b1+3b2+2 sum_rare b_i>=5, for all m>=3,
independent biases(1/2,1/2,epsilon,...,epsilon),0<epsilon<=1/(8m).
Natural logs; P(S)=v_S c_S^2; upper dyadic rounding. Primeness means proper
disjoint Boolean single-wire substitution. Full FEI and arbitrary weighted
product-biased FEI+ remain OPEN.

# sources actually read, revisions and theorem locators

Execution protocol2026-10-11-execution-v2 read in full; current BOARD
written27Oct04:12UTC, B09 STREAM_NOTES v2, own STATUS/LEARNED and preceding
23Oct13:53 run REPORT/CLAIMS/PROOF. Campaign README, CURRENT_STATUS,
CLAIM_REGISTRY, OBSTRUCTION_REGISTRY, PACKET_STATUS, STREAM_NEXT_ACTIONS and
plan were inspected at their B09/weighted/bridge locators; supplemental
CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING and sources route
map were consulted. New original dependency: A04527Oct00:56 PROOF/CLAIMS,
statement9d6a1705... and prooff8d7501f... (full hashes in CLAIMS/receipts).
The new source is reconstructed in REVIEW.md. Current paper rereads use
threshold38pp lines1347,1603,2014 and earlier29pp1062,1313,1729;
the percolation extracts were encoding-inspected but supply no new premise.
All four supplied PDF text extracts fail strict UTF-8 and decode as cp1252;
this is recorded rather than silently replacing characters. Earlier full
baseline intake remains prior-stage evidence. One read-only math recall
with two phrasings supplied contextual cards, no answer or new premise.
Current scheduled RESEARCH control and PRIMARY_DIRECTIVE were read;
current FEI scope governs. No external publication or literature claim added.

# complete derivation or exact first unsupported line

REVIEW.md reconstructs A045's prime boundary theorem at its new-obstruction
scope. A041 authored one upstream premise, which is explicitly not counted
as independently reaccepted. No source repair or source checker adoption.

PROOF.md proves the new nonsymmetric family is essential and prime: every
proper block has three explicit cofactor rows. Core counts0,1,2 require rare
counts3,1,0. For K~Binomial(m,epsilon), t_core=Pr(K<=2)/2 and
c12=(Pr(K=0)-Pr(K=1)-Pr(K=2))/2>=3/8. Their exact dyadic scales are1,
giving Jhi>=9ln4/64. Rare pivotality<=1/2 gives I<=1+2m epsilon;
the output mean lies in[-1/2,-1/4], so Var>=3/4. Core singleton scales
give J1/ln4>=1/2-binom(m,3)epsilon^3. Dropping only nonnegative L1 yields
0<Bstar+ln4R<=5ln4 m epsilon. Strict positivity uses the Maj3 physical
restriction, hence positive degree>=3 mass at every interior law. Therefore
Jhi/(Bstar+ln4R)>=9/(320m epsilon). For each fixed m choose epsilon
arbitrarily small; m may exceed any prescribed cutoff. No limit is moved
past a sum. The same truth table has core weights w in(1,2), rare weights1
and threshold w+1. Excluding ALL symmetric gates cannot remove it.

This is a diminished-account obstruction, not growing H/I. Deterministic
contraction at epsilon0 gives fair AND2 with a positive original core bill.
The exact first unsupported universal line remains a complete rare-input/core
transfer retaining that bill and paying perturbation from unused ORIGINAL
influence after all previous singleton/import/carry and terminal charges.
Conditional-input TC is not spectral erasure; the recovered pivotal-credit
failure remains coefficient-one only.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs precede enumeration. Commands, relative to this run:
python -X utf8 code/check.py --pilot; python -X utf8 code/check.py;
python -X utf8 code/review.py; python -X utf8 code/adversarial.py.
Pilot:79 exact assertions,1 case; main:2084 assertions,16 cases with
m=3..6 and epsilon=1/(km),k=8,16,64,256; source review:330 assertions,
12 T2 cases;m=1..4,k=8,32,128. All PASS. Adversarial:14 checks PASS,
including m1 symmetry, m2 nonprime rare-OR block, and fixed rational weight
ratios5/4,3/2,7/4. These hypothesis cuts are not counterexamples to the
stated m>=3 theorem. Exact runtimes are in the output JSON files; research
checks each finish below1s. No automatic dimension increase or symmetry
quotient. Every proper block is checked on the finite domains.

Arithmetic: exact Fraction physical centered-product expansion, degree
energies and dyadic scales; direct physical coefficient summation independently
checks the pilot transform; binomial pivotal/pair formulas independently check
main spectra. Natural logs use24-term outward atanh rational intervals, not
floats or tolerances. The all-arity conclusion comes from PROOF.md, not
finite extrapolation. Estimated80MB per checker,55s caps, no >300MB job,
GPU, detached worker, or background service. A core-Lean Boolean pigeonhole
attempt returned RUNTIME_UNVERIFIED after121.3s; no theorem, compiler or
axiom certificate is claimed. Rung: analytic proof plus exact finite
validation, pending independent review.

# proof dependencies and changed downstream conclusions

The A045 new prime obstruction survives independent reconstruction, with the
upstream-authorship caveat in REVIEW.md. New
A041-NONSYMMETRIC-TWO-WEIGHT-PRIME-BOUNDARY@1 adds an all-arity nonsymmetric
two-weight obstruction. It closes precisely the symmetric-exception loophole
left by A045. The singleton source is unchanged; Bstar remains its SAME
diminished remainder. Neither adding the old degree refund nor choosing only
large nonsymmetric primes supplies a complete high-sector payment. All prior
mantissas, imports, genuine low/high carries, positive S_tree, normalization,
ordinary KL and BOTH complete terminals remain booked; no credit renewed.
No claimed FEI or corrected-FEI+ theorem is refuted.

# one next mathematical action and independent reviewer

Construct an original rare-input/core transfer retaining the boundary core
high-sector bill and paying perturbation from the SAME unused original
influence after every old debit. A045/A044 should independently verify all
four cofactor-block cases, the degree restriction and exact denominator;
A043/A091 should check the disjoint-prime and exception scopes. A review
handoff is saved only; no message, acceptance or downstream use is assumed.

# actual persistence receipts or precise save blocker

Required REPORT/CLAIMS/PROGRESS/PACKET_DELTA, PROOF, REVIEW, frozen specs,
code and outputs are saved in this designated run; PROGRESS and PACKET_DELTA
are identical. STATUS is exactly two lines; dated WORKLOG and LEARNED are
appended once. Source and final artifact SHA256 receipts are in out/RECEIPTS.
Supervisor copy, mirror, brain ingestion and independent acceptance remain
unobserved. Research writes are confined to A041; the required checklist
lifecycle and wake/voice/formal helper calls are the only external hooks.
No git, mail, brain-store write, other-agent edit or trading-stack access.

The wake required an owner alert: owner-model/state/dream notes are stale;
these personal-context notes are not mathematical premises. The compute
snapshot reports status ok and no recent intervention; private-memory group
censuses include other work and retained objects, and do not establish a
current bottleneck. Existing work is left running. No process is stopped,
suspended, throttled or restarted. All A041 research check commands finish.

Universal bridge: This stage moves C020 whole-set witness cost and C024
history transfer by closing the symmetric-exception loophole in the proposed
diminished high-sector supplier: actual nonsymmetric two-weight prime gates
of unbounded arity have Jhi>=9ln4/64 while Bstar+ln4R<=5ln4 m epsilon.
The universal unpaid step is now a boundary-core-aware ORIGINAL high-sector
payment, with every old debit and both full terminals retained. NEXT is the
shortest route because paying another normalizer or excluding more small or
symmetric gates cannot fund a core bill that survives physical contraction.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
state='STATE: Stage22 saved: nonsymmetric two-weight prime boundary obstruction proved;2084+330+14 exact checks PASS; A045 new scoped obstruction HOLDS; review pending; FEI OPEN.\nNEXT: Pay boundary-core high-sector bill and rare perturbation from SAME unused ORIGINAL influence, old imports/carries/BOTH terminals retained; Bstar(+ln4R) fails after all symmetric/finite-prime exclusions; A045/A044/A091 review.\n'
(OWN/'STATUS.md').write_text(state,encoding='utf-8')
lesson='''Nonsymmetric two-weight prime boundary: for m>=3, F=1 iff3b1+3b2+2 sum_rare b>=5, biases(1/2,1/2,epsilon^m),0<epsilon<=1/(8m), has Jhi>=9ln4/64 and0<Bstar+ln4R<=5ln4 m epsilon. Every proper block has >=3 cofactor rows. Thus excluding ALL symmetric thresholds and a finite arity cutoff does not repair either diminished source. Real core ratio w in(1,2), threshold w+1 gives same truth table. m2 fails primeness (rare OR block); m1 is symmetric Maj3. The limiting AND2 core bill survives deterministic contraction and needs its ORIGINAL owner. No FEI counterexample; TC/erasure and coefficient-one scopes unchanged. Lean runtime unverified is not a certificate.'''
for name,body in [('LEARNED.md',lesson),('WORKLOG.md','Consumed A045 new prime boundary, independently reconstructed its new-obstruction scope (upstream-authorship caveat), proved nonsymmetric two-weight extension; pilot79/main2084/source330/adversarial14 exact assertions PASS. Saved full protocol artifacts. Original high-sector/core-transfer payment remains open.')]:
    f=OWN/name;s=f.read_text(encoding='utf-8') if f.exists() else ''
    if RUN not in s:f.write_text(s+'\n\n'+STAMP+' ['+RUN+'] '+body+'\n',encoding='utf-8')
sources=[src/'PROOF.md',src/'CLAIMS.json',OWN/'runs/20261023T135351Z-account03-A041-weighted-threshold-fei/PROOF.md',OWN.parents[1]/'BOARD.md']
save(R/'out/RECEIPTS.json',{'at':STAMP,'source_sha256':{str(p):sha(p) for p in sources if p.is_file()},'artifact_sha256':{str(p.relative_to(R)):sha(p) for p in R.rglob('*') if p.is_file() and p.name!='RECEIPTS.json'},'remote_copy':'UNOBSERVED','independent_review':'PENDING'})
print(json.dumps({'saved':RUN,'claim_sha256':claim['statement_sha256'],'progress_matches':(R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes(),'checks':main['checks']+review['checks']+adv['checks']}))
