import hashlib,json
from pathlib import Path

RUN=Path(__file__).resolve().parents[1]
HOME_AGENT=RUN.parents[1]
ROOT=HOME_AGENT.parents[1]
CAMPAIGN=Path('~/mop_fei100/reports/fei-2026-10-11')
RUN_ID=RUN.name
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):
    (RUN/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=json.loads((CAMPAIGN/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
results=json.loads((RUN/'out/CHECK_RESULTS.json').read_text(encoding='utf-8'))
assert results['status']=='PASS' and results['exact_assertions']==10246
old=HOME_AGENT/'runs/20261011T222159Z-fleet05-A063-information-revelation'
prior=json.loads((old/'CLAIMS.json').read_text(encoding='utf-8-sig'))
deps=[{k:c[k] for k in ('claim_id','version','statement_sha256')} for c in prior]
for dep in deps:
    dep['acceptance']='A063 independent reconstruction at stated scope' if dep['claim_id'].startswith('A037') else 'author-proved baseline; Claude B13 v2 checks singleton consequence; broader interface independent review pending'

derivation=(RUN/'DERIVATION.md').read_text(encoding='utf-8')
derivation=derivation.replace('B05\'s accepted selector bound is B_y >= (1-delta)(k-2)d.',
    "B05's selector bound is B_y >= (1-delta)(k-2)d. It can be reconstructed directly here: on each nonempty data packet the selector coefficients are a=p(c_T-delta), b=d, so q/b^2=(c_T/delta-1)^2+1>=1/(4delta). The inequality q h2(b^2/q)>=b^2 log2(q/b^2), summed over (2^k-1)2^r such packets, gives exactly (1-delta)(k-2)d. Thus this corollary uses the source bound with its proof reconstructed, not a floating certificate.")
derivation=derivation.replace('The strict last constant uses ln2>2/3,',
    'Both refunds are strictly positive: in the central y-first table rho0>1/2>rho1 since A,B>0>C; in the z1-first table rho0<1/2 while rho1=1, and both row weights are positive. The strict last constant uses ln2>2/3,')
(RUN/'DERIVATION.md').write_text(derivation,encoding='utf-8')

statement=('For every finite uniform-cube Boolean sign and a fixed two-coordinate block {i,j}, under the canonical physical/spectral singleton lift, the query-order refund is R_i_then_j=I(S_j;X_i|S_remaining). For every fixed block the MU ceiling obeys B_A-J_A=2R_A+sum_h P(h)(B_h-J_h), so it is exactly the accumulated singleton MU bound. For every even k>=4, the actual B05 Boolean family F=1+A_2k(z)[b_k(x)-1-(1-y)1_{x=0}], with b_k=(-1)^(x1*x2+...), delta=2^-k and d=2^-3k, has 0<R_y_then_z1,R_z1_then_y<=32*d^2/(3 ln 2)<16*d^2. All nonempty residual Fourier packets have exactly zero refund in either order. Its selector erasure satisfies B_y>=(1-delta)(k-2)d; for even k>=6 the block MU ceiling is at least (15/32)d. Thus a single additional control-query refund cannot pay the selector logarithm at a dimension-independent price. Full terminal spectra and actual control influence remain in the ledger.')
hypotheses=['Entropy and mutual information in bits; uniform finite cube; Boolean signs; omit zero spectral fibers.',
 'Canonical kernel at a singleton query makes the deleted root spectral bit independent of the physical outcome conditional on remaining spectral label and physical history; no coordinates repeated.',
 'Both coordinates of the fixed block are queried and their actual physical outcomes recorded; fixed order for the two-query reduction.',
 'All-k family theorem uses even k>=4, r=2k controls active only at their binary zero vertex; sign y=+1 selects the bent core and y=-1 its actual origin flip.',
 'Comparison to accumulated singleton uncertainty uses established J_h<=B_h; selector comparison reconstructs the source B05 lower bound. No inference that all tree debt or FEI fails.']
claim_hash=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest()
claim={
 'claim_id':'A063-TWO-QUERY-CENTRAL-PACKET-REFUND','version':1,
 'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':claim_hash,
 'contributors':['A063'],
 'proof_source':{'run_id':RUN_ID,'files':['DERIVATION.md','REPORT.md','code/check_refund.py','out/FROZEN_SPEC.json','out/CHECK_RESULTS.json','out/FIRST_RESULT.json']},
 'proof_dependencies':deps,
 'review_records':[],
 'status':'AUTHOR_PROVED_EXACTLY_VALIDATED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':['Universal one-selector-plus-one-control refund payment B_y<=K*d+M*R_A for finite fixed K,M>=0 on the B05 family'],
 'first_unproved_line':None,
 'next_consumers':['A037','A039','A064','A087','A094','A097','B20']}
save('CLAIMS.json',[claim])

sources=[
 (CAMPAIGN/'EXECUTION_PROTOCOL.json','Complete protocol, revision 2026-10-11-execution-v2; reread current stage.'),
 (ROOT/'BOARD.md','Stage snapshot headed 2026-10-14 05:21 UTC; full board read in resumed work, targeted B08/B13 and consumers reread.'),
 (ROOT/'claude/B13/STREAM_NOTES.md','Complete lead v2 2026-10-11 23:1xZ; A063 target, established MU and paid JS; no disagreement.'),
 (old/'CLAIMS.json','Exact A037/A063 baseline versions and statement hashes.'),
 (old/'REVIEW_A037.md','Independent baseline reconstruction accepted at stated scope.'),
 (CAMPAIGN/'runs/B05/20261011T193057Z-fleet01-B05-rare-restrictions/REPORT.md','Complete source, sections 2-4 Boolean family and selector lower bound; section 7 scope.'),
 (CAMPAIGN/'runs/B05/20261011T193057Z-fleet01-B05-rare-restrictions/CLAIMS.json','Legacy source claim B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO-v1, file pinned rather than inventing statement hash.'),
 (ROOT/'agents/A064/runs/20261011T224431Z-fleet05-A064-global-debt-potential/REPORT.md','Read reserve orientation and full terminal/control influence clauses; motivation, not a proof dependency.'),
 (ROOT/'agents/A097/runs/20261013T222610Z-fleet05-A097-cross-route-transfer/REPORT.md','Read source-bank/collision/terminal interface; motivation, not a proof dependency.'),
 (ROOT/'agents/A097/runs/20261013T222610Z-fleet05-A097-cross-route-transfer/CLAIMS.json','Read scoped transport source; no acceptance beyond already reconstructed baseline claimed.')]
receipts=[]
for p,scope in sources:
    assert p.exists(),p
    receipts.append({'path':str(p),'sha256':digest(p),'read_scope':scope})
save('out/SOURCE_RECEIPTS.json',receipts)
save('out/PRIOR_FAILURE.json',{'source_run':'20261013T234108Z-fleet05-A063-information-revelation',
 'helper':'A063-central-refund-v1','failure':'Fraction endpoint decimal serialization exceeded Python 4300-digit integer-string limit at the first completed k=4 case.',
 'accepted_validation_from_failed_run':False,'repair':'v2 outward interval endpoint rounding at denominator 2^384. Exact kernel probabilities remain unrounded. Domain, family and rigorous log tail unchanged.',
 'stage_destination':'Latest requested stage resumes productive unfinished proof in current run; historical draft remains untouched.'})

next_action=('At one selected A038/A039 exposed priority query, write the inherited common-row signed reference channel and price its nonmatching conversion correction from a named unused conditional child/control slack once, retaining both terminal spectral laws. Use the two-query refund theorem as an information control; do not reset rarity or continue refund-only B05 searches.')
progress={
 'protocol_revision':protocol['revision'],'run_id':RUN_ID,'stream':'B13','packet_id':'A063','gap_id':'G-R-MISMATCH','attempt_id':'A063-information-revelation-2-central-packet',
 'method':'Resume unfinished packet; exact conditional chain rule and coefficient support proof; analytic chi-square information bound; independent actual Boolean Walsh check and rational logarithm certificates.',
 'mathematical_delta':'Block refund barrier exactly equals accumulated singleton MU; two-query refund reduces to first physical outcome information. On actual B05 all-even-k family both orders have strictly positive refund below16d^2, confined to empty residual packet; rare selector erasure remains at least(1-delta)(k-2)d. FEI OPEN.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT',
 'mathematical_status':'NARROW_INFORMATION_INTERFACE_PROVED_EXACTLY_VALIDATED_REVIEW_PENDING_FULL_FEI_OPEN',
 'claim_versions_used':deps,
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'new narrow family/channel consequence of existing refund interface; no new broad candidate'}],
 'source_artifacts':['REPORT.md','DERIVATION.md','CLAIMS.json','code/check_refund.py','code/finalize.py','out/FROZEN_SPEC.json','out/FIRST_RESULT.json','out/CHECK_RESULTS.json','out/SOURCE_RECEIPTS.json','out/PRIOR_FAILURE.json','out/PERSISTENCE.json'],
 'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Universal source-owned conditional reference/erasure payment and full terminal bound still open.','Independent review, supervisor adoption, downstream mathematical use and mirror verification not performed.'],
 'packet_ids':['A063']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)

