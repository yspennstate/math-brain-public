from pathlib import Path
from fractions import Fraction as F
import importlib.util,hashlib,json,time,sys,collections
R=Path(__file__).resolve().parents[1]
old=R.parents[1]/'runs/20261014T074949Z-account05-A011-representation-existence/code/shared.py'
spec=importlib.util.spec_from_file_location('shared',old);s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)
(R/'out/HELPER_PROVENANCE.json').write_text(json.dumps({'path':str(old),'sha256':hashlib.sha256(old.read_bytes()).hexdigest()},indent=2),encoding='utf-8')
start=time.monotonic();mode=sys.argv[1];cases=roots=0;maxdim=0
labels3=[1,3,7,15,23,27,30,60,85,90,105,126,127,150,170,254]
domain=[(a,bits) for a in [1,2] for bits in range(1,2**(2**a)-1)] if mode=='pilot' else [(3,bits) for bits in labels3[int(mode)*4:(int(mode)+1)*4]]
def ck(x):s.ck(x)
def plus(A,B):return A[0]+B[0],A[1]+B[1]
def mul(k,A):return k*A[0],k*A[1]
def cec(P,Q):
 # Exact grouping of equal reference values reduces interval work.
 agg=collections.defaultdict(F)
 for p,q in zip(P,Q):
  if p:ck(q>0);agg[q]+=p
 lo=hi=F(0)
 for q,p in agg.items():
  x,y=s.log(1/q);lo+=p*x;hi+=p*y
 return lo,hi
def state(g,a,b,r,Rsrc):
 n=a+b;N=2**n;p=F(1,2**r);t=F(1,N);beta=6*p*t
 vals=[g[y%(2**a)]-2*g[0]*(x==0 and y==0) for x in range(2**r) for y in range(N)]
 coeff=s.fw(vals);P=[x*x for x in coeff];q=[sum(P[u*N+T] for u in range(2**r)) for T in range(N)]
 rep=[((Rsrc[T] if T<2**a else 0)+beta*t)/(1+beta) for T in range(N)]
 Q=[rep[T]*P[u*N+T]/q[T] for u in range(2**r) for T in range(N)]
 ck(sum(P)==1);ck(sum(Q)==(sum(Rsrc)+beta)/(1+beta))
 for T in range(N):
  aa=s.fw(g)[T] if T<2**a else 0
  ck(q[T]==aa*aa-4*p*t*g[0]*aa+4*p*t*t)
 return {'P':P,'Q':Q,'H':cec(P,P),'CE':cec(P,Q),'I':sum(s.inf(vals)),'vals':vals,'mass':sum(Q)}
for a,bits in domain:
 g=[1 if bits>>y&1 else -1 for y in range(2**a)];Pg=[x*x for x in s.fw(g)];Ig=sum(s.inf(g));Hg=cec(Pg,Pg)
 ck(Ig>=F(2*a,2**a));d=sum(g[0]!=g[1<<j] for j in range(a))
 for b in [1,2,3]:
  for r in [1,2]:
   p=F(1,2**r);t=F(1,2**(a+b));C=2*p*t*(a+b-d);E=2*p*t*d;J=2*r*p*t
   for model,Rsrc in [('P',Pg),('halfP',[x/2 for x in Pg]),('U',[F(1,2**a)]*(2**a))]:
    c=cec(Pg,Rsrc);root=state(g,a,b,r,Rsrc);ck(root['I']==Ig+C-E+J);ck(E<=Ig/4);ck(root['I']>=3*Ig/4)
    ck(root['CE'][1]<=2*c[0]+15*(C+E+J)+F(1,2**80))
    querysum=(F(0),F(0));prior=root;priorbill=root['CE'];resets=(F(0),F(0))
    for ell in range(1,b+1):
     j=ell-1;w=F(1,2**j);child=state(g,a,b-ell,r,Rsrc)
     dq=F(1,2)*s.inf(prior['vals'])[a] # overwritten below with exact physical probability
     dq=s.inf(prior['vals'])[a]
     ck(dq==2*p*(2**j)*t)
     Delta=s.sub(prior['H'],s.avg(Hg,child['H']))
     # Boundary / query inequality certified with a conservative elementary JS bound.
     hb=cec([dq,1-dq],[dq,1-dq]);ln2lo=s.log(F(2))[0] # log2(2)=1; natural ln bound is analytic, use rational9
     ck(Delta[1]<=dq*(a+b+r-j+8))
     querysum=plus(querysum,mul(w,Delta))
     leafbill=plus(mul(1-F(1,2**ell),c),mul(F(1,2**ell),child['CE']))
     L=plus(querysum,leafbill)
     Dprior=s.sub(prior['CE'],prior['H']);Dg=s.sub(c,Hg);Dchild=s.sub(child['CE'],child['H'])
     lam=s.sub(s.avg(Dg,Dchild),Dprior);resets=plus(resets,mul(w,lam))
     ck(abs((root['CE'][0]+resets[0])-L[0])<F(1,2**75))
     ck(abs((root['CE'][1]+resets[1])-L[1])<F(1,2**75))
     # The analytic certificate is rational; take C0=c_upper/Ig.
     C0=c[1]/Ig;K=4*C0+15;T=15*(a+b+r-ell)+ell*(a+b+r+8)-F(ell*(ell-1),2)
     ck(2*p*t*T<=F(41,4)*Ig)
     ck(L[1] <= (1+F(1,2**ell))*c[1]+2*p*t*T)
     ck(L[1] <= F(3,2)*c[1]+F(41,4)*Ig)
     ck(K*root['I']-L[1] >= (F(3,2)*C0+1)*Ig)
     ck(root['mass']==(sum(Rsrc)+6*p*t)/(1+6*p*t))
     ck(child['mass']==(sum(Rsrc)+6*p*t*(2**ell))/(1+6*p*t*(2**ell)))
     ck(len(set(child['vals']))==2);ck(len(set(g))==2)
     cases+=1;prior=child
     if time.monotonic()-start>55:raise RuntimeError('55 second frozen cutoff; incomplete')
    roots+=1;maxdim=max(maxdim,a+b+r)
out={'status':'PASS','mode':mode,'labelled_cores':len(domain),'root_reference_cases':roots,'prefix_reference_cases':cases,'exact_assertions':s.checks,'max_dimension':maxdim,'seconds':time.monotonic()-start,'arithmetic':'Fractions and outward rational logarithm bounds; no numerical sign claims'}
(R/f'out/CHECK_{mode}.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
