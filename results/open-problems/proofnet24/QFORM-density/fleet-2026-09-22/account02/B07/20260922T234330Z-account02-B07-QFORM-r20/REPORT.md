SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-22T23:43:30Z.
attacking: the large-row tiny-nonzero-pivot survivor — combine determinant-weighted two-star currency with the genuine small scalar square while preserving the original-coordinate product law; seek a pair/discriminant payment or a target-valid obstruction.

# account02/B07 r20 — anchor exterior packet survives a tiny scalar pivot

**Run:** `20260922T234330Z-account02-B07-QFORM-r20`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Coordinate minor selection / GEOMETRY  
**Fresh owner control:** revision `2026-09-22.15`; QFORM remains the sole research target and B07 is not paused.  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`).  
**Classification:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED` for an intermediate one-local-Schur-minor extraction; full QFORM remains OPEN.

## 1. Incoming state and source-pinned dependencies

The exact target remains: arbitrary independent real original coordinates with marginal probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No moment, bounded-support, log-concavity, rotation-independence, arbitrary-joint coarea, or conditional-projection-density hypothesis is used.

The newest designated partner result actually applied is account03/B07 r19:

`yspennstate/math-open-problems@309a7cf35906f05d767ff2fcf1be74367f479d1c`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260922T224159Z-account03-B07-qform-r19/REPORT.md`.

It proves, in the current O0/S0 two-star survivor, that one physical anchor has complete outside-row norm

`beta > 200^(-1/4)`                                                     (1.1)

and that exact zero diagonal is paid, while a diagonal of modulus at least `1/16` is paid by the discriminant mechanism. The only scalar-pivot collar left by that argument has

`0 < |d| < 1/16`.                                                       (1.2)

The S0 parent supplies the second-singular-value inheritance

`s_2(S) >= 1`                                                           (1.3)

from account02/B19 r17:

`yspennstate/math-open-problems@fc8343c379bbddf14be670349f664f7fcb39994a`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260922T192830Z-account02-B19-qform-r17/REPORT.md`.

