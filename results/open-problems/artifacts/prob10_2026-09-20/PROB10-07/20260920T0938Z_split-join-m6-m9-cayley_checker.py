from fractions import Fraction
from itertools import combinations
from math import factorial,gcd
from collections import defaultdict
import sys

MS=[int(x) for x in sys.argv[1:]] if len(sys.argv)>1 else [6,7,8,9]

def canon_part(blocks):
    bs=[tuple(sorted(b)) for b in blocks if b]
    return tuple(sorted(bs,key=lambda b:(b[0],len(b),b)))
def all_partitions(n):
    parts=[((0,),)]
    for i in range(1,n):
        out=set()
        for p in parts:
            for j in range(len(p)):
                q=[list(b) for b in p];q[j].append(i);out.add(canon_part(q))
            out.add(canon_part(list(p)+[(i,)]))
        parts=sorted(out)
    return parts
def merge_block_indices(p,sel):
    if len(sel)<2:return p
    ss=set(sel);merged=set();rem=[]
    for i,b in enumerate(p):
        (merged.update(b) if i in ss else rem.append(set(b)))
    rem.append(merged);return canon_part(rem)
def transition_rows(parts,pidx,m,required_mask=0):
    req=[i for i in range(m) if (required_mask>>i)&1]; rows=[]
    for p in parts:
        bmap={v:bi for bi,b in enumerate(p) for v in b}; rb=[bmap[v] for v in req]
        if len(set(rb))!=len(rb):rows.append({});continue
        rs=set(rb);opt=[i for i in range(len(p)) if i not in rs];d=defaultdict(int)
        for sm in range(1<<len(opt)):
            sel=list(rs);w=1
            for j,bi in enumerate(opt):
                if (sm>>j)&1:sel.append(bi);w*=len(p[bi])
            q=p if len(sel)<2 else merge_block_indices(p,sel);d[pidx[q]]+=w
        rows.append(dict(d))
    return rows
def N_rows(M,b):
    out=[]
    for i,row in enumerate(M):
        r=dict(row);r[i]=r.get(i,0)-b
        if r.get(i)==0:r.pop(i,None)
        out.append(r)
    return out
def vec_mul(v,rows):
    out=[0]*len(v)
    for i,a in enumerate(v):
        if a:
            for j,c in rows[i].items():out[j]+=a*c
    return out
def mat_vec(rows,u):return [sum(c*u[j] for j,c in row.items()) for row in rows]
def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p
def padd(a,b):
    o=[Fraction(0)]*max(len(a),len(b))
    for i,x in enumerate(a):o[i]+=x
    for i,x in enumerate(b):o[i]+=x
    return trim(o)
def psub(a,b):return padd(a,[-x for x in b])
def pmul(a,b):
    o=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):o[i+j]+=x*y
    return trim(o)
def pscale(a,c):return trim([c*x for x in a])
def peval(a,x):
    s=Fraction(0)
    for c in reversed(a):s=s*x+c
    return s
def binom_poly(j):
    p=[Fraction(1)]
    for r in range(j):p=pmul(p,[Fraction(-r),Fraction(1)])
    return pscale(p,Fraction(1,factorial(j)))
