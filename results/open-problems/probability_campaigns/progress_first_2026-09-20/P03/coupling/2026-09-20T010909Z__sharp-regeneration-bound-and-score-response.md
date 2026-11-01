Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.

# P03-B coupling report — sharp regeneration-length correction, repaired coupling debt, and a score-response identity

**Status:** PROVED PARTIAL + CORRECTION OF PRIOR P03-B ARGUMENT. The full Lyons–Pemantle–Peres speed-monotonicity conjecture remains unresolved here. This report proves a sharp one-dimensional regeneration lemma, repairs the previous P03-B debt criterion, and proves an exact finite-horizon identity isolating where negative bias-derivative contributions can occur. No external-novelty claim is made.

**Native role:** P03-B, `6aabe777361481919c9e614646464772`, probabilistic regeneration/coupling role under `operations/progress_first_2026-09-20/REGISTRY.md`.

**Captured master before this write:** `a6e6ec6323c081f26298413092eef618f59afa87`.

**Previous own checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T0010Z__regeneration-revisit-debt.md`.

**Complementary P03-A checkpoint used only to avoid duplication:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0104Z__adjacent-two-point-weight-optimization.md`. P03-A now has an analytic restricted-family theorem for every adjacent two-point law `{d,d+1}` through inward bias `lambda <= d-1/4`, and for `{2,3}` through `lambda=46/25`, i.e. outward `beta >= 25/46`. This report does not rederive that analytic identity.

## 1. Minimal source continuity check

The source convention in Ben Arous–Fribergh–Sidoravicius, arXiv:1111.5865, is outward bias `beta`: at a non-root vertex with `k` children,

\[
q_k(\beta):=P_\beta(\text{parent})=\frac1{1+\beta k},
\qquad
P_\beta(\text{a specified child})=\frac{\beta}{1+\beta k}.
\tag{1.1}
\]

The no-leaf assumption is `P(Z=0)=0`, and the conjectured monotonicity interval is the whole transient interval `beta>1/EZ`. The arXiv posting states the high-bias theorem with threshold `717` (and `717/d` at minimum offspring `d`). The final CPAM publication, DOI `10.1002/cpa.21505`, instead states the proved threshold `beta>=1160`; therefore the stale arXiv numerical threshold must not be treated as the strongest final theorem.

The strongest later source-uniform result recovered for minimum offspring `d>=2` is Song–Wang–Xiang, *Journal of Applied Probability* 62 (2025), DOI `10.1017/jpr.2024.113`: in the reciprocal inward parameter `lambda=1/beta`, speed is strictly decreasing for

\[
0\le \lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\tag{1.2}
\]

This is consistent with increasing speed in outward `beta`. Bowditch–Tokushige, arXiv:1906.07913, prove differentiability of the speed in the ballistic/CLT regime and express the derivative through a Gaussian covariance; arXiv:2006.03433 proves analyticity throughout the ballistic regime. None of these statements supplies the missing derivative sign in the full source range.

The only source detail needed below is the one-dimensional super-regeneration construction from arXiv:1111.5865, Sections 3–4. Under the conditioned law `tilde P` that time zero is a regeneration time of the auxiliary biased nearest-neighbor walk `Y`, let `tau` be its first nonzero regeneration time and

\[
B:=\#\{1\le n\le \tau:\Delta Y_n=-1\}.
\tag{1.3}
\]

The arXiv posting prints as Lemma 4.1 the deterministic claim `tau<=3B+1`. That printed claim is not correct under the displayed regeneration definition. This matters because the previous P03-B report inherited it.

## 2. Exact counterexample to the printed arXiv-v1 `3B+1` bound

Consider the nearest-neighbor path

\[
0,1,2,1,2,3,4,5,6,\ldots.
\tag{2.1}
\]

It is compatible with the event that time zero is a regeneration time because every later position is positive. There is exactly one backward step before the first positive regeneration, namely `2 -> 1`, so `B=1`.

The times before 5 fail to be positive regeneration times:

