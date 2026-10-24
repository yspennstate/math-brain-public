#!/usr/bin/env python3
"""Exact sanity checker for P13 strong strip-span theorem.

True model: two independent iid binary strings. One source-pair letter (u,v)
updates a whole strip column with the SAME v in every match indicator. No
independent Bernoulli matching array is used.

The theorem proved in the accompanying report is analytic and all-width:
for m=2w, every common future source word and all formal boundary states s,t,
|R_N(s)-R_N(t)| <= m. This checker exhaustively verifies the pathwise
statement for every source word through horizon m at m=2,4,6 and exhibits
a sharp span-m word B^m. All checks use exact integer arithmetic.
"""
import numpy as np

UV = ((0,0),(0,1),(1,0),(1,1))  # C,A,B,D
NAME = "CABD"
B_INDEX = 2

def bits(mask,m):
    return tuple((mask>>(m-1-i))&1 for i in range(m))

def transition_q(m,xmask,gmask,u,v):
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
    rho=Q[m//2]-V[m//2]
    assert rho in (0,1)
    return xp,gp,rho

def tables(m):
    ns=1<<(2*m)
    nxt=np.empty((4,ns),dtype=np.int32)
    rew=np.empty((4,ns),dtype=np.int8)
    for x in range(1<<m):
        for g in range(1<<m):
            s=(x<<m)|g
            for a,(u,v) in enumerate(UV):
                xp,gp,r=transition_q(m,x,g,u,v)
                nxt[a,s]=(xp<<m)|gp
                rew[a,s]=r
    return nxt,rew

def exhaustive_prefix_span(m):
    nxt,rew=tables(m)
    ns=nxt.shape[1]
    root_state=np.arange(ns,dtype=np.int32)
    root_reward=np.zeros(ns,dtype=np.int16)
    checked=0
    max_span=-1
    witness=""
    by_depth=[0]*(m+1)

    def dfs(depth,state,reward,word):
        nonlocal checked,max_span,witness
        span=int(reward.max())-int(reward.min())
        assert span<=m, (m,word,span)
        checked+=1
        by_depth[depth]+=1
        if span>max_span:
            max_span=span
            witness=word
        if depth==m:
            return
        for a in range(4):
            r2=reward+rew[a,state]
            s2=nxt[a,state]
            dfs(depth+1,s2,r2,word+NAME[a])

    dfs(0,root_state,root_reward,"")
    return checked,by_depth,max_span,witness,nxt,rew

def sharp_B_word(m,nxt,rew):
    ns=nxt.shape[1]
    state=np.arange(ns,dtype=np.int32)
    reward=np.zeros(ns,dtype=np.int16)
    for _ in range(m):
        reward += rew[B_INDEX,state]
        state = nxt[B_INDEX,state]
    lo=int(reward.min()); hi=int(reward.max())
    imin=int(reward.argmin()); imax=int(reward.argmax())
    def decode(s):
        mask=(1<<m)-1
        return bits(s>>m,m),bits(s&mask,m)
    return lo,hi,decode(imin),decode(imax)

print("P13 exact true-binary strip-span checker")
print("alphabet order C=(0,0), A=(0,1), B=(1,0), D=(1,1)")
for m in (2,4,6):
    checked,by_depth,max_span,witness,nxt,rew=exhaustive_prefix_span(m)
    lo,hi,smin,smax=sharp_B_word(m,nxt,rew)
    assert max_span==m
    assert hi-lo==m
    print(f"m={m} w={m//2} prefixes_checked={checked} by_depth={by_depth}")
    print(f"m={m} maximum_pathwise_span={max_span} first_witness={witness!r}")
    print(f"m={m} B^m_span={hi-lo} min={lo} max={hi}")
    print(f"m={m} B^m_min_state={smin} B^m_max_state={smax}")

m=12
print(f"proved_all_width_transfer_at_w=6: old_C<=2m={2*m}, new_C<=m={m}")
print("finite_to_infinite_interval_radius_at_w=6: old=24/N new=12/N")
print("SOURCE_ENDPOINT_NOT_INFERRED_FROM_FINITE_ENUMERATION")
print("ALL_EXACT_CHECKS_PASS")
