#!/usr/bin/env python3
"""HARD10-01 exact checks for the 2026-09-16 03Z checkpoint.

Finite enumeration is adversarial self-checking only, not a proof premise.

Checks representative adjacent/disjoint distinguished pairs through n=7 for:
  * the 3+3+1+1 common-ear geometry and its direct-edge present/absent reductions;
  * absence of 6+1+1 and 4+1+1+1+1 in these ranges;
  * reconnaissance for the final unresolved 5+1+1+1 stratum.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations


def norm(e): return tuple(sorted(e))

def forest_components(n, edges, mask):
    parent=list(range(n)); rank=[0]*n
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    for i,(a,b) in enumerate(edges):
        if not ((mask>>i)&1): continue
        a,b=find(a),find(b)
        if a==b: return None
        if rank[a]<rank[b]: a,b=b,a
        parent[b]=a
        if rank[a]==rank[b]: rank[a]+=1
    for i in range(n): parent[i]=find(i)
    return parent


def fixed_R_arrays(n,e,f):
    e,f=norm(e),norm(f)
    H=[g for g in combinations(range(n),2) if g not in (e,f)]
    N=1<<len(H); r=bytearray(N)
    a,b=e; c,d=f
    for mask in range(N):
        comp=forest_components(n,H,mask)
        if comp is None: continue
        ra,rb,rc,rd=comp[a],comp[b],comp[c],comp[d]
        if ra==rb or rc==rd: continue
        if rc in (ra,rb) and rd in (ra,rb) and rc!=rd: r[mask]=1
    root=bytearray(N)
    for mask in range(N):
        if not r[mask]: continue
        x=mask; mini=True
        while x:
            bit=x&-x
            if r[mask^bit]: mini=False; break
            x-=bit
        if mini: root[mask]=1
    counts=list(r)
    for i in range(len(H)):
        bit=1<<i
        for mask in range(N):
            if mask&bit: counts[mask]+=counts[mask^bit]
    return H,r,root,counts


def edge_set(H,m): return {H[i] for i in range(len(H)) if (m>>i)&1}

def root_fibers(Rs,roots): return {P:[A for A in Rs if (P&~A)==0] for P in roots}

def classify(M,r_masks,root_masks):
    Rs=[A for A in r_masks if (A&~M)==0]
    roots=[P for P in root_masks if (P&~M)==0]
    fib=root_fibers(Rs,roots)
    return tuple(sorted((len(v) for v in fib.values()),reverse=True)),Rs,roots,fib

def extension_single_edges(H,P,fiber):
    out=[]
    for A in fiber:
        if A==P: continue
        d=A^P
        if d.bit_count()!=1: return None
        out.append(H[(d&-d).bit_length()-1])
    return out

def ear_info(H,P,fiber):
    at=extension_single_edges(H,P,fiber)
    if at is None or len(at)!=2: return None
    common=set(at[0])&set(at[1])
    if len(common)!=1: return None
    w=next(iter(common))
    ends=tuple(sorted(next(v for v in ed if v!=w) for ed in at))
    return w,ends,tuple(at)

def direct_delta(n,E,e,f):
    E=sorted(set(map(norm,E))); e,f=norm(e),norm(f)
    ie,jf=E.index(e),E.index(f)
    A=B=C=D=0
    for m in range(1<<len(E)):
        if forest_components(n,E,m) is None: continue
        he=(m>>ie)&1; hf=(m>>jf)&1
        if not he and not hf: A+=1
        elif he and not hf: B+=1
        elif hf and not he: C+=1
        else: D+=1
    return B*C-A*D

def weighted_delta_one(n,E,e,f,g,t):
    E=sorted(set(map(norm,E))); e,f,g=norm(e),norm(f),norm(g)
    ie,jf,ig=E.index(e),E.index(f),E.index(g)
    Z=Ze=Zf=Zef=Fraction(0)
    for m in range(1<<len(E)):
        if forest_components(n,E,m) is None: continue
        wt=t if ((m>>ig)&1) else Fraction(1)
        Z+=wt
        if (m>>ie)&1: Ze+=wt
        if (m>>jf)&1: Zf+=wt
        if ((m>>ie)&1) and ((m>>jf)&1): Zef+=wt
    return Ze*Zf-Z*Zef

def pair_shape(pairs):
    mult=Counter(tuple(sorted(p)) for p in pairs)
    deg=Counter()
    for a,b in mult:
        deg[a]+=mult[(a,b)]; deg[b]+=mult[(a,b)]
    return tuple(sorted(mult.values(),reverse=True)), tuple(sorted(deg.values(),reverse=True)), len(deg)


def check_pair(n,e,f):
    H,r,root,counts=fixed_R_arrays(n,e,f)
    r_masks=[m for m,x in enumerate(r) if x]
    root_masks=[m for m,x in enumerate(root) if x]
    parts=Counter(); ear3311=Counter(); replacement=Counter(); scout5111=Counter(); gaps5111=Counter()
    checked3311=0
    for M,total in enumerate(counts):
        if total!=8: continue
        part,Rs,roots,fib=classify(M,r_masks,root_masks)
        parts[part]+=1
        E=edge_set(H,M)|{norm(e),norm(f)}
        if part==(3,3,1,1):
            checked3311+=1
            p3=[P for P in roots if len(fib[P])==3]
            p1=[P for P in roots if len(fib[P])==1]
            ears=[ear_info(H,P,fib[P]) for P in p3]
            assert all(x is not None for x in ears)
            same=(ears[0][0]==ears[1][0] and ears[0][1]==ears[1][1] and set(ears[0][2])==set(ears[1][2]))
            if not same:
                ear3311['cross_ear']+=1
                continue
            ear3311['common_ear']+=1
            ear_edges=set(ears[0][2]); u,v=ears[0][1]; g=norm((u,v))
            assert all(ear_edges <= edge_set(H,Q) for Q in p1)
            present=g in E
            ear3311['direct_present' if present else 'direct_absent']+=1
            if present:
                MB=M
                for ed in ear_edges: MB &= ~(1<<H.index(ed))
                partB,RsB,rootsB,fibB=classify(MB,r_masks,root_masks)
                assert partB==(1,1) and len(RsB)==2 and len(rootsB)==2
                gapG=direct_delta(n,E,e,f)
                EB=E-ear_edges
                gap_eff=weighted_delta_one(n,EB,e,f,g,Fraction(4,3))
                assert Fraction(gapG,1)==9*gap_eff
                replacement[('present',gapG)]+=1
            else:
                MB=M
                for ed in ear_edges: MB &= ~(1<<H.index(ed))
                MB |= 1<<H.index(g)
                partB,RsB,rootsB,fibB=classify(MB,r_masks,root_masks)
                assert partB==(1,1,1,1) and len(RsB)==len(rootsB)==4
                assert sum(g in edge_set(H,A) for A in RsB)==2
                replacement[('absent_allminimal4',direct_delta(n,E,e,f))]+=1
        elif part==(5,1,1,1):
            P=next(P for P in roots if len(fib[P])==5)
            atoms=extension_single_edges(H,P,fib[P]); assert atoms and len(atoms)==4
            common=set(atoms[0])
            for at in atoms[1:]: common &= set(at)
            assert len(common)==1
            w=next(iter(common)); attach={at:next(x for x in at if x!=w) for at in atoms}
            pairs=[]; dirs=[]
            for Q in roots:
                if len(fib[Q])!=1: continue
                Qe=edge_set(H,Q)
                p=tuple(sorted(attach[a] for a in atoms if a in Qe))
                assert len(p)==2
                pairs.append(p); dirs.append(norm(p) in E)
            sh=pair_shape(pairs)
            deg=Counter()
            for a,b in pairs:
                deg[a]+=1; deg[b]+=1
            absent=[p for p in pairs if norm(p) not in E]
            complement_ok=None; absent_middle=None
            if sh==((1,1,1),(2,2,1,1),4) and len(absent)==1:
                ap=absent[0]
                absent_middle=(deg[ap[0]]==2 and deg[ap[1]]==2)
                ends=tuple(sorted(v for v,d in deg.items() if d==1))
                complement_ok=(norm(ends) in E)
            scout5111[(sh,tuple(sorted(dirs)),absent_middle,complement_ok)]+=1
            gaps5111[direct_delta(n,E,e,f)]+=1
    assert parts.get((6,1,1),0)==0
    assert parts.get((4,1,1,1,1),0)==0
    return parts,checked3311,ear3311,replacement,scout5111,gaps5111


def main():
    configs=[
        (6,(0,1),(0,2),'n6_adjacent'),
        (6,(0,1),(2,3),'n6_disjoint'),
        (7,(0,1),(0,2),'n7_adjacent'),
        (7,(0,1),(2,3),'n7_disjoint'),
    ]
    for n,e,f,label in configs:
        print(label)
        parts,c,einfo,repl,scout,gaps=check_pair(n,e,f)
        print(' R8_partitions',dict(parts))
        print(' 3+3+1+1_checked',c,'ear_structure',dict(einfo))
        print(' 3+3+1+1_replacement',dict(repl))
        print(' count_6+1+1',parts.get((6,1,1),0))
        print(' count_4+1^4',parts.get((4,1,1,1,1),0))
        print(' 5+1^3_scout',dict(scout))
        print(' 5+1^3_gaps',dict(gaps))

if __name__=='__main__': main()
