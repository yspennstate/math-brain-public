---
name: fei_p9_forced_coordinate_posted_2026_11_11
description: "[VERIFIED] FEI P9 posted? Yes, github.com/yspennstate/fei-forced-coordinate 3e9219a (11 Nov): F_{k,1} (OR2/AND2 forced coordinate of P8) has E_x/Inf_x = (1+o(1))(k-1)log2(4/3), maximal; refereed by agent (proof stands); table fixed for a log cancellation at k >= 121"
metadata:
  node_type: memory
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T07:10:40+02:00
  status: verified
  evidence: github.com/yspennstate/fei-forced-coordinate 3e9219a; fei-hidden-coordinates 391bb88; referee notes the private repository, 06_math_research/lean_checks_agent/p9_referee @ 18d60c0c
  modified: 2026-11-11T05:32:11.899Z
---

P9 is public at github.com/yspennstate/fei-forced-coordinate (c00e663, 11 Nov 07:0x): "A forced coordinate with nearly maximal erasure entropy", 7 pp. Brain copy 06_math_research/fei_papers_agent/p9 and repo_p9.

Theorem: F_k = F_{k,1} of P8 Prop 12 (tilde f_k with y_j, j <= m, replaced by OR2 and y_j, j > m, by AND2; 2k+1 variables; x the only variable in both a shortest minterm and a shortest maxterm) has Inf_x = (3/4)^{k-1} and E_x/Inf_x = (1+o(1)) log2(1/Inf_x) = (1+o(1))(k-1) log2(4/3), the largest possible value (E_x <= h2(Inf_x) always). This answers P8's open question for t = 1; fixed t >= 2 stays open, and P8's remark now says so and cites P9 (public 45db393).

Proof shape: the ratio is a mean of Psi(r_uv) over u, v ~ Bin(m, 1/4) (Lemma 3); the majority tail t_uv is the z^m coefficient of Q = H/(z-1), an exact circle integral (Lemma 4); on |z| = 1, |X| = |Y| so |Q|^2 = (2-2w)^{n1}((5+3w)/8)^{n2}, strictly concave in w = cos theta, peak at w0 = (3n2-5n1)/(6m); Lemma 5 is exact by convexity (the exponent is at least (m-1) ln 4/3 on every class); Laplace at the real maximiser with the linear phase inside the Gaussian, error O(|T| m^{-1/5}) (Lemma 6); the phase moves by arccos(1/3) per step in u since g(z*) = (z*-1)/X(z*) = (4/3) z* (Lemma 7), irrational by Niven, so Weyl in blocks of L leaves |cos| >= eps on all but 6 eps of the weight.

Checks: exact ratios to k = 141, increasing (quotient to (k-1)log2(4/3): 0.80 at k = 21, 0.88 at 81, 0.909/0.915/0.918 at 121/133/141); full truth tables k = 3..9 agree to 1e-9; Laplace vs exact over the sqrt(m) window 0.149/0.095/0.071 of |T| at k = 41/81/141. Refereed 11 Nov 07:21 by an agent (Lemmas 2-7 and Sec 4 by hand, own WHT and double sum): theorem and proof stand.

Scar, numerics: the first posted table (c00e663) was wrong for k >= ~121 (52.59 at 133, 52.34 at 141, non-monotone). forced_exact.py took log2(tot/a2) as log2(numerator) - log2(denominator) of a Fraction equal to 1 + 1e-17; the two big logs cancel and the error is multiplied by a weight of the same size. Fix: log2(1 + d2/a2) with log1p (log2_1p in forced_exact.py). Corrected 121 45.276, 133 50.139, 141 53.319, matching the referee's exact sum. Lesson: a table that is supposed to grow and goes down is a bug report; and never take log of a ratio near 1 as a difference of logs.

Citations (the author's 07:06 order): bib widened to 20 entries (OWZ, OT13, CKLS, WWW, KKLMS, Han, Hod, KMS12 biased FEI, VW08 erasure entropy, OD14 ch. 8, FS09 ch. VIII, Weyl16, Niven, Shm1/3/8), each checked against its record; P8 gained KMS12 and VW08 (391bb88).

Scar from the repost: P8's post script uploads whole files from the brain copy, and 04ca5f6 silently reverted a margin fix someone else had pushed at 06:58 (192c8a7). Restored in 45db393. Before reposting a public repo, compare its head with the sha you last posted, and merge whatever came in between.

Related: [[fei_p8_hidden_coordinates_posted_2026_11_11]], [[fei_p7_linear_dnf_census_posted_2026_11_11]].

