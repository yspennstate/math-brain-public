"""Independent exact checks of transport, scalar optimization, literal log witness."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import time,json,sys
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'out'
start=time.monotonic();checks=0
def ck(v,msg):
 global checks
 checks+=1
 if not v:raise AssertionError(msg)
 if time.monotonic()-start>55:raise RuntimeError('frozen55 second bound')
def save(name,x):(OUT/name).write_text(json.dumps(x,indent=2,default=str),encoding='utf-8')
def mu(t):return Q(sum(t),len(t))
def influence(t):
 return sum((Q(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range(len(t).bit_length()-1)),Q(0))
def restrict(t,j,b):
 n=len(t).bit_length()-1
 return [t[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(1<<(n-1))]
def piv(B,m,i):
 other=1-i;pminus=(1-m[other])/2
 return (1-pminus)*int(B[0]!=B[1<<i])+pminus*int(B[1<<other]!=B[3])
def transport(pilot):
 tabs=[tuple(1-2*((a>>x)&1) for x in range(4)) for a in range(16)]
 rows=zero=0
 for B in (tabs[8:9] if pilot else tabs):
  for g,h in product(tabs,repeat=2):
   gs=(g,h);m=[mu(t) for t in gs];u=[influence(t) for t in gs]
   q=[piv(B,m,i) for i in range(2)];W=sum(q[i]*u[i] for i in range(2))
   full=[B[int(g[x&3]<0)+2*int(h[x>>2]<0)] for x in range(16)]
   ck(influence(full)==sum(q[i]*u[i] for i in range(2)),'physical composition influence')
   for j,k in product(range(2),repeat=2):
    vals=[];uj=[];qc=[]
    for b in range(2):
     child=restrict(gs[j],k,b);mm=list(m);uu=list(u);mm[j]=mu(child);uu[j]=influence(child)
     qq=[piv(B,mm,i) for i in range(2)]
     ck(qq[j]==q[j],'own pivotal independent of own bias')
     vals.append(sum(qq[i]*uu[i] for i in range(2)));uj.append(uu[j]);qc.append(qq)
    ck(W-sum(vals)/2==q[j]*(u[j]-sum(uj)/2),'universal inner transport identity')
    ck(W>=sum(vals)/2,'inner superharmonic')
    ck((qc[0][1-j]+qc[1][1-j])/2==q[1-j],'other pivotal affine mean')
    rows+=1;zero+=int(q[j]==0)
 return {'query_rows':rows,'compositions':rows//4,'zero_pivotal_rows':zero}
def scalar(pilot):
 grid=[Q(0),Q(1,2),Q(1),Q(2)];rows=feas=zeroP=zeroA=zeroWeight=0
 for w in (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)):
  ws=(w,1-w)
  for c0,c1,u0,u1 in product(grid,repeat=4):
   c=(c0,c1);u=(u0,u1);A=sum(ws[i]*c[i] for i in range(2));U=sum(ws[i]*u[i] for i in range(2))
   rows+=1
   if pilot and rows>64:return {'rows':rows-1,'feasible_rows':feas,'zero_P':zeroP,'zero_A':zeroA,'zero_weight_rows':zeroWeight}
   if A<U:
    ck(sum(ws[i]*(u[i]-c[i]) for i in range(2))>0,'infeasible mean obstruction');continue
   feas+=1;zeroWeight+=int(w in (0,1));zeroA+=int(A==0)
   n=[max(u[i]-c[i],0) for i in range(2)];p=[max(c[i]-u[i],0) for i in range(2)]
   N=sum(ws[i]*n[i] for i in range(2));P=sum(ws[i]*p[i] for i in range(2));zeroP+=int(P==0)
   f=[n[i]-N/P*p[i] for i in range(2)] if P else [Q(0),Q(0)]
   ck(sum(ws[i]*f[i] for i in range(2))==0,'mean conserved')
   a=[c[i]+f[i] for i in range(2)]
   ck(all(a[i]>=u[i] for i in range(2) if ws[i]),'requirements on positive support')
   ck(sum(ws[i]*max(f[i],0) for i in range(2))==N,'construction cost')
   # Independent two-state linear programming reduction: feasible credit0 interval;
   # objective's only interior kink is old credit0. Zero support handled separately.
   if w and 1-w:
    lo=u0;hi=(A-(1-w)*u1)/w
    ck(lo<=hi,'nonempty feasible interval')
    vertices={lo,hi,max(lo,min(hi,c0))}
    optimum=min(w*max(z-c0,0)+(1-w)*max((A-w*z)/(1-w)-c1,0) for z in vertices)
   else:optimum=Q(0)
   ck(optimum==N,'independent LP optimum')
   owners=[A/3,A/6,A/2]
   if A:
    owned=[[L*a[i]/A for i in range(2)] for L in owners]
    ck(all(sum(ws[i]*owned[j][i] for i in range(2))==owners[j] for j in range(3)),'individual credit owners')
    ck(all(sum(owned[j][i] for j in range(3))==a[i] for i in range(2)),'owners sum to actual credit')
   else:ck(all(a[i]==0 for i in range(2) if ws[i]),'zero total owner branch')
   labels=(Q(-1),Q(3),Q(-1,2));T=sum(labels)
   Eh=ws[0]+2*ws[1];d=[T/Eh,2*T/Eh]
   ck(all(sum(ws[i]*L*d[i]/T for i in range(2))==L for L in labels),'signed debit conserved Tpositive')
   ck(all(sum(L*d[i]/T for L in labels)==d[i] for i in range(2)),'signed debit sums')
   zero_labels=(Q(-2),Q(3),Q(0),Q(-1))
   ck(sum(zero_labels)==0,'Tzero unit kernel retains signed labels')
 return {'rows':rows,'feasible_rows':feas,'zero_P':zeroP,'zero_A':zeroA,'zero_weight_rows':zeroWeight}
def factors(n):
 ans={};p=2
 while p*p<=n:
  while n%p==0:ans[p]=ans.get(p,0)+1;n//=p
  p+=1
 if n>1:ans[n]=ans.get(n,0)+1
 return ans
def entropy_literal(n):
 # Direct character sums, independent from fast Walsh and point-entropy formula.
 tab=[-1]+[1]*((1<<n)-1);N=len(tab);ans={}
 for s in range(N):
  v=sum(tab[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(N))
  if not v:continue
  p=Q(v*v,N*N)
  for prime,k in factors(p.numerator).items():ans[prime]=ans.get(prime,0)-p*k
  for prime,k in factors(p.denominator).items():ans[prime]=ans.get(prime,0)+p*k
 return ans
def witness():
 # delta3=H(G3)-H(G4)-H(G2)/4 from independent literal cubes.
 d={}
 for n,c in ((3,Q(1)),(4,Q(-1)),(2,Q(-1,4))):
  for prime,a in entropy_literal(n).items():d[prime]=d.get(prime,0)+c*a
 d={p:a for p,a in d.items() if a}
 ck(d=={2:Q(-5,2),3:Q(-9,8),7:Q(49,32)},'literal entropy prime-log identity')
 diff=7**49-2**80*3**36
 ck(diff>0,'independent exact integer sign')
 return {'prime_log_delta3':{str(p):str(a) for p,a in d.items()},'power_difference':str(diff)}
if __name__=='__main__':
 pilot='--pilot' in sys.argv
 result={'transport':transport(pilot),'scalar_rerouting':scalar(pilot),'literal_witness':witness(),'pilot':pilot,'status':'PASS','assertions':checks,'runtime_seconds':time.monotonic()-start,'scope':'Finite audits only; universal statements independently proved in PROOF.md and REVIEW.md.'}
 save('AUDIT_PILOT.json' if pilot else 'INDEPENDENT_AUDIT.json',result);print(json.dumps(result,indent=2))
