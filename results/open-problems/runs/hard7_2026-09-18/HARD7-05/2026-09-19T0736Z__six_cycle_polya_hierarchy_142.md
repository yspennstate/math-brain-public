Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-05 metric MOVED: `W_{1/4}: 547/5000 = 0.1094 -> 27/250 = 0.108`; methods B8 / B3 / B29.**

# HARD7-05 bounded research iteration — six-cycle trace and a Pólya-series hierarchy

Status: **PARTIAL / source target OPEN.** This run proves the source-valid continuous-time bound

\[
\boxed{\theta_{2,1/4}\ge \frac{71}{500}=0.142,}
\tag{0.1}
\]

improving the preceding certified endpoint `703/5000 = 0.1406`. Hence

\[
\boxed{\frac{71}{500}\le \theta_{2,1/4}\le\frac14},\qquad
\boxed{W_{1/4}=\frac14-\frac{71}{500}=\frac{27}{250}=0.108.}
\tag{0.2}
\]

The full Molchan problem — determining `theta_{2,H}` for the one-sided interval `(0,T)` when `0<H<1`, `H != 1/2` — remains open. This is not a closure claim and no independent audit is requested or counted here.

## 1. Continuity, source refresh, ownership, and fleet state

I resumed the existing exclusive claim

`operations/claims/MOLCHAN-2025-THETA2H.md`

owned by `HARD7-05`. I did not create a new alias, alter another track, or update a shared root ledger.

At run start I reread the controlling HARD7 policy, the latest new-methods policy and owner directive, the probability-campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, the canonical claim, the HARD7-05 report chain through `2026-09-19T0726Z__sampled_ou_trace4_1406.md`, and the neighboring HARD7-04/HARD7-06 run directories. I also rechecked the intake/queue aliases for this exact source family rather than treating a queue absence as evidence of nonownership. No claim collision or posted equivalent surfaced.

Fresh primary-source check, **2026-09-19**: the current arXiv PDF of G. Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265, still states on p. 3 that the `alpha=2, H != 1/2` exponent values remain unsolved and displays the one-sided bound (3). URL: https://arxiv.org/pdf/2509.10265 . The current abstract likewise describes `theta_{2,H}` as problematic and records the duality that refutes the old `H(1-H)` formula. The source therefore remains eligible; the old conjectured parabola is not our target.

Dated literature queries for `theta_{2,1/4}`, `e(2,1/4)`, exact integrated-fBM persistence at `H=1/4`, and 2026 persistence follow-ups recovered Molchan's current preprint, Aurzada--Kilian's endpoint-asymptotic work, the 2023 simulation literature, and adjacent 2026 Gaussian-field persistence papers, but no later exact value or bound matching (0.1). This is bounded negative evidence only: **external novelty is not certified**.

The current arXiv source bound at `H=1/4` gives the baseline bracket `1/8 <= theta_{2,1/4} <= 1/4`. The present claim's frozen metric is the width of the best rigorously verified bracket at this exact source point.

## 2. Why change route after the four-step trace

The preceding run used B10/B14/B25 and obtained a four-step killed-OU trace bound. Simply repeating its one-exponential Pólya correction at six steps is too weak: the extra finite dimension by itself does not improve the certified `0.1406` endpoint. The new ingredient is to retain **multiple positive terms of the exact algebraic consequence of Pólya's inequality** before taking the six-cycle expectation.

This run therefore used a completely different numbered triple:

- **B8 — discretize:** pass from the killed operator to an exact six-cycle Gaussian loop and condition on one bipartition of the cycle.
- **B3 — prove something stronger:** derive an entire monotone Pólya-series hierarchy `g_m`, of which the `m=8` certificate is only one member.
- **B29 — add the points at infinity:** formulate the tail envelope in `x=e^{-beta u^2} in [0,1]`, so both `u=0` and `u=infinity` are included in one compact inequality; there is no unverified large-`u` interpolation gap.

