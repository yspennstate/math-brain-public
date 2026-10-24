#!/usr/bin/env python3
# Exact checker for P14-N10-3CUT-SMALLSIDE-STARTRIANGLE-57.
# Standard library only; synthesis arithmetic is Fraction-exact.

from fractions import Fraction
from itertools import combinations, permutations
from math import gcd
import hashlib

PAIR_KEYS=((0,1),(0,2),(1,2))

def connected_internal(k,mask):
    if k==1: return True
    edges=list(combinations(range(k),2)); parent=list(range(k))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    for i,(u,v) in enumerate(edges):
        if (mask>>i)&1:
            ru,rv=find(u),find(v)
            if ru!=rv: parent[ru]=rv
    r=find(0)
    return all(find(i)==r for i in range(k))

def eligible_attachments(k,mask):
    # In a 3-connected graph each separator terminal has a neighbour in Q.
    return all(any((mask>>(t*k+j))&1 for j in range(k)) for t in range(3))

def forest_state(k,internal_mask,attach_mask):
    # Terminals 0,1,2; Q={3,...,2+k}; no terminal-terminal edges on this side.
    q=list(range(3,3+k)); internal=list(combinations(q,2))
    attach=[(t,v) for t in range(3) for v in q]
    edges=[e for i,e in enumerate(internal) if (internal_mask>>i)&1]
    edges += [e for i,e in enumerate(attach) if (attach_mask>>i)&1]
    out=[0,0,0,0,0] # d,a,b,c,t = 0|1|2, 01|2, 02|1, 12|0, 012
    n=3+k
    for sm in range(1<<len(edges)):
        parent=list(range(n))
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]; x=parent[x]
            return x
        good=True
        for j,(u,v) in enumerate(edges):
            if (sm>>j)&1:
                ru,rv=find(u),find(v)
                if ru==rv:
                    good=False; break
                parent[ru]=rv
        if not good: continue
        roots=[find(i) for i in range(3)]
        e01=roots[0]==roots[1]; e02=roots[0]==roots[2]; e12=roots[1]==roots[2]
        if e01 and e02: idx=4
        elif e01: idx=1
        elif e02: idx=2
        elif e12: idx=3
        else: idx=0
        out[idx]+=1
    return tuple(out)

def invariants(s):
    d,a,b,c,t=s
    return d*t-(a*b+a*c+b*c), a*b*c+t*(a*b+a*c+b*c)-d*t*t

