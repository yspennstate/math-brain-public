from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def receipt(p):return {'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
v=read(R/'out/EXACT_RESULTS.json');w=read(R/'out/TENSOR_RESULTS.json');claim=read(R/'CLAIMS.json')[0]
assert v['status']==w['status']=='PASS'
assert v['assertions']+w['assertions']==61177
digest=hashlib.sha256(json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert digest==claim['statement_sha256']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text().splitlines())==2
write(R/'out/VALIDATION_TOTALS.json',{'status':'PASS','assertions':61177,'completed_helper_seconds':v['seconds']+w['seconds'],'credited_main_version':'v1.1 stronger outward auxiliary sign','prior_pilot_not_double_counted':True,'main':v,'tensor':w})
report=(R/'REPORT.md').read_text(encoding='utf-8')
report=report.replace('17.458394 helper seconds.',f'{v["seconds"]:.6f} helper seconds in the final v1.1 check. The initial pilot took 17.458394 seconds; its identical assertion domain is not counted twice. VALIDATION_REFINEMENT.json freezes the strengthened auxiliary sign (upper left side <= lower right side) before rerunning; no dimension or domain changed.')
(R/'REPORT.md').write_text(report,encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now}: Final sign audit strengthened the auxiliary log-sum cost check to outward-separated enclosures (not merely overlapping intervals). Frozen v1.1 keeps the same294-root/1764-reference domain; PASS58521 assertions in{v["seconds"]:.6f}s. No additional assertion credit. Final totals61177, protocol and statement digest PASS.\n')
items=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
  assert p.stat().st_size<20_000_000
  if p.suffix=='.json':read(p)
  items.append(receipt(p))
old=read(R/'out/PERSISTENCE_RECEIPTS.json')
old.update({'at_utc':now,'artifacts':items,'rolling':[receipt(A/n) for n in ['STATUS.md','WORKLOG.md','LEARNED.md']],'auxiliary_interval_sign':'OUTWARD_SEPARATED_PASS','all_saved_json':'PARSED','statement_digest':digest})
write(R/'out/PERSISTENCE_RECEIPTS.json',old)
for entry in old['artifacts']+old['rolling']:
 p=Path(entry['path']);assert receipt(p)==entry
print(json.dumps({'status':'FINAL_SAVED_HASHES_PASS','assertions':61177,'artifacts':len(items),'main_seconds':v['seconds'],'independent_review':'PENDING','full_FEI':'OPEN'}))
