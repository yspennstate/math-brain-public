from arithmetic import *
from functools import lru_cache

@lru_cache(None)
def ln_interval(p):
 k=p.bit_length()-1; t=Q(p,1<<k); z=(t-1)/(t+1)
 def atanh(z):
  s=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(32)),Q(0))
  return s,s+2*z**65/(65*(1-z*z))
 l,h=atanh(z); l2,h2=atanh(Q(1,3))
 return l+k*l2,h+k*h2
def nonnegative(a):
 lo=hi=Q(0)
 for p,c in a.items():
  l,h=ln_interval(p); lo+=c*(l if c>0 else h); hi+=c*(h if c>0 else l)
 if lo>=0:return True
 if hi<0:return False
 return sign(a)>=0
def ce(P,R):
 out={}
 for p,q in zip(P,R):
  if p:
   assert q>0
   out=add(out,log(q),-p)
 return out
def prob(f):return tuple(t*t for t in spectrum(f))
def phase_ref(u,weighted):
 P=prob(u); V=1-P[0]
 weights=[Q((j+1) if weighted else 1) for j in range(1,len(P))]
 return (P[0],)+tuple(V*w/sum(weights) for w in weights)

class State:
 def __init__(self,u,v,ru,rv,na,nb,ea=True,eb=True,z=None):
  self.u,self.v,self.ru,self.rv=u,v,ru,rv
  self.na,self.nb,self.ea,self.eb,self.z=na,nb,ea,eb,z
  self.k=len(u).bit_length()-1; self.a=Q(1,1<<na) if ea else Q(0); self.b=Q(1,1<<nb) if eb else Q(0)
  self.pi=Q(1,2) if z is None else Q(z==0)
  k=self.k; mask=(1<<k)-1
  self.g=tuple(u[x&mask] if ea and (x>>k)==0 else 1 for x in range(1<<(k+na)))
  self.h=tuple(v[x&mask] if eb and (x>>k)==0 else 1 for x in range(1<<(k+nb)))
  self.rg=self.branch(self.g,ru,self.a,na); self.rh=self.branch(self.h,rv,self.b,nb)
  def value(x):
   gv=u[x&mask] if ea and ((x>>k)&((1<<na)-1))==0 else 1
   hv=v[x&mask] if eb and ((x>>(k+na))&((1<<nb)-1))==0 else 1
   zval=(x>>(k+na+nb)) if z is None else z
   return gv if zval==0 else hv
  self.f=tuple(value(x) for x in range(1<<(k+na+nb+(z is None))))
  self.P=prob(self.f); self.Q=[]
  for idx,p in enumerate(self.P):
   t=idx&mask; am=(idx>>k)&((1<<na)-1); bm=(idx>>(k+na))&((1<<nb)-1)
   if not am and not bm:q=p
   elif am and not bm:q=(Q(1,4) if z is None else Q(z==0))*self.rg[t|(am<<k)]
   elif bm and not am:q=(Q(1,4) if z is None else Q(z==1))*self.rh[t|(bm<<k)]
   else:q=Q(0)
   self.Q.append(q)
  assert sum(self.Q)==1
  self.CE=ce(self.P,self.Q); self.H=entropy(self.f)
  self.cu=ce(prob(u),ru); self.cv=ce(prob(v),rv)
  self.du=add(self.cu,entropy(u),-1); self.dv=add(self.cv,entropy(v),-1)
  self.debt=add(scale(self.du,self.pi*self.a*(1-self.a)),self.dv,(1-self.pi)*self.b*(1-self.b))
  assert add(self.CE,self.H,-1)==self.debt
  self.core=self.pi*self.a*influence(u)+(1-self.pi)*self.b*influence(v)
  self.I=influence(self.f); self.ctrl=self.I-self.core
  assert self.core==sum((edge_inf(self.f,j) for j in range(k)),Q(0))
  self.L=add(add(scale(self.cu,self.pi*self.a),self.cv,(1-self.pi)*self.b),{2:self.core+7*self.ctrl})
  self.L=add(self.L,self.CE,-1)
  assert nonnegative(self.L)
  # Descendant rate is checked explicitly by the new stage checker.
 def branch(self,g,r,a,n):
  P=prob(g); mask=(1<<self.k)-1
  return tuple(p if not (idx>>self.k) or not (idx&mask) else a*a*r[idx&mask] for idx,p in enumerate(P))
 def child(self,kind,bit):
  na,nb,ea,eb,z=self.na,self.nb,self.ea,self.eb,self.z
  if kind=='A':na-=1;ea=ea and bit==0
  elif kind=='B':nb-=1;eb=eb and bit==0
  else:z=bit
  return State(self.u,self.v,self.ru,self.rv,na,nb,ea,eb,z)
 def index(self,kind):return self.k if kind=='A' else self.k+self.na if kind=='B' else self.k+self.na+self.nb
 def label(self,idx):
  am=(idx>>self.k)&((1<<self.na)-1); bm=(idx>>(self.k+self.na))&((1<<self.nb)-1)
  return ('s',idx) if not am and not bm else ('a',) if am and not bm else ('b',) if bm and not am else ('zero',)

