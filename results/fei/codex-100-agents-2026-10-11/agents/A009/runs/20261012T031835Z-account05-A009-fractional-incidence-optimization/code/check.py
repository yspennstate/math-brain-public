from pathlib import Path
from fractions import Fraction as F
from functools import cache
from math import prod
import time,json
RUN=Path(__file__).resolve().parents[1]
(RUN/'out').mkdir(exist_ok=True)
if (RUN/'out'/'CHECK.json').exists() and not (RUN/'out'/'PILOT_SLOW.json').exists():
 (RUN/'out'/'PILOT_SLOW.json').write_bytes((RUN/'out'/'CHECK.json').read_bytes())
start=time.perf_counter(); count=0
def ck(x):
 global count
 assert x
 count+=1

@cache
def log_bounds(x):
 x=F(x); ck(x>0); power=0
 while x>=2: x/=2; power+=1
 while x<1: x*=2; power-=1
 def ln(z):
  z=(z-1)/(z+1); L=36
  low=sum((2*z**(2*i+1)/F(2*i+1) for i in range(L)),F(0))
  error=2*z**(2*L+1)/(F(2*L+1)*(1-z*z))
  return low,low+error
 a,b=ln(x); c,d=ln(F(2))
 a,b=(a+power*c,b+power*d) if power>=0 else (a+power*d,b+power*c)
 vals=[a/c,a/d,b/c,b/d]
 return min(vals),max(vals)

def walsh(vals):
 vals=list(vals); step=1
 while step<len(vals):
  for i in range(0,len(vals),2*step):
   for j in range(i,i+step):
    a,b=vals[j],vals[j+step]; vals[j],vals[j+step]=a+b,a-b
  step*=2
 return vals

def geometry(q):
 points=[(x,y) for x in range(q) for y in range(q)]
 lines=[tuple(i for i,(x,y) in enumerate(points) if x==b) for b in range(q)]
 lines += [tuple(i for i,(x,y) in enumerate(points) if y==(a*x+b)%q) for a in range(q) for b in range(q)]
 ck(len(set(lines))==q*(q+1)); ck(all(len(l)==q for l in lines))
 for i in range(q*q): ck(sum(i in l for l in lines)==q+1)
 for i,l in enumerate(lines):
  for ll in lines[i+1:]: ck(len(set(l)&set(ll))<=1)
 return lines

def forest(A,lines):
 # One-root witness when A is contained in a line; otherwise a globally fixed
 # first-incidence ownership rule and deterministic source-SCC spanning forest.
 containing=[l for l,line in enumerate(lines) if set(A)<=set(line)]
 if containing:
  l=containing[0]; own={l:tuple(A)}
 else:
  own={}
  for j in A:
   l=next(l for l,line in enumerate(lines) if j in line)
   own.setdefault(l,[]).append(j)
  own={l:tuple(v) for l,v in own.items()}
 used=sorted(own)
 adj={l:[k for k in used if k!=l and set(own[l])&set(lines[k])] for l in used}
 reach={l:{l} for l in used}
 for l in used:
  todo=[l]
  while todo:
   z=todo.pop()
   for k in adj[z]:
    if k not in reach[l]:reach[l].add(k);todo.append(k)
 components=[]; unseen=set(used)
 while unseen:
  l=min(unseen); comp={k for k in unseen if k in reach[l] and l in reach[k]}
  components.append(comp);unseen-=comp
 roots=[]
 for comp in components:
  incoming=any(k in adj[l] for l in used if l not in comp for k in comp)
  if not incoming: roots.append(min(comp))
 roots.sort(); seen=set(roots); queue=list(roots); edges=[]
 for l in queue:
  fresh=[]
  for k in adj[l]:
   if k not in seen:
    j=min(set(own[l])&set(lines[k]));fresh.append((j,k));seen.add(k)
  # The fixed generator orders attachment occurrences numerically. Queue
  # order therefore follows attachment slots before child-gate labels.
  for j,k in sorted(fresh):edges.append((l,k,j));queue.append(k)
 ck(seen==set(used));ck(len(edges)+len(roots)==len(used))
 ck(set().union(*(set(v) for v in own.values()))==set(A))
 ck(sum(len(v) for v in own.values())==len(A))
 # A trace fixes initial sorted roots and all subsequent child lists in order.
 children={l:[] for l in used}
 for l,k,j in edges:children[l].append((j,k))
 for l in used:ck(children[l]==sorted(children[l]))
 trace=(tuple(roots),tuple((l,own[l],tuple(children[l])) for l in queue))
 ck(len(queue)==len(set(queue)))
 return own,roots,trace,bool(containing)

