SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-23T22:45:53Z.
attacking: the exact rank-one physical-pair collar of the overlap-two ledger, by combining a new square–hyperbola receiver for the collinear kernel-star endpoint with the completed mixed-hub theorem in the transverse branch.

# account02/B09 r15 — rank-one pair collar compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism / complementary constructions and source-valid obstructions  
Status: **NEW SUPPORTING THEOREM; FULL QFORM OPEN; FULL-TARGET CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full target is unchanged: independent original-coordinate real inputs with probability densities at most one, arbitrary symmetric `A` with at least three eigenvalues of modulus at least one, and no moments, support, log-concavity, diagonal-basis assumption, or post-rotation independence.

## 1. First unpaid implication

The first unpaid implication after this run is

`QFORM-RANKONE-OMEGA2-ENTANGLED-LEAFCURVATURE-v1`:

> Let a physical two-coordinate core `B` be exactly rank one (and, later, uniformly near rank one) with nontrivial overlap-two third-compound mass. The pure collinear kernel-star is now paid, and the transverse diffuse mixed frame is paid. What remains is to retain a genuinely general quadratic operator on the *same active leaf bank* in the collinear/near-collinear branch, or route it to an already-paid projected-crossing / ridge / finite-core receiver, without deleting a small matrix term or taking a worst conditional projection-density supremum.

The near-rank-one passage is separate: small coefficient norm is not a small random quadratic perturbation for arbitrary unbounded cap-one inputs.

## 2. New analytic lemma: square plus hyperbola from a bounded two-dimensional hub density

### Theorem 2.1 — `QFORM-JOINT2-SQUARE-HYPERBOLA-v1`

Let `(U,V)` have an arbitrary joint probability density `rho` on `R^2` satisfying `rho<=M`. Let `W` be independent of `(U,V)` and have a probability density bounded by `S`. Then

`T = U^2 + 2 V W`

has an essentially bounded density and

`||p_T||_infinity <= 3*2^(2/3) M^(2/3) S^(2/3)`.                 (2.1)

More generally, for nonzero real `a,b`,

`||p_(a U^2 + 2 b V W)||_infinity
 <= 3*2^(2/3) M^(2/3) S^(2/3) |a|^(-1/3)|b|^(-2/3)`.          (2.2)

The same coefficient gives `P{T in I}<=C|I|` for every interval. Continuity is not claimed.

### Proof

For a target value `t`, split the coarea density into `|V|<=r` and `|V|>r`.

On `|V|<=r`, integrate first in `U`. For fixed `(v,w)`, the two roots of `u^2=t-2vw` contribute at most

`M (t-2vw)_+^(-1/2)`.

For every `w!=0`, substitution `s=t-2vw` gives

`int_{-r}^r (t-2vw)_+^(-1/2) dv <= 2 sqrt(r/|w|)`.              (2.3)

For a probability density bounded by `S`, the exact one-dimensional bathtub estimate is

`E |W|^(-1/2) <= 2 sqrt(2S)`.                                    (2.4)

Thus the small-`V` contribution is at most

`4 sqrt(2) M sqrt(Sr)`.                                          (2.5)

On `|V|>r`, integrate first in `W`. Conditional on `(u,v)`, the density contribution is at most

`S/(2|v|) <= S/(2r)`.

Integrating the hub density, whose total mass is one, gives the large-`V` contribution `S/(2r)`. Therefore

`||p_T||_infinity <= 4 sqrt(2) M sqrt(Sr) + S/(2r)`.             (2.6)

The optimum satisfies

`r^(3/2)=sqrt(S)/(4 sqrt(2) M)`.

Substitution into (2.6) gives exactly (2.1). Scaling `x=sqrt(|a|)u` and `z=bw` gives (2.2). No probability is squared; the estimate is linear in interval length. The proof uses only the joint cap on the two-dimensional hub and the one-dimensional cap on the independent linear factor.

## 3. Exact rank-one physical pair and overlap-two minors

Let `H={h1,h2}` be two literal original coordinates and let

`B=A[H,H]`

have rank one with nonzero eigenvalue `tau`. Let `ell` be a unit eigenvector and `k` a unit vector spanning `ker B`, so

`B=tau ell ell^T`, `adj(B)=tau k k^T`.                            (3.1)

For an outside physical coordinate `i`, write

`u_i=A[H,i] in R^2`, `q_i=k^T u_i`.                              (3.2)

For distinct outside coordinates `i,j`, block determinant expansion gives the exact original-coordinate identity

