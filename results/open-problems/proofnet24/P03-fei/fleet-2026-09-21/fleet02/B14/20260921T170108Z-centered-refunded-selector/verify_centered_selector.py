#!/usr/bin/env python3
import json, math

def E(a,b):
    if a<=0.0 or b<=0.0: return 0.0
    s=a+b
    return a*math.log2(s/a)+b*math.log2(s/b)

def H(mu):
    return -sum(x*math.log2(x) for x in mu if x>0.0)

def fwht(vals):
    a=list(map(float,vals)); N=len(a); h=1
    while h<N:
        for j in range(0,N,2*h):
            for k in range(j,j+h):
                x=a[k]; y=a[k+h]; a[k]=x+y; a[k+h]=x-y
        h*=2
    return [x/N for x in a]

def Gamma(t): return E((1-t)/t,1-t)
def F(t): return Gamma(t)+2*(1-t)

TOL=5e-10; KAPPA=2/math.log(2)
counts={"nonconstant":0,"centered_character":0,"positive_centered_shell":0,
        "zero_centered_shell_noncharacter":0,"relevant_centered_coordinates":0}
mx={"centered_influence_increase":0.0,"shell_fraction_over_one":0.0,
    "erasure_selector":0.0,"decrement_selector":0.0}

for n in range(1,5):
    N=1<<n
    for mask in range(1<<N):
        vals=[1.0 if (mask>>x)&1 else -1.0 for x in range(N)]
        hats=fwht(vals); mu=[x*x for x in hats]
        p=[sum(mu[s] for s in range(N) if s&(1<<i)) for i in range(n)]
        I=sum(p)
        if I<=TOL: continue
        counts["nonconstant"]+=1
        anchor=sum((1<<i) for i,pi in enumerate(p) if pi>0.5)
        q=[min(pi,1-pi) for pi in p]; J=sum(q)
        mx["centered_influence_increase"]=max(mx["centered_influence_increase"],J-I)
        ent=H(mu)
        if J<=TOL:
            counts["centered_character"]+=1
            assert ent<=TOL
            continue
        W1=sum(mu[anchor^(1<<i)] for i in range(n)); r=W1/J
        mx["shell_fraction_over_one"]=max(mx["shell_fraction_over_one"],r-1.0)
        if r<=TOL:
            counts["zero_centered_shell_noncharacter"]+=1
            continue
        counts["positive_centered_shell"]+=1
        er=[]; de=[]
        for i,qi in enumerate(q):
            if qi<=TOL: continue
            counts["relevant_centered_coordinates"]+=1
            bit=1<<i
            B=sum(E(mu[t],mu[t|bit]) for t in range(N) if not(t&bit))
            er.append(B/qi)
            child=[]
            for bv in (0,1):
                sub=[vals[x] for x in range(N) if ((x>>i)&1)==bv]
                ch=fwht(sub); child.append(H([z*z for z in ch]))
            delta=ent-0.5*(child[0]+child[1])
            de.append(delta/qi)
        mx["erasure_selector"]=max(mx["erasure_selector"],min(er)-F(r))
        mx["decrement_selector"]=max(mx["decrement_selector"],min(de)-(F(r)+KAPPA))

status="PASS" if max(mx.values())<=TOL else "FAIL"
print(json.dumps({"status":status,"tolerance":TOL,"counts":counts,
                  "max_positive_violation":mx},indent=2,sort_keys=True))
