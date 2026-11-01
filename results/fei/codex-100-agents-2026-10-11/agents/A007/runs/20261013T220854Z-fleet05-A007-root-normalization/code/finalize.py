from pathlib import Path
import copy, hashlib, json
from datetime import datetime, timezone

root=Path(__file__).resolve().parents[1]
agent=root.parents[1]
workers=agent.parents[1]
reports=Path(r'~\mop_fei100\reports\fei-2026-10-11')
timestamp=datetime.now(timezone.utc).isoformat()
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def write_json(path,data): Path(path).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

a006=workers/'agents'/'A006'/'runs'/'20261013T214427Z-fleet05-A006-posterior-forest-optimization'
a009=workers/'agents'/'A009'/'runs'/'20261012T031835Z-fleet05-A009-fractional-incidence-optimization'
forest=reports/'source_material'/'reductions'/'paper'/'forests.tex'
sources=[reports/'EXECUTION_PROTOCOL.json',workers/'BOARD.md',workers/'claude'/'B02'/'STREAM_NOTES.md',
         a006/'CLAIMS.json',a006/'REPORT.md',a006/'FOREST_MOMENTS.md',a009/'REPORT.md',forest,
         agent/'runs'/'20261011T234502Z-fleet05-A007-root-normalization'/'REPORT.md',
         agent/'runs'/'20261011T234502Z-fleet05-A007-root-normalization'/'CLAIMS.json']
write_json(root/'out'/'SOURCES.json',[{'path':str(p),'sha256':sha(p)} for p in sources])

original=next(c for c in json.loads((a006/'CLAIMS.json').read_text(encoding='utf-8-sig')) if c['claim_id']=='A006-ACTUAL-FOREST-DETERMINANT-MOMENT-BOUNDS')
adopted=copy.deepcopy(original)
adopted['review_records'].append({'reviewer':'A007','verdict':'HOLDS_AT_ORIGINAL_STATED_SCOPE_NO_REPAIR',
    'proof_source':str(root/'REVIEW_A006.md'),'validation':str(root/'out'/'REVIEW_CHECK.json'),
    'method':'Independent multilinear determinant reconstruction and explicit queue-event enumeration; original source and all sharpness/boundary clauses reconstructed; no author code imported',
    'reviewer_supplied_substantive_repair':False,'timestamp_utc':timestamp})
adopted['status']='INDEPENDENTLY_RECONSTRUCTED_AT_STATED_SCOPE_LOCAL_ADOPTION_PENDING'
statement=("For every nonconstant Boolean g=2B-1 with the full finite signed prime-conjunction table, positive feasible fixed lambda and one fixed full support order per gate, every r>=1 and every fixed 0<beta<=1 with beta sum lambda<=1, common-core activation F=2A_r B-1 has a fixed feasible prime-table reference lambda'=beta lambda, pi'=2^-r pi, core-first orders. Keeping all base data witnesses and linking old roots through selected core coordinates injects distinct actual base partition-forest events into actual activated events, with multiplicity (c-1)! binom(u+c-2,c-1). For nonempty data T its selected mass is p S(T)G_U(T), with G_U, G_0 defined in LIFT.md and empty-core equality for the full partition-forest mass. The conditioned residual retains the exact signed normalizer log2[D'/(pD)]<=log2 beta. Core-only one-gate mass is p beta a 2^(-C_U), canceling root/name rarity. With the same base posterior, let J_U and L_0 be the rank-stripped joint masses in LIFT.md, and Psi=p Var(g)log2[D'/(pD)]-p sum_T P_g(T)[p log2 L_0(T)+2^-r sum_(U nonempty)log2 J_U(T)]. The full optimized activated surrogate residual satisfies R_F<=p R_g+(7/2)p I(g)+(6/5+log2(e)/4)I_core(F)+Psi. No bound Psi<=K I(F), arbitrary-seed FEI closure or universal PI-J payment is asserted.")
new={'claim_id':'A007-ACTUAL-DATA-WITNESS-ROOT-LIFT','version':1,'exact_statement':statement,
     'hypotheses':['finite uniform cube; nonconstant g; fresh positive r>=1 conjunction core',
          'g represented by all nonempty signed prime conjunctions; rarity pi_l=2^(-width_l)',
          'positive fixed feasible lambda; fixed beta in (0,1] with beta sum lambda<=1',
          'one globally fixed full support order per gate; activated order core first',
          'original forests.tex actual once-per-gate partition forests and conditioned nonempty-root law; no output-dependent reference choice',
          'entropy and costs in bits; gamma=6/5; structural cost exponents handled exactly',
          'R is the complete surrogate residual; h2(variance) and K_ref I remain outside it'],
     'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A007'],
     'proof_source':{'path':str(root/'LIFT.md'),'certificate':str(root/'out'/'EXACT_CHECK.json')},
     'proof_dependencies':[{'source':str(forest),'sha256':sha(forest),'locators':['eq:forestcost','eq:forestconditioning','thm:posteriorforest'],'status':'SOURCE_COMPLETE_BASELINE'},
          {'claim_id':adopted['claim_id'],'version':1,'status':'A007_INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE','use':'computation of base posterior masses only; lift injection and payment independently proved'}],
     'review_records':[],'status':'AUTHOR_PROVED_EXACTLY_CHECKED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
     'first_unproved_line':None,'next_consumers':['A006','A008','A009','A014','A015','A086','A094','B02','B03','B20']}
