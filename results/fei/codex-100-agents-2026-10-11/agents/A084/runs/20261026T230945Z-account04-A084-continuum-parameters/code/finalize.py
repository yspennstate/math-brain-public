from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1];OWN=R.parents[1]
P=Path(r'math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=json.loads(P.read_text(encoding='utf-8-sig'))
def save(name,x):(R/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8',newline='\n')
v=json.loads((R/'out/VALIDATION.json').read_text(encoding='utf-8'))
a=json.loads((R/'out/AUDIT.json').read_text(encoding='utf-8'))
formal=json.loads((R/'out/FORMAL.json').read_text(encoding='utf-8'))
assert v['status']==a['status']=='PASS'
source=Path(r'agents/A075/runs/20261023T133516Z-account03-A075-search-to-theorem-bridge/CLAIMS.json')
orig=json.loads(source.read_text(encoding='utf-8'))[0]
review=dict(orig)
review['review_records']=list(orig['review_records'])+[{'reviewer':'A084','independent_reviewer':True,'verdict':'HOLDS_UNCHANGED','scope':'Independent literal-character exact row reconstruction on1024 full circuits/3072 queries, plus analytic coefficient factorization, exceptional-row cancellation and supplied-credit induction. Source2/ln2 and3 remain valid; new sharp scalar extension is separate.'}]
review['status']='INDEPENDENT_A084_RECONSTRUCTION_HOLDS_UNCHANGED'
statement='For every finite uniform Boolean g and physical coordinate i, mu=E(g),t=ghat({i}),d=Inf_i(g), the full entropy-row decrement L(mu,t) is at most lambda_row*d, where lambda_row is the unique global maximum of ell(b)/b on b in(0,1], ell(b)=L(1-b,b). The maximum occurs at the unique beta in((1-1/sqrt(5))/2,1/2) with beta*ell_prime(beta)-ell(beta)=0. Exact rational certificates give 2<lambda_row<9/4 and the root/price enclosures in ROOT.json and AUDIT.json (approximately2.152204859). This constant is sharp over actual finite Boolean exceptional rows, not asserted optimal for full signed composition drift. For every Boolean composition h(g_1,...,g_r) on disjoint physical blocks, signed correction C=H(F)-sum q_j H(g_j) satisfies mean C_child-C_parent<=lambda_row Inf_i(F). For every fixed real K>=0, U=C+kappa I(F)+sum q_j rho_K(g_j), with kappa=lambda_row or9/4, is a nonnegative full-query superharmonic majorant of(H(F)-KI(F))_+. Supplied credits/old signed labels/full terminals propagate by the stated kernels, including all real surplus D>=0. The rational9/4 envelope saves exactly3I(F)/4 against the source rational3 envelope. Its INITIAL influence price remains FEI-equivalent at every fixed K; no FEI solution is asserted.'
hyp=['Finite uniform physical cubes, outputs +/-1, complete squared-Fourier entropy in bits and ordinary physical influence.','L and eta use continuous zero conventions; scalar certificate covers all real |mu|+|t|<=1, |t|<=d.','Original outer gate/disjoint core partition is fixed under all physical restrictions, constants/dummies allowed.','Rate K>=0 is fixed throughout the history and rho_K is the full finite stopping hull at that same rate.','Credit is actually supplied and every original influence owner remains unused after previous bookings; all stopped siblings, actual reaches and full terminal functions are retained.','No optimality for full signed drift and no universal initial O(I) source are claimed.']
digest=hashlib.sha256(json.dumps({'exact_statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
new={'claim_id':'A084-SHARP-BOOLEAN-ROW-CONTINUUM','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':digest,'contributors':['A084'],'proof_source':['PROOF.md','code/check.py','code/audit.py','out/ROOT.json','out/VALIDATION.json','out/AUDIT.json'],'proof_dependencies':[{'claim_id':orig['claim_id'],'version':orig['version'],'statement_sha256':orig['statement_sha256'],'acceptance':'A084_HOLDS_UNCHANGED','scope':'Exact signed row cancellation and original supplied-bank mechanism; scalar improvement proved separately.'}],'review_records':[],'status':'AUTHOR_ANALYTIC_PROOF_EXACT_CERTIFICATES_EXTERNAL_REVIEW_PENDING','supersedes':[],'refutes':['Universal primitive exceptional-row price2*d; actual4bit witness2^74>3^9*5^25. No full-drift2*Inf claim is refuted.'],'first_unproved_line':'No unsupported line identified within the analytic scalar and supplied-bank theorem; initial arbitrary-core influence payment remains open. Lean admission held, not formal certification.','next_consumers':['A075','A072','A074','A080','A089','A092','A083','B17','B20']}
claim_fields=set(protocol['required_per_run']['claim_fields'])
assert set(new)==set(review)==claim_fields
save('CLAIMS.json',[review,new])
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B17','packet_id':'A084','gap_id':'G-INITIAL-SIGNED-BANK-PRICE','attempt_id':'A084-sharp-Boolean-row-continuum-1','method':'Analytic diamond boundary reduction, unique critical point, exact rational interval root certification, independent literal Boolean reconstruction','mathematical_delta':'Sharp exceptional-row reserve lambda_row approximately2.152204859<9/4 replaces2/ln2; rational full-bank headroom3->9/4 saves3I/4. A075@1 independently HOLDS unchanged. Initial arbitrary-core funding remains OPEN.','deliverable_status':'COMPLETE_LOCAL_EXTERNAL_REVIEW_PENDING','mathematical_status':'COMPONENT_ANALYTIC_PROOF_AND_EXACT_CERTIFICATES; FULL_FEI_OPEN; NO_LEAN_CERTIFICATION','claim_versions_used':[{'claim_id':orig['claim_id'],'version':orig['version'],'statement_sha256':orig['statement_sha256']}],'claims_created_or_changed':[orig['claim_id']+'@1 independent review',new['claim_id']+'@1'],'source_artifacts':['out/INTAKE.json','PROOF.md','out/FROZEN_SPEC.json','out/VALIDATION.json','out/AUDIT.json','out/FORMAL.json'],'next_consumers':new['next_consumers'],'next_action':'A075/A074 independently audit scalar monotonicity and original-owner bank propagation; then fund initial arbitrary indecomposable-core U from an unused ORIGINAL O(I) source or a well-founded decreasing source construction.','stagnant_substantive_attempts':0,'blockers':['Universal original arbitrary-core initial source unpaid.','External review of new scalar extension pending.','Lean checker refused fresh compiler admission: hung window or under5500MB free.','Supervisor mirror/adoption unverified.'],'packet_ids':['A084']}
pf={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==pf
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
report=f'''# A084: a smaller sharp scalar reserve, with initial payment still open

## exact target, quantifiers, hypotheses and units

Every finite uniform Boolean core, every physical coordinate, every real parameter in |mu|+|t|<=1 with |t|<=d, and every fixed real K>=0. Entropy is in bits. The sharp exceptional-row coefficient is lambda_row, with 2<lambda_row<9/4 (approximately2.152204859). Arbitrary gates and disjoint arbitrary active cores inherit the smaller drift reserve. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL revision {protocol['revision']}; current board snapshot2026-10-26 23:10 UTC; B17 STREAM_NOTES v2 (its AND-map direction is stale because A084 stage2 finished it); own STATUS/LEARNED/WORKLOG and prior stage9 proof. Read campaign registries/plan, supplemental campaign files and source notes, both threshold and percolation text versions, with byte hashes/encoding/locators in out/INTAKE.json. Threshold38pp Proposition8.6 is contextual, not a premise for the new proof. Main exact dependency: {orig['claim_id']}@1, statement hash {orig['statement_sha256']}, PROOF sections1-4. A089 stage10 section5 supplies the all-partition price diagnosis, independently rederived here. No peer executable imported.

## complete derivation or exact first unsupported line

PROOF.md gives the complete derivation. Coordinatewise monotonicity of L reduces the entire real diamond to ell(b)=L(1-b,b); its logarithmic diagonal singularity is integrable. The explicit third derivative is negative; the second derivative changes sign exactly once, so b ell'-ell has one interior zero. Rational root signs, not a grid, enclose the maximum. Actual dyadic Boolean constructions show primitive scalar sharpness. Independent complete coefficient cancellation recovers A075 unchanged and transfers the new scalar price to full signed composition drift. Rational kappa9/4 gives the same full bank mechanism as source kappa3, reduced by exactly3I/4. Boundary zero/balanced/one, zero query influence and zero pivot probability are all included. The first universal unpaid line is an INITIAL unused original O(I) bank for an arbitrary core; the all-partition sandwich remains FEI-equivalent at fixed K. This is a component analytic proof, not a full FEI proof or formal certification.

## executed validation with domain, arithmetic, commands and outputs

Frozen specification: out/FROZEN_SPEC.json. Run python -X utf8 code/check.py --pilot, then code/check.py, then code/audit.py, from this run (or use their absolute paths). Pilot:32 circuits/96 rows,610 assertions,0.0619453 seconds. Main:1024 circuits/3072 rows,{v['assertions']} exact assertions,{v['runtime_seconds']:.4f} seconds. Arithmetic uses literal integer characters, Fraction coefficients, exact prime-log cancellation, and outward48-term rational atanh intervals. Independent direct-argument64-term log audit passes, with saved192-bit outward endpoints. Its runtime is {a['runtime_seconds']:.4f} seconds. Controls include b=0,1/2,1 and an actual4-bit primitive price2 failure, checked by2^74>3^9*5^25. The attempted Lean statement only encodes the algebraic last transfer, not the entropy analysis; checker exit {formal.get('exit_code')} refused fresh compiler admission before compilation. No Lean-checked claim is made.

The first full verifier was interrupted after detecting naive factorization of squared integers; exact square reduction fixed it and the same frozen domain passed. The independent audit initially passed its inequalities but failed serialization of large Fraction numerators; outward192-bit output rounding fixed persistence, and it was rerun successfully. Intake encountered a legacy cp1252 source and now records that explicit fallback. These execution faults supplied no claim evidence before their corrected reruns. Fresh memok exited0 before the formal attempt. Compute telemetry showed about4.4GB disk free; largest private-memory groups included Claude and ffmpeg. No shared process was stopped or throttled.

## proof dependencies and changed downstream conclusions

A075@1 independently HOLDS unchanged. The new claim improves its exceptional-row estimate and rational headroom only; its sharp scalar coefficient is NOT proved optimal for the full drift. Credit and debit signs are explicit: d_b=K I(child)-H(child)+a_b. Original owners, old signed labels and full outcomes remain. External acceptance of the new claim and initial funding remain pending. The old A084 fresh-guard theorem is not rerun or silently amended.

## one next mathematical action and independent reviewer

A075/A074 should reconstruct the scalar monotonicity/critical-point proof and original-owner bank induction. Next mathematical action: fund INITIAL U for arbitrary indecomposable Boolean cores using an unused ORIGINAL influence-priced source, or a well-founded source-price descent; do not extend already-paid guard histories. A083 may formalize the analytic scalar step when compiler admission permits.

## actual persistence receipts or precise save blocker

All run artifacts and the three rolling files are local to A084. out/RECEIPTS.json records SHA256 and byte size of the final files after this report is saved. Protocol field sets and matching PROGRESS/PACKET_DELTA are checked by code/finalize.py. No git, email, publication, brain mutation, other-agent edit or supervisor mirror is claimed. New external review and remote adoption are unverified.

## Universal bridge

C019 stopping-tree payment and C024 history transfer move by a certified reduction of the supplied universal rational reserve from3I to9I/4, saving3I/4 for arbitrary disjoint-core compositions and every real fixed K>=0. The sharp primitive coefficient is approximately2.152204859; the all-real proof replaces a grid with analytic boundary reduction and exact root signs. The initial arbitrary-core O(I) source remains unpaid and FEI-equivalent, so no full FEI conclusion follows. Paying that ORIGINAL initial source is the shortest remaining route because another guard/history class cannot remove this same fixed-K initial-price obstruction.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8',newline='\n')
now=datetime.now(timezone.utc).isoformat()
(OWN/'STATUS.md').write_text('STATE: Stage21 saved: sharp Boolean row price~2.152204859<9/4; all-real universal signed-bank reserve3->9/4 saves3I/4;18592 exact checks; A075@1 HOLDS;FEI OPEN.\nNEXT: A075/A074 review scalar/root and supplied-owner proof; fund INITIAL arbitrary-core bank from unused ORIGINAL O(I) source or well-founded decreasing source price; Lean admission held.\n',encoding='utf-8',newline='\n')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:f.write(f'\n{now}: Stage21 {R.name}: A075 whole-row identity independently HOLDS unchanged. Reduced real Boolean diamond to monotone ell(b), unique critical point, sharp primitive price~2.152204859<9/4; rational bank3->9/4 saves3I/4. Main1024 circuits/3072 rows/18592 exact assertions PASS1.3735s; independent64-term scalar audit PASS. Factoring-squares inefficiency interrupted/fixed; large-Fraction output fixed by outward192-bit rounding; same domain rerun. Lean compiler admission held after fresh memok0; no formal theorem. Initial arbitrary-core source/full FEI OPEN. All saves local; no shared process changes or remote adoption.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:f.write('\nStage21: Whole entropy row L(x,y) is coordinatewise increasing in absolute arguments because L_xy=2log2((x+y)/|x-y|)>=0, with integrable logarithmic diagonal. Boolean |mu|+|t|<=1 and |t|<=Inf reduce its sharp influence price to max ell(b)/b, ell=L(1-b,b). ell_second=4log2((1-2b)^2/[b(1-b)]), ell_third<0; unique beta~0.40486 maximizes ratio. Exact root certificate gives2<lambda_row~2.152204859<9/4, sharp over dyadic actual one-constant-branch cores. Full A075 signed drift inherits this bound, but full-drift optimum is not established. Universal supplied-bank rational reserve3->9/4 saves3I/4; initial source remains FEI-equivalent at fixed K. Factor perfect-square numerators before prime trial division; round saved huge Fraction interval endpoints outward instead of weakening arithmetic or raising digit limits.\n')
# Read back serialized bytes, validate shape, and preserve final receipts.
for name in ['CLAIMS.json','PROGRESS.json','PACKET_DELTA.json']:
 json.loads((R/name).read_text(encoding='utf-8'))
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
receipts=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='RECEIPTS.json':
  b=p.read_bytes();assert len(b)<20*1024*1024
  receipts.append({'path':str(p.relative_to(R)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
for p in [OWN/'STATUS.md',OWN/'WORKLOG.md',OWN/'LEARNED.md']:
 b=p.read_bytes();receipts.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save('out/RECEIPTS.json',{'saved_at':now,'artifacts':receipts,'field_checks':'PASS','remote_mirror':'UNVERIFIED'})
print(json.dumps({'status':'SAVED_AND_READ_BACK','files':len(receipts),'schema_checks':'PASS','new_claim':new['claim_id'],'full_FEI':'OPEN'}))
