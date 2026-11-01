from pathlib import Path
import json,time,sys,hashlib
root=Path(__file__).resolve().parents[1]
helper=root.parent/'20261022T221625Z-fleet03-A024-biased-child-stability/code/check.py'
exec(compile(helper.read_text(encoding='utf-8').split("pilot='--pilot'")[0],str(helper),'exec'))
run=root;start=time.monotonic();checks=0
pilot='--pilot' in sys.argv;cap=55 if pilot else 180
def bank(w,h):
 t=(1-stats(w)[0])/2;r=(1-stats(h)[0])/2
 return 5*(r*(1-r)*stats(w)[1]+t*(1-t)*stats(h)[1])
def tables(n):return [tuple(1 if c>>x&1 else -1 for x in range(1<<n)) for c in range(1<<(1<<n))]
def deadline():
 if time.monotonic()-start>cap:raise TimeoutError('frozen cap')
states=set();queries=0;negative=positive=0;rows=[]
def visit(w,h):
 global queries,positive,negative
 if (w,h) in states:return
 states.add((w,h));f=compose(w,h)
 t=(1-stats(w)[0])/2;r=(1-stats(h)[0])/2
 eq(stats(f)[1],r*stats(w)[1]+t*stats(h)[1])
 le(bank(w,h),5*stats(f)[1])
 nw=(len(w)-1).bit_length();nh=(len(h)-1).bit_length()
 for block,v,other,rate in [(0,w,h,r),(1,h,w,t)]:
  for i in range((len(v)-1).bit_length()):
   v0,v1,d,q,B=split(v,i);a=stats(v)[0];b=(stats(v0)[0]-stats(v1)[0])/2
   R=rem(rate,a,b);Rsign=sign(R);positive+=int(Rsign>0);negative+=int(Rsign<0)
   children=[(v0,h),(v1,h)] if block==0 else [(w,v0),(w,v1)]
   fi=i if block==0 else nw+i
   f0,f1,df,_,Bf=split(f,fi)
   eq(f0,compose(*children[0]));eq(f1,compose(*children[1]));eq(df,rate*d)
   eq(Bf,add(sc(B,rate),R));le(abs(b),d)
   le(sign(add(R,const(-5*rate*(1-rate)*abs(b)))),0)
   drift=bank(w,h)-sum(bank(*c) for c in children)/2
   eq(drift,5*(rate*(1-rate)*d+b*b*stats(other)[1]/4));le(0,drift)
   Rp=R if Rsign>0 else {};le(sign(add(Rp,const(-drift))),0)
   rows.append(dict(rate=str(rate),mean=str(a),beta=str(b),d=str(d),drift=str(drift)))
   for c in children:visit(*c)
   queries+=1;deadline()
n=1 if pilot else 2
for w in tables(n):
 for h in tables(n):visit(w,h)

# Independent scalar domain extends beyond physically feasible |a|+|b|<=1.
scalar=0;den=4 if pilot else 16
for j in range(den+1):
 for k in range(den+1):
  for l in range(-den,den+1):
   r=Q(j,den);a=Q(l,den);b=Q(k,den)
   le(sign(add(rem(r,a,b),const(-5*r*(1-r)*b))),0);scalar+=1
   deadline()

# Full adaptive prefix accounts: physical index chosen from actual current influences.
prefixes=0
def replay(w,h,depth,mode):
 global prefixes
 f=compose(w,h);nw=(len(w)-1).bit_length();n=(len(f)-1).bit_length()
 if not n or depth==0:return {},bank(w,h),{},stats(f)[2],Q(0)
 i=(0 if mode==0 else n-1) if mode<2 else max(range(n),key=lambda j:split(f,j)[2])
 block=int(i>=nw);v=h if block else w;j=i-nw if block else i
 v0,v1,d,_,_=split(v,j);rate=(1-stats(w if block else h)[0])/2
 b=(stats(v0)[0]-stats(v1)[0])/2;R=rem(rate,stats(v)[0],b)
 Rp=R if sign(R)>0 else {}
 children=[(w,v0),(w,v1)] if block else [(v0,h),(v1,h)]
 results=[replay(*c,depth-1,mode) for c in children]
 drift=bank(w,h)-sum(bank(*c) for c in children)/2
 bill=add(Rp,sc(add(results[0][0],results[1][0]),Q(1,2)))
 terminal=sum(z[1] for z in results)/2
 release=add(const(drift),sc(Rp,-1),sc(add(results[0][2],results[1][2]),Q(1,2)))
 eq(add(bill,const(terminal),release),const(bank(w,h)))
 # Nonzero OLD debit survives without any retrospective grant.
 eq(add(const(Q(1,7)),bill,const(terminal),release),const(Q(1,7)+bank(w,h)))
 f0,f1,df,_,_=split(f,i)
 entropy_drop=add(stats(f)[2],sc(add(stats(f0)[2],stats(f1)[2]),-Q(1,2)))
 Hfull=add(entropy_drop,sc(add(results[0][3],results[1][3]),Q(1,2)))
 eq(Hfull,stats(f)[2]);Ispent=df+sum(z[4] for z in results)/2
 prefixes+=1
 return bill,terminal,release,Hfull,Ispent
for w in tables(n):
 for h in tables(n):
  for mode in range(3):
   for depth in [1,2,2*n]:
    replay(w,h,depth,mode);deadline()

# Hypothesis adversaries and endpoints.
eq(compose((-1,1),(1,-1)),(1,1,-1,1))
overlap_F=(1,1);predicted=Q(1)
eq(stats(overlap_F)[1],0);eq(predicted!=stats(overlap_F)[1],True)
eq(bank((-1,),(-1,1,1,1)),0);eq(stats(compose((-1,),(-1,1,1,1)))[2],const(2))
eq(bank((1,),(-1,1)),0)
out=dict(status='PASS',pilot=pilot,roots=len(tables(n))**2,states=len(states),queries=queries,scalar_cases=scalar,adaptive_prefix_nodes=prefixes,positive_remainders=positive,negative_remainders=negative,exact_assertions=checks,runtime_seconds=time.monotonic()-start,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),helper_sha256=hashlib.sha256(helper.read_bytes()).hexdigest(),independent_review='PENDING')
(root/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
