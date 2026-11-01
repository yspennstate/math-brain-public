Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum reasoning is an owner preference, not authenticated runtime telemetry.

# P03-B coupling report — second-order escape recursion, variance absorption, and a sharper quenched elasticity threshold

**Status:** PROVED PARTIAL / NEW SECOND-ORDER MAXIMUM-PRINCIPLE LEMMA / STRICTLY STRONGER QUENCHED COMPONENT CERTIFICATE. The full Lyons–Pemantle–Peres speed-monotonicity conjecture remains open.

**Native role:** P03-B, `6aabe777361481919c9e614646464772`, regeneration/coupling, spine comparison and bounded-support counterexample/certificate role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`.

**Captured master before write:** `84e9590e61a598d9d276dc51a4e70b4630808f80`.

**Previous own checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T1620Z__escape-spine-score-isometry-and-elasticity-monotonicity.md`.

**Complementary P03-A checkpoint consumed, not duplicated:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T1559Z__mean-preserving-three-point-profile-and-mesoscopic-interior-order.md`. P03-A is developing recursive/analytic escape and speed identities, including a genuinely three-point mean-preserving family. This report stays on the quenched bounded-support spine/coupling side and only uses the inherited escape objects already present in P03-B.

---

## 1. Source normalization and bounded frontier check

The source problem is Gerard Ben Arous, Alexander Fribergh and Vladas Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865. Their `beta` is the **outward child bias**. At a non-root vertex with `k` children,

\[
P_\beta(x,x^*)=\frac1{1+\beta k},
\qquad
P_\beta(x,x_i)=\frac\beta{1+\beta k}.
\tag{1.1}
\]

The Galton-Watson tree has no leaves, `P(Z=0)=0`, and the conjecture asks that the speed increase throughout the transient interval `beta>1/EZ`. The old high-bias theorem is historical input, not the present frontier.

Bowditch--Tokushige, arXiv:1906.07913, prove differentiability in the ballistic/CLT regime and express the derivative through a two-dimensional Gaussian covariance; arXiv:2006.03433 proves analyticity in the ballistic regime. These are regularity tools, not the missing sign theorem.

The strongest broad later primary monotonicity result retained after the current bounded check is He Song, Longmin Wang and Kainan Xiang, *Journal of Applied Probability* 62 (2025), 1044--1052, DOI `10.1017/jpr.2024.113`. Their parameter `lambda` is reciprocal parent bias, `lambda=1/beta`; for minimum offspring `d>=2` they prove strict decrease for

\[
0\le \lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\tag{1.2}
\]

No inverse-parameter contradiction is inferred.

Useful source locators:

- https://arxiv.org/abs/1111.5865
- https://arxiv.org/abs/1906.07913
- https://arxiv.org/abs/2006.03433
- https://doi.org/10.1017/jpr.2024.113

---

## 2. Inherited escape-spine objects and the previous bottleneck

Fix a deterministic rooted tree satisfying

\[
d\le k_x\le D<\infty,
\qquad \beta d>1.
\tag{2.1}
\]

For a non-root vertex `x`, let

\[
h_x=P_\beta^x(T_{x^*}<\infty),
\qquad
t_x=1-h_x.
\tag{2.2}
\]

If `y` ranges over the children of `x`, set

\[
S_x=\sum_y t_y,
\qquad
\pi_x(y)=\frac{t_y}{S_x}.
\tag{2.3}
\]

The exact return recursion is

\[
h_x=\frac1{1+\beta S_x}.
\tag{2.4}
\]

Write the logarithmic derivative operator

\[
\mathcal D:=\beta\frac d{d\beta}
\tag{2.5}
\]

and define the escape elasticity

\[
g_x:=\mathcal D\log t_x
=-\frac{\beta h_x'}{1-h_x}.
\tag{2.6}
\]

The preceding P03-B reports proved the support bands

\[
\frac1{\beta D}\le h_x\le\frac1{\beta d},
\tag{2.7}
\]

\[
\frac1{\beta D-1}\le g_x\le\frac1{\beta d-1}.
\tag{2.8}
\]

They also proved a Green/spine representation and, by comparing the direct decrease of the return factors against terminal-child selection noise, obtained the sufficient condition

\[
4\kappa(x-1)^4>(\kappa-1)(\kappa x-1)^2,
\qquad
x=\beta d,
\quad
\kappa=D/d,
\tag{2.9}
\]

for `g_x'(beta)<0` on every such tree. For `[d,D]=[2,3]`, that condition begins at

