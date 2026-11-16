---
name: probm36_two_site_trap_posted_zenodo_24274954_2026_11_16
description: "[VERIFIED] Aldous Open Problem 2 (coalescing random walks, E T ~ 2 tau): paper posted 16 Nov 2026, repo two-site-trap-coalescence, Zenodo 10.5281/zenodo.24274954. A two-site trap graph where pair meeting means concentrate, tau ~ m, yet T/(2mr) tends to Exp(1); with r = log m, E T / (2 tau) grows like log m."
metadata:
  type: project
  created: 2026-11-16
  status: verified
---

Aldous (Bernoulli 19, 2013; arXiv:1309.6766, Open Problem 2) asked what conditions, beyond concentration of the mean
meeting times of pairs started from independent uniform points, give a mean coalescence time asymptotic to twice the
stationary mean meeting time tau. Paper: https://github.com/yspennstate/two-site-trap-coalescence, archived at
doi:10.5281/zenodo.24274954.

Result. Take a weighted complete graph on m vertices joined to a two-vertex trap with scale r.
- The pair means concentrate exactly when r = o(m), and in every fixed L^p exactly when r = m^{o(1)}; then tau ~ m.
- The coalescence time T satisfies T/(2mr) -> Exp(1) in Wasserstein distance, with all moments.
- With r = log m, E T / (2 tau) grows like log m. So pair-mean concentration alone does not give E T ~ 2 tau.
- Both stages of the plan Aldous proposed hold (Proposition 5.1); the hand-off between them fails (Remark 5.2), because
  once few walkers remain, one of them sits in the trap. The worst-start mixing time is at least of order mr.

How the proof goes. First-step analysis on three pair types gives every pair mean and tau in closed form (Lemma 2.1). A
death-rate bound a s(s-1)/6 (Lemma 3.1) and a comparison with a pure death chain give matching bounds on E T, and a
first-exit coupling gives the Wasserstein bound (Theorem 3.2). The asymptotics in r follow from the closed forms.

What existed before. The question and the two-stage plan are Aldous's. On the complete graph E T ~ 2 tau with
Kingman's total time as the limit law (Aldous and Fill, Chapter 14); the torus case is Cox (Ann. Probab. 17, 1989).
Oliveira (Trans. Amer. Math. Soc. 364, 2012; Ann. Probab. 41, 2013) bounded coalescence by the maximal hitting time and
gave the mean-field Wasserstein formulation followed here. Hermon (arXiv:1908.08525) showed that for transitive chains
relaxation time o(meeting time) suffices; Kanade, Mallmann-Trenn and Sauerwald (SODA 2019) and Hermon, Li, Yao and
Zhang (Ann. Probab. 50, 2022) treat the worst-pair normalisation and the early phase. New are the trap graph, its
closed forms, the bounds of Theorem 3.2 and the failure of the hand-off.

Checks. checks/check_exact.py verifies the identities symbolically and, for small m and rational epsilon, solves the
meeting-time equations on all ordered pairs and the coalescing chain on all occupied subsets in exact rational
arithmetic, comparing them with the closed forms. A first-reader audit (minor edit, six must-fix items) was applied
before posting. Two writing checks worth repeating: define a constant in the sentence before a display rather than
inside it, and never let one letter name two objects in the same paper.
