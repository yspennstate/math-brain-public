Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — METRIC MOVEMENT on active R09 successor G0013: `U_* = 2221/20000 -> U_MP`, where `U_MP = 17/171 + (8/19) z_* = 0.1107882326...` and `z_*` is the unique positive root of `175104 z^3 + 4500 z - 125 = 0`; Tang remains RETIRED/FROZEN at `UNBOUNDED_ABOVE` with supported retirement count `6`, and G0002 remains handed off at `Delta_8=UNMEASURED`. Methods used: B24 FIND THE EXTREMAL OBJECT, B11 DUALIZE, B5 ADD A PARAMETER AND DIFFERENTIATE/OPTIMIZE IN IT.** GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector or reasoning-effort selector, so I do not claim otherwise.

# R09 CLOSABLE OUTSIDE — G0013: moment-projection improvement of the global copula bound

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, ownership, and current status

I did **not** reopen Pengfei Tang, Question 4.11. The periodic-tree target remains retired from R09 at the frozen metric `UNBOUNDED_ABOVE`, supported retirement count `6`. I also did not reopen G0002 / Cerf Conjecture 53.1, which remains handed off at `Delta_8=UNMEASURED`.

The controlling current claim is `operations/claims/G0013.md`: R09 exclusively owns the Catalano--Lavenant uniform-copula Wasserstein problem. Let

\[
\lambda=\mathrm{Unif}[0,1],\qquad \nu=\lambda\otimes\lambda,
\]

and

\[
M:=\sup_{\pi\in\Pi(\lambda,\lambda)}W_2^2(\pi,\nu).
\]

The source conjectures

\[
M=\frac1{10},
\]

with the diagonal and antidiagonal as maximizers. R09's frozen metric is

`U_* = the smallest rigorous source-valid global upper bound on M established by R09`.

The preceding complete R09 report proved

\[
M\le \frac{2221}{20000}=0.11105.
\]

This run proves a smaller global upper bound `U_MP` below.

Before new mathematics I reread/recovered the required coordination state: campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; `operations/NEW_METHODS_2026-09-16.md`; the current `operations/claims/G0013.md`; the newest complete R09 report `runs/R09/20260917T1747Z_g0013_higher_mode_gap_5e7c91.md`; current neighboring R08/R10 searchable reports; and historical G0013 intake/attempt material including `G0013-A002`. The root `RESULTS.md` search surface still exposes an old R09 critical-percolation row, so it is stale relative to the newer exclusive claim; this worker does not edit shared roots. Large JSONL ledgers are not representable as a literal byte-for-byte read in one connector response, so exact G0013/attempt searches were used rather than pretending otherwise.

Historical G0013 work is preserved: A002 reduced finite grids to permutations and checked small `n`, but recorded the continuous extreme-copula obstruction. The current Brenier/Jacobi route is distinct and full-class.

## 2. Fresh source / later-paper / prior-art check — 17 September 2026

Primary source: Marta Catalano and Hugo Lavenant, *Measures of Dependence based on Wasserstein distances*, arXiv:2510.06034 (2025), Remark 3.

Current later paper: Stefan Schrott, *Couplings Farthest from the Independent Gaussian*, arXiv:2609.10467v1, submitted 9 September 2026. Its abstract still states that Catalano and Lavenant conjectured the monotone and antimonotone uniform couplings are farthest from independence, while Schrott proves the Gaussian analogue rather than the uniform conjecture.

Fresh bounded searches on 17 September used the exact source title/authors, `Catalano Lavenant Wasserstein copula conjecture`, `Couplings Farthest from the Independent Gaussian`, and Jacobi/Wright--Fisher Poincare + box-constraint combinations. I found no later source claiming a resolution of the uniform conjecture and no inspected source advertising the bound proved below. The Jacobi/Wright--Fisher literature contains the standard spectral/Dirichlet-form machinery; I did not find this moment-projection use in the bounded search. This is **negative bounded evidence only**. Publication novelty remains **UNVERIFIED**.

## 3. Starting point inherited from the previous global theorem

For a positive smooth copula density, let

\[
T=\nabla\phi=(u,v)
\]

be the Brenier map from the uniform square to `pi`, and write

\[
D^2\phi=\begin{pmatrix}a&b\\b&c\end{pmatrix}\succeq0,
\qquad w(x)=x(1-x).
\]

For `t,s in [0,1]` set

\[
q_t(y)=\lambda\{x:u(x,y)\le t\},\qquad
r_s(x)=\lambda\{y:v(x,y)\le s\}.
\]

