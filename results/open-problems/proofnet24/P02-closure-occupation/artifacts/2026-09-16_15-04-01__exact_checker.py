from fractions import Fraction as F
from itertools import combinations

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def transpose(A):
    return [list(row) for row in zip(*A)]

def matadd(A,B,sa=F(1),sb=F(1)):
    return [[sa*A[i][j]+sb*B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def matvec(A,x):
    return [sum(A[i][k]*x[k] for k in range(len(x))) for i in range(len(A))]

def det(A):
    A=[row[:] for row in A]
    n=len(A)
    d=F(1)
    for c in range(n):
        piv=next((r for r in range(c,n) if A[r][c]),None)
        if piv is None: return F(0)
        if piv!=c:
            A[c],A[piv]=A[piv],A[c]
            d=-d
        p=A[c][c]
        d*=p
        for r in range(c+1,n):
            if A[r][c]:
                q=A[r][c]/p
                for j in range(c+1,n):
                    A[r][j]-=q*A[c][j]
    return d

def inv(A):
    n=len(A)
    B=[A[i][:]+eye(n)[i][:] for i in range(n)]
    for c in range(n):
        piv=next((r for r in range(c,n) if B[r][c]),None)
        assert piv is not None
        B[c],B[piv]=B[piv],B[c]
        p=B[c][c]
        B[c]=[x/p for x in B[c]]
        for r in range(n):
            if r!=c and B[r][c]:
                q=B[r][c]
                B[r]=[B[r][j]-q*B[c][j] for j in range(2*n)]
    return [row[n:] for row in B]

def solve(A,b):
    return matvec(inv(A),b)

def submat(A,rows,cols):
    return [[A[i][j] for j in cols] for i in rows]

def stationary_check(P,pi):
    n=len(P)
    assert sum(pi)==1
    for j in range(n):
        assert sum(pi[i]*P[i][j] for i in range(n))==pi[j]

def fundamental(P,pi):
    n=len(P)
    Pi=[[pi[j] for j in range(n)] for _ in range(n)]
    Z=matadd(inv(matadd(matadd(eye(n),P,sb=F(-1)),Pi)),Pi,sb=F(-1))
    # Group-inverse identities; valid also for periodic chains.
    ImP=matadd(eye(n),P,sb=F(-1))
    assert matmul(ImP,Z)==matadd(eye(n),Pi,sb=F(-1))
    assert matmul(Z,ImP)==matadd(eye(n),Pi,sb=F(-1))
    assert all(sum(row)==0 for row in Z)
    for j in range(n):
        assert sum(pi[i]*Z[i][j] for i in range(n))==0
    return Z

def boundary_matrix(Z,pi,A):
    # M_A = [[Z_A^T,-pi_A],[1^T,0]]
    m=len(A)
    M=[]
    for rb in range(m):
        b=A[rb]
        M.append([Z[a][b] for a in A]+[-pi[b]])
    M.append([F(1)]*m+[F(0)])
    return M

def killed_data(P,A):
    n=len(P)
    A=tuple(A); B=tuple(i for i in range(n) if i not in A)
    posB={b:k for k,b in enumerate(B)}
    if not B:
        return {},{},{}
    Q=submat(P,B,B)
    N=inv(matadd(eye(len(B)),Q,sb=F(-1)))
    R=submat(P,B,A)
    Om=matmul(N,R)
    G={}
    t={}
    om={}
    for ii,i in enumerate(B):
        t[i]=sum(N[ii])
        om[i]=[Om[ii][a] for a in range(len(A))]
        G[i]={j:(N[ii][posB[j]] if j in posB else F(0)) for j in range(n)}
    for i in A:
        t[i]=F(0)
        om[i]=[F(int(i==a)) for a in A]
        G[i]={j:F(0) for j in range(n)}
    return G,t,om

def bordered_green_det(Z,pi,A,i,j):
    M=boundary_matrix(Z,pi,A)
    b=[Z[i][a] for a in A]+[F(1)]
    r=[Z[a][j] for a in A]+[-pi[j]]
    N=[M[k][:]+[b[k]] for k in range(len(M))]
    N.append(r+[Z[i][j]])
    return det(N)/det(M)

def H_from_Z(Z,pi,i,j):
    if i==j: return F(0)
    return (Z[j][j]-Z[i][j])/pi[j]

def run_chain(name,P,pi):
    stationary_check(P,pi)
    n=len(P)
    Z=fundamental(P,pi)
    port_checks=0
    sys_checks=0
    for m in range(1,n):
        for A in combinations(range(n),m):
            G,t,om=killed_data(P,A)
            M=boundary_matrix(Z,pi,A)
            Delta=det(M)
            assert Delta != 0, (name,A,"singular M")
            for i in range(n):
                b=[Z[i][a] for a in A]+[F(1)]
                sol=solve(M,b)
                assert sol[:-1]==om[i], (name,A,i,"omega",sol[:-1],om[i])
                assert sol[-1]==t[i], (name,A,i,"t",sol[-1],t[i])
                sys_checks+=1
                for j in range(n):
                    gd=bordered_green_det(Z,pi,A,i,j)
                    assert gd==G[i][j], (name,A,i,j,gd,G[i][j])
                    port_checks+=1

    source_checks=0
    # 2.5,2.6: return-cycle occupation for each i,j
    Gsingle={}
    tsingle={}
    for i in range(n):
        G,t,_=killed_data(P,(i,))
        Gsingle[i]=G; tsingle[i]=t
        gp=[]
        for j in range(n):
            val=F(int(i==j))+sum(P[i][x]*G[x][j] for x in range(n))
            assert val==pi[j]/pi[i], (name,"2.6",i,j,val,pi[j]/pi[i])
            gp.append(val); source_checks+=1
        assert sum(gp)==F(1)/pi[i]
        source_checks+=1 # 2.5

    # all hitting times H(i,j) via singleton absorption and source formulas
    H=[[F(0)]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                H[i][j]=tsingle[j][i]
                assert H[i][j]==H_from_Z(Z,pi,i,j), (name,"2.12",i,j)
                source_checks+=1

    # 2.7, 2.8
    for i in range(n):
        for j in range(n):
            if i==j: continue
            actual=Gsingle[i][j][j]
            rhs=pi[j]*(H[j][i]+H[i][j])
            assert actual==rhs, (name,"2.7",i,j,actual,rhs)
            source_checks+=1
            # probability i -> hit j before return i from first step/harmonic measure
            Gij,tij,omij=killed_data(P,(i,j))
            # starting after one step:
            prob=sum(P[i][x]*(F(1) if x==j else (F(0) if x==i else omij[x][1])) for x in range(n))
            rhs=F(1)/(pi[i]*(H[i][j]+H[j][i]))
            assert prob==rhs, (name,"2.8",i,j,prob,rhs)
            source_checks+=1

    # 2.9,2.10
    for l in range(n):
        G=Gsingle[l]
        for i in range(n):
            for j in range(n):
                if j==l:
                    continue
                rhs=pi[j]*(H[i][l]+H[l][j]-H[i][j])
                assert G[i][j]==rhs, (name,"2.9",i,j,l,G[i][j],rhs)
                source_checks+=1
                if i!=j and i!=l:
                    _,_,omjl=killed_data(P,(j,l))
                    # killed_data preserves the explicit boundary tuple (j,l).
                    prob=omjl[i][0]
                    rhsprob=(H[i][l]+H[l][j]-H[i][j])/(H[j][l]+H[l][j])
                    assert prob==rhsprob, (name,"2.10",i,j,l,prob,rhsprob)
                    source_checks+=1

    # 2.11
    for i in range(n):
        lhs=pi[i]*sum(pi[x]*H[x][i] for x in range(n))
        assert lhs==Z[i][i], (name,"2.11",i,lhs,Z[i][i])
        source_checks+=1

    # 2.13 and 2.14
    traceZ=sum(Z[j][j] for j in range(n))
    vals=[]
    for i in range(n):
        val=sum(pi[j]*H[i][j] for j in range(n))
        assert val==traceZ, (name,"2.13",i,val,traceZ)
        vals.append(val); source_checks+=1
    assert all(v==vals[0] for v in vals) # 2.14
    source_checks+=1

    # 2.15
    for i in range(n):
        for j in range(n):
            lhs=sum(pi[x]*Gsingle[i][x][j] for x in range(n))
            rhs=(pi[j]/pi[i])*Z[i][i]-Z[i][j]
            assert lhs==rhs, (name,"2.15",i,j,lhs,rhs)
            source_checks+=1

    return Z,port_checks,sys_checks,source_checks

def reversible_from_conductance(C):
    n=len(C)
    d=[sum(C[i]) for i in range(n)]
    tot=sum(d)
    P=[[C[i][j]/d[i] for j in range(n)] for i in range(n)]
    pi=[d[i]/tot for i in range(n)]
    return P,pi

chains=[]
# Exact reversible lazy path.
P1=[[F(1,2),F(1,2),F(0)],
    [F(1,4),F(1,2),F(1,4)],
    [F(0),F(1,2),F(1,2)]]
pi1=[F(1,4),F(1,2),F(1,4)]
chains.append(("lazy_path_3",P1,pi1))

# Connected weighted reversible chain with nonuniform stationary law.
C2=[[F(1),F(2),F(0),F(1)],
    [F(2),F(1),F(1),F(0)],
    [F(0),F(1),F(2),F(3)],
    [F(1),F(0),F(3),F(1)]]
P2,pi2=reversible_from_conductance(C2)
chains.append(("weighted_4",P2,pi2))

# Periodic 4-cycle, testing the group-inverse/Cesaro convention.
C3=[[F(0),F(1),F(0),F(1)],
    [F(1),F(0),F(1),F(0)],
    [F(0),F(1),F(0),F(1)],
    [F(1),F(0),F(1),F(0)]]
P3,pi3=reversible_from_conductance(C3)
chains.append(("periodic_cycle_4",P3,pi3))

# Periodic nonreversible directed 3-cycle: verifies the full Chapter 2 general-chain scope.
P4=[[F(0),F(1),F(0)],
    [F(0),F(0),F(1)],
    [F(1),F(0),F(0)]]
pi4=[F(1,3),F(1,3),F(1,3)]
chains.append(("directed_cycle_3_nonreversible",P4,pi4))

totp=tots=toti=0
Z1=None
for name,P,pi in chains:
    Z,p,s,i=run_chain(name,P,pi)
    if name=="lazy_path_3": Z1=Z
    totp+=p; tots+=s; toti+=i
    print(f"{name}: PORT determinant cases={p}, bordered-system cases={s}, source-identity exact checks={i}: PASS")

# Frozen exact falsifications on lazy_path_3.
P,pi=P1,pi1
A=(0,1)
G,t,om=killed_data(P,A)
EA=sum(pi[x]*t[x] for x in range(3))
piA=sum(pi[a] for a in A)
ZAA=sum(pi[x]/piA * sum(Z1[x][y] for y in A) for x in A)
naive_subset=ZAA/piA
assert EA==F(1,2)
assert naive_subset==F(5,9)
assert EA!=naive_subset

i=j=2
actual=G[i][j]
# naive boundary replacement omega -> pi(.|A):
H=[[F(0)]*3 for _ in range(3)]
for x in range(3):
    for y in range(3):
        H[x][y]=H_from_Z(Z1,pi,x,y)
E_boundary_Hj=sum((pi[a]/piA)*H[a][j] for a in A)
naive=pi[j]*(t[i]+E_boundary_Hj-H[i][j])
assert actual==F(2)
assert naive==F(13,6)
assert actual!=naive

print(f"counterexample subset extension: E_pi T_A={EA}, Z_AA/pi(A)={naive_subset}: EXACT FAIL as intended")
print(f"counterexample stationary-boundary substitution: actual G_A(2,2)={actual}, naive={naive}: EXACT FAIL as intended")
print(f"TOTAL: PORT determinant cases={totp}; bordered-system cases={tots}; source-identity exact checks={toti}; ALL PASS")
