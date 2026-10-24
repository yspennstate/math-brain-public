SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-23T21:30:06Z.
attacking: partner account03/B06 r45's off-diagonal anchored-curvature survivor; turn off-diagonal K_H currency into a determinant-favorable ORIGINAL-coordinate E2 receiver, then characterize exactly what failure of that receiver means.

# account02/B06 — anchored-K wedge receiver and quantitative alignment compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `b06-20260923T213006Z-8e3b1c4a`  
Role: Curved fiber integration  
Status: **NEW SUPPORTING THEOREM + QUANTITATIVE STRUCTURAL COMPILER + PINNED RESULT APPLIED + LATEST PARTNER r45 APPLIED / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains OPEN. Nothing here assumes moments, compact support, log-concavity, iid laws, a spectral-coordinate product law, or independence after rotation. Every active bank below consists of literal original coordinates. Continuity is not claimed by the new estimates.

The first unpaid implication on entry was partner r45's

`QFORM-INDEFINITE-NEARNULL-OFFDIAGONAL-K-AGGREGATION-v1`:

all diagonal anchored curvatures may be too small for its new physical-triple determinant receiver, while substantial off-diagonal/Frobenius currency remains. The task is to aggregate that currency before extracting an individual reciprocal minor or taking a curved-fiber supremum.

## 1. Sources actually used

Latest completed designated partner on this invocation is account03/B06 r45,

`yspennstate/math-open-problems@b5d4a62bb80a7ad84db292cb8d886282a95e851b`,

which proves the determinant-only three-physical-coordinate theorem

`||p_(Z^T M Z+ell^T Z+c)||_infinity <102 |det M|^(-1/3)`

and hence

`|(K_H)_{kk}|>=eta  =>  ||p_Q||_infinity <=102 eta^(-1/3)`         (1.1)

for every literal environment coordinate k. Thus its survivor has small diagonal entries of K_H.

Its predecessor r44 proves the exact anchored critical-curvature identity. For

`A=[[H,E],[E^T,C]],   H=[[a,b],[b,d]],   E=[alpha^T;beta^T]`,

define

`K_H=det(H) C-E^T adj(H)E`.                                      (1.2)

Every entry `(K_H)_{jk}` is the physical 3x3 minor anchored at the two hubs; if H is invertible, `K_H/det(H)` is exactly the environmental Schur matrix after completing both hubs.

