from fractions import Fraction
from itertools import product, combinations
from math import log2


def maj3(a,b,c): return 1 if a+b+c >= 1 else -1


def recmaj(bits,d):
    if d==0: return bits[0]
    m=3**(d-1)
    return maj3(recmaj(bits[:m],d-1),recmaj(bits[m:2*m],d-1),recmaj(bits[2*m:],d-1))


def truth(n, fn):
    xs=list(product((-1,1), repeat=n))
    return xs,{x:fn(x) for x in xs}


def infs(xs,v):
    n=len(xs[0]); out=[]
    for i in range(n):
        c=0
        for x in xs:
            y=list(x); y[i]*=-1; y=tuple(y)
            c += v[x]!=v[y]
        out.append(Fraction(c,len(xs)))
    return out


def walsh_entropy(xs,v):
    n=len(xs[0]); N=len(xs)
    arr=[]
    for mask in range(1<<n):
        x=tuple(1 if (mask>>i)&1 else -1 for i in range(n))
        arr.append(v[x])
    h=1
    while h<len(arr):
        for i in range(0,len(arr),2*h):
            for j in range(i,i+h):
                a,b=arr[j],arr[j+h]
                arr[j],arr[j+h]=a+b,a-b
        h*=2
    H=0.0
    mass=0.0
    for z in arr:
        p=(z/N)**2
        mass += p
        if p: H -= p*log2(p)
    assert abs(mass-1)<1e-12
    return H


def derivative_support(xs,v,i):
    E=set()
    for x in xs:
        y=list(x); y[i]*=-1; y=tuple(y)
        if v[x]!=v[y]: E.add(x)
    return E


def event_inf(xs,E):
    n=len(xs[0]); out=[]
    for i in range(n):
        c=0
        for x in xs:
            y=list(x); y[i]*=-1; y=tuple(y)
            c += ((x in E)!=(y in E))
        out.append(Fraction(c,len(xs)))
    return out


def min_subcube_errors(xs,E,pivot=0):
    n=len(xs[0]); N=len(xs); mins={}
    controls=[k for k in range(n) if k!=pivot]
    for r in range(1,len(controls)+1):
        best=Fraction(2,1)
        for C in combinations(controls,r):
            for s in product((-1,1),repeat=r):
                d=dict(zip(C,s))
                q={x for x in xs if all(x[i]==a for i,a in d.items())}
                e=Fraction(len(E.symmetric_difference(q)),N)
                if e<best: best=e
        mins[r]=best
    return mins


# 1. Exact recursive-majority formulas and analytic terminal bound.
formula_cases=0
for d in range(1,41):
    j=Fraction(1,2**d)
    J=Fraction(3,2)**d
    H=4*(J-1)
    depth_ratio=2*(J-1)
    Delta=depth_ratio-Fraction(d,2)
    assert Delta>0
    for r in range(1,2*d+4):
        q=Fraction(1,2**r)
        if r!=d:
            assert abs(j-q)>q/Fraction(16*r,1)
    e_lb=2*j*(1-Fraction(1,2**((d+1)//2)))
    assert e_lb > j/Fraction(16*d,1)
    root_ratio=Fraction(4,1)*(1-Fraction(2,3)**d)
    restricted_ratio=Fraction(4,1)-2*Fraction(2,3)**(d-1)
    assert restricted_ratio-root_ratio == Fraction(2,3)**d
    formula_cases += 1

# 2. Direct truth-table checks for M_1,M_2, including ALL sensitivity-domain coordinate subcubes.
brute_rows=0
subcube_cases=0
for d in (1,2):
    n=3**d
    xs,v=truth(n,lambda x,d=d:recmaj(x,d))
    a=infs(xs,v)
    assert all(z==Fraction(1,2**d) for z in a)
    J=sum(a,Fraction())
    assert J==Fraction(3,2)**d
    H=walsh_entropy(xs,v)
    H_formula=float(4*(J-1))
    assert abs(H-H_formula)<1e-11
    E=derivative_support(xs,v,0)
    assert Fraction(len(E),len(xs))==Fraction(1,2**d)
    eI=event_inf(xs,E)
    di=sum(eI,Fraction())/4
    assert di/a[0] == 2*(Fraction(3,2)**d-1)
    mins=min_subcube_errors(xs,E,0)
    for r,best in mins.items():
        q=Fraction(1,2**r)
        assert best > q/Fraction(16*r,1)
        subcube_cases += 1
    brute_rows += 1

# 3. Direct balanced-g composition check for all balanced Boolean g on m<=2.
composition_cases=0
for m in (1,2):
    base_x=list(product((-1,1),repeat=m))
    N=len(base_x)
    for neg_idx in combinations(range(N),N//2):
        neg=set(neg_idx)
        gv={x:(-1 if i in neg else 1) for i,x in enumerate(base_x)}
        I=sum(infs(base_x,gv),Fraction())
        if I==0: continue
        Hg=walsh_entropy(base_x,gv)
        def g(block): return gv[tuple(block)]
        nF=3*m
        xsF,vF=truth(nF,lambda x: maj3(g(x[:m]),g(x[m:2*m]),g(x[2*m:])))
        def and2(a,b): return 1 if (a==1 and b==1) else -1
        xsR,vR=truth(2*m,lambda x: and2(g(x[:m]),g(x[m:])))
        IF=sum(infs(xsF,vF),Fraction()); IR=sum(infs(xsR,vR),Fraction())
        assert max(infs(xsF,vF))<=Fraction(1,2)
        assert max(infs(xsR,vR))<=Fraction(1,2)
        assert IF == Fraction(3,2)*I
        assert IR == I
        HF=walsh_entropy(xsF,vF); HR=walsh_entropy(xsR,vR)
        assert abs(HF-(2+1.5*Hg))<1e-10
        assert abs(HR-(2+Hg))<1e-10
        assert abs((HR/float(IR)-HF/float(IF)) - 2/(3*float(I)))<1e-10
        psi=lambda x: x*x + Fraction(1,7)*x
        ag=infs(base_x,gv)
        A=sum((psi(z/2) for z in ag), Fraction())
        PF=HF-3*float(A); PR=HR-2*float(A)
        assert abs((PR/float(IR)-PF/float(IF))-2/(3*float(I)))<1e-10
        composition_cases += 1

print("PASS recursive_majority_formula_cases", formula_cases)
print("PASS direct_recursive_majority_rows", brute_rows)
print("PASS exhaustive_subcube_distance_cases", subcube_cases)
print("PASS balanced_composition_cases", composition_cases)
print("M2 minimum subcube errors checked through all 3^8-1 nontrivial sensitivity-domain coordinate subcubes grouped by codimension")
print("Key exact formulas:")
for d in (1,2,3,4,8,16):
    J=Fraction(3,2)**d
    Delta=2*(J-1)-Fraction(d,2)
    root=4*(1-Fraction(2,3)**d)
    gap=Fraction(2,3)**d
    print("d=%d J=%s Delta=%s H/J=%.12f descent_gap=%.12f" %
          (d, str(J), str(Delta), float(root), float(gap)))
