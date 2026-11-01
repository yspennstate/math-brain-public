# HARD7-04 idea checkpoint — quantitative post-giant histogram duality

**Status:** idea-before-verification checkpoint.  This is not a closure claim and contains no finite checker claim.

The preceding HARD7-04 recovery now has the source-size candidate
\[
|C_{2,n}|=(1+o_p(1))\frac{2R_*}{\varepsilon_n^2}\log(n\varepsilon_n^3),
\]
but the source phrase “Does the discrete duality principle still hold?” can reasonably be read more broadly than one component-size asymptotic.  The next useful mathematical question is therefore not another constant/certificate around the already-zero frozen drift metric.  It is whether giant deletion actually produces the **extinction-tilted degree law**, quantitatively and simultaneously over all degrees.

Let `n_d=#{i:d_i=d}` and let `N_d^{out}` count degree-`d` vertices outside the unique giant.  Let `xi_n` be the extinction probability of the size-biased excess branching process, with `t_n^*=-log xi_n`.  The target strengthened statement is

\[
\boxed{
\sum_{d\ge0}(1+d)\bigl|N_d^{out}-n_d\xi_n^d\bigr|
=o_p(n\varepsilon_n).
}
\tag{I.1}
\]

If true, after normalization it implies both vertex-degree and half-edge-size-biased empirical laws outside the giant are `o_p(epsilon_n)` in total variation from their extinction tilts.  This is a genuinely distributional discrete-duality statement, not just first-moment drift reflection.

## Counterexample-first stress test

The dangerous configuration is not one fixed degree class; it is a triangular array with as many occupied degree classes as finite third moment permits.  For independent clock survivors
\[
M_d(t)=\sum_{i:d_i=d}{\bf1}_{\{E_i>t\}},\qquad
m_d(t)=n_de^{-dt},
\]
classwise maximal inequalities give
\[
\mathbb E\sup_t|M_d(t)-m_d(t)|\le4\sqrt{n_d}.
\]
Summing naively over degrees could have destroyed the `n epsilon_n` scale.  But the support contains at most `d_max+1` classes and finite third moment gives `d_max=O(n^{1/3})` (indeed `o(n^{1/3})` under moment convergence), while
\[
\sum_d(1+d)^2n_d=O(n).
\]
Therefore
\[
\sum_d(1+d)\sqrt{n_d}
\le \sqrt{(d_{max}+1)\sum_d(1+d)^2n_d}
=O(n^{2/3})=o(n\varepsilon_n),
\]
since `epsilon_n n^{1/3}->infinity`.  Thus the maximal-support stress family does **not** refute (I.1); the source window has enough room for a simultaneous histogram theorem.

## Three new Section-B moves

- **B9 RANDOMIZE.** Use the exact independent exponential half-edge clocks to turn the ideal post-giant degree law into a product Bernoulli thinning with mean `n_d xi_n^d`.
- **B23 DO WHAT THE PROPOSER DID NOT EXPECT.** Prove a statement stronger than the size question: quantitative total-variation duality of the whole empirical degree law, rather than another bound on `C_2`.
- **B27 SWAP THE QUANTIFIERS.** Replace “for each fixed degree `d`” convergence by one simultaneous weighted `ell^1` estimate over **all** degree classes, including the largest degrees allowed by the source hypotheses.

Repository search found no prior HARD7-04 report using this exact B9/B23/B27 triple on `VDH-8.3-DUALITY`.

## Proof route to test

1. Prove the uniform all-degree clock estimate
   \[
   \sup_{t\ge0}\sum_d(1+d)|M_d(t)-m_d(t)|=o_p(n\varepsilon_n).
   \]
2. At the genuine giant stopping boundary `tau_n`, use `tau_n-t_n^*=o_p(epsilon_n)` and the Lipschitz bound
   \[
   |e^{-d\tau_n}-e^{-dt_n^*}|\le d|\tau_n-t_n^*|
   \]
   together with bounded second moment to replace `m_d(tau_n)` by `n_d xi_n^d` in weighted `ell^1`.
3. The already-proved root mismatch is stronger than needed:
   \[
   \sum_i d_i^2|1_{sleeping}-1_{E_i>\tau_n}|=o_p(n\varepsilon_n).
   \]
   Since zero-degree vertices never create root mismatch and `1+d\le2d^2` for `d>=1`, it transfers the clock histogram to the exact stopping remainder.
4. The literal complement of the giant also contains components explored before the giant.  The published/previously archived exploration input says their total half-edge mass is `o_p(n epsilon_n)`; for positive-degree vertices `1+d\le2d`, so adding them back changes the weighted histogram by only `o_p(n epsilon_n)`.
5. Normalize the resulting count vector.  If
   \[
   \pi_{n,d}^\dagger=\frac{n_d\xi_n^d}{\sum_j n_j\xi_n^j},
   \qquad
   \widehat\pi_{n,d}^{out}=\frac{N_d^{out}}{\sum_jN_j^{out}},
   \]
   then the elementary normalization inequality should yield
   \[
   \|\widehat\pi_n^{out}-\pi_n^\dagger\|_{TV}=o_p(\varepsilon_n).
   \]
   The same weighted estimate should give `o_p(epsilon_n)` total variation for the corresponding size-biased half-edge laws.

If each step survives exact checking on paper, this directly narrows the source-scope ambiguity left by the preceding size theorem.  It still would not by itself assert total-variation equivalence of the **entire graph law** after deleting the giant, and it would not satisfy repository closure without independent audits/prior-art reconciliation.