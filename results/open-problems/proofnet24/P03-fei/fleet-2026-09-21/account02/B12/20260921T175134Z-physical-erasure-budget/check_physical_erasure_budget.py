#!/usr/bin/env python3
import itertools, math, json, hashlib

TOL=1e-11

def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p*math.log2(p)-(1-p)*math.log2(1-p)

def walsh(vals):
    a=[float(v) for v in vals]
    n=len(a)
    h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j]=x+y
                a[j+h]=x-y
        h*=2
    return [x/n for x in a]

def entropy(ps):
    return -sum(p*math.log2(p) for p in ps if p>0.0)

def dtc_uniform(indices,m):
    M=len(indices)
    if M==0:
        return 0.0
    H=math.log2(M)
    cond=0.0
    for i in range(m):
        counts={}
        mask=~(1<<i)
        for x in indices:
            key=x & mask
            counts[key]=counts.get(key,0)+1
        # Fibres have size 1 or 2. The bit entropy is 1 exactly on a size-2 fibre.
        cond += sum(c/M for c in counts.values() if c==2)
    return H-cond

def all_subcubes(m):
    N=1<<m
    cubes=[]
    for pat in itertools.product((-1,0,1), repeat=m): # -1 means free
        pts=set()
        for x in range(N):
            if all(s==-1 or ((x>>i)&1)==s for i,s in enumerate(pat)):
                pts.add(x)
        cubes.append((pat,pts))
    return cubes

def spectral_law(vals):
    N=len(vals)
    j=sum(v*v for v in vals)/N
    c=walsh(vals)
    return [x*x/j for x in c]

def metrics(vals):
    N=len(vals); m=N.bit_length()-1
    E=[x for x,v in enumerate(vals) if v]
    M=len(E); j=M/N
    pos=[x for x,v in enumerate(vals) if v==1]
    neg=[x for x,v in enumerate(vals) if v==-1]
    a=len(pos)/M
    Hsign=h2(a)
    DTC=(len(pos)/M)*dtc_uniform(pos,m)+(len(neg)/M)*dtc_uniform(neg,m)

    I_E=0.0
    d=0.0
    for i in range(m):
        for x in range(N):
            y=x^(1<<i)
            I_E += (1.0 if ((vals[x]!=0)!=(vals[y]!=0)) else 0.0)/N
            d += (((vals[x]-vals[y])/2.0)**2)/N

    L=math.log2(1.0/j)
    Delta=d/j-0.5*L
    slack_iso=I_E-2*j*L
    slack_sign=4*d-I_E
    Ephys=Hsign+DTC
    rhs=slack_iso/(2*j)+slack_sign/(4*j)

    nu=spectral_law(vals)
    mean=sum(nu[s]*s.bit_count() for s in range(N))
    return {
        "j":j, "Hsign":Hsign, "DTC":DTC, "Ephys":Ephys,
        "Delta":Delta, "slack_iso":slack_iso, "slack_sign":slack_sign,
        "rhs":rhs, "spectral_mean":mean, "d_over_j":d/j,
    }

def tv(p,q):
    return 0.5*sum(abs(a-b) for a,b in zip(p,q))

def run():
    summary={"schema_version":1,"status":"PASS","dimensions":{}}
    max_identity=0.0
    max_mean=0.0
    max_tv_violation=0.0
    total=0
    tv_checks=0
    cubes={m:all_subcubes(m) for m in (1,2,3)}

    for m in (1,2,3):
        N=1<<m
        cnt=0
        for vals in itertools.product((-1,0,1), repeat=N):
            if not any(vals):
                continue
            M=metrics(vals)
            e1=abs(M["Ephys"]-M["rhs"])
            e2=abs(M["Delta"]-(M["slack_iso"]+M["slack_sign"])/(4*M["j"]))
            e3=abs(M["spectral_mean"]-M["d_over_j"])
            max_identity=max(max_identity,e1,e2)
            max_mean=max(max_mean,e3)
            assert M["slack_iso"]>=-TOL
            assert M["slack_sign"]>=-TOL
            assert M["Ephys"]+TOL>=M["Delta"]
            assert M["Ephys"]<=2*M["Delta"]+TOL

            E={x for x,v in enumerate(vals) if v}
            pat,Q=min(cubes[m], key=lambda pq: len(E.symmetric_difference(pq[1])))
            delta=len(E.symmetric_difference(Q))/len(E)
            assert delta<1.0
            pos=sum(v==1 for v in vals); neg=sum(v==-1 for v in vals)
            theta=min(pos,neg)/len(E)
            sigma=1 if pos>=neg else -1
            proxy=[sigma if x in Q else 0 for x in range(N)]
            actual=tv(spectral_law(vals),spectral_law(proxy))
            bound=math.sqrt(delta+4*theta)+delta/(1+math.sqrt(1-delta))
            max_tv_violation=max(max_tv_violation,actual-bound)
            assert actual<=bound+TOL
            tv_checks+=1
            cnt+=1
        summary["dimensions"][str(m)]={"nonzero_ternary_functions":cnt}
        total+=cnt

    tail=[]
    for k in (2,4,8,16,32):
        eps=1.0/k
        log2N=k*k
        entropy_excess=h2(eps)+eps*log2N
        mean_excess=eps
        tail.append({
            "k":k,
            "tv":eps,
            "mean_excess":mean_excess,
            "entropy_excess":entropy_excess,
            "entropy_excess_over_mean_excess":entropy_excess/mean_excess,
        })
    assert tail[-1]["tv"]<tail[0]["tv"]
    assert tail[-1]["entropy_excess"]>tail[0]["entropy_excess"]

    summary.update({
        "ternary_functions_checked":total,
        "tv_proxy_checks":tv_checks,
        "max_abs_conservation_error":max_identity,
        "max_abs_parseval_mean_error":max_mean,
        "max_tv_bound_violation":max_tv_violation,
        "synthetic_tv_mean_shannon_obstruction":tail,
    })
    payload=json.dumps(summary,sort_keys=True,separators=(",",":"))
    summary["result_digest_sha256"]=hashlib.sha256(payload.encode()).hexdigest()
    print(json.dumps(summary,indent=2,sort_keys=True))

if __name__=="__main__":
    run()
