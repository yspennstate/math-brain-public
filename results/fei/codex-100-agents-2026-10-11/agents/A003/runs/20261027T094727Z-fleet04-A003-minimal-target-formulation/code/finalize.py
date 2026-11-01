from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def put(p,s):p.write_text(s,encoding='utf-8')
def js(p,x):put(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
run=R.name
proto=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
checks=json.loads((R/'out/EXACT_CHECKS.json').read_text(encoding='utf-8'))
audit=json.loads((R/'out/INDEPENDENT_IMPLEMENTATION_AUDIT.json').read_text(encoding='utf-8'))
old=A/'runs/20261023T144012Z-fleet03-A003-minimal-target-formulation/IMPLICATIONS_BASELINE.md'
put(R/'IMPLICATIONS_BASELINE.md',old.read_text(encoding='utf-8'))
statement=('For every nonconstant uniform Boolean seed f, let F_m be its m-fold disjoint product. '
 'Sublinear total defects in B(F_m)<=lambda H(F_m)+K I(F_m)+o(m), lambda<1, imply the exact seed inequality and FEI((K+2/ln2)/(1-lambda)). '
 'Vanishing local defects in eligible-coordinate B or signed L selection imply the exact seed selection, with constants stated in DERIVATION.md. '
 'Complete reference CE(p_Fm,Q_m)<=C m I(f)+o(m) implies FEI(C). '
 'Under the fixed admitted witness identity h2(v)+Kref I+R*=H+vD(Pplus||U), U a subprobability and Kref=3+2log2(3)+log2(6e), '
 'admitted choices for an unbounded sequence m with R*(F_m)<=K m I(f)+o(m) imply FEI(Kref+K), improving the prior conservative sufficient constant by 2. '
 'All constants precede all seeds; errors may depend on the seed; all required constructions are hypotheses, not asserted universal suppliers.')
claim=dict(zip(proto['required_per_run']['claim_fields'],[None]*len(proto['required_per_run']['claim_fields'])))
claim.update(claim_id='A003-TENSOR-DEFECT-WITNESS-CONSTANT',version=1,exact_statement=statement,
 hypotheses=['Uniform finite Boolean cubes; disjoint product tensors; all seeds; an unbounded tensor sequence for each seed.',
 'lambda<1; 0<c<1; tau>0 for weak eligible-coordinate variants.',
 'Complete normalized source references or the ORIGINAL fixed admitted subprobability witness interface; no discarded terminals/query-KL/old bills.'],
 statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),contributors=['A003'],proof_source='DERIVATION.md',
 proof_dependencies=['Inherited A003 stage1 fixed witness identity; verbatim IMPLICATIONS_BASELINE.md',
 'B01 erasure-fraction and low-influence localization, STREAM_NOTES.md v1',
 'C007 exact signed Booleanity; elementary Fourier product and finite probability identities'],
 review_records=[{'reviewer':'A003','kind':'author proof and distinct implementation audit','verdict':'HOLDS_AT_STATED_CONDITIONAL_SCOPE','independent_agent':False},
 {'reviewer':'Lean tool admission','verdict':'SETUP_UNVERIFIED; compute admission held; no compiler started'}],
 status='AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=[],
 first_unproved_line='Construct the required fixed witnesses/references or eligible coordinate for EVERY Boolean core with one absolute price and the specified vanishing defect.',
 next_consumers=['A004','A086','A094','B01','B20'])
