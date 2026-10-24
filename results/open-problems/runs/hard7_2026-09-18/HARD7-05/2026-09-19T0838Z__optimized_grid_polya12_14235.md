Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-05 metric MOVED: `W_{1/4}: 27/250 = 0.108 -> 2153/20000 = 0.10765`; methods B5 / B18 / B24.**

# HARD7-05 bounded research iteration — extremal grid deformation, Craig dual route, and a sharper six-cycle certificate

Status: **PARTIAL / source target OPEN.** This run proves the source-valid continuous-time bound

\[
\boxed{\theta_{2,1/4}\ge \frac{2847}{20000}=0.14235,}
\tag{0.1}
\]

improving the preceding certified endpoint `71/500=0.142`. Consequently

\[
\boxed{\frac{2847}{20000}\le \theta_{2,1/4}\le \frac14},\qquad
\boxed{W_{1/4}=\frac14-\frac{2847}{20000}=\frac{2153}{20000}=0.10765.}
\tag{0.2}
\]

This is a strict source-metric improvement, not a finite-path simulation or a change of model. The full Molchan problem remains open.

## 1. Continuity, ownership, source refresh, and fleet state

I resumed the existing exclusive claim

`operations/claims/MOLCHAN-2025-THETA2H.md`

owned by `HARD7-05`. I did not restart admission, mint an alias, change another track's files, or update a shared root ledger.