The unsuccessful subroute is also informative: truncating the hierarchy too early does not beat the prior four-step certificate. The successful movement begins only after keeping enough positive terms; the exact archived checker uses eight.

## 3. Reuse only the already proved grid comparison

Let `X` be the variance-one stationary Lamperti/dual process for the source model at `H=1/4`. The preceding report proved, on the exact grid

\[
r=\frac{23}{40},\qquad \Delta=4\log\frac{40}{23},
\tag{3.1}
\]

that its covariance satisfies

\[
R_X(k\Delta)\le r^k,\qquad k\ge1.
\tag{3.2}
\]

Let `(Y_j)` be the stationary standard Gaussian AR(1) chain with correlation `r^{|i-j|}`. By Slepian,

\[
\Pr\{X(j\Delta)<0,\ 0\le j\le n\}
\le
\Pr\{Y_j<0,\ 0\le j\le n\}.
\tag{3.3}
\]

Continuous-time persistence implies the sampled event on the left. Therefore any rigorous lower bound on the sampled AR(1) decay rate is a lower bound on the continuous source exponent after division by `Delta`. No simulation-to-continuum inference is made here.

Let `P_r` be the reversible AR(1) Markov operator on `L^2(pi)` for standard Gaussian measure `pi`, and

\[
K=1_{(0,\infty)}P_r1_{(0,\infty)}.
\tag{3.4}
\]

Then the sampled survival rate is at least `-log ||K||`.

## 4. B8 — the six-cycle loop

Because `K` is self-adjoint and `K^6` is positive,

\[
\|K\|^6\le \operatorname{tr}K^6.
\tag{4.1}
\]

The full AR operator has Hermite eigenvalues `1,r,r^2,...`, hence

\[
\operatorname{tr}P_r^6=\sum_{m\ge0}r^{6m}=\frac1{1-r^6}.
\tag{4.2}
\]

Writing the cyclic six-step kernel integral and normalizing by (4.2) gives

\[
\operatorname{tr}K^6=\frac{P_6}{1-r^6},
\tag{4.3}
\]

where `P_6` is the positive-orthant probability of the centered six-dimensional Gaussian loop with cyclic precision

\[
Q_{ii}=\frac{1+r^2}{1-r^2},\qquad
Q_{i,i\pm1}=-\frac{r}{1-r^2}.
\tag{4.4}
\]

Partition the cycle into even sites `E={0,2,4}` and odd sites `O={1,3,5}`. The precision matrix has no odd-odd off-diagonal entries, so conditional on the even vector `Y=(Y_0,Y_2,Y_4)`, the three odd coordinates are independent. If the even coordinates are positive, their standardized conditional means are

\[
u_1=\frac{r(Y_0+Y_2)}{\sqrt{1-r^4}},\quad
u_2=\frac{r(Y_2+Y_4)}{\sqrt{1-r^4}},\quad
u_3=\frac{r(Y_4+Y_0)}{\sqrt{1-r^4}},
\tag{4.5}
\]

so each `u_i >= 0` and

\[
P_6=\mathbb E\left[1_{\{Y_0,Y_2,Y_4>0\}}
\prod_{i=1}^3\Phi(u_i)\right].
\tag{4.6}
\]

This is the key structural gain over the four-step calculation: a six-dimensional orthant problem becomes a three-dimensional Gaussian expectation with three conditionally independent factors.

## 5. B3 + B29 — a global Pólya-series hierarchy

For `u>=0`, put `q(u)=1-Phi(u)`, so `0<=q<=1/2`. Pólya's classical error-function inequality gives

\[
(2\Phi(u)-1)^2<1-e^{-2u^2/\pi},
\]

hence

\[
4q(u)(1-q(u))>e^{-2u^2/\pi}.
\tag{5.1}
\]

Choose the exact rational

