from itertools import product

CERTS={
2:[[],[0],[0],[0]],
4:[[0],[0,1],[0,1],[0,2]],
6:[[0,2],[0,1,2],[0,1,3],[0,1,3]],
8:[[0,1,2],[0,1,2,5],[0,1,3,5],[0,1,3,5]],
10:[[0,1,2,3],[0,1,2,5,7],[0,1,3,5,7],[0,1,3,6,7]],
12:[[0,1,2,3,5],[0,1,2,4,7,8],[0,1,2,5,7,9],[0,1,3,4,7,9]],
14:[[0,1,2,3,4,8],[0,1,2,3,5,8,10],[0,1,2,5,6,8,11],[0,1,3,5,7,10,11]],
16:[[0,1,2,3,4,5,9],[0,1,2,3,6,9,11,12],[0,1,2,5,7,9,11,13],[0,1,3,6,7,10,11,14]],
18:[[0,1,2,3,4,5,7,12],[0,1,2,3,5,8,11,12,14],[0,1,2,4,6,9,10,13,14],[0,1,2,5,7,8,11,13,15]],
20:[[0,1,2,3,4,5,6,9,13],[0,1,2,3,5,9,10,13,14,15],[0,1,2,5,7,8,11,13,15,17],[0,1,3,5,8,9,12,14,15,18]],
}

def diff_count(X,t,v):
    S=set(X)
    return sum(1 for x in X if (x+t)%v in S)

def mm(A,B):
    n=len(A); k=len(B); m=len(B[0])
    return [[sum(A[i][r]*B[r][j] for r in range(k)) for j in range(m)] for i in range(n)]
def tr(A): return [list(x) for x in zip(*A)]
def add(A,B): return [[x+y for x,y in zip(r,s)] for r,s in zip(A,B)]
def neg(A): return [[-x for x in r] for r in A]
def block(rows):
    out=[]
    for brow in rows:
        h=len(brow[0])
        for i in range(h):
            rr=[]
            for M in brow: rr.extend(M[i])
            out.append(rr)
    return out

def circulant_sign(v,X):
    X=set(X)
    first=[-1 if j in X else 1 for j in range(v)]
    return [[first[(j-i)%v] for j in range(v)] for i in range(v)]
def Rmat(v): return [[1 if i+j==v-1 else 0 for j in range(v)] for i in range(v)]
def kron_scalar_rows(M,v):
    return [[M[i][j] for j in range(4) for _ in range(v)] for i in range(4)]
def kron_scalar_cols(M,v):
    out=[]
    for i in range(4):
        for _ in range(v): out.append(M[i][:])
    return out

