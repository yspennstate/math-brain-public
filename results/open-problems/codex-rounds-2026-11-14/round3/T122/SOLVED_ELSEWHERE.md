# Literature stopping condition: Erdős–Rényi branch

Checked 2026-11-15. The earlier result survives the scope check. No new
post-report advance was found in the bounded search. The fixed-degree
regular branch is not established here.

The direct reference is Dmitry Panchenko,
[*The Mézard-Parisi formula*, arXiv:2610.39545v1](https://arxiv.org/abs/2610.39545),
submitted 29 October 2026. Its general lower bound, equation (2.11),
applies to permutation-invariant Poisson clauses with the stated
exponential integrability. The companion is Dmitry Panchenko,
[*Ghirlanda-Guerra identities and cavity equations for diluted spin glass models*,
arXiv:2610.39542v1](https://arxiv.org/abs/2610.39542), submitted the same day.

The matching upper bound comes from Dmitry Panchenko and Michel Talagrand,
[*Bounds for diluted mean-fields spin glass models*, arXiv:math/0405357](https://arxiv.org/html/math/0405357),
Theorem 4, with Proposition 2 supplying the cascade recursion.

Set theta(s,t)=beta(1-st)/2, arity 2, density d/2 and field zero.
The factorization has deterministic negative coefficient
b=-tanh(beta/2), so all required moments E[(-b)^k] are nonnegative.
[PROOF.md](PROOF.md) matches the hierarchical parameterizations explicitly,
including endpoint means and the compound Poisson edge correction.
This gives an arXiv-only route to the same Erdős–Rényi conclusion that
the earlier worker obtained from the separate OpenAI manuscript.

Writing I_d(beta) for the infimum in equation (4) of PROOF.md,

\[
 \frac{\operatorname{MaxCut}(G(n,d/n))}{n}
   \xrightarrow{\mathbb P} c(d),\qquad
 c(d)=\lim_{\beta\to\infty}\frac{I_d(\beta)}\beta,
 \qquad
 0\le\frac{I_d(\beta)}\beta-c(d)\le\frac{\log2}{\beta}.
\]

This is the zero-temperature value of the optimized hierarchical cavity
functional. It does not evaluate c(d) numerically or interchange the
temperature limit with hierarchy infima. The deduction depends on the
stated external theorems; their full proofs were not independently audited.
All ensemble transfer and temperature steps are proved in PROOF.md.