For the exact-rank-two endpoint below I use the completed orientation-free theorem
`QFORM-RANK2-AFFINE-HALF-RIESZ-v1` from

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`:
for an exact rank-two quadratic part with nonzero spectral determinant `D`, arbitrary affine terms and the original product input law,

`H_(1/2) <= 128 D^(-1/4)`.                                             (1.4)

The live corrections were reread before publication. In particular, this report never replaces a tiny nonzero `d` by zero, never selects one tiny coordinate minor and pays its reciprocal, and never rotates the independent coordinates.

## 2. Main theorem: an anchor-centered exterior packet

Let `S` be a real symmetric matrix. Fix one ORIGINAL physical coordinate `h`, permute it first, and write

`S = [[d, w^T], [w, C]]`,                                              (2.1)

where `w` is the complete outside row and `beta=||w||_2`. Let

`s = s_2(S)`                                                           (2.2)

be the second singular value. Define the anchor exterior energy

`E_h = sum_(j != h) ||S e_h wedge S e_j||_2^2`.                        (2.3)

By Cauchy--Binet this is exactly a determinant-weighted packet of ORIGINAL-coordinate `2 x 2` minors:

`E_h = sum_(j != h) sum_(p<q) det S[{p,q},{h,j}]^2`.                  (2.4)

### Theorem 2.1 — `QFORM-ANCHOR-EXTERIOR-PACKET-v1`

One has the dimension-free spectral lower bound

`boxed: E_h >= s^2 (d^2 + beta^2).`                                   (2.5)

Moreover, if `d != 0` and

`T = C - w w^T/d`                                                     (2.6)

is the exact physical scalar Schur complement, then the packet has the exact three-way decomposition

`boxed: E_h = A_h + B_h^shared + B_h^disjoint`,                       (2.7)

where

`A_h = ||d C - w w^T||_F^2 = d^2 ||T||_F^2`,                         (2.8)

`B_h^shared
 = sum_j sum_(p != j) (w_j C_pj - w_p C_jj)^2`,                    (2.9)

and

`B_h^disjoint
 = sum_j sum_(p<q; p,q != j) (w_p C_qj - w_q C_pj)^2`.              (2.10)

All indices in (2.8)--(2.10) are outside `h`. Thus at least one of these three determinant banks carries at least

`s^2(d^2+beta^2)/3`.                                                   (2.11)

### Proof of the spectral lower bound

For any matrix `S` and unit vector `x`, summing the Gram determinant over an orthonormal basis gives

`sum_j ||Sx wedge Se_j||^2
 = ||Sx||^2 ||S||_F^2 - ||S^T Sx||^2`.                                (2.12)

Take `x=e_h`. Diagonalize the positive semidefinite matrix `S^T S` with eigenvalues

`mu_1 >= mu_2 >= ... >= 0`,                                           (2.13)

and write `e_h=sum_k c_k v_k`. Then (2.12) equals

`sum_k c_k^2 mu_k sum_(ell != k) mu_ell`.                             (2.14)

For `k=1`, the inner sum is at least `mu_2`; for every `k>=2`, it is at least `mu_1>=mu_2`. Therefore (2.14) is at least

`mu_2 sum_k c_k^2 mu_k
 = s_2(S)^2 ||S e_h||^2
 = s^2(d^2+beta^2)`.                                                   (2.15)

This proves (2.5). No coordinate selection, support hypothesis, or sign condition occurs.

### Proof of the exact packet split

For the column pair `{h,j}`, an output pair containing `h`, say `{h,p}`, contributes

`det S[{h,p},{h,j}] = d C_pj - w_p w_j`.                              (2.16)

Summing (2.16)^2 over `p,j` gives (2.8).

If the output pair is wholly outside `h`, say `{p,q}`, its minor is

`det S[{p,q},{h,j}] = w_p C_qj - w_q C_pj`.                           (2.17)

If `j` belongs to `{p,q}`, this is the shared class (2.9); if `j` is different from both, it is the disjoint class (2.10). These classes are disjoint and exhaustive, proving (2.7). Finally (2.8) follows from `dT=dC-ww^T`. QED.

## 3. Application to the partner's large-row tiny-pivot collar

In the actual partner collar, (1.1)--(1.3) imply immediately

`E_h > beta^2 > 1/sqrt(200)
     = 0.0707106781186547...`.                                        (3.1)

Hence one of the three banks satisfies

`A_h, B_h^shared, or B_h^disjoint
 > 1/(3 sqrt(200))
 = 0.0235702260395516...`.                                            (3.2)

This is the first essential implication of the run: **the tiny nonzero scalar pivot cannot erase the determinant-weighted coordinate-minor currency.** The currency must move into one of three explicitly physical banks.

### 3a. Disjoint bank gives a genuine original-coordinate cross-bank exit

Fix `h` on the right side and independently color every other physical coordinate left/right with probability `1/2`. Each term of `B_h^disjoint`, indexed by distinct outside coordinates `j,p,q`, lands as the cross minor with columns `{h,j}` on the right and rows `{p,q}` on the left with probability `1/8`.

Therefore some deterministic original-coordinate cut `L|R`, with `h in R`, satisfies

`E_2(S[L,R]) >= B_h^disjoint/8`.                                     (3.3)

If the disjoint class is the winner in (3.2), then

`boxed: E_2(S[L,R]) > 1/(24 sqrt(200))
                    = 0.00294627825494395... .`                       (3.4)

This is exactly an aggregate ridge/cross-bank exit of the kind the existing B07 effective-dimension machinery can consume. No best `2 x 2` minor is selected.

### 3b. Shared bank is exactly a second-pivot / zero-self bank

For `p != j`, put

`m_pj = w_j C_pj - w_p C_jj`.                                       (3.5)

If `C_jj != 0`, let `S^(j)` denote the exact scalar Schur complement after pivoting the ORIGINAL coordinate `j`. Then

`boxed: m_pj = - C_jj S^(j)_ph.`                                    (3.6)

If `C_jj=0`, then instead

`boxed: m_pj = w_j C_pj`,                                           (3.7)

an exact zero-self two-edge product. Thus a winning `B_h^shared` is not an abstract exterior-algebra residue: it is a determinant-weighted bank of genuine second scalar-Schur edges and exact zero-self stars. This routes the collar into the designated second-pivot/zero-self mechanisms without treating a small nonzero diagonal as zero.

### 3c. First-pivot numerator bank

If `A_h` wins, then with the Schur numerator

`N_h = dC-ww^T = dT`,                                               (3.8)

one has

`||N_h||_F > beta/sqrt(3) > 200^(-1/4)/sqrt(3)
                       = 0.153525978386564...`.                     (3.9)

Because `|d|<1/16`, this also forces

`||T||_F > 2.456415654185...`.                                      (3.10)

There is one exact endpoint that is now paid: if `rank(N_h)=1`, then `rank(T)=1`, and the invertible triangular congruence implementing scalar completion gives

`rank(S)=1+rank(T)=2`.                                               (3.11)

Together with `s_2(S)>=1`, both nonzero eigenvalue magnitudes of `S` are at least one. The source-pinned rank-two affine theorem (1.4) therefore yields

`boxed: H_(1/2)(X^T S X + affine) <= 128.`                           (3.12)

Thus the genuinely unpaid `A_h` branch has `rank(N_h)>=2`; the exact rank-one Schur-numerator obstruction is already closed.

## 4. Source-valid stress: aggregate numerator mass does NOT give one useful local pair

The natural next shortcut would assert that a constant `A_h` forces one physical principal pair, or one entry of the Schur numerator, to be uniformly large. This is false in the exact target geometry.

Fix

`d=1/32`, `beta=2`,                                                   (4.1)

and for each `m` let

`v_m = m^(-1/2) (1,...,1)`, `w=2 v_m`, `C=0`,                       (4.2)

and

`S_m = [[d,w^T],[w,0]].`                                             (4.3)

The only nonzero eigenvalues are

`lambda_+ = (d+sqrt(d^2+16))/2 = 2.015686034224956...`,
`lambda_- = (d-sqrt(d^2+16))/2 = -1.984436034224956...`.             (4.4)

Hence `s_2(S_m)>1`. The anchor row has `beta=2`, and `0<d<1/16` exactly as in the tiny-pivot collar.

Here

`T_m = -ww^T/d`, `N_h=dT_m=-ww^T`,                                 (4.5)

so

`A_h=||ww^T||_F^2=beta^4=16`,
`B_h^shared=B_h^disjoint=0`.                                        (4.6)

But every entry of the numerator is

`|(N_h)_pq| = 4/m -> 0`,                                            (4.7)

and every physical principal pair involving the anchor has determinant

`det S_m[{h,j},{h,j}] = -w_j^2 = -4/m ->0`.                         (4.8)

Thus even a fixed **sixteen units** of determinant-weighted anchor packet mass can be spread over `m^2` vanishing Schur numerators. A one-pair or one-entry reciprocal extraction loses dimension and is invalid.

This is a genuine target-class construction, not a counterexample to QFORM. Put

`A_m = [1] direct_sum S_m`.                                          (4.9)

Then `A_m` has the three large eigenvalues `1,lambda_+,lambda_-`. Moreover `S_m` has exact rank two and

`|lambda_+ lambda_-|=4`.                                            (4.10)

For arbitrary independent cap-one inputs, (1.4) gives

`H_(1/2)(X^T S_m X) <= 128 * 4^(-1/4) = 128/sqrt(2)`.                (4.11)

The independent leading square has density bounded by `y^(-1/2)` on `y>0`, so convolution gives the full target-level bound

`||p_(Y^2 + X^T S_m X)||_infinity <= 128/sqrt(2)`.                  (4.12)

Classification of (4.1)--(4.12):

**`QFORM-ANCHOR-PACKET-ONE-LOCAL-MINOR-FALSE-v1` — CANDIDATE_REFUTED for the intermediate local-extraction claim; QFORM itself not refuted.**

The construction is also a useful regression control: it says the aggregate bank `A_h`, rather than any one `dT_pj`, is the correct currency.

## 5. Conditional proof map and first unpaid implication

Applying the completed designated partner r19 at the actual inequality gives the following correction-safe map for the O0/S0 large-row collar:

1. Partner r19 pays the exact-zero anchor and all `|d|>=1/16`; hence only `0<|d|<1/16` survives with `beta>200^(-1/4)`.
2. S0 inheritance gives `s_2(S)>=1`.
3. Theorem 2.1 forces more than `1/sqrt(200)` of anchor-centered second-compound mass despite the tiny pivot.
4. If the disjoint class wins, (3.4) gives a dimension-free ORIGINAL-coordinate `E_2` cross-bank/ridge exit.
5. If the shared class wins, (3.6)--(3.7) gives an exact second-pivot/zero-self bank.
6. If the first-pivot numerator class wins and has rank one, the exact rank-two theorem pays it by (3.12).
7. No proof may replace the remaining aggregate numerator by one local pair: the target family (4.1)--(4.12) disproves that shortcut.

The sharpened first unpaid implication is therefore

**`QFORM-ANCHOR-NUMERATOR-OR-SHARED-BANK-PAYMENT-v1`**:
turn either

`||dT||_F^2 >= 1/(3sqrt(200)),   rank(dT)>=2`,                     (5.1)

or the comparable shared second-pivot determinant bank into a universal product-preserving half-Riesz/density estimate, allowing arbitrarily diffuse entries and arbitrarily small nonzero second pivots. In the numerator branch the natural next split is by its second compound/stable rank: genuinely two-dimensional numerator area should feed the existing ridge/overlap machinery, while the near-rank-one case must be handled without perturbatively deleting its tiny extra directions.

Sibling O0 edge-bank and global O1/O2/O3 synthesis debts remain. Full QFORM and the stronger continuous-density conclusion remain OPEN.

## 6. Computation / regression

`checker.py` and `checker_output.txt` in this immutable run directory verify on seeded random symmetric matrices the exact identity (2.7), the lower bound (2.5), the current constants, and the diffuse stress (4.1)--(4.8). The terminal marker is

`QFORM_ANCHOR_EXTERIOR_PACKET_CHECK_PASS`.

The numerical checker is only a regression aid; all statements above have algebraic proofs.
