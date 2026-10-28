from fractions import Fraction as F
from math import comb
from pathlib import Path
import json,hashlib,time
RUN=Path(__file__).resolve().parents[1];OUT=RUN/'out';OUT.mkdir(exist_ok=True)
def save(n,o):(OUT/n).write_text(json.dumps(o,indent=2,default=str)+'\n',encoding='utf-8')
def C(v):return {(0,0):F(v)} if v else {}
def add(*ps):
 d={}
 for p in ps:
  for k,v in p.items():d[k]=d.get(k,F(0))+v
 return {k:v for k,v in d.items() if v}
def neg(p):return {k:-v for k,v in p.items()}
def mul(*ps):
 d=C(1)
 for p in ps:
  n={}
  for (i,j),v in d.items():
   for (a,b),w in p.items():n[i+a,j+b]=n.get((i+a,j+b),F(0))+v*w
  d={k:v for k,v in n.items() if v}
 return d
def power(p,k):return mul(*([p]*k))
u={(1,0):F(1)};k={(0,1):F(1)};one=C(1)
D=add(one,neg(mul(C(4),k,u)),mul(C(4),k,power(u,2)))
z=power(add(one,neg(mul(C(2),u))),2)
omk=add(one,neg(k));h2=mul(power(u,2),power(omk,2))
twoD=mul(C(2),D);den2=add(twoD,h2);slope=add(one,mul(C(6),u))
P=add(mul(z,k,slope,den2),mul(twoD,omk,slope),neg(mul(C(8),D,u,den2)))
def transform(p,x0,x1,y0,y1):
 q={}
 for (i,j),v in p.items():
  for a in range(i+1):
   for b in range(j+1):
    w=v*comb(i,a)*x0**(i-a)*(x1-x0)**a*comb(j,b)*y0**(j-b)*(y1-y0)**b
    q[a,b]=q.get((a,b),F(0))+w
 return q
def bernstein(p,box):
 q=transform(p,*box);n=max(i for i,j in p);m=max(j for i,j in p)
 return [[sum((q.get((a,b),F(0))*F(comb(i,a),comb(n,a))*F(comb(j,b),comb(m,b)) for a in range(i+1) for b in range(j+1)),F(0)) for j in range(m+1)] for i in range(n+1)]
def evaluate(p,x,y):return sum((v*x**i*y**j for (i,j),v in p.items()),F(0))
if __name__=='__main__':
 start=time.monotonic();boxes=[(F(i,16),F(i+1,16),F(j,8),F(j+1,8)) for i in range(4) for j in range(4)]
 save('POLYNOMIAL_FROZEN.json',{'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'actual_family':'products of width>=2 point signs, any physical data prefix, x exposure, restricted-factor reset','continuum_domain':'0<=u<=1/4,0<=k<=1/2; physical u>0,k=original defect/current defect','boxes':boxes,'case_count':16,'symmetry':'none','arithmetic':'Fraction polynomial power and Bernstein coefficients','memory_MB':20,'max_runtime_seconds':55})
 rows=[]
 for box in boxes:
  bs=bernstein(P,box);lo=min(v for row in bs for v in row)
  rows.append({'box':box,'minimum':lo,'coefficients':bs})
 minimum=min(r['minimum'] for r in rows)
 save('POLYNOMIAL_CERTIFICATE.json',{'power_coefficients':{str(k):v for k,v in P.items()},'degree':[max(i for i,j in P),max(j for i,j in P)],'boxes':rows,'minimum':minimum,'status':'PASS' if minimum>0 else 'UNRESOLVED','bit_credit_coefficient':8*minimum/165,'runtime_seconds':time.monotonic()-start})
 assert minimum>0,minimum
 # One explicit width3->width2 nonempty-profile change: independent integer sign.
 num=79*21*80**3;den=20*81**4
 assert num<den and 2*num**64<den**64
 save('INTEGER_SIGN.json',{'reset_bits':'(1/4)log2(num/den)','num':num,'den':den,'certified_margin':'reset < -1/256 bits','comparison':'2*num^64 < den^64','difference':den**64-2*num**64})
 print(json.dumps({'status':'PASS','boxes':16,'degree':[max(i for i,j in P),max(j for i,j in P)],'minimum':str(minimum),'bit_credit_coefficient':str(8*minimum/165),'integer_margin':'<-1/256','runtime_seconds':time.monotonic()-start}))