report=f'''# A063: the information actually revealed by a second query

Run `{RUN_ID}`, stream B13. The all-even-k theorem is proved below and in DERIVATION.md; independent review is pending. Full FEI remains OPEN.

## exact target, quantifiers, hypotheses and units

For every actual finite uniform-cube Boolean function and fixed two-coordinate canonical restriction experiment, identify the query-order refund as the information about the second spectral bit actually revealed by the first physical outcome. For every even k>=4 in the actual B05 family (r=2k, delta=2^-k, d=2^-3k), bound this information in both selector/control orders. Information units are bits; actual kernel probabilities and Boolean amplitudes are rational; zero fibers are omitted. No abstract spectrum is substituted for a Boolean function.

The result is `R_i_then_j=I(S_j;X_i|S_remaining)` and, for the family, `0<R_yz,R_zy<=32d^2/(3 ln2)<16d^2`. Every nonempty residual packet has zero refund. The block ceiling `R_A<=(B_A-J_A)/2` is exactly accumulated per-step MU; the family-specific channel support bound is much sharper. Prior AND2 supplies the already exact positive-refund sharpness example requested by the lead.

## sources actually read, revisions and theorem locators

Read the complete execution protocol (revision {protocol['revision']}); the latest board is headed 2026-10-14 05:21 UTC. Read B13 lead v2 2026-10-11 23:1xZ, particularly its A063 target and established MU/JS bounds. Followed that direction; no disagreement. These instructions prohibit repeating the telescope, conservation or MU proof, so those are baseline inputs.

The original A063 run supplies the canonical common-lift review and exact refund interface: A037 v1 `{deps[0]['statement_sha256']}` and A063 v1 `{deps[1]['statement_sha256']}`. The B05 source report sections 2-4 supply the actual family and logarithmic selector bound, whose lower-bound proof is reconstructed in DERIVATION.md. Read the A064 original reserve report and A097 20261013T222610Z scoped shared-data transfer report to keep complete terminals and one influence owner explicit. Board developments from A037/A038/A039/A061/A062/A064/A087/A094/A097 select the next mixed-query target, without treating board summaries as reviewed theorems. Exact local source hashes and reading scopes are in out/SOURCE_RECEIPTS.json. Earlier protocol/campaign/paper readings are recorded in the original run; no new paper theorem or complete new paper audit is claimed here.

## complete derivation or exact first unsupported line

DERIVATION.md contains the full finite-to-infinite analytic proof. The existing identities give `B_A-J_A=2R_A+sum_h P(h)(B_h-J_h)`. For two queries the first kernel depends only on the second spectral bit and the untouched residual; the second outcome is conditionally independent of root labels given the first outcome and residual. The conditional mutual-information chain rule gives the two-query formula.

The actual family has six coefficient classes and only one exceptional (empty) residual packet. In all other packets the 2x2 amplitude matrix has identical columns: `[[C_T,C_T],[d,d]]`. Either order therefore reveals zero information about the remaining block spectral bit. The central matrix is `[[1+C,C],[d,d]]`, C=-p(1-s+delta). For both order channels its raw conditional Bernoulli variance is at most 2d^2, and its outcome mean lies in [1/4,3/4]. The elementary KL/chi-square inequality gives the stated upper bound; opposite row probabilities prove strict positivity.

The selector bound is `B_y>=(1-delta)(k-2)d`. Consequently `R_A/B_y<=16d/((1-delta)(k-2))` tends to zero. For even k>=6 the accumulated MU ceiling is at least (15/32)d. A universal price `B_y<=K*d+M*R_A` for fixed finite K,M>=0 is thus false on actual Boolean functions. The same conclusion does not rule out paying the two-query block from control influence (which is much larger), more queries, or existing stopping certificates.

No unsupported line occurs inside this narrow theorem. The first unsupported universal line is that, after an actual mixed data/controller history, a named unused inherited conditional child/control slack pays the signed nonmatching reference conversion together with both complete retained terminal laws at a dimension-independent influence price. Information refund by itself provides no such bank.

## executed validation with domain, arithmetic, commands and outputs

Frozen specification: out/FROZEN_SPEC.json, helper v2, even k=4,6,...,40, 19 parameters and 38 query orders, six proved multiplicity classes. Full actual truth-table/Walsh reconstruction is confined to k=4,r=8,n=13 (8,192 truth entries and all 8,192 coefficients). No dimension escalation, random search or floating sign decision occurred. Estimated memory 70 MB, below the 300 MB memok trigger; no heavy job was launched.

Command from this run directory: `python -X utf8 code/check_refund.py`. Result: PASS, {results['exact_assertions']:,} exact assertions, observed runtime {results['runtime_seconds']:.3f} seconds (frozen pilot and maximum both 60 seconds). The independent physical edge count gives selector influence 1/4096 and control influence 13/4096. Conditional independence is checked by exact rational cross-products. Entropy and information signs use 64 rational atanh terms, dyadic logarithm reduction, explicit positive remainder, outward interval division, and outward endpoint rounding to denominator 2^384. Decimal display fields are never certificates. The checker retains all four normalized terminal spectral laws and their expected entropy rather than assigning zero terminal debt.

The failed v1 draft could not serialize an enormous exact Fraction endpoint at k=4; it established no accepted validation output. v2 repairs serialization by rigorous outward interval rounding while keeping the exact kernel and domain. out/PRIOR_FAILURE.json preserves this deviation. At k=4, display-only refund/d^2 values are approximately 2.89808 (selector first) and 2.01843 (control first); expected terminal entropy is approximately 0.112766 bits. Named finite cases verify the analytic theorem, not its all-k quantifier.

## proof dependencies and changed downstream conclusions

The acyclic proof uses the already reconstructed A037 lift and prior A063 fixed-block refund interface, plus elementary KL/chi-square and B13 baseline singleton MU. B05's selector lower-bound proof is reconstructed directly, so its legacy floating self-check is not imported as a certificate. One narrow extension is added; no new broad universal candidate is opened. Independent review remains separate from author validation.

A064/A097 should keep the complete terminal/core bill and control influence account: the rare selector's entropy is in nonempty packets that return exactly zero history refund in this small block. A037/A039 can use the first-outcome reduction to check actual-channel conversions at a mixed-history node, but it supplies neither a generic reference KL refund nor a renewed root bank. The exact amount moved is a quadratic information bound versus a logarithmic selector bill, not a universal FEI constant.

## one next mathematical action and independent reviewer

{next_action}

Independent reviewers: A087 (conditional chain rule and actual common-row reconstruction) and A094 (six-class all-k bound and retained-terminal audit). Consumers A037/A039/A064/A097 should attach the same source hashes before downstream use. This is a handoff in local files; no messages or writes to other agents were sent.

## actual persistence receipts or precise save blocker

The four required protocol files, DERIVATION.md, scripts, frozen specification, first completed instance and complete certificate outputs are saved in this unique run. code/finalize.py checks exact required key sets, statement digest, matching progress/delta, seven report fields, file sizes and two-line rolling status, then writes out/PERSISTENCE.json with actual SHA256 receipts. Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated locally. The productive unfinished draft from the earlier stage is continued here under the latest requested destination; historical drafts are retained unchanged. No repository/mirror copy, supervisor adoption, public release or independent review is claimed.

**Universal bridge:** This stage moves C019 stopping-tree payment and C024 history transfer by proving that an actual selector-plus-one-control history channel refunds at most 16d^2 while the rare selector erases at least (1-delta)(k-2)d; it also resolves the lead's block-versus-singleton question by exact algebraic equivalence. What remains is a source-owned signed conditional-reference reserve that transports unused child influence to erased/core entropy while retaining both full terminals. NEXT tests that missing conversion at the team's already exposed A038/A039 mixed query, which is the shortest continuation toward a universal bridge because another isolated refund search cannot produce the missing logarithmic payment.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')

(HOME_AGENT/'STATUS.md').write_text('STATE: A063 stage complete: all-k B05 two-query refund <16d^2, zero off empty packet; 10,246 exact checks PASS; MU block ceiling is per-step sum; review pending; FEI OPEN.\nNEXT: A087/A094 review; A037/A039/A064 price one exposed mixed-query signed conversion from unused inherited child/control slack, retaining both terminal bills and one influence owner.\n',encoding='utf-8')
with (HOME_AGENT/'WORKLOG.md').open('a',encoding='utf-8') as out:
    out.write('\n2026-10-14 05:26 UTC stage: Read latest board and B13 v2; resumed unfinished two-query proof. Proved R_i_then_j=I(S_j;X_i|W) and exact MU barrier equivalence. Actual B05 refund vanishes on every nonempty residual packet; both orders satisfy 0<R<16d^2 for all even k>=4. v1 Fraction serialization failed; v2 outward 384-bit endpoint rounding repaired it. Frozen 19-parameter/38-order pilot passed 10,246 exact assertions in 43.765 seconds, including independent n=13 Boolean Walsh/edge checks. Complete current run saved; retained terminal spectra; no FEI claim. Next switch from refund-only stress tests to inherited mixed-query signed conversion/owned child slack.\n')
with (HOME_AGENT/'LEARNED.md').open('a',encoding='utf-8') as out:
    out.write('\n2026-10-14: For a fixed two-query canonical block, R_i_then_j=I(S_j;X_i|S_remaining). Deleted first spectral bit and later physical outcome contribute no extra information conditional on the correct history. For any fixed block, B_A-J_A=2R_A+sum p(B_h-J_h); the block refund ceiling is exactly accumulated singleton MU, never a separate stronger inequality.\n\nActual B05 family r=2k, d=2^-3k: both selector/one-control orders have strictly positive refund <16d^2 for all even k>=4. Every nonempty residual spectral packet contributes exactly zero; only [[1+C,C],[d,d]] contributes, C=-p(1-2^-k/2+2^-k), where 2^-k/2 denotes 2^(-k/2). Raw Bernoulli variance <=2d^2 and mean in[1/4,3/4] prove the bound. Selector B_y>=(1-2^-k)(k-2)d remains logarithmic. This refutes fixed-price one-control-refund payment, not FEI or full block payment; control influence and complete terminal entropy remain.\n\nExact interval arithmetic lesson: bound denominator growth by outward endpoint rounding (here denominator2^384); leave kernel probabilities exact. A giant Fraction serialization failure is not a checked result. v2 completed frozen domain within60 seconds; preserve failed-draft provenance. Next use a named unused conditional bank at an actual mixed query; no renewed rarity/root reserve.\n')

req=protocol['required_per_run']
assert set(claim)==set(req['claim_fields'])
progress_fields=[x.split(' (')[0] for x in req['progress_fields']]
assert set(progress)==set(progress_fields)
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert all('## '+field in report for field in req['report_fields'])
assert len((HOME_AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
paths=[p for p in RUN.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json']
assert all(p.stat().st_size<20*1024*1024 for p in paths)
save('out/PERSISTENCE.json',{'status':'LOCAL_FILES_AND_SCHEMA_CHECKED','claim_statement_sha256':claim_hash,
 'required_file_key_sets':'PASS','progress_delta_identity':'PASS','report_field_sections':'PASS','rolling_status_two_lines':'PASS',
 'receipts':[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in paths],
 'rolling_receipts':[{'path':str(HOME_AGENT/name),'sha256':digest(HOME_AGENT/name)} for name in ('STATUS.md','WORKLOG.md','LEARNED.md')],
 'independent_review':'PENDING','mirror_verification':'NOT_PERFORMED','downstream_use':'NOT_CLAIMED'})
print(json.dumps({'status':'PASS','run_id':RUN_ID,'statement_sha256':claim_hash,'files':len(paths)+1,'exact_assertions':results['exact_assertions']},indent=2))
