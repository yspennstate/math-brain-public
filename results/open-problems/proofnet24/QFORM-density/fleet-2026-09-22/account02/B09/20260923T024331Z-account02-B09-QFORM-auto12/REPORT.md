SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-23T02:43:31Z.
attacking: mixed-hub smoothing on a source-coordinate star with dense same-side couplings; seek a quantitative star-vs-curvature routing certificate and direct linear small-ball bound without square-root decoupling.

# account02/B09 auto12 — two zero-core physical hubs absorb arbitrary same-side curvature

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T024331Z-account02-B09-QFORM-auto12`  
Role: Bilinear block mechanism / complementary constructions and source-valid counterexamples  
Status: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / PARTNER RESULT APPLIED / FULL TARGET OPEN**  
Execution label: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. Nothing below claims that the spectral hypothesis alone forces the new certificate. The contribution is an exact product-preserving endpoint for a hub/star geometry that the preceding one-hub mixed-frame theorem did not cover: two source-coordinate hubs with zero physical core and transverse full rows smooth **arbitrary** quadratic curvature on the entire complementary bank.

## 1. First unpaid implication

The first B09 implication is now

`QFORM-ZERO-HUBPAIR-WEDGE-OR-EXTERNAL-THIRD-v1`:

> In the no-pivot/hub survivor, route the matrix to one of: (i) two original-coordinate hubs whose physical 2x2 core is exactly zero and whose full complementary coupling rows have a quantitatively nondegenerate wedge; (ii) the already-paid mixed-Hub/Fresnel low-rank-plus-diagonal frame, cross-volume/ridge, pair, or transverse-rank-three exits; or (iii) a genuinely nonzero hub self/mutual core for which a third source-compatible smoother must remain unconditioned. Do not delete a small nonzero hub-core coefficient and do not replace the third direction by post-rotation independence.

The theorem below pays branch (i) while retaining the whole complementary quadratic operator. A rank-two product regression in Section 6 shows why an arbitrary nonzero hub core cannot simply be folded into the same proof.

## 2. Sources consumed at equations

Fresh control was QFORM-only with OWNER CONTROL revision `2026-09-22.15`. The live correction ledger was reread before publication. In particular, the proof does not use law-uniform pointwise quadratic-phase decay, an arbitrary-joint three-dimensional coarea bound, a conditional spectral-density supremum, a positive conditional-density moment, post-rotation independence, deletion of a small quadratic coefficient, or a single-good-minor implication.

The required newest compatible Claude package was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its Theorem H is applied to an actual target-valid inequality in Section 5.

For the two-dimensional product marginal used in the new theorem I use the source-pinned LPP statement recorded in the current synthesis

`yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`

`proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`:
any orthogonal two-dimensional marginal of a product of cap-one one-dimensional densities has density at most `2`. This is a joint-density statement; it does **not** assert independence of the projected coordinates.

A related but complementary current theorem is account01/B09's `QFORM-TWOHUB-PHYSICAL-STAR-DIFFUSE-v1`, source snapshot

`yspennstate/math-open-problems@65e50ba0b12d5aff76bd5b4f3e44db2d01d07d0a`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/20260923T021354Z-account01-B09-QFORM-auto11/REPORT.md`.
It gives `4 W^{-1/4}` for two hubs when the remaining leaf self-block is diagonal and the mixed rows have leverage at most `1/2`. The theorem below makes the opposite trade: it assumes the physical two-hub core is exactly zero, but then permits a completely arbitrary dense complementary quadratic block and imposes no leverage condition.

The latest completed designated partner result actually available was account03/B09
`QFORM-DOUBLE-NULL-TRANSVERSE-RANK3-OR-GLOBAL-KERNEL-v1`, source snapshot

