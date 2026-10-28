from pathlib import Path
import json,hashlib,copy,datetime
R=Path(__file__).resolve().parents[1];HOME=R.parents[1];TEAM=HOME.parents[1]
PREV=HOME/'runs/20261023T140159Z-account03-A081-dependency-certificates'
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(s):return hashlib.sha256(s.encode('utf-8')).hexdigest()
def key(n):return n['claim_id']+'@'+str(n['version'])
def dk(d):
 if isinstance(d,str):return d
 for k in ['claim_key','claim','key']:
  if k in d:return d[k]
 return d['claim_id']+'@'+str(d['version'])
pins=[]
def pin(p):
 b=p.read_bytes();dest=R/'out/sources'/f'{len(pins):02}_{p.name}';dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
 rec={'source':str(p),'snapshot':str(dest.relative_to(R)),'sha256':sha(dest)};pins.append(rec);return rec
prior_pin=pin(PREV/'PROOF_DEPENDENCIES.json');g=load(PREV/'PROOF_DEPENDENCIES.json');g['run_id']=R.name
v5dir=TEAM/'agents/A011/runs/20261023T134844Z-account03-A011-representation-existence'
v6dir=TEAM/'agents/A011/runs/20261027T025625Z-account04-A011-representation-existence'
objdir=TEAM/'agents/A094/runs/20261026T232939Z-account04-A094-proof-chain-challenger'
revdir=TEAM/'agents/A100/runs/20261027T023227Z-account04-A100-release-and-continuation-ledger'
units={'entropy':'bits','influence':'ordinary uniform physical total influence','mass':'complete subprobability, including ghost mass'}
new=[];relations=[]
def source_node(p,cid,ver,status,scope):
 rec=pin(p);c=copy.deepcopy(next(c for c in load(p) if c['claim_id']==cid and c['version']==ver))
 c['source_statement_sha256']=c['statement_sha256'];c['statement_sha256']=digest(c['exact_statement']);c['statement_hash_convention']='UTF8 exact_statement only; source-declared hash retained separately'
 c['source_declared_dependencies']=c['proof_dependencies'];c['proof_dependencies']=[];c['units']=units;c['source_claims_pin']=rec;c['source_status']=c['status'];c['status']=status;c['a081_scope']=scope
 c['statement_hypotheses_sha256']=digest(json.dumps({'exact_statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False))
 new.append(c);return c
def own(cid,statement,hypotheses,status='INDEPENDENT_EXACT_ACCOUNTING_RECONSTRUCTION',deps=()):
 c={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':digest(statement),'statement_hash_convention':'UTF8 exact_statement only','units':units,'status':status,'proof_dependencies':list(deps),'proof_sources':[{'path':str(R/'REVIEW.md')}],'first_unproved_line':None}
 c['statement_hypotheses_sha256']=digest(json.dumps({'exact_statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':'),ensure_ascii=False));new.append(c);return c
v5=source_node(v5dir/'CLAIMS.json','A011-PADDING-FRESH-RESET-SAME-SOURCE-BANK',5,'TERMINAL_FUNCTIONAL_ONLY_TRANSACTION_IDENTIFICATION_WITHDRAWN','Numerical functional retained as source claim; no complete transaction acceptance.')
v5['source_first_unproved_line']=v5['first_unproved_line']
v5['first_unproved_line']='WITHDRAWN identification Lterminal=CEroot+actual signed resets omits physical-query Qloss; numerical terminal-functional bound not refuted. Local-floor all-policy payment and universal supplier remain open.'
obj=source_node(objdir/'CLAIMS.json','A094-A011-V5-PHYSICAL-QUERY-KL-LEDGER-GAP',1,'A081_ACCOUNTING_AND_ALL_B_SIGN_RECONSTRUCTED','Original statement unchanged. Source definitions are not an accepted premise. Full witness family and telescope independently reconstructed.')
v6=source_node(v6dir/'CLAIMS.json','A011-PADDING-FRESH-RESET-SAME-SOURCE-BANK',6,'SOURCE_V6_PINNED_FULL_ROOT_ENVELOPE_REVIEW_PENDING','Inherited/calibrated descendants only; full original root envelope not independently reaudited.')
for p in [v5dir/'DERIVATION.md',v6dir/'DERIVATION.md',objdir/'DERIVATION.md',revdir/'REPORT.md',revdir/'CLAIMS.json']:
 pin(p)
reviewdir=TEAM/'agents/A031/runs/20261027T034059Z-account04-A031-convolution-identity'
rc=next(c for c in load(reviewdir/'CLAIMS.json') if key(c)==key(v6))
assert rc['exact_statement']==v6['exact_statement'] and rc['hypotheses']==v6['hypotheses']
v6['review_records']=rc['review_records']
v6['external_review_claims_pin']=pin(reviewdir/'CLAIMS.json')
pin(reviewdir/'DERIVATION.md');pin(reviewdir/'out/MAIN.json')
v6['status']='A031_FULL_SCOPED_REVIEW_PINNED_A081_ROOT_REVIEW_NOT_PERFORMED'
v6['source_first_unproved_line']=v6['first_unproved_line']
v6['first_unproved_line']='A031 exact-scope v6 review is pinned. A081 has not independently reaudited its whole root-envelope proof; original arbitrary-core source and mandatory local-floor admission remain unpaid.'
for dep in v6['source_declared_dependencies']:
 cid=dep['claim_id']
 if cid.startswith(('A050','A096')):
  matches=[]
  for p in sorted((TEAM/'agents'/cid[:4]/'runs').glob('*/CLAIMS.json'),reverse=True):
   for c in load(p):
    if c['claim_id']==cid and c['version']==dep['version'] and c['statement_sha256']==dep['statement_sha256']:matches.append(p)
  assert matches,cid
  n=source_node(matches[0],cid,dep['version'],'EXACT_SOURCE_INTERFACE_PINNED_NOT_FULLY_REAUDITED','v6 specialization independently derived in DERIVATION 4.1; full upstream theorem not newly accepted')
  relations.append({'from':key(v6),'to':key(n),'kind':'INTERFACE_SOURCE_NOT_FULL_PROOF_ACCEPTANCE'})
tel=own('A081-FULL-QUERY-CONTRACTION-SCOPE-CERTIFICATE','For any finite fixed-target physical restriction tree, let Q be covering complete subprobability references of preserved mass s>0, use raw child r(T)P_b(T)/m(T) on occupied fibers and r(T) on zero fibers, and normalize each child back to s. Then delta=D(P||Q)-mean D(P_b||Q_b)=sum_T m(T) KL(P(.|T)||Q(.|T))-(1/2)log2(Z0 Z1/s^2)>=0. With actual signed same-target reset total E, CE_root+E=H_root+sum reach*delta+mean full terminal D. Inherited-only descendants have E=0; normalized-vacuum calibration at the SAME mass has E<=0. The latter policies therefore have sum reach*delta+mean terminal D<=D_root. This makes NO claim for arbitrary locally rebuilt nonempty floors.',['Finite tree and one fixed target; nonrepeated queries along branches','Cover on true support; positive inherited Z; ghost fibers and scalar mass retained','Actual signed reset charges; full physical reaches; normalized-vacuum shape only if s<1'])
wit=own('A081-A011-V5-NORMALIZER-STRICT-GAP','For every integer b>=12 in the actual M1,a1,r1 dictator point edit, epsilon=2^(-1-b), the first-floor controller query has Zclean=(1+3epsilon^2)/[(1+3epsilon)(1-2epsilon+2epsilon^2)] and Zedit=2-Zclean. Denominator minus numerator equals epsilon(1-epsilon)(1-6epsilon)>0, so 1-Zclean Zedit=(1-Zclean)^2>0 and omitted query contraction is strictly positive. This invalidates only the root-plus-reset identification with H_root+mean terminal D, not the numerical functional bound or reserve adequacy.',['A011 v5 actual normalized root floor beta=3epsilon and true control kernel','One-bit dictator with exact supplied source, b>=12 untouched padding bits, one fresh fair controller','Bits and both complete terminal costs'],deps=[key(tel)])
margin=own('A081-V6-CONDITIONAL-ORIGINAL-OWNER-MARGIN','Suppose Ig>0,C0>=0, c<=C0 Ig, Braw<=135c/92+320S, S/Ig<=151/8192 and I_F>=4081Ig/4096+sum G with every G>=0. For SAME K=4C0+15 and full old 0<=U<=(C0+37/8)Ig, K I_F-Braw-U>=[(35751/23552)C0+18111/4096]Ig+K sum G>0. This is exact conditional scalar algebra and does not establish the physical root envelope or a source supplier.',['All named scalar hypotheses assumed explicitly','No new source/rate, complete Braw and full old U','Bits and physical influence'])
root=own('A081-V6-ROOT-ENVELOPE-UNREVIEWED-EXTRACT','In A011 v6 supplied-source fresh-control construction with fixed b>=12, complete root CE<=135c/92+320 sum_j(1+j(j+1))rho_j D_j for every finite edit count.',['Exact original root floors and true unqueried-control kernels of A011 v6','Supplied finite covering source c<=C0 I(g)','This is the root-only substatement rederived in A011 DERIVATION section4 equation6'],status='SOURCE_PROOF_PINNED_INDEPENDENT_ROOT_REVIEW_PENDING')
root['proof_sources']=[{'path':str(v6dir/'DERIVATION.md'),'sha256':sha(v6dir/'DERIVATION.md'),'locator':'section4 equation6'}]
root['first_unproved_line']='A081 has not independently reconstructed the entire physical root-envelope estimate.'
local=own('A081-OPEN-V5-LOCAL-FLOOR-QUERY-LOSS','For every useful required local-floor policy, pay accumulated physical-query KL contractions after all signed floor resets, full old U and all complete terminals from the SAME unused original influence bank.',['Original v5 local-floor descendants; no replacement by inherited-only/vacuum-only models'],status='OPEN')
local['first_unproved_line']=local['exact_statement'];local['proof_sources']=[]
v6['proof_dependencies']=[key(root),key(tel),key(margin)]
obj['proof_dependencies']=[key(tel),key(wit)]
relations += [
 {'from':key(obj),'to':key(v5),'kind':'REFUTES_TRANSACTION_IDENTIFICATION_ONLY_NOT_NUMERICAL_BOUND'},
 {'from':key(v6),'to':key(v5),'kind':'REPAIRS_BY_CHANGING_DESCENDANT_REFERENCE_POLICY'},
 {'from':key(v6),'to':key(local),'kind':'DOES_NOT_DISCHARGE_LOCAL_FLOOR_POLICY'},
 {'from':key(v6),'to':'A081-OPEN-ABSOLUTE-REFERENCE-SUPPLIER@1','kind':'SUPPLIED_REFERENCE_IS_NOT_UNIVERSAL_CONSTRUCTION'},
 {'from':key(obj),'to':key(v5),'kind':'AUDITED_DEFINITIONS_ONLY_NOT_PROOF_DEPENDENCY'}]
existing={key(n) for n in g['nodes']}
for n in new:assert key(n) not in existing;existing.add(key(n))
for n in new:
 for p in n.get('proof_sources',[]):
  if p.get('path')==str(R/'REVIEW.md'):p['sha256']=sha(R/'REVIEW.md')
g['nodes']+=new;g['stage12_scope_relations']=relations
g['stage12_contract']={'v5':'terminal functional only; transaction interpretation withdrawn','v6':'inherited or normalized-vacuum descendants; not local floors','root':'complete source supplied; root envelope pending independent review','old_U':'same ORIGINAL full old debit retained','mass':'s preserved; actual vacuum equals P(empty) only at s1','history':'query KL retained and paid inside root D for inherited/calibration policy','formal':'exact certificate/prose reconstruction; not a Lean-certified full theorem','FEI':'OPEN'}
save(R/'out/SOURCE_PINS.json',pins)
save(R/'out/NEW_NODES.json',new)
save(R/'PROOF_DEPENDENCIES.json',g)
save(R/'out/UNRESOLVED_LEAVES.json',[{'key':key(n),'status':n['status'],'first_unproved_line':n.get('first_unproved_line')} for n in g['nodes'] if n['status']=='OPEN' or n.get('first_unproved_line')])
print(json.dumps({'nodes':len(g['nodes']),'new_nodes':len(new),'source_pins':len(pins),'contract':g['stage12_contract']}))
