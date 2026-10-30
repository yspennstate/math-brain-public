SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B14, 2026-09-23T01:58:09Z.
attacking: simultaneous affine-envelope localization—localize the full small-ball supremum over conditioning-generated shifts, then splice it with volume-sampling certificates without any support or perturbative-law tax.

# fleet02/B14 r23 — simultaneous affine-envelope localization and kernel-only conditioning leakage

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `NEW SUPPORTING LOCALIZATION THEOREMS / FULL QFORM OPEN / CONTINUITY SEPARATE`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and source boundary

The target remains: for every dimension, every product law of independent real coordinates with one-dimensional probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal finite bound for the essential density of `X^TAX`, or give a valid counterexample. No moment, support, connectedness, log-concavity, identical-law, or post-rotation-independence hypothesis is added.


The assigned completed partner actually used is fleet03/B14 r23, canonical
`yspennstate/math-open-problems@1f87f660ea368893d7f0aae76399af0d904318fd:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260923T013540Z-fleet03-B14-QFORM-r23/REPORT.md`.
Its Theorem 3.1 is exact convex-output localization, and its proof records the stronger underlying fact needed here: every cap-one product law is a total-variation limit of finite convex mixtures of compact finite-fragment indicator product laws. I use that mixture approximation below to localize an *entire parameter family of output maps at once*.

The required newest Claude source was read at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The completed D/D' volume-sampling theorem is applied explicitly in Section 6.

## 2. Simultaneous convex-envelope localization

Let `D_n` be the class of product probability laws on `R^n` whose one-dimensional densities satisfy `0<=f_i<=1`. Let `F_n` be the subclass whose marginals have densities `1_E`, where `E` is a compact finite union of intervals of total length one.

Let `Theta` be an arbitrary index set. For every `theta in Theta`, let `P_theta:R^n->R` be measurable and let `Phi_theta` be a convex, total-variation-lower-semicontinuous extended functional of finite Borel measures on `R`. Define

`E_Theta(mu)=sup_(theta in Theta) Phi_theta((P_theta)_# mu)`.

### Theorem 2.1 — `QFORM-SIMULTANEOUS-CONVEX-ENVELOPE-LOCALIZATION-v1`

`boxed: sup_(mu in D_n) E_Theta(mu) = sup_(nu in F_n) E_Theta(nu).`       (2.1)

The equality is exact, including `+infinity`. No common maximizer in `theta`, no compact parameter set, and no support/fragment/moment bound is required.

### Proof

For fixed `theta`, pushforward is affine in the input measure and contracts total variation. Hence

`mu -> Phi_theta((P_theta)_#mu)`

is convex and TV-lower-semicontinuous. An arbitrary supremum of convex functions is convex, and an arbitrary supremum of lower-semicontinuous functions is lower-semicontinuous. Thus `E_Theta` has both properties.

By the finite-mixture TV approximation used in the assigned partner report, for every `mu in D_n` there exist

`mu_m=sum_r w_(m,r) nu_(m,r)`,  `nu_(m,r) in F_n`,

with `||mu_m-mu||_TV ->0`. Therefore

`E_Theta(mu)
 <= liminf_m E_Theta(mu_m)
 <= liminf_m sum_r w_(m,r) E_Theta(nu_(m,r))
 <= sup_(nu in F_n) E_Theta(nu).`

Taking the supremum over `mu in D_n` gives one inequality; `F_n subset D_n` gives the other. QED.

This is stronger than localizing one fixed output map and then optimizing afterwards: the output map, affine coefficient, target interval, or structural parameter may all be optimized jointly with the law before the finite-fragment reduction.

## 3. Exact small-ball version and the full affine envelope

For a finite positive Borel measure `eta` on `R`, define

`SB(eta)=sup_(t in R,h>0) eta([t,t+h])/h`.                       (3.1)

For every `eta`, `SB(eta)` is exactly the extended `L^infinity` density norm: if (3.1) is finite with value `C`, then `eta(I)<=C|I|` for every interval, hence for every open set by countable additivity and then every Borel set by regularity. Thus `eta<=C dx` and its density is bounded by `C`. Conversely a density bounded by `C` has every interval average at most `C`. Therefore

`SB(eta)=||d eta/dx||_infinity`, with value `+infinity` for singular or essentially unbounded laws.       (3.2)

Now let `{P_theta}` be any family of measurable real outputs and take `Phi_theta=SB`. Since `SB` is a supremum of positive linear event functionals, it is convex and TV-lower-semicontinuous. Theorem 2.1 gives

