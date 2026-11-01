SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B12, 2026-09-23T02:20:36Z.
attacking: dual-sign physical-core switching: absorb arbitrary-magnitude spectral additions by minority inertia, while paying an arbitrary-rank small spectral tail only through operator norm.

# fleet01/B12 r22 — dual-sign core switching for arbitrary added eigenvalues

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Additional eigenvalue control  
**Status:** `PROVED SUPPORTING STABILITY THEOREMS / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Target and first missing implication

The full target remains open: for independent real coordinates with densities at most one, and a real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal essential density bound for `X^T A X` (and separately continuity), or produce a genuine counterexample.

This run does not attempt a spectral rotation.  It stays in the original independent coordinates and proves a new stability theorem for *adding* spectral directions once the base matrix contains one positive and one negative protected physical core.  The first still-unpaid implication is structural: derive such protected cores, or a different already-paid grouped/ridge/cross certificate, from the bare global three-large-eigenvalue hypothesis.

## 1. Completed sources used

### 1.1 Designated partner fleet02/B12

I read the completed partner report

`yspennstate/math-open-problems@2e72dc67725bab71d3892291c9d28db1996cabbf`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260923T021551Z-fleet02-B12-qform-r23/REPORT.md`.

The partner proves the threshold hostile-inertia inequalities, for real symmetric `M,E` and `L>0`,

`N_+(M+E;L) >= N_+(M;L)-nu_-(E)`,

`N_-(M+E;L) >= N_-(M;L)-nu_+(E)`,                         (1.1)

and combines them with dense operator-norm tails on an actual physical core.  I apply (1.1) below to a selected physical compression and obtain an actual two-survivor inequality, rather than citing it only qualitatively.

The same partner report also records the finite-core theorem: on `m>=3` original coordinates, if the actual `m x m` quadratic matrix has three eigenvalues of modulus at least `L`, arbitrary affine terms allowed, then

`||p||_infinity <= 2 sqrt(6 pi m)/L`.                           (1.2)

### 1.2 Two-same-sign physical-three-block endpoint

I also use the completed theorem