`det A[H union {i}, H union {j}]
 = det(B) A_ij - u_i^T adj(B) u_j
 = -tau q_i q_j`.                                                (3.3)

Hence for any outside set `I`, the fixed-pair overlap-two currency is

`Omega_(2,H)(I)
 = sum_{i!=j in I} det A[H union {i},H union {j}]^2
 = tau^2 [ (sum_i q_i^2)^2 - sum_i q_i^4 ]`.                    (3.4)

This factorisation is valid regardless of the leaf block `A[I,I]`. In particular, large `Omega_(2,H)` does **not** force a transverse two-dimensional cross Gram: all `u_i` may be collinear while the kernel coordinates `q_i` are spread.

## 4. New rank-one collinear-star receiver

### Theorem 4.1 — `QFORM-RANKONE-PAIR-COLLINEAR-STAR-v1`

Assume in addition that the active leaf block is zero and the physical pair-to-leaf cross matrix has rank one:

`A[I,I]=0`,
`A[I,H]=r g^T`,                                                  (4.1)

where `g` is a unit vector in `R^2`, `r!=0`, and

`beta=k^T g !=0`.                                                (4.2)

For arbitrary independent cap-one inputs on `H union I`, the homogeneous quadratic form

`Q = X_H^T B X_H + 2 X_I^T A[I,H] X_H`                           (4.3)

has an essentially bounded density satisfying

`||p_Q||_infinity
 <= 6 |tau|^(-1/3) ||A[I,H] k||_2^(-2/3)`.                      (4.4)

If `Omega_(2,H)(I)>0`, then also

`boxed: ||p_Q||_infinity <= 6 Omega_(2,H)(I)^(-1/6)`.            (4.5)

The identical constants give linear interval estimates. An arbitrary independent additive quadratic form on a disjoint coordinate block may be convolved in without increasing the bound.

### Proof

Rotate **only inside the integral over the two physical hub coordinates** to the orthonormal coordinates

`U=ell^T X_H`, `V=k^T X_H`.

The original hub joint density is the product of two cap-one densities and is therefore bounded by one. Orthogonal change of variables preserves this two-dimensional joint cap; no independence of `(U,V)` is asserted.

Write `g=alpha ell + beta k`. The cross term equals

`2 (alpha U + beta V) (r^T X_I)`.

Now make the area-preserving shear

`V'=V+(alpha/beta)U`.

The hub density remains bounded by one, the rank-one core remains exactly `tau U^2`, and the cross term becomes

`2 beta V' W`, `W=r^T X_I`.                                     (4.6)

The reviewed one-dimensional product-projection bound gives

`||p_W||_infinity <= sqrt(2)/||r||_2`.                           (4.7)

Apply Theorem 2.1 with `M=1`, `S=sqrt(2)/||r||_2`, `a=tau`, `b=beta`. Since

`||A[I,H]k||_2=|beta| ||r||_2`,

(4.4) follows, with the powers of two collapsing to the constant `6`.

Finally (3.4) implies

`Omega_(2,H)(I) <= tau^2 ||A[I,H]k||_2^4`,

so (4.5) follows. QED.

### Exact target-valid family

Let `m>=2`, take

`B=diag(1,0)`,
`A[i,h1]=0`, `A[i,h2]=1/sqrt(m)`, `A[I,I]=0`.                    (4.8)

The active spectrum is exactly `{1,1,-1}` plus zeros, so this is in the owner's target for every `m`. The overlap-two currency is

`Omega_(2,H)=1-1/m`,                                             (4.9)

while the two-hub cross Gram has rank one, so the ordinary two-hub mixed-frame determinant vanishes. The new theorem nevertheless gives

`boxed: ||p_Q||_infinity <= 6`,
`boxed: P{Q in J} <= 6 |J|`.                                    (4.10)

Thus the exact singular-pair collinear star is not itself an obstruction to linear small-ball scale.

## 5. Required pinned mixed-hub theorem applied to a real dense same-side star

