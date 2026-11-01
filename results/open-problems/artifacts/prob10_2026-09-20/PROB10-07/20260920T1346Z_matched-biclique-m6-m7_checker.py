#!/usr/bin/env python3
from itertools import product
from fractions import Fraction
from math import gcd, factorial
from hashlib import sha256
from collections import defaultdict

WIDTHS=(6,7)


def rgs_partitions(n):
    out=[]
    def rec(a,mx):
        if len(a)==n:
            out.append(tuple(a)); return
        for v in range(mx+2):
            rec(a+[v], max(mx,v))
    rec([0],0)
    return out


def canonical_from_groups(old_part, merges):
    b=max(old_part)+1
    parent=list(range(b))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a!=b: parent[b]=a
    for grp in merges:
        grp=list(grp)
        if len(grp)>1:
            for z in grp[1:]: union(grp[0],z)
    lab={}; nxt=0; ans=[]
    for t in range(len(old_part)):
        r=find(old_part[t])
        if r not in lab: lab[r]=nxt; nxt+=1
        ans.append(lab[r])
    return tuple(ans)


def transfer_single(m, parts, pindex, forced_terms=()):
    rows=[]
    for part in parts:
        b=max(part)+1
        blocks=[[] for _ in range(b)]
        for t,c in enumerate(part): blocks[c].append(t)
        forced=[[] for _ in range(b)]
        for t in forced_terms: forced[part[t]].append(t)
        if any(len(q)>1 for q in forced):
            rows.append({}); continue
        must={i for i,q in enumerate(forced) if q}
        row=defaultdict(int)
        for mask in range(1<<b):
            if any(((mask>>i)&1)==0 for i in must): continue
            mult=1; sel=[]
            for i,B in enumerate(blocks):
                if (mask>>i)&1:
                    sel.append(i)
                    mult*=1 if forced[i] else len(B)
            np=canonical_from_groups(part,[sel])
            row[pindex[np]]+=mult
        rows.append(dict(row))
    return rows


def sort_forced(items):
    def key(x):
        if x=='h': return (-1,-1)
        return (0 if x[0]=='u' else 1, x[1])
    return tuple(sorted(items,key=key))


def transfer_pair(m, parts, pindex, forced=()):
    forced=sort_forced(forced)
    h_forced='h' in forced
    fu=[x[1] for x in forced if isinstance(x,tuple) and x[0]=='u']
    fv=[x[1] for x in forced if isinstance(x,tuple) and x[0]=='v']
    rows=[]
    for part in parts:
        b=max(part)+1
        blocks=[[] for _ in range(b)]
        for t,c in enumerate(part): blocks[c].append(t)
        U=[[] for _ in range(b)]; V=[[] for _ in range(b)]
        for t in fu: U[part[t]].append(t)
        for t in fv: V[part[t]].append(t)
        if any(len(q)>1 for q in U) or any(len(q)>1 for q in V):
            rows.append({}); continue
        row=defaultdict(int)
        for choices in product(range(4), repeat=b):
            good=True
            for i,c in enumerate(choices):
                if U[i] and c not in (1,3): good=False; break
                if V[i] and c not in (2,3): good=False; break
            if not good: continue
            shared=sum(c==3 for c in choices)
            mult=1; A=[]; B=[]
            for i,c in enumerate(choices):
                if c in (1,3):
                    A.append(i); mult*=1 if U[i] else len(blocks[i])
                if c in (2,3):
                    B.append(i); mult*=1 if V[i] else len(blocks[i])
            for h in ((1,) if h_forced else (0,1)):
                if h:
                    if shared: continue
                    merges=[list(set(A)|set(B))]
                else:
                    if shared>1: continue
                    merges=[list(set(A)|set(B))] if shared==1 else [A,B]
                np=canonical_from_groups(part,merges)
                row[pindex[np]]+=mult
        rows.append(dict(row))
    return rows


def apply_row(row,T):
    out=[0]*len(row)
    for i,a in enumerate(row):
        if a:
            for j,w in T[i].items(): out[j]+=a*w
    return out


def apply_col(T,col):
    out=[0]*len(col)
    for i,r in enumerate(T): out[i]=sum(w*col[j] for j,w in r.items())
    return out


def compose(A,B):
    out=[]
    for i in range(len(A)):
        r=defaultdict(int)
        for j,a in A[i].items():
            for k,b in B[j].items(): r[k]+=a*b
        out.append({k:v for k,v in r.items() if v})
    return out


