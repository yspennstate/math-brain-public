from pathlib import Path
from fractions import Fraction as Q
from math import comb, factorial
from functools import lru_cache
from itertools import product
import json, time

ROOT=Path(__file__).resolve().parents[1]
checks=0
def check(condition):
    global checks
    assert condition
    checks+=1

def polynomial(a,b):
    degree=3*a*b
    c=[0]*(degree+1)
    for k in range(3*b+1): c[a*k]+=(1<<(4*a-6*b))*comb(3*b,k)*3**k
    for k0 in range(a+1):
      for k1 in range(a-k0+1):
       for k2 in range(a-k0-k1+1):
        k3=a-k0-k1-k2
        c[b*(k1+2*k2+3*k3)]-=factorial(a)//(factorial(k0)*factorial(k1)*factorial(k2)*factorial(k3))*3**(k1+k2)*9**k3
    def horner_translate(seq):
        d=[0]
        for coefficient in reversed(seq):
            new=[0]*(len(d)+1)
            for i,v in enumerate(d): new[i]+=v; new[i+1]+=v
            new[0]+=coefficient
            d=new
        while len(d)>degree+1 and d[-1]==0:d.pop()
        return d
    cones=[horner_translate(c),horner_translate(c[::-1])]
    return c,cones

def walsh(truth):
    out=list(truth); step=1
    while step<len(out):
        for start in range(0,len(out),2*step):
            for j in range(start,start+step):
                x,y=out[j],out[j+step];out[j]=x+y;out[j+step]=x-y
        step*=2
    return [Q(x,len(out)) for x in out]

def direct_walsh(truth):
    return [Q(sum(v*(-1 if (i&s).bit_count()%2 else 1) for i,v in enumerate(truth)),len(truth)) for s in range(len(truth))]

def spectrum(truth):return [v*v for v in walsh(truth)]
def influence(p):return sum((v*s.bit_count() for s,v in enumerate(p)),Q(0))
def edges(truth):
    n=(len(truth)-1).bit_length()
    return sum((Q(sum(truth[x]!=truth[x^(1<<i)] for x in range(len(truth))),len(truth)) for i in range(n)),Q(0))

@lru_cache(None)
def factors(n):
    d=2; out={}
    while d*d<=n:
        while n%d==0:out[d]=out.get(d,0)+1;n//=d
        d+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def add(a,b,scale=Q(1)):
    out=dict(a)
    for p,c in b.items():
        out[p]=out.get(p,Q(0))+scale*c
        if not out[p]:del out[p]
    return out
def logexpr(q):
    q=Q(q);check(q>0)
    return add({p:Q(c) for p,c in factors(q.numerator).items()},{p:Q(c) for p,c in factors(q.denominator).items()},Q(-1))
def ce(p,q):
    out={}
    for x,y in zip(p,q):
        if x:out=add(out,logexpr(y),-x)
    return out
def entropy(p):return ce(p,p)
def kl(p,q):return add(ce(p,q),entropy(p),Q(-1))

@lru_cache(None)
def ln_bounds(n):
    k=n.bit_length()-1
    q=Q(n,1<<k);z=(q-1)/(q+1)
    def series(z):
        terms=36
        lower=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(terms)),Q(0))
        upper=lower+2*z**(2*terms+1)/(Q(2*terms+1)*(1-z*z))
        return lower,upper
    a,b=series(z);l,u=series(Q(1,3))
    return a+k*l,b+k*u
def nonnegative(expr):
    if not expr:return True
    lower=Q(0)
    for p,c in expr.items():
        a,b=ln_bounds(p);lower+=c*(a if c>0 else b)
    return lower>=0

def defect(r):
    return [(-1)**sum(((x>>(3*j))&7)==0 for j in range(r)) for x in range(1<<(3*r))]
def target_components(n,kind):
    if kind=='marginal': return [(Q(1),[Q(1,4)]*n)]
    if kind=='fair':return [(Q(1),[Q(1,2)]*n)]
    return [(Q(1,2),[Q(0)]*n),(Q(1,2),[Q(1,2)]*n)]
def component_law(params):
    return [prodq(params[i] if x>>i&1 else 1-params[i] for i in range(len(params))) for x in range(1<<len(params))]
def prodq(values):
    out=Q(1)
    for x in values:out*=x
    return out
def target(n,kind):
    components=target_components(n,kind)
    laws=[component_law(params) for _,params in components]
    q=[sum(w*law[x] for (w,_),law in zip(components,laws)) for x in range(1<<n)]
    check(sum(q)==1)
    return components,laws,q

