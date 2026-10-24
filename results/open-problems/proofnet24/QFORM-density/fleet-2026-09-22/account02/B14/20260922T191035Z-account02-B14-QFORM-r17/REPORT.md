SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B14, 2026-09-22T19:10:35Z.
attacking: prove a no-tax physical localization statement and test whether bounded-size original-coordinate active cores can retain the three-eigenvalue curvature; identify exactly where diffuse curvature goes when they cannot.

# account02/B14 — diffuse curvature relocation under physical localization

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Translations and localization  
**Run:** `20260922T191035Z-account02-B14-QFORM-r17`  
**Status:** `SUPPORTING_LOCALIZATION_LEMMA + RIGOROUS_MECHANISM_COUNTEREXAMPLE / FULL_QFORM_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The previous B14 run proved a determinant-only density bound from one nonsingular physical principal triple, but the target family

`A_m = [1] direct_sum (J_m/m) direct_sum (-J_m/m)`

shows that every such principal triple can be tiny. The first unpaid implication is therefore not another single-core selection theorem. It is:

**QFORM-OVERLAP1-CROSS-MINOR-BANK-PAYMENT-v1.** Convert an order-one packet of third-compound cross-minor mass into a small-ball/density estimate *before* reciprocating individual minors, uniformly in arbitrary outside-induced affine terms. The canonical diffuse family below shows that asymptotically all third-order curvature can live in overlap-one row/column minors on five physical coordinates even though every bounded-size principal active block has vanishing third singular value.

This report proves the exact relocation statement and a sharp active-core localization barrier. It does not pay that cross-minor bank, so the full conjecture remains open.

## 2. Exact no-tax physical localization

Let `S` be any fixed set of original coordinates and write `T=S^c`. For every deterministic outside value `z`,

`Q(x_S,z)=x_S^T A_SS x_S + 2 (A_ST z)^T x_S + z^T A_TT z`.

Hence conditioning on `X_T=z` preserves the original independence and density caps of the active variables `X_S`; all outside information enters the active problem only through an affine vector and a scalar constant. Therefore:

> If for this fixed `A_SS` one has an active-coordinate density bound `C` uniformly over every affine vector, scalar constant, and every independent cap-one law on `X_S`, then the full form has density at most `C` after averaging over arbitrary outside laws.

This has exactly zero tax in support location, fragment separation, tails, moments, or outside shift size. It is the correct physical localization interface. Its limitation is equally exact: outside conditioning never changes the active Hessian `2A_SS`.

## 3. Diffuse family: every bounded physical active block loses the third curvature direction

For `m>=1`, define on `2m+1` original coordinates

`A_m = [1] direct_sum (J_m/m) direct_sum (-J_m/m)`.

Its nonzero spectrum is exactly `{1,1,-1}`. Thus it satisfies the full spectral hypothesis with equality.

Take any active set `S` of cardinality `k`. If `S` omits the singleton coordinate, then `A_m[S,S]` has rank at most two. If `S` contains the singleton and contains `p` coordinates from the positive bank and `q` from the negative bank, then, after a coordinate permutation,

`A_m[S,S] = [1] direct_sum (J_p/m) direct_sum (-J_q/m)`.

Its nonzero eigenvalues are exactly

`1, p/m, -q/m`.

Consequently

`s_3(A_m[S,S]) = min(1,p/m,q/m) <= (k-1)/(2m)`.          (3.1)

In particular, to retain a local third singular value at least `c<=1`, one must leave at least

`|S| >= 1+2cm`                                                   (3.2)

original coordinates active. No fixed-size, or even `o(m)`-size, physical localization can preserve three order-one curvature directions in this target-valid family. Arbitrary outside values cannot repair this, because they generate only affine terms.

The same loss can be expressed in third-compound currency. Since the restriction has rank at most three,

`e_3(s(A_m[S,S])^2) = p^2 q^2 / m^4`

when the singleton and both banks are present, and is zero otherwise. Therefore for every `|S|=k`,

`e_3(s(A_m[S,S])^2) <= (k-1)^4/(16 m^4)`.                  (3.3)

The full matrix, however, has `e_3(s(A_m)^2)=1`. Thus a bounded active principal block captures a vanishing fraction of the global third-order curvature.

This is a mechanism counterexample, not a counterexample to QFORM.

## 4. Where the missing curvature goes: an exact overlap-one cross-minor bank

For an arbitrary real matrix `A`, the third compound satisfies

`sum_{|I|=|J|=3} det(A[I,J])^2 = ||C_3(A)||_F^2 = e_3(s_1(A)^2,...,s_n(A)^2)`.       (4.1)

This follows from the singular values of the exterior-power map `wedge^3 A`, which are all triple products `s_i s_j s_k`. Under the target hypothesis, the right side is at least one.

Now specialize (4.1) to `A_m`. A `3x3` cross minor is nonzero if and only if both the row set `I` and column set `J` contain the singleton coordinate, one positive-bank coordinate, and one negative-bank coordinate. Every such determinant has magnitude exactly `m^(-2)`. There are `m^4` ordered pairs `(I,J)`.

Let

`M_r = sum_{|I|=|J|=3, |I intersect J|=r} det(A_m[I,J])^2`.

Because every nonzero pair shares the singleton, `M_0=0`. Exact counting gives

`M_1 = m^2(m-1)^2 m^(-4) = ((m-1)/m)^2`,

`M_2 = 2m^2(m-1)m^(-4) = 2(m-1)/m^2`,

`M_3 = m^2 m^(-4) = 1/m^2`,

and hence

`M_1+M_2+M_3=1`.                                             (4.2)

Therefore

`M_1 -> 1` as `m -> infinity`.                                (4.3)

So the diffuse family does not lose third-order curvature at all: it relocates almost all of it into **overlap-one cross minors**. Each such minor uses `|I union J|=5` original coordinates, but each individual determinant is only `m^(-2)`; the order-one object is the entire packet of about `m^4` squared minors.

This sharply distinguishes two notions of localization:

- principal active-block localization loses curvature by (3.1)-(3.3);
- cross-minor localization can keep the curvature on five-coordinate row/column unions, but only as an aggregate bank before any reciprocal determinant payment.

## 5. Randomized principal-triple selection still fails

The nonzero principal `3x3` minors of `A_m` are exactly the `m^2` sets consisting of the singleton, one positive-bank coordinate, and one negative-bank coordinate, and every one has

`|det A_m[S,S]| = m^(-2)`.                                    (5.1)

Therefore for **every** probability distribution `pi` on the nonzero physical triples,

`E_pi |det A_m[S,S]|^(-1/3) = m^(2/3)`.                       (5.2)

Thus randomizing the previous one-principal-triple theorem cannot repair the diffuse obstruction: selector weighting is irrelevant because all available determinants have the same tiny size. Any dimension-free proof must aggregate before inversion rather than choose a triple and then pay its reciprocal determinant.

A useful general rank-three identity explains why the tempting selector still looks plausible. If `A=U Lambda U^T` has rank exactly three with `U^T U=I_3`, then

`det A[S,S] = det(Lambda) det(U_S)^2`,

so by Cauchy-Binet

`sum_{|S|=3} |det A[S,S]| = |det Lambda|`.                    (5.3)

In `A_m` this total principal determinant mass is exactly one, but (5.2) shows that a positive `L^1` determinant bank does not survive randomize-then-invert.

## 6. Completed partner result applied

Completed assigned-partner result consumed in full:

`account03/B14`, run `20260922T183537Z-account03-B14-QFORM-r16`, canonical report
`yspennstate/math-open-problems@1b9da0695f33c0d618a25e3ff5a85159d2dbe94d`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260922T183537Z-account03-B14-QFORM-r16/REPORT.md`.

