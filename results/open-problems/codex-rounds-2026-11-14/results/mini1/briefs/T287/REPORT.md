VERDICT: PROVED finite-size fourth-order low-SNR mutual-information and product-MMSE coefficients for fixed bounded symmetric iid priors

The general extensive-rank problem remains unresolved by this work. The completed piece is a rigorous local expansion, including every finite-size correction and its proportional-dimension coefficient. See [PROOF.md](PROOF.md).

For X=UVᵀ/√N, Y_t=√t X+W with standard Gaussian noise, let i(t)=I(X;Y_t)/(NP), e(t)=E||X−E[X|Y_t]||²/(NP), and ρ=M/N. With independent fixed bounded symmetric unit-variance entry priors, of fourth moments a,b,

\[
 i(t)=\tfrac12\log(1+\rho t)-Ct^4+O_{N,P,M}(t^5),\qquad
 e(t)=\frac\rho{1+\rho t}-8Ct^3+O_{N,P,M}(t^4),
\]

\[
 C=\frac{M^2}{48N^4}
 [(ab-3)^2+3(P-1)(a-1)^2+3(N-1)(b-1)^2+6(N-1)(P-1)].
\]

If M/N→α and P/N→β, then C→α²β/8. Rectangles are the only terms surviving this normalization. The same limiting coefficient describes the total correlation of the noisy entries, after subtracting their individual mutual informations. For Rademacher factors with N=P=M=2, the information-deficit coefficient is 5/96, the MMSE-improvement coefficient is 5/12, and the total-correlation coefficient is 1/32.

The limit here takes t→0 first. There is no uniform remainder estimate, no exchange of limits, and no claimed formula at fixed positive t. The theorem does not estimate U modulo signs and permutations. For the unscaled product UVᵀ, multiply e(t) by N. Priors with dimension-dependent sparsity or unbounded support are outside the proof. Novelty relative to earlier perturbative work is not claimed.

Verification command, run from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 check_coefficients.py > verification.stdout 2> verification.stderr
```

All ten exact enumerations passed. They cover one row, one column, unequal rectangular shapes, multiple latent columns, and different sparse fourth moments. A separate ordinary-polynomial integration checked the Hermite norm and gradient norm. Scalar tanh-posterior and log-cosh-likelihood calculations independently checked both expansion constants. The final run took 0.014677 seconds with peak resident memory 16,039,936 bytes. Inherited niceness was 20; the wrapper's attempt to increase it printed a warning. No GPU or numerical library was used. Data: [verification.json](verification.json); full output: [verification.stdout](verification.stdout); code: [check_coefficients.py](check_coefficients.py).

The first computation failed before running because macOS rejected a 768 MiB virtual-address-space limit. Removing that unsupported limit allowed the tiny exact calculation to run; actual RSS was checked. No mathematical assertion failed the checks. The analytic audit checked tail domination, inverse-density bounds, all fourth-cumulant patterns, and the scaling under transposition. Details and the exact failed command are in [LOG.md](LOG.md).

The bounded literature search took less than ten minutes. No solution or new advance after the supplied November 2026 status was found. The following primary pages were actually opened; the newer papers below predate that status:

- Antoine Maillard, Florent Krzakala, Marc Mézard, Lenka Zdeborová, *Perturbative construction of mean-field equations in extensive-rank matrix factorization and denoising*, [arXiv:2110.08775](https://arxiv.org/abs/2110.08775), including its HTML. It contains related fourth-order perturbative corrections.
- Jean Barbier, Francesco Camilli, Justin Ko, Koki Okajima, *On the phase diagram of extensive-rank symmetric matrix denoising beyond rotational invariance*, [arXiv:2411.01974](https://arxiv.org/abs/2411.01974), revised March 2025. Its abstract presents simulations and a conjectural mean-field ansatz for the symmetric model.
- Jean Barbier, Justin Ko, Anas A. Rahman, *A multiscale cavity method for sublinear-rank symmetric matrix factorization*, [arXiv:2403.07189](https://arxiv.org/abs/2403.07189), revised March 2026. Its abstract proves a variational formula for M=o(√ln N), which is outside proportional rank.
- Antoine Maillard, Jean-Christophe Mourrat, *Efficient computation of the asymptotics of extensive-rank HCIZ integrals*, [arXiv:2609.07771](https://arxiv.org/abs/2609.07771), September 2026. Its abstract proves convergence of a numerical scheme for the HCIZ boundary-value problem, rather than solving non-rotational iid factorization.

Next worker: seek a dimension-uniform bound on the normalized entropy remainder after the fourth-order term, for fixed bounded symmetric priors and bounded positive aspect ratios. Even a uniform O(t⁵) bound on a dimension-independent low-SNR interval would turn the iterated coefficient into a constraint on all subsequential fixed-SNR limits. The present Gaussian domination argument does not provide that bound.

Task: “push this problem forward by one checkable piece.” Started 2026-11-14 approximately 22:09 Asia/Tbilisi.
