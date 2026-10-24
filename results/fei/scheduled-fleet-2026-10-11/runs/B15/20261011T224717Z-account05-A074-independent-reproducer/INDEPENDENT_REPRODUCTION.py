from fractions import Fraction as F
from pathlib import Path
import json,time,hashlib
ROOT=Path(__file__).resolve().parent
SOURCE=Path('~/brain_workers/FEI100_20261011/agents/A073/runs/20261011T222436Z-account05-A073-certified-logarithms')
CASES=[('minimum_positive',[1,1,1,-1,1,1,1,1],[F(1,8),F(1,8),F(1,2)],4,1),('exact_zero',[1,-1,-1,-1,-1,1,1,1],[F(1,8),F(1,8),F(1,2)],4,1),('taxfree_AND',[1,1,1,-1],[F(1,8),F(1,4)],1,-1)]
checks=0
def check(v):
    global checks
    checks+=1
    assert v
def prod(xs):
    r=F(1)
    for x in xs:r*=x
    return r
def spectrum(table,p):
    n=len(p);N=1<<n
    # The unique multilinear polynomial interpolating the binary table.
    c=[F(x) for x in table]
    for i in range(n):
        for s in range(N):
            if s>>i&1:c[s]-=c[s^(1<<i)]
    for x in range(N):check(sum(c[s] for s in range(N) if s&x==s)==table[x])
    # Replace each binary variable x_i by p_i + u_i.
    b=[sum(c[t]*prod(p[i] for i in range(n) if (t^s)>>i&1) for t in range(N) if t&s==s) for s in range(N)]
    mu=[b[s]**2*prod(p[i]*(1-p[i]) for i in range(n) if s>>i&1) for s in range(N)]
    check(sum(mu)==1)
    for x in range(N):check(sum(b[s]*prod(F((x>>i)&1)-p[i] for i in range(n) if s>>i&1) for s in range(N))==table[x])
    piv=[sum(prod(p[j] if x>>j&1 else 1-p[j] for j in range(n) if j!=i) for x in range(N) if not(x>>i&1) and table[x]!=table[x^(1<<i)]) for i in range(n)]
    inf=[sum(mu[s] for s in range(N) if s>>i&1) for i in range(n)]
    for i in range(n):check(inf[i]==4*p[i]*(1-p[i])*piv[i])
    return c,b,mu,piv,inf
def ln_small(x):
    # x in [1,2]; ln x = sum_{k>=1}(1-1/x)^k/k.
    check(1<=x<=2)
    t=1-1/x;N=40
    a=sum((t**k/F(k) for k in range(1,N+1)),F(0))
    return a,a+t**(N+1)/(F(N+1)*(1-t))
L2=ln_small(F(2))
def log2(x):
    check(x>0)
    k=0
    while x<1:x*=2;k-=1
    while x>=2:x/=2;k+=1
    lo,hi=ln_small(x)
    return F(k)+lo/L2[1],F(k)+hi/L2[0]
def add_scaled(acc,w,interval):
    a,b=interval
    if w<0:a,b=b,a
    return acc[0]+w*a,acc[1]+w*b
def stringify(v):
    if isinstance(v,F):return str(v)
    if isinstance(v,dict):return {k:stringify(x) for k,x in v.items()}
    if isinstance(v,(tuple,list)):return [stringify(x) for x in v]
    return v
def rounded(interval,scale=10**8):
    a,b=interval
    return F((a*scale).__floor__(),scale),F((b*scale).__ceil__(),scale)
