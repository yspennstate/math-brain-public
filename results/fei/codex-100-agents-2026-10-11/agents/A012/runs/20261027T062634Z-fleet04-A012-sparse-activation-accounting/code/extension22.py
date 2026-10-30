import projection22 as m
from fractions import Fraction as F
from itertools import product
import json,time
start=time.monotonic();conversions=0;activations=0
def calibrate(p,q,cells,t):
    pp={};qq={}
    for a in set(p)|set(q):
        c=cells(a);pp[c]=pp.get(c,F(0))+p.get(a,F(0));qq[c]=qq.get(c,F(0))+q.get(a,F(0))
    rr={c:(1-t)*v+t*pp.get(c,F(0)) for c,v in qq.items()}
    r={a:v*rr[cells(a)]/qq[cells(a)] for a,v in q.items() if v and rr[cells(a)]}
    return r,pp,qq,rr
for n in range(4):
    for tt in range(2**(2**n)):
        root=m.spectrum(tt,n,(2,)*n)
        for kind in range(4):
            q=m.reference(root,n,kind)
            for cells in (lambda a:int(a!=0),lambda a:a):
                for t in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
                    r,pb,qb,rb=calibrate(root,q,cells,t)
                    debit=m.divergence(r,q)
                    saving=m.add(m.divergence(root,q),m.scale(m.divergence(root,r),-1),m.scale(debit,-1))
                    m.check(sum(r.values())==1);m.check(m.nonnegative(saving))
                    if t not in (0,1):
                        # t<1 retains all formerly positive cells.
                        rhs=m.scale(m.add(m.divergence(rb,qb),m.divergence(qb,rb)),(1-t)/t)
                        m.check(saving==rhs)
                    else:m.check(saving=={})
                    conversions+=1
        if root.get(0,F(0))!=0:continue
        for rwidth in range(1,4):
            p=F(1,2**rwidth);dim=n+rwidth
            # Inactive +1; active output is the actual original core.
            table=0
            for x in range(2**dim):
                active=(x&((1<<rwidth)-1))==((1<<rwidth)-1)
                value=((tt>>(x>>rwidth))&1) if active else 1
                table|=value<<x
            pf=m.spectrum(table,dim,(2,)*dim)
            overhead=m.add(m.logform(F(2),2*rwidth*p*(2-p)),m.logform((1-p)**2,-(1-p)**2))
            m.check(m.entropy(pf)==m.add(overhead,m.scale(m.entropy(root),p)))
            m.check(m.infl(pf)==p*(m.infl(root)+rwidth))
            for kind in range(4):
                q=m.reference(pf,dim,kind)
                qdata=sum((v for a,v in q.items() if a>>rwidth),F(0))
                induced={}
                for a,v in q.items():
                    data=a>>rwidth
                    if data:induced[data]=induced.get(data,F(0))+v/qdata
                # Exact chain decomposition on the data event.
                remainder=m.add(m.divergence(pf,q),m.scale(m.divergence(root,induced),-p))
                m.check(m.nonnegative(remainder));m.check(sum(induced.values())==1)
                activations+=1
result={'status':'PASS','conversions':conversions,'activation_reference_cases':activations,'assertions':m.COUNT,'elapsed_seconds':time.monotonic()-start,'negative_controls':'zero Q cells omitted only when true mass zero; t=1 removes ghost cells with full KL fee; t=0 is exactly unchanged'}
(m.RUN/'out/EXTENSION.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
