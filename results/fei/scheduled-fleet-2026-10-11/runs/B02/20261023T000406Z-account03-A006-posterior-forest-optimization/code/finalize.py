"""Persist stage artifacts; UTF-8 throughout; run only inside the A006 run."""
from pathlib import Path
import json, hashlib

run = Path(__file__).resolve().parent.parent
agent = run.parent.parent
base = agent.parent.parent
def read(p): return Path(p).read_text(encoding='utf-8')
def write(name, value): (run / name).write_text(value, encoding='utf-8')
def dump(name, value): write(name, json.dumps(value, indent=2, ensure_ascii=False)+'\n')
def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
source = base/'agents/A010/runs/20261022T231523Z-account03-A010-universal-residual-falsifier'
raw = json.loads(read(source/'CLAIMS.json'))
sources = raw if isinstance(raw,list) else raw['claims']
ids = ['A010-GENERIC-WIDTH-TWO-FOREST-MASS','A010-GROWING-DELETED-MATCHING-COMPLETE-COST']
selected = [next(c for c in sources if c['claim_id']==i) for i in ids]
for c in selected:
    h = hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
    assert h == c['statement_sha256'], (c['claim_id'], h)
check = json.loads(read(run/'out/CHECK.json'))
review = json.loads(read(run/'out/REVIEW.json'))
adversarial = json.loads(read(run/'out/ADVERSARIAL.json'))
assert all(x['status']=='PASS' for x in (check,review,adversarial))
assert review['matching_functions']==40 and review['distinct_canonical_histories']==4876
assert review['singleton_root_choices']==8310
dump('out/SOURCE_CLAIMS.json',selected)
write('REVIEW_A010.md', '''# Independent reconstruction of two A010 source claims

Verdict: HOLDS_NO_MATHEMATICAL_REPAIR for A010-GENERIC-WIDTH-TWO-FOREST-MASS@1 and A010-GROWING-DELETED-MATCHING-COMPLETE-COST@1, at the unchanged canonical statement-plus-hypotheses hashes copied in out/SOURCE_CLAIMS.json. Reviewer A006 supplies no repair to these versions. This reconstruction used direct physical character sums and a separately implemented queue, without importing A010 or earlier A006 helpers. A010's references to prior A006 work do not constitute an independent review of this stage's new theorem.

For the generic claim, assign every selected coordinate to an incident edge, so owned blocks have size one or two. In the directed incidence graph select one root in each source strongly connected component, and a spanning forest reachable from those roots. Order roots and children canonically, and assign each child to an owned coordinate contained in its gate. Execute the resulting queue once. Every gate is visited exactly once and the disjoint owned blocks union to the selected Fourier set. Thus this is an actual run, not a description counted repeatedly. With N used gates, R roots, sizes s, child counts c, total children N-R, its exact conditioned mass is

    lambda^N 4^-R / D * product [s(s+1) binom(2,s) (c+1)(c+2) binom(s+c-1,c)]^-1.

The singleton/two-element subset denominator is at most 6; the composition denominator is at most c+1; and (c+1)^2(c+2)<=2*6^c for every integer c>=0. The product is at least (lambda/72)^N(3/2)^R/D, hence at least (lambda/72)^|A|/D when 0<lambda<=1. This includes root exclusions: the full independent root-set probability, conditioned nonempty, is (lambda/4)^R/D. The weight packing rows ensure legality. For a set entirely on one side, distinct choices of one incident gate per coordinate give distinct actual singleton-root sets. Enumerating them gives exactly product deg(i)/(32b)^|A|D with fixed lambda=1/b; no permutation factor is inserted.

The independent queue checker visits every eligible nonempty coordinate set in 15 nonempty 2x2 surviving graphs and five overlapping path/cycle/component fixtures. It reconstructs actual execution, exact mass, root exclusions, all count/composition/label factors, and deduplicates singleton root sets. out/REVIEW.json records 4,876 canonical histories, 8,310 singleton choices and 81,047 assertions. Finite checks corroborate the all-parameter construction; they do not replace its proof.

For the matching claim, let u=2^-a, t=2^-b and r be the number of deleted matching edges with exactly one endpoint in U union V. Direct expansion of the actual Boolean truth table gives, for nonempty U union V,

    fhat(U,V)=-2[u 1_(V empty)+t 1_(U empty)+ut(k-1-2r)].

The exceptional set consists of exactly the k assignments with one matched pair active. Therefore q=u+t+(k-1)ut and I=I0+2k(a+b-4)ut. Summing the exact expression over the right-only and mixed sectors gives the source's stated R,M formulas. Its same-reference singleton and generic forest bounds imply C<=v log D+log72 I+R log(b/a)+M log b. The physical implicant boundary bound pays v log D by 9I/8; the source's uniform estimates pay R log(b/a) by 50I/9 and M log b by 9I/2. With log72<25/4 this gives C<1255I/72<18I. No changed reference or optimized toy law is used. The direct character-sum checker verifies all 40 matching functions for 2<=a<=b<=5, 0<=k<=a, their exact moments and physical influences, as well as the edge implicant boundary inequality. The universal inequalities are established by the source's analytic argument; finite enumeration alone does not certify them.

Scope: these are two reviewed source claims, not acceptance of every A010 claim or of full FEI. The current new degree-two extension remains awaiting another agent's review. The previous A006 stage's allegation of bad A010 hash metadata is withdrawn: its recorded hash correctly uses canonical JSON of statement and hypotheses. out/HASH_CONVENTION_CORRECTION.json pins the builder and both differently typed digests. Earlier immutable runs are preserved.
''')

