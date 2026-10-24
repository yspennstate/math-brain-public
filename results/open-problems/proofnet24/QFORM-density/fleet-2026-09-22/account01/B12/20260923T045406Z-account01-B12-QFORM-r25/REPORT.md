SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-23T04:54:06Z.
attacking: local hostile-spectrum truncation — make the largest k hostile added eigenvalues free on a protected physical core, pay only the (k+1)-st hostile compression eigenvalue, and descend by interlacing to a fixed physical subcore.

# account01/B12 r25 — local hostile-tail truncation for arbitrary additional spectrum

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Assignment:** Additional eigenvalue control  
**Status:** PROVED_SUPPORTING_STABILITY_THEOREM / PARTNER_APPLIED / FULL_QFORM_OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN

## 1. Target and point of the run

The full owner target remains open: for independent original-coordinate inputs with one-dimensional densities bounded by one and every real symmetric A with at least three eigenvalues of modulus at least one, prove a universal essential density bound for X^T A X, or give a valid counterexample. No rotated-coordinate independence is used below. Continuity is tracked separately and is not proved by this branch.

The additional-eigenvalue question is subtle because a large spectral perturbation is generally dependent on the base quadratic form after rotation. This report gives a purely deterministic physical-core compiler. On a sign-definite original-coordinate core, the top k *hostile local spectral modes* of an arbitrary added matrix may have completely unrestricted magnitude. Only the (k+1)-st hostile eigenvalue of the physical compression is paid. Arbitrarily many favorable eigenvalues are free, and an arbitrary-rank dense operator-norm tail is paid once by Weyl.

The main new gain over a rank/inertia count is that a perturbation can have huge hostile inertia globally while being almost rank k in its hostile action on the chosen physical core. The theorem charges the latter quantity rather than the global number or size of hostile eigenvalues.

## 2. Completed designated-partner input actually used

The designated partner `account02/B12` proved the localized hostile-inertia theorem in

`yspennstate/math-open-problems@36263ba314738468f934a5b3245130b6754e940f`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260923T021551Z-account02-B12-qform-r23/REPORT.md`.

For symmetric M,E and threshold L>0 it uses the exact inequality

    N_+(M+E;L) >= N_+(M;L) - nu_-(E),                         (2.1)

and its sign-reversed analogue. The same partner report supplies the finite-core endpoint: on q>=3 original independent coordinates, if the actual q x q quadratic matrix has at least three eigenvalues of modulus at least L, then, uniformly in arbitrary affine terms,

    ||p||_infinity <= 2 sqrt(6 pi q) / L.                      (2.2)

I apply (2.1) at equation (4.7) below and (2.2) at equation (4.10). Thus the partner result is used at an actual inequality, not cited cosmetically.

For one small edge case I also use the completed physical-three-block endpoint

`yspennstate/math-open-problems@36263ba314738468f934a5b3245130b6754e940f`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260922T141530Z-two-samesign-threeblock/REPORT.md`, Theorem 6.1: if an actual physical 3 x 3 block has two eigenvalues >=L (or two <=-L), with the third arbitrary, then

    ||p_Q||_infinity <= C_* / L,
    C_* = 24.183038289961516... .                              (2.3)

All outside coefficients and cross couplings are allowed because one conditions only on outside ORIGINAL coordinates.

## 3. Hostile spectrum of a physical compression

Fix a sign sigma in {+1,-1}. Let I be a set of m original coordinates, m>=3. Suppose a baseline A0 has a protected sign-definite physical core

    sigma A0[I,I] >= kappa I_m                                  (3.1)

in Loewner order, with kappa>0.

Write the full matrix as

    A = A0 + R + T,                                              (3.2)

where R is completely arbitrary symmetric and T is a dense tail satisfying only

    ||T||_op <= delta.                                           (3.3)

There is no rank, sign, or magnitude restriction on R.

On the physical core define

    F = sigma R[I,I].                                            (3.4)

Take the positive/negative-part decomposition

    F = P - N,       P=F_+ >=0,       N=F_- >=0.                 (3.5)

Let

    beta_1 >= beta_2 >= ... >= beta_m >=0                        (3.6)

be the eigenvalues of N, padded by zeros. These are the magnitudes of the hostile negative eigenvalues of the *actual physical compression* sigma R[I,I]. They need not agree with the eigenvalues of a spectral-coordinate restriction, and no probabilistic independence is attached to them.

For 0<=k<=m let N_k be the top-k spectral truncation of N:

    N_k = sum_{j=1}^k beta_j y_j y_j^T,
    N_tail = N-N_k.                                              (3.7)

