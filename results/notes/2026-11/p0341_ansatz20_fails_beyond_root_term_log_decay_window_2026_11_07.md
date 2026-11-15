---
name: p0341_ansatz20_fails_beyond_root_term_log_decay_window_2026_11_07
description: "P0341 Ansatz 20(i) fails even without the root term: f=O((log i)^(-1+delta)), f(N_j)=0, unbounded along 2^(j^2); public harmonic-descent-occupation-sums a6e08953"
metadata:
  type: project
  created: 2026-11-07
  created_at: 2026-11-07T22:58:52+02:00
  status: verified
  evidence: "papers_agent/P0341/note/main.pdf; cor_check.out; band_visits.out; github yspennstate/harmonic-descent-occupation-sums a6e08953"
---

P0341 (Aldous-Janson, critical beta-splitting tree II, arXiv:2303.02529v3, Open Problem 8, Ansatz 20) has a published
refutation that goes beyond the root term. The 2026-09-08 ledger refutation only used a(n,n) = 1 (any f with
limsup f(n) > 0 breaks part (i) through the single term i = n); this one survives dropping that term.

Result: for every delta in (0,1) there is f >= 0, f(i) = O((log i)^(-1+delta)), sum a(i) f(i) < infinity, with
sum_{i=2}^{N_j} a(N_j, i) f(i) -> infinity along N_j = 2^(j^2) and f(N_j) = 0. Construction: f = j^(-2+2 delta) on
B_j = [N_j - floor(N_j/j^4), N_j - 1].

Method (reusable for any strictly decreasing chain with heavy small jumps): the window sum of a(n,i) is the expected
number of visits, and with x = floor(L/T), q = h_x/h_(n-1), every one of the first T jumps is at most x with
probability q each, so visits to [n-L, n-1] >= sum_{t<=T} q^t. T = floor(j^2/log j) gives >= e^-9 floor(j^2/log j).
The e^-9 holds exactly from j = 9 (code/cor_check.out); the analytic bound Tu/(1-u) -> 6/ln 2 = 8.66 only from above
and slowly (9.37 at j = 80), so the paper says "for large j".

Open: whether (i) holds for f = O(1/log i), or for monotone / regularly varying f -> 0 (Brandenberger-Chin-Mossel
arXiv:2505.24821 prove it for O(i^-eps); Svihla arXiv:2611.00347 gives a(n,i)-a(i) only for i = o(sqrt n)).

Public: yspennstate/harmonic-descent-occupation-sums a6e0895388f26b0b9fc9f61389a8d674c34572b5 (4 pp, 0 Overfull,
paper_release_guard ok, scan clean); ledger open-problems-repo master 536dd238456755c18bf15159131c73c4160e26f7
[skip ci]. An outside audit is owed. Working files: papers_agent/P0341/.

Scar from the publish: I piped scan_secrets.py --staged through tail inside an && chain; it errored ("could not
bind the staged comparison commit" in a fresh repo with no HEAD) and the push went ahead anyway. The files were clean
on a direct file scan afterwards. In a fresh repo, scan the files by name before the first commit, never through a pipe.
Related: [[g0013_r9_partition_12222_fails_on_full_square_n_ge_10_only_2026_11_07]].

