SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B09, 2026-09-24T00:14:51Z.
attacking: global aggregation of the one-shared/two-shared third-compound sectors into a source-coordinate bilinear block or a bounded literal collar.

# fleet01/B09 — V-phase-stable square–hyperbola receiver and no-pivot-loss rank-one cross packet

Status: **NEW SUPPORTING THEOREMS / ESSENTIAL STEP APPLIED / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

This run stays on the exact owner target. No Gaussian, log-concavity, moment, compact-support, connected-support, spectral-coordinate independence, or diagonal-basis assumption is introduced. The results below are supporting receivers; they do not prove or disprove the unrestricted conjecture.

## 1. New analytic lemma: arbitrary V-only phase costs nothing

### Theorem 1 — `QFORM-JOINT2-SQUARE-HYPERBOLA-VPHASE-STABLE-v1`

Let `(U,V)` have an arbitrary joint probability density `rho` on `R^2` satisfying `rho<=M`. Let `W` be independent of `(U,V)` and have a probability density bounded by `S`. Let `H:R->R` be arbitrary measurable and let `a,b` be nonzero real numbers. Then

`T = a U^2 + H(V) + 2 b V W`

has an essentially bounded density satisfying

`||p_T||_infinity <= 3*2^(2/3) M^(2/3) S^(2/3) |a|^(-1/3)|b|^(-2/3)`.      (1.1)

The same coefficient gives

`P{T in I} <= C |I|`                                                   (1.2)

for every interval `I`. Continuity is **not** asserted.

This strictly extends fleet02/B09's completed square–hyperbola receiver, which is the special case `H=0`, without changing its constant.

### Proof

It suffices first to prove `a=b=1`; scaling is handled at the end. Split the pushforward density into the regions `|V|<=r` and `|V|>r`.

On `|V|<=r`, integrate in `U`. For fixed `(v,w)`, the two roots of

`u^2 = t-H(v)-2vw`

contribute at most

`M (t-H(v)-2vw)_+^(-1/2)`.                                            (1.3)

For any probability density `f<=L`, the one-sided inverse-half bathtub bound is

`sup_c int (c-z)_+^(-1/2) f(z) dz <= 2 sqrt(L)`.                       (1.4)

Indeed the decreasing singular kernel is maximized by placing density `L` on the interval `[c-1/L,c]`, giving `L int_0^(1/L) s^(-1/2) ds=2 sqrt(L)`.

For fixed `v!=0`, the variable `2vW` has density at most `S/(2|v|)`. Hence (1.4), with the arbitrary number `H(v)` merely translating the target, gives

`E_W (t-H(v)-2vW)_+^(-1/2) <= sqrt(2S/|v|)`.                          (1.5)

Therefore the small-`V` contribution is at most

`M sqrt(2S) int_{-r}^r |v|^(-1/2) dv
 = 4 sqrt(2) M sqrt(Sr)`.                                             (1.6)

On `|V|>r`, integrate first in `W`. For each `(u,v)` the affine map

`w -> u^2+H(v)+2vw`

has derivative `2v`, so the density contribution is at most `S/(2|v|)<=S/(2r)`. Integrating the hub density, whose total mass is one, gives

`large-V contribution <= S/(2r)`.                                    (1.7)

Thus

`||p_T||_infinity <= 4 sqrt(2) M sqrt(Sr) + S/(2r)`.                  (1.8)

The optimum satisfies

`r^(3/2)=sqrt(S)/(4 sqrt(2)M)`,                                       (1.9)

and substitution gives

`3*2^(2/3) M^(2/3) S^(2/3)`.                                         (1.10)

For general `a,b`, put `U~=sqrt(|a|)U` and `W~=|b|W` (absorbing signs into `H`/the target). The joint cap becomes `M/sqrt(|a|)` and the scalar cap becomes `S/|b|`; (1.1) follows. The same split applied to interval indicators gives (1.2). QED.

### Robustness actually proved

The theorem permits **arbitrary measurable curvature/phase in the effective hub coordinate `V`**, including `sigma V^2+cV+d`. It also permits an independent additive random variable by convolution. It does **not** permit an arbitrary function of the same leaf variable `W`; that is precisely where the current entangled-leaf-curvature problem remains.

