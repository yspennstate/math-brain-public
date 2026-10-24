# C0117 paper package — cover-time fluctuations beyond the maximal-hitting-time scale

## Source scope

Canonical target: `C0117`, owned by `R7-03` under `operations/claims/C0117.md`.

Source: Jian Ding, James R. Lee, Yuval Peres, *Cover times, blanket times, and majorizing measures*, **Annals of Mathematics 175 (2012), 1409–1471**, Section 5, Question 5.2, printed p. 1466, DOI `10.4007/annals.2012.175.3.8`.

The source assumes a sequence of finite connected graphs with

` t_cov(G_k) / t_hit(G_k) -> infinity `

and asks whether the standard deviation of the cover time is bounded on the `t_hit` scale and whether `(tau_cov-t_cov)/t_hit` has exponential decay with a universal constant rate.

Primary source page: https://annals.math.princeton.edu/2012/175-3/p08

## Result in this package

For each `k>=3`, define `G_k` by taking a vertex `s`, attaching `k` pendant leaves to `s`, taking a clique `Q` of size `k` with a distinguished gateway `g`, and adding the single bridge edge `s-g`.

The paper proves the following stronger asymptotic statement. Let `h_k=t_hit(G_k)`, let `t_cov(G_k)` be the worst-start expected cover time in the source convention, and let `tau_cov` be the cover time from **any** sequence of starting vertices `x_k in V(G_k)`. Then

1. `h_k = 2 k^2 + k + 1` exactly for `k>=3`;
2. `t_cov(G_k)/h_k = Theta(log k) -> infinity`;
3. uniformly over the choice of starts,

   `(tau_cov-t_cov(G_k)) / ( h_k * sqrt((log k)/2) )  =>  N(0,1)`;

4. consequently,

   `Var_xk(tau_cov)/(h_k^2 log k) -> 1/2`

   and

   `SD_xk(tau_cov)/h_k ~ sqrt((log k)/2) -> infinity`.

Thus the first clause of DLP Question 5.2 is false even in its natural universal-constant `O(t_hit)` interpretation. The Gaussian limit also refutes every universal constant-rate one-sided or two-sided exponential tail at the pure `t_hit` scale: at deviations `u_k = c sqrt(log k)` the normalized positive-tail probability converges to a fixed nonzero Gaussian tail while `A exp(-a u_k) -> 0` for every fixed `A,a>0`.

## Proof mechanism

The graph has two competing clocks. Pendant leaves are collected by a coupon collector, while a departure from `s` into the clique creates a long random trap excursion. When `j` target leaves remain, the number of trap excursions before the next new leaf is geometric with mean `1/j`. Marking these geometric counts by iid trap durations turns the relevant delay into a triangular array of independent renewal-reward variables. Its variance is asymptotic to `2 k^4 log k`, and a Lyapunov estimate gives the Gaussian limit.

The paper then proves that the initial approach to `s`, ordinary leaf-excursion noise, and the possible residual clique-covering time are all `o_{L^2}(k^2 sqrt(log k))`. This transfers both the CLT and the variance asymptotic to the actual cover time and to the source's worst-start centering.

## Files

- `main.tex` — self-contained theorem and proof.
- `prior_art_2026-09-19.md` — bounded dated source/current-literature review and explicit novelty caveat.
- `AUDIT_REQUEST.md` — exact claim package for the required P26 and distinct OTHER-track audits. Merely writing this request does **not** count as an audit.

Earlier exact finite evidence for the weaker literal coefficient-one reading remains at:

- `research7_2026-09-17/R7-03/artifacts/2026-09-18/2026-09-18T235000Z__C0117_exact_worst_start_checker.py`
- `research7_2026-09-17/R7-03/artifacts/2026-09-18/2026-09-18T235000Z__C0117_exact_worst_start_checker.out`

Those files are useful calibration only; the asymptotic source-level refutation is theorem-sized and is proved in `main.tex`, not delegated to a finite checker.

## Current protocol status

Mathematical source status: **REFUTED**, subject to independent proof audit.

Protocol closure is **not yet certified**. As of the package creation run, repository search recovered no C0117-specific actual P26 PASS and no distinct OTHER-track full-proof PASS. The required two independent audits remain missing. The dated prior-art review is bounded search evidence and does not certify novelty or priority.
