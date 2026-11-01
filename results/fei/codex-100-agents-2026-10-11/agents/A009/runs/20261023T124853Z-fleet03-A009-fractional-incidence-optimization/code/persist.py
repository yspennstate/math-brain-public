from pathlib import Path
import json, hashlib
from datetime import datetime, timezone

R=Path(__file__).resolve().parents[1]
AG=R.parents[1]
BASE=AG.parent
SOURCE=BASE/'A006'/'runs'/'20261023T112840Z-fleet03-A006-posterior-forest-optimization'
PROTO=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def rd(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def wr(p,x):p.write_bytes((json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode('utf-8'))
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
pilot=rd(R/'out/PILOT.json'); main=rd(R/'out/CHECK.json')
assert pilot['status']==main['status']=='PASS'
assert len(main['fixtures'])==4 and sum(x['truth_inputs'] for x in main['fixtures'])==184
assert sum(x['allocation_tuples'] for x in main['fixtures'])==656
assert len(main['source_review'])==5 and sum(x['truth_inputs'] for x in main['source_review'])==404
proto=rd(PROTO)
src=rd(SOURCE/'CLAIMS.json')[0]
assert src['statement_sha256']=='1895831db59ae421ddc431d33d703060798097b6193a4f1591d004e8f283cf08'
src['review_records'].append(dict(reviewer='A009',kind='INDEPENDENT_FULL_VERSION_RECONSTRUCTION',acceptance='HOLDS_UNCHANGED_SCOPE',evidence=['REVIEW_A006.md','out/CHECK.json'],formal_status='NOT_FORMALLY_CHECKED'))
src['status']='INDEPENDENT_A009_REVIEW_HOLDS_LOCAL; SHARED_ADOPTION_UNVERIFIED'
def claim(cid,statement,hyp,proof):
    d=dict(claim_id=cid,version=1,exact_statement=statement,hypotheses=hyp,
           statement_sha256=hashlib.sha256(json.dumps(dict(exact_statement=statement,hypotheses=hyp),sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')).hexdigest(),
           contributors=['A009'],proof_source=[proof,'code/check.py','out/CHECK.json'],proof_dependencies=[],
           review_records=[dict(reviewer='A009',kind='AUTHOR_ANALYTIC_PROOF_AND_EXACT_CERTIFICATES',acceptance='INDEPENDENT_AGENT_REVIEW_PENDING',formal_status='NOT_FORMALLY_CHECKED')],
           status='AUTHOR_PROOF_EXACT_CERTIFICATES; INDEPENDENT_AGENT_REVIEW_PENDING',supersedes=[],refutes=[],first_unproved_line=None,next_consumers=['A006','A008','A010','A015','Claude/B02','B20'])
    return d
c1=claim('A009-GLOBAL-INCIDENCE-ALLOCATION-DUAL',
 'For any finite relevant-coordinate support cover and any nonconstant Boolean function, fixed rational allocation witnesses give the complete nonempty uniform-mask pushforward cost upper bound C_e(Q_alpha)<=B(alpha)+v ln Z<=B(alpha) in DUAL.md. Minimizing B over all physical-coordinate incidence constraints is convex. The coordinate-price dual in equation (2) is valid, and rational feasible activations and nonnegative prices satisfying equation (3) certify a global optimum of this fixed-witness bound by exact arithmetic. This does not assert convexity or global optimality of the true pushforward cost, nor universal influence payment.',
 ['Activation probabilities lie strictly between zero and one; all sums of incident activation probabilities are at most one.', 'Witnesses are fixed distributions on actual mask tuples with physical union equal to each nonempty spectral output; all local subset draws and the global nonempty normalization are paid.', 'Natural logarithms in the optimization; divide by ln 2 for bits.'], 'DUAL.md')
c2=claim('A009-ALL-ACTIVATION-UNIFORM-MASK-CORE-OBSTRUCTION',
 'For every integer w>=8, set r=w*2^w and f=2[z OR product_(j=1)^r OR_w(X_j)]-1 on one common physical bit and disjoint private blocks. Every whole-set reference that chooses any nonempty active-support set among E_j={z} union X_j and then independently samples uniform nonempty local subsets, and every mixture of such references, has C_Q(f)/I(f)>w/4, while H(f)/I(f)<35/8. This includes every globally incidence-feasible independent activation vector and every retuning or mixture of forced-anchor activation samplers on these same uniform dictionaries.',
 ['Uniform physical cube; entropy and complete nonempty code cost in bits; physical flip influence.', 'Active supports are chosen before their independent uniform nonempty subset draws; dictionaries remain the specified supports. Adding a core atom or changing local subset laws is outside the refuted class.', 'Zero reference probability at a positive spectral atom is interpreted as infinite cost.'], 'RETUNING_OBSTRUCTION.md')
claims=[src,c1,c2]; wr(R/'CLAIMS.json',claims)
progress=dict(protocol_revision=proto['revision'],run_id=R.name,stream='B02',packet_id='A009',gap_id='C020-PHYSICAL-OVERLAP-DICTIONARY-PAYMENT',attempt_id='A009-stage10-incidence-dual-uniform-mask-barrier',
 method='Consume and independently review A006; change from original prime weights to a convex complete-allocation certificate; prove all-retuning dictionary obstruction.',
 mathematical_delta='Exact global incidence KKT dual/certificate; uniform-mask core obstruction survives arbitrary activation laws and mixtures, C/I>w/4 on actual bounded-FEI family; A006 whole-version review HOLDS.',
 deliverable_status='COMPLETE_LOCAL_ARTIFACTS',mathematical_status='SCOPED_AUTHOR_PROOFS_AND_EXACT_CERTIFICATES; FULL_FEI_OPEN',
 claim_versions_used=[dict(claim_id=src['claim_id'],version=src['version'],statement_sha256=src['statement_sha256'],acceptance='INDEPENDENT_A009_HOLDS_UNCHANGED')],
 claims_created_or_changed=[dict(claim_id=c['claim_id'],version=c['version'],status=c['status']) for c in claims],
 source_artifacts=['DUAL.md','RETUNING_OBSTRUCTION.md','REVIEW_A006.md','FROZEN_SPEC.json','code/check.py','out/PILOT.json','out/CHECK.json'],
 next_consumers=['A006','A008','A010','A015','Claude/B02','B20'],
 next_action='A008/A010 independently review the dual and all-activation obstruction; supply core/intersection dictionaries with nonuniform local subset laws before optimizing globally. Retain all allocation witnesses and the once-paid selector.',
 stagnant_substantive_attempts=0,blockers=['Universal influence-paid dictionary representation remains unproved.','Independent review of new A009 claims and supervisor mirror/adoption remain unverified.'],packet_ids=['A009'])
wr(R/'PROGRESS.json',progress); (R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
text=f'''# A009 stage10: global fractional incidence dual and a dictionary barrier

## exact target, quantifiers, hypotheses and units

For every finite support cover, derive an optimization certificate for the complete physical-union mask reference with ALL coordinate incidence constraints. DUAL.md proves a fixed-witness convex upper bound and exact rational KKT certificate. RETUNING_OBSTRUCTION.md proves that on the actual unbounded-read common-anchor family, every activation retuning and every mixture keeping uniform local subset dictionaries has C/I>w/4, although H/I<35/8. Costs are bits except the explicitly natural-log optimization. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Fresh BOARD (2026-10-23 12:47UTC), B02 STREAM_NOTES v2 and own STATUS; protocol 2026-10-11-execution-v2 and machine AGENTS. Read A006 stage10 REPORT, complete SHARED_TAG sections1--5 and CLAIMS; A015 stage9 REPORT and complete JOINT_DICTIONARY_CODE; A008 current COMMON_ANCHOR in full. Legacy campaign/paper intake is inherited from earlier stages, not newly reread in full. Source pins in out/SOURCE_PINS.json identify bytes actually consumed at finalization, not historical or remote receipts. User's deadline supersedes legacy protocol dates.

## complete derivation or exact first unsupported line

DUAL.md derives the physical-allocation log-sum certificate with every local activation, subset label, allocation posterior and negative nonempty normalizer retained. Dropping only the negative normalization term gives a convex objective under the global incidence constraints; its coordinate-price dual and rational KKT conditions certify a GLOBAL optimum of that bound. A dual lower bound alone is never mistaken for a code upper bound. The finite common-anchor fixtures provide feasible primal upper bounds <32I, not an all-parameter cost theorem.

The stronger obstruction conditions on the ENTIRE active-support set. To output only the common coordinate, each independent uniform local subset must equal that singleton, so its conditional probability is N^(-K)<=1/N. This survives arbitrary activation dependence, incidence-feasible weights, forced anchors and convex mixtures. At r=w*2^w the actual Boolean core atom exceeds1/2, I<2, and log N>w; hence complete cost/I>w/4. A direct exact entropy identity bounds actual H/I by35/8. A008's separate core-atom augmentation is outside this class and remains a viable repair. The candidate disjoint21/4 constant was not pursued as another isolated class bound.

The first unsupported universal line is finding and paying a core/intersection dictionary and its allocation witnesses with B<=K I. Optimizing the old uniform dictionaries cannot prove it. Neither this obstruction nor the dual solves FEI.

## executed validation with domain, arithmetic, commands and outputs

Frozen FROZEN_SPEC precedes searches. Commands: python -X utf8 code/check.py --pilot, then python -X utf8 code/check.py. Pilot PASS {pilot['assertions']} assertions in {pilot['elapsed_seconds']:.6f}s; main PASS {main['assertions']} assertions in {main['elapsed_seconds']:.6f}s. Main has4 physical common-anchor functions,184 truth inputs and656 allocation tuples; all actual physical subsets and coordinate constraints are retained. Five disjoint paired source profiles add404 truth inputs. Scalar bounds for121 parameters w8..128 are exact checks of the analytic proof, not giant truth-table claims. Pilot overlaps main and is not added to its count.

Integer Walsh spectra versus direct physical flips; rational witnesses, incidence feasibility, stationarity and complementary slackness; complete pushforward normalization; rational log-sum and cost intervals; independent actual-anchor enumeration versus union/occupation DP; separate source clause moments and <155I/24 cost checks all PASS. Log intervals use40-term rational atanh series with proved geometric tail. Floats appear only in runtime telemetry. No helper from a source agent is imported. Each job has55s frozen cap and40MB estimated memory; no >300MB job, GPU, remote compute, detached job or dimension escalation. Existing work was not interrupted.

## proof dependencies and changed downstream conclusions

REVIEW_A006 independently reconstructs the entire unchanged source claim@1, including arbitrary-overlap normalization/DP/full support and all-width disjoint payment: HOLDS without repair. Its copied source statement hash is preserved. New proofs are self-contained; A008/A015 determine scope and dispatch rather than being assumed entropy bounds. The new barrier strengthens failure of one fixed width-dependent activation law to ALL activation retunings and mixtures with the same uniform subset dictionaries. New A009 claims await independent-agent review; finite checking is not independent review or formal-kernel verification. No shared registry is edited.

## one next mathematical action and independent reviewer

A008/A010 should reconstruct the exact dual/KKT and core-atom barrier. Then augment supplied supports with genuinely changed core/intersection dictionaries or local subset laws, and run the incidence optimization on a complete allocation certificate with a once-paid selector. The shortest next universal step is proving an influence-paid representation theorem for those dictionaries; retuning uniform clause activations alone is now ruled out.

## actual persistence receipts or precise save blocker

All four exact-field protocol files, proofs, frozen specification, code and outputs saved locally; PACKET_DELTA is byte-identical to PROGRESS. Rolling STATUS, WORKLOG and LEARNED updated. out/PERSISTENCE.json records every other stage file hash/size and schema/readback checks, plus rolling-file pins. No git, brain write, remote mirror or supervisor adoption is claimed. Brain self-care is degraded/unverified: owner-model99.3h, state-of-mind83.9h and dream34.6h were stale at wake; personal-context freshness and consolidation remain affected and were not proof evidence. No stage research job remains running after completion.

## Universal bridge

C020 whole-set witness cost advances by an exact global incidence dual and rational optimum certificate for complete allocation bounds, plus an all-retuning obstruction locating the missing dictionary change on a meaningful unbounded-read actual Boolean family. A006's normalized pushforward/disjoint payment receives independent full-version acceptance. The universal representation and influence price remain open: adding core/intersection dictionaries and paying their selector and allocation cost is necessary. NEXT targets that exact missing mechanism and excludes an entire unsuccessful optimization family, rather than repeating a known FEI class or asserting a universal bound from finite cases.
'''
(R/'REPORT.md').write_bytes(text.encode('utf-8'))
now=datetime.now(timezone.utc).isoformat()
status='STATE: Stage10 saved: global incidence allocation dual/KKT; all activation retunings and mixtures of uniform masks have C/I>w/4 on bounded-FEI common-anchor family; A006 whole-version HOLDS; FEI OPEN.\nNEXT: A008/A010 review new dual and barrier; add core/intersection dictionaries or nonuniform subset laws, then pay full allocation/selector cost from influence.\n'
(AG/'STATUS.md').write_bytes(status.encode('utf-8'))
for name,entry in [('WORKLOG.md',f'\n{now} Stage10: consumed new A006/A015/A008 dictionaries; independent A006 full-version HOLDS. Derived global incidence convex witness bound and rational coordinate-price KKT certificate. Proved arbitrary activation/mixture uniform-mask core obstruction C/I>w/4 with H/I<35/8. Main {main["assertions"]} exact assertions PASS; new claims await review; full FEI OPEN. No jobs left running.\n'),('LEARNED.md','\nStage10 durable: for a union reference with uniform nonempty support masks, fixed allocation witnesses give convex Bernoulli cross-entropy B(alpha) minus witness entropy, under every coordinate incidence cap. Rational KKT prices certify its global optimum; B is a code upper bound, its dual alone is not. On common-anchor width-w supports, ANY activation law or mixture has Q({z})<=1/(2^(w+1)-1). At r=w*2^w,w>=8, actual C/I>w/4 but H/I<35/8. Retuning weights cannot replace a core dictionary. A006 normalized shared-tag claim@1 independently HOLDS including its scoped disjoint payment.\n')]:
    with (AG/name).open('ab') as f:f.write(entry.encode('utf-8'))
pins=[]
for p in [SOURCE/'REPORT.md',SOURCE/'SHARED_TAG.md',SOURCE/'CLAIMS.json',PROTO,
 BASE/'A015/runs/20261023T110145Z-fleet03-A015-minterm-barrier-analysis/JOINT_DICTIONARY_CODE.md',
 BASE/'A008/runs/20261023T121653Z-fleet03-A008-gate-label-compression/COMMON_ANCHOR.md']:
    pins.append(dict(path=str(p),sha256=digest(p),bytes=p.stat().st_size))
wr(R/'out/SOURCE_PINS.json',pins)
fields=set(proto['required_per_run']['progress_fields']); fields.remove('packet_ids (one primary ID, for compatibility)'); fields.add('packet_ids')
assert set(progress)==fields
for c in claims:assert set(c)==set(proto['required_per_run']['claim_fields'])
for field in proto['required_per_run']['report_fields']:assert '## '+field in text
for c in [c1,c2]:
    h=hashlib.sha256(json.dumps({k:c[k] for k in ('exact_statement','hypotheses')},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')).hexdigest()
    assert h==c['statement_sha256']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
files=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json' and '__pycache__' not in p.parts]
assert all(p.stat().st_size<20_000_000 for p in files)
receipts=[dict(path=str(p.relative_to(R)),sha256=digest(p),bytes=p.stat().st_size) for p in files]
rolling=[dict(path=str(AG/name),sha256=digest(AG/name)) for name in ['STATUS.md','WORKLOG.md','LEARNED.md']]
wr(R/'out/PERSISTENCE.json',dict(status='PASS',files=receipts,rolling=rolling,checks=['exact protocol fields','new claim statement hashes','source version unchanged','JSON readback','progress/delta byte equality','all files under20MB','actual domain counts','local persistence only']))
for p in R.rglob('*.json'):rd(p)
for item in receipts:assert digest(R/item['path'])==item['sha256']
print(json.dumps(dict(status='PERSISTED_VERIFIED',files=len(receipts),main_assertions=main['assertions'],source_review='A006_WHOLE_VERSION_HOLDS',full_fei='OPEN')),flush=True)
