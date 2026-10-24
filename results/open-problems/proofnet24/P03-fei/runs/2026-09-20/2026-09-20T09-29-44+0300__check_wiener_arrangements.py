import itertools, math, random, json, sys

LOG2E = math.log2(math.e)

def fwht(vals):
    a=[float(x) for x in vals]
    n=len(a); h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x=a[j]; y=a[j+h]
                a[j]=x+y; a[j+h]=x-y
        h*=2
    return [x/n for x in a]

def metrics(vals):
    N=len(vals); n=N.bit_length()-1
    hat=fwht(vals)
    p=[x*x for x in hat]
    H=-sum(x*math.log2(x) for x in p if x>0)
    inf=[]
    B=[]
    for i in range(n):
        mask=1<<i
        inf.append(sum(vals[x]!=vals[x^mask] for x in range(N))/N)
        bi=0.0
        for s in range(N):
            if s & mask: continue
            a=p[s]; b=p[s|mask]; q=a+b
            if q>0 and a>0 and b>0:
                t=b/q
                bi += q*(-t*math.log2(t)-(1-t)*math.log2(1-t))
        B.append(bi)
    I=sum(inf)
    J=sum(min(x,1-x) for x in inf)
    L=sum(abs(x) for x in hat)
    C=max(4.0,2*LOG2E+4*math.log2(max(1.0,L)))
    return H,I,J,L,C,inf,B

def span_add(S,v):
    return frozenset(set(S)|{x^v for x in S})

def all_linear_subspaces(n):
    subs={frozenset({0})}
    vecs=list(range(1,1<<n))
    changed=True
    while changed:
        changed=False
        cur=list(subs)
        for S in cur:
            for v in vecs:
                if v not in S:
                    T=span_add(S,v)
                    if T not in subs:
                        subs.add(T); changed=True
    return list(subs)

def all_affine_flats(n):
    flats=set()
    for V in all_linear_subspaces(n):
        for x in range(1<<n):
            flats.add(frozenset(y^x for y in V))
    return list(flats)

def sign_flat(A,n):
    return [-1 if x in A else 1 for x in range(1<<n)]

def random_affine_flat(n,rng):
    # Random affine subspace via random independent constraint rows, then enumerate.
    r=rng.randrange(0,n+1)
    rows=[]
    while len(rows)<r:
        v=rng.randrange(1,1<<n)
        # rank test via xor basis
        basis=[]
        for w in rows+[v]:
            x=w
            for b in basis:
                x=min(x,x^b)
            if x:
                basis.append(x); basis.sort(reverse=True)
        if len(basis)==len(rows)+1:
            rows.append(v)
    rhs=[rng.randrange(2) for _ in rows]
    A=[]
    for x in range(1<<n):
        if all(((x & row).bit_count() & 1)==b for row,b in zip(rows,rhs)):
            A.append(x)
    return frozenset(A)

def product_sign(flats,n):
    out=[1]*(1<<n)
    for A in flats:
        for x in range(1<<n):
            if x in A: out[x]*=-1
    return out

def check_general():
    count=0
    max_violation=-1e100
    worst=None
    for n in range(0,5):
        N=1<<n
        for truth in range(1<<N):
            vals=[-1 if (truth>>x)&1 else 1 for x in range(N)]
            H,I,J,L,C,inf,B=metrics(vals)
            v=H-C*J
            count+=1
            if v>max_violation:
                max_violation=v
                worst={"n":n,"truth":truth,"H":H,"I":I,"J":J,"L1":L,"C":C}
            if sum(B) > H + 1e-10:
                raise AssertionError(("Han-Shearer",n,truth,sum(B),H))
            if I>1e-12 and min((B[i]-C*inf[i] for i in range(n)), default=0.0) > 1e-10:
                raise AssertionError(("selector",n,truth,B,inf,C))
            # Fourier l1 norm cannot increase under a physical restriction.
            for i in range(n):
                plus=[vals[x] for x in range(N) if ((x>>i)&1)==0]
                minus=[vals[x] for x in range(N) if ((x>>i)&1)==1]
                if metrics(plus)[3] > L + 1e-10 or metrics(minus)[3] > L + 1e-10:
                    raise AssertionError(("restriction-L1",n,truth,i,L,metrics(plus)[3],metrics(minus)[3]))
    return count,max_violation,worst

