from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1];BASE=RUN.parents[1]
RID=RUN.name
OLD=RUN.parent/'20261011T234607Z-account05-A022-one-point-surgery'
old=json.loads((OLD/'CLAIMS.json').read_text(encoding='utf-8'))[0]
full=json.loads((RUN/'out/full_RESULTS.json').read_text())
pilot=json.loads((RUN/'out/pilot_RESULTS.json').read_text())
edge=json.loads((RUN/'out/EDGE_RECONSTRUCTION.json').read_text())
assert full['cases']==9212 and full['leaf_character_cases']==41650
assert all(r['verdict']=='PASS' for r in (full,pilot,edge))
statement=old['exact_statement']+' Extension: For every even k>=2, every r>=0 and every D of at most four vertices, the same activated fair-selector quadratic-bent surgery has an explicit physical stopping tree querying controls, then the first coordinate of each quadratic pair, then the selector, while retaining all partner bits at the leaves. Every access node obeys B<=4d (pair nodes obey B/d<=8-3log2(3)<4; control and selector nodes obey B/d<3 for d>0), so access bad-node odd-face credit is exactly zero. Every retained leaf is a character or a character times a defect on at most four points, and every such leaf on any dimension obeys H<=6I. Hence H(F)<=(4+2/ln2)I_removed+6I_terminal<=(4+2/ln2)I(F), with I_removed+I_terminal=I(F) exactly. The new stopping policy was certified on 9212 labelled roots at k=4,6,8 and r=0,2; all 41650 sparse-defect/character cases on dimensions 0..4 were also certified. No extension to arbitrary cores, overlapping controls or zero-cost constant-leaf completion is asserted.'
hyp=old['hypotheses']+['New all-dimensional result: quadratic paired bent reference, uniform fair selector, fresh point-activation controls, |D|<=4', 'New zero-credit result concerns the stated stopping access tree; complete retained terminal entropy is included']
claim={key:old[key] for key in old}
claim.update(version=2,exact_statement=statement,hypotheses=hyp,
    statement_sha256=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
    proof_source={'run_id':RID,'new_proof':'PROOF.md','inherited_proof':str(OLD/'ODDFACE_GAP.tex'),
        'finite_certificate':'out/full_RESULTS.json','cases':'out/full_CASES.jsonl','independent_implementation':'out/EDGE_RECONSTRUCTION.json'},
    proof_dependencies=[{'claim_id':old['claim_id'],'version':1,'scope':'inherited ledger statements and constant-child bound; partial independent acceptance for constant-child bound only'}],
    review_records=[{'reviewer':'A025','verdict':'HOLDS_FOR_INHERITED_CONSTANT_CHILD_SUBCLAIM_ONLY',
        'reviewed_version':1,'source':'~/brain_workers/FEI100_20261011/agents/A025/runs/20261012T045020Z-account05-A025-rare-event-counterfamily/REVIEW_A022.md',
        'new_version_review':'PENDING; separate edge implementation is author verification, not independent human acceptance'}],
    status='AUTHOR_PROVED_SCOPED_EXTENSION_PENDING_INDEPENDENT_REVIEW',
    supersedes=[{'claim_id':old['claim_id'],'version':1}],refutes=[],first_unproved_line=None,
    next_consumers=['A021','A023','A025','A028','A064','A067','A087','A094','A097','B05'])
(RUN/'CLAIMS.json').write_text(json.dumps([claim],indent=2)+'\n',encoding='utf-8')
next_action='Test whether a three-event overlapping-control policy preserves a fair or sufficiently weighted unedited bent branch, assigning every physical influence once and retaining complete sparse/controller terminal entropy; A087 primary and A094 alternate review.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RID,'stream':'B05','packet_id':'A022',
    'gap_id':'G-R-MISMATCH','attempt_id':'A022-stage3-paired-exposure-terminal-payment',
    'method':'mechanism change: intact quadratic-pair exposure, sparse terminal certificate, exact signed Walsh/prime-log ledger and independent edge representation',
    'mathematical_delta':'Extends prior k=4 zero-credit observation to every even k>=2 and every r>=0 using a different stopping tree; certifies H_terminal<=6I_terminal and H(F)<=(4+2/ln2)I(F) for |D|<=4.',
    'deliverable_status':'COMPLETE_LOCAL_FILES_WRITTEN',
    'mathematical_status':'SCOPED_PACKET_EXTENSION_PROVED; UNIVERSAL_C019_AND_FULL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING',
    'claim_versions_used':[{'claim_id':old['claim_id'],'version':1,'acceptance':'author proved; A025 independently accepts constant-child subclaim only'}],
    'claims_created_or_changed':[{'claim_id':old['claim_id'],'version':2}],
    'source_artifacts':['PROOF.md','out/FROZEN_SPEC.json','out/pilot_RESULTS.json','out/full_RESULTS.json','out/full_CASES.jsonl','out/full_LOG_RECEIPTS.json','out/EDGE_FROZEN_SPEC.json','out/EDGE_RECONSTRUCTION.json'],
    'next_consumers':claim['next_consumers'],'next_action':next_action,
    'stagnant_substantive_attempts':0,'blockers':['No universal arbitrary-core exposure policy; overlapping controls can destroy fair-selector weight. No independent acceptance of new extension yet.'],
    'packet_ids':['A022']}
