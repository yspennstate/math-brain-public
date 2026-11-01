#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
from collections import defaultdict
from math import factorial, gcd
import hashlib

MS=(4,5)

# ---------- partitions ----------
def canon_part(blocks):
    bs=[tuple(sorted(b)) for b in blocks if b]
    return tuple(sorted(bs,key=lambda b:(b[0],len(b),b)))

def all_partitions(n):
    parts=[((0,),)]
    for i in range(1,n):
        out=set()
        for p in parts:
            for j in range(len(p)):
                q=[list(b) for b in p]
                q[j].append(i)
                out.add(canon_part(q))
            out.add(canon_part(list(p)+[(i,)]))
        parts=sorted(out)
    return parts

# sparse matrix: list of row dictionaries

def zero_mat(n): return [dict() for _ in range(n)]

def eye_mat(n): return [{i:1} for i in range(n)]

def mat_add(A,B,ca=1,cb=1):
    n=len(A); C=zero_mat(n)
    for i in range(n):
        d=defaultdict(int)
        for j,v in A[i].items(): d[j]+=ca*v
        for j,v in B[i].items(): d[j]+=cb*v
        C[i]={j:v for j,v in d.items() if v}
    return C

def mat_mul(A,B):
    n=len(A); C=zero_mat(n)
    for i,row in enumerate(A):
        d=defaultdict(int)
        for j,a in row.items():
            for k,b in B[j].items(): d[k]+=a*b
        C[i]={k:v for k,v in d.items() if v}
    return C

def mat_eq(A,B): return A==B

def mat_zero(A): return all(not r for r in A)

def mat_pow(A,e):
    n=len(A); R=eye_mat(n); B=A
    while e:
        if e&1:R=mat_mul(R,B)
        e//=2
        if e:B=mat_mul(B,B)
    return R

def mat_diag(A): return [A[i].get(i,0) for i in range(len(A))]

def row_vec_mul(v,A):
    d=defaultdict(int)
    for i,a in v.items():
        for j,b in A[i].items():d[j]+=a*b
    return {j:z for j,z in d.items() if z}

def row_sum(v): return sum(v.values())

def scalar_d_T_A_1(discrete_idx,T,A):
    v={discrete_idx:1}
    v=row_vec_mul(v,T)
    v=row_vec_mul(v,A)
    return row_sum(v)

# ---------- transfer construction ----------
def layer_transfer(m, internal_n, edges, required=()):
    parts=all_partitions(m); pidx={p:i for i,p in enumerate(parts)}
    n=len(parts); M=zero_mat(n)
    eidx={e:i for i,e in enumerate(edges)}
    reqidx=[eidx[e] for e in required]
    for ii,p in enumerate(parts):
        for mask in range(1<<len(edges)):
            if any(((mask>>j)&1)==0 for j in reqidx): continue
            par=list(range(m+internal_n))
            def find(x):
                while par[x]!=x:
                    par[x]=par[par[x]];x=par[x]
                return x
            def union(a,b):
                a,b=find(a),find(b)
                if a==b:return False
                par[b]=a;return True
            ok=True
            for block in p:
                root=block[0]
                for v in block[1:]:
                    if not union(root,v): raise AssertionError
            for j,(u,v) in enumerate(edges):
                if (mask>>j)&1:
                    if not union(u,v):
                        ok=False;break
            if not ok: continue
            groups={}
            for t in range(m): groups.setdefault(find(t),[]).append(t)
            q=canon_part(groups.values())
            jj=pidx[q]
            M[ii][jj]=M[ii].get(jj,0)+1
    return parts,M

def build_transfers(m):
    star_edges=tuple(tuple(sorted((m,t))) for t in range(m))
    pair_edges=tuple([tuple(sorted((m,t))) for t in range(m)] +
                     [tuple(sorted((m+1,t))) for t in range(m)] + [(m,m+1)])
    parts,S=layer_transfer(m,1,star_edges)
    _,P=layer_transfer(m,2,pair_edges)
    cacheS={():S}; cacheP={():P}
    def Sreq(terms):
        key=tuple(sorted(terms))
        if key not in cacheS:
            req=tuple(tuple(sorted((m,t))) for t in key)
            cacheS[key]=layer_transfer(m,1,star_edges,req)[1]
        return cacheS[key]
    def Preq(specs):
        key=tuple(sorted(specs))
        if key not in cacheP:
            req=[]
            for z in key:
                if z[0]=='h': req.append((m,m+1))
                elif z[0]=='p': req.append(tuple(sorted((m,z[1]))))
                elif z[0]=='q': req.append(tuple(sorted((m+1,z[1]))))
                else: raise ValueError(z)
            cacheP[key]=layer_transfer(m,2,pair_edges,tuple(req))[1]
        return cacheP[key]
    return parts,S,P,Sreq,Preq

