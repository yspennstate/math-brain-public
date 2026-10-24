from itertools import combinations, product, permutations
from functools import lru_cache
import collections, sympy as sp

def canon(labels):
    mp={}; out=[]; nxt=0
    for a in labels:
        if a not in mp: mp[a]=nxt; nxt+=1
        out.append(mp[a])
    return tuple(out)
TERMINAL_STATES=[canon((0,1,2)),canon((0,1,1)),canon((0,0,1)),canon((0,1,0)),canon((0,0,0))]
def union_part(labels,a,b):
    labels=list(labels)
    if labels[a]==labels[b]: return None
    la,lb=labels[a],labels[b]
    return canon([la if q==lb else q for q in labels])
def introduce(labels): return canon(tuple(labels)+(max(labels,default=-1)+1,))
def forget(labels,idx): return canon(tuple(q for i,q in enumerate(labels) if i!=idx))

@lru_cache(None)
def transfer_path(length, required_tuple=()):
    req=set(required_tuple); M=[[0]*5 for _ in range(5)]
    for si,tstate in enumerate(TERMINAL_STATES):
        dp={introduce(tstate):1}
        stage=[(('s',0,t),t,3) for t in range(3)]
        nd=collections.defaultdict(int)
        for lab,cnt in dp.items():
            for bits in product([0,1],repeat=3):
                if any(eid in req and not bit for bit,(eid,_,__) in zip(bits,stage)): continue
                cur=lab; ok=True
                for bit,(eid,a,b) in zip(bits,stage):
                    if bit:
                        cur2=union_part(cur,a,b)
                        if cur2 is None: ok=False; break
                        cur=cur2
                if ok: nd[cur]+=cnt
        dp=nd
        for i in range(1,length):
            nd=collections.defaultdict(int)
            stage=[(('i',i-1,i),3,4)]+[(('s',i,t),t,4) for t in range(3)]
            for lab,cnt in dp.items():
                lab2=introduce(lab)
                for bits in product([0,1],repeat=4):
                    if any(eid in req and not bit for bit,(eid,_,__) in zip(bits,stage)): continue
                    cur=lab2; ok=True
                    for bit,(eid,a,b) in zip(bits,stage):
                        if bit:
                            cur2=union_part(cur,a,b)
                            if cur2 is None: ok=False; break
                            cur=cur2
                    if ok: nd[forget(cur,3)]+=cnt
            dp=nd
        for lab,cnt in dp.items():
            M[si][TERMINAL_STATES.index(forget(lab,3))]+=cnt
    return sp.Matrix(M)

S=transfer_path(1); N=S-4*sp.eye(5); assert N**3==sp.zeros(5)
one=sp.ones(5,1); q=sp.Matrix([[1,0,0,0,0]])
u,v,y=sp.symbols('u v y', nonnegative=True)

def edges_L(L):
    return [('s',i,t) for i in range(L) for t in range(3)] + [('i',i,i+1) for i in range(L-1)]

def transform_edge(e,L,perm,rev):
    k,a,b=e
    if k=='s':
        i=L-1-a if rev else a
        return ('s',i,perm[b])
    else:
        i,j=a,b
        if rev: i,j=L-1-j,L-1-i
        return ('i',i,j)

def same_orbit_key(pair,L):
    vals=[]
    for perm in permutations(range(3)):
      for rev in [0,1]:
        tr=sorted([transform_edge(e,L,perm,rev) for e in pair], key=repr)
        vals.append(tuple(tr))
    return min(vals,key=repr)

def cross_orbit_key(e,L,f,M):
    vals=[]
    for perm in permutations(range(3)):
      for r1 in [0,1]:
       for r2 in [0,1]:
        a=transform_edge(e,L,perm,r1); b=transform_edge(f,M,perm,r2)
        if L<M:
            vals.append(((L,a),(M,b)))
        elif L>M:
            vals.append(((M,b),(L,a)))
        else:
            vals.append(tuple(sorted(((L,a),(L,b)), key=repr)))
    return min(vals,key=repr)

def get_reps(maxL):
    reps=[]
    # same comp
    for L in range(1,maxL+1):
      seen={}
      for pair in combinations(edges_L(L),2):
        key=same_orbit_key(pair,L)
        if key not in seen: seen[key]=pair
      reps += [('same',L,L,pair[0],pair[1]) for pair in seen.values()]
    # cross comps, including same length distinct copies
    for L in range(1,maxL+1):
      for M in range(L,maxL+1):
        seen={}
        for e in edges_L(L):
          for f in edges_L(M):
            key=cross_orbit_key(e,L,f,M)
            if key not in seen: seen[key]=(e,f)
        reps += [('cross',L,M,e,f) for e,f in seen.values()]
    return reps

def quantity_coeffs(rep, required_mask):
    typ,L,M,e,f=rep
    row=q
    if typ=='same':
        req=[]
        if required_mask&1: req.append(e)
        if required_mask&2: req.append(f)
        T=transfer_path(L,tuple(sorted(req,key=repr))) if req else transfer_path(L)
        row=row*T
    else:
        req1=(e,) if required_mask&1 else ()
        req2=(f,) if required_mask&2 else ()
        T1=transfer_path(L,tuple(req1)) if req1 else transfer_path(L)
        T2=transfer_path(M,tuple(req2)) if req2 else transfer_path(M)
        row=row*T1*T2
    return (sp.Integer((row*one)[0]),sp.Integer((row*N*one)[0]),sp.Integer((row*N**2*one)[0]))
