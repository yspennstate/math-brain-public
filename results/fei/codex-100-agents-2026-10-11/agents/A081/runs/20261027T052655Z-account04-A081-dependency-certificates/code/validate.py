from pathlib import Path
import json,copy,hashlib
R=Path(__file__).resolve().parents[1]
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def digest(s):return hashlib.sha256(s.encode('utf-8')).hexdigest()
def key(n):return n['claim_id']+'@'+str(n['version'])
def dep(d):
 if isinstance(d,str):return d
 for k in ['claim_key','claim','key']:
  if k in d:return d[k]
 return d['claim_id']+'@'+str(d['version'])
g=load(R/'PROOF_DEPENDENCIES.json');new=load(R/'out/NEW_NODES.json');frozen={key(n):copy.deepcopy(n) for n in new}
contract=copy.deepcopy(g['stage12_contract']);relations=copy.deepcopy(g['stage12_scope_relations'])
def validate(z):
 ns={key(n):n for n in z['nodes']};assert len(ns)==len(z['nodes'])
 active=set();done=set()
 def walk(k):
  assert k in ns and k not in active
  if k in done:return
  active.add(k)
  for d in ns[k]['proof_dependencies']:walk(dep(d))
  active.remove(k);done.add(k)
 for k in ns:walk(k)
 assert ns['FEI-FINAL@1']['status']=='OPEN'
 assert ns['A081-OPEN-ABSOLUTE-REFERENCE-SUPPLIER@1']['status']=='OPEN'
 assert z['stage12_contract']==contract;assert z['stage12_scope_relations']==relations
 for k,n0 in frozen.items():
  n=ns[k]
  for field in ['exact_statement','hypotheses','units','status','proof_dependencies','statement_sha256','source_declared_dependencies']:
   assert n.get(field)==n0.get(field),(k,field)
  assert digest(n['exact_statement'])==n['statement_sha256']
  assert digest(json.dumps({'exact_statement':n['exact_statement'],'hypotheses':n['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False))==n['statement_hypotheses_sha256']
  if 'source_claims_pin' in n:
   p=n['source_claims_pin'];assert hashlib.sha256((R/p['snapshot']).read_bytes()).hexdigest()==p['sha256']
 for p in load(R/'out/SOURCE_PINS.json'):assert hashlib.sha256((R/p['snapshot']).read_bytes()).hexdigest()==p['sha256']
 return len(done)
count=validate(g);guards=[]
def reject(label,fn):
 z=copy.deepcopy(g);fn(z)
 try:validate(z)
 except (AssertionError,KeyError):guards.append(label);return
 raise AssertionError('accepted invalid fixture '+label)
def find(z,k):return next(n for n in z['nodes'] if key(n)==k)
v5='A011-PADDING-FRESH-RESET-SAME-SOURCE-BANK@5';v6=v5[:-1]+'6';tel='A081-FULL-QUERY-CONTRACTION-SCOPE-CERTIFICATE@1'
reject('self cycle',lambda z:find(z,v6)['proof_dependencies'].append(v6))
def feicycle(z):find(z,v6)['proof_dependencies'].append('FEI-FINAL@1');find(z,'FEI-FINAL@1')['proof_dependencies'].append(v6)
reject('cycle through final FEI',feicycle)
reject('missing exact dependency version',lambda z:find(z,v6)['proof_dependencies'].append('UNKNOWN@99'))
reject('duplicate exact version',lambda z:z['nodes'].append(copy.deepcopy(find(z,v6))))
reject('universal source promoted from supplied',lambda z:find(z,'A081-OPEN-ABSOLUTE-REFERENCE-SUPPLIER@1').update(status='PROVED'))
reject('FEI status promoted',lambda z:find(z,'FEI-FINAL@1').update(status='PROVED'))
reject('v5 entire claim accepted',lambda z:find(z,v5).update(status='PROVED'))
reject('v6 root proof accepted without review',lambda z:find(z,v6).update(status='PROVED'))
reject('v6 silently reuses v5 whole statement',lambda z:find(z,v6)['proof_dependencies'].append(v5))
reject('hypothesis removed',lambda z:find(z,tel)['hypotheses'].pop())
reject('units drift',lambda z:find(z,tel)['units'].update(entropy='nats'))
reject('query KL erased from statement',lambda z:find(z,tel).update(exact_statement='Braw = Hroot + Dterminal'))
reject('source definitions become proof premise',lambda z:find(z,'A094-A011-V5-PHYSICAL-QUERY-KL-LEDGER-GAP@1')['proof_dependencies'].append(v5))
reject('normalized shape conflated with actual vacuum',lambda z:z['stage12_contract'].update(mass='vacuum equals actual mass at all s'))
reject('local floors silently inherited',lambda z:z['stage12_contract'].update(v6='arbitrary local floors'))
reject('old original debit removed',lambda z:z['stage12_contract'].update(old_U='ignored'))
reject('scope edge promoted to proof acceptance',lambda z:z['stage12_scope_relations'][0].update(kind='FULL_V5_REFUTED'))
result={'status':'PASS','nodes':count,'new_nodes':len(new),'proof_edges':sum(len(n['proof_dependencies']) for n in g['nodes']),'cycle_through_FEI_rejected':True,'mutation_guards':guards,'guard_count':len(guards),'accepted_closure_claimed':False,'new_source_envelope_independent_review':'PENDING','FEI':'OPEN'}
(R/'out/GRAPH_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
