"""Exact regression for Theorem 5.1 of REPORT.md.

For every naturally labelled finite poset through n=6, compare the sliding
2K+1-window transfer count with direct topological-sort enumeration.  For every
incomparable pair also compare both orientation-event counts.  The proof in the
report is arbitrary-size; this file is only an independent finite regression.
"""


def closure(n, mask):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    a=[[False]*n for _ in range(n)]
    for k,(i,j) in enumerate(pairs):
        if (mask>>k)&1: a[i][j]=True
    for k in range(n):
        for i in range(n):
            if a[i][k]:
                for j in range(n):
                    if a[k][j]: a[i][j]=True
    cm=0
    for k,(i,j) in enumerate(pairs):
        if a[i][j]: cm|=1<<k
    return cm,a


def extensions(n,a):
    pred=[0]*n
    for i in range(n):
        for j in range(n):
            if a[i][j]: pred[j]|=1<<i
    out=[]; full=(1<<n)-1
    def rec(used,s):
        if used==full: out.append(tuple(s)); return
        for v in range(n):
            if not (used>>v)&1 and not (pred[v]&~used):
                rec(used|1<<v,s+[v])
    rec(0,[])
    return out


def transfer_count(n,a,K,event=None):
    pred=[set(i for i in range(n) if a[i][v]) for v in range(n)]
    states={0:1}
    for t in range(n):
        lo=max(0,t-K); hi=min(n-1,t+K); nxt={}
        for mask,c in states.items():
            def used(i):
                if i<lo: return True
                if i>hi: return False
                return bool(mask&(1<<(i-lo)))
            for v in range(lo,hi+1):
                if used(v): continue
                if event is not None:
                    x,y=event
                    if v==y and not used(x): continue
                if any(not used(p) for p in pred[v]): continue
                t2=t+1; lo2=max(0,t2-K); hi2=min(n-1,t2+K)
                if any(not (used(i) or i==v) for i in range(lo,min(lo2,hi+1))):
                    continue
                m2=0
                for i in range(lo2,hi2+1):
                    if used(i) or i==v: m2|=1<<(i-lo2)
                nxt[m2]=nxt.get(m2,0)+c
        states=nxt
    return sum(states.values())


def main():
    total_posets=0; total_extensions=0; total_pair_events=0
    for n in range(2,7):
        m=n*(n-1)//2; cs={}
        for mask in range(1<<m):
            cm,a=closure(n,mask); cs.setdefault(cm,a)
        pe=0; ee=0
        for a in cs.values():
            inc=[sum(1 for j in range(n) if i!=j and not(a[i][j] or a[j][i])) for i in range(n)]
            K=max(inc,default=0)
            ex=extensions(n,a); ee+=len(ex)
            assert transfer_count(n,a,K)==len(ex)
            pos=[]
            for s in ex:
                q=[0]*n
                for r,v in enumerate(s): q[v]=r
                pos.append(q)
            for i in range(n):
                for j in range(i+1,n):
                    if a[i][j] or a[j][i]: continue
                    f=sum(q[i]<q[j] for q in pos)
                    assert transfer_count(n,a,K,(i,j))==f
                    assert transfer_count(n,a,K,(j,i))==len(ex)-f
                    pe+=1
        print(f"n={n} closures={len(cs)} extensions={ee} incomparable_pair_tests={pe}")
        total_posets+=len(cs); total_extensions+=ee; total_pair_events+=pe
    print("POS3_FINITE_MEMORY_TRANSFER_CHECK_PASS")
    print("closures_total",total_posets)
    print("extensions_total",total_extensions)
    print("incomparable_pair_tests_total",total_pair_events)

if __name__=="__main__": main()
