from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json, math, time, sys
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'
pilot='--pilot' in sys.argv
spec={'helper':'A100-stage3-independent-prime-log-v1','family':'all Boolean heat roots n=1..3; all Boolean seeds n=1..2 under disjoint tensor/parity/point activation',
      'domain':{'heat_n':[1] if pilot else [1,2,3],'seed_n':[1] if pilot else [1,2],
                'm':[1] if pilot else [1,2],'ell':[2] if pilot else [2,3],'k':[1] if pilot else [1,2,3]},
      'case_count':{'heat_roots':4 if pilot else 276,'activated_roots':4 if pilot else 240},
      'symmetry':'none; labeled signs and coordinates kept','arithmetic':'integer FWHT, Fraction physical edges and formal prime-log identities; 24-term exact atanh ln intervals and 18-term e-series enclosure',
      'memory_estimate_MB':40,'max_runtime_seconds':60,'max_truth_table_dimension':4 if pilot else 10,'automatic_dimension_escalation':False}
(RUN/('PILOT_SPEC.json' if pilot else 'CHECK_SPEC.json')).write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
t0=time.perf_counter(); assertions=0
def check(ok,label):
    global assertions
    assert ok,label
    assertions+=1
class L:
    def __init__(self,d=None): self.d={p:F(v) for p,v in (d or {}).items() if v}
    def __add__(self,b):
        d=self.d.copy()
        for p,v in b.d.items(): d[p]=d.get(p,F(0))+v
        return L(d)
    def __sub__(self,b): return self+b*(-1)
    def __mul__(self,b): return L({p:v*b for p,v in self.d.items()})
    __rmul__=__mul__
    def __eq__(self,b): return self.d==b.d
    def pack(self): return {str(p):str(v) for p,v in sorted(self.d.items())}
def factor(n):
    out={}; p=2
    while p*p<=n:
        while n%p==0: out[p]=out.get(p,0)+1; n//=p
        p=3 if p==2 else p+2
    if n>1: out[n]=out.get(n,0)+1
    return out
@lru_cache(None)
def log(q):
    q=F(q); assert q>0
    d=factor(q.numerator)
    for p,v in factor(q.denominator).items(): d[p]=d.get(p,0)-v
    return L(d)
def sumL(xs):
    z=L()
    for x in xs: z=z+x
    return z
@lru_cache(None)
def ln_bounds(p):
    a=F(p); power=0
    while a>=2: a/=2; power+=1
    z=(a-1)/(a+1); steps=24
    lower=2*sum((z**(2*j+1)/F(2*j+1) for j in range(steps)),F(0))
    remainder=2*z**(2*steps+1)/(F(2*steps+1)*(1-z*z))
    z2=F(1,3)
    l2=2*sum((z2**(2*j+1)/F(2*j+1) for j in range(steps)),F(0))
    r2=2*z2**(2*steps+1)/(F(2*steps+1)*(1-z2*z2))
    return lower+power*l2, lower+remainder+power*(l2+r2)
def nat_bounds(x):
    lo=hi=F(0)
    for p,v in x.d.items():
        a,b=ln_bounds(p); lo+=v*(a if v>=0 else b); hi+=v*(b if v>=0 else a)
    return lo,hi
def transform(table):
    w=list(table); step=1
    while step<len(w):
        for j in range(0,len(w),2*step):
            for z in range(step):
                a,b=w[j+z],w[j+z+step]; w[j+z]=a+b;w[j+z+step]=a-b
        step*=2
    return [F(a,len(table)) for a in w]
def cube(table):
    n=(len(table)-1).bit_length(); a=transform(table); p=[v*v for v in a]
    e=[F(sum(table[x]!=table[x^(1<<i)] for x in range(len(table))),len(table)) for i in range(n)]
    check(sum(p)==1,'Parseval')
    for i in range(n): check(e[i]==sum((v for s,v in enumerate(p) if s&(1<<i)),F(0)),'physical derivative versus spectrum')
    return a,p,e
def M_of(p):
    n=(len(p)-1).bit_length(); rows=[]; tail=L(); weighted_D=L(); e=[]
    for i in range(n):
        bit=1<<i; d=sum((p[s] for s in range(len(p)) if s&bit),F(0)); e.append(d)
        cost=L(); wd=L(); total_r=F(0); total_mu=F(0)
        for s in range(len(p)):
            if s&bit: continue
            y=p[s|bit]; r=p[s]+y; total_r+=r
            if y:
                cost=cost+y*log(r/y); wd=wd+y*log(y/(d*r)); total_mu+=y/d
                if s.bit_count()>=2: tail=tail+y*log(r/y)
        check(total_r==1,'complete residual-law normalizer')
        if d:
            check(total_mu==1,'complete derivative-law normalizer')
            check(cost==d*log(1/d)-wd,'oriented refund identity')
        rows.append((cost,wd)); weighted_D=weighted_D+wd
    return sumL(x[0] for x in rows),tail,weighted_D,rows,e
