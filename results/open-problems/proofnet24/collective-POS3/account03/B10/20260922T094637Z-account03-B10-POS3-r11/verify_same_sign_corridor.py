from itertools import product


def closure(n, mask):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    r=[[False]*n for _ in range(n)]
    for k,(i,j) in enumerate(pairs):
        if (mask>>k)&1:
            r[i][j]=True
    for k in range(n):
        for i in range(n):
            if r[i][k]:
                for j in range(n):
                    if r[k][j]:
                        r[i][j]=True
    return tuple(tuple(x) for x in r)


def extensions(r):
    n=len(r)
    pred=[sum(1<<i for i in range(n) if r[i][j]) for j in range(n)]
    full=(1<<n)-1
    ans=[]
    def go(mask,w):
        if mask==full:
            ans.append(tuple(w)); return
        for v in range(n):
            if not (mask>>v)&1 and not (pred[v]&~mask):
                go(mask|(1<<v),w+[v])
    go(0,[])
    return ans


def cmp(r,x,y):
    if r[x][y]: return -1
    if r[y][x]: return 1
    return 0


def dtype(r,a,b,z):
    ca,cb=cmp(r,a,z),cmp(r,b,z)
    if ca==-1 and cb==0: return 'U+'
    if ca==0 and cb==1: return 'L+'
    if cb==-1 and ca==0: return 'U-'
    if cb==0 and ca==1: return 'L-'
    return None


total_cases=0
for n in range(2,7):
    m=n*(n-1)//2
    posets={closure(n,mask) for mask in range(1<<m)}
    cases=0
    for r in posets:
        ex=extensions(r)
        positions=[{v:i for i,v in enumerate(w)} for w in ex]
        for a in range(n):
            for b in range(a+1,n):
                if cmp(r,a,b)!=0: continue
                D={z:dtype(r,a,b,z) for z in range(n) if z not in (a,b)}
                D={z:t for z,t in D.items() if t is not None}
                if not D or not all(t.endswith('+') for t in D.values()):
                    continue
                L=[z for z,t in D.items() if t=='L+']
                U=[z for z,t in D.items() if t=='U+']
                n_ba=sum(P[b]<P[a] for P in positions)
                n_safe=sum(
                    all(P[l]<P[a] for l in L) and
                    all(P[b]<P[u] for u in U)
                    for P in positions
                )
                assert n_safe==2*n_ba, (n,a,b,D,n_safe,n_ba)
                cases+=1
    total_cases+=cases
    print(f'n={n} posets={len(posets)} all_positive_identity_cases={cases}')
print(f'total_identity_cases={total_cases}')
print('POS3_SAME_SIGN_CORRIDOR_CHECK_PASS')
