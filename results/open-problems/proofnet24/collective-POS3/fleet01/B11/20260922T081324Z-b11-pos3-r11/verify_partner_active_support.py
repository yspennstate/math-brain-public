from collections import Counter

N = 8
covers0 = [(1,2),(1,6),(2,0),(2,7),(3,0),(3,4),(4,7),(5,7),(6,0),(6,4),(6,5)]
R = [[False]*N for _ in range(N)]
for u,v in covers0:
    R[u][v] = True
for k in range(N):
    for i in range(N):
        if R[i][k]:
            for j in range(N):
                if R[k][j]:
                    R[i][j] = True

def inc(u,v):
    return u != v and not R[u][v] and not R[v][u]

def cover(u,v):
    return R[u][v] and not any(R[u][z] and R[z][v] for z in range(N) if z not in (u,v))

def linexts():
    pred = [{u for u in range(N) if R[u][v]} for v in range(N)]
    out = []
    def rec(pref, rem):
        if not rem:
            out.append(tuple(pref)); return
        for v in sorted(rem):
            if pred[v].isdisjoint(rem):
                rec(pref+[v], rem-{v})
    rec([], set(range(N)))
    return out

def valid(seq):
    p = {v:i for i,v in enumerate(seq)}
    return all(p[u] < p[v] for u in range(N) for v in range(N) if R[u][v])

def swap(seq,u,v):
    q=list(seq); i=q.index(u); j=q.index(v); q[i],q[j]=q[j],q[i]
    return tuple(q)

L = linexts(); E=len(L)
x,y,a = 2,0,5
F1=[r for r in range(N) if r not in (x,y,a) and cover(x,r) and inc(r,a) and r != y]
F2=[r for r in range(N) if r not in (x,y,a) and cover(r,a) and inc(r,x)]
F3=[r for r in range(N) if r not in (x,y,a) and cover(a,r) and inc(r,y)]
F4=[r for r in range(N) if r not in (x,y,a) and cover(r,y) and inc(r,a) and r != x]
A=H=C=0; BL=[]; BR=[]
for e in L:
    p={v:i for i,v in enumerate(e)}
    if p[a] < p[x] < p[y]: A += 1
    elif p[x] < p[a] < p[y]:
        H += 1
        if not valid(swap(e,x,a)): BL.append(e)
        if not valid(swap(e,a,y)): BR.append(e)
    elif p[x] < p[y] < p[a]: C += 1
    else: raise AssertionError(e)
lam=Counter()
for e in BL:
    p={v:i for i,v in enumerate(e)}
    cand=[r for r in F1+F2 if p[x] < p[r] < p[a]]
    lam[min(cand,key=lambda r:p[r])] += 1
rho=Counter()
for e in BR:
    p={v:i for i,v in enumerate(e)}
    cand=[r for r in F3+F4 if p[a] < p[r] < p[y]]
    rho[min(cand,key=lambda r:p[r])] += 1
num36=sum(e.index(3)<e.index(6) for e in L)
print('extensions',E)
print('partition',A,H,C)
print('families',F1,F2,F3,F4)
print('bad_left',len(BL),'lambda',dict(sorted(lam.items())))
print('bad_right',len(BR),'rho',dict(sorted(rho.items())))
print('cross_3_before_6',num36,'/',E)
assert (E,A,H,C)==(108,29,52,27)
assert F1==[] and F2==[6] and F3==[7] and F4==[3]
assert len(BL)==23 and lam==Counter({6:23})
assert len(BR)==25 and rho==Counter({7:19,3:6})
assert num36==60
print('POS3_ACTIVE_SUPPORT_PARTNER_CHECK_PASS')
