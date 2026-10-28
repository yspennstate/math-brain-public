"""Persist this stage and verify the exact field contract and hashes."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path(__file__).resolve().parents[1]; A=R.parents[1]; S=A.parents[1]
P=Path('math-open-problems/reports/fei-2026-10-11')
SRC=S/'agents/A008/runs/20261023T062437Z-account03-A008-gate-label-compression'
PRIOR=A/'runs/20261023T035924Z-account03-A015-minterm-barrier-analysis'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
pilot=read(R/'out/pilot.json'); full=read(R/'out/exact_checks.json')
assert pilot['assertions']==443 and full['assertions']==104744
assert pilot['script_sha256']==full['script_sha256']==sha(R/'code/check.py')
for k,v in {'generic_cases':784,'physical_cases':17,'physical_truth_points':66832,'signed_faces':20736,'scalar_profiles':625,'source_z_bound':97,'tree_hypotheses':12}.items(): assert full['counts'][k]==v
original=next(c for c in read(SRC/'CLAIMS.json') if c['claim_id']=='A008-RARE-CHILD-MOMENT-AND-FIXED-POLARITY-MIXTURE-OBSTRUCTION')
canonical=json.dumps({'statement':original['exact_statement'],'hypotheses':original['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False)
assert hashlib.sha256(canonical.encode('utf-8')).hexdigest()==original['statement_sha256']
imported=json.loads(json.dumps(original)); imported['review_records'].append({'reviewer':'A015','role':'Independent full-scope reconstruction and fresh exact helper, no source repair','verdict':'HOLDS_FULL_STATED_SCOPE','evidence':[str(R/'REVIEW_A008.md'),str(R/'out/exact_checks.json')]})
imported['status']='INDEPENDENTLY_REVIEWED_A015_AT_STATED_SCOPE'
imported['proof_source']=[str(SRC/x) for x in original['proof_source']]+[str(R/'REVIEW_A008.md')]
statement=('For independent uniform-cube blocks X,Y and nonconstant indicators U,V, a=EU,b=EV,g=2U-1,h=2V-1,F=2UV-1, any fixed positive normalized nonempty references q_g,q_h define a positive normalized nonempty Q by a uniform choice of X-only,Y-only,both and independent q sampling on used blocks. Its EXACT complete nonempty cost is C_Q(F)=Var(F)log2(3)+b C_g+a C_h and I(F)=b I(g)+a I(h). In particular, for independent w_X,w_Y>=4, r_i=2^w_i disjoint OR clauses of arbitrary widths in{w_i,w_i+1}, U_i their AND, F=2U_X[1-U_Y(-Y)]-1, choose each local nonempty clause mask by Bernoulli rho_i=1/(2r_i) conditioned nonempty and a uniform nonempty subset in each active clause. This FULL explicit joint-sector reference has C_Q(F)<=[11/2+log2(3)]I(F)<8I(F). Adding its actual empty/nonempty wrapper gives full cost<[13/2+log2(3)]I(F)<9I(F). Every mask, subset, sector and nonempty normalizer is included. This is a new root reference, not an original queue or a free reset; no universal physical-overlap or unlimited-composition claim is made.')
claim={'claim_id':'A015-ONCE-TAGGED-JOINT-DICTIONARY-REFERENCE','version':1,'exact_statement':statement,
 'hypotheses':['Costs in bits; uniform cube and physically disjoint component blocks','Generic identity: supplied positive normalized references fixed before sampling; local C is nonempty cross entropy','Explicit family: integers w_X,w_Y>=4; r_i=2^w_i disjoint clauses of widths w_i or w_i+1 in each component','References and clause dictionaries fixed before the target spectral set; full wrapper uses the stated actual Var(F)','No identification of this new sampler with the refuted original prime queues; no unpaid reference change in an existing history'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A015'],
 'proof_source':['JOINT_DICTIONARY_CODE.md','code/check.py','out/exact_checks.json'],
 'proof_dependencies':['Direct disjoint Fourier composition, explicit reference normalization, clause activation moments and pivotal counting; all proved in JOINT_DICTIONARY_CODE.md','Parseval Var(f)<=I(f); elementary Bernoulli inequality and binomial-series bound sum1/j!<3'],
 'review_records':[{'reviewer':'A015','role':'Author analytic proof plus exact independently represented physical-table checks; not independent-agent acceptance','verdict':'PASS','evidence':['JOINT_DICTIONARY_CODE.md','out/exact_checks.json']}],
 'status':'AUTHOR_PROOF_EXACT_CHECKS_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A007','A008','A014','A086','A094','B03','B20']}
dump(R/'CLAIMS.json',[imported,claim])
next_action=('Generalize the paid whole-set dictionary interface to physically overlapping clauses: identify an exact joint activation-moment replacement and pay the sector/dictionary tag once from a single influence account. First independently review this disjoint interface; do not restart a fixed pair of original polarity queues or infer unlimited composition closure.')
sources=[P/'EXECUTION_PROTOCOL.json',S/'BOARD.md',S/'claude/B03/STREAM_NOTES.md',SRC/'REPORT.md',SRC/'CLAIMS.json',SRC/'MIXTURE_OBSTRUCTION.md',PRIOR/'CLAIMS.json',PRIOR/'SUBPROBABILITY_TRANSPORT.md',P/'source_material/reductions/paper/forests.tex']
dump(R/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B03','packet_id':'A015','gap_id':'C020-WHOLE-SET-DICTIONARY-REFERENCE-PAYMENT','attempt_id':'A015-stage9-fixed-mixture-review-joint-mask-code','method':'Consume and independently reconstruct the new fixed-mixture obstruction; change representation to a once-paid normalized whole-set dictionary; exact disjoint sector and activation moments',
 'mathematical_delta':'Independent full-scope HOLDS for A008 fixed-polarity-mixture obstruction@1. New explicit joint dictionary repairs its actual family: nonempty cost<8I, full wrapped cost<9I, also independent mixed widths and unequal block parameters. All-parameter author proof plus104744 full exact checks. Physical-overlap influence payment and full FEI remain OPEN.',
 'deliverable_status':'COMPLETE_LOCAL_PROTOCOL_PROOFS_CHECKS_AND_RECEIPTS','mathematical_status':'A008_REVIEW_COMPLETE_NEW_BOUNDED_INTERFACE_PENDING_INDEPENDENT_REVIEW_UNIVERSAL_BRIDGE_OPEN',
 'claim_versions_used':[original['claim_id']+'@1 (independently reviewed; target obstruction, not a premise of new upper bound)','A015-SUBPROBABILITY-ORIGINAL-REFERENCE-HISTORY-TRANSFER@1 (conditional downstream application only; not a premise of new root bound)'],
 'claims_created_or_changed':[original['claim_id']+'@1: independent A015 review, statement unchanged',claim['claim_id']+'@1'],
 'source_artifacts':['REVIEW_A008.md','JOINT_DICTIONARY_CODE.md','FROZEN_SPEC.json','code/check.py','out/pilot.json','out/exact_checks.json','out/SOURCE_RECEIPTS.json','out/RECEIPTS.json'],
 'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Universal joint-dictionary payment under physical overlap remains unsupported; full FEI OPEN','New bounded disjoint-code proof and prior supplied-reference transport await independent review; no unlimited-composition closure','Brain self-care degraded/unverified: owner-model97.5h, state-of-mind82.1h, dream32.8h stale; personal-context freshness affected','Supervisor owns copying and registry adoption; remote persistence unverified','Checklist T-20261023-356 done attempt exited1: shared checklist lock held too long; research artifacts are complete, workflow closure unverified'],'packet_ids':['A015']}
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
report=f'''# A015 stage9: pay the shared clause dictionary once

## exact target, quantifiers, hypotheses and units

Replace the obsolete NEXT of paying the original nonsymmetric prime queue:
A008 now refutes even every fixed mixture of its two polarities. Independently
review that exact obstruction, then explicitly pay the missing whole-set
dictionary feature on its ACTUAL Boolean family. Units bits, physical
uniform cubes, disjoint blocks. The reusable exact identity holds for every
pair of independent indicators and every fixed positive normalized local
nonempty reference. The explicit bound holds for ALL integers w_X,w_Y>=4,
r_i=2^w_i, arbitrary patterns of disjoint clause widths in{{w_i,w_i+1}},
and F=2U_X[1-U_Y(-Y)]-1. It is not a universal representation theorem.

## sources actually read, revisions and theorem locators

Read BOARD current2026-10-23 10:53UTC, B03 STREAM_NOTES v2, own STATUS,
machine AGENTS and execution protocol2026-10-11-execution-v2. Source
campaign deadline in this legacy protocol is superseded by the user's
2026-10-23 14:49UTC direction. Read the crash-restore common note and
current compute state: no completed earlier product restarted. Read A007's
latest root-component/polarity report and claims, A010's latest component
factorization report, and A008's latest REPORT/CLAIMS and complete
MIXTURE_OBSTRUCTION.md. Reconstructed original forests.tex queue definitions
and conditioned root law; used own previous supplied-reference proof only
for an explicitly conditional downstream application. Baseline campaign
and paper reads are inherited, not falsely described as new full rereads.
No threshold theorem or assumed FEI inequality is needed by either current
proof. Exact source pins are out/SOURCE_RECEIPTS.json.

## complete derivation or exact first unsupported line

REVIEW_A008.md independently reconstructs the full version1 marked-child
moment and fixed-polarity-mixture obstruction, without repair. All finite
runs, arbitrary feasible weights/orders, root normalizers, repeated visits
and ambiguous outputs are retained. Its verdict is HOLDS at unchanged
hash8665cf2638011cb0dffa64b7c0cad0b347746eeb92dc2541e4bbc262ce55e6e5.
The source's nonempty cost/I>w/2592 and actual H/I<8 remain valid.

JOINT_DICTIONARY_CODE.md is the complete new proof. Choose one of three
sectors uniformly, then sample fixed local nonempty dictionaries independently
in used blocks. Q(S,empty)=q_X(S)/3, Q(empty,T)=q_Y(T)/3, and
Q(S,T)=q_X(S)q_Y(T)/3. Summing its entire output law gives EXACTLY

    C_Q(F)=Var(F)log2(3)+b C_g+a C_h,
    I(F)=b I(g)+a I(h).

For each clause component, choose rho=1/(2r) BEFORE the spectral target.
Draw a Bernoulli-rho activation mask conditioned nonempty and a uniform
nonempty coordinate subset in each active clause. The exact probability is

    q(S)=rho^t(1-rho)^(r-t)
         /[(1-(1-rho)^r) prod_active(2^d_j-1)].

This is a NEW sampler: there are no original queue visits/attachments whose
cost has silently been erased. All choices of this sampler are normalized
and paid. Bernoulli's inequality bounds inactive-mask length by1. Active
clause length is at most w+1+d_j<=(9/4)d_j. The actual Boolean activation
moment is4a sum d_j epsilon_j, at most2I(g), by direct pivotal counting.
Thus each entire local cost<=11I(g)/2, giving nonempty joint cost
<=[11/2+log2(3)]I(F)<8I(F). The family has I(F)>1, proved without large
rational powers using binomial comparison and sum1/j!<3. Adding the FULL
actual empty/nonempty wrapper gives cost<[13/2+log2(3)]I(F)<9I(F).

Every dictionary, width and prior is fixed before sampling. The actual
spectral product law is used only to calculate moments; it is not secretly
chosen as the reference. This is a mechanism repair on a known read-once
FEI family, not a new claim of resolving that FEI class.

First unsupported UNIVERSAL line: construct a whole-set dictionary reference
whose complete cost is influence-paid when physical supports overlap.
Disjoint moment factorization fails under shared variables. Also, repeatedly
applying the one-level identity can accumulate sector tags: no unlimited
composition closure is proved. No original queue bound or free reference
reset follows. Full FEI remains OPEN.

## executed validation with domain, arithmetic, commands and outputs

Frozen FROZEN_SPEC.json predates execution. Commands from this directory:
`python -X utf8 code/check.py --pilot` passed443 assertions in
{pilot['elapsed_seconds']}s; `python -X utf8 code/check.py` passed104744 in
{full['elapsed_seconds']}s. Total105187 assertions includes pilot overlap.
The counters separate assertion calls from domain sizes; an initial pilot
display counted domain sizes too, corrected before this final pilot/full
pair without changing the frozen family or acceptance conditions.

Full scope: all14 nonconstant two-bit functions in each component and four
fixed reference pairs give784 exact cost identities;16 mixed-width small
physical functions plus a16-variable homogeneous function give66832 truth
points and66815 nonempty coefficients checked. All20736 signed faces on
the small physical domain are enumerated against complete prime tables.
625 scalar profiles cover w4..128 and five width-pattern counts modulo
clause permutation. These use only exact moment quantities, not giant
truth tables or giant rational powers.97 obstruction parameters w32..128,
the rational PGF certificate, and12 marked-tree fixtures through height3
check the source reconstruction. All domain counts match the frozen spec.

Integer Walsh, direct truth-table flips, Fractions and prime-exponent
vectors certify identities exactly. Cost intervals use atanh-series log
bounds with an analytic tail and outward48-bit dyadic rounding. No floating
sign or numerical extrapolation is a proof premise. The toy dimensions
w1,2 are finite identity tests, outside the w>=4 analytic upper-bound
hypothesis; no false finite-to-infinite inference is made.

Negative controls PASS: removing the mask normalizer loses mass; reusing
the SAME OR2 variables gives actual influence1 versus the invalid disjoint
prediction3/2. Distinct source queue and new-reference semantics are explicit.
Code estimated100MB, frozen55s cap, no >300MB admission needed. Shared
snapshot:17316MB available,69.3percent commit, disk67GB. No running work
stopped, no GPU, no background jobs, no automatic dimension escalation.

## proof dependencies and changed downstream conclusions

A008 obstruction@1 gains an independent A015 full-scope review, with no
source statement repair or contributor change. The new construction does
not use that obstruction as a proof premise, only as the target demanding
a new mechanism. Its direct analytic proof depends on disjoint Fourier
algebra, an explicit sampler and physical pivotal moments. Independent
review of the new bounded interface is pending; finite checks are not
independent-agent acceptance. This narrower interface follows a source
review, not a new broad universal candidate added to the pending queue.

If separately accepted, prior A015 supplied-reference history transport
can project this positive Q through restrictions while retaining its root
bank. That is conditional on its pending independent review, and does not
pay arbitrary changed references. It is not a premise of the new<9I root
bound. Remote adoption/publication and registry changes are not claimed.

## one next mathematical action and independent reviewer

{next_action}
A008 or A007 should independently reconstruct the new code normalization,
activation moment and full-wrapper bound; A014/A086/A094 can test the
physical-overlap replacement. Do not repeat disjoint truth tables once
these pass. A single shared-variable negative control already rules out
blindly extending the product formula.

## actual persistence receipts or precise save blocker

Required four protocol files, code/, out/, frozen spec and two proofs saved
locally; PACKET_DELTA equals PROGRESS with packet_ids=[A015]. Three rolling
files are updated. code/persist.py checks schema fields, source statement
hash, helper hash, exact case counts, sizes and all saved receipt hashes.
out/RECEIPTS.json excludes itself and covers all other stage files and
rolling files. No save blocker. Supervisor-owned copying, mirror verification
and downstream adoption remain unverified; no git/mail/brain writes.
Checklist T-20261023-356 closure was attempted after artifact verification,
but exited1 with shared checklist lock held too long. Its workflow status
remains unverified; no lock was removed and no other agent was interrupted.
Brain self-care is degraded/unverified: owner-model97.5h, state-of-mind82.1h
and dream32.8h stale; personal-context freshness is affected, not a premise
of the mathematics.

**Universal bridge:** C020 whole-set witness cost now has an explicit paid
shared-dictionary repair on the actual family defeating ALL fixed polarity
queue mixtures: complete nonempty<8I and full<9I, including unequal block
parameters and arbitrary stated mixed widths. C024 transfer is available
only conditionally from the earlier supplied-reference proof. The remaining
universal step is a full joint dictionary/activation-moment payment under
physical overlap, with repeated sector tags charged to one account. NEXT
targets that exact missing compression feature rather than another isolated
known-class entropy bound or the now-refuted original two-queue mechanism.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
stamp=datetime.now(timezone.utc).isoformat()
(A/'STATUS.md').write_text('STATE: A015 stage9 saved: A008 fixed-polarity mixture obstruction independently HOLDS; new once-paid whole-set dictionary has nonempty<8I/full<9I on actual mixed-width family;105187 exact checks incl pilot; new proof pending review; FEI OPEN.\nNEXT: Independently review joint dictionary interface, then pay whole-set activation/tag cost under PHYSICAL OVERLAP from one influence account; fixed original two-polarity queues are refuted, repeated-sector closure unproved.\n',encoding='utf-8')
for name,entry in [('WORKLOG.md',f'{stamp} | {R.name}: Consumed A008 new fixed-mixture obstruction; independent full-scope HOLDS without repair. Changed mechanism to a normalized joint dictionary sampled once, proved exact sector CE identity and complete<8I nonempty/<9I full payment on actual family with unequal w and arbitrary mixed-width patterns.105187 exact assertions incl overlapping pilot, full17.136s. No universal overlap claim; NEXT exact joint activation/tag payment under physical overlap.\n'),('LEARNED.md',f'''## {stamp} — {R.name}

- A008 fixed-polarity-mixture obstruction@1 independently HOLDS: arbitrary positive feasible weights/orders cannot avoid cost/I>w/2592 on its actual Boolean family, despite H/I<8. Universal one-root existence does not pay repeated child names.
- On DISJOINT indicators U,V, uniform three-sector Q gives EXACT C_Q=Var(F)log3+b C_g+a C_h and I(F)=b I(g)+a I(h). This is a paid ONE-LEVEL interface, not unlimited-composition closure. Shared OR2 gives actual influence1 vs invalid predicted3/2.
- For r=2^w,w>=4 disjoint OR clauses with widths w or w+1, rho=1/(2r) nonempty-conditioned clause mask plus uniform nonempty subsets defines a fixed normalized reference. Its full local nonempty cost<=11I/2: base length<=1, active length<=9d/4, actual active-width moment<=2I. Reference parameters precede the target.
- Two independent such dictionaries, even with different w, give complete nonempty cost<=[11/2+log3]I<8I; actual full empty/nonempty wrapper yields<[13/2+log3]I<9I since I>1. New sampler replaces original queue; no free erasure, reference conversion or FEI borrowing occurs.
- Under physical overlap the product-moment proof breaks; no universal whole-set dictionary payment exists here. Repeated sector costs still require a single influence surplus account. Prior supplied-reference transport can be applied only conditionally on its independent review, without renewing the root budget.
''')]:
    p=A/name; old=p.read_text(encoding='utf-8')
    if R.name not in old:p.write_text(old+'\n'+entry,encoding='utf-8')
proto=read(P/'EXECUTION_PROTOCOL.json')['required_per_run']
assert set(progress)=={f.split(' (')[0] for f in proto['progress_fields']}
for c in [imported,claim]:assert set(c)==set(proto['claim_fields'])
assert read(R/'PROGRESS.json')==read(R/'PACKET_DELTA.json')
for field in proto['report_fields']:assert '## '+field in report
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
paths=sorted(p for p in R.rglob('*') if p.is_file() and p.name!='RECEIPTS.json')+[A/n for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]
receipts=[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in paths]
assert all(x['bytes']<20_000_000 for x in receipts)
dump(R/'out/RECEIPTS.json',receipts)
assert all(sha(Path(x['path']))==x['sha256'] for x in read(R/'out/RECEIPTS.json'))
print(json.dumps({'status':'SAVED_VERIFIED','receipts':len(receipts),'assertions_including_pilot':105187,'new_statement_hash':claim['statement_sha256']}))
