# Referee report: the divisible sandpile odometer at the critical lower tail

Paper: yspennstate/divisible-sandpile-critical-tail at 92ce290 (main.tex, 1031 lines, 12 pages). Referee:
an agent, 14 Nov 2026.
Claim: for d >= 5, i.i.d. centered scenery with an absolute exponential moment and lower tail exp(-t^(d/2)) up to
constants, the synchronous odometer u_{n+1} = (eta + P u_n)_+ grows at the order the paper states at the endpoint
gamma = d/2, which Bou-Rabee and Panagiotis (arXiv:2609.02829, Theorem 1.3(iii)(b)) exclude; the case gamma < 1 is
treated separately.

## Verdict

SOUND. One fix: three directly relevant prior papers were not cited. Added in commit 1c50c3b (main.tex and main.pdf,
README page count 12 -> 14; the added lines moved a page break). No other change.

## Proofs checked

- Green lemma; the Laplace split at R = C lambda^{1/(d-2)} giving K <= C lambda^q log lambda. Correct.
- Chernoff step with lambda = b (s / log s)^{p-1}, giving Phi. Correct.
- Smoothing lemma (Bernstein with the H_k norms). Correct.
- Upper increment: crude mean through tau_R; the window decomposition with k = eps h; the tail h > sqrt(n). Correct.
- Variational proposition (Holder, Fenchel, and the reverse example showing the bound is attained). Correct.
- Barrier lemma (P - I) log(1 + |x|^2) <= 1/(1 + |x|^2). Correct.
- Lower increment: the hole event, the induction u_j <= a f, A_n <= -(2 - log 2) a, and the Harris-FKG cost
  C a^p log a of order Phi(M). Correct.
- Integration lemma and the inversion Phi(x_T)/T -> p^{p-1}. Correct.
- gamma < 1: stretched-exponential concentration through a truncated martingale; lower bound with H = 4d(M + 1).
  Correct.

## Citations checked against the sources

- Bou-Rabee-Panagiotis arXiv:2609.02829: Theorem 1.3(iii)(b) on p. 6 (gamma in [1, inf), gamma != d/2), Lemma 2.1 and
  Theorem 2.2 on p. 15, Lemma 2.4 p. 16, Lemma 3.2 p. 21, Theorem 6.1 p. 51, Corollary 6.2 p. 52, Proposition 6.3 and
  Lemma 6.4 pp. 53, Lemma 6.5 p. 54, Theorem 6.6 p. 55. All as stated. Their table gives t^{(4-d)/4} for d = 3 and
  log t for d = 4, consistent with the paper's remarks on low dimensions.
- arXiv:2609.02820 (parking), Theorem 3.4 on p. 14. As stated.
- Levine-Peres is cited for the model.

## The fix

The introduction cited Levine-Peres for the model and then Bou-Rabee-Panagiotis, but not the work on the odometer
at critical density that Bou-Rabee-Panagiotis themselves build on. Added one sentence and three entries, each taken
from Bou-Rabee-Panagiotis's own bibliography:

- Levine, Murugan, Peres, Ugurcan, Ann. Henri Poincare 17 (2016) 1677-1711 (stabilization and explosion for i.i.d.
  masses at critical density).
- Cipriani, Hazra, Ruszel, PTRF 172 (2018) 829-868 (scaling limit of the odometer).
- Cipriani, Hazra, Ruszel, SPA 128 (2018) 3054-3081 (heavy-tailed masses).

Rebuilt: no undefined references, every entry cited, secret scan clean.

## Not changed (style only)

The two arXiv-list references in the bibliography link to a moving main branch; "programme" and "program" are mixed;
the abstract carries displayed formulas. None affects correctness.
