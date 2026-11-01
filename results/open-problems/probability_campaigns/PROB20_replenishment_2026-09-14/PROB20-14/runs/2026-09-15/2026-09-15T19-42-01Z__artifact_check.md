# PROB20-14 artifact execution certificate

**Status:** consistency check passed; not proof evidence for the universal theorem.

Artifact:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/one_sided_entropy_bridge_check.py`

The script was executed with Python using exact `fractions.Fraction` dynamic programming for the convolution probabilities. Test law:

\[
\pi_0=1/2,\qquad \pi_1=1/4,\qquad \pi_3=1/4,
\]
which is critical, with `N=14`.

Observed output values:

```text
a_n = 5709711/67108864
lambda_n = 2.464147727166984
D(Q||pi) = 0.0020106634260114477
lambda_n/n = 0.17601055194049886
K=0: tail_Q=0.9285714285714286, tail_pi=1, V_K=0, rhs=1
K=1: tail_Q=0.6687028467815621, tail_pi=0.75, V_K=0.25, rhs=0.7817069663166586
K=2: tail_Q=0.6687028467815621, tail_pi=0.75, V_K=0.25, rhs=0.7817069663166586
all assertions passed
```

The exact assertions checked were:

1. the conditioned marginal is normalized;
2. its exact mean is `(N-1)/N`;
3. `D(Q||pi) <= lambda_n/N`;
4. for each listed truncation `K`,
   \[
   \mathbb E_Q[X;X>K]
   \le
   \mathbb E_\pi[X;X>K]
   +\sqrt{2D(Q\|\pi)\,\mathbb E_\pi[X^2;X\le K]}.
   \]

This finite-support computation checks the algebra implemented in the new one-sided entropy step only. It does not test the infinite-variance quantifiers, the Palm theorem, or the every-fixed-level conclusion.
