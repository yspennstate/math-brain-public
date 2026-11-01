# fleet02/B12 — sign-routed physical cores with full dense-tail Schur stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control / complementary constructions and source-valid obstructions  
Status: **PROVED_SUPPORTING_THEOREMS / FULL_QFORM_OPEN**  
Continuity: **not claimed by the assembled argument**  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. First unpaid implication and sources actually used

The full target is still open. The current fleet03/B12 partner reduction shows that a form with at least four eigenvalues beyond a scale can, unless a paid physical-pair or ridge exit already fires, be reduced after at most one ORIGINAL-coordinate scalar Schur step to a three-large-eigenvalue low-pivot residual. Its completed one-sided scalar compiler states that if

`Q = a (X+m(Y))^2 + R(Y)` and `||p_R||_infinity <= M`, then

`||p_Q||_infinity <= 2 sqrt(M/|a|)`.

Source: `yspennstate/math-open-problems@c1a3b7726053b017abea5f96f1be1df48c9e6028`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260923T034842Z-qform-eigenvalue-r24/REPORT.md` (using its cited r23 compiler).

The required newest-Claude source `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`, proves the localized three-coordinate theorem used below: if an ORIGINAL-coordinate physical `3 x 3` principal quadratic block has all three eigenvalue magnitudes at least `c>0`, then after conditioning on every other original coordinate,

`||p_Q||_infinity <= 6 sqrt(pi)/c`,

uniformly in the induced affine terms. This is Theorem A in that source. No spectral-coordinate independence is involved.

This run attacks a matrix-level stability question left between those two ingredients: when an arbitrary signed eigenvalue replacement is large, a fixed local core can resonate; can two physical cores route the sign, and can that certificate survive a completely nonseparable small operator-norm tail and one preceding scalar Schur step?

## 2. General dual-core sign-routing lemma

Let `A0` be symmetric and let `v` be any vector. Let `H_+` and `H_-` be physical triples. Write

`B_sigma = A0[H_sigma,H_sigma]`,  `u_sigma = v[H_sigma]`,

and suppose both `B_sigma` are invertible. Put

`q_sigma = u_sigma^T B_sigma^{-1} u_sigma`.

Assume

`q_+ > 0`,  `q_- < 0`.                                             (2.1)

For `sigma in {+,-}` define

`gamma_sigma = ( ||B_sigma^{-1}||op + ||B_sigma^{-1}u_sigma||_2^2 / |q_sigma| )^{-1}`,

and `gamma=min(gamma_+,gamma_-)`.

### Lemma 2.1 — magnitude-free rank-one stability after sign routing

For every real `tau`, choose `H_+` if `tau>=0` and `H_-` if `tau<=0`. Then

`sigma_min( B_sigma + tau u_sigma u_sigma^T ) >= gamma_sigma`.       (2.2)

**Proof.** Sherman-Morrison gives

`(B+tau uu^T)^{-1} = B^{-1} - [tau/(1+tau q)] B^{-1}u u^T B^{-1}`.

Under the sign choice, `tau q>=0`, hence `|1+tau q|=1+|tau q|` and

`|tau|/|1+tau q| <= 1/|q|`.

Therefore

`||(B+tau uu^T)^{-1}||op
 <= ||B^{-1}||op + ||B^{-1}u||_2^2/|q| = gamma_sigma^{-1}`.

This proves (2.2). The estimate is independent of `|tau|`.  QED.

### Corollary 2.2 — arbitrary full-rank dense tail

Let `T` be any symmetric matrix, of arbitrary rank and sign, with `||T||op<=delta<gamma`. Then the selected physical triple of

`A = A0 + tau vv^T + T`

has smallest singular value at least `gamma-delta`. The newest-Claude physical-three-coordinate theorem therefore gives

`boxed: ||p_(X^T A X)||_infinity <= 6 sqrt(pi)/(gamma-delta).`        (2.3)

This is a matrix-certificate perturbation argument. It does **not** assert that `X^T T X` is a small random variable; for unbounded cap-one laws that assertion is false.

## 3. Full dense-tail propagation through one physical scalar Schur step

The preceding result can be placed behind the dependence-safe scalar compiler without requiring the dense perturbation to be block diagonal.

Partition a baseline in ORIGINAL coordinates as

`A0 = [[a0, b0^T], [b0, C0]]`,  `a0 != 0`,

and let

`S0 = C0 - b0 b0^T/a0`                                             (3.1)

be its scalar Schur complement. Let the rank-one spectral change be supported off the pivot,

`v=(0,w)`.

Add an arbitrary symmetric dense perturbation

`T = [[e, c^T], [c,E]]`,  `||T||op <= delta < |a0|`.                 (3.2)

The actual pivot is `a=a0+e`, so `|a|>=|a0|-delta`. The actual Schur quadratic matrix equals

`S_tau,T = S0 + tau ww^T + Delta`,                                  (3.3)

where

`Delta = E - (b0+c)(b0+c)^T/(a0+e) + b0 b0^T/a0`.

Expanding the last two terms and using `||E||<=delta`, `||c||<=delta`, `|e|<=delta` gives the deterministic bound

`||Delta||op <= rho`,                                               (3.4)

with

`rho = delta
     + (2||b0|| delta + delta^2)/(|a0|-delta)
     + ||b0||^2 delta/(|a0|(|a0|-delta)).`                          (3.5)

No random input appears in this estimate.

Assume now that two physical triples of the baseline Schur matrix `S0` satisfy (2.1), with `u_sigma=w[H_sigma]`, and let `gamma` be their dual-core constant. If

`rho < gamma`,                                                      (3.6)

then Lemma 2.1 plus Weyl gives a selected physical triple of the **actual Schur remainder** with gap at least `gamma-rho`. The newest-Claude Theorem A therefore gives

`||p_R||infinity <= 6 sqrt(pi)/(gamma-rho)`.                        (3.7)

Applying the completed fleet03/B12 one-sided scalar compiler to the actual pivot yields the hybrid bound

`boxed:
 ||p_Q||infinity
 <= 2 sqrt( 6 sqrt(pi) / [ (|a0|-delta)(gamma-rho) ] ).`            (3.8)

This theorem simultaneously permits:

* an arbitrary-magnitude rank-one change `tau vv^T`, with either sign of `tau`;
* a completely nonseparable dense tail `T` of arbitrary rank and sign;
* arbitrary dependence between the completed scalar square and its Schur remainder.

The only localization is in the deterministic physical certificates (2.1), not in the random variables after a spectral rotation.

For the useful block-diagonal baseline case `b0=0`, (3.5) reduces to

`rho <= delta + delta^2/(|a0|-delta).`                              (3.9)

## 4. Exact literal eigenvalue-replacement family

The dual-core hypothesis is non-vacuous even when the added direction is an **actual eigenvector** and its eigenvalue is replaced by an arbitrary real number.

Set

`C = [[ 4,-3,-3, 3],
      [-3, 4,-3, 3],
      [-3,-3, 4, 3],
      [ 3, 3, 3,-8]]`,                                             (4.1)

and

`v=(1,1,1,1)^T/2`.

Every row sum of `C` equals `1`, hence `Cv=v`. Two independent vectors supported on the first three coordinates and summing to zero have eigenvalue `7`, while `(1,1,1,-3)^T` has eigenvalue `-11`. Therefore

`spec(C)={1,7,7,-11}`                                               (4.2)

and, for every real `tau`,

`C_tau = C + tau vv^T`

has the exact spectrum

`spec(C_tau)={1+tau,7,7,-11}`.                                     (4.3)

Thus the eigenvalue `1` is literally replaced by the arbitrary real eigenvalue `1+tau`; it may be smaller, larger, zero, or of either sign, while three large eigenvalues remain fixed.

### 4.1 Negative-tau core

Take

`H_-={1,2,3}`.

Then

`B_- = 7 I_3 - 3 J_3`,  `u_-=(1,1,1)^T/2`.

The vector `u_-` lies in the one-dimensional eigenline of eigenvalue `-2`, and

`q_- = u_-^T B_-^{-1}u_- = -3/8`.                                  (4.4)

For `tau<=0`, the two orthogonal eigenvalues stay `7` and the negative eigenvalue becomes

`-2 + 3 tau/4 <= -2`.

Hence

`sigma_min(B_- + tau u_-u_-^T) >= 2`.                              (4.5)

### 4.2 Positive-tau core

Take

`H_+={2,3,4}`.

Then

`B_+ = [[4,-3,3],[-3,4,3],[3,3,-8]]`,  `u_+=(1,1,1)^T/2`.           (4.6)

A direct inverse calculation gives

`q_+ = 27/104 >0`.                                                  (4.7)

The baseline eigenvalues are

`7`,  `(3 sqrt(17)-7)/2`,  `-(3 sqrt(17)+7)/2`.                    (4.8)

For `tau>=0`, the update is positive semidefinite, so the two positive ordered eigenvalues cannot decrease. The vector

`x=(1,1,-2)^T`

satisfies `x perpendicular u_+` and

`x^T B_+ x / ||x||^2 = -9`.                                        (4.9)

The rank-one update vanishes on `x`, so the least eigenvalue of the updated block is at most `-9`. Consequently

`sigma_min(B_+ + tau u_+u_+^T)
 >= (3 sqrt(17)-7)/2 > 2`.                                         (4.10)

Combining (4.5) and (4.10), for **every** real `tau` one of these two physical triples has all three eigenvalue magnitudes at least `2`.

### 4.3 Dense-tail theorem for the literal replacement family

Let `E` be any symmetric `4 x 4` matrix with

`||E||op <= 1/4`.                                                   (4.11)

The sign-selected physical triple of `C_tau+E` has gap at least

`2-1/4=7/4`.                                                        (4.12)

Applying the required newest-Claude Theorem A after conditioning on the fourth original coordinate gives

`boxed:
 ||p_(X^T(C_tau+E)X)||infinity
 <= 6 sqrt(pi)/(7/4)
 = 24 sqrt(pi)/7
 = 6.076984631676055...`                                           (4.13)

for every real `tau`, every independent cap-one product law, and every dense tail (4.11).

This family remains far inside the target class: from (4.3), `s_3(C_tau)>=7`, so singular-value Weyl gives

`s_3(C_tau+E) >= 7-1/4 = 27/4 >1`.                                 (4.14)

Thus (4.13) is a genuine arbitrary-eigenvalue-replacement plus full-dense-tail target-class stability theorem.

## 5. Source-valid obstruction to one fixed physical core

The same exact family shows why sign routing is needed. The determinant lemma gives

`det(B_sigma+tau u_sigma u_sigma^T)=det(B_sigma)(1+tau q_sigma)`.

For the negative core (4.4), it becomes singular at

`tau=8/3`.

For the positive core (4.7), it becomes singular at

`tau=-104/27`.

At both values the **full** matrix still has the three fixed large eigenvalues `7,7,-11`. Hence no proof may demand that either one of these fixed triples remain uniformly conditioned under arbitrary signed replacement of the fourth eigenvalue. The obstruction is to a fixed-core proof interface, not to QFORM itself. The two-core sign-routed certificate removes both resonances.

## 6. Concrete partner application: one extra scalar eigenvalue plus a full dense tail

Now add one more physical coordinate and consider the five-dimensional baseline

`A_tau^0 = diag(2, C_tau)`.                                        (6.1)

Let `T` be **any** symmetric `5 x 5` matrix with `||T||op<=1/4`, including arbitrary pivot-to-residual cross coupling. The actual first pivot `a` obeys

`|a|>=7/4`.                                                        (6.2)

Write the lower-right compression of `T` as `E` and its first off-diagonal column as `c`. The actual Schur remainder is

`C_tau + E - cc^T/a`.

Therefore

`||E-cc^T/a||op
 <= 1/4 + (1/4)^2/(7/4)
 = 1/4 + 1/28
 = 2/7`.                                                           (6.3)

The sign-selected triple from Section 4 consequently has Schur-core gap at least

`2-2/7 = 12/7`.                                                     (6.4)

The newest-Claude localized theorem gives the Schur remainder density cap

`M <= 6 sqrt(pi)/(12/7) = 7 sqrt(pi)/2`.                            (6.5)

Now apply the completed fleet03/B12 one-sided scalar compiler to the **actual** first coordinate. Using (6.2),

`||p_Q||infinity
 <= 2 sqrt( M/|a| )
 <= 2 sqrt( (7 sqrt(pi)/2)/(7/4) )
 = 2 sqrt(2 sqrt(pi))
 = 3.765585055106859... .`                                         (6.6)

This is the requested compatible partner result applied at an actual inequality. The completed square is dependent on the Schur remainder; (6.6) does not use an independent-convolution step.

The five-dimensional family is also robustly inside the target class. Before `T`, it has the four fixed absolute eigenvalues `2,7,7,11`, independently of `tau`; hence

`s_4(A_tau^0+T) >= 2-1/4=7/4>1`.                                  (6.7)

So (6.6) controls a target-class family with one extra large direction, one literal arbitrary real eigenvalue replacement, and an arbitrary full-rank dense tail.

## 7. Why small operator norm is used only at matrix level

Nothing above bounds `X^T T X` in probability by `||T||`. Such a bound is impossible under the target assumptions: with `T=delta e_1e_1^T` and `X_1` uniform on `[R,R+1]`, which has density cap one,

`X^T T X >= delta R^2`

almost surely. The operator norm enters only through Weyl inequalities and the exact Schur perturbation formula (3.3)-(3.5).

## 8. Finite sanity check

`CHECKER.py` runs a deterministic 3,000-case stress suite over `tau` from `-10^6` to `10^6` and random symmetric tails of operator norm at most `1/4`. It checks the proved lower bounds on the selected Schur core, the Schur-tail norm, and the third/fourth singular values of the direct and scalar-extended target families. `CHECKER_OUTPUT.json` records zero violations. These computations are sanity checks only; Sections 2-6 are analytic proofs.

## 9. Remaining implication

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.** The new result pays a precise class in which a large signed eigenvalue change can resonate one physical core but a second core has the opposite inverse leverage; a full dense tail then costs only its matrix norm, and one preceding scalar Schur step costs the explicit dependence-safe compiler factor.

The first unpaid structural implication is now: from the bare no-pivot/high-window-leverage residual produced by the partner reduction, force either (i) a finite sign-routable family of physical triples/pairs of the type above, (ii) a weighted-volume/grouped-bank certificate already paid by D'/D5/collective-tail theory, or (iii) a hub/ridge exit. No such extraction from `s_3(A)>=1` is claimed here.
