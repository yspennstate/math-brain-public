VERDICT: PROVED exact cubic contrast eigengap and O(K^2 d log K) subspace recovery for odd-width orthonormal hard committees

For odd K>=3 and orthonormal teacher directions w_1,...,w_K in R^d,
consider Y=sign(sum_i sign(<w_i,X>)), with X standard Gaussian.
Let u=sum_i w_i/sqrt(K), P_0=I-uu^T, and let P_V project onto
the K-1 dimensional teacher subspace perpendicular to u. PROOF.md proves
the exact identity

    E[Y<u,X>((P_0X)(P_0X)^T-P_0)] = -rho_K P_V,
    rho_K = sqrt(2/pi)(1-2/pi)
            binom(K-1,(K-1)/2)/(2^(K-1) sqrt(K)),
    K rho_K -> (2/pi)(1-2/pi) = 0.231335037798230...

The proof computes every component of the third Gaussian Hermite tensor.
A separate raw-moment calculation recovers the eigenvalue. All one-sample
population moments of feature degree at most two, even allowing arbitrary
functions of the binary label, depend only on K and u. The displayed cubic
moment exposes the contrast subspace.

An explicit clipped spectral estimator recovers V with O(K^2 d log K)
samples at fixed accuracy and confidence. Section 7 removes the need to
know u: it estimates u from the label-weighted mean on an independent
batch and proves a dimension-free perturbation bound. Equations (10)–(12)
give finite-sample constants, failure probability, and operator/Frobenius
overlap guarantees. This is a polynomial-time upper bound for recovering
a subspace; it does not recover individual hidden units.

Reproduction command, from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > audit_output.txt 2>&1
```

The final run exited 0. It exhaustively enumerated all sign patterns for
K=3,5,...,17, checking exact rational majority coefficients and the
contrast eigenvalue by conditional integration over Gaussian magnitudes.
The largest numerical discrepancy between the two eigenvalue calculations
was 1.39e-17. A central-binomial recurrence, independently compared with
lgamma, gives K rho_K=0.231335616131 at K=100001, a ratio
1.000002499978 to the limit. The script also checks Gaussian moments,
the exact scalar second moment 2, clipping inequalities, and the numerical
constants in the concentration and sample-splitting bounds. The probability
and perturbation arguments are analytic proofs, not conclusions from these
finite checks.

Data: `exact_checks.csv`, `asymptotic_checks.csv`.
Full output: `audit_output.txt`. The script uses the standard library,
one thread, and CPU/wall-time limits of 60/120 seconds. Both runs completed
in under one second. It verified inherited niceness 20; peak RSS was under
16 MB. The sandbox prints a warning when the requested relative `nice -n 15`
tries to increase that already-low priority further.

Adversarial checks:

- K=3 is included in both the proof and exhaustive checks; K-2 is nonzero.
  Even K and its tie convention are excluded. K=1 has no contrast subspace
  and is excluded.
- The negative sign requires the smallest eigenvalues. Selecting the largest
  eigenvalues would recover the wrong space.
- At d=K, the known-u contrast space is already u^perp. The theorem remains
  valid; the unknown-u corollary still has a defined target.
- Conditioning on an estimated direction is legitimate only for the independent
  second batch. The estimator explicitly splits samples.
- A direction error comparable to 1/K can affect the signal. The sample-split
  corollary controls it explicitly; merely invoking consistency at fixed K
  would not suffice.
- The variance identity and absence of a degree-two population signal give
  no lower bound for general low-degree algorithms on the whole dataset.

What failed or remains uncertain: the literature search found no settlement
of the full question. SOLVED_ELSEWHERE.md records relevant 2025–2026 advances
and their scope. The prior local 3.27 K^2 AMP constant uses a formal expansion
and is not used here. No proof of either original threshold, the conjectured
algorithmic lower bound, or individual-unit specialization was obtained.
No novelty claim relative to all multi-index literature is made for the
special-case estimator. The proof requires exact orthonormal teachers; it
does not automatically transfer to the original independent Gaussian weights
when K grows with d. The logarithm and explicit constants are not optimized;
the first-batch confidence dependence uses Markov's inequality.

Next worker: quantify perturbations in the teacher Gram matrix and thereby
transfer this moment/estimator to independent Gaussian teachers in a stated
joint K,d regime. Separately, exploit the explicit cubic tensor to formulate
a growing-K low-degree calculation, distinguishing contrast-subspace recovery
from permutation-matched recovery of individual neurons. The upper bound here
cannot serve as that lower-bound argument.

Task: “push this problem forward by one checkable piece.” Received
14 November 2026, approximately 21:28 Asia/Tbilisi.