claims=[adopted,new]
assert adopted['exact_statement']==original['exact_statement'] and adopted['statement_sha256']==original['statement_sha256']
write_json(root/'CLAIMS.json',claims)

nextaction='Pay the signed Psi joint label/congestion functional by distributing selected core coordinates across existing data owners, using determinant-moment mass and preserving an invertible actual-trace map; A086/A094 independently review this root lift.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':root.name,'stream':'B02','packet_id':'A007',
    'gap_id':'C020/PI-J-JOINT-COST','attempt_id':'A007-stage3-actual-root-lift',
    'method':'Independent whole-claim determinant review; inverse-trace activation injection; exact rising-factorial event counts; binomial/Jensen rank payment with signed normalization retained',
    'mathematical_delta':'A006 determinant moment v1 independently accepted without repair. Generic signed-prime activation preserves all base data witnesses. Exact normalized mass transfer reduces new debt to Psi; rank and extra core-empty rarity paid by (7/2)p I(g), core rank and core-only normalization by (6/5+log2(e)/4)I_core. 28,708 exact assertions PASS. No universal Psi bound.',
    'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SCOPED_INTERFACE_PROVED_FULL_FEI_AND_UNIVERSAL_PIJ_OPEN',
    'claim_versions_used':[{'claim_id':adopted['claim_id'],'version':1,'status':adopted['status']},
          {'source':str(forest),'sha256':sha(forest),'status':'SOURCE_COMPLETE_BASELINE'}],
    'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'status':c['status']} for c in claims],
    'source_artifacts':['REPORT.md','LIFT.md','REVIEW_A006.md','FROZEN_SPEC.json','REVIEW_SPEC.json','code/check_lift.py','code/check_review.py','code/finalize.py','out/PILOT.json','out/PILOT_REPAIR.md','out/EXACT_CHECK.json','out/REVIEW_CHECK.json','out/SOURCES.json','out/RECEIPTS.json'],
    'next_consumers':new['next_consumers'],'next_action':nextaction,'stagnant_substantive_attempts':0,
    'blockers':['Psi<=K I(F) remains unproved for arbitrary overlapping prime tables','new narrow continuation is pending independent review; local acceptance is not shared-registry adoption','remote mirror not verified; supervisor owns publication'],
    'packet_ids':['A007']}
write_json(root/'PROGRESS.json',progress); write_json(root/'PACKET_DELTA.json',progress)