js(R/'CLAIMS.json',[claim])
progress={
 'protocol_revision':proto['revision'],'run_id':run,'stream':'B01','packet_id':'A003','gap_id':'UNIVERSAL-CORE-SOURCE-PRICE',
 'attempt_id':'A003-stage22-tensor-defect-witness-constant','method':'Asymptotic defect removal; fixed witness binary-overhead elimination; exact rational and symbolic-prime-log audits',
 'mathematical_delta':'Fixed witness implication improves from FEI(2+Kref+K) to FEI(Kref+K). Total o(m) overhead is allowed; local coordinate error must vanish. No arbitrary-core payment proved.',
 'deliverable_status':'COMPLETE_LOCAL_VERIFIED','mathematical_status':'AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW; FULL_FEI_OPEN',
 'claim_versions_used':['A003 stage21 IMPLICATIONS_BASELINE fixed witness identity','B01 STREAM_NOTES v1 erasure-fraction/localization','C007'],
 'claims_created_or_changed':['A003-TENSOR-DEFECT-WITNESS-CONSTANT@1'],
 'source_artifacts':['DERIVATION.md','TARGETS.md','IMPLICATIONS_BASELINE.md','out/SOURCES.json','out/EXACT_CHECKS.json','out/INDEPENDENT_IMPLEMENTATION_AUDIT.json'],
 'next_consumers':['A004','A086','A094','B01 lead','B20'],
 'next_action':'Construct original fixed whole-set witnesses for EVERY f^tensor m with R* <= 4m I(f)+A_f log2(1+m), retaining physical-query KL, complete terminals and original normalizers; first audit the tightened constant independently.',
 'stagnant_substantive_attempts':0,
 'blockers':['Universal structural payment/source construction open','Independent review pending','Lean admission held; no formal certificate','Mirrors unverified','Wake identity/state/dream freshness degraded'],
 'packet_ids':['A003']}