Uniformity of the two output marginals gives

\[
\int_0^1 q_t(y)\,dy=t,\qquad
\int_0^1 r_s(x)\,dx=s.
\tag{3.1}
\]

Define

\[
I_1=\int_0^1\mathrm{Var}(q_t)\,dt,
\qquad
I_2=\int_0^1\mathrm{Var}(r_s)\,ds.
\]

The previous R09 proof established the exact identity

\[
W_2^2(\pi,\nu)=I_1+I_2.
\tag{3.2}
\]

For each `t`, decompose the centered conditional CDF into the first Jacobi mode and its orthogonal remainder:

\[
q_t(y)-t=A_t\Bigl(y-\frac12\Bigr)+g_t(y),
\quad
A_t=12\int_0^1\Bigl(y-\frac12\Bigr)(q_t(y)-t)\,dy,
\tag{3.3}
\]

with

\[
\int g_t=0,\qquad
\int (y-\tfrac12)g_t=0,\qquad
h_t=\int g_t^2,\qquad
H_1=\int_0^1h_t\,dt.
\tag{3.4}
\]

Define `H_2` symmetrically for `r_s`. The shifted-Legendre/Jacobi eigenvalues `2,6,12,...`, together with `b^2<=ac`, gave the two coupled inequalities

\[
2I_1+I_2+4H_1\le\frac16,
\qquad
I_1+2I_2+4H_2\le\frac16.
\tag{3.5}
\]

Indeed the Jacobi spectral decomposition gives `E_1/2-I_1>=2H_1`, while the PSD Hessian gives `E_1<=1/6-I_2`; the second inequality is symmetric. Adding (3.5) gives

\[
S:=I_1+I_2\le\frac19-\frac43(H_1+H_2).
\tag{3.6}
\]

The preceding report used a deliberately coarse pointwise box estimate. The whole new contribution below is a stronger moment-projection estimate for `h_t`.

## 4. B11 — dualize: an exact one-sided moment projection

The key lemma is purely one-dimensional.

### Lemma 4.1 (relaxed moment-projection bound)

Let `q:[0,1]->[0,1]` be measurable with mean `t`. Put

\[
A=12\int_0^1\Bigl(y-\frac12\Bigr)(q(y)-t)\,dy,
\qquad
q(y)-t=A\Bigl(y-\frac12\Bigr)+g(y),
\]

where `g` is orthogonal to `1` and `y-1/2`, and set

\[
h=\int_0^1g(y)^2\,dy.
\]

Write

\[
m=\min(t,1-t),\qquad a=|A|.
\]

If `a>2m`, then

\[
\boxed{
 h\ge \frac{(a-2m)^3}{12(6m-a)}.
}
\tag{4.1}
\]

Also

\[
0\le a\le6m(1-m).
\tag{4.2}
\]

#### Proof

Replacing `q` by `1-q` if `t>1/2`, and reflecting `y -> 1-y` if necessary, preserves `h` and reduces to

\[
0<m=t\le\frac12,\qquad A=a>0.
\]

The bathtub/rearrangement principle applied to the increasing weight `y-1/2` gives

\[
a=12\int_0^1\Bigl(y-\frac12\Bigr)q(y)\,dy
\le12\int_{1-m}^1\Bigl(y-\frac12\Bigr)dy
=6m(1-m),
\]

which proves (4.2). In particular `a<6m` when `m>0`.

Assume `a>2m`. Let

\[
\ell(y)=m+a\Bigl(y-\frac12\Bigr),
\qquad
L=\frac{6m-a}{4m}\in(0,1),
\qquad
\alpha=1-L,
\]

and define the nonnegative ramp

\[
p(y)=\beta(y-\alpha)_+,
\qquad
\beta=\frac{2m}{L^2}.
\tag{4.3}
\]

Direct integration gives

\[
\int_0^1p=m,
\qquad
12\int_0^1\Bigl(y-\frac12\Bigr)p(y)\,dy
=6m-4mL=a.
\tag{4.4}
\]

Thus `p` has exactly the same two moments as `q` and `ell`. Notice that `p` need not satisfy the upper constraint `p<=1`; this is intentional. We relax the feasible set from `[0,1]` to `[0,infinity)`, so the resulting minimum remains a valid lower bound for `q`.

Let

\[
s(y)=\beta(y-\alpha),
\qquad p=\max(s,0),
\qquad \Lambda(y)=\ell(y)-s(y).
\]

