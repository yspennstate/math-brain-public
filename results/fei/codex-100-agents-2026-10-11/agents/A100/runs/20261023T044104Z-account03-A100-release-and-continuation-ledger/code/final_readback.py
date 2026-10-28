from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,time
R=Path(__file__).resolve().parents[1];O=R/'out';A=R.parent.parent;start=time.perf_counter()
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x):p.write_bytes((json.dumps(x,indent=2)+'\n').encode())
# Freeze this final fixed-domain audit before computation; no additional Boolean cases.
save(O/'FROZEN_FINAL_AUDIT_SPEC.json',{'helper_version':'A100-independent-final-readback-v1','family':'Same single w4,m0,d0,eta0 witness; no new search','case_count':1,'arithmetic':'Fraction and exact integer signs; byte SHA256 comparison','memory_estimate_MB':40,'max_runtime_seconds':55,'scope':'Independent calibrated-total integer certificate from saved exact probability classes, source-statement preservation and all local payload readback'})
x=load(O/'POSITIVE_RETURN_REVIEW.json');ratio=F(1);profile=F(1);z=F(49,64)
for c in x['classes']:
 p,q,r=F(c['P']),F(c['oldQ']),F(c['freshQ']);count=c['count'];exp=p*64*count;assert exp.denominator==1
 if p==z:
  calibrated=z
 else:
  calibrated=(1-z)*r/(1-F(63,128));profile*=((q/(1-F(18375,33856)))/(r/(1-F(63,128))))**count
 ratio*=(q/calibrated)**int(exp)
assert ratio<1;assert profile==F(975,959)**7*F(130,137)**8<1
assert profile==F(int(x['profile_ratio_numerator']),int(x['profile_ratio_denominator']))
save(O/'VACUUM_CALIBRATED_CERTIFICATE.json',{'status':'PASS','domain':'Same fixed A094 Boolean witness; probabilities independently collected from exact class receipt','calibrated_total_reached_charge':'log2(calibrated_ratio)/512 < 0','calibrated_ratio_numerator':str(ratio.numerator),'calibrated_ratio_denominator':str(ratio.denominator),'strict_numerator_less_denominator':True,'profile_ratio_equals_simplified_independent_expression':True,'profile_strictly_negative':True,'assertions':5,'independent_axis':'Direct integer total-charge sign, separate from REVIEW analytic Bernoulli-KL plus profile decomposition','new_general_theorem':'None'})
m=load(O/'PERSISTENCE_RECEIPTS.json');oldn=len(m['files'])
for f in m['files']:
 b=Path(f['path']).read_bytes();assert len(b)==f['bytes'] and hashlib.sha256(b).hexdigest()==f['sha256'],f['path']
for f in m['rolling_snapshot']:
 b=Path(f['path']).read_bytes();assert len(b)==f['bytes'] and hashlib.sha256(b).hexdigest()==f['sha256'],f['path']
for f in load(O/'ADDITIONAL_SOURCE_RECEIPTS.json'):
 b=Path(f['path']).read_bytes();assert len(b)==f['bytes'] and hashlib.sha256(b).hexdigest()==f['sha256'],f['path']
# Include final independent helper/spec/certificate in the updated immutable manifest.
files=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name not in ['PERSISTENCE_RECEIPTS.json','FINAL_READBACK.json'] and '__pycache__' not in p.parts:
  b=p.read_bytes();assert len(b)<20_000_000;files.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
m['files']=files;m['local_readback']='PASS';m['independent_final_readback']='out/FINAL_READBACK.json';save(O/'PERSISTENCE_RECEIPTS.json',m)
for f in files:
 b=Path(f['path']).read_bytes();assert len(b)==f['bytes'] and hashlib.sha256(b).hexdigest()==f['sha256']
protocol=load(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'));prog=load(R/'PROGRESS.json');cs=load(R/'CLAIMS.json')
assert set(prog)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']};assert prog['packet_ids']==['A100']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes();assert all(set(c)==set(protocol['required_per_run']['claim_fields']) for c in cs)
report=(R/'REPORT.md').read_text();assert all('## '+h+'\n' in report for h in protocol['required_per_run']['report_fields']);assert report.rstrip().split('## ')[-1].startswith('Universal bridge\n')
assert len(load(O/'NEXT_TEN_QUESTIONS.json'))==10;assert len((A/'STATUS.md').read_text().splitlines())==2
assert not cs[1]['review_records'];assert cs[0]['review_records'][-1]['reviewer']=='A100/account03/B20'
source=next(c for c in load(Path(load(O/'CRITICAL_SOURCE_RUNS.json')['A094'])/'CLAIMS.json') if c['claim_id']==cs[0]['claim_id'])
for k in ['claim_id','version','exact_statement','hypotheses','statement_sha256']:assert cs[0][k]==source[k]
assert time.perf_counter()-start<55
result={'status':'PASS','at_utc':datetime.now(timezone.utc).isoformat(),'original_current_payloads_checked':oldn,'final_current_payloads_rehashed':len(files),'rolling_snapshots_checked':3,'additional_source_receipts_checked':len(load(O/'ADDITIONAL_SOURCE_RECEIPTS.json')),'prior_immutable_original_hash_comparison':load(O/'PREVIOUS_RECEIPT_VERIFICATION.json')['immutable_payloads_compared_against_previous_saved_hashes'],'new_calibrated_total_integer_certificate':'PASS','new_corollary_independent_review':'PENDING','full_FEI':'OPEN','remote_adoption_mirror_public':'UNVERIFIED','brain_selfcare':'DEGRADED/UNVERIFIED: owner-model/state-of-mind stale; personalization continuity affected','runtime_seconds':round(time.perf_counter()-start,6)};save(O/'FINAL_READBACK.json',result);print(json.dumps(result,indent=2))