* time 1, level 1, fails because the future returns to level 1 at time 3;
* time 2, level 2, fails because the future goes below level 2 at time 3;
* time 3 is not a strict record;
* time 4 is not a strict record because level 2 was seen at time 2.

Time 5, at level 3, is a strict record and the chosen suffix stays strictly above 3 forever. Thus

\[
B=1,\qquad \tau=5>4=3B+1.
\tag{2.2}
\]

The issue in the printed arXiv proof is precise: the absence of a transition `j -> j-1` does **not** imply that the first hitting time of `j` is a regeneration time, because the path can later return to `j` via `j+1 -> j`.

This is a correction to the old arXiv posting, not a claim about the final 2014 proof text, which was not available in full in this run. The final paper's abstract has the different constant 1160, so I do not transfer the arXiv-v1 combinatorial constant into the published theorem.

## 3. Sharp deterministic replacement: `tau <= 4B+1`

The faulty bound has a simple sharp repair.

### Theorem 3.1 — sharp one-dimensional regeneration-length bound

Let `Y` be any nearest-neighbor integer path with `Y_0=0` such that time zero is a regeneration time, and let `tau>0` be its first positive regeneration time in the source sense:

\[
Y_\tau>\max_{0\le s<\tau}Y_s,
\qquad
Y_\tau<\min_{s>\tau}Y_s.
\tag{3.1}
\]

Let `B` be the number of down-steps before and including `tau`. Then

\[
\boxed{\tau\le 4B+1.}
\tag{3.2}
\]

Moreover the constant 4 is sharp: for every integer `B=k>=1` there exists a path with first positive regeneration time exactly `4k+1`.

#### Proof

Put

\[
H:=Y_\tau.
\]

If there are `B` down-steps and `U` up-steps before `tau`, then

\[
U-B=H,
\qquad
U+B=\tau,
\]

hence

\[
\tau=H+2B.
\tag{3.3}
\]

It is therefore enough to prove

\[
H\le 2B+1.
\tag{3.4}
\]

For each intermediate level `j=1,...,H-1`, let

\[
T_j:=\min\{n:Y_n=j\}.
\]

Because the walk is nearest-neighbor, `T_j` is a strict record time. Since `tau` is the **first** positive regeneration time, `T_j` is not a regeneration time. Therefore there exists a later time at which the path is at or below `j`. Define

\[
s_j:=\min\{n>T_j:Y_n\le j\}.
\tag{3.5}
\]

The step ending at time `s_j` is necessarily a down-step. There are only two possibilities:

1. `s_j=T_j+1`, in which case the step is `j -> j-1`;
2. `s_j>T_j+1`, in which case the path is strictly above `j` between `T_j` and `s_j`, so the final step is `j+1 -> j`.

Consequently a fixed down-step `r -> r-1` can be the witness (3.5) for at most two intermediate record levels, namely `j=r` and `j=r-1`. There are `H-1` intermediate levels and only `B` down-steps. Hence

\[
H-1\le 2B,
\]

which is (3.4). Combining with (3.3) proves (3.2).

For sharpness, for `k>=1` take the prefix

\[
0,
[1,2,1,2],
[3,4,3,4],
\ldots,
[2k-1,2k,2k-1,2k],
2k+1
\tag{3.6}
\]

and thereafter increase forever. There are exactly `k` down-steps, each `2r -> 2r-1`. The same down-step destroys regeneration at the two record levels `2r-1` and `2r`, and the first positive regeneration is the final visit to level `2k+1` at time `4k+1`. Therefore equality holds in (3.2). QED.

### Consequence for prior P03-B

The previous P03-B statement `tau<=3B+1`, and every quantitative inequality there that substituted that bound, is **withdrawn**. The earlier pathwise reverse-mismatch obstruction and the fresh-separated-pair positive drift lemma do not use `3B+1` and remain valid. The debt theorem is repaired next.

## 4. Repaired regeneration-debt inequality for bounded offspring

Assume

