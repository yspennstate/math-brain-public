import math, json
from fractions import Fraction
from itertools import product

def walsh(v):
    a=list(v); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for i in range(j,j+h):a[i],a[i+h]=a[i]+a[i+h],a[i]-a[i+h]
        h*=2
    return a

def packet(a,b):
    u=(a+b)**2/4; v=(a-b)**2/4
    if not u or not v:return 0.
    # Homogeneous entropy, stable for very small mass ratios.
    return (u*math.log1p(v/u)+v*math.log1p(u/v))/math.log(2)

C=2+1.5/math.log(2); checked=0; max_violation=0.
for n in range(1,5):
    N=1<<n
    for code in range(1<<N):
        f=[1-2*((code>>j)&1) for j in range(N)]
        for bit in range(n):
            g=[f[j] for j in range(N) if not ((j>>bit)&1)]
            h=[f[j] for j in range(N) if ((j>>bit)&1)]
            m=len(g); a=[x/m for x in walsh(g)]; b=[x/m for x in walsh(h)]
            eps=sum(x!=y for x,y in zip(g,h))/m; eps=min(eps,1-eps)
            B=sum(packet(x,y) for x,y in zip(a,b))
            kap=min(1-max(x*x for x in a),1-max(x*x for x in b))
            bound=eps*(C+math.log2(1+kap/(2*eps))) if eps else 0.
            assert B<=bound+1e-12,(n,code,bit,B,bound)
            max_violation=max(max_violation,B-bound);checked+=1

rows=[]
for k in range(4,42,2):
    r=2*k; d=Fraction(1,1<<k); p=Fraction(1,1<<r); s=Fraction(1,1<<(k//2))
    # bent Walsh signs have sum 2^(k/2), and the empty coefficient is +s.
    count_plus=((1<<k)+(1<<(k//2)))//2
    count_minus=(1<<k)-count_plus
    B_non=float(p)*((count_plus-1)*packet(float(s),float(s-2*d))+count_minus*packet(float(-s),float(-s-2*d)))
    B_other=((1<<r)-1)*packet(float(p*(s-1)),float(p*(s-2*d-1)))
    B_empty=packet(float(1+p*(s-1)),float(1+p*(s-2*d-1)))
    # For k>=18 rounding may erase empty-packet mismatch; these terms are nonnegative,
    # so B_non alone remains a valid numerical lower bound. Algebraic proof is exact.
    j=p*d; Ig=p*(Fraction(k,2)+r*(1-s)); Ih=p*(Fraction(k,2)+2*k*d+r*(1-s+2*d))
    lower=(1-d)*(k-2)
    kap=1-(1-p*(1-s))**2
    upper=float(j)*(C+math.log2(1+float(kap/(2*j))))
    assert B_non/float(j)+1e-11>=float(lower)
    assert B_non<=upper+1e-30
    rows.append(dict(k=k,r=r,j=str(j),max_child_influence=str(max(Ig,Ih)),nonempty_allocation_over_j=B_non/float(j),proved_lower_ratio=str(lower),log_upper_ratio=upper/float(j)))
print(json.dumps({'constant':C,'exhaustive_coordinate_checks':checked,'max_floating_violation':max_violation,'sparse_activation':rows,'scope':'Finite self-checks only; universal inequalities require analytic proof.'},indent=2))
