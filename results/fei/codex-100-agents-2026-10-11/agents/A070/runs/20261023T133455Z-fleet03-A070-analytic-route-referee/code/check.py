from pathlib import Path
import itertools, json, math, time
import primitives as E
from primitives import F,plus,times,log,interval,ce,spectrum,inf,marginal,children,ck
R=Path(__file__).resolve().parents[1]
started=time.perf_counter()
def pos(x):
 if not x:return {}
 a,b=interval(x)
 ck(a>0 or b<0)
 return x if a>0 else {}
def nonnegative(x):
 ck(not x or interval(x)[0]>=0)
def pairp(a,b):return [(u+v)/2 for u,v in zip(spectrum(a),spectrum(b))]
def tree(a,b,q,i=0):
 B=ce(pairp(a,b),q)
 if len(a)==1:
  ck(B=={});return {},{}, {},F(0)
 ac,bc=children(a,i),children(b,i);qc=marginal(q,i)
 D=plus(B,times(plus(*(ce(pairp(x,y),qc) for x,y in zip(ac,bc))),-F(1,2)))
 nonnegative(D)
 j=(inf(a,i)+inf(b,i))/2
 v=pos(plus(D,{2:-4*j}));paid=plus(D,times(v,-1))
 vv,aa,dd,jj=v,paid,D,j
 for x,y in zip(ac,bc):
  w,z,d,k=tree(x,y,qc)
  vv=plus(vv,times(w,F(1,2)));aa=plus(aa,times(z,F(1,2)))
  dd=plus(dd,times(d,F(1,2)));jj+=k/2
 ck(plus(vv,aa)==B)
 return vv,aa,dd,jj
funcs=list(itertools.product([-1,1],repeat=4))
cases=0
for a in funcs:
 for b in funcs:
  J=sum((inf(a,i)+inf(b,i))/2 for i in range(2))
  for q in [[F(1,4)]*4,[F(x,16) for x in [1,2,4,9]],pairp(a,b)]:
   B=ce(pairp(a,b),q);vs=[]
   for i in [0,1]:
    V,A,D,j=tree(a,b,q,i);ck(D==B);ck(j==J)
    nonnegative(A);nonnegative(plus({2:4*J},times(A,-1)))
    nonnegative(plus(B,times(V,-1)));nonnegative(plus(V,{2:4*J},times(B,-1)))
    vs.append(V);cases+=1
   nonnegative(plus({2:4*J},vs[0],times(vs[1],-1)))
   nonnegative(plus({2:4*J},vs[1],times(vs[0],-1)))
sharp=[]
for k in [1,2,4,8]:
 e=F(1,2**k);q=[e/16,F(1,16),(15-2*e)/16,e/16];a=[1,-1,1,-1]
 x=tree(a,a,q,0)[0];z=tree(a,a,q,1)[0];ell=log(1+e)
 ck(x==plus({2:F(4)},times(ell,-1)));ck(z==ell)
 if k>=2:ck(interval(z)[1]<F(5,8)<interval(x)[0])
 sharp.append({'k':k,'x_first':str(interval(x)),'z_first':str(interval(z))})
# A normalized real root; homogeneous physical children versus artificial renormalization.
g=[F(2+(1 if not (s&1) else -1)+2*(1 if not (s&2) else -1),3) for s in range(4)]
p=spectrum(g);ck(p==[F(4,9),F(1,9),F(4,9),0]);ck(sum(p)==1)
ch=children(g,0);cp=[spectrum(v) for v in ch]
ck(cp==[[F(1),F(4,9)],[F(1,9),F(4,9)]])
norm=[sum(v) for v in cp];cn=[[v/z for v in w] for w,z in zip(cp,norm)]
ck(cn==[[F(9,13),F(4,13)],[F(1,5),F(4,5)]])
mean=[(u+v)/2 for u,v in zip(*cn)]
ck(mean==[F(29,65),F(36,65)]);ck(marginal(p,0)==[F(5,9),F(4,9)])
q0=F(1,4096);q=[4*(1-q0)/5,(1-q0)/5,q0/2,q0/2];qc=marginal(q,0)
dh=plus(ce(p,q),times(plus(*(ce(v,qc) for v in cp)),-F(1,2)))
dn=plus(ce(p,q),times(plus(*(ce(v,qc) for v in cn)),-F(1,2)))
h=ce([F(1,5),F(4,5)],[F(1,5),F(4,5)])
ck(dh==plus(times(h,F(5,9)),{2:F(4,9)}))
ck(dn==plus(dh,times(log(q0/(1-q0)),F(64,585))))
ck(interval(dh)[0]>0);ck(interval(dn)[1]<0)
real={'function_values':list(map(str,g)),'homogeneous_decrement':str(interval(dh)),
 'normalized_child_decrement':str(interval(dn)),'erased_root':list(map(str,marginal(p,0))),
 'mean_normalized_children':list(map(str,mean))}
# Homogeneous degree-one extension. Prefix states are exact binomial aggregates.
degree=[];states=0
for n in [2,4,8,16,32,64]:
 Dsum={};V={};J=F(0)
 for d in range(n):
  for t in range(d+1):
   s=2*t-d;w=F(math.comb(d,t),2**d);states+=1
   D={} if d==0 else plus(times(log(F(d+1,d)),F(s*s,n)),times(log(d+1),F(1,n)))
   nonnegative(D)
   Dsum=plus(Dsum,times(D,w));V=plus(V,times(pos(plus(D,{2:-F(4,n)})),w));J+=w/n
 ck(Dsum==log(n));ck(J==1)
 nonnegative(plus(V,{2:F(4)},times(log(n),-1)))
 nonnegative(plus(log(n),times(V,-1)))
 degree.append({'n':n,'V_interval':str(interval(V)),'H':str(interval(log(n))),'J':'1'})
result={'status':'PASS','boolean_cases':cases,'boolean_functions':16,'sharpness':sharp,
 'real_normalization':real,'degree_one':degree,'degree_one_states':states,
 'exact_assertions':E.checks,'elapsed_seconds':time.perf_counter()-started,
 'scope':'Independent finite certificates and analytic proof audit; no universal FEI closure.'}
(R/'out/results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