`boxed:
 sup_(mu in D_n) sup_theta ||p_(P_theta(X))||_infinity^ext
 =sup_(nu in F_n) sup_theta ||p_(P_theta(X))||_infinity^ext. }   (3.3)

In particular, for one fixed symmetric matrix `B`, the entire affine family

`P_(ell,c)(x)=x^T B x+ell^T x+c`

localizes simultaneously:

`sup_(mu in D_n,ell,c)||p_(P_(ell,c)(X))||inf^ext
 =sup_(nu in F_n,ell,c)||p_(P_(ell,c)(X))||inf^ext.`            (3.4)

The affine coefficient is allowed to be arbitrarily large; finite fragments may be arbitrarily distant and their number is not uniformly bounded.

## 4. Range-affine terms are an exact quotient

Fix a symmetric `m x m` matrix `B`. Let `K=Ker(B)` and decompose

`ell=ell_K+ell_R`,  `ell_K in K`,  `ell_R in Range(B)`.

Choose `s` with `2Bs=ell_R`. With `y=x+s` (equivalently `x=y-s`),

`x^T B x+ell^T x+c
 =y^T B y+ell_K^T y+c'`                                          (4.1)

for a scalar `c'`. Coordinatewise translation is a bijection of both `D_m` and `F_m`: independence and the cap `<=1` are unchanged, and compact finite interval unions are merely translated.

Define

`C_B(ell)=sup_(mu in D_m)||p_(X^T B X+ell^T X)||inf^ext`.

### Theorem 4.1 — `QFORM-RANGE-AFFINE-QUOTIENT-v1`

`boxed: C_B(ell)=C_B(P_K ell).`                                  (4.2)

The same identity holds with `D_m` replaced by `F_m`. In particular, if `B` is invertible,

`boxed: sup_ell C_B(ell)=C_B(0).`                                (4.3)

Thus any worst-law centered theorem for an invertible physical core automatically handles every conditioning-generated affine term with the identical constant. One does not need a support radius to complete the square, because the completion translates the *admissible law class*, not a fixed bounded support.

For singular `B`, (4.2) isolates the genuine nuisance exactly: only the kernel component of the affine term can matter.

## 5. Ambient conditioning compiler: only kernel leakage survives

Take an original-coordinate decomposition `X=(U,V)` with independent blocks and

`Q(U,V)=U^T B U+2U^T C V+b^T U+F(V)`,                           (5.1)

where `F` is arbitrary measurable and finite almost surely. Put `K=Ker(B)` and `L=P_K C`.

Condition on `V=v`. By (4.1), the range component of `2Cv+b` is removable by translating the active product law. Hence any measurable envelope `H:K-> [0,infinity]` satisfying

`C_B(k)<=H(k)` for every `k in K`                               (5.2)

gives the exact product-preserving bound

`boxed:
 ||p_Q||inf^ext <= E H(P_K b+2L V). }`                           (5.3)

Indeed for every interval `I`, condition on `V`; the conditional active law is still the original cap-one product law, (5.2) bounds its interval probability by `H(...)|I|`, and averaging gives (5.3). No rotated variable is declared independent.

Two important zero-tax cases follow.

1. If `B` is invertible, `K={0}`, so all outside affine terms cost zero and `||p_Q||inf<=C_B(0)`.
2. If `B` is singular but `P_K C=0` (equivalently `Range(C) subset Range(B)`), then conditioning-generated outside affine terms cost zero. For the pure quadratic target `b=0`, again `||p_Q||inf<=C_B(0)`.

Thus the exact localization obstruction is not “large translations” or “distant fragments”; it is **kernel leakage**. If kernel leakage is nonzero, (5.3) says it should be averaged through its actual distribution before a worst-case supremum is taken. This is precisely compatible with the earlier B14 negative-moment/logarithmic-leakage compilers.

## 6. Required newest-Claude result applied to a real inequality

Claude's completed Theorem D/D' in `FOURIER_ROUTE_REPORT.md` at commit `e5f71d79eff325201dd0274053d20268ce65b837` applies to disjoint original-coordinate sets `I,J`, cross block `M=A[I,J]`, third-volume

`Z=e_3(M^T M)>0`,

and row volume-sampling marginals `alpha_i<=h<3/4`. It proves, uniformly in the self blocks and affine terms,

`||p_(X^TAX+b^TX+c)||inf
 <= 6 sqrt(e) (2h)^(-1/2)(3-4h)^(-1) Z^(-1/6).`                 (6.1)

Apply (3.3) with `theta=(b,c)`. We obtain the new exact extremal form

