from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def receipt(p):return {'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
old=read(R/'out/PERSISTENCE_RECEIPTS.json')
for entry in old['artifacts']+old['rolling']:
 assert receipt(Path(entry['path']))==entry
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for claim in read(R/'CLAIMS.json'):
 digest=hashlib.sha256(json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
 assert digest==claim['statement_sha256']
assert read(R/'out/VALIDATION_TOTALS.json')['exact_assertions']==1097416
result={'status':'FINAL_SAVED_HASHES_PASS','exact_assertions':1097416,'scope':'Readback of saved artifacts, protocol copies and statement digests; no tests repeated','new_independent_review':'PENDING','full_FEI':'OPEN'}
(R/'out/FINAL_VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
old['at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
old['final_saved_readback']='PASS'
old['artifacts']=[receipt(p) for p in sorted(R.rglob('*')) if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']
assert all(x['bytes']<20_000_000 for x in old['artifacts'])
(R/'out/PERSISTENCE_RECEIPTS.json').write_text(json.dumps(old,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(result))
