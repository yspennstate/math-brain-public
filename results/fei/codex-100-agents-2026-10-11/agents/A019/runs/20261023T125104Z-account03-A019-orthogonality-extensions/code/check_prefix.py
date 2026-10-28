import sys,json,time,importlib.util,hashlib
from pathlib import Path
from fractions import Fraction as Q
R=Path(__file__).resolve().parents[1]
P=R.parent/'20261023T105439Z-account03-A019-orthogonality-extensions/code/check_events.py'
sp=importlib.util.spec_from_file_location('a019_primitives',P)
h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
ck,add,lf,scale,const=h.ck,h.add,h.lf,h.scale,h.const

def influence(t):
    return sum(Q(sum(t[i]!=t[i^(1<<j)] for i in range(len(t))),len(t)) for j in range(len(t).bit_length()-1))

def fixture(k,m):
    rho=Q(1,1<<k);labels=['u']+['v'+str(i) for i in range(k)]+['s%d_%d'%(s,j) for s in range(m) for j in range(3)]
    def val(i):
        g=1
        for s in range(m):
            if all(not(i>>(1+k+3*s+j)&1) for j in range(3)):g=-g
        event=all(not(i>>(1+j)&1) for j in range(k)) and g==-1
        return 1 if event else 1-2*(i&1)
    tt=tuple(val(i) for i in range(1<<len(labels)));ref=h.contam(h.spectrum(tt))
    p=rho*(1-Q(3,4)**m)/2
    avgcost={};avgdebt={};avgclean={};avgi=Q(0);reach=Q(0);count=0
    def branch(t,r,l,s,j,weight,rg,eps):
        nonlocal avgcost,avgdebt,avgclean,avgi,reach,count
        if s==m:
            count+=1;reach+=weight;pp=h.spectrum(t);active=[i for i in range(len(pp)) if any(i>>l.index('s0_'+str(z))&1 for z in range(3))]
            mass=sum(pp[i] for i in active);ck(mass==7*rho/32)
            ck(all(r[i]==pp[i]*rg/2 for i in active if pp[i]));ck(influence(t)==sum(v*i.bit_count() for i,v in enumerate(pp)))
            ck(all(pp[i]==rho*rho/64 for i in active if pp[i]))
            sector=h.ce(tuple(pp[i] for i in active),tuple(r[i] for i in active))
            ck(sector==scale(mass,add((1,const(2*k+7)),(-1,lf(rg)))))
            debt=scale(-mass/2,lf(rg));c=h.actcost(t,r)
            ck(h.nonneg(add((1,c),(-1,debt))))
            # Cleanup ALL retained ghost coordinates; both physical children coincide.
            clean_t,clean_r,clean_l=t,r,list(l)
            ghosts=[x for x in l if x.startswith('s') and not x.startswith('s0_')]
            for name in ghosts:
                z=clean_l.index(name);a=h.restrict(clean_t,z,0);b=h.restrict(clean_t,z,1);ck(a==b)
                clean_t=a;clean_r=h.fold(clean_r,z);clean_l.pop(z)
            clean_cost=h.actcost(clean_t,clean_r)
            release=add((1,c),(-1,clean_cost));ck(h.nonneg(add((1,release),(-1,debt))))
            cq=h.spectrum(clean_t);ck(all(clean_r[i]==cq[i]/2 for i in range(len(cq)) if any(i>>clean_l.index('s0_'+str(z))&1 for z in range(3))))
            a=rho*(1-Q(3,4)*eps)/2;actual=4+2*influence(t)-Q(sum(t),len(t))
            ck(actual==6+3*rho/4+(2*k-3)*a)
            avgi+=weight*actual;avgcost=add((1,avgcost),(weight,c));avgdebt=add((1,avgdebt),(weight,debt));avgclean=add((1,avgclean),(weight,clean_cost))
            if count==1:
                ap,aq=h.actual_act(t,r);ck(h.ce(ap,aq)==c)
                indices=[2*(mask*len(t)+i)+e for mask in range(4) for i in active for e in (0,1)]
                ck(h.ce(tuple(ap[i] for i in indices),tuple(aq[i] for i in indices))==scale(mass/2,add((1,const(2*k+11)),(-1,lf(rg)))))
            return
        name='s%d_%d'%(s,j);z=l.index(name);rr=h.fold(r,z);ll=l[:z]+l[z+1:]
        for b in (0,1):
            child=h.restrict(t,z,b)
            if b==1:
                # j=0 => two unqueried bits, j=1 => one, j=2 => none.
                factor=(Q(5,8),Q(3,4),Q(1))[j]
                branch(child,rr,ll,s+1,0,weight/2,rg*factor,eps)
            elif j==2:branch(child,rr,ll,s+1,0,weight/2,rg,-eps)
            else:branch(child,rr,ll,s,j+1,weight/2,rg,eps)
    branch(tt,ref,labels,1,0,Q(1),Q(1),1)
    ck(reach==1);ck(count==4**(m-1));ck(avgi==6+3*rho/4+(2*k-3)*p)
    lam=add((Q(1,2),lf(Q(8,5))),(Q(1,4),lf(Q(4,3))))
    ck(avgdebt==scale(7*rho*(m-1)/64,lam));ck(h.nonneg(add((1,avgcost),(-1,avgclean),(-1,avgdebt))))
    ck(h.positive(add((1,lam),(-1,const(Q(3,8))))))
    return {'k':k,'m':m,'leaves':count,'q1_average_4I':str(avgi),'q1_cost_interval':h.summary(avgcost),'q1_ghost_debt_interval':h.summary(avgdebt),'q1_cleanup_release_interval':h.summary(add((1,avgcost),(-1,avgclean))),'whole_frontier_4I':str((6+avgi)/2)}