families=[]
for q in [2,3]:
 n=q*q; lines=geometry(q); N=len(lines); masks=[sum(1<<j for j in l) for l in lines]
 vals=[]; ideal=[]
 for x in range(1<<n):
  K=sum((x&mask)==mask for mask in masks)
  vals.append(1 if K else -1);ideal.append(2*K-1)
 fw=walsh(vals); gw=walsh(ideal); denom=1<<n
 P=[F(z*z,denom*denom) for z in fw]
 E2=F(sum((a-b)**2 for a,b in zip(vals,ideal)),denom)
 ck(E2==F(sum((a-b)**2 for a,b in zip(fw,gw)),denom*denom))
 ck(E2<=8*N*N*F(1,2**(2*q)))
 ck(sum(P)==1)
 I=sum(F(a.bit_count())*p for a,p in enumerate(P))
 Iphys=F(sum(vals[x]!=vals[x^(1<<j)] for x in range(1<<n) for j in range(n)),1<<n)
 ck(I==Iphys);v=1-P[0]
 lam=F(1,q+1);pi=F(1,2**q); D=(1+lam*pi)**N-1
 for j in range(n):ck(sum(lam for l in lines if j in l)==1)
 Rlo,Rhi=[z*v for z in log_bounds(D)]
 Bterms={};traces=[];off_mass=F(0)
 for mask,p in enumerate(P):
  if mask==0 or not p:continue
  A=[j for j in range(n) if mask>>j&1]
  own,roots,trace,contained=forest(A,lines)
  traces.append({'A':mask,'roots':roots,'trace':trace,'contained':contained})
  terms=[(F(len(own)),F(q+1)),(F(len(roots)),F(2**q))]
  for l,subset in own.items():
   kappa=len(set(A)&set(lines[l]));s=len(subset)
   terms.append((F(6*s,5),F(kappa,s)))
   for j in subset:
    rank=lines[l].index(j)+1
    pred=sum(z in A for z in lines[l][:rank-1])+1
    terms.append((F(6,5),F(rank,pred)))
  for coeff,x in terms:
   Bterms[str(x)]=Bterms.get(str(x),F(0))+p*coeff
  containing=sum(set(A)<=set(l) for l in lines)
  ck(F(gw[mask],denom)==((-1)**len(A))*2*pi*containing)
  if not contained:
   ck(gw[mask]==0);off_mass+=p
 ck(off_mass<=E2)
 for x,coeff in Bterms.items():
  lo,hi=log_bounds(F(x));Rlo+=coeff*lo;Rhi+=coeff*hi
 families.append({'q':q,'I':str(I),'v':str(v),'D':str(D),'error_L2_squared':str(E2),'off_line_spectral_mass':str(off_mass),'R_lower':str(Rlo),'R_upper':str(Rhi),'B_expected_log_coefficients':{x:str(c) for x,c in Bterms.items()},'witness_count':len(traces),'ratio_upper_display':float(Rhi/I)})
 (RUN/'out'/('TRACES_q'+str(q)+'.json')).write_text(json.dumps(traces,indent=2),encoding='utf-8')

# Exact endpoint for the infinite-family proof: all polynomial/2^q bills
# decrease after q=16; no Boolean cube is enumerated at these scalar values.
scalar=[]
for q in [16,17,32,64,128,256]:
 k=q+1;N=q*k;delta=F(1,2**q);eps=2*N*delta
 ck(eps<F(1,2))
 ck(F(q+1,q)**4<2)
 ck(F(17,16)<F(7,6));ck(F(7,6)**4<2)
 ck(F(5,8*q)+F(3,10)<F(1,2))
 ck(F(153,80)<2)
 bound=(F(49,5)+F(37,5)*N*delta+8*N*(q+2*q*q)*delta)/(2*(1-eps))
 ck(bound<14)
 scalar.append({'q':q,'epsilon':str(eps),'R_over_I_majorant':str(bound),'R_over_I_display':float(bound),'less_than_14':True})
q=16;k=q+1;N=q*k;delta=F(1,2**q);eps=2*N*delta
endpoint=(F(49,5)+F(37,5)*N*delta+8*N*(q+2*q*q)*delta)/(2*(1-eps))
ck(endpoint==F(186791,13540)); ck(14-endpoint==F(2769,13540))
out={'helper_version':'A009-affine-forest-v1.1-aggregated-logs','assertions':count,'runtime_seconds':time.perf_counter()-start,'status':'PASS','exact_families':families,'analytic_scalar_certificates':scalar,'endpoint_majorant':str(endpoint),'endpoint_margin_to_14':str(14-endpoint),'scope':'Full deterministic actual-forest residual; all-q proof is analytic, not finite extrapolation'}
(RUN/'out'/'CHECK.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'assertions':count,'runtime_seconds':out['runtime_seconds'],'status':'PASS','finite_ratios':[x['ratio_upper_display'] for x in families],'endpoint':str(endpoint)}))