## 2. New physical-pair theorem: arbitrary pair core, rank-one physical cross, zero active leaf curvature

### Theorem 2 — `QFORM-RANKONE-CROSS-ARBITRARY-PAIRCORE-v1`

Let `H={h1,h2}` be two literal original coordinates and `I=H^c`. Assume, on these active coordinates,

`A = [[B, g r^T], [r g^T, 0]]`,                                      (2.1)

where `B` is an arbitrary real symmetric `2x2` matrix, `g in R^2\{0}`, and `r in R^I\{0}`. Equivalently, the physical pair-to-leaf cross block has rank one. Define

`kappa_g = g^T adj(B) g`.                                             (2.2)

If `kappa_g !=0`, then for arbitrary independent original-coordinate inputs of density at most one,

`||p_(X^T A X)||_infinity
 <= 6 |kappa_g|^(-1/3) ||r||_2^(-2/3)`.                              (2.3)

The same coefficient multiplies interval length. Continuity is not claimed.

Most importantly, (2.3) has **no factor involving `det(B)` or `sigma_min(B)`**. It remains uniform as the second eigenvalue of the physical pair crosses through zero.

### Proof

Let `J=[[0,-1],[1,0]]` and put

`e = Jg/||g||`, `v=g/||g||`.

The orthogonal coefficient-space change `(X_H)->(U,V)=(e^T X_H,v^T X_H)` is performed only inside the two-dimensional hub integral. The transformed hub has an arbitrary joint density bounded by one; no independence of `U,V` is asserted. The cross term is exactly

`2 ||g|| V W`, `W=r^T X_I`.                                          (2.4)

The `U^2` coefficient of the transformed hub quadratic is

`a=e^T B e=(g^T adj(B)g)/||g||^2=kappa_g/||g||^2`.                  (2.5)

Write the transformed pair quadratic as

`aU^2+2cUV+dV^2`.

Since `a!=0`, the area-preserving shear

`U'=U+(c/a)V`, `V'=V`                                                (2.6)

removes the mixed hub term and leaves

`a U'^2 + (d-c^2/a)V^2 + 2||g|| V W`.                               (2.7)

The joint hub density remains bounded by one. The reviewed one-dimensional product-projection estimate used by fleet02/B09 gives

`||p_W||_infinity <= sqrt(2)/||r||_2`.                              (2.8)

Apply Theorem 1 with

`M=1`, `S=sqrt(2)/||r||_2`, `b=||g||`, and `H(V)=(d-c^2/a)V^2`.

Because `a=kappa_g/||g||^2`, all `||g||` factors cancel and the constant becomes exactly `6`, proving (2.3). QED.

## 3. Exact overlap-two identity and packet payment

For the pair `H`, the exact Schur-numerator identity from the preceding B09 run is

`N_H = det(B) D - U adj(B) U^T`,                                    (3.1)

where `U=A[I,H]` and `D=A[I,I]`. In Theorem 2, `D=0` and `U=r g^T`, hence

`N_H = -kappa_g r r^T`.                                               (3.2)

For distinct leaves `i!=j`,

`det A[H union {i}, H union {j}] = -(kappa_g) r_i r_j`.              (3.3)

With the ordered-pair convention used in the overlap ledger,

`Omega_(2,H)
 = kappa_g^2 [ (sum_i r_i^2)^2 - sum_i r_i^4 ]`.                    (3.4)

Consequently

`Omega_(2,H) <= kappa_g^2 ||r||_2^4`,                               (3.5)

and Theorem 2 implies the pivot-free packet estimate

`boxed: ||p_Q||_infinity <= 6 Omega_(2,H)^(-1/6)`                    (3.6)

whenever `Omega_(2,H)>0`.

Thus, in the exact zero-active-leaf-curvature/rank-one-cross geometry, **overlap-two mass is paid uniformly through singular, near-singular, definite, and indefinite physical pair cores**. The small second pair eigenvalue itself is not an obstruction. What remains is the entangled same-leaf curvature and/or genuinely higher-rank transverse cross geometry.

