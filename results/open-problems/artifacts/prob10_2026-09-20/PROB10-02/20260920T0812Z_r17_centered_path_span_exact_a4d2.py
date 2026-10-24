#!/usr/bin/env python3
# Exact-integer checker for R17 PROB10-02 centered path-span theorem.
# Finite exhaustive checks use integer Bellman iteration; no simulation enters a claim.

import numpy as np

UV=((0,0),(0,1),(1,0),(1,1))

def bits(mask,m):
    return tuple((mask>>(m-1-i))&1 for i in range(m))

def transition(m,xmask,gmask,u,v):
    x=bits(xmask,m)
    g=bits(gmask,m)
    V=[0]
    for z in g:
        V.append(V[-1]+z)
    a=[int(z==v) for z in x]+[int(u==v)]
    Q=[0]*(m+1)
    Q[0]=max(V[1],V[0]+a[0])
    for k in range(1,m):
        Q[k]=max(Q[k-1],V[k]+a[k],V[k+1])
    Q[m]=max(Q[m-1],V[m]+a[m])
    gp=0
    for k in range(1,m+1):
        gp=(gp<<1)|(Q[k]-Q[k-1])
    xp=((xmask & ((1<<(m-1))-1))<<1)|u
    w=m//2
    rho=Q[w]-V[w]
    assert rho in (0,1)
    return xp,gp,rho

def precompute(m):
    ns=1<<(2*m)
    nxt=np.empty((4,ns),dtype=np.int32)
    rew=np.empty((4,ns),dtype=np.int8)
    mask=(1<<m)-1
    for s in range(ns):
        x=s>>m
        g=s&mask
        for a,(u,v) in enumerate(UV):
            xp,gp,r=transition(m,x,g,u,v)
            nxt[a,s]=(xp<<m)|gp
            rew[a,s]=r
    return nxt,rew

def exact_word_supremum(m):
    # D_n[s,t] = max of R(s)-R(t) over common words of length <= n.
    # Monotone Bellman iteration stabilizes exactly.  A fixed point then
    # certifies the supremum over all finite common source words.
    nxt,rew=precompute(m)
    ns=nxt.shape[1]
    D=np.zeros((ns,ns),dtype=np.int16)
    rr=rew.astype(np.int16)
    for it in range(1,100):
        new=np.zeros_like(D)
        for a in range(4):
            cand=(rr[a,:,None]-rr[a,None,:]) + D[np.ix_(nxt[a],nxt[a])]
            new=np.maximum(new,cand)
        new=np.maximum(new,0)
        if np.array_equal(new,D):
            return int(D.max()),it-1
        D=new
    raise RuntimeError("Bellman iteration did not stabilize")

def run_word(m,x,g,word):
    R=0
    for a in word:
        u,v=UV[a]
        x,g,r=transition(m,x,g,u,v)
        R+=r
    return R

print("R17 PROB10-02 exact centered path-span checker")
for m in (2,3,4,5):
    mx,it=exact_word_supremum(m)
    print(f"PAIR_BELLMAN m={m} exact_supremum={mx} stabilized_after={it}")
    assert mx==m

# General sharpness family: compare x=1^m,g=0 with x=0^m,g=0 under
# A=(u,v)=(0,1) repeated m times.  This is the genuine shared-source strip.
for m in range(1,13):
    A=1 # UV[1]=(0,1)
    word=[A]*m
    hi=run_word(m,(1<<m)-1,0,word)
    lo=run_word(m,0,0,word)
    print(f"TIGHT_FAMILY m={m} rewards=({hi},{lo}) difference={hi-lo}")
    assert hi==m and lo==0 and hi-lo==m

print("THEOREM_FINITE_EXHAUSTIVE_SUPPORT_PASS")
print("GENERAL_TIGHT_FAMILY_PASS")
print("ALL_EXACT_CHECKS_PASS")