statement = ('For every labelled bipartite H of maximum degree at most two on sides 2<=a<=b, '
 'the positive edge DNF for G=K_ab minus H, with its original surviving edge primes, both endpoint orders, '
 'pi=1/4 and fixed lambda_e=1/b, has complete nonempty posterior all-partition forest cost C<42 I(f) '
 'when G is nonempty; if a>=4, C<(283/8)I(f)<36I(f). The empty G case is constant and handled separately. '
 'More generally for any G on 4<=a<=b with every left degree>=b/2 and right degree>=a/2, the same reference '
 'satisfies C<(91/8)I(f)+2J log2 b, where J is the total physical flip influence of the indicator of '
 'assignments having nonempty active sets on both sides and no active surviving G edge.')
hypotheses = ['Uniform independent physical Boolean bits; logarithms and entropy in bits.',
 'Actual partition-forest runs; posterior witness entropy subtracted; descriptions of one run not counted separately.',
 'Nonempty original surviving width-two prime table with both endpoint orders; lambda_e=1/b satisfies packing.',
 'Degree-two conclusion requires max degree(H)<=2; conditional dense-graph transfer has only the stated minimum-degree hypotheses.']
claim = dict(claim_id='A006-DELETED-DEGREE-TWO-COMPLETE-POSTERIOR-COST',version=1,
 exact_statement=statement,hypotheses=hypotheses,
 statement_sha256=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest(),
 contributors=['A006'],proof_source=['DELETED_DEGREE_TWO.md sections 1-5','REVIEW_A010.md','code/check.py','out/CHECK.json'],
 proof_dependencies=[ids[0]+'@1 (independently reconstructed locally; unchanged source hash in out/SOURCE_CLAIMS.json)'],
 review_records=[{'reviewer':'A006','kind':'author proof and exact validation; not independent acceptance','result':'PASS; formal compiler not started after admission hold','artifacts':['out/CHECK.json','out/REVIEW.json','out/ADVERSARIAL.json','out/LEAN_ADMISSION.json']}],
 status='AUTHOR_PROOF_EXACT_CHECKS_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=[],first_unproved_line=None,
 next_consumers=['B02 Claude lead','A010','A007','B20'])
dump('CLAIMS.json',[claim])
next_action = ('A010 or the B02 lead independently reconstruct the degree-two theorem and dense transfer, then test whether '
 'the physical defect-boundary charge J log2 b can be influence-paid for overlapping deletions of unbounded degree, '
 'or replace it by a sharper joint spectral-sector charge without resetting the original reference.')
