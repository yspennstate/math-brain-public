SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-22T22:52:41Z.
attacking: bounded-number small spectral directions inside a physical core: convert a rank-three spectral packet spread across 3+q original coordinates into a well-conditioned physical triple, then absorb arbitrary outside spectrum with the account04/B12 mixed-norm shear compiler.

# QFORM B12: finite small-spectral-tail localization with arbitrary outside completion

## Status

This run proves a new quantitative supporting theorem for the B12 additional-eigenvalue assignment. A rank-three spectral packet may be spread over a fixed number `m=3+q` of ORIGINAL coordinates and may be perturbed there by extra eigen-directions of either sign whose operator norm is explicitly budgeted. Cauchy--Binet forces one physical three-coordinate compression with enough determinant mass. After that extraction, **all remaining outside quadratic coefficients, signs, eigenvalue magnitudes and cross couplings are arbitrary**, and the completed account04/B12 mixed-norm shear theorem restores the outside quadratic remainder without any independent-convolution assumption.

Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. The result proves essential boundedness in its stated scope. Continuity is not proved.


## Source-valid dependencies actually used

1. **Physical two-same-sign triple theorem**, proved in this B12 line at
   `yspennstate/math-open-problems@b3c543b40dfaef13468466fa82625303a7719af8`
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260922T141530Z-two-samesign-threeblock/REPORT.md`.

   If one ORIGINAL-coordinate `3 x 3` principal block has at least two eigenvalues `>=g>0`, or at least two eigenvalues `<=-g`, then after conditioning all outside ORIGINAL coordinates the quadratic-plus-affine three-variable polynomial has density cap
   
   `C_*/g`,
   
   where
   
   `C_* = 2*pi + 3*sqrt(3) + sqrt((2*pi+3*sqrt(3))^2 + 3*pi^2)`
   `    = 24.183038289961516...`.

   The third eigenvalue of the physical triple is arbitrary.

2. **Assigned partner account04/B12 mixed-norm shear compiler**, complete supporting theorem at
   `yspennstate/math-open-problems@9ce47e2a0f2c8434d901df13a218450c2189d80e`
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260922T192552Z-account04-B12-mixed-shear-r1/REPORT.md`.

   If `(U,Z)` has joint density `h(u,z)` and
   
   `M(h)=int esssup_u h(u,z) dz`,
   
   then for every measurable `psi`,
   
   `||p_(U+psi(Z))||_infinity <= M(h)`.

   No independence between `U` and `psi(Z)` is assumed.

No pointwise van-der-Corput decay, post-rotation independence, arbitrary-joint coarea bound, worst normalized conditional fiber, fixed-good-minor implication, or two-slope gate is used.

## 1. Determinant-mass extraction from a three-frame

Let `U` be an `m x 3` real matrix with orthonormal columns,

`U^T U = I_3`,                                                   (1.1)

and for a three-element row set `I subset {1,...,m}` let `U_I` denote the `3 x 3` submatrix of those rows. Define

`gamma(U)=max_{|I|=3} det(U_I)^2`.                              (1.2)

### Lemma 1 — exact Cauchy--Binet frame extraction

`gamma(U) >= 1 / binom(m,3)`.                                   (1.3)

Moreover, if `I_*` attains the maximum, then

`sigma_min(U_(I_*))^2 >= gamma(U)`.                             (1.4)

### Proof

Cauchy--Binet applied to (1.1) gives

`1 = det(U^T U) = sum_{|I|=3} det(U_I)^2`.                      (1.5)

There are `N=binom(m,3)` terms, so one is at least `1/N`, proving (1.3).

Since deleting rows cannot increase the operator norm, `||U_I||_op<=||U||_op=1`. If the singular values of `U_I` are `s_1>=s_2>=s_3>=0`, then `s_1,s_2<=1`, hence

`det(U_I)^2=s_1^2 s_2^2 s_3^2 <= s_3^2`.                       (1.6)

Thus `sigma_min(U_I)^2=s_3^2>=det(U_I)^2`; at the maximizing triple this is (1.4). QED.

The point is that this is an aggregate-before-inversion step: determinant mass is summed over all physical triples before one triple is selected.

## 2. A three-frame produces a physical spectral gap

Let `Lambda` be real diagonal `3 x 3` with

`min_j |lambda_j(Lambda)| >= L > 0`.                            (2.1)

Put

`B_0 = U Lambda U^T`                                            (2.2)

on the `m` physical coordinates. For the maximizing triple `I_*`, set

