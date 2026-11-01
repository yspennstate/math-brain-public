from collections import Counter

SQ = ((1,0),(-1,0),(0,1),(0,-1))
DIAG = ((1,1),(-1,-1))
TRI = SQ + DIAG

def add(a,b):
    return (a[0]+b[0], a[1]+b[1])

def enum_square(n):
    total = 0
    allowed_turns = 0
    path=[(0,0)]
    seen={(0,0)}
    def rec():
        nonlocal total, allowed_turns
        if len(path)==n+1:
            total += 1
            allowed_turns += sum(
                (path[i+2][0]-path[i][0], path[i+2][1]-path[i][1]) in DIAG
                for i in range(n-1)
            )
            return
        p=path[-1]
        for d in SQ:
            q=add(p,d)
            if q not in seen:
                seen.add(q); path.append(q)
                rec()
                path.pop(); seen.remove(q)
    rec()
    return total, allowed_turns

def enum_one_diag(n):
    total=0
    expansion_hist=Counter()
    path=[(0,0)]
    seen={(0,0)}
    def expansion_count():
        idx=None
        for i,(u,v) in enumerate(zip(path,path[1:])):
            dv=(v[0]-u[0],v[1]-u[1])
            if dv in DIAG:
                idx=i; break
        assert idx is not None
        u,v=path[idx],path[idx+1]
        common=[]
        for d in SQ:
            w=add(u,d)
            if abs(w[0]-v[0])+abs(w[1]-v[1])==1:
                common.append(w)
        assert len(common)==2
        return sum(w not in seen for w in common)
    def rec(kdiag):
        nonlocal total
        if len(path)==n+1:
            if kdiag==1:
                total += 1
                expansion_hist[expansion_count()] += 1
            return
        p=path[-1]
        for d in TRI:
            nd=kdiag + (1 if d in DIAG else 0)
            if nd>1: continue
            q=add(p,d)
            if q not in seen:
                seen.add(q); path.append(q)
                rec(nd)
                path.pop(); seen.remove(q)
    rec(0)
    return total, expansion_hist

print('n sigma_n sigma_n+1 T_allowed(n+1) a_n1 B0 B1 B2 weighted_expansion_sum identity')
for n in range(2,9):
    sigma_n,_ = enum_square(n)
    sigma_np1,T = enum_square(n+1)
    a,h = enum_one_diag(n)
    weighted = h[1] + 2*h[2]
    assert a == h[0]+h[1]+h[2]
    assert T == weighted
    assert 2*a-T == 2*h[0]+h[1]
    print(n, sigma_n, sigma_np1, T, a, h[0], h[1], h[2], weighted, 'PASS')
print('ALL_EXACT_CHECKS_PASS')