progress = dict(protocol_revision='2026-10-11-execution-v2',run_id=run.name,stream='B02',packet_id='A006',
 gap_id='G-J-COST',attempt_id='A006-stage8-degree-two-defect-Dirichlet-transfer',
 method='Actual singleton-root posterior sums plus generic forest mass; physical defect Dirichlet energy and joint-sector perturbation.',
 mathematical_delta='Complete original-reference cost<42I for all deleted maximum-degree-two bipartite graphs; <36I if a>=4. General half-dense transfer C<91I/8+2J log2 b. Two source claims reconstructed; prior raw-hash diagnosis corrected.',
 deliverable_status='COMPLETE_LOCAL_PENDING_SUPERVISOR_COPY',
 mathematical_status='SCOPED_AUTHOR_PROOF; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 claim_versions_used=[c['claim_id']+'@'+str(c['version']) for c in selected],
 claims_created_or_changed=[claim['claim_id']+'@1'],
 source_artifacts=['DELETED_DEGREE_TWO.md','REVIEW_A010.md','out/SOURCE_CLAIMS.json','out/HASH_CONVENTION_CORRECTION.json','out/CHECK.json','out/REVIEW.json','out/ADVERSARIAL.json'],
 next_consumers=claim['next_consumers'],next_action=next_action,stagnant_substantive_attempts=0,
 blockers=['Full FEI: no universal payment of the defect spectral occupation or boundary charge.',
 'New theorem awaits independent agent review; no mirror/publication receipt is claimed.',
 'Lean compilation not admitted: memok exited 1; formal source unverified.',
 'Brain wake degraded: stale owner-model/state-of-mind and attachment timeouts; those personal notes remain unverified.'],packet_ids=['A006'])
dump('PROGRESS.json',progress)
write('PACKET_DELTA.json',read(run/'PROGRESS.json'))

