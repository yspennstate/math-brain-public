from fractions import Fraction
from itertools import combinations, product
import itertools, math, time

BITS=list(itertools.product([0,1],repeat=4))
IDX={b:i for i,b in enumerate(BITS)}

A_BITS=[
["0000","0001","0010","0100","1000"],["0001","0010","0011","0100","1000"],
["0001","0011","0100","0101","1000"],["0001","0011","0101","1000","1001"],
["0010","0011","0100","0110","1000"],["0010","0011","0110","1000","1010"],
["0011","0100","0101","0110","1000"],["0011","0101","0110","0111","1001"],
["0011","0101","0110","1000","1001"],["0011","0110","0111","1001","1010"],
["0011","0110","1000","1001","1010"],["0011","0111","1001","1010","1011"],
["0100","0101","0110","1000","1100"],["0101","0110","0111","1001","1100"],
["0101","0110","1000","1001","1100"],["0101","0111","1001","1100","1101"],
["0110","0111","1001","1010","1100"],["0110","0111","1010","1100","1110"],
["0110","1000","1001","1010","1100"],["0111","1001","1010","1011","1100"],
["0111","1001","1011","1100","1101"],["0111","1010","1011","1100","1110"],
["0111","1011","1100","1101","1110"],["0111","1011","1101","1110","1111"]]

B_BITS=[
["0000","0001","0010","0100","1000"],["0001","0010","0011","0100","1000"],
["0001","0011","0100","0101","1000"],["0001","0011","0101","1000","1001"],
["0010","0011","0100","0110","1000"],["0010","0011","0110","1000","1010"],
["0011","0100","0101","0110","1000"],["0011","0101","0110","0111","1000"],
["0011","0101","0111","1000","1001"],["0011","0110","0111","1000","1010"],
["0011","0111","1000","1001","1010"],["0011","0111","1001","1010","1011"],
["0100","0101","0110","1000","1100"],["0101","0110","0111","1000","1100"],
["0101","0111","1000","1001","1100"],["0101","0111","1001","1100","1101"],
["0110","0111","1000","1010","1100"],["0110","0111","1010","1100","1110"],
["0111","1000","1001","1010","1100"],["0111","1001","1010","1011","1100"],
["0111","1001","1011","1100","1101"],["0111","1010","1011","1100","1110"],
["0111","1011","1100","1101","1110"],["0111","1011","1101","1110","1111"]]

def parse(rows):
    return [[IDX[tuple(map(int,s))] for s in row] for row in rows]
TA,TB=parse(A_BITS),parse(B_BITS)

def det3(M):
    a,b,c=M[0]; d,e,f=M[1]; g,h,i=M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def replace_col(M,col,rhs):
    return [[rhs[r] if j==col else M[r][j] for j in range(3)] for r in range(3)]

def solve_vertex(triple):
    M=[list(q[1:]) for q in triple]
    rhs=[-q[0] for q in triple]
    D=det3(M)
    if D==0: return None
    return tuple(Fraction(det3(replace_col(M,j,rhs)),D) for j in range(3))

