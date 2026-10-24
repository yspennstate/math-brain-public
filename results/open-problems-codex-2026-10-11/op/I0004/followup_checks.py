import pathlib,json,math,time
from fractions import Fraction as F
ROOT=pathlib.Path(__file__).resolve().parent
def convergents(ds):
 p0,p1,q0,q1=0,1,1,0;out=[]
 for a in ds:
  p0,p1=p1,a*p1+p0;q0,q1=q1,a*q1+q0;out.append((p1,q1))
 return out
def check_family(name,a1,spikes,separators):
 ds=[0,a1,separators[0]]
 for i,A in enumerate(spikes):ds.extend([A,separators[i+1]])
 ds.extend([1000003,2,1000033]);conv=convergents(ds);P,R=conv[-1]
 towers=[(m,conv[2*m][0],conv[2*m][1],spikes[m-1],conv[2*m+1][1],conv[2*m+2][1]) for m in range(1,len(spikes)+1)]
 cap=2000000;towers=[t for t in towers if t[-1]<=cap];N=max(t[-1] for t in towers)
 C=[0]*(N+1);moments={};points=set()
 for m,p,q,A,qp,qn in towers:points.update([q,qn,(qn//q)*q])
 w=w2=0
 for n in range(1,N+1):
  C[n]=C[n-1]+(1 if 2*((n*P)%R)<R else -1)
  w+=C[n];w2+=C[n]*C[n]
  if n in points:moments[n]=n*w2-w*w
 results=[];bound=max(separators);T=2*bound+1;E=8*T+4;kappa=F(1,1048576*T*T)
 for m,p,q,A,qp,qn in towers:
  assert q%2==1
  assert abs(P*q-p*R)*qp<R
  J=qn//q;K=A//8;Nfull=J*q
  B=F(moments[q],q*q);Bnext=F(moments[qn],qn*qn)
  H=[C[j*q] for j in range(J)]
  VH=F(J*sum(h*h for h in H)-sum(H)**2,J*J)
  assert VH>=kappa*A*A
  error_sum=error_square=0;max_error=max_changed=0
  for j in range(J):
   changed=0
   for r in range(1,q+1):
    y=j*q+r;err=C[y]-C[r]-H[j]
    error_sum+=err;error_square+=err*err;max_error=max(max_error,abs(err))
    changed+=int((C[y]-C[y-1])!=(C[r]-C[r-1]))
   max_changed=max(max_changed,changed)
  assert max_changed<=4*T+2
  assert max_error<=E
  VZ=F(Nfull*error_square-error_sum*error_sum,Nfull*Nfull)
  VX=F(moments[Nfull],Nfull*Nfull)
  VY=B+VH
  assert VZ<=E*E
  assert VX>=F(A-1,A)*VY-(A-1)*VZ
  assert F(Nfull*Nfull,qn*qn)>=F(A-1,A)
  assert Bnext>=F(A-2,A)*B+F(1,2)*kappa*A*A-E*E*A
  for j in range(K):assert H[j]==j*(1 if P*q-p*R>0 else -1)
  # Monotonic scatter and the inherited-variance part of the all-scale estimate.
  Bfloat=float(B);L=K*q
  for n in [q,min(2*q,L),L,qn]:
   s=n*sum(x*x for x in C[1:n+1])-sum(C[1:n+1])**2
   if n<=L:assert 256*(n*n+s)>=n*n*(1+B)
   else:assert 1048576*T*T*(n*n+s)>=n*n*(1+B+A*A)
  results.append({'m':m,'q':q,'A':A,'next_q':qn,'J':J,'max_changed_letters':max_changed,'max_profile_error':max_error,'old_variance':float(B),'new_variance':float(Bnext),'offset_variance':float(VH),'error_variance':float(VZ),'scaled_variance_inequality':'exact pass','transfer_recursion':'exact pass'})
 return {'name':name,'a1':a1,'spikes':spikes,'separators':separators,'N':N,'towers':results}
start=time.monotonic()
families=[check_family('linear_gap',1,[33,34,35],[2,2,2,2]),check_family('variable_even_separators',1,[32,33],[4,6,4]),check_family('nonmonotone_spikes',3,[96,32],[2,4,2])]
algebra_cases=0
for A in range(1,65):
 for u in range(-8,9):
  for v in range(-8,9):
   assert A*(u+v)**2-(A-1)*u*u+A*(A-1)*v*v==(u+A*v)**2
   algebra_cases+=1
barriers=0
for k in [1,2,4,10]:
 for m in range(1,201):
  for t in range(m+1):
   assert m*((t+1)**3-t**3)+k*t**3<=(k+12)*m**3
   barriers+=1
out={'families':families,'scaled_square_cases':algebra_cases,'integer_cubic_barrier_cases':barriers,'seconds':time.monotonic()-start,'note':'Exact modular integer coding and rational variance checks. Finite checks support but do not replace FOLLOWUP.md proofs; huge eventual thresholds are not tested numerically.'}
(ROOT/'followup_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2));print('FOLLOWUP_EXACT_CHECKS_PASS')
