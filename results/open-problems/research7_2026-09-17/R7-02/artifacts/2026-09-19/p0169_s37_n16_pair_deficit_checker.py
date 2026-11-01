#!/usr/bin/env python3
from math import comb
from collections import defaultdict, Counter

def ceildiv(a,b):
    assert b>0
    return -((-a)//b)

def enumerate_profiles(N,target16):
    C=[comb(N,k) for k in range(N+1)]
    c=[[0]*(N+1) for _ in range(6)]
    for j in range(6):
        for k in range(j,N+1):
            c[j][k]=comb(N-j,k-j)
    out=[]; prefixes=0
    for u0 in (0,1):
        for b1 in range(C[1]+1):
            u1=b1-c[0][1]*u0
            for b2 in range(C[2]+1):
                u2=b2-c[0][2]*u0-c[1][2]*u1
                for b3 in range(C[3]+1):
                    prefixes+=1
                    u3=b3-c[0][3]*u0-c[1][3]*u1-c[2][3]*u2
                    R=target16+16*u1+16*u2+12*u3
                    lo=-10**30; hi=10**30; feasible=True
                    for k in range(N+1):
                        base=u0*c[0][k]+u1*c[1][k]+u2*c[2][k]+u3*c[3][k]
                        A=5*base-c[5][k]*R
                        B=5*c[4][k]-8*c[5][k]
                        M=5*C[k]
                        if B==0:
                            if not (0<=A<=M):
                                feasible=False; break
                        elif B>0:
                            lo=max(lo,ceildiv(-A,B)); hi=min(hi,(M-A)//B)
                        else:
                            bb=-B
                            lo=max(lo,ceildiv(A-M,bb)); hi=min(hi,A//bb)
                        if lo>hi:
                            feasible=False; break
                    if not feasible: continue
                    residue=(-2*R)%5
                    start=lo+((residue-lo)%5)
                    for u4 in range(start,hi+1,5):
                        u5=(-R-8*u4)//5
                        mu16=32*u0+16*u1+8*u2+4*u3+2*u4+u5-16
                        u=(u0,u1,u2,u3,u4,u5)
                        b=tuple(sum(u[j]*c[j][k] for j in range(6)) for k in range(N+1))
                        assert all(0<=b[k]<=C[k] for k in range(N+1))
                        assert -16*u1-16*u2-12*u3-8*u4-5*u5==target16
                        assert mu16*(2**N)==32*sum(b)-16*(2**N)
                        out.append((u,b,mu16))
    return prefixes,out

def q2_from_u(u):
    return 8*u[2]+12*u[3]+12*u[4]+10*u[5]

def dedup_by_up(arr):
    d={}
    for z in arr:
        d.setdefault(z['up'],z)
    return list(d.values())

def all_comp_sums(total,vecs):
    out=defaultdict(list)
    m=len(vecs)
    if m==0: return out
    def rec(i,rem,acc,counts):
        if i==m-1:
            x=rem
            sv=tuple(acc[j]+x*vecs[i][j] for j in range(6))
            out[sv].append(tuple(counts+[x]))
            return
        for x in range(rem+1):
            rec(i+1,rem-x,[acc[j]+x*vecs[i][j] for j in range(6)],counts+[x])
    rec(0,total,[0]*6,[])
    return out

print("P0169 S=37,n=16 B11/B12/B25 exact reduction")
print("arithmetic=integer; floating_point=False")

# B12 parent atlas.
p16,parents=enumerate_profiles(16,37)
assert p16==2307954 and len(parents)==254
assert Counter(z[2] for z in parents)==Counter({1:100,-1:100,3:27,-3:27})
assert all(q2_from_u(z[0])%4==2 for z in parents)
print("N16_L37_profiles",len(parents),"mu16_hist",sorted(Counter(z[2] for z in parents).items()))
q2small=[z for z in parents if abs(q2_from_u(z[0]))==2]
assert len(q2small)==50
# The one-coordinate deficit bound gives sum_i |t_i|<=5 and
# sum_i t_i=2Q2, so only Q2=+/-2 can survive.  The involution
# h(x)=-f(-x) keeps every oriented singleton coefficient fixed and flips
# every even Fourier level, so we may take Q2=+2 without loss.
q2plus=[z for z in q2small if q2_from_u(z[0])==2]
assert len(q2plus)==25
assert Counter(z[2] for z in q2plus)==Counter({-1:19,1:6})
print("B12_after_deficit_Q2_filter","Q2=+2 wlog","parents",len(q2plus),"mu16_hist",sorted(Counter(z[2] for z in q2plus).items()))

# Only these child masses are needed after the B12 mean argument:
# A=(e,t)=(0,0): plus/minus L=35, means +1/-3;
# B=(0,2): plus L35 mean+3, minus L31 mean-5;
# C=(1,0): plus/minus L34, means +2/-4;
# D=(1,2): plus L34 mean+4, minus L30 mean-6.
need=(30,31,34,35)
expected={30:1534,31:1282,34:573,35:376}
profiles={}
for L in need:
    p,o=enumerate_profiles(15,L)
    assert p==1546752 and len(o)==expected[L]
    profiles[L]=o
    print("N15_L",L,"profiles",len(o),"mu16_set",sorted({z[2] for z in o}))

# Exact mean sets prove the B12 collapse after the Q2=+2 normalization.
assert sorted({z[2] for z in profiles[35]})==[-3,-1,1,3]
assert sorted({z[2] for z in profiles[34]})==[-4,-2,0,2,4]
# Among Q2=+2 parents only mu=+/-1 occur.  If mu=+1, the plus-child
# mean constraints force t=0 at every coordinate, contradicting sum t=4.
# Thus mu=-1. Then the plus-child mean sets force t in {0,2}; since sum t=4,
# exactly two coordinates have t=2 and fourteen have t=0.
print("B12_forced_parent_mu16",-1)
print("B12_forced_t_pattern","two t=2; fourteen t=0")

idx={}
for L,arr in profiles.items():
    for z in arr:
        idx.setdefault((L,z[2]),{})[z[1]]=z

cat_data={
 'A':dict(e=0,t=0,s=2,Lp=35,Lm=35,mup=1,mum=-3,row3_lb=-15),
 'B':dict(e=0,t=2,s=4,Lp=35,Lm=31,mup=3,mum=-5,row3_lb=-17),
 'C':dict(e=1,t=0,s=3,Lp=34,Lm=34,mup=2,mum=-4,row3_lb=-22),
 'D':dict(e=1,t=2,s=5,Lp=34,Lm=30,mup=4,mum=-6,row3_lb=-24),
}

def coordinate_types(parent):
    U,b,mu=parent
    assert mu==-1
    parentQ2=q2_from_u(U)
    assert parentQ2==2
    groups=defaultdict(list)
    for name,d in cat_data.items():
        pluses=[z for z in profiles[d['Lp']] if z[2]==d['mup']]
        minusdict=idx.get((d['Lm'],d['mum']),{})
        for zp in pluses:
            bp=zp[1]
            if b[0]!=bp[0]: continue
            bm=tuple(b[q+1]-(bp[q+1] if q+1<=15 else 0) for q in range(16))
            zm=minusdict.get(bm)
            if zm is None: continue
            # R3_i = Q2(child-plus)-Q2(parent)+R2_i.
            R3=q2_from_u(zp[0])-parentQ2+d['t']
            # B25 pair-deficit bound:
            # u_ij >= |t_i-t_j|-(s_i+s_j-2). Summing j!=i gives
            # 2R3_i >= 4-35=-31 (A), 28-63=-35 (B),
            # 4-49=-45 (C), 28-77=-49 (D), hence the integer bounds above.
            if R3 < d['row3_lb']:
                continue
            groups[name].append(dict(up=zp[0],um=zm[0],R3=R3))
    for k in list(groups):
        groups[k]=dedup_by_up(groups[k])
    return groups

def solve(parent,groups,scenario):
    U=parent[0]
    target=tuple((16-j)*U[j] for j in range(6))
    sols=[]
    if scenario=="C": # 13A+2B+1C
        if not(groups['A'] and groups['B'] and groups['C']): return sols
        amap=all_comp_sums(13,[z['up'] for z in groups['A']])
        for ci,c in enumerate(groups['C']):
            for bi,b1 in enumerate(groups['B']):
                for bj in range(bi,len(groups['B'])):
                    b2=groups['B'][bj]
                    req=tuple(target[j]-c['up'][j]-b1['up'][j]-b2['up'][j] for j in range(6))
                    for ac in amap.get(req,[]):
                        sols.append((ac,ci,bi,bj))
    else: # 14A+1B+1D
        if not(groups['A'] and groups['B'] and groups['D']): return sols
        amap=all_comp_sums(14,[z['up'] for z in groups['A']])
        for di,d in enumerate(groups['D']):
            for bi,b in enumerate(groups['B']):
                req=tuple(target[j]-d['up'][j]-b['up'][j] for j in range(6))
                for ac in amap.get(req,[]):
                    sols.append((ac,di,bi))
    return sols

survivors=Counter()
type_counts={}
for parent in parents:
    if parent[2]!=-1 or q2_from_u(parent[0])!=2: continue
    g=coordinate_types(parent)
    for sc in ("C","D"):
        n=len(solve(parent,g,sc))
        if n:
            survivors[(parent[0],sc)]+=n
            type_counts[(parent[0],sc)]={k:len(g[k]) for k in "ABCD"}

expected_survivors=Counter({
 ((0,5,-1,-39,64,-29),"C"):9,
 ((0,5,-1,-39,64,-29),"D"):6,
})
assert survivors==expected_survivors
print("B25_exact_newton_incidence_survivors",sum(survivors.values()))
print("B25_surviving_parent_u",(0,5,-1,-39,64,-29))
print("B25_scenario_counts",sorted((sc,n) for (u,sc),n in survivors.items()))
print("B25_type_counts",type_counts)

# B11 Parseval budget for the sole remaining parent.
U=(0,5,-1,-39,64,-29)
pstar=next(p for p in parents if p[0]==U)
def kraw(N,r,k):
    return sum((-1)**j*comb(k,j)*comb(N-k,r-j)
               for j in range(max(0,r-(N-k)),min(r,k)+1))
Q=[]
for r in range(6):
    num=sum((2*pstar[1][k]-comb(16,k))*kraw(16,r,k) for k in range(17))
    assert (16*num)%65536==0
    Q.append((16*num)//65536)
Q=tuple(Q)
assert Q==(-1,37,2,-66,-17,29)
# The t-row vector is (2,2,0,...,0). Pair-level square cost cannot be 2:
# two unit edges cannot give degree vector (2,2,0,...); one coefficient 2
# realizes cost 4, so the exact minimum is 4.
level2_square_min=4
base_C=1+93+4+66+17+29
base_D=1+97+4+66+17+29
assert (base_C,base_D)==(210,214)
print("B11_Q0_to_Q5",Q)
print("B11_parseval_base_C",base_C,"excess_budget",256-base_C)
print("B11_parseval_base_D",base_D,"excess_budget",256-base_D)
print("S37_n16_status","NOT_ELIMINATED")
print("remaining_exact_newton_multisets",15)
print("ASSERTIONS_PASS")
