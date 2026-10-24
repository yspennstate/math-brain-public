SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B12, 2026-09-23T05:14:24Z.

# account04/B12 r2 — spectral-defect plus hostile-tail core compiler

Programme: QFORM-DENSITY-3EIG-20260922  
Assignment: Additional eigenvalue control  
Status: PROVED_SUPPORTING_STABILITY_THEOREM / ACCOUNT01-B12 APPLIED / FULL QFORM OPEN  
Execution: WITHOUT_VERIFIED_BRAIN

## 1. Scope

The owner target remains the universal density bound for Q = X^T A X, for arbitrary independent real cap-one densities and every symmetric A with at least three eigenvalues of modulus at least one. This report proves a dimension-free localized-core branch. It does not prove that the bare global three-eigenvalue hypothesis supplies the branch.

The baseline physical compression may already have r completely uncontrolled spectral directions. In addition, the first k hostile modes of an arbitrary added matrix may have unrestricted magnitude. Only the residual hostile compression eigenvalue and a deterministic dense-tail operator norm are paid.

No matrix tail is treated as a small random quadratic error.

## 2. Source pins and completed input

Fresh mathematical head before this write:

    yspennstate/math-open-problems@5704e7da5b6134fc8e3bdde6caedc7358a666f65

The completed designated result used below is account01/B12 r25:

    math-open-problems@8a6269fae9183252b85ba2ee787aedd905deef2a
    proofnet24/QFORM-density/fleet-2026-09-22/account01/B12/
    20260923T045406Z-account01-B12-QFORM-r25/REPORT.md

Its finite physical-core endpoint states: on q >= 3 original coordinates, if the actual quadratic block has at least three eigenvalues of modulus at least L, then, uniformly in arbitrary affine terms,

    ||p||_infinity <= 2 sqrt(6 pi q) / L.                       (2.1)

I apply (2.1) to the actual final principal block at (4.8).

The current owner request is brain commit at least c6450eeb9b45d5505db5ecee471d04d7b336fa3f. All live corrections against arbitrary-joint coarea, post-rotation independence, small-random-error use of operator norm, and a universal single good minor are observed.

## 3. The compiler

Let I be a set of m original coordinates and fix sigma in {+1,-1}. On this physical compression write

    A[I,I] = A0[I,I] + R[I,I] + T[I,I].                         (3.1)

Assume that for some kappa > 0 and integer r >= 0,

    N_+(sigma A0[I,I]; kappa) >= m-r.                           (3.2)

Thus the baseline core has at most r uncontrolled directions; it need not be sign-definite. Assume only

    ||T||_op <= delta.                                          (3.3)

For the arbitrary added compression put

    F = sigma R[I,I] = P-N,   P=F_+ >=0,   N=F_- >=0.           (3.4)

Let beta_1 >= ... >= beta_m >= 0 be the eigenvalues of N, and let N_k be its top-k spectral truncation. Then

    rank(N_k) <= k,   ||N-N_k||_op = beta_(k+1).                (3.5)

### Theorem 3.1 (spectral-defect plus hostile-tail compiler)

Let r+k <= m-3 and define

    L = kappa - delta - beta_(k+1).                              (3.6)

If L > 0, then the actual final physical compression satisfies

    N_+(sigma A[I,I]; L) >= m-r-k.                              (3.7)

Consequently every original-coordinate subblock J contained in I of size

    q = r+k+3                                                   (3.8)

has at least three eigenvalues of sign sigma and magnitude at least L. Hence the full ambient quadratic form obeys

    ||p_(X^T A X)||_infinity
       <= 2 sqrt(6 pi (r+k+3)) / (kappa-delta-beta_(k+1)).       (3.9)

The bound is uniform in the ambient dimension, every outside self block and cross coupling, all affine terms created by conditioning, the first k hostile eigenvalues, the entire favorable added spectrum, and all independent cap-one input laws.

## 4. Proof

Write N = N_k + N_tail and set

    M = sigma A0[I,I] + sigma T[I,I] + P - N_tail.              (4.1)

The perturbation E = sigma T[I,I] - N_tail satisfies

    ||E||_op <= delta + beta_(k+1).                              (4.2)

Since P >= 0, Weyl monotonicity and (3.2) give

    lambda_(m-r)(M)
       >= lambda_(m-r)(sigma A0[I,I]) - delta - beta_(k+1)
       >= L.                                                     (4.3)

Thus N_+(M;L) >= m-r. Now

    sigma A[I,I] = M - N_k.                                     (4.4)

Subtracting a positive semidefinite matrix of rank at most k can reduce the number of eigenvalues at or above L by at most k. Equivalently, by the hostile-inertia inequality used in account01/B12,

    N_+(M-N_k;L) >= N_+(M;L)-k >= m-r-k.                        (4.5)

This proves (3.7).

Choose any J contained in I with |J| = q = r+k+3. Let lambda_1 >= ... >= lambda_m be the eigenvalues of sigma A[I,I], and mu_1 >= ... >= mu_q those of sigma A[J,J]. Equation (4.5) gives

    lambda_(m-r-k) >= L.

Cauchy interlacing after deleting m-q physical coordinates gives

    mu_3 >= lambda_(3+m-q) = lambda_(m-r-k) >= L.               (4.6)

Therefore the actual final q by q principal block has three eigenvalues of modulus at least L. Condition on all original coordinates outside J. The coordinates X_J remain independent and cap one; outside couplings become only an arbitrary affine term. Applying the completed account01/B12 endpoint (2.1) to this actual block yields

    ||p_(X^T A X)||_infinity
       <= 2 sqrt(6 pi q)/L
       = 2 sqrt(6 pi (r+k+3))/(kappa-delta-beta_(k+1)).          (4.7)

This proves (3.9).

## 5. Concrete full-target inequality

Take r=k=1, m >= 5, and suppose on an actual original-coordinate core I,

    N_+(sigma A0[I,I]; 2) >= m-1,
    ||T||_op <= 1/2,
    beta_2 <= 1/2.                                               (5.1)

Then L >= 1, and a five-coordinate physical principal block of the final matrix has three actual eigenvalues of sign sigma and magnitude at least one. Equation (4.7) gives

    ||p_(X^T A X)||_infinity
       <= 2 sqrt(30 pi)
       = 19.4162591255... .                                      (5.2)

The one baseline defect direction and the leading hostile added mode are both completely free in magnitude and orientation. Favorable added modes, arbitrary outside spectrum, and all outside couplings are also free.

This is strictly beyond the sign-definite baseline case r=0: one may lose a genuine baseline direction before the arbitrary added spectrum is applied and still recover an actual bounded-dimensional spectral core.

## 6. Exact remaining gap

The full conjecture remains open. The bare global condition s_3(A) >= 1 does not currently force a decomposition (3.1) on a physical core with bounded r+k and positive margin

    kappa - delta - beta_(k+1) > 0.

Diffuse no-pivot matrices may have no such locally protected core. The complementary branch still must force a volume/ridge/grouped-bank/mixed-hub certificate when every candidate core has either many baseline defects or a large residual hostile tail.

Continuity is separate. The present argument proves essential boundedness only.

## 7. Correction compliance

No post-rotation independence is used. No arbitrary-joint coarea estimate is used. No worst-fiber conditional density cap is used. The operator norm in (4.2) is used only in deterministic eigenvalue perturbation. No universal single minor is assumed: once I is given, every J contained in I of the displayed size works by interlacing. The final spectral hypothesis is verified on the actual final principal block before account01/B12 is invoked.
