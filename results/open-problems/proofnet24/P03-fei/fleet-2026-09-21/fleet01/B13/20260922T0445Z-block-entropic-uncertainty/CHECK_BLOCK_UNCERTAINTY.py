from __future__ import annotations
import math, random

def h2(x: float) -> float:
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x)-(1.0-x)*math.log2(1.0-x)

def entropy(ps):
    return sum(-p*math.log2(p) for p in ps if p > 1e-18)

def fwht(a):
    a=[float(x) for x in a]
    h=1
    n=len(a)
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def uniform_spectrum(vals):
    N=len(vals)
    w=fwht(vals)
    return [(x/N)**2 for x in w]

def restrict_vals(vals,n,A,z):
    A=tuple(sorted(A)); Aset=set(A)
    comp=[i for i in range(n) if i not in Aset]
    out=[]
    for y in range(1<<len(comp)):
        x=0
        for k,i in enumerate(comp):
            if (y>>k)&1: x |= 1<<i
        for k,i in enumerate(A):
            if (z>>k)&1: x |= 1<<i
        out.append(vals[x])
    return out,comp

def singleton_uniform(vals,n,i):
    w=uniform_spectrum(vals)
    base=[m for m in range(1<<n) if ((m>>i)&1)==0]
    B=0.0
    for m in base:
        a,b=w[m],w[m|(1<<i)]
        t=a+b
        if t>1e-18:
            B += t*h2(b/t)
    child=[]
    for bit in (0,1):
        rv,_=restrict_vals(vals,n,[i],bit)
        child.append(uniform_spectrum(rv))
    mix=[0.5*(a+b) for a,b in zip(child[0],child[1])]
    JS=entropy(mix)-0.5*entropy(child[0])-0.5*entropy(child[1])
    return B,JS

def biased_coeffs(vals, ps):
    n=len(ps); N=1<<n
    out=[0.0]*N
    for x in range(N):
        pr=1.0
        phi=[1.0]*n
        for i,p in enumerate(ps):
            bit=(x>>i)&1
            pr*=p if bit else 1.0-p
            phi[i]=(bit-p)/math.sqrt(p*(1.0-p))
        prods=[1.0]*N
        for s in range(1,N):
            b=s & -s
            i=b.bit_length()-1
            prods[s]=prods[s^b]*phi[i]
        fx=vals[x]
        for s in range(N):
            out[s]+=pr*fx*prods[s]
    return out

def biased_block(vals,ps,A):
    n=len(ps); A=tuple(sorted(A)); Aset=set(A)
    comp=[i for i in range(n) if i not in Aset]
    c=biased_coeffs(vals,ps)
    w=[x*x for x in c]
    groups={}
    for s,mass in enumerate(w):
        T=tuple((s>>i)&1 for i in comp)
        groups.setdefault(T,[]).append(mass)
    HU=0.0
    for arr in groups.values():
        t=sum(arr)
        if t>1e-16:
            HU+=t*entropy([x/t for x in arr])
    zprobs=[]; laws=[]
    for z in range(1<<len(A)):
        pz=1.0
        for k,i in enumerate(A):
            p=ps[i]
            pz*=p if ((z>>k)&1) else 1.0-p
        rv,_=restrict_vals(vals,n,A,z)
        cc=biased_coeffs(rv,[ps[i] for i in comp])
        laws.append([x*x for x in cc]); zprobs.append(pz)
    mix=[0.0]*(1<<len(comp))
    avgH=0.0
    for pz,law in zip(zprobs,laws):
        avgH += pz*entropy(law)
        for j,x in enumerate(law): mix[j]+=pz*x
    MI=entropy(mix)-avgH
    eta=sum(h2(ps[i])+math.log2(max(ps[i],1.0-ps[i])) for i in A)
    return HU,MI,eta

def main():
    count=0; max_violation=-1e9; max_ratio=0.0
    for n in range(1,5):
        N=1<<n
        # Global output negation duplicates spectra/restrictions, so fix f(0)=+1.
        for tail in range(1<<(N-1)):
            vals=[1]+[1 if ((tail>>(x-1))&1)==0 else -1 for x in range(1,N)]
            for i in range(n):
                B,JS=singleton_uniform(vals,n,i)
                v=JS-B
                max_violation=max(max_violation,v)
                if B>1e-14: max_ratio=max(max_ratio,JS/B)
                count+=1
    rng=random.Random(20260922)
    biased_count=0; biased_max=-1e9
    for n in range(2,5):
        for _ in range(250):
            vals=[1 if rng.randrange(2)==0 else -1 for _ in range(1<<n)]
            ps=[0.03+0.94*rng.random() for _ in range(n)]
            r=1+rng.randrange(n)
            A=sorted(rng.sample(range(n),r))
            HU,MI,eta=biased_block(vals,ps,A)
            biased_max=max(biased_max,MI-HU-eta)
            biased_count+=1
    print("PASS" if max_violation < 2e-11 and biased_max < 2e-10 else "FAIL")
    print(f"uniform_singleton_cases={count}")
    print(f"uniform_max_JS_minus_B={max_violation:.3e}")
    print(f"uniform_max_JS_over_B={max_ratio:.12f}")
    print(f"biased_random_block_cases={biased_count}")
    print(f"biased_max_MI_minus_HU_minus_eta={biased_max:.3e}")
    vals=[1,-1,1,1]  # only (x0,x1)=(1,0) is -1
    HU,MI,eta=biased_block(vals,[0.2,0.9],[1])
    assert MI > HU and MI <= HU+eta+1e-12
    print(f"biased_penalty_example_HU={HU:.15f}")
    print(f"biased_penalty_example_MI={MI:.15f}")
    print(f"biased_penalty_example_eta={eta:.15f}")
    print(f"biased_unpenalized_gap={MI-HU:.15f}")

if __name__=="__main__":
    main()
