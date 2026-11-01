from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import sys,time,json,hashlib,itertools
import exact as c

ROOT=Path(__file__).resolve().parents[1]
c.eta=lru_cache(None)(c.eta)
CHECKS=0
def check(v):
 global CHECKS
 assert v
 CHECKS+=1
def overlap(a,b):check(not(a[1]<b[0] or b[1]<a[0]))
def close(a,b):
 overlap(a,b);check(Q(max(a[1]-b[0],b[1]-a[0]),c.SCALE)<Q(1,10**25))
def mean(v):return Q(sum(v),len(v))
def restrict(v,i,b):
 return [v[(x&((1<<i)-1))+((x>>i)<<(i+1))+(b<<i)] for x in range(len(v)//2)]
def H(v,tf=c.fwht):return c.add(*(c.eta(x*x) for x in tf(v)))
def R(tags,vu,vv):
 return c.add(c.times(c.eta(Q(tags.count(2),len(tags))),vu),c.times(c.eta(Q(tags.count(3),len(tags))),vv))
def phi(a,b):return c.phi(Q(a),Q(b))
def wrapper(ext,width,prefix,u,v,tf=c.fwht):
 states=[];j=ext
 for _ in range(4):states.append(j%3);j//=3
 C=[int(j==0) for j in states];K0=[0 if j==0 else 1 if j==1 else -1 for j in states]
 density=mean(C);E=[1,1] if prefix is None else [0,1];K=[0,0] if prefix is None else [prefix,0]
 e=mean(E);m=Q(0 if u==0 else u);n=Q(0 if v==0 else v);vu=1-m*m;vv=1-n*n
 N=1<<(5+width);f=[];tags=[]
 for a in range(N):
  z=a&3;old=(a>>2)&1;b=(a>>3)&((1<<width)-1);uu=u if u else (-1)**((a>>(3+width))&1);vvv=v if v else (-1)**((a>>(4+width))&1)
  if not C[z]:value=K0[z];label=0
  elif not E[old]:value=K[old];label=1
  elif not b:value=uu;label=2
  else:value=vvv;label=3
  f.append(value);tags.append(label)
 i=3;q=Q(1,1<<width);d=density*e*q*(1-m*n)
 check(all(x in [-1,1] for x in f));check(Q(sum(f[x]!=f[x^(1<<i)] for x in range(N)),N)==d)
 fs=tf(f);check(sum(a*a for s,a in enumerate(fs) if s&(1<<i))==d)
 B=c.add(*(phi(fs[s]**2,fs[s+(1<<i)]**2) for s in range(N) if not s&(1<<i)))
 children=[restrict(f,i,b) for b in [0,1]]
 D=c.add(H(f,tf),c.neg(c.times(c.add(*(H(t,tf) for t in children)),Q(1,2))))
 kap=c.add(R(tags,vu,vv),c.neg(c.times(c.add(*(R(restrict(tags,i,b),vu,vv) for b in [0,1])),Q(1,2))))
 k=c.add(c.eta(1-q),c.neg(c.times(c.eta(1-2*q),Q(1,2))))
 expectedkap=c.add(c.times(c.ln(Q(2)),density*e*q*vu),c.times(k,density*e*vv))
 close(kap,expectedkap)
 cs,ks,es,ps=map(tf,[C,K0,E,K]);delta=m-n;M=n+q*delta;x=q*abs(delta)
 S=c.add(*(phi((ks[s]*(t==0)+cs[s]*(ps[t]+M*es[t]))**2,x*x*cs[s]**2*es[t]**2) for s in range(4) for t in range(2)))
 formula=c.add(expectedkap,c.times(c.ln(Q(2)),density*e*(q-2*q*q)*(vv+delta*delta)),c.times(phi((1-q)**2,q*q),density*e*vv),c.neg(c.times(k,density*e*vv)),S)
 close(B,formula)
 if d:
  rhs=c.times(c.add(c.times(c.ln(Q(2)),Q(20)),c.ln(1/density)),d)
  margin=c.add(rhs,c.neg(D),kap);check(margin[0]>0)
 else:
  check(children[0]==children[1]);close(D,(0,0));close(kap,(0,0))
 return d

def bent(m,tf=c.fwht):
 N=1<<m;den=Q(1,N);s=Q(1,1<<(m//2))
 b=[(-1)**sum(((x>>j)&1)*((x>>(j+1))&1) for j in range(0,m,2)) for x in range(N)]
 g=list(b);g[0]=-1;F=b+g
 bs,gs,fs=map(tf,[b,g,F]);check(all(abs(x)==s for x in bs));check(sum(x>0 for x in bs)==(N+(1<<(m//2)))//2)
 for t in range(N):check(gs[t]==bs[t]-2*den);check(fs[t]==bs[t]-den);check(fs[t+N]==den)
 check(Q(sum(x!=y for x,y in zip(b,g)),N)==den)
 hb,hg,hf=H(b,tf),H(g,tf),H(F,tf)
 D=c.add(hf,c.neg(c.times(c.add(hb,hg),Q(1,2))))
 residual=c.add(c.times(D,1/den),c.neg(c.times(c.ln(Q(2)),Q(m))))
 if m>=4:
  # Uniform analytic remainder from the exact T2/2-T1 series.
  lo=c.times((c.SCALE,c.SCALE),Q(3)-8*den/(1-4*den))
  hi=c.times((c.SCALE,c.SCALE),Q(3)-Q(19,6)*den)
  check(residual[0]>=lo[0]);check(residual[1]<=hi[1])
 check(all(x in [-1,1] for x in F))
 return {'m':m,'density':str(den),'query_influence':str(den),'fine_R':0,'fine_R_children':[0,0],'D_over_query_I':c.serial(c.times(D,1/den)),'D_over_query_I_minus_log2_inverse_density':c.serial(residual),'root_H':c.serial(hf),'actual_children_H':[c.serial(hb),c.serial(hg)]}

def main(mode):
 start=time.perf_counter();rows=[];count=0
 if mode=='pilot':
  args=itertools.product([0,1,2,13,26,40,54,67,80],[1],[None,-1,1],[-1,1],[-1,1])
 elif mode=='main':args=itertools.product(range(81),[1,2],[None,-1,1],[-1,1,0],[-1,1,0])
 elif mode=='reproduce':args=itertools.product([0,13,40,80],[1],[None,-1,1],[-1,1,0],[-1,1,0])
 else:args=[]
 for args1 in args:
  wrapper(*args1,tf=c.direct if mode=='reproduce' else c.fwht);count+=1
  if time.perf_counter()-start>53:raise RuntimeError('frozen time cap reached; no finite-exhaustion conclusion')
 if mode in ['pilot','bent','reproduce']:
  for m in ([4] if mode=='pilot' else [2,4,6] if mode=='reproduce' else [4,6,8,10,12]):rows.append(bent(m,c.direct if mode=='reproduce' else c.fwht))
 elapsed=time.perf_counter()-start;check(elapsed<55)
 result={'mode':mode,'status':'PASS','assertions':CHECKS,'wrapper_roots':count,'seconds':elapsed,'rows':rows,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'arithmetic_helper_sha256':hashlib.sha256(Path(c.__file__).read_bytes()).hexdigest(),'full_actual_terminals':True}
 (ROOT/'out'/('CHECK_'+mode+'.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
 print(json.dumps({'mode':mode,'status':'PASS','assertions':CHECKS,'wrapper_roots':count,'seconds':elapsed,'bent_ratios':[(r['m'],r['D_over_query_I']['display']) for r in rows]}))
if __name__=='__main__':main(sys.argv[1])
