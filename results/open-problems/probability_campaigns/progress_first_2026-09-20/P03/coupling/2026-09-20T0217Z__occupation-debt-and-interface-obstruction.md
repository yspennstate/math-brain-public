Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.

# P03-B coupling report — occupation-debt representation and a source-valid negative local-response obstruction

**Status:** PROVED PARTIAL + RIGOROUS OBSTRUCTION TO A POINTWISE-SIGN MECHANISM. The full Lyons–Pemantle–Peres speed-monotonicity conjecture remains open here. This run does not repeat an already-known high-bias theorem and does not claim asymptotic monotonicity from a finite computation.

**Native role:** P03-B, `6aabe777361481919c9e614646464772`, probabilistic regeneration/coupling and counterexample-search role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`.

**Captured master immediately before write:** `e1137b3bf9e7094d8bdf21727151366f043e0980`.

**Previous own checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T010909Z__sharp-regeneration-bound-and-score-response.md`.

**Latest complementary P03-A checkpoint consumed only to avoid duplication:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0207Z__gini-covariance-and-three-degree-extension.md`. P03-A handles recursive/effective-degree analytic identities and now has a Gini-covariance sharpening plus a three-degree extension. I do not reproduce those calculations.

## 1. Minimal source continuity and convention

The primary source is Gérard Ben Arous, Alexander Fribergh and Vladas Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865:

https://arxiv.org/abs/1111.5865

The source assumes a Galton–Watson offspring variable `Z` with

\[
\mathbf P(Z=0)=0,
\]

and defines the **outward child-bias** parameter `beta` by, at a non-root vertex with `k` children,

\[
P_\beta(x,x^*)=\frac{1}{1+\beta k},
\qquad
P_\beta(x,x_i)=\frac{\beta}{1+\beta k}.
\tag{1.1}
\]

The walk is transient for `beta>1/E Z`, and the Lyons–Pemantle–Peres conjecture asks that the speed `v(beta)` increase on that whole transient interval. The old arXiv posting states the high-bias constants `717` and `717/d`; those are historical source values, not the strongest present range.

The current primary differentiability reference requested by the owner is Adam Bowditch and Yuki Tokushige, *Differentiability of the speed of biased random walks on Galton-Watson trees*, arXiv:1906.07913:

https://arxiv.org/abs/1906.07913

They prove differentiability where the walk is ballistic and satisfies the relevant CLT, with the derivative expressed through a two-dimensional Gaussian covariance; their later arXiv:2006.03433 proves analyticity in the ballistic regime. These regularity results do not determine the derivative sign.

The strongest source-uniform later monotonicity theorem currently used in this campaign is He Song, Longmin Wang and Kainan Xiang, *Journal of Applied Probability* 62 (2025), DOI `10.1017/jpr.2024.113`. In their reciprocal **parent-bias** convention `lambda=1/beta`, if the minimum offspring is `d>=2`, the speed is strictly decreasing for

\[
0\le \lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\tag{1.2}
\]

This is consistent with increasing speed in outward `beta`. Nothing below treats an inverse parametrization as a contradiction.

The full-source metric therefore remains

`R_full: 1 -> 1`.

The point of this run is instead to sharpen the probabilistic location of possible negative derivative contributions.

## 2. Inherited finite-horizon score-response identity

The previous P03-B run proved the following exact finite-horizon identity on a fixed locally finite rooted tree. At a non-root decision time `t`, let `K_t` be the current number of children and let

\[
m_k(\beta)=\frac{\beta k-1}{\beta k+1}
\tag{2.1}
\]

be the conditional radial drift at a `k`-child vertex. If

\[
F_{t,n}^{\pm}
=E_\beta\!\left[
\sum_{s=t+1}^{n}\xi_s
\,\middle|\,
\mathcal F_{t-1},\xi_t=\pm1
\right],
\]

then

\[
\frac d{d\beta}E_\beta|X_n|
=
E_\beta\sum_{t:X_{t-1}\ne o}
\frac{K_t}{(1+\beta K_t)^2}
\left(2+F_{t,n}^{+}-F_{t,n}^{-}\right).
\tag{2.2}
\]

The coefficient is always positive. The unresolved object is therefore the response bracket

\[
R_{t,n}:=2+F_{t,n}^{+}-F_{t,n}^{-}.
\tag{2.3}
\]

The preceding report only observed that a negative score contribution requires `R_{t,n}<0`. This run gives an exact occupation representation and then shows, by a source-valid finite cylinder, that pointwise nonnegativity of `R_{t,n}` is false.

## 3. New theorem: occupation-debt representation

Fix a decision vertex `x` at depth `ell`, its parent `a=x^*`, and one child `b` of `x`. Let

\[
r:=n-t
\]

be the number of steps remaining **after** the current `+/-` decision. Assume for the moment that every vertex reachable from `a` or `b` in at most `r` steps is non-root and has offspring in

\[
d\le K\le D.
\tag{3.1}
\]

This condition is automatic if `d<=Z<=D` globally and the decision is farther than `r` from the root.

For a starting vertex `y`, define the expected degree occupation measure up to horizon `r` by

\[
\mu_y^{(r)}(k)
:=
\sum_{j=0}^{r-1}
P_y\{K(X_j)=k\},
\qquad d\le k\le D.
\tag{3.2}
\]

Each occupation measure has total mass `r`.

### Theorem 3.1 — exact occupation-debt identity

With the notation above,

\[
\boxed{
R_{t,n}
=
2+\sum_{k=d}^{D}m_k(\beta)
\left(\mu_b^{(r)}(k)-\mu_a^{(r)}(k)\right).
}
\tag{3.3}
\]

Equivalently, because the signed occupation difference has total mass zero,

\[
\boxed{
R_{t,n}
=
2-
\sum_{k=d}^{D}
\bigl(m_k(\beta)-m_d(\beta)\bigr)
\left(\mu_a^{(r)}(k)-\mu_b^{(r)}(k)\right).
}
\tag{3.4}
\]

Hence the response debt

\[
D_{t,n}:=[-R_{t,n}]_+
=[F_{t,n}^{-}-F_{t,n}^{+}-2]_+
\tag{3.5}
\]

is exactly the amount by which the inward-start future accumulates more **degree-weighted radial drift occupation** than the outward-start future beyond the initial two-level deficit.

#### Proof

Let

\[
V_r(y)=E_y|X_r|.
\]

After the current step, the `+` branch starts from `b` at depth `ell+1`, whereas the `-` branch starts from `a` at depth `ell-1`. Therefore

\[
F_{t,n}^{+}=V_r(b)-|b|,
\qquad
F_{t,n}^{-}=V_r(a)-|a|,
\]

and since `|b|-|a|=2`,

\[
R_{t,n}=V_r(b)-V_r(a).
\tag{3.6}
\]

Away from the root, the conditional expected radial increment at a `k`-child vertex is exactly `m_k(beta)`. The Doob decomposition of radial distance thus gives

\[
V_r(y)
=
|y|+
\sum_{j=0}^{r-1}E_y m_{K(X_j)}(\beta).
\tag{3.7}
\]

Subtract (3.7) for `y=a` from the same formula for `y=b` and group terms by offspring value `k`. This gives (3.3). Since

\[
\sum_k\mu_a^{(r)}(k)
=
\sum_k\mu_b^{(r)}(k)=r,
\]

subtracting the common baseline `m_d(beta)` yields (3.4). QED.

### Interpretation

This is a useful change of object. A negative derivative contribution is not an opaque future-value phenomenon: it requires the parent-start process to accumulate, over the remaining horizon, more occupation of high-radial-drift degrees than the child-start process by enough to erase an initial radial advantage of exactly two.

That distinction is complementary to P03-A. P03-A controls the bias derivative through recursive escape/effective-degree identities. Here the derivative's bad part is rewritten as a discrepancy between two future **degree occupation measures**.

## 4. New coupling bound: negative debt is charged to degree mismatch

Set

\[
\Delta_{d,D}(\beta)
:=m_D(\beta)-m_d(\beta)
=
\frac{2\beta(D-d)}{(1+\beta d)(1+\beta D)}.
\tag{4.1}
\]

Because `m_k` is increasing in `k`, equation (3.4) immediately yields a total-variation control.

### Corollary 4.1 — occupation-TV debt bound

Let

\[
\|\mu_a^{(r)}-\mu_b^{(r)}\|_{TV}
:=
\frac12\sum_{k=d}^{D}
\left|\mu_a^{(r)}(k)-\mu_b^{(r)}(k)\right|.
\tag{4.2}
\]

Then

\[
\boxed{
D_{t,n}
\le
\left[
\Delta_{d,D}(\beta)
\|\mu_a^{(r)}-\mu_b^{(r)}\|_{TV}
-2
\right]_+.
}
\tag{4.3}
\]

Since each occupation measure has total mass `r`, its total-variation difference is at most `r`. Therefore

\[
\boxed{
D_{t,n}
\le
[r\Delta_{d,D}(\beta)-2]_+.
}
\tag{4.4}
\]

In particular,

\[
\boxed{
R_{t,n}\ge0
\quad\text{whenever}\quad
r\Delta_{d,D}(\beta)\le2.
}
\tag{4.5}
\]

Thus a negative local derivative contribution has a deterministic **latency requirement**:

\[
r>
\frac{2}{\Delta_{d,D}(\beta)}
=
\frac{(1+\beta d)(1+\beta D)}{\beta(D-d)}.
\tag{4.6}
\]

#### Proof

Let

\[
\eta(k)=\mu_a^{(r)}(k)-\mu_b^{(r)}(k),
\qquad
w_k=m_k-m_d\in[0,\Delta_{d,D}].
\]

Because `sum_k eta(k)=0`, the positive and negative masses of `eta` agree and equal the total variation in (4.2). Hence

\[
\sum_k w_k\eta(k)
\le
\Delta_{d,D}\sum_{\eta(k)>0}\eta(k)
=
\Delta_{d,D}\|\mu_a^{(r)}-\mu_b^{(r)}\|_{TV}.
\]

Combine this with (3.4) and the definition of `D_{t,n}`. QED.

The same statement has a more coupling-oriented form. Let `(Y_j^-,Y_j^+)`, `0<=j<r`, be **any** coupling of the two future paths started from `a` and `b`, with the correct marginals. Define

\[
c_\beta(i,j)
:=
[m_i(\beta)-m_j(\beta)]_+
=
\left[
\frac{2\beta(i-j)}{(1+\beta i)(1+\beta j)}
\right]_+.
\tag{4.7}
\]

For each `j`,

\[
E_a m_{K(X_j)}-E_b m_{K(X_j)}
\le
E\,c_\beta(K(Y_j^-),K(Y_j^+)).
\]

Therefore

\[
\boxed{
D_{t,n}
\le
\left[
\sum_{j=0}^{r-1}
E\,c_\beta(K(Y_j^-),K(Y_j^+))
-2
\right]_+.
}
\tag{4.8}
\]

This is the probabilistic target I wanted: one does **not** need to dominate positions pathwise. It is enough to couple the two futures so that their cumulative positive degree-drift mismatch costs less than two on average.

A cruder but often convenient consequence is

\[
D_{t,n}
\le
\left[
\Delta_{d,D}(\beta)
\sum_{j=0}^{r-1}
P\{K(Y_j^-)\ne K(Y_j^+)\}
-2
\right]_+.
\tag{4.9}
\]

This turns the derivative-sign problem into a coupling occupation problem instead of the impossible universal radial-ordering problem ruled out in the first P03-B run.

## 5. Rigorous source-valid obstruction: the response bracket can actually be negative

A natural hope after (2.2) would be to prove every response bracket `R_{t,n}` nonnegative. That route is false, even in a bounded-support, no-leaf family well inside the transient regime.

Take

\[
P(Z=2)=P(Z=6)=\frac12,
\qquad
\beta=\frac35.
\tag{5.1}
\]

Then `E Z=4`, so `beta=3/5>1/EZ=1/4`; the source walk is transient. The support is bounded and has no leaves.

Consider a vertex `x` sufficiently far from the root, its parent `a`, and one child `b`. In the finite radius-six neighborhood relevant to the calculation below, impose the following offspring cylinder:

* every vertex in the descendant subtree rooted at `x` has offspring `2`;
* every vertex outside that descendant subtree has offspring `6`.

Only finitely many offspring variables are specified, so under the iid `{2,6}` Galton–Watson law this cylinder has strictly positive probability. It is enough that `a` be more than six levels above the root boundary so that the root cannot be reached during the six-step comparison.

On this cylinder, both children of `x` have the same low-degree local environment, so the `+` branch average in (2.2) equals the value from the chosen child `b`.

Define the exact finite-horizon dynamic program

\[
H_0(z)=|z|,
\]

\[
H_{s+1}(z)
=
\frac{1}{1+\beta\nu(z)}H_s(z^*)
+
\frac{\beta}{1+\beta\nu(z)}
\sum_{c\text{ child of }z}H_s(c).
\tag{5.2}
\]

This is simply `H_s(z)=E_z|X_s|`. Because `beta=3/5` and all local degrees are integers, every value in (5.2) is rational. Exact iteration on the finite radius-six cylinder gives

\[
H_5(b)-H_5(a)
=
\frac{5829895342}{45068672891}
>0,
\tag{5.3}
\]

but at the next horizon

\[
\boxed{
H_6(b)-H_6(a)
=
-\frac{4151554886882}{23841327959339}
<0.
}
\tag{5.4}
\]

Numerically the latter is about `-0.1741327032605906`, but the sign claim is the exact rational inequality (5.4), not a simulation.

By (3.6), a score-response term with six steps remaining therefore satisfies

\[
R_{t,n}<0
\]

on this positive-probability source-valid cylinder. Since the current vertex has `K_t=2`, the susceptibility coefficient in (2.2) is

\[
\frac{2}{(1+2\beta)^2}
=
\frac{50}{121}>0.
\]

The corresponding conditional local derivative contribution is exactly

\[
\frac{50}{121}
\left(-\frac{4151554886882}{23841327959339}\right)
=
-\frac{207577744344100}{2884800683080019}
<0.
\tag{5.5}
\]

### What this obstruction does and does not prove

It proves:

1. **Pointwise sign is impossible.** One cannot prove the full conjecture by showing every finite-horizon response bracket in (2.2) is nonnegative.
2. **Cancellation is genuinely necessary.** Even for a no-leaf bounded-support source family in the transient regime, some histories/local environments contribute negatively to the bias derivative.
3. **Degree-selection matters.** The negative bracket is generated by an interface where the inward start sees a high-degree region and the outward start sees a low-degree region; the initial two-level outward advantage can be erased by accumulated future drift occupation.

It does **not** prove:

* negative asymptotic speed derivative;
* failure of the Lyons–Pemantle–Peres conjecture;
* that all negative contribution occurs before the first revisit of the decision edge;
* that this cylinder dominates after annealed averaging.

In fact, the known/source-restricted positive theorems make clear that local negative terms must be outweighed globally in many regimes. The point is to identify the exact compensation that a successful proof must control.

## 6. Comparison with the latency bound

For the obstruction parameters `d=2,D=6,beta=3/5`,

\[
m_2=\frac1{11},
\qquad
m_6=\frac{13}{23},
\]

so

\[
\Delta_{2,6}(3/5)
=
\frac{13}{23}-\frac1{11}
=
\frac{120}{253}.
\tag{6.1}
\]

Corollary 4.1 says negative response is impossible whenever

\[
r\frac{120}{253}\le2,
\]

that is for every integer `r<=4`. The exact interface calculation stays positive also at `r=5` and first turns negative at `r=6` for this cylinder. Thus the universal latency bound is conservative by only one step in this explicit example; it is not vacuous.

This also gives a concrete test for future coupling ideas. Any proposed coupling bound that claims nonnegative local response for this cylinder through six steps must be wrong, because it would contradict the exact rational certificate (5.4).

## 7. What changed this run

The full source remains unresolved:

`R_full: 1 -> 1`.

The intermediate obligation ledger moved materially:

* `C1` source assumptions and outward/inward bias normalization: DONE and unchanged.
* `C2` universal pathwise radial domination: already RIGOROUSLY OBSTRUCTED in the first P03-B run.
* `C3` super-regeneration deterministic length control: corrected previously to the sharp `tau<=4B+1`.
* `C4` finite-horizon score-response identity: inherited and retained.
* `C5` **NEW PROVED PARTIAL:** exact occupation-debt identity (3.3)–(3.5).
* `C6` **NEW PROVED PARTIAL:** total-variation and arbitrary-coupling mismatch bounds (4.3), (4.8), with the explicit latency threshold (4.6).
* `C7` **NEW RIGOROUS OBSTRUCTION:** pointwise nonnegativity of every response bracket is false, witnessed exactly by the `{2,6}`, `beta=3/5`, six-step cylinder (5.4).
* `C8` global annealed control of the occupation mismatch / derivative sign: OPEN.

This is not a stagnation run. It replaces an amorphous future-response term by an explicit occupation measure discrepancy and supplies a hard counterexample that rules out one tempting proof mechanism.

## 8. Remaining obstruction and next attack

Equation (4.8) suggests the next genuinely probabilistic step. At a decision time, couple the inward-start and outward-start futures and split the cumulative mismatch cost into two pieces:

\[
\sum_j c_\beta(K_j^-,K_j^+)
=
\text{fresh-selection mismatch}
+
\text{revisit/history mismatch}.
\tag{8.1}
\]

The exact interface obstruction shows that the first term cannot simply be discarded: a fresh low-degree branch facing a previously selected high-degree parent region can accumulate real negative debt. What should still be possible is an **annealed compensation lemma**: under the regeneration/spine law, bound the expected positive occupation imbalance of the parent-start future by a one-step size/visit-bias term plus a geometrically decaying return kernel.

A precise next target is therefore to prove, for bounded support `d<=Z<=D`, a regeneration-block inequality of the form

\[
E\left[
\sum_j c_\beta(K_j^-,K_j^+)
\,\middle|\,\mathcal F_{t-1}
\right]
\le
A_\beta(K_t,\text{parent history})
+
\sum_{s\ge1}r_\beta^s B_s,
\tag{8.2}
\]

where the first term is an explicit spine/selection correction and `r_beta<1` comes from an actual return probability, not from the obsolete pointwise-ordering idea. The objective is then to average (8.2) under the regeneration law and compare the result with the fixed budget `2` in (4.8).

A useful complementary handoff to P03-A is the exact message:

> the analytic covariance term has a probabilistic interpretation as a future degree-occupation imbalance; a local sign proof cannot work, because `{2,6}` at outward `beta=3/5` already has an exact negative six-step score bracket. Any analytic bound that succeeds globally must exploit cancellation under the tilted/spine law rather than pointwise positivity.

No finite simulation is being promoted to an asymptotic theorem. The only finite computation used here is an exact rational certificate for a local mechanism obstruction, while the new occupation and coupling bounds are proved for arbitrary finite horizons under the stated bounded-support/root-avoidance hypotheses.
