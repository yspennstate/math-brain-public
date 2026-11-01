"""Signed triangle; prescribed third reset at a genuinely nonfair private query."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
import argparse,json,time
R=Path(__file__).resolve().parents[1]
CHECKS=0;D=1<<256;LC={}
def ck(b):
    global CHECKS
    assert b
    CHECKS+=1
def rounding(v):
    return F(v[0].numerator*D//v[0].denominator,D),F(-((-v[1].numerator*D)//v[1].denominator),D)
def log(x):
    if x in LC:return LC[x]
    assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length();z=x/F(2)**k
    if z<1:k-=1;z*=2
    assert 1<=z<2
    def ln(z):
        t=(z-1)/(z+1);v=t;s=F(0)
        for j in range(28):s+=v/(2*j+1);v*=t*t
        return 2*s,2*s+2*v/(57*(1-t*t))
    a,b=ln(z);c,d=ln(F(2));ans=(F(k)+a/d,F(k)+b/c);LC[x]=ans
    return ans
def logs(ts):
    a=b=F(0)
    for w,x in ts:
        if not w:continue
        lo,hi=log(x)
        if w<0:lo,hi=hi,lo
        # multiplicity is ALREADY included in w; round only weighted masses.
        lo,hi=rounding((w*lo,w*hi));a+=lo;b+=hi
    return a,b
def add(*xs):return sum(z[0] for z in xs),sum(z[1] for z in xs)
def mul(x,c):return (x[0]*c,x[1]*c) if c>=0 else (x[1]*c,x[0]*c)
def sub(x,y):return add(x,mul(y,-1))
def saved(x):return [str(z) for z in rounding(x)]
def zero(v):ck(v[0]<=0<=v[1])
def subsets(mask):
    z=mask
    while True:
        yield z
        if not z:break
        z=(z-1)&mask

class Triangle:
    def __init__(self,L):
        self.L=L;self.n=2*L+4
        self.private=[8,((1<<L)-1)<<4,((1<<L)-1)<<(L+4)]
        self.clauses=[self.private[0]|1|4,self.private[1]|1|2,self.private[2]|2|4]
        self.U=[]
        for j in range(8):
            u=0
            for k,e in enumerate(self.clauses):
                if j>>k&1:u|=e
            self.U.append(u)
        self.w=[2*F((-1)**j.bit_count(),1<<u.bit_count()) for j,u in enumerate(self.U)]
    @lru_cache(None)
    def coeff(self,S):return sum((w for u,w in zip(self.U,self.w) if not S&~u),F(0))-F(S==0)
    @lru_cache(None)
    def amp(self,h,S):
        fixed=sum(1<<i for i,s in h)
        if S&fixed:return F(0)
        out=F(0)
        for V in subsets(fixed):
            sign=(-1)**sum(s for i,s in h if V>>i&1)
            out+=sign*self.coeff(S|V)
        return out
    def p(self,h,S):return self.amp(h,S)**2
    def labels(self,h=(),erase=0):
        forbidden=erase|sum(1<<i for i,s in h)
        singles=[1<<i for i in range(5) if not forbidden>>i&1]
        blocks=[(self.private[1]&~16)&~forbidden,self.private[2]&~forbidden]
        for flags in product([0,1],repeat=2):
            if any(v and not m for v,m in zip(flags,blocks)):continue
            m=1;rep=0
            for v,b in zip(flags,blocks):
                if v:m*=(1<<b.bit_count())-1;rep|=b&-b
            for pick in range(1<<len(singles)):
                S=rep
                for j,b in enumerate(singles):
                    if pick>>j&1:S|=b
                yield m,S
    def mass(self,h,S,erase=0):return sum((self.p(h,S|V) for V in subsets(erase)),F(0))
    def entropy(self,h=(),erase=0):
        ts=[];total=F(0)
        for m,S in self.labels(h,erase):
            z=self.mass(h,S,erase);total+=m*z
            if z:ts.append((-m*z,z))
        ck(total==1)
        return logs(ts)
    def row(self,h,i):
        bit=1<<i;ms=[];bs=[];e=F(0);total=F(0);cross=F(0)
        for m,S in self.labels(h,bit):
            u,v=self.amp(h,S),self.amp(h,S|bit)
            a,b=u*u,v*v;r=a+b;total+=m*r;e+=m*b;cross+=m*u*v
            if a:bs.append((m*a,r/a))
            if b:bs.append((m*b,r/b));ms.append((m*b,r/b))
        ck(total==1);ck(cross==0)
        return e,logs(ms),logs(bs)
    def cmi(self,h,i,j):
        bi,bj=1<<i,1<<j;ts=[]
        for m,S in self.labels(h,bi|bj):
            z=[[self.p(h,S|(bi if a else 0)|(bj if b else 0)) for b in [0,1]] for a in [0,1]]
            total=sum(sum(r) for r in z)
            if not total:continue
            for a,b in product([0,1],repeat=2):
                p=z[a][b]
                if p:ts.append((m*p,p*total/(sum(z[a])*sum(z[k][b] for k in [0,1]))))
        return logs(ts)
    def js(self,h,i,erase=0):
        bit=1<<i;ts=[]
        for u in [0,1]:
            child=h+((i,u),)
            for m,S in self.labels(child,erase):
                p=self.mass(child,S,erase);r=self.mass(h,S,erase|bit)
                if p:ck(r>0);ts.append((m*p/2,p/r))
        return logs(ts)
    def full_ce(self,h,ref):
        total=F(0);act=F(0);ts=[];ghost=F(0)
        for m,S in self.labels(h):
            p=self.p(h,S);q=ref(S);total+=m*q;act+=m*p
            if p:ck(q>0);ts.append((-m*p,q))
            elif q:ghost+=m*q
        ck(total==act==1)
        return logs(ts),ghost
    def lift(self,h,i,S):
        bit=1<<i
        return (self.p(h,S&~bit)+self.p(h,S|bit))/2
    def nonfair_node(self,h):
        # Incoming Q=fair_a(marg_a p); query y (bit 4).
        _,_,By=self.row(h,4)
        CEold,ghostold=self.full_ce(h,lambda S:self.lift(h,0,S))
        new=[];inc=[];delta_terms=[];normalizer=[]
        for u in [0,1]:
            child=h+((4,u),)
            incoming=lambda S:self.lift(h,0,S)+self.lift(h,0,S|16)
            fresh=lambda S:self.lift(child,2,S)
            ci,gi=self.full_ce(child,incoming);cn,gn=self.full_ce(child,fresh)
            inc.append(ci);new.append(cn);normalizer.append({'outcome':u,'incoming_ghost':str(gi),'fresh_ghost':str(gn),'H_full':saved(self.entropy(child)),'CE_full':saved(cn)})
            for m,S in self.labels(child):
                p=self.p(child,S)
                if p:delta_terms.append((m*p/2,incoming(S)/fresh(S)))
            # Exact signed collapse on all compressed labels.
            for m,S in self.labels(child):
                u0,v0=self.amp(h,S),self.amp(h,S|16)
                ck(self.amp(child,S)==u0+(1 if u==0 else -1)*v0)
        avg=lambda xs:mul(add(*xs),F(1,2))
        rho=self.cmi(h,4,0);Ic=self.cmi(h,4,2);Jc=self.js(h,4,4)
        delta=logs(delta_terms);net=sub(delta,rho)
        zero(sub(rho,sub(CEold,add(By,avg(inc)))))
        zero(sub(delta,sub(avg(new),avg(inc))))
        zero(add(net,Ic,Jc))
        zero(sub(self.row(h,0)[2],self.row(h,2)[2]))
        # Generic nonnegativity is analytic; allow tiny interval overlap at zero.
        ck(rho[1]>=0 and Ic[1]>=0 and Jc[1]>=0)
        bound=add(By,avg(new));zero(sub(sub(bound,CEold),net))
        s,t=dict(h)[3],dict(h)[1]
        if t==0:ck(self.row(h,4)[0]>0)
        # q=1/4 exact witness to a nonfair reference kernel.
        theta=(self.lift(h,0,16)/(self.lift(h,0,0)+self.lift(h,0,16))) if self.lift(h,0,0)+self.lift(h,0,16) else None
        if (s,t)==(1,0):
            q=F(1,1<<self.L);u=1-2*q+q*q/2;v=-q+q*q/2
            ck(theta==2*v*v/(u*u+3*v*v));ck(theta!=F(1,2))
            if self.L==2:ck(theta==F(49,218));ck(rho[0]>0)
        return CEold,bound,{'x':s,'b':t,'rho_actual_conditional_KL':saved(rho),'Delta_prescribed_reset':saved(delta),'net_Delta_minus_rho':saved(net),'CMI_y_c':saved(Ic),'J_y_after_c_marginal':saved(Jc),'kernel_theta_vacuum':str(theta),'old_full_CE':saved(CEold),'new_full_bill':saved(bound),'terminals':normalizer}

def case(L):
    T=Triangle(L);one=(F(1),F(1));oldM=[]
    rootrows=[T.row((),i) for i in [0,1,2,3,4,4+L]]
    M=add(*(mul(z[1],1 if i<4 else L) for i,z in enumerate(rootrows)))
    epriv=rootrows[3][0]+L*(rootrows[4][0]+rootrows[5][0]);q=F(1,1<<L)
    ck(epriv==(2-2*q+q*q)/8+2*L*q*(3-q)/8)
    Bx=rootrows[3][2];Bb=[];CE2=[];newbills=[];nodes=[]
    for s in [0,1]:
        Bb.append(T.row(((3,s),),1)[2])
        for t in [0,1]:
            ce,new,node=T.nonfair_node(((3,s),(1,t)))
            CE2.append(ce);newbills.append(new);nodes.append(node)
    prefix=add(M,Bx,mul(add(*Bb),F(1,2)))
    bill2=add(prefix,mul(add(*CE2),F(1,4)))
    bill3=add(prefix,mul(add(*newbills),F(1,4)))
    spare=sub((17*epriv,17*epriv),bill3)
    ck(spare[0]>F(1,32))
    ck(sub((17*epriv,17*epriv),bill2)[0]>F(1,32))
    # Check an independent analytic uniform bound for the already-paid second bank.
    if L>=16:ck(q*(L+F(3,2))<=F(35,131072))
    positive=[(n['x'],n['b']) for n in nodes if F(n['Delta_prescribed_reset'][0])>0]
    return {'L':L,'old_M_x_b_debits':saved(prefix),'original_I_private':str(epriv),'previous_complete_bill':saved(bill2),'third_complete_bill':saved(bill3),'original_spare':saved(spare),'positive_reset_nodes':positive,'nodes':nodes}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
    start=time.monotonic();domain=[1,2,3] if args.pilot else list(range(1,16))+[16,32,64]
    records=[]
    for L in domain:
        assert time.monotonic()-start<(55 if args.pilot else 180)
        records.append(case(L))
        (R/'out/CHECKPOINT.json').write_text(json.dumps({'cases':records},indent=2)+'\n',encoding='utf-8')
    ans={'cases':records,'assertions':CHECKS,'runtime_seconds':time.monotonic()-start,'method':'direct conditional-KL likelihood intervals, signed compressed exact spectrum'}
    assert ans['runtime_seconds']<(55 if args.pilot else 180)
    name='PILOT.json' if args.pilot else 'CHECK.json'
    (R/'out'/name).write_text(json.dumps(ans,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'file':name,'cases':len(records),'assertions':CHECKS,'seconds':ans['runtime_seconds'],'positive_reset_nodes':[(z['L'],z['positive_reset_nodes']) for z in records]}))