\[
d\le Z\le D\quad\text{a.s.},
\qquad 1\le d\le D<\infty,
\qquad \beta d>1,
\tag{4.1}
\]

and compare outward biases `beta` and `beta+eps`, with `eps>0`, under the common-uniform coupling from the previous P03-B report. Let

\[
q_k(\beta)=\frac1{1+\beta k},
\qquad
\delta_k:=q_k(\beta)-q_k(\beta+\varepsilon)>0,
\tag{4.2}
\]

\[
\delta_{\min}:=\min_{d\le k\le D}\delta_k,
\qquad
\delta_{\max}:=\max_{d\le k\le D}\delta_k,
\tag{4.3}
\]

and let

\[
R_\varepsilon:=
\max_{d\le i,j\le D}
[q_i(\beta+\varepsilon)-q_j(\beta)]_+
=[q_d(\beta+\varepsilon)-q_D(\beta)]_+.
\tag{4.4}
\]

The auxiliary one-dimensional walk has back-step threshold `q_d(beta)`. Let `S` be the event that the two tree walks separate at least once before `tau`, and let `N_sep` be the number of decision times before `tau` at which they are at distinct vertices.

Before separation, an auxiliary back-step exposes a common uniform variable conditional on the interval `[0,q_d(beta)]`. At the first such opportunity, the favorable split interval at a common degree `k` has length `delta_k`. Therefore

\[
\widetilde P(S)
\ge
\frac{\delta_{\min}}{q_d(\beta)}
\widetilde P(B\ge1).
\tag{4.5}
\]

Conversely, conditional on the one-dimensional sign path, separation can first occur only at one of the `B` auxiliary back-steps. A union bound gives

\[
\widetilde P(S\mid Y)
\le
B\frac{\delta_{\max}}{q_d(\beta)}.
\tag{4.6}
\]

Since `N_sep<=tau 1_S`, (4.6) and Theorem 3.1 imply

\[
\widetilde E N_{sep}
\le
\frac{\delta_{\max}}{q_d(\beta)}
\widetilde E[B\tau]
\le
\frac{\delta_{\max}}{q_d(\beta)}
\widetilde E[B(4B+1)].
\tag{4.7}
\]

At the first favorable split, the radial gap jumps by `+2`. At any already-separated decision time, the exact radial expected-gap identity from the previous run gives a loss no worse than `-2R_eps`. Hence, for

\[
G_\tau:=|X^{\beta+\varepsilon}_\tau|-|X^\beta_\tau|,
\]

we obtain the corrected bound

\[
\boxed{
\widetilde E G_\tau
\ge
2\frac{\delta_{\min}}{q_d(\beta)}
\widetilde P(B\ge1)
-
2R_\varepsilon
\frac{\delta_{\max}}{q_d(\beta)}
\widetilde E[B(4B+1)].
}
\tag{4.8}
\]

Thus a sufficient condition for strict speed increase is

\[
\boxed{
\delta_{\min}\widetilde P(B\ge1)
>
R_\varepsilon\delta_{\max}
\widetilde E[B(4B+1)].
}
\tag{4.9}
\]

This is weaker than the previous, invalid `3B+1` version but is now supported by a sharp deterministic regeneration estimate.

### `{2,3}` infinitesimal specialization

For `d=2,D=3` and `beta>1/2`, as `eps downarrow 0`,

\[
\frac{\delta_{\min}}\varepsilon\to\frac{3}{(1+3\beta)^2},
\qquad
\frac{\delta_{\max}}\varepsilon\to\frac{2}{(1+2\beta)^2},
\tag{4.10}
\]

and

\[
R_0=q_2(\beta)-q_3(\beta)
=\frac{\beta}{(1+2\beta)(1+3\beta)}.
\tag{4.11}
\]

Therefore the corrected first-order scalar sufficient condition is

\[
\boxed{
\frac{\widetilde P(B_\beta\ge1)}
{\widetilde E[B_\beta(4B_\beta+1)]}
>
\frac{2\beta(1+3\beta)}{3(1+2\beta)^3}.
}
\tag{4.12}
\]