write('REPORT.md', '''# A006 stage 8: overlapping deletions with the original posterior reference

## exact target, quantifiers, hypotheses and units

For every 2<=a<=b and every labelled bipartite deleted graph H with maximum degree at most two, bound the COMPLETE posterior forest cost of the actual Boolean edge DNF G=K_ab minus H. The proved bound is C<42I; when a>=4, C<(283/8)I<36I. The reference keeps all original surviving primes, both endpoint orders, pi=1/4, one fixed lambda=1/b, and all actual partition runs. Entropy is in bits. The empty surviving graph is constant and treated separately. A reusable broader result for half-dense G on 4<=a<=b is C<(91/8)I+2J log2 b. This is a restricted all-parameter proof and a conditional transfer, not a proof or disproof of full FEI. The exact theorem and hypotheses are in CLAIMS.json and DELETED_DEGREE_TWO.md.

## sources actually read, revisions and theorem locators

At this stage: BOARD.md, B02 STREAM_NOTES.md, own rolling files, machine-wide instructions, protocol revision 2026-10-11-execution-v2, A010 run 20261022T231523Z REPORT.md/GROWING_MATCHING.md/CLAIMS.json and relevant helper/finalizer conventions; A008 run 20261021T234312Z REPORT.md/ROOT_PAYMENT.md and hash convention; A010 earlier run 20261021T161852Z code/finalize.py hash builder. The campaign's older end date in the protocol is superseded by the user's explicit 2026-10-23 deadline. Campaign registries, plans, context papers and earlier stages were inherited from earlier source reads; this report does not assert fresh full-paper rereads. Current source claims and their unchanged canonical hashes are pinned in out/SOURCE_CLAIMS.json; bytes read for main dependencies are pinned in out/SOURCE_PINS.json.

## complete derivation or exact first unsupported line

DELETED_DEGREE_TWO.md supplies the full derivation. Actual singleton-root choices sum exactly to product deg(i)/(32b)^|A|D, with no duplicate root sets or factorial. Generic SCC-rooted forest events supply the remaining mixed-sector mass. The root normalization is paid by <9I/8 at the SAME reference. The physical defect event E has exactly h+w_L+w_R+c4<=9a/2 configurations. Its boundary influence J equals the Fourier Dirichlet energy of delta=-2*1_E. Sector perturbation uses the single budget J_R+J_M<=J, rather than spending J twice. The pivotal lower bound I>=(3/2)a2^-a pays J log b by 12I. The constants are 283/8 for a>=4 and 2963/72 for a=2,3,b>=4; b<=3 costs <75I/8. Before the degree-two count is used, the proof yields the broader half-dense transfer C<(91/8)I+2J log b.

For actual posterior optimization, inf_eta[expected negative log run mass minus H(eta)]=-log Q(A), attained by the posterior q(run)/Q(A). Every event used is an actual run. Restricting to selected legal events gives an upper bound on the complete all-run cost, never a lower certificate for a larger family. This also upper-bounds the joint variational infimum containing this legal weight vector.

First unsupported universal line: paying J log b (or a sharper joint spectral occupation replacement) by an absolute constant times I for unbounded deleted degree or arbitrary prime tables. The degree-two exception count cannot be dropped: the saved outside-domain examples violate it. No full conjecture claim follows from these computations.

## executed validation with domain, arithmetic, commands and outputs

Specifications were frozen before execution in FROZEN_SPEC.json, REVIEW_SPEC.json and ADVERSARIAL_SPEC.json. Pilot: 330 functions, 329 nonconstant, 18,784 physical inputs, 22,116 assertions, PASS in 0.579260 seconds. Full census: all 8,875 labelled maximum-degree-two deleted graphs with 2<=a<=b<=4 (no symmetry reduction), plus six specified larger path/cycle/component fixtures: 8,881 functions, 8,880 nonconstant, 2,056,480 physical inputs and 2,180,788 assertions, PASS in 20.828496 seconds. Integer Walsh transforms and physical flips check the actual Boolean spectra, defect counts, influences, exact Dirichlet identity and sector inequalities. Rational atanh remainder intervals rigorously enclose logarithms; no floating sign is used. Reproduce with python -X utf8 code/check.py using its frozen pilot/full CLI documented in that source. Outputs are out/CHECK.json, out/CHECK_ROWS.jsonl and pilot equivalents.

Independent source reconstruction: python -X utf8 code/review.py; 40 matching functions by direct character sums, 20 queue graphs, 4,876 canonical histories, 8,310 distinct singleton root choices and 81,047 assertions, PASS in 7.733031 seconds. out/REVIEW.json and REVIEW_A010.md record the arithmetic and all-parameter proof reconstruction. The implementation imports no author helpers. Two outside-domain examples run via python -X utf8 code/adversarial.py: PASS, 12 assertions; the defect counts 7 and 98 show precisely where the degree-two count fails. The latter also verifies the relevant joint-sector identity under half-density; it is not an exact enumeration of the complete forest reference.

All jobs are small and bounded; no dimension was automatically raised. The memory guard exited 1 (1.3 GB physical free versus 4.0 GB required), so no Lean compiler was launched. code/JointEnergy.lean is unverified formal source, with the hold recorded in out/LEAN_ADMISSION.json. No formal acceptance is claimed. Research computations have finished; no research job remains running.

## proof dependencies and changed downstream conclusions

A010-GENERIC-WIDTH-TWO-FOREST-MASS@1 and A010-GROWING-DELETED-MATCHING-COMPLETE-COST@1 have been reconstructed without mathematical repair, at their original canonical hashes; source statements are copied byte-faithfully as JSON values. The new theorem uses the generic mass claim; the matching theorem is reviewed context, not a circular proof dependency. The width-two signed root payment is rederived directly from the physical implicant-fiber cut, not accepted merely because of a source hash. These two reviews reduce source-review debt; the new degree-two theorem still needs independent review.

Correction to A006 stage 7: the raw-text SHA mismatch was mistakenly classified as invalid A010 metadata. The original builder hashes canonical JSON containing both statement and hypotheses, and its recorded digest is valid. out/HASH_CONVENTION_CORRECTION.json pins this distinction. This run supersedes that diagnosis; the earlier run and all other agents' files remain unchanged. Downstream users should retain the source claim version and canonical digest, not perform a metadata repair.

## one next mathematical action and independent reviewer

Ask existing A010 or the B02 lead to independently reconstruct equations (4)--(16), especially the physical boundary normalization and the single sector-energy budget. Then address the universal bottleneck by paying the dense-transfer J log b term or replacing it with a sharper spectral charge for growing-degree overlaps, retaining the same original reference. These named consumers are handoff targets; no message has been sent and no review acceptance is implied.

## actual persistence receipts or precise save blocker

All artifacts are saved locally in this run and the three A006 rolling files are current. out/PERSISTENCE.json records UTF-8 readback, schema validation, matching progress copies, file-size limits and SHA-256 receipts. No remote mirror, supervisor ingestion or downstream mathematical use is asserted. Administrative brain self-care is degraded: the fresh wake failed on attachment timeouts and stale owner-model/state-of-mind sources; those personal notes remain unverified. Mathematical conclusions here use the explicitly named current mathematical sources and saved exact checks. Nothing in the failed wake was used as proof evidence.

## Universal bridge

C020 whole-set witness cost advances from disjoint deleted matching edges to every overlapping deleted path/cycle union, with complete same-prime posterior cost <42I (and <36I for a>=4), and exposes the more general half-dense transfer C<(91/8)I+2J log b. Actual-run posterior entropy and the original normalizer are retained. The remaining universal bridge is an influence payment for the defect's joint spectral occupation beyond bounded deleted degree, not another root estimate. Studying that exact unpaid charge is the shortest continuation toward full FEI because it removes the present structural hypothesis within the existing whole-set coding mechanism; another isolated low-degree census would not remove it.
''')

