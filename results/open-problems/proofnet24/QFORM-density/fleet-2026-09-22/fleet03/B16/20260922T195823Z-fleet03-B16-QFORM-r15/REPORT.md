SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B16, 2026-09-22T19:58:23Z.

attacking: an unnormalized projection-product Fourier interface that retains original-coordinate product structure after quadratic decoupling.

# fleet03/B16 — unnormalized ambiguity-kernel budget and an exact three-map Brascamp–Lieb obstruction

**Run:** `20260922T195823Z-fleet03-B16-QFORM-r15`  
**Status:** `SUPPORTING_THEOREM + REFUTED_NAIVE_ASSEMBLY / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full QFORM conjecture remains OPEN. Continuity of the full output density is not proved here. This run changes mechanism from the previous physical-pivot case split to a product-preserving Fourier/decoupling interface, in response to the live all-positive conditional-height obstruction.

## 1. Source state and partner result actually used


The designated partner result actually used is fleet04/B16, run `20260922T191443Z-fleet04-B16-QFORM-r3`, canonical report

`yspennstate/math-open-problems:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B16/20260922T191443Z-fleet04-B16-QFORM-r3/REPORT.md`.

For its two diffuse uniform blocks, if `M_m(Z)=||rho_{Y|Z}||_infinity`, then for every `0<alpha<2`

`E M_m(Z)^alpha = [m^(-alpha/2) Gamma(m+1) Gamma(2-alpha)/Gamma(m+1-alpha)]^2`

and hence `E M_m^alpha ~ Gamma(2-alpha)^2 m^alpha -> infinity`; for `alpha>=2` the moment is already infinite at fixed `m`. Therefore a replacement interface should not normalize by the conditional fiber mass and then pay a positive height moment.

## 2. Unnormalized one-coordinate ambiguity kernel

Let `f` be any probability density on `R` with `0<=f<=1`. Define

`k_f(u,v) = (1/2) f((v+u)/2) f((v-u)/2)`

and its Fourier transform only in the `v` variable

`K_f(u,xi) = integral_R exp(i xi v) k_f(u,v) dv`.

Also set

`q_f(u)=K_f(u,0)=integral_R f(x)f(x-u) dx`.

The key point is that `K_f` is **unnormalized**. It contains the difference-fiber mass `q_f(u)` rather than dividing by it.

### Theorem 1 — `QFORM-UNNORMALIZED-AMBIGUITY-LP-v1`

For every cap-one probability density `f`:

1. `0<=q_f(u)<=1` and `integral q_f(u)du=1`;
2. `|K_f(u,xi)|<=q_f(u)` for every `(u,xi)`;
3. for every `p>=2`,

`integral_R integral_R |K_f(u,xi)|^p dxi du <= pi`.

In particular

`||K_f||_(L^2(R^2)) <= sqrt(pi)`

with a constant independent of support fragmentation, moments, centering, and dimension.

If `f=1_E` for any measurable set `E` of Lebesgue measure one, then the `p=2` estimate is an exact identity:

`integral integral |K_f|^2 = pi`.

Thus even the phase-aligned fragmented indicator laws that defeat law-uniform pointwise van der Corput decay have the same finite unnormalized `L^2` ambiguity budget.

### Proof

The identities for `q_f` follow by the substitution `v=2x-u`:

`q_f(u)=integral f(x)f(x-u)dx`.

Since `f(x-u)<=1`, `q_f(u)<=integral f=1`, and Fubini gives `integral q_f=1`. The triangle inequality gives `|K_f|<=q_f`.

With Fourier convention `hat h(xi)=integral exp(i xi v)h(v)dv`, Plancherel gives, for fixed `u`,

`integral |K_f(u,xi)|^2 dxi = 2pi integral k_f(u,v)^2 dv`.

Because both density factors lie in `[0,1]`,

`k_f(u,v)^2 <= (1/2) k_f(u,v)`.

Hence

`integral |K_f(u,xi)|^2 dxi <= pi q_f(u)`.

For `p>=2`, use `|K_f|^(p-2)<=q_f(u)^(p-2)`:

`integral |K_f(u,xi)|^p dxi <= pi q_f(u)^(p-1)`.

Now `0<=q_f<=1`, so integrating `u` gives at most `pi integral q_f=pi`.

If `f=1_E`, then `f^2=f`, so `k_f^2=(1/2)k_f` almost everywhere. The Plancherel inequality is then equality, and integration in `u` gives exactly `pi`. QED.

## 3. Exact quadratic decoupling identity with no conditional density normalization

Let `X=(X_1,...,X_n)` have independent coordinate densities `f_j<=1`, let `X'` be an independent copy, let `A=A^T`, and

`phi_A(t)=E exp(i t X^T A X)`.

Put `u=x-x'`, `v=x+x'`. The Jacobian is `2^(-n)` and

`x^T A x - x'^T A x' = u^T A v`.

Therefore the preceding kernels tensorize to the **exact identity**

`|phi_A(t)|^2
 = integral_(R^n) product_(j=1)^n K_(f_j)(u_j, t(Au)_j) du`.       (3.1)

No independence is asserted after an eigenvector rotation. No conditional density of `V=X+X'` given `U=X-X'` is normalized. If one did normalize, the denominator would be precisely `q_f(u)` and could be arbitrarily small; (3.1) instead keeps that small fiber mass in the integral.