I have **not** proved (4.12) on a new bias interval. P03-A already covers the entire `{2,3}` mixture family through inward `lambda=46/25`, so P03-B should not spend the next run duplicating that restricted theorem. The value of (4.12) is as a corrected probabilistic bridge for broader bounded-support families.

## 5. New score-response identity: exact location of negative derivative contributions

The regeneration coupling suggests that the hard part is not the local effect of increasing bias; it is the future environmental response after a radial decision. The following identity makes that statement exact without invoking Aïdékon's recursive formula.

Fix a rooted locally finite tree and a finite horizon `n`. Away from the root, let `K_t` be the number of children at the vertex occupied just before transition `t`, and let

\[
\xi_t:=|X_t|-|X_{t-1}|\in\{-1,+1\}.
\]

At a `k`-child vertex define the conditional radial drift

\[
m_k(\beta)=\frac{\beta k-1}{\beta k+1}.
\tag{5.1}
\]

For a non-root transition, the likelihood score with respect to outward bias is exactly

\[
\boxed{
S_t:=\partial_\beta\log P_\beta(X_t\mid X_{t-1},T)
=
\frac{\xi_t-m_{K_t}(\beta)}{2\beta}.
}
\tag{5.2}
\]

Indeed an outward specified-child step has score `1/[beta(1+beta k)]`, while an inward step has score `-k/(1+beta k)`, and (5.2) gives both values. In particular

\[
E_\beta[S_t\mid\mathcal F_{t-1}]=0.
\tag{5.3}
\]

For each non-root decision time define the expected remaining radial rewards conditioned on the sign of the current step,

\[
F_{t,n}^{\pm}
:=
E_\beta\left[
\sum_{s=t+1}^{n}\xi_s
\,\middle|\,
\mathcal F_{t-1},\ \xi_t=\pm1
\right],
\tag{5.4}
\]

where in the `+` case the chosen child is averaged according to its actual uniform conditional law. Root transitions are beta-independent and have zero score.

### Theorem 5.1 — finite-horizon score-response decomposition

For every finite horizon for which the displayed expectations are finite (automatic for finite `n`),

\[
\boxed{
\frac{d}{d\beta}E_\beta |X_n|
=
E_\beta\sum_{\substack{1\le t\le n\\X_{t-1}\ne o}}
\frac{K_t}{(1+\beta K_t)^2}
\left(2+F_{t,n}^{+}-F_{t,n}^{-}\right).
}
\tag{5.5}
\]

The same identity holds after annealed averaging over a Galton–Watson environment because that environment law is beta-independent.

#### Proof

For finite `n`, differentiate the path likelihood. Since the environment law has no beta dependence,

\[
\frac{d}{d\beta}E_\beta|X_n|
=
E_\beta\left[
|X_n|\sum_{t=1}^{n}S_t
\right],
\tag{5.6}
\]

with root-score terms equal to zero. Write radial displacement as the sum of increments. For a fixed `t`, every increment before `t` is measurable with respect to `F_{t-1}`, so its product with `S_t` has expectation zero by (5.3). The current-step term is

\[
E_\beta[\xi_tS_t\mid\mathcal F_{t-1},K_t=k]
=
\frac{\operatorname{Var}(\xi_t\mid K_t=k)}{2\beta}
=
\frac{2k}{(1+\beta k)^2}.
\tag{5.7}
\]

For the future reward in (5.4), let

\[
p_k=\frac{\beta k}{1+\beta k},
\qquad
q_k=\frac1{1+\beta k}.
\]

The outward and inward scores are respectively

\[
s_+=\frac1{\beta(1+\beta k)},
\qquad
s_-=-\frac{k}{1+\beta k}.
\]

Therefore

\[
E_\beta\left[
S_t\sum_{s=t+1}^{n}\xi_s
\,\middle|\,\mathcal F_{t-1},K_t=k
\right]
=
p_ks_+F_{t,n}^{+}+q_ks_-F_{t,n}^{-}
=
\frac{k}{(1+\beta k)^2}
(F_{t,n}^{+}-F_{t,n}^{-}).
\tag{5.8}
\]