`yspennstate/math-open-problems@b3c543b40dfaef13468466fa82625303a7719af8`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260922T141530Z-two-samesign-threeblock/REPORT.md`, Theorem 6.1.

If an actual physical `3 x 3` principal block has two eigenvalues at least `L`, or two eigenvalues at most `-L`, while the third is arbitrary, then after conditioning on all other ORIGINAL coordinates,

`||p_Q||_infinity <= C_*/L`,                                    (1.3)

where

`C_* = 24.183038289961516...`.

All outside quadratic coefficients and cross couplings are allowed; they become affine terms after original-coordinate conditioning.

## 2. Compression does not increase hostile inertia

For a real symmetric matrix `R` and a coordinate set `H`,

`nu_+(R[H,H]) <= nu_+(R)`,
`nu_-(R[H,H]) <= nu_-(R)`.                                      (2.1)

This is immediate from the variational characterization of inertia: a positive (respectively negative) subspace for the compressed quadratic form is also a positive (respectively negative) subspace for the full quadratic form after extending vectors by zero outside `H`.

This elementary fact is the bridge between the global added spectral cloud and the physical core on which independence is available.

## 3. Main theorem: dual-sign triple switch

Let `A0,S,R` be real symmetric `n x n` matrices and

`A=A0+S+R`.                                                       (3.1)

Assume there are two ORIGINAL-coordinate triples `H_+` and `H_-` (they need not be disjoint) such that

`A0[H_+,H_+] >= kappa I_3`,
`A0[H_-,H_-] <= -kappa I_3`,                                    (3.2)

for some `kappa>0`.  Assume also

`||S||op <= delta < kappa`.                                      (3.3)

No magnitude bound is placed on `R`.

### Theorem 3.1 — `QFORM-DUAL-SIGN-TRIPLE-MINORITY-INERTIA-v1`

If

`min(nu_+(R),nu_-(R)) <= 1`,                                    (3.4)

then the full ambient quadratic form has an essentially bounded density and

`boxed: ||p_(X^T A X)||_infinity <= C_*/(kappa-delta).`          (3.5)

Every eigenvalue of `R` may have arbitrary magnitude.  The tail `S` may have arbitrary rank and arbitrary signs.

#### Proof

Set `L=kappa-delta>0`.

**Case 1: `nu_-(R)<=1`.**  Use the positive core `H_+`.  Let

`M=(A0+S)[H_+,H_+]`, `E=R[H_+,H_+]`.

Compression is operator-norm contractive, hence from (3.2)-(3.3)

`M >= L I_3`, so `N_+(M;L)=3`.                                  (3.6)

By (2.1), `nu_-(E)<=nu_-(R)<=1`.  Applying the completed partner inequality (1.1) gives the actual inequality

`N_+(A[H_+,H_+];L)
 >= N_+(M;L)-nu_-(E)
 >= 3-1 = 2.`                                                    (3.7)

Thus the actual final physical triple has at least two eigenvalues `>=L`.  Apply (1.3), condition on every original coordinate outside `H_+`, and average the uniform conditional interval bound.  This gives (3.5).

**Case 2: `nu_+(R)<=1`.**  Use the negative core `H_-`.  Equivalently apply Case 1 to `-A`, because

`-(A0+S)[H_-,H_-] >= L I_3`

and `nu_-(-R)=nu_+(R)<=1`.  Therefore the final physical triple has at least two eigenvalues `<=-L`, and (1.3) again gives (3.5).  QED.

### Interpretation

A favorable spectral cloud is free, regardless of rank and magnitude.  In addition, **one hostile global eigendirection is also free**.  The choice between the positive and negative physical cores is made only after inspecting the inertia of the arbitrary large perturbation; no random variable is rotated.

## 4. Arbitrary rank-three addition is free

For every symmetric matrix `R`,

`nu_+(R)+nu_-(R)=rank(R)`.

Hence if `rank(R)<=3`,

`min(nu_+(R),nu_-(R)) <= 1`.                                    (4.1)

Therefore Theorem 3.1 immediately gives:

### Corollary 4.1 — arbitrary rank-three spike cloud + dense tail

Under (3.2)-(3.3), **every** symmetric perturbation `R` of rank at most three, with arbitrary nonzero eigenvalues of either signs and arbitrary eigenvectors, satisfies

`boxed: ||p_Q||_infinity <= C_*/(kappa-delta).`                  (4.2)

This is stronger than controlling three individually small added eigenvalues: their magnitudes are completely unrestricted.

For example, if `kappa=1` and `delta<=1/2`, then

`boxed: ||p_Q||_infinity <= 2 C_* = 48.36607657992303...`        (4.3)

uniformly over all rank-three additions `R`.

## 5. Spectral threshold form: arbitrarily many small and large added eigenvalues

Let an arbitrary symmetric spectral addition be

`E=sum_j theta_j v_j v_j^T`,                                     (5.1)

with orthonormal `v_j`.  Fix a threshold `eta` with `0<=eta<kappa` and split

`S_eta = sum_{|theta_j|<=eta} theta_j v_j v_j^T`,
`R_eta = sum_{|theta_j|> eta} theta_j v_j v_j^T`.                (5.2)

Then

`||S_eta||op <= eta`.                                            (5.3)

Write

`N_+(eta)=#{j:theta_j>eta}`,
`N_-(eta)=#{j:theta_j<-eta}`.                                    (5.4)

If

`min(N_+(eta),N_-(eta)) <= 1`,                                  (5.5)

then Theorem 3.1 with `delta=eta` gives

`boxed: ||p_(X^T(A0+E)X)||_infinity <= C_*/(kappa-eta).`         (5.6)

Thus:

* arbitrarily many added eigenvalues of one sign may be arbitrarily large;
* one added eigenvalue of the opposite sign may also be arbitrarily large;
* arbitrarily many remaining eigenvalues of either sign may be added inside the entire interval `[-eta,eta]`;
* the bound depends only on the small-tail threshold `eta`, not on the magnitudes of the large eigenvalues.

No convolution with `X^T E X` is used.  The small spectral tail is used only as deterministic matrix perturbation of a physical core.

## 6. General finite-core version

The same sign-switch idea extends to larger physical cores and uses the partner finite-core theorem (1.2).

Assume now that `H_+` and `H_-` each contain `m>=3` original coordinates and

`A0[H_+,H_+] >= kappa I_m`,
`A0[H_-,H_-] <= -kappa I_m`,                                    (6.1)