`M_0 = B_0[I_*,I_*] = U_(I_*) Lambda U_(I_*)^T`.                (2.3)

Because all three factors are square,

`sigma_min(M_0)`
` >= sigma_min(U_(I_*))^2 sigma_min(Lambda)`
` >= L gamma(U).`                                               (2.4)

Now add any real symmetric in-core perturbation `E` and write

`eta = ||E||_op`.                                                (2.5)

The physical triple perturbation satisfies `||E[I_*,I_*]||_op<=eta`; therefore the singular-value Weyl inequality gives

`sigma_min(M_0+E[I_*,I_*]) >= L gamma(U)-eta`.                  (2.6)

No sign assumption on `E` is used.

## 3. Main theorem: finite small spectral tail + arbitrary completion

### Theorem — `QFORM-FINITE-SMALL-SPECTRAL-TAIL-ARBITRARY-COMPLETION-v1`

Let `X_1,...,X_n` be independent real random variables with probability densities bounded by one. Let `A` be any real symmetric `n x n` matrix. Choose a set `T` of `m>=3` ORIGINAL coordinates, and suppose its physical principal block has a decomposition

`A[T,T] = U Lambda U^T + E`,                                    (3.1)

where

- `U` is `m x 3` with `U^T U=I_3`;
- `Lambda` is real diagonal and `min_j |lambda_j|>=L>0`;
- `E` is arbitrary real symmetric;
- `eta=||E||_op < L gamma(U)`.

No condition is imposed on `A[T,T^c]` or `A[T^c,T^c]`.

Then `Q=X^T A X` has an essentially bounded density and

`boxed( ||p_Q||_infinity <= C_* / (L gamma(U)-eta) ).`          (3.2)

In particular, since `gamma(U)>=1/N`, `N=binom(m,3)`, the source-free numerical criterion

`eta < L/N`                                                     (3.3)

implies

`boxed( ||p_Q||_infinity <= C_* / (L/N-eta) ).`                 (3.4)

Every coefficient and every eigenvalue contributed outside `T` may have arbitrary sign and arbitrary magnitude; arbitrary cross coupling to `T` is allowed.

### Proof

Choose the maximizing physical triple `I_* subset T` from Lemma 1. By (2.6), its final physical quadratic block

`M=A[I_*,I_*]`

obeys

`g:=sigma_min(M) >= L gamma(U)-eta >0`.                         (3.5)

Because `M` is real symmetric, all three of its eigenvalues have absolute value at least `g`. Among three real signs, two agree, so `M` has either two eigenvalues at least `g` or two eigenvalues at most `-g`.

Let `Z=X_(I_*^c)` denote every other ORIGINAL coordinate. Fix `Z=z`. The full quadratic form is

`Q = X_(I_*)^T M X_(I_*) + ell(z)^T X_(I_*) + psi(z)`,          (3.6)

where `ell(z)` is an arbitrary affine tilt induced by the unrestricted cross block and `psi(z)` is the unrestricted outside quadratic remainder. The three coordinates of `X_(I_*)` remain independent with density cap one. The physical two-same-sign triple theorem therefore gives, uniformly in `z`,

`||p_(U_z)||_infinity <= C_*/g`,                                (3.7)

for

`U_z = X_(I_*)^T M X_(I_*) + ell(z)^T X_(I_*)`.                (3.8)

Let `g_Z(z)` be the product density of the outside ORIGINAL coordinates and define the joint density

`h(u,z)=g_Z(z) p_(U_z)(u)`.                                     (3.9)

Then

`M(h)=int esssup_u h(u,z) dz <= C_*/g`.                         (3.10)

Now apply the completed assigned-partner account04/B12 mixed-norm shear theorem with the **actual dependent remainder** `psi(z)`. It yields

`||p_(U+psi(Z))||_infinity <= M(h) <= C_*/g`.                   (3.11)

Using (3.5) gives (3.2), and (1.3) gives (3.4). There is no convolution with an allegedly independent spectral remainder. QED.

## 4. Pure spectral-window corollary inside a fixed physical block

Let

`s_1(B)>=s_2(B)>=...>=s_m(B)`

be the singular values of the physical block `B=A[T,T]`. Suppose

`s_3(B)>=L`,
` s_4(B)<=eta `                                                   (4.1)

(with `s_4=0` if `m=3`). Take the three eigenvectors corresponding to the three largest eigenvalue magnitudes of `B` as the columns of `U`, put their eigenvalues into `Lambda`, and put every remaining spectral direction into `E`. Then `||E||_op=s_4(B)<=eta` and Theorem 3 applies.

