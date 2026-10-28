from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[1]
OLD=R.parent/'20261023T014805Z-account03-A047-boundary-search/code/check.py'
exec(compile(OLD.read_text(encoding='utf-8').split('cases=')[0],str(OLD),'exec'))
ROOT=R
def family(r,balanced):
 def base(z):return -1 if (z>>(2 if z&1 else 1))&1 else 1
 n=r+1+int(balanced)
 return tuple(base((x>>1)&((1<<r)-1))*(-1 if ((x>>1)&((1<<r)-1)) in ({1} if not x&1 else {1,4,5}) else 1)*(-1 if balanced and x>>(r+1)&1 else 1) for x in range(1<<n))
def fresh(t,a):
 p,_=spec(t);essential=0
 for s in p:essential|=s
 if len(p)==1:return p.copy()
 q={s:(1-a)*v for s,v in p.items()};q[0]=p.get(0,F(0));q[essential]=q.get(essential,F(0))+a*(1-p.get(0,F(0)))
 return {s:v for s,v in q.items() if v}
def lift(t,q,eps):
 mu=F(sum(t),len(t));law={0:(eps+mu)**2/4,1:(eps-mu)**2/4}
 for s,v in q.items():
  if s:law[s<<1]=v/4;law[(s<<1)|1]=v/4
 return {s:v for s,v in law.items() if v}
def activate(t,eps):return tuple(eps if not x&1 else t[x>>1] for x in range(2*len(t)))
def transaction(t,q,j,new):
 p,_=spec(t);ts,cc,old,E,O=step(t,tuple(range(len(t).bit_length()-1)),q,j);ps=[spec(z)[0] for z in ts]
 pe=marginal(p,j);qe=marginal(q,j)
 out=[sum(v*(ps[b].get(s,F(0))/(2*pe[s]) if pe.get(s,F(0)) else F(1,2)) for s,v in qe.items()) for b in [0,1]]
 oldK=scale(add(*(kl(p,o) for p,o in zip(ps,old))),F(1,2));newK=scale(add(*(kl(p,n) for p,n in zip(ps,new))),F(1,2))
 sigma=add(newK,scale(oldK,-1));chain=bounds(add(kl(p,q),sigma,scale(E,-1),scale(O,-1),scale(newK,-1)))
 ck(chain[0]<=0<=chain[1] and chain[1]-chain[0]<F(1,1<<80))
 ck(set(q)==set(p));ck(all(set(o)==set(n)==set(p) for p,o,n in zip(ps,old,new)))
 return ts,ps,old,out,sigma
def one(r,a,balanced,mode):
 t=family(r,balanced);q=fresh(t,a);children=[restrict(t,0,b) for b in [0,1]];pc=[spec(z)[0] for z in children]
 d=F(1,1<<r);u=0 if balanced else 4*d*d;c=a*(1-u);beta=1-a;tscalar=[4*d*d,36*d*d];E=20*d*d
 for b in [0,1]:
  ck(F(sum(children[b]),len(children[b]))==(0 if balanced else -2*d))
  ck(pc[b][len(children[b])-1]==tscalar[b]);ck(len(pc[b])==1<<r)
  ck(all(any(s>>j&1 for s in pc[b]) for j in range(len(children[b]).bit_length()-1)))
 p,I=spec(t);ck(sum(v for s,v in p.items() if s&1)==2*d);ck(p[len(t)-1]==4*d*d)
 ck(all(any(s>>j&1 for s in p) for j in range(len(t).bit_length()-1)))
 gamma=add(*(scale(lv((beta+c/E)/(beta+c/tb)),tb/2) for tb in tscalar));ck(bounds(gamma)[0]>=0)
 new=[fresh(z,a) for z in children]
 pure=mode==0
 if not pure:
  actual=activate(t,mode);oldq=lift(t,q,mode);new=[lift(z,n,mode) for z,n in zip(children,new)];j=1
 else:actual=t;oldq=q;j=0
 actual_children,ps,olds,outs,sigma=transaction(actual,oldq,j,new)
 eta=F(4,5)*c*(1 if pure else F(1,2));expected_out=[(1-eta)/2,(1+eta)/2];ck(outs==expected_out)
 normalizer=kl({0:F(1,2),1:F(1,2)},{0:outs[0],1:outs[1]})
 predicted=add(normalizer,scale(gamma,1 if pure else F(1,2)))
 diff=bounds(add(sigma,scale(predicted,-1)));ck(diff[0]<=0<=diff[1] and diff[1]-diff[0]<F(1,1<<80))
 for b in [0,1]:
  full=(1<<(r+int(balanced)))-1;Lb=beta+c/tscalar[b];LE=beta+c/E
  for s,pv in ps[b].items():
   v=s if pure else s>>1
   ratio=(LE/Lb if v==full else F(1))/(2*outs[b])
   ck(olds[b][s]/new[b][s]==ratio)
 lo,hi=bounds(sigma);ck(lo>eta*eta/2)
 if a==F(1,6):ck(lo>(F(1,128) if pure else F(1,512)))
 _,ii=spec(actual);influence=sum(v for s,v in spec(actual)[0].items() if s>>j&1);ck(influence==(2*d if pure else d))
 row={'r':r,'alpha':str(a),'balanced':balanced,'mode':'core' if pure else 'activation','epsilon':None if pure else mode,'dimension':len(actual).bit_length()-1,'queried_influence':str(influence),'actual_reference_outcomes':list(map(str,outs)),'sigma_interval':list(map(str,(lo,hi))),'Gamma_interval':list(map(str,bounds(gamma))),'normalizer_interval':list(map(str,bounds(normalizer))),'ratio_lower':str(lo/influence),'same_essential_mask':True,'same_source_reference_support':True,'all_physical_children_retained':True,'source_query_reset_full_KL_identity':'exact atom likelihood products plus telescoping; interval equality diagnostic only'}
 save(('PILOT_' if '--pilot' in sys.argv else '')+f'CASE_r{r}_a{a.numerator}-{a.denominator}_b{int(balanced)}_m{mode}.json',row);return row
if __name__=='__main__':
 assert (ROOT/'FROZEN_SPEC.json').exists()
 pilot='--pilot' in sys.argv
 rows=[one(r,a,b,m) for r in ([4] if pilot else [4,5,6,7]) for a in ([F(1,6)] if pilot else [F(1,6),F(1,7)]) for b in [False,True] for m in [0,-1,1]]
 result={'status':'PASS','cases':len(rows),'assertions':COUNT,'physical_query_nodes':NODES,'runtime_seconds':time.perf_counter()-START,'rows':rows,'formal_status':'analytic proof with exact checks, no formal verification claimed'}
 save('PILOT.json' if pilot else 'CHECK.json',result);print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
