---
name: p0242_lumping_af445_resolved_hermon_peres_our_note_on_n_2026_11_12
description: "Aldous-Fill Open Problem 4.45 (lumping and tau_1^(2)) open? No: Hermon-Peres 2018 answered it (log|V| on bounded degree). Our posted note: (n-2)/2 <= K(n) <= n-1 in the number of states; repo lumping-mixing-time"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T01:13:04+02:00
  status: verified
  evidence: "git ls-remote of lumping-mixing-time main = e9c2c6353e36; ledger commit affd7c1a164f read back from GitHub with blob ok; Codex referee REPORT.md verdict SOUND (brain repo 06_math_research/p0242_lumping_2026_11_12/referee); Hermon-Peres DOI 10.1214/18-EJP154 checked on Crossref and the arXiv text read"
---

P0242 (Aldous-Fill Open Problem 4.45: is tau_1^(2) of a lumped reversible chain at most an absolute constant times
tau_1^(2) of the original?) is RESOLVED IN THE LITERATURE, negative: J. Hermon and Y. Peres, "On sensitivity of
mixing times and cutoff", Electron. J. Probab. 23 (2018), paper no. 25, DOI 10.1214/18-EJP154, arXiv:1610.04357
(Problem 1.6, Theorem 3(c), Remark 1.8). On bounded-degree graphs the factor is of order log|V| at most, and that
order occurs. Our ledger rows of 13 Sep and 10 Oct ("K = 1 fails, sharp constant open") were written without
that paper.

What we posted (12 Nov 2026): "Lumping and the mixing time of a reversible chain: the dependence on the number of
states", https://github.com/yspennstate/lumping-mixing-time (main e9c2c6353e36). With K(n) the supremum of the ratio
over reversible chains with at most n states: max(1, floor((n-2)/2)) <= K(n) <= n-1.
- Upper bound: tau_1^(2)(hat X) <= tau_0(hat X) <= tau_0(X) <= (n-1) tau_2(X) <= (n-1) tau_1^(2)(X).
- The last step is tau_2 <= tau_1^(2) with constant one (Aldous-Fill Open Problem 4.48(b)); the brain already had
  it as part (b) of P0243 (card claim_58a424cb31744ae4b4b1134d0b319492). The paper is where that proof is public.
- Lower bound: a weighted comb with 2N+2 states (teeth with heavy loops, a heavy end); lumping each tooth with its
  spine vertex multiplies tau_1^(2) by a factor tending to N. Exact at t = 256: N = 8 gives 7.7304.
- Hitting times of sets: max_b hat E_b T_{hat A} <= (n - |A|) max_y E_y T_A.
Open: the order of K(n) between (n-2)/2 and n-1.

Checks: exact rational program in the repo; Codex referee on Mac mini 1, verdict SOUND, with its own programs
(3,840 comb parameter sets, 600 networks, 21,000 chains); nine wording points applied. Records: ledger master
affd7c1a164f; math-brain-public main a9d616ac0804; brain repo 06_math_research/p0242_lumping_2026_11_12 (NOTES.md,
referee/REPORT.md, referee/LOG.md). Not yet on Zenodo or ResearchGate at the time of writing.

**Why:** a ledger row said "sharp constant open" for a problem a 2018 paper had answered; the forward-citation and
problem-number search found it only when the paper was being written.
**How to apply:** before working an Aldous-Fill open problem (or any problem from a 2002-2014 list), search the
problem number together with "Aldous Fill open problem" and read Hermon's and Peres's papers on sensitivity of
mixing times first; then ask what the answer leaves open (here: the dependence on the number of states).
Related: [[p0143_longest_minimum_weight_path_paper_posted_2026_11_11]],
[[conjecture_credited_to_the_preprint_that_quoted_it_and_already_proved_2026_11_11]].