`boxed:
 sup_(mu in D_n,b,c)||p_(X^TAX+b^TX+c)||inf^ext
 =sup_(nu in F_n,b,c)||p_(X^TAX+b^TX+c)||inf^ext
 <=6 sqrt(e)(2h)^(-1/2)(3-4h)^(-1)Z^(-1/6). }`                 (6.2)

This is an actual equation-level application of the required newest-Claude package. It says the full affine volume certificate may be proved/searched on compact finite-fragment extreme products with **zero** support-radius, fragment-count, fragment-separation, or translation tax. No affine maximizer has to exist.

The newer volume-stability theorem at
`math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`
sharpens the analytic constant and controls the marginal gate under matrix perturbation. If

`M=M0+E`, `s3(M0)>=a>0`, `max_i(P_Range(M0))_ii<=1/2`, `||E||op<=a/16`,

then the same simultaneous affine envelope satisfies

`boxed:
 sup_(mu in D_n,b,c)||p_(X^TAX+b^TX+c)||inf
 <=24 sqrt(3)e/(5a)<23/a, }`                                    (6.3)

and by (3.3) its supremum is again exactly the finite-fragment extreme supremum.

Equation (6.3) is the correct support-free way to use a small matrix perturbation: the actual perturbed block `M` remains inside the Fourier/volume certificate. It never compares `Law(X^TAX)` to the law for `M0`.

## 7. Compatibility with the remote-fragment perturbation obstruction

The previous B14 correction `QFORM-NO-UNIFORM-COEFFICIENT-PERTURBATION-CONTINUITY-v1` exhibited target-valid matrices `A_epsilon->A_0` in operator norm and compact two-fragment cap-one inputs for which the two output laws stay separated in total variation by at least `1/128`. Therefore no proof may infer a small output-law error merely from a small coefficient error under arbitrary supports.

There is no conflict with (6.3). The volume-stability theorem is continuity of an **analytic certificate in matrix geometry**, not continuity of the random output law. This distinction is now exact:

- law perturbation: false uniformly because remote fragments amplify small coefficients;
- certificate perturbation: valid in the stated volume-marginal regime because every perturbed coefficient remains in `M` and the Brascamp--Lieb determinant is re-estimated directly.

The witness to the law-continuity failure already lies in `F_n`, so Theorem 2.1 cannot and should not remove it.

## 8. How the assigned partner result is used

Fleet03/B14 r23 established fixed-output convex localization and exposed the finite-mixture TV approximation. Theorem 2.1 uses that completed result to pass an arbitrary supremum over output maps/affine parameters through localization *before* selecting a parameter. This is needed for conditioning: the affine term `2Cv+b` may vary over an unbounded set as `v` ranges over arbitrarily distant outside fragments.

The range quotient (4.2) then removes every range-compatible part of that unbounded family without choosing support centers or invoking moments. The ambient inequality (5.3) identifies the only surviving parameter as the actual kernel leakage `P_K(2CV+b)`, which may then be paid by a source-valid negative-moment/logarithmic estimate rather than a support bound.

## 9. Remaining implication

Full QFORM remains OPEN. The new localization step removes a genuine proof-interface ambiguity: simultaneous optimization over affine shifts and target intervals is exactly compatible with compact finite-fragment extremization, and all range-affine conditioning terms quotient out.

The first unpaid implication is now:

`QFORM-KERNEL-LEAKAGE-OR-VOLUME-EXIT-v1` — in each surviving no-pivot/heavy-star state under `s_3(A)>=1`, expose either

(a) a volume/ridge/bank certificate such as (6.2)-(6.3), or
(b) an original-coordinate active core for which the only conditioning dependence is a kernel leakage admitting an integrable envelope `H` in (5.3).

One may not replace (b) by bounded support, a fixed fragment count, a moment estimate, post-rotation independence, or small-output-law perturbation from a nearby matrix.

## 10. Integrity

- Full conjecture: `OPEN / NOT PROVED / NOT DISPROVED`.
- New proved theorem: simultaneous convex-envelope localization, (2.1), including the exact affine small-ball extremal identity (3.3)-(3.4).
- New proved theorem: range-affine quotient (4.2) and kernel-leakage ambient compiler (5.3).
- Required newest-Claude result actually applied: volume-sampling D/D' at (6.1)-(6.2).
- Newer compatible volume-stability result actually applied: (6.3).
- Assigned partner fleet03/B14 r23 actually consumed: its finite-mixture localization premise is the key input in Theorem 2.1.
- No moments, support diameter, fixed fragment number, centering, Gaussianity, log-concavity, or rotated independence was used.
- Essential boundedness is the target here; continuity remains a separate conclusion except in source branches that prove it.