def primitive(poly):
    den=1
    for c in poly:den=den*c.denominator//gcd(den,c.denominator)
    ints=[int(c*den) for c in poly];g=0
    for z in ints:g=gcd(g,abs(z))
    if g>1:ints=[z//g for z in ints];den//=g
    return den,ints

def orbit_reps(m):
    r0=m;r1=m+1
    return [((0,1),(0,2)),((0,1),(2,3)),((0,1),(0,r0)),((0,1),(2,r0)),((0,r0),(1,r0)),((0,r0),(0,r1)),((0,r0),(1,r1))]

def tree_count_containing_forest(block, req):
    B=set(block); edges=[e for e in req if e[0] in B and e[1] in B]
    q=len(B)
    if q==1:return 1
    par={v:v for v in B}
    def find(x):
        while par[x]!=x:
            par[x]=par[par[x]];x=par[x]
        return x
    for u,v in edges:
        ru,rv=find(u),find(v)
        if ru==rv:return 0
        par[rv]=ru
    comps=defaultdict(int)
    for v in B:comps[find(v)]+=1
    c=len(comps);prod=1
    for s in comps.values():prod*=s
    if c>=2:return (q**(c-2))*prod
    return prod//q

def core_vector_formula(m,req,parts):
    out=[]
    for p in parts:
        bmap={v:bi for bi,b in enumerate(p) for v in b}
        if any(bmap[u]!=bmap[v] for u,v in req):out.append(0);continue
        z=1
        for B in p:z*=tree_count_containing_forest(B,req)
        out.append(z)
    return out

def enumerate_core_vectors(m,reqs,parts,pidx):
    E=list(combinations(range(m),2));eidx={e:i for i,e in enumerate(E)}
    rms={r:sum(1<<eidx[e] for e in r) for r in reqs};vecs={r:[0]*len(parts) for r in reqs};total=0
    for mask in range(1<<len(E)):
        par=list(range(m))
        def find(x):
            while par[x]!=x:
                par[x]=par[par[x]];x=par[x]
            return x
        ok=True
        for j,(u,v) in enumerate(E):
            if (mask>>j)&1:
                ru,rv=find(u),find(v)
                if ru==rv:ok=False;break
                par[rv]=ru
        if not ok:continue
        total+=1;groups={}
        for t in range(m):groups.setdefault(find(t),[]).append(t)
        pi=pidx[canon_part(groups.values())]
        for r,rm in rms.items():
            if (mask&rm)==rm:vecs[r][pi]+=1
    return vecs,total

def brute_small():
    m,n=3,2;V=m+n;E=list(combinations(range(m),2))+[(i,r) for r in range(m,m+n) for i in range(m)]
    Z=0;Ze=[0]*len(E);Zef=defaultdict(int)
    for mask in range(1<<len(E)):
        par=list(range(V))
        def find(x):
            while par[x]!=x:
                par[x]=par[par[x]];x=par[x]
            return x
        chosen=[];ok=True
        for j,(u,v) in enumerate(E):
            if (mask>>j)&1:
                ru,rv=find(u),find(v)
                if ru==rv:ok=False;break
                par[rv]=ru;chosen.append(j)
        if not ok:continue
        Z+=1
        for i in chosen:Ze[i]+=1
        for i,j in combinations(chosen,2):Zef[(i,j)]+=1
    ds=[Ze[i]*Ze[j]-Z*Zef[(i,j)] for i,j in combinations(range(len(E)),2)]
    assert min(ds)>0
    return len(E),Z,len(ds),min(ds)

def run_m(m):
    base=m+1;parts=all_partitions(m);pidx={p:i for i,p in enumerate(parts)}
    M=transition_rows(parts,pidx,m,0);N=N_rows(M,base)
    U=[[1]*len(parts)]
    for j in range(1,m+1):U.append(mat_vec(N,U[-1]))
    assert any(U[m-1]) and not any(U[m])
    reps=orbit_reps(m);forced={0};reqs=set()
    for rep in reps:
        e,f=rep
        for cond in [set(),{e},{f},{e,f}]:
            reqs.add(frozenset(ed for ed in cond if ed[1]<m))
            for rv in sorted({v for ed in cond for v in ed if v>=m}):
                rm=0
                for ed in cond:
                    if rv in ed:
                        t=ed[0] if ed[1]==rv else ed[1];rm|=1<<t
                forced.add(rm)
    cvecs={req:core_vector_formula(m,req,parts) for req in reqs}
    if m==6:
        enum,total_enum=enumerate_core_vectors(m,reqs,parts,pidx)
        assert total_enum==sum(cvecs[frozenset()])
        assert all(enum[r]==cvecs[r] for r in reqs)
        print(f'CORE_CAYLEY_FORMULA_ENUM_CROSSCHECK m=6 forests={total_enum} reqsets={len(reqs)} PASS')
    T={0:M}
    for rm in forced:
        if rm:T[rm]=transition_rows(parts,pidx,m,rm)
    binoms=[binom_poly(j) for j in range(m)]
    def cp(v):
        o=[Fraction(0)]
        for j in range(m):
            s=sum(a*b for a,b in zip(v,U[j]))
            if s:o=padd(o,pscale(binoms[j],Fraction(s,base**j)))
        return o
    def iv(core,edges):
        v=core[:]
        for rv in sorted({z for ed in edges for z in ed if z>=m}):
            rm=0
            for ed in edges:
                if rv in ed:
                    t=ed[0] if ed[1]==rv else ed[1];rm|=1<<t
            v=vec_mul(v,T[rm])
        return v
    infos=[]
    for rep in reps:
        e,f=rep;k=len({v for ed in rep for v in ed if v>=m});P={}
        for tag,cond in [('0',set()),('e',{e}),('f',{f}),('ef',{e,f})]:
            creq=frozenset(ed for ed in cond if ed[1]<m);P[tag]=cp(iv(cvecs[creq],cond))
        R=psub(pmul(P['e'],P['f']),pmul(P['0'],P['ef']));den,ints=primitive(R);first=1 if k==0 else 0;val=peval(R,first)
        assert min(ints)>=0 and val>0,(m,rep,ints,val)
        infos.append((rep,k,den,ints,val))
    total=sum(cvecs[frozenset()])
    return parts,total,infos

print('PROB10-07 complete split K_m join independent_n certificate via Cayley core vectors')
print('scope=uniform measure on ALL forests; exact Fraction arithmetic')
for m in MS:
    parts,core,infos=run_m(m)
    print(f'M={m} Bell={len(parts)} core_forests={core} orbits={len(infos)} ALL_N_EXACT_PASS')
    for i,(rep,k,den,ints,val) in enumerate(infos,1):
        print(f' ORBIT {i} rep={rep} k={k} den={den} degree={len(ints)-1} min_coeff={min(ints)} first_physical={val} coeffs={ints}')
b=brute_small();assert b==(9,198,36,124)
print(f'DIRECT_BRUTE K3_JOIN_I2 edges={b[0]} forests={b[1]} pairs={b[2]} min_delta={b[3]} ALL_PAIR_PASS')
print('PROB10_07_SPLIT_JOIN_M6_M9_EXACT_PASS')
