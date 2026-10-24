# P0334 checks — 2026-10-12

The complete analytic proof and its hostile-referee audit are in ATTEMPT.md. These checks concern finite auxiliary steps, not a formalization of the infinite-dimensional theorem.

## Source hypothesis audit

Original Bobkov–Ledoux Theorem 5.3, p.46, was read; no endpoint monotonicity is present. Corollary A.22, p.109, proves the exact equality between its J_p and the weighted derivative integral, with f the density of the absolutely continuous COMPONENT. Proposition A.17, p.104, and Lemma 5.8, p.51, explicitly define absolute continuity locally. Proposition B.13, p.125, states the underlying weighted derivative bound for all absolutely continuous functions. This removes the possible hidden assumption that the auxiliary increasing envelope must have a smooth density or lack atoms.

Original Beare–Kaji Theorems 3.1 and 3.2, p.16, were read. They require integrability of Q; in our necessity proof it follows from L^p-valuedness of the empirical difference. Their limit identification and local absolute continuity criterion are exactly the L^1 ingredients used.

## Numerical finite checks

Run: `python -X utf8 numerical_checks.py`, exit code 0. Results: `numerical_results.json`.

- Fixed seed 3341012; n=8,32,128,512 and p=1.5,2,4; 180 replications per pair (2160 samples).
- Piecewise-constant derivative with narrow spikes at dyadic scales down to 2^-14 on both endpoints, plus a zero-derivative interval giving an atom. The signed residual subtracts a second derivative profile; the comparison envelope integrates its absolute derivative.
- 1000 random evaluation points per replication (2,160,000 comparisons). Largest excess of the residual increment over the envelope increment: 5.551115123125783e-17 (floating-point rounding).
- Integrated p-errors were computed analytically on the common refinement of all quantile knots and empirical bins: integrate |a+bt|^p using sign(z)|z|^(p+1)/(p+1), with a separate constant-slope case. This is not a uniform-grid endpoint approximation.
- Every sample's integrated residual error was at most the integrated envelope error within the stated tolerance. All empirical mean errors were below the published (generous) bound (5p)^p K_p.
- Runtime about 1.02 seconds; arrays are far below the 1GB limit. Finite spikes and Monte Carlo cannot prove an asymptotic theorem or sharpness; the analytic argument handles infinite tails.

## Analytic boundary cases

1. Point mass: Q constant, K_p=0 and the process is zero.
2. Bernoulli(theta), 0<theta<1: Q has a jump, violates local AC, and ||sqrt(n)(Q_n-Q)||_p^p=n^(p/2)|theta_n-theta| grows at scale n^((p-1)/2) for p>1 by the scalar binomial CLT. Thus there is no L^p tightness. This tests the necessity of local AC independently of the weighted derivative (which alone would miss the jump).
3. Gaussian: Q'~1/[t sqrt(2log(1/t))] near zero. K_p is finite precisely for 1<=p<2; at p=2 the tail integrand is comparable to 1/[t log(1/t)] and diverges. This matches Bobkov–Ledoux p.46 and prevents an incorrect claim for all Gaussian L^p spaces.
4. Pareto quantile Q(t)=(1-t)^(-a), a>0: Q'=a(1-t)^(-a-1), so K_p finite iff a<1/p-1/2. Equality produces logarithmic divergence. This is possible only for p<2 and implies ap<1 as required for Q in L^p.
5. Q'(t)=1+0.5 sin(1/t)+0.5 sin(1/(1-t)), 0<t<1: nonnegative, bounded, continuous on the interior, and highly oscillatory near endpoints. Q is locally AC, K_p finite for every finite p, and the proof applies without endpoint monotonicity. No density regularity at support endpoints is asserted.

## Lean check

`Domination.lean` proves the finite weighted-increment analogue of the absolute-derivative envelope: |sum w_i(a_i-b_i)| <= sum w_i|a_i-b_i| for nonnegative weights. Imports are limited to Real.Basic and the Finset ordered big-operator module. No sorry, added axioms, or native_decide. Ordinary kernel checking is used. Command: `lake env lean ~/brain_workers/TRIO_1011/op/P0334/Domination.lean`, run from ~/lean_verify with a 3600-second subprocess timeout, one Lean command at a time. Completed with EXIT CODE 0. `lean_check.txt` records the standard Lean axioms propext, Classical.choice, and Quot.sound. This checks only the finite weighted-sum domination step, not the full probabilistic theorem.
