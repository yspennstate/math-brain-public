# Referee report, 2026-10-11

Verdict on the full problem: unresolved. Verdict on the recorded lower
obstruction: the complete proof in ATTEMPT.md checks against the cited
all-moments inputs. No novelty claim is made.

The principal logical risks have been examined:

- The law must be fixed, not triangular. Here R_j is selected once,
  all Y_j are defined once, and the final normalization s is fixed.
- A stage's all-moments theorem must not be applied uniformly over a
  changing law. Its threshold N_j is obtained after fixing S_j and
  before choosing R_j. Later variance normalization is a scalar dilation,
  and both metrics admit the required scaling relation.
- No conditioning argument changes the finite-past law. Good-event
  probabilities are unconditional and combined by a union bound with
  the exact-equality event; no independence between these events is needed.
- Tail probabilities control all n_j^2 entries. The sum of future q_k
  is <=2q_j, enforced recursively. This gives summable failure bounds.
- L^p convergence uses sum ||Y_j||_p=sum 2^-j, not sum E|Y_j|^p
  alone. Independence then identifies the limiting variance in L^2.
- The radius deficit is t_j/[s(1+r_j)], with s<2 and r_j<=1.
  The test rectangle remains FIXED, independent of j and the sample.
- For r>=1/sqrt(2), the integration endpoint 1/(2r)<=sqrt(2)/2<3/4.
  The chord density is uniformly >1/4 throughout that interval.
- The radius test is bounded 1-Lipschitz, so no uncontrolled outlier
  contribution occurs. The ball bound uses layer cake with bounded radii.
- The final exponent statement is simultaneous in all delta>alpha:
  on the one eventual good-event intersection, delta>=alpha+1/j holds
  for all sufficiently large j, for each real delta>alpha.
- Borel–Cantelli uses only summability; the cross-size coupling is arbitrary.
- An expectation bound for the nonnegative random distance is valid;
  a signed bias estimate for the mean ESD is not inferred.
- eps=2/3 and larger are outside the construction. The compatible
  exponent window closes exactly at eps=2/3.

The formal certificate concerns five algebraic inequalities only.
The stochastic construction, integration, and use of the published
theorems remain conventional written mathematics. Numerical checks are
auxiliary sanity checks, not proof of an asymptotic rate.

The earlier brain assertion that scalar variance truncation “caps delta”
was not used. Its direction of implication is insufficient. A matching
upper bound, or a stronger lower obstruction that changes the candidate
exponent, is still required to solve C0109.