\[
\beta>0.826892471630794\ldots.
\tag{2.10}
\]

The weakness in (2.9) is now identifiable: the direct term and branch-selection term were bounded separately over the entire future Green series. That discards an exact same-vertex cancellation. The present run keeps that cancellation before taking any support extrema.

---

## 3. Exact first-order recursion for the escape elasticity

Let

\[
\bar g_x:=E_{\pi_x}[g_y]
=\sum_y\pi_x(y)g_y.
\tag{3.1}
\]

Because

\[
t_x=\frac{\beta S_x}{1+\beta S_x},
\tag{3.2}
\]

we have

\[
\mathcal D\log S_x
=\sum_y\pi_x(y)\mathcal D\log t_y
=\bar g_x.
\tag{3.3}
\]

Differentiating (3.2) logarithmically gives the exact Bellman recursion

\[
\boxed{
 g_x=h_x(1+\bar g_x).
}
\tag{3.4}
\]

This is equivalent to the inherited Green representation, but it is better suited to a second derivative because it retains the local variance term exactly.

Also

\[
\mathcal D h_x=-t_x g_x.
\tag{3.5}
\]

Finally, since

\[
\mathcal D\log\pi_x(y)
=g_y-\bar g_x,
\tag{3.6}
\]

we have

\[
\mathcal D\bar g_x
=E_{\pi_x}[\mathcal D g_y]
+\operatorname{Var}_{\pi_x}(g_y).
\tag{3.7}
\]

Equations (3.4)--(3.7) contain the local cancellation that was lost in the previous global Gruss estimate.

---

## 4. New second-order recursion

Define

\[
u_x:=-\mathcal D g_x.
\tag{4.1}
\]

Thus `u_x>=0` is exactly the statement that `g_x` decreases as outward bias increases.

Differentiate (3.4), use (3.5) and (3.7), and write `m_x=bar g_x`. Then

\[
\begin{aligned}
\mathcal D g_x
&=(\mathcal D h_x)(1+m_x)
+h_x\mathcal D m_x\\
&=-t_xg_x(1+m_x)
+h_x\left(E_{\pi_x}[\mathcal D g_y]
+\operatorname{Var}_{\pi_x}(g_y)\right).
\end{aligned}
\tag{4.2}
\]

Since `g_x=h_x(1+m_x)`, this becomes

\[
\boxed{
 u_x
=h_x\left[
 t_x(1+m_x)^2
-\operatorname{Var}_{\pi_x}(g_y)
+E_{\pi_x}u_y
\right].
}
\tag{4.3}
\]

This is the key identity of the run. The adverse terminal-child selection contribution is exactly the variance term; it does not need to be bounded as a separate future covariance.

---

## 5. Variance absorption by a one-dimensional quadratic

Introduce

\[
x:=\beta d>1,
\qquad
\kappa:=\frac Dd\ge1.
\tag{5.1}
\]

From (2.7),

\[
t_x\ge c:=\frac{x-1}{x}.
\tag{5.2}
\]

From (2.8), every child elasticity lies in

\[
a\le g_y\le b,
\qquad
 a:=\frac1{\kappa x-1},
\qquad
 b:=\frac1{x-1}.
\tag{5.3}
\]

For `m=E_pi g_y`, Bhatia--Davis gives

\[
\operatorname{Var}_\pi(g_y)
\le (b-m)(m-a).
\tag{5.4}
\]

Therefore the local bracket in (4.3), apart from the child `u` term, is bounded below by