for name in ('PROGRESS.json','PACKET_DELTA.json'):
    (RUN/name).write_text(json.dumps(progress,indent=2)+'\n',encoding='utf-8')
report=f'''# A022 stage 3: paired exposure and terminal sparse surgery

## exact target, quantifiers, hypotheses and units

Uniform Boolean signs and entropy in bits. For every even k>=2, r>=0,
and D subset of the k-cube with |D|<=4, use paired quadratic bent b,
its edited branch b(1-2 1_D), one fair selector and r fresh point-activation
controls. Prove a stopping payment with each influence used once, including
the complete entropy of all unqueried partner bits. Scoped target achieved;
full FEI and the universal B05 localized bridge remain OPEN.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json (2026-10-11-execution-v2, all rules), current registry
and status, BOARD.md (2026-10-13 22:05 UTC), B05 STREAM_NOTES.md v2,
and lead run 20261011T225000Z §§1-2 were read. Own stage2 CLAIMS.json,
ODDFACE_GAP.tex, signed-Walsh/log kernel, STATUS, LEARNED and WORKLOG
provide the inherited scoped result. A025 run 20261012T045020Z REVIEW_A022.md
accepts only the constant-child bound; its fresh-control tower is not repeated.
A067's padding-access reserve and A097 LEARNED's physical removed/terminal
partition informed the unpaid-core audit; neither theorem is used as a premise.
A083 run 20261012T023941Z FORMAL_SCOPE.md and CLAIMS.json give the
coefficient comparison behind C005, reconstructed analytically in PROOF.md §3.
Threshold 38-page text §8.2 Proposition 8.6, (75)-(79), confirms the full-law
shared-data entropy/influence identities. SEED_LEMMAS.md was revisited;
no effective-piece or percolation implication is used in this proof.

## complete derivation or exact first unsupported line

Complete scoped proof: PROOF.md §§1-3. Query controls first (constant-child
B<3d), then one coordinate per intact quadratic pair while leaving the fair
selector unqueried (the reference branch contributes exactly 1/2 derivative,
so actual d>=1/4 and B/d<=8-3log2(3)<4). Query selector after the pairs become
characters, so common-character invariance reduces this access node to the
constant-child lemma. STOP at character-times-at-most-four-point leaves.
Section 2 proves dimension-free H_leaf<=6I_leaf, including dense small fibers
and the possible character-induced influence changes.

The exact physical partition is I=I_removed+I_terminal. Entropy telescopes
with all leaf entropy retained, giving H<=(4+2/ln2)I_removed+6I_terminal
<=(4+2/ln2)I. Threshold-4 bad credit is zero on access nodes only.
This avoids the previously certified data-first cancellation debt by delaying
partners; it does not prove that an arbitrary completion to constants is good.

First unsupported universal line: an arbitrary core or overlapping controller
admits an exposure/stopping policy with a uniformly paid unedited derivative
and complete terminal entropy. The d>=1/4 step uses an intact quadratic pair
and a fair selector. Neither hypothesis is automatic outside this class.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede execution: out/FROZEN_SPEC.json and EDGE_FROZEN_SPEC.json.
No symmetry quotient. Full domain: all 2516 k=4 patterns of sizes1..4,
all 2080 k=6 singleton/pair patterns plus three explicit larger patterns,
seven fixed k=8 patterns, each at r=0,2: 9212 actual Boolean roots.
The maximum truth-table dimension is 11. Leaf exhaustion includes every
E of size<=4 and every character on dimensions 0..4: 2702 sets, 41650 cases.
Arithmetic is signed integer Walsh, exact rational prime-log forms and outward
80-bit log2 intervals from a positive 50-term atanh series with proved tail.
Entropy and influence telescope symbolically, not by numerical tolerance.

Executed from own A022 folder, using python -X utf8:

- code/paired_access.py pilot: 272 roots, 74 leaf/character cases;
  {pilot['assertions']+pilot['kernel_assertions']:,} checks, {pilot['runtime_seconds']:.6f}s, PASS.
- code/paired_access.py full: 9212 roots, 41650 leaf/character cases;
  {full['assertions']+full['kernel_assertions']:,} checks, {full['runtime_seconds']:.6f}s, PASS.
- code/edge_reconstruct.py: all 9212 roots, {edge['checks']:,} checks,
  {edge['runtime_seconds']:.6f}s, PASS. This uses direct pair truth tables and cube
  edges, no Fourier transform or logarithm kernel; it independently reproduces
  removed/terminal influence and the sparse-character structural hypotheses.

Total executed checks: 956934. Full access counts: 9212 control nodes,
44468 pair nodes, 48900 selector nodes, all good at threshold4.
Memory estimates 180 MB for Walsh and 60 MB for reconstruction, below the
300 MB memok trigger; observed peak memory was not instrumented. Pilot and
full runs stayed within their 60s/1800s limits; no heavy concurrent job or
automatic dimension increase. Exact certificates are in out/; float runtime
measurements are metadata only. The separate representation is author
validation and does not count as an independent human review.

## proof dependencies and changed downstream conclusions

A022-ODDFACE-SURGERY-GAP-LEDGER v2 preserves all v1 statements and appends
the new stopping theorem; it does not open a differently named broad claim.
Its inherited constant-child subclaim has A025's scoped independent acceptance.
Other inherited and new conclusions await review. C005's analytic scalar
inequality is supplied directly in §3, including signed amplitudes and endpoints;
A083's Lean coefficient certificate is source support, not a formal claim
about real entropy. The sparse-leaf proof includes elementary edge isoperimetry.

Downstream change: the k=4 finite zero-credit observation is no longer the
only access guarantee for bounded surgery. A021/A023/A028 can use intact-pair
exposure for every even dimension, provided they preserve the fair unedited
branch and certify all terminal controllers. A025's tower remains a separate
result; no tower experiment is repeated. No shared registry was edited.

## one next mathematical action and independent reviewer

{next_action}
The review must distinguish access credit from constant-leaf completion and
check the character influence monotonicity only in the u<=1/4 regime.

## actual persistence receipts or precise save blocker

All four required protocol files, PROOF.md, executable code and exact outputs
are locally saved in this run. STATUS has exactly two lines; WORKLOG is
appended and LEARNED records the durable theorem and its scope.
out/ARTIFACT_RECEIPTS.json records byte counts and SHA256 for run artifacts;
the finalize script rechecks required field sets, statement hash, compatibility
copy equality and the 20 MB size cap. No save blocker. Supervisor mirror,
registry adoption, independent acceptance and downstream use are unverified.

Universal bridge: This stage moves C019 and the B05 localized odd-face bridge
on bounded bent surgery: all access bad-node credit is eliminated for every
even k and every number of fresh controls, and the retained leaf cost is paid
by the disjoint terminal influence budget with coefficient6. The universal
gap remains the existence of analogous exposure and certified terminal leaves
for arbitrary cores and overlapping controllers. NEXT tests the first
overlap/fairness failure with the same one-use partition, the shortest route
from this mechanism to the universal payment rather than another isolated
finite-dimensional maximum.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(BASE/'STATUS.md').write_text('STATE: A022 stage 3 complete: all-even-k paired exposure gives zero access bad credit for <=4 flips, terminal H<=6I, root H<=(4+2/ln2)I; 956934 checks PASS; review pending; full FEI OPEN.\nNEXT: A087/A094 review; extend intact-pair exposure to three overlapping control events with fair-branch weight and complete terminal entropy paid from one physical influence partition.\n',encoding='utf-8')
with (BASE/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-13 22:09 UTC stage / saved '+datetime.datetime.now(datetime.timezone.utc).isoformat()+': Consumed A025 constant-child scoped acceptance and board overlapping-controller frontier. Changed cancellation-debt mechanism to query one coordinate per quadratic pair before partners. Proved all-even-k/all-r zero access credit for <=4 flips and sparse terminal H<=6I, retaining complete terminal entropy; explicit C005 scalar reconstruction yields root H<=(4+2/ln2)I. Frozen 9212 roots plus 41650 leaf/character cases PASS, independent edge implementation PASS; total956934 checks. Universal arbitrary-core/overlap exposure remains open; v2 pending independent review.\n')
with (BASE/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nPaired exposure theorem (stage3): For quadratic bent b on any even k>=2, fresh point activation on any r>=0 and a fair b/edited-b selector with <=4 edits, controls -> first bit of every pair -> selector -> STOP has zero K4 bad credit at all access nodes. Pair nodes have d>=1/4 because the untouched fair branch retains an intact partner; B/d<=8-3log2(3)<4. Selector nodes reduce by common character shift to constant-child bound B/d<3. Leaves retain all partners, each a character times <=4 point defects. Universally for those leaves H<=6I: u<=1/4 makes character multiplication increase influence and isoperimetry pays the entropy; u>1/4 forces dimension<=3 and a minimum-cut argument pays H. Exact partition I_removed+I_terminal=I gives H<=(4+2/ln2)I_removed+6I_terminal. Zero access credit does NOT mean zero credit after arbitrary completion to constants. Fairness and intact quadratic partners are essential; arbitrary or biased overlapping controllers remain unpaid. A025 independently accepts only inherited v1 constant-child lemma, not this extension.\n')
protocol=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text())
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
expected={x if not x.startswith('packet_ids ') else 'packet_ids' for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
receipt=[]
for p in sorted(RUN.rglob('*')):
    if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
        data=p.read_bytes();assert len(data)<20*1024*1024
        receipt.append({'path':str(p.relative_to(RUN)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(RUN/'out/ARTIFACT_RECEIPTS.json').write_text(json.dumps({'schema_check':'PASS','compatibility_copy':'IDENTICAL','statement_hash_convention':'registry JSON statement/hypotheses convention','files':receipt,'mirror':'UNVERIFIED'},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'saved_run':str(RUN),'artifact_count':len(receipt),'schema':'PASS','total_checks':956934,'largest_bytes':max(x['bytes'] for x in receipt)}))
