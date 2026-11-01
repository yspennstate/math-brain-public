Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.

# P03-B coupling report — first-split hazard amplification and fresh-pivotal degree tilt

**Status:** PROVED PARTIAL. The full Lyons–Pemantle–Peres speed-monotonicity conjecture remains unresolved here. This run proves a strictly stronger regeneration-coupling lower bound by using every pre-decoupling auxiliary backstep as a positive split opportunity, rather than only asking whether a regeneration block contains a backstep. It also proves a fresh-pivotal degree-tilt lemma and identifies a rigorous obstruction to any coupling argument that retains the worst possible post-split degree pair. No external-novelty claim is made.

**Native role:** P03-B, `6aabe777361481919c9e614646464772`, probabilistic regeneration/coupling and counterexample role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`.

**Captured master immediately before write:** `169b7e1d6cfbb025e9e6f47fad4618e9a403dba3`.

**Previous own checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T032221Z__exact-backstep-law-and-backstep-only-debt.md`.

**Latest complementary P03-A checkpoint consumed only to avoid duplication:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0401Z__harmonic-tail-stieltjes-extension.md`. P03-A now has a stronger distribution-sensitive analytic interval theorem based on the harmonic-tail statistic. I do not duplicate that Aïdékon/Stieltjes analysis or claim the elementary bounded-support consequences below as endpoint improvements over P03-A.

## 1. Source normalization and current external baseline

The primary coupling source is Gérard Ben Arous, Alexander Fribergh and Vladas Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865. It assumes a Galton–Watson offspring variable `Z` with

\[
\mathbf P(Z=0)=0,
\]

and uses **outward child bias** `beta`: at a non-root vertex with `k` children,

\[
q_k(\beta):=P_\beta(\text{parent})=\frac1{1+\beta k},
\qquad
P_\beta(\text{a specified child})=\frac\beta{1+\beta k}.
\tag{1.1}
\]

Thus increasing `beta` means stronger drift away from the root. The walk is transient for `beta>1/EZ`; the source conjecture asks that the speed `v(beta)` increase throughout that interval. The arXiv source proves the old high-bias range and provides the common-uniform/super-regeneration coupling used below.

Bowditch--Tokushige, arXiv:1906.07913, prove differentiability where the walk is ballistic and satisfies their CLT assumptions, with a Gaussian-covariance derivative representation; arXiv:2006.03433 proves analyticity in the ballistic regime. Those papers do not supply the missing derivative sign.

The strongest source-uniform later range retained in the campaign is He Song, Longmin Wang and Kainan Xiang, *Journal of Applied Probability* 62 (2025), DOI `10.1017/jpr.2024.113`. In reciprocal parent bias `lambda=1/beta`, when the minimum offspring is `d>=2`, they prove strict speed decrease on

\[
0\le \lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\tag{1.2}
\]

This is consistent with increasing speed in outward `beta`; no inverse-parametrization contradiction is present.

The fixed full-source metric remains

`R_full: 1 -> 1`.

## 2. Inherited exact one-dimensional block law

For the coupling theorem assume

\[
d\le Z\le D\quad\text{a.s.},
\qquad 1\le d\le D<\infty,
\qquad \beta d>1.
\tag{2.1}
\]

Set

\[
q:=q_d(\beta)=\frac1{1+\beta d},
\qquad
p:=1-q=\frac{\beta d}{1+\beta d},
\qquad
c:=p-q=\frac{\beta d-1}{\beta d+1},
\qquad
r:=\frac qp=\frac1{\beta d}.
\tag{2.2}
\]

Use the source common uniforms and the auxiliary nearest-neighbor walk `Y` whose backstep event is `U<=q`. Under the `0-SR` conditioning let `tau` be the first positive super-regeneration time and let

\[
B:=\#\{1\le n\le\tau:\Delta Y_n=-1\}.
\tag{2.3}
\]

The preceding P03-B run proved an exact negative-binomial level-chain representation and, with

\[
\mathcal L(r):=\sum_{m\ge1}\frac{r^m}{1-r^m},
\qquad
A(\beta,d):=1+3p+c\mathcal L(r),
\tag{2.4}
\]

the exact moments

\[
\widetilde E B=\frac q{c^2},
\qquad
\widetilde E\tau=\frac1{c^2},
\qquad
\widetilde E[B(B-1)]
=\frac{2q^2}{c^4}A(\beta,d).
\tag{2.5}
\]

The same run proved that negative radial gap increments can occur only at auxiliary backsteps. Its remaining quantitative weakness was different: it lower-bounded the positive decoupling probability by using only the event `B>=1`, thereby discarding the fact that **every backstep before decoupling is another independent-uniform chance to split in the favorable direction**.

That is the point repaired below.

## 3. New finite-epsilon theorem: every pre-split backstep contributes positive hazard

Couple a `beta` walk `X^-` and a `(beta+epsilon)` walk `X^+` with the source common uniforms. While the walks are at the same vertex of degree `k`, the only radial decoupling interval has length

\[
\delta_k(\epsilon)
:=q_k(\beta)-q_k(\beta+\epsilon)
=\frac{\epsilon k}
{(1+\beta k)(1+(\beta+\epsilon)k)}.
\tag{3.1}
\]

On that interval `X^+` goes outward and `X^-` goes inward, so the radial gap jumps from zero to `+2`.

Define

\[
\delta_-:=\min_{d\le k\le D}\delta_k(\epsilon),
\qquad
\delta_+:=\max_{d\le k\le D}\delta_k(\epsilon),
\tag{3.2}
\]

and conditional backstep hazards

\[
\alpha_-:=\frac{\delta_-}{q},
\qquad
\alpha_+:=\frac{\delta_+}{q}.
\tag{3.3}
\]

After separation, a radial gap decrement by `2` at current degrees `(i,j)` can occur only on an interval of length

\[
[q_i(\beta+\epsilon)-q_j(\beta)]_+.
\]

Hence its worst possible unconditional width is

\[
R_\epsilon
:=\left[q_d(\beta+\epsilon)-q_D(\beta)\right]_+,
\qquad
\rho_\epsilon:=\frac{R_\epsilon}{q}.
\tag{3.4}
\]

Finally write

\[
\mathcal G(s):=\widetilde E[s^B],\qquad 0\le s\le1.
\tag{3.5}
\]

### Theorem 3.1 — first-split hazard amplification

Let

\[
\Delta_\tau:=|X^+_\tau|-|X^-_\tau|.
\]

Then for every `epsilon>0`,

\[
\boxed{
\widetilde E\Delta_\tau
\ge
2\bigl[1-\mathcal G(1-\alpha_-)\bigr]
-
2\rho_\epsilon
\left[
\widetilde E B
-
\frac{1-\mathcal G(1-\alpha_+)}{\alpha_+}
\right].
}
\tag{3.6}
\]

The quotient is interpreted by continuity if needed. For `epsilon>0` under the present finite-support assumptions, `alpha_+>0`.

#### Proof

Order the auxiliary backsteps before `tau` as `t_1<...<t_B`. Let `S` be the event that the two tree walks have decoupled at least once before `tau`.

**Step 1: lower-bound the favorable first split.** Before the first split the two walks occupy the same vertex. At the `j`th auxiliary backstep, conditional on the entire past and on the fact that `Y` backsteps, the current uniform is uniform on `[0,q]`. If the common current degree is `K_j`, the conditional probability of favorable decoupling is

\[
\frac{\delta_{K_j}(\epsilon)}q\ge\alpha_-.
\]

The `0-SR` event and the auxiliary up/down skeleton depend only on whether each uniform lies below or above `q`; they do not reveal its location inside `[0,q]`. Thus the same conditional hazard bound remains valid after conditioning on the auxiliary skeleton and on the previous failures to split. Consequently, given `B=b`,

\[
\widetilde P(S^c\mid B=b)\le(1-\alpha_-)^b,
\]

and therefore

\[
\widetilde P(S)
\ge1-\widetilde E(1-\alpha_-)^B
=1-\mathcal G(1-\alpha_-).
\tag{3.7}
\]

This is the positive-hazard gain missing from the preceding bound.

**Step 2: a reverse mismatch needs prior separation.** At the `j`th backstep, a radial gap decrement is impossible if the walks have never previously separated: at equal degree the `(beta+epsilon)` walk has a smaller parent probability. If separation has occurred, then conditional on the current degree pair and on the auxiliary backstep, the probability of a reverse mismatch is at most `rho_epsilon` by (3.4).

Before the `j`th backstep, there have been at most `j-1` favorable split opportunities. Each has conditional hazard at most `alpha_+`. Hence, again by sequential conditioning,

\[
\widetilde P(\text{a split occurred before }t_j\mid B\ge j)
\le1-(1-\alpha_+)^{j-1}.
\tag{3.8}
\]

Let `N_-` be the number of radial `-2` reverse mismatches after the first split. Summing (3.8) gives

\[
\begin{aligned}
\widetilde E N_-
&\le
\rho_\epsilon\,
\widetilde E\sum_{j=1}^{B}
\left[1-(1-\alpha_+)^{j-1}\right]\\
&=
\rho_\epsilon
\left[
\widetilde E B
-
\frac{1-\mathcal G(1-\alpha_+)}{\alpha_+}
\right].
\end{aligned}
\tag{3.9}
\]

**Step 3: pathwise gap accounting.** At the first split the gap increases by exactly `2`. Auxiliary upsteps cannot decrease the radial gap, and every later decrease is by at most `2` and is counted by `N_-`. Therefore pathwise

\[
\Delta_\tau\ge2\mathbf1_S-2N_-.
\tag{3.10}
\]

Taking expectations and combining (3.7)--(3.9) proves (3.6). QED.

### Remark 3.2 — compound-geometric interpretation of `G`

The exact downcrossing chain from the previous run gives a useful probabilistic interpretation. At state zero, the chain makes a `0->0` self-loop with probability `p`; that self-loop ends the regeneration block. Otherwise it makes a nontrivial excursion away from zero and, upon returning, restarts independently. If `C^+` denotes the area of one nontrivial excursion and

\[
\phi(s)=E[s^{C^+}],
\]

then the number of nontrivial excursions before the terminating self-loop is geometric on `{0,1,2,...}` with success probability `p`, and

\[
\boxed{
\mathcal G(s)=\frac{p}{1-q\phi(s)}.
}
\tag{3.11}
\]

Thus (3.6) is not only an infinitesimal statement; the exact level-chain recurrence from the previous report can in principle evaluate the finite-`epsilon` bound.

## 4. New infinitesimal coupling bound

For

\[
a_k(\beta):=\frac{k}{(1+\beta k)^2},
\tag{4.1}
\]

we have

\[
\frac{\delta_k(\epsilon)}\epsilon\longrightarrow a_k(\beta).
\tag{4.2}
\]

Because `beta d>1`, the continuous function `k/(1+beta k)^2` is decreasing for `k>=d`. Therefore

\[
\frac{\delta_-}\epsilon\to a_D(\beta),
\qquad
\frac{\delta_+}\epsilon\to a_d(\beta).
\tag{4.3}
\]

Also set

\[
R_0:=q_d(\beta)-q_D(\beta)\ge0.
\tag{4.4}
\]

Since `B` has a finite second moment, as `x downarrow 0`,

\[
\mathcal G(1-x)
=1-x\widetilde E B
+\frac{x^2}{2}\widetilde E[B(B-1)]
+o(x^2).
\tag{4.5}
\]

Substitute (2.5) and (4.2)--(4.5) into Theorem 3.1. The positive term contributes

\[
\frac{2a_D}{c^2}
\]

at first order in `epsilon`, while the reverse-debt term contributes at most

\[
\frac{2R_0a_d}{c^4}A(\beta,d).
\]

The common super-regeneration identity gives

\[
v(\beta+\epsilon)-v(\beta)
=
\frac{\widetilde E\Delta_\tau}{\widetilde E\tau},
\qquad
\widetilde E\tau=c^{-2}.
\tag{4.6}
\]

Therefore:

### Theorem 4.1 — amplified lower right derivative

For every bounded-support offspring law satisfying (2.1),

\[
\boxed{
\liminf_{\epsilon\downarrow0}
\frac{v(\beta+\epsilon)-v(\beta)}\epsilon
\ge
2a_D(\beta)
-
\frac{2R_0a_d(\beta)}{c^2}
A(\beta,d).
}
\tag{4.7}
\]

In particular,

\[
\boxed{
a_D(\beta)c^2
>
R_0a_d(\beta)A(\beta,d)
}
\tag{4.8}
\]

is a rigorous sufficient condition for a strictly positive lower right derivative. Wherever the Bowditch--Tokushige differentiability theorem applies, (4.7) is a lower bound for `v'(beta)` itself.

