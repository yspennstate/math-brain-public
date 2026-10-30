from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1];CAMP=ROOT.parents[1]
PROTO=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def write(p,t):p.write_text(t,encoding='utf-8',newline='\n')
def save(p,v):write(p,json.dumps(v,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
main=json.loads((RUN/'out/EXACT_CHECK.json').read_text(encoding='utf-8'))
ind=json.loads((RUN/'out/INDEPENDENT.json').read_text(encoding='utf-8'))
sharp=json.loads((RUN/'out/SHARPNESS.json').read_text(encoding='utf-8'))
assert all(x['status']=='PASS' for x in [main,ind,sharp])
total=sum(x['assertions'] for x in [main,ind,sharp]);assert total==91721
oldrun=ROOT/'runs/20261023T064432Z-fleet03-A053-near-tensor-perturbations'
source_run=CAMP/'agents/A051/runs/20261023T113401Z-fleet03-A051-near-extremizer-definition'
source_claims=json.loads((source_run/'CLAIMS.json').read_text(encoding='utf-8'))
sources=[PROTO,CAMP/'BOARD.md',CAMP/'claude/B11/STREAM_NOTES.md',
 oldrun/'MULTI_SURGERY_PROOF.md',oldrun/'CLAIMS.json',
 source_run/'STOPPING.md',source_run/'REPORT.md',source_run/'CLAIMS.json',
 CAMP/'agents/A052/runs/20261023T055856Z-fleet03-A052-critical-source-structure/REPORT.md',
 CAMP/'agents/A054/runs/20261023T105740Z-fleet03-A054-connectedness-alternatives/REPORT.md',
 CAMP/'agents/A055/runs/20261023T112023Z-fleet03-A055-extremal-obstruction-referee/REPORT.md']
save(RUN/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p)} for p in sources])
save(RUN/'out/REVIEW_RECORD.json',{'reviewer':'A053','source_claims':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256']} for c in source_claims],
 'source_proof_sha256':sha(source_run/'STOPPING.md'),'verdict':'HOLDS_WITHOUT_REPAIR_AT_SECTIONS_1_2_SCOPE','review_source':'REVIEW_A051.md',
 'scope':'fixed original error-event transport, occupation Jensen and complete signed bank, equations1--3a; retains source channel inequality, also derived in own proof',
 'excluded':'No independent acceptance of source large activation constants, no universal selector, no new-theorem independent-agent acceptance or registry adoption'})
compute=Path(r'~\.claude\compute\compute_state.json')
if compute.exists():
 d=json.loads(compute.read_text(encoding='utf-8-sig'))
 b=json.loads((RUN/'out/COMPUTE_BEFORE.json').read_text(encoding='utf-8'))
 save(RUN/'out/COMPUTE_AFTER.json',{'observed_utc':datetime.now(timezone.utc).isoformat(),'snapshot_ts':d.get('ts'),'before_snapshot_ts':b['snapshot'].get('ts'),'same_timestamp':d.get('ts')==b['snapshot'].get('ts'),'observation_interval_seconds':(datetime.now(timezone.utc)-datetime.fromisoformat(b['observed_utc'])).total_seconds(),'interpretation':'Unchanged snapshot is not a fresh safety admission; no governor process or other work stopped/restarted.'})