def normineq(q):
    q=tuple(int(x) for x in q)
    if all(x==0 for x in q): return None
    g=0
    for x in q: g=math.gcd(g,abs(x))
    if g>1: q=tuple(x//g for x in q)
    return q

vertex_cache={}
def vertices(ineqs):
    key=tuple(sorted(set(q for q in (normineq(x) for x in ineqs) if q is not None)))
    if key in vertex_cache: return vertex_cache[key]
    vs=set()
    for tri in combinations(key,3):
        x=solve_vertex(tri)
        if x is None: continue
        if all(Fraction(q[0])+sum(Fraction(q[j+1])*x[j] for j in range(3))>=0 for q in key):
            vs.add(x)
    vertex_cache[key]=tuple(vs)
    return vertex_cache[key]

def gauss_solve(A,b):
    n=len(b)
    M=[[Fraction(x) for x in A[i]]+[Fraction(b[i])] for i in range(n)]
    for col in range(n):
        piv=next(r for r in range(col,n) if M[r][col])
        M[col],M[piv]=M[piv],M[col]
        z=M[col][col]; M[col]=[x/z for x in M[col]]
        for r in range(n):
            if r!=col and M[r][col]:
                z=M[r][col]
                M[r]=[M[r][j]-z*M[col][j] for j in range(n+1)]
    return [M[i][-1] for i in range(n)]

def lambdas(T,v):
    cols=[[1]+list(BITS[T[j]]) for j in range(5)]
    A=[[cols[j][i] for j in range(5)] for i in range(5)]
    return gauss_solve(A,[1]+list(BITS[v]))

def diff(i,j):
    return tuple(BITS[i][k]-BITS[j][k] for k in range(4))

# Normalized w1=1. Each tuple is c0+c2*w2+c3*w3+c4*w4 >= 0.
BASE_A=[(1,-1,0,0),(0,1,-1,0),(0,0,1,-1),(0,0,0,1),(-1,1,1,0)]
BASE_B=[(1,-1,0,0),(0,1,-1,0),(0,0,1,-1),(0,0,0,1),(1,-1,-1,0)]

def verify_hinges(cells,base,label):
    cases=0; feasible=0; minval=None
    for ci,T in enumerate(cells):
        for v in range(16):
            if v in T: continue
            lam=lambdas(T,v)
            support=T+[v]
            for j in support: # every knot of residual as a function of threshold t
                ds=[diff(k,j) for k in support]
                nz=[r for r,d in enumerate(ds) if any(d)]
                for signs in product([0,1], repeat=len(nz)):
                    signmap={nz[a]:signs[a] for a in range(len(nz))}
                    ineqs=list(base)
                    for r in nz:
                        d=ds[r]
                        ineqs.append(d if signmap[r] else tuple(-x for x in d))
                    vs=vertices(ineqs)
                    cases += 1
                    if not vs: continue
                    feasible += 1
                    rc=[Fraction(0) for _ in range(4)]
                    for r,k in enumerate(support):
                        if r not in signmap or not signmap[r]: continue
                        coeff=Fraction(1) if k==v else -lam[T.index(k)]
                        for h in range(4): rc[h]+=coeff*Fraction(ds[r][h])
                    for x in vs:
                        val=rc[0]+sum(rc[h+1]*x[h] for h in range(3))
                        minval=val if minval is None or val<minval else minval
                        assert val>=0, (label,ci,T,v,j,signs,rc,x,val)
    return cases,feasible,minval

def det_fraction(M):
    n=len(M); A=[[Fraction(x) for x in row] for row in M]; out=Fraction(1)
    for c in range(n):
        piv=next((r for r in range(c,n) if A[r][c]),None)
        if piv is None: return Fraction(0)
        if piv!=c: A[c],A[piv]=A[piv],A[c]; out=-out
        z=A[c][c]; out*=z
        for j in range(c,n): A[c][j]/=z
        for r in range(c+1,n):
            z=A[r][c]
            if z:
                for j in range(c,n): A[r][j]-=z*A[c][j]
    return out

def affine_alpha(T,vals):
    M=[[1]+list(BITS[i]) for i in T]
    return gauss_solve(M,[vals[i] for i in T])

def verify_reference_triangulation(cells,wref,label):
    s=[sum(wref[k]*BITS[i][k] for k in range(4)) for i in range(16)]
    q=[x*x for x in s]
    sumdet=0; minout=None
    for T in cells:
        M=[[1]+list(BITS[i]) for i in T]
        d=abs(det_fraction(M)); assert d==1,(label,"nonunimodular",T,d)
        sumdet += int(d)
        alpha=affine_alpha(T,q)
        tight=[]
        for v in range(16):
            lv=alpha[0]+sum(alpha[k+1]*BITS[v][k] for k in range(4))
            r=Fraction(q[v])-lv
            assert r>=0,(label,"not-lower",T,v,r)
            if r==0: tight.append(v)
            elif v not in T: minout=r if minout is None or r<minout else minout
        assert set(tight)==set(T),(label,"extra-tight",T,tight)
    assert sumdet==24
    return sumdet,Fraction(sumdet,math.factorial(4)),minout

def main():
    import sys
    mode=(sys.argv[1].upper() if len(sys.argv)>1 else "ALL")
    t0=time.time()
    if mode in ("A","ALL"):
        ta=verify_reference_triangulation(TA,(4,3,2,1),"A")
        print("REFERENCE_TRIANGULATION_A_PASS",ta)
        a=verify_hinges(TA,BASE_A,"A")
        print("BALANCED_CONE_HINGES_PASS", "cases",a[0],"feasible_sign_cells",a[1],"min_residual",a[2])
        print("A_EXACT_PASS")
    if mode in ("B","ALL"):
        vertex_cache.clear()
        tb=verify_reference_triangulation(TB,(8,4,2,1),"B")
        print("REFERENCE_TRIANGULATION_B_PASS",tb)
        b=verify_hinges(TB,BASE_B,"B")
        print("DOMINANT_CONE_HINGES_PASS", "cases",b[0],"feasible_sign_cells",b[1],"min_residual",b[2])
        print("B_EXACT_PASS")
    print("VERTEX_CACHE_SIZE",len(vertex_cache))
    print("ELAPSED_SECONDS",round(time.time()-t0,3))
    print("ALL_EXACT_CHECKS_PASS")
if __name__=="__main__": main()