e_lo=sum((F(1,math.factorial(j)) for j in range(19)),F(0))
e_hi=e_lo+F(1,math.factorial(19))/(1-F(1,20))
beta_lo=2+2/(e_hi*e_hi)
heat_cases=0; tree_cases=0
for n in spec['domain']['heat_n']:
    for mask in range(1<<(1<<n)):
        table=[1-2*((mask>>x)&1) for x in range(1<<n)]; a,p,e=cube(table)
        rootK=sumL(-v*log(v) for s,v in enumerate(p) if s and v)*F(1,2)
        costs=[]; erasures=[]; childKs=[]; childIs=[]
        for i in range(n):
            bit=1<<i; C=L(); E=L()
            for s in range(1,len(p)):
                if s&bit: continue
                u,v=p[s],p[s|bit]; q=u+v
                if q:
                    for child in [(a[s]+a[s|bit])**2,(a[s]-a[s|bit])**2]:
                        if child: C=C+F(1,2)*child*log(child/q)
                if u: E=E+u*log(q/u)
                if v: E=E+v*log(q/v)
            level=-p[bit]*log(p[bit]) if p[bit] else L()
            cost=C+level; costs.append(cost); erasures.append(E)
            check(abs(a[bit])<=e[i],'Boolean mean derivative granularity')
            check(nat_bounds(cost)[1]<=beta_lo*e[i],'joint singleton price beta=2+2/e^2')
            ks=[]; infl=[]
            for sign in [0,1]:
                child=[table[x] for x in range(1<<n) if ((x>>i)&1)==sign]
                ca=transform(child); cp=[v*v for v in ca]
                ks.append(sumL(-v*log(v) for s,v in enumerate(cp) if s and v)*F(1,2))
                infl.append(sum((s.bit_count()*v for s,v in enumerate(cp)),F(0)))
            childKs.append(sumL(ks)*F(1,2)); childIs.append(sum(infl,F(0))/2)
            check(2*(rootK-childKs[-1])==E+cost,'heat singleton exact terminal identity')
            check(sum(e,F(0))-childIs[-1]==e[i],'singleton influence telescope')
        # Fixed first query followed by every remaining coordinate: recursive physical tree.
        def tree(tab):
            dim=(len(tab)-1).bit_length()
            if dim==0: return L(),L(),F(0)
            ca=transform(tab); cp=[v*v for v in ca]; localE=L(); localC=L()
            for s in range(2,len(cp),2):
                u,v=cp[s],cp[s|1]; q=u+v
                if u: localE=localE+u*log(q/u)
                if v: localE=localE+v*log(q/v)
                if q:
                    for c in [(ca[s]+ca[s|1])**2,(ca[s]-ca[s|1])**2]:
                        if c: localC=localC+F(1,2)*c*log(c/q)
            if cp[1]: localC=localC-cp[1]*log(cp[1])
            di=sum((cp[s] for s in range(1,len(cp),2)),F(0))
            l=tree(tab[::2]); r=tree(tab[1::2])
            return localE+(l[0]+r[0])*F(1,2),localC+(l[1]+r[1])*F(1,2),di+(l[2]+r[2])/2
        E,P,spent=tree(table)
        check(2*rootK==E+P,'complete singleton-tree heat telescope')
        check(spent==sum(e,F(0)),'tree physical influence nonreuse')
        check(nat_bounds(P)[1]<=beta_lo*spent,'complete tree joint price')
        heat_cases+=1; tree_cases+=1
activation_cases=0; sample=[]
for n in spec['domain']['seed_n']:
    for mask in range(1<<(1<<n)):
        seed=[1-2*((mask>>x)&1) for x in range(1<<n)]; sa,sp,se=cube(seed)
        seedM,seedTail,seedWD,seedRows,_=M_of(sp); seedI=sum(se,F(0))
        for m in spec['domain']['m']:
            for ell in spec['domain']['ell']:
                for k in spec['domain']['k']:
                    coreD=m*n+ell; N=coreD+k; table=[]
                    for x in range(1<<N):
                        h=1-2*(((x>>(m*n))&((1<<ell)-1)).bit_count()%2)
                        for b in range(m): h*=seed[(x>>(b*n))&((1<<n)-1)]
                        table.append(h if (x>>coreD)==0 else 1)
                    a,p,e=cube(table); actualM,actualTail,actualWD,rows,_=M_of(p)
                    q=F(1,2**k); d=(1-q)**2+q*q; J=m*seedI+ell
                    Dc=(1-q)*log(2**(k-1))+q*log(q/d)
                    check(sum(e,F(0))==q*(J+k),'activation full physical budget')
                    check(actualWD==q*(m*seedWD+k*J*log(2)+k*Dc),'full original-seed KL refund retained')
                    check(actualM==q*m*seedM+k*(q*(1-q)*log(2)+q*q*log(d/(q*q))),'complete M identity')
                    check(actualTail==q*m*seedM+k*q*(1-k*q)*log(2),'oriented degree>=2 tail identity')
                    for i in range(m*n):
                        si=i%n
                        if se[si]:
                            check(rows[i][1]==q*seedRows[si][1]+q*se[si]*k*log(2),'individual core likelihood ratio')
                        else: check(e[i]==0,'irrelevant seed coordinate retained as irrelevant')
                    for i in range(m*n,coreD):
                        check(rows[i][1]==q*k*log(2) and rows[i][0]==L(),'parity rarity refund and zero oriented cost')
                    for i in range(coreD,N): check(rows[i][1]==q*Dc,'control likelihood ratio')
                    activation_cases+=1
                    if mask==1 and n==2 and m==1 and ell==2: sample.append({'n':n,'m':m,'ell':ell,'k':k,'I':str(sum(e,F(0))),'M_formal_prime_log':actualM.pack(),'weighted_KL_formal_prime_log':actualWD.pack()})
result={'helper':spec['helper'],'status':'PASS','assertions_passed':assertions,'failures':0,
        'heat_roots':heat_cases,'complete_heat_trees':tree_cases,'activated_roots':activation_cases,
        'runtime_seconds':time.perf_counter()-t0,'arithmetic':spec['arithmetic'],'sample':sample,
        'e_enclosure':{'lower':str(e_lo),'upper':str(e_hi)},'beta_lower':str(beta_lo),
        'scope':'Finite independent certificates support the separate all-dimensional derivations; no FEI upper bound or infinite-family extrapolation.'}
(OUT/('PILOT_CHECK.json' if pilot else 'INDEPENDENT_CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['sample','e_enclosure','beta_lower']},indent=2),flush=True)
