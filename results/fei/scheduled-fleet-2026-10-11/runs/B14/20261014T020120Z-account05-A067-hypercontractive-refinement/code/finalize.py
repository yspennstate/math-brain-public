import copy,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent; HOME=ROOT.parent.parent
def dump(path,obj):path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
full=json.loads((ROOT/'out/CHECK_FULL.json').read_text());pilot=json.loads((ROOT/'out/CHECK_PILOT.json').read_text());reviews=json.loads((ROOT/'out/REVIEWS.json').read_text())
paths=[HOME.parent/'A066/runs/20261014T012949Z-account05-A066-semigroup-dissipation/CLAIMS.json',HOME.parent/'A070/runs/20261014T005025Z-account05-A070-analytic-route-referee/CLAIMS.json']
ids=['A066-JOINT-SINGLETON-COEFFICIENT-TWO-OBSTRUCTION','A070-MASK-REFUND-BOOLEANITY-AND-EDGE-CONVERSION-AUDIT']
claims=[]
for path,cid in zip(paths,ids):
    c=copy.deepcopy(next(c for c in json.loads(path.read_text()) if c['claim_id']==cid))
    c['review_records'].append({'reviewer':'account05/A067','verdict':'ACCEPT_AT_FULL_STATED_SCOPE_WITHOUT_REPAIR','reviewer_contributed_repair':False,'proof_source':str(ROOT/'AUDIT.md'),'validation_source':str(ROOT/'out/REVIEWS.json'),'independent_method':'New direct Boolean truth-table and paired-input enumeration; rational-log sign enclosures; infinite-family analytic reconstruction','source_claims_file_sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    c['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A067_LOCAL_RECEIPT';claims.append(c)
statement='For all finite disjoint uniform blocks X,Z, Boolean g(X), indicators A(X),B(X), and two fixed subcube indicators p(Z),q(Z) with arbitrary fixed-coordinate sets and assignments, put E=(Ap) XOR (Bq) or E=(Ap) OR (Bq), F=g(-1)^E. Assume P_Z(E(x,Z))<=1/4 for every x. With I_X,I_Z belonging to final F and Q_access=H(F)-E_Z H(F_Z), Q_access<=K I_Z+2I_X, K=4+log2(5)+2/ln(2)<19/2. Compatible assignments permit K=6+2/ln(2)<9. After contracting controls outside the two fixed sets, one row-independent normalized complete reference on every nonempty control subset uses at most five flat cells (four when compatible) with log-cardinality<=twice conditional mean degree. The combined final mask owns the core reserve once. Every actual core entropy is retained. If every actual F_z satisfies U(F_z)<=bI(F_z), b>=0, then H(F)<=K I_Z+(4+2b)I_X<=max(K,4+2b)I(F). In particular all actual cores of Fourier degree at most two give H(F)<=K I(F), with unbounded controller widths. No arbitrary core admission or arbitrary control-dependent seed is asserted.'
hyp=['Actual Boolean signs on finite uniform cubes; entropy in bits and ordinary physical influence','Seed and event-domain flags depend on X alone; two controller subcubes fixed globally, possibly overlapping, unequal, nested or incompatible','Final combined edit-fiber probability at most 1/4 for every core assignment; XOR or union-once editing','All actual conditional core entropies retained; U certificate required on every actual core for the FEI corollary; irrelevant controls contracted','Empty edits and empty contracted control block treated separately by continuity/trivial access zero']
newid='A067-TWO-SUBCUBE-COMPLETE-CELL-REFERENCE'
sha=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
deps=[{'claim_id':'A067-BOUNDED-FIBER-TWO-EVENT-ACCESS-RESERVE','version':1,'scope':'Accepted A088 ownership/channel identities only; no bounded-cardinality assumption reused','source':str(HOME/'runs/20261013T222025Z-account05-A067-hypercontractive-refinement/DERIVATION.md'),'acceptance_source':str(HOME.parent/'A088/runs/20261013T234248Z-account05-A088-booleanity-referee/AUDIT.md')},{'claim_id':'A067-LOCAL-BOOLEAN-GRANULARITY','version':1,'scope':'Only terminal U corollary; independently accepted A088 and A070','source':str(HOME/'runs/20261011T220539Z-account05-A067-hypercontractive-refinement/REPORT.md')}]
claims.append({'claim_id':newid,'version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':sha,'contributors':['account05/A067'],'proof_source':str(ROOT/'DERIVATION.md'),'proof_dependencies':deps,'review_records':[],'status':'AUTHOR_PROVED_EXACT_VALIDATION_PASSED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A070','A088','A094','A069','B14','B20']})
dump(ROOT/'CLAIMS.json',claims)
nextact='Replace the U terminal hypothesis by a signed transfer of the actual retained-core normalized KL reference (A096); first preserve all banks on A070\'s g=q*y cancellation witness, then formulate one core-dependent branch-split lemma for C019.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B14','packet_id':'A067','gap_id':'FEI-B14-A067-INITIAL','attempt_id':'stage4-flat-cell-complete-reference','method':'Common normalized Fourier-cell reference; exact integer cell-moment certificates; Boolean combined-mask ownership; retained actual core terminals','mathematical_delta':'Dimension-free access coefficient <19/2 for two fixed arbitrary subcube controllers with core-dependent flags and final fiber cap 1/4; <9 for compatible assignments. Large-fiber cardinality loss removed. A066 and A070 new source claims independently accepted at scope.','deliverable_status':'COMPLETE_SAVED_LOCAL','mathematical_status':'RESTRICTED_ACCESS_THEOREM_PROVED_PENDING_REVIEW_FULL_FEI_OPEN','claim_versions_used':deps,'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'status':c['status']} for c in claims],'source_artifacts':[str(ROOT/f) for f in ['DERIVATION.md','AUDIT.md','FROZEN_SPEC.json','out/CHECK_FULL.json','out/REVIEWS.json']],'next_consumers':['A070','A088','A094','A069','B14','B20'],'next_action':nextact,'stagnant_substantive_attempts':0,'blockers':['Universal retained-core terminal payment remains open; supervisor mirror adoption and independent reviews of new theorem not claimed'],'packet_ids':['A067']}
dump(ROOT/'PROGRESS.json',progress);(ROOT/'PACKET_DELTA.json').write_bytes((ROOT/'PROGRESS.json').read_bytes())
total=full['assertions']+pilot['assertions']+reviews['assertions']
report=f'''# exact target, quantifiers, hypotheses and units

Close the large-fiber label loss from A067 stage 3 for two fixed subcube controllers. For every finite Boolean core seed and arbitrary core event flags, XOR or union-once editing has dimension-free physical access cost Q<=K I_Z+2 I_X, K=4+log2(5)+2/ln2<19/2; compatible assignments give K<9. Assume every final fiber has probability <=1/4. Influences belong to final F and entropy is in bits. There is no bound on controller width or fiber cardinality. All actual terminal core entropies remain. U<=bI on every actual terminal gives H<=max(K,4+2b)I. Degree-two actual cores, including arbitrary two-bit core flags/seeds, give H<=KI with arbitrary control widths. Full FEI remains open.

# sources actually read, revisions and theorem locators

- EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2, all fields; current canonical claim query and own stage-1/3 source claims/derivations.
- BOARD.md dated 2026-10-14 01:51 UTC, including its B14 and intervening update rows; B14 STREAM_NOTES.md v2 and own STATUS/LEARNED.
- A088 run 20261013T234248Z, AUDIT.md and CLAIMS.json: independent acceptance of A067 bounded-fiber v1, ownership/channel and retained terminals.
- A069 run 20261014T000110Z, DERIVATION.md and CLAIMS.json: simultaneous Boolean refund v1, already independently accepted by A070; comparison only.
- A070 run 20261014T005025Z, DERIVATION.md Sections 2-3 and CLAIMS.json: normalized-real and signed physical conversion audit v1, independently accepted here.
- A066 run 20261014T012949Z, DERIVATION.md and CLAIMS.json: coefficient-two obstruction v1, independently accepted here.
- A068 run 20261013T234128Z CLAIMS.json metadata: cyclic theorem accepted independently, inherited-reference obstruction remains pending from our perspective.
- Source-bound earlier A088/A070 review locators for local granularity located via rg; its two independent acceptances are consumed through the A088 current proof chain.

# complete derivation or exact first unsupported line

DERIVATION.md is the full all-dimensional proof. Split controls into shared and two private blocks. Compatible Fourier rows are flat on four nonempty cells; incompatible shared assignments split the shared-only cell by conflict parity, giving at most five. The reference includes the zero-mass double-private cell and covers every nonempty contracted-control subset. Uniform cell entropy is bounded by twice its mean degree, with the parity-affine and empty-deletion cases proved. A single row-independent complete reference gives B_Z<=h2(alpha)+alpha log2(M)+2I_Z. Final-mask Boolean ownership and cube isoperimetry give alpha<=I_Z and h2(alpha)<=2(I_X+I_Z). Add the accepted channel price 2I_Z/ln2 once. The physical core reserve is paid once against the combined final mask.

No unsupported line remains in this access theorem. The first unsupported universal line is a complete paid reference for arbitrary retained core terminals: U<=bI is a genuine admission hypothesis, not a consequence asserted here. Nor does this theorem allow the source g to depend on controls.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was written before execution. Commands from A067: python -X utf8 runs/{ROOT.name}/code/check.py --mode pilot; python -X utf8 runs/{ROOT.name}/code/reviews.py; python -X utf8 runs/{ROOT.name}/code/check.py --mode full. Pilot: {pilot['tested']} cases, {pilot['assertions']} assertions, {pilot['runtime_seconds']:.4f}s. Full: {full['tested']} valid Boolean cases and {full['outside_final_fiber_cap']} explicitly rejected outside-cap inputs out of 36,096 frozen inputs; {full['assertions']} assertions, {full['runtime_seconds']:.4f}s. This covers all 90 shared/private/conflict geometries with contracted control dimension <=5 and controller codimensions >=2, all one-bit seed/domain truth tables, XOR and OR; plus three geometries with all two-bit seed/domain truth tables. Geometry reduction uses permutations/reflections only and preserves ordered event flags. It is not an exhaustive sweep of all Boolean functions at these dimensions.

Integer FWHT, exact rational physical influences, exact equal Fourier-cell squares and integer-power cardinality/mean-degree inequalities are checked. Entropy access including every actual leaf is certified by 20-term rational atanh logarithm intervals with proved tail and outward 80-bit rounding. The infinite-dimension bridge is the analytic cell proof, not extrapolation of finite cases. Review job: {reviews['assertions']} assertions, {reviews['runtime_seconds']:.4f}s; actual bent truth tables for m=2..5 and independently enumerated resampling/physical pairs for A070. Total primary checks including pilot and reviews: {total}. Estimated memory <=100 MB; no >300 MB job was scheduled. Full maximum runtime frozen at 600 seconds, pilot/review at 60; no automatic dimension increase, GPU, external service or background helper.

# proof dependencies and changed downstream conclusions

New claim {newid}@1 uses accepted A067 bounded-fiber v1 only for exact restriction/channel identities and final Boolean ownership, and accepted A067 granularity v1 only for terminal admission. The new cell proof and whole-mask isoperimetry are supplied here. The large-fiber constant no longer grows as r/(r-log2 k); unequal overlapping controllers have one complete common reference. A069/A070 refunds are comparison sources, not logical dependencies or a replacement for the retained core.

AUDIT.md and CLAIMS.json independently accept A066's coefficient-two obstruction and A070's signed-conversion audit without repair. Their original statement hashes are preserved. These two reviews reduce the observed live pending queue before the new coherent candidate is opened; the A068 inherited-reference obstruction and the new A067 theorem remain pending locally. No shared index or another agent's files were changed.

# one next mathematical action and independent reviewer

{nextact} Independent reviewers for this completed theorem: A070 and A088, with A094 as additional Booleanity referee. Review must reconstruct the complete five-cell reference, the single final-core reserve, and terminal scope; no request to repeat a preaccepted baseline.

# actual persistence receipts or precise save blocker

All four protocol files, code/, out/, FROZEN_SPEC.json, DERIVATION.md and AUDIT.md are saved in this run. STATUS.md, WORKLOG.md and LEARNED.md are current. out/RECEIPTS.json records file SHA256/size and exact protocol key checks. PACKET_DELTA.json is byte-identical to PROGRESS.json. Every file is below 20 MB. Local persistence is verified; supervisor mirror/index/public adoption and independent acceptance of the new theorem are not claimed.

# Universal bridge

This stage moves C019 stopping-tree payment from bounded-cardinality edit fibers to two fixed arbitrarily wide, unequal or overlapping subcube controllers: a single complete output reference removes the ambient label factor, with access coefficient <19/2 (<9 when compatible) and one owned final-core reserve. It closes the full class when all actual core terminals have U<=bI, in particular degree-two cores. Arbitrary terminal payment and sources depending on controls remain open. NEXT targets the actual retained-core KL reference and signed branch transfer because those are the unpaid universal terms already exposed by A070/A096; another fixed-class enumeration would not remove them.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
stage='2026-10-14 stage4 02:01 UTC'
(HOME/'STATUS.md').write_text('STATE: Stage 4 complete: two-subcube complete-reference access K<19/2 (compatible K<9); two independent source reviews; new theorem pending review, full FEI open.\nNEXT: '+nextact+'\n',encoding='utf-8')
for name,entry in [('WORKLOG.md',f'\n### {stage}\nProved complete flat-cell reference for unequal/overlapping/incompatible fixed subcube controllers with arbitrary core flags. Executed {full["tested"]} valid cases, {full["outside_final_fiber_cap"]} outside-cap rejections, {total} primary checks; no failure. Independently accepted A066 coefficient-two and A070 conversion audits. Saved {ROOT.name}; full FEI and universal core admission remain open.\n'),('LEARNED.md',f'\n### {stage}: common Fourier-cell reference\nTwo fixed subcube controllers yield at most four compatible or five incompatible complete nonempty frequency cells. Every occupied row is flat within a cell; log2 cell size<=2 conditional mean degree, including conflict-parity cells after empty deletion. Keeping the unused double-private cell gives a positive common conditional reference on all nonempty labels. With every final edit fiber <=1/4, Boolean final-mask ownership yields alpha<=I_Z and h2(alpha)<=2(I_X+I_Z), hence access <=(4+log2(5)+2/ln2)I_Z+2I_X (<19/2 coefficient; compatible <9). Actual core U admission yields max(K,4+2b) FEI; degree-two terminals have b=1. Width/cell cardinality can be unbounded. Fixed seed independent of controls remains substantive. A070 refund-alone conversion is false despite a positive full bank; A066 joint singleton coefficient two fails for every bent edit m>=2.\n')]:
    old=(HOME/name).read_text(encoding='utf-8')
    if stage not in old:(HOME/name).write_text(old+entry,encoding='utf-8')
protocol=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text())
expected=set(protocol['required_per_run']['claim_fields']);assert all(set(c)==expected for c in claims)
expected=set(k.split(' (')[0] for k in protocol['required_per_run']['progress_fields']);assert set(progress)==expected
assert (ROOT/'PACKET_DELTA.json').read_bytes()==(ROOT/'PROGRESS.json').read_bytes()
receipts=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='RECEIPTS.json':
        assert p.stat().st_size<20_000_000
        receipts.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
dump(ROOT/'out/RECEIPTS.json',{'protocol_fields_match':True,'packet_delta_byte_identical':True,'new_statement_sha256':sha,'files':receipts,'rolling_files':[{'path':str(HOME/n),'sha256':hashlib.sha256((HOME/n).read_bytes()).hexdigest()} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]})
print(json.dumps({'files':len(receipts),'new_claim':newid,'primary_checks':total,'full_valid_cases':full['tested'],'new_claim_sha256':sha}))
