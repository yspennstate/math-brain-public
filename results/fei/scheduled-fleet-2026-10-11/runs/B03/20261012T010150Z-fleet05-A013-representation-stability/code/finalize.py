from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]; BASE=A.parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj): (R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
transport=json.loads((R/'out/TRANSPORT_RESULTS.json').read_text())
general=json.loads((R/'out/GENERAL_RESULTS.json').read_text())
ref=json.loads((R/'out/REFERENCE_RESULTS.json').read_text())
post=json.loads((R/'out/POSTERIOR_RESULTS.json').read_text())
assert all(x['status']=='PASS' for x in [transport,general,ref,post])
source_a012=BASE/'agents/A012/runs/20261011T234525Z-fleet05-A012-sparse-activation-accounting'
ac=json.loads((source_a012/'CLAIMS.json').read_text(encoding='utf-8-sig'))
if isinstance(ac,dict):ac=ac.get('claims',ac)
reviewed=next(c for c in ac if c['claim_id']=='A012-CONTROL-FIRST-POSTERIOR-REPAIR')
assert reviewed['statement_sha256']=='b5b1d941a3fd7511b0ce648ad4d4f6573d0e89f7f04dffc6c1ff9a8943ba1895'
reviewed['review_records']=list(reviewed.get('review_records',[]))+[{'reviewer':'A013/fleet05','verdict':'HOLDS_AT_STATED_SCOPE','source':str(R/'A012_REVIEW.md'),'sha256':digest(R/'A012_REVIEW.md'),'method':'Independent analytic reconstruction and fresh actual-child Fourier/joint-law implementation; no author code imported','validation':[str(R/'out/REFERENCE_RESULTS.json'),str(R/'out/POSTERIOR_RESULTS.json')],'scope':'Exact sharp balanced-core activation reference, all-r sharp coefficient, and control-first posterior; no universal core FEI payment.'}]
reviewed['status']='INDEPENDENTLY_ACCEPTED_LOCAL'
statement='For every Boolean f on a uniform n-dimensional cube, n>=1, the positive full-minterm cover with one common physical order and the fixed first-gate tie has S=0 and averaged physically restricted label cost at most its parent label cost. With P(S)=fhat(S)^2, K=|S|, Z=1{i in S}, and inherited ranks r_j, its exact rank reset is (6/5)[E Z log2 K - Inf_i log2 r_i + sum_(r_j>r_i) Inf_j log2((r_j-1)/r_j)], and its exact rarity reset is E[(n-1)(K-Z)1{120(K-Z)<11(n-1)}-nK1{120K<11n}]. Root odds, root probabilities and vacuum-weighted normalizers retain the actual child counts as in GENERAL_RESET.md. For the actual bent-prefix family chi_[d] b_m, m=4t>=4, querying a prefix bit has influence one while the averaged combined L+S+R reset is unbounded as m increases; it exceeds 1/2 already at m=256 by an exact rational certificate. Nevertheless, for every prefix depth D the cumulative positive rank/rarity and vacuum-weighted root-normalizer increments are less than (33/16) I(b_m), and including terminal entropy uses one total reserve of (65/16) I(b_m). This refutes fixed-cover local monotonicity and any absolute queried-influence surcharge, not full FEI or optimized alternative covers.'
claim={'claim_id':'A013-AVERAGED-QUEUE-TRANSPORT','version':1,'exact_statement':statement,'hypotheses':['Boolean signs, uniform physical cube, bits','Positive full-minterm AND cover; common order, fixed first-gate tie; inherited order under actual restriction','For the reserve/counterfamily: quadratic bent core m divisible by four, fresh character prefix d>=0','No independently optimized gate orders or alternative covers are asserted'],'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A013/fleet05'],'proof_source':{'paths':[str(R/'GENERAL_RESET.md'),str(R/'DERIVATION.md')],'sha256':[digest(R/'GENERAL_RESET.md'),digest(R/'DERIVATION.md')],'validation':[str(R/'out/GENERAL_RESULTS.json'),str(R/'out/TRANSPORT_RESULTS.json')]},'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['B03 STREAM_NOTES.md v2 target for A013: exact L,S,R do not increase under physical restriction, interpreted for inherited covers','An absolute queried-influence surcharge bounds the averaged exact inherited-cover L+S+R reset'],'first_unproved_line':None,'next_consumers':['B03','A011','A012','A015','A039','A064','A086','A094','B20']}
save('CLAIMS.json',[claim,reviewed])
next_action='Extend the compensated degree-factorial/rank and one-time rarity-entry ledger to grouped gates in a fixed normalized overlapping-cover reference, retaining actual child roots and terminal entropy; A086/A094 independently reconstruct the present reset and reserve.'
sources=[BASE/'BOARD.md',BASE/'claude/B03/STREAM_NOTES.md',BASE/'claude/B03/runs/20261011T223500Z-claude-B03-pp-congestion/CLAIMS.json',source_a012/'DERIVATION.md',source_a012/'CLAIMS.json',source_a012/'A013_ACTIVATION_REVIEW.md',BASE/'agents/A039/runs/20261011T221511Z-fleet05-A039-physical-child-reference-transfer/DERIVATION.md']
sources=[p for p in sources if p.exists()]
sources.extend(BASE.glob('agents/A039/runs/*/DERIVATION.md'))
sources.extend(BASE.glob('agents/A086/runs/*/ACTIVATION_DEBT_PROJECTION.md'))
sources.extend(BASE.glob('context/*threshold*38*.txt'))
sources=list(dict.fromkeys(sources))
protocol=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
sources.append(protocol)
source_receipts=[{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size} for p in sources]
save('out/SOURCE_RECEIPTS.json',source_receipts)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B03','packet_id':'A013','gap_id':'C020-ordered-cover-history-transfer','attempt_id':'A013-stage2-averaged-reset-single-use-reserve','method':'Exact physical-child Fourier folding, factorial rank telescoping, one-time rarity entry, rational certificates; independent A012 review','mathematical_delta':'Universal full-minterm averaged label contraction and exact rank/rarity reset; unbounded queried-influence surcharge obstruction; bent-prefix full-depth single-use reserve 33/16 plus terminal total 65/16; A012 sharp activation/posterior independently reconstructed.','deliverable_status':'COMPLETE_LOCAL_SAVED','mathematical_status':'SCOPED_TRANSPORT_RESOLVED; UNIVERSAL_RESERVE_AND_FULL_FEI_OPEN','claim_versions_used':['B03-R-REFINED-WITNESS-BOUND@1 (definitions only, reconstructed)','A012-CONTROL-FIRST-POSTERIOR-REPAIR@1 (independently reconstructed)'],'claims_created_or_changed':['A013-AVERAGED-QUEUE-TRANSPORT@1','A012-CONTROL-FIRST-POSTERIOR-REPAIR@1 review only; original immutable source untouched'],'source_artifacts':source_receipts,'next_consumers':['B03','A011','A012','A015','A039','A064','A086','A094','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['No universal single-use retained-state reserve is proved for arbitrary overlapping covers; independent review of new A013 claim pending; supervisor mirroring unverified.'],'packet_ids':['A013']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
total=sum(x['exact_assertions'] for x in [transport,general,ref,post])
report=f'''# A013 stage 2: exact averaged transport and retained-state payment

## exact target, quantifiers, hypotheses and units

Study the B03 lead v2 request that exact Theorem R L,S,R decrease under physical restriction, for inherited useful ordered covers. Bits throughout. We resolve the full-minterm/common-order case in all dimensions, refute that monotonicity and every absolute queried-influence surcharge on an actual Boolean family, and replace it by a full-depth retained-core reserve for that family. This is not an FEI counterexample. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

BOARD.md (snapshot 2026-10-12 01:00 UTC), B03 STREAM_NOTES.md v2 (23:2xZ), own stage-1 STATUS/LEARNED and proof, protocol revision 2026-10-11-execution-v2 in full, and B03-R-REFINED-WITNESS-BOUND@1 in lead CLAIMS.json. The 38pp threshold-paper Sections 5.3-5.4 provide the original queue and G_j definitions. Consumed A012 stage-2 DERIVATION/CLAIMS and its review of our stage-1 activation clause; read A039 physical-child/reference projection and A086 stage-2 debt projection to avoid repeating their results. Source receipts are in out/SOURCE_RECEIPTS.json. Campaign baseline and earlier paper versions were recovered from the prior stage; no new literature-priority claim is made.

## complete derivation or exact first unsupported line

GENERAL_RESET.md proves the all-dimensional averaged update using the actual signed child Fourier coefficients. L contracts, S=0, and rank/rarity reset exactly. DERIVATION.md proves the counterfamily chi_[d] b_m, the unbounded averaged combined reset at queried influence one, and the rational m=256 positive certificate. It then pays all positive rank/rarity/root-normalizer increases over every prefix depth with one reserve <33/16 times core influence; terminal entropy increases the total allocated reserve to 65/16. Common-order optimality is explicit and does not optimize independent gate orders or alternate covers. The terminal positive/negative bent minterm counts differ and are retained separately. Thus the lead's monotonicity direction is false even in its averaged form. Its entropy upper bound is not refuted.

A012_REVIEW.md independently reconstructs the sharp activation reference, unique r=3 maximum 15/4+(49/12)log2(8/7), and true control-first witness posterior tending to two bits. The core reference bill survives with its activation probability. First unsupported universal line: a single-use retained-state reserve for arbitrary overlapping covers and physical descendants, with terminal entropy retained and no prior universal core FEI assumption.

## executed validation with domain, arithmetic, commands and outputs

All checks use Python -X utf8, Fraction, integer truth-table Fourier transforms, exact prime-log vectors, and outward rational atanh logarithm bounds. Frozen specs precede all searches. Estimated memory 70 MB, internal cutoff 50 seconds; no heavy job or memok threshold was needed, no GPU or automatic dimension increase. Commands below are relative to this run:

- python -X utf8 code/check_transport.py: {transport['exact_assertions']} assertions, {transport['elapsed_seconds']:.6f} seconds, PASS. Eight bent-prefix truth-table cases (m4,d0..4; m8,d0..2), nine binomial ledgers (m4,8,16; D1,2,4), rational analytic sign cases m256,512,1024,2048.
- python -X utf8 code/check_general.py: {general['physical_query_cases']} labelled physical-query cases, {general['exact_assertions']} assertions, {general['elapsed_seconds']:.6f} seconds, PASS. All Boolean tables n1..3 and each singleton query, no symmetry reduction.
- python -X utf8 code/check_reference.py: {ref['activation_reference_cases']} independent activation reference cases, {ref['exact_assertions']} assertions, {ref['elapsed_seconds']:.6f} seconds, PASS. All balanced cores n1,2 and two frozen n3 cores, r1..3, actual/uniform/half-uniform nonempty references.
- python -X utf8 code/check_posterior.py: literal-core true joint witnesses r1..3, sharp coefficient r1..5 plus analytic all-r tail; {post['exact_assertions']} assertions, {post['elapsed_seconds']:.6f} seconds, PASS.

Total completed assertions: {total}. Analytic proofs, not the finite grid, establish all-dimensional statements. Attempts are preserved honestly: initial combined checker exposed the terminal-count error (corrected before certification); combined and unsplit review attempts hit their 50-second cutoff and produced no PASS; a shell inline-preparation attempt had a quoting error and changed nothing. Split domains were frozen explicitly rather than escalating compute. Successful outputs are out/TRANSPORT_RESULTS.json, GENERAL_RESULTS.json, REFERENCE_RESULTS.json and POSTERIOR_RESULTS.json.

## proof dependencies and changed downstream conclusions

The new A013 claim is self-contained after specifying the exact lead/paper functionals; no unreviewed campaign theorem is a proof premise. A012@1 receives an independent local acceptance of its precise statement, recorded without changing its source. A012's prior acceptance of our activation clause does not accept our entire stage-1 package. The original A013 claim remains unchanged. B03/A011/A015 must replace inherited-cover monotonicity or a queried-influence tax by a compensated history transfer or an explicitly changed cover. Other lead bounds and full FEI are not invalidated.

## one next mathematical action and independent reviewer

{next_action}

## actual persistence receipts or precise save blocker

The four protocol files, full proofs, frozen specs, checker sources and outputs are saved in this unique run. out/PERSISTENCE_RECEIPTS.json records SHA256 and byte sizes for all saved artifacts except itself. STATUS.md is current; WORKLOG.md is appended and LEARNED.md records durable statements. No file exceeds 20 MB. Shared indices, other-agent folders and brain are untouched. Supervisor copy/mirror and downstream use are not claimed.

Universal bridge: This stage moves C020 and C024 by replacing a false local monotonicity premise with an exact universal full-minterm reset, and closes the positive full-depth transport payment on the bent-prefix stress family at 33/16 core influence (65/16 including terminal entropy). The remaining bridge is a single-use retained-state reserve for arbitrary overlapping covers and changing signed child spectra. The next grouped-gate compensated ledger attacks exactly that universal unpaid term while preserving child roots and terminal entropy, making it a shorter route to full FEI than another isolated class bound.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A013 stage 2 complete locally: universal minterm reset, averaged monotonicity refuted, single-use bent reserve; A012 v1 independently accepted; '+str(total)+' exact assertions; full FEI OPEN.\nNEXT: Replace lead v2 false monotonicity direction by grouped-gate compensated rank/rarity reserve with actual child roots and terminal entropy; A086/A094 review.\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8') as h:h.write(f'\n{stamp} Stage 2 {R.name}: read board/lead; exact full-minterm reset and label contraction; bent-prefix averaged unbounded local surcharge obstruction; full-depth reserve 33/16, terminal total65/16; A012 independently reconstructed. Corrected unequal terminal minterm counts; bounded split checks PASS ({total} assertions), cutoff attempts preserved. Universal overlapping-cover reserve remains open.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as h:h.write('\nStage 2 durable facts: For inherited common-order full-minterm covers, averaged L contracts and S=0, but R need not contract. The exact reset is in GENERAL_RESET.md; signed physical-child folding, not either child alone, yields residual spectrum. Bent-prefix m=4t gives unbounded reset/queried influence, yet one retained-core bank pays all positive rank, rarity and vacuum-weighted normalizers at33/16, or65/16 with terminal entropy. Positive and negative bent cores have different minterm counts. Scope excludes optimized independent gate orders and alternate covers. A012 sharp activation reference and true witness posterior independently reconstructed; arbitrary core debt remains. Computational cutoff is not a passed certificate; split frozen grids and analytic all-parameter proof.\n')
fields=json.loads(protocol.read_text(encoding='utf-8-sig'))['required_per_run']
pf=[x.split(' (')[0] for x in fields['progress_fields']]
assert set(progress)==set(pf)
for cl in [claim,reviewed]:assert set(cl)==set(fields['claim_fields'])
receipts=[]
for path in sorted(R.rglob('*')):
 if path.is_file() and path.name!='PERSISTENCE_RECEIPTS.json':
  assert path.stat().st_size<20_000_000
  receipts.append({'path':str(path),'bytes':path.stat().st_size,'sha256':digest(path)})
for path in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']:receipts.append({'path':str(path),'bytes':path.stat().st_size,'sha256':digest(path)})
save('out/PERSISTENCE_RECEIPTS.json',receipts)
print(json.dumps({'status':'SAVED_AND_SCHEMA_CHECKED','completed_assertions':total,'claim_count':2,'receipt_count':len(receipts)}))