#### Exact improvement over the preceding P03-B bound

The preceding backstep-only theorem gave

\[
\liminf_{\epsilon\downarrow0}
\frac{v(\beta+\epsilon)-v(\beta)}\epsilon
\ge
2c^2a_D
-
\frac{2R_0a_d}{c^2}A(\beta,d).
\tag{4.9}
\]

The negative term is unchanged, but the positive term is now `2a_D` rather than `2c^2 a_D`. Thus the proved gain is exactly

\[
\boxed{2(1-c^2)a_D>0.}
\tag{4.10}
\]

The reason is conceptual rather than algebraic: the old bound only used whether a block possessed at least one backstep; Theorem 3.1 uses the full number of pre-split backstep opportunities.

#### Regular-tree self-check

If `D=d`, then `R_0=0` and (4.7) becomes

\[
\liminf_{\epsilon\downarrow0}
\frac{v(\beta+\epsilon)-v(\beta)}\epsilon
\ge2a_d(\beta).
\]

For the deterministic `d`-ary tree,

\[
v(\beta)=\frac{\beta d-1}{\beta d+1},
\qquad
v'(\beta)=\frac{2d}{(1+\beta d)^2}=2a_d(\beta),
\]

so the amplified bound is exact in the zero-disorder endpoint. The previous bound lost the factor `c^2` even there; this is a strong internal check that the new positive-hazard accounting is the correct normalization.

