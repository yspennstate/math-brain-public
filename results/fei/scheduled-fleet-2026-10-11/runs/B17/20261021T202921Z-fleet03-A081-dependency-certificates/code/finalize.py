from pathlib import Path
from fractions import Fraction as F
import hashlib,json,copy,datetime,importlib.util

R=Path(__file__).resolve().parents[1];HOME=R.parents[1]
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def save(p,x):Path(p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def sth(s):return hashlib.sha256(s.encode('utf-8')).hexdigest()
pins=read(R/'out/SOURCE_PINS.json');results=read(R/'out/EXACT_CHECK.json')
assert results['status']=='PASS' and results['seconds']<55
source=next(p for p in pins if p['source'].endswith('A095-restricted-result-extraction\\CLAIMS.json'))
claims_source=read(R/source['snapshot']);target=copy.deepcopy(claims_source[0])
old=read(HOME/'runs/20261014T092812Z-fleet05-A081-dependency-certificates/PROOF_DEPENDENCIES.json')
g=copy.deepcopy(old);g['run_id']=R.name
g['prior_certificate']={'path':str(HOME/'runs/20261014T092812Z-fleet05-A081-dependency-certificates/PROOF_DEPENDENCIES.json'),'sha256':sha(HOME/'runs/20261014T092812Z-fleet05-A081-dependency-certificates/PROOF_DEPENDENCIES.json'),'scope':'Imported prior accepted graph unchanged; not a fresh proof review of all its sources.'}
units={'entropy':'bits','influence':'uniform physical total influence','log':'base 2, except explicit ln'}
def node(key,statement,hypotheses,status='INDEPENDENTLY_RECONSTRUCTED_BY_A081',deps=(),locator='REVIEW.md'):
    cid,v=key.rsplit('@',1)
    return {'claim_id':cid,'version':int(v),'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':sth(statement),'statement_hash_convention':'UTF8 exact_statement only','units':units,'status':status,'proof_sources':[{'path':str(R/locator),'sha256':sha(R/locator)}],'proof_dependencies':list(deps),'evidence':[{'path':str(R/'out/EXACT_CHECK.json'),'sha256':sha(R/'out/EXACT_CHECK.json')}],'first_unproved_line':None}
transport=node('A081-COMPLETE-NORMALIZED-PHYSICAL-TRANSPORT@1','For finite actual Boolean physical children P0,P1 and complete normalized Q positive on actual parent support, marginalize Q to r and set raw Qb=2r*pi_b, pi_b=Pb/(P0+P1) on positive fibers, pi_b=1/2 on zero true fibers. Z0,Z1>0, Z0+Z1=2; CE_parent-mean CE_child=Delta+L-mean log2 Zb>=0. Every finite adaptive tree retains complete mean terminal CE. Product-compatible zero-fiber kernels preserve any untouched independent prescribed terminal additively.', ['Finite uniform cube; actual phase-aware child laws','Full reference mass retained; base-two CE','No reference reset or bank renewal; product-compatible zero-fiber rule for terminal tensor'])
profile=node('A081-A095-SIGNED-PROFILE-ROOT-AUDIT@1','For all integers w>=4,m>=0, the prescribed support-completed R=P_(h_w*h_2) reference of the all-zero fair-selector point edit has full root CE<1005/256.', ['Exactly h_w*h_2 on disjoint blocks, m dummies, fair fresh selector','All-zero full-point edit; complete support-completed reference, not arbitrary Q'])
edge=node('A081-A095-ADAPTIVE-EDGE-AUDIT@1','For all integers w>=4,m>=0 and every finite adaptive tree querying only width-w coordinates without repetition, the actual fair-selector point edit of padded h_w*h_2 satisfies E I_leaf>=1-2^(-w-m-2)>=63/64.', ['Width-two block, selector, padding and independent terminal stay unqueried','Unique all-zero edited path with its original physical reaches','All executed destroyed edges remain debited'])
newtarget=node(target['claim_id']+'@'+str(target['version']),target['exact_statement'],target['hypotheses'],deps=[transport['claim_id']+'@1',profile['claim_id']+'@1',edge['claim_id']+'@1'])
newtarget['source_statement_sha256']=target['statement_sha256'];newtarget['source_declared_dependencies']=target['proof_dependencies']
newtarget['source_claims_pin']={'path':str(R/source['snapshot']),'sha256':source['sha256']}
openleaf=node('A081-OPEN-PRESCRIBED-WEAK-RESET@1','Pay a specified useful weak non-flat descendant reference reset, its channel cost, complementary complete terminal and old executed debit from the SAME unused original ancestor account at an absolute rate for arbitrary cores.', ['Arbitrary incoming prescribed reference; actual physical child normalizers','No renewed bank; both complete terminal laws retained'],status='OPEN')
openleaf['first_unproved_line']=openleaf['exact_statement'];openleaf['proof_sources']=[];openleaf['evidence']=[]
g['nodes'] += [transport,profile,edge,newtarget,openleaf]
for i,p in enumerate(pins):
    g['sources']['stage7_'+str(i)]={'local_path':str(R/p['snapshot']),'local_sha256':p['sha256'],'original_local_path':p['source'],'pin_scope':'Exact immutable local source bytes; no remote adoption asserted'}
g['scope_relations'].append({'from':newtarget['claim_id']+'@1','to':'FEI-FINAL@1','kind':'NO_UNIVERSAL_IMPLICATION','reason':'Prescribed structural source; no arbitrary incoming positive profile or descendant reset payment. Untouched independent terminal stays outside core bank.'})
g['stage7_unresolved_leaf']='A081-OPEN-PRESCRIBED-WEAK-RESET@1'
save(R/'PROOF_DEPENDENCIES.json',g)

def key(n):return n['claim_id']+'@'+str(n['version'])
def depkey(d):
    if isinstance(d,str):return d
    for k in ['claim_key','claim','key']:
        if k in d:return d[k]
    return d['claim_id']+'@'+str(d['version'])
def acyclic(graph):
    nodes={key(n):n for n in graph['nodes']};seen=set();active=set()
    def walk(k):
        assert k in nodes,('missing exact dependency',k)
        assert k not in active,('proof cycle',k)
        if k in seen:return
        active.add(k)
        for d in nodes[k]['proof_dependencies']:walk(depkey(d))
        active.remove(k);seen.add(k)
    for k in nodes:walk(k)
    return len(seen)
def new_valid(graph):
    acyclic(graph);nodes={key(n):n for n in graph['nodes']}
    for n in graph['nodes'][-5:]:
        assert sth(n['exact_statement'])==n['statement_sha256']
        assert n['units']['entropy']=='bits'
    nt=nodes[newtarget['claim_id']+'@1'];assert nt['source_claims_pin']['sha256']==sha(nt['source_claims_pin']['path'])
    assert nodes['FEI-FINAL@1']['status']=='OPEN'
    assert nodes['A081-OPEN-PRESCRIBED-WEAK-RESET@1']['status']=='OPEN'
    assert len(nt['proof_dependencies'])==3
    for d in nt['proof_dependencies']:assert nodes[depkey(d)]['status']=='INDEPENDENTLY_RECONSTRUCTED_BY_A081'
    assert nt['hypotheses']==target['hypotheses']
new_valid(g)
guards=[]
def reject(name,mutate):
    z=copy.deepcopy(g);mutate(z)
    try:new_valid(z)
    except (AssertionError,KeyError):guards.append({'name':name,'verdict':'REJECTED'});return
    raise AssertionError('Guard accepted '+name)
reject('direct FEI cycle',lambda z:z['nodes'][0]['proof_dependencies'].append('FEI-FINAL@1'))
reject('two-node cycle through FEI',lambda z:(z['nodes'][0]['proof_dependencies'].append(newtarget['claim_id']+'@1'),z['nodes'][-2]['proof_dependencies'].append('FEI-FINAL@1')))
reject('wrong exact dependency version',lambda z:z['nodes'][-2]['proof_dependencies'].__setitem__(0,transport['claim_id']+'@2'))
reject('changed statement without hash',lambda z:z['nodes'][-2].__setitem__('exact_statement','universal FEI'))
reject('unit substitution nats',lambda z:z['nodes'][-2].__setitem__('units',{'entropy':'nats'}))
reject('wrong source bytes',lambda z:z['nodes'][-2]['source_claims_pin'].__setitem__('sha256','0'*64))
reject('mark FEI closed by status',lambda z:z['nodes'][0].__setitem__('status','PROVED'))
reject('promote unpaid reset',lambda z:z['nodes'][-1].__setitem__('status','PROVED'))
reject('drop terminal transport dependency',lambda z:z['nodes'][-2]['proof_dependencies'].pop())
reject('substitute arbitrary reference',lambda z:z['nodes'][-2].__setitem__('hypotheses',['arbitrary incoming Q']))
reject('renew bank',lambda z:z['nodes'][-2]['hypotheses'].append('renew child bank'))
reject('query protected width-two factor',lambda z:z['nodes'][-2]['hypotheses'].append('allow width-two query'))

# Counterexample to extending the physical influence floor to all data queries.
spec=importlib.util.spec_from_file_location('independent',R/'code/check.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
w=4;m=0;gg,ff,qq,pp=mod.root(w,m);mean=F(0)
for x in range(1<<(w+2)):
    terminal=[ff[x],ff[x+(1<<(w+2))]];mean+=mod.influence(terminal)/F(1<<(w+2))
assert mean==F(1,64) and mean<F(63,64)
save(R/'out/SCOPE_BOUNDARY.json',{'status':'PASS','actual_boolean_family':'w=4,m=0 same root','forbidden_policy':'query all six DATA coordinates, retain selector','mean_remaining_influence':str(mean),'refutes_only':'63/64 floor after querying protected width-two factor','does_not_refute':'A095 scoped theorem or FEI'})
save(R/'out/GRAPH_VALIDATION.json',{'status':'PASS','nodes':acyclic(g),'prior_nodes':len(old['nodes']),'new_nodes':5,'new_source_pins':len(pins),'guards':guards,'proof_cycle_through_FEI':'REJECTED','full_fei_status':'OPEN','old_source_scope':'prior graph preserved; local new pins rehashed, not all old theorems re-reviewed'})

# Preserve exact source statement/hypotheses and declare hash convention separately in graph.
target['proof_dependencies']=[{'claim_id':x['claim_id'],'version':1,'statement_sha256':x['statement_sha256'],'scope':'exact reviewed lemma; REVIEW.md','units':'bits'} for x in [transport,profile,edge]]
target['review_records'].append({'reviewer':'A081/fleet03','at':NOW,'verdict':'ACCEPT_AT_ENTIRE_ORIGINAL_SCOPE_NO_REPAIR','proof_source':str(R/'REVIEW.md'),'validation_source':str(R/'out/EXACT_CHECK.json'),'independence':'Independent integer Walsh/direct characters/physical edges/Fraction posterior and rational-log implementation; no author checker imported','reviewer_contributed_repair':False,'rung':'analytic proof with exact finite validation; no Lean certification of full theorem'})
target['status']='INDEPENDENTLY_ACCEPTED_AT_ENTIRE_ORIGINAL_SCOPE_BY_A081'
target['first_unproved_line']=None
statement=f'A081 stage7 graph contains {len(g["nodes"])} exact versioned nodes and preserves the prior {len(old["nodes"])} nodes, adds the complete prescribed A095 unbounded-width history proof chain and one unresolved reset leaf, has no proof cycle, and rejects all twelve declared invalid mutations. FEI remains OPEN.'
cert={'claim_id':'A081-VERSIONED-DEPENDENCY-CERTIFICATE','version':7,'exact_statement':statement,'hypotheses':['Finite frozen source snapshot; inherited evidence states preserved','Proof graph separate from advisory review/workflow edges; units and exact source versions retained'],'statement_sha256':sth(statement),'contributors':['A081/fleet03'],'proof_source':{'graph':str(R/'PROOF_DEPENDENCIES.json'),'validator':str(R/'code/finalize.py'),'output':str(R/'out/GRAPH_VALIDATION.json')},'proof_dependencies':[{'claim_id':target['claim_id'],'version':1,'statement_sha256':target['statement_sha256'],'scope':'prescribed structural reference and wide-only histories; no reset'}],'review_records':[],'status':'CHECKED_LOCAL_DEPENDENCY_CERTIFICATE','supersedes':['A081-VERSIONED-DEPENDENCY-CERTIFICATE@6 as current graph snapshot; prior artifact preserved'],'refutes':[],'first_unproved_line':'Universal prescribed-reference reset plus both terminal bills and old debit is unpaid.','next_consumers':['A094','A095','A096','A097','A099','B17','B20']}
save(R/'CLAIMS.json',[target,cert])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B17','packet_id':'A081','gap_id':'G-R-MISMATCH','attempt_id':'A081-stage7-source-profile-history-review','method':'Independent analytic reconstruction, exact physical/reference replay, versioned dependency graph and adversarial guard mutations','mathematical_delta':'A095 unbounded-width signed-profile history@1 independently accepted at entire original scope; all w>=4,m>=0, every adaptive wide-only history, same rate4 and surplus>3/256; no universal constant improvement.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_DEPENDENCY_ACCEPTED_FULL_FEI_OPEN','claim_versions_used':[target['claim_id']+'@1','A081-VERSIONED-DEPENDENCY-CERTIFICATE@6'],'claims_created_or_changed':[target['claim_id']+'@1','A081-VERSIONED-DEPENDENCY-CERTIFICATE@7'],'source_artifacts':['out/SOURCE_PINS.json','out/CONTEXT_INTAKE.json','REVIEW.md','out/EXACT_CHECK.json','PROOF_DEPENDENCIES.json'],'next_consumers':['A094','A095','A096','A097','A099','B17','B20'],'next_action':'Expose one protected h2 coordinate with SAME inherited Q and old debit; name and price a prescribed useful child reset plus complementary full terminal from genuinely unused original surplus; A094/A086 independently challenge scope.','stagnant_substantive_attempts':0,'blockers':['No universal incoming-reference/source price or fresh-reset payment','Supervisor adoption, copying and mirror verification unverified'],'packet_ids':['A081']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
lean=read(R/'out/LEAN_RECEIPT.json') if (R/'out/LEAN_RECEIPT.json').exists() else {'status':'NOT_AVAILABLE'}
report=f'''# exact target, quantifiers, hypotheses and units

A081/B17 stage7 independently audits A095-UNBOUNDED-WIDTH-SIGNED-PROFILE-HISTORY@1. For all integers w>=4,m>=0, preserve the prescribed support-completed source-spectrum reference on the fresh fair-selector all-zero point edit of padded h_w*h2, through every finite adaptive tree querying only width-w coordinates. Exact source statement/hypotheses remain in CLAIMS.json. Entropy, cross entropy and divergence are bits; influence is actual uniform physical pivotal influence. Full FEI remains OPEN. The current user deadline 23 October 14:49 UTC supersedes the older protocol endpoint.

# sources actually read, revisions and theorem locators

Execution protocol v2 was read in full; campaign indices, plan, supplement/source notes and four paper exports were consulted as context. Current BOARD snapshot 21 October20:32 UTC, B17 STREAM_NOTES v2 and own stage6 direct this continuation. Critical sources are A095 run20261021T180853Z DERIVATION1–4 and CLAIMS; A094 run20261021T155244Z AUDIT3–5, PROFILE_CERTIFICATE and CLAIMS; own stage6 graph. out/SOURCE_PINS.json freezes {len(pins)} source files; out/CONTEXT_INTAKE.json records background byte hashes, encoding and locators. Local paper/source intake is not a new blanket theorem acceptance. A001's new all-history actual-reference result is navigation, not an accepted premise here.

# complete derivation or exact first unsupported line

REVIEW.md independently reconstructs the four signed coefficient classes, the complete normalized reference root price, its all-w/all-m bound CE_root<1005/256, the unique edited-path physical debit, mean I_leaf>=63/64, and full normalized reference CE nonincrease through arbitrary finite adaptive histories. Hence 4 E I_leaf-E CE_leaf>3/256. Every child normalizer and zero true/reference-only fiber stays in the model. Untouched independent prescribed terminals stay fully additive outside the core bank. Verdict: HOLDS at the entire original scope, without repair. Rung: analytic proof with exact finite validation; the full theorem is not Lean-checked. Lean padding-only attempt: {lean['status']}.

The first unsupported universal line is a useful specified fresh descendant reference reset plus complementary full terminal, signed conversion and old executed debit paid from ONE unused ancestor account for arbitrary cores at an absolute rate. The signed profile here is tied to R=P_(h_w*h2); replacing it with an arbitrary supplied reference is invalid. No reset theorem or universal FEI improvement is claimed.

# executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json precedes replay. Commands: python -X utf8 code/check.py --pilot; python -X utf8 code/check.py; python -X utf8 code/finalize.py, from this run. The independent helper imports no author checker. Full domain w=4,5 and m=0,1,2: six actual roots, {sum(x['states'] for x in results['cases'])} distinct labeled wide-only restrictions and 24 named complete tree policies, including reverse/outcome-dependent queries and branch stopping. Integer Walsh transforms, separate direct character sums, direct physical edge counts, Fraction posterior/reference masses and exact child normalizers pass {results['assertions']} assertions in {results['seconds']:.3f} internal seconds. Logs use 24 range-reduced atanh terms with rigorous tail 2z^49/[49(1-z^2)] and outward rounding to2^-80. All-parameter scope follows from the written induction, not this finite domain.

The first pilot failed on exact zero release because outward intervals overlap; exact symbolic cancellation of identical rational-log terms resolves equality without a tolerance. A full attempt then encountered Python's integer-to-string size limit from accumulated interval denominators; outward dyadic log rounding controls size without changing a sign. Final authoritative replay passes. Pilot4435 assertions are a subset, not added to the full count. out/SCOPE_BOUNDARY.json separately realizes a forbidden all-data query with mean remaining influence1/64, refuting only the extended63/64 floor. Graph validation passes with {len(g['nodes'])} nodes and12 rejection guards, including direct and indirect cycles through FEI. No numerical FEI counterfamily is inferred.

Estimated helper memory120MB; peak unmeasured. Fresh memok exits0 before the direct windowless Lean attempt; receipt is saved. No heavy search, automatic dimension increase, GPU, detached job or visible window is used. Compute state read OK with zero recent interventions; no process was stopped to free resources.

# proof dependencies and changed downstream conclusions

The previous {len(old['nodes'])}-node graph is preserved and extended by three explicit reviewed technical statements, the original A095 theorem and an open reset leaf. Prior mathematical acceptance states are inherited, not recertified. A094's review of generic transport is evidence rather than a backwards proof dependency on its later profile, so mutual review does not create a mathematical cycle. Exact statement versions, source bytes, scope and bits are explicit. A095's whole stated theorem receives independent acceptance by A081; unrelated rank, collision, arbitrary-core and reset clauses receive none. Full FEI and universal reference availability remain OPEN.

# one next mathematical action and independent reviewer

Expose one untouched h2 coordinate in this SAME account, specify the desired actual descendant reset, and price its signed cost plus the complementary full terminal from the genuinely unused original surplus after old debits. A094/A086 should independently challenge the dependency and scope records; A095/A096/A097 are consumers. This handoff is saved locally; no message or external adoption is presumed. Another no-reset wide-depth sweep is unnecessary.

# actual persistence receipts or precise save blocker

The four protocol files, REVIEW, graph, frozen spec, independent checker, source snapshots, exact results, boundary witness, Lean receipt and schema/persistence receipts are saved in the assigned run. Rolling STATUS has two lines and dated WORKLOG/LEARNED updates. out/PERSISTENCE_RECEIPTS.json hashes local files. Supervisor copying, canonical adoption, remote mirrors and external review of this audit are unverified. The wake warning about stale personal-context notes was surfaced and those notes were not premises. User's own-folder-only rule excludes shared checklist/mesh/brain mutations; no git, messaging, brain write, trading access or other-agent mutation occurred.

# Universal bridge

This stage moves C024 history transfer and C019 stopping payment by independently accepting the prescribed unequal-amplitude unbounded-width all-history rate4 theorem and placing its full reference/physical cost chain into a cycle-checked dependency certificate. The uniform scoped surplus is>3/256, and the universal constant improvement is zero. Arbitrary incoming signed profiles, universally paid source references and specified fresh resets with complete complementary terminals remain unpaid. NEXT tests the protected h2 exposure/reset on the SAME original bank because that is the precise missing hereditary payment; more already-paid wide-only histories would add no route to full FEI.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(R/'REVIEW.md').write_text((R/'REVIEW.md').read_text(encoding='utf-8').replace('Verdict pending the executed replay: the analytic chain holds at its exact stated scope.','Verdict: HOLDS at the entire original stated scope; the independent exact replay passes.'),encoding='utf-8')
# Refresh proof pins after replacing the provisional verdict sentence.
for n in g['nodes'][-5:]:
    for p in n['proof_sources']:
        if p['path']==str(R/'REVIEW.md'):p['sha256']=sha(R/'REVIEW.md')
save(R/'PROOF_DEPENDENCIES.json',g)
(HOME/'STATUS.md').write_text(f'STATE: A081 stage7 complete: A095 all-width/all-padding adaptive wide-block history independently HOLDS at SAME rate4; {results["assertions"]} exact assertions and12 graph guards PASS; full FEI OPEN.\nNEXT: Price one prescribed h2 descendant reset plus complementary full terminal and old debit from SAME unused ancestor bank; A094/A086 scope review; no renewed bank.\n',encoding='utf-8')
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{NOW} A081 stage7: independently reconstructed A095 wide-only theorem all w>=4,m>=0, unchanged rate4 surplus>3/256; {results["assertions"]} exact assertions on972 labeled restrictions/24 histories;12 adversarial graph guards. Equality interval issue fixed by exact cancellation; denominator serialization issue fixed by outward dyadic rounding. Scoped acceptance only; reset/universal FEI unpaid. Lean receipt {lean["status"]}.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage7: A095 h_w*h2 signed profile gives complete prescribed-source root CE<1005/256 for every w>=4,m>=0; any wide-only adaptive tree retains mean physical influence>=63/64, so SAME-rate4 surplus>3/256 without reset. Negative signed linear term is essential to this price proof; it is not an arbitrary-Q theorem. Posterior zero true fibers keep reference mass; product terminal factorization needs product-compatible kernels. Querying protected h2 invalidates the influence floor (w4,m0 all-data exposure leaves mean1/64). Mutual review is evidence, not a backwards proof edge. Exact-zero information differences need algebraic cancellation, not tolerance; log intervals should be outward dyadically rounded before summation to prevent denominator/serialization blowup.\n')
protocol=read(next(R/p['snapshot'] for p in pins if p['source'].endswith('EXECUTION_PROTOCOL.json')))
cf=set(protocol['required_per_run']['claim_fields']);pf={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert all(set(c)==cf for c in read(R/'CLAIMS.json'));assert set(progress)==pf
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert all(h in report for h in protocol['required_per_run']['report_fields'])
assert len((HOME/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert all(sha(R/p['snapshot'])==p['sha256'] for p in pins)
save(R/'out/SCHEMA_VALIDATION.json',{'status':'PASS','claim_field_count':len(cf),'progress_field_count':len(pf),'progress_delta_identical':True,'new_source_pins_valid':True,'statement_hash_conventions':'Original source digest preserved; graph exact_statement UTF8 digest explicit','status_two_lines':True})
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in str(p) and p.name!='PERSISTENCE_RECEIPTS.json']
assert all(p.stat().st_size<20_000_000 for p in files)
save(R/'out/PERSISTENCE_RECEIPTS.json',{'at':NOW,'scope':'local only; no supervisor/remote adoption asserted','files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]})
print(json.dumps({'status':'PASS','nodes':len(g['nodes']),'guards':len(guards),'assertions':results['assertions'],'files':len(files),'full_fei':'OPEN','lean':lean['status']}))
