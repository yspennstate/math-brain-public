# account03/B11 r24 — Plucker-edge stability and an aggregate-before-inversion dichotomy

**Run:** `20260923T080909Z-account03-B11-QFORM-r24`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** indefinite signatures / quantitative inequalities  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_STRUCTURAL_THEOREM / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 0. Scope and source boundary

The full target remains open: for arbitrary independent real coordinates with densities at most one and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal `L^infinity` density bound for `X^T A X`, or give a genuine counterexample.

This run preserves the live corrections: no post-rotation independence, no arbitrary-joint rank-three coarea bound, no conditional-density-cap substitute for independence, no law-uniform pointwise van-der-Corput estimate, and no claim that one uniformly good physical minor is forced by the three-large-eigenvalue hypothesis. The result below is instead an **aggregate-before-inversion** statement: it first measures all physical two-row spectral areas and only then decides whether localization is forced.


The localized receiver used below is account03/B11 `QFORM-LOCALIZED-3BLOCK-REPAIR-v1`, canonical source `yspennstate/math-open-problems@a9f23a3a387c9be219fcaf08ef66079f8c124e0c`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260922T192514Z-account03-B11-QFORM-r14/REPORT.md`. It states that an ORIGINAL-coordinate principal `3 x 3` block of smallest singular value at least `s0>0` gives

`||p_(X^T A X)||_infinity <= 128*2^(1/4)/s0`,

uniformly over all outside coefficients and couplings.

The designated partner source used below is account04/B11, `yspennstate/math-open-problems@4110bbfd21beffa0260a017d468b0a486af56db1`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260922T222040Z-account04-B11-cone-envelope-r3/REPORT.md`. Its null-scalar smoothing theorem is recalled in Section 4.

## 1. A weighted EKR stability lemma for edge measures

The first result is purely combinatorial, but it is exactly matched to the Plucker weights of a three-dimensional spectral frame.

### Lemma 1 — `QFORM-WEIGHTED-EDGE-STAR-TRIANGLE-v1`

Let `p` be any probability distribution on the two-element subsets (edges) of a finite vertex set. Draw two edges `E,F` independently from `p`, and set

`delta = P(E cap F = empty)`.

Let `q_v=P(v in E)` be the star mass at a vertex. For `0<=delta<=1`, with `tau=delta^(1/3)`, at least one of the following holds:

1. some vertex `v` has

   `q_v >= 1-delta-tau`;

2. some three vertices `a,b,c` have triangle mass

   `p_ab+p_ac+p_bc >= 1-delta-tau`.

For `delta=0` the same statement holds with right side one.

### Proof

For an edge `e`, write

`r_e = P(F cap e = empty)`.

Averaging over `E` gives `E r_E=delta`, so choose `e0={a,b}` with `r:=r_e0<=delta`. Put

`m=p_ab`,
`A=sum_{x notin {a,b}} p_ax`,
`B=sum_{x notin {a,b}} p_bx`.

Every edge that is not disjoint from `{a,b}` is exactly `{a,b}`, `{a,x}`, or `{b,x}`, hence

`m+A+B=1-r`.                                           (1.1)

If `A<=tau`, the star at `b` has mass

`q_b=m+B=1-r-A >=1-delta-tau`.

Likewise, if `B<=tau`, the star at `a` has the required mass. It remains to assume `A,B>tau`.

For each `x notin {a,b}` define `A_x=p_ax` and `B_x=p_bx`, and let

`S=sum_x A_x B_x`.

An edge `{a,x}` and an edge `{b,y}` are disjoint whenever `x!=y`. Counting both ordered orientations in `(E,F)`,

`delta >=2(AB-S)`.                                      (1.2)

Normalize `a_x=A_x/A`, `b_x=B_x/B`. Then

`sum_x a_x b_x = S/(AB)
              >=1-delta/(2AB)
              >=1-tau/2`,                               (1.3)

because `AB>tau^2` and `delta=tau^3`.

Choose `c` with `a_c=max_x a_x`. Since a weighted average is at most the maximum,

`a_c >= sum_x a_xb_x >=1-tau/2`.                       (1.4)

Moreover,

`sum_x a_xb_x
 <= a_c b_c +(1-a_c)*1
 =1-a_c(1-b_c)`.

Together with (1.3),

`a_c(1-b_c)<=tau/2`.

For `tau<=1`, (1.4) gives `a_c>=1/2`, hence

`b_c>=1-tau`.                                           (1.5)

Therefore

`p_ab+p_ac+p_bc
 =m+A a_c+B b_c
 >=m+A(1-tau/2)+B(1-tau)
 >=m+A+B-tau
 =1-r-tau
 >=1-delta-tau`.                                        (1.6)

This proves the lemma. For `delta=0`, the same argument is obtained by taking the evident limiting case; alternatively (1.2) says the normalized `a` and `b` measures have inner product one, hence they are the same point mass. `QED`