cid='A053-ARBITRARY-SURGERY-CRITICAL-RADIUS'
statement='For n>=3, let F be a Boolean sign with normalized Fourier support minimum Hamming distance at least3, and let Boolean G differ from F at exactly R>=1 vertices. For every relevant ORIGINAL coordinate i, L_i(G)<(37/4)R Inf_i(G). At K=10R the complete-child expected D_K gain is greater than(3/2)R2^-n. Thus a least-essential-dimension positive fixed-K witness, K>=0, has distance R>4K/37 from EVERY such seed; distance0 is also excluded. Linear dependence on the edit count is optimal in order for an ALL-relevant-coordinate guarantee: for every odd k>=3, the explicit Hamming-kernel bent-selector G* on n=r=2^k bits differs from such a seed at r+1 vertices, is tensor-prime with full Fourier support, satisfies H(G*)<=3I(G*), and has L_z/Inf_z>=(r-k-3)(1-1/r), whose ratio to the edit count tends to1. No fresh inherited bank or universal critical-source selection is claimed.'
claims=[{'claim_id':cid,'version':2,'exact_statement':statement,
 'hypotheses':['Uniform finite binary cube; normalized Walsh transform; entropy bits; n>=3','Upper bound uses arbitrary edit set of R vertices and a seed with Fourier support distance>=3; queried coordinate relevant','Critical corollary requires an actual positive fixed-K witness of least essential dimension among all Boolean positive K-witnesses; no existence assumed','Order lower family is the actual Boolean construction in SHARPNESS_PROOF.md, odd k>=3'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A053'],
 'proof_source':'LINEAR_RADIUS_PROOF.md and SHARPNESS_PROOF.md',
 'proof_dependencies':['Self-contained row entropy/curvature, Boolean granularity, Hamming packing, sparse-derivative Cauchy-Schwarz and edited-edge cancellation; elementary Hamming-kernel/bent construction'],
 'review_records':[{'reviewer':'A053','kind':'author derivations, main exact checks, separate direct-character replay and physical/compressed sharpness certificates','outcome':'91721 full new-stage assertions PASS; independent-agent review pending'}],
 'status':'AUTHOR_PROOF_EXACT_VALIDATION_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[cid+'@1 (valid weaker quadratic-rate statement)'],'refutes':[],
 'first_unproved_line':'No gap claimed in the stated linear neighborhood theorem or its all-policy order lower family. A genuine critical source outside these neighborhoods still lacks a selected paid original block with sufficient unused independent release.',
 'next_consumers':['B11','A051','A052','A055','A090','A094','B20']}]
save(RUN/'CLAIMS.json',claims)
versions=[cid+'@1 (comparison only; row bound rederived)']+[c['claim_id']+'@'+str(c['version'])+' (A051 sections1--2 scoped review only)' for c in source_claims]
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B11','packet_id':'A053','gap_id':'G-A053-CRITICAL-QUANTITATIVE-SEPARATION',
 'attempt_id':'A053-stage20-linear-radius-and-prime-sharpness',
 'method':'Sparse derivative Cauchy lower influence; seed-independent edited-edge cancellation; universal low-dimension bound; Hamming-kernel sharpness; original complete-child bank',
 'mathematical_delta':'Quadratic5R+17R^2/4 improved to linear37R/4 for every relevant original singleton; genuine K-critical edit radius improves to R>4K/37. Tensor-prime/full-support FEI3 Hamming-kernel family has singleton price asymptotic to its edit count, proving linear-order sharpness for all-coordinate guarantees. A051 occupation equation/bank independently reconstructed at sections1--2 scope.',
 'deliverable_status':'COMPLETE_SAVED_LOCAL; independent review, shared adoption and supervisor copies pending',
 'mathematical_status':'LINEAR_CRITICAL_RADIUS_AND_ORDER_SHARPNESS_AUTHOR_CHECKED; FULL_FEI_OPEN; UNIVERSAL_SELECTOR_OPEN',
 'claim_versions_used':versions,'claims_created_or_changed':[cid+'@2'],
 'source_artifacts':[str(p) for p in sources]+['LINEAR_RADIUS_PROOF.md','SHARPNESS_PROOF.md','REVIEW_A051.md','out/EXACT_CHECK.json','out/INDEPENDENT.json','out/SHARPNESS.json','out/FROZEN_SPEC_V2.json','out/FROZEN_SHARPNESS.json'],
 'next_consumers':['B11','A051','A052','A055','A090','A094','B20'],
 'next_action':'Use genuine nonnegative smaller-child reserves to select an ORIGINAL block or force unused quotient-rank release on the residual R>4K/37 critical class; all-coordinate improvement is limited by the FEI3 prime sharpness family. A090/A094 review cancellation, Cauchy branch and lower family.',
 'stagnant_substantive_attempts':0,
 'blockers':['No universal critical original-block selector or unused-rank lower funding','New v2 awaits independent-agent review; supervisor mirror/adoption unverified','Checklist working T-20261023-452 failed: checklist lock held too long; no lock modified; closure outcome recorded separately if available','Brain self-care degraded/unverified: owner model, state of mind and dream stale; not mathematical premises'],
 'packet_ids':['A053']}
