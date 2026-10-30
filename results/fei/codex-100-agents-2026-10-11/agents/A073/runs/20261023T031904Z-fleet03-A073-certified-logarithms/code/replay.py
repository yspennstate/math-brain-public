from fractions import Fraction as F
from pathlib import Path
from math import comb
import json,hashlib,time
R=Path(__file__).resolve().parents[1];O=R/'out';O.mkdir(exist_ok=True)
old=R.parent/'20261023T025235Z-fleet03-A073-certified-logarithms'
def save(n,d):(O/n).write_text(json.dumps(d,indent=2,default=str)+'\n',encoding='utf-8')
start=time.monotonic();src=old/'out/POLYNOMIAL_CERTIFICATE.json'
save('REPLAY_FROZEN.json',{'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'certificate_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'family':'stage18 rational polynomial sign and actual width4 sequential-reset example','domain':'16 boxes, degree(5,3), interpolation grid6x4 perbox','case_count':384,'symmetry':'none','arithmetic':'Fraction Bernstein-basis evaluation vs independent unexpanded expression; integer products','memory_MB':25,'max_runtime_seconds':55})
cert=json.loads(src.read_text(encoding='utf-8'));minimum=F(cert['minimum']);checks=0
for row in cert['boxes']:
 x0,x1,y0,y1=map(F,row['box']);bs=[[F(v) for v in a] for a in row['coefficients']]
 assert min(v for a in bs for v in a)>=minimum>0
 for i in range(6):
  for j in range(4):
   t=F(i,5);s=F(j,3);u=x0+(x1-x0)*t;k=y0+(y1-y0)*s
   D=1-4*k*u+4*k*u*u;z=(1-2*u)**2;h2=u*u*(1-k)**2
   direct=z*k*(1+6*u)*(2*D+h2)+2*D*(1-k)*(1+6*u)-8*D*u*(2*D+h2)
   b=sum((bs[a][b]*comb(5,a)*t**a*(1-t)**(5-a)*comb(3,b)*s**b*(1-s)**(3-b) for a in range(6) for b in range(4)),F(0))
   assert b==direct;checks+=1
# Width4 followed by two actual sequential on-observations. The source child
# has the uniform four-atom spectrum; use the exact reference from the failed
# cumulative-erasure witness, not the invalid predicted reference.
num=3941*3500**2*5375*65536;den=245*16316**4
assert num<den
assert 2*num**128<den**128
save('INTEGER_SEQUENTIAL_SIGN.json',{'num':num,'den':den,'reset_bits':'(1/4)log2(num/den)','certified_margin':'reset < -1/512 bits','comparison':'2*num^128 < den^128','positive_integer_difference':den**128-2*num**128})
save('REPLAY.json',{'status':'PASS','coefficient_identity_checks':checks,'minimum':minimum,'explicit_sequential_margin':'<-1/512 bits','runtime_seconds':time.monotonic()-start,'scope':'Independent representation in same agent; not independent-agent acceptance'})
print(json.dumps({'status':'PASS','identities':checks,'minimum':str(minimum),'integer_sequential_margin':'<-1/512','runtime_seconds':time.monotonic()-start}))