Hence, if

`s_4(A[T,T]) < L/binom(m,3)`,                                   (4.2)

then

`boxed( ||p_Q||_infinity
 <= C_* / ( L/binom(m,3) - s_4(A[T,T]) ) ).`                    (4.3)

This is a literal theorem about adding extra smaller eigenvalues of either sign inside a finite physical core while allowing completely arbitrary larger or smaller eigenvalues elsewhere.

### Four-coordinate corollary

For `m=4`, `N=4`. Therefore any physical `4 x 4` block satisfying

`s_3(B)>=L`, `s_4(B)<=L/8`                                      (4.4)

forces

`boxed( ||p_Q||_infinity <= 8 C_*/L
       =193.46430631969213.../L ).`                             (4.5)

If the four-coordinate block is exactly rank three, `s_4(B)=0`, the bound improves to

`boxed( ||p_Q||_infinity <= 4 C_*/L
       =96.73215315984606.../L ).`                              (4.6)

Every outside eigenvalue and cross coupling remains arbitrary.

### Any fixed number q of additional small in-core eigenvalues

Put `m=3+q` and `N=binom(q+3,3)`. If

`s_3(A[T,T])>=L`,
`s_4(A[T,T])<=L/(2N)`,                                         (4.7)

then

`boxed( ||p_Q||_infinity <= 2 N C_*/L ).`                       (4.8)

Thus for each fixed `q`, any `q` additional in-core eigenvalues of either sign at the indicated scale are quantitatively harmless, while the entire outside completion is free.

## 5. Spectral-leverage version for added global directions

Suppose the protected physical block is `U Lambda U^T` on `T`, and added global spectral terms are

`F = sum_r tau_r v_r v_r^T`,                                   (5.1)

with arbitrary real `tau_r`. Their compression to `T` satisfies

`||F[T,T]||_op
 <= sum_r |tau_r| ||(v_r)_T||_2^2`.                            (5.2)

Therefore Theorem 3 remains valid whenever

`sum_r |tau_r| ||(v_r)_T||_2^2 < L gamma(U),                   (5.3)

with the bound

`||p_Q||_infinity
 <= C_* / (L gamma(U)-sum_r |tau_r| ||(v_r)_T||_2^2).`          (5.4)

The `tau_r` may have either sign and individually arbitrary magnitude. Directions supported wholly outside `T` have zero leverage and cost exactly zero. This is a quantitative additional-eigenvalue statement in the original coordinate geometry.

## 6. Why this is a genuine advance but not the full theorem

The theorem closes the following previously unpaid intermediate case: the three large spectral directions may be **rotated inside a finite original-coordinate packet**, rather than already aligned with three physical coordinates or exact disjoint banks. Cauchy--Binet converts the whole three-frame volume into one physical triple before reciprocal curvature is paid. A bounded number of additional small in-packet eigenvalues is allowed, and arbitrary spectrum outside the packet is absorbed without independence assumptions.

The dependence on

`N=binom(m,3)`                                                   (6.1)

is the limitation. For a genuinely delocalized three-frame spread over `m -> infinity` physical coordinates, `gamma(U)` can be of order `m^-3`; the theorem then loses dimension. This is consistent with the known singleton-plus-two-banks and Hadamard/diffuse stress families. Therefore this result does **not** provide the missing exhaustive passage from the bare global hypothesis `s_3(A)>=1` to a universal physical core.

The remaining B12 obligation is now: replace the worst triple extraction when `gamma(U)` is tiny by grouped-coordinate aggregation (two-bank/three-bank/ridge/cross-volume machinery), while keeping the finite-packet theorem as the localized branch. The latest correction that a nonzero mutual edge plus two transverse slopes can still create a rank-two product singularity is respected: this proof spends a genuine third singular resource before invoking any density theorem.

## 7. Regularity and integrity

The result proves existence of an essentially bounded density. It does **not** establish a continuous representative under arbitrary cap-one input densities. The account04/B12 partner supplies a sufficient mixed translation-modulus condition for continuity, but no such universal modulus is proved here.

All conditioning is on ORIGINAL independent coordinates. No Gaussianity, log-concavity, moment, compact-support, connected-support, pointwise phase decay, post-rotation independence, arbitrary-joint coarea, normalized worst conditional-fiber cap, or Monte Carlo argument is used.

Claim ID: `QFORM-FINITE-SMALL-SPECTRAL-TAIL-ARBITRARY-COMPLETION-v1`.