## 4. Designated fleet02/B09 result applied at an actual inequality

The newest completed fleet02/B09 handoff read in this run is r15, canonical mathematics

`yspennstate/math-open-problems@57b57dc6fa114b1c782a91599bdfbe94a358b2cb`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260923T224553Z-fleet02-B09-QFORM-r15/REPORT.md`.

Its Theorem 2.1 states

`||p_(aU^2+2bVW)||_infinity
 <=3*2^(2/3) M^(2/3)S^(2/3)|a|^(-1/3)|b|^(-2/3)`                    (4.1)

for joint hub cap `M` and an independent scalar factor of cap `S`.

Take eight leaves and

`B_0=diag(8,0)`,
`r_i=2/sqrt(8)`,
`A[I,H]=r e_2^T`,
`A[I,I]=0`.                                                         (4.2)

Then `||r||_2=2`, so the projection `W=r^T X_I` has density at most `S=sqrt(2)/2=1/sqrt(2)`. Apply the partner theorem with `M=1`, `a=8`, `b=1`:

`||p_Q||_infinity
 <=3*2^(2/3)*(1/sqrt(2))^(2/3)*8^(-1/3)
 =(3/2)2^(1/3)
 =1.8898815748423097...`.                                           (4.3)

This is a literal target-valid inequality: the active spectrum at `sigma=0` is `{8,2,-2}` plus zeros.

Now replace the zero second pair eigenvalue by an arbitrary `sigma`:

`B_sigma=diag(8,sigma)`.                                             (4.4)

Theorem 1 absorbs the new term `H(V)=sigma V^2` with **exactly the same bound (4.3)**. For every `|sigma|<=1`, the two nontrivial star-block eigenvalues are

`(sigma +- sqrt(sigma^2+16))/2`,                                    (4.5)

whose smaller absolute value is at least

`(sqrt(17)-1)/2 = 1.5615528128...>1`.                               (4.6)

Hence the entire family is in the owner's three-large-eigenvalue target and

`boxed: ||p_(Q_sigma)||_infinity <1.890`,
`boxed: P{Q_sigma in J}<1.890 |J|`                                  (4.7)

for every `|sigma|<=1`, uniformly through the singular transition `sigma=0`.

On the same family,

`Omega_(2,H)=8^2 [ 2^4 - 8*(2/sqrt(8))^4 ]=896`,                    (4.8)

independent of `sigma`, consistent with (3.2)-(3.4).

## 5. What this changes in the global Omega_2 frontier

The previous unpaid implication was `QFORM-OMEGA12-AGGREGATE-BEFORE-PIVOT-INVERSION-v1`. Theorem 2 removes one genuine source of reciprocal-pivot loss:

* if a concentrated overlap-two packet has zero active leaf curvature and rank-one physical pair-to-leaf cross, **no inversion of the physical pair core is needed at all**;
* the exact packet is paid by `6 Omega_(2,H)^(-1/6)` even while `det(B)` passes through zero;
* therefore the singular/near-singular pair collar can no longer be blamed on the small second pair eigenvalue in this rank-one-cross endpoint.

The remaining first unpaid implication is more specific:

`QFORM-OMEGA2-RANKONECROSS-ENTANGLED-LEAFCURVATURE-OR-TRANSVERSE-EXIT-v1`:

> Starting from a concentrated overlap-two packet, retain arbitrary same-active-leaf curvature when the pair-to-leaf cross is rank one or near rank one, or force a transverse projected-crossing / grouped-hub / fixed-volume exit. The new theorem already handles every pair-core sign and singularity in the zero-active-leaf-curvature endpoint, so the next argument should spend the leaf curvature itself rather than invert the pair pivot.

A tempting stronger statement with an arbitrary function of the *same* star variable `W` has **not** been proved here; the bathtub step only survives arbitrary `V`-only translations. This distinction is important under the live correction against unsupported conditional-density assumptions.

## 6. Continuity and full-target status

Theorem 1 and Theorem 2 establish an essentially bounded density and direct `O(|I|)` interval anti-concentration. Continuity is not separately established for these receivers. The unrestricted owner target, including full-target continuity, remains **OPEN / not proved / not disproved**.