\[
F_{x,\kappa}(m)
:=c(1+m)^2-(b-m)(m-a).
\tag{5.5}
\]

Expanding,

\[
F_{x,\kappa}(m)
=(1+c)m^2+[2c-(a+b)]m+(c+ab).
\tag{5.6}
\]

Its leading coefficient is positive. A direct simplification of its discriminant gives

\[
\operatorname{disc}(F_{x,\kappa})
= -\frac{x\,P_\kappa(x)}
{(x-1)^2(\kappa x-1)^2},
\tag{5.7}
\]

where

\[
\boxed{
P_\kappa(x)
:=4\kappa^2x^3
-8\kappa^2x^2
+3\kappa^2x
-4\kappa x^2
+10\kappa x
-4\kappa
-x.
}
\tag{5.8}
\]

Hence

\[
P_\kappa(x)\ge0
\quad\Longrightarrow\quad
F_{x,\kappa}(m)\ge0
\quad\text{for every real }m.
\tag{5.9}
\]

This is stronger than checking only the actually attainable interval `[a,b]`, so no hidden realizability assumption enters the certificate.

When `P_kappa(x)>0`, the quadratic has the explicit uniform margin

\[
\boxed{
q_{x,\kappa}
:=\inf_mF_{x,\kappa}(m)
=
\frac{x^2P_\kappa(x)}
{4(2x-1)(x-1)^2(\kappa x-1)^2}
>0.
}
\tag{5.10}
\]

---

## 6. New quenched monotonicity theorem by a minimum principle

The second-order recursion now closes without the global branch-selection estimate.

### Theorem 6.1 — variance-absorption certificate

Fix `1<=d<=D<infinity` and a deterministic rooted tree with every non-root offspring count in `[d,D]`. Let `beta d>1`, put `x=beta d`, `kappa=D/d`, and let `g_x(beta)` be the escape elasticity (2.6).

If

\[
\boxed{P_\kappa(x)\ge0,}
\tag{6.1}
\]

then

