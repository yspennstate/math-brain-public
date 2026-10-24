#!/usr/bin/env python3
from fractions import Fraction

STATES = [(x,y,z) for x in (0,1) for y in (0,1) for z in (0,1)]

def comps8(D):
    for a0 in range(D+1):
      for a1 in range(D-a0+1):
       for a2 in range(D-a0-a1+1):
        for a3 in range(D-a0-a1-a2+1):
         for a4 in range(D-a0-a1-a2-a3+1):
          for a5 in range(D-a0-a1-a2-a3-a4+1):
           for a6 in range(D-a0-a1-a2-a3-a4-a5+1):
            a7=D-a0-a1-a2-a3-a4-a5-a6
            yield (a0,a1,a2,a3,a4,a5,a6,a7)

def phi_z_to_xy(c):
    D=sum(c)
    nz=[sum(cc for s,cc in zip(STATES,c) if s[2]==z) for z in (0,1)]
    nxy={(x,y):sum(cc for s,cc in zip(STATES,c) if (s[0],s[1])==(x,y))
         for x in (0,1) for y in (0,1)}
    best=Fraction(0)
    for z in (0,1):
        if nz[z]==0:
            continue
        tv=Fraction(0)
        for x in (0,1):
            for y in (0,1):
                joint=sum(cc for s,cc in zip(STATES,c) if s==(x,y,z))
                tv += abs(Fraction(joint,nz[z])-Fraction(nxy[x,y],D))
        best=max(best,tv/2)
    return best

def phi_zy_to_x(c):
    D=sum(c)
    px1=Fraction(sum(cc for s,cc in zip(STATES,c) if s[0]==1),D)
    groups=[]
    for y,z in ((0,0),(0,1),(1,0),(1,1)):
        n=sum(cc for s,cc in zip(STATES,c) if (s[1],s[2])==(y,z))
        x1=sum(cc for s,cc in zip(STATES,c)
               if (s[1],s[2])==(y,z) and s[0]==1)
        groups.append((n,x1))
    best=Fraction(0)
    for mask in range(1,16):
        n=sum(groups[i][0] for i in range(4) if (mask>>i)&1)
        if n==0:
            continue
        x1=sum(groups[i][1] for i in range(4) if (mask>>i)&1)
        best=max(best,abs(Fraction(x1,n)-px1))
    return best

def rho2_xz_y(c):
    D=sum(c)
    ny1=sum(cc for s,cc in zip(STATES,c) if s[1]==1)
    if ny1 in (0,D):
        return None
    py=Fraction(ny1,D)
    between=Fraction(0)
    for x,z in ((0,0),(0,1),(1,0),(1,1)):
        n=sum(cc for s,cc in zip(STATES,c) if (s[0],s[2])==(x,z))
        if n==0:
            continue
        y1=sum(cc for s,cc in zip(STATES,c)
               if (s[0],s[2])==(x,z) and s[1]==1)
        q=Fraction(y1,n)
        between += Fraction(n,D)*(q-py)**2
    return between/(py*(1-py))

D=10
BUDGET=Fraction(1,10)
total=nondeg=feasible=0
best=Fraction(-1)
maximizers=[]
for c in comps8(D):
    total += 1
    r2=rho2_xz_y(c)
    if r2 is None:
        continue
    nondeg += 1
    p1=phi_z_to_xy(c)
    p2=phi_zy_to_x(c)
    if max(p1,p2) <= BUDGET:
        feasible += 1
        if r2 > best:
            best=r2
            maximizers=[(c,p1,p2)]
        elif r2 == best:
            maximizers.append((c,p1,p2))

assert total == 19448
assert nondeg == 18876
assert feasible == 316
assert best == Fraction(1,9)
assert len(maximizers) == 24

w,p1,p2=maximizers[0]
assert w == (0,0,0,0,0,1,5,4)
assert p1 == Fraction(1,10)
assert p2 == 0

print("D0030 exact binary-grid scan")
print("state order:", STATES)
print("denominator:", D)
print("sequential phi budget:", BUDGET)
print("total compositions:", total)
print("nondegenerate-V2 compositions:", nondeg)
print("feasible compositions:", feasible)
print("max rho((V1,V3),V2)^2:", best)
print("number of maximizers:", len(maximizers))
print("canonical maximizer counts:", w)
print("phi(V3 ; V1,V2):", p1)
print("phi(V3,V2 ; V1):", p2)
print("ALL_EXACT_CHECKS_PASS")
