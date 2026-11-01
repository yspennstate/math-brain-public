Model actually run: GPT-5.6 Sol; reasoning level UNVERIFIED. This was not GPT-6 at maximum, and I do not claim otherwise.

# P03-A analytic proof report — core-tail Gini decomposition and an unbounded-tail monotonicity extension

**Status:** PROVED PARTIAL (new repository theorem candidate; not independently audited; no claim of external novelty; the full Lyons–Pemantle–Peres conjecture remains unresolved).

**Native role:** P03-A, `6aa7b398af30819181ca50ba3c4e6c33`, complementary analytic recursive/derivative role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`. Old D0047 history is preserved. Canonical ownership was checked at assignment; this report does not create or take another worker's claim.

**Captured master immediately before write:** `d8d34035a572395bc60bcb3130b5b3082841b90b`.

## 1. Source convention, current boundary, and nonduplication

Let `nu` be the offspring variable of a supercritical Galton–Watson tree without leaves,

\[
P(\nu=0)=0,\qquad m=E\nu\in(1,\infty).
\]

Ben Arous–Fribergh–Sidoravicius use child/outward bias `beta`; this analytic line uses reciprocal parent bias

\[
\lambda=1/\beta,
\]

so at a vertex with `k` children

\[
P_\lambda(x,x^*)=\frac{\lambda}{\lambda+k},\qquad
P_\lambda(x,x_i)=\frac1{\lambda+k}.
\]

Increasing `lambda` pushes toward the root, so the source conjecture asks for nonincreasing speed `ell_lambda` throughout the transient interval `0<lambda<m`.

Current source continuity used here:

* Ben Arous, Fribergh and Sidoravicius, arXiv:1111.5865, old high-outward-bias monotonicity;
* Aïdékon, arXiv:1111.4313 / PTRF 159 (2014), exact speed representation;
* Bowditch–Tokushige, arXiv:1906.07913 and arXiv:2006.03433, differentiability / analyticity in ballistic regimes, without the missing sign;
* Song–Wang–Xiang, J. Appl. Probab. 62 (2025), 1044–1052, DOI `10.1017/jpr.2024.113`: if the minimum offspring is `d>=2`, strict parent-bias decrease is proved source-uniformly for

\[
0\le\lambda\le
\theta_d:=\frac{d}{1+\sqrt{1-1/d}}.
\tag{1.1}
\]

A bounded literature refresh on 20 September 2026 found no checked source-wide resolution. This is bounded negative evidence, not a novelty certificate.

Repository continuity consumed rather than duplicated:

* latest own P03-A report `2026-09-20T0401Z__harmonic-tail-stieltjes-extension.md`, which supplies the exact effective-degree derivative identity, the finite-mean unbounded-support sensitivity bound below `lambda=d`, and Stieltjes bounds for the escape tilt;
* P03-B `2026-09-20T0412Z__first-split-hazard-amplification.md`, which is the distinct regeneration/coupling route. Its first-split hazard theorem is not reproved here;
* complementary P01 T06 `proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T03-58-29Z__run-report.md`, which already develops a sharp pairwise-Gini method for **bounded** support and proves wide bounded-support rectangles. I do not count another bounded-support Gini rectangle as the main advance here.

The fixed full-source metric remains

`R_full: 1 -> 1`.

The new target is different: keep a rigorous high-quality bounded-degree **core**, but allow a genuinely unbounded offspring tail of controlled mass, with no upper cutoff on the tail values.

## 2. Inherited effective-degree reduction

Assume for the new theorem

\[
P(\nu\ge d)=1,\qquad d\ge2,\qquad E\nu<\infty,
\tag{2.1}
\]

and work first with `1<=lambda<d`.

For conditional current offspring `n`, let `B_0,...,B_n` be iid copies of the quenched escape probability from a child-root before hitting its parent, and set

\[
S_n=\sum_{i=0}^n B_i,
\qquad
c_n(\lambda)=E\left[\frac{S_n}{(n+1)(\lambda-1+S_n)}\right].
\tag{2.2}
\]

Writing `p_n=P(nu=n)`, define the escape-tilted offspring law

\[
C=\sum_{n\ge d}p_nc_n,
\qquad
\pi_n=\frac{p_nc_n}{C},
\qquad
M=\sum_{n\ge d}n\pi_n.
\tag{2.3}
\]

The inherited Aïdékon reduction is

\[
\boxed{\ell_\lambda=\frac{M-\lambda}{M+\lambda}},
\qquad
\boxed{\ell'_\lambda=
\frac{2(\lambda M'-M)}{(M+\lambda)^2}}.
\tag{2.4}
\]

Put

\[
g_n=-\partial_\lambda\log c_n.
\]

The previous analytic reports justify differentiation under the finite-mean hypothesis on compact subintervals of `[1,d)` and give the exact covariance identity

\[
\boxed{
M'=\sum_{n<m}\pi_n\pi_m(m-n)(g_n-g_m).
}
\tag{2.5}
\]

They also give the global upper sensitivity bound

\[
0\le g_n\le q_+(\lambda):=
\frac{d(d-1)}{(d-\lambda)(d^2-\lambda)}
\qquad(n\ge d).
\tag{2.6}
\]

The new argument refines the *lower* sensitivity only on a finite core, and charges the complement by its escape-tilted first moment.

## 3. New universal lower sensitivity: no maximum degree is needed

Let `U_i=-B_i' >=0`, `T_n=sum_i U_i`, and `A_n=lambda-1+S_n`. The pointwise ratio whose `c_n`-weighted mean is `g_n` is