def sub_scalar_I(T,c):
    out=[]
    for i,r in enumerate(T):
        q=dict(r); q[i]=q.get(i,0)-c
        if q.get(i)==0: q.pop(i,None)
        out.append(q)
    return out


def identity_sparse(n): return [{i:1} for i in range(n)]


def poly_add(A,B,scale=Fraction(1)):
    C=dict(A)
    for k,v in B.items():
        C[k]=C.get(k,Fraction(0))+scale*v
        if C[k]==0: del C[k]
    return C


def poly_mul(A,B):
    C=defaultdict(Fraction)
    for (i,j),a in A.items():
        for (p,q),b in B.items(): C[(i+p,j+q)]+=a*b
    return {k:v for k,v in C.items() if v}


def binom_coeff(n):
    c=[Fraction(1)]
    for t in range(n):
        d=[Fraction(0)]*(len(c)+1)
        for i,a in enumerate(c):
            d[i]+=-t*a; d[i+1]+=a
        c=d
    f=factorial(n)
    return [a/f for a in c]


def poly_eval(P,x,y): return sum(c*(x**i)*(y**j) for (i,j),c in P.items())


def primitive_digest(P):
    den=1
    def lcm(a,b): return a//gcd(a,b)*b
    for c in P.values(): den=lcm(den,c.denominator)
    ints={k:int(c*den) for k,c in P.items()}
    g=0
    for v in ints.values(): g=gcd(g,abs(v))
    if g: ints={k:v//g for k,v in ints.items()}
    payload=';'.join(f'{i},{j}:{ints[(i,j)]}' for i,j in sorted(ints))
    return den,g,sha256(payload.encode()).hexdigest()


ORBITS=[
("SS_same_layer_diff_terminal",[('S',[('e',0),('f',1)])]),
("SS_diff_layers_same_terminal",[('S',[('e',0)]),('S',[('f',0)])]),
("SS_diff_layers_diff_terminal",[('S',[('e',0)]),('S',[('f',1)])]),
("P_same_h_spoke",[('P',[('e','h'),('f',('u',0))])]),
("P_same_same_endpoint_diff_terminal",[('P',[('e',('u',0)),('f',('u',1))])]),
("P_same_opposite_same_terminal",[('P',[('e',('u',0)),('f',('v',0))])]),
("P_same_opposite_diff_terminal",[('P',[('e',('u',0)),('f',('v',1))])]),
("PP_diff_matching_matching",[('P',[('e','h')]),('P',[('f','h')])]),
("PP_diff_matching_spoke",[('P',[('e','h')]),('P',[('f',('u',0))])]),
("PP_diff_spokes_same_terminal",[('P',[('e',('u',0))]),('P',[('f',('u',0))])]),
("PP_diff_spokes_diff_terminal",[('P',[('e',('u',0))]),('P',[('f',('u',1))])]),
("PS_matching_ordinary",[('P',[('e','h')]),('S',[('f',0)])]),
("PS_spokes_same_terminal",[('P',[('e',('u',0))]),('S',[('f',0)])]),
("PS_spokes_diff_terminal",[('P',[('e',('u',0))]),('S',[('f',1)])]),
]


def classify_pair(edge1,edge2,k):
    a,b=edge1,edge2
    def side(e):
        if e[0]=='match': return ('P',e[1], 'h', None)
        _,t,r=e
        if r<2*k: return ('P',r//2, 'spoke', (r%2,t))
        return ('S',r-2*k,'spoke',(None,t))
    A,B=side(a),side(b)
    if A[0]=='S' and B[0]=='S':
        if A[1]==B[1]: return 'SS_same_layer_diff_terminal'
        return 'SS_diff_layers_same_terminal' if A[3][1]==B[3][1] else 'SS_diff_layers_diff_terminal'
    if A[0]=='S' or B[0]=='S':
        P,S=(B,A) if A[0]=='S' else (A,B)
        if P[2]=='h': return 'PS_matching_ordinary'
        return 'PS_spokes_same_terminal' if P[3][1]==S[3][1] else 'PS_spokes_diff_terminal'
    if A[1]==B[1]:
        if A[2]=='h' or B[2]=='h': return 'P_same_h_spoke'
        ea,ta=A[3]; eb,tb=B[3]
        if ea==eb: return 'P_same_same_endpoint_diff_terminal'
        return 'P_same_opposite_same_terminal' if ta==tb else 'P_same_opposite_diff_terminal'
    if A[2]=='h' and B[2]=='h': return 'PP_diff_matching_matching'
    if A[2]=='h' or B[2]=='h': return 'PP_diff_matching_spoke'
    return 'PP_diff_spokes_same_terminal' if A[3][1]==B[3][1] else 'PP_diff_spokes_diff_terminal'


def generic_orbit_check(m,k=2,r=2):
    edges=[]
    for t in range(m):
        for R in range(2*k+r): edges.append(('spoke',t,R))
    for q in range(k): edges.append(('match',q))
    cnt=defaultdict(int)
    for i in range(len(edges)):
        for j in range(i+1,len(edges)): cnt[classify_pair(edges[i],edges[j],k)]+=1
    assert set(cnt)=={name for name,_ in ORBITS}
    assert sum(cnt.values())==len(edges)*(len(edges)-1)//2
    return len(edges),sum(cnt.values()),dict(sorted(cnt.items()))


def certify_width(m):
    parts=rgs_partitions(m); pindex={p:i for i,p in enumerate(parts)}
    S=transfer_single(m,parts,pindex,()); P=transfer_pair(m,parts,pindex,())
    mu=m+1; lam=m*m+4*m+2
    assert {r.get(i,0) for i,r in enumerate(S)}=={mu}
    assert {r.get(i,0) for i,r in enumerate(P)}=={lam}
    N=sub_scalar_I(S,mu); Q=sub_scalar_I(P,lam)
    assert compose(N,Q)==compose(Q,N)
    NP=[identity_sparse(len(parts))]; QP=[identity_sparse(len(parts))]
    for _ in range(m):
        NP.append(compose(NP[-1],N)); QP.append(compose(QP[-1],Q))
    for i in range(m+1):
        for j in range(m+1):
            if i+j>=m: assert all(not r for r in compose(QP[i],NP[j]))

    scache={():S}; pcache={():P}
    def getT(kind,forced):
        if kind=='S':
            key=tuple(sorted(forced))
            if key not in scache: scache[key]=transfer_single(m,parts,pindex,key)
            return scache[key]
        key=sort_forced(forced)
        if key not in pcache: pcache[key]=transfer_pair(m,parts,pindex,key)
        return pcache[key]

    ones=[1]*len(parts); w={}; ncols=[ones]
    for _ in range(1,m): ncols.append(apply_col(N,ncols[-1]))
    for j in range(m):
        cur=ncols[j]; w[(0,j)]=cur
        for i in range(1,m-j):
            cur=apply_col(Q,cur); w[(i,j)]=cur
    bx=[binom_coeff(i) for i in range(m)]; by=[binom_coeff(i) for i in range(m)]
    start=pindex[tuple(range(m))]

    def row_for(layers,cond):
        row=[0]*len(parts); row[start]=1
        for kind,marks in layers:
            forced=[edge for mark,edge in marks if mark in cond]
            row=apply_row(row,getT(kind,forced))
        return row

    def response(layers,cond):
        row=row_for(layers,cond); R={}
        for (i,j),col in w.items():
            a=sum(u*v for u,v in zip(row,col))
            if not a: continue
            s=Fraction(a,lam**i*mu**j); term={}
            for dx,cx in enumerate(bx[i]):
                for dy,cy in enumerate(by[j]):
                    if cx and cy: term[(dx,dy)]=s*cx*cy
            R=poly_add(R,term)
        return R

    lines=[]
    for name,layers in ORBITS:
        C0=response(layers,set()); Ce=response(layers,{'e'}); Cf=response(layers,{'f'}); Cef=response(layers,{'e','f'})
        R=poly_add(poly_mul(Ce,Cf),poly_mul(C0,Cef),Fraction(-1))
        assert not [(ij,c) for ij,c in R.items() if c<0]
        deg=max(i+j for i,j in R)
        a=sum(kind=='P' for kind,_ in layers)
        xmin=1 if a==0 else 0
        first=poly_eval(R,xmin,0)
        assert first>0
        _,_,dig=primitive_digest(R)
        lines.append((name,deg,len(R),first,dig))
    ge,gp,gc=generic_orbit_check(m)
    return len(parts),mu,lam,ge,gp,gc,lines


def graph_matched(m,k,r):
    right=2*k+r; E=[]
    for t in range(m):
        for j in range(right): E.append((t,m+j,f'L{t}-R{j}'))
    for i in range(k): E.append((m+2*i,m+2*i+1,f'M{i}'))
    return m+right,E


def brute(m,k,r):
    n,E=graph_matched(m,k,r); q=len(E)
    Z=0; Ze=[0]*q; Zef=[[0]*q for _ in range(q)]
    for mask in range(1<<q):
        parent=list(range(n)); rank=[0]*n; inc=[]; ok=True
        def find(a):
            while parent[a]!=a:
                parent[a]=parent[parent[a]]; a=parent[a]
            return a
        for i,(u,v,_) in enumerate(E):
            if (mask>>i)&1:
                u,v=find(u),find(v)
                if u==v: ok=False; break
                if rank[u]<rank[v]: u,v=v,u
                parent[v]=u
                if rank[u]==rank[v]: rank[u]+=1
                inc.append(i)
        if not ok: continue
        Z+=1
        for i in inc: Ze[i]+=1
        for a in range(len(inc)):
            for b in range(a+1,len(inc)):
                i,j=inc[a],inc[b]; Zef[i][j]+=1; Zef[j][i]+=1
    best=None
    for i in range(q):
        for j in range(i+1,q):
            d=Ze[i]*Ze[j]-Z*Zef[i][j]
            if best is None or d<best[0]: best=(d,i,j)
    assert best[0]>0
    return q,Z,q*(q-1)//2,best[0],E[best[1]][2],E[best[2]][2]


def deletion_contraction_witness():
    m,k,r=6,1,1; n,E=graph_matched(m,k,r); q=len(E); g=m*(2*k+r)
    Z=[0,0]; Ze=[[0]*q for _ in range(2)]; Zef=[[[0]*q for _ in range(q)] for __ in range(2)]
    for mask in range(1<<q):
        parent=list(range(n)); rank=[0]*n; inc=[]; ok=True
        def find(a):
            while parent[a]!=a:
                parent[a]=parent[parent[a]]; a=parent[a]
            return a
        for i,(u,v,_) in enumerate(E):
            if (mask>>i)&1:
                u,v=find(u),find(v)
                if u==v: ok=False; break
                if rank[u]<rank[v]: u,v=v,u
                parent[v]=u
                if rank[u]==rank[v]: rank[u]+=1
                inc.append(i)
        if not ok: continue
        h=(mask>>g)&1; Z[h]+=1
        for i in inc:
            if i!=g: Ze[h][i]+=1
        L=[i for i in inc if i!=g]
        for a in range(len(L)):
            for b in range(a+1,len(L)):
                i,j=L[a],L[b]; Zef[h][i][j]+=1; Zef[h][j][i]+=1
    e,f=0,1; A,B=Z
    Ae,Af,Aef=Ze[0][e],Ze[0][f],Zef[0][e][f]
    Be,Bf,Bef=Ze[1][e],Ze[1][f],Zef[1][e][f]
    DA=Ae*Af-A*Aef; DB=Be*Bf-B*Bef
    Ee=B*Ae-A*Be; Ef=B*Af-A*Bf
    DG=(Ae+Be)*(Af+Bf)-(A+B)*(Aef+Bef)
    assert A*B*DG==B*(A+B)*DA+A*(A+B)*DB-Ee*Ef
    assert Ee*Ef>0 and DG>0
    return A,B,DA,DB,Ee,Ef,DG,E[e][2],E[f][2]


def main():
    print('PROB10-07 matched-biclique width-6/7 exact certificate')
    print('scope=uniform measure on ALL forests of G_m(k,r)=K_{m,2k+r}+M_k; m=6,7; k>=1; r>=0')
    print('mechanism=P=lambda I+Q, S=(m+1)I+N, QN=NQ, Q^i N^j=0 for i+j>=m')
    for m in WIDTHS:
        states,mu,lam,ge,gp,gc,lines=certify_width(m)
        print(f'WIDTH m={m} bell_states={states} mu={mu} lambda={lam} generic_edges={ge} generic_pairs={gp} orbit_types={len(gc)}')
        for name,deg,terms,first,dig in lines:
            print(f'ORBIT m={m} name={name} degree={deg} positive_terms={terms} first_physical={first} digest={dig}')
    for pars in ((6,1,0),(7,1,0),(6,1,1)):
        q,z,pairs,mind,e,f=brute(*pars)
        print(f'BRUTE m={pars[0]} k={pars[1]} r={pars[2]} edges={q} forests={z} pairs={pairs} minDelta={mind} arg={e},{f}')
    A,B,DA,DB,Ee,Ef,DG,e,f=deletion_contraction_witness()
    print(f'DC_WITNESS G6(1,1) g=M0 e={e} f={f} A={A} B={B} DeltaA={DA} DeltaB={DB} Ee={Ee} Ef={Ef} EeEf={Ee*Ef} DeltaG={DG}')
    print('PROB10_07_MATCHED_BICLIQUE_M6_M7_EXACT_PASS')

if __name__=='__main__': main()