js(R/'PROGRESS.json',progress);js(R/'PACKET_DELTA.json',progress)
put(R/'TARGETS.md','''# Fixed targets and exact constants

All information is in bits. Constants precede every dimension and seed. Let c0=2/ln2 and Kref=3+2log2(3)+log2(6e). DERIVATION.md gives the complete definitions, quantifiers and proof. These are sufficient targets, not proved universal inputs.

| Route | Fixed unpaid structural target | Sufficient FEI constant |
|---|---|---|
| Weak erasure | If max Inf<1/4, choose i with Inf_i>=I/(2d) and B_i<=4Inf_i | 4+c0 |
| Erasure fraction | B<=lambda H+KI, lambda<1 | (K+c0)/(1-lambda) |
| Signed Booleanity | Under EVERY exact convolution equation, choose relevant i with L_i<=4Inf_i | 4+3/ln2 |
| Fixed whole-set witness | Construct admitted witnesses for every F_m with R*<=4mI(f)+o(m) | Kref+4 (previous conservative bound Kref+6) |
| Full-reference supplier | Construct normalized complete Q_f,m with CE<=C mI(f)+o(m) | C |

The witness row retains the original admissible family and its normalizers; its full definition is in DERIVATION.md and the copied baseline. It is stronger than unrestricted matching-reference existence. No same-constant converse from FEI is asserted for these prescribed structural targets. An unspecified finite eligible-coordinate price or unrestricted source-existence claim remains a finiteness equivalence.

The new relaxation is precise: logarithmic TOTAL overhead is harmless on product powers. Logarithmic LOCAL coordinate error is not removed by product replication. Exact tensor products also preserve every seed's high-average eligibility and low-influence cutoff. A product of imperfect references keeps its KL bill linear, so this relaxation does not pay an arbitrary source by itself.
''')
report=f'''# A003 stage22: remove tensor overhead and tighten the witness constant

## exact target, quantifiers, hypotheses and units

Compare fixed whole-set witnesses, good-coordinate erasure and exact signed Booleanity with all constants explicit. The conditional witness implication improves from H<=(2+Kref+K)I to H<=(Kref+K)I, where Kref=3+2log2(3)+log2(6e). This change removes a bounded binary-entropy overhead on tensor powers; it does not prove the unpaid witness residual inequality. All information is in bits. The full FEI conjecture remains OPEN. Exact new statement and quantifiers are in CLAIMS.json; TARGETS.md is the compact diagram.

## sources actually read, revisions and theorem locators

Execution protocol2026-10-11-execution-v2 read completely; current BOARD timestamp2026-10-27 09:54UTC and B01 STREAM_NOTES v1; A003 STATUS/LEARNED and stage20/21 derivation and implication baseline; A001/A002/A004 current statuses. Campaign README/status/claim/obstruction/packet/action registries and plan, supplemental campaign/claims/counterexamples/seed/mapping, sources inventory, and the four requested paper text versions were loaded with selected relevant locators. out/SOURCES.json pins actual bytes and out/INTAKE.md gives the selections. This is not a fresh full audit of every paper. No external-paper theorem is a new proof premise. The fixed witness identity is copied verbatim in IMPLICATIONS_BASELINE.md, subsection beginning “For the conditioned posterior-forest route”. B01 supplies the inherited erasure and weak-coordinate implications; full signed Booleanity is C007. Brain recall supplied normalization/Booleanity warnings only, not proof authority.

## complete derivation or exact first unsupported line

DERIVATION.md gives the all-dimensional author proof. F_m has product squared spectrum, H_m=mH and I_m=mI; each local B_i,L_i,Inf_i repeats. Total o(m) defects disappear by division, but local defects must tend to zero. High-average eligibility and the low-influence cutoff are preserved. The ORIGINAL witness identity gives H(F_m)<=h2(v_m)+Kref mI+R*(F_m). Since h2(v_m)<=1, R*<=K mI+o(m) implies H<= (Kref+K)I. This saves exactly2 against the old one-function estimate h2(v)<=2I. The complete-reference alternative follows from CE>=H. Fixed imperfect product references retain mD(p||Q), so their unpaid mismatch survives. A rational non-Boolean family satisfies normalization but violates a nonzero-shift convolution equation and has H/I unbounded, checking the necessity of exact Booleanity.

The FIRST unsupported line is a noncircular construction of the admitted whole-set tensor witnesses or complete references at a fixed absolute linear price with sublinear overhead, for EVERY Boolean seed. No finite census, local reset, chosen exact-match reference or padding admission supplies that line. The tightened constant is a conditional interface consequence, not an independent solution of C020.

## executed validation with domain, arithmetic, commands and outputs

Both specifications were saved before their bounded loops. Main: all278 Boolean tables n0..3, m2,3, no symmetry, integer character sums and exact Fraction identities: {checks['exact_assertions']} predicates on556 tensor cases PASS in {checks['seconds']:.3f}s. It checks normalized spectra, all signed autocorrelations, exact marginals, homogeneous fibre kernels, influence and eligible-coordinate replication. Audit: independently evaluate physical products for every n<=2 table; direct Walsh transform; represent H,B,L and relative entropy as exact rational coefficients of prime logarithms. {audit['exact_assertions']} predicates on44 physical products and32 rational non-Boolean controls PASS in {audit['seconds']:.3f}s. Exact symbolic equality proves the finite identities; no floating sign is a certificate. These are two implementations by A003, not independent-agent acceptance. Each job stayed below the55s pilot cap and estimated40MB; no >300MB admission or heavy job was used. Commands: python -X utf8 <run>/code/stage22.py and audit22.py. The Lean helper rejected compute admission (hung-window/free-memory gate), so no compiler started; formal status is UNVERIFIED and no retry was made. Rung: author proof with exact finite algebra validation, independent review pending.

## proof dependencies and changed downstream conclusions

One scoped candidate is created. Baseline tensor and Booleanity identities are not claimed as new. The witness implication's sufficient constant drops by2 because bounded binary entropy is amortized rather than charged to each seed influence. The coordinate and signed constants stay unchanged. Universal source payment remains open; normalized references must retain the vacuum, support, old debits, BOTH terminal liabilities and all query KL in any claimed source bill. A001's current query-KL warning is retained. Prior accepted A003 stage19/20 claims are untouched.

## one next mathematical action and independent reviewer

Have A004 or A086 independently reconstruct the sharper witness implication from the exact baseline identity, with A094 checking quantifiers and full-source scope. Then seek original admitted witnesses for every tensor seed with R*<=4mI+A_f log2(1+m). The error coefficient may depend on the fixed seed but the price4 may not. This is a local saved handoff, not a sent message.

## actual persistence receipts or precise save blocker

All four protocol files, derivation, target diagram, copied baseline, code/specifications, exact outputs and source hashes are inside this run. Rolling files are updated. Final readback checks schema fields, claim statement hash, delta byte identity, required artifacts and sizes below20MB; out/VALIDATION.json and out/ARTIFACTS.json are the receipts. No git, messages, brain writes, external mutation, deletion or other-agent edits. The wake reports stale personal-context notes; those were not used as mathematical premises. The resource snapshot's6.6GB free disk supersedes the older hook's2.0GB only as a later measurement, not as a cleanup claim. Shared work was not stopped. Supervisor collection and remote mirrors remain unverified.

**Universal bridge:** C020 gains a sharper exact implication: the fixed residual target costs Kref+K instead of Kref+K+2, and may carry any o(m) total overhead on m product copies. C018 and the signed route gain matching defect scales, preserving eligible-coordinate and weak-influence quantifiers. No universal payment inequality is closed. What remains is the ORIGINAL arbitrary-core witness/source construction. NEXT allows logarithmic bookkeeping that the prior dimension-free additive target unnecessarily forbade, while keeping the full original linear bill; it addresses the universal supplier directly rather than another isolated class or optional reset.
'''
put(R/'REPORT.md',report)
put(R/'out/FORMAL_STATUS.json',json.dumps({'status':'SETUP_UNVERIFIED','output':'Compute admission held (hung window or under 5500 MB free); no new compiler process','scope':'attempted affine arithmetic lemma only; no FEI formalization'},indent=2)+'\n')
put(A/'STATUS.md','STATE: A003 stage22 saved: witness implication tightened by2 to Kref+K; tensor total/local defect scales explicit;405972+544 exact checks PASS;author proof pending review;FEI OPEN.\nNEXT: A004/A086/A094 audit constant; construct ORIGINAL fixed witnesses for EVERY tensor seed with R*<=4mI+o(m), retaining old bills/query KL/BOTH terminals.\n')
stamp=datetime.now(timezone.utc).isoformat()
for name,line in [('WORKLOG.md',f'\n{stamp} stage22: tensor defect mechanism; original exact witness identity removes binary-entropy +2 from sufficient FEI constant. Main405972 and symbolic audit544 exact predicates PASS. Lean admission held, no compiler. Arbitrary-core supplier remains open; no optional reset repeated.\n'),('LEARNED.md','\nA003 stage22: Under the ORIGINAL fixed subprobability witness identity h2(v)+Kref I+R*=H+vD, universal R*<=KI actually implies FEI(Kref+K), saving2 over the one-seed h2(v)<=2I bound: apply to product powers, h2(v_m)<=1, divide by m. More generally R*(f^m)<=KmI+o(m) suffices. Total erasure/source overhead o(m) vanishes; local B_i/L_i errors must vanish because each coordinate price repeats. High-average eligibility and max influence are invariant. Products of a fixed mismatched reference keep linear KL, so logarithmic bookkeeping tolerance does not pay an unpaid source. Author proof pending independent review; full FEI OPEN.\n')]:
    with (A/name).open('a',encoding='utf-8') as fp:fp.write(line)
assert set(progress)=={x.split(' (')[0] for x in proto['required_per_run']['progress_fields']}
assert set(claim)==set(proto['required_per_run']['claim_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert hashlib.sha256(claim['exact_statement'].encode()).hexdigest()==claim['statement_sha256']
for heading in proto['required_per_run']['report_fields']:assert '## '+heading in report
files=[p for p in R.rglob('*') if p.is_file()]
assert all(p.stat().st_size<20_000_000 for p in files)
js(R/'out/ARTIFACTS.json',[{'path':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in files])
js(R/'out/VALIDATION.json',{'status':'PASS','schema_fields':'exact protocol sets','statement_hash':'PASS','delta_byte_identity':'PASS','report_fields':'PASS','artifact_sizes':'PASS','full_FEI':'OPEN','independent_review':'PENDING'})
print(json.dumps({'status':'SAVED_VERIFIED','run':run,'main_checks':checks['exact_assertions'],'audit_checks':audit['exact_assertions'],'new_constant':'Kref+K (was Kref+K+2)','FEI':'OPEN'}))
