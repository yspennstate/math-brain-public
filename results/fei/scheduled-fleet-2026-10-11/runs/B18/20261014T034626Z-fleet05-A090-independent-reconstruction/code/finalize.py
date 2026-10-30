import json, hashlib
from pathlib import Path
from datetime import datetime, timezone
root=Path(__file__).resolve().parents[1]; agent=root.parents[1]
def save(name,obj):
    (root/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
statement=('For every even d>=4 and every Boolean sign g on r>=1 disjoint physical bits, let '
'b(y)=(-1)^(sum_j y_(2j-1)y_(2j)), delta=2^-d, t=2^(-d/2), and F=b(y)+1[y=0](g(x)-1). '
'Write hat b(R)=sigma_R t and a_V=hat g(V). For each relevant gate query i, retaining '
'the residual gate mask V and sigma_R preserves the complete normalized derivative/reference KL exactly. '
'Retaining only V loses influence-weighted KL L_i=delta a_i^2 D0_i, where '
'D0_i=sum_sigma N_sigma delta log2(rho_i/c_(i,sigma)), '
'N_sigma=(2^d+sigma 2^(d/2))/2, rho_i=1-delta+delta(a_empty^2+a_i^2), '
'c_(i,sigma)=(sigma+t(a_empty-1))^2+delta a_i^2. '
'The combined gate-row losses satisfy 0<=sum_i L_i<=2delta sum_i a_i^2<=2delta '
'<=Inf_(y_1)(F)/4, and Inf_(y_j)(F)=1/2+delta(1-a_empty). '
'This is a dedicated single reserve for precisely these quotient losses; no other charge, '
'universal terminal payment, non-flat-core extension or full FEI conclusion is asserted.')
claim={
 'claim_id':'A090-ARBITRARY-GATE-SIGNED-REFUND-PARTITION','version':1,
 'exact_statement':statement,
 'hypotheses':['Uniform finite physical Boolean cube; entropy and KL in bits',
 'Even d>=4; specified quadratic bent core; any r>=1 and any Boolean gate on disjoint bits',
 'Complete row laws mu_i(T)=p_(T+i)/e_i and r_i(T)=p_T+p_(T+i); irrelevant queries omitted',
 'If a_i=0 the exceptional derivative cell has zero weight; no conditioning of reference on derivative support',
 'The reserved quarter of Inf_(y_1) is dedicated only to the sum of the specified quotient losses'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),
 'contributors':['A090'],'proof_source':{'path':str(root/'DERIVATION.md'),'locator':'Signed conditional partition for arbitrary gates; complete derivation and single physical reserve'},
 'proof_dependencies':[], 'review_records':[],
 'status':'AUTHOR_PROVED_SCOPED_LEMMA_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['A096','A001','A073','A098','A099','B18','B20']}
save('CLAIMS.json',[claim])
summary=json.loads((root/'out'/'check.json').read_text())
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':root.name,
 'stream':'B18','packet_id':'A090','gap_id':'OPEN-C018-TERMINAL-KL','attempt_id':4,
 'method':'Independent Walsh-amplitude reconstruction; exact signed likelihood partition; Parseval summed reserve; integer truth-table validation',
 'mathematical_delta':'Generalized the explicit two-bit positive-erasure quotient to arbitrary Boolean gates over the specified bent core. Full sign/mask partition preserves KL; total sign-deletion loss <=2delta <=one dedicated core quarter-reserve. Terminal payment remains open.',
 'deliverable_status':'COMPLETE_LOCAL_FILES_SAVED',
 'mathematical_status':'SCOPED_LEMMA_AUTHOR_PROVED_PENDING_REVIEW_FULL_FEI_OPEN',
 'claim_versions_used':['A073-NONZERO-ERASURE-BINARY-REMAINDER@1 (source statement and special-case comparison; not a proof dependency)','A096-SINGLE-SPECTATOR-REFUND-OWNERSHIP@1 (source statement and interface context; not a proof dependency)','A090-DEGREE-COARSENED-REFUND-OBSTRUCTION@1 (prior accepted obstruction reported on current BOARD)'],
 'claims_created_or_changed':[claim['claim_id']+'@1'],
 'source_artifacts':[str(root/'DERIVATION.md'),str(root/'FROZEN_SPEC.json'),str(root/'code'/'check.py'),str(root/'out'/'check.json')],
 'next_consumers':claim['next_consumers'],
 'next_action':'A096/A001 integrate signed gate partition into a single terminal ledger; A073/A098 independently audit the arbitrary-gate Parseval reserve and non-flat-core extension obstruction.',
 'stagnant_substantive_attempts':0,
 'blockers':['No globally nonoverlapping reserve for retained gate/core terminal entropy; no complete sufficient signed partition theorem for general non-flat Boolean cores.'],
 'packet_ids':['A090']}
save('PROGRESS.json',progress); save('PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

Independently reconstruct a live complete-reference candidate and report the first unsupported universal implication. New closed scope: every arbitrary Boolean gate g on r>=1 bits attached at a single vertex of the specified quadratic bent core, every even d>=4. Entropy/KL in bits and ordinary physical influence. The signed partition preserves full gate-query KL. Its mask-only quotient losses jointly cost at most 2^(1-d), paid once by a dedicated quarter of one core coordinate's influence. Full FEI remains OPEN; this scoped lemma is author-proved, pending independent review.

# sources actually read, revisions and theorem locators

Read the current BOARD.md, B18 STREAM_NOTES.md and own STATUS.md at stage start. B18 notes remain the old baseline direction; current dispatch consumes a new dependency instead of repeating the closed census or singleton tax. Read the full EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2. Read A096 runs/20261014T013836Z-fleet05-A096-live-gap-ledger/CLAIMS.json, especially A096-SINGLE-SPECTATOR-REFUND-OWNERSHIP@1. Read A073 runs/20261014T023508Z-fleet05-A073-certified-logarithms/CLAIMS.json, especially A073-NONZERO-ERASURE-BINARY-REMAINDER@1. Reconstructed amplitudes and the arbitrary-gate extension before comparing A073 DERIVATION.md, sections Nonzero-erasure Boolean boundary family and First unsupported universal line. Earlier original-source reading is preserved in prior run reports; no new paper theorem is invoked here. Board reports A081 independently accepting our degree-refund obstruction, so it is not repeated. A098 already reviewed A073's specific family; this stage extends its hypotheses rather than duplicating that review.

# complete derivation or exact first unsupported line

Complete derivation is in DERIVATION.md, with one exact claim in CLAIMS.json. The point mutation yields hat F(R,V)=sigma_R t 1[V=empty]+delta(a_V-1[V=empty]). Query likelihood ratios are constant on (V,sigma_R) fibers, proving signed-partition sufficiency without a product reference. On every nonempty residual gate mask the derivative and reference core laws coincide. The sole loss cell has conditional core likelihood rho_i/c_(i,sigma), bounded by 4 for d>=4. Chain rule gives L_i=delta a_i^2 D0_i, 0<=D0_i<=2. Summed first-level Parseval gives sum_i L_i<=2delta independently of gate dimension. Direct physical edges yield Inf_(y_1)=1/2+delta(1-a_empty), hence the dedicated reserve inequality.

First unsupported universal implication: extend this sufficient partition to a general non-flat core AND pay the retained terminal gate/core charge and all quotient losses with one globally nonoverlapping influence ledger. Equivalently, no finite universal K has been reconstructed for sum_i e_i D(mu_i||r_i)>=sum_i e_i log2(1/e_i)-K I(F). The arbitrary gate remains in the quotient laws; small coarsening loss does not pay its terminal charge. The reserve statement assigns no activation, core-entropy or other charges to the same quarter.

# executed validation with domain, arithmetic, commands and outputs

Frozen spec FROZEN_SPEC.json preceded all computation. No symmetry reduction. Pilot: every labeled r=1,2 gate with d=4, 20 cases, 3387 assertions, 0.030 seconds. Main: every labeled r=1,2,3 gate with d=4 and every r=1,2 gate with d=6, {summary['cases']} cases, {summary['exact_assertions']} assertions, {summary['elapsed_seconds']:.3f} seconds, maximum physical dimension {summary['maximum_dimension']}. All PASS; {summary['genuine_nonproduct_cases']} cases have genuinely distinct core-sign conditional reference values on a positive derivative cell. Integer Walsh transforms and Fraction arithmetic independently verify actual Boolean spectra, Parseval, physical edges, complete references and quotient normalizations, fiberwise likelihood equality, the exact exceptional-cell formulas and rational likelihood/reserve bounds. Logs need no numerical approximation: ratio<=4 proves KL<=2. Analytic quantifiers are supplied separately by the proof; finite checks do not extrapolate to arbitrary r or d.

Commands: python -X utf8 runs\\{root.name}\\code\\check.py --pilot; python -X utf8 runs\\{root.name}\\code\\check.py. Outputs out/pilot.json and out/check.json. Estimated memory below 80 MB; no job expected above 300 MB, so memok not triggered. No background process, GPU, automatic dimension escalation or heavy job.

# proof dependencies and changed downstream conclusions

The new proof uses elementary Walsh expansion, KL chain rule, Parseval and actual physical edge counting, with no unproved campaign dependency. It specializes to A073's binary family for d>=4, reproducing its exact conditional formula but making no new full-scope acceptance entry for the already reviewed special case. It supplies A096/A001 a complete non-product signed conditional partition and a dimension-free combined reserve for arbitrary gates over this core. It does not invalidate our prior degree-refund obstruction: the sign partition explicitly retains information that degree compression could discard. Shared-selector and activation budgets remain separate unresolved obligations.

# one next mathematical action and independent reviewer

A096/A001 should integrate this signed partition into one terminal ledger and identify exactly which retained charge consumes the remaining core slack; A073/A098 should independently reconstruct this arbitrary-gate theorem. The next mathematical question is whether a non-flat core admits a similarly complete likelihood partition with a provably available reserve, rather than assuming alphabet size controls refund. No messages were sent to other agents; these are source-bound handoffs in saved artifacts.

# actual persistence receipts or precise save blocker

All artifacts are saved only inside the assigned A090 run and rolling files. out/schema.json records exact protocol-field, hash and compatibility-copy validation; out/manifest.json records sizes and SHA256 digests. Local save is verified. No mirror adoption, external upload, independent acceptance of the new claim or campaign closure is asserted. No save blocker.

**Universal bridge:** This stage moves C018 erasure/terminal refund and C024 history transfer by constructing a complete sufficient signed partition for every Boolean gate on the specified bent core, plus a joint quotient-loss bound <=2^(1-d) with one isolated physical reserve. The remaining universal bridge is simultaneous payment of the retained terminal charge and all historical charges for arbitrary non-flat cores. NEXT integrates this exact conditional row into the live terminal ledger; it targets the known missing refund information and budget ownership directly, rather than adding another FEI class bound.
'''
(root/'REPORT.md').write_text(report,encoding='utf-8')
(agent/'STATUS.md').write_text('STATE: Stage 4 complete: arbitrary-gate signed partition preserves full KL; summed mask-quotient loss <=2^(1-d) fits one dedicated core quarter-reserve; 140237 exact checks PASS; review pending; FEI OPEN.\nNEXT: A096/A001 integrate retained signed terminal row into one ledger; A073/A098 independently audit arbitrary-gate Parseval reserve and test a non-flat-core extension.\n',encoding='utf-8')
stamp=datetime.now(timezone.utc).isoformat()
for filename,entry in [
 ('WORKLOG.md',f'\n{stamp} Stage 4 ({root.name}): consumed A073 positive-erasure statement and A096 spectator ownership interface. Reconstructed arbitrary-gate bent-core partition before source proof comparison. Signed residual mask/sign preserves complete KL; mask-only loss sums to <=2delta by first-level Parseval. All 296 frozen cases passed 140237 exact assertions in 6.627 s. New scoped lemma pending independent review; retained terminal/global ledger remains unpaid.\n'),
 ('LEARNED.md','\nStage 4 durable fact: for F=b_d+1[y=0](g-1), even d>=4, any Boolean gate g, complete gate-query likelihood depends only on residual gate mask V and bent Fourier sign sigma_R. Forgetting sigma loses only the V=empty conditional KL: L_i=delta a_i^2 D0_i. Since c_sigma>=(1-2sqrt(delta))^2>=1/4 and rho<=1, D0_i<=2; sum_i L_i<=2delta sum_i a_i^2<=2delta<=Inf_(y_1)(F)/4. This quarter is a dedicated reserve only for these losses. Sufficiency and a bounded lost remainder do not pay the retained terminal charge or provide a universal non-flat-core partition.\n')]:
    with (agent/filename).open('a',encoding='utf-8') as f: f.write(entry)
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
cf=protocol['required_per_run']['claim_fields']; pf=protocol['required_per_run']['progress_fields']
pf=[x.split(' (')[0] for x in pf]
assert set(claim)==set(cf); assert set(progress)==set(pf)
assert (root/'PROGRESS.json').read_bytes()==(root/'PACKET_DELTA.json').read_bytes()
assert claim['statement_sha256']==hashlib.sha256(claim['exact_statement'].encode()).hexdigest()
assert all(h in report for h in protocol['required_per_run']['report_fields'])
save('out/schema.json',{'status':'PASS','claim_fields_exact':True,'progress_fields_exact':True,'compatibility_identical':True,'statement_sha256_verified':True,'report_fields_present':True})
manifest=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name!='manifest.json':
        raw=p.read_bytes(); assert len(raw)<20*1024*1024
        manifest.append({'path':str(p.relative_to(root)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
for p in [agent/'STATUS.md',agent/'WORKLOG.md',agent/'LEARNED.md']:
    raw=p.read_bytes(); manifest.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
save('out/manifest.json',manifest)
print(json.dumps({'status':'SAVED_AND_SCHEMA_PASS','run':str(root),'claim':claim['claim_id'],'files_hashed':len(manifest)}))
