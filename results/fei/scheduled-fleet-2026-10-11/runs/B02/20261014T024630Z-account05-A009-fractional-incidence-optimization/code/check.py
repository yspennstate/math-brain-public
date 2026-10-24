import itertools, math, time, json, sys
from pathlib import Path
from fractions import Fraction as R
import numpy as np
from scipy.optimize import minimize, nnls

ROOT=Path(__file__).resolve().parents[1]; DEN=10**8; checks=0
def ck(x):
 global checks
 assert x
 checks+=1
def scc_matchings(A,edges):
 es=[e for e in edges if set(e)<=set(A)]
 for bits in range(1<<len(es)):
  M=tuple(e for k,e in enumerate(es) if bits>>k&1); used=[j for e in M for j in e]
  if len(set(used))!=len(used): continue
  U=tuple(j for j in A if j not in used)
  if any(e[0] in U and e[1] in U for e in es): continue
  yield M,U
def spectrum(n,edges):
 vals=[1 if any((b>>u&1) and (b>>v&1) for u,v in edges) else -1 for b in range(1<<n)]
 w=vals[:]; d=1
 while d<len(w):
  for j in range(0,len(w),2*d):
   for k in range(j,j+d): w[k],w[k+d]=w[k]+w[k+d],w[k]-w[k+d]
  d*=2
 ck(sum(x*x for x in w)==4**n)
 I=R(sum(vals[b]!=vals[b^(1<<j)] for b in range(1<<n) for j in range(n)),1<<n)
 P={b:R(w[b]**2,4**n) for b in range(1,1<<n) if w[b]}
 ck(sum(P[b]*b.bit_count() for b in P)==I)
 return P,I
def occupation(n,edges,b,lam):
 A=tuple(j for j in range(n) if b>>j&1); total=R(0); counts=[R(0)]*len(edges); trace_polynomial={}
 index={e:k for k,e in enumerate(edges)}
 for M,U in scc_matchings(A,edges):
  matched={j for e in M for j in e}; neighbors=[tuple(v for e in edges if u in e for v in e if v!=u) for u in U]
  for nu in itertools.product(*neighbors):
   chosen=tuple(tuple(sorted((u,v))) for u,v in zip(U,nu)); used=M+chosen
   ck(len(set(used))==len(used)); ck(len(used)==len(A)-len(M))
   h={j:0 for j in matched}; k=R(1,24**len(M)*8**len(U))
   for v in nu:
    if v in matched: h[v]+=1
    else: ck(v not in A); k/=4
   for u,v in M:
    c=h[u]+h[v]; k*=R(math.factorial(h[u])*math.factorial(h[v]),(c+1)**2*(c+2))
   mask=sum(1<<index[e] for e in used)
   trace_polynomial[mask]=trace_polynomial.get(mask,R(0))+k
   mass=k*math.prod(lam[index[e]] for e in used)
   total+=mass
   for e in used: counts[index[e]]+=mass
 ck(total>0)
 ck(sum(counts)>=total); ck(sum(counts)<=len(A)*total)
 ck(total==sum(k*math.prod(lam[e] for e in range(len(edges)) if mask>>e&1) for mask,k in trace_polynomial.items()))
 return total,counts,trace_polynomial
def Dval(lam): return math.prod(1+x/4 for x in lam)-1
def lnunit(x):
 z=(x-1)/(x+1); zz=z*z; power=z; total=R(0)
 for k in range(20): total+=power/(2*k+1); power*=zz
 return 2*total,2*total+2*power/(41*(1-zz))
LN2=lnunit(R(2))
def logint(x):
 shift=0
 while x>=2: x/=2; shift+=1
 while x<1: x*=2; shift-=1
 lo,hi=lnunit(x)
 return R(shift)+lo/LN2[1],R(shift)+hi/LN2[0]
def convex_proposal(edges,n,v,c,base):
 inc=np.array([[float(j in e) for e in edges] for j in range(n)])
 cf=np.array([float(x) for x in c]); vf=float(v)
 def obj(t):
  lam=np.exp(t); h=np.log1p(lam/4).sum(); Z=-np.expm1(-h)
  return vf*(h+np.log(Z))-cf@t
 def grad(t):
  lam=np.exp(t); h=np.log1p(lam/4).sum(); Z=-np.expm1(-h)
  return vf*(lam/(4+lam))/Z-cf
 result=minimize(obj,np.log([float(x) for x in base]),jac=grad,method='SLSQP',bounds=[(-30.,0.)]*len(edges),constraints=[{'type':'ineq','fun':lambda t:1-inc@np.exp(t),'jac':lambda t:-inc*np.exp(t)}],options={'maxiter':1000,'ftol':1e-13})
 raw=np.exp(result.x); scale=max(1.,max(inc@raw)); raw/=scale
 lam=[R(max(1,math.floor(float(x)*DEN)),DEN) for x in raw]
 ck(all(sum(lam[k] for k,e in enumerate(edges) if j in e)<=1 for j in range(n)))
 D=Dval(lam); root=[(x/(4+x))*(D+1)/D for x in lam]
 target=np.array([float(c[k]-v*root[k]) for k in range(len(edges))])
 active=[j for j in range(n) if 1-float(sum(lam[k] for k,e in enumerate(edges) if j in e))<1e-6]
 matrix=np.array([[float(lam[k]) if j in e else 0. for j in active] for k,e in enumerate(edges)])
 yf=np.zeros(n)
 if active:
  ys,_=nnls(matrix,target)
  for j,y in zip(active,ys): yf[j]=y
 prices=[R(max(0,round(float(y)*DEN))+1,DEN) for y in yf]
 return lam,prices,{'numeric_success':bool(result.success),'iterations':int(result.nit),'message':str(result.message)}
