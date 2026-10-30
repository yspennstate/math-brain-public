from pathlib import Path
from datetime import datetime, timezone
import json, hashlib
ROOT=Path(__file__).resolve().parents[3]
RUN=Path(__file__).resolve().parents[1]
CAMP=ROOT.parents[1]
PROTO=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def write(p,s): p.write_text(s,encoding='utf-8',newline='\n')
def save(p,x): write(p,json.dumps(x,indent=2)+'\n')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
result=json.loads((RUN/'out/EXACT_CHECK.json').read_text(encoding='utf-8'))
assert result['status']=='PASS'
sources=[PROTO,CAMP/'BOARD.md',CAMP/'claude/B11/STREAM_NOTES.md',ROOT/'runs/20261022T211342Z-fleet03-A053-near-tensor-perturbations/TWO_QUERY_PROOF.md',CAMP/'agents/A052/runs/20261023T014825Z-fleet03-A052-critical-source-structure/RANK_PAIR_PROOF.md',CAMP/'agents/A051/runs/20261023T002518Z-fleet03-A051-near-extremizer-definition/REPORT.md',CAMP/'agents/A055/runs/20261022T233657Z-fleet03-A055-extremal-obstruction-referee/REPORT.md']
save(RUN/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p)} for p in sources])
cid='A053-THIRD-QUERY-ALL-POLICY-OBSTRUCTION'
statement='For every integer r>=7, the Boolean G_r in THIRD_QUERY_PROOF.md is one physical vertex edit of a triple-parity-coded seed of Fourier support distance at least 3, has odd negative count and no nontrivial Boolean tensor factorization, satisfies H(G_r)<=3 I(G_r), and admits an original three-query selector block with entropy decrement L3>(2r-3)2^(-2r) and influence debit Q3=3*2^(-2r)-6*2^(-6r-3). Thus L3/Q3 is unbounded. For every fixed K>=9 and r>=7 with 2r-3>3K, the complete three-query bank B3=L3-KQ3 is positive although its retained two-query prefix bank B2<-2^(-6r-4). In particular r16,K9 gives B3>2*2^(-32). This refutes the proposed all-policy third-query extension, not FEI or an existential critical-source selector.'
claims=[{
 'claim_id':cid,'version':1,'exact_statement':statement,
 'hypotheses':['Uniform binary cube, normalized Walsh transform, entropy in bits','Specified actual Boolean family and original selector-triple query, all original terminal reaches','The general-K prefix bound uses the preceding two-query theorem; K9 is also directly recomputed'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A053'],'proof_source':'THIRD_QUERY_PROOF.md',
 'proof_dependencies':['A053-ANCESTOR-PACKING-ALL-POLICY-TWO-QUERY-PAYMENT@1 for general-K negative prefix only; divergent local price proof is self-contained'],
 'review_records':[{'reviewer':'A053','kind':'author analytic proof and exact arithmetic verification','outcome':'PASS; independent review of new theorem pending'}],
 'status':'AUTHOR_CHECKED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['Unregistered proposal: extend all-policy two-query payment through a third query at a fixed rate, with earlier bank retained'],
 'first_unproved_line':'No gap claimed in the stated construction. Universal critical-source original-block selection with sufficient independent unused affine release remains open.',
 'next_consumers':['B11','A052','A090','A094','B20']}]
save(RUN/'CLAIMS.json',claims)
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B11','packet_id':'A053',
 'gap_id':'G-A053-CRITICAL-QUANTITATIVE-SEPARATION','attempt_id':'A053-stage18-third-query-boundary-rank-review',
 'method':'Bent-selector parity coding, point surgery, complete tree bank, exact Walsh and rational entropy certificates; independent rank-interface reconstruction',
 'mathematical_delta':'All-policy two-query payment cannot extend one query at any fixed rate. Tensor-prime point-edited distance-three seeds have unbounded third-block local price despite negative prefix bank; roots FEI3. A052 rank funding and specified local pair independently reconstructed.',
 'deliverable_status':'COMPLETE_SAVED_LOCAL; supervisor adoption and mirror pending',
 'mathematical_status':'RESTRICTED_ROUTE_OBSTRUCTION_AUTHOR_CHECKED; FULL_FEI_OPEN; UNIVERSAL_CRITICAL_SELECTOR_OPEN',
 'claim_versions_used':['A053-ANCESTOR-PACKING-ALL-POLICY-TWO-QUERY-PAYMENT@1','A052-RANK-RELEASE-ORIGINAL-PAIR-PAYMENT@1: reviewed interface, not construction dependency'],
 'claims_created_or_changed':[cid+'@1'],
 'source_artifacts':[str(p) for p in sources]+['THIRD_QUERY_PROOF.md','RANK_INTERFACE_REVIEW.md','out/EXACT_CHECK.json','out/FROZEN_SPEC.json','out/FROZEN_SPEC_V2.json'],
 'next_consumers':['B11','A052','A090','A094','B20'],
 'next_action':'Prove a critical-source third-query selection or independent-rank funding dichotomy retaining the same ancestor bank; A090/A094 review new boundary proof; A052 consume review.',
 'stagnant_substantive_attempts':0,
 'blockers':['Universal critical-source selector remains open','New theorem awaits independent review; mirror/adoption pending','Brain self-care degraded/unverified: stale owner model and state-of-mind context'],
 'packet_ids':['A053']}
