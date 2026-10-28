from base import *
import sys
import base
raw_value=value
raw_spectrum=spectrum
@lru_cache(None)
def cv(f,skip):return raw_value(f,skip)
def value(f,skip=0):return cv(tuple(f),skip)
@lru_cache(None)
def cs(f):return tuple(raw_spectrum(f))
def spectrum(f):return cs(tuple(f))
base.value=value
base.spectrum=spectrum
start=time.monotonic(); count=0
def ok(x):
 global count
 assert x
 count+=1
def le(x,y):
 global count
 certified_le(x,y);count+=1
def joint(a,c):
 return [Q(sum((x,y)==p for x,y in zip(a,c)),len(a)) for p in [(-1,-1),(-1,1),(1,-1),(1,1)]]
def entropy(q):
 z={}
 for p in q:
  if p:z=add(z,logterm(-p,p))
 return z
def gv(f):
 n=len(f).bit_length()-1;v=value(f);out={}
 for j in range(n):
  d=v
  for bit in (0,1):d=add(d,value(restrict(f,j,bit)),-Q(1,2))
  out=add(out,d)
 return out
def pair(am,cm,m):
 a=[1 if am>>z&1 else -1 for z in range(1<<m)]
 c=[1 if cm>>z&1 else -1 for z in range(1<<m)]
 F=fixture(a,c);h=mux(a,c);wh=value(h,1);T=remainder(a,c)
 ok(T==rhs_remainder(a,c));le(T,Q(389,64));le(add({},T,-1),0)
 R=add(add(wh,value(a),-Q(1,2)),value(c),-Q(1,2));gm=R;control={};mi={}
 for j in range(m):
  dT=T;dW=wh;dH=entropy(joint(a,c))
  for bit in (0,1):
   ab,cb=restrict(a,j,bit),restrict(c,j,bit)
   childT=remainder(ab,cb)
   ok(childT==rhs_remainder(ab,cb))
   dT=add(dT,childT,-Q(1,2));dW=add(dW,value(mux(ab,cb),1),-Q(1,2))
   dH=add(dH,entropy(joint(ab,cb)),-Q(1,2))
  u,v=spectrum(a)[1<<j],spectrum(c)[1<<j]
  bill=add({2:Q(5,32)*(u*u+v*v)},dH,Q(32))
  le(add(dT,bill,-1),0)
  gm=add(gm,dW);control=add(control,dT);mi=add(mi,dH)
 le(mi,2);le(control,Q(1029,16))
 data={}
 for j in range(6):
  d=value(F)
  for bit in (0,1):d=add(d,value(restrict(F,j,bit)),-Q(1,2))
  data=add(data,d)
 full=add(gv(F),gm,-Q(1,32))
 ok(full==add(control,add(data,R,-Q(1,32))))
 le(add(data,R,-Q(1,32)),Q(1167,32));le(full,Q(3225,32))
 influence=sum(Q(sum(F[x]!=F[x^(1<<j)] for x in range(len(F))),len(F)) for j in range(6))
 ok(influence>=Q(9,8));le(full,256*influence)
 ok(time.monotonic()-start<60)
 cv.cache_clear();cs.cache_clear()

mode=sys.argv[1]
if mode=='pilot': cases=[(a,c,1) for a in range(4) for c in range(4)]
else:cases=[(a,c,2) for a in range(16) for c in range(16)]+[(a,c,3) for a,c in [(0,255),(1,128),(15,23),(15,232),(7,19),(1,255),(105,150),(23,105)]]
if mode.startswith('main'):
 block=int(mode[4:]);cases=cases[64*block:64*(block+1)]+cases[256+2*block:258+2*block]
for am,cm,m in cases:pair(am,cm,m)
for a,c in [(1,1),(1,-1),(-1,1),(-1,-1)]:
 F=fixture([a],[c]);p=spectrum(F)
 weighted=sum(Q(1<<s.bit_count())*v*v for s,v in enumerate(p))
 ok(weighted<=Q(961,64));ok(weighted<16)
ok(Q(3,2)*Q(5,64)+Q(5,128)==Q(5,32))
ok(64+Q(5,16)+Q(1167,32)==Q(3225,32)<101<256*Q(9,8))
out={'status':'PASS','mode':mode,'pairs':len(cases),'assertions':count,'seconds':time.monotonic()-start,'arithmetic':'Fraction/prime-log, 32-term outward atanh bounds','independent_person_review':'PENDING','peak_memory':'unmeasured; estimate100MB'}
save('out/'+mode+'.json',out);print(json.dumps(out))