\[
q_n^{\rm pt}=
\frac{1+(\lambda-1)T_n/S_n}{A_n}.
\tag{3.1}
\]

For `lambda>=1`, the numerator is at least one. Also `B_i<=1`, hence

\[
A_n=\lambda-1+S_n\le n+\lambda.
\]

Therefore, for **every** `n>=d` and without any upper-support assumption,

\[
\boxed{
g_n(\lambda)\ge\frac1{n+\lambda}.}
\tag{3.2}
\]

Fix a finite core cutoff `D>d`. If `d<=n<m<=D`, (2.6) and (3.2) imply

\[
g_n-g_m
\le Q_{d,D}(\lambda)
:=q_+(\lambda)-\frac1{D+\lambda}.
\tag{3.3}
\]

Both terms on the right move in the favorable direction with `lambda`, so `Q_{d,D}` is increasing on `[1,d)`. Thus for `1<=lambda<=L<d`,

\[
g_n-g_m\le Q_{d,D}(L)
\qquad(d\le n<m\le D).
\tag{3.4}
\]

This is the first part of the new bridge: low degrees get a substantially smaller pairwise oscillation than the global worst-case `q_+` even when the actual offspring support is unbounded.

## 4. New core-tail Gini decomposition

Split the tilted degree defect `M-d` into

\[
x_0:=\sum_{d\le n\le D}\pi_n(n-d),
\qquad
x_\infty:=\sum_{n>D}\pi_n(n-d).
\tag{4.1}
\]

Let `W=D-d`. Decompose the pair sum (2.5) into pairs entirely inside the core and pairs whose larger coordinate exceeds `D`.

### 4.1 Core pairs

Define

\[
G_0:=\sum_{d\le n<m\le D}\pi_n\pi_m(m-n).
\]

For `j=d,...,D-1`, put

\[
a_j=\sum_{n=d}^{j}\pi_n,
\qquad
b_j=\sum_{m=j+1}^{D}\pi_m.
\]

Counting each pair once across every cut between it gives

\[
G_0=\sum_{j=d}^{D-1}a_jb_j.
\tag{4.2}
\]

Because `a_j+b_j<=1`,

\[
a_jb_j\le b_j(1-b_j).
\]

Also

\[
\sum_{j=d}^{D-1}b_j=x_0.
\]

Cauchy–Schwarz gives `sum b_j^2 >= x_0^2/W`, hence the **defect-aware core Gini bound**

\[
\boxed{
G_0\le x_0-\frac{x_0^2}{W}.
}
\tag{4.3}
\]

For a pure endpoint core this is sharp. The important feature is that the covariance cost now vanishes quadratically as the core approaches either endpoint, instead of paying a distribution-free `W/4` loss.

### 4.2 Tail pairs

Let

\[
G_\infty:=
\sum_{m>D}\sum_{d\le n<m}\pi_n\pi_m(m-n).
\]

Since `m-n<=m-d`,

\[
\boxed{
G_\infty\le x_\infty.
}
\tag{4.4}
\]

