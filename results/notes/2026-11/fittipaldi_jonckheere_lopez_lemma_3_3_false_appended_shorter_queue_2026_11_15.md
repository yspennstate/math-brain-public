---
name: fittipaldi_jonckheere_lopez_lemma_3_3_false_appended_shorter_queue_2026_11_15
description: "Power-of-D load balancing, tagged-queue arrival rate (Fittipaldi, Jonckheere and Lopez, arXiv:1809.05373, Lemma 3.3): the claim that lambda^N(x,k) is eventually non-decreasing in N fails as stated. By the paper's own equation (3.4), appending a server shorter than k multiplies the rate by (N-D+1)/N."
metadata:
  type: project
  created: 2026-11-15
  status: provisional
---

The paper is E. Fittipaldi, M. Jonckheere and F. J. Lopez, on the tagged queue in the power-of-D (join the shortest
of D sampled queues) system, arXiv:1809.05373 (v1). For a configuration x = (x_1, x_2, ...) with x_1 = k, lambda^N(x,k)
is the arrival rate to server 1 when only the first N servers exist (their (3.1); Lemma 3.1 gives
lambda^N(x,k) = lambda N ((N-D)!/N!) S^D(pi_{k+1}^N(x), pi_k^N(x))). Lemma 3.3 states that there is an N_0, not depending
on x or k, after which N -> lambda^N(x,k) is non-decreasing. It supports the almost-sure half of their Theorem 3.2.

The counterexample comes from the paper's coupling. Equation (3.4) writes lambda^{N+1}(x,k) as three terms; the second
needs x_{N+1} > k and the third x_{N+1} = k, and the text after (3.4) notes that x_{N+1} < k contributes nothing,
since a red arrival would then go to server N+1. So when x_{N+1} < k only the first term is left:

    lambda^{N+1}(x,k) = (lambda N - (D-1) lambda) ((N-D)!/N!) S^D(pi_{k+1}^N, pi_k^N) = ((N-D+1)/N) lambda^N(x,k),

a strict decrease for D >= 2 whenever lambda^N(x,k) > 0. Take x periodic, (1, 2, 0) repeated, and k = 1: the running
assumption pi_k^N - pi_{k+1}^N >= D and pi_k^N >= D holds for all large N, lambda^N(x,1) > 0, and x_{N+1} = 0 < 1 for
infinitely many N. The sequence decreases infinitely often, so no N_0 exists.

What survives: the rates in the example still converge, and the factor (N-D+1)/N tends to 1, so the convergence the
lemma was meant to support may hold by another argument (for instance a bound on the total variation of the sequence
rather than monotonicity). The appendix proof by direct computation omits the case x_{N+1} < k.

How it was found: an open-problem worker read the coupling and proposed the shorter-queue case; equation (3.4) and the
example were then checked line by line against the arXiv PDF. The authors have not been contacted. What would change
this: a later version of the paper that restricts the lemma, or a reading of (3.4) under which the x_{N+1} < k case
keeps a red-process term.