\[
\beta=\frac{51}{80}>\frac2\pi,
\qquad x=e^{-\beta u^2}\in[0,1].
\tag{5.2}
\]

Then (5.1) implies

\[
q(u)(1-q(u))\ge \frac{x}{4}.
\tag{5.3}
\]

Since `q -> q(1-q)` is increasing on `[0,1/2]`,

\[
q(u)\ge h(x):=\frac{1-\sqrt{1-x}}2.
\tag{5.4}
\]

Now

\[
h(x)=\sum_{k\ge1}\frac{C_{k-1}}{4^k}x^k,
\tag{5.5}
\]

with positive Catalan coefficients. Thus every truncation

\[
g_m(x)=\sum_{k=1}^m\frac{C_{k-1}}{4^k}x^k
\tag{5.6}
\]

satisfies `0<=g_m(x)<=h(x)<=1/2` on the **closed** compact interval `[0,1]`. Consequently

\[
\Phi(u)\le1-g_m(e^{-\beta u^2})
\quad\text{for every }u\in[0,\infty].
\tag{5.7}
\]

This is the stronger reusable statement: `g_m` increases pointwise to `h`, so the resulting six-cycle upper envelopes decrease monotonically with `m`. There is no special finite-`u` window and no hidden tail case.

For this run take `m=8`:

\[
g_8(x)=\frac{x}{4}+\frac{x^2}{16}+\frac{x^3}{32}
+\frac{5x^4}{256}+\frac{7x^5}{512}+\frac{21x^6}{2048}
+\frac{33x^7}{4096}+\frac{429x^8}{65536}.
\tag{5.8}
\]

Applying (5.7) to the three factors in (4.6) gives a 729-term finite expansion. Write `b_0=1` and `b_k=-C_{k-1}/4^k` for `1<=k<=8`. Then

\[
P_6\le
\sum_{k_1,k_2,k_3=0}^8 b_{k_1}b_{k_2}b_{k_3}
T(k_1,k_2,k_3),
\tag{5.9}
\]

where

\[
T(k_1,k_2,k_3)=
\mathbb E\left[1_{\{Y>0\}}
\exp\left(-\beta\sum_{i=1}^3k_i u_i^2\right)\right].
\tag{5.10}
\]

## 6. Every term in (5.9) reduces to a trivariate orthant formula

Let `C` be the `3 x 3` covariance matrix of the even sites under the six-cycle loop. For a fixed triple `k=(k_1,k_2,k_3)`, write

\[
\beta\sum_i k_i u_i^2=Y^T A_kY,
\tag{6.1}
\]

where `A_k` is an exact rational positive-semidefinite matrix because `r=23/40` and `beta=51/80`.

Gaussian quadratic tilting gives

\[
T(k)=\det(I+2CA_k)^{-1/2}\,
\Pr\{Z_k>0\},
\tag{6.2}
\]

with

\[
Z_k\sim N(0,C_k),\qquad C_k=(C^{-1}+2A_k)^{-1}.
\tag{6.3}
\]

For a centered trivariate Gaussian with correlations `rho_12,rho_13,rho_23`,

\[
\Pr\{Z_1,Z_2,Z_3>0\}
=\frac18+\frac{\arcsin\rho_{12}+\arcsin\rho_{13}+\arcsin\rho_{23}}{4\pi}.
\tag{6.4}
\]

Thus the entire six-cycle bound needs only rational matrix inversion, square-root enclosures, and arcsine enclosures. The even marginal is equicorrelated and the three `u_i` are the three edge sums of its triangle, so `T(k_1,k_2,k_3)` is permutation-invariant. The checker evaluates the 165 sorted triples with exact multiplicities, representing all 729 terms.

## 7. Exact certificate

Artifacts:

- `artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T0736Z__trace6_polya8_exact_check.py`
- `artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T0736Z__trace6_polya8_exact_check.out`

