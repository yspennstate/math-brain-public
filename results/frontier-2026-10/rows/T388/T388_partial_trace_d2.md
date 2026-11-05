# T388, target 2: in the whitened spiked cumulant model the partial trace M_n = (1/n) sum (|x|^2 - d - 2) x x^T equals kappa4 u u^T plus noise of norm about 2 sqrt 2 d/sqrt n, so its bottom eigenvector finds u at n = O(d^2 log d), matching the low-degree threshold; Oja's rule on the same statistic does it in one pass at n of order d^2, so the d^3 of online SGD belongs to learners that see x only through <w, x>, not to one-pass algorithms

Sources: Szekely, Bardone, Gerace, Goldt, arXiv:2312.14922 (model and low-degree bound, via the dossier and the 18 Oct move); the
store card on online He4 SGD in this model (claim_e556914f, d^3 measured).

## The statistic

The model is x = S(z + beta g u), with z ~ N(0, I_d), g = ±1 and S whitening, so Cov x = I. The only signal is the fourth cumulant
along u, kappa = -2 beta^4/(1+beta^2)^2, which is -1/2 at beta = 1. For a whitened vector,
E[x_i x_j x_k x_l] = δ_ij δ_kl + δ_ik δ_jl + δ_il δ_jk + kappa u_i u_j u_k u_l. Summing over k = l gives

    E[(|x|^2 - d - 2) x x^T] = kappa u u^T     (|u| = 1).

So the partial trace of the empirical fourth-moment tensor, M_n = (1/n) sum_i a_i x_i x_i^T with a_i = |x_i|^2 - d - 2, is a rank-one
spike plus a mean-zero sum. The weight a_i has standard deviation about sqrt(2d). Each term has variance ||E[a^2 |x|^2 x x^T]|| ≈ 2d^2
and norm about d^(3/2). Matrix Bernstein, after truncating a_i at sqrt(d) polylog d, gives

    ||M_n - kappa u u^T|| <~ d sqrt(log d/n) + d^(3/2) polylog(d)/n.

This is below |kappa|/2 once n >~ d^2 log d/kappa^2. Davis-Kahan then puts the bottom eigenvector within angle O(d sqrt(log d/n)/|kappa|)
of u. This degree-4 spectral method runs in time O(n d^2), and its rate matches the low-degree threshold n ~ d^2 of 2312.14922
(Theorem 5, theta_c = 2) up to the log. The method is elementary. It is the partial-trace idea of tensor PCA applied to the sample
fourth moment, and is probably known in some form. I have not found a citation for this model.

## Checks (`t388.py`, `t388_out.txt`, `t388_oja.py`, `t388_oja_out.txt`; beta = 1, 3 seeds each)

Overlap |<v, u>| of the bottom eigenvector of M_n, at n = c d^2:

| c | d = 16 | d = 32 | d = 64 |
|---|---|---|---|
| 0.5 | 0.32 | 0.24 | 0.20 |
| 8 | 0.60 | 0.37 | 0.57 |
| 32 | 0.83 | 0.88 | 0.87 |
| 128 | 0.96 | 0.97 | |

At fixed c the overlap does not fall as d grows, so n ∝ d^2 is the right scale. The transition sits where the predicted noise norm
2 sqrt 2 d/sqrt n crosses |kappa|, between c = 8 and c = 32.

## One pass is enough: Oja's rule

The update w <- (w - eta a_i (w.x_i) x_i)/|...| is projected online SGD on the per-sample loss a_i (w.x_i)^2/2 on the sphere. It
uses each sample once. Its population loss is kappa m^2/2 with m = <w, u>, which is information exponent 2, not 4. Streaming-PCA
bounds (Jain et al. 2016, Allen-Zhu and Li 2017) require n of order (variance/gap^2) log d = 8 d^2 log d/(4 kappa^2) for this
statistic. The step was eta = 2 log n/(|kappa| n), from a uniform random start. Measured overlap:

| c | d = 16 | d = 32 |
|---|---|---|
| 128 | 0.32 | 0.28 |
| 512 | 0.86 | 0.87 |
| 2048 | 0.96 | 0.96 |

That is again a collapse at fixed c, with a constant about 16 times the offline one. The extra factor is the log n of the step rule
and the variance-to-gap ratio.

## What this says about the row

The d^3 of online SGD with a He4 neuron (claim_e556914f, slope 3.24) is the cost of a learner whose per-sample gradient depends on
x only through <w, x> and x. That is a single-index correlation loss with information exponent 4. Weighting by |x|^2, a feature
any network with a quadratic or ReLU-pair unit can form, turns the problem into information exponent 2 in m. Then one pass at
n ~ d^2 log d suffices. So the restated row splits in two.

1. Polynomial time, any number of passes: settled up to the log factor. Success comes from the partial trace at d^2 log d.
   Failure at o(d^2) is conditional, from the low-degree bound.
2. GD or SGD on the actual network of 2312.14922 (ReLU, m = 5d, multi-pass). Still open. The question is now whether the network's
   training dynamics build the |x|^2 weighting, and that is what multi-pass training would need to explain. It is not a question of
   sample reuse in itself. The Oja run shows reuse is not needed.

## Files

`t388.py`, `t388_out.txt`, `t388_oja.py`, `t388_oja_out.txt`, `DOSSIER.md`.