# ---------- exact polynomial arithmetic in x,y ----------
# poly dict (i,j) -> Fraction for x^i y^j

def pclean(p): return {k:v for k,v in p.items() if v}
def padd(a,b,sgn=1):
    d=defaultdict(Fraction); d.update(a)
    for k,v in b.items(): d[k]+=sgn*v
    return pclean(d)
def pmul(a,b):
    d=defaultdict(Fraction)
    for (i,j),u in a.items():
        for (k,l),v in b.items():d[(i+k,j+l)]+=u*v
    return pclean(d)
def pscale(a,c): return pclean({k:c*v for k,v in a.items()})
def peval(a,x,y): return sum(c*(x**i)*(y**j) for (i,j),c in a.items())

def binom_poly_1d(n,var):
    # dict degree -> Fraction for binom(var,n)
    p={0:Fraction(1)}
    for r in range(n):
        q=defaultdict(Fraction)
        for d,c in p.items():
            q[d]+=c*(-r);q[d+1]+=c
        p=dict(q)
    fac=factorial(n)
    return {d:c/Fraction(fac) for d,c in p.items()}

def tensor_binom(i,j):
    px=binom_poly_1d(i,'x'); py=binom_poly_1d(j,'y')
    return {(a,b):cx*cy for a,cx in px.items() for b,cy in py.items()}