def main():
    (ROOT/'out').mkdir(exist_ok=True)
    start=time.perf_counter();records=[];receipts=[]
    for name,table,p,A,orient in CASES:
        c,b,mu,piv,inf=spectrum(table,p)
        n=len(p);a=[i for i in range(n) if A>>i&1];bb=[i for i in range(n) if not(A>>i&1)]
        def lift(x,inds):return sum(((x>>j)&1)<<i for j,i in enumerate(inds))
        marginal=[sum(mu[s] for s in range(1<<n) if s&~A==lift(t,bb)) for t in range(1<<len(bb))]
        children=[];joint=[]
        for z in range(1<<len(a)):
            tab=[table[lift(z,a)|lift(x,bb)] for x in range(1<<len(bb))]
            weight=prod(p[i] if z>>j&1 else 1-p[i] for j,i in enumerate(a))
            _,bc,mc,pc,ic=spectrum(tab,[p[i] for i in bb])
            children.append({'table':tab,'weight':weight,'spectrum':mc})
            joint.append([weight*x for x in mc])
        for t,q in enumerate(marginal):check(sum(row[t] for row in joint)==q)
        for j,i in enumerate(bb):check(sum(child['weight']*sum(child['spectrum'][s] for s in range(1<<len(bb)) if s>>j&1) for child in children)==inf[i])
        M=(F(0),F(0));J=(F(0),F(0));terms=[]
        for s,m in enumerate(mu):
            if m:
                q=marginal[sum(((s>>i)&1)<<j for j,i in enumerate(bb))]
                M=add_scaled(M,-m,log2(m/q));terms.append((-m,m/q))
        for child in children:
            for t,m in enumerate(child['spectrum']):
                if m:
                    w=child['weight']*m
                    J=add_scaled(J,w,log2(m/marginal[t]));terms.append((-w,m/marginal[t]))
        D=(M[0]-J[1],M[1]-J[0]) if orient==1 else (J[0]-M[1],J[1]-M[0])
        if name=='exact_zero':
            # M=0 since selector spectral coordinate is deterministic; J=0 since all child laws equal q.
            check(all(mu[s]==0 for s in range(1<<n) if not(s&A)))
            check(all(child['spectrum']==marginal for child in children))
            M=J=D=(F(0),F(0))
        if name=='minimum_positive':check(D[0]>F(5,2048) and D[1]<F(3,1024))
        if name=='taxfree_AND':check(D[0]>F(1195,10000))
        # Load source only after the independent mathematical calculation.
        sourcepath=SOURCE/'out'/f'{name}.json';data=sourcepath.read_bytes();src=json.loads(data)
        receipts.append({'path':str(sourcepath),'sha256':hashlib.sha256(data).hexdigest()})
        check(table==src['table'] and p==list(map(F,src['biases'])) and A==src['physical_block_mask'])
        for key,ours in [('centered_coefficients',b),('spectrum',mu),('pivotal_probabilities',piv),('spectral_influences',inf)]:check(ours==list(map(F,src['parent'][key])))
        check(marginal==list(map(F,src['marginal'])))
        for ours,theirs in zip(children,src['children']):
            check(ours['table']==theirs['table']);check(ours['weight']==F(theirs['weight']));check(ours['spectrum']==list(map(F,theirs['spectrum'])))
        if name!='exact_zero':
            slo,shi=map(F,src['outward_decimal_interval_bits'])
            check(slo<D[0] and D[1]<shi)
        record={'name':name,'table':table,'biases':p,'block':A,'orientation':orient,'binary_polynomial':c,'centered_coefficients':b,'spectrum':mu,'pivotal':piv,'influences':inf,'marginal':marginal,'children':children,'physical_spectral_joint':joint,'M_interval':M,'J_interval':J,'oriented_residual_interval':D,'outward_residual_interval':rounded(D),'source_agreement':True}
        (ROOT/'out'/f'{name}.json').write_text(json.dumps(stringify(record),indent=2),encoding='utf-8')
        records.append({'name':name,'interval':stringify(rounded(D))})
        check(time.perf_counter()-start<55)
    summary={'cases':3,'exact_checks':checks,'failures':0,'runtime_seconds':time.perf_counter()-start,'records':records,'source_receipts':receipts,'no_original_code_imported':True}
    (ROOT/'out/validation.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