`Lambda` is affine. Since `q-p` has zero zeroth and first centered moments by (4.4),

\[
\int_0^1(q-p)\Lambda=0.
\tag{4.5}
\]

Pointwise, `p` is the Euclidean projection of `s` onto `[0,infinity)`, hence for every `q(y)>=0`,

\[
(q-p)(p-s)\ge0.
\]

Using `p-ell=(p-s)-Lambda` and (4.5),

\[
\int(q-p)(p-\ell)\ge0.
\]

Therefore the Hilbert-space norm identity gives

\[
\|q-\ell\|_2^2
=\|p-\ell\|_2^2+\|q-p\|_2^2+2\langle q-p,p-\ell\rangle
\ge\|p-\ell\|_2^2.
\tag{4.6}
\]

But `q-ell=g`, so the left side is `h`. Also

\[
\int_0^1p^2=\frac{4m^2}{3L},
\]

and because `p` and `ell` have the same two moments,

\[
\int p\ell=\int\ell^2=m^2+\frac{a^2}{12}.
\]

Hence

\[
h\ge\frac{4m^2}{3L}-m^2-\frac{a^2}{12}
=\frac{(a-2m)^3}{12(6m-a)},
\]

which is (4.1). QED.

This is a genuine dual/projection certificate: the affine function `Lambda` is the dual multiplier for the two moment constraints, and the positive-part ramp is the relaxed primal optimizer.

## 5. B24 + B5 — find and optimize the relaxed extremal object

The projection lemma gives a much better universal relation between first-mode mass and higher-mode mass.

### Lemma 5.1

Let

\[
C:=\left(\frac{125}{768}\right)^{1/3}.
\]

For every `q` in Lemma 4.1,

\[
\boxed{
\frac{A^2}{12}\le\frac{m^2}{3}+C h^{1/3}.
}
\tag{5.1}
\]

#### Proof

If `a<=2m`, the claim is immediate. Assume `a>2m`. By (4.1),

\[
\frac{\left(a^2/12-m^2/3\right)^3}{h}
\le
\frac{(a+2m)^3(6m-a)}{144}.
\tag{5.2}
\]

Set

\[
u=\frac{a}{2m}.
\]

Then `u>1`; by (4.2), `u<=3(1-m)`, and `m<=1/2`. The right side of (5.2) becomes

\[
K(m,u)=\frac{m^4}{9}(3-u)(u+1)^3.
\tag{5.3}
\]

For fixed `m`,

\[
\frac{d}{du}\bigl[(3-u)(u+1)^3\bigr]
=4(u+1)^2(2-u).
\]

Thus if `m<=1/3`, the feasible interval contains `u=2` and

\[
K\le3m^4\le\frac1{27}<\frac{125}{768}.
\]

If `1/3<=m<=1/2`, then the upper feasible endpoint satisfies `3(1-m)<=2`, so the maximum occurs at `u=3(1-m)`, giving

\[
K\le\frac{m^5(4-3m)^3}{3}.
\]

Its logarithmic derivative has numerator

\[
20-24m>0
\]

throughout `[1/3,1/2]`, so the maximum is at `m=1/2`:

\[
K\le\frac{(1/2)^5(5/2)^3}{3}=\frac{125}{768}=C^3.
\]

Taking cube roots proves (5.1). QED.

The relaxed extremal object is now explicit: in the one-sided nonnegative moment relaxation the worst constant occurs at the endpoint `m=1/2`, `u=3/2`. This is not claimed to be the true `[0,1]`-constrained extremizer; the discarded upper box constraint can only improve the estimate.

## 6. Integrated nonlinear bound for every conditional-CDF family

Apply Lemma 5.1 to `q_t`, where

\[
m_t=\min(t,1-t).
\]

Using (3.3)--(3.4),

\[
I_1
=\int_0^1\left(\frac{A_t^2}{12}+h_t\right)dt
\le
\int_0^1\frac{m_t^2}{3}\,dt
+C\int_0^1h_t^{1/3}dt+H_1.
\]

Now

\[
\int_0^1\frac{m_t^2}{3}\,dt
=\frac1{36},
\]

and Jensen's inequality for the concave map `x^(1/3)` gives

\[
\int_0^1h_t^{1/3}dt\le H_1^{1/3}.
\]

Therefore

\[
\boxed{
I_1\le F(H_1):=\frac1{36}+C H_1^{1/3}+H_1.
}
\tag{6.1}
\]

