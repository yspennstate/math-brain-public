import json,hashlib,datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parent.parent
BASE=AGENT.parent.parent
RUN=ROOT.name
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
proof=ROOT/'DERIVATION.md'
validation=json.loads((ROOT/'out'/'validation.json').read_text())
pilot=json.loads((ROOT/'out'/'pilot_validation.json').read_text())
assert validation['status']=='PASS' and validation['total_cases']==8598
assert pilot['total_cases']==142 and pilot['runtime_seconds']<60
sources=[
 Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'),
 BASE/'BOARD.md',BASE/'claude'/'B16'/'STREAM_NOTES.md',
 BASE/'agents'/'A002'/'runs'/'20261013T220534Z-account05-A002-hardness-preserving-transformations'/'REPORT.md',
 BASE/'agents'/'A034'/'runs'/'20261011T223816Z-account05-A034-phase-energy-transfer'/'CONDITIONAL_PHASE_THEOREM.tex',
 AGENT/'runs'/'20261012T044009Z-account05-A079-correlated-auxiliaries'/'DERIVATION.md',
 AGENT/'runs'/'20261012T044009Z-account05-A079-correlated-auxiliaries'/'REVIEW_A034.md',
 BASE/'agents'/'A032'/'LEARNED.md',BASE/'agents'/'A032'/'STATUS.md',BASE/'agents'/'A034'/'STATUS.md'
]
manifest=[{'path':str(p),'sha256':sha(p)} for p in sources]
save(ROOT/'out'/'SOURCE_MANIFEST.json',manifest)
save(ROOT/'out'/'FAILED_PILOTS.json',[
 {'helper':'v2 uncached','result':'Stopped by 60-second runtime guard during exhaustive n=3; no inequality failure; no successful full-domain receipt.'},
 {'helper':'v2 certificate-cache optimization, same domain','result':'Stopped by 60-second runtime guard during exhaustive n=3; no inequality failure. Superseded by explicitly frozen v3 pilot/full schedule.'}
])
statement='For every n>=0 and every two quadratic Boolean phases g0,g1 on the same uniform physical n-bit cube, G(z,y)=g_z(y) has selector entropy decrement L=H(G)-(H(g0)+H(g1))/2 <= (12-(9/2)log2(3))*Inf_z(G), and H(G) <= (16/3-(3/2)log2(3))*I(G). Both constants are attained by g0=1 and g1=(-1)^(y0*y1). The admitted distinct-label quadratic affine-row function f(x,z,y)=(-1)^(xz+zy0y1) restricts at x=0 to this witness, so arbitrary label collision does not preserve a conditional constant of two. For X=z,Y=(y0,y1), the witness retains H(S_Y|S_X)=2-(3/8)log2(3) and I_Y=1/2.'
claim={
 'claim_id':'A079-SHARP-QUADRATIC-TWO-PHASE-COLLISION','version':1,
 'exact_statement':statement,
 'hypotheses':['Normalized Walsh transform; entropy in bits; influence is physical squared Fourier mean degree','Two actual quadratic sign phases on the same full uniform data cube','One independent uniform physical selector bit','No assertion for unequal affine supports or repeated collision closure'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A079'],
 'proof_source':{'path':str(proof),'sha256':sha(proof)},'proof_dependencies':[],
 'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':['Unqualified extension of A034 conditional constant two through an X restriction merging two quadratic labels'],
 'first_unproved_line':None,'next_consumers':['A034','A080','A088','A092','B16','B20']}
save(ROOT/'CLAIMS.json',[claim])
next_action='Handle a collision of two quadratic affine-cell rows with unequal cell supports or weights: retain conditional spectral entropy and charge the physical separator plus terminal energy. Obtain exact endpoint certificates before claiming recursive closure.'
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':RUN,'stream':'B16','packet_id':'A079','gap_id':'G-PHASE-COND','attempt_id':'A079-phase-3',
 'method':'Change from flat bent transport to nonflat quadratic two-phase collision; affine Fourier support overlap and polar-rank case proof with physical core energy; exact integer Walsh and rational log verification.',
 'mathematical_delta':{'local_constant':'12-(9/2)log2(3), sharp','whole_constant':'16/3-(3/2)log2(3), sharp','conditional_auxiliary_entropy':'Retained exactly; physical-selector witness H(S_Y|S_X)=2-(3/8)log2(3).','boundary':'Two same-full-cube quadratic phases; unequal supports and repeated collisions remain open.','external_review_consumed':'A002 stage3 independently accepts A079-CORRELATED-BENT-HARDNESS-TRANSPORT@1; no self-review or claim of universal resolution.'},
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'RESTRICTED_TARGET_AUTHOR_PROVED_PENDING_REVIEW; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A034-QUADRATIC-AFFINE-ROW-CONDITIONAL','version':1,'use':'Admission/scope comparison only; not a dependency of the new inequality.'},{'claim_id':'A079-CORRELATED-BENT-HARDNESS-TRANSPORT','version':1,'use':'Prior mechanism and A002 independent review receipt; not a dependency of the new inequality.'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'status':claim['status']}],
 'source_artifacts':manifest,'next_consumers':claim['next_consumers'],'next_action':next_action,
 'stagnant_substantive_attempts':0,'blockers':['Independent review pending','Unequal-support and repeated-collision universal payment unproved; full FEI open'],
 'packet_ids':['A079']}
