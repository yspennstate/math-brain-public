#!/usr/bin/env python3
"""Exact audit of the B20 adjacent-pair path-resolution formulas on all labelled graphs n=3..5."""
from itertools import combinations


def forest(n,E,S):
    p=list(range(n))
    def f(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    for i in S:
        u,v=E[i]
        if u==v: return False
        ru,rv=f(u),f(v)
        if ru==rv: return False
        p[rv]=ru
    return True


def sig(n,E):
    out=dict(d=0,a=0,b=0,c=0,t=0)
    for m in range(1<<len(E)):
        S=[i for i in range(len(E)) if m>>i&1]
        if not forest(n,E,S): continue
        p=list(range(n))
        def f(x):
            while p[x]!=x:
                p[x]=p[p[x]]; x=p[x]
            return x
        for i in S:
            u,v=E[i]; ru,rv=f(u),f(v); p[rv]=ru
        r=[f(0),f(1),f(2)]
        if r[0]==r[1]==r[2]: out['t']+=1
        elif r[0]==r[1]: out['a']+=1
        elif r[0]==r[2]: out['b']+=1
        elif r[1]==r[2]: out['c']+=1
        else: out['d']+=1
    return out


def paths(n,E,s,t):
    A=[[] for _ in range(n)]
    for i,(u,v) in enumerate(E):
        A[u].append((v,i)); A[v].append((u,i))
    ans=[]
    def rec(u,seen,P):
        if u==t:
            ans.append(tuple(P)); return
        for v,i in A[u]:
            if v in seen: continue
            seen.add(v); P.append(i); rec(v,seen,P); P.pop(); seen.remove(v)
    rec(s,{s},[])
    return ans


def contract(n,E,P):
    p=list(range(n))
    def f(x):
        if p[x]!=x: p[x]=f(p[x])
        return p[x]
    for i in P:
        u,v=E[i]; ru,rv=f(u),f(v)
        if ru!=rv: p[rv]=ru
    ids={}; mp={}
    for v in range(n):
        r=f(v)
        if r not in ids: ids[r]=len(ids)
        mp[v]=ids[r]
    EE=[(mp[u],mp[v]) for i,(u,v) in enumerate(E) if i not in set(P)]
    return len(ids),EE,mp


def count(n,E,separate=None):
    ans=0
    for m in range(1<<len(E)):
        S=[i for i in range(len(E)) if m>>i&1]
        if not forest(n,E,S): continue
        if separate is not None:
            p=list(range(n))
            def f(x):
                while p[x]!=x:
                    p[x]=p[p[x]]; x=p[x]
                return x
            for i in S:
                u,v=E[i]; ru,rv=f(u),f(v); p[rv]=ru
            if f(separate[0])==f(separate[1]): continue
        ans+=1
    return ans


def decomp(n,E):
    # terminals: a=0, b=1, c=2; paths are b-c paths.
    Q=Aoff=Amid=0
    for P in paths(n,E,1,2):
        V={1}
        for i in P: V.update(E[i])
        nn,EE,mp=contract(n,E,P)
        Z=count(nn,EE)
        if 0 in V:
            Amid+=Z
        else:
            D=count(nn,EE,(mp[0],mp[1]))
            Q+=D
            Aoff+=Z-D
    return Q,Aoff,Amid


def main():
    graphs=0
    for n in range(3,6):
        U=list(combinations(range(n),2))
        for gm in range(1<<len(U)):
            E=[U[i] for i in range(len(U)) if gm>>i&1]
            s=sig(n,E)
            Q,Aoff,Amid=decomp(n,E)
            assert Q==s['c']
            assert Aoff+Amid==s['t']
            graphs+=1
    print('ADJACENT_PATH_RESOLUTION=PASS')
    print('LABELED_GRAPHS_N3_TO_N5=',graphs)
    print('Q_PATH_IDENTITIES=',graphs)
    print('A_PATH_SPLIT_IDENTITIES=',graphs)
    print('TOTAL_EXACT_IDENTITIES=',2*graphs)

if __name__=='__main__': main()
