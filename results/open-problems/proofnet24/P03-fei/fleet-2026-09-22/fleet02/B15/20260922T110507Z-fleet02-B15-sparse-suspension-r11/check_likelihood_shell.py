import math
from collections import defaultdict


def solve_c(r):
    mu = sum(r)
    if abs(mu - 1.0) < 1e-14:
        return None
    def f(c):
        prod = 1.0
        for x in r:
            prod *= (1.0 - c*x)
        return 1.0 - c - prod
    lo, hi = 1e-14, 1.0
    for _ in range(220):
        mid = (lo + hi)/2.0
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi)/2.0


def q_nonempty(r):
    c = solve_c(r)
    if c is None:
        raise ValueError("mu=1 boundary not used in this checker")
    t = [c*x for x in r]
    q = {}
    n = len(r)
    for mask in range(1, 1 << n):
        v = 1.0/c
        for i,ti in enumerate(t):
            v *= ti if (mask >> i) & 1 else (1.0-ti)
        q[mask] = v
    return c,q


def kl(P,Q):
    return sum(p*math.log2(p/Q[x]) for x,p in P.items() if p > 0)


def shell_kl(P,Q,signs=None,delta=1.0):
    cells = defaultdict(lambda: [0.0,0.0])
    for x in set(Q):
        p = P.get(x,0.0)
        q = Q[x]
        is_singleton = x != 0 and (x & (x-1)) == 0
        if is_singleton:
            z = ("single",x)
        elif p == 0.0:
            z = ("zero",)
        else:
            ell = math.log2(p/q)
            sg = signs.get(x,0) if signs is not None else 0
            z = ("tail",sg,math.floor(ell/delta))
        cells[z][0] += p
        cells[z][1] += q
    return sum(p*math.log2(p/q) for p,q in cells.values() if p > 0)


def sparse_shell(m,delta=1.0):
    p = 2.0**(1-m)
    cells = defaultdict(lambda:[0.0,0.0])
    kocc = 0.0
    for k in range(m+1):
        mult = math.comb(m,k)
        p_atom = (1-p)**2 if k == 0 else p*p
        q_atom = (p**k)*((1-p)**(m-k))
        Pk = mult*p_atom
        Qk = mult*q_atom
        if Pk:
            kocc += Pk*math.log2(p_atom/q_atom)
        if k == 0:
            z=("single-y",)
        else:
            ell=math.log2(p_atom/q_atom)
            z=("tail",-1,math.floor(ell/delta))
        cells[z][0]+=Pk
        cells[z][1]+=Qk
    ks=sum(Pc*math.log2(Pc/Qc) for Pc,Qc in cells.values() if Pc)
    return p,kocc,ks


def h2(x):
    if x <= 0 or x >= 1:
        return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)


def rm_classes(d):
    N={(1,1):3,(3,1):1}
    if d==1:
        return N
    for _ in range(1,d):
        items=list(N.items())
        pair=defaultdict(int)
        for (k1,a1),n1 in items:
            for (k2,a2),n2 in items:
                pair[(k1+k2,a1+a2)] += n1*n2
        triple=defaultdict(int)
        for (kp,ap),npair in pair.items():
            for (k3,a3),n3 in items:
                triple[(kp+k3,1+ap+a3)] += npair*n3
        new=defaultdict(int)
        for (k,a),cnt in N.items():
            new[(k,a+1)] += 3*cnt
        for key,cnt in triple.items():
            new[key] += cnt
        N=dict(new)
    return N


def rm_shell(d,delta=1.0):
    N=rm_classes(d)
    n=3**d
    r=2.0**(-d)
    mu=(1.5)**d
    c=solve_c([r]*n)
    t=c*r
    cells=defaultdict(lambda:[0.0,0.0])
    kocc=0.0
    H=0.0
    for (k,a),cnt in N.items():
        p_atom=2.0**(-2*a)
        q_atom=(1.0/c)*(t**k)*((1.0-t)**(n-k))
        pm=cnt*p_atom
        qm=cnt*q_atom
        ell=math.log2(p_atom/q_atom)
        H += pm*(2*a)
        kocc += pm*ell
        if k==1:
            z=("single-ratio",)
        else:
            z=("tail",math.floor(ell/delta))
        cells[z][0]+=pm
        cells[z][1]+=qm
    ks=sum(Pc*math.log2(Pc/Qc) for Pc,Qc in cells.values() if Pc)
    Hmax=(n*h2(c*r)-h2(c))/c
    return mu,H,Hmax,kocc,ks,len(N)


def main():
    tol=1e-10

    raw=[0,-4,-4,0,-4,0,0,-4,-12,0,0,4,0,4,4,0]
    P={m:(w/16.0)**2 for m,w in enumerate(raw) if w}
    r=[sum(p for m,p in P.items() if (m>>i)&1) for i in range(4)]
    c,Q=q_nonempty(r)
    signs={m:(1 if raw[m]>0 else -1) for m in P}
    K=kl(P,Q); Ks=shell_kl(P,Q,signs,1.0)
    tail=sum(p for m,p in P.items() if m&(m-1))
    assert K-Ks <= tail + tol
    assert tail <= sum(r)-1 + tol
    print("PRIME4", "mu", sum(r), "c", c, "Kocc", K, "Kshell", Ks, "loss", K-Ks, "tail", tail)

    P3={1:3/5}
    for m in range(2,8):
        P3[m]=1/15
    r3=[sum(p for m,p in P3.items() if (m>>i)&1) for i in range(3)]
    c3,Q3=q_nonempty(r3)
    raw3=[-2,6,2,2,2,2,-2,-2]
    signs3={m:(1 if raw3[m]>0 else -1) for m in P3}
    K3=kl(P3,Q3); Ks3=shell_kl(P3,Q3,signs3,1.0)
    tail3=sum(p for m,p in P3.items() if m&(m-1))
    assert K3-Ks3 <= tail3 + tol
    assert tail3 <= sum(r3)-1 + tol
    print("OR_AND3", "mu", sum(r3), "c", c3, "Kocc", K3, "Kshell", Ks3, "loss", K3-Ks3, "tail", tail3)

    max_sparse_loss=0.0
    for m in range(2,31):
        p,K,KS=sparse_shell(m,1.0)
        max_sparse_loss=max(max_sparse_loss,abs(K-KS))
        assert abs(K-KS) < 2e-10
    print("SPARSE_M2_30", "max_abs_loss", max_sparse_loss)

    max_ratio=0.0
    min_center5=1e100
    for d in range(1,5):
        mu,H,Hmax,K,KS,nclasses=rm_shell(d,1.0)
        loss=K-KS
        ratio=loss/(mu-1.0) if mu>1 else 0.0
        compiled5=5.0*(mu-1.0)-Hmax+KS
        max_ratio=max(max_ratio,ratio)
        min_center5=min(min_center5,compiled5)
        assert loss <= (mu-1.0)+2e-9
        assert abs(H-4.0*(mu-1.0)) < 2e-10
        assert compiled5 >= -2e-9
        print("RM3", d, "classes", nclasses, "mu", mu, "Kocc", K, "Kshell", KS, "loss_over_excess", ratio, "compiled_C5", compiled5)
    print("RM3_SUMMARY", "max_loss_over_excess", max_ratio, "min_compiled_C5", min_center5)
    print("PASS")


if __name__ == "__main__":
    main()