pins = [base/'BOARD.md',base/'claude/B02/STREAM_NOTES.md',
 source/'GROWING_MATCHING.md',source/'CLAIMS.json',
 base/'agents/A008/runs/20261021T234312Z-account03-A008-gate-label-compression/ROOT_PAYMENT.md',
 Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
dump('out/SOURCE_PINS.json',[{'path':str(p),'sha256':digest(p)} for p in pins])
status = ('STATE: Stage8 saved: complete original-reference cost<42I for every maximum-degree-two deleted bipartite graph (<36I if a>=4); exact checks PASS; full FEI OPEN.\n'
 'NEXT: A010/B02 independent review, then pay or replace the dense-transfer 2J log2 b charge for growing-degree overlaps without a reference reset.\n')
(agent/'STATUS.md').write_text(status,encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n2026-10-23 stage8 completed: all-parameter degree-two deletion proof (<42I, a>=4 <36I); half-dense transfer <91I/8+2Jlog b. Exact census 8,881 functions / 2,180,788 assertions PASS; source reconstruction 4,876 queue histories / 8,310 singleton choices / 81,047 assertions PASS; two out-of-domain tests PASS. Corrected stage7 false metadata diagnosis: canonical source hash valid. memok exit1, Lean not started. New theorem awaits independent review; full FEI open; no research jobs left running.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\n2026-10-23: For H max-degree2, E={both active sides nonempty,no surviving edge} has exactly h+w_L+w_R+c4<=9a/2 points. Its physical indicator influence J equals Fourier energy of -2*1_E; sector errors share J_R+J_M<=J. This pays complete same-reference cost<42I, <283I/8 when a>=4. For arbitrary half-dense bipartite G, retain C<91I/8+2Jlog2 b, with J still unpaid. Count fails outside degree2 (deleted three-star:7 points; two deletedK33:98). Preserve actual root sets and fixed root order; singleton choices sum productdeg/(32b)^sD without factorial. Source-hash correction supersedes earlier A006 diagnosis: A010 builder hashes canonical JSON of statement plus hypotheses, not raw statement text; its source metadata was valid. New result has author proof/exact checks, independent review pending; no Lean compiler acceptance.\n')

protocol = json.loads(read(pins[-1]))
assert set(progress)==set(x.split(' (')[0] for x in protocol['required_per_run']['progress_fields'])
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
report=read(run/'REPORT.md')
assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
assert report.rsplit('## Universal bridge',1)[1].strip()
receipts=[]
for p in sorted(run.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  assert p.stat().st_size<20*1024*1024, p
  if p.suffix in ('.json','.jsonl','.md','.py','.lean'): read(p)
  receipts.append({'path':str(p.relative_to(run)),'bytes':p.stat().st_size,'sha256':digest(p)})
dump('out/PERSISTENCE.json',{'status':'PASS_LOCAL_READBACK','claim_schema':'PASS','progress_schema':'PASS','compatibility_copy':'IDENTICAL','formal_status':'UNVERIFIED_SOURCE_ONLY','full_FEI':'OPEN','remote_mirror':'NOT_CHECKED','files':receipts,'rolling':[{'path':str(p),'sha256':digest(p)} for p in [agent/'STATUS.md',agent/'WORKLOG.md',agent/'LEARNED.md']]})
print(json.dumps({'status':'SAVED_AND_VALIDATED','run':run.name,'claim':claim['claim_id'],'files':len(receipts),'full_FEI':'OPEN'}))
