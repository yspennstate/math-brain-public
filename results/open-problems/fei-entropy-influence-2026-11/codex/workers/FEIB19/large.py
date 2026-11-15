"""Large symbolic-width towers; no truth-table expansion."""
import math,json,os,time,resource,itertools,sys
import numpy as np
import mpmath as mp
from experiment import phi,best_order,masses
mp.mp.dps=85
M=mp.mpf;ln2=mp.log(2)
def lc(x):return mp.log1p(-mp.exp(x)) if x<-1 else mp.log(-mp.expm1(x))
def P(a,b):
    if not a or not b:return M(0)
    return (a*mp.log1p(b/a)+b*mp.log1p(a/b))/ln2

class Stable:
    def __init__(self):self.lp=self.lq=-ln2;self.ld=self.lc=M(0);self.TL=self.TE=M(0);self.n=1
    def empty(self):
        p=mp.exp(self.lp);b=1-2*p;c=mp.exp(self.lc);d=mp.exp(self.ld)
        return P(b*b,c*c)/d
    def ratio(self):return self.TL+self.empty(),self.TE+self.empty()
    def step(self,k,kind):
        if kind=='XOR':
            FL,FE=self.ratio();p=mp.exp(min(self.lp,self.lq));lb=mp.log1p(-2*p) if p<M('.5') else mp.ninf
            sign=-1 if self.lp>self.lq else 1
            logsmall=lc(k*lb)-ln2 if lb!=mp.ninf else -ln2
            loglarge=mp.log1p(mp.exp(k*lb))-ln2 if lb!=mp.ninf else -ln2
            self.lp,self.lq=(logsmall,loglarge) if sign**k>0 else (loglarge,logsmall)
            self.lc+=(k-1)*lb;self.n*=k
            new=self.empty();self.TL=FL-new;self.TE=FE-new;return
        lp,lq=(self.lp,self.lq) if kind=='AND' else (self.lq,self.lp)
        p=mp.exp(lp);c=mp.exp(self.lc);d=mp.exp(self.ld);la=(k-1)*lp
        inc=(-mp.expm1(la))*P(4*p*p,c*c)/d
        self.TL+=inc;self.TE+=inc
        newp=k*lp;newq=lc(newp)
        self.lp,self.lq=(newp,newq) if kind=='AND' else (newq,newp)
        self.ld+=la;self.lc+=la;self.n*=k
    def row(self,name):
        F,E=self.ratio()
        return dict(name=name,n=self.n,F=float(F),E=float(E),gap=float(F-E),log2_influence=str(self.ld/ln2),log2_small_probability=str(min(self.lp,self.lq)/ln2))

def andor():
    rows=[]
    for k in [2,3,4,5,10,100,1000]:
        for first in ['AND','OR']:
            a=Stable()
            for depth in range(1,5):
                a.step(k,first if depth%2 else ('OR' if first=='AND' else 'AND'));rows.append(a.row(f'{first}_alternation_width{k}_depth{depth}'))
    for w,s in [(2,7),(2,8),(3,6),(3,18),(10,1000),(100,1000),(1000,1000)]:
        a=Stable()
        for depth in range(1,5):
            a.step(w,'AND');a.step(s,'OR');rows.append(a.row(f'tribes({w},{s})_tower{depth}'))
    for seq in [('AND','OR','XOR'),('XOR','OR','AND','OR'),('OR','AND','XOR','OR')]:
        for k in [2,3,10,1000]:
            a=Stable()
            for kind in seq:a.step(k,kind)
            rows.append(a.row(f'{seq}_width{k}'))
    return rows

def majority_bins(n):
    r=(n-1)//2
    def logchoose(n,k):return math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)
    ld=logchoose(2*r,r)-2*r*math.log(2);la=np.full(n+1,-np.inf)
    for s in range(r+1):la[2*s+1]=2*(ld+logchoose(r,s)-logchoose(2*r,2*s))
    A=np.zeros(n);B=np.zeros(n);B[0]=math.exp(la[1])
    for k in range(1,n):
        for d in range(1,k+1):
            l=logchoose(k-1,d-1)
            if math.isfinite(la[d]):A[k]+=math.exp(l+la[d])
            if math.isfinite(la[d+1]):B[k]+=math.exp(l+la[d+1])
    return math.exp(ld),A,B

