#!/usr/bin/env python3
"""Exact unit-weight checks for the B20 three-terminal path/contraction decomposition.

No external packages are used.  Parallel edges created by contraction remain distinct;
loops are automatically forbidden from a forest.
"""
from itertools import combinations


def is_forest(n, edges, chosen):
    p=list(range(n))
    def f(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    for i in chosen:
        u,v=edges[i]
        if u==v: return False
        ru,rv=f(u),f(v)
        if ru==rv: return False
        p[rv]=ru
    return True


def signature(n, edges, terms=(0,1,2)):
    out=dict(d=0,a=0,b=0,c=0,t=0)
    m=len(edges)
    for mask in range(1<<m):
        ch=[i for i in range(m) if mask>>i&1]
        if not is_forest(n,edges,ch): continue
        p=list(range(n))
        def f(x):
            while p[x]!=x:
                p[x]=p[p[x]]; x=p[x]
            return x
        for i in ch:
            u,v=edges[i]; ru,rv=f(u),f(v); p[rv]=ru
        r=[f(x) for x in terms]
        if r[0]==r[1]==r[2]: out['t']+=1
        elif r[0]==r[1]: out['a']+=1
        elif r[0]==r[2]: out['b']+=1
        elif r[1]==r[2]: out['c']+=1
        else: out['d']+=1
    return out


def contract(n,edges,chosen):
    p=list(range(n))
    def f(x):
        if p[x]!=x: p[x]=f(p[x])
        return p[x]
    for i in chosen:
        u,v=edges[i]; ru,rv=f(u),f(v)
        if ru!=rv: p[rv]=ru
    lab={}; mp={}
    for v in range(n):
        r=f(v)
        if r not in lab: lab[r]=len(lab)
        mp[v]=lab[r]
    ee=[]
    for i,(u,v) in enumerate(edges):
        if i not in chosen: ee.append((mp[u],mp[v]))
    return len(lab),ee,mp


def forest_count(n,edges,separate=None):
    ans=0; m=len(edges)
    for mask in range(1<<m):
        ch=[i for i in range(m) if mask>>i&1]
        if not is_forest(n,edges,ch): continue
        if separate is not None:
            p=list(range(n))
            def f(x):
                while p[x]!=x:
                    p[x]=p[p[x]]; x=p[x]
                return x
            for i in ch:
                u,v=edges[i]; ru,rv=f(u),f(v); p[rv]=ru
            if f(separate[0])==f(separate[1]): continue
        ans+=1
    return ans


def simple_paths(n,edges,s,t,forbidden=None):
    adj=[[] for _ in range(n)]
    for i,(u,v) in enumerate(edges):
        if forbidden is not None and (u==forbidden or v==forbidden): continue
        adj[u].append((v,i)); adj[v].append((u,i))
    out=[]
    def dfs(u,seen,path):
        if u==t:
            out.append(tuple(path)); return
        for v,i in adj[u]:
            if v in seen: continue
            seen.add(v); path.append(i)
            dfs(v,seen,path)
            path.pop(); seen.remove(v)
    dfs(s,{s},[])
    return out


def pair_path_sum(n,edges,x,y,z):
    ans=0
    for P in simple_paths(n,edges,x,y,forbidden=z):
        nn,ee,mp=contract(n,edges,set(P))
        ans+=forest_count(nn,ee,separate=(mp[z],mp[x]))
    return ans


def minimal_terminal_trees(n,edges,terms=(0,1,2)):
    out=[]; m=len(edges)
    for mask in range(1<<m):
        ch=[i for i in range(m) if mask>>i&1]
        if not is_forest(n,edges,ch): continue
        def connected(chosen):
            p=list(range(n))
            def f(x):
                while p[x]!=x:
                    p[x]=p[p[x]]; x=p[x]
                return x
            for i in chosen:
                u,v=edges[i]; ru,rv=f(u),f(v); p[rv]=ru
            r=[f(x) for x in terms]
            return r[0]==r[1]==r[2]
        if not connected(ch): continue
        if any(connected([j for j in ch if j!=i]) for i in ch): continue
        out.append(tuple(ch))
    return out


def steiner_sum(n,edges,terms=(0,1,2)):
    ans=0
    for T in minimal_terminal_trees(n,edges,terms):
        nn,ee,_=contract(n,edges,set(T))
        ans+=forest_count(nn,ee)
    return ans


def main():
    checked=0
    for n in range(3,6):
        all_edges=list(combinations(range(n),2))
        for gm in range(1<<len(all_edges)):
            E=[all_edges[i] for i in range(len(all_edges)) if gm>>i&1]
            s=signature(n,E)
            assert s['a']==pair_path_sum(n,E,0,1,2)
            assert s['b']==pair_path_sum(n,E,0,2,1)
            assert s['c']==pair_path_sum(n,E,1,2,0)
            assert s['t']==steiner_sum(n,E)
            checked+=1
    print('PATH_CONTRACTION_CHECK=PASS')
    print('LABELED_GRAPHS_N3_TO_N5=',checked)
    print('PAIR_STATE_IDENTITIES=',3*checked)
    print('STEINER_STATE_IDENTITIES=',checked)
    print('TOTAL_EXACT_IDENTITIES=',4*checked)

if __name__=='__main__':
    main()