Adding (5.7) and (5.8), then summing in `t`, proves (5.5). QED.

### Interpretation

Every local susceptibility coefficient

\[
\frac{K_t}{(1+\beta K_t)^2}
\]

is positive. Therefore a negative contribution to the derivative can occur only at histories satisfying

\[
F_{t,n}^{-}-F_{t,n}^{+}>2.
\tag{5.9}
\]

This is an exact probabilistic obstruction statement: increasing outward bias gives an immediate radial advantage of 2 when it flips an inward decision to an outward one; the only way to reverse the sign is for the **future expected displacement after the inward choice** to beat the future after the outward choice by more than those two levels.

On a regular tree away from the root, the future radial law after either choice is spatially homogeneous, so the response term vanishes and only the positive local susceptibility remains. In a Galton–Watson tree, (5.9) can only arise from heterogeneous future geometry plus the history/selection created by revisits. This matches, in a derivative language, the previous coupling lemma that fresh separated iid degree pairs have positive expected gap drift.

Define the response debt

\[
D_{t,n}:=[F_{t,n}^{-}-F_{t,n}^{+}-2]_+.
\tag{5.10}
\]

Equation (5.5) reduces a derivative proof to controlling the weighted accumulated response debt. This is the probabilistic quantity P03-B should attack; P03-A's recursive effective-degree derivatives are complementary and need not be duplicated.

## 6. What changed this run

The fixed full-source metric remains

`R_full: 1 -> 1`.

The obligation ledger changed materially:

* `C1` source convention and inverse-bias normalization: DONE.
* `C2` universal pathwise radial domination: RIGOROUSLY OBSTRUCTED in the prior P03-B report for nondegenerate bounded support.
* `C3` old inherited deterministic estimate `tau<=3B+1`: **REFUTED** by the explicit `B=1,tau=5` path.
* `C4` correct deterministic regeneration estimate: **DONE, SHARP**, `tau<=4B+1` with equality examples for every `B>=1`.
* `C5` previous regeneration-debt theorem: **REPAIRED** with `E[B(4B+1)]`; the old `E[B(3B+1)]` version is withdrawn.
* `C6` exact localization of finite-horizon derivative negativity: **NEW PROVED PARTIAL**, equation (5.5), with negative contribution possible only through response debt (5.10).
* `C7` full-source derivative sign / full monotonicity: OPEN.

This is not a stagnation run: two reusable structural lemmas changed, and one erroneous inherited quantitative step was removed before it could contaminate later work.

## 7. Remaining obstruction and next attack

The strongest next probabilistic attack is no longer to estimate `B` from the stale `3B+1` combinatorics. It is to bound the response debt (5.10) by explicit return/revisit events.

A concrete target is the following conditional implication for bounded support `d<=Z<=D`:

> prove that, on a regeneration block, the weighted sum of `D_{t,n}` is bounded by a constant times the number (or weighted number) of returns across already exposed parent edges, with a coefficient small enough to be dominated by the positive susceptibility term in (5.5).

The first subproblem is to condition at a decision time on whether the outward child is fresh and then couple the two future paths until the first return to the decision edge. Before that return the outward branch is an independent Galton–Watson subtree; after that return all possible negative response can be charged to a genuine revisit. If this produces a geometric return factor rather than the coarse `B(4B+1)` debt, it can survive well below the classical high-bias regime and can address bounded-support families not already covered by P03-A.

A secondary route, if that charge is still too coarse, is a spine comparison under the environment seen from the particle: express `F^- - F^+` as a difference of two spine Green functions and show that the negative part requires size-biased selection of an already explored high-degree ancestor. This would directly connect the Bowditch–Tokushige covariance derivative to a nonnegative fresh-subtree term minus an explicit revisit correction.

No finite simulation is needed for either step; both are source-level probabilistic inequalities.
