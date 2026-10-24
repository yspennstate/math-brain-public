#!/usr/bin/env python3
import itertools, math, json, hashlib, sys, time

TOL=5e-10

def fwht_int(vals):
    a=list(vals); n=len(a); h=1
    while h<n:
        for b in range(0,n,2*h):
            for j in range(b,b+h):
                x=a[j]; y=a[j+h]
                a[j]=x+y; a[j+h]=x-y
        h*=2
    return a

def entropy_probs(ps):
    return -sum(p*math.log2(p) for p in ps if p>0)

def eta(p):
    q=min(p,1-p)
    if q<=0: return 0.0
    if q>=0.5: return 1.0
    r=0.5+math.sqrt(q*(1-q))
    if r<=0 or r>=1: h=0.0
    else: h=-r*math.log2(r)-(1-r)*math.log2(1-r)
    return 1.0-h

def stats(vals):
    N=len(vals); n=N.bit_length()-1
    w=fwht_int(vals)
    den=N*N
    mu=[x*x/den for x in w]
    H=entropy_probs(mu)
    p=[sum(mu[s] for s in range(N) if (s>>i)&1) for i in range(n)]
    J=sum(min(x,1-x) for x in p)
    Phi=sum(eta(x) for x in p)
    return H,p,J,Phi,mu

def center(vals):
    H,p,J,Phi,mu=stats(vals)
    mask=sum(1<<i for i,x in enumerate(p) if x>0.5+1e-12)
    if mask:
        vals=[v*(-1 if ((x&mask).bit_count()&1) else 1) for x,v in enumerate(vals)]
        H,p,J,Phi,mu=stats(vals)
    return vals,H,p,J,Phi,mu

def partitions(n):
    # restricted growth strings, canonical set partitions
    if n==0:
        yield []
        return
    a=[0]*n
    def rec(i,mx):
        if i==n:
            blocks=[[] for _ in range(mx+1)]
            for j,b in enumerate(a): blocks[b].append(j)
            yield blocks
            return
        for b in range(mx+2):
            a[i]=b
            yield from rec(i+1,max(mx,b))
    a[0]=0
    yield from rec(1,0)

def affine_children(vals, blocks, anchors):
    n=(len(vals)).bit_length()-1
    nonanchors=[i for block,a in zip(blocks,anchors) for i in block if i!=a]
    d=len(nonanchors); m=len(blocks)
    # Each restriction z of nonanchor y_i = x_i xor x_anchor.
    children=[]
    for zraw in range(1<<d):
        z={i:(zraw>>r)&1 for r,i in enumerate(nonanchors)}
        out=[]
        for yraw in range(1<<m):
            x=0
            for b,(block,a) in enumerate(zip(blocks,anchors)):
                ya=(yraw>>b)&1
                if ya: x |= 1<<a
                for i in block:
                    if i==a: continue
                    xi=ya ^ z[i]
                    if xi: x |= 1<<i
            out.append(vals[x])
        children.append(out)
    return children

def quotient_distribution(mu, blocks):
    m=len(blocks)
    out=[0.0]*(1<<m)
    for s,p in enumerate(mu):
        y=0
        for b,block in enumerate(blocks):
            parity=0
            for i in block: parity ^= (s>>i)&1
            if parity: y|=1<<b
        out[y]+=p
    return out

def shell1(mu):
    return sum(mu[s] for s in range(len(mu)) if s.bit_count()==1)

def color_base_drop(mu,n,m):
    # average over all labeled m-colorings of J-Q; J from centered mu
    p=[sum(mu[s] for s in range(1<<n) if (s>>i)&1) for i in range(n)]
    J=sum(p)
    tot=0.0; cnt=0
    for colors in itertools.product(range(m), repeat=n):
        r=[0.0]*m
        for s,prob in enumerate(mu):
            if prob==0: continue
            par=[0]*m
            x=s
            while x:
                bit=(x & -x).bit_length()-1
                par[colors[bit]] ^= 1
                x &= x-1
            for b,v in enumerate(par):
                if v: r[b]+=prob
        Q=sum(min(x,1-x) for x in r)
        tot += J-Q
        cnt += 1
    return tot/cnt