The owner-required pinned source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`.

Two completed ingredients from it are used at their proved scopes:

* `FOURIER_ROUTE_REPORT.md`, Lemma 4.2: if a literal scalar pivot is `a!=0`, then

  `D(Q)<=|a|^(-1/2) H_(1/2)(Schur_a Q)`.                           (1.3)

* its `D_k` theorem at `k=2,q=1`: on the diffuse natural-two-volume arm of a literal cross block M,

  `|phi(t)|<=min(1,2 pi sqrt(e) e_2(M^T M)^(-1/4)|t|^(-1))`.      (1.4)

Together with the already-completed account02/B06 heavy-row transfer, (1.4) gives the row-gate-free compiler

`H_(1/2)(R)<=8 e^(1/4) e_2(M^T M)^(-1/8)`                         (1.5)

for every quadratic polynomial R having the literal cross block M. All same-bank curvature, additional cross directions and affine terms are retained.

`COUNTEREXAMPLE_SEARCH.md` Theorem A is applied in Section 7 to an actual diffuse aligned target family.

## 2. First physical completion and the exact K identity

Assume `a!=0`; no rotation is made. Complete only the original coordinate X corresponding to the first hub. Put

`delta=d-b^2/a=det(H)/a`,
`gamma=beta-(b/a)alpha`,
`R=C-alpha alpha^T/a`.                                            (2.1)

The remaining quadratic matrix on the untouched original coordinates `(Y,Z)` is

`S1=[[delta,gamma^T],[gamma,R]].`                                 (2.2)

Also define the unscaled innovation vector used by r43-r45,

`Gamma=a beta-b alpha=a gamma`.                                  (2.3)

A direct expansion of (1.2) gives the exact identity

`boxed: K_H=a(delta R-gamma gamma^T).`                             (2.4)

Equivalently, for environment indices u,v,

`(K_H)_(uv)=a delta R_(uv)-a gamma_u gamma_v`.                    (2.5)

This identity keeps the critical-value curvature and the moving hyperbolic centre in the same physical coordinates.

## 3. Main analytic theorem: anchored-K wedge square-peel receiver

Choose disjoint sets U,V of environment ORIGINAL coordinates. For `u in U` and distinct `v,w in V`, (2.5) implies

`det [[gamma_v,gamma_w],[R_(uv),R_(uw)]]
 = [gamma_v (K_H)_(uw)-gamma_w (K_H)_(uv)]/det(H)`                (3.1)

or, using `Gamma=a gamma`,

` = [Gamma_v (K_H)_(uw)-Gamma_w (K_H)_(uv)]/[a det(H)]`.         (3.2)

Define the aggregate anchored wedge currency

`W_(U,V)
 :=sum_(u in U) sum_(v<w in V)
      [Gamma_v (K_H)_(uw)-Gamma_w (K_H)_(uv)]^2.`                 (3.3)

Let M be the literal cross block of S1 whose row bank is `{Y} union U` and whose column bank is V. Every determinant in (3.2) is one of the 2x2 minors entering `e_2(M^T M)`. Therefore Cauchy-Binet gives

`boxed:
 e_2(M^T M)>=W_(U,V)/[a^2 det(H)^2].`                             (3.4)

### Theorem 3.1 — `QFORM-ANCHORED-K-WEDGE-SQUARE-PEEL-v1`

Whenever `W_(U,V)>0`, the full ambient quadratic form satisfies

`boxed:
 ||p_Q||_infinity
 <=8 e^(1/4) |a|^(-1/4)|det H|^(1/4) W_(U,V)^(-1/8).`             (3.5)

Equivalently, since `|det H|=|a delta|`,

`||p_Q||_infinity
 <=8 e^(1/4)|delta|^(1/4) W_(U,V)^(-1/8).`                        (3.6)

Here (3.6) uses W defined with Gamma as in (3.3).

#### Proof

The literal X-square peel (1.3) gives

`D(Q)<=|a|^(-1/2)H_(1/2)(R1)`,                                   (3.7)

where R1 is the entire polynomial on `(Y,Z)` with quadratic matrix S1. Apply (1.5) to its literal cross block M and then (3.4):

`D(Q)
 <=8e^(1/4)|a|^(-1/2)e_2(M^TM)^(-1/8)
 <=8e^(1/4)|a|^(-1/2)|a detH|^(1/4)W_(U,V)^(-1/8),`               (3.8)

which is (3.5), hence (3.6). QED.

The important feature is the sign of the determinant power: this receiver is **determinant-favorable**, not determinant-singular. If a fixed amount of wedge curvature survives, the bound improves as the indefinite hub tends to rank one. No conditional density supremum over a hyperbola appears.

On the diffuse natural-two-volume row arm, the required pinned theorem (1.4) is being used at the literal inequality (3.8), not merely cited. The heavy-row arm is exactly the aggregate transfer already proved by this slot; it still does not select or divide by one small local minor.

## 4. Quantitative compiler: failure means rank-one alignment up to diagonal

The wedge currency has an exact structural meaning. Let

`G=||Gamma||_2^2`,                                                (4.1)

and suppose first that the innovation is not concentrated on one environment coordinate:

`max_j Gamma_j^2 <=G/2.`                                         (4.2)

Define the off-diagonal alignment defect

`Delta_K
 := min_(tau in R)
    [sum_(u!=v)((K_H)_(uv)-tau Gamma_u Gamma_v)^2]^(1/2).`        (4.3)

### Lemma 4.1 — `QFORM-ANCHORED-K-WEDGE-ALIGNMENT-COMPILER-v1`

There is a bipartition of the environment indices into disjoint U,V for which

`boxed: W_(U,V)>=G Delta_K^2/81.`                                 (4.4)

Consequently

`boxed:
 ||p_Q||_infinity
 <=8 sqrt(3)e^(1/4)
      ( |delta|/(||Gamma||_2 Delta_K) )^(1/4).`                   (4.5)

The universal coefficient is

`8 sqrt(3)e^(1/4)=17.7919780793...`.                              (4.6)

#### Proof of the compiler

For each row u, delete its u-th coordinate and write

`g^(u)=(Gamma_v)_(v!=u)`, `k^(u)=((K_H)_(uv))_(v!=u)`.

Set

`T_u=||g^(u) wedge k^(u)||^2
   =sum_(v<w; v,w!=u)
      [Gamma_v(K_H)_(uw)-Gamma_w(K_H)_(uv)]^2`,                   (4.7)

and `T=sum_u T_u`. Because (4.2) gives `||g^(u)||^2>=G/2`, the least-squares coefficient

`c_u=<g^(u),k^(u)>/||g^(u)||^2`

has residuals

`r_(uv)=(K_H)_(uv)-c_u Gamma_v`, `v!=u`,

satisfying

`sum_(u!=v) r_(uv)^2 <=2T/G`.                                    (4.8)

Symmetry of K_H gives

`c_u Gamma_v-c_v Gamma_u=r_(vu)-r_(uv)`.                         (4.9)

Therefore

`||c wedge Gamma||^2
 <=2 sum_(u!=v)r_(uv)^2
 <=4T/G`.                                                        (4.10)

Choosing `tau=<c,Gamma>/G`, the identity

`||c wedge Gamma||^2=G||c-tau Gamma||^2`

gives

`||c-tau Gamma||^2<=4T/G^2`.                                    (4.11)

For u != v,

`(K_H)_(uv)-tau Gamma_u Gamma_v
 =r_(uv)+(c_u-tau Gamma_u)Gamma_v`.

Hence

`Delta_K^2<=12T/G`.                                              (4.12)

Now choose a random bipartition with each coordinate independently put in U with probability 1/3 and in V with probability 2/3. Every ordered u and unordered pair {v,w} of distinct other indices is captured with probability

`(1/3)(2/3)^2=4/27`.

Thus

`E W_(U,V)=4T/27`,                                                (4.13)

so some partition has `W_(U,V)>=4T/27>=G Delta_K^2/81`. This proves (4.4). Insert it into (3.6); because `81^(1/8)=sqrt(3)` and `G^(-1/8)=||Gamma||^(-1/4)`, (4.5) follows. QED.

### Exact zero-currency classification

If every wedge vanishes and Gamma is nonlocalized, (4.4) forces `Delta_K=0`. Thus there is a scalar tau for which

`boxed: K_H-tau Gamma Gamma^T is diagonal off the nose;`          (4.14)

that is, every off-diagonal entry obeys

`(K_H)_(uv)=tau Gamma_u Gamma_v`, `u!=v`.                         (4.15)

At the exact rank-one hub endpoint `delta=0`, (2.4) gives

`K_H=-(1/a)Gamma Gamma^T`,                                       (4.16)

so the collapse of all wedge currency is not accidental: it is exactly the algebraic endpoint predicted by r44.

If (4.2) fails, one literal environment coordinate h satisfies

`|Gamma_h|>||Gamma||/sqrt(2)`.                                   (4.17)

Thus failure of the diffuse compiler produces a bounded-cardinality physical chain certificate rather than an uncontrolled fiber maximum.

## 5. Latest partner r45 applied to the new compiler

Partner r45 has already paid every diagonal anchored curvature through (1.1). Its remaining debt is exactly the all-diagonals-small, off-diagonal-K chamber. The present compiler turns that debt into a precise trichotomy.

On the inherited r43/r44 innovation branch,

`||Gamma||>=2^(-12)`.                                            (5.1)

Therefore either:

1. **innovation-heavy:** some literal environment coordinate obeys

   `|Gamma_h|>2^(-12)/sqrt(2)`;                                  (5.2)

2. **off-diagonal misalignment:** Gamma is diffuse and `Delta_K>0`, in which case

   `boxed:
   ||p_Q||_infinity
    <=142.335825 (|delta|/Delta_K)^(1/4);`                        (5.3)

3. **aligned collar:** Gamma is diffuse and K_H is close, in off-diagonal Frobenius norm, to `tau Gamma Gamma^T` plus a diagonal matrix. More quantitatively, if the density is not paid at a desired constant C by (4.5), then

   `Delta_K < [8 sqrt(3)e^(1/4)/C]^4 |delta|/||Gamma||`.          (5.4)

Thus a genuine near-null survivor must approach the rank-one alignment locus at least linearly in `|delta|` (up to the explicit innovation factor), rather than merely having nonzero aggregate K_H.

Combine this with r45: if additionally some `|(K_H)_(kk)|>=eta`, (1.1) pays the whole form by `102 eta^(-1/3)`. Hence the unresolved chamber has **both** small physical diagonal K-curvatures and small off-diagonal distance from the aligned rank-one pattern, or else a single heavy innovation coordinate.

This is a strict narrowing of r45's `QFORM-INDEFINITE-NEARNULL-OFFDIAGONAL-K-AGGREGATION-v1` debt.

## 6. Companion fallback: spend operator curvature before localizing a minor

There is a second, weaker but gate-free way to use r44's K_H identity. Let H be invertible indefinite, put

`D=|det H|`, `kappa=sigma_min(H)`, `Kop=||K_H||_op`.

The completed environmental quadratic matrix is `S=K_H/det H`, so `||S||=Kop/D`. The arbitrary-rank quarter-small-ball lemma and pair-log smoothing from the pinned pair-extension give

`boxed:
 ||p_Q||_infinity
 <=3*400^(1/3) (D kappa Kop)^(-1/6).`                             (6.1)

If S has rank one, the sharper rank-one affine small-ball theorem gives

`boxed:
 ||p_Q||_infinity
 <=8 sqrt(5) (kappa Kop)^(-1/4).`                                 (6.2)

The determinant D cancels completely in (6.2). This does not solve the near-null collar because kappa may vanish, but it is a useful fallback on the rank-one-K side of the compiler and again spends aggregate curvature before any entrywise reciprocal.

## 7. A diffuse aligned exact-target family: the remaining pattern is real, but not a counterexample

The alignment branch cannot simply be declared impossible. For N>=2 let `Z_1,...,Z_N,X,Y` be independent cap-one variables and set

`gamma=(sqrt(2/N),...,sqrt(2/N))`, `||gamma||=sqrt(2)`,

`Q_(N,epsilon)=X^2-epsilon Y^2+2Y(gamma dot Z)`, `0<epsilon<=1`.   (7.1)

The ORIGINAL-coordinate matrix has three nonzero eigenvalues

`1`, and `(-epsilon +/- sqrt(epsilon^2+8))/2`,                    (7.2)

all of modulus at least one. Thus (7.1) is a genuine owner-target family, with every individual star edge tending to zero as N grows.

Take the physical pair `(X,Y)`. Here

`Gamma=gamma`, `K_H=-gamma gamma^T`, `delta=-epsilon`.             (7.3)

Hence

`Delta_K=0`, every wedge currency W_(U,V) vanishes identically, and

`max_k |(K_H)_(kk)|=2/N ->0`.                                    (7.4)

So **both** partner r45's diagonal-K gate and the new wedge-misalignment gate vanish along a perfectly valid target family. This refutes the tempting intermediate claim that target spectrum alone forces either a fixed anchored diagonal or a fixed anchored wedge.

Nevertheless the family is uniformly bounded by a source-valid grouping. Put

`L=gamma dot Z`.

The original-product one-dimensional projection theorem gives

`||p_L||_infinity <=sqrt(2)/||gamma||=1`.                        (7.5)

Because L uses a coordinate bank disjoint from X,Y, the three variables X,Y,L are genuinely independent. In these variables

`Q_(N,epsilon)=X^2-epsilon Y^2+2YL`                              (7.6)

has 3x3 matrix

`M_epsilon=[[1,0,0],[0,-epsilon,1],[0,1,0]]`.                    (7.7)

Its least eigenvalue modulus for `0<epsilon<=1` is at least

`sigma_0=(sqrt(5)-1)/2`.                                         (7.8)

Now apply the required pinned `COUNTEREXAMPLE_SEARCH.md` Theorem A to the actual three independent cap-one variables `(X,Y,L)`:

`boxed:
 ||p_(Q_(N,epsilon))||_infinity
 <=6 sqrt(pi)/sigma_0
 =3 sqrt(pi)(sqrt(5)+1)
 =17.2073434455... .`                                            (7.9)

This is not post-rotation independence: L is a function of a disjoint ORIGINAL product bank. The example identifies the correct next object. Exact alignment can be harmless because an entire diffuse bank may be grouped into one source-valid scalar; what remains hard is the same alignment in the presence of arbitrary diagonal/light-bank twists and extra coupled curvature.

## 8. First unpaid implication after this run

The new debt is

`QFORM-R45-ALIGNED-HOLLOW-K-DIAGONAL-TWIST-v1`.

After r45 and the present compiler, retain the complete cross tail and arbitrary same-bank curvature and assume:

* every principal anchored curvature `(K_H)_(kk)` is below the r45 extraction scale;
* Gamma is diffuse (otherwise (4.17) is a physical one-coordinate chain certificate);
* `K_H` is quantitatively close off-diagonally to `tau Gamma Gamma^T` at the near-null scale forced by (5.4).

In the exact zero-defect case, (2.4) says the first Schur light matrix is diagonal plus a rank-one term aligned with the same innovation gamma. Equivalently the original light block is diagonal plus a rank-at-most-two form living in the physical slope span. The next receiver should exploit that **source-preserving two-projection + diagonal-twist structure** directly. The model (7.1) shows the no-twist endpoint is paid by legitimate grouping and pinned Theorem A; r44's logarithmic example shows that discarding the aligned third curvature entirely (`K_H=0`) is invalid. The missing bridge is therefore a weighted two-projection/diagonal-twist estimate uniform through the indefinite null limit, not a lower bound on one local minor.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity remains OPEN.

## 9. Algebraic checks

The identities used above are exact:

`K_H=a(delta R-gamma gamma^T)`,

and for every distinct u,v,w,

`det[[gamma_v,gamma_w],[R_uv,R_uw]]
 =[Gamma_v K_uw-Gamma_w K_uv]/[a det H]`.

A finite random sanity check of the quantitative compiler on symmetric matrices and diffuse Gamma found no violation of

`max_(U,V) W_(U,V)>=||Gamma||^2 Delta_K^2/81`;

the proof in Section 4 is algebraic and does not rely on that computation.