## 5. New spine-side comparison: fresh pivotal sites are biased toward smaller offspring

The first-order split mechanism itself has a useful degree law that is independent of P03-A's analytic escape tilt.

Suppose a favorable split opportunity occurs while the common walk is at a **freshly discovered** vertex. Before revealing its offspring, that degree has the original law `P(Z=k)`. Conditional on a split at that opportunity,

\[
P_\epsilon(K=k\mid\text{split at this fresh opportunity})
\propto
P(Z=k)\,\delta_k(\epsilon).
\tag{5.1}
\]

As `epsilon downarrow 0`, this converges to the pivotal law

\[
\boxed{
P_{\rm piv}(K=k)
=
\frac{P(Z=k)a_k(\beta)}{E[a_Z(\beta)]}.
}
\tag{5.2}
\]

### Lemma 5.1 — fresh pivotal stochastic domination

If `beta d>=1`, then

\[
K_{\rm piv}\preceq_{\rm st} Z.
\tag{5.3}
\]

#### Proof

For real `x>=d`,

\[
\frac d{dx}\frac{x}{(1+\beta x)^2}
=
\frac{1-\beta x}{(1+\beta x)^3}\le0.
\tag{5.4}
\]

Thus the likelihood ratio in (5.2), `a_k/Ea_Z`, is nonincreasing in `k`. A decreasing likelihood-ratio tilt is stochastically dominated by the untilted law. Equivalently, for every increasing `f`,