This directly answers the partner obstruction at the level of the primitive object: the partner family has divergent **normalized** conditional projection-height moments, while every original uniform indicator coordinate in that same family satisfies the exact finite identity

`integral integral |K_f(u,xi)|^2 dxi du = pi`.                         (3.2)

The new interface therefore avoids the exact source of the `m^alpha` blowup in fleet04/B16. This is a genuine inequality applied to the partner family, not a claim that (3.1) is already enough to close QFORM.

## 4. First attempted assembly and exact obstruction

A natural attempt is to select three physical coordinates and combine Theorem 1 with a three-map Loomis–Whitney/Brascamp–Lieb estimate. This would be attractive because three `L^2(R^2)` factors on a three-dimensional `u`-space have exactly the formal scaling needed for a `|t|^(-3/2)` gain.

I test that implication immediately.

Let `B=(b_jk)` be the symmetric `3x3` physical block on the selected coordinates. After the outside `u` variables are fixed, each selected kernel is evaluated on the affine rank-two map

`L_j^t(u)=(u_j, t(Bu)_j + c_j)`, `j=1,2,3`.

Translations `c_j` do not affect the Brascamp–Lieb datum. Ignoring the harmless scalar `t`, the two row covectors of `L_j` are `e_j^T` and the `j`th row `b_j^T`. When they are independent, a kernel direction is

`n_j=e_j cross b_j`.

For symmetric

`B=[[b11,b12,b13],[b12,b22,b23],[b13,b23,b33]]`,

the three kernel directions are

`n_1=(0,-b13,b12)`,
`n_2=(b23,0,-b12)`,
`n_3=(-b23,b13,0)`.

Hence the exact identity

`n_1+n_2+n_3=0`                                                       (4.1)

holds for **every symmetric B**. In particular

`det[n_1 n_2 n_3]=0`.                                                 (4.2)

For the codimension-one geometric Loomis–Whitney datum with three rank-two maps `R^3 -> R^2` and exponent `1/2` on each factor, finiteness requires the three kernel directions to span `R^3`; equivalently the determinant in (4.2) must be nonzero. Thus the desired finite three-factor Brascamp–Lieb constant is impossible. If one of the maps has rank below two, the datum is at least as degenerate.

### Consequence — `QFORM-SYMMETRIC-THREE-AMBIGUITY-BL-FAIL-v1`

The source-valid unnormalized `L^2` ambiguity budget **cannot** be assembled into the missing general theorem merely by choosing one symmetric physical `3x3` block and applying the naive three-map `L^2` Brascamp–Lieb/Loomis–Whitney inequality. The obstruction is algebraic and universal, not a bad choice of block or a small-minor issue.

This does **not** refute the characteristic-function route. It pinpoints why the most obvious use of the new product-preserving kernel fails.

## 5. What this changes in the proof search

Two distinct bad interfaces are now separated cleanly:

* fleet04/B16 proves that **normalizing first** and paying any positive conditional projection-height moment diverges even on a target-valid diffuse product family;
* this run proves that **keeping the correct unnormalized kernel** removes that divergence, but the most naive same-three-coordinate `L^2` Brascamp–Lieb assembly is singular for every symmetric quadratic block because of (4.1).

Therefore the next target-relevant Fourier mechanism must use information that the failed three-map datum discards. Two concrete options remain source-valid:

1. **asymmetric/lateral decoupling:** split physical coordinates into different source banks before the multilinear estimate, so the maps are governed by a genuinely nonsymmetric cross block and the forced relation `n_1+n_2+n_3=0` disappears; or
2. **fractional many-coordinate aggregation:** use more than three original-coordinate ambiguity kernels with leverage weights before selecting curvature, so no single singular three-map datum bears the full reciprocal cost.

Both must retain the unnormalized `q_f` weights until after the multilinear integration. Any route that divides by them recreates the partner's all-positive-moment obstruction.

A useful exact successor obligation is therefore:

> Prove a dimension-free multilinear estimate for the decoupled integral (3.1) using an asymmetric cross-bank or many-coordinate weighted datum, with a gain strong enough to make `integral |phi_A(t)|dt` finite whenever `A` has three singular/eigenvalues at least one in modulus.

The bare spectral hypothesis does not guarantee a fixed good cross block, so such an estimate must aggregate before reciprocal-minor payment.

## 6. Scope/status

* Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
* Full continuity conclusion: **OPEN**.
* `QFORM-UNNORMALIZED-AMBIGUITY-LP-v1`: proved for every one-dimensional cap-one probability density and every `p>=2`.
* Exact decoupling identity (3.1): proved for every symmetric `A` and all independent cap-one coordinates.
* `QFORM-SYMMETRIC-THREE-AMBIGUITY-BL-FAIL-v1`: proved as an obstruction to the naive three-selected-coordinate `L^2` Brascamp–Lieb assembly.
* Designated partner fleet04/B16 is applied explicitly through its diffuse cube family: normalized positive height moments diverge, while the unnormalized original-coordinate ambiguity budget stays exactly `pi` per indicator coordinate.

No Gaussian, log-concavity, moment, compact-support, connected-support, or eigenbasis-independence assumption is introduced.