def primitive_poly(p):
    den=1
    for c in p.values(): den=den*c.denominator//gcd(den,c.denominator)
    ints={k:int(c*den) for k,c in p.items()}
    g=0
    for z in ints.values(): g=gcd(g,abs(z))
    if g==0:return Fraction(0),{}
    ints={k:z//g for k,z in ints.items()}
    return Fraction(g,den),ints

# ---------- span obstruction ----------
def rank_fraction(rows):
    A=[[Fraction(x) for x in row] for row in rows]
    if not A:return 0
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None:continue
        A[r],A[piv]=A[piv],A[r]
        z=A[r][c];A[r]=[u/z for u in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c];A[i]=[u-z*v for u,v in zip(A[i],A[r])]
        r+=1
        if r==m:break
    return r

def flatten(A):
    n=len(A); out=[]
    for i in range(n):
        for j in range(n):out.append(A[i].get(j,0))
    return out

def in_span(target,basis):
    cols=[flatten(B) for B in basis]; t=flatten(target)
    rows=[list(vals) for vals in zip(*cols)]
    rows_aug=[r+[tt] for r,tt in zip(rows,t)]
    return rank_fraction(rows)==rank_fraction(rows_aug)

# ---------- orbit specification ----------
def orbit_specs(m,S,P,Sreq,Preq):
    Sa=Sreq((0,)); Sb=Sreq((1,)); Sab=Sreq((0,1))
    Ph=Preq((('h',0),))
    Pp0=Preq((('p',0),)); Pp1=Preq((('p',1),))
    Pq0=Preq((('q',0),)); Pq1=Preq((('q',1),))
    Ph_p0=Preq((('h',0),('p',0)))
    Pp0p1=Preq((('p',0),('p',1)))
    Pp0q0=Preq((('p',0),('q',0)))
    Pp0q1=Preq((('p',0),('q',1)))
    return [
      ('OO_same_layer_diff_terminal',0,1,S,Sa,Sb,Sab),
      ('OO_diff_layer_same_terminal',0,2,mat_mul(S,S),mat_mul(Sa,S),mat_mul(S,Sa),mat_mul(Sa,Sa)),
      ('OO_diff_layer_diff_terminal',0,2,mat_mul(S,S),mat_mul(Sa,S),mat_mul(S,Sb),mat_mul(Sa,Sb)),
      ('hM_same_layer',1,0,P,Ph,Pp0,Ph_p0),
      ('MM_same_endpoint_diff_terminal',1,0,P,Pp0,Pp1,Pp0p1),
      ('MM_opposite_endpoint_same_terminal',1,0,P,Pp0,Pq0,Pp0q0),
      ('MM_opposite_endpoint_diff_terminal',1,0,P,Pp0,Pq1,Pp0q1),
      ('hh_diff_layer',2,0,mat_mul(P,P),mat_mul(Ph,P),mat_mul(P,Ph),mat_mul(Ph,Ph)),
      ('hM_diff_layer',2,0,mat_mul(P,P),mat_mul(Ph,P),mat_mul(P,Pp0),mat_mul(Ph,Pp0)),
      ('MM_diff_layer_same_terminal',2,0,mat_mul(P,P),mat_mul(Pp0,P),mat_mul(P,Pp0),mat_mul(Pp0,Pp0)),
      ('MM_diff_layer_diff_terminal',2,0,mat_mul(P,P),mat_mul(Pp0,P),mat_mul(P,Pp1),mat_mul(Pp0,Pp1)),
      ('hO',1,1,mat_mul(P,S),mat_mul(Ph,S),mat_mul(P,Sa),mat_mul(Ph,Sa)),
      ('MO_same_terminal',1,1,mat_mul(P,S),mat_mul(Pp0,S),mat_mul(P,Sa),mat_mul(Pp0,Sa)),
      ('MO_diff_terminal',1,1,mat_mul(P,S),mat_mul(Pp0,S),mat_mul(P,Sb),mat_mul(Pp0,Sb)),
    ]

def count_poly(m,disc,T,Qpowers,Npowers,lam,mu):
    p={}
    for i in range(m):
        for j in range(m-i):
            A=mat_mul(Qpowers[i],Npowers[j])
            c=scalar_d_T_A_1(disc,T,A)
            if c:
                term=pscale(tensor_binom(i,j),Fraction(c, (lam**i)*(mu**j)))
                p=padd(p,term)
    return p

def family_certificate(m):
    parts,S,P,Sreq,Preq=build_transfers(m)
    n=len(parts); I=eye_mat(n)
    mu=m+1; lam=m*m+4*m+2
    assert len(set(mat_diag(S)))==1 and mat_diag(S)[0]==mu
    assert len(set(mat_diag(P)))==1 and mat_diag(P)[0]==lam
    assert mat_eq(mat_mul(S,P),mat_mul(P,S))
    N=mat_add(S,I,1,-mu);Q=mat_add(P,I,1,-lam)
    assert mat_eq(mat_mul(N,Q),mat_mul(Q,N))
    Npowers=[eye_mat(n)];Qpowers=[eye_mat(n)]
    for i in range(1,m+1):
        Npowers.append(mat_mul(Npowers[-1],N));Qpowers.append(mat_mul(Qpowers[-1],Q))
    assert mat_zero(Npowers[m]) and mat_zero(Qpowers[m])
    for i in range(m+1):
        for j in range(max(0,m-i),m+1):
            if i+j>=m:
                assert mat_zero(mat_mul(Qpowers[i],Npowers[j]))
    # exact obstruction to the old one-generator matched-layer algebra
    basis=[eye_mat(n)]+[Npowers[i] for i in range(1,m)]
    onegen=in_span(P,basis)
    assert not onegen
    # marked/unmarked commutation for all marked matrices actually used
    specs=orbit_specs(m,S,P,Sreq,Preq)
    seen=[]
    for _,_,_,T0,Te,Tf,Tef in specs:
        seen += [T0,Te,Tf,Tef]
    # deduplicate by repr-ish flatten tuple
    uniq={tuple(flatten(T)):T for T in seen}.values()
    for T in uniq:
        assert mat_eq(mat_mul(T,S),mat_mul(S,T))
        assert mat_eq(mat_mul(T,P),mat_mul(P,T))
    disc=parts.index(canon_part([(i,) for i in range(m)]))
    infos=[]
    for name,a,b,T0,Te,Tf,Tef in specs:
        C0=count_poly(m,disc,T0,Qpowers,Npowers,lam,mu)
        Ce=count_poly(m,disc,Te,Qpowers,Npowers,lam,mu)
        Cf=count_poly(m,disc,Tf,Qpowers,Npowers,lam,mu)
        Cef=count_poly(m,disc,Tef,Qpowers,Npowers,lam,mu)
        R=padd(pmul(Ce,Cf),pmul(C0,Cef),-1)
        # all present coefficients must be positive; missing monomials are zeros
        assert R and all(c>0 for c in R.values()),(m,name,R)
        firstx=1 if a==0 else 0
        first=peval(R,firstx,0)
        assert first>0,(m,name,first)
        scale,ints=primitive_poly(R)
        assert scale>0 and all(z>0 for z in ints.values())
        terms=';'.join(f'{i},{j}:{ints[(i,j)]}' for i,j in sorted(ints))
        digest=hashlib.sha256(terms.encode()).hexdigest()
        infos.append((name,a,b,max(i+j for i,j in ints),len(ints),scale,first,digest,terms))
    return len(parts),mu,lam,infos

# ---------- actual graph and brute-force regression ----------
def graph_edges(m,k,r):
    right=list(range(m,m+2*k+r))
    E=[]
    for u in range(m):
        for v in right:E.append((u,v))
    for j in range(k): E.append((m+2*j,m+2*j+1))
    return E

def brute_all_pairs(m,k,r):
    E=graph_edges(m,k,r); V=m+2*k+r
    Z=0; Ze=[0]*len(E); Zef=defaultdict(int)
    for mask in range(1<<len(E)):
        par=list(range(V));chosen=[];ok=True
        def find(x):
            while par[x]!=x:
                par[x]=par[par[x]];x=par[x]
            return x
        for j,(u,v) in enumerate(E):
            if (mask>>j)&1:
                ru,rv=find(u),find(v)
                if ru==rv:ok=False;break
                par[rv]=ru;chosen.append(j)
        if not ok:continue
        Z+=1
        for i in chosen:Ze[i]+=1
        for i,j in combinations(chosen,2):Zef[(i,j)]+=1
    md=None;arg=None
    for i,j in combinations(range(len(E)),2):
        d=Ze[i]*Ze[j]-Z*Zef[(i,j)]
        assert d>0,(m,k,r,i,j,d)
        if md is None or d<md:md,arg=d,(i,j)
    return len(E),Z,len(E)*(len(E)-1)//2,md,arg

# classification completeness for a generic k=2,r=2 instance

def classify_pair(m,k,r,e,f):
    # right vertices m..m+2k-1 are paired; rest ordinary
    def desc(ed):
        u,v=ed
        if u>=m and v>=m:
            # matching h
            j=(u-m)//2
            return ('h',j,None,None)
        if u>=m: u,v=v,u
        # u terminal, v right
        if v < m+2*k:
            j=(v-m)//2; side=(v-m)%2
            return ('M',j,side,u)
        else:
            j=v-(m+2*k)
            return ('O',j,None,u)
    a,b=desc(e),desc(f)
    # sort h/M/O only where convenient
    if a[0]=='O' and b[0]=='O':
        if a[1]==b[1]: return 'OO_same_layer_diff_terminal'
        return 'OO_diff_layer_same_terminal' if a[3]==b[3] else 'OO_diff_layer_diff_terminal'
    if a[0] in ('h','M') and b[0] in ('h','M'):
        if a[1]==b[1]:
            if {a[0],b[0]}=={'h','M'}: return 'hM_same_layer'
            if a[0]==b[0]=='M':
                if a[2]==b[2]: return 'MM_same_endpoint_diff_terminal'
                return 'MM_opposite_endpoint_same_terminal' if a[3]==b[3] else 'MM_opposite_endpoint_diff_terminal'
            raise AssertionError((a,b))
        else:
            if a[0]==b[0]=='h': return 'hh_diff_layer'
            if 'h' in (a[0],b[0]): return 'hM_diff_layer'
            return 'MM_diff_layer_same_terminal' if a[3]==b[3] else 'MM_diff_layer_diff_terminal'
    # cross pair/O
    if a[0]=='O':a,b=b,a
    if a[0]=='h':return 'hO'
    if a[0]=='M':return 'MO_same_terminal' if a[3]==b[3] else 'MO_diff_terminal'
    raise AssertionError((a,b))

def orbit_completeness(m):
    k=r=2;E=graph_edges(m,k,r);counts=defaultdict(int)
    for e,f in combinations(E,2):counts[classify_pair(m,k,r,e,f)]+=1
    names={z[0] for z in orbit_specs(m,*build_transfers(m)[1:])}
    assert set(counts)==names and sum(counts.values())==len(E)*(len(E)-1)//2
    return dict(sorted(counts.items())),len(E)*(len(E)-1)//2

def main():
    print('PROB10-07 matched-biclique two-nilpotent exact certificate')
    print('scope=uniform measure on ALL forests of G_m(k,r)=K_{m,2k+r}+M_k; m=4,5; k>=1; r>=0')
    print('mechanism=P=lambda I+Q, S=(m+1)I+N, QN=NQ, total nilpotent degree < m')
    for m in MS:
        bell,mu,lam,infos=family_certificate(m)
        counts,npairs=orbit_completeness(m)
        print(f'WIDTH m={m} Bell={bell} star_diag={mu} pair_diag={lam} one_generator_P_in_QN=False orbit_templates={len(infos)} generic_pair_count={npairs}')
        print('GENERIC_ORBIT_MULTS',';'.join(f'{k}:{v}' for k,v in counts.items()))
        for name,a,b,deg,terms,scale,first,digest,termstr in infos:
            print(f'ORBIT m={m} name={name} distinguished_pair_layers={a} distinguished_single_layers={b} degree={deg} terms={terms} scale={scale.numerator}/{scale.denominator} first_physical={first.numerator}/{first.denominator} digest={digest}')
            print('COEFFS',termstr)
        print(f'WIDTH_{m}_ALL_PARAMETER_EXACT_PASS')
    for fam in [(4,1,0),(4,1,1),(5,1,0)]:
        e,z,p,d,arg=brute_all_pairs(*fam)
        print(f'DIRECT_BRUTE G_{fam[0]}({fam[1]},{fam[2]}) edges={e} forests={z} pairs={p} min_delta={d} arg={arg} ALL_PAIR_PASS')
    print('PROB10_07_MATCHED_BICLIQUE_M4_M5_EXACT_PASS')

if __name__=='__main__':main()