\[
E_{\rm piv}f(K)\le Ef(Z).
\tag{5.5}
\]

QED.

Since `q_k(beta)` decreases in `k`, this also gives

\[
\boxed{
E_{\rm piv}q_K(\beta)
\ge E q_Z(\beta).
}
\tag{5.6}
\]

So fresh pivotal splits occur preferentially at thinner vertices. This does **not** by itself settle the future response: after the split one walk sits in a fresh child subtree while the other is on an already exposed ancestor side. It does, however, identify the correct Palm tilt that a refined spine/history comparison must use. It is distinct from P03-A's escape tilt, although both happen to downweight high degrees in their respective regimes.

## 6. Rigorous obstruction to the remaining worst-pair mechanism

Theorem 4.1 fixes the positive side of the old coupling estimate, but it also makes the remaining obstruction transparent. If `D>d`, then as

\[
\beta d\downarrow1,
\]

we have `c^2 downarrow 0`, whereas

\[
R_0
=\frac1{1+\beta d}-\frac1{1+\beta D}
\longrightarrow
\frac12-\frac{d}{d+D}>0,
\]

and `a_d,a_D` remain finite and strictly positive. Since `A(beta,d)>=1`, the negative term in (4.7) obeys

\[
\frac{2R_0a_d}{c^2}A(\beta,d)\to+\infty.
\tag{6.1}
\]

