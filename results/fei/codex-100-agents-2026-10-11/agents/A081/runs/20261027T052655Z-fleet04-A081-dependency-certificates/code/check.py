from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib
R=Path(__file__).resolve().parents[1]
count=0
def ck(x):
 global count
 count+=1
 if not x:raise AssertionError(count)
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def fw(v):
 v=list(v);h=1
 while h<len(v):
  for j in range(0,len(v),2*h):
   for k in range(j,j+h):v[k],v[k+h]=v[k]+v[k+h],v[k]-v[k+h]
  h*=2
 return [F(x,len(v)) for x in v]
def plus(*xs):
 d={}
 for x in xs:
  for p,a in x.items():d[p]=d.get(p,F(0))+a
 return {p:a for p,a in d.items() if a}
def scale(a,x):return {p:a*c for p,c in x.items() if a*c}
def logq(q):
 assert q>0
 d={}
 for z,sg in [(q.numerator,1),(q.denominator,-1)]:
  p=2
  while p*p<=z:
   while z%p==0:d[p]=d.get(p,0)+sg;z//=p
   p+=1
  if z>1:d[z]=d.get(z,0)+sg
 return {p:F(a) for p,a in d.items() if a}
def div(P,Q):return plus(*(scale(p,logq(p/q)) for p,q in zip(P,Q) if p))
def main():
 start=time.perf_counter();cases=0;ghosts=0
 for n in range(4):
  size=1<<n
  for table in range(1<<size):
   values=[1 if table>>x&1 else -1 for x in range(size)]
   A=fw(values);P=[a*a for a in A]
   ck(sum(P)==1)
   for i in range(n):
    old=[t for t in range(size) if not t>>i&1]
    for mass in [F(1),F(1,2)]:
     for mixed in [False,True]:
      Q=[mass*((p+F(1,size))/2 if mixed else p) for p in P]
      m=[P[t]+P[t|1<<i] for t in old];r=[Q[t]+Q[t|1<<i] for t in old]
      Pc=[[(A[t]+sg*A[t|1<<i])**2 for t in old] for sg in [1,-1]]
      raw=[[rr*p/mm if mm else rr for p,mm,rr in zip(pc,m,r)] for pc in Pc]
      Z=[sum(q) for q in raw];ck(sum(Z)/2==mass);ck(min(Z)>0)
      Qi=[[mass*q/z for q in rawb] for z,rawb in zip(Z,raw)]
      conditional=plus(*(scale(P[t],logq((P[t]/m[j])/(Q[t]/r[j]))) for j,t in enumerate(old) if P[t]),*(scale(P[t|1<<i],logq((P[t|1<<i]/m[j])/(Q[t|1<<i]/r[j]))) for j,t in enumerate(old) if P[t|1<<i]))
      contraction=plus(div(P,Q),scale(F(-1,2),plus(*(div(pc,qi) for pc,qi in zip(Pc,Qi)))))
      rhs=plus(conditional,scale(F(-1,2),logq(Z[0]*Z[1]/mass**2)))
      ck(contraction==rhs);ck(Z[0]*Z[1]<=mass**2)
      if not mixed:ck(contraction=={});ck(Z==[mass,mass])
      if any(mm==0 and rr>0 for mm,rr in zip(m,r)):ghosts+=1
      # One full split and arbitrary actual signed reset: exact ledger telescope.
      Qnew=[[mass*(p+F(1,len(pc)))/2 for p in pc] for pc in Pc]
      reset=scale(F(1,2),plus(*(plus(div(pc,qn),scale(-1,div(pc,qi))) for pc,qn,qi in zip(Pc,Qnew,Qi))))
      terminal=scale(F(1,2),plus(*(div(pc,qn) for pc,qn in zip(Pc,Qnew))))
      ck(plus(div(P,Q),reset)==plus(contraction,terminal))
      cases+=1
 # Independent literal permitted-family witness, b12: all 16384 target values.
 b=12;n=b+1;sz=1<<n;e=F(1,sz)
 values=[-1 if x&1 else 1 for x in range(2*sz)];values[0]=-values[0]
 A=fw(values);zlit=F(0)
 for t in range(sz):
  old=F(int(t==1));m=A[t]**2+A[t+sz]**2
  ck(m==(old-e)**2+e*e)
  r=(old*old+3*e*e)/(1+3*e)
  zlit+=r*old*old/m
 ck(zlit==(1+3*e*e)/((1+3*e)*(1-2*e+2*e*e)))
 witness=[]
 for b in range(12,65):
  e=F(1,1<<(1+b));den=(1+3*e)*(1-2*e+2*e*e);num=1+3*e*e
  ck(den-num==e*(1-e)*(1-6*e));ck(den>num>0)
  z=num/den;ze=2-z
  ck(0<z<1<ze<2);ck(1-z*ze==(1-z)**2>0)
  witness.append({'b':b,'epsilon':str(e),'Zclean':str(z),'Zedit':str(ze),'normalizer_product':str(z*ze)})
 # v6 conditional owner-margin coefficients, independent of physical root proof.
 c=4*F(4081,4096)-F(135,92)-1
 k=15*F(4081,4096)-320*F(151,8192)-F(37,8)
 ck(c==F(35751,23552));ck(k==F(18111,4096));ck(c>0 and k>0)
 ck(time.perf_counter()-start<55)
 result={'status':'PASS','assertions':count,'one_query_reset_profiles':cases,'ghost_profiles':ghosts,'truth_tables':278,'literal_b12_target_values':16384,'literal_b12_data_fibers':8192,'witness_b_range':[12,64],'witnesses':53,'margin_coefficients':[str(c),str(k)],'seconds':time.perf_counter()-start,'arithmetic':'Fraction and exact prime-log linear forms','scope':'one-query identity replay plus literal actual-family witness, all-b factorization and affine coefficient algebra; NOT full v6 root-envelope review','formal_rung':'exact finite certificate with analytic general telescope; not Lean-certified','FEI':'OPEN'}
 save(R/'out/EXACT_CERTIFICATE.json',result);save(R/'out/WITNESSES.json',witness)
 print(json.dumps(result))
if __name__=='__main__':main()