`yspennstate/math-open-problems@b81d91f2d8a5d0de6f7dfe468158ef0cd4b858c3`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T014949Z-account03-B09-QFORM-auto11/REPORT.md`.
It is applied to an explicit target family in Section 5.2.

## 3. Main theorem: arbitrary remainder behind a zero two-hub core

Let the independent original coordinates be split as

`{h,s} union K`.

Allow arbitrary affine terms. Assume only

`A_hh=A_ss=A_hs=0`.                                             (3.1)

Put

`u=A[K,h]`, `v=A[K,s]`,

and define the full-row wedge currency

`Delta = ||u||_2^2 ||v||_2^2 - <u,v>^2`.                       (3.2)

Equivalently, by Cauchy--Binet,

`Delta = sum_{i<j in K} (u_i v_j-u_j v_i)^2`.                  (3.3)

Thus `Delta` aggregates all transverse source-coordinate star mass before any reciprocal local minor is paid.

### Theorem 3.1 — `QFORM-ZERO-HUBPAIR-ARBITRARY-REMAINDER-v1`

If `Delta>0`, then for every collection of independent input densities bounded by one and every symmetric complementary block `A_KK`, with arbitrary affine terms,

`boxed:
||p_Q||_infinity <= 2 sqrt(2) Delta^(-1/4).
`                                                                    (3.4)

In particular every interval `L` satisfies the direct linear small-ball estimate

`boxed:
P{Q in L} <= 2 sqrt(2) Delta^(-1/4) |L|.
`                                                                    (3.5)

The output density is in fact continuous. No moment, support, centering, identical-law, log-concavity, or smoothness assumption is used. The whole operator `A_KK` is retained exactly.

### Proof

Write the affine coefficients of `X_h,X_s` as `2 alpha,2 beta`; absorb the remaining affine and constant terms into `H`. From (3.1), exactly

`Q = 2 X_h U + 2 X_s V + H(X_K)`,                              (3.6)

where

`U=<u,X_K>+alpha`,
`V=<v,X_K>+beta`,                                             (3.7)

and `H` is an arbitrary quadratic-affine function of all coordinates in `K`. In particular, `H` may contain every dense same-side coupling in `A_KK` and may be arbitrarily dependent on `(U,V)`.

Because `Delta>0`, the two coefficient rows `u,v` are linearly independent. Let

`G=[[||u||^2,<u,v>],[<u,v>,||v||^2]]`,

so `det G=Delta`. The map `X_K -> (U,V)` is an invertible two-dimensional linear scaling of an orthogonal two-dimensional projection of the original product source. The LPP two-dimensional marginal theorem therefore gives the joint-density cap

`||p_(U,V)||_infinity <= M := 2/sqrt(Delta)`.                  (3.8)

No independence between `U` and `V` is claimed or needed.

Now condition on the entire original-coordinate bank `X_K`. Then `U,V,H` are constants, while `X_h` and `X_s` remain independent with their original density caps. If `U,V !=0`, the two summands `2U X_h` and `2V X_s` have density caps respectively `1/(2|U|)` and `1/(2|V|)`. Young's convolution inequality gives

`||p_(Q|X_K)||_infinity
 <= min{1/(2|U|),1/(2|V|)}
 = 1/[2 max(|U|,|V|)].`                                      (3.9)

The same formula, with `1/0=+infinity`, gives the correct one-dimensional bound when exactly one coefficient vanishes. Since `(U,V)` has a joint density, the event `U=V=0` has probability zero.

Set

`R=max(|U|,|V|)`.

The square `[-r,r]^2` has area `4r^2`, so (3.8) implies

`P(R<=r) <= min(1,4 M r^2)`.                                  (3.10)

Layer cake now yields the integrable reciprocal coefficient bound

`E R^(-1)
 = integral_0^infinity P(R<1/t) dt
 <= integral_0^infinity min(1,4M/t^2) dt
 =4 sqrt(M).`                                                  (3.11)

Averaging (3.9),

`||p_Q||_infinity
 <= (1/2) E R^(-1)
 <=2 sqrt(M)
 <=2 sqrt(2) Delta^(-1/4),`                                   (3.12)

which proves (3.4), and (3.5) follows by integration over `L`.

For continuity, for almost every `X_K` both `U` and `V` are nonzero and the conditional density is a translate of a convolution of two `L^1` densities, hence continuous in the output variable. Equation (3.9) is dominated by the integrable random variable `(2R)^{-1}` from (3.11). Dominated convergence therefore shows that the mixture density is continuous. QED.

### What the proof spends

The smoothing resource is not a selected `2x2` minor. It is the **entire two-row wedge** (3.3). The only reciprocal singularity after conditional linear anti-concentration is `1/max(|U|,|V|)`, and a two-dimensional joint-density cap is exactly strong enough to integrate it. This is why the interval exponent stays one. There is no Cauchy--Schwarz probability squaring, no resampled square-root loss, and no worst conditional spectral-density supremum.

## 4. A target-valid diffuse same-side-curvature family

Let `m=2^k` with `k>=3`, and on an `m`-coordinate original leaf bank choose three orthonormal Walsh vectors `c,d,w`, each with entries `+/-m^{-1/2}`. Take two additional original-coordinate hubs `h,s` and define

`Q_m = 2 X_h <c,Y> + 2 X_s <d,Y> + <w,Y>^2`.                 (4.1)

In the orthonormal grouped basis generated by

`{e_h,c,e_s,d,w}`,

the coefficient matrix is the orthogonal direct sum of two hyperbolic blocks

`[[0,1],[1,0]]`

and one scalar block `[1]`. Hence

`spec_nonzero(A_m)={1,-1,1,-1,1}`.                            (4.2)

This is a literal target family, with five eigenvalues of modulus at least one. Nevertheless every physical hub-leaf coefficient is only `m^{-1/2}`, while the dense same-side leaf block `w w^T` has entries of magnitude `m^{-1}`. Every physical diagonal is `0` or `1/m`; every hub-leaf `2x2` principal determinant has magnitude `1/m`; every leaf-leaf determinant of the rank-one same-side block is zero. Thus for every fixed no-pivot threshold `tau>0`, sufficiently large `m` lies in the strict no-small-physical-pivot chamber.

Here `u=c`, `v=d`, so

`Delta=1`.                                                     (4.3)

Theorem 3.1 therefore gives, for every admissible independent cap-one product law and every `m`,

`boxed: ||p_(Q_m)||_infinity <= 2 sqrt(2) < 2.829.`            (4.4)

More importantly, the analytic theorem would remain valid if `w w^T` in (4.1) were replaced by **any** symmetric quadratic operator on the leaf bank. The target-valid rank-one choice is used only to exhibit the three-large-eigenvalue hypothesis explicitly.

## 5. Required completed results applied to actual inequalities

### 5.1 Required e5f Theorem H: one physical hub plus dense same-side rank two

Take a Walsh bank of size `m>=8` and three orthonormal flat vectors `c,v_1,v_2`. On one additional original-coordinate hub define

`F_m=2 X_h<c,Y> + <v_1,Y>^2 + <v_2,Y>^2`.                    (5.1)

This has compressed spectrum

`{1,-1,1,1}`,                                                 (5.2)

so it is target-valid. The same-side operator `v_1v_1^T+v_2v_2^T` is dense.

Apply Theorem H from the required `e5f71d79.../RESULTS.md` with one source-coordinate hub, rank `r=2`, `lambda_1=lambda_2=1`, and augmented leaf rows

`rho_i=((v_1)_i,(v_2)_i,c_i)`.

Their Gram matrix is `I_3`, and each leverage equals `3/m<=1/2`. The source theorem gives at the actual equation

`|phi_F(t)|
 <= (2|t|)^(-1) (4 pi |t|)^(-1) (4 pi)^3
 = 8 pi^2 |t|^(-2).`                                         (5.3)

Therefore

`integral_R |phi_F(t)| dt
 <= integral_R min(1,8pi^2/t^2) dt
 = 8 sqrt(2) pi`,                                             (5.4)

and Fourier inversion yields

`boxed: ||p_(F_m)||_infinity <=4 sqrt(2)<5.657.`              (5.5)

This is a direct application of the newest-source mixed-hub smoothing result to an actual source-coordinate star with dense same-side couplings, not a copied theorem statement.

### 5.2 Latest designated partner account03/B09 applied

Let the three-coordinate left bank be `(x,u_1,u_2)` and the right bank `(v_1,v_2,y_1,...,y_m)`. Put

`M_m=
[[1,0,m^(-1/2),...,m^(-1/2)],
 [1,0,0,...,0],
 [0,1,0,...,0]]`

and take the pure bipartite form

`T_m=2 (x,u_1,u_2) M_m (v_1,v_2,y_1,...,y_m)^T`.             (5.6)

For the partner's double-null notation one has `B=I_2`, `kappa=e_1`, and the aggregate transverse vector

`tau=m^(-1/2)(1,...,1)`, so `||tau||_2=1`. The partner theorem gives the actual bound

`boxed: ||p_(T_m)||_infinity <=3 sqrt(e)<4.947`,              (5.7)

and hence `P{T_m in L}<=3sqrt(e)|L|`.

Indeed

`M_m M_m^T=[[2,1,0],[1,1,0],[0,0,1]]`,

whose singular values are `phi,1,phi^(-1)`, `phi=(1+sqrt(5))/2`. Thus the nonzero spectrum of the symmetric bipartite matrix is

`{+phi,+1,+phi^(-1),-phi,-1,-phi^(-1)}`,                     (5.8)

so four eigenvalues have modulus at least one. Each individual transverse coefficient tends to zero as `m^-1/2`, while the partner's aggregate norm stays one. This is the same aggregate-before-inversion principle as Theorem 3.1, through a complementary rank-three cross-bank mechanism.

## 6. Sharp qualitative regressions for the next routing step

### 6.1 Wedge collapse

The condition `Delta>0` cannot be discarded in an arbitrary-remainder theorem. Let `X_h,X_s,Y` be independent `Uniform[-1/2,1/2]` and set

`Q=2Y(X_h+X_s)`.                                               (6.1)

The two full hub rows are collinear, so `Delta=0`. The triangular variable `X_h+X_s` has a density positive at zero and is independent of `Y`; their product has a logarithmically unbounded density at zero. The quadratic matrix has rank two, so this is not a QFORM counterexample. It is the mandatory rank-two regression showing that a transverse third source direction must be retained when the wedge collapses.

### 6.2 A nonzero hub mutual edge is not a harmless perturbation

Let `X_1,X_2,Y_1,Y_2` be iid `Uniform[-1/2,1/2]` and take

`Q=(X_1+Y_1)(X_2+Y_2)`.                                      (6.2)

Relative to hubs `X_1,X_2`, the two complementary coupling rows are transverse, but the hub mutual coefficient is nonzero. The two factors in (6.2) are independent, each has a continuous density positive at zero, so their product again has a logarithmically unbounded density. The coefficient matrix has spectrum `{1,-1,0,0}``, hence this is again a rank-two obstruction rather than a QFORM counterexample.