def affine(c): return c[0]+c[1]*u+c[2]*v
def rayleigh(rep):
    I=affine(quantity_coeffs(rep,0)); Ie=affine(quantity_coeffs(rep,1)); If=affine(quantity_coeffs(rep,2)); Ief=affine(quantity_coeffs(rep,3))
    return sp.Poly(sp.expand(Ie*If-I*Ief),u,v,domain=sp.QQ)
def desc(rep):
    typ,L,M,e,f=rep
    return f'{typ} P{L}:{e} P{M}:{f}'
def bern2(poly):
    p=sp.Poly(sp.expand(poly),y,domain=sp.QQ); assert p.degree()<=2
    c0=p.coeff_monomial(1); c1=p.coeff_monomial(y); c2=p.coeff_monomial(y**2)
    return [sp.factor(c0),sp.factor(c0+c1/2),sp.factor(c0+c1+c2)]

def run(maxL):
    ABC={}; rhos={}
    for L in range(1,maxL+1):
        M=transfer_path(L); A=sp.Integer(M[0,0]); B=sp.Integer(M[0,1]); C=sp.Rational(M[0,4]-B,6)
        assert M==A*sp.eye(5)+B*N+C*N**2
        ABC[L]=(A,B,C)
        a=sp.Rational(B,A); c=sp.Rational(C,A); rhos[L]=sp.factor((a*a/2-c)/a)
    print('ABC last',maxL,ABC[maxL],'rho',rhos[maxL])
    print('rho monotone',all(rhos[L]>rhos[L+1]>0 for L in range(1,maxL)))
    rho_min=min(rhos.values()); rho_max=max(rhos.values())
    h=rho_min+y*(rho_max-rho_min); vstrip=u**2/2-h*u
    reps=get_reps(maxL); print('reps',len(reps))
    unique={}
    for idx,rep in enumerate(reps):
        P=rayleigh(rep); key=tuple(P.terms())
        if key not in unique: unique[key]=(rep,P)
        if idx%100==0: print('i',idx,'unique',len(unique), flush=True)
    print('unique',len(unique))
    reg=0; exc=[]; fail=[]
    for rep,P in unique.values():
        R=sp.Poly(sp.expand(P.as_expr().subs(v,vstrip)),u,y,domain=sp.QQ)
        Pu=sp.Poly(R.as_expr(),u,domain=sp.QQ[y]); bs=[]
        for i in range(5):
            ri=sp.expand(Pu.coeff_monomial(u**i))
            if ri!=0: bs.extend(bern2(ri))
        const=sp.factor(R.as_expr().subs({u:0,y:0}))
        if all(b>=0 for b in bs) and const>=0 and (const>0 or all(b>=0 for b in bs)):
            # const zero allowed only if all positive for u>0 to inspect later
            if const>0: reg+=1
            else: exc.append((rep,P,R,'zero-const'))
        else: exc.append((rep,P,R,'bern-fail'))
    print('reg positive const',reg,'exc',len(exc))
    # certify exceptions by quartic discriminant pattern or positive-u coefficients for zero const
    cert=0
    for rep,P,R,kind in exc:
        Pu=sp.Poly(R.as_expr(),u,domain=sp.QQ[y]); cs=[sp.factor(Pu.coeff_monomial(u**i)) for i in range(5)]
        ok=False; reason=''
        if cs[0]==0:
            # require every coefficient u^i i>=1 Bernstein nonnegative and some positive so R>=0; strict u>0 if c1 positive
            allb=[]
            for i in range(1,5):
                if cs[i]!=0: allb+=bern2(cs[i])
            if all(b>=0 for b in allb) and all(b>0 for b in bern2(cs[1])):
                ok=True; reason='zero-const-positive-coeffs'
        if not ok and cs[4]>0 and cs[3]!=0:
            # require c2,c1,c0 positive on strip; c3 negative; discr 4c4c2-c3^2 >0
            cond=[]
            for i in [0,1,2]:
                cond += bern2(cs[i])
            c3b=bern2(-cs[3])
            D=sp.factor(4*cs[4]*cs[2]-cs[3]**2)
            Db=bern2(D) if sp.Poly(D,y).degree()<=2 else []
            if all(b>0 for b in cond) and all(b>0 for b in c3b) and Db and all(b>0 for b in Db):
                ok=True; reason=f'disc D={D}'
        if ok: cert+=1
        else:
            fail.append((rep,P,R,cs)); reason='FAIL'
        print('EXC',desc(rep),kind,reason)
    print('cert',cert,'fail',len(fail))
    for rep,P,R,cs in fail:
        print('FAILREP',desc(rep)); print('P',P.as_expr()); print('R',R.as_expr())
    return ABC,rhos,reps,unique,exc,fail

if __name__=='__main__':
    import sys
    run(int(sys.argv[1]) if len(sys.argv)>1 else 7)