No support diameter appears. Combining (2.5), (2.6), (3.4), (4.3) and (4.4), uniformly for `1<=lambda<=L`, gives

\[
M'
\le
Q_{d,D}(L)\left(x_0-\frac{x_0^2}{W}\right)
+q_+(L)x_\infty.
\tag{4.5}
\]

Since `M=d+x_0+x_infty`, define

\[
A:=LQ_{d,D}(L),
\qquad
B:=Lq_+(L)-1.
\tag{4.6}
\]

Then

\[
\boxed{
\lambda M'-M
\le
-d+(A-1)x_0-\frac{A}{W}x_0^2+B x_\infty.
}
\tag{4.7}
\]

If `A>1`, the core quadratic has maximum

\[
-d+\frac{W(A-1)^2}{4A}=-\delta_0,
\]

where

\[
\boxed{
\delta_0:=d-\frac{W(A-1)^2}{4A}.
}
\tag{4.8}
\]

(If `A<=1`, simply set `delta_0=d`.) Therefore

\[
\boxed{
\lambda M'-M\le-\delta_0+B x_\infty.
}
\tag{4.9}
\]

This isolates the entire effect of arbitrarily large offspring values into one tilted tail defect `x_infty`.

## 5. New Stieltjes transport of the original tail into the tilted tail

The previous P03-A Stieltjes lemma gives, for `1<=lambda<=L<d`,

\[
\frac1{n+\kappa_L}\le c_n(\lambda)\le\frac1{n+\lambda},
\qquad
\kappa_L:=\frac{L(d-1)}{d-L},
\tag{5.1}
\]

where the lower bound uses `kappa_lambda<=kappa_L`.

Consequently

\[
x_\infty
=\frac{\sum_{n>D}(n-d)p_nc_n}{\sum_n p_nc_n}
\le
\frac{T_D}{J_L},
\tag{5.2}
\]

with the bounded original-law functionals

\[
T_D:=E\left[\frac{\nu-d}{\nu+1}\mathbf1_{\{\nu>D\}}\right],
\qquad
J_L:=E\left[\frac1{\nu+\kappa_L}\right].
\tag{5.3}
\]

Indeed, on the numerator `c_n<=1/(n+lambda)<=1/(n+1)`, while the denominator is at least `J_L`.

Combining (4.9) and (5.2) proves the run's main theorem.

### Theorem 5.1 — unbounded-support core-tail certificate

Assume `P(nu>=d)=1`, `d>=2`, and `E nu<infinity`. Fix integers `D>d` and a bias endpoint `1<L<d`. Define `q_+(L)`, `Q_{d,D}(L)`, `A`, `B`, `delta_0`, `T_D` and `J_L` by (2.6), (3.3), (4.6), (4.8), and (5.3). If

\[
\boxed{\delta_0>0
\quad\text{and}\quad
B\frac{T_D}{J_L}<\delta_0,}
\tag{5.4}
\]

then

\[
\ell'_\lambda<0
\qquad(1\le\lambda\le L).
\tag{5.5}
\]

Since the 2025 source theorem overlaps this interval from zero through `theta_d>1`, strict monotonicity holds on the entire interval

\[
\boxed{0\le\lambda\le L.}
\tag{5.6}
\]

This theorem imposes **no upper bound** on the offspring support.

### Corollary 5.2 — tail-mass-only form

If

\[
\varepsilon:=P(\nu>D),
\]

then `T_D<=epsilon`, while the core mass gives

\[
J_L\ge\frac{1-\varepsilon}{D+\kappa_L}.
\]

Thus

\[
x_\infty\le
\frac{\varepsilon(D+\kappa_L)}{1-\varepsilon}.
\tag{5.7}
\]

A sufficient condition is therefore

\[
\boxed{
\varepsilon<
\frac{\delta_0}
{B(D+\kappa_L)+\delta_0}.}
\tag{5.8}
\]

This is the substantive removal of the bounded-support restriction: a small amount of probability may sit at arbitrarily large offspring values, and the proof automatically downweights it through the escape tilt.

## 6. Concrete theorem: 99% of the law on degrees 3 and 4, arbitrary unbounded tail, through `lambda=8/3`

Take

\[
d=3,\qquad D=4,\qquad L=\frac83.
\tag{6.1}
\]

Exact arithmetic gives

