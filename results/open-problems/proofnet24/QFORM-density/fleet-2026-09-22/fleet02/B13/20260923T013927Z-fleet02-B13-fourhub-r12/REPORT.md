SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B13, 2026-09-23T01:39:27Z.
attacking: the entropic co-heavy three-volume obstruction, sharpening six physical hubs to a four-by-four hub pair and an exact Schur aggregate.

# fleet02/B13 — entropic D' rebalancing gives four-by-four physical hubs and a Schur aggregate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Extremal product laws`  
Status: **PROVED SUPPORTING TARGET-LEVEL THEOREM / FULL QFORM OPEN / FULL CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication and exact source boundary

The full target remains: for arbitrary independent real coordinates with densities `0<=f_i<=1` and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal essential density bound for `X^T A X`, or produce a valid counterexample. No moment, support, connectedness, log-concavity, diagonal-basis product structure, or post-rotation independence assumption is used below.

The first unpaid implication attacked here is the designated-partner obstruction

`QFORM-SIX-HUB-LOW-3VOLUME-GLUING-v1`.

The new result improves its structural side: the six-row alternative can be replaced by **four row hubs and four column hubs**, and then by one genuine physical row-column pair carrying a fixed fraction of all third-volume currency. That pair retains the entire residual Schur `e_2` bank (or, at zero edge, the entire mixed-hub cofactor bank); no single residual minor is selected.

Completed inputs actually used at equations:

1. Newest Claude Fourier source `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`: Theorem D' permits row three-volume marginals up to any `h<3/4` and gives
   `6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1) Z^(-1/6)` for the natural three-volume law. I extend the same proof below to an arbitrary entropy-reweighted physical minor law; the determinant step is written explicitly.
2. Designated partner fleet03/B13 r20, source `yspennstate/math-open-problems@c7d99a5becf262e519f50bd221ab49c0bd807534`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260923T003350Z-fleet03-B13-qform-r20/REPORT.md`: the identity `K(mu)=Z exp(-D(mu||w))` and entropy-projection-versus-hub mechanism. The present run changes the row cap from `1/2` to the D' cap `5/8`, which reduces the entropy-dual hub count from six to four.
3. fleet01/B04 r23, available at `yspennstate/math-open-problems@bf2ad8d54b9240e4aab6a24f648931faf6f4e054`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260923T005009Z-fleet01-B04-QFORM-r23/REPORT.md`: the exact joint-volume/Schur identity. It is re-derived below for the pair produced by the new entropy argument.
4. The partner's preceding countable extreme-product reduction fleet03/B13 r19: full essential boundedness, through the supplied full-to-no-pivot synthesis, is equivalent to bounding a strict no-`1/16`-pivot rational finite-grid product-indicator class. Its proof uses finite-mixture approximation and does not assume an attained infinite-line bathtub optimizer, a bounded support radius, a bounded diameter, or a bounded fragment count.

Live corrections consumed include the failure of arbitrary-joint rank-three coarea, law-uniform pointwise quadratic-phase decay, post-rotation independence, bounded-diameter/fixed-fragment extremality, universal single-minor selection, and small-matrix-perturbation continuity on unbounded supports. None is used.

## 2. Entropic D' for an arbitrary physical minor law

Let `I,J` be disjoint original-coordinate banks and let `M=A[I,J]`. Put

`Z=e_3(M^T M)=sum_{|S|=|T|=3} det(M[S,T])^2`,

and assume `Z>0`. Let `A_3` be the finite set of nonzero physical `3x3` minors `a=(S,T)`. For **any** probability law `mu` on `A_3`, define

`alpha_i=P_mu(i in S)`, `beta_j=P_mu(j in T)`,

and

`K(mu)=exp(H(mu)+E_mu log det(M[S,T])^2)`.

### Theorem 2.1 — `QFORM-DPRIME-ENTROPIC-MINOR-v1`

Fix `1/2<=h<3/4`. If

`alpha_i<=h` for every row `i`,

then every full ambient quadratic polynomial having this original-coordinate cross block obeys

`||p_Q||_infinity <= C_h K(mu)^(-1/6)`,

where

`C_h = 6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1)`.                 (2.1)

All same-side quadratic blocks, outside couplings, affine terms and signs are arbitrary. The proof gives an `L^1` characteristic function, hence a continuous density in this paid branch.

