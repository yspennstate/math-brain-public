from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def read(name):return json.loads((R/name).read_text(encoding='utf-8'))
def write(name,obj):(R/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
result=read('out/CHECK_RESULT.json'); formal=read('out/LEAN_RESULT.json')
assert result['status']=='PASS'
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
peer=Path('agents/A097/runs/20261023T143952Z-account03-A097-cross-route-transfer')
original=json.loads((peer/'CLAIMS.json').read_text(encoding='utf-8-sig'))[0]
assert hashlib.sha256(original['exact_statement'].encode()).hexdigest()==original['statement_sha256']
raw_proof=(peer/'PROOF.md').read_bytes()
raw_hash=hashlib.sha256(raw_proof).hexdigest()
lf_hash=hashlib.sha256((peer/'PROOF.md').read_text(encoding='utf-8').encode()).hexdigest()
assert lf_hash=='4d9f47f5251bcdbe4ec1bdc8faa8fd22398ab5f4d0eb0a18443970012bc62c0f'
write('out/SOURCE_BINDING.json',{'initial_raw_binding_check':'FAILED','cause':'Declared peer proof hash is LF-normalized text, current read-only source has CRLF','raw_sha256':raw_hash,'lf_normalized_sha256':lf_hash,'crlf_count':raw_proof.count(bytes([13,10])),'source_mutated':False,'main_statement_exact_hash':'MATCH'})
statement='For every finite calibrated law p with vacuum r, t=1-r>0, event mass 0<a<t, and finite-CE incoming reference q0 with mass 0<b<ell<t, preserving the vacuum and both conditional reference profiles including ghosts gives signed CE change Delta(z)=a log2(b/z)+(t-a)log2((t-b)/(t-z)). Its derivative is t(z-a)/(z(t-z)ln2), and its unique minimizer on ell<=z<t is max(a,ell). For supplied disjoint full-terminal seed weights beta_h and physical reaches rho_h, the full change is sum rho_h beta_h Delta_h and the SAME original residual is B-C-U minus that change. The derivative displayed in A097 PROOF.md omits t; its main statement and minimizer survive. No universal source or FEI bound is supplied.'
claim={
 'claim_id':'A083-A097-SIGNED-FLOOR-DERIVATIVE-AUDIT','version':1,
 'exact_statement':statement,
 'hypotheses':['Bits; finite normalized laws and finite current CE; t>0,0<a<t,0<b<ell<t','Only profile-preserving class, ghosts retained, fixed vacuum','Disjoint full-terminal controller/seed supports and unchanged beta; physical reaches; ALL old U and original B retained','Correction contributor to this reconstruction; corrected proof requires external independent review'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A083'],
 'proof_source':{'path':str(R/'REVIEW.md'),'sha256':hashlib.sha256((R/'REVIEW.md').read_bytes()).hexdigest(),'formal_verification':formal['status'],'formal_scope':'Finite Rat derivative regression source only; NOT kernel-checked when admission held'},
 'proof_dependencies':[],
 'review_records':[{'source_claim':original['claim_id'],'source_version':original['version'],'source_statement_sha256':original['statement_sha256'],'verdict':'MAIN_STATEMENT_RECONSTRUCTED_HOLDS; PROOF_DISPLAY_ERROR_FACTOR_t; corrected reconstruction pending independent review','reviewer':'A083','independence':'No peer code/helper imports; direct likelihood comparison, Walsh characters, rational accounting and analytic differentiation','contributor_recusal':'A083 supplies the displayed-derivative correction and does not independently accept a corrected source version'}],
 'status':'PROOF_RECONSTRUCTED_WITH_DISPLAY_CORRECTION_PENDING_EXTERNAL_REVIEW','supersedes':[],
 'refutes':[{'source':'A097 stage21 PROOF.md derivative display only','false_display':"Delta prime=(z-a)/(z(t-z)ln2)",'witness':'t=3/4,a=1/4,z=1/3: derivative*ln2=9/20, printed RHS*ln2=3/5','scope':'Does not refute the claim statement, minimizer, bound or owner theorem'}],
 'first_unproved_line':'Construct a useful required compatible class for every Boolean core and an influence-priced original source with actual remaining same-owner capacity after all old invoices and full terminals.',
 'next_consumers':['A097','A085','A094','A096','A099','B20']}
write('CLAIMS.json',[claim])
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B17','packet_id':'A083',
 'gap_id':'C024-REQUIRED-COMPATIBLE-ADMISSION-ORIGINAL-SOURCE','attempt_id':'A083-stage21-A097-signed-floor-audit',
 'method':'Independent analytic reconstruction and exact rational likelihood/Boolean/owner certificates; narrow formal regression attempted under admission',
 'mathematical_delta':'A097 arbitrary-current signed-floor main statement reconstructed; missing positive factor t in derivative exposed and corrected; all minimizers, prices and same-owner criterion survive. 8520 exact checks; no universal payment.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_PROOF_WITH_DISPLAY_ERRATUM; EXTERNAL_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':[original['claim_id']+'@1'],
 'claims_created_or_changed':[claim['claim_id']+'@1'],
 'source_artifacts':['REVIEW.md','code/check.py','code/Derivative.lean','out/CHECK_RESULT.json','out/LEAN_RESULT.json','out/SOURCE_RECEIPTS.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'A097 correct the derivative display; A085/A094 independently review corrected reconstruction. A050/A011/A097 specify a necessary useful compatible profile class and pay its signed admission from actual unused original influence or supply O(I) initial capacity.',
 'stagnant_substantive_attempts':0,
 'blockers':['Universal original source and required useful profile class remain unsupplied','Lean admission held; no kernel success','Supervisor mirror, shared adoption and independent corrected-proof acceptance unverified'],
 'packet_ids':['A083']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
report='''# exact target, quantifiers, hypotheses and units

Review A097-SIGNED-ARBITRARY-REFERENCE-FLOOR-OWNER@1 for all finite calibrated laws and its supplied full-terminal SAME original account. Bits; 0<a<t=1-r,0<b<ell<t; preserve both incoming conditional reference profiles, ghosts and vacuum. Main statement HOLDS under reconstruction; a derivative display omits the positive factor t. Corrected reconstruction is pending independent review. Full FEI is OPEN.

# sources actually read, revisions and theorem locators

Execution protocol v2 read in full; current BOARD, B17 STREAM_NOTES v2, own stage20 handoff and A097 stage21 PROOF/REPORT/CLAIMS/checker read. Peer LF-normalized proof SHA256 4d9f47f5251bcdbe4ec1bdc8faa8fd22398ab5f4d0eb0a18443970012bc62c0f; actual CRLF byte SHA256 cadf52c8fabac7eecb20cf9ed86248697b0de76eaf0c771e89a2ca335d68b765. The initial byte-binding assertion failed; out/SOURCE_BINDING.json reconciles the22 CRLF line endings without editing the peer source. Claim statement SHA256 8e3a5074a89063d0bb52d1a8ac5d9e3743fbbd167e47b159b86e4b760171e170 matches exactly. out/SOURCE_RECEIPTS.json pins baseline campaign files, registers, plan and all four manuscript texts; out/BASELINE_EXCERPTS.json records relevant locators. Baselines are orientation, not new theorem premises or a fresh literature audit. Legacy manuscript decoders are explicitly recorded; no source bytes were rewritten. Prior B17 scalar formal work is already complete, so protocol dispatch consumes the new handoff dependency. Brain wake warned of stale identity/state/dream sources; owner alerted, none used as proof premises.

# complete derivation or exact first unsupported line

REVIEW.md reconstructs finite CE cancellation, sharp minimization, the logarithmic bound, signed original-owner substitution, all strict side conditions and the actual Boolean endpoint. Correct derivative: ln(2)Delta'(z)=-a/z+(t-a)/(t-z)=t(z-a)/(z(t-z)). At t=3/4,a=1/4,z=1/3 it equals9/20; the source display gives3/5. This is a missing unnormalized mass factor, not a changed base or minimizer. Since t>0, the minimizer max(a,ell), both signed prices and the original-owner theorem survive unchanged. First unsupported universal line: construct a useful necessary compatible class and influence-priced arbitrary-core original source with sufficient actual unused capacity after all old charges and both full terminals.

# executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json precedes execution and specifies all loop bounds, no symmetry and no dimension escalation. Its case-count entry gives the finite loop domain rather than an evaluated numeric total; realized exact counts are418 profiles,924 candidate comparisons,334 explicit missing-factor witnesses and288 ledger cases. python -B -X utf8 code/check.py: PASS8520 exact assertions in0.153s. Arithmetic: Fraction/integer powers and independently reconstructed Walsh characters, no floating signs. Vacuum r=0, ghost profiles, both minimizer regimes, zero beta, unequal reaches, both actual Boolean children, negative releases and double-credit failures checked. This finite evidence supports the continuum proof; it is not its substitute. The actual Boolean products27/25>1 and27/32<1 certify both signs exactly. The narrow Rat regression source was submitted to the admission runner only: formal memory admission held, so no compiler/kernel/axiom success is claimed. out/FORMAL_MEMOK.json and out/LEAN_RESULT.json preserve the refusal. Earlier standalone memok passed; the later fresh admission differs because current available memory changed. No guard was overridden.

# proof dependencies and changed downstream conclusions

No peer helper code or proof claim is an assumed mathematical premise. The independent reconstruction uses finite sums, elementary differentiation, ln(1+x)<=x and exact original budget algebra. A097's main statement is supported; its proof display needs the factor t restored before reuse of derivative magnitudes. The old proof's sign argument remains valid. A083 contributes that correction and recuses from independent acceptance of a corrected version; A085/A094 should review it. No changes to universal FEI constants, initial-source supply or arbitrary profile-changing conversion are warranted.

# one next mathematical action and independent reviewer

A097 correct the displayed derivative and A085/A094 review the corrected reconstruction. The next mathematical target remains A050/A011/A097's useful REQUIRED compatible profile class for arbitrary cores, with its exact signed bill paid from the SAME original unused influence after old invoices and all terminals. Optional favorable conversions and further derivative grids cannot pay that missing universal source.

# actual persistence receipts or precise save blocker

Four protocol files, REVIEW.md, independent checker, frozen domain, exact outputs, formal regression draft/refusal and source byte receipts saved locally. out/PERSISTENCE.json validates schema keysets, identical compatibility copy, source binding and file sizes below20MB. Rolling STATUS/WORKLOG/LEARNED updated. No shared tree, brain, git or other agent folder was modified. Supervisor copying, remote mirror, downstream adoption and independent corrected-proof review remain unverified. No research job remains running.

Universal bridge: C024 history transfer gains a source-bound audit of signed arbitrary-current-reference admission and a concrete missing-factor correction, with the SAME original account preserved across every full terminal. C019 gains no additional stopping payment and no universal FEI constant improves. The unpaid bridge is still the useful mandatory compatible class or the O(I) initial arbitrary-core source. NEXT attacks that exact universal supply step rather than another isolated class result; the derivative correction prevents a later quantitative argument from silently using the wrong mass scale.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
status='STATE: A083 stage21 saved: A097 signed-floor theorem reconstructed; derivative missing factor t corrected (9/20 vs3/5);8520 exact checks PASS;Lean admission HELD;FEI OPEN.\nNEXT: A097 fix display;A085/A094 review correction;A050/A011 specify REQUIRED useful compatible arbitrary-core class and SAME-original unused payer or O(I) initial source.\n'
(A/'STATUS.md').write_text(status,encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+' stage21: independently reconstructed A097 signed-floor theorem; found missing positive t in derivative, with exact9/20 vs3/5 regression. Main minimizer/budget unchanged.418 profile+288 ledger cases/8520 exact assertions PASS. Lean refused at fresh memory admission, no retry/bypass. Source decoder failure on legacy text handled explicitly read-only; proof sources remain strict UTF8. Local protocol artifacts saved; external corrected-proof review pending.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+' Durable stage21: unnormalized binary CE projection Delta=a log(b/z)+(t-a)log((t-b)/(t-z)) has derivative t(z-a)/(z(t-z)ln2), not (z-a)/(z(t-z)ln2). At t3/4,a1/4,z1/3 these give9/20 and3/5 after multiplying ln2. Positive t preserves the minimizer max(a,ell), but derivative magnitudes must retain it. Arbitrary incoming-reference conversion may refund prepaid mismatch: update C once, never add its release again. Fixed conditional profiles must retain ghosts; changing profiles needs a separate bill. Main A097 scoped theorem reconstructed; corrected proof requires independent review; universal original O(I) source remains unpaid.\n')
for c in read('CLAIMS.json'):assert set(c)==set(protocol['required_per_run']['claim_fields'])
keys=set(protocol['required_per_run']['progress_fields']);keys.remove('packet_ids (one primary ID, for compatibility)');keys.add('packet_ids')
assert set(progress)==keys
assert read('PROGRESS.json')==read('PACKET_DELTA.json')
assert all(f'# {s}' in report for s in protocol['required_per_run']['report_fields'])
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
receipts=[]
for p in R.rglob('*'):
 if p.is_file() and p.name!='PERSISTENCE.json':
  assert p.stat().st_size<20*1024*1024
  receipts.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
write('out/PERSISTENCE.json',{'status':'PASS','verified_at_utc':stamp,'schema_keysets':'exact','compatibility_copy':'identical','peer_source_binding':'verified','local_only':True,'artifacts':receipts})
print(json.dumps({'status':'PASS','files':len(receipts),'claims':1,'assertions':result['exact_assertions'],'formal_status':formal['status'],'run':str(R)}))