def primitive(s):
    g=0
    for x in s: g=gcd(g,x)
    return tuple(x//g for x in s)

def permute_state(s,perm):
    d,a,b,c,t=s; pv={(0,1):a,(0,2):b,(1,2):c}; vals=[]
    for x,y in PAIR_KEYS:
        vals.append(pv[tuple(sorted((perm[x],perm[y])))])
    return (d,vals[0],vals[1],vals[2],t)

def canonical_state(s):
    return min(primitive(permute_state(s,p)) for p in permutations(range(3)))

def synthesis(s):
    # Up to a positive overall scale, synthesize the same terminal-transfer
    # state with a positive star plus nonnegative triangle boundary edges.
    d,a,b,c,t=s; kap,sig=invariants(s)
    p,q,r=Fraction(a,d),Fraction(b,d),Fraction(c,d); h=Fraction(kap,d*d)
    if h==0: return ('triangle',p,q,r)
    vals=[p,q,r]
    for i,j,k in permutations(range(3)):
        pp,qq,rr=vals[i],vals[j],vals[k]
        den=pp*qq-h*(pp+qq)
        if den<=0: continue
        r0=h*(pp*qq+h)/den
        if not (0<r0<=rr): continue
        alpha=pp*qq/h; beta=pp*r0/h; gamma=qq*r0/h
        D=1+alpha+beta+gamma
        P=alpha*beta/D; Q=alpha*gamma/D; R=beta*gamma/D
        H=alpha*beta*gamma/(D*D)
        assert (P,Q,R,H)==(pp,qq,r0,h)
        return ('star+triangle',(i,j,k),alpha,beta,gamma,rr-r0)
    raise AssertionError(('no synthesis',s,kap,sig))

def compatible(pi,pj):
    blocks=[[{0},{1},{2}],[{0,1},{2}],[{0,2},{1}],[{1,2},{0}],[{0,1,2}]]
    def rank(P): return 3-len(P)
    parent=list(range(3))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    for P in (blocks[pi],blocks[pj]):
        for B in P:
            B=list(B)
            for z in B[1:]:
                a,b=find(B[0]),find(z)
                if a!=b: parent[a]=b
    rjoin=3-len({find(i) for i in range(3)})
    return rank(blocks[pi])+rank(blocks[pj])==rjoin

def main():
    K=[[int(compatible(i,j)) for j in range(5)] for i in range(5)]
    expected=[[1,1,1,1,1],[1,0,1,1,0],[1,1,0,1,0],[1,1,1,0,0],[1,0,0,0,0]]
    assert K==expected
    print('claim=P14-N10-3CUT-SMALLSIDE-STARTRIANGLE-57')
    print('compatibility_matrix=')
    for row in K: print(' ',row)
    all_orbits=[]
    for k in (1,2,3):
        nint=k*(k-1)//2; labelled=0; states=set(); min_kap=None; max_kap=None; min_sig=None
        for im in range(1<<nint):
            if not connected_internal(k,im): continue
            for am in range(1<<(3*k)):
                if not eligible_attachments(k,am): continue
                labelled+=1; s=forest_state(k,im,am); states.add(s); kap,sig=invariants(s)
                assert kap>0 and sig>=0; synthesis(s)
                min_kap=kap if min_kap is None else min(min_kap,kap)
                max_kap=kap if max_kap is None else max(max_kap,kap)
                min_sig=sig if min_sig is None else min(min_sig,sig)
        orbits=sorted({canonical_state(s) for s in states}); all_orbits.extend((k,s) for s in orbits)
        print(f'k={k} labelled_eligible={labelled} distinct_states={len(states)} terminal_perm_projective_orbits={len(orbits)} kappa_min={min_kap} kappa_max={max_kap} sigma_min={min_sig}')
        for s in orbits:
            kap,sig=invariants(s); print(' ORBIT',k,s,'kappa',kap,'sigma',sig,'synthesis',synthesis(s))
    # Exact triangle+defect decomposition and kappa conservation under adding
    # any one terminal edge, checked on every projective orbit.
    for k,s in all_orbits:
        d,a,b,c,t=s; kap,_=invariants(s)
        p,q,r=Fraction(a,d),Fraction(b,d),Fraction(c,d); h=Fraction(kap,d*d)
        lhs=(Fraction(d+a+b+c+t,d),Fraction(d+b+c,d),Fraction(d+a+c,d),Fraction(d+a+b,d),Fraction(1))
        tri=(1+p+q+r+p*q+p*r+q*r,1+q+r,1+p+r,1+p+q,Fraction(1))
        assert lhs==(tri[0]+h,tri[1],tri[2],tri[3],tri[4])
        w=Fraction(7,5)
        tests=((d,a+w*d,b,c,t+w*(b+c)),(d,a,b+w*d,c,t+w*(a+c)),(d,a,b,c+w*d,t+w*(a+b)))
        for sp in tests:
            assert sp[0]*sp[4]-(sp[1]*sp[2]+sp[1]*sp[3]+sp[2]*sp[3])==kap
    payload='\n'.join(f'{k}:{",".join(map(str,s))}' for k,s in all_orbits).encode()
    print('orbit_manifest_sha256='+hashlib.sha256(payload).hexdigest())
    print('TOTAL_ORBITS='+str(len(all_orbits)))
    print('EXACT_CHECK_PASS')

if __name__=='__main__': main()
