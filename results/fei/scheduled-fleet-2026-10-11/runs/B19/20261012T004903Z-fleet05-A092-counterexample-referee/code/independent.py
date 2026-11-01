"""Independent A092 audit v1: recursive transform and -ln(1-t) bounds."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json, time

ROOT=Path(__file__).resolve().parents[1]
N=80

@lru_cache(None)
def minus_ln(x):
    assert F(1,2)<=x<=1
    t=1-x
    power=t
    total=F(0)
    for j in range(1,N+1):
        total+=power/j
        power*=t
    return total,total+power/((N+1)*(1-t))

@lru_cache(None)
def log2(x):
    assert x>0
    k=0
    while x>1:
        x/=2
        k+=1
    while x<F(1,2):
        x*=2
        k-=1
    a,b=minus_ln(x)
    c,d=minus_ln(F(1,2))
    return F(k)-b/c,F(k)-a/d

def plus(a,b): return a[0]+b[0],a[1]+b[1]
def times(c,a): return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def minus(a,b): return plus(a,times(-1,b))
def entropy(law):
    assert sum(law)==1
    result=(F(0),F(0))
    for p in law:
        assert p>=0
        if p: result=plus(result,times(-p,log2(p)))
    return result
def binary(p): return entropy([p,1-p])

def spectrum(table,biases):
    """Expand values in the unnormalized basis product (x_i-p_i)."""
    v=list(map(F,table))
    for i,p in enumerate(biases):
        for mask in range(len(v)):
            if mask&(1<<i): continue
            u,w=v[mask],v[mask|(1<<i)]
            v[mask]=(1-p)*u+p*w
            v[mask|(1<<i)]=w-u
    law=[]
    for mask,c in enumerate(v):
        mass=c*c
        for i,p in enumerate(biases):
            if mask&(1<<i): mass*=p*(1-p)
        law.append(mass)
    assert sum(law)==1
    return law

def audit(table,biases,reveal):
    n=len(biases)
    B=[i for i in range(n) if i not in reveal]
    parent=spectrum(table,biases)
    marginal=[F(0)]*(1<<len(B))
    spectral_joint={}
    for mask,mass in enumerate(parent):
        b=sum(((mask>>i)&1)<<j for j,i in enumerate(B))
        a=sum(((mask>>i)&1)<<j for j,i in enumerate(reveal))
        marginal[b]+=mass
        spectral_joint[a,b]=mass
    physical_joint={}
    child_average=(F(0),F(0))
    for z in range(1<<len(reveal)):
        weight=F(1)
        for j,i in enumerate(reveal): weight*=biases[i] if (z>>j)&1 else 1-biases[i]
        child=[]
        for y in range(1<<len(B)):
            x=sum(((z>>j)&1)<<i for j,i in enumerate(reveal))
            x+=sum(((y>>j)&1)<<i for j,i in enumerate(B))
            child.append(table[x])
        law=spectrum(child,[biases[i] for i in B])
        child_average=plus(child_average,times(weight,entropy(law)))
        for b,mass in enumerate(law): physical_joint[z,b]=weight*mass
    M=(F(0),F(0)); conditional_physical=(F(0),F(0))
    for b,q in enumerate(marginal):
        assert sum(physical_joint[z,b] for z in range(1<<len(reveal)))==q
        if q:
            M=plus(M,times(q,entropy([spectral_joint[a,b]/q for a in range(1<<len(reveal))])))
            conditional_physical=plus(conditional_physical,times(q,entropy([physical_joint[z,b]/q for z in range(1<<len(reveal))])))
    physical_entropy=(F(0),F(0))
    for i in reveal: physical_entropy=plus(physical_entropy,binary(biases[i]))
    J=minus(physical_entropy,conditional_physical)
    # Reconstruct both identities from separate conditional and marginal calculations.
    M_alt=minus(entropy(parent),entropy(marginal))
    J_alt=minus(entropy(marginal),child_average)
    assert max(M[0],M_alt[0])<=min(M[1],M_alt[1])
    assert max(J[0],J_alt[0])<=min(J[1],J_alt[1])
    tax=(F(0),F(0))
    for i in reveal: tax=plus(tax,plus(binary(biases[i]),log2(max(biases[i],1-biases[i]))))
    return parent,M,J,minus(J,M),minus(plus(M,tax),J)

def outward(a):
    scale=10**18
    return [str(F(a[0].numerator*scale//a[0].denominator,scale)),str(F(-((-a[1].numerator*scale)//a[1].denominator),scale))]

def main():
    start=time.perf_counter(); rows=[]
    for k in range(-16,17):
        lo,hi=log2(F(2)**k)
        assert lo<=k<=hi
    for p in [F(1,8),F(1,16),F(1,32),F(1,64)]:
        law,M,J,E,D=audit([1,1,1,-1],[p,F(1,4)],[0])
        assert E[0]>0 and D[0]>0
        assert law==[(1-p/2)**2,p*(1-p)/4,3*p*p/4,3*p*(1-p)/4]
        if p==F(1,8): assert E[0]>F(1195,10000)
        bound=minus(E,times(p,minus(times(F(1,2),log2(1/p)),(F(7),F(7)))))
        assert bound[0]>0
        rows.append({'p':str(p),'spectrum':list(map(str,law)),'M_bits':outward(M),'J_bits':outward(J),'excess_bits':outward(E),'excess_rational':list(map(str,E))})
    # A071's stated minimum-positive case; no acceptance of its full grid.
    table=[1]*8; table[3]=-1
    law,M,J,E,D=audit(table,[F(1,8),F(1,8),F(1,2)],[2])
    saved=F(12119843879252555703,4096*2**60)
    assert D[0]>F(2566,1000000)
    assert saved<D[0] and saved>F(2566,1000000)
    calibration={'truth_table':table,'biases':['1/8','1/8','1/2'],'reveal':[2],'defect_bits':outward(D),'defect_rational':list(map(str,D)),'source_lower_bound':str(saved)}
    # Uniform AND is a scope guard, not an unbounded-ratio family.
    uniform=spectrum([1,1,1,-1],[F(1,2),F(1,2)])
    assert uniform==[F(1,4)]*4
    influence=sum(mask.bit_count()*m for mask,m in enumerate(uniform))
    assert influence==1 and entropy(uniform)[0]<=2<=entropy(uniform)[1]
    result={'status':'PASS','helper_version':'A092-independent-v1','AND_cases':rows,'A071_minimum_case':calibration,'uniform_AND':{'H':2,'I':1,'tensor_ratio':2},'terms':N,'certificate_arithmetic':'Fraction only; positive -ln(1-t) series and tail','runtime_seconds':time.perf_counter()-start}
    (ROOT/'out'/'REPRODUCTION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','AND_cases':4,'A071_cases':1,'runtime_seconds':result['runtime_seconds']}))

if __name__=='__main__': main()
