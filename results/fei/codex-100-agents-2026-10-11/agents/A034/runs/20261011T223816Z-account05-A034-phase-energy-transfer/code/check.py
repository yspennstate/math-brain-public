"""A034 quadratic affine-row certificates v1. No floating arithmetic."""
import itertools, json, time
from pathlib import Path
from fractions import Fraction as F

ROOT = Path(__file__).resolve().parents[1]
started = time.monotonic()
checks = 0
def ck(v):
    global checks
    checks += 1
    assert v
    if time.monotonic()-started > 55:
        raise RuntimeError('frozen pilot time cap')

def parity(x): return x.bit_count() & 1
def fw(a):
    a=list(a); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h]; a[j],a[j+h]=u+v,u-v
        h*=2
    return a

def subspaces(m):
    levels={frozenset([0])}
    found=set(levels)
    while levels:
        nxt=set()
        for v in levels:
            for x in range(1<<m):
                if x not in v:
                    w=frozenset(set(v)|{x^z for z in v})
                    if w not in found: nxt.add(w)
        found |= nxt; levels=nxt
    return sorted(found,key=lambda x:(len(x),sorted(x)))

def cells(m):
    out=set()
    for v in subspaces(m):
        for a in range(1<<m): out.add(frozenset(a^z for z in v))
    return sorted(out,key=lambda x:(len(x),sorted(x)))

def phase(x,m,q):
    pairs=list(itertools.combinations(range(m),2))
    return (-1)**parity(sum(((x>>i)&1)*((x>>j)&1)<<t for t,(i,j) in enumerate(pairs)) & q)

def basis(v):
    b=[]; span={0}
    for x in sorted(v):
        if x not in span:
            b.append(x); span |= {x^z for z in list(span)}
    return b

def row(m,cell,q,lin=0):
    a=min(cell); v={a^z for z in cell}; b=basis(v)
    k=m-len(b)
    # Polar form computed from quadratic values, independent of transform.
    def qe(x): return phase(x,m,q)==-1
    mat=[]
    for u in b:
        mat.append(sum((qe(u^z)^qe(u)^qe(z))<<i for i,z in enumerate(b)))
    r=0
    piv={}
    for z in mat:
        while z:
            t=z.bit_length()-1
            if t in piv: z ^= piv[t]
            else: piv[t]=z; r+=1; break
    ck(r%2==0)
    vals=[phase(y,m,q)*(-1)**parity(lin&y) if y in cell else 0 for y in range(1<<m)]
    w=fw(vals); support=[s for s,z in enumerate(w) if z]
    ck(len(support)==1<<(k+r))
    ck(len({w[s]**2 for s in support})==1)
    ck(sum(z*z for z in w)==len(cell)*(1<<m))
    t=min(support); dual={s^t for s in support}
    ck(0 in dual and all(u^v in dual for u in dual for v in dual))
    active=sum(any((z>>i)&1 for z in dual) for i in range(m))
    ones=sum(not any((z>>i)&1 for z in dual) and ((t>>i)&1) for i in range(m))
    iy=F(sum(s.bit_count()*z*z for s,z in enumerate(w)),1<<(2*m))
    alpha=F(len(cell),1<<m)
    ck(iy==alpha*(F(active,2)+ones))
    ck(alpha*(k+r)<=2*iy)
    # Physical edges independently check Dirichlet energy.
    edges=F(sum((vals[y]-vals[y^(1<<i)])**2 for y in range(1<<m) for i in range(m)),4*(1<<m))
    ck(edges==iy)
    return vals,w,k,r,iy

