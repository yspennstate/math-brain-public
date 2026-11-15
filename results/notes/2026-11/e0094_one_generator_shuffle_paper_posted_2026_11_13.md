---
name: e0094_one_generator_shuffle_paper_posted_2026_11_13
description: "[VERIFIED] E0094 Diaconis 2013 Q3 (add one permutation to (1,2) and the n-cycle, odd n): paper posted, doubling map gives O(n log^3 n), any added pi needs (2-o(1))log(n!)/log4; github one-generator-shuffle c0c2213, Zenodo 24200518"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T16:55:35+02:00
  status: provisional
  evidence: ""
---

Diaconis, Bernoulli 19 (2013), Question 3: for odd n and S={(1,2),(1..n)} (base walk Theta(n^3 log n): DSC 1993 Thm 2 upper, Wilson ECP 2003 Thm 1 lower - his 'symmetrized Rudvalis shuffle' is exactly these moves), which added element speeds mixing most. Result (Codex proofs, two audits MINOR): sigma(x)=2x mod n, sigma c sigma^-1 = c^2, every transposition a word of length <= 12h-9 (h=ceil log2 n), comparison constant 720h^2 with random transpositions, full-spectrum chi^2 bound -> t_mix(eps) <= ceil(720h^2(n-1)[2 log n + log(1+1/(4eps^2))]). Lower bound for any added pi: ball (5*4^r-2)/3, t_mix >= (2-o(1)) log(n!)/log 4. Main predecessor: DSC 1993 Thm 7 (different generators, x->2x, x->2x+1 on Z_{n-1}+inf, plus (0,inf)) already O(n log^3 n); our contribution is the prescribed-pair construction. Small n exact: base vs sigma t(1/4) 29/13, 103/42, 254/74 for n=5,7,9; n=5 exhaustive best is 9 (14 perms, e.g. (1,2,4,0,3)), so doubling is not optimal. Open: log^2 gap, optimal pi. Paper: github.com/yspennstate/one-generator-shuffle commit c0c22135, Zenodo 10.5281/zenodo.24200518 (md5 cf8f7115). RG folder Downloads/career/researchgate_queue/q4/one-generator-shuffle (queued). Referee reports: 06_math_research/referee_reports/2026-11-13/E0094A, E0094AR. Related: [[f0083_stable_allocation_uniqueness_paper_posted_2026_11_13]].

Update 2026-11-14 03:10 (an agent): independent post-posting referee ACCEPT, no correction. Every lemma and constant checked by hand (12h-9 words, A = 720 h^2, eigenvalue and multiplicity bounds, ball count (5*4^r-2)/3); a script written from the text alone reproduced the n = 5, 7, 9 table exactly, the 14 best added permutations for n = 5 with time 9, and the word bounds for all odd n <= 301 (longest 87 at n = 301, bound 99). referee_reports/2026-11-14/E0094_posted_referee (da2d35ff).
