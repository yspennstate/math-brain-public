from pathlib import Path
from fractions import Fraction as F
import json,hashlib,datetime as dt,subprocess,sys
R=Path(__file__).resolve().parents[1];O=R/'out';OWN=R.parents[1];ROOT=R.parents[3]
SOURCE=ROOT/'agents/A095/runs/20261022T235414Z-fleet03-A095-restricted-result-extraction'
ONE=ROOT/'agents/A094/runs/20261022T230414Z-fleet03-A094-proof-chain-challenger'
PRIOR=R.parent/'20261021T203248Z-fleet03-A086-joint-code-referee'
FUTURE=ROOT/'agents/A011/runs/20261023T000841Z-fleet03-A011-representation-existence'
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocolpath=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=load(protocolpath);result=load(O/'EXACT_RESULTS.json');pilot=load(O/'PILOT.json');formal=load(O/'LEAN_RECEIPT.json')
assert result['status']=='PASS' and result['histories']==48 and result['assertions']==54283
assert result['helper_sha256']==sha(R/'code/check.py')
assert pilot['status']=='PASS' and pilot['histories']==15
claims=load(SOURCE/'CLAIMS.json')
canonical=json.dumps({'exact_statement':claims[0]['exact_statement'],'hypotheses':claims[0]['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False)
assert hashlib.sha256(canonical.encode('utf-8')).hexdigest()==claims[0]['statement_sha256']
assert sha(SOURCE/'DERIVATION.md')==claims[0]['proof_source']['sha256']
originalone=load(ONE/'CLAIMS.json')
match=next(c for c in originalone if c['claim_id']==claims[1]['claim_id'])
assert all(match[k]==claims[1][k] for k in ['version','exact_statement','hypotheses','statement_sha256'])
stamp=dt.datetime.now(dt.timezone.utc).isoformat()
positive1=sum(F(x['e1'][0])>0 for x in result['rows']);positive2=sum(F(x['e2'][0])>0 for x in result['rows'])
negative2=sum(F(x['e2'][1])<0 for x in result['rows'])
zero_cases=sum(x['second_zero_reference_boundary'] for x in result['rows'])
assert positive1>0 and positive2>0 and zero_cases>0
assert all(F(x['remaining_lower'])>F(3,256) for x in result['rows'])
graph={claims[0]['claim_id']:[claims[1]['claim_id'],'A095-UNBOUNDED-WIDTH-SIGNED-PROFILE-HISTORY'],claims[1]['claim_id']:['A095-UNBOUNDED-WIDTH-SIGNED-PROFILE-HISTORY'],'A095-UNBOUNDED-WIDTH-SIGNED-PROFILE-HISTORY':[]}
def walk(v,stack):
    assert v not in stack,'cyclic proof dependency'
    for u in graph[v]:walk(u,stack+[v])
for v in graph:walk(v,[])
save(O/'DEPENDENCY_AND_SIGN_CHECKS.json',{'acyclic':True,'graph':graph,'positive_first_reset':positive1,'positive_second_reset':positive2,'negative_second_reset':negative2,'zero_reference_boundaries':zero_cases,'no_author_checker_imported':True})
for claim in claims:
    claim['review_records'].append({'reviewer':'A086/fleet03','at':stamp,'verdict':'HOLDS_AT_FULL_NAMED_SCOPE_WITHOUT_REPAIR','proof':str(R/'RECONSTRUCTION.md'),'validation':str(O/'EXACT_RESULTS.json'),'independence':'Own direct-character/physical-edge library; new exact symbolic complete-ledger implementation; no A094/A095 checker imported','substantive_repair_supplied':False,'rung':'independently reconstructed analytic proof with exact finite certificates','formal_step_status':formal['status']})
    claim['status']='INDEPENDENTLY_RECONSTRUCTED_AT_STATED_SCOPE';claim['first_unproved_line']=None
save(R/'CLAIMS.json',claims)

future=load(FUTURE/'CLAIMS.json')
future_meta=[{'claim_id':x['claim_id'],'version':x['version'],'exact_statement':x['exact_statement'],'status':'FUTURE_AUDIT_LEAD_ONLY_NOT_ACCEPTED_HERE'} for x in future]
save(O/'NEXT_SOURCE_METADATA.json',future_meta)
sources=[SOURCE/x for x in ['REPORT.md','CLAIMS.json','DERIVATION.md','PROGRESS.json']]+[ONE/x for x in ['CLAIMS.json','DERIVATION.md']]+[PRIOR/x for x in ['REPORT.md','RECONSTRUCTION.md','CLAIMS.json','code/check.py']]+[protocolpath,ROOT/'BOARD.md',ROOT/'claude/B18/STREAM_NOTES.md',FUTURE/'CLAIMS.json']
(O/'INPUT_STATUS.md').write_bytes((OWN/'STATUS.md').read_bytes())
sources.append(O/'INPUT_STATUS.md')
save(O/'SOURCE_RECEIPTS.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p),'scope':'future metadata only' if p==FUTURE/'CLAIMS.json' else 'critical source or accepted source reconstruction'} for p in sources])
try:
    state=load(Path(r'~\.claude\compute\compute_state.json'))
    save(O/'COMPUTE_RECEIPT.json',{k:state.get(k) for k in ['ts','status','mode','cpu_pct','mem_avail_mb','commit_avail_mb','disk_free_gb','hung_windows']})
except (OSError,ValueError) as exc:save(O/'COMPUTE_RECEIPT.json',{'status':'UNREADABLE','detail':repr(exc)})

progress=load(PRIOR/'PROGRESS.json')
progress.update(run_id=R.name,attempt_id='A086-stage18-two-narrow-resets-independent-review',method='Direct character sums, literal physical edges, normalized inherited references and exact symbolic two-reset complete ledger',mathematical_delta='A095 two-narrow-reset@1 and A094 one-reset@1 independently HOLD at full named scope without repair. SAME original rate4 bank: S0>451/256, p1<5/4,p2<1/2, retained surplus>3/256. Arbitrary-core source pricing and further resets remain OPEN.',deliverable_status='COMPLETE_LOCAL',mathematical_status='TWO_SCOPED_SOURCE_PROOFS_RECONSTRUCTED_FULL_FEI_OPEN',claim_versions_used=[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256']} for c in claims]+[{'claim_id':'A095-UNBOUNDED-WIDTH-SIGNED-PROFILE-HISTORY','version':1,'status':'previous A086 full-scope acceptance retained'}],claims_created_or_changed=[{'claim_id':c['claim_id'],'version':c['version'],'change':'independent review only; exact statement unchanged'} for c in claims],source_artifacts=[str(p) for p in sources],next_consumers=['A095','A094','A096','A097','A099','A011','B20'],next_action='Audit A011 newly saved arbitrary-core source-prefix floor v2 with original C0 and U_star retained; isolate the SAME-rate second-representation-edit payment from diminished original source capacity. A094 independent review; do not renew C0.',stagnant_substantive_attempts=0,blockers=['Universal influence-priced arbitrary incoming source/reference remains unpaid; full FEI OPEN.','Further prescribed resets need SAME diminished-bank payment; current two-reset proof does not pay arbitrary repetition.','Formal attempt admission held; no Lean certificate.','Canonical adoption, supervisor copying and remote mirror verification remain unverified.'],packet_ids=['A086'])
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)

fields={
'exact target, quantifiers, hypotheses and units':'''Independently review A095-TWO-NARROW-RESETS-SAME-RATE4-BANK@1 and its A094 one-reset dependency. For ALL w>=4,m>=0, ANY finite adaptive wide-only tree in the all-zero selector point edit of h_w*h_2, and ANY prescribed real eta in[0,1/4], perform the two specified zero-child narrow queries/resets with the fixed canonical references. Every off-path/complementary terminal, old query release and earlier positive reset booking is retained. The complete final expected ledger is below4I_root-3/256 from the SAME original bank. Entropy and CE are ideal bits; influence is actual uniform-cube physical influence. Selector, padding and arbitrary independent terminals are unqueried; product-compatible zero-fiber posteriors and finite terminal CE are retained. No arbitrary reset, individual leaf price or local4Inf claim is substituted.''',
'sources actually read, revisions and theorem locators':f'''BOARD, B18 STREAM_NOTES v2 and saved STATUS were read at entry. Protocol{protocol['revision']} and the previous A086 complete reconstruction/proof acceptance are retained. Critical new sources are A095 run20261022T235414Z REPORT, CLAIMS and DERIVATION1–4, and A094 run20261022T230414Z DERIVATION1–6 and exact claim. A095's unchanged statement/hypothesis canonical hash is{claims[0]['statement_sha256']}; raw proof hash{sha(SOURCE/'DERIVATION.md')}. Both are verified. Hash convention is sorted compact UTF-8 JSON of exact_statement plus hypotheses. The A094 imported statement, hypotheses, version and hash match its original claim record exactly. Prior campaign/paper background remains in the previous stage's receipts and is not claimed as a fresh paper audit. A011's newly saved arbitrary-core claim metadata is read only as the next review lead; its proof is NOT accepted here. out/SOURCE_RECEIPTS.json pins actual source bytes. No external literature/priority/novelty claim is made.''',
'complete derivation or exact first unsupported line':'''RECONSTRUCTION.md independently derives the whole account. Literal sparse support completion gives a normalized probability reference, with no latent duplicate witnesses. Keeping positive q,q² terms at w4 and splitting w>=5 proves original reserve S0=4Iroot-CEroot>451/256. This is distinct from the old surviving-terminal margin. Actual residual sources h_t*h_1 and-h_t have identical nonzero signed profiles; their differing epsilon and residual dimensions give first reached FULL fresh cost<5/4 and second<1/2. Character boundaries t0,1 and sparse profiles t2,3 are explicit; t0,m0 has a zero old reference atom with zero true mass and total CE0. The first mixture price holds for every real eta by pointwise Q1>=(3/4)Qcan, rather than finite extrapolation.

Every physical query disintegrates its CURRENT complete CE with both actual normalizers retained. Exact reset substitution gives G_final+T_final=CEroot+e1+e2, where e2 uses the child reference inherited FROM Q1, already installed by reset1. Both complete siblings and all old releases stay in the equation. Nonnegative old CE bounds p1=max(e1,0)<5/4,p2=max(e2,0)<1/2, so SAME-bank remainder exceeds3/256 without reclaiming negative credits. Physical influence is unchanged by resets. Independent prescribed terminal CE/KL remains completely additive outside this bank.

Verdict HOLDS at full named scope for both claims, without substantive repair. Rung: independently reconstructed analytic proof with exact finite certificates. First unsupported UNIVERSAL line: influence-priced arbitrary incoming source construction or further useful resets at a fixed dimension-independent rate from the SAME diminished bank. This proof supplies neither.''',
'executed validation with domain, arithmetic, commands and outputs':f'''FROZEN_SPEC.json precedes all jobs. From this run execute python -B -X utf8 code/check.py pilot, then code/check.py. Pilot:15 histories/{pilot['assertions']} assertions PASS. Main:48 histories/{result['assertions']} assertions PASS in{result['runtime_seconds']:.3f}s. The fixed domain is(w,m)=(4,0),(4,1),(5,0), every d=0..w and eta0,1/8,1/4:16 prefix depths and48 two-reset histories. A fixed labelled zero-path comb policy is checked finitely; arbitrary-policy scope follows analytically from its exact finite ledger and original reach2^-d. No symmetry or all-policy census is falsely claimed; no automatic dimension increase occurs.

The implementation imports only OWN previously accepted A086 direct-character/physical-edge arithmetic, whose hash is pinned. It imports no A094/A095 checker. Integer direct character sums, Fraction physical edges/actual normalizers and rational log intervals verify complete references. Eighteen-term range-reduced atanh bounds with exact remainder are rounded outward to96 binary fractional bits. Symbolic log-linear expressions verify the WHOLE expectation identity exactly, not merely within floating tolerance. Both nonunit normalizers and true-zero fibers occur. True-zero terminal labels retain product-compatible reference mass. Both signed reset charges are positive in actual cases: first{positive1}, second{positive2}; second is negative in{negative2}. There are{zero_cases} explicit zero-reference boundary histories. Every cumulative booking and original influence telescope passes; incomplete/failed execution would emit FAIL_OR_INCOMPLETE and a nonzero exit. Pilot counts are not added to the main total.

The separate core-only padding formalization targets forall natural m,16m+17<=17*2^m. Fresh memok exits1; status{formal['status']} means the compiler is NOT launched. out/LEAN_ADMISSION.txt and LEAN_RECEIPT.json retain the hold. This provides no Lean certificate and is not a mathematical refutation. Mathematical helper estimate140MB, observed internal runtime below55s; peak RAM unmeasured. No heavy search, Mathlib build, GPU, detached worker, window-opening launcher, other-agent process stop or new worker is used.''',
'proof dependencies and changed downstream conclusions':'''The exact source versions/statements/hashes are unchanged; local claim copies add A086's independent reviews. The graph is acyclic: two-reset@1 uses one-reset@1 and all-wide@1; one-reset@1 uses all-wide@1; the prior all-wide review does not depend on either new claim. out/DEPENDENCY_AND_SIGN_CHECKS.json records this and nonzero sign/boundary coverage. Source reference construction and point-path bounds are reconstructed, not inferred from BOARD status alone. Two scoped source proofs now have this independent reconstruction; canonical registry adoption and a further independent review of the two-reset theorem remain separate. Universal FEI constant improvement is zero. A095's remaining-wide-coordinate reset and arbitrary repeated reset payment remain unpaid.''',
'one next mathematical action and independent reviewer':'''Audit A011's NEW arbitrary-core source-prefix fresh-floor v2 while retaining its ORIGINAL C0 and old U_star, then isolate the first SAME-rate second-representation-edit admission against genuinely unused original capacity. A094 is the independent reviewer, A011 the producer, and A095/A096/A097/A099 consume this completed ownership audit. A095's post-two-reset wide-query target is still useful as a stress fixture, but another structural-family enumeration would not remove the arbitrary-core/source hypothesis. Do not refresh C0 or turn rate4C0+15 into a newly funded bank after each edit.''',
'actual persistence receipts or precise save blocker':'''All four protocol files, full reconstruction, frozen spec, independent helper, exact outputs, formal admission/source receipt, source hashes, dependency/sign checks and persistence/schema receipts are saved in this assigned run. STATUS has two lines; WORKLOG and LEARNED receive dated updates. Saved protocol files and hashes are reread before completion, every file is below20MB, and no remote persistence is presumed. Research mutations stay inside A086; no git, mail, brain research write, trading access, source-tree mutation or other-agent edit is performed. Required wake/checklist bookkeeping is separate. Brain self-care is degraded: stale owner-model/state-of-mind notes were surfaced and are excluded from the mathematical premises. Slow source loading and one corrected local intake path are execution issues, not mathematical failures. Supervisor copying, remote mirrors, canonical adoption and downstream use remain unverified.'''
}
report='# A086: two narrow resets independently paid from one original bank\n\n'+'\n\n'.join('## '+k+'\n\n'+fields[k] for k in protocol['required_per_run']['report_fields'])
report+='''\n\n## Universal bridge

This stage moves C024 history transfer and C019 stopping-tree payment through C020 complete-reference cost by independently accepting TWO actual prescribed narrow resets from the SAME original rate4 source bank, for all widths, padding, prior adaptive wide histories and allowed continuum mixtures. The original451/256 quota pays both conservative positive bookings with surplus>3/256, retaining every old release and both complete terminal bills; the one-reset dependency is independently reconstructed too. Universal constant improvement is zero: arbitrary-core initial source pricing and fixed-rate cumulative edits remain unpaid. NEXT audits A011's new arbitrary-core source-prefix mechanism and its SAME-bank second-edit bottleneck because that removes the structural profile assumption and tests rate inflation, which another isolated class bound cannot settle.\n'''
(R/'REPORT.md').write_text(report,encoding='utf-8',newline='\n')
(OWN/'STATUS.md').write_text('STATE: Stage18 COMPLETE_LOCAL: A095 TWO narrow resets and A094 one-reset dependency independently HOLD at SAME original rate4;54283 exact checks/48 histories PASS; FEI OPEN.\nNEXT: Audit A011 NEW arbitrary-core source-prefix floor v2 and SAME-rate second edit with ORIGINAL C0/U_star, old debits and both terminals retained; A094 review; do not renew source bank.\n',encoding='utf-8',newline='\n')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:f.write(f'\n{stamp} {R.name}: Independent A095 two-reset@1/A094 one-reset@1 reconstruction HOLDS without repair. {result["assertions"]} exact checks/48 histories PASS, {result["runtime_seconds"]:.3f}s; exact symbolic G+T=CEroot+e1+e2 with second inheritance from Q1 and all old bills. Fresh memok held formal attempt; no compiler. Next NEW A011 arbitrary-core/source-prefix v2 and fixed-rate second edit; full FEI OPEN.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:f.write(f'\n{stamp}: All w>=4,m>=0/adaptive wide prefixes: ORIGINAL 4Iroot-CEroot>451/256 differs from mean-terminal surplus. Prescribed first h_t*h1 mixed eta<=1/4 reset costs reach<5/4; second -h_t reset reach<1/2. With old full releases retained, final ledger=CEroot+e1+e2, e2 inherited FROM Q1; p1+p2<7/4 leaves>3/256 at SAME rate4. t0,m0 second canonical old atom is0 with true mass0 (selector dictator CE0), so never force reference positivity on every atom or log0 there. Arbitrary-core initial pricing/fixed-rate repeated edits remain unpaid; a fresh C0 after each edit would hide rate inflation.\n')
expected=set(protocol['required_per_run']['progress_fields']);expected.discard('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
for c in claims:assert set(c)==set(protocol['required_per_run']['claim_fields'])
assert load(R/'PROGRESS.json')==load(R/'PACKET_DELTA.json')
assert len((OWN/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
actual=(R/'REPORT.md').read_text(encoding='utf-8')
assert actual.endswith('another isolated class bound cannot settle.\n') and all('## '+k in actual for k in fields)
save(O/'SCHEMA_VALIDATION.json',{'status':'PASS','claim_fields_exact':True,'progress_fields_exact':True,'packet_delta_identical':True,'source_claim_and_proof_hash_verified':True,'rolling_status_two_lines':True,'dependency_graph_acyclic':True})
manifest=[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']
assert all(x['bytes']<20*1024*1024 for x in manifest)
save(O/'PERSISTENCE_RECEIPTS.json',{'at':stamp,'artifacts':manifest,'rolling':[{'path':str(OWN/p),'sha256':sha(OWN/p)} for p in ['STATUS.md','WORKLOG.md','LEARNED.md']],'remote_verification':'UNVERIFIED'})
for x in load(O/'PERSISTENCE_RECEIPTS.json')['artifacts']:assert sha(R/x['path'])==x['sha256']
print(json.dumps({'status':'COMPLETE_LOCAL','assertions':result['assertions'],'histories':48,'formal':formal['status'],'positive_first':positive1,'positive_second':positive2,'zero_boundary_cases':zero_cases,'artifacts_verified':len(manifest),'full_fei':'OPEN'}))
print('ACTUAL_REPORT:',actual.splitlines()[0])
print('NEXT_LEAD:',[(x['claim_id'],x['version']) for x in future_meta])
completed=subprocess.run([sys.executable,'-B',r'task_checklist_hook.py','done','T-20261023-113','A086 stage18: A095 two-reset and A094 one-reset scoped proofs independently HOLD;54283 exact checks/48 histories;all protocol and rolling files verified;full FEI OPEN;formal admission held.'],capture_output=True,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW)
print('CHECKLIST_RETURN_CODE',completed.returncode)
if completed.stderr:print(completed.stderr[:700])
raise SystemExit(completed.returncode)
