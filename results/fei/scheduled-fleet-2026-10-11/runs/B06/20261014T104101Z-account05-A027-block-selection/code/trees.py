import exact as x
import json,time
from fractions import Fraction as Q
from pathlib import Path
run=Path(__file__).resolve().parents[1]; trees=0
cores=[(1,)*32]+[tuple(-1 if j==k else 1 for j in range(32)) for k in range(32)]
for u in cores:
    coreleafH=x.add(*[(Q(1,4),x.H(x.restrict(u,((0,a),(1,b))))) for a in (0,1) for b in (0,1)])
    corePi=x.add((1,x.H(u)),(-1,coreleafH))
    for r in (1,2,3):
        p=Q(1,1<<r); f=x.identity(u,(-1,)+(1,)*((1<<r)-1))
        orders=[(0,1),(0,5,1),(5,0,1),tuple(range(5,5+r))+(0,1)]
        for order in orders:
            leafH={}; leafI=Q(0); qcore=qctrl=Q(0); localcore={}
            def rec(depth,fixed,w):
                global leafH,leafI,qcore,qctrl,localcore
                fv=x.restrict(f,tuple(fixed)); cf=tuple((i,b) for i,b in fixed if i<5)
                uv=x.restrict(u,cf); nv=r-sum(i>=5 for i,b in fixed); pv=Q(1,1<<nv)
                if depth==len(order) or any(i>=5 and b==1 for i,b in fixed):
                    leafH=x.add((1,leafH),(w,x.H(fv))); leafI+=w*x.I(fv); return
                i=order[depth]; local_i=i-sum(j<i for j,b in fixed)
                f0=x.restrict(f,tuple(fixed+[(i,0)])); f1=x.restrict(f,tuple(fixed+[(i,1)]))
                decrement=x.add((1,x.H(fv)),(Q(-1,2),x.H(f0)),(Q(-1,2),x.H(f1)))
                q=w*x.inf(fv,local_i)
                if i<5:
                    qcore+=q; uc0=x.restrict(u,tuple(sorted(cf+((i,0),)))); uc1=x.restrict(u,tuple(sorted(cf+((i,1),))))
                    d0=x.neg(uc0); d1=x.neg(uc1)
                    x.check(all(d<=Q(1,2) and 1-8*d+8*d*d>=0 for d in (d0,d1)),'tree core children inside sharp band')
                    delta=x.add((1,x.H(uv)),(Q(-1,2),x.H(uc0)),(Q(-1,2),x.H(uc1)))
                    err=x.add((1,decrement),(-pv,delta)); x.check(x.bounds(err)[1]<=0,'actual tree signed core correction nonpositive')
                    localcore=x.add((1,localcore),(w,err))
                else:
                    qctrl+=q; x.check(x.bounds(decrement)[1]<=6*x.inf(fv,local_i),'own physical control allowance six')
                rec(depth+1,fixed+[(i,0)],w/2); rec(depth+1,fixed+[(i,1)],w/2)
            rec(0,[],Q(1))
            x.check(x.I(f)==qcore+qctrl+leafI,'complete interleaved influence partition')
            error=x.add((1,x.H(f)),(-1,leafH),(-p,corePi))
            x.check(x.bounds(error)[1]<=6*qctrl,'interleaved zero-core-surcharge transfer')
            x.check(x.bounds(localcore)[1]<=0,'accumulated signed refund not renewed')
            trees+=1
result={'status':'PASS','trees':trees,'assertions':sum(x.counts.values()),'counts':x.counts,'elapsed_seconds':time.monotonic()-x.START,'max_dimension':8,'all_trees_proper_core':True}
(run/'out'/'trees.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8'); print(json.dumps(result))
