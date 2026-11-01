from itertools import product, combinations
from fractions import Fraction

def det(M):
    A=[list(map(int,r)) for r in M]; n=len(A)
    if n==0:return 1
    sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            rr=next((i for i in range(k+1,n) if A[i][k]),None)
            if rr is None:return 0
            A[k],A[rr]=A[rr],A[k]; sign=-sign
        piv=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*piv-A[i][k]*A[k][j])//prev
        prev=piv
        for i in range(k+1,n):A[i][k]=0
    return sign*A[-1][-1]

def rankmod(rows,p):
    A=[list(r) for r in rows]; r=0
    if not A:return 0
    for c in range(len(A[0])):
        q=next((i for i in range(r,len(A)) if A[i][c]%p),None)
        if q is None:continue
        A[r],A[q]=A[q],A[r]
        iv=pow(A[r][c]%p,-1,p); A[r]=[(x*iv)%p for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]%p:
                f=A[i][c]%p
                A[i]=[(A[i][j]-f*A[r][j])%p for j in range(len(A[0]))]
        r+=1
    return r

# ---- rank 4 obstruction -------------------------------------------------
cube4=[tuple((x>>i)&1 for i in range(4)) for x in range(1,16)]
def valid_counts4(p):
    f=[0]*(1<<15)
    for a in product(range(p),repeat=4):
        if not any(a):continue
        mask=0
        for t,u in enumerate(cube4):
            if sum(ai*ui for ai,ui in zip(a,u))%p in (0,1):mask|=1<<t
        f[mask]+=1
    g=f[:]
    for j in range(15):
        b=1<<j
        for mask in range(1<<15):
            if not mask&b:g[mask]+=g[mask|b]
    return g
for p,m,want in [(7,9,6),(11,9,6),(11,10,5)]:
    g=valid_counts4(p); best=-1; arg=None
    for I in combinations(range(15),m):
        mask=sum(1<<i for i in I)
        if g[mask]>best:best,arg=g[mask],I
    assert best==want and best<m
    print(f'p={p} m={m} max_nonzero_binary_valued_forms={best} witness_U_indices={arg}')

# characteristic stability for every p>=7
ds=set(); maxn=maxd=0; nb=0
for I in combinations(range(15),4):
    B=[cube4[i] for i in I]; D=det(B)
    if D==0:continue
    nb+=1; ds.add(D)
    for b in product((0,1),repeat=4):
        cr=[]
        for j in range(4):
            C=[list(r) for r in B]
            for i in range(4):C[i][j]=b[i]
            cr.append(det(C))
        for u in cube4:
            n=sum(u[j]*cr[j] for j in range(4))
            maxn=max(maxn,abs(n)); maxd=max(maxd,abs(n-D))
assert ds=={-3,-2,-1,1,2,3} and maxn<=5 and maxd<=5
print('dim4_characteristic_stability bases',nb,'detset',sorted(ds),
      'max_abs_num',maxn,'max_abs_num_minus_det',maxd,'PASS')
print('C256a universal conclusion: for every prime p>=7 and m>=9, rank_Fp(A)>=5 for A in G_m')

# sharp rank-5 witnesses at m=9,10
def indep_sets(edges):
    E={tuple(sorted(e)) for e in edges}; out=[]
    for mask in range(1,32):
        if all(not(((mask>>i)&1) and ((mask>>j)&1)) for i,j in E):
            out.append(tuple((mask>>i)&1 for i in range(5)))
    return out
def graph_matrix(edges):
    B=[tuple(1 if i==j else 0 for i in range(5)) for j in range(5)]
    U=B+[tuple(1 if i in e else 0 for i in range(5)) for e in edges]
    F=B+[a for a in indep_sets(edges) if a not in B]
    F=F[:len(U)]
    A=[[sum(u[i]*a[i] for i in range(5)) for a in F] for u in U]
    return A
