# Appended to A070's own exact arithmetic primitives; no A069 code is imported.
from itertools import product
def joint(a,b,m,k,theta,eps):
 n=(len(a)-1).bit_length();N=2**m;M=N//2**k;t=F(1,N*N)
 A=(1+3*t*theta)/4;B=5*(1-t*theta)/16;r=7*(1-t*theta)/(32*(N-1))
 a0=A+(2**k-1)*r;b0=B+(2**k-1)*r;w=2**k*r
 qc=[a0,b0]+[w]*(2*M-2)
 core=[F(j+1,len(a)*(len(a)+1)//2) for j in range(len(a))]
 v=[]
 for x in range(len(a)*2*M):
  y=x%len(a);z=x//len(a);c=z&1
  p=F(a[y]+b[y],2);q=F(a[y]-b[y],2)
  v.append((-1 if z==0 else 1)*(eps*p+(-1)**c*q))
 ref=[core[s%len(a)]*qc[s//len(a)] for s in range(len(v))]
 return v,ref,core,qc
cases=private=core_queries=correlated=0;rows=[]
families=[]
for n in [1,2]:
 funcs=list(product([-1,1],repeat=2**n))
 for a,b in product(funcs,repeat=2):
  for m,theta,eps in (product(range(1,4),[F(0),F(1,3),F(1)],[-1,1]) if n==1 else [(1,F(1,3),1)]):
   cases+=1
   for k in range(m):
    v,ref,cr,qc=joint(a,b,m,k,theta,eps);N=len(a);M=2**(m-k);eta=F(1,M)
    ck(all(abs(x)==1 for x in v));ck(sum(ref)==1)
    ps=spectrum(v);d=F(sum(x!=y for x,y in zip(a,b)),N)
    cm=[sum(ps[j*N:(j+1)*N]) for j in range(2*M)]
    expected=[(1-d)*(1-eta)**2+d*eta**2,d*(1-eta)**2+(1-d)*eta**2]+[eta**2]*(2*M-2)
    ck(cm==expected);ck(sum(ps)==1);ck(inf(v,n+1)==eta)
    dc=decrement(v,ref,n+1)
    formula=plus(times(log(1+qc[2]/qc[0]),cm[0]),times(log(1+qc[2]/qc[1]),cm[1]),times(log((1+qc[0]/qc[2])*(1+qc[1]/qc[2])),eta**2),{2:2*(M-2)*eta**2})
    ck(dc==formula);ck(interval(dc)[1]<4*eta);private+=1
    pa,pb=spectrum(a),spectrum(b);pc=[(x+y)/2 for x,y in zip(pa,pb)]
    ck([sum(ps[j*N+s] for j in range(2*M)) for s in range(N)]==pc)
    if any(ps[j*N+s]!=cm[j]*pc[s] for j in range(2*M) for s in range(N)):correlated+=1
    for bit in range(n):
     aa=children(a,bit);bb=children(b,bit);rm=marginal(cr,bit)
     childcost=[]
     for av,bv in zip(aa,bb):childcost.append(ce([(x+y)/2 for x,y in zip(spectrum(av),spectrum(bv))],rm))
     db=plus(ce(pc,cr),times(plus(*childcost),-F(1,2)))
     ck(decrement(v,ref,bit)==db)
     ck(inf(v,bit)==(inf(a,bit)+inf(b,bit))/2)
     core_queries+=1
ck(cases==544);ck(private==832);ck(core_queries==1088);ck(correlated>0)
# Complete old references before u; physical control transforms independently checked.
early=[]
for m,d in product(range(1,7),[F(0),F(1,256)]):
 rho=F(1,2**m);t=rho*rho;alpha=1-t*d;Q=[]
 for s in range(2**(m+2)):
  if s==0:q=t*d
  elif s<4:q=alpha*{1:F(1,4),2:F(1,4),3:F(1,16)}[s]
  else:q=alpha*(F(7,80) if s&2 else F(7,20))/(2*(2**m-1))
  Q.append(q)
 f0=[];f1=[]
 for x in range(len(Q)):
  c=x&1;u=(x>>1)&1;z=x>>2;q=-1 if c==0 and z==0 else 1
  f0.append(q*(-1)**u);f1.append(q*(-1)**c)
 dc=times(decrement(f0,Q,1),1-d)
 if d:dc=plus(dc,times(decrement(f1,Q,1),d))
 x=d*t
 u0=plus(times(log(5),2*rho-t),times(log((1+3*x)/(1-x)),(1-rho)**2))
 expected=times(u0,1-d)
 if d:expected=plus(expected,times(log((1+3*x)/(4*x)),d*t),times(log(F(5,4)),d*(1-t)))
 ck(dc==expected);ck(interval(dc)[1]<F(485,256));ck(interval(dc)[1]<4*(1-d))
 early.append(dict(m=m,d=str(d),decrement_interval=[str(v) for v in interval(dc)]))
# Actual source first core children, no numerical approximation to disagreement.
def maj(xs):return 1 if sum(xs)>0 else -1
a=[maj([maj([(-1)**((y>>j)&1) for j in range(k,k+3)]) for k in [0,3,6]]) for y in range(512)]
b=a.copy();b[0]*=-1
for branch,expected in [(0,F(1,256)),(1,F(0))]:
 av=children(a,0)[branch];bv=children(b,0)[branch]
 ck(F(sum(x!=y for x,y in zip(av,bv)),256)==expected)
# Source's positive unresolved-core c exit retains two NONCONSTANT children.
v,ref,cr,qc=joint([-1,1],[-1,1],2,0,F(0),1)
v=children(v,2)[1];ref=marginal(ref,2)
bill=decrement(v,ref,1);ck(bill==log(F(68,31)));ck(inf(v,1)==0);ck(interval(bill)[0]>1)
ck(all(sum(inf(w,i) for i in range((len(w)-1).bit_length()))==1 for w in children(v,1)))
# Frozen-theta first-three residual-width bounds, covering the entire rectangle.
for l in [1,2,3]:
 M=2**l;e=F(1,M);L=F(8*(M-1),7);U=1+F(10*M,7)
 V=plus(times(log(1+1/L),1-2*e+2*e*e),times(log(1+U),2*e*e),{2:2*(M-2)*e*e})
 ck(interval(V)[1]<4*e)
ck(F(4887,1280)<4);ck(F(485,256)<4*F(255,256))
ck(F(5,8)-F(3,5)-F(1,512)==F(59,2560))
result=dict(status='PASS',assertions=checks,root_pair_cases=cases,private_prefix_cases=private,core_invoice_identities=core_queries,correlated_joint_examples=correlated,early_u_cases=len(early),unresolved_exit_bill_interval=[str(v) for v in interval(bill)],elapsed_seconds=time.perf_counter()-start,memory_estimate_mb=64)
(R/'out/CHECK.json').write_bytes((json.dumps(result,indent=2)+'\n').encode('utf-8'))
(R/'out/EARLY_U.json').write_bytes((json.dumps(early,indent=2)+'\n').encode('utf-8'))
print(json.dumps(result))