The checker was executed before archival. It uses only Python integers and `Fraction` for the certificate. Square roots are bracketed by integer `isqrt`; arcsines are enclosed by their positive Taylor series with an exact geometric tail; `333/106 < pi < 355/113` fixes all `pi` inequalities. Decimal prints are display only.

Its certified upper enclosure is

\[
P_6<0.1461924319321283\ldots
<\frac{935667494307}{6400000000000},
\tag{7.1}
\]

which is exactly the amount needed for

\[
\operatorname{tr}K^6
=\frac{P_6}{1-r^6}
<\frac{474}{3125}=0.15168.
\tag{7.2}
\]

The checker then verifies the pure-integer inequality

\[
\left(\frac{474}{3125}\right)^{500}
<\left(\frac{23}{40}\right)^{1704}.
\tag{7.3}
\]

Its archived last line is

`ALL_EXACT_CHECKS_PASS = True`.

The checker commit is `2d538935d1929437b26115da92d5a65b74be717d`; the archived-output commit is `1c87325ee4238e40894a7b0ae9388a7fb36e16f9`.

## 8. Finish the exponent bound

From (4.1), (4.3), and (7.2),

\[
\|K\|^6<\frac{474}{3125}.
\]

Therefore the continuous source exponent obeys

\[
\theta_{2,1/4}
\ge \frac{-\log\|K\|}{\Delta}
\ge \frac{-\log(474/3125)}{24\log(40/23)}.
\tag{8.1}
\]

By (7.3), taking logarithms gives

\[
-\log(474/3125)
>\frac{1704}{500}\log(40/23).
\]

Substituting into (8.1),

\[
\theta_{2,1/4}>
\frac{1704}{500\cdot24}
=\frac{71}{500}.
\tag{8.2}
\]

Thus the non-strict certified bracket (0.2) follows. The source upper endpoint `1/4` is unchanged.

Metric movement is therefore

\[
\boxed{W_{1/4}:\frac{547}{5000}=0.1094
\longrightarrow \frac{27}{250}=0.108.}
\tag{8.3}
\]

This is genuine source-level movement, not a changed metric, simulation fit, or finite sampled-path surrogate.

## 9. Capability statement requested by owner

The scheduler/interface situation is unchanged in the relevant respect: the exposed automation schema offers task title, prompt, schedule, timing mode, and enabled state, but **no model selector, no reasoning-effort selector, and no guaranteed run duration**. GPT-6/maximum is therefore still request text only. This run actually identifies as GPT-5.6 Sol; reasoning telemetry is not exposed, so it is `UNVERIFIED`.

I did not modify or probe any other task in this run. Repository evidence is more nuanced than the older denial sentence: `operations/NEW_METHODS_2026-09-16.md` records earlier `You cannot modify this task` probes for P26/P01/P03, while the later root `RESULTS.md` records a successful P26 prompt update in another authorized exposed context. An inaccessible native task cannot be repaired by a GitHub edit or a duplicate schedule; changing a genuinely denied task requires the authorized owning account/workspace interface or platform support. No scheduler change was attempted here.

## 10. Next mathematical obligation

The useful object is now the hierarchy, not another receipt. Two genuinely different continuations are visible:

1. push `m` upward in the same **six-cycle** formula, where every additional coefficient is positive and the upper envelope decreases monotonically; or
2. find a tractable analogue for `tr K^8`, where conditioning on one bipartition leaves a four-dimensional tilted orthant law and the present exact trivariate formula no longer closes automatically.

The second route is structurally more interesting because it attacks the finite-trace approximation rather than merely adding Pólya coefficients. If the fixed width fails to move for three consecutive future runs, Section I applies; this run resets the unchanged counter because the source-relevant metric moved.

## ledger_delta

`HARD7-05 | Molchan 2025 theta_{2,H}; fixed metric W_{1/4} | 547/5000 -> 27/250 | PARTIAL / source OPEN | new certified endpoint theta_{2,1/4} >= 71/500`