def certify(edges,n,v,c,lam,y):
 D=Dval(lam); root=[x/(4+x)*(D+1)/D for x in lam]; C=sum(c)
 ck(C>=v); ck(C>0)
 delta=R(0)
 for k in range(len(edges)):
  if c[k]<v*root[k]:
   denominator=v*(root[k]-c[k]/C); ck(denominator>0)
   delta=max(delta,(v*root[k]-c[k])/denominator)
 ck(0<=delta<=1)
 r=[(1-delta)*root[k]+delta*c[k]/C for k in range(len(edges))]
 b=[c[k]-v*r[k] for k in range(len(edges))]; ck(all(x>=0 for x in b))
 chi=sum((c[k]/C)**2*4*D/lam[k] for k in range(len(edges)))-1; ck(chi>=0)
 rootgap=v*delta**2*chi
 slack=sum(y[j]*(1-sum(lam[k] for k,e in enumerate(edges) if j in e)) for j in range(n)); ck(slack>=0)
 phigap=R(0)
 for k,(u,w) in enumerate(edges):
  z=lam[k]*(y[u]+y[w]); ck(z>0)
  phigap+=(b[k]-z)**2/z
 gap=2*(rootgap+slack+phigap)
 return gap,{'lambda':[str(x) for x in lam],'coordinate_prices':[str(x) for x in y],'c':[str(x) for x in c],'v':str(v),'D':str(D),'root_marginals':[str(x) for x in root],'mixture_delta':str(delta),'b':[str(x) for x in b],'root_chi_square':str(chi),'natural_root_gap_bound':str(rootgap),'natural_slack':str(slack),'natural_edge_gap_bound':str(phigap),'bit_gap_upper':str(gap)}
def case(n,edges,name):
 P,I=spectrum(n,edges); v=sum(P.values()); degree=max(sum(j in e for e in edges) for j in range(n)); base=[R(1,degree)]*len(edges); D0=Dval(base)
 W={}; polynomials={}; c=[R(0)]*len(edges); fullmass=R(0)
 for b in range(1,1<<n):
  if any((b>>j&1) and not any(j in e for e in edges) for j in range(n)): continue
  mass,counts,poly=occupation(n,edges,b,base); fullmass+=mass/D0
  if b in P:
   W[b]=mass; polynomials[b]={str(k):str(x) for k,x in poly.items()}
   for k in range(len(edges)): c[k]+=P[b]*counts[k]/mass
 ck(fullmass<=1); ck(v<=sum(c)<=I); ck(I/2<=sum(c))
 lam,y,discovery=convex_proposal(edges,n,v,c,base)
 gap,cert=certify(edges,n,v,c,lam,y)
 basecostlo=R(0); basecosthi=R(0)
 for b,mass in W.items():
  lo,hi=logint(D0/mass); basecostlo+=P[b]*lo; basecosthi+=P[b]*hi
 lo,hi=logint(Dval(lam)/D0); costlo=basecostlo+v*lo; costhi=basecosthi+v*hi
 for k in range(len(edges)):
  lo,hi=logint(lam[k]/base[k]); costlo-=c[k]*hi; costhi-=c[k]*lo
 ck(costlo<=costhi)
 cert.update({'name':name,'n':n,'edges':edges,'I':str(I),'base_lambda':[str(x) for x in base],'P':{str(b):str(x) for b,x in P.items()},'W_base':{str(b):str(x) for b,x in W.items()},'occupation_coefficients':polynomials,'base_cost_interval':[str(basecostlo),str(basecosthi)],'frozen_cost_interval':[str(costlo),str(costhi)],'frozen_global_lower':str(costlo-gap),'gap_over_I_upper':str(gap/I),'target_gap_pass':gap<=I/1000,'cost_over_I_display':float(costhi/I),'gap_over_I_display':float(gap/I),'proposal_only':discovery})
 return cert
def run(pilot):
 start=time.perf_counter(); cases=[]; n=3 if pilot else 4; possible=list(itertools.combinations(range(n),2))
 inputs=[(n,tuple(e for k,e in enumerate(possible) if mask>>k&1),f'graph-{n}-{mask}') for mask in range(1,1<<len(possible))]
 if not pilot:
  inputs += [(5,tuple(sorted(E)),name) for name,E in [('cycle5',[(0,1),(1,2),(2,3),(3,4),(0,4)]),('path5',[(0,1),(1,2),(2,3),(3,4)]),('star5',[(0,j) for j in range(1,5)]),('clique5',list(itertools.combinations(range(5),2))),('triangle-two-leaves',[(0,1),(1,2),(0,2),(0,3),(1,4)])]]
 for n,edges,name in inputs:
  cert=case(n,edges,name); cases.append(cert)
  (ROOT/'out'/'PARTIAL.json').write_text(json.dumps(cases,indent=2),encoding='utf-8')
 passed=sum(c['target_gap_pass'] for c in cases)
 summary={'helper_version':'A009-complete-star-weight-gap-v1','functions':len(cases),'checks':checks,'elapsed_seconds':time.perf_counter()-start,'gap_target_passed':passed,'all_gap_targets_passed':passed==len(cases),'maximum_gap_over_I_display':max(c['gap_over_I_display'] for c in cases),'maximum_frozen_cost_over_I_display':max(c['cost_over_I_display'] for c in cases),'all_exact_checks_passed':True}
 (ROOT/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps({'summary':summary,'certificates':cases},indent=2),encoding='utf-8')
 print(json.dumps(summary))
if __name__=='__main__':
 sys.set_int_max_str_digits(0)
 run('--pilot' in sys.argv)