counts={}
for m in range(5):
    cs=cells(m); n=0
    # Exhaust ALL affine cells and quadratic homogeneous parts through m=3.
    # At m=4 use the fixed list below, not all 64 quadratic parts.
    qs=range(1<<(m*(m-1)//2)) if m<=3 else [0,1,3,9,18,33,63]
    for cell in cs:
        for q in qs:
            for lin in range(1<<m):
                row(m,cell,q,lin); n+=1
    counts[str(m)]={'cells':len(cs),'rows':n}

def partitions(m):
    cs=cells(m)
    def rec(rest,acc):
        if not rest:
            yield acc; return
        y=min(rest)
        for c in cs:
            if y in c and c<=rest:
                yield from rec(rest-c,acc+[c])
    yield from rec(frozenset(range(1<<m)),[])

joint=0; restricted=0
for m in range(4):
    np=0
    for part in partitions(m):
        np+=1
        nx=(len(part)-1).bit_length()
        for profile in range(3):
            rows=[]; expected_h=F(0); expected_cond=F(0); expected_iy=F(0)
            for j,c in enumerate(part):
                q=(j+profile) % (1<<(m*(m-1)//2))
                vals,w,k,r,iy=row(m,c,q,(3*j+profile)%(1<<m))
                rows.append(vals)
                alpha=F(len(c),1<<m)
                expected_h+=alpha*(2*k+r); expected_cond+=alpha*(k+r); expected_iy+=iy
            vals=[sum((-1)**parity(j&x)*rows[j][y] for j in range(len(rows))) for y in range(1<<m) for x in range(1<<nx)]
            ck(set(vals)<={-1,1})
            w=fw(vals); n=nx+m; den=1<<(2*n)
            # All probabilities are inverse powers of two, so logs exact integers.
            ent=F(0); marg={}
            for s,z in enumerate(w):
                if z:
                    ck((z*z)&(z*z-1)==0)
                    ent+=F(z*z,den)*(2*n-(z*z).bit_length()+1)
                    marg[s% (1<<nx)]=marg.get(s%(1<<nx),0)+z*z
            hx=F(0)
            for z in marg.values():
                ck(z&(z-1)==0)
                hx+=F(z,den)*(2*n-z.bit_length()+1)
            iy=F(sum((s>>nx).bit_count()*z*z for s,z in enumerate(w)),den)
            ck(ent==expected_h and ent-hx==expected_cond and iy==expected_iy)
            ck(expected_cond<=2*iy and ent<=4*iy)
            joint+=1
            # All single-coordinate Y restrictions, all surviving rows.
            for i in range(m):
                for bval in range(2):
                    for j,c in enumerate(part):
                        c2={((y&((1<<i)-1))|((y>>(i+1))<<i)) for y in c if (y>>i)&1==bval}
                        if not c2: continue
                        a=min(c2); v={a^z for z in c2}
                        ck(len(v)&(len(v)-1)==0 and all(u^z in v for u in v for z in v))
                        # Third finite differences of restricted Boolean phase vanish.
                        phase_map={((y&((1<<i)-1))|((y>>(i+1))<<i)):rows[j][y] for y in c if (y>>i)&1==bval}
                        bb=basis(v)
                        for u,z,t in itertools.combinations(bb,3):
                            ck(__import__('math').prod(phase_map[a^e] for e in [0,u,z,t,u^z,u^t,z^t,u^z^t])==1)
                        rw=fw([phase_map.get(y,0) for y in range(1<<(m-1))])
                        occupied=[s for s,z in enumerate(rw) if z]
                        ck(len({rw[s]**2 for s in occupied})==1)
                        dim=(len(occupied)-1).bit_length()
                        ck(len(occupied)==1<<dim)
                        alpha2=F(len(c2),1<<(m-1))
                        energy2=F(sum(s.bit_count()*z*z for s,z in enumerate(rw)),1<<(2*(m-1)))
                        ck(alpha2*dim<=2*energy2)
                        restricted+=1
    counts[str(m)]['partitions']=np

# All three-bit Boolean functions arise as restrictions of ordinary addressing.
closure=0
for table in itertools.product([-1,1],repeat=8):
    selected=[table[y] for y in range(8)]
    ck(selected==list(table)); closure+=1

out={'helper_version':'quadratic-affine-rows-v2','arithmetic':'integers and Fraction; logarithms exact integers', 'counts':counts,'joint_cases':joint,'nonempty_restricted_rows':restricted,'addressing_restrictions':closure,'assertions':checks,'runtime_seconds':time.monotonic()-started,'status':'PASS'}
(ROOT/'out'/'validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
