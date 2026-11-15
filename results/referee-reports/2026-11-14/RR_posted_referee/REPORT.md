VERDICT: ACCEPT WITH MINOR CORRECTIONS (made and pushed, cd5fd38)

Independent post-posting referee pass on "The logarithmic factor in the tuned constant-step rate of random reshuffling",
https://github.com/yspennstate/rr-constant-step-log-factor (paper/rr_log_factor.tex at 6085335, 335 lines, read in full
14 Nov 2026 06:0x-06:5x laptop time). Referee: an agent (Claude Opus 5.5), a session that did not write the paper.
Lane: T-20261112-017 independent referee passes on posted papers.

Checked by hand, all correct:
- The instance: mu = L n1/n, x* = 0, G = s, sigma*^2 = s^2 n1/n2; the n1 = 1 restatement ((n-1)/n^2 >= 1/(2n)).
- (2.1)-(2.2): X_{k+1} = A X_k + B_k with A = r^{n1}, the mean and variance recursions.
- Lemma 2.1: E B = gamma s/(n1+1) sum (r^q - r^{n1}) (stiff q uniform on 0..n1-1, flat q uniform on 0..n1), the
  pair count giving (1-r) sum (k+1) r^k, the Chebyshev-sum bound phi <= 1, phi >= 2/(n1+1), phi >= r^{n1-1}.
- Lemma 2.2: sum c_t = 0, 0 <= e_q <= (q gamma L)^2/2 with q <= n1, sum |c_t| = 2 gamma s n1, the stiff part of E_1
  constant, the flat part the Mann-Whitney U with Var = n1 n2 (n+1)/12, sd(E1+E2) <= sd(E1) + sup|E2|.
- Theorem 1.1(a): both cases (gamma L n1 <= 1/2 with the split at u = (Lambda - ln Lambda)/2, using ln(1-x) >= -2x and
  3 - ln 3 > 2 ln 2; gamma L n1 > 1/2 using K >= 2 and m >= gamma s/(n1+1)), and the condition K >= n1(Lambda-ln Lambda)/2.
- Proposition 3.1 (random-sign start). Theorem 1.1(b): gamma L n1 = Lambda/K <= 1/2, A^K <= e^{-Lambda}, 1 - A^2 >=
  gamma L n1, (n+1)/n2 <= 3, L n1^2 = mu n n1. The final Theta statement: bracket <= (5 Lambda/6)^2 + 9/4 Lambda^2 <=
  4 Lambda^2, Lambda - ln Lambda >= Lambda/2, constants 1/2048 and 2.

Independent numerics (rr_exact.py, written from the paper's statements; a backward DP over (stiff seen, flat seen) on
B = sum c_t (r^q - 1), closed forms for E X_K and Var X_K, not the paper's recursion):
- DP equals brute-force enumeration of all arrangements (5 cases, 1e-15 relative); Monte Carlo of RR itself (4e5 runs)
  agrees within sampling error.
- phi bounds: no violation over n1 <= 200 and 400 values of r. Stationary mean = (gamma s/2) phi(r) to 2.7e-13.
- Lemma 2.2: no violation over 8 (n, n1) and 60 steps each; Var B / first-order term = 0.9098 .. 1.0000 for gamma L n1 <= 0.1
  (paper: 0.91 to 1.00).
- Rate from x0 = D (continuous minimisation): min/unit 1.5402, 1.4003, 1.4176, 1.3177, 1.2998 on the posted instances
  (paper 1.54, 1.40, 1.42, 1.32, 1.30; (1000,100,1e4) 1.289 from the paper's script), argmin gamma mu T/Lambda 1.05..1.10,
  error at the tuned step below bound (b) in every case, min/lower(a) 128.7..190.0.
- code/rr_check.py rerun: output byte-identical to code/check_output.txt (14 min).

Corrections made (cd5fd38, author the author):
1. Section 5 said the rate was checked for (n,n1) in {(40,1),(100,10),(100,50),(1000,100)} and K in {10^3,10^4}, i.e.
   eight instances, and then reported "all six cases". The script runs six: (100,50,10^3) and (1000,100,10^3) are not
   among them, and on (100,50,10^3) the minimum is 1.545 units, outside the stated 1.29..1.54. The sentence now names the
   six instances.
2. "From x0 = -D the minimum is 2e-4 to 0.018 times the same unit" was the minimum over the script's grid; the error has a
   sharp dip where E X_K = 0. Locating that root (closed form via phi, brentq) and minimising next to it gives
   1.0e-4, 7.3e-4, 1.06e-2, 1.37e-3, 1.44e-2, 1.69e-2 on the six instances, at gamma mu T/Lambda = 0.84..0.87. The text
   now says 1.0e-4 to 0.017 and where the minimum sits; code/minus_start.py and its output were added (README lists them).
3. Two related papers were not cited: J. Li, arXiv:2609.04578 (constant-step last-epoch rate O~(T^-2 + n^2 T^-3) under a
   Lipschitz Hessian, up to logarithms) and Z. Liu and Z. Zhou, arXiv:2505.23056 (nonsmooth shuffling, last iterate).
   Both now cited in the introduction (abstracts read from arxiv.org/abs on 14 Nov). Data-availability line: "scripts".
Recompiled twice: 6 pages, no undefined references. No SHA256SUMS in this repo.

Not changed, noted: the lint's W16 flags the abstract's "known upper/lower bounds" as undefined jargon; the introduction
defines both with citations in its second paragraph, so it stands. The theorem covers gamma <= 1/L only; Remark 4.1 says so.

Not checked: the content of the 2026 arXiv papers cz (2610.19444) and lgh (2610.29166) beyond their titles in search
results; Liu and Zhou's Section 6 wording was not re-read.
