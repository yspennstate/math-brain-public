---
name: p0177_mode_location_revised_existing_repo_check_github_first_2026_11_12
description: "Mode of classical and free Brownian motion at large time (Hasebe-Ueda Problem 4.6): where is the paper and what does it prove? brownian-mode-location, revised 12 Nov: finite variance suffices in both cases (t >= 600 v classical, t > 7(7+4 sqrt 2) v free), maximizers m - mu_3/(2t) and m - 3 mu_3/t. Scar: a ledger row with no public_repo is not 'unposted' - search the account's repos before writing a paper."
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T02:09:41+02:00
  status: verified
  evidence: "brownian-mode-location main 185b844a; ledger ff91b693; math-brain-public 6520487c; Codex referee SOUND (brain 06_math_research/p0177_mode_location_2026_11_12, commit 068755e5)"
---

P0177 (Hasebe-Ueda, ALEA 15 (2018) 353-374, Problem 4.6: where is the mode of classical and free Brownian motion
with an initial distribution at large time?).

Where it lives: https://github.com/yspennstate/brownian-mode-location (public since 5 Nov 2026, commit f78b5275;
revised 12 Nov 2026, main 185b844a15e23e16927bd8f26947e045d07cd65d). Ledger master ff91b693, math-brain-public main
6520487c (table row + papers/public/brownian-mode-location).

What the revised paper proves, for a law mu with mean m, variance v, central moments mu_k, beta_3 = E|X-m|^3:
- classical: the density of mu * N(0,t) has a unique global maximizer for t >= 600 v, within sqrt(2) v/sqrt(t) and
  within beta_3/t of m (finite variance only; the 5 Nov version needed the exponential moment condition);
- free: the density of mu boxplus S(0,t) has a unique global maximizer for t > 7(7+4 sqrt 2) v, within
  4(7+4 sqrt 2) v/sqrt(t) and within 26((2+sqrt 2)^3 v^(3/2) + beta_3)/t of m (26 replaces 64);
- third moment: maximizers m - mu_3/(2t) + o(1/t) and m - 3 mu_3/t + o(1/t); seventh moment: second terms
  (mu_5 - 6 v mu_3)/(8 t^2) and (5 mu_5 - 22 v mu_3)/t^2;
- under E exp(eps X^2) = alpha: unique mode within Q/t of m for t >= max{600 L, 36 log(2 alpha)/eps} and also for
  t >= 72 log(2 alpha^2)/eps (L = log(alpha)/eps, Q = 8 alpha (3/(2 e eps))^(3/2)); compact support of diameter D:
  free law unimodal, mode within 136 D^3/t of m for t >= 23 D^2.
The free density can have a second local maximum just above the threshold (0.8 delta_0 + 0.199 delta_1 + 0.001
delta_50), so the free statement is about the global maximizer, not unimodality.

Checks: code/mode_checks.py (SymPy coefficients, mpmath maximizers, threshold scans); Codex referee gpt-6.1-sol on
worker machine 1, own programs, verdict SOUND, seven editorial points applied. The second threshold in Corollary 4(i) was
ported from the 5 Nov version after the referee ran and was checked by hand only. Novelty: arXiv fielded searches
and the four works citing Hasebe-Ueda show nothing on the mode's location; not otherwise verified.

What went wrong on the way: I wrote a whole new manuscript before finding that the problem already had a public
paper. The ledger row had no public_repo field and the math-brain-public table had no row, and I took that as
"not posted". The push to a "new" repo was rejected because the name existed; nothing was overwritten. The fix was
to fold the new results into the existing repo as one more commit (never a second repo, never a force push).
Before writing a paper for a solved problem: list the account's repos and search them by topic words
(gh api "users/yspennstate/repos?per_page=100&page=N" --jq '.[].name + " " + .description', or
gh api repos/yspennstate/<planned-name>), as well as the ledger and the public table. A missing ledger field is
not evidence that nothing was posted.

