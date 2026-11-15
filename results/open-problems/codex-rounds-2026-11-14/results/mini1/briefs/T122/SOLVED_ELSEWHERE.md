# A recent cavity-formula advance; scope for T122

Checked 2026-11-14. The literature stopping condition is met. The references
below are recent proof manuscripts, not a claim here of a completed independent
audit of their proofs. The Erdős–Rényi implication is spelled out below. Coverage
of uniformly random regular graphs has not been established in this session.

## References actually opened

1. Dmitry Panchenko, *The Mézard-Parisi formula*,
   [arXiv:2610.39545v1](https://arxiv.org/abs/2610.39545), submitted 2026-10-29.
   [Full text, Theorem 2.1](https://arxiv.org/html/2610.39545v1).
   Equation (2.10) identifies the hierarchical variational value for the named
   diluted even-spin and random K-sat models. Equation (2.11) supplies a lower
   bound for general permutation-invariant clause laws satisfying (2.4).
   The named spin examples have symmetric random couplings; they should not
   simply be identified with deterministic antiferromagnetic couplings.

2. Dmitry Panchenko, *Ghirlanda-Guerra identities and cavity equations for
   diluted spin glass models*,
   [arXiv:2610.39542v1](https://arxiv.org/abs/2610.39542), submitted 2026-10-29.
   This companion gives the perturbation and cavity details for the lower bound.

3. OpenAI, *The Mézard–Parisi formula for diluted spin glasses*, dated
   2026-09-23. No arXiv identifier was found for this manuscript.
   [Manuscript](https://github.com/openai/math/blob/main/preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/paper.pdf).
   The primary TeX was read:
   [author and date](https://raw.githubusercontent.com/openai/math/main/preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/main.tex),
   [model and Theorem 2.1](https://raw.githubusercontent.com/openai/math/main/preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/model.tex),
   [zero-temperature discussion](https://raw.githubusercontent.com/openai/math/main/preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/consequences.tex).
   Theorem 2.1 asserts equality between Poisson diluted pressure and the
   infimum of the Panchenko–Talagrand trial functional over finite hierarchies,
   under its integrability, factorization, independence, and positivity
   hypotheses. The deterministic interaction needed here satisfies these
   hypotheses, as checked next.

The general upper-bound assumptions were also checked in Dmitry Panchenko and
Michel Talagrand, *Bounds for diluted mean-fields spin glass models*,
[arXiv:math/0405357](https://arxiv.org/html/math/0405357), equations (1.2)–(1.4).
The following implication uses the equality asserted by reference 3 directly;
it does not require an unproved identification of the two new papers' trial
parameterizations.

## Application to the Poisson antiferromagnet

This is a deduction from the cited theorem, conditional on its validity.
Set p=2, interaction density alpha=d/2, external field zero, and, for beta>0,

\[
 \theta_\beta(s,t)=\beta\,\mathbf 1\{s\ne t\}.
\]

The required factorization is the elementary identity

\[
 e^{\theta_\beta(s,t)}
 =e^{\beta/2}\cosh(\beta/2)
       \bigl(1-\tanh(\beta/2)st\bigr).
\]

Thus take a=e^{beta/2}cosh(beta/2), b=-tanh(beta/2), and deterministic
f_1(s)=f_2(s)=s. Deterministic random variables are independent copies.
For every positive integer k, E[(-b)^k]=tanh(beta/2)^k>=0, and
|b f_1(s)f_2(t)|<1. The maximum absolute interaction is beta, so
integrability holds. The clause is also invariant under swapping inputs.

Let H_n be the multigraph obtained from Pois(dn/2) independent ordered pairs
of uniform vertices, allowing loops and repetitions. Write

\[
 P_n(\beta)=\frac1n\mathbb E\log
   \sum_{\sigma\in\{-1,1\}^n}e^{\beta\operatorname{Cut}_{H_n}(\sigma)},
 \qquad
 I_d(\beta)=\inf_{r,\zeta,\mathbf m}
                  \mathcal B_{r,\beta}(\zeta,\mathbf m),
\]

with the functional and admissible hierarchies exactly as in reference 3,
Section 2, evaluated at the preceding parameters. Its theorem asserts
P_n(beta) -> I_d(beta) for every fixed beta>0.

For every finite graph, including a multigraph, one largest summand and the
bound of 2^n times that summand give

\[
 \frac{\mathbb E\operatorname{MaxCut}(H_n)}n
 \le \frac{P_n(\beta)}\beta
 \le \frac{\mathbb E\operatorname{MaxCut}(H_n)}n
                      +\frac{\log2}{\beta}.
\]

The expected optima divided by n are bounded between zero and d/2. If A
and B are their liminf and limsup, passage to limits gives
B <= I_d(beta)/beta <= A+log(2)/beta. Let beta tend to infinity. Then
A=B=:c(d), and

\[
 c(d)=\lim_{\beta\to\infty}\frac{I_d(\beta)}\beta,
 \qquad
 0\le\frac{I_d(\beta)}\beta-c(d)\le\frac{\log2}{\beta}.
\]

The thermodynamic limit is taken first. This argument does not interchange
temperature and hierarchy infima or claim that an optimizer exists.

## Transfer to G(n,d/n)

Poisson splitting makes the multiplicities C_{uv}, for distinct unordered
pairs u<v, independent Pois(d/n) variables. Loops never contribute to a cut.
Collapsing repeated edges leaves G(n,q), q=1-exp(-d/n). For x>=0,

\[
 0\le x-1+e^{-x}\le x^2/2.
\]

The first inequality follows from e^{-x}>=1-x. For the second, the function
1-x+x^2/2-e^{-x} has value and derivative zero at zero and second derivative
1-e^{-x}>=0.

Since E(C_{uv}-1)_+=d/n-1+exp(-d/n), the expected number of deleted edges
is at most d^2(n-1)/(4n). For n>d, couple G(n,q) and G(n,d/n)
monotonically using one independent uniform variable for each pair.
The expected number of added edges has the same upper bound. Adding or
removing one edge changes MaxCut by at most one. Consequently

\[
 \left|\mathbb E\operatorname{MaxCut}(H_n)
       -\mathbb E\operatorname{MaxCut}(G(n,d/n))\right|
 \le \frac{d^2(n-1)}{2n}.
\]

Thus the simple Erdős–Rényi expected optimum has the same limit c(d).
For convergence in probability, resample each independent Bernoulli edge.
The Efron–Stein inequality and the one-edge Lipschitz bound give
Var(MaxCut) <= binom(n,2)(d/n)(1-d/n)=O(n). Chebyshev's inequality finishes.

An independent normalization check uses the score S(sigma)=-sum_{uv}sigma_u
sigma_v, with multiplicity and loops counted. The identity
Cut(sigma)=(|E|+S(sigma))/2 gives c(d)=d/4+g_S/2, where
g_S=lim_n E max_sigma S(sigma)/n exists by this same identity. Moreover
Z_cut(beta)=exp(beta|E|/2) Z_S(beta/2), consistent with the formula above.
For a loop, the two terms cancel, another check on the Poisson convention.

## What remains outside this finding

The sources located use Poisson interaction counts and independent sampled
endpoints. A fixed-degree regular graph is a different ensemble. No transfer
to its hierarchical cavity formula is claimed here. Nor was the long proof
of either new manuscript independently checked in this session. The finding
is a substantial recent advance, with an explicit application of the stated
general theorem to the Erdős–Rényi branch of T122.