for m,p,edges in [(9,7,[(0,1),(1,2),(2,3),(3,4)]),
                   (10,11,[(0,1),(1,2),(2,3),(3,4),(4,0)])]:
    A=graph_matrix(edges)
    cols=list(zip(*A))
    assert len(A)==m and all(x in (0,1) for r in A for x in r)
    assert len(set(map(tuple,A)))==m and len(set(cols))==m
    assert all(any(r) for r in A) and all(any(c) for c in cols)
    assert rankmod(A,p)==5
    print(f'construction m={m} p={p} rank=5')

# ---- p=7 rank 5 obstruction at m=12 -----------------------------------
cube5=[tuple((x>>i)&1 for i in range(5)) for x in range(1,32)]
forms5=[a for a in product(range(7),repeat=5) if any(a)]
valid=[]
for u in cube5:
    mask=0
    for j,a in enumerate(forms5):
        if sum(ai*ui for ai,ui in zip(a,u))%7 in (0,1):mask|=1<<j
    valid.append(mask)
nodes=leaves=0
def dfs(start,sel,cand):
    global nodes,leaves
    nodes+=1; need=12-len(sel)
    if 31-start<need or cand.bit_count()<12:return False
    if len(sel)==12:
        leaves+=1
        return rankmod([cube5[i] for i in sel],7)==5
    if rankmod([cube5[i] for i in sel],7)+need<5:return False
    for i in range(start,31-need+1):
        nc=cand&valid[i]
        if nc.bit_count()<12:continue
        sel.append(i)
        if dfs(i+1,sel,nc):return True
        sel.pop()
    return False
ex=dfs(0,[],(1<<len(forms5))-1)
assert not ex
print('p7_rank5_m12_exhaustive exists',ex,'nodes',nodes,'terminal_rank_checks',leaves,'PASS')
print('C256b conclusion: for p=7 and every m>=12, rank_F7(A)>=6 for A in G_m')

# explicit p=7 rank-5 m=11 witness, showing the threshold is sharp
U=[(0,0,0,0,1),(0,0,1,1,1),(0,1,0,1,0),(0,1,0,1,1),(0,1,1,1,0),
   (0,1,1,1,1),(1,0,1,0,0),(1,0,1,0,1),(1,1,0,0,0),(1,1,1,1,0),(1,1,1,1,1)]
F=[(0,0,0,0,1),(0,0,0,1,0),(0,0,1,0,0),(0,1,0,0,0),(0,1,0,6,1),
   (0,1,1,6,0),(1,0,0,0,0),(1,0,6,1,0),(1,6,0,1,0),(1,6,6,2,0),(6,1,1,6,0)]
A=[[sum(u[j]*a[j] for j in range(5))%7 for a in F] for u in U]
cols=list(zip(*A))
assert all(x in (0,1) for r in A for x in r)
assert len(set(map(tuple,A)))==11 and len(set(cols))==11 and rankmod(A,7)==5
print('p7_rank5_m11_explicit_witness PASS')

# transfer the m=12 obstruction to every prime >=31
md=0
for I in combinations(range(31),5):md=max(md,abs(det([cube5[i] for i in I])))
assert md==5
print('max_abs_det_5x5_boolean_distinct_nonzero',md,'PASS')
print('C256c conclusion: for every prime p>=31 and m>=12, rank_Fp(A)>=6 for A in G_m')

# ---- metric update using run18 exact M1 and certified M2 lower bounds ----
cases=[
(9,7,651685823418402269683200,2942127020232812160000,
 3564857875550413515432975,12917332537615113519104),
(10,11,325043331888785398807391827200,807305539038902680414176000,
 446298905163058911334081193175,849874851189084309818441728)]
for m,p,M1,M2,on,od in cases:
    dmax=m-5
    c=Fraction(p*(p*p-1),p**dmax-1)
    scale=Fraction(2**(m+1),2**(m*m))
    new=scale*(M1-c*M2); old=Fraction(on,od)
    assert new<old
    print(f'm={m} p={p} dmax={dmax} c={c}')
    print('new_r=',new,'decimal=',float(new))
    print('strict_improvement=',old-new,'decimal=',float(old-new))
print('SELF-CHECK PASS')
