SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T06:44:11Z.
attacking: hybrid hostile-spectrum stability: strip arbitrary hostile spikes, average only the residual hostile trace over a small original-coordinate subset, then apply the completed account04/B12 hostile-tail compiler.

# account03/B12 r27 — Ky Fan spike stripping plus mean hostile-tail stability

Programme: QFORM-DENSITY-3EIG-20260922
Assignment: Additional eigenvalue control
Status: PROVED SUPPORTING STABILITY THEOREM / DESIGNATED account04/B12 RESULT APPLIED / FULL QFORM OPEN
Continuity: not proved by this branch; essential boundedness only
Execution: WITHOUT_VERIFIED_BRAIN

## 1. Scope and source pins

Let X=(X_1,...,X_n) have independent real coordinates with probability densities bounded by one, and let A=A^T. No moment, support, Gaussian, log-concavity, identical-law, or post-rotation independence hypothesis is used.


The designated partner result actually applied below is:

    yspennstate/math-open-problems@f319b51a1b43b4904c8784348f0a3725954bb7e7
    proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/
    20260923T051424Z-account04-B12-spectral-defect-hostile-tail-r2/REPORT.md

Its theorem says: on an original-coordinate core of size m0, if the baseline compression has at least m0-r eigenvalues of one chosen sign at least kappa, an arbitrary added compression has hostile eigenvalues beta_1>=...>=beta_m0>=0, a further dense perturbation has operator norm at most delta, and r+k<=m0-3, then whenever

    L = kappa-delta-beta_(k+1) > 0,

one has

    ||p_(X^T A X)||_infinity <= 2 sqrt(6 pi (r+k+3)) / L.      (1.1)

All outside self-blocks and cross couplings are retained. The theorem uses the operator norm only for deterministic eigenvalue perturbation, not to claim the random quadratic remainder is small.

## 2. New theorem

Fix an ORIGINAL-coordinate core I of size m and a sign sigma in {+1,-1}. Decompose on I

    A[I,I] = A0[I,I] + R[I,I] + T[I,I].                        (2.1)

Assume

    N_+(sigma A0[I,I]; kappa) >= m-r                          (2.2)

for some kappa>0 and integer r>=0, and

    ||T[I,I]||_op <= delta < kappa.                            (2.3)

Write the Jordan decomposition of the arbitrary added compression

    sigma R[I,I] = P-N,     P,N >= 0.                         (2.4)

Let the eigenvalues of N be

    beta_1 >= beta_2 >= ... >= beta_m >= 0.                    (2.5)

For an integer K>=0, let N_K be the top-K spectral truncation of N (N_0=0), let

    H_K := N-N_K,
    tau_K := tr(H_K)/m = (1/m) sum_{j>K} beta_j.                (2.6)

Thus the first K hostile eigenvalues are completely excluded from tau_K and may be arbitrarily large.

### Theorem 2.1 — QFORM-KYFAN-MEAN-HOSTILE-TAIL-STABILITY-v1

Let

    0 <= K <= m-r-3                                           (2.7)

and choose any integer q with

    r+K+3 <= q <= m.                                          (2.8)

Put

    ell := q-r-K-2 >= 1,                                      (2.9)

and

    L_(q,K) := kappa-delta - q tau_K / ell.                    (2.10)

If L_(q,K)>0, then the FULL ambient quadratic form has a density satisfying

    boxed:
    ||p_(X^T A X)||_infinity
       <= 2 sqrt(6 pi q) / L_(q,K).                            (2.11)

The first K hostile added eigenvalues may have arbitrary magnitude and orientation. Every favorable added eigenvalue is free. The residual hostile tail H_K may have arbitrary rank and arbitrarily large individual eigenvalues; only its mean spectral mass tau_K is charged. Everything outside I, including arbitrarily large/small eigenvalues of either sign and all cross couplings, is unrestricted.

This is strictly different from a small-operator-norm tail theorem: no bound on ||H_K||_op is assumed.

## 3. Proof

### 3.1 Select a physical q-set with small residual hostile trace