Symmetrically,

\[
\boxed{
I_2\le F(H_2).
}
\tag{6.2}
\]

This replaces the preceding report's coefficient `97/100` by the rigorously derived algebraic constant

\[
C=(125/768)^{1/3}=0.5459877904\ldots.
\]

## 7. New full-class global bound

Let `x_*>0` be the unique positive solution of

\[
C x+\frac{19}{3}x^3=\frac1{36},
\tag{7.1}
\]

put

\[
h_*=x_*^3,
\qquad
U_{\rm MP}:=\frac19-\frac83h_*.
\tag{7.2}
\]

### Theorem 7.1

For every copula `pi` on `[0,1]^2`,

\[
\boxed{
W_2^2(\pi,\lambda\otimes\lambda)\le U_{\rm MP}.
}
\tag{7.3}
\]

Equivalently, if `z_*=C x_*`, then `z_*` is the unique positive root of

\[
\boxed{
175104z^3+4500z-125=0,
}
\tag{7.4}
\]

and

\[
\boxed{
U_{\rm MP}=\frac{17}{171}+\frac8{19}z_*.
}
\tag{7.5}
\]

The exact checker certifies

\[
0.027010941<z_*<0.027010942
\]

and hence

\[
\boxed{
0.11078823246783626
<U_{\rm MP}
<0.1107882328888889
<\frac{2221}{20000}=0.11105.
}
\tag{7.6}
\]

#### Proof for positive smooth copula densities

Let

\[
S=I_1+I_2=W_2^2(\pi,\nu).
\]

Suppose for contradiction that `S>U_MP`. Dropping the nonnegative `H_i` terms from (3.5) gives

\[
S+I_1\le\frac16,
\qquad
S+I_2\le\frac16.
\]

Therefore each component also has the lower bound

\[
I_1=S-I_2\ge2S-\frac16,
\qquad
I_2=S-I_1\ge2S-\frac16.
\tag{7.7}
\]

By (7.1)--(7.2),

\[
2U_{\rm MP}-\frac16
=\frac1{36}+C h_*^{1/3}+h_*
=F(h_*).
\tag{7.8}
\]

Thus (7.7) and `S>U_MP` imply

\[
I_i>F(h_*),\qquad i=1,2.
\]

Since `F` is strictly increasing and (6.1)--(6.2) give `I_i<=F(H_i)`, we must have

\[
H_1>h_*,\qquad H_2>h_*.
\tag{7.9}
\]

Adding (3.5),

\[
3S+4(H_1+H_2)\le\frac13.
\]

Using (7.9),

\[
S<\frac19-\frac83h_*=U_{\rm MP},
\]

contradiction. Hence (7.3) holds for positive smooth copula densities.

To obtain (7.4), set `z=Cx` and use `C^3=125/768` in (7.1):

\[
z+\frac{4864}{125}z^3=\frac1{36},
\]

which is exactly (7.4). The derivative of its left side is strictly positive, so the positive root is unique. Equation (7.5) follows by eliminating `z_*^3` from (7.2) using (7.4).

#### Extension to arbitrary copulas

Let `(U,V)~pi`. Convolve each coordinate modulo one with independent smooth strictly positive circular noise of scale `epsilon`:

\[
U_\epsilon=(U+Z_1^\epsilon)\bmod1,
\qquad
V_\epsilon=(V+Z_2^\epsilon)\bmod1.
\]

Because Haar/uniform measure on the circle is invariant under convolution, both marginals remain uniform. The resulting copula `pi_epsilon` has a positive smooth periodic density. As `epsilon->0`, `pi_epsilon` converges weakly to `pi`; on the bounded square this also gives convergence in quadratic Wasserstein distance. Therefore

\[
W_2(\pi_\epsilon,\nu)\to W_2(\pi,\nu).
\]

Applying the smooth theorem to every `pi_epsilon` and passing to the limit proves (7.3) for all copulas. QED.

## 8. Metric movement and what remains

The diagonal and antidiagonal still give the exact lower bound

\[
M\ge\frac1{10}.
\]

This run therefore improves the full source bracket to

\[
\boxed{
\frac1{10}\le M\le U_{\rm MP}=0.1107882326\ldots.
}
\tag{8.1}
\]

The new upper bound is at least

\[
\frac{36811}{140625000}=0.0002617671\ldots
\]

below the preceding rational bound `2221/20000`, as certified by exact arithmetic. The remaining gap to the conjectured value is about `0.01078823` in squared Wasserstein distance.