def review_owner():
    # Reconstruct scalar ownership and endpoint directly from complete spectra.
    rows=[]
    for n,supp in [(2,(0,)),(3,(0,)),(3,(0,3))]:
        A=tuple(int(i in supp) for i in range(1<<n));p=Q(len(supp),1<<n);t=h.core(A);t0=tuple(1-2*(i&1) for i in range(len(t)))
        rr=h.contam(h.spectrum(t));r0=h.contam(h.spectrum(t0));parent,qr=h.lift(t0,t,r0,rr)
        c1=h.ce(h.spectrum(t),rr);bank=add((1,const(1+influence(t))),(-Q(1,4),add((1,const(1)),(1,c1))))
        cp=h.actcost(parent,qr);w=add((1,const(4+2*influence(parent)-p/2)),(-1,cp))
        eta=lambda x:scale(-x,lf(x)) if x else {}
        f=lambda x:eta((1-x)**2)
        delta=add((1,f(p/2)),(-Q(1,2),f(p)),(Q(1,4),eta(p*p)),(1,const(2*p-p*p/2)))
        D=scale(p*p/2,lf((2+p*p)/(1+p*p)))
        om=add((1,const(3+p/2)),(-Q(1,2),delta),(Q(1,2),D),(-1,h.psi(p/4)),(1,h.afun(p*p/16,(2+p*p)/32)))
        ck(add((1,w),(-1,bank))==om);ck(h.positive(add((1,const(Q(85,64))),(-1,om))))
        c0=h.actcost(t0,r0);ca=h.actcost(t,rr);tq=add((1,cp),(-Q(1,2),c0),(-Q(1,2),ca),(-1,const(p)))
        ck(h.positive(add((1,const(Q(1,4))),(-1,tq))))
        spent,leaves,_,_=h.tree(A,rr,list(range(n))) # May stop early; not the ALL-bit endpoint!
        # Force every event coordinate for endpoint, even after event determination.
        def allbits(t,r):
            if len(t)==2:return h.actcost(t,r)
            folded=h.fold(r,1)
            return add((Q(1,2),allbits(h.restrict(t,1,0),folded)),(Q(1,2),allbits(h.restrict(t,1,1),folded)))
        L=allbits(t,rr);S=scale(Q(1,2),add((1,ca),(-1,L)));J=2*(influence(t)-1+p)
        wf=add((1,w),(1,tq),(1,S),(-1,const(J/2+Q(1,8))))
        endpoint=add((1,const(6-3*p/2-Q(1,8))),(-Q(1,2),c0),(-Q(1,2),L))
        ck(wf==endpoint);ck(h.positive(add((1,wf),(-1,const(2)))))
        rows.append({'n':n,'support':list(supp),'Omega_interval':h.summary(om),'Tq_interval':h.summary(tq),'finished_reserve_interval':h.summary(wf)})
    ck(545**8<2*512**8);ck(290**8<2*273**8)
    return rows

def main():
    start=time.perf_counter();pilot='--pilot' in sys.argv
    cases=[fixture(*z) for z in ([(1,2)] if pilot else [(1,2),(2,2),(1,3)])]
    ck(75**2<2**13);ck(Q(97,4096)<Q(1,2))
    witness=6+Q(97,4096)-Q(21,2);ck(witness<-4)
    review=[] if pilot else review_owner()
    elapsed=time.perf_counter()-start;assert elapsed<60
    out={'status':'PASS','assertions':h.ns['checks'],'cases':cases,'review_cases':review,'lambda_integer_certificate':{'left':75**2,'right':2**13,'strict':75**2<2**13},'k8_family_reserve_upper':str(witness),'seconds':elapsed,'helper_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'full_FEI':'OPEN','scope_note':'Literal finite tests verify formulas; the infinite theorem is the displayed analytic derivation, not finite sampling.'}
    (R/'out'/('PILOT.json' if pilot else 'CHECKS.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({'status':'PASS','assertions':out['assertions'],'cases':len(cases),'review_cases':len(review),'seconds':elapsed}))
if __name__=='__main__':main()
