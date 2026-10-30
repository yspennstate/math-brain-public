from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from functools import lru_cache
import json,time,runpy,sys
ROOT=Path(__file__).resolve().parents[1]
U=runpy.run_path(str(ROOT.parent/'20261011T221822Z-fleet05-A048-tensor-stress/code/check.py'))
add,scale,entropy,walsh,influence,logvec,interval=[U[k] for k in ('add','scale','entropy','walsh','influence','logvec','interval')]
checks=0
def eq(a,b):
 global checks
 assert a==b,(a,b);checks+=1
def nonneg(v):
 global checks
 if v:assert interval(v)[0]>=0,v
 checks+=1
def ser(v):return {str(k):str(x) for k,x in sorted(v.items())}
def product(a,b):return [a[z%len(a)]*b[z//len(a)] for z in range(len(a)*len(b))]
def tensor(a,T):
 b=[1]
 for _ in range(T):b=product(b,a)
 return b
def law(tab):return {s:x*x for s,x in enumerate(walsh(tab)) if x}
def marg(p,mask):
 out=defaultdict(F)
 for s,x in p.items():out[s&mask]+=x
 return dict(out)
def ent(p):return entropy(p.values())
def CE(p,q):
 out={}
 for s,x in p.items():
  eq(q.get(s,F(0))>0,True);out=add(out,scale(logvec(q[s]),-x))
 return out
def KL(p,q):return add(CE(p,q),scale(ent(p),-1))
@lru_cache(None)
def global_masks(N,used):
 inds=[i for i in range(N) if not used>>i&1]
 return tuple(sum(((z>>j)&1)<<i for j,i in enumerate(inds)) for z in range(1<<len(inds)))
def restricted(tab,hist):
 N=(len(tab)-1).bit_length();used=sum(1<<i for i,b in hist);base=sum(b<<i for i,b in hist)
 masks=global_masks(N,used);arr=[tab[base|s] for s in masks]
 return {masks[s]:x*x for s,x in enumerate(walsh(arr)) if x},influence(arr)
def guard_tab(g,m):
 return [g[z>>(m+1)]*(-1 if z>>m&1 else 1) if z&((1<<m)-1)==(1<<m)-1 else 1 for z in range(len(g)*(1<<(m+1)))]
def guarded(g,m,T,index):
 n=(len(g)-1).bit_length();h=tensor(g,T);tab=guard_tab(h,m);floor=guard_tab([1],m);N=m+1+n*T;lowmask=(1<<(m+1))-1
 p=law(tab);p0=law(floor);pg=law(g);ph=law(h);t=F(1,1<<m)
 expected={}
 for low,x in p0.items():
  for z,y in (ph.items() if low>>m&1 else [(0,F(1))]):expected[low|(z<<(m+1))]=x*y
 eq(p,expected);eq(ent(p),add(ent(p0),scale(ent(pg),t*T)))
 eq(influence(tab),t*(m+1+T*influence(g)))
 # Actual and nonmatching uniform spectator references; both keep full seed CE.
 q={}
 for low,x in p0.items():
  for z,y in ([(z,F(1,1<<(n*T))) for z in range(1<<(n*T))] if low>>m&1 else [(0,F(1))]):q[low|(z<<(m+1))]=x*y
 eq(sum(q.values()),1);eq(CE(p,q),add(ent(p0),{2:t*T*n} if n else {}))
 rootKL=KL(p,q);eq(rootKL,scale(add({2:F(n)},scale(ent(pg),-1)),t*T))
 leafH=leafCE=leafKL={};leafI=F(0);M=J={}
 def visit(hist,qv,reach):
  nonlocal leafH,leafCE,leafKL,leafI,M,J
  pv,Iv=restricted(tab,hist);p0v,_=restricted(floor,hist)
  if len(hist)==m or any(b==0 for i,b in hist):
   leafH=add(leafH,scale(ent(pv),reach));leafCE=add(leafCE,scale(CE(pv,qv),reach));leafKL=add(leafKL,scale(KL(pv,qv),reach));leafI+=reach*Iv
   return
  i=len(hist);mask=((1<<N)-1)^(1<<i);pe=marg(pv,mask);qe=marg(qv,mask);pe0=marg(p0v,lowmask^(1<<i));kids=[];qkids=[]
  # Conditional erasure KL is zero; nonmatching seed KL is retained in T.
  eq(KL(pv,qv),KL(pe,qe))
  for b in (0,1):
   ch=hist+((i,b),);pb,_=restricted(tab,ch);p0b,_=restricted(floor,ch);raw={}
   for s,x in qe.items():
    low=s&lowmask;k=p0b.get(low,F(0))/(2*pe0[low])
    if pe.get(s,F(0)):eq(k,pb.get(s,F(0))/(2*pe[s]))
    if k:raw[s]=x*k
   eq(sum(raw.values()),F(1,2));qb={s:2*x for s,x in raw.items()}
   eq(sum(qb.values()),1);kids.append(pb);qkids.append(qb)
   visit(ch,qb,reach/2)
  mm=add(ent(pv),scale(ent(pe),-1));jj=add(ent(pe),scale(add(*(ent(k) for k in kids)),F(-1,2)))
  M=add(M,scale(mm,reach));J=add(J,scale(jj,reach))
  eq(KL(pv,qv),scale(add(*(KL(k,qc) for k,qc in zip(kids,qkids))),F(1,2)))
 visit((),q,F(1))
 eq(leafH,scale(ent(pg),t*T));eq(leafI,t*(1+T*influence(g)))
 eq(rootKL,leafKL);eq(add(ent(p),scale(leafH,-1)),ent(p0));eq(add(M,J),ent(p0))
 eq(add(CE(p,q),scale(leafCE,-1)),ent(p0));nonneg(add({2:7*m*t},scale(ent(p0),-1)))
 result={'index':index,'n':n,'m':m,'T':T,'root_entropy':ser(ent(p)),'floor_entropy':ser(ent(p0)),'terminal_entropy':ser(leafH),'controller_removed_influence':str(m*t),'terminal_influence':str(leafI),'source_uniform_seed_KL':ser(rootKL),'terminal_seed_KL':ser(leafKL),'controller_M':ser(M),'controller_J':ser(J)}
 (ROOT/'out'/f'guard_{index:04}.json').write_text(json.dumps(result,indent=2)+'\n')
 return result
def classifier(g):
 pg=law(g);mu=F(sum(g),len(g));beta=sum((p for s,p in pg.items() if s and not s&1),F(0))
 means=[F(g[2*z]+g[2*z+1],2) for z in range(4)]
 eq(beta,sum((x*x for x in means),F(0))/4-mu*mu)
 tab=[g[z>>1] if z&1 else 1 for z in range(16)];kernels={};compatible=True
 for hist in ((),((0,0),),((0,1),)):
  p,_=restricted(tab,hist);groups=defaultdict(dict)
  for s,x in p.items():groups[s&3][s>>2]=x
  for low,dist in groups.items():
   total=sum(dist.values());k={s:x/total for s,x in dist.items()};u=low>>1
   if u in kernels and k!=kernels[u]:compatible=False
   kernels[u]=k
 eq(compatible,beta==0)
 pg2=law(product(g,g));beta2=sum((p for s,p in pg2.items() if s and not s&9),F(0))
 eq(beta2,(mu*mu+beta)**2-mu**4)
 return compatible
def entropy_boundary(tab,i,Zmask):
 N=(len(tab)-1).bit_length();allmask=(1<<N)-1;Qmask=allmask^Zmask;p=law(tab)
 kids=[restricted(tab,((i,b),))[0] for b in (0,1)]
 L=add(ent(p),scale(ent(marg(p,Qmask)),-1));Lc=scale(add(*(add(ent(k),scale(ent(marg(k,Qmask&~(1<<i))),-1)) for k in kids)),F(1,2))
 drift=add(L,scale(Lc,-1));inf=F(sum(tab[z]!=tab[z^(1<<i)] for z in range(len(tab))),len(tab))
 if not Zmask>>i&1:
  pe=marg(p,allmask&~(1<<i));pqe=marg(p,Qmask&~(1<<i))
  MF=add(ent(p),scale(ent(pe),-1));MQ=add(ent(marg(p,Qmask)),scale(ent(pqe),-1))
  JF=add(ent(pe),scale(add(*(ent(k) for k in kids)),F(-1,2)));JQ=add(ent(pqe),scale(add(*(ent(marg(k,Qmask&~(1<<i))) for k in kids)),F(-1,2)))
  iz=add(MQ,scale(MF,-1));bz=add(JF,scale(JQ,-1));eq(drift,add(bz,scale(iz,-1)));nonneg(iz);nonneg(bz);nonneg(add({2:3*inf},scale(drift,-1)))
 return p,kids,drift,inf
def boundaries():
 h2=[1,1,1,-1];h3=[1]*7+[-1]
 p,kids,d,inf=entropy_boundary(h3,0,6);eq(d,{2:F(1),3:F(-3,8)});eq(inf,F(1,4))
 tab=product(h3,h2);p,kids,d2,inf2=entropy_boundary(tab,0,6);eq(d2,d)
 qc=[F(1,2),F(1,4),F(1,8),F(1,8)];ph=law(h3);q={c*8+s:qc[c]*x for c in range(4) for s,x in ph.items()};pe=marg(p,30);qe=marg(q,30)
 eq(KL(p,q),KL(pe,qe))
 childKL=[]
 for b,k in enumerate(kids):
  raw={s:x*k.get(s,F(0))/(2*pe[s]) for s,x in qe.items() if k.get(s,F(0))}
  eq(sum(raw.values()),F(1,2));qb={s:2*x for s,x in raw.items()};childKL.append(KL(k,qb))
  for c in range(4):
   pm={s&6:x for s,x in k.items() if s>>3==c};qm={s&6:x for s,x in qb.items() if s>>3==c}
   eq({s:x/sum(pm.values()) for s,x in pm.items()},{s:x/sum(qm.values()) for s,x in qm.items()})
 eq(KL(p,q),scale(add(*childKL),F(1,2)))
 f=guard_tab(h2,1);p,kids,d3,inf3=entropy_boundary(f,2,12);eq(ent(p),{2:F(3)});eq([ent(k) for k in kids],[{2:F(2)}]*2);eq(d3,{2:F(1)});eq(inf3,F(1,4));eq(3*inf3<F(1),True)
 result={'outside_Z_h3_drift':ser(d),'retained_likelihood_source_KL':ser(KL(law(tab),q)),'spectator_query_drift':'1','spectator_query_influence':'1/4','strict_certificate':'ln2>2/3 implies 2Inf/ln2<3/4<1'}
 (ROOT/'out'/'BOUNDARIES.json').write_text(json.dumps(result,indent=2)+'\n')
 return result
def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv;results=[];index=0
 domain=[(2,mask,1,1) for mask in range(4)] if pilot else [(n,mask,m,T) for n in range(3) for mask in range(1<<(1<<n)) for m in range(1,4) for T in (1,2)]+[(3,mask,1,1) for mask in range(256)]
 for n,mask,m,T in domain:
  g=[1-2*((mask>>z)&1) for z in range(1<<n)];results.append(guarded(g,m,T,index));index+=1
 classifications=[classifier([1-2*((mask>>z)&1) for z in range(8)]) for mask in range(4 if pilot else 256)]
 if not pilot:eq(sum(classifications),18)
 boundary=boundaries();formulas=[]
 if not pilot:
  Hg={2:F(2)};Ig=F(1)
  for m in range(1,9):
   t=F(1,1<<m);H0=entropy(law(guard_tab([1],m)).values())
   for T in range(1,9):
    H=add(H0,scale(Hg,t*T));I=t*(m+1+T*Ig)
    eq(add(H,scale(H0,-1)),{2:2*t*T});eq(I-t*(m+1),t*T*Ig)
    formulas.append({'m':m,'T':T,'H':ser(H),'I':str(I),'terminal_seed_entropy':str(2*t*T)})
 summary={'status':'PASS','cases':11 if pilot else 711,'guarded_count':len(results),'classifier_count':len(classifications),'classifier_admitted':sum(classifications),'assertions':checks,'seconds':time.perf_counter()-start,'boundaries':boundary,'formulas':formulas}
 (ROOT/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(summary,indent=2)+'\n')
 print(json.dumps({k:v for k,v in summary.items() if k not in ('boundaries','formulas')}))
if __name__=='__main__':main()
