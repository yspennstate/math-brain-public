#!/usr/bin/env python3
from itertools import combinations
from collections import Counter
from fractions import Fraction


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


def is_R(n, M_edges, mask, e, f):
    comp=forest_components(n,M_edges,mask)
    if comp is None: return False
    a,b=e; c,d=f
    ra,rb,rc,rd=comp[a],comp[b],comp[c],comp[d]
    if ra==rb or rc==rd: return False
    return rc in (ra,rb) and rd in (ra,rb) and rc!=rd


def graph_R(n, M_edges, e, f):
    Rs=[m for m in range(1<<len(M_edges)) if is_R(n,M_edges,m,e,f)]
    Rset=set(Rs)
    roots=[m for m in Rs if all((m^(1<<i)) not in Rset for i in range(len(M_edges)) if (m>>i)&1)]
    fib={P:[A for A in Rs if (P&~A)==0] for P in roots}
    return Rs,roots,fib


def fixed_arrays(n,e,f):
    e,f=norm(e),norm(f)
    H=[g for g in combinations(range(n),2) if g not in (e,f)]
    N=1<<len(H); r=bytearray(N); root=bytearray(N)
    for m in range(N): r[m]=1 if is_R(n,H,m,e,f) else 0
    for m in range(N):
        if r[m] and all(not r[m^(1<<i)] for i in range(len(H)) if (m>>i)&1): root[m]=1
    counts=list(r)
    for i in range(len(H)):
        bit=1<<i
        for m in range(N):
            if m&bit: counts[m]+=counts[m^bit]
    return H,r,root,counts


def classify_subgraph(M,H,r,root):
    Rs=[A for A,x in enumerate(r) if x and (A&~M)==0]
    roots=[P for P,x in enumerate(root) if x and (P&~M)==0]
    fib={P:[A for A in Rs if (P&~A)==0] for P in roots}
    return tuple(sorted((len(v) for v in fib.values()),reverse=True)),Rs,roots,fib


def edges_of(mask,edges): return [edges[i] for i in range(len(edges)) if (mask>>i)&1]


def atom_edges(P,family,edges):
    base=set(edges_of(P,edges)); ans=[]
    for A in family:
        d=set(edges_of(A,edges))-base
        if len(d)==1: ans.append(next(iter(d)))
    return ans


def ear_from_size3(P,family,edges):
    atoms=atom_edges(P,family,edges); assert len(atoms)==2
    common=set(atoms[0])&set(atoms[1]); assert len(common)==1
    c=next(iter(common)); ends=tuple(sorted(next(iter(set(a)-{c})) for a in atoms))
    return tuple(sorted(atoms)),c,ends


def weighted_delta(n,M_edges,e,f,weights=None):
    weights=weights or {}; all_edges=[norm(e),norm(f)]+list(M_edges)
    A=B=C=D=Fraction(0)
    for mask in range(1<<len(all_edges)):
        parent=list(range(n))
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]; x=parent[x]
            return x
        ok=True; wt=Fraction(1)
        for i,(u,v) in enumerate(all_edges):
            if not ((mask>>i)&1): continue
            ru,rv=find(u),find(v)
            if ru==rv: ok=False; break
            parent[ru]=rv
            if i>=2: wt*=weights.get((u,v),weights.get((v,u),Fraction(1)))
        if not ok: continue
        he=bool(mask&1); hf=bool(mask&2)
        if not he and not hf:A+=wt
        elif he and not hf:B+=wt
        elif hf and not he:C+=wt
        else:D+=wt
    return A,B,C,D,B*C-A*D


def compress_ear(M_edges,ear_edges,endpoints):
    s={norm(x) for x in ear_edges}; g=norm(endpoints)
    out=[x for x in M_edges if norm(x) not in s]; assert g not in out
    out.append(g); return sorted(out),g


def downward_closed(k,N):
    base={0}|{1<<i for i in range(k)}; need=N-len(base)
    if need<0:return []
    extras=[m for m in range(1<<k) if m not in base]; out=[]
    for ch in combinations(extras,need):
        F=base|set(ch); ok=True
        for m in F:
            x=m
            while x:
                b=x&-x
                if (m^b) not in F: ok=False; break
                x-=b
            if not ok: break
        if ok: out.append(F)
    return out


def allowed_pairs(k,F):
    return [(i,j) for i,j in combinations(range(k),2) if ((1<<i)|(1<<j)) in F]


def local_badpair_filter(k,F):
    H=set(allowed_pairs(k,F))
    def edge(i,j): return tuple(sorted((i,j))) in H
    for a,b in H:
        for c in range(k):
            if c not in (a,b) and not edge(a,c) and not edge(b,c): return False
    return True


def check_size9_downsets():
    summary={}; survivors={}
    for k in range(4,9):
        fams=downward_closed(k,9)
        sig=Counter((sum(m.bit_count()==2 for m in F),sum(m.bit_count()==3 for m in F)) for F in fams)
        summary[k]=(len(fams),dict(sig))
        sf=[F for F in fams if local_badpair_filter(k,F)]; survivors[k]=len(sf)
        if k==4:
            for F in sf:
                H=allowed_pairs(k,F); deg=[0]*4
                for a,b in H: deg[a]+=1;deg[b]+=1
                assert sorted(deg)==[2,2,2,2] and len(H)==4
    assert survivors=={4:3,5:0,6:0,7:0,8:1}
    return summary,survivors


