# Referee report: the waiting time for a bridge pattern in simple random walk

Paper: yspennstate/bridge-pattern-waiting-time at 433f9f9 (paper/main.tex, 10 pages). Referee: an agent,
14 Nov 2026.
Claim: for fixed lambda, the first time T_n at which the last n steps of simple random walk form a bridge from 0 to the
level nearest lambda sqrt(n) of the right parity satisfies E T_n ~ gamma_lambda n, with gamma_lambda = 1 + E F_lambda,
F_lambda the first time the Slepian process B(t+1) - B(t) hits lambda. This answers Pitman and Tang, Open problem 2.3
(arXiv:1411.0041v3; Seminaire de Probabilites XLVII, 2015). The constant is a convergent series of determinant
integrals from Shepp's formulas, with a remainder bound; gamma_0 ~ 1.5439, gamma_1 ~ 2.4135.

## Verdict

SOUND. Two fixes, both in commit f3c8d2a ("Fix arrows and a lemma number"), PDF rebuilt (10 pages, no undefined
references):

1. Three arrows were missing from the PDF. In the source, `\to` at lines 176, 211 and 250 had become a backslash
   followed by a TAB character and the letter o (a script wrote "\t" inside an ordinary Python string). LaTeX printed
   "o" where the arrow should be, in three displayed limits. Restored.
2. `\cite[Lemma~2.3]{PTS}` (two places) cites the Pitman-Tang-Shepp companion paper (arXiv:1411.0040, EJP 20 (2015)
   no. 61), where the lemma in question is numbered 4.3 in both the arXiv v2 and the journal version. Corrected.

No change to any statement or proof.

## Proofs checked

- Tail bound P(T_n > k n) <= C rho^k, uniform in n; uniform integrability of T_n / n. Correct.
- Convergence in law of T_n / n to 1 + F_lambda through the scaling limit of the windowed walk (Donsker in the space of
  window paths, the hitting time a continuous functional off a null set, with the first-slab boundary handled
  separately). Correct.
- The Li martingale identity used for E T_n at fixed n. Correct.
- Column-sum lemma for the matching matrix and the two different averaged limits (first bridge law against uniform).
  Correct; the uniform average indeed gives a different constant, as stated.
- Gaussian bound and local limit theorem used in the slab estimates. Correct.
- Slepian lemma and the Karlin-McGregor series for the slab probabilities; r_h and the remainder R_h(M). Correct.
- First-slab closed form 3/4 - 1/pi and the pi/2 value in the bridge case. Re-derived; correct.
- The remark that Pitman and Tang's (2.3) states the reciprocals of the quantities used here, with the counterexample.
  Checked against arXiv:1411.0041v3; correct.

## Citations checked against the sources

- Pitman-Tang arXiv:1411.0041v3: Theorem 1.8(3), Theorem 2.1 with (2.3) and (2.4), Open problem 2.3 and the note after
  it on an argument through the matching matrix alone, Proposition 2.4, Lemma 2.5, and E F <= 3 (so gamma_0 <= 4).
  All as cited.
- Pitman-Tang-Shepp arXiv:1411.0040v2: Lemma 4.3 (fixed above).
- Not checked: the equation numbers (2.15)-(2.16) and (2.25)-(2.26) in Shepp (1971), Ann. Math. Statist., and the
  numbering of the open problem in the published Seminaire version (both behind publisher pages).
- Forward search (14 Nov, two wordings): no later paper giving the asymptotics of E T_n for bridge patterns turned up;
  the problem is still listed as open where the Pitman-Tang paper is indexed.

## Numbers checked independently

- Table 1 (exact E T_n): recomputed by first-step analysis on the last n - 1 letters, a route that does not use the
  matching matrix (exact rationals for n <= 6, floats to n = 12, lambda in {0, 1}). Every entry agrees, e.g.
  lambda = 1, n = 4: 469/52.
- The omitted-slab bounds 1.4e-6 (lambda = 0) and 7.2e-5 (lambda = 1). Agree.
- gamma_0 without the Slepian series: exact E T_n / n for lambda = 0 at n = 10, 12, ..., 20 by value iteration on the
  last n - 1 letters (2^19 states at n = 20, sup-norm change under 1e-11) is 1.53215, 1.53396, 1.53529, 1.53631,
  1.53711, 1.53775. Fitting a + b n^{-1/2} + c n^{-1} (+ d n^{-3/2}) gives a = 1.5454 (1.5436). This agrees with
  the paper's 1.54388 +- 0.00019 to the accuracy such a short extrapolation allows (script
  agent_run/bpwt_refs/indep_iter.py).

## Minor (not acted on)

- The abstract runs to 157 words; several sentences in Section 2 are long.
- The data-availability statement links the repository root rather than the code folder.
