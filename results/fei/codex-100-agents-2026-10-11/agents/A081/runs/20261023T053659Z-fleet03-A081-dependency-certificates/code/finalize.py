from pathlib import Path
from fractions import Fraction as F
import json,hashlib,copy,datetime
R=Path(__file__).resolve().parents[1];H=R.parents[1]
def load(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def save(p,o):Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def digest(s):return hashlib.sha256(s.encode()).hexdigest()
res=load(R/'out/EXACT_CERTIFICATE.json');assert res['status']=='PASS' and res['seconds']<55
assert F(res['conservative_actual_reserve_lower'])>2
pins=load(R/'out/SOURCE_PINS.json')
for p in pins:assert sha(R/p['snapshot'])==p['sha256']
review='''# Independent reconstruction and exact dependency extension

All costs are bits and influence is ordinary uniform physical influence. Only the literal w=4,m=0,d=0,eta=0 h4*h2 point-selector fixture is claimed. Queries use labels4,5,0 on original source coordinates; selector6 stays unqueried. Every sibling and old release remains in the ledger. No independent terminal funds a charge.

The checker constructs all128 physical Boolean values, computes each Fourier coefficient by a direct character sum (not the author checker or FWHT), and checks normalization. It reconstructs canonical references on actual true source support, including every complementary mask. Actual physical child probabilities determine the posterior transport; zero true fibers receive equal kernels. Raw child normalizers sum to2 and are positive. The third pair is529/452,375/452.

On the third zero child the three (P,Qold,Qfresh) classes are (49/64,18375/33856,63/128) once; (1/64,1695/33856,7/128) seven times; (1/64,113/8464,1/64) eight times. Thus e3=log2(N/D)/512 for N=12250^49*3390^7*452^8 and D=11109^49*3703^7*529^8. Exact integer comparisons N>16D and N^2<512D^2 establish1/128<e3<9/1024. This independently accepts A094's obstruction at its full stated fixture scope, without repair. It rejects a free-reset shortcut only, not FEI or the two-reset theorem.

Let Gj denote all reached complete query releases and Tj all reached complete terminal costs. At each query, parentCE=release+(CEchild0+CEchild1)/2 by definition and the release is independently checked nonnegative. A reset changes no physical function; its exact signed charge is its original reach times (CEfresh-CEinherited). The checker symbolically cancels logarithm terms to verify G3+T3=CEroot+e1+e2+e3 exactly. The second inherited model is transported from Q1, and the third from Q2; no stale reference is used.

The original accepted root bank exceeds451/256. The previous all-parameter theorem books p1=max(e1,0)<5/4 and p2=max(e2,0)<1/2. As p3=e3<9/1024, the SAME original bank leaves strictly more than451/256-5/4-1/2-9/1024=3/1024. This already proves affordability of this fixture, without reclaiming negative charges. A sharper independent interval calculation gives Iroot=91/64 and 4Iroot-CEroot-sum max(ej,0)>2. All complete original releases and both terminal siblings at every query remain present. An untouched product terminal can be retained additively using the previously accepted product-compatible transport; the finite computation itself contains only the core fixture.

Logarithm intervals reuse only A081's prior scalar routine: range reduction to[1,2),24-term atanh series with explicit remainder, outward rounding to2^-80. Positive/negative weights select the appropriate interval endpoints. Exact-zero symbolic cancellations are performed before sign tests. New direct-check assertion count and prior expression-library count are reported separately. This is a rational interval certificate and mathematical proof, not a Lean kernel proof.

The all-parameter remaining-wide-reset leaf stays OPEN: one positive and affordable fixture does not prove payment for arbitrary w,m,eta,wide-prefix histories or an unbounded reset sequence. A095's newer nonvanishing-booking obstruction was read as context only; its all-m proof and A011's arbitrary-core floor are not accepted by this stage. Their reference/policy compatibility and the actual unused original source surplus remain unresolved.
'''
(R/'REVIEW.md').write_text(review,encoding='utf-8')
g=load(R/'out/source_snapshots/00_PROOF_DEPENDENCIES.json');prior_count=len(g['nodes']);g['run_id']=R.name
c=copy.deepcopy(load(R/'out/source_snapshots/03_CLAIMS.json')[1])
units={'entropy':'bits','influence':'ordinary uniform physical total influence','log':'base2 except explicit ln'}
def node(cid,s,h,deps):return {'claim_id':cid,'version':1,'exact_statement':s,'hypotheses':h,'statement_sha256':digest(s),'statement_hash_convention':'UTF8 exact_statement only','units':units,'status':'INDEPENDENTLY_EXACT_CERTIFIED_BY_A081','proof_dependencies':deps,'proof_sources':[{'path':str(R/'REVIEW.md'),'sha256':sha(R/'REVIEW.md')}],'evidence':[{'path':str(R/'out/EXACT_CERTIFICATE.json'),'sha256':sha(R/'out/EXACT_CERTIFICATE.json')}],'first_unproved_line':None}
n=node(c['claim_id'],c['exact_statement'],c['hypotheses'],[])
n['source_claim_statement_sha256']=c['statement_sha256'];n['source_claims_pin']={'path':str(R/pins[3]['snapshot']),'sha256':pins[3]['sha256']}
stmt='For the exact w4,m0,d0,eta0 fixture of A094-CANONICAL-RETURN-POSITIVE-DEBIT-EXACT@1, all THREE positive signed reset bookings are paid from the SAME original rate4 root bank, with every old query release and full sibling terminal retained. The conservative remaining bank is strictly greater than2 bits; the inherited all-parameter estimates alone give strictly greater than3/1024 bits. No negative reset charge is reclaimed. This is a single physical Boolean fixture, not a uniform third-reset or universal FEI theorem.'
hyp=['Exactly the A094 fixture: queries original narrow4,narrow5,wide0; reset only each zero child','All references canonical at eta0; actual normalized physical-child inheritance from the current model','Original quota4Iroot, no renewal; all old charges retained; information bits']
paid=node('A081-THREE-RESET-FIXTURE-SAME-ORIGINAL-BANK',stmt,hyp,[n['claim_id']+'@1','A095-TWO-NARROW-RESETS-SAME-RATE4-BANK@1','A081-STRUCTURAL-ORIGINAL-ROOT-RESERVE@1'])
g['nodes'] += [n,paid]
contract={'fixture':{'w':4,'m':0,'d':0,'eta':0,'queries':[4,5,0]},'quota':'4I_original','bookings':['max(e1,0)','max(e2,0)','max(e3,0)'],'references':'inherited from CURRENT reset model','complete_siblings':'ALL','old_query_releases':'ALL','reserve_strictly_greater_than':'2','units':'bits'}
g['stage9_ledger_contract']=contract;g['stage9_scope']='Exact third-reset fixture paid; general wide-reset leaf remains OPEN'
for i,p in enumerate(pins):g['sources']['stage9_'+str(i)]={'local_path':str(R/p['snapshot']),'local_sha256':p['sha256'],'original_local_path':p['source']}
def key(n):return n['claim_id']+'@'+str(n['version'])
def dep(d):
 if isinstance(d,str):return d
 for k in ['claim_key','claim','key']:
  if k in d:return d[k]
 return d['claim_id']+'@'+str(d['version'])
def valid(z):
 nodes={key(a):a for a in z['nodes']};assert len(nodes)==len(z['nodes']);active=set();seen=set()
 def walk(k):
  assert k in nodes and k not in active
  if k in seen:return
  active.add(k)
  for d in nodes[k]['proof_dependencies']:walk(dep(d))
  active.remove(k);seen.add(k)
 for k in nodes:walk(k)
 for k in ['FEI-FINAL@1','A081-OPEN-WIDE-RESET-AFTER-TWO-NARROW@1','A081-OPEN-PRESCRIBED-WEAK-RESET@1']:assert nodes[k]['status']=='OPEN'
 assert z['stage9_ledger_contract']==contract
 for a in z['nodes'][-2:]:assert a['statement_sha256']==digest(a['exact_statement']) and a['units']==units
 assert z['nodes'][-1]['hypotheses']==hyp and z['nodes'][-1]['proof_dependencies']==paid['proof_dependencies']
 assert sha(z['nodes'][-2]['source_claims_pin']['path'])==z['nodes'][-2]['source_claims_pin']['sha256']
 return len(seen)
guards=[]
def reject(label,fn):
 z=copy.deepcopy(g);fn(z)
 try:valid(z)
 except (AssertionError,KeyError):guards.append(label);return
 raise AssertionError('accepted bad mutation '+label)
reject('FEI self-cycle',lambda z:z['nodes'][0]['proof_dependencies'].append('FEI-FINAL@1'))
reject('cycle through FEI and paid fixture',lambda z:(z['nodes'][0]['proof_dependencies'].append(key(paid)),z['nodes'][-1]['proof_dependencies'].append('FEI-FINAL@1')))
reject('wrong version',lambda z:z['nodes'][-1]['proof_dependencies'].__setitem__(0,key(n)[:-1]+'2'))
reject('changed statement',lambda z:z['nodes'][-1].__setitem__('exact_statement','Full FEI'))
reject('nats',lambda z:z['nodes'][-1].__setitem__('units',{'entropy':'nats'}))
reject('changed source hash',lambda z:z['nodes'][-2]['source_claims_pin'].__setitem__('sha256','0'*64))
reject('universal promotion',lambda z:z['nodes'][0].__setitem__('status','PROVED'))
reject('drop old booking',lambda z:z['stage9_ledger_contract']['bookings'].pop(0))
reject('renew quota',lambda z:z['stage9_ledger_contract'].__setitem__('quota','4I_child'))
reject('drop sibling',lambda z:z['stage9_ledger_contract'].__setitem__('complete_siblings','NONE'))
reject('stale inherited model',lambda z:z['stage9_ledger_contract'].__setitem__('references','root'))
reject('universalize hypothesis',lambda z:z['nodes'][-1].__setitem__('hypotheses',['arbitrary source']))
save(R/'PROOF_DEPENDENCIES.json',g);save(R/'out/GRAPH_VALIDATION.json',{'status':'PASS','nodes':valid(g),'prior_nodes':prior_count,'new_nodes':2,'rejected_mutations':guards,'FEI':'OPEN','general_third_reset':'OPEN'})
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
c['review_records'].append({'reviewer':'A081/fleet03','at':now,'verdict':'HOLDS_AT_FULL_STATED_FIXTURE_SCOPE_NO_REPAIR','proof_source':str(R/'REVIEW.md'),'validation_source':str(R/'out/EXACT_CERTIFICATE.json'),'independence':'Own physical Boolean construction and direct character sums; author checker not imported'})
c['status']='INDEPENDENTLY_EXACT_CERTIFIED_BY_A081'
newclaim={k:copy.deepcopy(paid[k]) for k in ['claim_id','version','exact_statement','hypotheses','statement_sha256','proof_dependencies','status','first_unproved_line']}
newclaim.update(contributors=['A081/fleet03'],proof_source={'path':str(R/'REVIEW.md'),'certificate':str(R/'out/EXACT_CERTIFICATE.json')},review_records=[],supersedes=[],refutes=[],next_consumers=['A094','A095','A086','A099','B17'])
save(R/'CLAIMS.json',[c,newclaim])
next_action='Prove a uniform bound for the actual inherited remaining-wide reset after both narrow bookings, preserving CURRENT reference, original unused source surplus, old releases and both full terminals; A094/A086 review. Do not replace the source surplus by a rare-edit-only allowance.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B17','packet_id':'A081','gap_id':'G-R-MISMATCH','attempt_id':'A081-stage9-positive-third-reset-same-bank','method':'Direct-character rational fixture reconstruction, exact integer sign bounds, complete symbolic ledger and versioned DAG mutation checks','mathematical_delta':'A094 positive third-reset obstruction independently HOLDS. New exact SAME-bank three-reset fixture reserve>2 bits; coarse inherited estimate>3/1024. General third-reset and FEI remain OPEN.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'EXACT_SCOPED_THIRD_RESET_PAYMENT_FULL_FEI_OPEN','claim_versions_used':['A094-CANONICAL-RETURN-POSITIVE-DEBIT-EXACT@1','A095-TWO-NARROW-RESETS-SAME-RATE4-BANK@1','A081-STRUCTURAL-ORIGINAL-ROOT-RESERVE@1'],'claims_created_or_changed':[key(n),key(paid)],'source_artifacts':['REVIEW.md','out/SOURCE_PINS.json','out/FROZEN_SPEC.json','out/EXACT_CERTIFICATE.json','PROOF_DEPENDENCIES.json','out/GRAPH_VALIDATION.json'],'next_consumers':['A094','A095','A086','A099','B17','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Uniform third-reset payment and arbitrary-core source/reference supply remain unproved','Full proof not Lean kernel checked','Supervisor copying and canonical adoption unverified'],'packet_ids':['A081']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

A081/B17 stage9 independently audits A094-CANONICAL-RETURN-POSITIVE-DEBIT-EXACT@1 and pays that exact third-reset fixture from its SAME original rate4 bank. Domain is w4,m0,d0,eta0, queries narrow4,narrow5,wide0 with canonical zero-child resets. Entropy/CE/KL use bits; physical total influence is91/64. No arbitrary-width or universal claim follows.

# sources actually read, revisions and theorem locators

Current BOARD (2026-10-23 05:35 UTC), B17 STREAM_NOTES v2, own stage8 STATUS and proof graph; A094 20261023T035625 RECONSTRUCTION section5 and exact claim; A095 20261023T044042 DERIVATION sections1–5 as contextual obstruction. Immutable source bytes and hashes are in out/SOURCE_PINS.json. Prior accepted sources retain their previous evidence states; this is not a rereview of every historic theorem. Machine-wide rules and execution protocol were read. Personal-model/state-of-mind brain notes are stale, degraded and not authority. No shared registry, brain, other agent, git or external system was written.

# complete derivation or exact first unsupported line

REVIEW.md gives the reconstructed reference classes, exact integer certificate1/128<e3<9/1024 and complete identity G3+T3=CEroot+e1+e2+e3. All old releases and complete sibling terminals stay retained. Independent conservative positive-booking calculation leaves>2 bits, while the previous uniform bounds already give>3/1024. The first unsupported line is uniform payment of this specified reset for arbitrary width/padding/prefix/eta, and ultimately influence-priced arbitrary-core reference supply.

# executed validation with domain, arithmetic, commands and outputs

Frozen single labelled case in out/FROZEN_SPEC.json,128 physical root points, exact Fraction character sums, normalized complete references, bounded rational logarithm intervals and integer power comparisons. Command: python -X utf8 {R/'code/check.py'}. Result PASS: {res['assertions']} new direct assertions (prior expression assertions separately excluded), runtime{res['seconds']:.4f}s; pilot and full scope are the same one fixture. No unbounded search, floating proof, GPU or heavy job was used; estimated memory80MB below the300MB memok gate. No Lean proof is claimed.

# proof dependencies and changed downstream conclusions

PROOF_DEPENDENCIES.json preserves81 prior nodes and adds2, yielding83. Twelve declared invalid graph/ledger mutations are rejected, including a cycle through FEI, source/version/units tampering, renewal and discarded sibling/booking. FEI-FINAL and both general reset leaves remain OPEN. The narrow structural affordability result now includes one actual positive-cost third reset; free canonical returns remain invalid.

# one next mathematical action and independent reviewer

{next_action}

# actual persistence receipts or precise save blocker

Four protocol files, checker, review, source snapshots, graph and exact output saved locally. out/PERSISTENCE_RECEIPTS.json and FINAL_READBACK.json enumerate verified local bytes and schema checks. Supervisor copying, remote publication and canonical adoption are unverified and outside this run's write authorization.

# Universal bridge

This stage moves C024 history transfer and C020 whole-set witness cost by certifying one genuine positive third reset paid from the SAME original ancestor bank after both previous reset bookings, retaining complete releases and terminals, with>2 bits remaining. Universal FEI constant improvement is zero. Uniform third-reset pricing and arbitrary-core reference supply remain open. NEXT targets actual inherited conversion cost against the actual unused source surplus, the shortest remaining connection to a hereditary universal payment theorem rather than another isolated function class.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(H/'STATUS.md').write_text('STATE: A081 stage9 complete: A094 positive third reset independently HOLDS; exact three-reset fixture SAME original rate4 reserve>2 bits;83-node DAG/12 guards PASS; FEI OPEN.\nNEXT: '+next_action+'\n',encoding='utf-8')
for name,txt in [('WORKLOG.md',f'{now}: Stage9 direct-character fixture reconstructed positive third debit and complete three-reset ledger; {res["assertions"]} exact assertions,83-node DAG/12 rejection guards. SAME original reserve>2 bits. General third reset and FEI OPEN; remote adoption unverified.'),('LEARNED.md','Stage9 durable: after eta0 narrow4,narrow5 resets of h4*h2 point-selector (w4,m0,d0), wide0 zero-child canonical return has normalizer529/452 and e3=log2(12250^49*3390^7*452^8/(11109^49*3703^7*529^8))/512 in(1/128,9/1024). Positive does not mean unaffordable: SAME original bank minus all three positive bookings>2 bits exactly. Global prior bounds alone leave>3/1024. This fixture does not discharge the uniform third-reset leaf; rare-edit-only allowance is a distinct account.')]:
 with (H/name).open('a',encoding='utf-8') as f:f.write('\n'+txt+'\n')
claimfields={'claim_id','version','exact_statement','hypotheses','statement_sha256','contributors','proof_source','proof_dependencies','review_records','status','supersedes','refutes','first_unproved_line','next_consumers'}
progressfields={'protocol_revision','run_id','stream','packet_id','gap_id','attempt_id','method','mathematical_delta','deliverable_status','mathematical_status','claim_versions_used','claims_created_or_changed','source_artifacts','next_consumers','next_action','stagnant_substantive_attempts','blockers','packet_ids'}
assert all(set(a)==claimfields for a in load(R/'CLAIMS.json'));assert set(progress)==progressfields
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes();assert len((H/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
save(R/'out/SCHEMA_VALIDATION.json',{'status':'PASS','claim_fields_exact':True,'progress_fields_exact':True,'delta_identical':True,'rolling_status_two_lines':True})
files=[p for p in R.rglob('*') if p.is_file() and p.name not in ['PERSISTENCE_RECEIPTS.json','FINAL_READBACK.json']]
assert all(p.stat().st_size<20*1024*1024 for p in files)
receipts=[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files]
save(R/'out/PERSISTENCE_RECEIPTS.json',{'status':'VERIFIED_LOCAL','remote':'UNVERIFIED','files':receipts})
for a in receipts:assert sha(R/a['path'])==a['sha256']
save(R/'out/FINAL_READBACK.json',{'status':'PASS','files_rehashed':len(receipts),'nodes':valid(load(R/'PROOF_DEPENDENCIES.json')),'report_readback':(R/'REPORT.md').read_text(encoding='utf-8')==report,'FEI':'OPEN','formal_kernel_proof':False,'remote':'UNVERIFIED'})
print(json.dumps({'status':'PASS','assertions':res['assertions'],'nodes':len(g['nodes']),'guards':len(guards),'local_files_verified':len(receipts),'FEI':'OPEN'}))
