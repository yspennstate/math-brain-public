from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,hashlib,sys
sys.set_int_max_str_digits(100000)
ROOT=Path(__file__).resolve().parents[1]; AGENT=ROOT.parents[1]; OUT=ROOT/'out'
TEAM=AGENT.parents[1]
LEAD=TEAM/'claude/B17/runs/20261011T224300Z-claude-B17-erasure-census-affine-bridge'
A071=TEAM/'agents/A071/runs/20261011T233808Z-fleet05-A071-search-space-design'
A082=TEAM/'agents/A082/runs/20261012T004123Z-fleet05-A082-finite-inequalities'
A074=TEAM/'agents/A074/runs/20261012T043949Z-fleet05-A074-independent-reproducer'
BASE=Path(r'~\mop_fei100\reports\fei-2026-10-11')
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x): p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(statement,hyp):return hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
now=datetime.now(timezone.utc).isoformat(); protocol=read(BASE/'EXECUTION_PROTOCOL.json')
failure=read(OUT/'small_failure_certificate.json'); math=read(OUT/'math_audit.json')
screen=read(OUT/'screen_audit.json');pilot=read(OUT/'screen_pilot.json')
# Clarify legacy output key after the final source audit's naming correction.
for name,data in [('screen_audit.json',screen),('screen_pilot.json',pilot)]:
    old='source_2^-46_bound_valid_for_actual_n4_domain'
    if old in data:data['source_2^-46_bound_valid_for_this_prime_count']=data.pop(old);save(OUT/name,data)