\[
q_+(L)=\frac{54}{19},
\qquad
\frac1{D+L}=\frac3{20},
\qquad
Q_{3,4}(L)=\frac{1023}{380},
\]

and hence

\[
A=\frac{682}{95},
\qquad
B=\frac{125}{19},
\qquad
\kappa_L=16.
\tag{6.2}
\]

The core margin is

\[
\boxed{
\delta_0
=3-\frac{(A-1)^2}{4A}
=\frac{432911}{259160}
\approx1.67043911.}
\tag{6.3}
\]

The tail-mass threshold from (5.8) is

\[
\boxed{
\varepsilon<
\frac{432911}{34532911}
\approx0.0125361861.}
\tag{6.4}
\]

Therefore the clean condition

\[
P(\nu\ge3)=1,
\qquad
P(\nu>4)\le\frac1{100},
\qquad
E\nu<\infty
\tag{6.5}
\]

implies strict monotonicity through `lambda=8/3`, with **no restriction whatsoever on how large the offspring values above 4 may be**.

For `epsilon=1/100`, (5.7) gives

\[
x_\infty\le\frac{20}{99}.
\]

Thus (4.9) has the explicit sign margin

\[
\boxed{
\lambda M'-M
\le
-\frac{796199}{2332440}
<-0.3413
\qquad(1\le\lambda\le8/3).}
\tag{6.6}
\]

Consequently:

### Corollary 6.1

For every finite-mean no-leaf offspring law satisfying (6.5),

\[
\boxed{
\ell_\lambda\text{ is strictly decreasing on }
0\le\lambda\le\frac83.}
\tag{6.7}
\]

This is qualitatively different from the exact `{3,4}` rare-mixture results elsewhere in the repository: one percent of the original law may be spread over an **unbounded** set of arbitrarily large degrees. It is also different from the complementary P01 bounded-support rectangles, because no finite upper support is assumed here.

No external novelty claim is made pending independent review and a dedicated prior-art search.

## 7. What moved and what remains

### Full source metric

`R_full: 1 -> 1`.

The original conjecture for every no-leaf supercritical finite-mean offspring law on the full transient interval is not solved.

### Genuine intermediate obligations

Before this run, P03-A could handle arbitrary unbounded support by global mean/harmonic-tail criteria, but the strongest derivative envelope still paid the minimum-degree singularity uniformly and did not combine a strong low-degree core with an arbitrary remote tail.

After this run:

1. `g_n>=1/(n+lambda)` is available without a maximum-degree assumption;
2. the exact covariance is split into a low-degree Gini core and an unbounded tail;
3. the core has the defect-aware quadratic bound `G_0<=x_0-x_0^2/(D-d)`;
4. the remote tail is charged only by `x_infty`, then transported back to the original law by Stieltjes weights;
5. an explicit theorem reaches `lambda=8/3` for every minimum-degree-3 law with at most 1% mass above degree 4, even when that tail has unbounded support.

### Remaining gap

The real analytic barrier is still `lambda=d`. The inherited escape/sensitivity upper bound `q_+(lambda)` contains `(d-lambda)^{-1}` and diverges as the parent bias approaches the minimum degree. The new core-tail argument shows that *remote high degrees are not the fundamental obstruction*: they can be isolated and paid for cheaply. The obstruction is now concentrated in the sensitivity of the minimum-degree core itself.

The minimum-offspring-one case is also untouched by this theorem.

## 8. Next attack

Do **not** repeat another tail cutoff optimization next run. The next method must attack the singular factor itself.

The concrete analytic target is an averaged score bound of the form

\[
E_{\pi_\lambda}
\left[g_\nu\,\middle|\,\nu\in\{d,d+1\}\right]
\le C_{P,L}<\infty
\]

that remains finite as `lambda up to d`, using either:

1. the escape recursion differentiated before taking the deterministic minimum-degree floor, so small escape probabilities are compensated by their probability under the tilted environment; or
2. the P03-B regeneration score-response identity to replace the pointwise `U/B` bound by a block-averaged sensitivity.

If that averaged core estimate is obtained, the core-tail theorem above will immediately transport it to laws with arbitrary remote offspring tails instead of restarting from bounded support.

No new checker or audit artifact was created: this run's progress is analytic, and the exact rational examples are direct consequences of the displayed formulas. Candidate-proof audit is deferred per the progress-first owner directive.