At run start I reread `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the canonical claim, the HARD7-05 checkpoint chain through `2026-09-19T0736Z__six_cycle_polya_hierarchy_142.md`, and the newest visible neighboring HARD7-04/HARD7-06 activity. Targeted searches through repository claims/intake aliases for Molchan, `theta_{2,H}`, and arXiv:2509.10265 still return this claim as the canonical owner and no posted equivalent.

Fresh source/literature check dated **2026-09-19**: G. Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265, still states in the current PDF that for `alpha=2`, `H != 1/2`, the exponent values remain an unsolved problem; the displayed one-sided bound (3) remains the source baseline. Primary source: https://arxiv.org/abs/2509.10265 and https://arxiv.org/pdf/2509.10265 . Fresh searches for exact `theta_{2,1/4}` and 2026 integrated-fBM persistence follow-ups recovered Molchan's source, Aurzada--Müller (arXiv:2603.14934, random Hurst exponent), Molchan (arXiv:2608.26680, multivariate-time fBM), and adjacent Gaussian-field persistence work, but no exact value or later bound resolving the present `H=1/4` target. This is bounded negative evidence only; external novelty is **not** certified.

The source upper endpoint remains `U_{1/4}=1/4`. The preceding run proved `L_{1/4}=71/500` and hence `W_{1/4}=27/250`.

## 2. Why this run changes route rather than only increasing a checker parameter

The previous run used B8/B3/B29 and fixed the comparison grid at `r=23/40` and the Pólya Gaussian rate at `beta=51/80`. Merely increasing the Catalan truncation `m` at those same parameters does improve the trace, but it leaves two analytic sources of slack untouched.

This run used a different triple:

- **B5 — add a parameter and differentiate/deform it: SUCCESS.** I treated both the Slepian grid correlation `r` and the Pólya exponential rate `beta` as free parameters and pushed them toward their exact admissible boundaries. This gives the source-level improvement in (0.1).
- **B18 — say it in another language: PROMISING BUT NOT THE WINNING CERTIFICATE THIS RUN.** I rewrote the Gaussian tail by Craig's integral, producing a second exact finite-mixture route to the same killed-operator trace that does not use Pólya at all. The route is recorded in Section 5. Its first coarse partitions are weaker per term than the optimized Catalan route, so I did not spend the bookkeeping budget certifying a losing partition.
- **B24 — find the extremal object: SUCCESS.** The admissible Slepian grid is controlled by the boundary where the polynomial `Q` from the covariance factorization changes sign. Rather than accept `23/40`, I pushed to the safe rational `1439/2500`, immediately below the numerically located boundary, and proved admissibility exactly on the entire required range.

Thus the new mathematics is parameter-boundary identification plus an alternative Gaussian-tail dualization; the exact checker only certifies the final finite arithmetic.

## 3. B24 + B5: move the Slepian grid to the covariance boundary

For the variance-one stationary Lamperti/dual process `X` at `H=1/4`, the earlier exact covariance algebra gives, for `t>=0`, with

\[
q=e^{-t/4},\qquad z=q^2,
\]

\[
R_X(t)-q=\frac{1-q^2}{6q^5}F(q),
\tag{3.1}
\]
where
\[
F(q)=-P(z)+2(1+z)(1-z^2)^{3/2},
\tag{3.2}
\]
\[
P(z)=2+2z-3z^2-2z^3-2z^4.
\tag{3.3}
\]
Squaring the competition in (3.2) gives the exact factorization
\[
P(z)^2-4(1+z)^2(1-z^2)^3=z^3Q(z),
\tag{3.4}
\]
with
\[
Q(z)=8z^5+16z^4+8z^3-20z^2-7z+4.
\tag{3.5}
\]

The B24 observation is that the first loss of this direct comparison is encoded by the first positive zero of `Q`; numerically this puts the grid boundary near `r=0.57566...`. That numerical root is only exploratory. For the proof choose the exact rational

\[
\boxed{r=\frac{1439}{2500}=0.5756},\qquad
\Delta=4\log\frac{2500}{1439}.
\tag{3.6}
\]

Let `z_0=r^2`. On `0<=z<=z_0`,

\[
P(z)\ge 2-3z_0^2-2z_0^3-2z_0^4>0.
\tag{3.7}
\]
Also
\[
Q'(z)=40z^4+64z^3+24z^2-40z-7
\le 40z_0^4+64z_0^3+24z_0^2-7<0.
\tag{3.8}
\]
The exact checker verifies both inequalities and
\[
Q(z_0)=
\frac{1276405115334233190492364517601}
{1192092895507812500000000000000000}>0.
\tag{3.9}
\]
Therefore `Q(z)>0` throughout `[0,z_0]`. Equations (3.4), (3.7), and positivity imply
\[
P(z)>2(1+z)(1-z^2)^{3/2},
\]
so `F(q)<0` for every `0<q<=r`. Hence
\[
R_X(k\Delta)\le r^k\qquad(k\ge1).
\tag{3.10}
\]

Let `(Y_j)` be stationary Gaussian AR(1) with correlation `r^{|i-j|}`. Slepian gives the finite-grid comparison
\[
\Pr\{X(j\Delta)<0,\ 0\le j\le n\}
\le
\Pr\{Y_j<0,\ 0\le j\le n\}.
\tag{3.11}
\]
Continuous-time persistence implies the sampled event on the left, so an upper bound on AR(1) sampled survival is rigorously an upper bound on continuous persistence. No discrete-to-continuous interpolation assumption is used.

## 4. B5: move the Pólya exponential rate to its boundary

Write `q_N(u)=1-\Phi(u)` for `u>=0`. Pólya's error-function inequality gives
\[
4q_N(u)(1-q_N(u))\ge e^{-2u^2/\pi}.
\tag{4.1}
\]
The previous run used `beta=51/80`. Here choose
\[
\boxed{\beta=\frac{191}{300}=0.63666\ldots}.
\tag{4.2}
\]
Since `pi>333/106`,
\[
\frac2\pi<\frac{212}{333}<\frac{191}{300}=\beta.
\tag{4.3}
\]
Thus
\[
4q_N(u)(1-q_N(u))\ge e^{-\beta u^2}.
\tag{4.4}
\]
With `x=e^{-beta u^2}` and
\[
h(x)=\frac{1-\sqrt{1-x}}2
=\sum_{k\ge1}\frac{C_{k-1}}{4^k}x^k,
\tag{4.5}
\]
monotonicity of `q(1-q)` on `[0,1/2]` gives `q_N(u)>=h(x)`. Therefore for every truncation
\[
g_m(x)=\sum_{k=1}^m\frac{C_{k-1}}{4^k}x^k
\]
we have the global bound
\[
\Phi(u)\le1-g_m(e^{-\beta u^2}),\qquad u\in[0,\infty].
\tag{4.6}
\]
This run uses `m=12`.

## 5. B18: an independent Craig-integral language for future runs

For `u>=0`, the Gaussian upper tail has Craig's representation
\[
1-\Phi(u)=\frac1\pi\int_0^{\pi/2}
\exp\left(-\frac{u^2}{2\sin^2\vartheta}\right)d\vartheta.
\tag{5.1}
\]
This converts the tail itself into a positive mixture of Gaussian exponentials. If
\[
0=a_0<a_1<\cdots<a_N=\pi/2,
\]
then monotonicity of `sin` gives, for every `j>=2`,
\[
1-\Phi(u)\ge
\sum_{j=2}^N\frac{a_j-a_{j-1}}\pi
\exp\left(-\frac{u^2}{2\sin^2 a_{j-1}}\right).
\tag{5.2}
\]
For an equal-angle partition, the weights are rational; rigorous rational lower bounds on `sin(a_j)` turn each coefficient into a rational Gaussian exponential. Substituting (5.2) into the conditional six-cycle formula below expands the orthant probability into the *same kind* of exactly evaluable quadratic Gaussian tilts used in Section 6. Thus (5.1) gives a Pólya-free hierarchy.

I explored this route far enough to verify the mechanism and compare its finite-mixture efficiency. Coarse partitions lose too much in the left endpoints and did not beat the optimized Pólya certificate within this bounded run. No theorem or source movement is claimed from the exploratory Craig partitions. The important gain is conceptual: future work can improve the tail approximation independently of Pólya, rather than only adding more Catalan coefficients.

## 6. Six-cycle trace with the optimized parameters

Let `P_r` be the reversible AR(1) Markov operator on standard Gaussian `L^2`, and
\[
K=1_{(0,\infty)}P_r1_{(0,\infty)}.
\tag{6.1}
\]
As in the preceding run,
\[
\|K\|^6\le\operatorname{tr}K^6
=\frac{P_6}{1-r^6},
\tag{6.2}
\]
where `P_6` is the positive-orthant probability of the centered six-dimensional cyclic Gaussian loop with precision
\[
Q_{ii}=\frac{1+r^2}{1-r^2},\qquad
Q_{i,i\pm1}=-\frac{r}{1-r^2}.
\tag{6.3}
\]
Conditioning on even sites `Y=(Y_0,Y_2,Y_4)` makes the three odd sites independent, with standardized means
\[
u_1=\frac{r(Y_0+Y_2)}{\sqrt{1-r^4}},\quad
u_2=\frac{r(Y_2+Y_4)}{\sqrt{1-r^4}},\quad
u_3=\frac{r(Y_4+Y_0)}{\sqrt{1-r^4}},
\tag{6.4}
\]
and therefore
\[
P_6=\mathbb E\left[1_{\{Y>0\}}
\prod_{i=1}^3\Phi(u_i)\right].
\tag{6.5}
\]

Apply (4.6) with `m=12`. Writing `b_0=1` and `b_k=-C_{k-1}/4^k`,
\[
P_6\le
\sum_{k_1,k_2,k_3=0}^{12}
 b_{k_1}b_{k_2}b_{k_3}T(k_1,k_2,k_3),
\tag{6.6}
\]
where
\[
T(k)=\mathbb E\left[1_{\{Y>0\}}
 e^{-\beta\sum_i k_i u_i^2}\right].
\tag{6.7}
\]
If `C` is the covariance of `Y` and `A_k` is the exact rational positive-semidefinite matrix satisfying
\[
\beta\sum_i k_i u_i^2=Y^TA_kY,
\]
then Gaussian quadratic tilting yields
\[
T(k)=\det(I+2CA_k)^{-1/2}\Pr\{Z_k>0\},
\qquad
Z_k\sim N(0,(C^{-1}+2A_k)^{-1}).
\tag{6.8}
\]
For a centered trivariate Gaussian,
\[
\Pr\{Z_1,Z_2,Z_3>0\}
=\frac18+\frac{\arcsin\rho_{12}+\arcsin\rho_{13}+\arcsin\rho_{23}}{4\pi}.
\tag{6.9}
\]
Thus (6.6) is a finite exact-arithmetic problem. Permutation symmetry reduces the `13^3=2197` expanded terms to `455` sorted triples with exact multiplicities.

## 7. Exact certificate and exponent calculation

Executed artifacts:

- `artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T0838Z__optimized_grid_polya12_exact_check.py`
- `artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T0838Z__optimized_grid_polya12_exact_check.out`

The finite certificate uses Python integers and `Fraction` for all decisive inequalities. Square roots are bracketed by integer `isqrt`; arcsines use positive Taylor partial sums plus an exact geometric remainder; `333/106 < pi < 355/113` handles every `pi` comparison. Printed decimals are diagnostics only.

It certifies
\[
P_6<0.145959659245604\ldots,
\]
and, crucially,
\[
\operatorname{tr}K^6<\frac{303}{2000}=0.1515.
\tag{7.1}
\]
It also verifies the pure rational/integer power inequality
\[
\left(\frac{303}{2000}\right)^{2500}
<\left(\frac{1439}{2500}\right)^{8541}.
\tag{7.2}
\]
The archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

From (6.2) and (7.1),
\[
\theta_{2,1/4}
\ge \frac{-\log\|K\|}{\Delta}
>\frac{-\log(303/2000)}{24\log(2500/1439)}.
\tag{7.3}
\]
Equation (7.2) implies
\[
-\log(303/2000)>
\frac{8541}{2500}\log(2500/1439).
\tag{7.4}
\]
Substitution into (7.3) gives
\[
\theta_{2,1/4}>
\frac{8541}{2500\cdot24}
=\frac{2847}{20000}.
\tag{7.5}
\]
Hence the non-strict bracket (0.2) follows.

Metric movement is
\[
\boxed{W_{1/4}:\frac{27}{250}=0.108
\longrightarrow\frac{2153}{20000}=0.10765.}
\tag{7.6}
\]

## 8. Capability statement requested by owner

The exposed automation interface still offers task title, prompt, schedule, timing mode, and enabled state, but **no model selector, no reasoning-effort selector, and no guaranteed run duration**. GPT-6/maximum remains prompt text only. This invocation actually identifies as GPT-5.6 Sol; authenticated reasoning telemetry is unavailable, so the reasoning level is `UNVERIFIED`.

I did not modify or probe another schedule. Repository policy records historical `You cannot modify this task` failures for P26/P01/P03 and later successful updates in a different authorized exposed context. A task genuinely denied in the current owning context cannot be repaired by a GitHub edit or duplicate schedule; it requires the authorized owning account/workspace interface or platform support.

## 9. Next obligation

The source metric moved, so Section I is **not** triggered and the unchanged counter resets. The strongest genuinely different next route is to turn the Craig representation (5.1) into an exact optimized exponential-mixture minorant and compare it against the Catalan hierarchy at fixed six-cycle length. A second route is the eight-cycle trace, where the obstacle becomes a four-dimensional tilted orthant probability rather than a trivariate one.

The next run must use a different numbered triple from B5/B18/B24; a natural candidate is B6/B17/B27.

## ledger_delta

`HARD7-05 | Molchan 2025 theta_{2,H}; fixed metric W_{1/4} | 27/250 -> 2153/20000 | PARTIAL / source OPEN | certified theta_{2,1/4} >= 2847/20000`.
