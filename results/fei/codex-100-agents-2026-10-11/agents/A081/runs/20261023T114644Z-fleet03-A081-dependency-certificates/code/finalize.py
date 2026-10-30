from pathlib import Path
import json,hashlib,copy,datetime
R=Path(__file__).resolve().parents[1];H=R.parents[1]
def load(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def save(p,o):Path(p).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def digest(s):return hashlib.sha256(s.encode()).hexdigest()
pins=load(R/'out/SOURCE_PINS.json');result=load(R/'out/EXACT_CERTIFICATE.json')
assert result['status']=='PASS' and result['source_query_cases']==120 and result['seconds']<55
for p in pins:assert sha(R/p['snapshot'])==p['sha256']
review='''# Statement-level dependency audit

All entropy, cross entropy (CE) and divergence are bits; influence is the ordinary uniform physical total influence. A source reference R is a subprobability of mass s in(0,1], positive on the true spectrum. Complete divergence includes the penalty -log2 s. No source or child reference is silently normalized.

## The exact conditional frontier interface

For the A011 v2 padding-then-source policy, A094 section5 records these lower bounds on the SAME original quota K I(F)-L, K=4C0+15: root/final >=(3C0/2+45/4)Ig+4C0G; padding >=(2C0+11/2)Ig+KG; intermediate source >=(C0+45/8)Ig+KG. C0,G>=0. L is a SIGNED full ledger, not a sum of positive charges alone. Source cost c<=C0 Ig is supplied. Every off-path terminal and reference mass is retained.

Subtracting (C0+11/2)Ig leaves coefficients (C0/2+23/4), C0, and1/8, respectively, all nonnegative. Hence the admitted old U<=(C0+37/8)Ig leaves at least7Ig/8. A086's U<=(C0+1)Ig is smaller by29Ig/8, with the SAME residual7Ig/8. This algebra is independently certified. The physical derivation and source inheritance were read in A011 v2 and A094; external reviews are pinned as external reviews, not silently upgraded to a new full physical review by A081.

There is also a sharp consequence of these THREE INTERFACE LOWER BOUNDS alone. The root bound dominates the intermediate bound, and min(padding,source)=[C0+11/2+min(C0,1/8)]Ig after dropping nonnegative G. Thus U<=[C0+37/8+min(C0,1/8)]Ig suffices for reserve7Ig/8. Equality of this scalar minimum is an algebraic fact. It is not an upper bound on the actual bank and does not repair incompatible histories. For C0>=1/8 this coefficient is C0+19/4; the improvement over A094 is1/8, not29/8. These refer to different comparisons.

The q>=3 coefficients rest on (q^2+15q+7)/2^q<=61/8. Twice the numerator at q minus the next numerator equals q^2+13q-9, positive for every integer q>=3 (its forward difference2q+14>0). Also (q+1)/2^q decreases. The finite rational replay merely tests these formulas; the monotonic argument establishes the unbounded parameter range. b>=2,r>=1 is essential here. No claim at b1 is inferred.

## Exact source-reference kernel and complete ledger

With true source child laws P0,P1, m=(P0+P1)/2 and r_marg the queried-membership marginal of R, use raw_j=r_marg Pj/m on positive m fibers and raw_j=r_marg on zero fibers. Z0+Z1=2s and Rj=s raw_j/Zj, retaining mass s. On true atoms Pj/Rj=(m/r_marg)(Zj/s). KL disintegration gives Dparent-average Dchild=L_cond-average log2(Zj/s)>=0. This retains every zero-true reference fiber and the original s penalty. Entropy restriction decrement is nonnegative, and the exact physical tree identity is L=H(F)+sum_leaf reach Dleaf, with all signed charges and sibling terminals. Original-source inheritance does not supply a new descendant inequality c_h<=C0 I_h.

The separate checker exhausts all16 nonconstant labelled Boolean tables of ambient dimension1 or2, both masses1 and1/3, mixtures0 and1/4 with full uniform, and each source coordinate:120 physical query/reference cases. Direct character sums, Fraction kernels, exact prime-log cancellation and rigorous scalar log intervals check contraction, zero-true reference fibers and mass penalties. These finite tests are evidence for the independently derived kernel identity; they are not an arbitrary-dimension supplier theorem. Author checkers are not imported; only A081's previously pinned scalar log library is reused.

## The supplier is FEI-equivalent, not an already paid hypothesis

Define SUPPLY: there exists a finite absolute C0 such that for every finite Boolean f there exists a subprobability R_f, positive on the true spectrum, with CE(P_f,R_f)<=C0 I(f). Then SUPPLY implies FEI at the same constant: write R=sQ, so CE=H+D(P||Q)-log2 s>=H. Conversely FEI at C0 implies SUPPLY by choosing R=P_f (mass1), including constants. No computational claim is needed for this elementary equivalence. The graph records it as a semantic equivalence, never a proof-dependency edge through FEI. SUPPLY remains OPEN. Choosing R=P_f as an auxiliary entropy estimate inside an already conditional proof does not establish its influence-paid premise.

Repeatedly paying only by C_next=4C+15 yields exactly C_j=(C_initial+5)4^j-5. It is not a dimension-independent bound for unbounded edit depth. This demonstrates a limitation of that recurrence, not divergence of H/I and not a counterexample to FEI. A fixed-depth class result or A011 v3's two-edit extension does not close the supplier or arbitrary fixed-rate aggregation; v3 is context only and not admitted here.

## First unsupported line and graph semantics

The missing continuation is a reference-and-policy-compatible handoff of an ACTUAL inherited nonempty-profile conversion, including its reached signed conversion debit, old external U, source entropy changes and both complete terminals, paid by one original supplier; ultimately that supplier must be constructed at an absolute constant. A095's canonical/narrow-first account is not identified with A011's floor/padding-first account. A094's positive RAW third debit and A081's >2-bit fixture reserve stay unchanged.

Previously83 nodes are preserved. New source nodes retain exact versions, source-declared hashes, plain-statement hashes, hypotheses, proof sources and the original dependency scopes. A011's source proofs are PINNED_NOT_REAUDITED; A086/A094 reviews are accepted only as scoped external review evidence. The conditional coefficient and supplier-equivalence nodes are independently checked by A081. Open supply/handoff leaves cannot be promoted merely by these conditional statements. Proof-cycle validation is independent of workflow/review/semantic relations and rejects any cycle through FEI.
'''
(R/'REVIEW.md').write_text(review,encoding='utf-8')
g=load(R/'out/sources/00_PROOF_DEPENDENCIES.json');prior_count=len(g['nodes']);g['run_id']=R.name
units={'entropy':'bits','influence':'ordinary uniform physical total influence','log':'base2 except explicit ln'}
new=[]
def key(n):return n['claim_id']+'@'+str(n['version'])
def dep(d):
 if isinstance(d,str):return d
 for k in ['claim_key','claim','key']:
  if k in d:return d[k]
 return d['claim_id']+'@'+str(d['version'])
def imported(idx,cid,ver,status):
 c=next(c for c in load(R/pins[idx]['snapshot']) if c['claim_id']==cid and c['version']==ver)
 n=copy.deepcopy(c);n['source_statement_sha256']=n['statement_sha256'];n['statement_sha256']=digest(n['exact_statement']);n['statement_hash_convention']='UTF8 exact_statement only; original hash retained separately';n['units']=units;n['status']=status
 n['source_claims_pin']={'path':str(R/pins[idx]['snapshot']),'sha256':pins[idx]['sha256']};n['proof_sources']=[n['proof_source']];n['a081_review_scope']='Dependency metadata and quantitative interface only; no new blanket acceptance of full physical source theorem'
 new.append(n);return n
env=imported(6,'A011-POINT-EDIT-GENERAL-ENVELOPE-ONE-USE-HISTORY',1,'SOURCE_PROOF_PINNED_NOT_REAUDITED_BY_A081')
v1=imported(5,'A011-PADDING-FRESH-RESET-SAME-SOURCE-BANK',1,'SOURCE_PROOF_PINNED_NOT_REAUDITED_BY_A081')
v2=imported(3,'A011-PADDING-FRESH-RESET-SAME-SOURCE-BANK',2,'SCOPED_EXTERNAL_REVIEWS_PINNED_A081_INTERFACE_ONLY')
a86=imported(1,'A086-NONVANISHING-ALL-FRONTIER-OLD-BOOKING-ALLOWANCE',1,'A094_SCOPED_EXTERNAL_ACCEPTANCE_PINNED_A081_INTERFACE_ONLY')
a94=imported(1,'A094-LARGER-NONVANISHING-ALL-FRONTIER-ALLOWANCE',1,'AUTHOR_PHYSICAL_PROOF_PINNED_A081_COEFFICIENT_CONSEQUENCE_CHECKED')
def own(cid,stmt,hyp,deps=(),status='INDEPENDENTLY_CHECKED_CONDITIONAL_THEOREM_BY_A081'):
 n={'claim_id':cid,'version':1,'exact_statement':stmt,'hypotheses':hyp,'statement_sha256':digest(stmt),'statement_hash_convention':'UTF8 exact_statement only','units':units,'status':status,'proof_dependencies':list(deps),'proof_sources':[{'path':str(R/'REVIEW.md'),'sha256':sha(R/'REVIEW.md')}],'first_unproved_line':None}
 new.append(n);return n
algebra=own('A081-SHARP-CONDITIONAL-FRONTIER-ALLOWANCE','For Ig>0,C0>=0,G>=0, assume the SAME original rate4C0+15 account has full signed frontier margins at least(3C0/2+45/4)Ig+4C0G at root/final,(2C0+11/2)Ig+KG at padding, and(C0+45/8)Ig+KG at source. Then every external U in[0,(C0+37/8+min(C0,1/8))Ig] leaves at least7Ig/8 at ALL frontiers. This is the sharp scalar consequence of those three lower bounds after discarding G, not an upper bound on the actual bank or a payment for a different model/policy.',['The displayed physical frontier inequalities are ASSUMED in this algebraic theorem','C0 and Ig belong to ONE original source; complete signed ledger and mass penalties retained'])
equiv=own('A081-ABSOLUTE-REFERENCE-SUPPLIER-EQUIVALENT-FEI','There exists an absolute finite C0 with, for every finite uniform-cube Boolean f, a finite-cost subprobability R_f positive on its Fourier support satisfying CE(P_f,R_f)<=C0 I(f), if and only if uniform-cube FEI holds with that same C0. The forward direction uses CE=H+D(P||R/s)-log2 s>=H, and the reverse takes R=P_f. This equivalence does not prove either universal assertion.',['Information bits; ordinary uniform physical influence; source mass s in(0,1]','Constants allowed; choose the point spectrum at constants'])
supplier=own('A081-OPEN-ABSOLUTE-REFERENCE-SUPPLIER','Construct one absolute finite C0 and an influence-priced complete source reference for EVERY Boolean function; supplied c<=C0 I is not a construction.',['Every finite uniform cube; fixed C0 independent of dimension and edit depth'],status='OPEN');supplier['first_unproved_line']=supplier['exact_statement'];supplier['proof_sources']=[]
handoff=own('A081-OPEN-COMPATIBLE-INHERITED-PROFILE-HANDOFF','Pay one ACTUAL inherited nonempty-profile conversion into the prescribed A011 floor/padding-first history from the SAME unused original source account, retaining current reference, old U, source entropy changes and BOTH complete terminal costs.',['Actual model/policy compatibility must be proved; no renewed C0, bank or source','Nonvanishing allowance alone does not supply the conversion'],status='OPEN');handoff['first_unproved_line']=handoff['exact_statement'];handoff['proof_sources']=[]
g['nodes']+=new
g['stage10_semantic_relations']=[{'from':key(supplier),'to':'FEI-FINAL@1','kind':'EQUIVALENT_NOT_PROOF_EDGE','proof':key(equiv)},{'from':key(a94),'to':key(handoff),'kind':'ALLOWANCE_DOES_NOT_DISCHARGE_COMPATIBILITY'},{'from':key(algebra),'to':key(a94),'kind':'CONDITIONAL_COEFFICIENT_REFINEMENT_NOT_PHYSICAL_REVIEW'}]
contract={'source':'ONE original supplied source','source_price':'ASSUMED, NOT CONSTRUCTED','policy':'A011 v2 padding-then-source only','ledger':'SIGNED includes all credits and old bookings','mass':'original subprobability mass retained','old_U':'fully charged at every frontier','independent_terminal':'additive outside core bank','compatibility':'OPEN','universal_supplier':'OPEN','units':'bits'}
g['stage10_contract']=contract
for i,p in enumerate(pins):g['sources']['stage10_'+str(i)]={'local_path':str(R/p['snapshot']),'local_sha256':p['sha256'],'original_local_path':p['source']}
def valid(z):
 ns={key(n):n for n in z['nodes']};assert len(ns)==len(z['nodes']);active=set();seen=set()
 def walk(k):
  assert k in ns and k not in active
  if k in seen:return
  active.add(k)
  for d in ns[k]['proof_dependencies']:walk(dep(d))
  active.remove(k);seen.add(k)
 for k in ns:walk(k)
 for k in ['FEI-FINAL@1',key(supplier),key(handoff),'A081-OPEN-WIDE-RESET-AFTER-TWO-NARROW@1']:assert ns[k]['status']=='OPEN'
 assert z['stage10_contract']==contract
 for i,n in enumerate(z['nodes'][prior_count:]):
  assert n['exact_statement']==new[i]['exact_statement'] and digest(n['exact_statement'])==n['statement_sha256']
  assert n['hypotheses']==new[i]['hypotheses'] and n['units']==units and n['status']==new[i]['status']
  assert n['proof_dependencies']==new[i]['proof_dependencies']
  if 'source_claims_pin' in n:assert sha(n['source_claims_pin']['path'])==n['source_claims_pin']['sha256']
 assert all(x['kind']!='PROOF' for x in z['stage10_semantic_relations'])
 return len(seen)
guards=[]
def reject(label,fn):
 z=copy.deepcopy(g);fn(z)
 try:valid(z)
 except (AssertionError,KeyError):guards.append(label);return
 raise AssertionError(label)
reject('cycle through FEI and conditional allowance',lambda z:(z['nodes'][0]['proof_dependencies'].append(key(algebra)),z['nodes'][prior_count+5]['proof_dependencies'].append('FEI-FINAL@1')))
reject('FEI self-cycle',lambda z:z['nodes'][0]['proof_dependencies'].append('FEI-FINAL@1'))
reject('wrong source version',lambda z:z['nodes'][prior_count+3]['proof_dependencies'][0].__setitem__('version',3))
reject('source hash mismatch',lambda z:z['nodes'][prior_count+4]['source_claims_pin'].__setitem__('sha256','0'*64))
reject('nats',lambda z:z['nodes'][prior_count+5].__setitem__('units',{'entropy':'nats'}))
reject('universal supplier promotion',lambda z:z['nodes'][-2].__setitem__('status','PROVED'))
reject('compatibility promotion',lambda z:z['nodes'][-1].__setitem__('status','PROVED'))
reject('treat source price as proved',lambda z:z['stage10_contract'].__setitem__('source_price','PROVED'))
reject('renewed source',lambda z:z['stage10_contract'].__setitem__('source','descendant'))
reject('erase old U',lambda z:z['stage10_contract'].__setitem__('old_U','refunded'))
reject('positive-parts only ledger',lambda z:z['stage10_contract'].__setitem__('ledger','positive parts only'))
reject('normalize subprobability for free',lambda z:z['stage10_contract'].__setitem__('mass','normalized to1'))
reject('use external terminal to fund core',lambda z:z['stage10_contract'].__setitem__('independent_terminal','funds core'))
reject('canonical narrow-first policy substitution',lambda z:z['stage10_contract'].__setitem__('policy','arbitrary canonical narrow-first'))
reject('drop b>=2 hypothesis',lambda z:z['nodes'][prior_count+4].__setitem__('hypotheses',['b>=1']))
reject('alter exact statement',lambda z:z['nodes'][prior_count+5].__setitem__('exact_statement','FEI'))
save(R/'PROOF_DEPENDENCIES.json',g)
save(R/'out/GRAPH_VALIDATION.json',{'status':'PASS','nodes':valid(g),'prior_nodes':prior_count,'new_nodes':len(new),'rejected_mutations':guards,'unresolved_new_leaves':[key(supplier),key(handoff)],'FEI':'OPEN','peer_vs_own_evidence_distinguished':True})
fields=['claim_id','version','exact_statement','hypotheses','statement_sha256','proof_dependencies','status','first_unproved_line']
claims=[]
for n in [algebra,equiv]:
 c={k:copy.deepcopy(n[k]) for k in fields};c.update(contributors=['A081/fleet03'],proof_source={'path':str(R/'REVIEW.md'),'certificate':str(R/'out/EXACT_CERTIFICATE.json')},review_records=[],supersedes=[],refutes=[],next_consumers=['A094','A086','A011','A099','B17']);claims.append(c)
save(R/'CLAIMS.json',claims)
next_action='A094/A086/A011: prove one actual model-and-policy-compatible inherited-profile handoff using the SAME unused original source account, old U and both complete terminals; or supply the absolute reference premise without invoking FEI. Do not substitute the conditional allowance for this step.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B17','packet_id':'A081','gap_id':'G-R-MISMATCH','attempt_id':'A081-stage10-frontier-supplier-cycle-audit','method':'Pinned exact source versions, conditional affine certificate, direct-character source-kernel replay and semantic-vs-proof graph separation','mathematical_delta':'A086/A094 nonvanishing allowance chain pinned at precise external-review scopes. Exact algebra refines the conditional allowance by min(C0,1/8)Ig while preserving7Ig/8. Absolute supplier proved equivalent to FEI as a statement, not established; supplier and compatibility OPEN.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'CONDITIONAL_COEFFICIENT_AND_EQUIVALENCE_PROVED_FULL_FEI_OPEN','claim_versions_used':[key(n) for n in [env,v1,v2,a86,a94]],'claims_created_or_changed':[key(algebra),key(equiv)],'source_artifacts':['REVIEW.md','PROOF_DEPENDENCIES.json','out/SOURCE_PINS.json','out/FROZEN_SPEC.json','out/EXACT_CERTIFICATE.json','out/GRAPH_VALIDATION.json'],'next_consumers':['A094','A086','A011','A099','B17','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Actual reference/policy compatible handoff unpaid','Absolute influence-priced supplier equivalent to FEI remains unproved','Full arbitrary-source physical theorem not reaudited by A081; peer review scopes retained','Brain wake degraded: personal model98.2h,state82.8h,dream33.5h stale; unused','Shared compute heartbeat stale; no shared-service mutation authorized','Supervisor copy and remote adoption unverified'],'packet_ids':['A081']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

A081/B17 stage10 encodes the A011 v1/v2 -> A086 -> A094 conditional frontier allowance chain, with every version, source mass, policy and supplied hypothesis preserved. It independently proves the scalar consequence and the equivalence of an absolute reference supplier with FEI. All quantities use bits and physical uniform influence. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

BOARD 2026-10-23 11:45 UTC; B17 STREAM_NOTES v2; own stage9 STATUS and83-node graph; A094 20261023T110024 DERIVATION sections1–6; A011 20261023T000841 DERIVATION and exact dependency records; A086/A094 source claims and reviews. out/SOURCE_PINS.json contains immutable local snapshots, hashes and original paths. The governing execution protocol is pinned. Earlier source proof evidence is preserved without blanket new acceptance. The fresh required wake reports degraded personal-model98.2h, state82.8h and dream33.5h; these were not mathematical authority. Shared checklist/git/brain updates remain excluded by the explicit A081-only write scope.

# complete derivation or exact first unsupported line

REVIEW.md derives the all-C0 conditional allowance: if the named original frontier margins hold, U<=[C0+37/8+min(C0,1/8)]Ig leaves>=7Ig/8 at every frontier. This refines A094 by min(C0,1/8)Ig; A094 itself improves A086 by29Ig/8, both with the SAME7Ig/8 reserve. These quantities differ from stage9's>2-bit reserve for one canonical-reset fixture. CE>=H makes a universal absolute-cost supplier FEI-equivalent; selecting the true source law does not prove its influence price. The first unsupported continuation is an actual compatible profile handoff and ultimately that supplier. Full physical A011/A094 proofs retain their explicit external evidence states.

# executed validation with domain, arithmetic, commands and outputs

Frozen120 source-query/reference cases: every nonconstant labelled Boolean table on1 or2 bits, source masses1 and1/3, uniform mixtures0 and1/4, every coordinate. Direct character sums, Fraction posterior transport, prime-log exact cancellation and rigorous log intervals verify retained mass and KL contraction, including reference-only zero-true fibers. The unbounded coefficient argument is analytic, with finite q3..64,C0=k/8 for k0..64 and recurrence depth0..8 replay. Command: python -X utf8 {R/'code/check.py'}. PASS: {result['assertions']} direct assertions, runtime{result['seconds']:.4f}s; prior scalar-library assertions excluded. Estimated80MB, below300MB memok gate; no heavy job or Lean kernel proof. Single full frozen job is the pilot, counted once.

# proof dependencies and changed downstream conclusions

Graph preserves83 nodes and adds{len(new)}, total{len(g['nodes'])};16 adversarial mutations are rejected, including cycles through FEI, source-version/hash/unit changes, silently proved source hypotheses, free mass normalization, ledger/policy substitution and dropped old bookings. Semantic FEI equivalence and review relations are separate from proof edges. The absolute supplier, actual handoff, general third reset and FEI remain OPEN. No arbitrary two-edit v3 or fixed-rate unbounded iteration is admitted.

# one next mathematical action and independent reviewer

{next_action}

# actual persistence receipts or precise save blocker

Four protocol files, review, checker, pinned sources, exact output and graph are saved in this assigned run. Local schema and readback/hash receipts are in out/. STATUS remains two lines; WORKLOG and LEARNED are appended. Shared compute heartbeat/log were read and are stale; no service was restarted or work stopped. No git, messages, other-agent writes, GPU or detached jobs. Supervisor copying, remote publication and canonical adoption are unverified.

# Universal bridge

This stage moves C024 history transfer and C020 whole-set witness cost by certifying the exact nonvanishing allowance interface, its additional min(C0,1/8)Ig conditional slack, and the distinction between that paid conditional propagation and the FEI-equivalent unpaid universal supplier. Universal constant improvement is zero. Actual model/policy-compatible handoff and absolute source construction remain open. NEXT attacks that precise missing implication, avoiding a circular FEI-dependent supplier and directing assembly toward a dimension-independent theorem rather than another finite class.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(H/'STATUS.md').write_text(f'STATE: A081 stage10 complete: {len(g["nodes"])}-node graph/16 guards PASS; conditional frontier allowance refined by min(C0,1/8)Ig; absolute supplier FEI-equivalent and OPEN;120 exact source-query cases PASS.\nNEXT: '+next_action+'\n',encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
for filename,txt in [('WORKLOG.md',f'{now}: Stage10 pinned source-envelope/paddingv1/v2/A086/A094 chain; distinguished external physical review from own scalar proof. {result["assertions"]} exact assertions/120 source-query cases; {len(g["nodes"])} nodes/16 guards PASS. Compatible handoff and absolute supplier remain unpaid; no universal FEI claim.'),('LEARNED.md','Stage10: A094 allowance(C0+37/8)Ig vs A086(C0+1)Ig gains29Ig/8 with SAME7Ig/8 residual; three interface margins sharpen allowance further by min(C0,1/8)Ig, conditional only. Universal existence of subprobability R with CE<=absolute C0 I is equivalent to FEI, not an independent supplier construction. Record equivalence as semantic relation, never a circular proof. C_next=4C+15 gives C_j=(C_initial+5)4^j-5; unbounded edit depth is not a uniform bound. Canonical narrow-first and floor padding-first models remain incompatible absent an explicit paid handoff.')]:
 with (H/filename).open('a',encoding='utf-8') as f:f.write('\n'+txt+'\n')
protocol=load(R/'out/sources/08_EXECUTION_PROTOCOL.json');found={}
def scan(o):
 if isinstance(o,dict):
  for k,v in o.items():
   if k in ['claim_fields','progress_fields','report_fields']:found[k]=v
   else:scan(v)
 elif isinstance(o,list):
  for v in o:scan(v)
scan(protocol)
assert all(set(c)==set(found['claim_fields']) for c in claims)
assert set(progress)=={x.split(' (')[0] for x in found['progress_fields']}
assert all(x in report for x in found['report_fields']) and report.rstrip().split('# Universal bridge')[-1].strip()
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((H/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
save(R/'out/SCHEMA_VALIDATION.json',{'status':'PASS','exact_protocol_fields':True,'identical_delta':True,'status_two_lines':True})
files=[p for p in R.rglob('*') if p.is_file() and p.name not in ['FINAL_READBACK.json','PERSISTENCE_RECEIPTS.json']]
assert all(p.stat().st_size<20*1024*1024 for p in files)
receipts=[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files]
save(R/'out/PERSISTENCE_RECEIPTS.json',{'status':'VERIFIED_LOCAL','remote':'UNVERIFIED','files':receipts})
for p in receipts:assert sha(R/p['path'])==p['sha256']
save(R/'out/FINAL_READBACK.json',{'status':'PASS','nodes':valid(load(R/'PROOF_DEPENDENCIES.json')),'files_rehashed':len(receipts),'report_readback':(R/'REPORT.md').read_text(encoding='utf-8')==report,'FEI':'OPEN','formal_kernel_proof':False,'remote':'UNVERIFIED'})
print(json.dumps({'status':'PASS','nodes':len(g['nodes']),'guards':len(guards),'assertions':result['assertions'],'cases':120,'files':len(receipts),'FEI':'OPEN'}))
