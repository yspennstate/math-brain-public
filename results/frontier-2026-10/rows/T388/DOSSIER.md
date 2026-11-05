# T388 Learning from higher-order cumulants: the spiked cumulant model

Lead: unassigned. Dossier written 2026-10-16 by agent A from the row and the arXiv records below (abstracts read 16 Oct
09:2x-09:3x).

## STATEMENT
As in the list row (online SGD on a two-layer network learns the spike with n = Theta(d^2) up to logs and fails with
n = o(d^2)), with a flag on the target: online SGD from a random start on an information-exponent-4 problem is known to need
about d^3 samples for tensor PCA (Bardone-Goldt below), so the d^2 claim may hold only for multi-pass or batch methods.
The first target is to settle which algorithm the d^2 belongs to.

## FRONTIER
- Szekely, Bardone, Gerace, Goldt arXiv:2312.14922: exact likelihood-ratio norm; statistical distinguishability needs n >~ d,
  polynomial-time (low-degree) needs n >~ d^2; neural networks learn to distinguish with quadratic sample complexity, random
  features do not.
- Bardone, Goldt arXiv:2404.08602: recovering one direction from an order-p tensor by online SGD needs about d^(p-1) samples;
  correlated latent variables across cumulants accelerate learning.
- Open: a theorem for SGD on the spiked cumulant model at either rate.

## ARCHITECTURE
Online SGD's escape from the equator is governed by the information exponent: the first nonzero Hermite order of the
correlation between the network's output and the spike. In the spiked cumulant model the first signal is in the 4th cumulant,
which is exponent 4 and gives d^3 for online SGD; batch methods reuse samples and can reach the low-degree rate d^2.

## FAILURE POINT
The row asks online SGD to hit the low-degree rate, which the information-exponent theory says online SGD from a random start
does not do for exponent 4 without smoothing or sample reuse.

## SHAPE
Days: check 2312.14922's training protocol (online or multi-pass) for its quadratic claim. Weeks for a theorem either way.

## OBSTRUCTION
If the network result is multi-pass, the target is a multi-pass SGD theorem at d^2 (sample reuse, as in Dandi et al.-type
analyses); if online, an explanation of how online SGD beats the exponent-4 rate.

## TARGETS
1. Read 2312.14922's experiments: online or multi-pass, batch size, and the observed exponent.
2. Re-state the row for the algorithm that matches (likely: multi-pass GD at n = d^2 polylog d), then attempt the matching
   failure at n = o(d^2) via the low-degree bound.

## RESULTS

2026-10-31 (agent B), T388_partial_trace_d2.md. In the whitened spiked cumulant model x = S(z + beta g u), g = +-1, the
matrix M_n = (1/n) sum (|x|^2 - d - 2) x x^T has mean kappa u u^T with kappa = -2 beta^4/(1 + beta^2)^2, and its bottom
eigenvector finds u once n is of order d^2. A one-pass Oja iteration on the same weighted matrices reaches u at n of order
d^2 as well, against the d^3 that online SGD needs at information exponent 4.

2026-11-04 (agent C), audit (AUDIT_agent_C.md). The identity is exact. The statistic is FOBI (Cardoso 1989) shifted by
(d + 2) I; fixed-d theory is in arXiv:1406.4765 and 1701.06836, a reweighted-PCA relative in high dimension in 1704.01041.
Weak recovery holds at n > 2(d^2 + 6d)/kappa^2, and above it overlap^2 = 1 - 2(d^2 + 6d)/(kappa^2 n), within 0.03 of
simulation at c >= 32 for d = 16, 32, 64. With the decaying step of Jain et al. (arXiv:1602.06929) one pass needs about 4
times the offline sample size at d = 32. Jain et al. allow indefinite matrices but need them bounded, so a truncated
version with its bias bound is still to be written. No novelty is claimed for the d^2 rate; the row (online SGD on a
two-layer network) stays open.
