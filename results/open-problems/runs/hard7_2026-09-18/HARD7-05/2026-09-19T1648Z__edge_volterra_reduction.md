Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-05 metric no movement: `W_{1/4}=103389/1000000 = 0.103389 -> 103389/1000000 = 0.103389`; methods B6 / B21 / B29.**

# HARD7-05 bounded research iteration — an edge-smoothed Gaussian comparator and a Volterra-operator reduction

Status: **PARTIAL / source target OPEN.**

This run does **not** claim a new numerical lower endpoint for `theta_{2,1/4}`. It produces a different source-valid comparison family and converts its persistence exponent exactly into the operator norm of a Gaussian-copula deformation of the classical Volterra operator. It also reduces one useful norm certificate to an explicit finite Gaussian cone problem.

The retained source bracket is

\[
\frac{146611}{10^6}\le \theta_{2,1/4}\le \frac14,
\qquad
W_{1/4}=\frac{103389}{10^6}.
\tag{0.1}
\]

The run is therefore honestly **no movement** in the frozen quantity. The value is the new route, not another certificate for the old route.

## 1. Continuity, source, ownership, and current-status check

I resumed the canonical exclusive claim

`operations/claims/MOLCHAN-2025-THETA2H.md`

owned by `HARD7-05`; I did not restart admission, mint a duplicate alias, overwrite another owner, edit another track, or update a shared root ledger.

