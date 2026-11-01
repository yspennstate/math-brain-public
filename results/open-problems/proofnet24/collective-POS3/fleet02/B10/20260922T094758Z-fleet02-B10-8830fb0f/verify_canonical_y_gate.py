#!/usr/bin/env python3
from itertools import combinations

def closure_bits(n, mask):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    rel=[[False]*n for _ in range(n)]
    for k,(i,j) in enumerate(pairs):
        if (mask>>k)&1: rel[i][j]=True
    for k in range(n):
        for i in range(n):
            if rel[i][k]:
                for j in range(n):
                    if rel[k][j]: rel[i][j]=True
    out=0
    for k,(i,j) in enumerate(pairs):
        if rel[i][j]: out |= 1<<k
    return out

def rel_from_bits(n,bits):
    rel=[[False]*n for _ in range(n)]
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    for k,(i,j) in enumerate(pairs):
        if (bits>>k)&1: rel[i][j]=True
    return rel

def closure_from_covers(n,edges):
    rel=[[False]*n for _ in range(n)]
    for a,b in edges: rel[a][b]=True
    for k in range(n):
        for i in range(n):
            if rel[i][k]:
                for j in range(n):
                    if rel[k][j]: rel[i][j]=True
    return rel

def linear_extensions(rel, verts=None):
    n=len(rel)
    if verts is None: verts=tuple(range(n))
    verts=tuple(verts)
    pred={v:{u for u in verts if rel[u][v]} for v in verts}
    out=[]
    def rec(done,seq):
        if len(seq)==len(verts):
            out.append(tuple(seq)); return
        for v in verts:
            if v not in done and pred[v] <= done:
                rec(done|{v},seq+(v,))
    rec(set(),tuple())
    return out

def width(rel):
    n=len(rel); best=0
    for mask in range(1<<n):
        k=mask.bit_count()
        if k<=best: continue
        vs=[i for i in range(n) if (mask>>i)&1]
        if all(not rel[a][b] and not rel[b][a] for a,b in combinations(vs,2)):
            best=k
    return best

def covers_up(rel,p):
    n=len(rel)
    return [r for r in range(n) if rel[p][r] and
            not any(rel[p][z] and rel[z][r] for z in range(n) if z not in (p,r))]

def count_before(exts,a,b):
    return sum(e.index(a)<e.index(b) for e in exts)

def legal_slot_count(rel,tau,x):
    pos={v:i for i,v in enumerate(tau)}
    L=0; U=len(tau)
    for z in tau:
        if rel[z][x]: L=max(L,pos[z]+1)
        if rel[x][z]: U=min(U,pos[z])
    assert L<=U
    return L,U,U-L+1

def fiber_counts(a,b):
    if b>=a:
        pq=a*b-a*(a-1)//2
        qp=a*(a+1)//2
    else:
        pq=b*(b+1)//2
        qp=a*b-b*(b-1)//2
    assert pq-qp == min(a,b)*(b-a)
    return pq,qp

common_pairs=0; fibers=0; gate_cases=0; struct_two_one=0
unique_counts={}; width3_posets=0
for n in range(2,7):
    seen=set(); k=n*(n-1)//2
    for mask in range(1<<k): seen.add(closure_bits(n,mask))
    unique_counts[n]=len(seen)
    for bits in seen:
        rel=rel_from_bits(n,bits)
        if width(rel)>3: continue
        width3_posets += 1
        exts=linear_extensions(rel); E=len(exts)
        for p in range(n):
            for q in range(n):
                if p==q or rel[p][q] or rel[q][p]: continue
                Pp={z for z in range(n) if rel[z][p]}
                Pq={z for z in range(n) if rel[z][q]}
                if Pp!=Pq: continue
                common_pairs += 1
                M=count_before(exts,p,q); N=E-M
                rest=[v for v in range(n) if v not in (p,q)]
                fp=fq=0
                for tau in linear_extensions(rel,rest):
                    Lp,Up,a=legal_slot_count(rel,tau,p)
                    Lq,Uq,b=legal_slot_count(rel,tau,q)
                    assert Lp==Lq
                    cp,cq=fiber_counts(a,b)
                    fp += cp; fq += cq; fibers += 1
                assert (fp,fq)==(M,N)
                Upfam=[r for r in covers_up(rel,p) if not rel[q][r] and not rel[r][q]]
                Uqfam=[s for s in covers_up(rel,q) if not rel[p][s] and not rel[s][p]]
                O=sum(any(e.index(r)<e.index(q) for r in Upfam) for e in exts)
                I=sum(any(e.index(s)<e.index(p) for s in Uqfam) for e in exts)
                assert O-I == M-N
                if len(Upfam)==2 and len(Uqfam)==1:
                    struct_two_one += 1
                    r1,r2=Upfam; s=Uqfam[0]
                    assert not rel[r1][r2] and not rel[r2][r1]
                    assert all(not rel[r][s] and not rel[s][r] for r in Upfam)
                if 3*M>2*E and Upfam and all(3*count_before(exts,q,r)>2*E for r in Upfam):
                    gate_cases += 1
                    assert len(Upfam)==2
                    assert len(Uqfam)<=1
                    B=N
                    alphas=[count_before(exts,r,q) for r in Upfam]
                    assert all(3*a<E for a in alphas)
                    assert O < 2*E/3
                    if Uqfam:
                        s=Uqfam[0]; delta=count_before(exts,s,p)
                        assert I==delta
                        assert 3*delta < 6*B-E
                        assert delta < B
                    else:
                        assert I==0
                    assert 6*B>E

covers=[(0,3),(0,5),(1,3),(1,6),(2,4),(2,5),(4,7),(5,6)]
rel=closure_from_covers(8,covers)
assert width(rel)==3
exts=linear_extensions(rel); E=len(exts)
p,q=2,1
M=count_before(exts,p,q); B=E-M
Upfam=[r for r in covers_up(rel,p) if not rel[q][r] and not rel[r][q]]
Uqfam=[s for s in covers_up(rel,q) if not rel[p][s] and not rel[s][p]]
assert Upfam==[4,5] and Uqfam==[3]
qr=[count_before(exts,q,r) for r in Upfam]
delta=count_before(exts,3,p)
O=sum(any(e.index(r)<e.index(q) for r in Upfam) for e in exts)
I=sum(e.index(3)<e.index(p) for e in exts)
assert (E,M,B,qr,delta,O,I)==(360,243,117,[246,288],12,138,12)
assert O-I==M-B
assert 3*M>2*E and all(3*x>2*E for x in qr)
assert 3*delta < 6*B-E and delta<B
balanced=[]
for a,b in combinations(range(8),2):
    if rel[a][b] or rel[b][a]: continue
    c=count_before(exts,a,b)
    if 3*c>=E and 3*c<=2*E: balanced.append((a,b,c,E-c))
assert balanced
print("unique_n2_to_n6", unique_counts)
print("width_le_3_posets_n2_to_n6", width3_posets)
print("common_predecessor_ordered_pairs", common_pairs)
print("exact_deletion_fibers_checked", fibers)
print("canonical_local_gate_cases", gate_cases)
print("two_out_one_reverse_structural_pairs", struct_two_one)
print("calibration_covers", covers)
print("calibration_E_M_B", E,M,B)
print("calibration_out_covers_reverse_cover", Upfam,Uqfam)
print("calibration_q_before_outcovers", qr)
print("calibration_reverse_minority", delta)
print("calibration_O_I", O,I)
print("calibration_balanced_escape_first", balanced[0])
print("POS3_CANONICAL_Y_GATE_CHECK_PASS")
