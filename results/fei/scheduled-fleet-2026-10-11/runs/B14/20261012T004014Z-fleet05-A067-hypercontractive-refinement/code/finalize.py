"""Persist the source-bound stage package; no research search is performed here."""
from pathlib import Path
import json, hashlib
from fractions import Fraction
from datetime import datetime, timezone

R = Path(__file__).resolve().parent.parent
A = R.parent.parent
HOME = A.parent.parent
P = Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol = json.loads(P.read_text(encoding='utf-8-sig'))
now = datetime.now(timezone.utc).isoformat()
run_id = R.name
def load(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(name, value):
    (R/name).write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

results = {n: load(R/'out'/n) for n in ['check_pilot.json','check_full.json','check_bent.json','check_reserve.json','TRIBES_NODE_WITNESS.json']}
for n in ['check_pilot.json','check_full.json','check_bent.json','check_reserve.json']:
    assert results[n]['complete'], n
tribes_rows = [x for x in results['check_full.json']['rows'] if x['family']=='edited_tribes']
assert len(tribes_rows)==8
for x in tribes_rows:
    assert Fraction(x['tree']['max_ratio'][1])<9
    assert x['tree']['leaf_predicate']

review_sources = [
    A.parent/'A066/runs/20261011T233317Z-fleet05-A066-semigroup-dissipation/CLAIMS.json',
    A.parent/'A070/runs/20261011T230551Z-fleet05-A070-analytic-route-referee/CLAIMS.json',
]
wanted = {
    'A066-POSITIVE-RESTRICTION-HEAT-LEDGER',
    'A066-MAJORITY-DEFECTED-ADDRESS-HEAT-CALIBRATION',
    'A070-HYBRID-SCOPE-AND-THREE-REFERENCE-NOGO',
}
claims = []
for source in review_sources:
    for c in load(source):
        if c['claim_id'] not in wanted: continue
        c['review_records'].append({
            'reviewer':'fleet05/A067', 'verdict':'ACCEPT_AT_STATED_SCOPE',
            'independent':True, 'substantive_repair':False,
            'proof_source':str(R/'REVIEW_B14_QUEUE.md'),
            'scope':'Independent analytic reconstruction; no central registry adoption asserted.',
        })
        c['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL_RECEIPT'
        claims.append(c)
assert len(claims)==3

old_path=A/'runs/20261011T220539Z-fleet05-A067-hypercontractive-refinement/CLAIMS.json'
old=load(old_path)
granularity=next(c for c in old if 'granularity' in (c['claim_id']+' '+c['exact_statement']).lower() and 'H' in c['exact_statement'])
new_id='A067-PADDING-STRIP-RESERVE-AND-LEAF-ACCESS'
statement=(
    'For every Boolean seed g on m>=1 uniform core coordinates, every physical vertex x0, and r>=1 dummy padding coordinates, '
    'let F_r differ from g only at (x0,all +), let d=2^(1-m-r), and let I_core=sum of the core-coordinate influences of F_r. '
    'For every physical tree that queries only padding coordinates along the unique edited branch and stops every clean branch, '
    'the total expected entropy drop Q_pad satisfies Q_pad<=4 I_queried+(1+6/ln(2)) I_core. '
    'The core reserve is allocated once across the whole tree. If every leaf satisfies U<=b I, b>=0, where '
    'U=sum_nonempty hat f(S)^2(max{|T|:hat f(T)!=0,T contains S}-|S|), then '
    'H(F_r)<=(3+2b+6/ln(2)) I(F_r); a sufficient admission is U(g)<=b I(g) and U(F_0)<=b I(F_0). '
    'For fixed finite g and r>=2, with L the number of its nonzero Fourier coefficients and p=2^(-m-r), '
    'the padding-node drop Delta_r obeys |Delta_r/(2p)-4|<=4 L p (|m+r-3|+m+3/(2ln(2))), hence the ratio tends to 4. '
    'The point-defect padding nodes satisfy 0<=Delta<=5 Inf at every dimension. Consequently dictator one-point surgery '
    'and Maj3 tensor point defects have explicit U<=I stopping trees paid at node rate 5, with full terminal entropy retained. '
    'There is no uniform padding-node rate for arbitrary varying seeds: quadratic bent seeds of even dimension m at fixed r>=2 have '
    'Delta_r/(2p)=4+2^(1-r)(m+2r-6+3/ln(2))+O(2^(-r)*2^(1-m/2-r)). '
    'These are a padding-access theorem and its scope guards, not universal admission of arbitrary Boolean core leaves.'
)
hypotheses=[
    'Finite uniform cubes, Boolean outputs {-1,1}; Fourier entropy in bits and standard total influence.',
    'Physical one-vertex edit of an actual Boolean seed and dummy padding, not a spectral projection.',
    'Trees stop clean branches and query only remaining relevant padding on the edited branch; terminal entropy is retained.',
    'The conditional FEI certificate requires the stated U<=b I condition on every terminal restriction; it is not automatic.',
    'The fixed-seed limit keeps seed dimension and spectrum fixed; the bent guard instead keeps r fixed while m grows.',
]
new={
    'claim_id':new_id,'version':1,'exact_statement':statement,'hypotheses':hypotheses,
    'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
    'contributors':['fleet05/A067'], 'proof_source':str(R/'DERIVATION.md'),
    'proof_dependencies':[
        {'claim_id':granularity['claim_id'],'version':granularity['version'],'proof_source':str(old_path),
         'acceptance_scope':'Stage-1 local granularity certificate independently accepted by A088 and A070; only used for terminal U certificate.'},
        {'claim_id':'C005','version':1,'acceptance_scope':'Physical singleton restriction identity and its channel <=2 Inf/ln2; reconstructed in source campaign.'},
        {'claim_id':'C019','version':1,'acceptance_scope':'Exact finite physical-tree entropy and influence telescopes, not the conjectural universal stopping payment.'},
    ],
    'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
    'supersedes':[],'refutes':[], 'first_unproved_line':None,
    'next_consumers':['A070','A088','A094','A064','A069','B06','B13','B14','B20'],
}
claims.append(new)
fields=set(protocol['required_per_run']['claim_fields'])
for c in claims: assert set(c)==fields, (c['claim_id'],set(c)^fields)
write('CLAIMS.json',claims)

sources=[str(R/n) for n in ['DERIVATION.md','REVIEW_B14_QUEUE.md','FROZEN_SPEC.json','FROZEN_SPEC_BENT.json','FROZEN_SPEC_RESERVE.json']]
sources += [str(R/'out'/n) for n in results]
progress={
    'protocol_revision':protocol['revision'],'run_id':run_id,'stream':'B14','packet_id':'A067',
    'gap_id':'FEI-B14-A067-INITIAL','attempt_id':'A067-STAGE2-PADDING-STRIP-RESERVE',
    'method':'Exact Boolean Fourier restriction formulas, granularity-controlled scalar second differences, one retained-core reserve, rational log intervals, source-bound independent reviews.',
    'mathematical_delta':'C019 padding access paid for every seed by 4 I_queried+(1+6/ln2) I_core. Fixed-seed node ratio tends to 4 with explicit error; point-defect trees have uniform node rate 5. Growing bent seeds disprove uniform node rates. Universal core-leaf admission remains open.',
    'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS; MIRROR_COPY_NOT_PERFORMED_OR_VERIFIED',
    'mathematical_status':'RESTRICTED_BRIDGE_PROVED_PENDING_INDEPENDENT_REVIEW; FULL_FEI_OPEN',
    'claim_versions_used':[{'claim_id':x['claim_id'],'version':x['version']} for x in new['proof_dependencies']],
    'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'change':'new proof candidate' if c['claim_id']==new_id else 'independent acceptance receipt'} for c in claims],
    'source_artifacts':sources,'next_consumers':new['next_consumers'],
    'next_action':'Extend the one-reserve padding ledger to two edits with shared active core, proving reserve ownership under restriction and retaining terminal entropy; reject any payment that merely recharges retained influence at descendants.',
    'stagnant_substantive_attempts':0,
    'blockers':['Universal payment for access inside an arbitrary active Boolean core is not proved.','New candidate awaits independent review.','B14 lead continuity bound has a small-eps finite-domain caveat; new theorem does not use it.'],
    'packet_ids':['A067'],
}
pf={s.split(' (',1)[0] for s in protocol['required_per_run']['progress_fields']}
assert set(progress)==pf
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)

report='''# A067 stage 2: padding access with one retained-core reserve

## exact target, quantifiers, hypotheses and units

Pay access to Boolean leaves with U<=bI in C019, rather than assert hereditary support control. For every Boolean seed g on m>=1 coordinates, add r>=1 dummy coordinates and flip one physical vertex. In bits, every padding-only restriction tree that stops clean branches satisfies

    Q_pad <= 4 I_queried + (1+6/ln2) I_core.

The reserve is used once over the entire padding tree. If all terminal restrictions satisfy U<=bI, the complete ledger gives H<=(3+2b+6/ln2)I; for b=1 the constant is <14. A sufficient admission is the U condition for both the unedited seed g and the fully stripped edited seed F_0. This is a measurable Boolean-specific restriction certificate. It does not admit arbitrary core leaves. Full FEI remains open.

## sources actually read, revisions and theorem locators

Stage-start BOARD.md (00:39 UTC), B14 STREAM_NOTES.md v2 (23:25 UTC), own STATUS.md, LEARNED.md and stage-1 proof/claim package were consumed before continuing. The lead's requested padding-strip limit and U stopping access are the direction followed. EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2 was read in full and reloaded for schema checks. Campaign registries, plan, research-push seeds and the threshold/percolation text contexts read in stage 1 remain inherited background; no paper theorem is newly invoked as an unchecked payment.

New source-bound reads: A066 stage 2 (20261011T233317Z), DERIVATION.md Sections 1-5 and its two claim versions; A070 stage 2 (20261011T230551Z), DERIVATION.md Sections 5-6 and its hybrid claim; A088 (20261011T223053Z) review receipts for the stage-1 A067/A068 certificates; A070 acceptance of A069. The B14 lead's 20261011T224500Z neutralization REPORT.md/CLAIMS.json were also read. Exact source hashes are in out/SOURCE_MANIFEST.json.

The lead's asymptotic neutralization is compatible with this route, but its displayed continuity bound needs a small-eps qualification: n=1,N=2 makes its proposed eps greater than 1, outside h2's domain. That version was not independently accepted or used here. REVIEW_B14_QUEUE.md gives the exact source-bound caveat.

## complete derivation or exact first unsupported line

DERIVATION.md is the complete proof, including units and terminal obligations. Section 1 derives an exact entropy-drop formula from all signed Fourier coefficients. Section 2 uses Boolean coefficient granularity and a scalar second difference to prove the fixed-seed padding-node ratio tends to 4, with explicit bound 4Lp(|m+r-3|+m+3/(2ln2)). Section 3 proves every point-defect node has rate <=5, handling dimensions 1,2,3 exactly. Section 4 constructs U<=I stopping trees for dictator surgery and Maj3 tensor point defects; their complete ledger has rate 5. These known FEI classes are calibration of the access mechanism, not the main advance.

Section 5 proves a scope obstruction: for an even-dimensional quadratic bent seed at fixed padding r, the node rate grows with slope 2^(1-r) in seed dimension. The explicit m=2,r=2 rate already exceeds 5. This is not an unbounded H/I family.

Section 6 sums padding corrections before paying them. Expected queried influence is the same d at each surviving padding depth. The aggregate correction is at most (1+6/ln2)md; cube edge-connectivity and the exact one-vertex pivot change prove md<=I_core, including constant seeds. The terminal certificate and this single reserve combine into one coefficient on expected leaf influence. No reserve is renewed at descendants. Section 7 records finite edited-tribes tests. Their last-padding nodes can exceed rate 5, so even padding strips cannot inherit the point-defect rate for arbitrary seeds.

The first unsupported line for universal FEI is a dimension-independent payment of access inside an arbitrary active core to U-certified leaves, with the entire remaining entropy retained. An unmodified arbitrary seed is a positive-probability clean leaf of the padding tree; treating that leaf as paid would simply assume the missing theorem.

## executed validation with domain, arithmetic, commands and outputs

All computations were frozen before execution. FROZEN_SPEC.json uses helper 1.1 after a documented pilot repair, exact integer Walsh transforms and Fraction influence/U. Entropy uses rational intervals for logarithms via 20 positive atanh-series terms with a proved tail bound; bent checks use 32 terms. Every sign decision uses the rational interval, not the printed decimal. No job exceeded 100 MB estimated memory, so the >300 MB memory gate was not triggered. No dimension escalation, GPU, window or background job was used.

- code/check.py pilot: 9 cases, 196 assertions, 0.029 seconds. The original pilot found an attempted irrelevant-padding query on a clean tribes branch. The helper now queries only relevant coordinates; out/PILOT_REPAIR.md preserves the failure and correction.
- code/check.py full: 45 cases, 1,816 assertions, 0.286 seconds. Domains: dictator surgery n=2..10; Maj3 tensor point defects n=1..8; width-two edited tribes with two or three blocks and r=2..5; fixed dictator/AND2/Maj3/address2 seeds with r=2..6. Actual physical children, U leaves, queried and terminal influence, terminal entropy and telescopes were checked.
- code/check_bent.py: 60 compressed cases, 656 assertions, 0.276 seconds. Even m=2..40, r=2,3,4; direct truth-table reconciliation at m=2,4,6,8,r=2. Exact multiplicities and rational intervals validate the displayed Taylor error and complete padding reserve, without constructing a 2^40 truth table.
- code/check_reserve.py: every one of the 276 Boolean sign seeds on m=1,2,3, each with r=1..4: 1,104 cases, 17,301 assertions, 1.369 seconds. Included six constant seeds and 720 admitted U<=I trees. Core-influence reserve, actual seed/edited leaves and the full padding entropy telescope were independently checked from truth tables.
- code/tribes_witness.py: diagnostic replay of two already frozen width-two tribes cases, 114 assertions, 0.014 seconds. out/TRIBES_NODE_WITNESS.json records actual restricted truth tables, coordinate labels, rational I,U and entropy-drop intervals. The two-block example certifies a last-padding node rate >8; the three-block example exceeds 5. The exact integer inequalities 3^9>2^14 and 3^9*5^25<2^76 certify the dimension-three point-defect rate <5 and bent m=2,r=2 rate >5.

These five jobs performed 20,083 assertions, with overlapping cases counted as executions, not distinct functions. Final packaging verifies the eight finite tribes trees have all node rates <9 and all leaves U<=I; hence their finite complete ledgers give H<=9I. No all-width tribes theorem is claimed. Outputs retain rational endpoints and timings. Regenerate with python -X utf8 followed by the corresponding code path and pilot/full argument. The frozen specs contain exact domains, counts, memory estimates and runtime limits; no search is performed by code/finalize.py.

## proof dependencies and changed downstream conclusions

The padding reserve itself uses the exact singleton physical restriction identity C005 and elementary Boolean cube edge-connectivity, not hypercontractive smoothing. Conditional terminal payment uses the stage-1 A067 local coefficient-granularity theorem, already independently reconstructed by A088 and A070. C019 is used only for its exact physical entropy/influence telescopes. The conjectural universal erasure or stopping payment is not a dependency.

REVIEW_B14_QUEUE.md independently reconstructs A066-POSITIVE-RESTRICTION-HEAT-LEDGER v1, A066-MAJORITY-DEFECTED-ADDRESS-HEAT-CALIBRATION v1, and A070-HYBRID-SCOPE-AND-THREE-REFERENCE-NOGO v1 at their stated scopes, without author repair. CLAIMS.json preserves their statements and adds A067 acceptance receipts. Central adoption is pending. These receipts reduce the local source-bound pending queue to the lead's neutralization candidate; the single coherent new padding-access candidate keeps that queue at two. No second new broad candidate is opened.

Downstream substitution: retain the one core reserve instead of a universal node rate. Fixed-seed padding stripping does converge to rate 4, but varying bent cores refute uniformity. The terminal U certificate is useful once access is separately paid. Consumers must keep that admission condition and must not extrapolate the finite tribes tests to arbitrary widths.

## one next mathematical action and independent reviewer

Extend the single-reserve ledger to two physical edits with shared active core, tracking reserve ownership through actual restrictions and keeping terminal entropy. This tests the first interaction absent from dummy-padding stripping and can address arbitrary core access; another isolated seed calculation cannot. A070 is the requested independent analytic reviewer, with A088/A094 for the exact coefficient and arithmetic reconstruction. Review is requested through artifacts only; no messages were sent.

## actual persistence receipts or precise save blocker

All four protocol files, proof, independent-review note, frozen specs, code and exact outputs are saved in this agent's run directory. out/SAVE_RECEIPT.json records actual sizes and SHA256 hashes, and out/SOURCE_MANIFEST.json binds the read-only inputs. code/finalize.py checks the protocol field sets and the byte-identical progress compatibility copy. The reviewed statements are preserved. Every artifact is below 20 MB. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current. No shared index, other agent folder, brain database or git tree was modified. Supervisor copying, GitHub mirror verification and independent acceptance of the new claim are not claimed.

## Universal bridge

C019 advances by a universal payment for dummy-padding access: Q_pad<=4I_queried+(1+6/ln2)I_core for every Boolean seed, with one retained-core reserve. When actual terminal leaves obey U<=bI this closes the complete ledger at 3+2b+6/ln2; the fixed-seed node limit and rate-five stress trees are supporting certificates. What remains is access inside arbitrary active cores, or shared-core edits, without repeatedly spending retained influence or omitting leaf entropy. The next two-edit ownership calculation is the shortest extension toward that universal obligation because it tests the interaction that padding alone never exposes, rather than adding another already isolated FEI class.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
assert report.rsplit('## ',1)[1].startswith('Universal bridge\n')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()

(A/'STATUS.md').write_text('STATE: Stage 2 complete: universal padding-access reserve proved; new claim awaits independent review; full FEI open.\nNEXT: Pay shared active-core access for two edits with one owned reserve and retained terminal entropy; A070/A088 review.\n',encoding='utf-8')
entry=f'''\n## {now} — {run_id}\nFollowed B14 padding-strip direction. Proved exact node formula, fixed-seed ratio-four limit, all-dimensional rate-five point-defect/stress trees, and universal whole-padding payment 4 I_queried+(1+6/ln2) I_core. Bent seeds show no uniform individual-node rate. Tested 1,104 small-seed padding cases, 60 compressed bent cases and 45 family cases plus pilot/diagnostics, totaling 20,083 executed assertions. Repaired pilot irrelevant-coordinate selection, preserving its failure. Finite edited-tribes last-padding nodes exceed 5 (one exceeds 8); universal core-access payment remains a separate unpaid gap. Independently accepted three A066/A070 claim versions without repair; lead continuity bound finite-eps caveat recorded but unused. Saved protocol package and exact outputs locally; no external mirror claim. Next: shared-core two-edit reserve ownership.\n'''
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f: f.write(entry)
learn=f'''\n## Stage 2 durable facts ({run_id})\nFor any m>=1 Boolean seed with r>=1 dummy pads and one physical vertex flip, total padding-tree entropy drop is at most 4 I_queried+(1+6/ln2) I_core. The proof sums second differences over the edited path before paying a single reserve; cube edge-connectivity ensures md<=I_core. Conditional leaves U<=bI give H<=(3+2b+6/ln2)I, but arbitrary clean core leaves are not certified. For fixed finite seed the padding-node drop/influence tends to 4 with explicit error 4Lp(|m+r-3|+m+3/(2ln2)). Varying quadratic bent seeds at fixed r have node-rate slope 2^(1-r) in seed dimension, so no universal node-only payment exists. Point defects and explicit dictator-surgery/Maj3-tensor U-stopping trees have all-dimensional rate 5. Width-two edited-tribes finite tests expose last-padding node rates >5 and >8; even padding queries cannot inherit a universal point-defect rate. Actual relevance must be tested before querying a nominal padding coordinate on a clean restriction. Lead neutralization continuity bound needs eps<=1 domain qualification at small n,N; its fixed-seed asymptotic is unaffected. Full proofs and rational certificates are in this stage's DERIVATION.md and out/.\n'''
with (A/'LEARNED.md').open('a',encoding='utf-8') as f: f.write(learn)

external=[P, HOME/'BOARD.md', HOME/'claude/B14/STREAM_NOTES.md', old_path,*review_sources,
          A.parent/'A088/runs/20261011T223053Z-fleet05-A088-booleanity-referee/CLAIMS.json',
          HOME/'claude/B14/runs/20261011T224500Z-claude-B14-granularity-neutralization/REPORT.md',
          HOME/'claude/B14/runs/20261011T224500Z-claude-B14-granularity-neutralization/CLAIMS.json']
external += [s.parent/'DERIVATION.md' for s in review_sources]
write('out/SOURCE_MANIFEST.json',{'created_at':now,'sources':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in external]})
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='SAVE_RECEIPT.json']
files += [A/n for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]
assert all(p.stat().st_size<20_000_000 for p in files)
write('out/SAVE_RECEIPT.json',{
    'created_at':now,'schema_checked':True,'claim_count':len(claims),'new_candidate_count':1,
    'progress_copy_byte_identical':True,'all_files_under_20MB':True,
    'mathematical_checks':'20,083 assertions in executed jobs; eight additional finite tribes node-rate and leaf checks during packaging.',
    'external_mirror_verified':False,'new_claim_independently_reviewed':False,
    'files':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(files)],
})
print(json.dumps({'complete':True,'claim_count':len(claims),'new_claim_id':new_id,'receipt_files':len(files),'local_proof_dependency':granularity['claim_id'],'run_id':run_id}))
