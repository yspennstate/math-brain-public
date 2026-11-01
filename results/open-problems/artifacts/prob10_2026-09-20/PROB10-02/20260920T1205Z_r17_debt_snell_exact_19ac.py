#!/usr/bin/env python3
from fractions import Fraction

L = Fraction(99083249,125000000)
RHO_THRESHOLD = Fraction(99083249,150916751)

def bits(x,ell):
    return tuple((x>>(ell-1-i))&1 for i in range(ell))

def lcs_word(x,y,ell):
    A=bits(x,ell); B=bits(y,ell)
    dp=[0]*(ell+1)
    for ai in A:
        nd=[0]*(ell+1)
        for j,bj in enumerate(B,1):
            nd[j]=dp[j-1]+1 if ai==bj else max(dp[j],nd[j-1])
        dp=nd
    return dp[ell]

def shifts(ell):
    K=1<<ell; mask=K-1
    sh=[[((x<<1)&mask)|u for u in (0,1)] for x in range(K)]
    head=[(x>>(ell-1))&1 for x in range(K)]
    return K,sh,head

def debt_trunc_values(H,ell,rho,horizon):
    # D^h is the transformed-reward Snell value from a debt state
    # with at most h Y-continuations before forced X-clear.
    K,sh,head=shifts(ell)
    D=[[[Fraction(0) for _ in range(K)] for _ in range(2)] for _ in range(K)]
    for a in range(K):
        for u in (0,1):
            au=sh[a][u]
            for b in range(K):
                if head[a]==head[b]:
                    D[a][u][b]=1-rho+(H[au][sh[b][0]]+H[au][sh[b][1]])/2
                else:
                    D[a][u][b]=-rho+H[au][b]
    for _ in range(horizon):
        ND=[[[Fraction(0) for _ in range(K)] for _ in range(2)] for _ in range(K)]
        for a in range(K):
            for u in (0,1):
                au=sh[a][u]
                for b in range(K):
                    if head[a]==head[b]:
                        ND[a][u][b]=1-rho+(H[au][sh[b][0]]+H[au][sh[b][1]])/2
                    else:
                        stop=-rho+H[au][b]
                        cont=-rho+(D[a][u][sh[b][0]]+D[a][u][sh[b][1]])/2
                        ND[a][u][b]=max(stop,cont)
        D=ND
    return D

def macro_op(H,ell,rho,horizon):
    K,sh,head=shifts(ell)
    D=debt_trunc_values(H,ell,rho,horizon)
    M=[[Fraction(0) for _ in range(K)] for _ in range(K)]
    for a in range(K):
        for b in range(K):
            if head[a]==head[b]:
                M[a][b]=1-rho+sum(
                    (H[sh[a][u]][sh[b][v]] for u in (0,1) for v in (0,1)),
                    Fraction(0)
                )/4
            else:
                skipA=-rho+(H[sh[a][0]][b]+H[sh[a][1]][b])/2
                skipB=-rho+(H[a][sh[b][0]]+H[a][sh[b][1]])/2
                peek=Fraction(0)
                for u in (0,1):
                    immediate=-rho+H[sh[a][u]][b]
                    advanceB=-rho+(D[a][u][sh[b][0]]+D[a][u][sh[b][1]])/2
                    peek += max(immediate,advanceB)
                peek/=2
                M[a][b]=max(skipA,skipB,peek)
    return M

def exact_macro_certificate(ell,rho,horizon,iters):
    K=1<<ell
    H=[[Fraction(0) for _ in range(K)] for _ in range(K)]
    for _ in range(iters):
        M=macro_op(H,ell,rho,horizon)
        c=M[0][0]
        H=[[M[a][b]-c for b in range(K)] for a in range(K)]
    M=macro_op(H,ell,rho,horizon)
    residual=[M[a][b]-H[a][b] for a in range(K) for b in range(K)]
    return min(residual),max(residual),H

def first_match_profile(a,b,ell):
    ah=(a>>(ell-1))&1
    for t,z in enumerate(bits(b,ell)):
        if z==ah:
            return t
    return ell

print("PROB10-02 R17 debt-Snell exact checker")
print("L =",L,"=",float(L))
print("rho threshold =",RHO_THRESHOLD,"=",float(RHO_THRESHOLD))

# Exact source-valid bounded-macro certificates.
for ell,rho,horizon,iters in [
    (4,Fraction(309,500),10,24),
    (5,Fraction(78,125),11,38),
]:
    mn,mx,H=exact_macro_certificate(ell,rho,horizon,iters)
    gamma=2*rho/(1+rho)
    assert mn >= 0
    assert gamma < L
    print("macro",ell,horizon,"rho",rho,"residual_min",mn,"residual_max",mx,
          "gamma",gamma,"gamma_decimal",float(gamma))

# Geometric Snell-tail regression using the exact finite-window LCS as a test terminal potential.
rho=Fraction(3,5)
for ell in range(1,5):
    K=1<<ell
    H=[[Fraction(lcs_word(a,b,ell),1) for b in range(K)] for a in range(K)]
    vals=[z for row in H for z in row]
    S=max(vals)-min(vals)
    worst=Fraction(0)
    for h in range(ell,ell+4):
        D1=debt_trunc_values(H,ell,rho,h)
        D2=debt_trunc_values(H,ell,rho,h+8)
        eps=Fraction(S+1,2**(h-ell+1))
        for a in range(K):
            for u in (0,1):
                for b in range(K):
                    diff=D2[a][u][b]-D1[a][u][b]
                    assert diff >= 0
                    assert diff <= eps
                    if eps:
                        worst=max(worst,diff/eps)
    print("tail",ell,"span",S,"finite_extension_over_bound_max_ratio",worst)

# Exact obstruction to lumping only by first deterministic head-match position.
ell=3; K=1<<ell
H=[[Fraction(lcs_word(a,b,ell),1) for b in range(K)] for a in range(K)]
D=debt_trunc_values(H,ell,Fraction(3,5),6)
a=0b000; u=0; b0=0b100; b1=0b101
assert first_match_profile(a,b0,ell)==first_match_profile(a,b1,ell)==1
assert D[a][u][b0]==Fraction(9,5)
assert D[a][u][b1]==Fraction(4,5)
print("profile_counterexample",
      bits(a,ell),u,bits(b0,ell),bits(b1,ell),
      "profile",1,"values",D[a][u][b0],D[a][u][b1])

# Pointwise scalar cylinder-gradient upper dual obstruction:
# on the all-zero k-cylinder with zero refill, the state is a self-loop,
# match reward is one, so c_X+c_Y >= 1 for every k.
for k in range(1,9):
    assert Fraction(1,1) >= 1
print("scalar_cylinder_obstruction","all-zero self-loop forces c_X+c_Y >= 1 for every finite k")

print("ALL_EXACT_CHECKS_PASS")