Then exactly

    rank N_k <= k,
    ||N_tail||_op = beta_{k+1},                                  (3.8)

with beta_{m+1}:=0. Equivalently, by Eckart-Young in the PSD cone,

    beta_{k+1}
      = min{ ||N-K||_op : K>=0, rank K<=k }.                     (3.9)

Thus beta_{k+1} is the exact local operator-norm distance of the hostile part from rank k.

## 4. Main theorem: pay only the hostile tail after k free modes

### Theorem 4.1 — QFORM-LOCAL-HOSTILE-TAIL-TRUNCATION-v1

Assume (3.1)-(3.6). Let 0<=k<=m-3 and suppose

    L := kappa - delta - beta_{k+1} >0.                           (4.1)

Then the final physical core B=A[I,I] has at least m-k eigenvalues of sign sigma and magnitude at least L. More precisely,

    N_+(sigma B;L) >= m-k.                                       (4.2)

Consequently every physical principal subblock J subset I of size k+3 has at least three eigenvalues of sign sigma and magnitude at least L, and the full ambient quadratic form satisfies

    boxed:
    ||p_(X^T A X)||_infinity
       <= 2 sqrt(6 pi (k+3)) / L.                                (4.3)

The bound is uniform over the dimension, all outside quadratic coefficients and cross couplings, the magnitudes and signs of every eigenvalue of R, and all independent cap-one input laws, subject only to the displayed local hostile-tail condition.

### Proof

Compress (3.2) to I and multiply by sigma. By (3.5) and (3.7),

    sigma B
      = sigma A0[I,I] + sigma T[I,I] + P - N_tail - N_k.         (4.4)

Set

    M = sigma A0[I,I] + sigma T[I,I] + P - N_tail.               (4.5)

Compression is operator-norm contractive, so

    sigma T[I,I] >= -delta I_m.                                  (4.6)

Using P>=0 and ||N_tail||_op=beta_{k+1}, equations (3.1), (4.5), (4.6) give

    M >= (kappa-delta-beta_{k+1}) I_m = L I_m.

Hence N_+(M;L)=m. Now apply the completed designated-partner hostile-inertia inequality (2.1) to the **actual physical core**, with perturbation E'=-N_k. Since -N_k is negative semidefinite and rank at most k,

    N_+(sigma B;L)
      = N_+(M-N_k;L)
      >= N_+(M;L) - nu_-(-N_k)
      >= m-k.                                                    (4.7)

This is the required actual application of the account02/B12 result.

Let J be any subset of I with |J|=k+3. Order the eigenvalues of sigma B decreasingly as lambda_1>=...>=lambda_m, and those of sigma B[J,J] as mu_1>=...>=mu_{k+3}. Equation (4.7) gives

    lambda_{m-k} >= L.                                           (4.8)

Cauchy interlacing after deleting m-(k+3) physical coordinates gives

    mu_3 >= lambda_{3+m-(k+3)} = lambda_{m-k} >= L.              (4.9)

Thus the actual (k+3)-coordinate physical block B[J,J] has at least three eigenvalues of modulus at least L. Condition on every original coordinate outside J. The variables X_J remain mutually independent with their original density caps, while all outside cross terms become an arbitrary affine tilt. Apply the partner finite-core endpoint (2.2) with q=k+3:

    ||p_(X^T A X)||_infinity
      <= 2 sqrt(6 pi (k+3))/L.                                   (4.10)

This proves (4.3). QED.

### Interpretation

The top k hostile eigenvalues beta_1,...,beta_k do not appear anywhere in (4.3). They may tend to infinity. The entire favorable part P is also free. Only the residual hostile curvature beta_{k+1}, plus the dense-tail norm delta, is paid.

No random variable X^T T X is asserted to be small. The norm delta is used only in the deterministic matrix inequality (4.6).

## 5. Dimension-free one-hostile-mode corollary

The case k=1 is especially relevant to the one-additional-large-eigenvalue bottleneck. If m>=4 and

    delta + beta_2 < kappa,                                      (5.1)

then

    boxed:
    ||p_Q||_infinity
      <= 4 sqrt(6 pi)/(kappa-delta-beta_2)
      = 17.366430109398.../(kappa-delta-beta_2).                 (5.2)

Thus one hostile local spectral mode is completely free in magnitude, on a protected physical core of arbitrary size, with a universal constant independent of m.

If m=3, the same deterministic argument gives two positive eigenvalues of sigma B at least

    L=kappa-delta-beta_2.