with `||S||op<=delta<kappa`.  Put `L=kappa-delta`.

### Theorem 6.1 — `QFORM-DUAL-MCORE-HOSTILE-BUDGET-v1`

If either

`nu_-(R) <= m-3`                                                 (6.2+)

or

`nu_+(R) <= m-3`,                                                (6.2-)

then

`boxed: ||p_Q||_infinity <= 2 sqrt(6 pi m)/L.`                   (6.3)

Indeed, choose the corresponding sign core.  Before `R`, all `m` eigenvalues of that compressed core have the chosen sign and magnitude at least `L`.  The partner inequality (1.1), together with (2.1), leaves at least

`m-(m-3)=3`                                                       (6.4)

such eigenvalues after `R`.  Equation (1.2) then gives (6.3) after original-coordinate conditioning.

A rank-only corollary follows.  If `rank(R)=r`, then

`min(nu_+(R),nu_-(R)) <= floor(r/2)`.                            (6.5)

Hence every arbitrary-magnitude perturbation of rank

`boxed: r <= 2m-5`                                               (6.6)

is covered by one of the two sign cores.  For instance, a pair of five-dimensional opposite-sign definite physical cores absorbs an arbitrary rank-five spectral perturbation plus an arbitrary-rank dense tail of operator norm `<kappa`, with

`||p_Q||_infinity <= 2 sqrt(30 pi)/(kappa-delta)`                (6.7)

(`2 sqrt(30 pi)=19.41625912555699...`).

The `m=3` endpoint is better than (6.6): the two-same-sign theorem only needs **two** survivors, so Theorem 3.1 absorbs rank three rather than merely rank one.

## 7. Sharpness of the rank-three switch mechanism

The rank-three conclusion in Corollary 4.1 is sharp for this *two designated physical triples + two-survivor* mechanism.

Take the six-coordinate base

`A0=diag(kappa,kappa,kappa,-kappa,-kappa,-kappa)`                 (7.1)

with the obvious positive and negative triples.  For `M>2kappa`, add

`R_M=diag(-M,-M,0, M,M,0)`.                                     (7.2)

Then `rank(R_M)=4` and `nu_+(R_M)=nu_-(R_M)=2`.  On the positive protected triple the final eigenvalues are

`kappa-M, kappa-M, kappa`,                                      (7.3)

so only one positive direction remains at level `kappa`.  On the negative protected triple they are

`-kappa+M, -kappa+M, -kappa`,                                   (7.4)

so only one negative direction remains at level `kappa`.  Therefore neither designated triple can invoke the two-same-sign endpoint.

This is **not** a counterexample to QFORM; it only shows that rank four cannot be made completely free by this specific two-triple switch without more reserve, more cores, or another certificate.

## 8. Deterministic stress check

As corroboration only, I generated 5000 random positive physical triples `B0>=kappa I`, arbitrary dense tails with operator norm at most `delta<kappa`, and arbitrary large symmetric perturbations having at most one negative eigenvalue.  In every test the second largest eigenvalue of `B0+tail+R` stayed at least `kappa-delta`, exactly as (3.7) predicts.  The analytic proof above is the proof; the check is not a premise.

Constants used in the check:

`C_*=24.183038289961516...`,
`2 C_*=48.36607657992303...`,
`2 sqrt(24 pi)=17.366430109398422...`,
`2 sqrt(30 pi)=19.41625912555699...`.

## 9. What this pays and what remains

**Paid by this run.**  Once opposite-sign protected physical cores exist, one may add:

1. an arbitrary-rank small spectral tail of either sign;
2. an arbitrary high-rank large cloud of one sign plus at most one large direction of the other sign; or
3. in particular, any rank-three arbitrary-magnitude symmetric spectral perturbation;

without any independence assumption on the induced quadratic remainder.

**Still open.**  The bare global hypothesis `s_3(A)>=1` does not yet force the dual protected physical cores in (3.2), and diffuse/grouped examples warn against assuming such local cores universally.  A full proof still needs an exhaustive product-preserving extraction routing every matrix into this or one of the already-paid ridge/grouped-bank/hub/cross-volume branches.

**Regularity.**  The arguments above prove essential boundedness in their stated scopes.  They do not establish the separately requested continuous-density conclusion.

**Full target status:** OPEN / NOT PROVED / NOT DISPROVED.