At run start I reread the governing HARD7 control and new-methods files, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md` and `QUEUE.md`, the canonical claim, the newest visible HARD7-05 report, and newest visible neighbouring HARD7-04/HARD7-06 activity. The intake tree is too large to render byte-for-byte through the connector in one bounded invocation, so I used the required root ledgers plus a canonical source/alias/claim-targeted intake search rather than falsely claiming a literal full-byte scan. No ownership collision, posting exclusion, handoff, or source-closure marker surfaced.

The primary source remains G. Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265 (2025), whose open target is the family of one-sided integrated-fBM persistence exponents `theta_{2,H}`, `0<H<1`, `H != 1/2`:

https://arxiv.org/abs/2509.10265

A fresh bounded web/arXiv search on **19 September 2026** used the exact title, arXiv identifier, `theta_{2,H}`, and `integrated fractional Brownian persistence exponent 2026`. It recovered Molchan's source and adjacent 2026 persistence work, including Aurzada--Müller on random Hurst exponents (arXiv:2603.14934) and Molchan on multivariate-time fBM (arXiv:2608.26680), but no later exact determination of `theta_{2,1/4}` or of the full `theta_{2,H}` family. This is dated bounded negative evidence, not a claim of exhaustive worldwide novelty.

## 2. Frozen source input from the preceding checkpoints

For `H=1/4`, the already certified Lamperti reduction writes the sampled stationary source covariance as

\[
\operatorname{Cov}(X_0,X_k)=R(q^k),
\qquad q=e^{-\Delta/4}.
\tag{2.1}
\]

The exact source covariance algebra proved earlier in this track is

\[
R(u)-u=
\frac{1-u^2}{6u^5}
\left[-P(u^2)+2(1+u^2)(1-u^4)^{3/2}\right],
\tag{2.2}
\]

with

\[
P(z)=2+2z-3z^2-2z^3-2z^4.
\tag{2.3}
\]

The inherited exact envelope is

\[
R(u)\le u\qquad (0<u\le r_0),
\qquad
r_0=\frac{287831}{500000}=0.575662.
\tag{2.4}
\]

The previous run compared `(X_j)` with an ordinary AR(1) covariance `rho^k`. The new route changes the comparison category.

## 3. B6/B21: edge-smoothing a latent AR(1) chain

Let `(U_j)_{j\in\mathbb Z}` be a stationary standard Gaussian AR(1) chain with

\[
\operatorname{Cov}(U_0,U_k)=r^{|k|},\qquad 0<r<1,
\tag{3.1}
\]

and define

\[
Y_j:=\frac{U_j+U_{j-1}}{\sqrt{2(1+r)}}.
\tag{3.2}
\]

Then `Y_j` is stationary standard Gaussian. For `k>=1`, a direct four-term covariance calculation gives

\[
\operatorname{Cov}(Y_0,Y_k)
=\frac{r^k+r^{k-1}+r^{k+1}+r^k}{2(1+r)}
=\frac{1+r}{2}r^{k-1}.
\tag{3.3}
\]

Choose

\[
q=r=\frac45,
\qquad
\Delta=4\log\frac54.
\tag{3.4}
\]

The comparator covariance is therefore

\[
C_1=\frac9{10},\qquad C_2=\frac{18}{25},\qquad
C_k=\frac9{10}\left(\frac45\right)^{k-1}.
\tag{3.5}
\]

### Proposition 3.1 — exact all-lag source domination

For every integer `k>=1`,

\[
R\!\left((4/5)^k\right)<C_k.
\tag{3.6}
\]

**Proof.** For `k=1,2`, use (2.2). Given a proposed rational cap `c>u`, put `z=u^2` and

\[
D=\frac{6u^5(c-u)}{1-u^2},\qquad T=P(z)+D.
\tag{3.7}
\]

Then `R(u)<c` follows once `T>0` and

\[
4(1+z)^2(1-z^2)^3<T^2.
\tag{3.8}
\]

The exact checker verifies (3.8) at `(u,c)=(4/5,9/10)` with positive squared margin

\[
\frac{1105311526912}{1373291015625}>0,
\tag{3.9}
\]

and at `(u,c)=(16/25,18/25)` with positive squared margin

\[
\frac{105836211695476746288627712}
{352249480783939361572265625}>0.
\tag{3.10}
\]

For every `k>=3`,

\[
q^k\le q^3=\frac{64}{125}=0.512
<\frac{287831}{500000}=r_0,
\tag{3.11}
\]

so the inherited envelope (2.4) gives `R(q^k)<=q^k`. But, because `q=r`,

\[
\frac{C_k}{q^k}
=\frac{(1+r)/2}{r}
=\frac98>1.
\tag{3.12}
\]

Hence `R(q^k)<C_k` for every `k>=3` as well. QED.

This was counterexample-tested before proof: the first thing checked was whether lag two or a later lag defeats the smoothed comparator. Lag two does not; after lag two the old exact covariance cone takes over automatically.

By Slepian, the source sampled persistence probability is bounded above by that of `(Y_j)`. Since the continuous source persistence event is contained in its sampled event, the inherited Lamperti reduction yields

\[
\theta_{2,1/4}
\ge \frac{-\log \lambda_{\rm edge}(4/5)}{4\log(5/4)},
\tag{3.13}
\]

where `lambda_edge(r)` is the exponential survival rate of

\[
U_j+U_{j-1}<0\quad\text{for all sampled }j.
\tag{3.14}
\]

No numerical value for `lambda_edge(4/5)` is asserted here.

## 4. B6/B21: exact conversion to a Gaussian Volterra norm

Let `phi` be standard Gaussian measure and `k_r(x,y)` the Mehler kernel of the stationary AR(1) transition relative to `phi`. Define

\[
(T_r f)(x)=\int_{y<-x} k_r(x,y)f(y)\,\phi(dy).
\tag{4.1}
\]

Then, up to an irrelevant one-step boundary convention,

\[
\Pr(U_j+U_{j-1}<0,\ 1\le j\le n)
=\langle 1,T_r^n1\rangle_{L^2(\phi)}.
\tag{4.2}
\]

The kernel in (4.1) is symmetric. Moreover `T_r` is Hilbert--Schmidt: squaring the Mehler kernel and normalizing produces a centered bivariate Gaussian density times `1/(1-r^2)`, and the half-space `x+y<0` has probability `1/2`; hence

\[
\|T_r\|_{HS}^2=\frac{1}{2(1-r^2)}<\infty.
\tag{4.3}
\]

The kernel of `T_r^2` is strictly positive for every pair `(x,z)`, because its intermediate integral ranges over the nonempty half-line

\[
y<\min\{-x,-z\}.
\tag{4.4}
\]

Thus the compact positive operator has a Perron root controlling (4.2), and

\[
\lambda_{\rm edge}(r)=\|T_r\|.
\tag{4.5}
\]

Now define the triangular Gaussian operator

\[
(A_a f)(x)=\int_{y>x} k_a(x,y)f(y)\,\phi(dy)
\tag{4.6}
\]

and reflection `(Rf)(x)=f(-x)`. Changing variables `y=-v` in (4.1) gives exactly

\[
T_r=A_{-r}R.
\tag{4.7}
\]

Gaussian reflection symmetry also gives

\[
RA_{-r}R=A_{-r}^*.
\tag{4.8}
\]

Therefore

\[
T_r^2=A_{-r}A_{-r}^*,
\tag{4.9}
\]

and, since `R` is unitary,

\[
\boxed{\lambda_{\rm edge}(r)=\|A_{-r}\|_{2\to2}.}
\tag{4.10}
\]

This is the main route change of the run: the comparison persistence exponent is a **singular-value problem for a triangular Gaussian-copula operator**, not another killed-half-line AR eigenvalue.

### Solvable deformation point

At `r=0`, `k_0(x,y)=1`, so

\[
(A_0 f)(x)=\int_x^\infty f(y)\,\phi(dy).
\tag{4.11}
\]

Under the Gaussian quantile unitary `u=Phi(x)`, this becomes

\[
(V^*g)(u)=\int_u^1 g(v)\,dv,
\tag{4.12}
\]

which is the adjoint of the classical Volterra operator on `L^2(0,1)`. Hence

\[
\boxed{\lambda_{\rm edge}(0)=\|A_0\|=\frac{2}{\pi}.}
\tag{4.13}
\]

The web search for this operator shape recovered the classical Volterra norm and general Volterra-operator literature, but did not surface a source giving the exact norm of the Gaussian-copula deformation `A_a` for `a<0`. That search is route reconnaissance, not a novelty certification.

## 5. An exact finite trace/cone reduction

The Volterra representation gives one route; even trace powers give another.

For every integer `n>=2`, trace expansion gives

\[
\operatorname{tr}(T_r^n)
=\int \prod_{i=0}^{n-1}
 k_r(x_i,x_{i+1})
 1_{\{x_i+x_{i+1}<0\}}
 \prod_{i=0}^{n-1}\phi(dx_i),
\qquad x_n=x_0.
\tag{5.1}
\]

Without the indicators the integral is

\[
\operatorname{tr}(P_r^n)=\sum_{m\ge0}r^{mn}=\frac1{1-r^n}.
\tag{5.2}
\]

After normalization, the cyclic Gaussian loop has covariance

\[
\operatorname{Cov}(X_i,X_{i+d})
=\frac{r^d+r^{n-d}}{1-r^n},
\qquad 0\le d\le n.
\tag{5.3}
\]

Consequently

\[
\boxed{
\operatorname{tr}(T_r^n)
=\frac{1}{1-r^n}
\Pr_{\rm loop}\{X_i+X_{i+1}<0\ \forall i\pmod n\}.
}
\tag{5.4}
\]

For `n=8,r=4/5`, the exact checker inverts the cyclic precision matrix and verifies the first covariance row

\[
\left(
\frac{456161}{325089},
\frac{9620}{7929},
\frac{400}{369},
\frac{8000}{7929},
\frac{320000}{325089},
\frac{8000}{7929},
\frac{400}{369},
\frac{9620}{7929}
\right),
\tag{5.5}
\]

as well as

\[
\operatorname{tr}(P_{4/5}^8)=\frac{390625}{325089}.
\tag{5.6}
\]

For even `n`, the edge sums satisfy the exact alternating dependence

\[
\sum_{i=0}^{n-1}(-1)^i(X_i+X_{i+1})=0.
\tag{5.7}
\]

Thus the `n=8` probability in (5.4) is a seven-dimensional Gaussian cone probability. Since eighth powers of all self-adjoint eigenvalues are nonnegative,

\[
\lambda_{\rm edge}(4/5)^8\le \operatorname{tr}(T_{4/5}^8).
\tag{5.8}
\]

This is now a concrete finite target: a sufficiently sharp **rigorous** upper bound on the loop cone probability in (5.4) would immediately turn into a new source exponent lower bound through (3.13). A Monte Carlo or floating orthant call would not count; it needs interval/exact certification.

## 6. B29: compactifying the Schur search, and why the simplest version fails

To attack `||A_{-r}||` or equivalently `||T_r||` directly, I tested positive subinvariant weights. For the elementary exponential weight

\[
h_c(x)=e^{-cx},\qquad c>0,
\tag{6.1}
\]

a direct truncated-normal calculation gives

\[
\frac{(T_rh_c)(x)}{h_c(x)}
=
\exp\!\left(c(1-r)x+\frac{c^2(1-r^2)}2\right)
\Phi\!\left(
-\frac{(1+r)x}{\sqrt{1-r^2}}+c\sqrt{1-r^2}
\right).
\tag{6.2}
\]

As `x -> -infinity`, the Gaussian CDF tends to one while the exponential factor tends to zero. As `x -> +infinity`, the Gaussian tail beats the linear exponential. Hence the ratio tends to zero at **both** ends and its supremum is attained on a finite interval. This is the B29 compactification: the infinite-domain Schur problem can be reduced to a bounded interval plus analytic tails.

However, exploratory optimization of this simple exponential family, and then of a two-parameter exponential-quadratic extension, stayed far above the operator cap needed to beat (0.1). Those floating searches are deliberately **not** archived as certificates and do not move the metric. The failure is informative: the next Schur attack needs a weight shaped like the true positive singular function (for example a Gaussian-CDF/polynomial hybrid), or the trace/cone route in §5.

## 7. What was tried, what moved, and what remains

The preceding run used B5/B20/B27. This run used a different triple:

- **B6 — DEFORM TO A SOLVABLE POINT: SUCCESS.** The edge comparator deforms at `r=0` to the classical Volterra operator, giving the exact anchor `2/pi` and a continuous operator family to attack.
- **B21 — ASK WHO ELSE HAS THIS SHAPE: SUCCESS.** Reflection converts the survival transfer operator exactly to the singular norm of the triangular Gaussian-copula operator `A_{-r}`. This imports Volterra/operator-norm machinery and gives the finite even-trace loop representation.
- **B29 — ADD THE POINTS AT INFINITY: PARTIAL / SIMPLE FAMILY FAILS.** Exponential Schur weights compactify the global supremum exactly, but the simplest one- and two-parameter families do not produce a competitive cap.

Frozen metric:

\[
W_{1/4}:\quad \frac{103389}{10^6}\longrightarrow\frac{103389}{10^6}.
\tag{7.1}
\]

This is the first unchanged run after a sequence of genuine movements, so section-I stagnation is **not** triggered.

The next source-facing obligation is no longer “improve the same AR quasimode.” It is one of two precise new objects:

1. prove a sharp global norm bound for `A_{-4/5}` using a nontrivial subinvariant/Volterra argument; or
2. rigorously certify a useful upper bound for the explicit seven-dimensional `n=8` loop cone probability in (5.4), then convert it exactly through (5.8) and (3.13).

Either route is independent of finite simulation of the original continuous path.

## 8. Exact self-check and immutable artifacts

The route was written before checker construction:

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T1640Z__edge_volterra_idea.md`

