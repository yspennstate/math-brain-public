#!/usr/bin/env python3
from itertools import combinations
from collections import Counter


def norm(e): return tuple(sorted(e))


def comps(n, edges, mask):
    p=list(range(n)); r=[0]*n
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    for i,(a,b) in enumerate(edges):
        if not ((mask>>i)&1): continue
        a,b=find(a),find(b)
        if a==b: return None
        if r[a]<r[b]: a,b=b,a
        p[b]=a
        if r[a]==r[b]: r[a]+=1
    return [find(i) for i in range(n)]


def fixed_R(n,e,f):
    e,f=norm(e),norm(f)
    H=[g for g in combinations(range(n),2) if g not in (e,f)]
    N=1<<len(H)
    R=bytearray(N); root=bytearray(N)
    a,b=e; c,d=f
    for m in range(N):
        C=comps(n,H,m)
        if C is None: continue
        ra,rb,rc,rd=C[a],C[b],C[c],C[d]
        if ra!=rb and rc!=rd and {ra,rb}=={rc,rd}: R[m]=1
    for m in range(N):
        if not R[m]: continue
        x=m
        while x:
            bit=x&-x
            if R[m^bit]: break
            x-=bit
        else:
            root[m]=1
    cnt=list(R)
    for i in range(len(H)):
        bit=1<<i
        for m in range(N):
            if m&bit: cnt[m]+=cnt[m^bit]
    return H,R,root,cnt


def bit_edge(H,b): return H[b.bit_length()-1]
def edges_of(H,m): return {H[i] for i in range(len(H)) if (m>>i)&1}


def partition_for(M,rlist,roots):
    rs=[a for a in rlist if not(a&~M)]
    ro=[p for p in roots if not(p&~M)]
    fib={p:[A for A in rs if not(p&~A)] for p in ro}
    return tuple(sorted((len(v) for v in fib.values()),reverse=True)),rs,ro,fib


def star_info(H,P,F):
    atoms=[]
    for A in F:
        d=A^P
        if d and not(d&(d-1)): atoms.append(d)
    if len(F)!=4 or len(atoms)!=3: return None
    E=[bit_edge(H,b) for b in atoms]
    common=set(E[0])&set(E[1])&set(E[2])
    if len(common)!=1: return None
    w=next(iter(common)); ats=[]
    for a,b in E: ats.append(b if a==w else a)
    return w,tuple(sorted(ats))


def same_component_pair(n,H,P,A):
    C=comps(n,H,P)
    pairs=[]
    for a,b in combinations(A,2):
        if C[a]==C[b]: pairs.append(frozenset((a,b)))
    return pairs,C


def cell_counts(n, full_edges, e, f):
    E=list(map(norm,full_edges)); e=norm(e); f=norm(f)
    ie=E.index(e); jf=E.index(f)
    A=B=C=D=0
    for m in range(1<<len(E)):
        if comps(n,E,m) is None: continue
        be=(m>>ie)&1; bf=(m>>jf)&1
        if be and bf: D+=1
        elif be: B+=1
        elif bf: C+=1
        else: A+=1
    return A,B,C,D,B*C-A*D


