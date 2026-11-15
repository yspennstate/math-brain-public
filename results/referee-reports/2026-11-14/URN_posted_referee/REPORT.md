VERDICT: ACCEPT WITH ONE MINOR CORRECTION (made and pushed, cffb6eb)

Independent post-posting referee pass on "On a contractivity question of Neri and Pinto for generalized Polya urns",
https://github.com/yspennstate/urn-euclidean-contractivity (paper/main.tex at 9bb5f73, 360 lines, read in full
14 Nov 2026 05:4x laptop time). Referee: an agent (Claude Opus 5.5), in a session that did not write the paper
(written 20 Oct 2026 by another Claude Opus 5.5 session). Lane: T-20261112-017 independent referee passes on posted papers.

Checked by hand:
- Lemma 2.1: (i) Q(1) = sum_{ij} R_ij - d lambda = 0; (iii) w J_{d-1}(R^T - lambda I) w^T = sum_{i<=d-2} w_i((wR)_i - lambda w_i),
  and v -> vC_{d-1} is an isometry from R^{d-1} onto (H, ||.||_{d-1}); (iv) the relabelling identity (w^s R^s)_j = (wR)_{s(j)}.
- Theorem 1.1: Q(t,-t) = -2t^2(r+s), Q_(1) = -(r+s)t^2; second eigenvalue lambda - r - s from the trace.
- Lemma 3.1: the four columns (wR)_0 = 5a+5b, (wR)_1 = a + eps c, (wR)_{d-2} = e + eps b, (wR)_{d-1} = 5c+5e, the source of
  the eps terms for d = 4 (R_12 and R_{2,1}), f(a,b) = -a^2 + 6ab - 6b^2; every entry of the table in Proposition 3.2 for
  d = 4 and d >= 5; the remark Q = 6b^2 at a = 3b, e = 3c, c = -b; Lambda_H(R^(4)) = 3 sqrt 2 - 4 = 0.24264.
- Example 4.1: wR = (-69, 296, -227), Q = 11, Q_(1) = 23.
- Example 4.2: w(R - 6I) = (2,6,4,-4,-2,-6), Q = 4; the shift x = y + 3 gives y^3 + 4y^2 + 2y + 3 and Routh-Hurwitz (8 > 3).
- Theorem 1.3: L maps H to H with spectrum mu - lambda; the Perron-Frobenius step for gamma < lambda; the Lyapunov
  construction, (vKC)E = vK and w P w^T = v G v^T, giving <L(w) + Aw, w>_P = -|v|^2/2; the optimality step,
  Re(L(z) P conj(z)^T) = <L(x),x>_P + <L(y),y>_P. Corollary 1.4 follows. All correct.

Independent numerics (urn_check.py, numpy/scipy, written from the paper's statements, not from code/checks.py):
- Every entry of the Section 6 table for 4 <= d <= 10 (Lambda_d, Lambda_H, min_k, max_k) agrees to all five printed digits;
  Example 4.1 readings 6.73803, 1.15630, (14.70006, 5.96644, 1.10783); every vector and value of Example 4.2; its
  characteristic polynomial; gamma = 5.7417, 5.8541, 5.9381, 98.7402, 2.8390.
- The Lyapunov P built with A = 0.999(lambda - gamma) for R^(4), R^(5), R^(8), Example 4.1 and Example 4.2 satisfies (1.4)
  on 20,000 random w in H each (largest value of <L(w) + Aw, w>_P between -1.6e-4 and -1.1e-1).
- code/checks.py rerun: exit 0, ALL PASS, output byte-identical to the posted code/checks_output.txt.

Correction made: the sentence after Corollary 1.4 said the urns of Theorem 1.2 "for d >= 3 have gamma/lambda between 0.95
and 0.99". Theorem 1.2 uses R^(d) for every d >= 4, and gamma/lambda for R^(d) is 0.9914 at d = 9 and rises with d
(0.9926, 0.9972, 0.9989, 0.9994 at d = 10, 20, 40, 60; gamma_tail.out). The sentence now refers to the urns whose gamma is
computed in Section 6 (R^(4), R^(5), R^(8), Example 4.1), for which the range is correct. Recompiled (8 pages, no errors or
undefined references), SHA256SUMS rebuilt from the staged blobs, checked from a clean core.autocrlf=false clone with
sha256sum -c (6 OK). Nothing else in the paper changed.

Not checked: the hypotheses of Neri and Pinto's Theorems 3.2 and 3.3 beyond inequality (1.1) as the paper quotes them
(arXiv 2607.07309 not read here), and the Lean file (no Lean toolchain run). Literature after July 2026 on the question
was not searched in this pass.

The paper-lint finding W19 (introduction does not set the result against earlier work) does not apply: the introduction
states the question of [NP, Remark 3.7], what [NP] proves, and how each reading fails; the flagged "own earlier work" is
the code repository citation.