The required completed Theorem H from

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`

is now applied at an actual target inequality, without any decoupling square root.

Let `m>=8` and choose flat orthonormal Walsh vectors `c,d,v in R^m`. With two literal physical hubs `a,b`, set on the principal coordinates `H union I`

`F_m = X_a^2
     + 2 X_a <c,Y>
     + 2 X_b <d,Y>
     + <v,Y>^2`.                                                 (5.1)

The leaf same-side block `vv^T` is dense in the physical coordinates. The mixed rows are

`rho_i=(v_i,c_i,d_i)`,

so their Gram is `I_3` and every physical leverage is `3/m<=1/2`. Theorem H with two hubs and one Fresnel square gives

`|phi_(F_m)(t)| <= 8 pi^(5/2) |t|^(-5/2)`.                      (5.2)

Integrating `min(1,K|t|^(-5/2))` exactly and using Fourier inversion gives

`boxed:
 ||p_(F_m)||_infinity
 <= (5/3) 2^(6/5)
 = 3.828994516656783...`.                                        (5.3)

Therefore

`P{F_m in J} <= (5/3)2^(6/5)|J|`.                               (5.4)

The principal spectrum decomposes into

`{(1+sqrt(5))/2, (1-sqrt(5))/2} union {1,-1} union {1}`,

plus zeros, hence it contains at least three eigenvalues of modulus at least one. Moreover Theorem H permits arbitrary blocks `A_HJ,A_IJ,A_JJ` on a further disjoint bank `J`; conditioning `J` leaves the estimate unchanged. Thus arbitrary dense same-side curvature and couplings on that conditioned bank are retained rather than deleted. The fixed principal block already supplies the target spectral hypothesis, so arbitrary extensions remain target-valid by interlacing.

This is the requested mixed-hub smoothing on a literal source-coordinate star: no post-rotation independence and no square-root decoupling loss.

## 6. Latest designated account03/B09 result applied to an actual inequality

The newest completed account03/B09 handoff available in this run is r42,

`math-open-problems@6642b95f1b9f447bdb961c5cbebe5b7d003faa20`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T215045Z-account03-B09-QFORM-r42/REPORT.md`.

For a physical three-coordinate bank with rank-two cross block it proves, for every `p>2`,

`||p_Q||_infinity
 <= C_p Delta^(-p/[2(p+1)]) ||Pn||^(-1/(p+1))`,                 (6.1)

with the explicit `C_p` in that report.

Apply it to

`Q_s = 2s Y1 Y3 + 2 Y1 Z1 + 2 Y2 Z2`.                           (6.2)

Here the physical cross block from `(Y1,Y2,Y3)` to `(Z1,Z2)` has `Delta=1`, its kernel is `e3`, and `||P e3||=s`. The full spectrum is

`{+sqrt(s^2+1),-sqrt(s^2+1),+1,-1,0}`,                          (6.3)

so this is target-valid. Taking `p=5/2` gives

`C_(5/2)=6.965474689127744...`,
`||p_(Q_s)||_infinity <= 6.9654746892 s^(-2/7)`.                 (6.4)

At `s=32`,

`boxed: ||p_(Q_32)||_infinity <= 2.5876639023`,                  (6.5)

with a continuous density and the same coefficient multiplying interval length. This improves the previous fixed-`p=4`/kernel-derivative power on this genuine source-coordinate family. The partner's stress family also shows that the anisotropy ratio cannot be bounded from `s_3(A)>=1` alone; that is a structural obstruction, not a QFORM counterexample.

## 7. What the rank-one overlap ledger now says

At an exact rank-one pair core, overlap-two mass has the factorised kernel-star form (3.4). There are now two paid endpoint geometries:

1. **Collinear star, zero active leaf curvature:** Theorem 4.1 pays it directly at the linear small-ball scale, in fact by `6 Omega_2^(-1/6)` whenever `Omega_2>0`.
2. **Transverse diffuse mixed frame with low-rank-plus-diagonal active leaf curvature:** the pinned Theorem H pays the source-coordinate star without decoupling; (5.1) is a target-valid dense same-side example.

A useful source-valid obstruction is immediate: large `Omega_(2,H)` does not imply a positive two-hub Gram determinant. In (4.8), `Omega_(2,H)->1` while the cross Gram has determinant zero. Therefore the global overlap-two compiler cannot close the singular collar merely by invoking a two-hub determinant receiver. It must use the internal rank-one square plus the effective kernel hub, or spend genuinely transverse leaf curvature before taking absolute values.

The remaining difficult branch is exactly when general same-leaf curvature is entangled with that one effective kernel-star projection (or when the physical core is only near rank one). The present proof does not condition that curvature away and does not interpret small coefficient norm as a small random perturbation.

## 8. Counterexample status

The required pinned `COUNTEREXAMPLE_SEARCH.md` still reports no valid counterexample to the unrestricted conjecture, and the current version read in this run still reports none. This run found no full-target counterexample. The constructions above refute only intermediate structural shortcuts and provide paid target-valid subclasses.
