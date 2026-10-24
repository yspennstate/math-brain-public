#!/usr/bin/env python3
from collections import deque
from fractions import Fraction

UV=((0,0),(0,1),(1,0),(1,1))
L_SOURCE=Fraction(792665992,10**9)
U_SOURCE=Fraction(826275942762282626,10**18)

def transition_dp(w,state,uv):
    x,g=state;u,v=uv
    V=[0]
    for z in g: V.append(V[-1]+z)
    m=[int(z==v) for z in x]+[int(u==v)]
    Q=[0]*(2*w+1)
    Q[0]=max(V[1],V[0]+m[0])
    for k in range(1,2*w):
        Q[k]=max(Q[k-1],V[k]+m[k],V[k+1])
    Q[2*w]=max(Q[2*w-1],V[2*w]+m[2*w])
    gp=tuple(Q[k]-Q[k-1] for k in range(1,2*w+1))
    xp=tuple(x[1:])+(u,)
    reward=Q[w]-V[w]
    return (xp,gp),reward

def transition_carry(w,state,uv):
    x,g=state;u,v=uv
    L=2*w
    cprev=0; cs=[]
    for i in range(L):
        c=0 if g[i] else max(cprev,int(x[i]==v))
        cs.append(c);cprev=c
    gp=[]
    for i in range(L-1):
        c_before=cs[i]
        c_after=cs[i+1]
        gp.append(g[i+1]+c_after-c_before)
    gp.append((1-cs[-1])*int(u==v))
    reward=g[w]+cs[w]
    assert reward in (0,1)
    xp=tuple(x[1:])+(u,)
    return (xp,tuple(gp)),reward

def reachable_graph(w):
    s0=((0,)*(2*w),(0,)*(2*w))
    seen={s0};q=deque([s0]);states=[]
    while q:
        s=q.popleft();states.append(s)
        for uv in UV:
            t,_=transition_carry(w,s,uv)
            if t not in seen:
                seen.add(t);q.append(t)
    idx={s:i for i,s in enumerate(states)}
    tr=[];rs=[]
    for s in states:
        row=[];r=0
        for uv in UV:
            a=transition_dp(w,s,uv)
            b=transition_carry(w,s,uv)
            assert a==b
            t,z=b;row.append(idx[t]);r+=z
        tr.append(row);rs.append(r)
    return states,tr,rs

def exact_bellman_bracket(w,T):
    states,tr,v=reachable_graph(w)
    v=[int(x) for x in v]
    for _ in range(T):
        v=[v[a]+v[b]+v[c]+v[d] for a,b,c,d in tr]
    den=4**(T+1)
    return len(states),min(v),max(v),den

def tail_potential_min(w):
    L=2*w
    b=[Fraction(0) for _ in range(L)]
    for i in range(w,L-1): b[i]=Fraction(1)
    b[-1]=Fraction(2,3)
    dp={(0,0):Fraction(0)}
    for i in range(L):
        nd={}
        for (c0p,c1p),val in dp.items():
            for x in (0,1):
                for g in (0,1):
                    if g:
                        c0=c1=0
                    else:
                        c0=max(c0p,int(x==0));c1=max(c1p,int(x==1))
                    add=-b[i]*g
                    if i>=1:
                        gp0=g+c0-c0p; gp1=g+c1-c1p
                        add += b[i-1]*Fraction(gp0+gp1,2)
                    if i==w:
                        add += Fraction((1 if (g or c0) else 0)+(1 if (g or c1) else 0),2)
                    key=(c0,c1); nv=val+add
                    if key not in nd or nv<nd[key]: nd[key]=nv
        dp=nd
    best=None
    for (c0,c1),val in dp.items():
        nv=val+b[-1]*Fraction(2-c0-c1,4)
        if best is None or nv<best: best=nv
    return best

print('SOURCE_INTERVAL', L_SOURCE, U_SOURCE, 'WIDTH', U_SOURCE-L_SOURCE)
settings=[(1,12),(2,30),(3,40),(4,50),(5,40)]
for w,T in settings:
    N,lo,hi,den=exact_bellman_bracket(w,T)
    print('WIDTH',w,'REACHABLE',N,'T',T)
    print('BELLMAN_LO',lo,'/',den,'DEC',format(lo/den,'.15f'))
    print('BELLMAN_HI',hi,'/',den,'DEC',format(hi/den,'.15f'))
    print('BELLMAN_GAP',hi-lo,'/',den,'DEC',format((hi-lo)/den,'.15g'))
    if w==5:
        assert Fraction(hi,den) < L_SOURCE
        print('W5_CANNOT_MOVE_CURRENT_LOWER_ENDPOINT_PASS')
for w in (1,2,3,4,5,8,12,24,48):
    z=tail_potential_min(w)
    assert z==Fraction(2,3)
    print('TAIL_POTENTIAL_SPATIAL_MIN',w,z)
print('CARRY_FACTOR_EXACT_ON_ALL_ENUMERATED_REACHABLE_STATES_PASS')
print('ALL_EXACT_CHECKS_PASS')
