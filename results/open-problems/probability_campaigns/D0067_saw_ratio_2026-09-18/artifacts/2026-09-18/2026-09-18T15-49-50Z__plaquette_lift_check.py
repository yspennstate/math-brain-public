#!/usr/bin/env python3
from collections import defaultdict

DIRS=((1,0),(-1,0),(0,1),(0,-1))

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def R(v): return (-v[1],v[0])

def gen_saws(n):
    walk=[(0,0)]
    seen={(0,0)}
    out=[]
    def rec():
        if len(walk)==n+1:
            out.append(tuple(walk))
            return
        z=walk[-1]
        for d in DIRS:
            w=add(z,d)
            if w not in seen:
                seen.add(w); walk.append(w)
                rec()
                walk.pop(); seen.remove(w)
    rec()
    return out

def local_clear(walk,c,M):
    try:
        i=walk.index(c)
    except ValueError:
        return True
    return len(walk)-1-i > M

def late_extra_count(walk,M):
    N=len(walk)-1
    if N==0: return 0
    z,prev=walk[-1],walk[-2]
    idx={v:i for i,v in enumerate(walk)}
    ans=0
    for d in DIRS:
        c=add(z,d)
        if c==prev:
            continue
        if c in idx and N-idx[c] > M:
            ans+=1
    return ans

def source_counts(saws,n,M):
    A=G=0
    late=0
    for w in saws[n]:
        late += late_extra_count(w,M)
        x,y=w[-2],w[-1]
        e=sub(y,x); s=R(e)
        mid=add(x,s); z=add(y,s)
        prefix=w[:-1]
        if local_clear(prefix,mid,M) and local_clear(w,z,M):
            A+=1
        if mid not in prefix and z not in prefix:
            G+=1
    return A,G,late

def target_counts(saws,N,M):
    O=G=0
    late=0
    for w in saws[N]:
        late += late_extra_count(w,M)
        if N<2:
            continue
        x,mid,z=w[-3],w[-2],w[-1]
        s=sub(mid,x); e=sub(z,mid)
        if s != R(e):
            continue
        opposite=add(x,e)
        if local_clear(w,opposite,M):
            O+=1
        if opposite not in w:
            G+=1
    return O,G,late

def main():
    MAXN=10
    saws={n:gen_saws(n) for n in range(MAXN+1)}
    expected={0:1,1:4,2:12,3:36,4:100,5:284,6:780,7:2172,8:5916,9:16268,10:44100}
    assert {n:len(saws[n]) for n in expected} == expected
    print("square-lattice SAW counts verified through n=10:", expected)
    print("columns: n M A_nM O_(n+1)M G_n G_target abs(A-O) blocker_bound")
    for n in range(2,10):
        for M in range(1,6):
            A,G,Ln=source_counts(saws,n,M)
            O,Gt,Lnp1=target_counts(saws,n+1,M)
            Lnm1=sum(late_extra_count(w,M) for w in saws[n-1])
            bound=Ln+Lnm1+Lnp1
            assert G==Gt
            assert abs(A-O)<=bound
            print(n,M,A,O,G,Gt,abs(A-O),bound)
    print("ALL_EXACT_CHECKS_PASS")

if __name__=="__main__":
    main()
