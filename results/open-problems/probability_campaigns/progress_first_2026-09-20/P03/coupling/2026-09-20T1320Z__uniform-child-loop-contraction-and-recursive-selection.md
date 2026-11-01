Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum reasoning was requested as a preference, but no authenticated runtime telemetry establishes that setting.

# P03-B coupling report — uniform child-loop contraction and recursive subtree-selection bound

**Status:** PROVED PARTIAL / NEW QUENCHED RETURN LEMMA / NEW POSTERIOR-TRANSPORT REDUCTION. The full Lyons–Pemantle–Peres speed-monotonicity conjecture remains open.

**Native role:** P03-B, `6aabe777361481919c9e614646464772`, regeneration/coupling, spine comparison and source-valid counterexample role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`.

**Captured master immediately before write:** `8487f4954b27e51eeb997b2c2c6746756f2f600e`.

**Previous own checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T1215Z__two-sided-return-elasticity-and-fresh-child-charge.md`.

**Complementary P03-A checkpoint consumed, not duplicated:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T1158Z__explicit-two-coordinate-terminal-strip-for-balanced-one-two-three-law.md`. P03-A is developing recursive escape/speed identities, especially minimum-offspring-one terminal strips. This report stays on the probabilistic excursion/revisit ledger for minimum offspring `d>=2`.

---

## 1. Source normalization and current benchmark

Primary source: G. Ben Arous, A. Fribergh and V. Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865. Their parameter `beta` is the **outward child bias**. At a non-root vertex with `k` children,

\[
q_k(\beta):=P_\beta(\text{parent}\mid k)=\frac1{1+\beta k},
\qquad
P_\beta(\text{a specified child}\mid k)=\frac\beta{1+\beta k}.
\tag{1.1}
\]

The offspring law has `P(Z=0)=0`; increasing `beta` means stronger outward bias. The LPP conjecture asks that the asymptotic speed be increasing throughout the source transient interval `beta>1/EZ`.

Bowditch–Tokushige, arXiv:1906.07913, prove differentiability in the ballistic/CLT regime and identify the derivative through a two-dimensional Gaussian covariance; arXiv:2006.03433 strengthens regularity to analyticity in the ballistic regime. These are regularity/covariance tools, not a sign theorem.

The strongest broad later primary monotonicity result retained by the bounded source check on 20 September 2026 is He Song, Longmin Wang and Kainan Xiang, *The speed of a biased walk on a Galton–Watson tree without leaves is monotonic for low values of bias*, J. Appl. Probab. 62 (2025), 1044–1052. Their parameter is reciprocal parent bias `lambda=1/beta`; for minimum offspring `d>=2` they prove strict decrease for

\[
0\le \lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\tag{1.2}
\]

No inverse-parametrization contradiction is inferred.

For the new statements below fix a deterministic rooted tree in which every non-root vertex has at least `d>=2` children and assume

\[
\beta d>1.
\tag{1.3}
\]

Every Galton–Watson environment with offspring support in `[d,D]` satisfies these quenched hypotheses almost surely.

---

## 2. Inherited bottleneck

The preceding P03-B run proved a two-sided elasticity estimate for the probability

\[
h_x(\beta)=P_\beta^x(T_{x^*}<\infty)
\]

that a walk started at a child `x` ever returns to its parent. It then priced the adverse **first** return following discovery of a fresh child. That still left a serious concern: a walk may make many returning excursions through already discovered children, and a naive iteration of first-return bounds risks both double counting and an artificial geometric loss.

The key question for this run is therefore:

> Can the entire physical stack of returning descendant excursions be shown to move in the favorable direction, leaving only posterior-selection and parent-side terms as possible negative debt?

The answer is yes on the whole region `beta d>1`, with no high-bias constant and no upper-support assumption.

---

## 3. New strengthened return-elasticity lemma

Let `x` be a non-root vertex with children `x_1,...,x_k`, where `k>=d`. Put

\[
h_x(\beta)=P_\beta^x(T_{x^*}<\infty).
\]

The exact first-step recursion is

\[
\boxed{
 h_x=\frac1{1+\beta S_x},
 \qquad
 S_x:=\sum_{i=1}^k(1-h_{x_i}).
}
\tag{3.1}
\]

The earlier report controlled the derivative of the **odds** `h/(1-h)`. The following logarithmic estimate is different and is the useful quantity for a child excursion started from the parent.

### Theorem 3.1 — uniform logarithmic return contraction

For every `beta d>1`, in the Dini-derivative sense and hence at every differentiability point,

\[
\boxed{
-\beta\,\frac{d}{d\beta}\log h_x(\beta)
\ge
\frac{\beta d}{1+\beta d}.
}
\tag{3.2}
\]

Equivalently, for every `beta_2>beta_1>1/d`,

\[
\boxed{
\frac{h_x(\beta_2)}{h_x(\beta_1)}
\le
\frac{1+\beta_1d}{1+\beta_2d}.
}
\tag{3.3}
\]

This is uniform over all deterministic trees with minimum offspring `d`.

### Proof

First kill the walk when it reaches descendant depth `N` below `x`; write `h_x^{(N)}` for the probability of hitting `x^*` before that boundary. The recursion (3.1) remains exact with the corresponding truncated child-return probabilities.

Define

\[
a_y:=-\beta\frac{\partial_\beta h_y^{(N)}}{h_y^{(N)}}
\]

for vertices above the killed boundary, and put

\[
\xi:=\beta d,
\qquad
 a_0:=\frac\xi{1+\xi}.
\tag{3.4}
\]

At the last nonabsorbing level all child-return probabilities are zero. If that vertex has `k>=d` children, then

\[
h_y^{(N)}=\frac1{1+\beta k},
\qquad
 a_y=\frac{\beta k}{1+\beta k}\ge a_0.
\]

Assume inductively that every child `y_i` obeys `a_{y_i}>=a_0`. From (3.1), with

\[
S=\sum_i(1-h_{y_i}),
\]

one gets

\[
a_y
=
\frac{\beta\left(S+\sum_i a_{y_i}h_{y_i}\right)}{1+\beta S}.
\tag{3.5}
\]

Because `a_{y_i}>=a_0`,

\[
S+\sum_i a_{y_i}h_{y_i}
\ge
S+a_0\sum_i h_{y_i}
=
\frac{\xi k+S}{1+\xi}.
\tag{3.6}
\]

Therefore `a_y>=a_0` follows once

\[
\xi k+S\ge d+\xi S.
\tag{3.7}
\]

But `0<=S<=k` and `xi>1`, so

\[
\xi k-d-(\xi-1)S
\ge
\xi k-d-(\xi-1)k
=k-d\ge0.
\tag{3.8}
\]

This completes the backward induction. Thus every finite killed truncation satisfies

\[
\partial_\beta\log h_x^{(N)}
\le
-\frac{d}{1+\beta d}.
\]

Integrating from `beta_1` to `beta_2` gives

\[
\frac{h_x^{(N)}(\beta_2)}{h_x^{(N)}(\beta_1)}
\le
\frac{1+\beta_1d}{1+\beta_2d}.
\]

As `N` increases, the killed hitting probabilities increase to the infinite-tree hitting probability, so the same finite comparison survives in the limit. This proves (3.3); (3.2) follows by taking one-sided derivatives. `square`

### Why this is stronger than the inherited bound for the present purpose

The preceding odds estimate alone yields

\[
-\beta h_x'/h_x\ge 1-h_x,
\]

which can be arbitrarily small as `beta d downarrow 1`. The new bound instead gives

\[
-\beta h_x'/h_x\ge \frac{\beta d}{1+\beta d}>\frac12.
\]

That extra factor is exactly what is needed to beat the increasing probability of choosing a child when the outward bias rises.

---

## 4. Uniform contraction of every returning child-excursion kernel

Fix a non-root vertex `v` with `k>=d` children and a particular child `u`. Define the quenched probability that a visit to `v` is followed by a step to `u` **and that the resulting excursion returns to `v`**:

\[
\ell_{v,u}(\beta)
:=
\frac{\beta}{1+\beta k}\,h_u(\beta).
\tag{4.1}
\]

### Theorem 4.1 — child-loop kernel contracts on the entire region `beta d>1`

For `beta_2>beta_1>1/d`,

\[
\boxed{
\frac{\ell_{v,u}(\beta_2)}{\ell_{v,u}(\beta_1)}
\le
R_d(\beta_1,\beta_2)
:=
\frac{\beta_2}{\beta_1}
\left(\frac{1+\beta_1d}{1+\beta_2d}\right)^2
<1.
}
\tag{4.2}
\]

At differentiability points this implies the explicit logarithmic margin

\[
\boxed{
-\beta\frac d{d\beta}\log\ell_{v,u}(\beta)
\ge
c_d(\beta)
:=
\frac{\beta d-1}{\beta d+1}>0.
}
\tag{4.3}
\]

### Proof

By (3.3),

\[
\frac{h_u(\beta_2)}{h_u(\beta_1)}
\le
\frac{1+\beta_1d}{1+\beta_2d}.
\]

Hence

\[
\frac{\ell_{v,u}(\beta_2)}{\ell_{v,u}(\beta_1)}
\le
\frac{\beta_2}{\beta_1}
\frac{1+\beta_1k}{1+\beta_2k}
\frac{1+\beta_1d}{1+\beta_2d}.
\tag{4.4}
\]

For fixed `beta_2>beta_1`, the ratio `(1+beta_1 k)/(1+beta_2 k)` decreases with `k`; since `k>=d`, replacing `k` by `d` proves the first inequality in (4.2).

Writing `x_i=beta_i d`, the assertion `R_d<1` is equivalent to

\[
x_1(1+x_2)^2-x_2(1+x_1)^2
=(x_2-x_1)(x_1x_2-1)>0,
\]

which follows from `x_2>x_1>1`.

Taking `beta_2 downarrow beta_1` gives (4.3). Equivalently, directly combine

\[
-\beta h_u'/h_u\ge\frac{\beta d}{1+\beta d}
\]

with

\[
\beta\frac d{d\beta}\log\frac{\beta}{1+\beta k}
=\frac1{1+\beta k}
\le\frac1{1+\beta d}.
\]

`square`

This removes a false intermediate threshold. A crude use of the old odds bound suggested that returning child excursions were only uniformly decreasing once `beta d` exceeded the golden ratio. The strengthened logarithmic lemma shows that **no such threshold exists**: every returning child-excursion kernel is already strictly decreasing for the whole region `beta d>1`.

---

## 5. Entire stacks of returning descendant excursions

Let `A` be any fixed subset of the children of `v` and set

\[
L_A(\beta):=\sum_{u\in A}\ell_{v,u}(\beta).
\tag{5.1}
\]

By (4.2), termwise,

\[
\boxed{
L_A(\beta_2)\le R_d(\beta_1,\beta_2)L_A(\beta_1).
}
\tag{5.2}
\]

At a visit to `v`, a returning excursion through a child in `A` resets the walk at `v` with the same fixed environment. Therefore the number `C_A` of consecutive returning `A`-child excursions before the first departure that is not of this type is geometric:

\[
P(C_A\ge n\mid T)=L_A^n,
\qquad
E[C_A\mid T]=G_A:=\frac{L_A}{1-L_A}.
\tag{5.3}
\]

Since `x/(1-x)` is increasing and `R_d<1`, (5.2) yields

\[
\boxed{
G_A(\beta_2)
\le
R_d(\beta_1,\beta_2)\,G_A(\beta_1).
}
\tag{5.4}
\]

Indeed,

\[
\frac{R L}{1-RL}<R\frac{L}{1-L}
\]

for `0<R<1` and `0<L<1`.

The earlier universal return bound `h_u<=1/(beta d)` also gives

\[
L_A\le L_{\rm all}
\le\frac1{\beta d},
\qquad
\boxed{
G_A\le\frac1{\beta d-1}.
}
\tag{5.5}
\]

Thus **the complete quenched stack of returning descendant excursions is monotone decreasing with outward bias**, not merely its first-return probability.

For the near-critical test used repeatedly in P03-B, `d=2`, `beta=3/5`, the logarithmic margin is already

\[
c_d=\frac{6/5-1}{6/5+1}=\frac1{11}.
\tag{5.6}
\]

For example, moving from `beta=0.60` to `0.61`, (4.2) gives the uniform factor

\[
R_2(0.60,0.61)\approx0.9984308633<1.
\]

The effect is small near `beta d=1`, but its sign is rigorous and source-uniform.

---

## 6. Exact posterior transport split at a historical vertex

Now return to the annealed Galton–Watson path filtration. At a historical vertex `v`, let

\[
Q_v=(1+\beta Z_v)^{-1}
\]

have current posterior mean `M` and variance `V`, and suppose exactly `c` children have already been discovered. Put

\[
\alpha_c=1+\beta c.
\]

The next departure categories have probabilities

\[
P(\text{parent})=M,
\qquad
P(\text{specified known child }i)=\beta M,
\qquad
P(\text{new child})=1-\alpha_cM.
\tag{6.1}
\]

As established in the earlier local-history report, the posterior mean innovations are

\[
\Delta M_R=\frac VM
\tag{6.2}
\]

for a parent or known-child reuse, and

\[
\Delta M_N=-\frac{\alpha_cV}{1-\alpha_cM}
\tag{6.3}
\]

for discovery of a new child.

Hence the probability-times-innovation coefficients are exactly

\[
\boxed{
M\Delta M_R=V,
\qquad
\beta M\Delta M_R=\beta V,
\qquad
(1-\alpha_cM)\Delta M_N=-\alpha_cV.
}
\tag{6.4}
\]

This has an important interpretation for the revisit-score ledger:

- a parent departure carries positive coefficient `V`;
- a known-child departure carries positive coefficient `beta V`;
- a first discovery carries negative coefficient `-alpha_c V`.

Therefore a future return probability that **decreases** with `beta` is favorable after a known-child reuse but adverse after the first discovery of that child. This algebra explains why the fresh-child first-return debt found in the preceding report is genuinely one-shot.

---

## 7. Known-child first-return debt descends recursively into subtree Fisher information

Fix one already known child `u`. Let `Pi_u^beta` be the current posterior law of the environment in the subtree rooted at `u`, based only on the history already observed in that subtree. Conditional posterior factorization of the Galton–Watson environment makes this subtree posterior independent of `Q_v` once the canonical path history is fixed.

For a sampled subtree environment `T_u`, write

\[
h(T_u,\beta)=P_\beta^u(T_v<\infty)
\]

and define

\[
H_u(\beta):=E_{\Pi_u^\beta}[h(T_u,\beta)].
\tag{7.1}
\]

Let

\[
L_u:=\partial_\beta\log\frac{d\Pi_u^\beta}{d\Pi_u^{\beta_0}}
\]

be the centered posterior score at the current parameter, and let

\[
I_u:=E_{\Pi_u^\beta}[L_u^2]
\]

be its Fisher information. Differentiating (7.1) gives the exact physical-plus-selection split

\[
\boxed{
H_u'
=E_{\Pi_u}[\partial_\beta h]
+\operatorname{Cov}_{\Pi_u}(h,L_u).
}
\tag{7.2}
\]

Theorem 3.1 gives, pointwise in the subtree environment,

\[
\partial_\beta h
\le
-\frac{d}{1+\beta d}\,h.
\tag{7.3}
\]

Also `0<=h<=r:=1/(beta d)`, so

\[
\operatorname{Var}_{\Pi_u}(h)\le\frac{r^2}{4}.
\tag{7.4}
\]

Cauchy–Schwarz in (7.2) therefore gives

\[
\boxed{
H_u'
\le
-\frac{d}{1+\beta d}H_u
+\frac{r}{2}\sqrt{I_u}.
}
\tag{7.5}
\]

Multiplying by the exact known-child transport coefficient `beta V` from (6.4) yields

\[
\boxed{
\beta V H_u'
\le
-\frac{\beta d}{1+\beta d}\,V H_u
+\frac{V}{2d}\sqrt{I_u}.
}
\tag{7.6}
\]

This is the new recursive selection bound.

The first term is strictly favorable. The **only** way an already known child can create adverse first-return transport is through the second term, namely score already stored in that child's posterior history. There is no independent adverse physical-return term.

Summing over the `c` known children gives

\[
\boxed{
\beta V\sum_{i=1}^c H_i'
\le
-\frac{\beta d}{1+\beta d}V\sum_{i=1}^cH_i
+\frac{V}{2d}\sqrt{c\sum_{i=1}^c I_i}.
}
\tag{7.7}
\]

For bounded support `Z<=D`, this is at most

\[
-\frac{\beta d}{1+\beta d}V\sum_iH_i
+\frac{V\sqrt D}{2d}\sqrt{\sum_i I_i}.
\tag{7.8}
\]

Equation (7.7) is useful because it replaces an uncontrolled continuation-value difference by a recursively lower subtree Fisher quantity. Along a single realized excursion this recursive term moves **down one generation**; it does not branch into all descendants simultaneously.

For a genuinely fresh child, the subtree prior does not depend on `beta`, so `I_u=0`. Its physical return derivative is negative. Because the local innovation at first discovery is negative rather than positive, this gives precisely the one-shot adverse term from the preceding report. Once the child has been discovered, later reuse has the positive coefficient in (6.4), and its physical return contribution is favorable by (7.6).

---

## 8. What has now been removed from the obstruction

The preceding P03-B checkpoint still allowed the possibility that repeated descendant returns themselves accumulated a large physical negative debt. Theorems 3.1, 4.1 and (5.4) rule that out on the entire region `beta d>1`:

1. child-to-parent return probability contracts at a uniform logarithmic rate;
2. the increased probability of choosing a child cannot overcome that contraction;
3. every specified returning child-excursion kernel decreases;
4. every fixed aggregate stack of returning child excursions decreases;
5. after a child is known, the local degree-posterior innovation has the favorable sign for that decreasing physical kernel.

Thus **repeated known-child physical excursions are not the missing adverse mechanism**.

The descendant side now has only two possible sources of debt:

- the already quantified one-shot fresh-child discovery term;
- recursive posterior-selection score carried inside an already explored child subtree, bounded by (7.6)–(7.8).

The other unresolved channel is parent-side transport. Hitting a specified child from its parent is not the same monotone kernel as returning to one's parent, so Theorem 4.1 does not silently assign it a sign. That channel must still be combined with the earlier selected-ancestor/common-spine bounds.

This is a structural reduction, not a full monotonicity theorem.

---

## 9. Relation to source ranges

The new quenched loop theorem assumes only `beta d>1`, i.e.

\[
\lambda=1/\beta<d.
\]

For `d=2`, this component result therefore remains valid all the way to `lambda<2`, while Song–Wang–Xiang's full speed theorem is currently sourced only through

\[
\lambda\le \frac{2}{1+1/\sqrt2}\approx1.17157.
\]

No extension of the published speed interval is claimed. The point is narrower but useful: in the entire larger component range, a proof failure cannot be blamed on the sign of the quenched returning-child loop kernel.

The exact bad local-history examples from earlier P03-B reports are consistent with this. For example, at `d=2`, `beta=51/100`, the local conditioned threshold can already have the wrong derivative sign after two departures for a highly heterogeneous `{2,100}` law, yet (4.3) still gives

\[
c_d=\frac{1.02-1}{1.02+1}=\frac1{101}>0.
\]

So that local reversal is genuinely a **selection** phenomenon, not a physical descendant-return reversal.

---

## 10. Remaining obstruction and next attack

**Full-source metric:** unchanged. The Lyons–Pemantle–Peres conjecture remains open.

**New proved partial result:** every quenched returning child-excursion kernel, and every fixed stack of such loops, contracts strictly for all `beta d>1`; known-child first-return transport has the recursive Fisher bound (7.6).

**Remaining obstruction:** control the recursive subtree-score term

\[
\frac{V}{2d}\sqrt{I_u}
\]

without paying it independently at every revisit, and combine the resulting descendant ledger with parent-side selected-ancestor transport. The parent-side term remains genuinely different because it concerns hitting a specified child from above.

**Next attack:** use discovery order to charge each subtree posterior score to the unique excursion that created it. Along a realized path, (7.6) moves the unresolved selection term one generation downward and the return probability supplies a factor at most `r=1/(beta d)<1`. The target is a non-branching score-descent inequality of the form

\[
\mathcal D_{\rm known}
\le
\mathcal D_{\rm fresh}
+
 r\,\mathcal D_{\rm next\ generation},
\tag{10.1}
\]

which would sum geometrically along each excursion spine rather than over all children. The existing common-spine/selected-ancestor estimates can then be attached only when the descent exits through the parent. If (10.1) fails, the correct fallback is an exact finite multi-vertex cylinder identifying where posterior score is amplified rather than contracted.

No CLOSABLE gate, modulo shard, or audit wait was used. The prior R7-01 Potts work is untouched; P10 remains its separate owner.

---

## obligation ledger

- `source_bias_convention`: satisfied; outward `beta` preserved.
- `later_primary_range`: satisfied; 2025 reciprocal-bias theorem retained without inversion error.
- `new_regeneration_or_coupling_math`: satisfied; uniform full-stack child-loop contraction proved.
- `negative_derivative_control`: advanced; known-child physical debt eliminated and recursive selection term bounded by subtree Fisher information.
- `bounded_support_counterexample_tests`: retained; earlier wrong-sign local posterior examples are reclassified as selection rather than physical-return failures.
- `full_speed_monotonicity`: OPEN.
- `next_bottleneck`: non-branching score descent plus parent-side attachment.

`ledger_delta`: the descendant-return obstruction has been reduced from an uncontrolled repeated-revisit stack to a one-shot fresh-discovery term plus a recursively lower posterior-Fisher term; every quenched known-child return stack is now proved favorable for all `beta d>1`.