save(RUN/'PROGRESS.json',progress)
(RUN/'PACKET_DELTA.json').write_bytes((RUN/'PROGRESS.json').read_bytes())
report="""# A053 stage18: first collision defeats all-policy payment

## exact target, quantifiers, hypotheses and units
Test extension of the preceding every-policy two-query payment through the first possible signed coefficient collision. Uniform cubes, actual Boolean signs, normalized Walsh transform, entropy in bits. All original terminal entropies and influence debits remain. The all-policy extension fails for every fixed rate; the roots themselves satisfy FEI(3). Full FEI remains OPEN.

## sources actually read, revisions and theorem locators
BOARD (02:33 UTC snapshot at initial read), B11 STREAM_NOTES v2 and own stage17 STATUS; protocol revision 2026-10-11-execution-v2. Prior TWO_QUERY_PROOF.md supplies the every-policy prefix theorem. A052 RANK_PAIR_PROOF.md sections1--5 was read whole and independently reconstructed in RANK_INTERFACE_REVIEW.md. Latest A051/A055 reports constrain criticality and SAME-bank scope; neither supplies a theorem dependency here. Campaign block-restriction and log-allocation sources supplied background: bent bad-selector coordinates are known. The contribution is their first third-query collision inside a point-edited distance-three seed, with old prefix credit retained. SOURCE_RECEIPTS.json binds source artifacts; earlier required campaign/paper baseline reads are not claimed as new work.

## complete derivation or exact first unsupported line
Complete proof: THIRD_QUERY_PROOF.md. A 2r-bit bent quadratic g and its zero-vertex edit g' form the selector h=(g,g'). Encode all 2r+1 inputs by disjoint physical parity triples, then edit physical vertex0. The n=6r+3-bit G has full Fourier support and odd negative count, hence no nontrivial Boolean tensor factorization. The seed has support distance>=3. Query the three original physical selector bits. Write d=2^(-2r), p=2^(-6r-3). Exact complete query debits are Q2=2d-4p and Q3=3d-6p.

All four prefix children and eight terminal children retain original reaches. Before the physical edit, selector spectral conditional entropy is at least (2r-2)d. A finite coupling argument bounds the full root-plus-weighted-terminal edit error by 2^(-3r)(90r+37)/8<d for r>=7. Hence L3>(2r-3)d and L3/Q3>(2r-3)/3. For any fixed K>=9 choose 2r-3>3K. The whole three-query bank is then positive although the old prefix bank is <-p/2. At r16,K9 the whole debt exceeds 2d. This retains the prior negative credit, rather than granting a fresh budget. However I(G)>=3r and H(G)<=6r+3 give H/I<=3: this is not a counterexample to FEI or to a criticality-dependent existential block rule.

First unsupported universal line: choose an original proper block on every least-dimensional positive fixed-K source whose UNUSED independent-rank child release pays the signed entropy decrement in the SAME ancestor bank. The displayed FEI3 family fails this critical eligibility hypothesis. Tensor primitivity alone is insufficient.

## executed validation with domain, arithmetic, commands and outputs
Frozen specifications preceded computation. Command: python -X utf8 runs/20261023T023627Z-fleet03-A053-near-tensor-perturbations/code/check_boundary.py.
Complete physical truth tables at r1,n9 and r2,n15; every Walsh coefficient compared with the derived signed spectrum; independent character-sum oracle for all512 n9 labels and sixteen frozen n15 labels; physical edge influences; seed support distances; all four actual prefix and eight actual terminal spectra. Compressed profiles r1..16 use exact multiplicities without enumerating the n99 truth table. The infinite-dimensional step is the separate analytic argument.

PASS: 101069 assertions, 7.344123 seconds. Integer transforms/edges, Fraction, rational atanh24 logarithm intervals. Serialized endpoints are rounded OUTWARD to denominator2^40; internal signs remain exact. V1 passed physical checks then failed displaying a fraction larger than Python's4300-digit limit. V1_FAILURE.json and check_boundary_v1.py preserve the failure; V2 changes serialization only and passes. A separate first attempt to write the finalizer failed Python parsing before creating any protocol files; the replacement finalizer uses a direct patch. Frozen memory estimate80MB; no large-memory job or background work. No formal-kernel certificate is claimed.

## proof dependencies and changed downstream conclusions
The general-K negative prefix uses the previous author-checked theorem; K9 prefix signs are independently recomputed directly. The divergent local price and FEI3 estimate are self-contained. No accepted registered theorem is refuted, and no change to the two-query theorem is needed. A052's finite-rank interface and specified original-pair payment were independently reconstructed: overlapping swaps cannot be added without rank independence. Ancillary affine-minimal/full-span source facts are outside the review, and are not needed for the reviewed local payment. Shared registry adoption is not claimed.

## one next mathematical action and independent reviewer
Change mechanism to criticality-dependent third-query selection or independent-rank release, retaining the SAME bank. A090/A094 are proposed reviewers of the new boundary proof; A052 is the consumer of the rank-interface reconstruction. No message was sent. The next lemma should exclude or fund the dangerous signed merge on a least-dimensional positive fixed-K witness.

## actual persistence receipts or precise save blocker
The four protocol files, proofs, review, code and outputs are saved locally. Required JSON field sets are checked; PACKET_DELTA is byte-identical to PROGRESS with packet_ids=[A053]. out/PERSISTENCE_RECEIPTS.json binds hashes and sizes. Supervisor copying and independent review remain pending. Shared registries, other agents' folders, brain memory and mirrors were not modified. All own numerical jobs exited. Brain self-care remains degraded/unverified because owner-model and state-of-mind sources are stale; personal-context reliability remains affected, and those sources were not used as mathematical evidence.

## Universal bridge
This stage moves C019 stopping-tree payment by closing the ALL-POLICIES third-query route negatively, even with the proven two-query credit and exact tensor primitivity. It also independently reconstructs the finite-rank lower-funding interface that prevents duplicate affine refunds. The remaining bridge is a universal critical-source selector with sufficient independent unused release and the complete original terminal bank. The next selection/rank dichotomy targets that unpaid universal step; extending bounds for this already-FEI3 class would not.
"""
write(RUN/'REPORT.md',report)
write(ROOT/'STATUS.md','STATE: Stage18 saved: all-policy third-query payment fails with old prefix bank retained;101069 exact checks PASS;roots FEI3;A052 rank/local-pair review reconstructed;FEI OPEN.\nNEXT: Critical-source third-query selection or independent-rank funding in SAME ancestor bank;A090/A094 review boundary proof.\n')
stamp=datetime.now(timezone.utc).isoformat()
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:
 f.write('\n'+stamp+' stage18: bent-selector parity code plus physical point surgery gives divergent third-query local price despite old negative prefix bank. Physical n9/n15 plus compressed r1..16:101069 exact checks PASS in7.344123s. V1 serialization failure preserved; outward dyadic endpoint output repaired it. Finalizer first write failed parsing before mutation; direct patch corrected it. A052 rank/local-pair reconstructed; ancillary affine-minimality outside review. New theorem pending independent review/mirror; FEI and critical selector OPEN. All numerical jobs exited.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:
 f.write('\nStage18 boundary: h=(bent g,g-zero-flip), all inputs encoded by parity triples, then edit physical0. Seed support distance>=3; odd negative count implies edited root tensor-prime. For d=2^-2r,p=2^-6r-3, selector Q3=3d-6p and L3>(2r-3)d for r>=7. Entire prefix bank stays<-p/2 at K>=9 but whole three-query bank>0 if2r-3>3K. Roots FEI3: only ALL-POLICIES payment fails, not critical existential selection. Edit error<=2^-3r(90r+37)/8<d. A052 refund ownership uses independent rank, not separate overlapping swaps. Serialize huge exact bounds by outward dyadic rounding; never use floating signs.\n')
proto=json.loads(PROTO.read_text(encoding='utf-8'))['required_per_run']
assert set(claims[0])==set(proto['claim_fields'])
assert set(progress)==set('packet_ids' if x.startswith('packet_ids ') else x for x in proto['progress_fields'])
assert all(x in report for x in proto['report_fields'])
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
receipts=[]
for p in sorted(RUN.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
  assert p.stat().st_size<20_000_000
  receipts.append({'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(RUN/'out/PERSISTENCE_RECEIPTS.json',{'schema':'PASS','compatibility_bytes':'IDENTICAL','files':receipts,'mirror':'not verified; supervisor pending'})
print(json.dumps({'saved':str(RUN),'schema':'PASS','files':len(receipts),'assertions':result['assertions']},indent=2))
