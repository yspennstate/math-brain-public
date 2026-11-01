"""Persist the stage18 author-checked result and exact protocol records."""
import hashlib
import json
from pathlib import Path

R = Path(__file__).resolve().parents[1]
A = R.parent.parent
OLD = A / 'runs/20261021T213328Z-fleet03-A017-recursive-addressing'
SIX = A / 'runs/20261014T102650Z-fleet05-A017-recursive-addressing'
P = Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p, x): p.write_text(json.dumps(x, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
def sha(b): return hashlib.sha256(b).hexdigest()
protocol = read(P)
for name in ['INHERITED_CRITICAL_PROOF.md', 'DERIVATION.md', 'INHERITED_STAGE5_PROOF.md']:
    source = SIX / name
    if source.exists():
        (R / name).write_bytes(source.read_bytes())
source = OLD / 'out/paper_source_notes.json'
if source.exists():
    (R / 'out/inherited_paper_source_notes.json').write_bytes(source.read_bytes())

consumers = ['A018','A020','A030','A090','A091','B04']
statement = ('For every n, quadratic q on the uniform binary cube, linear address M, '
 'independent physical sign data y_z, and E of at most twelve vertices in one fiber of M, '
 'F(x,y)=(-1)^q(x)(1-2*1_E(x))*y_(Mx) satisfies H(F)<=(4+2/ln(2))*(I(F)-1). '
 'Moreover, for a quadratic polar matrix Q, Q_i nonzero, P={partial_i q=1}, and '
 'g=(-1)^q*(1-2*1_E), every original physical j!=i with Q_ij=0 and '
 'Q_j outside span(Q_i) satisfies Inf_j(g)>=1/4-2*|E intersect P^c|/2^n. '
 'If E is contained in P and a physical set J consists of such j with Q_jk=0 '
 'for every j,k in J, querying all J in any fixed order is K4-good on every '
 'history and gives H(g)<=K*sum_j Inf_j(g)+average_a H(g|J=a) and '
 'I(g)=sum_j Inf_j(g)+average_a I(g|J=a), K=4+2/ln(2).')
deps = [
 {'claim_id':'A017-FOUR-EDGE-COMPATIBILITY','version':1,
  'status':'AUTHOR_CHECKED_PENDING_INDEPENDENT_REVIEW',
  'used_for':'Planar four-pair case and twelve-edit terminal bound.'},
 {'claim_id':'A017-TWO-EDIT-SHARED-ADDRESS-STOPPING','version':4,
  'status':'AUTHOR_CHECKED_PENDING_INDEPENDENT_REVIEW',
  'used_for':'Physical stopping ledger, five-control certificate, odd five-pair case and JS bound.'}]
claim = dict(claim_id='A017-FOUR-EDGE-COMPATIBILITY', version=2,
 exact_statement=statement,
 hypotheses=['Uniform cube; base-two entropy; actual Boolean phases and original physical influence.',
 'Twelve-edit theorem: edits in one linear-address fiber, independent physical data labels.',
 'One tangent step: nonzero Q_i, Q_ij=0, Q_j not in span(Q_i); e_out<=2^n/32 suffices for K4 payment.',
 'Whole tangent block: E subset P and pairwise Q_jk=0; full residual leaf entropies remain unpaid.'],
 statement_sha256=sha(statement.encode('utf-8')),contributors=['A017'],
 proof_source=['PROOF.md','INHERITED_STAGE17_PROOF.md','INHERITED_STAGE6_PROOF.md','code/','out/'],
 proof_dependencies=deps, review_records=[],
 status='AUTHOR_CHECKED_PROOF_AND_EXACT_CERTIFICATES_PENDING_REVIEW',
 supersedes=['A017-FOUR-EDGE-COMPATIBILITY@1'],refutes=[],first_unproved_line=None,
 next_consumers=consumers)
next_action = ('Transfer eligibility or refund across one interacting original physical query, '
 'retaining BOTH full child entropies and the SAME unused original influence. '
 'A090/A091 should reconstruct the complete twelve-edit dependency chain and block invariant.')
progress = dict(protocol_revision=protocol['revision'],run_id=R.name,stream='B04',packet_id='A017',
 gap_id=read(OLD/'PROGRESS.json')['gap_id'],
 attempt_id='A017-stage18-tetrahedral-closure-and-physical-tangent-history',
 method='Exact tetrahedral normal forms and symmetry orbits; separate direct Boolean character sums; physical half-cube edge counting and hereditary tangent blocks.',
 mathematical_delta='Closed affine-span-three critical node, hence unconditional twelve coherent same-fiber edit stopping at unchanged K. Proved a count-independent physical tangent lower bound and pairwise noninteracting whole-block payment on every history; full leaf payment remains open.',
 deliverable_status='LOCAL_COMPLETE_REVIEW_AND_SUPERVISOR_TRANSFER_PENDING',
 mathematical_status='AUTHOR_CHECKED_RESTRICTED_PROOF;FULL_FEI_OPEN',
 claim_versions_used=[{'claim_id':d['claim_id'],'version':d['version']} for d in deps],
 claims_created_or_changed=[{'claim_id':claim['claim_id'],'version':2}],
 source_artifacts=['REPORT.md','PROOF.md','CLAIMS.json','INHERITED_STAGE17_PROOF.md','INHERITED_STAGE6_PROOF.md','code/','out/'],
 next_consumers=consumers,next_action=next_action,stagnant_substantive_attempts=0,
 blockers=['Independent proof review pending, including inherited dependencies.',
 'Full FEI: interacting-query history transfer and retained leaf-entropy payment are unproved.',
 'Lean admission held; no Lean certification.',
 'Supervisor adoption and remote mirror verification pending.'],packet_ids=['A017'])
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
save(R/'CLAIMS.json',[claim])
save(R/'PROGRESS.json',progress)
(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())

fields = protocol['required_per_run']['report_fields']
sections = [
'''Author-checked result, independent review pending: the previously conditional twelve-edit stopping theorem is now unconditional, at K=4+2/ln(2), in all dimensions for the actual family stated in CLAIMS.json. Entropy is in bits and influence uses uniform original physical coordinates. The separate tangent-block theorem allows arbitrarily many inside-half edits and block coordinates, under its explicit polar-row and pairwise noninteraction hypotheses. Its full leaf entropies remain in the conclusion. Full FEI remains OPEN.''',
'''This stage read BOARD.md, B04 STREAM_NOTES v2, own STATUS/LEARNED and the full execution protocol, plus the prior stage17 proof and stage6 dependency arguments used here. Source locators: PROOF.md sections 1-4 for the tetrahedral reduction and twelve-edit consequence, sections 5-7 for the physical tangent lemma and block invariant. Copies of prior proofs and certificates are included. Threshold/percolation paper reading belongs to earlier stages; no fresh reading or new theorem from those papers is claimed here. Campaign deadline follows the current owner instruction, 2026-10-23 14:49 UTC. No additional worker was launched.''',
'''The critical node has four surviving pivotal pairs. If R removals, A additions and D double edits are counted, R-A=12 and R+A+2D<=12 force R=12,A=D=0. The survivor set lies in a four-dimensional derivative hyperplane. The inherited proof pays affine-span-two survivors. For affine-span-three, normalize W={0,1,2,4} in four child coordinates, with selected children a and a-2*1_W on one half and a common quadratic b on the other. There are 4096 normalized a choices. Eleven explicitly checked generators reduce the 1024 normalized quadratic b choices to 14 orbits. All 57344 representatives have B_i<=4 Inf_i by exact positive-integer products. Unqueried affine symmetries transport only this selected-coordinate inequality; no other physical influence budget is transported. PROOF.md gives the converse actual twelve-edit realization and the complete all-dimensional stopping deduction from the inherited small-dimensional/odd-lattice/terminal results.

The count-independent mechanism uses original physical edges: tangent j with independent polar row has unedited outside-half influence 1/4, and each outside edit loses at most 2/2^n. Thus Inf_j>=1/4-2 e_out/2^n; e_out<=2^n/32 makes the query K4-good. For E subset P and pairwise noninteracting eligible physical J, restriction removes only zero columns from the relevant rows, so eligibility holds on EVERY history. The whole block spends sum_j Inf_j(g) once and retains the exact full leaf entropy and influence. Actual fixtures show failure after dropping tangency, row independence, or pairwise noninteraction.

No unsupported line is used in the scoped claims. The first unsupported universal line is extending eligibility/payment through interacting physical queries or paying all retained leaves using the same unused original influence. The block may be empty; its existence does not solve FEI. Inherited claims remain author-checked pending external review.''',
'''Frozen specifications precede searches in out/*_spec.json, with helper version/hash, exact Boolean domain, case count, symmetry, arithmetic, memory estimate and runtime ceiling. All jobs were small, sequential and below the 300 MB estimated admission threshold; peak RAM was not measured and no automatic dimension escalation occurred. Commands were python -X utf8 code/orbits.py, code/tetra.py [--pilot], code/independent.py [--pilot], code/tangent.py [--pilot], and code/block.py [--pilot], according to each script's saved invocation/specification.

Exact outputs: orbits.json has 1024 outside words, 11264 generator actions and 14 orbits (0.153 s). tetra_certificate.json has 57344 parents, 540 histograms, zero failures (7.384 s). independent_certificate.json reconstructs 57344 actual 64-bit truth tables using XOR/popcount character sums, 11264 actual-parent generator actions and 137217 assertions (10.810 s). This is a different representation by the same author, not external-agent review. Exact global maxima agree by cross multiplication. Entropy signs use integer products/prime-exponent products, never floating-point logarithmic decisions.

tangent_certificate.json verifies 4624 actual parents and 9252 assertions (0.304 s), including sharp and failed-hypothesis fixtures. block_certificate.json covers all 65536 inside-half masks in its five-bit family, all three query histories, four full leaves per parent and 262144 assertions (8.982 s). The block pilot covered only 16 masks; its smaller maximum spent influence reflects that smaller domain. The interacting fixture retains the actual truth table. Pilots finished below 60 seconds. Code/CriticalCounts.lean states only the elementary count rigidity. Its requested check returned SETUP_UNVERIFIED: admission held because of hung-window/free-memory conditions; no compiler process was started and no Lean verification is claimed. The exact receipt is out/lean_attempt.json.''',
'''A017-FOUR-EDGE-COMPATIBILITY@2 supersedes version1 and depends on its planar and terminal cases, and A017-TWO-EDIT-SHARED-ADDRESS-STOPPING@4 for the physical ledger and remaining local cases. Both dependencies retain their pending independent-review status. Two finite implementations agree but do not constitute external acceptance of the complete theorem. The downstream change is precise: remove the affine-span-three condition from the twelve-edit consequence. The new physical block gives a count-independent all-history access payment but no leaf-entropy theorem. The earlier actual bad generic K4 parent and distance-fourteen obstruction are not refuted or discarded.''',
next_action+''' This is shorter than another fixed edit-count census because it addresses the missing history transfer for arbitrary inside edits and full retained child entropy. Independent reviewers requested through saved handoff: A090/A091, with A018/A020 as downstream consumers. No external message was sent.''',
'''All local files are written beneath A017. out/PERSISTENCE_RECEIPTS.json records paths, byte sizes and SHA256 values after JSON/schema/compatibility checks; it excludes itself. Each file is under 20 MB. STATUS.md, WORKLOG.md and LEARNED.md are updated. No remote-copy or independent acceptance receipt exists; supervisor transfer is pending. No job was left running and no process was stopped. Brain self-care is degraded/unverified: the model-of-owner and state-of-mind notes were stale (about 87.8 and 72.4 hours at wake); personalization based on them is unverified, and they were not used as mathematical premises.'''
]
report = '# A017 stage18: twelve-edit closure and physical tangent histories\n\n'
report += '\n\n'.join('## '+h+'\n\n'+s for h,s in zip(fields,sections))
report += '''\n\n## Universal bridge

This stage moves C019 stopping-tree payment and the associated C018 erasure bill: the affine-span-three critical node is paid, making the all-dimensional twelve coherent same-fiber edit theorem unconditional at the same K, while the noninteracting physical tangent block now pays every query on every history with no inside-edit count bound and with both full child entropies retained. The remaining universal gap is interacting-query eligibility/refund and full leaf-entropy payment from the same unused original influence. That transfer, rather than another isolated finite-edit class, is the shortest next route toward full FEI; neither universal bridge is closed here.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
status = ('STATE: A017 stage18 saved: unconditional <=12-edit stopping at SAME K; tetra57344 independently PASS; arbitrary-inside-edit physical tangent block paid on all histories; FEI OPEN, review pending.\n'
 'NEXT: Transfer eligibility/refund across one interacting physical query with BOTH full child entropies and SAME unused original influence; A090/A091 review full12/block invariant.\n')
(A/'STATUS.md').write_text(status,encoding='utf-8')
for name, note in [
 ('WORKLOG.md','Closed tetrahedral four-pair case with 57344 exact cases in two implementations; derived unconditional twelve-edit all-dimensional stopping at unchanged K. Proved robust physical tangent bound and count-independent noninteracting block payment; exact 65536-mask history certificate passed. Interacting eligibility counterfixture saved. Full FEI and retained-leaf payment remain open; external review pending; Lean admission held.'),
 ('LEARNED.md','For g=(-1)^q(1-2*1_E), Q_i nonzero, P={partial_i q=1}, original physical Q_ij=0 and Q_j outside span(Q_i) imply Inf_j>=1/4-2|E intersect P^c|/2^n. If E subset P and eligible J has Q_jk=0 pairwise, eligibility survives every restriction history: H(g)<=K sum_J Inf_j(g)+average H(leaves), I(g)=sum_J Inf_j(g)+average I(leaves). Full leaf entropy is unpaid. Dropping pairwise noninteraction fails: q=x0*x1+x2*x3, edits make P constant, query x2=0 yields constant child. The twelve-edit tetrahedron reduces to 14*4096 exact cases; all pass B<=4Inf, closing the prior conditional twelve-edit theorem pending external review.')]:
    p=A/name
    prior=p.read_text(encoding='utf-8-sig') if p.exists() else ''
    marker='2026-10-23 stage18 (20261023T012331Z)'
    if marker not in prior:
        p.write_text(prior+'\n\n'+marker+': '+note+'\n',encoding='utf-8')

assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert sha(claim['exact_statement'].encode('utf-8'))==claim['statement_sha256']
for h in fields: assert '## '+h+'\n' in report
assert '## Universal bridge' in report
manifest=[]
for f in sorted(R.rglob('*')):
    if not f.is_file() or f.name=='PERSISTENCE_RECEIPTS.json': continue
    b=f.read_bytes()
    assert len(b)<20*1024*1024, f
    if f.suffix=='.json': read(f)
    manifest.append({'path':f.relative_to(R).as_posix(),'bytes':len(b),'sha256':sha(b)})
save(R/'out/PERSISTENCE_RECEIPTS.json',dict(status='LOCAL_FILES_VALIDATED',
 full_fei='OPEN',review='PENDING',remote='SUPERVISOR_PENDING',files=manifest,
 rolling=[{'path':n,'sha256':sha((A/n).read_bytes())} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]))
print(json.dumps({'status':'LOCAL_FILES_VALIDATED','files':len(manifest),'claim':claim['claim_id']+'@2','full_fei':'OPEN','review':'PENDING'}))