For each q-subset J of I,

    tr H_K[J,J] = sum_{i in J} (H_K)_ii.                       (3.1)

Averaging uniformly over all q-subsets, each coordinate appears with probability q/m. Hence

    E_J tr H_K[J,J] = (q/m) tr H_K = q tau_K.                  (3.2)

Therefore there exists an ORIGINAL-coordinate q-subset J such that

    tr H_K[J,J] <= q tau_K.                                   (3.3)

No probabilistic statement about X is used here; this is a deterministic averaging identity.

### 3.2 Baseline spectral defect does not worsen on J

Let lambda_1>=...>=lambda_m be the eigenvalues of sigma A0[I,I], and mu_1>=...>=mu_q those of sigma A0[J,J]. From (2.2),

    lambda_(m-r) >= kappa.                                    (3.4)

Cauchy interlacing for the principal compression gives

    mu_(q-r) >= lambda_(m-r) >= kappa.                         (3.5)

Thus

    N_+(sigma A0[J,J]; kappa) >= q-r.                          (3.6)

So the same defect count r is valid on the selected physical q-core.

### 3.3 Bound the partner theorem's local hostile residual by the global mean tail

Let

    F_J := sigma R[J,J].                                       (3.7)

Denote by eta_1>=...>=eta_q>=0 the eigenvalues of the negative part (F_J)_-. Since

    -F_J = N_K[J,J] + H_K[J,J] - P[J,J]
          <= N_K[J,J] + H_K[J,J]                              (3.8)

in Loewner order, min-max monotonicity gives

    eta_j <= lambda_j(N_K[J,J]+H_K[J,J])                      (3.9)

for every j.

The matrix N_K[J,J] has rank at most K. Hence Weyl's rank-K inequality yields, for every a>=1 with K+a<=q,

    lambda_(K+a)(N_K[J,J]+H_K[J,J])
       <= lambda_a(H_K[J,J]).                                  (3.10)

Now choose the partner theorem's local hostile allowance

    k := q-r-3.                                                (3.11)

Then

    k+1 = q-r-2 = K+ell,                                       (3.12)

where ell is (2.9). Combining (3.9)-(3.12),

    eta_(k+1)
      <= lambda_ell(H_K[J,J])
      <= tr H_K[J,J]/ell
      <= q tau_K/ell.                                          (3.13)

The middle inequality is the elementary PSD bound ell*lambda_ell <= trace.

### 3.4 Apply the completed account04/B12 theorem

On the selected q-coordinate physical core J we now have:

    N_+(sigma A0[J,J]; kappa) >= q-r,
    ||T[J,J]||_op <= delta,
    r+k = q-3,
    eta_(k+1) <= q tau_K/(q-r-K-2).                            (3.14)

All hypotheses of the completed account04/B12 theorem (1.1) hold. Its residual gap is at least L_(q,K), so if L_(q,K)>0,

    ||p_(X^T A X)||_infinity
       <= 2 sqrt(6 pi (r+k+3))/L_(q,K)
       = 2 sqrt(6 pi q)/L_(q,K).                               (3.15)

This proves (2.11).

The application is to the ACTUAL final principal block. Conditioning is only on outside ORIGINAL coordinates inside the partner endpoint, so outside quadratic dependence is never replaced by an independent convolution.

## 4. Dimension-free corollaries

Put

    g := kappa-delta > 0,
    d := r+K.                                                   (4.1)

Then q=d+2+s with integer s>=1, and (2.10) becomes

    L_(q,K) = g - tau_K (1 + (d+2)/s).                         (4.2)

Therefore any strict mean-tail gap

    tau_K < g                                                  (4.3)

can be converted into a bounded-size physical core provided m is large enough relative only to d and the ratio tau_K/g.

More explicitly, if 0<=theta<1 and

    tau_K <= theta g,                                          (4.4)

choose

    s >= max{1, ceil(2 theta(d+2)/(1-theta))},
    q=d+2+s <= m.                                              (4.5)