assert failure['terms']==130
err=tuple(map(Q,failure['error_interval']));assert err[0]>Q(failure['claimed_error_bound_upper']) and err[0]>Q(failure['computed_S_error_bound'])
assert Q('8.0557')<err[0]<=err[1]<Q('8.0558')
assert Q(screen['safe_eta'])<Q(1,1<<43) and Q(pilot['safe_eta'])<Q(1,1<<46)
assert Q(1,1<<40)*(1-Q(screen['safe_eta']))>Q(screen['safe_eta'])
assert sha(ROOT/'code/source_certlog.py')==failure['helper_sha256']==sha(LEAD/'code/certlog.py')
# Independently generate the exact 64-edge/complement mask set and reconcile A074.
edges={sum(1<<x for x in [a,a^(1<<i)]) for a in range(16) for i in range(4)}
expected=edges|{65535^m for m in edges}; c74=read(A074/'out/census_n4.json')
assert len(expected)==64 and expected==set(c74['equality_masks'])
# Check complete source-bound prior replay receipts rather than repeat either census.
c71=read(A071/'out/full_census.json');c82=read(A082/'out/review_census.json')
assert c71['complete'] and c82['complete']
assert c71['enumeration_sha256']==c82['representative_sha256']
assert c71['counts']['entropy_evaluated']==c82['counts']['canonical_translation']==5778648
assert c71['candidate_masks']==c82['candidates']==[7]
assert c71['counts']['raw']==c82['counts']['raw']==1<<31
original=next(c for c in read(LEAD/'CLAIMS.json') if c['claim_id']=='B17-KB5-CUTOFF')
assert digest(original['exact_statement'],original['hypotheses'])==original['statement_sha256']
review=dict(original);review['proof_source']={'original_run':str(LEAD),'original_proof_source':original['proof_source'],'independent_reconstruction':str(ROOT/'REPORT.md'),'own_output':str(OUT/'math_audit.json')}
review['review_records']=original['review_records']+[{'reviewer':'A085/fleet05','verdict':'ACCEPT_AT_STATED_SCOPE','at_utc':now,'method':'Independent Walsh/direct character/inverse/physical edge reconciliation; exact prime forms and rational signs at every coordinate','substantive_original_repair':False,'source':str(ROOT/'REPORT.md')}]
review['status']='INDEPENDENTLY_REVIEWED_AT_STATED_SCOPE';review['next_consumers']=list(dict.fromkeys(review['next_consumers']+['A090','A094','B20']))
statement='The audited B17 certlog.py SHA256 1990ab0cd16537a6ae3f9d03bbcb1ca5c16db9f1a54590385dd0ec096fadb99f has a false documented 2^(-46) S error bound for its allowed up-to-600-term integer prime-log screen: in NumPy 2.4.3 the saved Fortran-contiguous (2,130) input with primes through 733 and exponents below 2^50 has exact certified positive summation error between 8.0557 and 8.0558, while 2^(-46) S<8.0001, for both exact and source-computed S. For the intended matching-dimension first-m-prime domain, m<=600, checked log constants have relative error <=u=2^(-53); under normal IEEE round-to-nearest products and sums, error is bounded by eta_m S with eta_m=(m+1)/(2^53-m)<2^(-43). Hence the existing 2^(-40) computed-S sign threshold is safe. In the actual m=54 four-bit census domain eta_54<2^(-46), so no original finite Boolean constant is refuted.'
hyp=['Saved exact coefficient vector in out/small_failure_certificate.json; integer dtype, |e|<2^50','Fortran-contiguous (2,130) input, NumPy 2.4.3, source helper version pinned by SHA256','Safe-bound theorem assumes matching coefficient/prime dimensions with first m primes, m<=600','IEEE binary64 round-to-nearest; normal finite products and sum; source prime constants independently certified within relative error 2^-53','No assertion that the screen-error witness is a Boolean spectrum; no globally smallest failure claim']
new={'claim_id':'A085-CERTLOG-GENERAL-ERROR-BOUND-FAILURE','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':digest(statement,hyp),'contributors':['A085/fleet05'],'proof_source':['REPORT.md','code/audit.py','out/small_failure_certificate.json','out/screen_pilot.json','out/screen_audit.json'],'proof_dependencies':['Positive atanh series with proved rational remainder','Elementary IEEE rounding-factor bound gamma_m=mu/(1-mu)'],'review_records':[],'status':'EXACT_COUNTEREXAMPLE_AND_SCOPED_REPAIR_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[{'source_file':str(LEAD/'code/certlog.py'),'source_sha256':failure['helper_sha256'],'locator':'LinLog.float_screen docstring','exact_false_statement':'Integer entries <2^50 and <=600 terms imply |computed form-true form|<2^-46 S without any layout restriction.'}],'first_unproved_line':None,'next_consumers':['A081','A082','A083','A090','A094','B17','B15','B20']}
claims=[new,review]
assert all(set(c)==set(protocol['required_per_run']['claim_fields']) for c in claims)
assert all(digest(c['exact_statement'],c['hypotheses'])==c['statement_sha256'] for c in claims)
save(ROOT/'CLAIMS.json',claims)
verdicts=[{'target':'certlog.py advertised 600-term 2^-46 S bound','verdict':'ERROR','witness':'out/small_failure_certificate.json','impact':'General helper error budget must change; source sign threshold and actual census constants survive'}, {'target':'B17-KB4-CENSUS@1','verdict':'HOLDS_SOURCE_LOGIC_WITH_NO_FULL_RERUN','checked':'Actual m54 screen bound, integer ranges, attaining values, 64/32/192 orbit saturation; A074 exact equality-mask set','limitation':'A085 did not rerun bundled all-table four-metric census'}, {'target':'B17-KB5-CUTOFF@1','verdict':'ACCEPT_AT_STATED_SCOPE','checked':'All coordinates, exact coefficients/influences, K5>107/40>K4'}, {'target':'A071-EXACT-FIVEBIT-ERASURE-SELECTION@1','verdict':'HOLDS_LOOKUP_COVERAGE_AUDIT_WITH_PRIOR_REPLAY_RECONCILIATION','checked':'289 lookup upper bounds, seed lower, integer bounds, covering filters, 640 orbit, A071/A082 full replay hashes/counts','limitation':'A085 did not rerun 2^31-mask census'}]
save(ROOT/'CERTIFICATE_FAILURE.json',{'packet_id':'A085','helper_error':failure,'completed_scope_verdicts':verdicts,'existing_finite_claims_invalidated':[],'required_helper_change':'Use 2^-43 S under explicit matching <=600-prime integer domain, or prove stronger layout-specific reduction bound. Keep 2^-40 screen threshold.','smallest_failure_qualification':'130 is the smallest prefix in this frozen construction, not globally minimal.','full_fei':'OPEN'})
save(OUT/'review_verdicts.json',{'at_utc':now,'verdicts':verdicts,'A074_64_masks_match':True,'A071_A082_complete_replay_receipts_match':True,'own_census_rerun':False})
files=[TEAM/'BOARD.md',TEAM/'claude/B17/STREAM_NOTES.md',BASE/'EXECUTION_PROTOCOL.json',LEAD/'CLAIMS.json']
files += [LEAD/f for f in ['code/certlog.py','code/census_n4.py','code/search_n56.py','code/write_records.py','out/census_n4.json']]
files += [A071/f for f in ['REPORT.md','CLAIMS.json','code/sparse_search.py','code/full_census.py','code/check_final.py','out/full_census.json']]
files += [A082/f for f in ['REPORT.md','out/review_census.json','out/review_verdict.json']]
files += [A074/f for f in ['REPORT.md','out/census_n4.json']]
files += [TEAM/'claude/B15/runs/20261011T225100Z-claude-B15-erasure-countersearch/CLAIMS.json']
save(OUT/'source_receipts.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in files])
progress={'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B17','packet_id':'A085','gap_id':'FEI-B17-A085-INITIAL','attempt_id':'A085-stage2-screen-range-orbit-audit','method':'Exact allowed-layout counterexample; source-hash-bound gamma error proof; independent Walsh/edge/orbit/lookup reconstruction without census reruns','mathematical_delta':'False general 2^-46 S helper budget exposed by 130 terms; existing 2^-40 threshold proved safe and actual 54-prime bound proved. B17 five-bit cutoff accepted; four-bit orbit/range/logic and A071 lookup/coverage audits pass. No finite FEI constant invalidated.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'NARROW_HELPER_ERROR_FOUND_AND_REPAIR_PROVED; FINITE_CONSTANTS_SURVIVE; FULL_FEI_OPEN','claim_versions_used':[{'claim_id':'B17-KB4-CENSUS','version':1,'use':'Source numerical-logic/orbit audit, no full bundle replay'},{'claim_id':'B17-KB5-CUTOFF','version':1,'use':'Object of independent exact reconstruction'},{'claim_id':'A071-EXACT-FIVEBIT-ERASURE-SELECTION','version':1,'use':'Lookup/covering audit using prior A082 complete replay receipts'},{'claim_id':'A082-FINITE-TRUE-ERASURE','version':1,'use':'Its n4 value has independent A074 full-census source'}],'claims_created_or_changed':[{'claim_id':new['claim_id'],'version':1,'change':'New narrow generic-helper error certificate and scoped threshold repair'},{'claim_id':review['claim_id'],'version':1,'change':'Independent scoped acceptance; statement unchanged'}],'source_artifacts':['REPORT.md','CERTIFICATE_ADVERSARY.md','CERTIFICATE_FAILURE.json','FROZEN_SPEC.json','RECHECK_SPEC.json','code/audit.py','out/screen_audit.json','out/small_failure_certificate.json','out/math_audit.json','out/review_verdicts.json','out/source_receipts.json'],'next_consumers':['A081','A082','A083','A090','A094','A097','A064','A099','B17','B15','B20'],'next_action':'A090/A094 independently reconstruct screen-error and eta proof; B17 correct generic helper contract. Audit a concrete A097/A064/A099 terminal-inclusive stopping residual with certified affine-five leaf constants, retaining nonreused influence.','stagnant_substantive_attempts':0,'blockers':['Independent review of A085 helper repair and downstream correction pending','Full FEI requires unrestricted terminal-inclusive nonreusing path payment; finite constants do not prove it'],'packet_ids':['A085']}
assert set(progress)=={k.split(' (')[0] for k in protocol['required_per_run']['progress_fields']}
save(ROOT/'PROGRESS.json',progress);(ROOT/'PACKET_DELTA.json').write_bytes((ROOT/'PROGRESS.json').read_bytes())
(AGENT/'STATUS.md').write_text('STATE: A085 stage2 complete: exact 130-term helper error-budget failure; existing screen threshold safe; cutoff/orbit/lookup audits pass; new repair review pending; full FEI OPEN.\nNEXT: A090/A094 review helper certificate; B17 correct generic contract; audit A097/A064/A099 terminal-inclusive stopping residual with affine-five leaves and one coordinate budget.\n',encoding='utf8')
entry=f'\n{now} — Stage 20261013T213517Z: read new board and B17 v2. Did not repeat censuses/grid. Certified Fortran (2,130) error>8.0557 against advertised bound<8.0001; proved eta600<2^-43 and eta54<2^-46, preserving sign threshold and finite conclusions. Five Boolean witnesses, 64/32/192/640 orbit counts, 289 lookup bounds, integer ranges and prior full-replay receipts checked; 167+2402+563+291 counted checks. Low-order-convergent harness assumption corrected and logged. Saved exact failure, scoped acceptance and protocol artifacts; full FEI OPEN.\n'
with (AGENT/'WORKLOG.md').open('a',encoding='utf8') as f:f.write(entry)
with (AGENT/'LEARNED.md').open('a',encoding='utf8') as f:
    f.write(f'\n## {now} stage 2\n\n- B17 certlog SHA256 {failure["helper_sha256"]}: advertised <=600-term 2^-46 S error bound is false for allowed Fortran-layout arrays. Saved 130-prime integer form has certified error in (8.0557,8.0558), versus bound<8.0001. Smallest tested prefix, not global minimality; not a Boolean-spectrum witness.\n- On intended matching first-m-prime domain, m<=600, logs verified to relative u=2^-53 and integer conversion exact. eta_m=(m+1)/(2^53-m) bounds signed and absolute-sum errors. eta600<2^-43 and delta(1-eta)>eta for delta=2^-40 prove existing sign threshold safe. Actual n4 m54 gives eta54<2^-46 for every reduction layout.\n- A scale of 2^-320 is a rounding resolution, not automatically a total log error bound. Positive series remainder must stay in the interval; source carries it correctly.\n- Exact zero of one float-selected coordinate ratio alone does not classify an extremizer. Orbit saturation (64 known extremizers versus exactly 64 selected-coordinate zeros) completes that argument. Full orbit sets reconcile with A074.\n- All 289 A071 five-bit lookup upper entries and seed lower checked independently; 16-packet numerator ceiling<2^63. Values may exceed 2^53 safely because they remain int64, not floating. Covering filters order physical influences, then translate; no affine mixing. No full census rerun needed after A082 independent completion.\n')
report=(ROOT/'REPORT.md').read_text(encoding='utf8');assert all(f in report for f in protocol['required_per_run']['report_fields'])
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
v={'protocol_fields':'PASS','original_statement_hash':'PRESERVED_AND_RECHECKED','compatibility_copy':'BYTE_IDENTICAL','helper_copy_hash':'MATCHES_ORIGINAL','exact_error_violation':'PASS','source_screen_threshold':'SAFE_ON_STATED_DOMAIN','A074_orbit_set':'64_MASKS_MATCH','A071_A082_prior_complete_replay':'COUNTS_AND_HASH_MATCH','lookup_entries':289,'integer_ranges':'PASS','own_full_census_replay':False,'new_audit_review':'PENDING','shared_source_mutations':False,'mirror_or_adoption':'UNVERIFIED','full_fei':'OPEN','at_utc':now}
save(OUT/'validation.json',v)
manifest=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='manifest.json' and '__pycache__' not in p.parts:
        assert p.stat().st_size<20_000_000;manifest.append({'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size})
save(OUT/'manifest.json',manifest);assert all(sha(ROOT/x['path'])==x['sha256'] for x in manifest)
print(json.dumps({'validation':v,'files':len(manifest),'largest_bytes':max(x['bytes'] for x in manifest)},indent=2),flush=True)