\[
\boxed{g_v'(\beta)\le0}
\tag{6.2}
\]

at every non-root vertex `v`.

If `P_kappa(x)>0`, the inequality is strict at every vertex and admits the uniform logarithmic-derivative margin

\[
\boxed{
-\mathcal D g_v
\ge
\frac{x^2P_\kappa(x)}
{4(2x-1)(x-1)^2(\kappa x-1)^3}.
}
\tag{6.3}
\]

Equivalently,

\[
\boxed{
-g_v'(\beta)
\ge
\frac1\beta
\frac{x^2P_\kappa(x)}
{4(2x-1)(x-1)^2(\kappa x-1)^3}.
}
\tag{6.4}
\]

#### Proof

Under (6.1), (5.9) and (4.3) give

\[
u_v\ge h_vE_{\pi_v}u_y.
\tag{6.5}
\]

The inherited Green differentiation bounds imply that `u` is uniformly bounded on every compact bias interval contained in `beta d>1`; equivalently one can obtain the same bound by differentiating the absolutely convergent escape-spine Green series. Let

\[
M:=\inf_vu_v> -\infty.
\tag{6.6}
\]

If `M<0`, then because `h_v<=1/x<1`,

\[
u_v\ge h_vM\ge \frac1xM
\tag{6.7}
\]

for every `v` (the last inequality reverses in the useful direction because `M<0`). Taking the infimum gives

\[
M\ge \frac1xM,
\tag{6.8}
\]

which is impossible for `M<0` because `x>1`. Hence `M>=0`, proving (6.2).

If `P_kappa(x)>0`, (5.10) gives instead

\[
u_v\ge h_v(q_{x,\kappa}+E_{\pi_v}u_y).
\tag{6.9}
\]

We already know `M>=0`. Also `h_v>=1/(beta D)=1/(kappa x)`. Taking infima in (6.9),

\[
M\ge \frac1{\kappa x}(q_{x,\kappa}+M).
\tag{6.10}
\]

Therefore

\[
M\ge \frac{q_{x,\kappa}}{\kappa x-1},
\tag{6.11}
\]

which is exactly (6.3) after inserting (5.10). Since `D=beta d/d beta`, (6.4) follows. `square`

### What changed relative to the previous report

The previous certificate treated branch-selection movement as an external covariance and paid a full Gruss range at every future level. Theorem 6.1 instead differentiates the exact local Bellman equation once more. The branch-selection term then appears as `Var_pi(g)` and is absorbed by the positive direct term before any recursive propagation. This is the reason the threshold improves substantially.

---

## 7. Explicit `[2,3]` and `[3,4]` consequences

### 7.1 Offspring support `[2,3]`

Here

\[
\kappa=\frac32,
\qquad x=2\beta,
\]

and

\[
P_{3/2}(x)
=\frac14\left(36x^3-96x^2+83x-24\right).
\tag{7.1}
\]

The cubic has a unique real root above one,

\[
x_*=1.24458397617609\ldots.
\tag{7.2}
\]

Hence every deterministic tree whose offspring counts lie in `{2,3}` satisfies

\[
\boxed{
 g_v'(\beta)<0
 \quad\text{for every vertex whenever}\quad
 \beta>0.622291988088045\ldots .
}
\tag{7.3}
\]

The inherited global-Green certificate only gave

\[
\beta>0.826892471630794\ldots.
\tag{7.4}
\]

Thus the same quenched component theorem now reaches much closer to the natural descendant-contraction boundary `beta d>1`, which here is `beta>1/2`.

This is **not** a new speed-monotonicity interval. It proves monotonicity of the escape elasticity component on every `[2,3]` deterministic environment; the regeneration-time/displacement quotient and parent-side transport remain to be controlled.

### 7.2 Offspring support `[3,4]`

Here

\[
\kappa=\frac43,
\qquad x=3\beta,
\]

and, after multiplying by nine,

\[
9P_{4/3}(x)
=64x^3-176x^2+159x-48.
\tag{7.5}
\]

The relevant root is

\[
x_*=1.20361513840303\ldots,
\tag{7.6}
\]

so the new certificate is

\[
\boxed{
\beta>0.401205046134342\ldots .
}
\tag{7.7}
\]

The preceding report's coarse certificate simplified to `beta>1/2`, so this is again a strict improvement.

---

## 8. Near-regular asymptotics improve from the previous scale

Let

\[
\kappa=1+\varepsilon,
\qquad
x=1+\delta.
\tag{8.1}
\]

A direct exact expansion of (5.8) gives

\[
\boxed{
P_{1+\varepsilon}(1+\delta)
=
4(1+\varepsilon)^2\delta^3
+4\varepsilon(1+\varepsilon)\delta^2
-\varepsilon^2\delta
-\varepsilon^2.
}
\tag{8.2}
\]

Therefore the positive root nearest the contraction boundary satisfies

\[
\boxed{
\delta_*(\varepsilon)
=2^{-2/3}\varepsilon^{2/3}
+o(\varepsilon^{2/3})
\qquad(\varepsilon\downarrow0).
}
\tag{8.3}
\]

So for nearly regular support, the new component certificate approaches `beta d=1` at scale `(D/d-1)^{2/3}`. The improvement comes from variance absorption at the same vertex, not from a sharper estimate of the old future-covariance term.

For `kappa=1` exactly,

\[
P_1(x)=4(x-1)^3,
\tag{8.4}
\]

and Theorem 6.1 recovers the regular-tree fact for every `x>1`.

---

## 9. Local self-checks

The following checks were done before delivery.

1. **Recursion check.** Starting from `t=beta S/(1+beta S)`, direct logarithmic differentiation gives `g=h(1+bar g)`.
2. **Selection-score check.** `D log pi_y=g_y-bar g`, hence `D bar g=E Dg+Var(g)` with a **positive** variance sign. This sign is important; after moving to `u=-Dg`, the variance becomes the adverse term in (4.3).
3. **Quadratic check.** Expanding `c(1+m)^2-(b-m)(m-a)` gives (5.6), and its discriminant simplifies to (5.7).
4. **Regular-tree check.** At `kappa=1`, `P_1(x)=4(x-1)^3>0`; the exact regular value is `g=1/(x-1)`, which indeed decreases.
5. **Numerical root checks.** The `[2,3]` polynomial has root `1.24458397617609...`; the `[3,4]` polynomial has root `1.20361513840303...`.
6. **Claim-scope check.** No finite simulation is used to infer asymptotic speed monotonicity. The new theorem is quenched and all-dimensional, but only for the escape-elasticity component.

---

## 10. Remaining obstruction and next attack

### Previous obstruction

The preceding report had reduced descendant terminal-child information to a martingale/Fisher budget but still paid its effect against regeneration time/displacement as a separate covariance. Its direct-vs-selection sign theorem required the relatively conservative condition (2.9).

### New theorem/bound

The new exact recursion

\[
u_x=h_x\left[t_x(1+\bar g_x)^2-\operatorname{Var}_{\pi_x}(g)+E_{\pi_x}u_y\right]
\]

absorbs branch-selection variance locally. It yields the strictly stronger support-only certificate `P_kappa(beta d)>=0`, with explicit strict margin (6.3). For `[2,3]`, the threshold improves from `0.826892...` to `0.622291988...`; for `[3,4]`, from `0.5` to `0.401205046...`.

### Remaining obstruction

This still does **not** sign the derivative of the asymptotic speed. The missing pieces are now:

1. convert the quantitative escape-elasticity margin (6.3) into a positive contribution in the actual regeneration quotient `E Delta X / E Delta tau` rather than in the isolated harmonic escape kernel;
2. control parent-side selected-ancestor transport and the covariance of regeneration duration with the terminal escape environment;
3. in the gap `1/EZ<beta<=1/d`, descendant loop suppression itself is false in heterogeneous environments, as proved in the earlier P03-B loop-reversal report, so a different compensation mechanism is still required there.

### Next attack

Use (6.3) as a **margin**, not merely a sign. At a decisive outward escape, write the derivative of the conditioned regeneration-time transform as a local direct term plus the same `pi`-selection variance appearing in (4.3). The target is to prove that, for a nontrivial bounded-support family such as `{2,3}`, the regeneration-time covariance is bounded by a fixed fraction of the explicit margin

\[
\frac{x^2P_\kappa(x)}
{4(2x-1)(x-1)^2(\kappa x-1)^3}.
\]

The parent-side remainder can then be attached to the already proved common-spine/selected-ancestor geometric occupation bounds. If that quotient comparison fails even in `{2,3}`, the fallback is an exact finite-cylinder obstruction identifying which regeneration-time term defeats the local variance absorption.

---

## 11. Obligation ledger

- `R_full` — full LPP monotonicity over every no-leaf Galton-Watson law and every `beta>1/EZ`: **OPEN**.
- `R_escape2` — control the second beta derivative of the quenched escape elasticity under bounded support: **IMPROVED THIS RUN**; exact recursion (4.3) and support-only certificate (6.1) proved.
- `R_23` — obtain a nontrivial all-environment `[2,3]` component interval beyond the preceding Green/Gruss certificate: **PROVED PARTIAL**, now `beta>0.622291988088045...` for `g'<0`.
- `R_margin` — produce a positive explicit derivative margin usable by the regeneration quotient: **PROVED PARTIAL**, equation (6.3).
- `R_regquot` — dominate regeneration-time/displacement covariance by the positive harmonic margin: **OPEN; NEXT ATTACK**.
- `R_parent` — merge parent-side selected-ancestor transport with the descendant margin without double charging: **OPEN**.
- `R_criticalgap` — handle `1/EZ<beta<=1/d`, where return-loop suppression can reverse: **OPEN; requires compensation, not monotone-loop coupling**.

No audit-wait or admission loop was entered; the run was spent on the active mathematical bottleneck.