save(ROOT/'PROGRESS.json',progress);save(ROOT/'PACKET_DELTA.json',progress)
report=f'''# A079 correlated auxiliaries: one sharp nonflat collision

## exact target, quantifiers, hypotheses and units

For every n and every pair of quadratic sign phases on the same uniform physical
data cube, settle the selector entropy decrement and the whole-function H/I
bound for G(z,y)=g_z(y). Entropy is in bits. The sharp constants are
kappa=12-(9/2)log2(3) and Cstar=16/3-(3/2)log2(3), respectively.
This is a first label collision, with terminal phase entropy and physical data
influence retained. Full FEI remains open.

## sources actually read, revisions and theorem locators

Read BOARD.md at stage start (2026-10-13 23:59 UTC snapshot), B16 STREAM_NOTES.md
(v2; still directs the flat bent family), own STATUS and prior run derivations.
Read the complete execution protocol revision 2026-10-11-execution-v2.
Read A002 stage3 REPORT: its independent review accepts our prior correlated
bent transport claim, and its erasure-deficit analysis confirms this direction
does not remove seed hardness. Read A034 status and its source-complete v1
CONDITIONAL_PHASE_THEOREM.tex (quadratic affine rows, injective-label restriction
clause); newer run folders contained no new source-complete theorem at inspection.
Read A032 current learned/status: weighted nonfair rows remain unproved, so do
not use their floating-point bound as a premise. Source paths and SHA256s are in
out/SOURCE_MANIFEST.json. Earlier paper/plan reads are inherited context, not
newly claimed reads in this stage.

The lead's unchanged flat-bent target has already been resolved as FEI-hard in
our previous stage and reviewed by A002. Moving to the first nonflat collision
follows that result; no disagreement with a mathematical lead claim is needed.

## complete derivation or exact first unsupported line

DERIVATION.md supplies a dimension-independent proof. Quadratic squared spectra
are uniform affine laws of even polar rank. Their dyadic ranks and exact overlap
give the full selector entropy increment; the correlation takes values zero or
signed powers of one half. Enumerating those correlation/rank regimes proves
the sharp decrement. Keeping the physical influence of terminal phases sharpens
the full-function constant to Cstar.

The actual equality case G=(-1)^(zy0y1) has H=4-(9/8)log2(3), I_z=1/4,
I_y=1/2. For the physical split X=z,Y=y, its conditional auxiliary entropy is
2-(3/8)log2(3), so its conditional ratio exceeds two. The admitted distinct-label
f(x,z,y)=(-1)^(xz+zy0y1) restricts at x=0 to G. Thus unrestricted collision closure
with constant two fails; A034 v1 itself remains valid at its stated scope.

First unsupported universal line: unequal affine-cell supports, or repeated
collisions whose phases cease to be quadratic, admit a uniform physical
separator payment after retaining terminal costs. No such bridge is proved here.

## executed validation with domain, arithmetic, commands and outputs

The two initial full-domain pilots stopped at their 60-second runtime guards;
neither yielded a successful full-domain receipt or an inequality failure.
They are recorded in out/FAILED_PILOTS.json. With cached certificate expressions
and explicitly frozen pilot/full specs, the bounded pilot passed {pilot['total_cases']}
cases and {pilot['assertions']} assertions in {pilot['runtime_seconds']:.3f}s.
Command: `python -X utf8 code\\run_frozen.py --pilot`.

Full command: `python -X utf8 code\\run_frozen.py`.
It passed {validation['total_cases']} cases and {validation['assertions']} assertions in
{validation['runtime_seconds']:.3f}s (600-second cap). Every quadratic pair on n=0,1,2,3
was checked modulo simultaneous global sign: 2,8,128,8192 cases. The remaining
268 cases were frozen n=4 mask pairs/rank endpoints and n=6 mask pairs.
Arithmetic: integer Walsh, Fraction, GF(2) rank, exact prime-log identities,
and rational atanh enclosures with proved tails. The analytic proof uses integer
comparisons 3^5<2^8, 3^12>2^19, 5^10>2^23 and rational comparisons. Floating
approximations are not certificates. Validation includes physical influence,
overlap formulas, correlation/rank constraints, both claimed inequalities,
and the conditional entropy chain identity. This is an author implementation,
not independent review or a Lean proof.

The frozen estimate is below 80MB, with largest truth table 128 signs; the
300MB memok gate was not triggered. No dimensions were raised automatically.
out/validation.json, pilot_validation.json, sharp_witness.json,
rank_overlap_histogram.json and frozen specs contain receipts.

## proof dependencies and changed downstream conclusions

The new inequality is proved self-contained, without using an unreviewed claim.
A034 v1 is used only to identify an actual admissible pre-collision example.
A002's review is consumed as evidence for the prior mechanism; its new deficit
theorem is not silently accepted as a premise. No old claim is superseded.
The two-phase constant-two extension is refuted by an actual Boolean restriction;
the sharp local cost and physical terminal slack repair this one collision.
Do not sum the sharp whole-function bound through a tree without proving a new
payment invariant.

## one next mathematical action and independent reviewer

{next_action}
Independent reviewer requested through this artifact: A092 or A088, using a
separate affine-support calculation and reconstruction of the rank-zero/mu-zero
physical-energy endpoint. A034 and A080 are next mathematical consumers.

## actual persistence receipts or precise save blocker

The four protocol files, DERIVATION.md, code and out receipts are saved locally
inside the assigned run. STATUS.md, WORKLOG.md and LEARNED.md are updated.
out/PERSISTENCE_RECEIPT.json records SHA256s and successful schema/readback checks.
No remote copy, independent acceptance, downstream use or publication is claimed.
The supervisor owns subsequent copies; there is no local save blocker.

**Universal bridge:** This stage moves C019 stopping-tree payment by proving the
sharp one-node quadratic collision decrement kappa, retaining terminal entropy
and influence, and sharpens the complete one-collision H/I constant to Cstar.
The noninjective restriction boundary is now a checked Boolean witness rather
than an admission guess. The remaining bridge is unequal-support or repeated
collision payment. That is the shortest next route to a universal argument:
flat correlated bent padding has already been shown to transport arbitrary seed
hardness, while a separator payment could handle the first genuinely new
operation needed by restriction closure. Full FEI remains open.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: Stage3 complete: sharp quadratic pair collision L<=kappa Inf_z, H<=Cstar I; exact 8598 cases PASS; author proof pending review; full FEI OPEN.\nNEXT: Unequal affine-support two-row collision payment with terminal physical energy; A092/A088 review DERIVATION.md.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n{now} Stage3 {RUN}: read board/lead/status and consumed A002 independent bent-transport review. Changed mechanism to nonflat two quadratic phases. Proved sharp kappa and Cstar in all dimensions; real Boolean collision defeats constant-two extension. Two pilots capped at60s; revised pilot142 cases passed, full8598 cases passed with {validation["assertions"]} assertions. Unequal supports/repeated collisions still unsupported; next two-affine-cell payment. Local receipts saved; no remote write.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nStage3 durable facts (author proof pending independent review): for G(z,y)=g_z(y) with two quadratic phases on the same full cube, L<=kappa Inf_z, kappa=12-(9/2)log2(3), and H<=Cstar I, Cstar=16/3-(3/2)log2(3); both sharp at (-1)^(zy0y1). Quadratic polar rank gives uniform affine Fourier supports, physical I>=rank/2 and mu=0 or signed half powers. Include terminal core influence to improve the whole bound. The mu=0 rank-sum2 case needs affine-plane exclusion of the origin: physical mean degree >=3/2. Conditional auxiliary entropy of the witness is 2-(3/8)log2(3), I_y=1/2. A034 admitted (-1)^(xz+zy0y1) restricts at x=0 to that witness; injectivity is essential for constant-two closure. Unequal-support cells and repeated collisions are not covered. Exact certified 8598 cases; cached rational sign certificates avoid repeated large Fraction computations. Do not conflate whole-node bound with a reusable recursive charge. A002 independently accepted our prior correlated bent transport v1.\n')
protocol=json.loads(sources[0].read_text(encoding='utf-8-sig'))['required_per_run']
assert set(claim)==set(protocol['claim_fields'])
expected={x if not x.startswith('packet_ids ') else 'packet_ids' for x in protocol['progress_fields']}
assert set(progress)==expected
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
for title in protocol['report_fields']:assert '## '+title in report
assert report.rstrip().split('\n\n')[-1].startswith('**Universal bridge:**')
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
files=[p for p in ROOT.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json']
assert all(p.stat().st_size<20_000_000 for p in files)
receipts={'schema_check':'PASS','packet_delta_identical':True,'report_fields':'PASS','rolling_status_two_lines':True,'local_only':True,'independent_review':'PENDING','files':[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]}
save(ROOT/'out'/'PERSISTENCE_RECEIPT.json',receipts)
print(json.dumps({'status':'SAVED_AND_READBACK_CHECKED','cases':validation['total_cases'],'assertions':validation['assertions'],'run':str(ROOT)},indent=2))