def verify_v(v,sets):
    want=[v//2-1,v//2,v//2,v//2]
    assert [len(X) for X in sets]==want
    for t in range(1,v):
        assert sum(diff_count(X,t,v) for X in sets)==v-2,(v,t)
    A,B,C,D=[circulant_sign(v,X) for X in sets]
    mats=[A,B,C,D]
    Q=[[0]*v for _ in range(v)]
    for M in mats: Q=add(Q,mm(M,tr(M)))
    for i in range(v):
        for j in range(v):
            wantq=4*(v+1)*(i==j)-4
            assert Q[i][j]==wantq,(v,i,j,Q[i][j],wantq)
    sums=[sum(M[0]) for M in mats]
    assert sums==[2,0,0,0],(v,sums)
    R=Rmat(v)
    BR=mm(B,R); CR=mm(C,R); DR=mm(D,R)
    DTR=mm(tr(D),R); CTR=mm(tr(C),R); BTR=mm(tr(B),R)
    G=block([
      [A,BR,CR,DR],
      [neg(BR),A,DTR,neg(CTR)],
      [neg(CR),neg(DTR),A,BTR],
      [neg(DR),CTR,neg(BTR),A],
    ])
    K=[[-1,1,1,-1],[1,-1,1,-1],[1,1,-1,-1],[-1,-1,-1,-1]]
    T=[[-1,-1,-1,1],[-1,-1,1,-1],[-1,1,-1,-1],[1,-1,-1,-1]]
    S=[[1,1,1,-1],[-1,-1,1,-1],[-1,1,-1,-1],[1,-1,-1,-1]]
    I4=[[4*(i==j) for j in range(4)] for i in range(4)]
    assert mm(K,tr(K))==I4
    assert mm(T,tr(T))==I4
    assert mm(S,tr(S))==I4
    assert mm(K,tr(S))==[[-2*T[i][j] for j in range(4)] for i in range(4)]
    topR=kron_scalar_rows(T,v); botL=kron_scalar_cols(S,v)
    top=[K[i]+topR[i] for i in range(4)]
    bottom=[botL[i]+G[i] for i in range(4*v)]
    H=top+bottom
    n=4*(v+1)
    assert len(H)==n and all(len(r)==n for r in H)
    HH=mm(H,tr(H))
    for i in range(n):
        for j in range(n): assert HH[i][j]==n*(i==j),(v,i,j,HH[i][j])
    return n

def main():
    for v in sorted(CERTS):
        n=verify_v(v,CERTS[v])
        print(f'v={v}: BGS difference family and bordered Hadamard order {n} PASS')
    print('ALL EXACT BGS CHECKS PASSED')

if __name__=='__main__': main()

# --- exact universal minimum-defect repair census ---
from itertools import combinations
from collections import defaultdict


def all_masks(v,k):
    for C in combinations(range(v),k):
        m=0
        for i in C:
            m |= 1<<i
        yield m


def rotmask(m,t,v):
    full=(1<<v)-1
    if t==0:
        return m
    return ((m<<t)&full)|(m>>(v-t))


def half_diff_vec(m,v):
    return tuple((m&rotmask(m,t,v)).bit_count() for t in range(1,v//2+1))


def exchange_neighbors(m,v):
    yield m
    ones=[i for i in range(v) if (m>>i)&1]
    zeros=[i for i in range(v) if not ((m>>i)&1)]
    for a in ones:
        for b in zeros:
            yield m^(1<<a)^(1<<b)


def universal_reach(v,k):
    ms=list(all_masks(v,k))
    V={m:half_diff_vec(m,v) for m in ms}
    groups=defaultdict(list)
    for m,x in V.items():
        groups[x].append(m)
    U={}
    for x,L in groups.items():
        common=None
        for m in L:
            reach={V[n] for n in exchange_neighbors(m,v)}
            common=reach if common is None else common & reach
        U[x]=common
    return U


def vector_sumset(A,B):
    return {tuple(a+b for a,b in zip(x,y)) for x in A for y in B}


def verify_minimum_defect_repair(v):
    ks=[v//2-1,v//2,v//2,v//2]
    lam=v-2
    h=v//2
    U=[universal_reach(v,k) for k in ks]
    target=(lam,)*h
    P12=defaultdict(list)
    for x in U[0]:
        for y in U[1]:
            P12[tuple(a+b for a,b in zip(x,y))].append(vector_sumset(U[0][x],U[1][y]))
    P34=defaultdict(list)
    for x in U[2]:
        for y in U[3]:
            P34[tuple(a+b for a,b in zip(x,y))].append(vector_sumset(U[2][x],U[3][y]))
    states=0
    for p in range(h-1):
        for q in range(h-1):
            if p==q:
                continue
            cur=list(target)
            cur[p]+=1
            cur[q]-=1
            cur=tuple(cur)
            for a,RAs in P12.items():
                b=tuple(c-x for c,x in zip(cur,a))
                if b not in P34:
                    continue
                for RA in RAs:
                    for RB in P34[b]:
                        states += 1
                        assert any(tuple(t-z for t,z in zip(target,r)) in RB for r in RA), (v,p,q,a,b)
    return states


def run_repair_census():
    expected={4:0,6:15,8:122,10:1046,12:13569,14:217422}
    for v,want in expected.items():
        got=verify_minimum_defect_repair(v)
        assert got==want,(v,got,want)
        print(f'v={v}: minimum-defect vector states={got}; universal one-round repair PASS')
    print('ALL EXACT BORDERED REPAIR CHECKS PASSED')

if __name__=='__main__':
    run_repair_census()
