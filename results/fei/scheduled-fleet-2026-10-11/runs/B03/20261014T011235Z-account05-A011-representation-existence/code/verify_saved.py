import pathlib,json,hashlib,datetime
R=pathlib.Path(__file__).resolve().parents[1]; A=R.parents[1]
def digest(p):
 b=p.read_bytes();return {'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
manifest=json.loads((R/'out/PERSISTENCE_RECEIPTS.json').read_text())
for item in manifest['artifacts']+manifest['rolling']:
 p=pathlib.Path(item['path']);assert digest(p)==item
claims=json.loads((R/'CLAIMS.json').read_text())
for claim in claims:
 h=hashlib.sha256(json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
 assert h==claim['statement_sha256']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
out=json.loads((R/'out/EXACT_RESULTS.json').read_text())
assert out['status']=='PASS' and out['exact_assertions']==847665
assert out['helper']==digest(R/'code/check_point_edit.py')
review=json.loads((R/'REVIEW_DELTA.json').read_text())
assert review['review_records'][0]['verdict']=='HOLDS_AT_STATED_SCOPE'
certificate=json.loads((R/'out/EXACT_bent.json').read_text())['neutral_countercertificate'][0]
from fractions import Fraction as F
assert F(certificate['data_increment'])==0
assert F(certificate['true_H_minus_m_interval'][0])>8*F(certificate['selector_I'])
assert len((A/'STATUS.md').read_text().splitlines())==2
report=(R/'REPORT.md').read_text()
assert '847,665' in report and '\n\n' not in report.rsplit('## Universal bridge',1)[1].strip()
result={'status':'PASS','prior_artifact_hashes':'ALL_MATCH','canonical_claim_hash':'MATCH','compatibility':'BYTE_EQUAL','complete_job_total':847665,'neutral_K8_countercertificate':'STRICT_RATIONAL_POSITIVE','prior_phase_review':'A086_HOLDS_CONSUMED','new_claim_review':'PENDING','full_FEI':'OPEN'}
(R/'out/FINAL_ARTIFACT_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
manifest['at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
manifest['final_artifact_check']='PASS'
manifest['artifacts']=[digest(p) for p in sorted(R.rglob('*')) if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']
assert all(p['bytes']<20_000_000 for p in manifest['artifacts'])
(R/'out/PERSISTENCE_RECEIPTS.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
