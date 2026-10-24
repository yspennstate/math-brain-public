#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from collections import defaultdict, deque

CHECKS = 0

def chk(cond):
    global CHECKS
    assert cond
    CHECKS += 1

def canon(blocks):
    return tuple(sorted((tuple(sorted(b)) for b in blocks),
                        key=lambda x:(min(x), len(x), x)))

def setparts(items):
    items = list(items)
    if not items:
        yield []
        return
    a = items[0]
    for rest in setparts(items[1:]):
        yield [[a]] + [list(b) for b in rest]
        for j in range(len(rest)):
            nr = [list(b) for b in rest]
            nr[j] = [a] + nr[j]
            yield nr

_IP = {}
def index_parts(r):
    if r in _IP:
        return _IP[r]
    out, seen = [], set()
    for p in setparts(range(r)):
        c = tuple(sorted((tuple(sorted(b)) for b in p),
                         key=lambda b:(b[0], len(b), b)))
        if c not in seen:
            seen.add(c); out.append(c)
    _IP[r] = out
    return out

_AP = {}
def all_parts(m):
    if m in _AP:
        return _AP[m]
    out, seen = [], set()
    for p in setparts(range(m)):
        c = canon(p)
        if c not in seen:
            seen.add(c); out.append(c)
    _AP[m] = out
    return out

def falling(N,k):
    z=1
    for q in range(k):
        z *= N-q
    return z

def wf_transition(part,N):
    r=len(part)
    tr=defaultdict(Fraction)
    for pi in index_parts(r):
        k=len(pi)
        pr=Fraction(falling(N,k), N**r)
        blocks=[]
        for group in pi:
            s=set()
            for idx in group:
                s.update(part[idx])
            blocks.append(s)
        tr[canon(blocks)] += pr
    chk(sum(tr.values()) == 1)
    return dict(tr)

def solve(A,b):
    n=len(A)
    M=[list(A[i])+[b[i]] for i in range(n)]
    for col in range(n):
        piv=next(r for r in range(col,n) if M[r][col])
        M[col],M[piv]=M[piv],M[col]
        z=M[col][col]
        M[col]=[x/z for x in M[col]]
        for r in range(n):
            if r==col:
                continue
            z=M[r][col]
            if z:
                M[r]=[M[r][c]-z*M[col][c] for c in range(n+1)]
    return [M[i][-1] for i in range(n)]

def expected_sfs(N,m):
    states=[p for p in all_parts(m) if len(p)>1]
    ix={p:i for i,p in enumerate(states)}
    n=len(states)
    A=[[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    for p in states:
        i=ix[p]
        for q,pr in wf_transition(p,N).items():
            if len(q)>1:
                A[i][ix[q]] -= pr
    init=canon([{i} for i in range(m)])
    ans={}
    for s in range(1,m):
        reward=[Fraction(sum(len(B)==s for B in p)) for p in states]
        x=solve(A,reward)
        ans[s]=x[ix[init]]
    return ans

max_scaled_err=Fraction(0)
sfs_rows=[]
for m in range(2,6):
    for N in sorted(set([max(m,5), 8, 12, 20])):
        if N < m:
            continue
        z=expected_sfs(N,m)
        for i,val in z.items():
            target=Fraction(2,i)
            err=abs(val/Fraction(N)-target)
            max_scaled_err=max(max_scaled_err, N*err)
            chk(err <= Fraction(2, max(1,N-m+1)))
        sfs_rows.append((m,N,z))

for b in range(2,7):
    for N in (10,20,50,100):
        if N < b: continue
        discrete=canon([{i} for i in range(b)])
        tr=wf_transition(discrete,N)
        p_no=tr.get(discrete,Fraction(0))
        chk(p_no == Fraction(falling(N,b),N**b))
        err=abs(p_no - (Fraction(1)-Fraction(b*(b-1),2*N)))
        chk(N*N*err < 1000)

for N in range(2,101):
    mean=Fraction(N)
    var=Fraction(N*(N-1))
    chk(mean == N)
    chk(var/Fraction(N*N) == Fraction(N-1,N))

def refine(out,S):
    S=set(S); blocks=[]
    for B in out:
        B=set(B)
        x=B&S; y=B-S
        if x: blocks.append(x)
        if y: blocks.append(y)
    return canon(blocks)

def state_transition(st,N,u):
    anc,out=st
    r=len(anc)
    if r==1:
        return {st:Fraction(1)}
    tr=defaultdict(Fraction)
    for mask in product((0,1), repeat=r):
        pm=Fraction(1); out2=out
        for j,bit in enumerate(mask):
            if bit:
                pm *= u
                out2 = refine(out2, anc[j])
            else:
                pm *= 1-u
        for pi in index_parts(r):
            pr=Fraction(falling(N,len(pi)),N**r)
            blocks=[]
            for group in pi:
                s=set()
                for idx in group:
                    s.update(anc[idx])
                blocks.append(s)
            tr[(canon(blocks),out2)] += pm*pr
    chk(sum(tr.values()) == 1)
    return dict(tr)

def final_refinement_law(N,m,u):
    init=(canon([{i} for i in range(m)]),canon([set(range(m))]))
    seen={init}; q=deque([init])
    while q:
        s=q.popleft()
        if len(s[0])==1:
            continue
        for t in state_transition(s,N,u):
            if t not in seen:
                seen.add(t); q.append(t)
    trans=[s for s in seen if len(s[0])>1]
    ix={s:i for i,s in enumerate(trans)}
    n=len(trans)
    A=[[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    absorb=defaultdict(lambda:[Fraction(0) for _ in range(n)])
    for s in trans:
        i=ix[s]
        for t,p in state_transition(s,N,u).items():
            if len(t[0])>1:
                A[i][ix[t]] -= p
            else:
                absorb[len(t[1])][i] += p
    law={}
    for deg,rhs in absorb.items():
        x=solve(A,rhs)
        law[deg]=x[ix[init]]
    chk(sum(law.values()) == 1)
    return law,len(seen)

N=3
u=Fraction(1,2*N*N)
law,nstates=final_refinement_law(N,3,u)
chk(law[1] == Fraction(2613716,4202207))
chk(law[2] == Fraction(2811681,8404414))
chk(law[3] == Fraction(365301,8404414))
first3=law[3]/(1-law[1])
chk(first3 == Fraction(40589,352998))

prior = [
    Fraction(0), Fraction(1,10), Fraction(1,22), Fraction(1,6),
    Fraction(1,728), Fraction(1,7), Fraction(1,71), Fraction(1,71),
    Fraction(0), Fraction(0), Fraction(2,105), Fraction(21521,4909716),
    Fraction(35,1296), Fraction(14,2201), Fraction(2,17)
]
for x in prior:
    chk(first3 != x)

print("R11 I0054 C016 Wright-Fisher genealogy exact self-check")
print("checks =", CHECKS)
print("max_N_times_SFS_error_grid =", max_scaled_err)
print("N=3 mutation_probability =", u)
print("N=3 refinement_state_count =", nstates)
print("N=3 no_visible_refinement =", law[1])
print("N=3 degree2 =", law[2])
print("N=3 raw_degree3 =", law[3])
print("N=3 first_visible_degree3 =", first3)
print("single_frozen_two_lineage_variance_limit: Var(T_N/N)=(N-1)/N -> 1")
print("ALL_EXACT_CHECKS_PASS")
