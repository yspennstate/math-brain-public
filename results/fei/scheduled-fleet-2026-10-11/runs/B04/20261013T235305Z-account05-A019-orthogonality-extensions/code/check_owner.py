import json,time,hashlib,sys
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
R=Path(__file__).resolve().parents[1];pilot='--pilot' in sys.argv
spec={'helper_version':'A019-folded-owner-v1','family':'Boolean modules f_j(z,y_j) with one shared separator and disjoint private blocks; no balance hypothesis','domain':'pilot all256 ordered one-private-bit pairs; full also all4096 ordered two/one-private-bit pairs and all4096 ordered one-private-bit triples; sharp parity family r=1..32 in closed form','case_count':256 if pilot else 8448,'symmetry':'none; character folding checked rather than quotiented','arithmetic':'integer Walsh, Fraction physical influences and exact cross-energy; rational log intervals for entropy boundary','memory_estimate_MB':60,'maximum_runtime_seconds':60 if pilot else 120}
(R/('out/OWNER_PILOT_SPEC.json' if pilot else 'out/OWNER_SPEC.json')).write_text(json.dumps(spec,indent=2))
started=time.monotonic();checks=0;cases=0
def ck(t):
 global checks
 checks+=1;assert t
def fw(t):
 a=t[:];s=1
 while s<len(a):
  for i in range(0,len(a),2*s):
   for j in range(i,i+s):a[j],a[j+s]=a[j]+a[j+s],a[j]-a[j+s]
  s*=2
 return tuple(Q(z,len(t)) for z in a)
def infhat(c):return sum(Q(j.bit_count())*z*z for j,z in enumerate(c))
def lnunit(x):
 z=(x-1)/(x+1);l=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(40)),Q(0));return l,l+2*z**81/(81*(1-z*z))
l2,u2=lnunit(Q(2))
@lru_cache(None)
def log(x):
 k=x.numerator.bit_length()-x.denominator.bit_length();t=x/(2**k if k>=0 else Q(1,2**(-k)))
 if t<1:k-=1;t*=2
 l,u=lnunit(t);return Q(k)+l/u2,Q(k)+u/l2
@lru_cache(None)
def H(ps):
 lo=hi=Q(0)
 for p in ps:
  if p:l,u=log(p);lo-=p*u;hi-=p*l
 return lo,hi
def modules(k):
 out=[]
 for mask in range(2**(2**(k+1))):
  tt=[1-2*((mask>>i)&1) for i in range(2**(k+1))];g=[tt[b::2] for b in (0,1)]
  d=Q(sum(x!=y for x,y in zip(*g)),2**k);flip=d>Q(1,2)
  folded=[g[0],[-x for x in g[1]] if flip else g[1]];c0,c1=map(fw,folded)
  J=(infhat(c0)+infhat(c1))/2;q=abs(1-2*d);delta=(1-q)/2
  kappa=infhat(tuple((x-y)/2 for x,y in zip(c0,c1)))
  ck(J>=2*delta*(1-delta));ck(J>=delta)
  out.append((tt,g,folded,k,J,q,delta,kappa,flip,c0,c1))
 return out
M1=modules(1);M2=None if pilot else modules(2)
def test(ms):
 global cases
 cases+=1
 if time.monotonic()-started>spec['maximum_runtime_seconds']:raise TimeoutError('frozen deadline')
 n=sum(m[3] for m in ms);raw=[];fold=[]
 for y in range(2**n):
  for b in (0,1):
   a=t=1;off=0
   for m in ms:
    jj=(y>>off)&(2**m[3]-1);a*=m[1][b][jj];t*=m[2][b][jj];off+=m[3]
   raw.append(a);fold.append(t)
 c=fw(fold);cr=fw(raw);J=sum(m[4] for m in ms)
 q=Q(1)
 for m in ms:q*=m[5]
 d=(1-q)/2;loss=sum(m[6] for m in ms)-d
 ck(loss>=0);ck(loss<=J-d)
 ck(sum(c[j]*c[j] for j in range(len(c)) if j&1)==d)
 ck(sum(Q(j.bit_count()-(j&1))*c[j]*c[j] for j in range(len(c)))==J)
 ck(d==Q(sum(fold[j]!=fold[j^1] for j in range(len(fold))),len(fold)))
 actual=sum(Q(j.bit_count()-1)*c[j]*c[j] for j in range(len(c)) if j&1)
 predicted=Q(0)
 for j,m in enumerate(ms):
  other=Q(1)
  for k,u in enumerate(ms):
   if k!=j:other*=u[5]
  charge=(1-other)*m[4]/2+other*m[7]
  ck(charge<=m[4]);predicted+=charge
 ck(actual==predicted);ck(actual<=J)
 flip=sum(m[8] for m in ms)%2
 ck(all(cr[j]*cr[j]==c[j^flip]*c[j^flip] for j in range(len(c))))
 priv0=fold[0::2];priv1=fold[1::2];p=tuple(x*x for x in c);p0=tuple(x*x for x in fw(priv0));p1=tuple(x*x for x in fw(priv1))
 hL,hU=H(p);L0,U0=H(p0);L1,U1=H(p1)
 if d==0:
  ck(priv0==priv1);ck(all(c[j]==0 for j in range(len(c)) if j&1))
 else:ck(hU-(L0+L1)/2 <= 3*d/l2+2*actual)
for a in M1:
 for b in M1:test([a,b])
if not pilot:
 for a in M2:
  for b in M1:test([a,b])
 for a in M1:
  for b in M1:
   for c in M1:test([a,b,c])
sharp=[]
for r in range(1,33):
 J=Q(r,2);d=Q(1,2);loss=Q(r-1,2)
 ck(loss==J-d);sharp.append({'r':r,'folded_loss':str(loss),'private_influence':str(J),'loss_over_private':str(loss/J)})
out={'status':'PASS','cases':cases,'assertions':checks,'runtime_seconds':time.monotonic()-started,'sharp_family':sharp,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/('out/OWNER_PILOT.json' if pilot else 'out/OWNER_CHECK.json')).write_text(json.dumps(out,indent=2));print(json.dumps({k:out[k] for k in ('status','cases','assertions','runtime_seconds')}))