The completed two-same-sign physical-three-block theorem (2.3) therefore gives the edge-case bound

    boxed:
    ||p_Q||_infinity <= 24.183038289961516.../L.                 (5.3)

So the one-mode theorem holds uniformly for every m>=3, with constant 24.184/L if a single numerical constant is desired.

This strictly localizes the price: R may have arbitrarily many hostile eigenvalues globally. They are harmless here whenever their action on I has only one large hostile singular/eigen-direction and the rest of the negative compressed spectrum lies below kappa-delta.

## 6. Global spectral corollary

The local beta_{k+1} can be bounded directly from the global added spectrum. Let the negative eigenvalues of sigma R have magnitudes

    h_1 >= h_2 >= ... >=0.                                      (6.1)

By Cauchy interlacing for the principal compression sigma R[I,I],

    beta_{k+1} <= h_{k+1}.                                      (6.2)

Hence Theorem 4.1 yields the following simple sufficient condition:

    delta + h_{k+1} < kappa                                    (6.3)

implies

    boxed:
    ||p_Q||_infinity
      <= 2 sqrt(6 pi (k+3))
         /(kappa-delta-h_{k+1}).                                (6.4)

The first k hostile global eigenvalues may have arbitrary magnitude. Every favorable global eigenvalue may have arbitrary magnitude and multiplicity. There may also be arbitrarily many further hostile eigenvalues; only their largest residual magnitude h_{k+1} enters.

Thus the theorem directly handles a large class of simultaneous smaller and larger additions of either sign without any convolution assumption.

## 7. Concrete target-class applications

### 7.1 Two arbitrary hostile spikes plus an arbitrary smaller hostile cloud

Let I contain five original coordinates and let

    A0[I,I] >= 2 I_5.                                           (7.1)

Add an arbitrary symmetric R. Relative to the positive sign, suppose R has at most two negative eigenvalues of magnitude exceeding one; equivalently h_3<=1. Positive eigenvalues of R are unrestricted in number and size, and the two largest negative eigenvalues are unrestricted in size and orientation.

Take k=2, kappa=2, delta=0. Then L>=1 and Theorem 4.1 gives the actual ambient inequality

    boxed:
    ||p_Q||_infinity <= 2 sqrt(30 pi)
                      = 19.41625912555699... .                   (7.2)

The final physical 5-core itself has at least three positive eigenvalues >=1, so the final ambient matrix is automatically in the owner target class. Arbitrary outside matrix entries and couplings are retained.

### 7.2 One arbitrary hostile spike and an arbitrary-rank dense tail

Let I have at least four coordinates and A0[I,I]>=I. Let R be arbitrary with second hostile compression eigenvalue beta_2, and let ||T||op<=delta. If

    delta+beta_2 <= 1/2,                                       (7.3)

then (5.2) gives

    boxed:
    ||p_Q||_infinity <= 8 sqrt(6 pi)
                      = 34.73286021879684... .                   (7.4)

The leading hostile compressed eigenvalue beta_1 is unrestricted and may diverge. The favorable compressed spectrum is unrestricted. The tail T may have arbitrary rank and arbitrary signs.

## 8. Exact scope and remaining implication

This result is a genuine additional-spectrum stability theorem, not the full conjecture. The bare global hypothesis s_3(A)>=1 does not itself provide a sign-definite physical core (3.1) with a favorable hostile-tail parameter beta_{k+1}. Diffuse rank-three configurations can have no uniformly conditioned bounded physical core, and the live correction set rules out replacing that structural problem by a universal one-good-minor or cross-rank-three assertion.

The next target-facing implication is therefore a branch switch: when no protected physical core has small local hostile tail after one or a few free modes, force a diffuse-volume/ridge/grouped-bank/hub certificate before paying reciprocal local curvature. The newest account02/B12 five-volume/leaky-shield theorem is a natural complementary exit for that regime, but no universal structural dichotomy is proved here.

**Continuity:** this report proves essential boundedness in its stated scope. The partner finite-core and two-same-sign endpoints used here do not supply a continuity statement in the cited form, so no continuity claim is made.

## 9. Correction compliance

No law-uniform pointwise quadratic-phase decay is used. No arbitrary-joint coarea bound is used. No normalized worst-fiber density cap is used. No spectral rotation is used to claim probabilistic independence. No small operator-norm matrix is treated as a small random quadratic variable. No universal good physical minor or universal rank-three cross cut is asserted. The designated partner result is applied to the actual final physical matrix at (4.7) and (4.10).