save(RUN/'PROGRESS.json',progress);(RUN/'PACKET_DELTA.json').write_bytes((RUN/'PROGRESS.json').read_bytes())
report=f"""# A053 stage20: linear critical radius, with prime sharpness

## exact target, quantifiers, hypotheses and units
For every n>=3 Boolean seed F of normalized Fourier support distance>=3 and every R-vertex Boolean edit G, pay every relevant ORIGINAL singleton with a rate linear in edit count. Entropy bits; R is the number of edited vertices, not an affine-reset reserve. Retain the complete original child ledger. Derive a necessary condition on genuine least-dimensional positive K-witnesses and determine whether the all-coordinate rate can have smaller order. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators
BOARD12:27UTC, B11 STREAM_NOTESv2 and own stage19 STATUS read first. Fresh complete reports: A05111:34, A05410:57, A05511:20; A052 newest12:04 run lacked REPORT at initial inspection, so completed05:58 REPORT was used instead. A051 STOPPING Sections1--5 read whole; REVIEW_A051 independently reconstructs Sections1--2 and equations1--3a only. Other reports are context, not accepted theorem premises. Own previous proof and protocol field sets reloaded. Earlier campaign/registry/manuscript baseline reads are retained, not represented as a fresh full-paper audit. SOURCE_RECEIPTS binds observed bytes.

Required exact-session wake completed with warnings: owner model99h, state-of-mind83.6h, latest dream34.3h stale. Personal-context and consolidation freshness remain degraded/unverified. No affected note is a mathematical premise. Current owner deadline14:49UTC governs over the older protocol clock.

## complete derivation or exact first unsupported line
LINEAR_RADIUS_PROOF gives the full upper proof. The previous common row estimate is rederived as L_i<10Rp+(2n+5/2)beta, beta<=4sR^2p^2, s(n+1)<=1/p. If the seed is independent of i, edited pairs cancel in the off-anchor transform: |ehat(S+i)|<=Inf_i(G), so beta<=s Inf_i(G)^2. This gives L_i/Inf_i<37R/4 directly. If the seed depends on i, Fourier Cauchy at a nonzero physical derivative gives Inf_i(F)>=1/s_i>=(n+1)p. For n+1>=4R this survives surgery at at least(n+1)p/2; otherwise the universal L_i/Inf_i<n+7/2 suffices. The cases give the SAME linear bound.

Both complete children retain reach1/2. Exact accounting is E D_K(child)-D_K(G)=K Inf_i-L_i. Therefore K10R gives gain>(3/2)Rp. Genuine criticality requires the opposite sign because every smaller child is nonviolating; hence every such witness has R>4K/37 from every distance-three-support seed. This strengthens stage19's quadratic threshold5R+17R^2/4; the old sharper single-edit two-query rate9 remains unchanged.

SHARPNESS_PROOF constructs an actual order lower family. For odd k>=3, r=2^k, use the kernel of the binary Hamming parity-check matrix to encode a bent quadratic on m=r-1-k bits; add a selector. Flip its selector-one zero fibre and physical0. The r+1 edits give full Fourier support and odd negative count, hence tensor primitivity. Querying the ORIGINAL selector has I_z=d(1-1/r), occupied off-anchor mass d(1-1/r)^2 and L_z/I_z>=(r-k-3)(1-1/r). Dividing by edit count tends to1. The roots satisfy FEI3 by I>=(7r-9)/16 and H<=r. This proves linear order necessary for paying EVERY coordinate; it neither refutes a selected critical query nor FEI.

First unsupported universal line: criticality must select a paid original proper block, or force enough unused independent child rank, on the residual far-from-code class. Neither primitivity nor full support supplies that selection. The theorem is root-local and cannot be booked again after restrictions destroy its packing hypothesis.

## executed validation with domain, arithmetic, commands and outputs
Frozen specifications precede adopted jobs. Commands: python -B -X utf8 this-run/code/prepare.py; code/run_checks.py (sequential pilot, full and separate replay); code/run_sharpness.py. The controllers capture actual exits and logs and use CREATE_NO_WINDOW for each synchronous child.

Pilot592 roots/1776 cuts,21344 assertions PASS. Main1503 roots/4572 original singleton cuts: all16 signed n3 character seeds with every edit set size0..3; nine fixed n6 and six fixed n9 noncharacter coded-seed edits, including size8. {main['assertions']} assertions PASS in{main['runtime_seconds']:.6f}s. The new predicates are seed-derivative Cauchy, actual edited-edge cancellation and linear payment/gain; old successful tests were not rerun unchanged. Every proof branch is hit, and96 irrelevant-G cuts are explicitly excluded from division.

Separate direct-character/physical-edge implementation with its own32-term rational log helper:1478 roots, {ind['assertions']} checks PASS in{ind['runtime_seconds']:.6f}s. It also verifies the reviewed occupation guard: e1/8, expected depth7/4, occupied error moment3/8 versus false independent product7/32. This is a separate A053 implementation, not independent-agent acceptance.

Sharpness: complete n8 truth table, every coefficient and directional edge, exact negative parity, seed packing and all signed amplitude groups; compressed profiles k3,5,7,9 with exact mass/influence/off-anchor identities. {sharp['assertions']} assertions PASS in{sharp['runtime_seconds']:.6f}s. Large spectra are represented by proved multiplicities, never expanded. Infinite linear-order sharpness is the analytic Hamming-kernel construction, not finite extrapolation.

Combined NEW full-stage count{total}, excluding pilot and all previous stages; it differs from prior115350 because the predicates and domains changed. Integer Walsh versus direct characters, Fraction and explicit rational atanh tails; no floating sign decisions. No mathematical job failed. Each job55s guard, estimated80MB, peak unmeasured; no >300MB job, GPU, automatic dimension increase, detached work or Lean certificate.

## proof dependencies and changed downstream conclusions
Version2 strengthens the existing A053 arbitrary-surgery candidate rather than opening a new broad universal claim. The row estimates are rederived; the linear improvement uses physical derivative Cauchy and edge cancellation. The order lower family is self-contained Boolean algebra. Version1 remains valid as a weaker bound. No accepted source theorem is refuted. Universal FEI constant gain remains0.

A051 Sections1--2 occupation and complete signed-bank identities independently HOLD without repair, at the stated retained one-query channel scope; source large activation constants are not newly accepted. Expected depth alone is not a substitute for occupation of the SAME original error event. A052 fixed-partition invariance, A054 marked-direction costs and A055 all-block absolute-error guard are consumed at report scope to avoid reusing known failed funding mechanisms.

## one next mathematical action and independent reviewer
A051/A052/A055 should use genuine nonnegative smaller-child reserves to select one ORIGINAL proper block or prove unused quotient-rank lower funding on the residual R>4K/37 critical class. A090/A094 should reconstruct the dependent/independent branch split, the beta bound and the prime Hamming-kernel lower family. All-coordinate improvement below linear edit count is blocked by the FEI3 example; conditional selection is the required next mechanism. No external message was sent.

## actual persistence receipts or precise save blocker
Four exact-schema protocol files, two proofs, scoped review, frozen specs, code and exact outputs saved only in the requested A053 run. STATUS is two lines; WORKLOG/LEARNED updated. Finalizer checks exact field sets, statement hashes,20MB cap and byte-identical PROGRESS/PACKET_DELTA; subsequent readback verifies saved hashes. Supervisor copies, shared adoption and independent-agent review remain pending.

Checklist working T-20261023-452 failed with RuntimeError: checklist lock held too long. No lock was changed; administrative closure is separately recorded if attempted. Snapshot13:57:59 local was not assumed fresh; before/after timestamps and bounded governor-log tail are recorded, with no governor restart or interference with existing work. No git, brain write, trading access or research mutation outside A053. All stage mathematical jobs finished.

## Universal bridge
C019 stopping-tree payment gains a linear critical separation R>4K/37, replacing the previous square-root-order radius from a quadratic payment rate, and an actual tensor-prime/full-support FEI3 family proving this all-coordinate rate has optimal linear order. Universal constant gain is zero: neither result selects a block on genuine critical sources outside the excluded neighborhoods. NEXT exploits exact nonnegative smaller-child reserves and unused quotient rank to choose an ORIGINAL block in the SAME bank; it targets the remaining universal implication rather than another primitivity test or fresh inherited budget.
"""
write(RUN/'REPORT.md',report)
write(ROOT/'STATUS.md',f'STATE: Stage20 saved: linear37R/4 original-singleton payment;critical radiusR>4K/37;prime full-support FEI3 family proves linear order sharp;{total} exact full checks PASS;FEI OPEN.\nNEXT: Critical ORIGINAL block selection or unused quotient-rank funding on residual far-from-code class in SAME bank;A090/A094 review v2 branches and prime sharpness.\n')
stamp=datetime.now(timezone.utc).isoformat()
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:
 f.write('\n'+stamp+f' stage20: v2 linear37R/4 rate via sparse-derivative Cauchy and edited-edge cancellation, replacing quadratic bound. Critical R>4K/37. Hamming-kernel bent-selector plus physical0 edit gives actual prime/full-spectrum FEI3 roots and price asymptotic to edit count. Main{main["assertions"]}+separate replay{ind["assertions"]}+sharpness{sharp["assertions"]}={total} full checks PASS; pilot excluded. A051 occupation Sections1--2 reconstructed, strict3/8 versus7/32 correlation guard. Checklist working failed shared lock; no lock touched. Own jobs finished, fullFEI/critical selector OPEN; independent review and supervisor copying pending.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:
 f.write('\nStage20: every relevant original singleton of an R-vertex edit of a distance-three-support Boolean seed pays at37R/4, not just the prior5R+17R^2/4. Seed dependence gives I_F>=1/s_i>=(n+1)p; seed independence gives |ehat(S+i)|<=I_G by cancellation of doubly edited edges. Split n+1>=4R versus small dimension. Genuine K-critical radius must exceed4K/37. Linear order is sharp for all-coordinate payment: odd k>=3,r2^k,nr,Hamming-kernel bent seed, edit selector-one zero fibre and physical0, totalr+1 edits. Full-support odd-negative-count root is tensor-prime, FEI3, and selector price>=(r-k-3)(1-1/r). Thus criticality/selection is essential for an absolute rate. A051 occupation uses E[1_Z tau], never the unjustified productP(Z)E tau. Root-local packing is not a fresh inherited bank.\n')
proto=json.loads(PROTO.read_text(encoding='utf-8'))['required_per_run']
assert set(claims[0])==set(proto['claim_fields'])
assert set(progress)==set('packet_ids' if x.startswith('packet_ids ') else x for x in proto['progress_fields'])
assert all(s in report for s in proto['report_fields'])
assert report.rstrip().splitlines()[-1].startswith('C019')
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((ROOT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
receipts=[]
for p in sorted(RUN.rglob('*')):
 if p.is_file() and '__pycache__' not in str(p) and p.name not in ['PERSISTENCE_RECEIPTS.json','HANDOFF_CHECK.json']:
  assert p.stat().st_size<20_000_000
  receipts.append({'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(RUN/'out/PERSISTENCE_RECEIPTS.json',{'schema':'PASS','compatibility_copy':'BYTE_IDENTICAL','files':receipts,'rolling':[{'path':str(p),'sha256':sha(p)} for p in [ROOT/'STATUS.md',ROOT/'WORKLOG.md',ROOT/'LEARNED.md']],'mirror':'not verified; supervisor pending'})
print(json.dumps({'saved':str(RUN),'schema':'PASS','artifacts':len(receipts),'full_new_stage_checks':total,'new_claim':cid+'@2'},indent=2))
