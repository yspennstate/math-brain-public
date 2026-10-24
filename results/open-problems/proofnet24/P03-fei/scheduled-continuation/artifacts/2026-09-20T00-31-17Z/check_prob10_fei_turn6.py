#!/usr/bin/env python3
import functools, itertools, json, math

def walsh_coeffs(vals):
    a=[float(v) for v in vals]
    N=len(a); h=1
    while h<N:
        for i in range(0,N,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return [x/N for x in a]

def probs(vals):
    return [x*x for x in walsh_coeffs(vals)]

def restrict(vals,i,bit):
    n=(len(vals)).bit_length()-1
    out=[]
    for s in range(1<<(n-1)):
        x=0; pos=0
        for j in range(n):
            if j==i:
                if bit: x |= 1<<j
            else:
                if (s>>pos)&1: x |= 1<<j
                pos+=1
        out.append(vals[x])
    return tuple(out)

def B_i(vals,i):
    p=probs(vals); n=(len(vals)).bit_length()-1
    ans=0.0
    for s in range(1<<n):
        if (s>>i)&1: continue
        r=p[s]; q=p[s|(1<<i)]; m=r+q
        if m:
            if r: ans += r*math.log2(m/r)
            if q: ans += q*math.log2(m/q)
    return ans

def K_i(vals,i):
    p=probs(vals); n=(len(vals)).bit_length()-1
    ans=0.0
    for s in range(1<<n):
        if (s>>i)&1: continue
        r=p[s]; q=p[s|(1<<i)]
        if r and q and r!=q:
            ans += min(r,q)*abs(math.log2(r/q))
    return ans

def influence(vals,i):
    N=len(vals)
    return sum(vals[x]!=vals[x^(1<<i)] for x in range(N))/N

def total_influence(vals):
    n=(len(vals)).bit_length()-1
    return sum(influence(vals,i) for i in range(n))

@functools.lru_cache(None)
def Rstar(vals):
    n=(len(vals)).bit_length()-1
    if all(x==vals[0] for x in vals):
        return 0.0
    best=float("inf")
    for i in range(n):
        v0=restrict(vals,i,0); v1=restrict(vals,i,1)
        cost=B_i(vals,i)+0.5*(Rstar(v0)+Rstar(v1))
        best=min(best,cost)
    return best

def product(f,g):
    nf=(len(f)).bit_length()-1
    ng=(len(g)).bit_length()-1
    out=[]
    for y in range(1<<ng):
        for x in range(1<<nf):
            out.append(f[x]*g[y])
    return tuple(out)

def all_funcs(n):
    N=1<<n
    for mask in range(1<<N):
        yield tuple(1 if (mask>>x)&1 else -1 for x in range(N))

def onepoint(n):
    vals=[1]*(1<<n); vals[0]=-1
    return tuple(vals)

def B_one_formula(n):
    N=1<<n
    A=(N-2)**2/(N*N)
    b=4/(N*N)
    m=A+b
    theta=b/m
    h=0.0 if theta in (0,1) else -theta*math.log2(theta)-(1-theta)*math.log2(1-theta)
    return m*h + 4*(N-2)/(N*N)

def K_one_formula(n):
    N=1<<n
    if n<=1: return 0.0
    return 8/(N*N)*math.log2((N-2)/2)

def R_one_formula(n):
    r=0.0
    for m in range(2,n+1):
        r=B_one_formula(m)+0.5*r
    return r

def main():
    out={"status":"PASS"}
    # Bellman/tree optimizer mechanism atlas through n=4
    atlas={}
    for n in range(1,5):
        mx=(-1.0,None)
        count=0
        for f in all_funcs(n):
            I=total_influence(f)
            if I>0:
                ratio=Rstar(f)/I
                if ratio>mx[0]+1e-13:
                    mx=(ratio,f)
            count+=1
        neg=[i for i,v in enumerate(mx[1]) if v<0] if mx[1] else []
        atlas[str(n)]={"functions_checked":count,"max_Rstar_over_I":mx[0],"extremizer_negative_points":neg}
    out["allocation_atlas"]=atlas

    # Exhaustive tensorization checks for 2+2 and 1+3 variables.
    tensor=[]
    for na,nb in [(2,2),(1,3)]:
        fail=[]
        checked=0
        Fs=list(all_funcs(na)); Gs=list(all_funcs(nb))
        for f in Fs:
            for g in Gs:
                checked+=1
                lhs=Rstar(product(f,g))
                rhs=Rstar(f)+Rstar(g)
                if abs(lhs-rhs)>2e-11:
                    fail.append({"lhs":lhs,"rhs":rhs})
                    break
            if fail: break
        tensor.append({"blocks":[na,nb],"pairs_checked":checked,"failures":fail})
    out["tensorization_checks"]=tensor

    # One-point exact formulas vs truth tables, plus asymptotic ratios.
    one=[]
    for n in range(2,13):
        f=onepoint(n)
        bf=B_one_formula(n); kt=K_one_formula(n)
        bcheck=B_i(f,0) if n<=8 else None
        kcheck=K_i(f,0) if n<=8 else None
        one.append({
            "n":n,
            "B_formula":bf,
            "B_direct":bcheck,
            "K_formula":kt,
            "K_direct":kcheck,
            "Rstar_formula":R_one_formula(n),
            "I":2*n/(1<<n),
            "Rstar_over_I":R_one_formula(n)/(2*n/(1<<n))
        })
        if n<=8 and (abs(bf-bcheck)>2e-12 or abs(kt-kcheck)>2e-12):
            out["status"]="FAIL"
    out["one_point_checks"]=one

    # Exact analytical monotonicity obstruction values for K_i:
    # 1/2 K_i(w_{n-1}) > K_i(w_n) for n>=4.
    obs=[]
    for n in range(4,13):
        par=K_one_formula(n); child=0.5*K_one_formula(n-1)
        obs.append({"n":n,"parent_K_i":par,"average_child_K_i":child,"increase":child-par})
        if not child>par:
            out["status"]="FAIL"
    out["K_restriction_monotonicity_obstruction"]=obs

    # Ensure exhaustive tensor checks passed.
    if any(x["failures"] for x in tensor):
        out["status"]="FAIL"
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