Therefore **no refinement that keeps the same worst-pair reverse width `R_0` can approach the auxiliary critical line `beta d=1` merely by improving the favorable split count**. The singular loss is now entirely on the post-split orientation/history side.

This is a useful negative result for mechanism design: the next coupling advance has to replace

\[
R_0=\max_{i,j}[q_i(\beta)-q_j(\beta)]_+
\]

by an annealed, history-sensitive quantity. Further work on the scalar backstep count alone cannot remove this obstruction.

## 7. Remaining obstruction and next concrete attack

### What changed in this run

* `C6` exact auxiliary downcrossing chain and moments: **inherited PROVED PARTIAL**.
* `C8` old worst-pair derivative bound (4.9): **strictly superseded**.
* `C9` finite-`epsilon` first-split hazard theorem (3.6): **NEW PROVED PARTIAL**.
* `C10` amplified derivative lower bound (4.7), exact on regular trees: **NEW PROVED PARTIAL**.
* `C11` fresh pivotal law (5.2) and stochastic domination (5.3): **NEW PROVED PARTIAL**.
* Full source monotonicity on `(1/EZ,infinity)`: **OPEN**.

### Remaining mathematical obstruction

After a first-order favorable split, the two walks no longer see identically distributed degree histories. A fresh-fresh pair has favorable annealed drift, but an exposed ancestor may be selected by past returns. The current bound throws away all of that structure and pays the extremal degree cost `R_0` at every eligible later backstep. Section 6 proves that this worst-pair replacement is the singular bottleneck.

### Next attack

Work at first order in `epsilon` and condition on a single pivotal split. At the `j`th subsequent auxiliary backstep replace `R_0` by

\[
\mathcal R_j
:=
E\Bigl[
[q_{K_j^+}(\beta)-q_{K_j^-}(\beta)]_+
\,\Bigm|\,
\text{one pivotal split and no later bias pivot}
\Bigr].
\tag{7.1}
\]

Decompose `mathcal R_j` according to whether each current vertex is fresh or previously exposed. For a fresh pivotal site use the exact Palm tilt (5.2); for fresh descendants use the original offspring law. The target lemma is a summable history correction of the form

\[
\sum_{j\ge1}w_j\mathcal R_j
\le
\text{fresh cancellation}
+
\text{explicit return kernel},
\tag{7.2}
\]

where the weights `w_j` come from the exact reversible downcrossing chain. Proving (7.2) would attack precisely the factor that diverges in (6.1), without duplicating P03-A's recursive derivative identities.

No simulation result is used as proof in this report.
