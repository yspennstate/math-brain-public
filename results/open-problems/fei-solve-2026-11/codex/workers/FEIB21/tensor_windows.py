"""Exact block moments, summed directly or by Gauss quadrature over block position.
Only local files are written. Quadrature is numerical, not directed-rounding certification.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
import math,json,time,resource,sys
from decimal import Decimal,localcontext,getcontext
import numpy as np
getcontext().prec=85
Z=Decimal(0);ONE=Decimal(1);TWO=Decimal(2)

def phi(p,q):
    if p<=0 or q<=0:return 0.
    # Stable when one mass is much smaller than the other.
    if p<q:p,q=q,p
    p,q=float(p),float(q)
    return (p*math.log1p(q/p)+q*math.log1p(p/q))/math.log(2)

class Moments:
    def __init__(self,L,D):
        getcontext().prec=max(100,L)
        self.L,self.D=L,D
        a=TWO**(-L);q=1-(1-a)**(D-1)
        self.a,self.q=a,q
        self.nn=[(1-q/2)**(L-r)*(1-3*q/4)**r for r in range(L+1)]
        self.b=((1-q)/2)**L
        self.nm=[v-self.b for v in self.nn]
        self.mm=[self.nn[r]-2*self.b+self.b*TWO**(-r) for r in range(L+1)]
        self.A=self.nn[0]**D;self.B=self.nm[0]**D
        self.delta=self.A-self.B
    def base(self,k,t):
        D=self.D
        return tuple(tab[k]**(D-t)*tab[k+1]**t for tab in (self.nn,self.nm,self.mm))
    def wg(self,base,k,t,mods=()):
        vals=list(base)
        for r,num in mods:
            for j,tab in enumerate((self.nn,self.nm,self.mm)):
                vals[j]*=tab[r-num]/tab[r]
        a,b,c=vals
        return a-2*b+c,a+2*b+c-2*(self.A+self.B)+1
    def evaluate(self,quadrature=0,rmax=2):
        L,D=self.L,self.D
        final=tuple(tab[L]**D for tab in (self.nn,self.nm,self.mm))
        w0,g0=self.wg(final,L,0)
        none=phi(g0,w0)
        out1=none
        w1,g1=self.wg(final,L,0,((L,1),))
        single=D*L*phi(g1-g0,w1-w0)
        out2=none+single
        out3=out2
        if rmax>=3:
            for same,mult in [(True,D*L*(L-1)/2),(False,D*(D-1)*L*L/2)]:
                mods=((L,2),) if same else ((L,1),(L,1))
                wp,gp=self.wg(final,L,0,mods)
                out3+=mult*phi(gp-2*g1+g0,wp-2*w1+w0)
        xws=None
        if quadrature:
            xs,ws=np.polynomial.legendre.leggauss(quadrature)
            xws=[(Decimal(str(1+(D-1)*(x+1)/2)),float(w)*(D-1)/2) for x,w in zip(xs,ws)]
            # Euler-Maclaurin/trapezoid endpoint correction: integral over [1,D]
            # plus half endpoints. Error is assessed against independent node counts.
            xws +=[(ONE,.5),(Decimal(D),.5)]
        else:xws=[(Decimal(t),1.) for t in range(1,D+1)]
        for k in range(L):
            for t,weight in xws:
                base=self.base(k,t)
                wf,gf=self.wg(base,k,t)
                wa,ga=self.wg(base,k,t,((k+1,1),))
                out1+=weight*phi(ga-gf,wa-wf)
                if rmax<2:continue
                # earlier first selected coordinate: same block, earlier block, later block
                classes=[(k+1,k,True), (k+1,(t-1)*(k+1),False),(k,(D-t)*k,False)]
                for r,mult,same in classes:
                    if mult<=0:continue
                    wb,gb=self.wg(base,k,t,((r,1),))
                    mods=((k+1,2),) if same else ((k+1,1),(r,1))
                    wc,gc=self.wg(base,k,t,mods)
                    out2+=weight*float(mult)*phi(gc-ga-gb+gf,wc-wa-wb+wf)
                if rmax<3:continue
                # A class describes block count, available positions per block,
                # prefix count per block, and whether it is the new last block.
                groups=[(ONE,k,k+1,True),(t-1,k+1,k+1,False),(D-t,k,k,False)]
                def triple(b1,b2,mult):
                    if mult<=0:return 0.
                    selected=[b1,b2,(0,k+1)]
                    ww=gg=Z
                    for mask in range(8):
                        by={}
                        for j,(bid,rr) in enumerate(selected):
                            if (mask>>j)&1:
                                if bid not in by:by[bid]=[rr,0]
                                by[bid][1]+=1
                        w,g=self.wg(base,k,t,tuple(tuple(v) for v in by.values()))
                        sign=-1 if (3-mask.bit_count())%2 else 1
                        ww+=sign*w;gg+=sign*g
                    return float(mult)*phi(gg,ww)
                for ii,(num,avail,rr,special) in enumerate(groups):
                    bid=0 if special else 1+ii*2
                    if avail>=2:out3+=weight*triple((bid,rr),(bid,rr),num*avail*(avail-1)/2)
                    if num>1:out3+=weight*triple((bid,rr),(bid+1,rr),num*(num-1)/2*avail*avail)
                    for jj in range(ii+1,len(groups)):
                        nb,ab,rb,sb=groups[jj];bidb=0 if sb else 1+jj*2
                        out3+=weight*triple((bid,rr),(bidb,rb),num*nb*avail*ab)
        result=dict(L1=out1/float(self.delta),L2=out2/float(self.delta),none=none/float(self.delta))
        if rmax>=3:result['L3']=out3/float(self.delta)
        return result

def bounds(L,D):
    m=Moments(L,D);A=m.A;delta=m.delta
    eta=Decimal(D)*m.b/m.nn[0]
    rho=m.q/(4-2*m.q)
    alpha=Decimal(math.comb(L,3))*rho**3
    gamma=(TWO**-L)*Decimal(1+L+math.comb(L,2))
    eps=min(ONE,2*A*eta/delta*(eta+D*gamma+D*(D-1)*alpha))
    kap=A*D*alpha/delta
    err=2*float(eps)+8/math.log(2)*math.sqrt(float(kap))
    err+=float(eps)*math.log2(math.e*(3+8*float(A/(eps*delta))))
    dd=float(delta)
    err+=dd*math.log2(math.e*(1+dd**-2))
    return dict(lambda_L=float(Decimal(D*D*L)*TWO**-L),delta=dd,A=float(A),eps=float(eps),kappa=float(kap),erasure_error_bound=err)

def main():
    start=time.time();rows=[]
    if len(sys.argv)>1 and sys.argv[1]=='validate':
        sys.path.insert(0,os.path.abspath('inputs'))
        from tree_dnf import Tree
        for w,D in [(3,2),(4,3),(6,4),(10,8),(12,16),(9,24)]:
            x=Moments(w-1,D).evaluate(rmax=3);T=Tree(w,D);v=T.witness('robin',3)
            residual=max(abs(x['L'+str(r)]-v[r]/float(T.inf_d)) for r in [1,2,3])
            assert residual<1e-8,(w,D,x,v,residual)
            rows.append(dict(w=w,D=D,**x,residual=residual))
    else:
        for L in [9,11,13,15,19,23,31,39,59,79,119,159,239]:
            D=round(math.sqrt(1.4*2**L/L));m=Moments(L,D)
            quad=0 if D<800 else 24
            x=m.evaluate(quad);b=bounds(L,D)
            if quad:
                y=m.evaluate(48);x['quadrature_change']=max(abs(x[k]-y[k]) for k in ['L1','L2']);x.update(y)
            rows.append(dict(w=L+1,D=D,quadrature=quad,**b,**x,L1_offset=x['L1']-math.log2(D),L2_prediction=2+7*b['lambda_L']/16))
            print(json.dumps(rows[-1]),flush=True)
    out=dict(rows=rows,seconds=time.time()-start,nice=os.getpriority(os.PRIO_PROCESS,0),maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    json.dump(out,open('tensor_validate.json' if len(sys.argv)>1 and sys.argv[1]=='validate' else 'tensor_asymptotics.json','w'),indent=2)
    print(json.dumps(out) if len(sys.argv)>1 else 'saved tensor_asymptotics.json',flush=True)
if __name__=='__main__':main()