def information(p,components,laws,q):
    joint=[[p[x]*w*law[x]/q[x] for x in range(len(p))] for (w,_),law in zip(components,laws)]
    v=[sum(row) for row in joint]
    info={};condtc={};remaining={}
    n=(len(p)-1).bit_length()
    for j,row in enumerate(joint):
        if not v[j]:continue
        posterior=[z/v[j] for z in row]
        info=add(info,kl(posterior,p),v[j])
        marginals=[[sum(posterior[x] for x in range(len(p)) if (x>>i&1)==bit) for bit in (0,1)] for i in range(n)]
        tc={}
        for m in marginals:tc=add(tc,entropy(m))
        tc=add(tc,entropy(posterior),Q(-1));condtc=add(condtc,tc,v[j])
        for i,m in enumerate(marginals):remaining=add(remaining,kl(m,[1-components[j][1][i],components[j][1][i]]),v[j])
    residual=add(add(condtc,kl(v,[w for w,_ in components])),remaining)
    check(residual==kl(p,q))
    return info,joint

def main():
    start=time.perf_counter()
    c,cones=polynomial(7,4)
    for row in cones:
        check(len(row)==85)
        for value in row:check(value>=0)
        check(row[0]==row[1]==0)
    # Independent exact negative endpoint value, not a failed positivity heuristic.
    a,b=10,11
    endpoint=(8*a**9+(a**3+b**3)**3)**5-4*(3*a**5+b**5)**9
    check(endpoint>0)
    # The prior degree-six identity is independently expanded on integer pairs.
    for x,y in product(range(5),repeat=2):
        check(4*(3*x*x+y*y)**3-(8*x**3+(x+y)**3)**2==3*(x-y)**2*(3*x*x+y*y)**2)
    receipts=[]
    mask=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1]
    gate=[1-a*a for a in mask];aw=walsh(mask);bw=walsh(gate)
    check(sum(v*v for v in bw)==Q(3,8))
    tau={2:Q(2),3:Q(-9,8)}
    for r in (1,2):
        truth=defect(r);p=spectrum(truth);n=3*r
        check(sum(p)==1);check(influence(p)==edges(truth)==Q(3*r,4))
        formula=[prodq(Q(9 if (s>>(3*j))&7==0 else 1,16) for j in range(r)) for s in range(len(p))]
        check(p==formula)
        if r==1:check(walsh(truth)==direct_walsh(truth))
        targets=[]
        for kind in ('marginal','fair','mixture'):
            comp,laws,q=target(n,kind)
            info,joint=information(p,comp,laws,q)
            gap=add(add(kl(p,q),info,Q(3,4)),tau,-Q(r))
            check(nonnegative(gap))
            if kind=='marginal':check(gap=={})
            targets.append((kind,q))
        # Four mask bits low, three tag bits next, core bits last.
        full=[mask[x&15]+gate[x&15]*(-1 if ((x>>4)&7).bit_count()%2 else 1)*truth[x>>7] for x in range(1<<(n+7))]
        check(all(v in (-1,1) for v in full))
        parent=spectrum(full)
        check(influence(parent)==edges(full)==Q(23,8)+Q(9*r,32))
        expected_entropy=add({2:Q(5),3:Q(-9,16)},entropy(p),Q(3,8))
        check(entropy(parent)==expected_entropy)
        controller_marginal=[sum(parent[u::16]) for u in range(16)]
        check(controller_marginal==[aw[u]**2+bw[u]**2 for u in range(16)])
        check(influence(controller_marginal)==Q(7,4))
        conditional=add(entropy(parent),entropy(controller_marginal),Q(-1))
        fixed_conditional=add(add({2:Q(5),3:Q(-9,16)},entropy(controller_marginal),Q(-1)),entropy(p),Q(3,8))
        check(conditional==fixed_conditional)
        for bit in (0,1):
            child=[full[(x&15)|(bit<<4)|((x>>4)<<5)] for x in range(1<<(n+6))]
            pc=spectrum(child);expected=[Q(0)]*len(pc)
            for u in range(16):
                expected[u]+=aw[u]**2
                for s,z in enumerate(p):expected[u|(3<<4)|(s<<6)]+=bw[u]**2*z
            check(pc==expected)
            for kind,q in targets:
                qc=[Q(0)]*len(pc)
                for u in range(16):
                    qc[u]+=aw[u]**2
                    for s,z in enumerate(q):qc[u|(3<<4)|(s<<6)]+=bw[u]**2*z
                check(sum(qc)==1)
                debit=add(ce(pc,qc),entropy(parent),Q(-1))
                check(debit=={p:c*Q(3,8) for p,c in kl(p,q).items()})
        receipts.append({'r':r,'core_points':len(truth),'parent_points':len(full),'complete_children':2,'targets_per_child':3})
    result={'status':'PASS','exact_assertions':checks,'seconds':time.perf_counter()-start,
            'independent_coefficients':[str(z) for z in c],
            'cone_coefficients':[[str(z) for z in row] for row in cones],
            'endpoint_positive_integer':str(endpoint),'boolean_fixtures':receipts,
            'arithmetic':'integer/Fraction/prime-log vectors;36-term outward rational atanh bounds'}
    (ROOT/'out/independent.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('independent_coefficients','cone_coefficients')}))

if __name__=='__main__':main()