def scan_case(n,e,f):
    H,R,root,cnt=fixed_R(n,e,f)
    rlist=[m for m,x in enumerate(R) if x]
    roots=[m for m,x in enumerate(root) if x]
    p10=Counter(); p11=Counter(); regimes=Counter(); failures=[]
    for M,v in enumerate(cnt):
        if v not in (10,11): continue
        part,rs,ro,fib=partition_for(M,rlist,roots)
        if v==11:
            p11[part]+=1
            continue
        p10[part]+=1
        if part!=(4,4,1,1): continue
        L=[p for p in ro if len(fib[p])==4]
        S=[p for p in ro if len(fib[p])==1]
        infos=[star_info(H,p,fib[p]) for p in L]
        if len(L)!=2 or len(S)!=2 or not all(infos):
            failures.append(("bad-stars",M)); continue
        (w,A),(x,B)=infos
        full=edges_of(H,M)|{norm(e),norm(f)}
        if w==x:
            if set(A)!=set(B):
                failures.append(("same-center-different-spokes",M,A,B)); continue
            pp,CP=same_component_pair(n,H,L[0],A)
            pq,CQ=same_component_pair(n,H,L[1],A)
            if len(pp)!=1 or len(pq)!=1:
                failures.append(("same-center-pair-count",M,pp,pq)); continue
            if pp[0]==pq[0]:
                regimes[("same-center","same-pair")]+=1
                pair=set(pp[0]); third=next(a for a in A if a not in pair)
                a0=next(iter(pair)); a1=next(a for a in pair if a!=a0)
                if not (CP[a0]==CP[a1] and CQ[a0]==CQ[a1]):
                    failures.append(("same-pair-label",M))
                if CP[third]==CP[a0] or CQ[third]==CQ[a0]:
                    failures.append(("same-pair-not-diagonal",M,A,pp,pq))
            else:
                regimes[("same-center","distinct-pairs")]+=1
                branch=set()
                for ed in edges_of(H,L[0]^L[1]): branch.update(ed)
                if not set(A)<=branch or len(branch)!=4:
                    failures.append(("distinct-pair-not-branch",M,A,branch,pp,pq))
            continue
        P,Q=L
        CP=edges_of(H,P)|{norm(e),norm(f)}
        CQ=edges_of(H,Q)|{norm(e),norm(f)}
        tA={a for a in A if norm((w,a)) in CQ}
        tB={b for b in B if norm((x,b)) in CP}
        connector=norm((w,x)) in full
        if connector:
            regimes[("distinct","connector",len(tA&tB))]+=1
        else:
            ua=set(A)-tA; ub=set(B)-tB
            regimes[("distinct","no-connector",len(tA&tB))]+=1
            if len(tA&tB)!=1 or len(tA|tB)!=3 or len(ua)!=1 or len(ub)!=1 or ua!=ub:
                failures.append(("no-connector-normal-form",M,tA,tB,ua,ub))
    return p10,p11,regimes,failures


def main():
    k4=list(combinations(range(4),2))
    same_dist=[(0,1),(2,3),(0,2),(0,3),(1,2),(1,3),(0,4),(1,4),(2,4)]
    no_conn=[(0,1),(0,2),(0,3),(0,4),(0,5),(1,4),(1,5),(2,3),(2,5),(3,4)]
    print("bare K4",cell_counts(4,k4,(0,1),(2,3)))
    print("same-center distinct-pair core",cell_counts(5,same_dist,(0,1),(2,3)))
    print("distinct-center no-connector core",cell_counts(6,no_conn,(0,1),(2,3)))
    assert cell_counts(4,k4,(0,1),(2,3))[-1]==6
    assert cell_counts(5,same_dist,(0,1),(2,3))[-1]==124
    assert cell_counts(6,no_conn,(0,1),(2,3))[-1]==280

    cases=[
      ("n6_adj",6,(0,1),(0,2)),
      ("n6_dis",6,(0,1),(2,3)),
      ("n7_adj",7,(0,1),(0,2)),
      ("n7_dis",7,(0,1),(2,3)),
    ]
    for name,n,e,f in cases:
        p10,p11,reg,fail=scan_case(n,e,f)
        print(name,"R10",dict(p10))
        print(name,"4411 regimes",dict(reg),"failures",len(fail))
        print(name,"R11",dict(p11))
        assert not fail, fail[:3]
    print("All tested same-center distinct-pair cases place all three spokes at exact-two branch vertices.")
    print("All tested same-center same-pair cases have the third attachment diagonally opposite in the component-pair square.")
    print("All tested distinct-center/no-connector cases have distinct ear pairs sharing one endpoint and a common fourth-branch third attachment.")
    print("OK")

if __name__=="__main__":
    main()