def transport(s,kind):
 i=s.index(kind); children=[s.child(kind,t) for t in [0,1]]
 assert all(children[t].f==restrict(s.f,i,t) for t in [0,1])
 inherited=[[Q(0)]*len(c.P) for c in children]
 for j in range(len(children[0].P)):
  i0=(j&((1<<i)-1))|((j>>i)<<(i+1)); mass=s.P[i0]+s.P[i0|(1<<i)]; qm=s.Q[i0]+s.Q[i0|(1<<i)]
  if mass:kernel=[c.P[j]/(2*mass) for c in children]
  else:
   am=(i0>>s.k)&((1<<s.na)-1); bm=(i0>>(s.k+s.na))&((1<<s.nb)-1)
   owner=s.label(i0)[0]
   if kind=='z' and owner in ['a','b']:kernel=[Q(owner=='a'),Q(owner=='b')]
   elif (kind=='A' and am and s.ea) or (kind=='B' and bm and s.eb):kernel=[Q(1),Q(0)]
   else:kernel=[Q(1,2),Q(1,2)]
  assert sum(kernel)==1
  for t in [0,1]:inherited[t][j]=qm*kernel[t]
 savings={}
 for c,raw in zip(children,inherited):
  normal=sum(raw); assert normal>0
  rq=[q/normal for q in raw]; groups={}
  for j in range(len(c.P)):groups.setdefault(c.label(j),[]).append(j)
  calibrated=[Q(0)]*len(c.P)
  for ids in groups.values():
   p=sum(c.P[j] for j in ids); q=sum(rq[j] for j in ids)
   if p:assert q>0
   for j in ids:calibrated[j]=rq[j]*p/q if p else Q(0)
  assert calibrated==c.Q,(kind,s.na,s.nb,s.ea,s.eb,s.z)
  assert nonnegative(add(ce(c.P,rq),c.CE,-1))
 release=add(s.debt,add(children[0].debt,children[1].debt),-Q(1,2))
 expect=scale(s.du,s.pi*s.a*s.a) if kind=='A' else scale(s.dv,(1-s.pi)*s.b*s.b) if kind=='B' else {}
 assert release==expect
 assert s.core==(children[0].core+children[1].core)/2
 assert s.pi*s.a==sum(c.pi*c.a for c in children)/2
 assert (1-s.pi)*s.b==sum((1-c.pi)*c.b for c in children)/2
 inf=edge_inf(s.f,i)
 assert s.ctrl==inf+(children[0].ctrl+children[1].ctrl)/2
 drift=add(s.CE,add(children[0].CE,children[1].CE),-Q(1,2))
 rhs=add({2:7*inf},add(children[0].L,children[1].L),Q(1,2)); rhs=add(rhs,s.L,-1)
 assert drift==rhs
 return children

def main():
 start=time.perf_counter(); pilot='--pilot' in sys.argv; nr=nt=0
 pairs=[(6,12)] if pilot else [(u,v) for u in range(16) for v in range(16)]
 for uc,vc in pairs:
  u,v=table(2,uc),table(2,vc)
  for weighted in [False,True]:
   ru,rv=phase_ref(u,weighted),phase_ref(v,weighted)
   assert nonnegative(add({2:4*influence(u)},ce(prob(u),ru),-1))
   assert nonnegative(add({2:4*influence(v)},ce(prob(v),rv),-1))
   for na in [1,2]:
    for nb in [1,2]:
     s=State(u,v,ru,rv,na,nb);nr+=1
     for kind in ['A','B','z']:transport(s,kind);nt+=1
 result={'helper_version':'A056-fixed-phase-book-v1','pilot':pilot,'roots':nr,'physical_transports':nt,'child_reference_equalities':2*nt,'arithmetic':'Fraction FWHT; prime-log equality; 32-term rational atanh intervals with proved tail, exact integer-product fallback','assertions':'ALL PASS','runtime_seconds':time.perf_counter()-start}
 (R/'out'/('pilot.json' if pilot else 'checks.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
