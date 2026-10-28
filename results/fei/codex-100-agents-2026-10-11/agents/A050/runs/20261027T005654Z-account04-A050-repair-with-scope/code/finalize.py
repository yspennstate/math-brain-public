from pathlib import Path
import json,hashlib,datetime,copy
run=Path(__file__).resolve().parents[1]; home=run.parents[1]
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
main=read(run/'out/MAIN.json'); audit=read(run/'out/AUDIT.json')
assert main['status']==audit['status']=='PASS'
source=Path('agents/A096/runs/20261023T140303Z-account03-A096-live-gap-ledger/CLAIMS.json')
adopt=copy.deepcopy(next(c for c in read(source) if c['claim_id']=='A096-GHOST-COMPLETE-HEREDITARY-WITNESS-TRANSPORT'))
adopt['review_records'].append({'reviewer':'A050','verdict':'HOLDS_AT_STATED_SCOPE','reconstruction':'PROOF.md section1; independent direct/FWHT and prime-exponent complete CE/KL identities','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'limits':'No source price or stricter fixed fresh-profile preservation accepted.'})
adopt['status']='INDEPENDENTLY_RECONSTRUCTED_HOLDS_AT_STATED_SCOPE'
adopt['proof_source']={'external':str(source.parent/'DERIVATION.md'),'local_reconstruction':'PROOF.md section1','checks':['out/MAIN.json','out/AUDIT.json']}
consumers=['A047','A048','A049','A073','A085','A094','A096','A097','A099','B10','B20']
statement=('For every finite uniform Boolean physical query tree and supplied complete reference Q=bP+sum c_j delta_Wj, b>0, c_j>=0, b+sum c_j=1, arbitrary occupied or ghost witnesses, the interface requiring reference vacuum mass to equal the actual spectral vacuum mass, while permitting the inherited nonempty conditional profile and moving witnesses, is closed under every physical query followed by calibration. At each raw child, r=P(empty), z=Q(empty), q*(empty)=r and q*(s)=(1-r)q(s)/(1-z) off empty when r<1; when r=1 take q*=P. The unique profile-preserving calibration changes complete CE by -D(Bern(r)||Bern(z))<=0. For r<1 b*=b(1-r)/(1-z) lies in (0,1], nonempty witness coefficients scale by (1-r)/(1-z), and one reusable empty witness has coefficient r(1-b*). Nonempty witness count never increases and at most one empty slot is added over the entire tree. With B_v=H(P_v)-H(MP_v), J_v=H(MP_v)-mean H(P_vt), E_v=erasure KL, O_v=D(fair||actual reference outcome), d_vt=calibration KL, the exact local identity is B_v+mean CE(P_vt,Q*_vt)=CE(P_v,Q_v)-J_v-E_v-O_v-mean d_vt. It telescopes at actual physical reaches, retaining both full terminal bills and all old bookings under the SAME original supplied CE capacity. All releases and terminal mismatch similarly telescope to original KL. This does not preserve fixed nonempty floors, fixed alpha or current-essential full masks, and gives no original influence price or terminal FEI surplus.')
new={'claim_id':'A050-VACUUM-CALIBRATED-HEREDITARY-REFERENCE','version':1,'exact_statement':statement,'hypotheses':['Finite uniform Boolean physical query tree; entropy/CE/KL in bits.','Complete positive true-law mixture source genuinely supplied; ghost references retained until actual accounted calibration.','Downstream class accepts moving nonempty profile and one permanent empty slot; no mandatory nonempty floor or fixed alpha.','Both physical children, actual reaches, old bills and original capacity retained.'],'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A050; standard binary information projection composed with A096 ghost-complete transport'],'proof_source':['PROOF.md sections2--4','code/check.py','code/audit.py','out/MAIN.json','out/AUDIT.json'],'proof_dependencies':['A096-GHOST-COMPLETE-HEREDITARY-WITNESS-TRANSPORT@1: independently reconstructed without repair','Finite KL/Gibbs inequality, exact Boolean restriction, elementary mixture normalization'],'review_records':[],'status':'ANALYTIC_PROOF_EXACT_VALIDATION_INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':'Supply a noncircular original complete CE<=C I source for every Boolean core and a required useful continuation/terminal policy; a stricter nonempty floor needs its actual same-owner admission payment.','next_consumers':consumers}
claims=[adopt,new]; save(run/'CLAIMS.json',claims)
next_action='A096/A097/A094 independently review repeated vacuum calibration and SAME original CE/KL identities; specify a genuinely required nonempty floor or influence-price the original arbitrary-core complete source, retaining both full terminals and old U.'
progress={'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B10','packet_id':'A050','gap_id':'C024-SAME-REFERENCE-CERTIFIED-UNUSED-FRONTIER','attempt_id':'A050-stage11-repeated-vacuum-calibration-v1','method':'Independently reconstruct ghost-complete transport; integrate unique nonpositive vacuum calibration into every child and exact original CE/KL telescope.','mathematical_delta':f"Mandatory vacuum matching survives arbitrary physical continuations with at most one permanent empty slot, exact binary-KL release and no repeated debit. {main['assertions']} primary exact assertions and {audit['rows']} independent full CE/KL profile checks PASS. No universal FEI constant improvement.",'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_ANALYTIC_PROOF_REVIEW_PENDING_FULL_FEI_OPEN','claim_versions_used':['A096-GHOST-COMPLETE-HEREDITARY-WITNESS-TRANSPORT@1','A050-FIXED-PROFILE-ZERO-COST-REPAIR@1: prior embedded hereditary substatement only'],'claims_created_or_changed':[c['claim_id']+'@'+str(c['version']) for c in claims],'source_artifacts':['PROOF.md','out/INTAKE_RECEIPTS.json','out/FROZEN_SPEC.json','out/PILOT.json','out/MAIN.json','out/AUDIT_SPEC.json','out/AUDIT.json','out/LEAN_REVIEW.json'],'next_consumers':consumers,'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Arbitrary-core initial CE<=C I source remains unpaid; calibrated class alone is FEI-equivalent.','Required fixed nonempty floor/alpha/essential-mask profiles not inherited.','New theorem independent review, remote save/adoption unverified.','Administrative working receipt failed: checklist lock held too long; mathematical output is unaffected.'],'packet_ids':['A050']}
save(run/'PROGRESS.json',progress);save(run/'PACKET_DELTA.json',progress)
leanfiles=list((run/'out/lean').glob('*/receipt.json')) if (run/'out/lean').exists() else []
lean='The attempted core-Lean check concerns only cleared-denominator distributivity, not KL, entropy, or the full theorem; see out/LEAN_REVIEW.json and any wrapper receipt. No complete formal certification is claimed.'
report=f'''# A050 stage11: free repeated vacuum calibration, with scope

## exact target, quantifiers, hypotheses and units

For every finite Boolean uniform physical query tree, repair mandatory matching of the reference vacuum mass while keeping an inherited nonempty profile and moving witnesses. A positive true-law source component is supplied, not influence-priced. All units are bits; both full terminals, actual reaches and old bills stay in the SAME original account. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Protocol {protocol['revision']} read in full; current BOARD, B10 STREAM_NOTES v2, own stage10 REPORT/PROOF/CLAIMS and rolling state. Current campaign registries/plan, advisory campaign and sources, and four supplied context texts were read for intake; hashes and sizes are in out/INTAKE_RECEIPTS.json, extracted locators in out/INTAKE_EXTRACTS.json. Main mathematical dependency is A096 stage21 20261023T140303Z DERIVATION2--3 and ghost-complete claim@1, exact statement hash {adopt['statement_sha256']}. A097 stage21 20261023T143952Z PROOF supplies the declared nonempty-floor distinction; its printed derivative omits factor t, as already flagged by the board, and is not used here. Old B10 biased tax is not reopened. Source notes may guide but are not proof premises.

## complete derivation or exact first unsupported line

PROOF1 independently reconstructs A096 unchanged at its supplied-reference scope. PROOF2 gives the unique vacuum calibration q*, exact CE decrease -binaryKL, all endpoint definitions and an explicit mixture representation with at most one permanent empty witness. PROOF3 combines query, full CE and calibration releases in one exact original-account telescope. PROOF4 lists admitted applications and gives an actual AND3/AND2 floor counterexample. The additional hypothesis is downstream acceptance of inherited nonempty profiles; no globally weakest-condition claim is made. The theorem covers every Boolean core conditionally on its initial complete source. First unsupported universal line: construct that source at O(I) price and pay a useful required terminal policy. Taking Q=P shows that existence of such a cheap complete source in this broad class remains FEI-equivalent.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec saved before pilot; its preexecution case count was corrected to 2+4+16+256 labelled functions and actual distinct witnesses. Commands from A050: python -X utf8 runs/{run.name}/code/check.py --pilot; then the same without --pilot; python -X utf8 runs/{run.name}/code/audit.py. Pilot PASS:328 trees/23244 assertions in0.208s. Main exhausts n=0..3, all labelled truth tables, all fixed orders plus one adaptive order, every distinct original witness in empty/full/first-coordinate and both fair/deterministic ghost kernels. PASS:{main['trees']} trees/{main['nodes']} nodes/{main['assertions']} exact assertions; {main['nontrivial_calibrations']} nontrivial calibrations, {main['ghost_occurrences']} ghost occurrences and {main['endpoint_calibrations']} endpoint calibrations, {main['seconds']:.3f}s. Direct Walsh and independent FWHT agree. Independent checker proves two full ledger identities on EACH of136 profiles by exact rational prime-exponent arithmetic, plus actual Boolean floor exclusion, {audit['seconds']:.3f}s. Pilot counts are excluded from main. General tree scope follows the finite algebraic proof, not extrapolation. No failed numerical sign was relabeled a counterexample.

Estimated checker memory<100MB, no dimension escalation, GPU or detached process. Fresh memok passed (8.8GB physical,20.1GB commit free) before optional core Lean. Mathlib compilation's known memory use exceeds this packet's1.5GB job limit and was not launched. {lean} Shell startup and teardown delays are not checker CPU/runtime receipts.

## proof dependencies and changed downstream conclusions

A096 ghost-complete transport independently HOLDS without mathematical repair; review recorded locally under its exact source statement/version. Its source registration wording is too strong: the occupied hereditary substatement is already embedded in A050-FIXED-PROFILE-ZERO-COST-REPAIR@1's exact_statement, though no separate hereditary ID exists. No source file was changed. New calibrated theorem is a contributor result awaiting external review. Matching-empty moving-reference consumers now need no repeated conversion; prescribed fixed nonempty floor, alpha or essential-full-mask consumers still need actual class-relative admission. No initial source, universal terminal surplus or FEI constant is supplied.

## one next mathematical action and independent reviewer

{next_action}

## actual persistence receipts or precise save blocker

Four exact-field protocol files, proof, frozen specifications, pilot/main/independent audit, source hashes and local schema/hash receipts saved inside A050. STATUS has exactly STATE/NEXT; WORKLOG and LEARNED are updated. No git, mail, brain write, shared-tree mutation or workload stop occurred. Supervisor copying, independent acceptance and mirror verification remain unverified. Wake reported stale owner-model/state-of-mind and incomplete dream; that alert was surfaced before relying on notes. Checklist working receipt returned a lock timeout, not success.

## Universal bridge

This stage advances C024 history transfer and C020 whole-reference accounting inside C019 by proving mandatory vacuum matching costs zero or releases prepaid CE after EVERY physical query in the moving-profile interface, with one empty slot rather than a growing witness list. Its numerical universal FEI improvement is zero. The initial arbitrary-core source and useful stopping/terminal policy remain unpaid, and a mandatory nonempty floor can still fail. NEXT asks consumers to name that stricter requirement or price the original source, because repeated optional vacuum resets cannot fund the missing all-dimensional bridge.
'''
(run/'REPORT.md').write_text(report,encoding='utf-8')
(home/'STATUS.md').write_text('STATE: A050 stage11 COMPLETE_LOCAL: A096 ghost transport HOLDS; repeated vacuum matching free, <=one permanent empty slot;2054924 exact assertions+136 independent ledger profiles PASS;FEI OPEN.\nNEXT: '+next_action+'\n',encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
for name,msg in [('WORKLOG.md',f'{now} stage11 {run.name}: independently reconstructed A096 ghost-complete CE/KL identity; proved unique repeated vacuum calibration releases exact binary KL and preserves finite witnesses with one empty slot. Main11080 trees/2054924 assertions; independent136 complete CE+KL identities PASS. New theorem review pending; original source and fixed nonempty-floor payment OPEN. Working checklist lock timed out. No unrelated processes stopped.'),('LEARNED.md','Stage11: Vacuum-matching reference class is hereditary if inherited nonempty conditional profiles and moving witnesses are allowed. For r=p0<1,z=q0, k=(1-r)/(1-z), q*=r at vacuum and kq elsewhere, b*=kb<=1, scale nonempty witness coefficients and consolidate vacuum coefficient r(1-b*). At r=1 take P. CE decreases exactly binaryKL(r||z). One vacuum slot suffices for arbitrary finite depth. Query B+mean childCE equals parentCE minus JS, erasure KL, outcome KL and mean calibration KL; keep SAME original owner/old U/full terminals. Mandatory nonempty floors and fixed alpha/masks do not follow; AND2 matched full mass1/4 fails floor1/3. Existence of universal complete CE<=CI source in this broad class remains FEI-equivalent. Prior occupied heredity is embedded in native A050 combined claim, not absent from CLAIMS.')]:
 with (home/name).open('a',encoding='utf-8',newline='') as f:f.write('\n'+msg+'\n')
claimfields=set(protocol['required_per_run']['claim_fields'])
progressfields={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
for c in claims:
 assert set(c)==claimfields,(set(c)^claimfields)
 assert hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256']
assert set(progress)==progressfields,(set(progress)^progressfields)
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert len((home/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
receipts=[]
for p in sorted(run.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  data=p.read_bytes();assert len(data)<20*1024*1024
  receipts.append({'path':str(p.relative_to(run)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
save(run/'out/PERSISTENCE.json',{'status':'PASS','schema':'exact protocol field sets','files':receipts,'remote_adoption':'UNVERIFIED'})
print(json.dumps({'status':'COMPLETE_LOCAL','claims':len(claims),'files':len(receipts),'main_assertions':main['assertions'],'independent_profiles':audit['rows'],'full_fei':'OPEN'}))
