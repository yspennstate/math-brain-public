#!/usr/bin/env python3
from itertools import permutations

def defect_identity(c,k,triples):
    # triples (root,middle,leaf)
    roots=sorted(r for r,m,l in triples)
    assert roots==list(range(2*c,3*c))
    non=sorted([x for r,m,l in triples for x in (m,l)])
    assert non==list(range(2*c))
    diffs=sorted([abs(r-m) for r,m,l in triples]+[abs(m-l) for r,m,l in triples])
    assert diffs==list(range(k+1,k+2*c+1))
    mins=[]; revsum=0
    for r,m,l in triples:
        a,b=sorted((m,l)); mins.append(a)
        if m==b:
            revsum += b-a
    E=sum(mins)-c*(c-1)//2
    lhs=c*(c-2*k-1)
    rhs=3*E+revsum
    assert E>=0 and lhs==rhs
    return E,revsum

def exact_cover_find(c,k):
    roots=list(range(2*c,3*c))
    non=list(range(2*c))
    D=list(range(k+1,k+2*c+1))
    Dset=set(D)
    triples=[]
    for r in roots:
        for m in non:
            d1=r-m
            if d1 not in Dset: continue
            for l in non:
                if l==m: continue
                d2=abs(m-l)
                if d2 not in Dset or d2==d1: continue
                triples.append((r,m,l,d1,d2))
    items=[('r',r) for r in roots]+[('n',x) for x in non]+[('d',d) for d in D]
    mp={it:[] for it in items}
    for idx,(r,m,l,d1,d2) in enumerate(triples):
        for it in [('r',r),('n',m),('n',l),('d',d1),('d',d2)]:
            mp[it].append(idx)
    used_r=set();used_n=set();used_d=set();chosen=[]
    def compat(t):
        r,m,l,d1,d2=t
        return r not in used_r and m not in used_n and l not in used_n and d1 not in used_d and d2 not in used_d
    def dfs():
        if len(chosen)==c:
            return list(chosen)
        best=None
        for it in items:
            typ,val=it
            covered=(val in used_r if typ=='r' else val in used_n if typ=='n' else val in used_d)
            if covered: continue
            cand=[j for j in mp[it] if compat(triples[j])]
            if not cand: return None
            if best is None or len(cand)<len(best):
                best=cand
                if len(best)==1: break
        for j in best:
            r,m,l,d1,d2=triples[j]
            used_r.add(r);used_n.add(m);used_n.add(l);used_d.add(d1);used_d.add(d2);chosen.append(triples[j])
            ans=dfs()
            if ans is not None: return ans
            chosen.pop();used_r.remove(r);used_n.remove(m);used_n.remove(l);used_d.remove(d1);used_d.remove(d2)
        return None
    ans=dfs()
    if ans is None: return None
    return [(r,m,l) for r,m,l,d1,d2 in ans]

def tensor_minimal(c,k):
    assert c==2*k+1
    out=[]
    for r in range(c):
        middle=(2*r)%c
        leaf=c+r
        root=2*c+r
        out.append((root,middle,leaf))
    return out

def brute_c2_k0():
    c=2;k=0
    roots=list(range(4,6)); non=list(range(4)); target=list(range(1,5))
    for perm in permutations(non):
        pairs=[(perm[0],perm[1]),(perm[2],perm[3])]
        for rr in permutations(roots):
            diffs=[]
            for i,(m,l) in enumerate(pairs):
                diffs += [rr[i]-m,abs(m-l)]
            if sorted(diffs)==target:
                return False,(rr,pairs)
    return True,None

checks=0
for k in range(0,101):
    c=2*k+1
    sol=tensor_minimal(c,k)
    E,rev=defect_identity(c,k,sol)
    assert E==0 and rev==0
    checks += 1
print('TENSOR_MINIMAL_CHECKS',checks)

examples={
    (3,0):[(6,0,4),(7,2,1),(8,5,3)],
    (4,1):[(8,2,4),(9,0,7),(10,5,1),(11,3,6)],
}
for key,sol in examples.items():
    defect_identity(*key,sol)
print('EXPLICIT_NON_TENSOR_CHECKS',len(examples))

census={}
for c in range(1,9):
    vals=[]
    for k in range(0,(c-1)//2+1):
        sol=exact_cover_find(c,k)
        if sol is not None:
            defect_identity(c,k,sol)
            vals.append(k)
    census[c]=vals
print('CENSUS',census)
expected={1:[0],2:[],3:[0,1],4:[0,1],5:[0,1,2],6:[0,1,2],7:[0,1,2,3],8:[0,1,2,3]}
assert census==expected

ok,w=brute_c2_k0()
assert ok and w is None
print('C2K0_EXHAUSTIVE_NONEXISTENCE',ok)
print('ALL_CHECKS_PASSED')