def majorities():
    rows=[]
    for n in [3,5,7,9,15,31,101,301,999]:
        alpha,A,B=majority_bins(n);c=1.;F=0.
        for depth in range(1,41):
            inc=float(phi(A,c*c*B).sum())/(alpha*c);F+=inc;c*=alpha
            if depth in [1,2,3,4,10,20,40]:rows.append(dict(name=f'MAJ{n}_tower{depth}',n=n**depth,depth=depth,arity=n,F=F,E=0.,gap=F,increment=inc,influence=c,alpha=alpha))
    return rows

def and_majorities():
    rows=[]
    for r in [3,5,7,9,31,101,999]:
        alpha,A,B=majority_bins(r);F=float(phi(A,B).sum())/alpha
        for w in [2,3,10,100,1000]:
            a=Stable();a.n=r;a.ld=a.lc=mp.log(alpha);a.TL=mp.mpf(F);a.TE=mp.mpf(0);a.step(w,'AND')
            rows.append(a.row(f'AND{w}_MAJ{r}'))
    return rows

def pm(depthmax=20):
    spec=np.load('../FEIB16/pm_record_spectrum.npy');mu=spec**2;alph=[57/256,1/256];pairs=[masses(mu,i) for i in [0,9]]
    scores=[0.];ers=[0.];paths=[''];rows=[]
    for depth in range(1,depthmax+1):
        new=[math.inf]*(depth+1);ne=[math.inf]*(depth+1);npth=['']*(depth+1)
        for core in range(depth):
            delta=alph[0]**core*alph[1]**(depth-1-core)
            for j,(p,q) in enumerate(pairs):
                val=best_order(p,delta*delta*q)[0]/(alph[j]*delta)
                ev=float(phi(p,delta*delta*q).sum())/(alph[j]*delta);r=core+(j==0)
                if scores[core]+val<new[r]:new[r]=scores[core]+val;npth[r]=paths[core]+('C' if j==0 else 'K')
                ne[r]=min(ne[r],ers[core]+ev)
        scores,ers,paths=new,ne,npth
        j=int(np.argmin(scores));rows.append(dict(depth=depth,n=18**depth,F=min(scores),E=min(ers),gap=min(scores)-min(ers),path_bottom_to_top=paths[j],states=[dict(core=r,F=scores[r],E=ers[r]) for r in range(depth+1)]))
        print('PM',depth,min(scores),min(ers),flush=True)
    # A fixed order at c=1 gives a uniform upper bound for all later increments.
    constants=[]
    for p,q in pairs:
        _,order=best_order(p,q)
        from experiment import zeta
        a,b=zeta(p),zeta(q);R=0;As=[a[0]];Bs=[b[0]]
        for j in order:
            old=R;R|=1<<j;As.append(max(0,a[R]-a[old]));Bs.append(max(0,b[R]-b[old]))
        alpha=float(sum(Bs));C=1/math.log(2)
        for A,B in zip(As,Bs):
            if B:C+=B*math.log2(1+A/B)/alpha
        constants.append(C)
    aa=max(alph);q=depthmax
    tail=aa**q*(2*math.log2(1/aa)*(q/(1-aa)+aa/(1-aa)**2)+max(constants)/(1-aa))
    return dict(rows=rows,C_fixed_orders=constants,tail_upper=tail,F_interval=[rows[-1]['F'],rows[-1]['F']+tail],E_interval=[rows[-1]['E'],rows[-1]['E']+tail],rounding='ordinary binary64, analytic tail bound; not directed rounding')

if __name__=='__main__':
    start=time.time();mode=sys.argv[1]
    data=pm() if mode=='pm' else dict(andor=andor(),majority=majorities(),and_majority=and_majorities())
    out=dict(mode=mode,precision=85,seconds=time.time()-start,nice=os.getpriority(os.PRIO_PROCESS,0),maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,data=data)
    json.dump(out,open(mode+'.json','w'),indent=2)
    if mode!='pm':print(json.dumps(data,indent=2))
