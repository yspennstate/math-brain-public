"""Exact finite checks for the second attempt. No infinite-graph inference."""
from fractions import Fraction as F
from itertools import combinations, product
import json

def connection_matrix(n, edges, p):
    T = [[F(0) for _ in range(n)] for _ in range(n)]
    for bits in product((0,1), repeat=len(edges)):
        prob = p**sum(bits)*(1-p)**(len(edges)-sum(bits))
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        for bit,(u,v) in zip(bits,edges):
            if bit:
                parent[find(u)] = find(v)
        for u in range(n):
            for v in range(n):
                if find(u)==find(v):
                    T[u][v] += prob
    return T

def mul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]

def inverse(A):
    n = len(A)
    M = [list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for i in range(n):
        k = next(k for k in range(i,n) if M[k][i])
        M[i],M[k] = M[k],M[i]
        a = M[i][i]
        M[i] = [x/a for x in M[i]]
        for k in range(n):
            if k != i:
                a = M[k][i]
                M[k] = [x-a*y for x,y in zip(M[k],M[i])]
    return [row[n:] for row in M]

results=[]
contact_checks=0
bubble_checks=0
graphs={'K4':list(combinations(range(4),2)),
        'C4':[(0,1),(1,2),(2,3),(3,0)],
        'P4':[(0,1),(1,2),(2,3)]}
p,q = F(1,4),F(1,3)
t=(q-p)/(1-p)
assert p+(1-p)*t==q
for name,edges in graphs.items():
    n=4
    Tp,Tq=connection_matrix(n,edges,p),connection_matrix(n,edges,q)
    A=[[F(0) for _ in range(n)] for _ in range(n)]
    for u,v in edges:
        A[u][v]=A[v][u]=F(1)
    Delta=max(sum(row) for row in A)
    K=max(sum(row) for row in Tp) # valid norm upper bound by symmetry/Schur
    z=t*Delta*K
    assert z<1
    AT=mul(A,Tp)
    S=mul(Tp,inverse([[F(i==j)-t*AT[i][j] for j in range(n)] for i in range(n)]))
    bound=t*Delta*K*K/(1-z)
    for u in range(n):
        for v in range(n):
            assert F(0)<=Tq[u][v]-Tp[u][v]<=S[u][v]-Tp[u][v]
            assert Tq[u][v]-Tp[u][v]<=bound
    assert max(sum(row) for row in Tq)<=K/(1-z)

    # Independent finite contact-count distribution, then the conditional
    # merger lower bound used before the asymptotic tail estimate.
    graph_adj=[[] for _ in range(n)]
    for u,v in edges:
        graph_adj[u].append(v)
        graph_adj[v].append(u)
    for R in (1,2):
        balls=[]
        for x in range(n):
            S={x}
            for _ in range(R):
                S |= {y for a in list(S) for y in graph_adj[a]}
            balls.append(S)
        L=(R+1)*max(map(len,balls))
        tails=[[[F(0) for _ in range(n+1)] for v in range(n)] for u in range(n)]
        for bits in product((0,1),repeat=len(edges)):
            prob=p**sum(bits)*(1-p)**(len(edges)-sum(bits))
            parent=list(range(n))
            def find(x):
                while parent[x]!=x:
                    x=parent[x]
                return x
            for bit,(a,c) in zip(bits,edges):
                if bit:
                    parent[find(a)]=find(c)
            for u in range(n):
                for v in range(n):
                    if find(u)==find(v):
                        continue
                    C={x for x in range(n) if find(x)==find(u)}
                    D={x for x in range(n) if find(x)==find(v)}
                    Z=sum(bool(balls[x]&D) for x in C)
                    for N in range(1,Z+1):
                        tails[u][v][N]+=prob
        for u in range(n):
            for v in range(n):
                EZ=sum(tails[u][v][1:],F(0))
                bk_sum=sum((Tp[u][x]*Tp[v][y]
                            for x in range(n) for y in balls[x]),F(0))
                bubble_u=sum((a*a for a in Tp[u]),F(0))
                bubble_v=sum((a*a for a in Tp[v]),F(0))
                assert EZ<=bk_sum
                assert bk_sum*bk_sum<=max(map(len,balls))**2*bubble_u*bubble_v
                bubble_checks+=1
                for N in range(1,n+1):
                    m=(N+L-1)//L
                    merger_lower=1-(1-t**R)**m
                    assert tails[u][v][N]*merger_lower<=Tq[u][v]-Tp[u][v]
                    contact_checks+=1
    results.append({'graph':name,'configurations_per_parameter':2**len(edges),
                    'p':str(p),'q':str(q),'t':str(t),'K_upper':str(K),
                    'series_ratio_upper':str(z),'difference_bound':str(bound),
                    'entrywise_resolvent_bound':'passed'})

# Demonstrate exactly the failure of treating a repeated new edge as independent.
assert t>t*t
# Explicit parameter with light GP(2) clusters but divergent l2 column.
b,pbad=2,F(3,4)
assert b*pbad*pbad==F(9,8)>1
partial_l2=[1+sum(F(b+1)*b**(n-1)*pbad**(2*n) for n in range(1,N+1))
            for N in (10,20,40)]
assert partial_l2[0]<partial_l2[1]<partial_l2[2]
for m in range(1,101):
    assert (1-F(1,m))**m<=F(1,2)

out={'finite_operator_tests':results,
     'exact_contact_merger_inequalities_checked':contact_checks,
     'exact_expected_contact_and_bubble_inequalities_checked':bubble_checks,
     'repeated_edge_probability':str(t),'incorrect_independent_square':str(t*t),
     'GP2_p_three_quarters_l2_shell_ratio':'9/8',
     'GP2_column_partial_lower_bounds':[str(x) for x in partial_l2],
     'scope':'Exact finite verification only; infinite arguments are written proofs.'}
open('operator_checks_output.json','w',encoding='utf-8').write(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
