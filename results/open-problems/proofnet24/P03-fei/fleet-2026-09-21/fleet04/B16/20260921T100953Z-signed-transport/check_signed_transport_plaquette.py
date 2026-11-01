#!/usr/bin/env python3
import itertools, json, math, random
from collections import defaultdict

TOL = 2e-10
SEED = 160921
random.seed(SEED)

def fwht_int(vals):
    a = list(map(int, vals))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def truth(n, mask):
    N = 1 << n
    out = [1] * N
    for x in range(1, N):
        if (mask >> (x-1)) & 1:
            out[x] = -1
    return out

def pointwise(*fs):
    return [math.prod(z) for z in zip(*fs)]

def entropy_from_W(W):
    N = len(W)
    den = N*N
    ans = 0.0
    for w in W:
        if w:
            p = (w*w)/den
            ans -= p*math.log2(p)
    return ans

def H(f):
    return entropy_from_W(fwht_int(f))

def all_mod_sign(n):
    return [truth(n, m) for m in range(1 << ((1 << n)-1))]

def rand_bool_list(n):
    return [1 if random.random()<0.5 else -1 for _ in range(1<<n)]

def triple_transport_exact(f,g):
    N=len(f); Wf=fwht_int(f); Wg=fwht_int(g); h=pointwise(f,g); Wh=fwht_int(h)
    total=0
    neg_num=0
    for A in range(N):
        row=0
        for B in range(N):
            z=Wf[A]*Wg[B]*Wh[A^B]
            row += z
            total += z
            if z<0: neg_num += -z
        assert row == N*Wf[A]*Wf[A], ("row",A,row,N*Wf[A]*Wf[A])
    for B in range(N):
        col=sum(Wf[A]*Wg[B]*Wh[A^B] for A in range(N))
        assert col == N*Wg[B]*Wg[B], ("col",B)
    for C in range(N):
        xm=sum(Wf[A]*Wg[A^C]*Wh[C] for A in range(N))
        assert xm == N*Wh[C]*Wh[C], ("xor",C)
    assert total == N**3, ("total",total,N**3)
    lhs = H(f)+H(g)-H(h)
    # Signed conditional entropy is half of this by the analytic identity.
    return lhs, neg_num/(N**3)

def fourway_curvature_exact(sigma,f,g):
    funcs=[sigma,pointwise(f,sigma),pointwise(g,sigma),pointwise(f,g,sigma)]
    Ws=[fwht_int(x) for x in funcs]
    N=len(sigma)
    # Exact one-coordinate marginals.
    for slot in range(4):
        for s in range(N):
            tot=0
            others=[j for j in range(4) if j!=slot]
            # enumerate two free labels, third forced by xor zero
            j1,j2,j3=others
            for x in range(N):
                for y in range(N):
                    lab=[None]*4
                    lab[slot]=s; lab[j1]=x; lab[j2]=y
                    lab[j3]=s^x^y
                    z=1
                    for q in range(4): z*=Ws[q][lab[q]]
                    tot+=z
            assert tot == (N**2)*(Ws[slot][s]**2), ("4marg",slot,s,tot,(N**2)*Ws[slot][s]**2)
    # Floating cross-ratio identity.
    ent=[entropy_from_W(W) for W in Ws]
    kappa=ent[1]+ent[2]-ent[0]-ent[3]
    cross=0.0
    neg=0.0
    for A in range(N):
        a=Ws[0][A]/N
        for B in range(N):
            b=Ws[1][B]/N
            for C in range(N):
                c=Ws[2][C]/N
                D=A^B^C
                d=Ws[3][D]/N
                nu=a*b*c*d
                if nu<0: neg += -nu
                if nu:
                    ratio=(a*a*d*d)/(b*b*c*c)
                    cross += nu*math.log2(ratio)
    assert abs(kappa-cross) < TOL, ("cross",kappa,cross)
    # Plaquette involutions.
    def kap(base):
        return H(pointwise(f,base))+H(pointwise(g,base))-H(base)-H(pointwise(f,g,base))
    k0=kap(sigma)
    assert abs(k0-kappa)<TOL
    assert abs(kap(pointwise(f,sigma))+k0)<TOL
    assert abs(kap(pointwise(g,sigma))+k0)<TOL
    assert abs(kap(pointwise(f,g,sigma))-k0)<TOL
    return kappa,neg

def char_phase(n,S):
    return [(-1)**((x&S).bit_count()&1) for x in range(1<<n)]

def monomial_phase(n,A):
    A=tuple(A)
    out=[]
    for x in range(1<<n):
        bit=1
        for i in A:
            bit &= ((x>>i)&1)
        out.append(-1 if bit else 1)
    return out

def subgroup(gens):
    if not gens:
        return [[1]]
    N=len(gens[0]); one=tuple([1]*N)
    seen={one}; stack=[one]
    while stack:
        h=stack.pop()
        for g in gens:
            z=tuple(a*b for a,b in zip(h,g))
            # identify global sign because H is sign-invariant; canonicalize first value +1
            if z[0] < 0: z=tuple(-a for a in z)
            if z not in seen:
                seen.add(z); stack.append(z)
    return [list(z) for z in seen]

def T(P,f):
    return sum(H(pointwise(f,s))-H(s) for s in P)/len(P)

def C(P,f,g):
    return 0.5*sum(H(pointwise(f,s))+H(pointwise(g,s))-H(s)-H(pointwise(f,g,s)) for s in P)/len(P)

