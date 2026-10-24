import json, hashlib, copy
from pathlib import Path
from datetime import datetime, timezone

run = Path(__file__).resolve().parents[1]
agent = run.parents[1]
root = agent.parents[1]
campaign = Path('~/mop_fei100/reports/fei-2026-10-11')
a8 = root/'agents/A008/runs/20261014T050954Z-account05-A008-gate-label-compression'
a10 = root/'agents/A010/runs/20261014T031741Z-account05-A010-universal-residual-falsifier'
a6 = root/'agents/A006/runs/20261014T035304Z-account05-A006-posterior-forest-optimization'
now = datetime.now(timezone.utc).isoformat()
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name, obj): (run/name).write_text(json.dumps(obj, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
def statement_hash(c):
    return hashlib.sha256(json.dumps({'statement':c['exact_statement'], 'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
protocol = json.loads((campaign/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
baseline = campaign/'source_material/reductions/paper/forests.tex'
sources = [campaign/'EXECUTION_PROTOCOL.json', root/'BOARD.md', root/'claude/B02/STREAM_NOTES.md', baseline, a8/'REPORT.md', a8/'CONNECTED_SCALES.md', a8/'CLAIMS.json', a10/'REPORT.md', a6/'JOINT_EDGE_SLICE.md', a6/'ROOT_LAW_RELAXATION.md']
save('SOURCE_RECEIPTS.json', [{'path':str(p), 'sha256':digest(p), 'bytes':p.stat().st_size} for p in sources])
baseline_dep = {'source':str(baseline),'sha256':digest(baseline),'locators':['original conditioned queue','eq:forestcost','eq:forestconditioning','eq:foresttarget'],'status':'SOURCE_BASELINE_RECONSTRUCTED; NO UNIVERSAL PAYMENT ASSUMED'}
claim = {
 'claim_id':'A009-ARBITRARY-CORE-PRIVATE-LEAF-COMPLETE-PAYMENT','version':1,
 'exact_statement':'For every finite simple core graph H on r>=1 hubs, including isolated hubs, and every integer vector m_i>=1, attach m_i degree-one private leaves to hub i and retain all core edges. For the uniform Boolean positive edge DNF f_G, fix precisely its positive edge primes, both endpoint orders, rarity pi=1/4, private-edge weights lambda=1/(2m_i) and core-edge weights lambda_ij=1/[2 max(d_H(i),d_H(j))]. These strictly positive weights satisfy every coordinate packing constraint. In the original conditioned forest queue, the private-block star event family has exact nonempty output subprobability Q_PL(A)=product_i U_(h_i)(t_i)/D, D=product_all_edges(1+lambda_e/4)-1, U_0(t)=(lambda_private/32)^t, U_1(0)=1/64, U_1(t)=t! lambda_private^t/[24*8^(t-1)*t^2*(t+1)] for t>=1. It is positive on every nonempty A and its complete nonempty spectral cross-entropy C_PL=sum_(A nonempty) fhat_G(A)^2*(-log2 Q_PL(A)) satisfies C_PL<=[log2(96)+9/4+9/(8 ln2)]I(f_G)<(843/80)I(f_G)<11I(f_G). All core-gate absent-root, subset, count, attachment and chronology factors are retained. This proves a dimension-independent complete reference payment on arbitrary cores with private leaves; it asserts no universal graph payment, optimal weights, or free transfer to the original core function.',
 'hypotheses':['Uniform independent physical signs; entropy and costs in bits','Finite positive simple graph edge DNF; every hub has at least one genuine degree-one private leaf','Same full prime table and both endpoint orders fixed before the Fourier set is sampled','Original once-per-gate source-SCC conditioned queue and ideal reference costs; no free prefix rounding','Expected cost uses the actual Boolean squared Fourier spectrum and physical total influence'],
 'statement_sha256':'','contributors':['A009'],
 'proof_source':{'path':str(run/'PRIVATE_LEAF_PAYMENT.md'),'code':[str(run/'code/check.py'),str(run/'code/verify.py')],'certificates':[str(run/'out/CHECK.json'),str(run/'out/VERIFY.json')]},
 'proof_dependencies':[baseline_dep],
 'review_records':[{'reviewer':'A009','verdict':'AUTHOR_ANALYTIC_PROOF_AND_SEPARATE_QUEUE_IMPLEMENTATION_CHECK; NOT INDEPENDENT_AGENT_ACCEPTANCE','method':'Pure Python original Bernoulli conditioning and chronological queue replay independent of FWHT checker; 22392 distinct traces; physical payment proved for all dimensions','reviewer_supplied_substantive_repair':False}],
 'status':'ANALYTICALLY_PROVED_EXACT_CHECKED_PENDING_INDEPENDENT_AGENT_REVIEW','supersedes':[],'refutes':[],
 'first_unproved_line':None,'next_consumers':['A006','A008','A010','A014','A086','B02','B20']}
claim['statement_sha256'] = statement_hash(claim)
review = copy.deepcopy(next(c for c in json.loads((a8/'CLAIMS.json').read_text(encoding='utf-8-sig')) if c['claim_id']=='A008-CONNECTED-GRAPH-TWO-SCALE-QUANTIFIER-SEPARATION'))
assert statement_hash(review)==review['statement_sha256']=='cf0f06a75dabf85738b3cbfcfabc9142aa5cbbb9c62add74dfe300bcc59321f5'
review['review_records'].append({'reviewer':'A009','verdict':'HOLDS_AT_WHOLE_ORIGINAL_SCOPE_NO_REPAIR','proof_source':str(run/'REVIEW_CONNECTED.md'),'validation':str(run/'out/VERIFY.json'),'method':'Independent full all-m physical spectrum, uniform-scale lower bound, needed complete/surrogate guard and sharper maximal-matching repair reconstructed directly; finite character-sum checks supplement the analytic proof','reviewer_supplied_substantive_repair':False,'timestamp_utc':now})
review['status']='WHOLE_INDEPENDENT_RECONSTRUCTION_BY_A009_LOCAL_ADOPTION_PENDING'
save('CLAIMS.json',[claim,review])
next_action='A006/A010 replace the private-leaf conditional payment and disjoint-block numerator on one genuinely shared-neighbor or leafless incidence, retaining the same original prime reference, global weights, full normalizer and true Boolean spectrum; A008/A086 independently reconstruct the new whole private-leaf theorem.'
progress = {
 'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B02','packet_id':'A009','gap_id':'G-J-COST','attempt_id':'A009-private-leaf-core-payment-v1',
 'method':'Explicit positive global fractional incidence vector; actual chronological private-block forest summation; exact conditional-false-event influence payment; independent whole connected-scale review',
 'mathematical_delta':'Arbitrary core graphs with arbitrary positive private-leaf counts have complete same-prime reference cost <11I in all dimensions, including one leaf per hub and unbounded core degree. 1098 frozen actual Boolean functions and 22392 original queue traces pass exact checks. A008 connected two-scale claim wholly reconstructed without repair.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS_PENDING_SUPERVISOR_COPY','mathematical_status':'PRIVATE_LEAF_CLASS_COMPLETE_PAYMENT_PROVED; GENERAL_GRAPH_PI_J_AND_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':review['claim_id'],'version':review['version'],'statement_sha256':review['statement_sha256'],'use':'Independent review and motivation, not a premise of new private-leaf proof'}],
 'claims_created_or_changed':[claim['claim_id']+'@1',review['claim_id']+'@1: A009 whole independent review'],
 'source_artifacts':['REPORT.md','CLAIMS.json','PRIVATE_LEAF_PAYMENT.md','REVIEW_CONNECTED.md','SOURCE_RECEIPTS.json','FROZEN_SPEC.json','VERIFY_SPEC.json','code/check.py','code/verify.py','out/PILOT.json','out/CHECK.json','out/VERIFY.json'],
 'next_consumers':['A006','A008','A010','A014','A086','B02','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Shared or missing private neighbors have no proved replacement for conditional-false-event label payment and disjoint private-block queue mass.','Independent-agent acceptance of the new theorem and supervisor mirror verification remain unobserved.'], 'packet_ids':['A009']}
save('PROGRESS.json',progress); save('PACKET_DELTA.json',progress)
report = '''# A009: complete fractional-incidence payment with arbitrary cores

## exact target, quantifiers, hypotheses and units

For every finite simple graph H on r>=1 hubs and every m_i>=1, attach m_i private degree-one leaves at each hub, retaining all core edges. Prove a complete nonempty reference cross-entropy bound on the actual uniform Boolean edge DNF, in bits, using one global positive packing-feasible vector on precisely the original primes. The result is C_PL <= [log2 96+9/4+9/(8 ln2)] I < (843/80) I <11I. Core degree, core density, hub count and unequal leaf counts are unrestricted. This is a class theorem beyond bounded-read formulas, not a universal FEI solution or a global-weight optimality assertion.

## sources actually read, revisions and theorem locators

The execution protocol is 2026-10-11-execution-v2. BOARD.md snapshot 2026-10-14 05:41 UTC, the B02 lead's v2 notes (2026-10-11 23:35), and the preceding A009 STATUS were read before choosing the new mechanism. The original forests.tex baseline (sha256 d2314f2c9606a9f4b68f3f0c8a3406aa95f24647a3487e35c5b73e50bf03703a) supplies the original queue, eq:forestcost, eq:forestconditioning and eq:foresttarget definitions; its size/subset probabilities were read directly. New source-bound inputs are A010 stage4 REPORT (uniform-scale failure versus the infimum), A008 stage5 REPORT, CONNECTED_SCALES and CLAIMS (connected broom and same-prime repair), and A006 stage5 JOINT_EDGE_SLICE and ROOT_LAW_RELAXATION. A006 stage5 REPORT was absent when read; its prose files are advisory and no new A006 claim is used as a premise. SOURCE_RECEIPTS.json pins the bytes actually consumed. Prior baseline reading is inherited, not claimed to be newly re-executed wholesale.

## complete derivation or exact first unsupported line

PRIVATE_LEAF_PAYMENT.md contains the full proof and all-dimensional inequalities. Each private edge at hub i receives 1/(2m_i), and each core edge ij receives 1/[2 max(d_H(i),d_H(j))]. Hub incidence is at most one and leaf incidence at most one half. The actual chosen events use private gates; every unused core gate remains in the nonempty-root normalizer D. Exact chronological stars give block numerators U_0(t)=(1/(64m))^t, U_1(0)=1/64 and U_1(t)=t! (1/(2m))^t/[24*8^(t-1)*t^2*(t+1)]. These imply Q_PL(A)>=D^-1 96^-|A| product_i m_i^-t_i.

Write q=Pr(false), a_i=Pr(false,hub_i negative), b_i=Pr(false,hub_i positive). Genuine private leaves give b_i<=2^-m_i a_i, Inf_hub_i=2(a_i-b_i)>=a_i and >=2q/3, and each leaf has influence 2b_i. Thus all private label charges sum to at most (9/4) I. Total weight is at most 3r/4; v=4q(1-q) and I>=2rq/3 pay v log2 D by 9I/(8 ln2), including its negative sign when D<1. Adding the log2(96) I pointwise cost proves the displayed bound. Rational inequalities log2 96<33/5 and ln2>2/3 yield 843/80<11. The first unsupported extension is a same-reference replacement for the block numerator and b_i<=2^-m_i a_i when a vertex has zero private leaves or its neighbors are shared. Attaching leaves changes f and supplies no free transfer to the original core.

REVIEW_CONNECTED.md reconstructs the whole unchanged A008-CONNECTED-GRAPH-TWO-SCALE-QUANTIFIER-SEPARATION v1, hash cf0f06a75dabf85738b3cbfcfabc9142aa5cbbb9c62add74dfe300bcc59321f5: influence and singleton spectral mass, divergent uniform-scale complete/surrogate cost, exact repaired normalizer, and its sharper C_MS<(53/5)I for all m>=2. Verdict HOLDS without repair. Its needed A010 guard and A006 mass lower bound are directly reconstructed; no whole review of their additional independent claims is asserted.

## executed validation with domain, arithmetic, commands and outputs

Both searches were frozen in FROZEN_SPEC.json and VERIFY_SPEC.json before execution. From this run directory the completed commands are `python -X utf8 code/check.py --pilot`, `python -X utf8 code/check.py`, and `python -X utf8 code/verify.py`. Pilot: 10 functions, 300 truth inputs, 4677 assertions, 0.0515 seconds. Full: every labelled core on 1..4 hubs with private counts in {1,2}, no symmetry reduction, exactly 1098 functions and 1,341,228 truth inputs, maximum dimension 12; 72325 assertions, 4.3841 seconds. Scalar inequalities were also checked through m=64. Full physical signs, integer FWHT, exact Fraction influence identities and rational logarithm enclosures check the actual complete cost. The maximum displayed ratio was 5.77498; the rigorous decision uses enclosing rationals, never this display.

Separate pure-Python replay: all cores on 1..3 hubs with counts {1,2}, plus single hubs with 3 and 4 leaves, 76 functions, 22392 distinct actual queue traces; 402460 assertions, 3.2800 seconds. It starts from every present/absent Bernoulli root factor, divides by exact root-conditioning probability, executes chronological queues, checks ownership and deduplicates traces. Five broom functions m=2..6 are independently checked by direct Walsh character sums. Total successful assertions across the three jobs: 479462. out/PILOT.json, out/CHECK.json and out/VERIFY.json record outcomes; partial JSONL rows were saved during the search. Estimated memory was 120 MB and 80 MB, below the memok trigger, with no background jobs or automatic dimension increases. Exact finite checks supplement the analytic all-dimensional proof.

## proof dependencies and changed downstream conclusions

The new theorem depends on the original conditioned queue definitions and elementary graph/probability identities, not on a claimed universal payment or unreviewed joint-optimization relaxation. Its positive weights and full expectation provide an explicit same-reference certificate on a meaningful unbounded-read family. Arbitrary densely connected cores are allowed even when every hub has only one private leaf; rarity of a defect tail is unnecessary. Unused core gates are paid in D, so this is not a sampled-set table selector. A008's connected-scale separation is independently accepted locally at its original whole scope. The new A009 claim is author-proved and exact-checked but awaits independent-agent review. Full FEI and general-graph PI-J remain OPEN.

## one next mathematical action and independent reviewer

NEXT_ACTION

The shortest useful extension replaces the two private-neighbor payment steps on one genuine overlap while retaining all actual queue factors. A008/A086 are requested consumers for whole-claim reconstruction; no message was sent and no acceptance or downstream adoption is presumed.

## actual persistence receipts or precise save blocker

The four required protocol files, both proof/review notes, frozen specifications, code and outputs are saved locally in this unique run. SOURCE_RECEIPTS.json pins external read-only inputs; out/PERSISTENCE_RECEIPTS.json records local SHA256 and size readback after saving. STATUS.md has exactly two current lines; WORKLOG.md appends this stage and LEARNED.md records the all-dimensional statement and failed universal extension. PROGRESS and PACKET_DELTA are identical. No files outside A009 were written. Supervisor copying, mirror verification and public release are unobserved; there is no local save blocker.

## Universal bridge

This stage moves C020 whole-set witness cost / B02 PI-J from finite optimized graph instances and disconnected or broom repairs to a proved complete cost <11I for every arbitrary core with at least one private leaf at every hub. The entire root, label, subset, child-count, attachment, chronology and conditioning ledger is paid under the true spectrum using a single global feasible vector. What remains is a payment and witness numerator for shared or missing private neighbors; neither a selector nor attaching new leaves closes that gap. NEXT tests a same-reference replacement for those exact two private-neighbor steps on one overlap, the shortest route toward arbitrary graph PI-J and ultimately full FEI rather than another isolated class calibration.
'''.replace('NEXT_ACTION',next_action)
(run/'REPORT.md').write_text(report,encoding='utf-8')
(agent/'STATUS.md').write_text('STATE: A009 stage5 complete: arbitrary core with m_i>=1 private leaves has complete same-prime cost <11I; 479462 checks; A008 connected two-scale whole HOLDS; full FEI OPEN.\nNEXT: Replace private-neighbor conditional payment and block queue numerator on one shared/leafless incidence; A008/A086 review whole theorem.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+now+' | Stage5 '+run.name+': read board/lead/status and new connected-scale results. Explicit full-prime global weights plus exact private-block stars pay arbitrary-core expected cost <11I for all positive private-leaf counts. Frozen 1098 Boolean cases, independent 22392 queue traces, 479462 total assertions pass. Whole A008 connected separation reconstructed without repair. Missing A006 stage5 report not a premise. Shared/leafless neighbors remain the first unpaid extension; independent-agent review and supervisor adoption pending.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n'+now+' | Arbitrary-core/private-leaf payment: weights private 1/(2m_i), core 1/[2max(d_i,d_j)] are globally feasible. Private-only selected traces still pay ALL core absent roots in D. Complete cross-entropy <=[log2 96+9/4+9/(8ln2)]I<843I/80<11I. On false events a_i,b_i, genuine private leaves imply b_i<=2^-m_i a_i, hub influence2(a_i-b_i)>=2q/3, each leaf influence2b_i; label sum <=9I/4 and normalizer<=9I/(8ln2). No small-tail assumption: m_i=1 allowed and core arbitrary. Shared/leafless neighbors break both conditional independence and block trace disjointness; attaching leaves changes the function and is not a universal transfer. New claim pending independent-agent review. A008 connected broom separation wholly reconstructed unchanged, including sharper 53I/5 repair.\n')
assert set(progress)=={k.split(' (')[0] for k in protocol['required_per_run']['progress_fields']}
for c in [claim,review]:
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    assert statement_hash(c)==c['statement_sha256']
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert len((agent/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for heading in protocol['required_per_run']['report_fields']: assert '## '+heading in report
receipts=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        assert p.stat().st_size<20_000_000
        receipts.append({'path':str(p.relative_to(run)),'sha256':digest(p),'bytes':p.stat().st_size})
save('out/PERSISTENCE_RECEIPTS.json',{'timestamp_utc':now,'schema_checks':'PASS','claims_statement_hashes':'PASS','progress_delta_identical':True,'files':receipts,'rolling_files':[{'path':str(agent/n),'sha256':digest(agent/n),'bytes':(agent/n).stat().st_size} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]})
print(json.dumps({'saved':True,'files':len(receipts),'claim_sha256':claim['statement_sha256'],'protocol_validation':'PASS','run':str(run)}))