def check_core_values():
    # Exact-two K4: marked exchange matching 02,13; distinguished 03,12.
    M=[(0,1),(2,3),(0,2),(1,3)]
    d=weighted_delta(4,M,(0,3),(1,2),{(0,2):Fraction(1,3),(1,3):Fraction(1,3)})[-1]
    assert d==Fraction(322,81)
    # 4+1+1 wheel normal form, incidence-four direct edge 02.
    M2=[(0,2),(1,3),(0,4),(1,4),(2,4),(0,3)]
    vals=[weighted_delta(5,M2,(0,1),(2,3),{(0,2):s})[-1] for s in [Fraction(0),Fraction(1),Fraction(2),Fraction(1,3)]]
    assert vals==[Fraction(12),Fraction(84),Fraction(220),Fraction(260,9)]
    return d,vals


def run_target_checks(n,e,f):
    H,r,root,counts=fixed_arrays(n,e,f); target=Counter(); gaps=Counter(); details=Counter()
    for M,total in enumerate(counts):
        if total!=10: continue
        part,Rs,roots,fib=classify_subgraph(M,H,r,root)
        if part not in {(9,1),(7,3),(4,3,3)}: continue
        target[part]+=1; M_edges=edges_of(M,H); gap=weighted_delta(n,M_edges,e,f)[-1]; gaps[(part,gap)]+=1
        if part==(9,1):
            P=next(P for P in roots if len(fib[P])==9); S=next(P for P in roots if len(fib[P])==1)
            atoms=atom_edges(P,fib[P],H); assert len(atoms)==4
            base=set(edges_of(P,H)); famsets=[frozenset(set(edges_of(A,H))-base) for A in fib[P]]
            allowed=[(i,j) for i,j in combinations(range(4),2) if frozenset([atoms[i],atoms[j]]) in famsets]
            deg=[0]*4
            for i,j in allowed: deg[i]+=1;deg[j]+=1
            assert sorted(deg)==[2,2,2,2]
            bad=[p for p in combinations(range(4),2) if p not in allowed]; assert len(bad)==2 and set(bad[0]).isdisjoint(bad[1])
            gs=[]
            for i,j in bad:
                common=set(atoms[i])&set(atoms[j]); assert len(common)==1
                c=next(iter(common)); ends=tuple(sorted((next(iter(set(atoms[i])-{c})),next(iter(set(atoms[j])-{c})))))
                gs.append(norm(ends)); assert norm(ends) not in M_edges
            assert all(a in set(edges_of(S,H)) for a in atoms)
            B=[x for x in M_edges if x not in set(atoms)]+gs
            BR,Broots,Bfib=graph_R(n,B,e,f); assert tuple(sorted(map(len,Bfib.values()),reverse=True))==(1,1)
            db=weighted_delta(n,B,e,f,{gs[0]:Fraction(1,3),gs[1]:Fraction(1,3)})[-1]
            assert gap==81*db; details['9+1_exact_two_compression']+=1
        elif part==(7,3):
            Q=next(P for P in roots if len(fib[P])==3); P=next(P for P in roots if len(fib[P])==7)
            ear,center,ends=ear_from_size3(Q,fib[Q],H); assert all(x in set(edges_of(P,H)) for x in ear); assert norm(ends) not in M_edges
            B,g=compress_ear(M_edges,ear,ends); BR,Broots,Bfib=graph_R(n,B,e,f)
            assert tuple(sorted(map(len,Bfib.values()),reverse=True))==(7,1)
            db=weighted_delta(n,B,e,f,{g:Fraction(1,3)})[-1]; assert gap==9*db and db>=0
            details['7+3_to_7+1']+=1
        else:
            P=next(P for P in roots if len(fib[P])==4); qs=[Q for Q in roots if len(fib[Q])==3]
            ears=[ear_from_size3(Q,fib[Q],H) for Q in qs]; assert ears[0][0]==ears[1][0]
            ear,center,ends=ears[0]; assert all(x in set(edges_of(P,H)) for x in ear); assert norm(ends) not in M_edges
            B,g=compress_ear(M_edges,ear,ends); BR,Broots,Bfib=graph_R(n,B,e,f)
            assert tuple(sorted(map(len,Bfib.values()),reverse=True))==(4,1,1)
            gi=B.index(g); assert sum(1 for A in BR if (A>>gi)&1)==4
            db=weighted_delta(n,B,e,f,{g:Fraction(1,3)})[-1]; assert gap==9*db
            details['4+3+3_common_ear']+=1
    return target,gaps,details


def main():
    summary,survivors=check_size9_downsets(); print('size9_downsets',summary); print('local_badpair_survivors',survivors)
    k4,wheel=check_core_values(); print('K4_two_marked_at_1/3',k4,'after_two_path_factor',81*k4)
    print('wheel_incidence4_delta_values_s0_s1_s2_s1/3',wheel,'after_path_factor',9*wheel[-1])
    for n,e,f,label in [(6,(0,1),(0,2),'n6_adjacent'),(6,(0,1),(2,3),'n6_disjoint')]:
        target,gaps,details=run_target_checks(n,norm(e),norm(f))
        print(label,'targets',dict(target)); print(label,'gaps',{str(k):v for k,v in gaps.items()}); print(label,'details',dict(details))
    print('OK')

if __name__=='__main__': main()
