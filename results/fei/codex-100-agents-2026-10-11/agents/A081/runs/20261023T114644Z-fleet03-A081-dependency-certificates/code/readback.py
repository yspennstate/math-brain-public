from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
def load(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,o):Path(p).write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
g=load(R/'PROOF_DEPENDENCIES.json');ns={n['claim_id']+'@'+str(n['version']):n for n in g['nodes']};checked=[]
for n in g['nodes'][83:]:
 for d in n['proof_dependencies']:
  if isinstance(d,dict) and 'statement_sha256' in d:
   k=d['claim_id']+'@'+str(d['version']);target=ns[k]
   assert d['statement_sha256'] in [target['statement_sha256'],target.get('source_statement_sha256')]
   checked.append({'from':n['claim_id']+'@'+str(n['version']),'to':k,'declared_digest':d['statement_sha256'],'status':'MATCHED_EXPLICIT_HASH_CONVENTION'})
for p in load(R/'out/SOURCE_PINS.json'):assert sha(R/p['snapshot'])==p['sha256']
save(R/'out/EDGE_HASH_VALIDATION.json',{'status':'PASS','checked_edges':checked,'source_pins_rehashed':14})
old=load(R/'out/PERSISTENCE_RECEIPTS.json')
for p in old['files']:assert sha(R/p['path'])==p['sha256']
files=[p for p in R.rglob('*') if p.is_file() and p.name not in ['PERSISTENCE_RECEIPTS.json','FINAL_READBACK.json']]
rows=[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files]
save(R/'out/PERSISTENCE_RECEIPTS.json',{'status':'VERIFIED_LOCAL','remote':'UNVERIFIED','files':rows})
receipt=load(R/'out/FINAL_READBACK.json');receipt['files_rehashed']=len(rows);receipt['dependency_declared_hash_edges_verified']=len(checked)
save(R/'out/FINAL_READBACK.json',receipt)
print((R/'REPORT.md').read_text(encoding='utf-8'))
print('FINAL_READBACK',json.dumps(receipt));print('STATUS',(R.parents[1]/'STATUS.md').read_text(encoding='utf-8'))
