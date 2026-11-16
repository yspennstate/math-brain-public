---
name: e0103_inertial_boolean_coverage_posted_zenodo_24271165_2026_11_16
description: "[VERIFIED] Konstantopoulos Open problem 1 (coverage time of the inertial mobile Boolean model): paper posted 16 Nov 2026, repo inertial-boolean-coverage, Zenodo 10.5281/zenodo.24271165. d/a a.s. for d >= 2 with finite mean speed, alpha/a under a tail condition, an exponential limit on the log log scale in d = 1."
metadata:
  type: project
  created: 2026-11-16
  status: verified
---

E0103 is Open problem 1 of T. Konstantopoulos, arXiv:1407.6834: the time for the inertial mobile Boolean model (Poisson
points of intensity lambda, each moving forever at its own random constant velocity V, balls of radius r) to cover a
large set. Paper: https://github.com/yspennstate/inertial-boolean-coverage, archived at doi:10.5281/zenodo.24271165.

Results, with a = lambda omega_{d-1} r^{d-1} E|V|:
- d >= 2 and 0 < E|V| < infinity: C(LK)/log L -> d/a almost surely and in L^1 for K with nonempty interior, and alpha/a
  when K has Minkowski dimension alpha > 1 (Theorem 1.1; second moment method plus a count of points near a line).
- Under the tail condition (log h) E[|V|; |V| > h] -> 0, the limit alpha/a holds for every alpha and every d >= 1
  (Theorem 1.2; slow and fast particles are handled separately).
- In d = 1 a finite-mean speed law with P(V > u) = 1/(u log u (log log u)^2) gives C([0, L])/log log L -> Exp(lambda)
  (Theorem 1.3), so the log L scale of Theorem 1.1 can fail without the tail condition.

What existed before. Konstantopoulos posed the question for the inertial model. The upper bounds use the net argument
of Peres, Sinclair, Sousi and Stauffer for mobile geometric graphs, and the planar coverage law is Liu, Dousse, Nain
and Towsley, arXiv:1101.0376, Theorem 1(2); both are credited in the paper. New are the almost-sure and L^1 limits in
every d >= 2, the fractal-set constant alpha/a, the tail condition under which d = 1 behaves the same way, and the
d = 1 example on the log log scale.

A check worth repeating. The constant c(d) in Peres-Sinclair-Sousi-Stauffer Theorem 1.4 is printed as the reciprocal
of the Wiener sausage capacity constant, so the paper describes it in words instead of quoting the formula. A
first-reader audit (minor edit, eight must-fix items) was applied before posting.
