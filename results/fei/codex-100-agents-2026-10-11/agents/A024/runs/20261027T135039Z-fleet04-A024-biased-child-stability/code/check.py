from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter
import json,time,sys,hashlib
root=Path(__file__).resolve().parents[1]
helper=root.parent/'20261022T221625Z-fleet03-A024-biased-child-stability/code/check.py'
exec(compile(helper.read_text(encoding='utf-8').split("pilot='--pilot'")[0],str(helper),'exec'))
start=time.monotonic();checks=0;pilot='--pilot' in sys.argv;cap=55 if pilot else 180
def deadline():
 if time.monotonic()-start>cap:raise TimeoutError('frozen cap')
def save(n,v):(root/'out'/n).write_text(json.dumps(v,indent=2),encoding='utf-8')
def plus(v):return v if sign(v)>0 else {}
@lru_cache(None)
def xi(w,h):
 t=(1-stats(w)[0])/2;r=(1-stats(h)[0])/2
 return 5*(r*(1-r)*stats(w)[1]+t*(1-t)*stats(h)[1])
g=tuple(1 if x in [0,1,2] else -1 for x in range(8))
gp=tuple(-a if x==4 else a for x,a in enumerate(g))
w=tuple((g if s==0 else gp)[x] for x in range(8) for s in range(2))
eq(stats(w)[0],-Q(1,8));eq(stats(w)[1],Q(3,2))
g0,g1,d,q,Bw=split(w,0)
eq(g0,g);eq(g1,gp);eq(d,Q(1,8));eq(q,Q(3,8))
fibers=Counter((abs(a),abs(b)) for a,b in zip(walsh(g0),walsh(g1)))
actual=Counter((abs((a+b)/2),abs((a-b)/2)) for a,b in zip(walsh(g0),walsh(g1)))
eq(actual,Counter({(Q(1,8),Q(1,8)):4,(Q(3,8),Q(1,8)):3,(Q(5,8),Q(1,8)):1}))
eq(Bw,add(sc(L(Q(1,8),Q(1,8)),4),sc(L(Q(3,8),Q(1,8)),3),L(Q(5,8),Q(1,8))))
le(sign(add(Bw,const(-Q(1,2)))),-1)
r=Q(3,16);a=b=-Q(1,8);R=rem(r,a,b)
Bfixed=add(sc(Bw,r),R);E=add(Bfixed,const(-Q(3,32)))
le(sign(add(E,const(-Q(1,128))))*-1,-1)
le(sign(add(E,const(-Q(1,120)))),-1);le(sign(R)*-1,-1)
proofs={n:dict(expression=serialize(v),rational_log_bounds=[str(z) for z in bounds(v)]) for n,v in dict(inner_good=add(const(Q(1,2)),sc(Bw,-1)),lift_excess_lower=add(E,const(-Q(1,128))),lift_excess_upper=add(const(Q(1,120)),sc(E,-1)),positive_R=R).items()}
rows=[];roots=[];Hseed=None
for N in range(1,3 if pilot else 6):
 h=tuple(-1 if (x&7) in (0,1,2) and (x>>3).bit_count()%2 else 1 for x in range(1<<(N+3)))
 f=compose(w,h);roots.append((w,h))
 if Hseed is None:Hseed=stats(f)[2]
 eq(stats(f)[2],Hseed)
 eq((1-stats(h)[0])/2,r);eq(stats(h)[1],Q(3*N+5,8));eq(stats(f)[1],Q(27*N+81,128))
 f0,f1,df,qf,Bf=split(f,0)
 eq(f0,compose(g,h));eq(f1,compose(gp,h));eq(df,Q(3,128));eq(qf,Q(3*N+14,128));eq(Bf,Bfixed)
 le(sign(add(Bf,const(-4*df)))*-1,-1)
 D=xi(w,h)-(xi(g,h)+xi(gp,h))/2
 eq(D,Q(5*(3*N+44),2048));eq(qf-D,Q(33*N+4,2048));le(0,qf-D)
 eq(xi(w,h),Q(5*(189*N+783),2048))
 eq(Q(1,7)+qf+(xi(g,h)+xi(gp,h))/2-(Q(1,7)+xi(w,h)),Q(33*N+4,2048))
 le(sign(add(R,const(-D))),0)
 rows.append(dict(N=N,dimension=(len(f)-1).bit_length(),d=str(df),q=str(qf),I=str(stats(f)[1]),Xi=str(xi(w,h)),drift=str(D),full_terminal_deficit=str(qf-D)))
 deadline()