## 2. Plucker specialization: a star is geometrically impossible above 2/3

Let `R` be an `n x 3` matrix with orthonormal columns and rows `r_i in R^3`. Define

`w_ij = ||r_i wedge r_j||^2`,  `i<j`.

The Cauchy--Binet / exterior-frame identity gives

`sum_{i<j} w_ij = e_2(R^T R)=e_2(I_3)=3`.              (2.1)

Thus

`p_ij=w_ij/3`                                             (2.2)

is a probability distribution on physical row pairs. Its star mass has an exact formula. Put `c_i=||r_i||^2`. Then

`sum_{j!=i} w_ij
 =sum_j [c_i ||r_j||^2-(r_i dot r_j)^2]
 =3c_i-r_i^T(sum_j r_jr_j^T)r_i
 =2c_i`.                                                  (2.3)

Since `RR^T` is an orthogonal projection, `0<=c_i<=1`; hence every normalized Plucker star satisfies

`q_i=(1/3)sum_{j!=i}w_ij =2c_i/3 <=2/3`.                 (2.4)

This makes Lemma 1 much stronger here: sufficiently small disjoint-edge mass cannot end in the star alternative.

### Theorem 2 — `QFORM-PLUCKER-EDGE-STABILITY-LOCALIZATION-v1`

Let

`Delta = sum_{e cap f=empty} p_e p_f`                    (2.5)

be the ordered probability that two independently Plucker-volume-sampled physical row pairs are disjoint. Put

`eta=Delta+Delta^(1/3)`.

If `eta<1/3`, there is a physical triple `T={i,j,k}` such that

`sigma_min(R_T)^2 >= 1-3eta`.                            (2.6)

In particular, if

`Delta <=1/64`,                                           (2.7)

then

`sigma_min(R_T)^2 >=13/64`.                              (2.8)

### Proof

Lemma 1 applied to (2.2) produces either a star or a triangle carrying at least `1-eta` of the normalized edge mass. If `eta<1/3`, then `1-eta>2/3`, so (2.4) excludes the star. Hence some triple `T` satisfies

`sum_{e subset T} w_e >=3(1-eta)`.                       (2.9)

Let

`S_T=sum_{i in T} r_i r_i^T = R_T^T R_T`.

Because `S_T<=I_3`, its eigenvalues `1>=theta_1>=theta_2>=theta_3>=0`. Also

`e_2(S_T)=sum_{e subset T} ||r_i wedge r_j||^2`,          (2.10)

so (2.9) gives

`theta_1theta_2+theta_1theta_3+theta_2theta_3 >=3(1-eta)`.

The first two products are each at most one, hence

`theta_2theta_3 >=1-3eta`.                               (2.11)

Since `theta_2<=1`, `theta_3>=1-3eta`. But `theta_3=sigma_min(R_T)^2`, proving (2.6).

For `Delta<=1/64`, `Delta^(1/3)<=1/4`, so `eta<=17/64` and

`1-3eta >=1-51/64=13/64`. `QED`

## 3. Exact-rank-three indefinite consequence

Consider an exact-rank-three real symmetric form

`A=R M R^T`,  `R^T R=I_3`,                             (3.1)

where `M` is invertible symmetric of signature `(2,1)` or `(1,2)` and

`sigma_min(M)>=s>0`.                                      (3.2)

This includes the target scale `s>=1`.

If `Delta<=1/64`, Theorem 2 gives a triple `T` with `sigma_min(R_T)^2>=13/64`. Its ORIGINAL-coordinate principal block is

`A_T=R_T M R_T^T`.

Singular-value submultiplicativity from below gives

`sigma_min(A_T)
 >=sigma_min(R_T)^2 sigma_min(M)
 >=13s/64`.                                               (3.3)

Now apply the completed localized three-block receiver cited in Section 0:

`||p_(X^T A X)||_infinity
 <= [128*2^(1/4)]/(13s/64)
 = [8192*2^(1/4)/(13)] s^(-1)
 <749.384/s`.                                             (3.4)

We have therefore proved the following correction-safe dichotomy:

### Corollary 3 — `QFORM-EXACT-RANK3-LOCAL-OR-DISJOINT-WEDGE-v1`

For every exact-rank-three indefinite target (3.1)--(3.2), either

`Delta >=1/64`,                                           (3.5)

or

`||p_(X^T A X)||_infinity <749.384/s`.                   (3.6)

No physical minor was selected before aggregation. The aggregate Plucker law decides whether localization is forced. This is precisely an aggregate-before-inversion reduction and is insensitive to the number of physical coordinates.

The result is a supporting theorem, not the full conjecture: arbitrary additional spectrum can alter a physical principal block by cancellation, and the large-`Delta` branch still requires a product-preserving grouped receiver.