Then

    L_(q,K) >= (1-theta)g/2,                                  (4.6)

and

    boxed:
    ||p_Q||_infinity
       <= 4 sqrt(6 pi q) / [(1-theta)g].                       (4.7)

Thus fixed defect count d and any fixed mean hostile fraction theta<1 give a dimension-free density bound even when the residual hostile tail has rank comparable to m.

### Concrete inequality

Take r=K=1, m>=10, and suppose

    tau_1 <= g/4.                                              (4.8)

Choose q=10. Then ell=6 and

    L_(10,1) >= g - (10/6)(g/4) = 7g/12.                      (4.9)

Therefore

    boxed:
    ||p_Q||_infinity
       <= (24/7) sqrt(60 pi) / g
       = 47.07212054727954... / g.                             (4.10)

The largest hostile added eigenvalue is entirely free. Moreover the residual hostile spectrum may itself contain very large spikes: only the average (1/m)sum_{j>=2} beta_j is constrained.

## 5. Why this is a genuine additional-eigenvalue theorem

The preceding account04/B12 hostile-count compiler pays the number of hostile modes above a threshold. The present theorem gives a complementary mechanism: it first strips K arbitrary global spikes, then uses ORIGINAL-coordinate subset averaging to turn only the residual Ky Fan tail mean into a local spectral bound. In particular, a residual eigenvalue of size 100g is compatible with tau_K<=g/4 when the core dimension is sufficiently large and the rest of the residual spectrum is small; no global beta_(K+1) bound is needed.

The theorem also handles repeated/dense hostile additions. For example H_K=theta g I has rank m and tau_K=theta g; the conclusion remains dimension-free for every fixed theta<1 once q is chosen as above. Repeated eigenvalues are therefore not a degeneracy in this stability branch.

Favorable-sign added spectrum P is never charged, because it can only increase the relevant signed eigenvalues. Arbitrary additions outside the selected physical core are already absorbed by the completed finite-core/partner endpoint. The theorem is symmetric under sigma=+1 and sigma=-1, so either-sign protected baselines are covered.

## 6. Computation and checks

CHECK.py is a deterministic finite sanity checker for the matrix inequalities only. With seed 20260923 it generated 2500 random instances with 5<=m<=12, random defect counts r, spike counts K, admissible q, random baseline eigenframes, and arbitrary symmetric added compressions. It verified:

1. the selected q-subset obeys tr H_K[J,J] <= q tau_K;
2. the baseline compression has at least q-r eigenvalues >=kappa;
3. the actual local hostile eigenvalue eta_(q-r-2) is at most q tau_K/(q-r-K-2).

All 2500 tests passed. The maximum observed eta/bound ratio was 1.00000000000001 (floating-point tolerance). These tests are not evidence for the full conjecture and are not used in the proof.

## 7. Remaining gap and continuity

FULL QFORM remains OPEN / NOT PROVED / NOT DISPROVED.

This theorem is conditional on a protected original-coordinate baseline core I and a decomposition whose residual hostile Ky Fan mean tau_K is below the surviving signed gap. The bare global assumption s_3(A)>=1 has not been shown to force such a core/decomposition with bounded d=r+K and tau_K<kappa-delta.

The complementary unresolved regime is therefore one in which every candidate one-sided protected core has either many baseline/spike defects or residual hostile mean comparable to its signed gap. That regime should be attacked by the existing cross-energy, volume, ridge, grouped-bank, or hub mechanisms rather than by treating the remainder as independent noise.

The present branch proves an essentially bounded density through the partner endpoint. It does NOT establish a continuous density. Continuity remains separate for this branch and for the unrestricted target.

## 8. Correction compliance

No post-rotation independence is used. No pointwise oscillatory-decay claim is used. No arbitrary-joint coarea lemma is used. No naive fiber supremum is integrated. No small matrix norm is interpreted as a small random quadratic error. No universal single good minor is assumed. The physical subset is produced by an exact trace-averaging identity, and the final density theorem is invoked only after verifying its spectral hypotheses on that actual original-coordinate subset.