commit `0eb9f7d0b223b10eb3241b9f0984a629f097fbfa`, read back successfully.

Exact finite checker:

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T1643Z__edge_volterra_exact_check.py`

commit `8c57e0ea3b6ee6f005050afdd07a4c7d9387467c`, read back on `master`.

Archived executed output:

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-19T1643Z__edge_volterra_exact_check.out`

commit `63adcc80de4c80ab3ffb5d076d9f3f62458b5494`, read back successfully and ending

`ALL_EXACT_CHECKS_PASS = True`.

The checker is explicitly a **self-check**. It certifies the two direct covariance inequalities and the rational `n=8` loop covariance/precision algebra. The operator-theoretic claims are proved on the page above; no floating spectral computation is promoted to theorem status.

## 9. Scheduler/model capability honesty

The actual runtime identifies itself as **GPT-5.6 Sol**; reasoning level is **UNVERIFIED**. This is not GPT-6 maximum.

The exposed native automation interface still offers title, prompt, schedule/timing mode and enabled state, but **no model selector, no reasoning-effort selector and no guaranteed run duration**. Therefore GPT-6/maximum remains a prompt-text request only. Changing that requires a platform/native scheduler capability that exposes and authorizes model/reasoning selection; a repository edit cannot do it.

The historical `P26` “You cannot modify this task” receipt is no longer the whole current story: current root `RESULTS.md` records that a P26 full prompt update succeeded in one authorized P/C context, while other IDs/contexts have still rejected edits. The correct workaround for a task that remains denied is the authorized task/account/workspace interface or platform support. Do not bypass the restriction and do not create a duplicate schedule.

## 10. Ledger delta for the authorized shared-root maintainer

```yaml
track: HARD7-05
target: MOLCHAN-2025-THETA2H
status: PARTIAL
metric: W_1/4
before: 103389/1000000
after: 103389/1000000
movement: no movement
methods: [B6, B21, B29]
new_result: >-
  Source-valid q=r=4/5 edge-smoothed AR comparison proved at all lags;
  comparator survival rate exactly equals the norm of triangular Gaussian
  Volterra deformation A_{-r}; n=8 even-trace bound reduced to an explicit
  seven-dimensional Gaussian loop cone probability.
remaining_obligation: >-
  Certify a sharp norm upper bound for A_{-4/5} or a rigorous loop-cone
  probability upper bound strong enough to improve theta_{2,1/4} >= 0.146611.
```