#### Proof

Use the same physical-coordinate Weyl differencing as in Theorem D/D'. With `W=X_J-X'_J`, whose coordinates remain independent and have densities at most one, write

`F(W)=prod_i |psi_i(2t(MW)_i)|`.

Then

`|phi_Q(t)|^2 <= E F(W)`.                                         (2.2)

Put `q=2h`, so `1<=q<3/2`. Since `0<=F<=1`, Jensen gives

`E F <= (E F^q)^(1/q)`.                                           (2.3)

Apply Brascamp--Lieb to `F^q` with row exponents `alpha_i` and coordinate exponents `1-beta_j`. Rows with `alpha_i=0` are dropped; columns with `beta_j=1` are dropped exactly as in the corrected determinant proof of the source theorem. For positive Gaussian parameters `d_i,e_j`, expansion of `det(D+M^T D_I M)` into diagonal-plus-PSD minors gives

`det(D+M^T D_I M)`
` >= sum_(S,T in A_3) det(M[S,T])^2 prod_(i in S)d_i prod_(j notin T)e_j`.

Weighted AM-GM with weights `mu_(S,T)` yields

`det(D+M^T D_I M)`
` >= K(mu) prod_i d_i^(alpha_i) prod_j e_j^(1-beta_j)`.            (2.4)

Thus the Gaussian BL constant is at most

`K(mu)^(-1/2) prod_i alpha_i^(-alpha_i/2)`
`                 *prod_j(1-beta_j)^(-(1-beta_j)/2)`.             (2.5)

The scalar source lemma gives, because `q/alpha_i>=2`,

`int |psi_i(2ts)|^(q/alpha_i) ds`
` <= (2pi/|t|) sqrt(alpha_i/q)`.                                  (2.6)

After raising (2.6) to the powers `alpha_i`, the `alpha_i` factors cancel those in (2.5), while `sum alpha_i=3`. Also

`prod_j(1-beta_j)^(-(1-beta_j)/2) <= exp(3/2)`.                   (2.7)

Therefore

`E F^q <= e^(3/2)(2pi)^3 q^(-3/2)|t|^(-3)K(mu)^(-1/2)`.          (2.8)

Combining (2.2)-(2.3),

`|phi_Q(t)| <= B |t|^(-3/(2q))`,

`B=[e^(3/2)(2pi)^3 q^(-3/2)K(mu)^(-1/2)]^(1/(2q))`.              (2.9)

Set `a=3/(2q)>1`. Integrating `min(1,B|t|^-a)` on the real line gives

`||p_Q||_infinity <= 2 sqrt(e) q^(-1/2) a/(a-1) K(mu)^(-1/6)`,

which, with `q=2h`, is exactly (2.1). QED.

For the clean cap used below,

`h=5/8`,

so

`C_(5/8)=24 sqrt(e/5)=17.6959336187295...`.                       (2.10)

## 3. Entropy rebalancing or four physical row hubs

Let `w` be the natural three-volume law

`w_(S,T)=det(M[S,T])^2/Z`.

For every probability law `mu` on `A_3`, the exact identity is

`K(mu)=Z exp(-D(mu||w))`.                                         (3.1)

Fix `h in [1/2,3/4)` and `L>0`. Let

`F_h={mu: alpha_i(mu)<=h for every physical row i}`.

### Theorem 3.1 — `QFORM-ENTROPIC-3VOLUME-OR-h-HUB-v1`

At least one of the following holds.

**Paid branch.** There exists `mu in F_h` with `D(mu||w)<=L`; then

`||p_Q||_infinity <= C_h e^(L/6) Z^(-1/6)`.                       (3.2)

**Hub branch.** There is a set of physical rows `H` with

`|H|<=floor(3/h)`                                                 (3.3)

such that

`e_3(M[I\H,J]^T M[I\H,J]) < e^(-L) Z`.                           (3.4)

If `F_h` is empty, the surviving volume in (3.4) is actually zero and `|H|<3/h`.

#### Proof: infeasible case

Treat each supported minor atom `(S,T)` as a 3-uniform row edge `S` (duplicate row triples are harmless). If `F_h` is empty, there is no fractional matching `x_a>=0` with vertex loads at most one and total weight at least `1/h`: otherwise normalizing by its total weight would produce a probability law with every row load at most `h`.

Finite LP duality therefore gives a fractional vertex cover `y_i>=0` with

`sum_i y_i < 1/h`,

and `sum_(i in S)y_i>=1` on every supported atom. Let

`H={i:y_i>=1/3}`.

Every supported row triple meets `H`, and

`|H|/3 <= sum_i y_i <1/h`,

so `|H|<3/h`. Deleting `H` kills every nonzero `3x3` minor, proving the strengthened conclusion.

#### Proof: feasible but entropy-expensive case

Assume `F_h` is nonempty and put

`D_*=min_(mu in F_h) D(mu||w)`.

If `D_*<=L`, (3.1) and Theorem 2.1 give (3.2). Suppose `D_*>L`. The finite-alphabet entropy projection has the convex dual

`D_*=sup_(lambda_i>=0) [-log E_w exp(-Lambda(S))-h sum_i lambda_i]`,

`Lambda(S)=sum_(i in S)lambda_i`.                                 (3.5)

Choose a dual vector making the bracket bigger than `L`, and put `R=sum_i lambda_i`. Then

`E_w exp(-Lambda(S)) < exp(-L-hR)`.                               (3.6)

Set

`H={i:lambda_i>=hR/3}`.

Its size satisfies `|H|<=3/h`. If a supported triple is disjoint from `H`, then `Lambda(S)<hR`, hence

`P_w(S cap H=empty) exp(-hR)
 < E_w exp(-Lambda(S))
 < exp(-L-hR)`.

Thus

`P_w(S cap H=empty)<e^(-L)`.                                      (3.7)

By Cauchy--Binet, the left side is exactly the ratio in (3.4). QED.

### Clean four-hub specialization

Take

`h=5/8`, `L=log 64`.

Then either

`boxed: ||p_Q||_infinity <= 48 sqrt(e/5) Z^(-1/6)
                           =35.3918672374591... Z^(-1/6),}`        (3.8)

or there is a set of at most **four** physical rows `H` for which

`e_3(M[I\H,J]^T M[I\H,J]) < Z/64`.                               (3.9)

This strictly improves the designated partner's six-row entropy branch, at the price of the still-universal D' prefactor in (3.8).

## 4. Two-sided four-by-four hubs force one physical Schur aggregate

Apply Theorem 3.1 first to `M` and then, if needed, to `M^T`. The transpose is simply the opposite orientation of the same disjoint original-coordinate cut, so product provenance is unchanged.

### Theorem 4.1 — `QFORM-DPRIME-FOURBYFOUR-SCHUR-AGGREGATE-v1`

For every `M` with `Z>0`, at `h=5/8`, `L=log64`, either the full ambient quadratic form is already paid by (3.8), or there exist

`H_R subset I`, `H_C subset J`, `|H_R|,|H_C|<=4`,

such that under the natural third-volume law

`P_w(S intersects H_R and T intersects H_C)>31/32`.               (4.1)

Consequently some genuine physical pair `(i,j) in H_R x H_C` obeys

`boxed: Z_ij:=sum_(S contains i,T contains j)det(M[S,T])^2
             > (31/512) Z.}`                                     (4.2)

#### Proof

If neither orientation is paid, Theorem 3.1 gives

`P_w(S intersects H_R)>63/64`,
`P_w(T intersects H_C)>63/64`.

The union bound gives (4.1). Moreover

`1_{S hits H_R,T hits H_C}
 <= sum_(i in H_R,j in H_C)1_{i in S,j in T}`.

Taking expectations and using at most sixteen pairs yields (4.2). QED.

Now write the cross block around this distinguished original-coordinate row and column as

`M=[[a,r^T],[c,N]]`, `a=M_ij`.

If `a!=0`, set

`S_*=N-c r^T/a`.

For every two-row/two-column choice `P,Q`,

`det [[a,r_Q^T],[c_P,N_PQ]]=a det((S_*)_PQ)`.

Squaring and summing gives the exact source-safe identity

`boxed: Z_ij=a^2 e_2(S_* S_*^T).}`                                (4.3)

Hence in the unpaid branch

`boxed: a^2 e_2(S_* S_*^T) > (31/512)Z.}`                         (4.4)

If `a=0`, Laplace expansion instead gives

`det [[0,r_Q^T],[c_P,N_PQ]]=-r_Q^T adj(N_PQ)c_P`,

so with

`H_ij=sum_(P,Q)[r_Q^T adj(N_PQ)c_P]^2`,

one has

`boxed: H_ij=Z_ij>(31/512)Z.}`                                    (4.5)

Thus entropy concentration has been converted to **one physical pair plus an aggregate residual bank**, not to one local residual minor.

### No-pivot specialization

In the strict no-`tau`-pivot class, `0<tau<=1`,

`a^2 < tau^2+tau=tau(1+tau)<=2tau`.                               (4.6)

Therefore the nonzero-edge branch satisfies

`boxed: e_2(S_* S_*^T) > 31 Z/[512 tau(1+tau)]
                         >=31 Z/(1024 tau).}`                      (4.7)

The zero-edge branch retains (4.5). These are physical-coordinate aggregate currencies compatible with the current correction set.

A useful corollary: if `s_3(M)>=gamma`, then `Z>=gamma^6`. Hence either

`||p_Q||_infinity <=35.3918672374591.../gamma`,                    (4.8)

or there is a physical pair carrying the Schur/cofactor currency in (4.4)-(4.7) with `Z` replaced by at least `gamma^6`.

## 5. Extremal-product transfer and the counterexample normal form

The designated partner's preceding r19 reduction is used here exactly to avoid an infinite-line attainment assumption. If full essential boundedness is false, the supplied full-to-no-pivot synthesis plus finite-mixture approximation produces, for arbitrarily large slab ratios, a **finite rational-grid product-indicator witness** in the strict no-`1/16`-pivot class. Grid denominator, support radius, translations, gaps and fragment count are unrestricted.

Theorem 4.1 applies to every physical cross block of each such finite witness. Thus on any block with useful third volume, an escaping witness has only two possibilities:

1. the entropically rebalanced D' law pays it by (3.8), with zero support assumptions; or
2. one original-coordinate row-column pair carries at least `31/512` of all third-volume currency, and after completing that physical edge the **whole** Schur `e_2` bank, or the zero-edge mixed-hub cofactor bank, remains quantitatively large.

No centered interval, bounded support, bounded diameter, bounded fragment count or attained global bathtub optimizer appears in this passage.

The pinned `D_5` theorem remains the complementary exit: a quantitatively large fifth volume pays without any marginal gate. The present theorem is aimed precisely at the D5-small/co-heavy third-volume survivor.

## 6. New first unpaid implication

The remaining B13 debt is now narrower than the partner's six-hub gluing problem:

**`QFORM-N3-ENTROPIC-PAIR-SCHUR-AGGREGATE-SMOOTHING-v1`.**

In the strict no-pivot finite-grid extreme-product class, suppose a useful cross block escapes the entropically reweighted D' payment in both orientations. Then consume the forced physical pair without selecting a local residual minor:

`a!=0:  a^2 e_2(S_*S_*^T) >31 Z/512`,

or

`a=0:   H_ij>31 Z/512`.

Derive a dimension-free averaged-frequency/fractional-potential estimate from this **aggregate** currency, or route it to a completed mixed-hub/Fresnel, D5, determinant-pair, grouped-bank or ridge branch. Small operator error may not be treated as a small random quadratic perturbation on arbitrary unbounded product supports.

This is a genuine reduction in the obstruction: six unspecified heavy rows have become at most four hubs per side and then one physical pair with a constant-fraction aggregate Schur/cofactor bank.

## 7. Deterministic sanity checks

A companion checker tests the exact pair-Schur identity on random finite matrices and the zero-edge cofactor identity, and verifies the clean constants

`C_(5/8)=24 sqrt(e/5)`,
`2 C_(5/8)=48 sqrt(e/5)=35.3918672374591...`,
`1-2/64=31/32`,
`(31/32)/16=31/512`.

In 300 random nonzero-edge tests up to size seven, the maximum relative Schur identity error was below `2e-15`; in 100 zero-edge tests it was below `5e-16`. These computations are diagnostic only; the theorem is the analytic proof above.

## 8. Status

Full QFORM essential boundedness remains **OPEN / NOT PROVED**. Full-target continuity remains **OPEN**. Continuity is obtained only in the paid D' branch of this report. The new result is a target-level structural/analytic reduction for the remaining no-pivot extreme-product geometry.