def check_function(vals, n, counters):
    vals,H,p,J,Phi,mu=center(vals)
    counters["functions"]+=1
    W1=shell1(mu)
    # m-color averaged collision budget
    if J>1e-14:
        for m in (2,3):
            if m>n+1: continue
            av=color_base_drop(mu,n,m)
            rhs=(J-W1)/m
            counters["color_checks"]+=1
            counters["min_color_slack"]=min(counters["min_color_slack"], av-rhs)
            if av+TOL<rhs:
                raise AssertionError(("color",n,av,rhs))
    for blocks in partitions(n):
        if len(blocks)==n: continue
        # choose anchor maximizing eta(p_i)
        anchors=[max(block,key=lambda i: eta(p[i])) for block in blocks]
        children=affine_children(vals,blocks,anchors)
        child_stats=[stats(ch) for ch in children]
        avgH=sum(x[0] for x in child_stats)/len(child_stats)
        avgJ=sum(x[2] for x in child_stats)/len(child_stats)
        avgPhi=sum(x[3] for x in child_stats)/len(child_stats)
        dist=quotient_distribution(mu,blocks)
        HY=entropy_probs(dist)
        HXY=H-HY
        JS=HY-avgH
        rb=[]
        for b in range(len(blocks)):
            rb.append(sum(prob for y,prob in enumerate(dist) if (y>>b)&1))
        q=[min(x,1-x) for x in rb]
        Q=sum(q)
        M=sum(max(eta(p[i]) for i in block) for block in blocks)
        G=sum(eta(x) for x in q)-avgPhi
        D=J-avgJ
        deltaH=H-avgH
        deltaE=(H-Phi)-(avgH-avgPhi)
        rhs_corr=HXY+sum(eta(x) for x in q)-M-G
        counters["partition_checks"]+=1
        counters["min_D_minus_JQ"]=min(counters["min_D_minus_JQ"],D-(J-Q))
        counters["max_entropy_identity"]=max(counters["max_entropy_identity"],abs(deltaH-(HXY+JS)))
        counters["max_JS_bound_violation"]=max(counters["max_JS_bound_violation"],JS-(Phi-M))
        counters["max_corrected_violation"]=max(counters["max_corrected_violation"],deltaE-rhs_corr)
        counters["min_G"]=min(counters["min_G"],G)
        if abs(deltaH-(HXY+JS))>TOL: raise AssertionError(("entropy",n,deltaH,HXY,JS))
        if JS>Phi-M+TOL: raise AssertionError(("js",n,JS,Phi-M,blocks))
        if D+TOL<J-Q: raise AssertionError(("D",n,D,J-Q,blocks))
        if G<-TOL: raise AssertionError(("G",n,G,blocks))
        if deltaE>rhs_corr+TOL: raise AssertionError(("corr",n,deltaE,rhs_corr,blocks))

def main():
    counters={
      "functions":0,"partition_checks":0,"color_checks":0,
      "min_D_minus_JQ":1e100,"max_entropy_identity":0.0,
      "max_JS_bound_violation":-1e100,"max_corrected_violation":-1e100,
      "min_G":1e100,"min_color_slack":1e100
    }
    # exhaustive modulo global sign through n=3
    for n in (1,2,3):
        total=1<<((1<<n)-1)
        for mask in range(total):
            vals=[1]+[-1 if ((mask>>(x-1))&1) else 1 for x in range(1,1<<n)]
            check_function(vals,n,counters)
    # deterministic broad n=4 sample: first/last 1024 masks plus 2048 LCG masks
    n=4; total=1<<15
    masks=set(range(1024))|set(range(total-1024,total))
    x=17
    for _ in range(2048):
        x=(1103515245*x+12345)&0x7fffffff
        masks.add(x%total)
    for mask in sorted(masks):
        vals=[1]+[-1 if ((mask>>(x-1))&1) else 1 for x in range(1,1<<n)]
        check_function(vals,n,counters)
    counters["n4_sampled_functions"]=len(masks)
    counters["status"]="PASS"
    print(json.dumps(counters,sort_keys=True,indent=2))

if __name__=="__main__":
    main()
