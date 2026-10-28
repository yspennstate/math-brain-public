from pathlib import Path
import copy,json,hashlib,datetime
R=Path(__file__).resolve().parents[1];HOME=R.parents[1];NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def save(p,x):Path(p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def digest(s):return hashlib.sha256(s.encode('utf-8')).hexdigest()
pins=read(R/'out/SOURCE_PINS.json');res=read(R/'out/EXACT_RESETS.json');assert res['status']=='PASS' and res['seconds']<55
assert res['case_count']==96
review=(R/'REVIEW.md').read_text(encoding='utf-8').replace('Verdict pending exact replay: the analytic chain below reconstructs','Verdict: HOLDS at the entire named scope. The exact replay passes and the analytic chain below reconstructs')
(R/'REVIEW.md').write_text(review,encoding='utf-8')
source95=read(R/'out/source_snapshots/06_CLAIMS.json');source94=read(R/'out/source_snapshots/08_CLAIMS.json')
c2=copy.deepcopy(source95[0]);c1=copy.deepcopy(source94[1])
old=read(R/'out/source_snapshots/03_PROOF_DEPENDENCIES.json');g=copy.deepcopy(old);g['run_id']=R.name
g['prior_certificate']={'snapshot':'out/source_snapshots/03_PROOF_DEPENDENCIES.json','sha256':sha(R/'out/source_snapshots/03_PROOF_DEPENDENCIES.json'),'scope':'Prior76 nodes and their evidence states preserved; this is not a new proof review of every old source.'}
units={'entropy':'bits','influence':'ordinary uniform physical total influence','log':'base2 except explicit ln'}
def node(cid,statement,hypotheses,deps=(),status='INDEPENDENTLY_RECONSTRUCTED_BY_A081'):
 return {'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':digest(statement),'statement_hash_convention':'UTF8 exact_statement only','units':units,'status':status,'proof_sources':[{'path':str(R/'REVIEW.md'),'sha256':sha(R/'REVIEW.md')}],'proof_dependencies':list(deps),'evidence':[{'path':str(R/'out/EXACT_RESETS.json'),'sha256':sha(R/'out/EXACT_RESETS.json')}],'first_unproved_line':None}
root='A095-UNBOUNDED-WIDTH-SIGNED-PROFILE-HISTORY@1'
bank=node('A081-STRUCTURAL-ORIGINAL-ROOT-RESERVE','For every w>=4,m>=0 on the exact prescribed h_w*h2 fair-selector point0 source, the ORIGINAL unused root quota S0=4I_root-CE_root is strictly greater than451/256. This sharpens395/256 for that same account; it does not rename or renew the surviving-terminal3/256 account.',['Exact original source/reference of A095 wide-only theorem; bits','All old releases and complete references conserved'],[root])
n1=node(c1['claim_id'],c1['exact_statement'],c1['hypotheses'],[root,bank['claim_id']+'@1'])
cost2=node('A081-SECOND-CANONICAL-NARROW-RESET-COST','For t=w-d>=0 after the first prescribed narrow reset, the actual child00 source is -h_t. Its complete canonical source-spectrum cost C2 is<2 when t>=4 and<4 otherwise; for t=0,m=0 its actual selector spectrum and reference are(0,1),cost0. With original reach2^(-d-2), the reached fresh cost is<1/2.',['w>=4,m>=0,0<=d<=w; all-zero point edit','Canonical reference on TRUE source support; W=1 allowed only with matching zero true atom','No arbitrary-reference or individual-child influence price asserted'])
n2=node(c2['claim_id'],c2['exact_statement'],c2['hypotheses'],[n1['claim_id']+'@1',bank['claim_id']+'@1',cost2['claim_id']+'@1'])
unpaid=node('A081-OPEN-WIDE-RESET-AFTER-TWO-NARROW','After BOTH prescribed narrow resets, expose an actual remaining wide coordinate and pay its SPECIFIED fresh reference reset, old query releases, cumulative booked positive e1/e2 and complementary full terminal from the SAME remaining original ancestor bank.',['All old debits retained; no fresh quota; actual physical child normalizers','Structural target only; arbitrary-core universal leaf remains separately open'],status='OPEN')
unpaid['proof_sources']=[];unpaid['evidence']=[];unpaid['first_unproved_line']=unpaid['exact_statement']
for nn,idx in [(n1,8),(n2,6)]:
 nn['source_claims_pin']={'path':str(R/pins[idx]['snapshot']),'sha256':pins[idx]['sha256']}
 original=c1 if idx==8 else c2
 nn['source_statement_sha256']=original['statement_sha256'];nn['source_declared_dependencies']=original['proof_dependencies']
g['nodes'] += [bank,n1,cost2,n2,unpaid]
for i,p in enumerate(pins):g['sources']['stage8_'+str(i)]={'local_path':str(R/p['snapshot']),'local_sha256':p['sha256'],'original_local_path':p['source'],'pin_scope':'Exact local immutable snapshot; remote adoption unverified'}
contract={'quota':'4I_original','bookings':['max(e1,0)','max(e2,0)'],'old00_owner':'normalized physical child inherited FROM Q1','complete_siblings':'ALL','old_query_releases':'ALL','source':'point0 padded h_w*h2 only','eta_domain':'real[0,1/4]','units':'bits','no_reset_credit_reclaimed':True}
g['stage8_ledger_contract']=contract
g['scope_relations'].append({'from':n2['claim_id']+'@1','to':'A081-OPEN-PRESCRIBED-WEAK-RESET@1','kind':'STRUCTURAL_PROGRESS_DOES_NOT_DISCHARGE_UNIVERSAL_LEAF','reason':'Prescribed source and reset rule only; no arbitrary incoming-profile/source construction.'})
g['stage8_unresolved_leaf']=unpaid['claim_id']+'@1'
def key(n):return n['claim_id']+'@'+str(n['version'])
def dep(d):
 if isinstance(d,str):return d
 for k in ['claim_key','claim','key']:
  if k in d:return d[k]
 return d['claim_id']+'@'+str(d['version'])
def valid(graph):
 nodes={key(n):n for n in graph['nodes']};assert len(nodes)==len(graph['nodes']);active=set();seen=set()
 def walk(k):
  assert k in nodes and k not in active
  if k in seen:return
  active.add(k)
  for x in nodes[k]['proof_dependencies']:walk(dep(x))
  active.remove(k);seen.add(k)
 for k in nodes:walk(k)
 assert nodes['FEI-FINAL@1']['status']=='OPEN'
 assert nodes['A081-OPEN-PRESCRIBED-WEAK-RESET@1']['status']=='OPEN'
 assert nodes[unpaid['claim_id']+'@1']['status']=='OPEN'
 for n in graph['nodes'][-5:]:
  assert digest(n['exact_statement'])==n['statement_sha256'];assert n['units']['entropy']=='bits'
 for n in graph['nodes'][-5:]:
  if 'source_claims_pin' in n:assert sha(n['source_claims_pin']['path'])==n['source_claims_pin']['sha256']
 assert nodes[n1['claim_id']+'@1']['hypotheses']==c1['hypotheses'];assert nodes[n2['claim_id']+'@1']['hypotheses']==c2['hypotheses']
 assert len(nodes[n2['claim_id']+'@1']['proof_dependencies'])==3
 assert graph['stage8_ledger_contract']==contract
 return len(seen)
valid(g);guards=[]
def reject(name,fn):
 z=copy.deepcopy(g);fn(z)
 try:valid(z)
 except (AssertionError,KeyError):guards.append({'name':name,'status':'REJECTED'});return
 raise AssertionError(name)
reject('FEI self cycle',lambda z:z['nodes'][0]['proof_dependencies'].append('FEI-FINAL@1'))
reject('cycle through two-reset claim and FEI',lambda z:(z['nodes'][0]['proof_dependencies'].append(n2['claim_id']+'@1'),z['nodes'][-2]['proof_dependencies'].append('FEI-FINAL@1')))
reject('wrong exact dependency version',lambda z:z['nodes'][-2]['proof_dependencies'].__setitem__(0,n1['claim_id']+'@2'))
reject('changed statement with unchanged digest',lambda z:z['nodes'][-2].__setitem__('exact_statement','full FEI'))
reject('nats substitution',lambda z:z['nodes'][-2].__setitem__('units',{'entropy':'nats'}))
reject('wrong source bytes',lambda z:z['nodes'][-2]['source_claims_pin'].__setitem__('sha256','0'*64))
reject('promote FEI by status',lambda z:z['nodes'][0].__setitem__('status','PROVED'))
reject('promote third-reset unpaid leaf',lambda z:z['nodes'][-1].__setitem__('status','PROVED'))
reject('drop second-price dependency',lambda z:z['nodes'][-2]['proof_dependencies'].pop())
reject('substitute arbitrary supplied reference',lambda z:z['nodes'][-2].__setitem__('hypotheses',['arbitrary Q']))
reject('renew original quota',lambda z:z['stage8_ledger_contract'].__setitem__('quota','4I_fresh_child'))
reject('drop first reset positive booking',lambda z:z['stage8_ledger_contract']['bookings'].pop(0))
reject('drop second reset positive booking',lambda z:z['stage8_ledger_contract']['bookings'].pop())
reject('use pre-first-reset old00 reference',lambda z:z['stage8_ledger_contract'].__setitem__('old00_owner','pre-first-reset Q'))
reject('discard complementary sibling terminal',lambda z:z['stage8_ledger_contract'].__setitem__('complete_siblings','only edited child'))
reject('discard old query release',lambda z:z['stage8_ledger_contract'].__setitem__('old_query_releases','only last query'))
save(R/'PROOF_DEPENDENCIES.json',g)
for row in res['cases']:
 for Z in row['child_normalizers']:
  from fractions import Fraction
  assert sum(Fraction(z) for z in Z)==2 and all(Fraction(z)>0 for z in Z)
 assert Fraction(row['conservative_final_reserve_lower'])>Fraction(3,256)
save(R/'out/GRAPH_VALIDATION.json',{'status':'PASS','nodes':valid(g),'prior_nodes':len(old['nodes']),'new_nodes':5,'guards':guards,'full_fei':'OPEN','general_unpaid_reset':'OPEN','source_specific_next_reset':'OPEN','new_pins':len(pins),'scope':'New source pins and graph checked; prior evidence states inherited, not all old theorems re-reviewed'})

for c,nn,locator in [(c1,n1,'sections1–2,4'),(c2,n2,'sections1–5')]:
 c['proof_dependencies']=[{'claim_id':dep(x).rsplit('@',1)[0],'version':int(dep(x).rsplit('@',1)[1]),'units':'bits','scope':'Exact reviewed graph dependency; source original dependency text preserved in graph'} for x in nn['proof_dependencies']]
 c['review_records'].append({'reviewer':'A081/account03','at':NOW,'verdict':'ACCEPT_AT_ENTIRE_ORIGINAL_SCOPE_NO_REPAIR','proof_source':str(R/'REVIEW.md'),'locator':locator,'validation_source':str(R/'out/EXACT_RESETS.json'),'independence':'Independent physical truth tables, exact Walsh/edge/reference implementation using own prior scalar library; no author checker imported','reviewer_contributed_repair':False,'rung':'analytic all-parameter reconstruction with exact finite certificate; full theorem not Lean-checked'})
 c['status']='INDEPENDENTLY_ACCEPTED_AT_ENTIRE_ORIGINAL_SCOPE_BY_A081';c['first_unproved_line']=None
statement=f'A081 stage8 dependency certificate preserves all76 prior nodes, adds five exact scoped nodes for the original reserve and two prescribed narrow reset chain plus its next unpaid leaf, has81 nodes without a proof cycle, and rejects16 declared invalid mutations. Full FEI and the arbitrary-core universal reset leaf remain OPEN.'
cert={'claim_id':'A081-VERSIONED-DEPENDENCY-CERTIFICATE','version':8,'exact_statement':statement,'hypotheses':['Frozen local source bytes and exact statement versions','Physical influence and base-two complete CE; review/workflow evidence separate from proof edges'],'statement_sha256':digest(statement),'contributors':['A081/account03'],'proof_source':{'graph':str(R/'PROOF_DEPENDENCIES.json'),'validator':str(R/'code/finalize.py'),'output':str(R/'out/GRAPH_VALIDATION.json')},'proof_dependencies':[{'claim_id':c2['claim_id'],'version':1,'statement_sha256':c2['statement_sha256'],'scope':'Entire original structural two-reset theorem only'}],'review_records':[],'status':'CHECKED_LOCAL_DEPENDENCY_CERTIFICATE','supersedes':['A081-VERSIONED-DEPENDENCY-CERTIFICATE@7 as current graph snapshot; prior artifact preserved'],'refutes':[],'first_unproved_line':'Next specified wide reset after cumulative p1+p2; universal arbitrary-core source/reference payment remains unpaid.','next_consumers':['A094','A095','A086','A096','A097','A099','B17','B20']}
save(R/'CLAIMS.json',[c1,c2,cert])
next_action='Price one actual remaining-wide query and prescribed fresh reset AFTER BOTH p1+p2 bookings, with SAME original bank, inherited child normalizers and complementary full terminal; A094/A086 independently challenge scope.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B17','packet_id':'A081','gap_id':'G-R-MISMATCH','attempt_id':'A081-stage8-two-prescribed-reset-chain-audit','method':'Independent all-parameter source/profile and exact conserved-ledger reconstruction, bounded rational replay and adversarial versioned graph checks','mathematical_delta':'A094 one-reset and A095 two-reset@1 independently accepted at entire original scopes. SAME rate4 original-bank surplus>451/256 pays cumulative positive bookings<5/4+1/2, leaving>3/256 for every width/padding/adaptive wide prefix. Universal constant improvement zero.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_RESET_DEPENDENCIES_ACCEPTED_FULL_FEI_OPEN','claim_versions_used':[root,c1['claim_id']+'@1',c2['claim_id']+'@1','A081-VERSIONED-DEPENDENCY-CERTIFICATE@7'],'claims_created_or_changed':[c1['claim_id']+'@1',c2['claim_id']+'@1','A081-VERSIONED-DEPENDENCY-CERTIFICATE@8'],'source_artifacts':['out/SOURCE_PINS.json','out/FROZEN_SPEC.json','REVIEW.md','out/EXACT_RESETS.json','PROOF_DEPENDENCIES.json'],'next_consumers':['A094','A095','A086','A096','A097','A099','B17','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Arbitrary-core source reference and hereditary prescribed-reset payment unproved','Formal compiler not admitted: fresh memok exit1; no compiler launched','Supervisor copying, canonical adoption and mirror verification unverified'],'packet_ids':['A081']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
lean=read(R/'out/LEAN_RECEIPT.json') if (R/'out/LEAN_RECEIPT.json').exists() else {'status':'NO_RECEIPT'}
report=f'''# exact target, quantifiers, hypotheses and units

A081/B17 stage8 audits A094-NARROW-QUERY-PRESCRIBED-RESET-SAME-RATE4@1 and A095-TWO-NARROW-RESETS-SAME-RATE4-BANK@1 at their entire exact original scopes. For every w>=4,m>=0, any finite adaptive wide-only prefix and prescribed real eta in[0,1/4], retain the same source-spectrum incoming reference on the fair-selector point0 edit of padded h_w*h2, both full terminal siblings and every old complete release through the two specified narrow resets. Entropy/CE/KL are bits; influence is actual uniform physical influence. Full FEI remains OPEN. The current campaign endpoint is23 October14:49 UTC.

# sources actually read, revisions and theorem locators

Read current BOARD snapshot23 October00:41 UTC, B17 STREAM_NOTES v2, own stage7 STATUS/LEARNED and prior76-node graph. The B17 initial census/uncertainty baseline is retired rather than repeated. Critical new sources: A095 run20261022T235414Z CLAIMS and full DERIVATION1–4; A094 run20261022T230414Z CLAIMS and full DERIVATION1–6. The execution protocol v2 is reloaded and its exact fields enforced. out/SOURCE_PINS.json freezes10 files, including current coordination, prior graph and own scalar library. A096/A097 current claims were read for navigation; no new mathematical acceptance of those chains is inferred. Earlier campaign/paper intake is inherited from the pinned stage7 baseline, not represented as a new blanket paper audit.

# complete derivation or exact first unsupported line

REVIEW.md reconstructs the sharper ORIGINAL unused quota S0=4I_root-CE_root>451/256, both actual sparse source profiles, their true supports, boundary sources, and the real-eta mixture domination. The complete reached first fresh cost is<5/4 and the second is<1/2. The second inherited old reference is the normalized physical child FROM Q1 after the first reset. With actual signed substitutions e1,e2, the exact ledger is G_final+T_final=CE_root+e1+e2. Even conservative p1=max(e1,0),p2=max(e2,0) bookings leave S0-p1-p2>3/256 from the SAME original quota. Every complementary full H+KL terminal and old release stays charged. Both source claims HOLD at entire original scope without repair.

The changed451/256 bound sharpens A094's395/256 estimate for the same original-root account by retaining positive terms at w4 and separating w>=5. It does not rename the earlier3/256 surviving-terminal margin. At t0,m0 the second canonical model is(0,1), matching its actual selector spectrum; the zero reference atom has zero true mass and contributes zero, so no positive-normalizer/old-mass assumption is improperly applied.

Rung: independently reconstructed analytic proof with exact finite certificates, not a Lean-checked full theorem. The integer451=320+128+3 formal-attempt status is {lean['status']}; it establishes no formal reset theorem. The first source-specific unpaid line is a further actual wide query and SPECIFIED reset after BOTH positive bookings, with the same diminished bank. Universally paid arbitrary incoming-reference/source profiles remain absent. Neither class theorem closes FEI.

# executed validation with domain, arithmetic, commands and outputs

The frozen spec precedes replay. From this run: python -X utf8 code/check_resets.py --pilot; python -X utf8 code/check_resets.py; python -X utf8 code/finalize.py. Pilot2 cases pass3110 assertions and are a subset, not added again. The full declared domain(w,m)=(4,0),(4,1),(5,0), every d=0..w, eta0,1/8,1/4 and two named prefix policies gives96 policy/reference cases. The policy names coincide physically at d0 and d1; no96-distinct-history assertion is made. Arbitrary width/padding/adaptive policy and every real eta are proved analytically, not extrapolated from this finite set.

The separate implementation imports only A081's own pinned stage7 Walsh/scalar library, not an author checker. Direct physical truth tables, integer Walsh transforms, physical edge counts, exact Fraction reference normalizers, likelihood identities and signed rational-log expressions pass {res['assertions']} new assertions in {res['seconds']:.3f} internal seconds. The prior library's8928 internal assertions are recorded separately and not added. Log bounds use24 range-reduced atanh terms with rational tail and outward2^-80 rounding. Exact expression cancellation checks the complete ledger, not a tolerance. Full normalized references after the first reset differ from the stale pre-reset alternative in actual tested cases. The W1 endpoint and untouched independent prescribed terminal's reference-only atom are retained. Observed core reference-only zero-true-fiber count is0; no claim of a nonzero core-fiber exercise is made.

Graph validation checks81 nodes and16 invalid mutations: proof cycles through FEI, wrong versions/hashes/units, status promotion, renewed quota, missing positive bookings, stale old00 reference, discarded sibling or old release. Estimated mathematical-helper memory120MB; peak unmeasured; no heavy search, GPU, automatic dimension increase, detached job or visible window. Fresh memok exits1, so the compiler is NOT launched; only the core arithmetic source and NOT_ADMITTED receipt are saved. Current compute state read OK with zero recent interventions; no process is stopped for resource relief.

# proof dependencies and changed downstream conclusions

The prior76-node graph and evidence states are preserved; five nodes add the sharpened root reserve, exact A094 first-reset version, second canonical fresh cost, exact A095 two-reset version and new open post-two-reset wide leaf. Local source pins, statement-hash conventions and bits are explicit. The general arbitrary-core reset leaf stays OPEN; the structural reset is a scope relation, not its discharge. A094/A095 review records are evidence, not backwards proof edges. The named two-reset candidate now receives an A081 independent full-scope acceptance; no repair means no contributor conflict is introduced. Universal constant improvement is zero.

# one next mathematical action and independent reviewer

{next_action} A095/A096/A097/A099 may consume these pinned scoped dependencies. Further bare no-reset telescoping is already paid; a new actual reset must retain the cumulative bookings and all current terminals. No handoff message or supervisor adoption is presumed.

# actual persistence receipts or precise save blocker

The four protocol files, REVIEW, graph, frozen spec, independent checker, exact outputs, immutable source snapshots, formal receipt and schema/readback receipts are saved in the assigned run. STATUS remains two lines; WORKLOG and LEARNED receive dated updates. out/PERSISTENCE_RECEIPTS.json hashes local artifacts, all below20MB. Supervisor copying, remote mirror verification and canonical adoption are unverified. Brain self-care is degraded: personal-model/state-of-mind notes are stale and were not relied upon. The user's own-folder-only rule excludes shared checklist/mesh/brain mutation. No git, messaging, trading access or other-agent edit occurs.

# Universal bridge

This stage moves C024 history transfer and C019 stopping-tree payment by independently accepting the full two-prescribed-reset chain at SAME original rate4 for every width, padding and allowed wide prefix, with conservative cumulative reset bookings and all complete terminals. The original-bank bound is sharpened to>451/256 and the post-booking reserve is>3/256; the universal FEI constant improvement is zero. A further specified wide reset after both debits, and arbitrary-core source/reference availability, remain unpaid. NEXT targets that exact hereditary reset rather than repeating automatic no-reset histories, because the missing preserved-bank payment is the exposed route toward the universal bridge.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(HOME/'STATUS.md').write_text(f'STATE: A081 stage8 complete: A094 one/A095 two prescribed narrow resets independently HOLDS; SAME rate4 original bank>451/256 leaves>3/256;{res["assertions"]} exact assertions/16 graph guards PASS; FEI OPEN.\nNEXT: Pay specified remaining-wide query/reset AFTER BOTH p1+p2 from SAME unused original bank with complementary full terminal and old releases; A094/A086 review.\n',encoding='utf-8')
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{NOW} Stage8: independently accepted exact A094 one-reset and A095 two-reset@1 at full original scope. Reconstructed sharp original S0>451/256 versus prior looser395/256 for same account, cumulative bookings<5/4+1/2 and reserve>3/256. {res["assertions"]} exact assertions/96 declared policy-reference cases; own library count separate; W1 zero-reference endpoint retained.81-node graph/16 rejection guards PASS; arbitrary reset/FEI OPEN.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage8: A095 two narrow resets at same rate4 independently holds. Sharpened original ROOT reserve451/256 versus395/256 is a stronger bound on the same4I_root-CE_root account, not the surviving-terminal3/256 bound. First positive reset booking<5/4; second<1/2; cumulative reserve>3/256 without renewing quotas or reclaiming negative credits. Second old00 reference MUST be inherited FROM Q1 after first reset. Canonical -h_t second cost<2 at t>=4,<4 otherwise; t0,m0 actual/reference(0,1) has W1 and zero old true/reference atom, so no positive-old-mass hypothesis applies. Arbitrary real eta<=1/4 follows from reference domination, not sample interpolation. Universal arbitrary-core source/reference and further prescribed wide reset remain unpaid.\n')
protocol=read(R/'out/source_snapshots/05_EXECUTION_PROTOCOL.json');cf=set(protocol['required_per_run']['claim_fields']);pf={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert all(set(c)==cf for c in read(R/'CLAIMS.json'));assert set(progress)==pf
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert all(x in report for x in protocol['required_per_run']['report_fields'])
assert len((HOME/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert all(sha(R/p['snapshot'])==p['sha256'] for p in pins)
save(R/'out/SCHEMA_VALIDATION.json',{'status':'PASS','claim_fields_exact':True,'progress_fields_exact':True,'report_fields_present':True,'progress_delta_equal':True,'rolling_status_two_lines':True,'new_source_pins_valid':True})
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in str(p) and p.name!='PERSISTENCE_RECEIPTS.json'];assert all(p.stat().st_size<20_000_000 for p in files)
save(R/'out/PERSISTENCE_RECEIPTS.json',{'at':NOW,'scope':'LOCAL_ONLY; remote/supervisor adoption unverified','files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]})
print(json.dumps({'status':'PASS','nodes':len(g['nodes']),'guards':len(guards),'new_assertions':res['assertions'],'files':len(files),'full_fei':'OPEN','lean':lean['status']}))