That report gives a target-valid four-variable family for which the full output is uniformly bounded but

`sup_b ||p_(Q3 | Q'=b)||_infinity = infinity`,

and proves that the bad conditional fiber has small positive mass. Its correct replacement is **mass-weighted scalar conditioning / aggregate-before-supremum**.

The present result is the matrix-side analogue. In `A_m`, taking a worst or randomized principal active block destroys the order-one curvature bank; the correct replacement must retain the squared-minor packet before taking a reciprocal local cost. The two obstructions therefore point to the same proof architecture:

1. keep law-side mixture/fiber mass before conditional supremum;
2. keep matrix-side compound mass before determinant inversion;
3. only then apply an affine-uniform physical estimate and average outside variables.

No post-rotation independence, arbitrary-joint coarea bound, positive conditional projection moment, scalar conditional supremum, or fixed bounded active-core spectral reduction is used.

## 7. Remaining connection to the full target

A sufficient next theorem is an overlap-one packet estimate of the following qualitative form. Whenever

`sum_{|I|=|J|=3, |I intersect J|=1} det(A[I,J])^2 >= c0`,

prove directly under the original cap-one product law, uniformly in arbitrary affine perturbations and additional spectral components, a small-ball bound

`P{X^T A X + ell^T X + c in J} <= C(c0) |J|`

without first selecting one `(I,J)` and paying `|det A[I,J]|^(-alpha)`.

The `A_m` calculation proves that this overlap-one obligation is not artificial: it carries asymptotically the entire third compound in the canonical diffuse rank-three obstruction while every bounded principal active block is spectrally degenerate. The full QFORM theorem remains open until this or an equivalent aggregate mechanism is proved.