report="""# A007 stage 3: actual root lift and paid activation ranks

## exact target, quantifiers, hypotheses and units

Bridge C020 / PI-J (the B02 lead target). For every nonconstant finite Boolean g=2B-1 represented by all signed prime conjunctions, fix positive feasible lambda and one full physical support order per gate. For every r>=1, activate through a fresh common positive conjunction: F=2A_r B-1, p=2^-r. Fix beta in (0,1] with beta sum lambda<=1 and use the exact activated prime table, lambda'=beta lambda and core-first orders. All references are chosen globally, before the Fourier set. Costs are bits; gamma=6/5; F rank discrepancies use natural logarithms only in the source notation. This stage proves an exact actual-event mass lift and a quantitative payment of all new physical rank and extra empty-core rarity. It does not prove generic activation FEI closure or universal PI-J.

With R_g,R_F the complete optimized surrogate residuals (including v log D but excluding h2(v) and K_ref I), and Psi the explicit signed joint functional in LIFT.md, the result is

    R_F <= p R_g + (7/2)p I(g) + [6/5+log2(e)/4]I_core(F) + Psi.

I_core(F)=2rp E B. The still-unpaid Psi retains gate scaling, congestion, root-removal credit and entropy of added actual events. No negative normalizer is discarded.

## sources actually read, revisions and theorem locators

Read BOARD.md at stage start and reread its 2026-10-13 22:15 UTC snapshot, B02 STREAM_NOTES.md v2 (2026-10-11 23:35 UTC), and own STATUS/LEARNED/WORKLOG. Read execution protocol revision 2026-10-11-execution-v2 in full. Read A006 stage-3 REPORT, CLAIMS and FOREST_MOMENTS.md, all determinant/moment clauses; read A009 stage-2 REPORT, its affine-prime full residual and linear-hypergraph transfer (T); read A086 stage-2 review records relevant to prior A007 acceptance. Reread forests.tex actual queue definition, source-SCC partition forests, eq:forestcost, eq:forestconditioning and thm:posteriorforest. Source hashes are in out/SOURCES.json. Prior-stage public-paper baseline remains inherited, not claimed as newly reread.

The lead's original review-A009/activated-tribes assignment was completed in stage 2. A009 has now paid the affine-plane whole-set residual at its stated q>=16 scope, so the previous coordinatewise affine pressure is not a PI-J obstruction and repeating that family would duplicate work. A006 supplies a new exact mass dependency. This stage reviews that entire dependency before continuing the existing root-normalization packet. It does not claim the stream-wide review cap has disappeared or open another broad FEI candidate; its narrow continuation leaves the same C020/PI-J gap explicit.

## complete derivation or exact first unsupported line

The complete analytic proof is LIFT.md. For each base actual forest and selected nonempty core U, choose an old root to own U; preserve every data assignment, edge attachment and within-coordinate child sequence, and connect all other former roots through selected core coordinates. Deleting core-attached edges and replaying the old fixed queue order recovers the unique base event. Therefore the construction counts distinct actual generator events. Its added multiplicity is (c-1)! binom(|U|+c-2,c-1), rather than |U|^(c-1).

The selected mass is p S(T)G_U(T). For empty selected core this equals the full partition-forest mass by a bijection; for nonempty selected core it is a lower bound on full mass. For core-only sets, summing one-gate outcomes gives p beta a 2^(-C_U). Keeping log D'=Lambda'+log Z' yields exact normalizer log[D'/(pD)] and the signed bound <=log beta only after the identity is tested. The core-only rare-root/name block cancels to delta' in [0,p beta a log e].

The quantitative refinement bounds private rank shift pointwise by gamma |T|log(r/|U|), then averages over the binomial selected core. The exact reciprocal-binomial identity removes any log r loss, paying all new private ranks by 3p I(g). Extra empty-core roots cost <=p I(g)/2. Core ranks across both data and core-only sectors total <=(6/5)I_core(F); core-only normalization costs <=(log e/4)I_core(F). The remaining signed Psi is defined with the SAME base posterior, preserving congestion and scale labels rather than optimizing those pieces separately.

The first unsupported line is Psi<=K I(F), with a dimension-independent K, for suitable globally fixed feasible weights on arbitrary overlapping signed prime tables. A paid base R_g alone does not supply it. It is not part of the claimed theorem. REVIEW_A006.md independently reconstructs the whole determinant-moment claim, including actual chronology, rational bounds, SCC factorization boundary and positive-mass sharpness, with no repair. Its local acceptance does not imply an all-dimensional influence bound.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs FROZEN_SPEC.json and REVIEW_SPEC.json were saved before their jobs. Pilot: all four nonconstant labelled monotone n=2 prime tables, r=1, completed in 0.014 seconds with 247 assertions after correcting a Walsh sign convention in the first attempt (out/PILOT_REPAIR.md). No mathematical statement was altered. Main domain: all 22 labelled nonconstant monotone prime tables at n=2,3, each r=1,2,3, all covered nonempty data sets and eligible ownership assignments. No symmetry reduction, random search or automatic dimension increase. Main completed in 0.186 seconds: 27,571 assertions; 66 activated truth tables, 123 assignments, 127 root minors/base events, 2,036 lifted events and 396 core-only events.

Arithmetic is integer truth tables/FWHT, exact rational influence/normalizers, integer sparse determinant polynomials, explicit parent/attachment/child-sequence enumeration, and formal weights z^gamma with rational z. Irrational structural weights were never rounded or called rational. The quantitative rank inequalities and reciprocal-binomial identities are tested rationally in the same fixed domain. The all-r extension is the analytic proof, not an extrapolation of the finite run.

Targeted independent review checks forced sunflowers e=1,...,5, all 81 K4 full-set assignments, and all eight heterogeneous {01,12,023} full-set assignments: 1,137 assertions; 164 minors, 374 actual events, 64 nontrivial factorial moments and five sharp positive-Fourier-mass examples. Its observed runtime was 0.043 seconds. The frozen heterogeneous pre-count was mistakenly four; actual count is 2*2*2*1=8 and no domain changed, as recorded in REVIEW_CHECK.json. Aggregate successful full checks: 28,708 assertions. These counts exclude earlier pilot assertions and the superseded pre-refinement main output.

Reproduction commands, from this run directory:

    python -X utf8 code/check_lift.py --pilot --out out/PILOT.json
    python -X utf8 code/check_lift.py --out out/EXACT_CHECK.json
    python -X utf8 code/check_review.py
    python -X utf8 code/finalize.py

Both jobs were estimated below 100 MB, so the >300 MB memok trigger did not apply. One job ran at a time, each below the frozen 60-second limit. No GPU, git, network messaging, brain mutation or shared-file write was used. Memory estimate is not a measured peak.

## proof dependencies and changed downstream conclusions

A006-ACTUAL-FOREST-DETERMINANT-MOMENT-BOUNDS v1 is independently accepted here at its unchanged exact statement and hash. The review reconstructs all clauses and supplies no repair; A007 is an independent reviewer rather than contributor to that source version. Its use in this stage computes the correct base posterior mass; the activation injection, binomial rank payment and signed normalizer derivation are separately proved. The original forests.tex source is hash-pinned. A009's new affine theorem is context for dispatch only, not an unreviewed proof premise.

New claim A007-ACTUAL-DATA-WITNESS-ROOT-LIFT v1 is author-proved/exactly-checked and pending A086/A094 review. The stage removes the rank-shift and extra empty-core rare-root debt from the generic activation gap and identifies Psi as the remaining joint payment. It does not refute any Boolean FEI claim, promise generic closure, equate B mass with exact queue probabilities, or assert free selection among reference scales.

## one next mathematical action and independent reviewer

Pay Psi by spreading selected core ownership across the existing used data gates, retaining an invertible actual-trace map and using the accepted determinant moment masses for the resulting posterior. This directly addresses the remaining congestion/scale-label debt at arbitrary overlap. A086 or A094 should reconstruct LIFT.md as a whole, especially recovery of old roots, repeated-slot multiplicity, the rank-stripped posterior and every signed normalizer. A006/A008 can use the explicit J functional; A015 can use the root-conditioned activation interface. No external message was sent.

## actual persistence receipts or precise save blocker

All run artifacts are written only under A007's authorized stage directory; STATUS.md is current and WORKLOG.md/LEARNED.md appended. out/RECEIPTS.json records SHA256 and sizes of run artifacts and rolling files. code/finalize.py verifies exact protocol fields, matching PROGRESS/PACKET_DELTA, preserved reviewed statement/hash, the 20 MB file cap and on-disk receipt hashes. Local persistence is complete. Supervisor GitHub/brain copying is not performed or verified here. No save blocker.

## Universal bridge

This stage moves C020 whole-set witness cost / the lead's PI-J target by supplying an invertible generic actual-forest activation lift, exact rising-factorial event credit and signed nonempty-root normalization, then paying all added physical rank and core-empty rarity by (7/2)p I(g) and core rank/normalization by [6/5+log2(e)/4]I_core(F). A006's whole determinant interface now has an independent reconstruction. The precise remainder is Psi, the signed joint congestion/scale-label functional with actual root-removal credit; full FEI still requires its arbitrary-overlap influence payment and a universally paid base reference. NEXT spreads core ownership to attack that same functional with the accepted determinant mass, rather than adding an isolated class estimate, because it targets the exact remaining obstruction to composition of a universal PI-J reference.
"""
(root/'REPORT.md').write_text(report,encoding='utf-8')
(agent/'STATUS.md').write_text('STATE: A007 stage 3 complete: A006 determinant-moment v1 independently accepted; actual data-witness root lift and all added activation ranks paid; 28,708 exact assertions PASS; Psi/universal PI-J/FEI OPEN; new proof review pending.\nNEXT: Pay signed Psi label/congestion debt by distributing core ownership over existing data gates with an invertible actual-trace map and determinant posterior; A086/A094 review LIFT.md.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+timestamp+' -- Stage 3: read new B02 board, consumed A009 affine closure as dispatch context, independently reconstructed A006 entire determinant-moment v1 without repair. Derived actual witness-preserving activation lift with rising-factorial added event multiplicity and exact signed normalizer. Binomial averaging pays all new ranks and extra core-empty rarity; signed joint Psi remains unpaid. Full fixed-domain checks: 28,708 assertions, 66 Boolean activations, 2,036 lifted events. Corrected initial Walsh sign convention and heterogeneous pre-count; no mathematical repair. All artifacts saved locally; supervisor mirror unverified.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('''\n## Stage 3 durable additions

- A006 determinant factorial-moment v1 independently reconstructed as a whole with no repair. Keep incoming Laplacian orientation, one root per ORIGINAL source SCC, h! local label multiplicities, and fixed coordinate/root order. Factor the SCC polynomial, never expectations of factors sharing attachment variables.
- A generic signed-prime activation can preserve every old data witness: assign all selected core coordinates to one old root and attach other roots through core coordinates. Delete these edges to invert the actual trace. Multiplicity is (c-1)! binom(u+c-2,c-1), not u^(c-1).
- Selected activated mass is p S(T)G_U(T); full equality only at empty selected core. Core-only single-gate summed mass p beta a 2^(-C_U) cancels both root rarity and gate name to delta'=log[D'/(p beta a)].
- Retain exact log[D'/(pD)] before bounding it by log beta. Scaling old feasible lambda requires beta sum lambda<=1 for new shared-core incidence; beta label debt is real and stays in Psi.
- All activation physical rank is paid generically: private shift <=3p I(g), fresh core rank <=(6/5)I_core(F). This uses pointwise rank ratio <=r/u and binomial reciprocal identities, not a conditional uniformity claim about overlapping data gates.
- Extra empty-core root rarity <=p I(g)/2; core-only delta' <=(log2(e)/4)I_core(F). Therefore R_F<=pR_g+(7/2)pI(g)+(6/5+log2(e)/4)I_core(F)+Psi. Exact Psi in LIFT.md keeps congestion, scale labels, root-removal credit and repeated-slot event entropy. Psi<=K I(F) is the first unpaid line.
- A009 paid the affine-plane whole-set PI-J residual q>=16 at its reported scope. Old coordinatewise pressure is not a PI-J failure. Next use distributed core ownership and determinant posterior masses to pay the arbitrary-overlap Psi, not another affine calibration.
''')

protocol=json.loads((reports/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
claim_fields=set(protocol['required_per_run']['claim_fields'])
progress_fields={f.split(' (')[0] for f in protocol['required_per_run']['progress_fields']}
assert set(progress)==progress_fields
assert all(set(c)==claim_fields for c in claims)
assert json.loads((root/'PACKET_DELTA.json').read_text(encoding='utf-8'))==progress
assert all('## '+field in report for field in protocol['required_per_run']['report_fields'])
assert report.rstrip().split('## Universal bridge\n')[1].count('\n')==1
receipts=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name!='RECEIPTS.json':
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
    p=agent/name; receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
write_json(root/'out'/'RECEIPTS.json',{'timestamp_utc':timestamp,'local_only':True,'protocol_schema':'PASS','files':receipts})
for receipt in receipts: assert sha(receipt['path'])==receipt['sha256']
print(json.dumps({'status':'PASS','claims':len(claims),'receipt_files':len(receipts),'run':str(root),'full_fei':'OPEN'}))
