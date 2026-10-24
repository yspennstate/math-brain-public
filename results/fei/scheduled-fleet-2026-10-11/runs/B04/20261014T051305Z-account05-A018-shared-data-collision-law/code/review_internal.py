from pathlib import Path
from fractions import Fraction as Q
import time,json,sys
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1;assert x;assert time.perf_counter()-start<60
def energy(v):
 N=len(v);n=(N-1).bit_length()
 return sum(Q((v[x]-v[x^(1<<bit)])**2,4*N) for x in range(N) for bit in range(n))
def W(v):
 if len(v)==1:return v[:]
 k=len(v)//2;a=W(v[:k]);b=W(v[k:])
 return [x+y for x,y in zip(a,b)]+[x-y for x,y in zip(a,b)]
def table(n,m):return [1-2*((m>>x)&1) for x in range(1<<n)]
cases=0;violations=0
for n in ([1] if '--pilot' in sys.argv else [1,2]):
 N=1<<n
 for gm in range(1<<N):
  g=table(n,gm)
  for em in range(1<<N):
   e=[(em>>x)&1 for x in range(N)];b=[a*(1-2*z) for a,z in zip(g,e)];D=[a*z for a,z in zip(g,e)]
   J=(energy(g)+energy(b))/2;k=energy(D);pin=pout=Q(0)
   for bit in range(n):
    for x in range(N):
     xx=x^(1<<bit)
     if g[x]!=g[xx]:
      if e[x] and e[xx]:pin+=Q(1,N)
      if not e[x] and not e[xx]:pout+=Q(1,N)
   ck(2*k-J==pin-pout);ck((k<=J/2)==(pin<=pout));violations+=int(k>J/2);cases+=1
   if em.bit_count()==1:ck(k==Q(n,2*N) and J>=Q(n,N))
signed=[]
if '--pilot' not in sys.argv:
 gs=[[1,1,-1,1],[1,-1]];es=[[1,0,1,0],[1,0]]
 for m1 in range(16):
  for m2 in range(16):
   masks=[m1,m2]
   def endpoint(j,b):return [a*(1-2*e*((masks[j]>>b)&1)) for a,e in zip(gs[j],es[j])]
   def val(i):
    b=i&3;t=(i>>2)&3;u=i>>4
    return endpoint(0,b)[t]*endpoint(1,b)[u]
   v=[val(i) for i in range(32)];w=W(v);p=[Q(c*c,1024) for c in w]
   I=energy(v);ck(I==sum(z*s.bit_count() for s,z in enumerate(p)))
   d=sum(p[s]*(s&3).bit_count() for s in range(32));J=I-d
   E=sum(p[s] for s in range(32) if s&3==3)
   Tpriv=2*sum(p[s]*(s>>2).bit_count()*(s&3).bit_count() for s in range(32))
   correction=Q(0);owner=Q(0)
   for bit in (0,1):
    for history in (0,1):
     b=history<<(1-bit);bb=b|(1<<bit);q=[];js=[];ks=[]
     for j in range(2):
      a=endpoint(j,b);h=endpoint(j,bb)
      q.append(sum(Q(x*y,len(a)) for x,y in zip(a,h)))
      js.append((energy(a)+energy(h))/2);ks.append(energy([Q(x-y,2) for x,y in zip(a,h)]))
      if ((masks[j]>>b)^(masks[j]>>bb))&1==0:ck(2*ks[-1]-js[-1]==-js[-1])
     aa=[x*y for y in endpoint(1,b) for x in endpoint(0,b)];hh=[x*y for y in endpoint(1,bb) for x in endpoint(0,bb)]
     actual=energy([Q(x-y,2) for x,y in zip(aa,hh)])
     expected=sum((1-q[1-j])*js[j]/2+q[1-j]*ks[j] for j in range(2));ck(actual==expected)
     owner+=expected/2
     correction+=sum(q[1-j]*(2*ks[j]-js[j]) for j in range(2))/2
   ck(Tpriv==2*owner);ck(Tpriv==2*J+correction);ck(2*E<=d)
   if correction<=0:ck(Tpriv+2*E<=2*I)
   cases+=1;signed.append({'masks':masks,'I':str(I),'J':str(J),'d':str(d),'W':str(correction),'T_private':str(Tpriv),'mixed_energy':str(E)})
   (ROOT/'out/INTERNAL_PARTIAL.json').write_text(json.dumps(signed,indent=2)+'\n',encoding='utf8')
out={'status':'PASS','cases':cases,'checks':checks,'half_private_violations':violations,'positive_W_products':sum(Q(r['W'])>0 for r in signed),'elapsed_seconds':time.perf_counter()-start,'product_rows':signed,'review_scope':'Full all-dimensional proof reconstructed in REPORT; finite cases validate the independent edge representation'}
(ROOT/'out'/('INTERNAL_PILOT.json' if '--pilot' in sys.argv else 'INTERNAL_REVIEW.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:out[k] for k in ('status','cases','checks','half_private_violations','positive_W_products','elapsed_seconds')}))