def check_flat_pairs():
    count=0
    max_l1=0.0
    max_violation=-1e100
    worst=None
    C2=2*LOG2E+8*math.log2(3)
    for n in range(1,5):
        flats=all_affine_flats(n)
        signs=[sign_flat(A,n) for A in flats]
        for ia,A in enumerate(flats):
            for ib,B in enumerate(flats):
                vals=[x*y for x,y in zip(signs[ia],signs[ib])]
                H,I,J,L,C,inf,B=metrics(vals)
                count+=1
                max_l1=max(max_l1,L)
                v=H-C2*J
                if v>max_violation:
                    max_violation=v
                    worst={"n":n,"ia":ia,"ib":ib,"H":H,"J":J,"L1":L}
    return count,max_l1,max_violation,worst,C2

def check_random_arrangements():
    rng=random.Random(20260920)
    records=[]
    total=0
    max_violation=-1e100
    max_lratio=0.0
    for m in [3,4]:
        Cm=2*LOG2E+4*m*math.log2(3)
        for n in [5,6]:
            for _ in range(2500):
                flats=[random_affine_flat(n,rng) for __ in range(m)]
                vals=product_sign(flats,n)
                H,I,J,L,C,inf,B=metrics(vals)
                total+=1
                max_lratio=max(max_lratio,L/(3**m))
                max_violation=max(max_violation,H-Cm*J)
        records.append({"m":m,"C_m":Cm})
    return total,max_violation,max_lratio,records

def check_parallel_cancellation():
    n=4
    A=frozenset(x for x in range(1<<n) if ((x>>0)&1)==0 and ((x>>1)&1)==0 and ((x>>2)&1)==0)
    B=frozenset(x for x in range(1<<n) if ((x>>0)&1)==0 and ((x>>1)&1)==0 and ((x>>2)&1)==1)
    C=frozenset(x for x in range(1<<n) if ((x>>0)&1)==0 and ((x>>1)&1)==0)
    sA=sign_flat(A,n); sB=sign_flat(B,n); sC=sign_flat(C,n)
    prod=[a*b for a,b in zip(sA,sB)]
    # q=1_C, so (-1)^q=sigma_C; product cancels exactly.
    final=[x*y for x,y in zip(sC,prod)]
    H,I,J,L,Cc,inf,Bbits=metrics(final)
    qH,qI,qJ,qL,qC,qinf,qB=metrics(sC)
    return {
        "A_size":len(A),"B_size":len(B),"C_size":len(C),
        "sigmaA_sigmaB_equals_sigmaC":prod==sC,
        "final_constant":len(set(final))==1,
        "final_I":I,
        "quadratic_phase_influences":qinf,
    }

def main():
    gc,gviol,gworst=check_general()
    pc,pmaxl,pviol,pworst,C2=check_flat_pairs()
    rc,rviol,rlratio,rrecords=check_random_arrangements()
    obstruction=check_parallel_cancellation()
    out={
        "status":"PASS" if max(gviol,pviol,rviol)<=1e-10 and obstruction["final_constant"] else "FAIL",
        "general_boolean_exhaustive":{"cases":gc,"max_violation":gviol,"worst":gworst},
        "affine_flat_pair_exhaustive":{"cases":pc,"C2":C2,"max_observed_L1":pmaxl,"max_violation":pviol,"worst":pworst},
        "random_arrangements":{"cases":rc,"max_violation":rviol,"max_L1_over_3powm":rlratio,"constants":rrecords},
        "parallel_codim3_cancellation":obstruction,
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
