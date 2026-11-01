"""Independent direct character sums and ordered reference transport."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
import arith as A
ROOT=Path(__file__).resolve().parents[1];START=time.perf_counter();N=0
def ck(b,s):
 global N
 N+=1
 if not b:raise AssertionError(s)
def add(*x):return A.plus(*x)
def nn(x,s):ck(not x or A.interval(x)[0]>=0,s)
def ent(p):return add(*[(-v,A.log(v)) for v in p if v])
def kl(p,q):
 ck(len(p)==len(q) and sum(p)==sum(q)==1,'independent KL normalization')
 ck(all(not x or y>0 for x,y in zip(p,q)),'source support')
 return add(*[(x,A.log(x/y)) for x,y in zip(p,q) if x])
def insert(s,j,b):return (s% (1<<j))+((s//(1<<j))<<(j+1))+(b<<j)
def child(t,j,b):return tuple(t[insert(s,j,b)] for s in range(len(t)//2))
@lru_cache(None)
def stats(t):
 size=len(t);n=size.bit_length()-1
 w=[sum(t[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(size)) for s in range(size)]
 p=tuple(F(z*z,size*size) for z in w);ck(sum(p)==1,'direct Parseval')
 ds=tuple(F(sum(t[x]!=t[x^(1<<j)] for x in range(size)),size) for j in range(n))
 for j in range(n):ck(ds[j]==sum(p[s] for s in range(size) if s>>j&1),'direct physical versus direct Fourier influence')
 H=ent(p);M=add(*[(1,ent([d,1-d])) for d in ds]);TC=add((1,M),(-1,H));nn(TC,'full actual total correlation')
 return p,ds,H,M,TC
def transport(t,Q,j):
 p,ds,H,M,TC=stats(t);n=len(t)//2;K=kl(p,Q)
 pe=[p[insert(s,j,0)]+p[insert(s,j,1)] for s in range(n)];qe=[Q[insert(s,j,0)]+Q[insert(s,j,1)] for s in range(n)]
 ts=[child(t,j,b) for b in [0,1]];ps=[stats(z)[0] for z in ts];r=[];Qs=[]
 for b in [0,1]:
  raw=[qe[s]*(ps[b][s]/(2*pe[s]) if pe[s] else F(1,2)) for s in range(n)];rb=sum(raw);ck(rb>0,'positive predicted outcome');r.append(rb);Qs.append(tuple(x/rb for x in raw))
 ck(sum(r)==1,'predictions normalized')
 ks=[kl(ps[b],Qs[b]) for b in [0,1]];O=add((F(-1,2),A.log(4*r[0]*r[1])));E=add((1,K),(-1,kl(pe,qe)))
 ck(not add((1,K),(-1,E),(-1,O),(F(-1,2),ks[0]),(F(-1,2),ks[1])),'direct exact KL chain')
 nn(E,'direct erasure KL nonnegative');nn(O,'direct outcome KL nonnegative')
 return ts,Qs,r,E,O,ks
def product(ds):
 result=[]
 for s in range(1<<len(ds)):
  a=F(1)
  for j,d in enumerate(ds):a*=d if s>>j&1 else 1-d
  result.append(a)
 return tuple(result)
def walk(t,Q,g,ids,cids,seq,path):
 if not seq:return t,Q,g,ids,cids
 j=ids.index(seq[0]);who=ids[j];ts,Qs,r,E,O,ks=transport(t,Q,j)
 gm=stats(g)[3];gs=[g,g] if who==0 else [child(g,cids.index(who),b) for b in [0,1]]
 PP=add((1,kl(stats(t)[0],Q)),(2,gm));pcs=[add((1,ks[b]),(2,stats(gs[b])[3])) for b in [0,1]]
 nn(add((1,PP),(F(-1,2),pcs[0]),(F(-1,2),pcs[1]),(-1,O)),'independent u/core pre-query drift')
 b=path[0];ci=cids if who==0 else [x for x in cids if x!=who]
 return walk(ts[b],Qs[b],gs[b],ids[:j]+ids[j+1:],ci,seq[1:],path[1:])
def main():
 counts={'entries':0,'pivot_cuts':0,'reset_children':0,'post_reset_queries':0};witness=None
 for code in [0,1,3,6,7,15]:
  g=tuple(-1 if code>>s&1 else 1 for s in range(4))
  for lm in range(4):
   for c in [0,1]:
    t=tuple(g[s>>2]*(-1 if (((s&1)+((s>>2)&lm).bit_count()+c)&1)*((s>>1)&1) else 1) for s in range(16))
    for ref in ['uniform','ascending']:
     Q=(F(1,16),)*16 if ref=='uniform' else tuple(F(s+1,136) for s in range(16));counts['entries']+=1
     for seq in [[],[0],[2],[0,2],[2,0]]:
      for outcome in range(1<<len(seq)):
       path=[(outcome>>j)&1 for j in range(len(seq))]
       a,R,h,ids,cids=walk(t,Q,g,list(range(4)),[2,3],seq,path)
       K=kl(stats(a)[0],R);_,_,hh,mm,tt=stats(h);P=add((1,K),(2,mm))
       bs,Rs,r,E,O,ks=transport(a,R,ids.index(1));counts['pivot_cuts']+=1
       if r[0]!=F(1,2) and witness is None:
        ck(4*r[0]*r[1]<1,'nonzero-O rational sign');nn(O,'nonzero-O certified enclosure')
        witness={'core_code':code,'L_mask':lm,'c':c,'reference':ref,'query_ids':seq,'outcomes':path,'r':[str(x) for x in r],'O':A.value(O)}
       meanpre=add((F(1,2),add((1,ks[0]),(2,mm))),(F(1,2),add((1,ks[1]),(2,mm))))
       ck(not add((1,P),(-1,meanpre),(-1,E),(-1,O)),'direct pivot pre-reset boundary exact')
       for b in [0,1]:
        pp,dd,HH,MM,TT=stats(bs[b]);ck(HH==hh and MM==mm and TT==tt,'direct character boundary H/M/TC')
        Qnew=product(dd);ck(kl(pp,Qnew)==TT,'direct actual product reset');V=add((1,TT),(1,MM));Pold=add((1,ks[b]),(2,mm))
        ck(not add((1,Pold),(-1,V),(-1,ks[b]),(-1,hh)),'direct signed reset identity');nn(add((1,Pold),(-1,V)),'direct reset nonincrease');counts['reset_children']+=1
        for j in range(len(dd)):
         zs,Qs,rr,ee,oo,kk=transport(bs[b],Qnew,j);vv=[];counts['post_reset_queries']+=1
         for bb in [0,1]:
          p0,d0,H0,M0,T0=stats(zs[bb]);v0=add((1,kk[bb]),(1,M0));vv.append(v0)
          nn(add((1,v0),(-1,T0)),'full final product KL');nn(add((1,v0),(-1,kk[bb])),'full inherited KL');ck(not add((1,H0),(1,v0),(-1,H0),(-1,kk[bb]),(-1,M0)),'full terminal entropy retained')
         nn(add((1,V),(F(-1,2),vv[0]),(F(-1,2),vv[1]),(-1,oo)),'direct post-reset continuation drift')
 ck(counts=={'entries':96,'pivot_cuts':1248,'reset_children':2496,'post_reset_queries':3648},'independent frozen coverage');ck(witness is not None,'test exercises genuinely nonzero pivot O')
 # Fixed negative control: dropping affinity is actually false, not merely unproved.
 t=tuple(-1 if s==15 else 1 for s in range(16));p=stats(t)[0]
 ck(p[0]==F(49,64) and all(x==F(1,64) for x in p[1:]),'actual4-bit point source')
 ts,Qs,r,E,O,ks=transport(t,p,0);ck(not E and not O and not ks[0] and not ks[1],'source-reference exact zero KLs before non-affine reset')
 ck(not stats(ts[0])[4],'zero child TC');TC=stats(ts[1])[4];formula=add((1,A.const(2)),(F(-9,8),A.log(F(3))))
 ck(TC==formula,'actual non-affine child TC closed form');ck(2**16>3**9,'strict negative-control integer certificate');nn(TC,'positive TC enclosure')
 negative={'function':'F(v,y)=(-1)^(v*y0*y1*y2), constant core g=1, Q=p_F','K_entry':0,'M_core_entry':0,
 'expected_reset_KL':A.value(add((F(1,2),TC))),'failure':'Expected reset KL>0 despite zero K+2Mcore; child phase is non-affine, outside theorem.'}
 elapsed=time.perf_counter()-START;ck(elapsed<55,'direct frozen runtime')
 out={'status':'PASS','direct_assertions':N,'auxiliary_scalar_assertions':A.COUNT,'seconds':elapsed,'counts':counts,'nonzero_pivot_O_witness':witness,'non_affine_negative_control':negative}
 (ROOT/'out/DIRECT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
if __name__=='__main__':main()
