"""Finalize and submit the exclusively owned DRAFT; never integrates the store."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

R=Path(__file__).resolve().parent
stamp=datetime.now(timezone.utc).isoformat()
def get(name):
    return json.loads((R/name).read_text(encoding='utf-8-sig'))
def put(name,obj):
    (R/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

claims=[
 {'claim_id':'w469-C0052-CYCLE-001','target':'C0052',
  'statement':'For a sourceless random current on a uniform four-edge cycle at t>0, the odd-edge indicators are all the same Bernoulli variable of parameter h=tanh(t)^4/(1+tanh(t)^4). Hence E[B_e B_f]=h>h^2=E B_e E B_f for distinct edges; conditioning on the source set alone does not give independent edge values.',
  'assumptions':['Finite four-cycle, zero field, free boundary','Positive uniform parameter t','One current with empty parity source set'],
  'source':'owner-own-work: CYCLE_OBSTRUCTION.md',
  'proof_or_counterexample':'The source constraint allows exactly the all-even and all-odd parity vectors. Their weights are cosh(t)^4 and sinh(t)^4. The odd indicators coincide with the sector bit. This invalidates transplanting tree edge factorization to cyclic graphs.',
  'independent_reviewer':'w470 requested; pending','remaining_gap':'No cyclic-graph nonlinear comparison or 3D original-current connection lower bound is proved.','status':'proved special case','review_state':'unreviewed','recorded_utc':stamp},
 {'claim_id':'w469-C0052-LOCALIZED-001','target':'C0052',
  'statement':'For homogeneous zero-field nearest-neighbor Ising on Z^3 at 0<beta<beta_c, let R=ceil(xi), B_R=[-R,R]^3 intersect Z^3, and chi_R=sum_(x in B_R)G(0,x). Sample independent x2 and y on B_R with weights G(0,x)/chi_R and x3 uniformly on B_R, put x4=x3+y, and let p be the thermodynamic limit of the original two-current connection probability for (0,x2,x3,x4). Then -g(beta)>=2 |B_R|/xi^3 (chi_R/chi)^2 E p. A lower bound (chi_R/chi)^2 E p>=epsilon>0 along beta_n increasing to beta_c suffices for the literal C0052 source criterion.',
  'assumptions':['Homogeneous nearest-neighbor ferromagnet, zero field, free-boundary thermodynamic state','0<beta<beta_c so chi and xi are finite and xi>0','g and exponential xi as in source equations (7.1)-(7.2)','Thermodynamic limit first, fixed endpoints and beta; finite-volume switching and convergence of spin correlations'],
  'source':{'campaign':'owner-own-work: ATTEMPT.md localized route','primary_url':'https://www.ihes.fr/~duminil/publi/2017PIMS.pdf','locator':'(7.1)-(7.2), Exercise 61'},
  'proof_or_counterexample':'All summands of -U4 are nonnegative. Retain x2,x3,y in B_R with x4=x3+y, and use -U4=2G(0,x2)G(x3,x3+y)p. Translation invariance gives total sampling mass |B_R|chi_R^2. Divide by chi^2 xi^3. Since |B_R|=(2ceil(xi)+1)^3>=8xi^3, the quantitative input gives -g>=16epsilon along the sequence.',
  'independent_reviewer':'w470 requested; pending','remaining_gap':'The displayed positive lower bound is still unproved for the actual near-critical 3D law; neither a susceptibility-mass floor nor a current-intersection floor is assumed proved. No critical-field all-subsequence statement follows automatically.','status':'sketch','review_state':'unreviewed','recorded_utc':stamp}]
known={json.loads(line)['claim_id'] for line in (R/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()}
with (R/'CLAIMS.jsonl').open('a',encoding='utf-8') as stream:
    for claim in claims:
        if claim['claim_id'] not in known:
            stream.write(json.dumps(claim,ensure_ascii=False)+'\n')

bundle=get('bundle_001.json')
if not any(entry['key']=='cycle-law' for entry in bundle['entries']):
    bundle['entries'].append({'key':'cycle-law','namespace':'probability.statmech',
      'logical_name':'sourceless-cycle-current-parity-mixture-dependence',
      'kind':'concept','title':'Cycle parity blocks tree edge independence',
      'statement':'DRAFT; independent mathematical review pending. '+claims[0]['statement']+' The finite-tree comparison q>=e*r^2/4 therefore requires a new dependence argument before any extension to the full critical Z^3 lattice.',
      'proof_text':None,'assumptions':claims[0]['assumptions'],'domain':'probability theory',
      'source':{'source_id':'owner-proofswarm-w469:cycle-law','url':'local:brain_workers/w469/CYCLE_OBSTRUCTION.md','revision':'campaign-draft-2026-10-10','license':'owner-own-work','excerpt':None}})
    bundle['relations'].append({'from_key':'cycle-law','to_key':'nonlinear','kind':'cites','rationale':'The nonlinear entry requires a finite tree, where sources fix each edge parity. The cycle entry exhibits a shared parity bit with E[B_e B_f]=h rather than h^2, documenting why that factorization cannot extend unchanged.'})
put('bundle_001.json',bundle)
keys={entry['key'] for entry in bundle['entries']}
for entry in bundle['entries']:
    assert entry['kind']=='concept' and entry['proof_text'] is None
    assert entry['source']['license'].startswith('owner-own-work')
    assert entry['statement'].startswith('DRAFT;')
for rel in bundle['relations']:
    assert rel['from_key'] in keys
    if 'to_key' in rel:
        assert rel['to_key'] in keys
allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
assert all(rel['kind'] in allowed for rel in bundle['relations'])
put('BUNDLE_VALIDATION.json',{'schema_checks':'PASS','entries':len(bundle['entries']),'relations':len(bundle['relations']),'concept_only':True,'mathematical_proof_receipt':False,'integrator_run':False})

status=get('SOURCE_STATUS.json')
status['exact_statement']=status['exact_statement'].replace('zero-field nearest-neighbor','zero-field homogeneous nearest-neighbor')
status['prior_work_checks']['live_population_store']=get('LOCAL_STORE_CHECK.json')['store_path']+'; exact C0052 problem and old reduction IDs both still truth_status=unverified at read'
status['canonical_store_check']='See CANONICAL_STORE_CHECK.json if present; absence of a verified disposition is not an openness or novelty certificate.'
put('SOURCE_STATUS.json',status)

receipt=get('INBOX_CLAIM_RECEIPT.json')
dest=Path('~/math-brain-inbox/w469/bundle_001.json')
assert receipt['agent']=='w469' and receipt.get('acquired'), 'Exclusive own-inbox claim missing'
assert any(Path(item['resource']).resolve()==dest.resolve() and item['mode']=='exclusive' and datetime.fromisoformat(item['expires_at'].replace('Z','+00:00'))>datetime.now(timezone.utc) for item in receipt['acquired']), 'Own-inbox claim invalid or expired'
dest.parent.mkdir(parents=True,exist_ok=True)
if dest.exists():
    prior=json.loads(dest.read_text(encoding='utf-8-sig'))
    assert prior.get('author_agent')=='w469' and prior.get('bundle_slug')==bundle['bundle_slug'], 'Refusing to overwrite a different artifact'
part=dest.with_suffix('.json.part')
part.write_text(json.dumps(bundle,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert json.loads(part.read_text(encoding='utf-8-sig'))==bundle
part.replace(dest)
assert json.loads(dest.read_text(encoding='utf-8-sig'))==bundle
put('BUNDLE_STATE.json',{'prepared':True,'submitted':True,'submitted_utc':stamp,'path':str(dest),
  'reviewed':False,'review_status':'w470 pending; source correction and own lemmas require independent checks',
  'ingested':None,'ingestion_status':'NOT_CONFIRMED','retrievable':None,'retrieval_status':'NOT_CHECKED',
  'source_tag':'owner-own-work','concept_only':True,'live_store_mutation_by_w469':False,
  'different_model_gate':'NOT_PASSED','requested_models_are_not_attestations':True})

verification=get('VERIFICATION.json')
tree=get('TREE_VERIFICATION.json')
patch=get('PATCH_CHECK.json')
report=(
'C0052 remains unproved in this packet. The exact 2017 source criterion is g(beta) not tending to zero as beta increases to beta_c; current October 2026 openness is UNKNOWN. The old store-backed source card asserted an unspecified infimum-over-scales equivalence, stronger than the supplied definition.\n\n'
'The packet gives an independent rare-corridor counterexample, a fourth-moment weak-limit reduction, the exact localized near-critical endpoint normalization, and a nonlinear original-versus-augmented current comparison on finite trees. A four-cycle parity example identifies why direct tree factorization cannot extend to the full lattice. REVIEW_W468.md keeps the paired finite-tree formulas with their stated scope; w470 review of all own lemmas is pending.\n\n'
f'Measured with python -X utf8 verify_obstruction.py: 5 exact corridor families, 768 four-point switching tuples including repeated endpoints, and 3 weighted moment identities passed in {verification["active_seconds"]:.3f} active seconds. At t=0.1, bare versus augmented hit probabilities are 0.0049792510 and 0.0099337092. With python -X utf8 verify_tree_bound.py: {tree["exact_pair_total"]} exact nonuniform path-pairs and 30 comparison controls passed in {tree["active_seconds"]:.3f} active seconds. Fresh gate receipts are retained. These are finite controls, not a 3D proof or a formal-check receipt.\n\n'
f'Proposed source-line measurement from python -X utf8 prepare_packet.py: unsupported equivalence count {patch["before_unsupported_equivalence_count"]} before versus {patch["after_unsupported_equivalence_count"]} after in the local replacement; target line {patch["target_line"]}. This is a proposed card correction; live recall improvement has not been measured.\n\n'
'Apply: reviewer applies patches/01_c0052_source_criterion.diff to the named source in a reviewer copy after checking PATCH_CHECK.json, then the validating integration coordinator reissues the corrected canonical card; do not edit SQLite directly.\n\n'
f'DRAFT submitted under exclusive own-file claim: {dest.as_posix()} (6 concept entries, 5 relations, owner-own-work). Submitted, reviewed, ingested and retrievable are recorded separately in BUNDLE_STATE.json; ingestion and retrieval are unconfirmed. No integration command or live store write was run. HOOK_PROPOSALS.jsonl is staged in the worker folder for the permitted coordinator to submit.\n\n'
'Risks: the rare-corridor paths are not Ising currents; finite trees do not model cycle-space dependence; scalar tightness does not establish random-distribution tightness; near-critical nonvanishing does not by itself prove every critical subsequential field non-Gaussian. No served-model receipt is available, so no different-model proof gate is claimed.\n\n'
'NEXT: w470 independently checks the weak-limit, localized and nonlinear-tree reductions; then attempt a dependence-aware original-current weighted-overlap lower bound on the full 3D lattice.\n')
(R/'REPORT.md').write_text(report,encoding='utf-8')
packet=get('REVIEW_PACKET.json')
packet['required_reviews'] += ['finite-cycle parity obstruction','localized near-critical original-current criterion']
packet['brain_submission']=get('BUNDLE_STATE.json')
packet['next_proof_step']='Control original-current overlap after cycle-space mixing, or establish a quantitative original-versus-augmented comparison on critical Z^3.'
files=['INDEPENDENT.md','ATTEMPT.md','TREE_NONLINEAR.md','CYCLE_OBSTRUCTION.md','REVIEW_W468.md','CLAIMS.jsonl','SOURCE_STATUS.json','VERIFICATION.json','TREE_VERIFICATION.json','COMPUTE_GATE_initial.json','COMPUTE_GATE.json','LOCAL_STORE_CHECK.json','CANONICAL_STORE_CHECK.json','bundle_001.json','BUNDLE_VALIDATION.json','BUNDLE_STATE.json','PATCH_CHECK.json','patches/01_c0052_source_criterion.diff','HOOK_PROPOSALS.jsonl','INBOX_CLAIM_RECEIPT.json','REPORT.md','verify_obstruction.py','verify_tree_bound.py','prepare_packet.py','finalize_packet.py']
packet['artifacts']=[{'path':str(R/file),'sha256':hashlib.sha256((R/file).read_bytes()).hexdigest()} for file in files if (R/file).exists()]
put('REVIEW_PACKET.json',packet)
print(json.dumps({'submitted_path':str(dest),'concept_entries':len(bundle['entries']),'relations':len(bundle['relations']),'claim_rows':len((R/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()),'review_ready':True,'parent_solved':False}))
