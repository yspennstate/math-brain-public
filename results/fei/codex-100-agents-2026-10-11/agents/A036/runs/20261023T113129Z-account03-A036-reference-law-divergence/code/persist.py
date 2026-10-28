from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys
sys.set_int_max_str_digits(200000)
R=Path(__file__).resolve().parents[1];A=R.parents[1];N=0
def ck(v):
 global N
 N+=1;assert v,N
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
p=json.loads(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'));schema={}
def walk(j):
 if isinstance(j,dict):
  for k,v in j.items():
   if k in ['report_fields','claim_fields','progress_fields']:schema[k]=v
   else:walk(v)
walk(p)
claims=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'));ck(len(claims)==2)
for c in claims:ck(set(c)==set(schema['claim_fields']));ck(c['statement_sha256']==hashlib.sha256(c['exact_statement'].encode()).hexdigest());ck(Path(c['proof_source']).exists());ck(c['status']=='ANALYTIC_PROOF_EXACT_CHECKS_REVIEW_PENDING')
keys=set('packet_ids' if k.startswith('packet_ids') else k for k in schema['progress_fields'])
for name in ['PROGRESS.json','PACKET_DELTA.json']:
 j=json.loads((R/name).read_text(encoding='utf-8'));ck(set(j)==keys);ck(j['packet_ids']==['A036']);ck(j['run_id']==R.name)
ck((R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes());report=(R/'REPORT.md').read_text(encoding='utf-8')
for h in schema['report_fields']:ck('# '+h+'\n' in report)
ck(report.strip().split('\n')[-1].startswith('Universal bridge:'));status=(A/'STATUS.md').read_text(encoding='utf-8').splitlines();ck(len(status)==2);ck(status[0].startswith('STATE: '));ck(status[1].startswith('NEXT: '))
for x in json.loads((R/'out/SOURCES.json').read_text(encoding='utf-8')):ck(sha(Path(x['path']))==x['sha256'])
for x in json.loads((R/'out/MANIFEST.json').read_text(encoding='utf-8')):ck(sha(R/x['path'])==x['sha256']);ck((R/x['path']).stat().st_size==x['bytes'])
summary=json.loads((R/'out/VALIDATION_SUMMARY.json').read_text(encoding='utf-8'));ck(summary['executed_assertions_in_PASS_receipts']==172303)
for x in summary['receipts']:ck(x['status']=='PASS');ck(x.get('cases',1)>0);ck(x['seconds']<(240 if x['file']=='SCALAR.json' else 55))
ck(len((R/'out/SCALAR_PROGRESS.jsonl').read_text(encoding='utf-8').splitlines())==60)
audit=json.loads((R/'out/INDEPENDENT_CERTIFICATE.json').read_text(encoding='utf-8'));ratio=F(1)
for g in audit['likelihood_groups']:ratio*=F(g['ratio'])**g['exponent']
ck(ratio==F(int(audit['product_numerator']),int(audit['product_denominator'])));ck(ratio>1);D=audit['denominator_D'];ck(D==8192)
# Independently consume the actual source/inherited/fresh atomic certificate.
atomratio=F(1)
for row in audit['atoms']:
 p=list(map(F,row['source']));old=list(map(F,row['inherited']));new=list(map(F,row['fresh']));ck(sum(p)==sum(old)==sum(new)==1);ck(all((a==0)==(b==0) for a,b in zip(p,new)))
 for a,b,c in zip(p,old,new):
  if a:
   power=a*D/2;ck(power.denominator==1);atomratio*=(b/c)**int(power)
ck(atomratio==ratio)
# A third route compares the exact closed formula with the atomic rational product.
d=F(1,32);e=d*d;alpha=F(1,6);formula=F(1)
for c in [1,-1]:
 ac=(1-2*c*d+2*e)/4;power=D*ac;ck(power.denominator==1);formula*=(1-alpha*e/(4*ac))**int(power)
rr=F(8192,3125)*(1+49*e)**5/((1+80*e)**4*(1+16*e));eta=alpha*(F(3,10)-F(4,5)*e-e*(1+2*e)/(2*(1+4*e*e)));ck((D*e).denominator==1);formula*=rr**int(D*e);formula/=(1-eta*eta)**(D//2);ck(formula==ratio)
files=[p for p in R.rglob('*') if p.is_file()]
for p in files:ck(p.stat().st_size<20*1024*1024)
receipt={'status':'PASS','assertions':N,'files_checked':len(files),'claims':2,'atomic_and_grouped_and_closed_formula_rational_products_identical':True,'max_file_bytes':max(p.stat().st_size for p in files),'review':'INDEPENDENT_EXTERNAL_PENDING','full_FEI':'OPEN','stopped':0,'research_jobs_running':0}
(R/'out/PERSISTENCE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print(json.dumps(receipt))