This exact factorization proves that Theorem 3.1 must not be extended to an arbitrary nonzero hub core merely by continuity or by deleting a small coefficient. A target proof in that chamber must explicitly spend an external third spectral/product resource.

## 7. Comparison with preceding B09 progress

The preceding account02/B09 theorem `QFORM-ONE-HUB-RANKR-MIXEDFRAME-v1` pays

`A_II=D+sum lambda_k v_kv_k^T`

when the augmented one-hub frame is diffuse. It allows arbitrary hub self-curvature and arbitrary outside blocks, but its leaf operator must be diagonal plus low rank. Account01/B09's current two-hub star theorem pays a two-hub diffuse frame when the remaining leaf self-block is diagonal.

Theorem 3.1 occupies the missing complementary corner: the two-hub core is exactly zero, while the leaf/complement operator is **completely arbitrary**, the random shift `H` may be fully correlated with `(U,V)`, and no mixed-row leverage bound is needed. This is precisely the product-preserving use of conditional linear anti-concentration requested for the B09 mechanism.

It does not close N3 because the bare spectral hypothesis has not been shown to force an exact zero two-hub core with `Delta` bounded below. The next proof obligation is structural: force this new exit, an already-paid diffuse/ridge/pair/cross-volume exit, or retain a quantitative external third resource through a genuinely nonzero hub core.

## 8. Status

- `QFORM-ZERO-HUBPAIR-ARBITRARY-REMAINDER-v1`: complete supporting proof supplied here; independent review not yet performed.
- Required `e5f71d79...` mixed-hub Theorem H: applied to (5.1)-(5.5).
- Latest completed account03/B09 theorem: applied to (5.6)-(5.8).
- Full QFORM target: **OPEN**.
- Essential boundedness: proved in the stated branches.
- Continuity: proved for Theorem 3.1 and for the two applied Fourier/partner branches; global continuity remains separate and open.