## 4. Designated partner result applied to a genuine rotated large-Delta example

The completed account04/B11 cone-envelope theorem says: if `Z` is independent of `(V,W)`, `||p_Z||_infinity<=L`, and `(V,W)` has joint-density cap `M0`, then

`T=2 alpha ZW + beta V^2 +2 gamma VW+delta0 W^2 + affine`

satisfies

`||p_T||_infinity
 <=3*2^(2/3)(L M0)^(2/3)|alpha|^(-2/3)|beta|^(-1/3)`.    (4.1)

Apply it to four independent cap-one original coordinates. Set

`Z=X_1`,
`V=(X_2+X_3+X_4)/sqrt(3)`,
`W=(X_2-X_3)/sqrt(2)`.                                   (4.2)

The coefficient vectors for `V,W` are orthonormal. The source-valid two-dimensional product-projection theorem gives

`||p_(V,W)||_infinity <=e`,                               (4.3)

while `Z` is genuinely independent of that pair and `||p_Z||_infinity<=1`. Thus, for

`T=2ZW+V^2`,                                               (4.4)

(4.1) with `alpha=beta=1` yields the actual target-level inequality

`||p_T||_infinity <=3(2e)^(2/3)
                   =9.2755051971...`.                    (4.5)

On the orthonormal active basis `{e_1,v,w}`, the quadratic matrix is

`H0=[[0,0,1],[0,1,0],[1,0,0]]`,

whose eigenvalues are `{1,1,-1}`. Thus (4.4) is a genuinely rotated `(2,1)` target form; replacing it by `-T` gives `(1,2)`.

It also lies in the **large disjoint-Plucker-mass branch** of Corollary 3. Taking `R=[e_1,v,w]`, the six pair weights are

`{5/6,5/6,1/3,2/3,1/6,1/6}`,

with total three, and the ordered disjoint-pair probability is exactly

`Delta=1/9 >1/64`.                                       (4.6)

So the designated partner theorem pays a concrete nontrivial representative of the branch left by the new dichotomy.

## 5. Why the third direction removes the rank-two logarithm

The mandatory control remains exact. If `X,Y` are independent `Uniform[-1/2,1/2]`, then for `0<|t|<1/2`,

`p_(2XY)(t)=log(1/(2|t|))`,                              (5.1)

so an opposite-sign rank-two saddle has an unbounded logarithmic density.

In (4.4), the hyperbolic part `2ZW` has precisely this local mechanism. The partner proof splits according to `|W|`: away from zero the Jacobian gives the rank-two `1/|W|` behavior, but the independent third curvature `V^2` changes the near-zero kernel to `|W|^(-1/2)`, which is integrable. Importantly, `V` and `W` need not themselves be independent; only the genuine original-coordinate product provenance needed for the joint pair-density cap and the independence of the separate scalar bank is used.

The new Plucker theorem gives the complementary structural picture. In a three-dimensional spectral frame, if independent physical pairs almost always intersect, exterior-volume mass is forced into one physical triple because a Plucker star can carry at most `2/3` of the total. That triple supplies three-dimensional curvature directly. If disjoint pair mass is substantial, the needed third direction must instead be extracted by grouping disjoint original-coordinate banks before paying reciprocal minors; the partner example (4.2)--(4.6) shows exactly how such a grouped third direction kills the logarithm.

## 6. Remaining implication

The first unpaid B11 implication is now

`QFORM-DISJOINT-PLUCKER-MASS-TO-PRODUCT-RECEIVER-v1`:

> Starting from a dimension-free lower bound `Delta>=1/64` on disjoint Plucker-pair mass, aggregate the corresponding disjoint original-coordinate banks and prove that either a rank-two-cross-plus-square / null-scalar / ridge receiver has dimension-free currency, or an already-paid physical pair / localized / diffuse branch fires.

The key restriction is that one may not select a single disjoint pair and pay its reciprocal determinant; the mass may be spread over arbitrarily many small pairs. The aggregation must occur before inversion, exactly as required by the live `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` and Plucker-support corrections.

Arbitrary additional spectrum remains a separate bridge: the theorem above is exact-rank-three because a tail can cancel the selected component on a physical principal block. The supporting result proves essential boundedness in the localized branch and in the partner example. It does **not** establish global continuity.

## 7. Exact finite checks

The accompanying `VERIFY.py` checks:

- the threshold arithmetic `Delta=1/64 -> eta=17/64 -> 1-3eta=13/64`;
- the constant `8192*2^(1/4)/13`;
- the explicit frame (4.2), its orthonormality, all six wedge weights, total Plucker mass three, and `Delta=1/9`;
- the active matrix eigenvalues `{1,1,-1}`;
- the partner constant `3(2e)^(2/3)`.

These finite checks support the algebra only; the proofs above are analytic and do not rely on Monte Carlo evidence.