def chain_tests():
    n=3
    chars=[char_phase(n,S) for S in range(1<<n)]
    P=subgroup(chars)
    assert len(P)==8
    gs=[monomial_phase(n,(0,1)),monomial_phase(n,(0,2)),monomial_phase(n,(1,2))]
    fs=all_mod_sign(n)
    maxerr=0.0; tests=0
    for g in gs:
        P2=subgroup(P+[g])
        for f in fs:
            lhs=T(P,f)-T(P2,f); rhs=C(P,f,g)
            maxerr=max(maxerr,abs(lhs-rhs)); tests+=1
            assert abs(lhs-rhs)<TOL
        # quotient invariance on deterministic sample.
        for _ in range(40):
            f=random.choice(fs); p=random.choice(P); q=random.choice(P)
            base=C(P,f,g)
            shifted=C(P,pointwise(f,p),pointwise(g,q))
            maxerr=max(maxerr,abs(base-shifted)); tests+=1
            assert abs(base-shifted)<TOL
        P=P2
    # Initial character group gives T=H(f).
    for f in fs:
        assert abs(T(subgroup(chars),f)-H(f))<TOL
    return {"tests":tests+len(fs),"final_group_size":len(P),"max_error":maxerr}

def householder_test(n,A,f):
    N=1<<n; d=len(A); m=1<<d; Ac=[i for i in range(n) if i not in A]
    W=fwht_int(f); hat=[w/N for w in W]
    g=monomial_phase(n,A); W2=fwht_int(pointwise(f,g)); hat2=[w/N for w in W2]
    # enumerate outside labels R over subsets of Ac
    proj_energy=0.0; maxerr=0.0
    for rmask in range(1<<len(Ac)):
        R=0
        for k,i in enumerate(Ac):
            if (rmask>>k)&1: R |= 1<<i
        xs=[]; labels=[]
        for tmask in range(1<<d):
            T=0
            for k,i in enumerate(A):
                if (tmask>>k)&1: T |= 1<<i
            labels.append(R|T); xs.append(hat[R|T])
        v=[((-1)**(t.bit_count()))/math.sqrt(m) for t in range(m)]
        alpha=sum(v[i]*xs[i] for i in range(m))
        proj_energy += alpha*alpha
        ys=[xs[i]-2*alpha*v[i] for i in range(m)]
        for i,L in enumerate(labels):
            maxerr=max(maxerr,abs(ys[i]-hat2[L]))
    assert abs(proj_energy-1/m)<TOL, (proj_energy,1/m)
    assert maxerr<TOL, maxerr
    dist=sum((a-b)**2 for a,b in zip(hat,hat2))
    assert abs(dist-4/m)<TOL, (dist,4/m)
    return proj_energy,maxerr,dist

def main():
    out={"seed":SEED,"status":"PASS"}
    # Exhaustive triple signed-transport marginals through n=3.
    triple_cases=0; max_neg=0.0; min_defect=1e9
    first_negative=None
    for n in range(1,4):
        fs=all_mod_sign(n)
        for f in fs:
            for g in fs:
                defect,neg=triple_transport_exact(f,g)
                triple_cases+=1; max_neg=max(max_neg,neg); min_defect=min(min_defect,defect)
                if neg>0 and first_negative is None:
                    first_negative={"n":n,"f":f,"g":g,"negative_mass":neg,"triangle_defect_bits":defect}
    out["triple_transport"]={"cases":triple_cases,"max_n":3,"max_negative_mass":max_neg,
                             "min_triangle_defect_bits_observed":min_defect,
                             "first_negative_example":first_negative}
    # Exact 4-way marginals + cross-ratio: exhaustive n=2, sampled n=3.
    four_cases=0; maxerr=0.0; maxneg=0.0; mink=1e9; maxk=-1e9
    fs2=all_mod_sign(2)
    for s in fs2:
        for f in fs2:
            for g in fs2:
                k,neg=fourway_curvature_exact(s,f,g)
                four_cases+=1; maxneg=max(maxneg,neg); mink=min(mink,k); maxk=max(maxk,k)
    fs3=all_mod_sign(3)
    for _ in range(250):
        s,f,g=(random.choice(fs3) for __ in range(3))
        k,neg=fourway_curvature_exact(s,f,g)
        four_cases+=1; maxneg=max(maxneg,neg); mink=min(mink,k); maxk=max(maxk,k)
    out["fourway_transport"]={"cases":four_cases,"n2_exhaustive":len(fs2)**3,"n3_sampled":250,
                              "max_negative_mass":maxneg,"min_curvature_bits":mink,"max_curvature_bits":maxk}
    out["group_chain"]=chain_tests()
    hh=0; max_hh_err=0.0
    for n in range(2,5):
        fs=all_mod_sign(min(n,3)) if n<=3 else [rand_bool_list(4) for _ in range(100)]
        # if n=4 random list already right dimension; n<=3 exhaustive
        for d in range(2,n+1):
            A=tuple(range(d))
            sample=fs if n<4 else fs
            for f in sample:
                pe,er,dist=householder_test(n,A,f)
                hh+=1; max_hh_err=max(max_hh_err,er,abs(pe-2**(-d)),abs(dist-2**(2-d)))
    out["householder"]={"cases":hh,"max_n":4,"max_error":max_hh_err}
    # Explicit signed transport frustration example: one-point defects at two different points in n=3.
    f=truth(3,1); g=truth(3,2)
    defect,neg=triple_transport_exact(f,g)
    out["explicit_frustration_example"]={"f_truth":f,"g_truth":g,"negative_mass":neg,
                                         "Hf":H(f),"Hg":H(g),"Hfg":H(pointwise(f,g)),
                                         "triangle_defect_bits":defect}
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