This is **PARTIAL / OPEN_CURRENT**, not source closure. No equality-case claim is made.

## 9. What the three methods did

**B24 FIND THE EXTREMAL OBJECT — succeeded.** Instead of optimizing over copulas directly, optimize the one-dimensional moment defect forced by each conditional CDF. The relaxed extremal constant can be solved exactly; its worst endpoint is `m=1/2`, `u=3/2`.

**B11 DUALIZE — succeeded.** The affine multiplier `Lambda` and the positive-part ramp give a complete Hilbert-projection certificate for the one-sided moment relaxation. This is the mechanism that cuts the previous box-lemma constant substantially.

**B5 ADD A PARAMETER AND OPTIMIZE — succeeded.** The normalized first-mode parameter `u=a/(2m)` turns the constant into the two-parameter elementary function `K(m,u)`, whose exact maximum is `125/768`; inserting that into the coupled Jacobi inequalities moves the global metric.

No checker was built before the route moved. After the analytic theorem was complete, I created one exact arithmetic self-check for the finite algebra/root-bracketing core:

- `artifacts/R09/20260917T1831Z_g0013_moment_projection_exact.py`, creation commit `d9f891a46195e7f23629c5565700ca2c21e5c355`;
- `artifacts/R09/20260917T1831Z_g0013_moment_projection_exact.out`, creation commit `0039b992df4f16d0355d5ca8a8e55cc3f462f3cf`.

The output ends `SELF_CHECK_ONLY / PASS`. It certifies finite algebra and rational root brackets; the theorem-sized argument is written above.

## 10. Next genuinely different routes

Do not repeat B24/B11/B5 next run. The highest-value next triple is:

- **B3 PROVE SOMETHING STRONGER:** solve the full two-sided `[0,1]` moment-projection problem rather than the relaxed nonnegative one. Preliminary algebra suggests the true pointwise constant is materially smaller than `C`, so this can move `U_*` again.
- **B12 FIND WHAT IS CONSERVED:** exploit the nesting `q_t(y)` in `t`; the current proof treats different `t` levels independently and therefore discards cross-level structure.
- **B18 SAY IT IN ANOTHER LANGUAGE:** rewrite the full two-sided projection as a clipped-affine convex program / optimal-control obstacle problem and seek a contact-set dual certificate that can be integrated in `t`.

The present run moved the metric, so the supported G0013 stagnation count resets to `0`.

## 11. Model / scheduler control

The limitation is unchanged in the interface available to this run. Task management exposes title, prompt, schedule/timing, enablement and related delivery controls, but **no model-family selector, no reasoning-effort selector, and no authenticated applied-run model telemetry**. Thus GPT-6/maximum remains prompt-only here; I cannot honestly assert that it ran.

To enforce GPT-6 at maximum, the scheduler/product API would need explicit model and reasoning fields plus authenticated runtime telemetry, or the task would need to be managed from an authorized owning surface that exposes those controls. The repository policy records historical modification probes, including P26, returning `You cannot modify this task`; that is an authorization-context boundary. The valid workaround is the owning authorized context, an ownership/admin transfer, or platform support, not cloning the task or bypassing permissions. No scheduler change was attempted in this run, consistent with the deployment guard.

## 12. Structured `ledger_delta`

```json
{
  "worker": "R09",
  "active_claim": "G0013",
  "source_status": "OPEN_CURRENT",
  "status": "PARTIAL",
  "metric": "U_* = smallest rigorous source-valid global upper bound on M",
  "before": "2221/20000",
  "after": "U_MP = 17/171 + (8/19) z_*, z_*>0 root of 175104 z^3 + 4500 z - 125 = 0",
  "after_decimal_certified_between": [0.11078823246783626, 0.1107882328888889],
  "movement": true,
  "supported_unchanged_count": 0,
  "methods": [24, 11, 5],
  "new_theorem_scope": "all copulas on [0,1]^2",
  "source_closed": false,
  "tang_q4_11": "RETIRED_FROZEN / UNBOUNDED_ABOVE / count 6",
  "g0002": "HANDOFF / Delta_8 UNMEASURED",
  "checker": "artifacts/R09/20260917T1831Z_g0013_moment_projection_exact.py",
  "checker_output": "artifacts/R09/20260917T1831Z_g0013_moment_projection_exact.out",
  "checker_status": "SELF_CHECK_ONLY / PASS",
  "shared_roots_edited": false,
  "next_methods": [3, 12, 18]
}
```
