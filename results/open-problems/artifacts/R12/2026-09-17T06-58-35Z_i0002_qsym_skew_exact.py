#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations
from math import comb

# Exact finite-core self-check for R12 / I0002.

def padd(a,b):
    c=dict(a)
    for k,v in b.items():
        c[k]=c.get(k,F(0))+v
        if c[k]==0: del c[k]
    return c

def pscale(a,s): return {k:v*s for k,v in a.items() if v*s}

def pmul_lin(a,c0,c1):
    out={}
    for k,v in a.items():
        out[k]=out.get(k,F(0))+v*c0
        out[k+1]=out.get(k+1,F(0))+v*c1
    return {k:v for k,v in out.items() if v}

def pmul(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items(): out[i+j]=out.get(i+j,F(0))+x*y
    return {k:v for k,v in out.items() if v}

def canon(d): return tuple(sorted(d.items()))
def deanon(t): return dict(t)

# Embedded Manhattan q-interpolation:
# horizontal lines remain statically oriented; at a vertical attempt on column x,
# direction d has conditional probability (1+d*q*V_x)/2.
def step_states(states, force_axis=None):
    ns={}
    axes=(force_axis,) if force_axis else ('H','V')
    for (x,y,Ht,Vt),p in states.items():
        H=deanon(Ht); V=deanon(Vt)
        for axis in axes:
            axis_prob=F(1) if force_axis else F(1,2)
            if axis=='H':
                orientations=[(H[y],F(1))] if y in H else [(1,F(1,2)),(-1,F(1,2))]
                for d,pe in orientations:
                    H2=dict(H); H2[y]=d
                    key=(x+d,y,canon(H2),Vt)
                    pp=pscale(p,axis_prob*pe)
                    ns[key]=padd(ns.get(key,{}),pp)
            else:
                orientations=[(V[x],F(1))] if x in V else [(1,F(1,2)),(-1,F(1,2))]
                for v,pe in orientations:
                    V2=dict(V); V2[x]=v
                    for d in (1,-1):
                        pp=pscale(p,axis_prob*pe)
                        pp=pmul_lin(pp,F(1,2),F(d*v,2))
                        key=(x,y+d,Ht,canon(V2))
                        ns[key]=padd(ns.get(key,{}),pp)
    return ns

def full_return(n):
    st={(0,0,(),()):{0:F(1)}}
    for _ in range(n): st=step_states(st)
    out={}
    for (x,y,_,_),p in st.items():
        if x==0 and y==0: out=padd(out,p)
    return out

def word_return(word):
    st={(0,0,(),()):{0:F(1)}}
    for a in word: st=step_states(st,a)
    out={}
    for (x,y,_,_),p in st.items():
        if x==0 and y==0: out=padd(out,p)
    return out

def qeven_to_y(p):
    assert all(k%2==0 for k in p)
    out={}
    for e,a in p.items():
        k=e//2
        for j in range(k+1):
            out[j]=out.get(j,F(0))+a*F(comb(k,j))*((-1)**j)
    return {j:v for j,v in sorted(out.items()) if v}

expected={
2:{1:F(1,8)},
4:{0:F(1,32),2:F(3,128)},
6:{0:F(3,128),1:F(3,512),2:F(3,1024),3:F(5,1024)},
8:{0:F(5,256),1:F(3,1024),2:F(7,2048),3:F(1,512),4:F(35,32768)},
}
for n,e in expected.items():
    py=qeven_to_y(full_return(n))
    assert py==e,(n,py,e)
    assert all(v>=0 for v in py.values())
    print(f'n={n} p_n(q)=sum c_j(1-q^2)^j coefficients:', py)

bad=word_return('HVVHVV')
assert bad=={0:F(1,16),2:F(1,8),4:F(1,16)}
print('fixed axis word HVVHVV:',bad,'=(1+q^2)^2/16')

# Four-state exact no-go for generic heat-trace monotonicity under an
# additional Frobenius-orthogonal divergence-free skew perturbation.
def mat_add(A,B): return [[A[i][j]+B[i][j] for j in range(4)] for i in range(4)]
def mat_scale(A,c): return [[c*A[i][j] for j in range(4)] for i in range(4)]
def cyc(a,b,c):
    M=[[F(0) for _ in range(4)] for __ in range(4)]
    cyc=(a,b,c)
    for k in range(3):
        i,j=cyc[k],cyc[(k+1)%3]
        M[i][j]+=1; M[j][i]-=1
    return M
S=[[F(-3) if i==j else F(1) for j in range(4)] for i in range(4)]
C1,C2,C3=cyc(0,1,2),cyc(0,2,3),cyc(0,1,3)
A=mat_add(mat_add(mat_scale(C1,F(2,3)),C2),mat_scale(C3,F(-1)))
B=mat_scale(C1,F(-2,3))
G0=mat_add(S,A); G1=mat_add(G0,B)
for M in (A,B):
    assert all(M[i][j]==-M[j][i] for i in range(4) for j in range(4))
    assert all(sum(M[i])==0 for i in range(4))
assert sum(A[i][j]*B[i][j] for i in range(4) for j in range(4))==0
for G in (G0,G1):
    assert all(sum(G[i])==0 for i in range(4))
    assert all(G[i][j]>=0 for i in range(4) for j in range(4) if i!=j)
    assert all((G[i][j]+G[j][i])/2==S[i][j] for i in range(4) for j in range(4))

def perm_sign(p):
    inv=sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])
    return -1 if inv%2 else 1

def charpoly(G):
    ans={}
    for p in permutations(range(4)):
        term={0:F(1)}
        for i,j in enumerate(p):
            entry={}
            if i==j: entry[1]=F(1)
            if G[i][j]: entry[0]=entry.get(0,F(0))-G[i][j]
            term=pmul(term,entry)
        ans=padd(ans,pscale(term,F(perm_sign(p))))
    return ans

def poly_from_factors(fs):
    r={0:F(1)}
    for f in fs: r=pmul(r,f)
    return r
cp0=charpoly(G0); cp1=charpoly(G1)
target0=poly_from_factors([{1:F(1)},{0:F(4),1:F(1)},{0:F(56,3),1:F(8),2:F(1)}])
target1=poly_from_factors([{1:F(1)},{0:F(4),1:F(1)},{0:F(20),1:F(8),2:F(1)}])
assert cp0==target0,(cp0,target0)
assert cp1==target1,(cp1,target1)
print('charpoly G0 = lambda(lambda+4)(lambda^2+8lambda+56/3)')
print('charpoly G1 = lambda(lambda+4)(lambda^2+8lambda+20)')
print('A,B Frobenius-orthogonal; G0,G1 valid Eulerian generators with same symmetric part.')
print('Hence at t=pi: Tr exp(tG1)-Tr exp(tG0)')
print('=2 exp(-4pi)[1-cos(2pi sqrt(6)/3)] > 0 exactly.')
print('ALL_EXACT_CHECKS_PASS')
