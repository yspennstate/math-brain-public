# Projection entropy and the remaining spectral bridge

Root creative lead, 2026-09-15. **The entropy bound proposed below is not proved in general.** This note separates an exact sufficient principle from numerical evidence.

Completed development: C056 now proves beta>=0, with a sharp explicit lower bound, for every rank-one phase frame in every dimension and background rank. Combined with C035, it closes joint two-eigenvalue concavity for that entire frame family. The general projection flag remains open.

For an orthogonal projection flag \(W\subset W+[u],W+[v]\subset W+[u,v]\), put
\[
H_0=H(\mu_W),\ H_1=H(\mu_{W+[u]}),\
H_2=H(\mu_{W+[v]}),\ H_3=H(\mu_{W+[u,v]}),
\qquad \beta=H_1+H_2-H_0-H_3.
\]
For \(K_{p,q}=P_W+p uu^*+q vv^*\), conditioning on cardinality gives exactly
\[
H(P_{K_{p,q}})
=H(\operatorname{Bern}(p)+\operatorname{Bern}(q))
+H_0+p(H_1-H_0)+q(H_2-H_0)-\beta pq
+G(p(1-q),q(1-p)),
\]
where \(G\) is the concave, coordinatewise nondecreasing Jensen-Shannon perspective of the two middle projection laws, as in ROOT_RANK_TWO_SPECTRAL.md.

Therefore:

- If \(\beta\ge0\), ordinary two-trial count entropy concavity (C075, theta=0), the term -2 beta times the slope product, and the perspective calculation prove nonpositive entropy curvature in every same-sign spectral direction. The upper bound 2log2 is not needed for this implication.
- If the flag also has a positive unlabeled diamond coupling, opposite-sign directions are nonpositive by the frozen-log argument (or by common interior regularization). The two facts together prove full joint \((p,q)\) concavity for that flag.
- ROOT_RANK_TWO_SPECTRAL.md proves beta>=0 (and the stronger auxiliary upper bound) and the resulting theorem for \(W=0\), without equal-modulus restrictions. Complementation also covers top codimension zero. The prior rank-one-bottom coupling theorem handles the opposite-sign part for any rank-one \(W\), but a general nonnegativity proof for \(\beta\) remains missing there.
- C034/C035/C036 give further explicit coupling families, so proving beta>=0 within one of them would supply a new spectral theorem. A common random-permutation realization alone does not imply the bound for arbitrary channels: the nonphysical V4 example has negative \(\beta\).

## Bounded numerical evidence, not a proof

A reproducible NumPy QR experiment used seed 202609150056, dimensions 4 through 8, every bottom rank 1 through n-3, and 70 complex Gaussian frames per case: **1,050 samples**. The minimum observed beta was 0.07162577865496145 at (n,r,index)=(8,4,65); the maximum was 1.1952683352348998 at (4,1,46), below 2log2=1.3862943611198906. Floating-point QR and determinants are exploratory only. No inequality is certified by this sample.

The first console summary accidentally printed a hardcoded 1,400 sample count; the actual nested loops have 70(1+2+3+4+5)=1,050 samples, as recorded here. The count error affects no mathematical value.

Exact reproduction:

~~~python
import numpy as np,itertools,math
rng=np.random.default_rng(202609150056)
def ent(Q,cols):
    Z=Q[:,cols]
    ps=[abs(np.linalg.det(Z[list(I)]))**2
        for I in itertools.combinations(range(len(Q)),len(cols))]
    return -sum(x*math.log(x) for x in ps if x>0)
lo=(float('inf'),None); hi=(-float('inf'),None); count=0
for n in [4,5,6,7,8]:
    for r in range(1,n-2):
        for k in range(70):
            Q=np.linalg.qr(rng.normal(size=(n,n))
                          +1j*rng.normal(size=(n,n)))[0]
            A=list(range(r))
            beta=(ent(Q,A+[r])+ent(Q,A+[r+1])
                  -ent(Q,A)-ent(Q,A+[r,r+1]))
            count+=1
            if beta<lo[0]: lo=(float(beta),[n,r,k])
            if beta>hi[0]: hi=(float(beta),[n,r,k])
print(count,lo,hi)
~~~

A creative follow-up should prove beta>=0 in a new flag family, or certify a counterexample to it. It must control the actual projection laws and not assume submodularity of their entropies from ordinary entropy submodularity.