# Reconstruct complete stopping ledgers from actual spectra at every node.
node_count=0;zero_beta=zero_rate=one_rate=0
def replay(w,h,depth,policy):
 global node_count,zero_beta,zero_rate,one_rate
 f=compose(w,h);n=(len(f)-1).bit_length();nw=(len(w)-1).bit_length()
 if not n or depth==0:
  return dict(outer={},inner={},H=stats(f)[2],I=stats(f)[1],Xi=xi(w,h),terminal_H=stats(f)[2],terminal_I=stats(f)[1],terminal_Xi=xi(w,h))
 i=0 if policy==0 else n-1 if policy==1 else max(range(n),key=lambda j:split(f,j)[2])
 block=int(i>=nw);v=h if block else w;j=i-nw if block else i
 v0,v1,dv,_,Bv=split(v,j);rate=(1-stats(w if block else h)[0])/2
 beta=(stats(v0)[0]-stats(v1)[0])/2
 children=[(w,v0),(w,v1)] if block else [(v0,h),(v1,h)]
 f0,f1,df,_,Bf=split(f,i)
 eq(f0,compose(*children[0]));eq(f1,compose(*children[1]));eq(df,rate*dv)
 Rv=rem(rate,stats(v)[0],beta);eq(Bf,add(sc(Bv,rate),Rv))
 D=xi(w,h)-sum(xi(*c) for c in children)/2
 le(sign(add(Rv,const(-D))),0)
 JS=add(stats(f)[2],sc(add(stats(f0)[2],stats(f1)[2]),-Q(1,2)),sc(Bf,-1))
 le(sign(JS)*-1,0);le(sign(add(JS,const(-3*df))),0)
 res=[replay(*c,depth-1,policy) for c in children]
 outer=add(Bf,const(-4*df),sc(add(res[0]['outer'],res[1]['outer']),Q(1,2)))
 inner=add(sc(add(Bv,const(-4*dv)),rate),sc(add(res[0]['inner'],res[1]['inner']),Q(1,2)))
 tXi=sum(z['terminal_Xi'] for z in res)/2
 tI=sum(z['terminal_I'] for z in res)/2
 tH=sc(add(res[0]['terminal_H'],res[1]['terminal_H']),Q(1,2))
 gap=add(inner,const(xi(w,h)-tXi),sc(outer,-1));le(sign(gap)*-1,0)
 entropy_gap=add(const(7*(stats(f)[1]-tI)+xi(w,h)-tXi),inner,sc(stats(f)[2],-1),tH)
 le(sign(entropy_gap)*-1,0)
 eq(stats(f)[1],df+(stats(f0)[1]+stats(f1)[1])/2)
 node_count+=1;zero_beta+=int(beta==0);zero_rate+=int(rate==0);one_rate+=int(rate==1)
 deadline()
 return dict(outer=outer,inner=inner,H=stats(f)[2],I=stats(f)[1],Xi=xi(w,h),terminal_H=tH,terminal_I=tI,terminal_Xi=tXi)
for ww,hh in roots[:2 if pilot else 3]:
 for policy in range(3):
  for depth in (1,2,3):replay(ww,hh,depth,policy)

# Exact affine-in-N identity, retaining slope and intercept independently.
eq(Q(3,128)-Q(15,2048),Q(33,2048));eq(Q(14,128)-Q(220,2048),Q(4,2048))
# Endpoint and disjointness controls, actual functions.
eq(xi((-1,),(-1,1,1,1)),0);eq(stats(compose((-1,),(-1,1,1,1)))[2],const(2))
overlap=tuple(1-(1-x)*(1-y)//2 for x,y in zip((-1,1),(1,-1)))
eq(stats(overlap)[1],0);eq(Q(1)!=stats(overlap)[1],True)
save('CERTIFICATES.json',proofs)
out=dict(status='PASS',pilot=pilot,roots=rows,adaptive_prefix_nodes=node_count,zero_beta_nodes=zero_beta,zero_rate_nodes=zero_rate,one_rate_nodes=one_rate,exact_assertions=checks,runtime_seconds=time.monotonic()-start,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),helper_sha256=hashlib.sha256(helper.read_bytes()).hexdigest(),independent_review='PENDING')
save('PILOT.json' if pilot else 'VALIDATION.json',out);print(json.dumps(out))
