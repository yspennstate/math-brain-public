Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum reasoning is an owner preference, not authenticated runtime telemetry.

# P03-B coupling report — last-exit factorization, zero-lag score orthogonality, and a direct-regeneration hazard certificate

**Status:** PROVED PARTIAL / NEW REGENERATION-SPINE FACTORIZATION / NEW QUENCHED COMPONENT CERTIFICATE / NEW QUENCHED OBSTRUCTION. The full Lyons–Pemantle–Peres speed-monotonicity conjecture remains open.

**Native role:** P03-B, `6aabe777361481919c9e614646464772`, regeneration/coupling, spine comparison and bounded-support counterexample/certificate role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`.

**Captured master before write:** `b18fa21185c8b647a03409b2ffb45ae916b8192e`.

**Previous own checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T1718Z__second-order-escape-recursion-and-variance-absorption.md`.

**Complementary P03-A checkpoint consumed, not duplicated:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T1700Z__fine-secant-monotonicity-above-sqrt2-for-small-three-point-perturbations.md`. P03-A is handling recursive/analytic fixed-point and speed identities. This report stays on the probabilistic last-exit/regeneration side.

---

## 1. Source normalization and current checked frontier

Primary source: Gérard Ben Arous, Alexander Fribergh and Vladas Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865.

Their `beta` is the **outward child bias**. At a non-root vertex with `k` children,

\[
P_\beta(x,x^*)=\frac1{1+\beta k},
\qquad
P_\beta(x,x_i)=\frac\beta{1+\beta k}.
\tag{1.1}
\]

The Galton-Watson tree has no leaves, `P(Z=0)=0`; the source conjecture asks that the speed increase throughout the transient interval `beta>1/EZ`. The historical high-bias theorem is not treated as the present frontier.

Bowditch--Tokushige, arXiv:1906.07913, prove differentiability in the ballistic/CLT regime and identify the derivative through a two-dimensional Gaussian covariance. Their later arXiv:2006.03433 proves analyticity in the ballistic regime. These are regularity/covariance tools, not the missing sign theorem.

The strongest broad later primary monotonicity result retained after a bounded check on 20 September 2026 is He Song, Longmin Wang and Kainan Xiang, *J. Appl. Probab.* 62 (2025), 1044--1052, DOI `10.1017/jpr.2024.113`. In their reciprocal parent-bias convention `lambda=1/beta`, for minimum offspring `d>=2` they prove strict decrease for

\[
0\le\lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\tag{1.2}
\]

No inverse-parametrization contradiction is inferred.

Source locators:

- https://arxiv.org/abs/1111.5865
- https://arxiv.org/abs/1906.07913
- https://arxiv.org/abs/2006.03433
- https://doi.org/10.1017/jpr.2024.113

The fixed full-source metric remains

`R_full: 1 -> 1`.

The new theorems below are quenched bounded-support component results. Assume

\[
2\le d\le k_v\le D<\infty,
\qquad \beta d>1.
\tag{1.3}
\]

---

## 2. Why the filtration is changed in this run

The preceding P03-B report obtained an exact second-order recursion for the escape elasticity

\[
g_v:=\beta\partial_\beta\log(1-h_v)
\]

and a support-uniform region in which `g_v'(beta)<0`. The remaining speed obstruction was still phrased as covariance between regeneration duration/displacement and the terminal child selected on the escape spine.

That formulation pays too early for the terminal child. At one fresh level there is an exact pathwise factorization: the child through which the walk **finally leaves the current vertex forever** is independent of the entire collection of returning child excursions made before that last exit, once the tree is fixed and we condition on not hitting the parent. This gives two things that were not isolated before:

1. the terminal-child score has **exactly zero covariance with the current one-level last-exit duration**;
2. standard regeneration fails to advance exactly one level only through an explicit collision event: the terminal child was already used by one of the returning excursions.

The rest of the run quantifies that collision and its derivative.

---

## 3. Exact last-exit factorization at a fresh vertex

Fix a deterministic tree satisfying (1.3), and let `x` be a non-root vertex with `k` children `y_1,...,y_k`. Suppose `x` has just been visited for the first time. Let

\[
A_x:=\{T_{x^*}=\infty\}
\tag{3.1}
\]

be the event that the walk never returns to the parent of `x`.

For child `y_i`, define

\[
h_i:=P_{y_i}(T_x<\infty),
\qquad
t_i:=1-h_i,
\tag{3.2}
\]

and put

\[
p:=\frac\beta{1+\beta k},
\qquad q:=\frac1{1+\beta k}.
\tag{3.3}
\]

At any visit to `x`, exactly one of three trial types occurs:

- parent failure, with mass `q`;
- enter child `i` and eventually return to `x`, with mass
  \[
  \ell_i:=p h_i;
  \tag{3.4}
  \]
- enter child `i` and never return to `x`, with mass
  \[
  e_i:=p t_i.
  \tag{3.5}
  \]

Let

\[
L:=\sum_i\ell_i,
\qquad E:=\sum_i e_i.
\tag{3.6}
\]

Then `q+L+E=1`, and summing over any number of returning loops gives

\[
P_x(A_x)=\frac{E}{1-L}.
\tag{3.7}
\]

This is the usual escape probability `t_x`.

Let `C` be the number of returning child excursions before the terminal departure, let `I_1,...,I_C` be their child labels, and let `J` be the terminal child label. Conditional on the fixed tree and on `A_x`, a word `i_1,...,i_c;j` has probability

\[
\frac{\ell_{i_1}\cdots\ell_{i_c}e_j}{P_x(A_x)}.
\tag{3.8}
\]

Using (3.7), this factors exactly as

\[
\boxed{
P(C=c\mid T,A_x)=(1-L)L^c,
\qquad c=0,1,2,\ldots,
}
\tag{3.9}
\]

\[
\boxed{
P(I_r=i\mid C,T,A_x)=\frac{\ell_i}{L}
}
\tag{3.10}
\]

iid over the returning loops, and

\[
\boxed{
P(J=j\mid T,A_x)=\pi_j:=\frac{e_j}{E}
=\frac{t_j}{\sum_m t_m}.
}
\tag{3.11}
\]

Most importantly,

\[
\boxed{
J\ \perp\ (C,I_1,I_2,\ldots,\text{all returning-excursion paths})
\quad\text{conditional on }(T,A_x).
}
\tag{3.12}
\]

This is an exact factorization, not a bound.

### Consequence: zero-lag score orthogonality

Let `R_i` denote the hitting time of `x` from `y_i`, under the child-path law conditioned on return. The one-level last-exit duration from first arrival at `x` until the terminal step from `x` to `J` is

\[
\tau_x^{\rm last}
=1+\sum_{r=1}^{C}(1+R_{I_r}).
\tag{3.13}
\]

The inherited terminal-child score is

\[
\zeta_x(J)
:=\partial_\beta\log\pi_J
=\frac{g_J-\bar g_x}{\beta},
\qquad
\bar g_x:=\sum_j\pi_jg_j.
\tag{3.14}
\]

By (3.12),

\[
\boxed{
E[\tau_x^{\rm last}\,\zeta_x(J)\mid T,A_x]=0.
}
\tag{3.15}
\]

Thus the terminal-child selection score cannot contribute to the derivative of the **current** one-level last-exit duration. Its first possible time cost is delayed to history inside the selected child. This removes a genuine zero-lag term from the regeneration-covariance ledger.

A terminology warning is important. If `J` was visited during an earlier returning loop, the terminal arrival at `J` is not a standard first-visit regeneration time. Thus `tau_x^{last}` is a one-level last-exit block, not automatically the full next standard regeneration interval. The next section isolates exactly when the two coincide.

---

## 4. Exact collision formula for one-level standard regeneration

Because `x` itself was fresh, the next standard regeneration occurs exactly one level below `x` **if and only if** the terminal child `J` has not appeared among `I_1,...,I_C`.

Let

\[
F_x:=\{J\notin\{I_1,\ldots,I_C\}\}.
\tag{4.1}
\]

Conditional on `J=j`, use (3.9)--(3.10):

\[
P(F_x\mid J=j,T,A_x)
=E\left[\left(1-\frac{\ell_j}{L}\right)^C\right]
=\frac{1-L}{1-L+\ell_j}.
\tag{4.2}
\]

Define

\[
a_j:=\frac{1-L}{1-L+\ell_j}.
\tag{4.3}
\]

Then the exact one-level standard-regeneration probability is

\[
\boxed{
\Phi_x(\beta;T)
:=P(F_x\mid T,A_x)
=\sum_j\pi_j a_j.
}
\tag{4.4}
\]

Since `ell_j<=L`,

\[
a_j\ge1-L,
\]

so

\[
\boxed{
\Phi_x\ge1-L.
}
\tag{4.5}
\]

The support-uniform return bound `h_i<=1/(beta d)` gives

\[
L=\sum_i p h_i
\le \frac1{\beta d}\sum_i p
<\frac1{\beta d}.
\tag{4.6}
\]

Therefore

\[
\boxed{
P(\text{next standard regeneration skips at least one level}
\mid T,A_x)
\le L<\frac1{\beta d}.
}
\tag{4.7}
\]

This is a new direct bridge from returned-excursion control to the actual standard-regeneration geometry. It is not yet a tail bound for arbitrarily many skipped levels, because after a collision the selected child carries self-history.

---

## 5. Physical loop contraction makes every fixed-child freshness factor increase

The preceding P03-B report proved that every returning-child kernel

\[
\ell_i(\beta)=\frac\beta{1+\beta k}h_i(\beta)
\tag{5.1}
\]

is decreasing throughout `beta d>1`, with the explicit logarithmic margin

\[
\boxed{
-\beta\frac{\ell_i'}{\ell_i}
\ge c_x:=\frac{\beta d-1}{\beta d+1}.
}
\tag{5.2}
\]

Consequently

\[
-\beta L'\ge c_xL.
\tag{5.3}
\]

Differentiate (4.3). Since `1-L+ell_j>0`,

\[
\beta a_j'
=
\frac{(-\beta L')\ell_j+(1-L)(-\beta\ell_j')}
{(1-L+\ell_j)^2}.
\tag{5.4}
\]

Using (5.2)--(5.3) and `L+(1-L)=1`,

\[
\boxed{
\beta a_j'
\ge
c_x\frac{\ell_j}{(1-L+\ell_j)^2}
\ge c_x\ell_j>0.
}
\tag{5.5}
\]

Thus, if the terminal child label were held fixed, increasing outward bias would **strictly increase** the probability that this child had not already been consumed by a returning excursion. Any reversal of the full one-level regeneration probability (4.4) must therefore come from movement of the terminal-child law `pi`.

This separates the physical loop effect from the branch-selection effect exactly.

---

## 6. New support-uniform derivative certificate for the direct-regeneration hazard

Write

\[
x:=\beta d>1,
\qquad
\kappa:=\frac Dd\ge1.
\tag{6.1}
\]

The inherited support bands are

\[
\frac1{\beta D}\le h_i\le\frac1{\beta d},
\tag{6.2}
\]

and

\[
\frac1{\beta D-1}\le g_i\le\frac1{\beta d-1}.
\tag{6.3}
\]

Set

\[
\Delta_h
:=\frac1{\beta d}-\frac1{\beta D}
=\frac{\kappa-1}{\kappa x},
\tag{6.4}
\]

\[
\Delta_g
:=\frac1{\beta d-1}-\frac1{\beta D-1}
=\frac{(\kappa-1)x}{(x-1)(\kappa x-1)}.
\tag{6.5}
\]

From `beta pi_j'=pi_j(g_j-bar g)`, differentiating (4.4) gives the exact decomposition

\[
\boxed{
\beta\Phi_x'
=
\sum_j\pi_j\,\beta a_j'
+\operatorname{Cov}_{\pi}(a,g).
}
\tag{6.6}
\]

The first term is the favorable physical loop contraction; the covariance is the only terminal-child selection debt.

From (5.5), `ell_j=p h_j`, and (6.2),

\[
\sum_j\pi_j\beta a_j'
\ge c_x\sum_j\pi_j\ell_j
\ge c_x\frac{p}{\beta D}.
\tag{6.7}
\]

For the selection term, as a function of `ell`, `a=(1-L)/(1-L+ell)` has derivative magnitude at most `1/(1-L)`. Hence

\[
\operatorname{osc}(a)
\le \frac{p\Delta_h}{1-L}
\le \frac{p\Delta_h}{1-1/x}.
\tag{6.8}
\]

Grüss' inequality and (6.5) therefore give

\[
\operatorname{Cov}_{\pi}(a,g)
\ge
-\frac{p\Delta_h\Delta_g}{4(1-1/x)}.
\tag{6.9}
\]

Combining (6.6)--(6.9),

\[
\boxed{
\beta\Phi_x'
\ge
p\left[
\frac{c_x}{\beta D}
-
\frac{\Delta_h\Delta_g}{4(1-1/x)}
\right].
}
\tag{6.10}
\]

Substitution of `c_x=(x-1)/(x+1)` yields a support-ratio-only sufficient condition.

### Theorem 6.1 — quenched direct-regeneration monotonicity certificate

For every deterministic tree with offspring counts in `[d,D]`, every fresh non-root vertex `x`, and every `beta d>1`, define `Phi_x` by (4.4). If

\[
\boxed{
4(x-1)^3(\kappa x-1)
>
(\kappa-1)^2x^2(x+1),
\qquad x=\beta d,
\quad\kappa=D/d,
}
\tag{6.11}
\]

then

\[
\boxed{
\Phi_x'(\beta)>0.
}
\tag{6.12}
\]

So in this region, **after conditioning the fresh vertex to be a regeneration vertex**, increasing outward bias strictly increases the quenched probability that the next standard regeneration occurs exactly one level below it. This is a component theorem, not speed monotonicity.

### `[2,3]` consequence

For `d=2,D=3`, `kappa=3/2`, condition (6.11) is

\[
24x^4-89x^3+119x^2-72x+16>0.
\tag{6.13}
\]

The relevant root above one is

\[
x_*=1.67716282976912\ldots,
\tag{6.14}
\]

hence

\[
\boxed{
\beta>0.838581414884562\ldots
\quad\Longrightarrow\quad
\Phi_x'(\beta)>0
}
\tag{6.15}
\]

uniformly over every deterministic `[2,3]`-degree tree and every fresh vertex.

For comparison only, the 2025 Song--Wang--Xiang full-speed theorem for minimum offspring `d=2`, translated to outward bias, starts at

\[
\beta\ge\frac{1+1/\sqrt2}{2}
=0.853553390593\ldots.
\tag{6.16}
\]

Thus the **component** certificate (6.15) penetrates a little below the strongest checked support-uniform full-speed interval. It is not being promoted to a speed theorem because the annealed regeneration-environment tilt, regeneration duration, and multi-level collision histories remain unresolved.

---

## 7. A rigorous quenched obstruction near `beta d=1`

The direct-regeneration hazard is not monotone on every bounded-support deterministic tree throughout the full region `beta d>1`. This shows that the branch-selection covariance in (6.6) is a real mechanism, not merely a loose estimate.

Take a deterministic `[2,3]`-degree tree whose current vertex has exactly two children. Let the first child root a regular binary subtree and the second child root a regular ternary subtree. Then

\[
h_2=\frac1{2\beta},
\qquad
h_3=\frac1{3\beta}.
\tag{7.1}
\]

Substituting these values into the exact collision formula (4.4) gives

\[
\boxed{
\Phi(\beta)
=
\frac{(12\beta+1)(144\beta^2-18\beta-17)}
{12(3\beta+1)(4\beta+1)(12\beta-5)}.
}
\tag{7.2}
\]

Differentiating exactly,

\[
\boxed{
\Phi'(\beta)
=
\frac{
51840\beta^4-15552\beta^3-11592\beta^2+1536\beta+719
}
{12(3\beta+1)^2(4\beta+1)^2(12\beta-5)^2}.
}
\tag{7.3}
\]

At the source-compatible outward-bias value `beta=51/100` (so `beta d=1.02>1`),

\[
\boxed{
\Phi'(51/100)
=-\frac{2094340625}{27174124824}<0.
}
\tag{7.4}
\]

This is a **quenched deterministic mechanism obstruction**, not an annealed Galton-Watson counterexample: the two infinite regular descendant subtrees do not have positive probability under a nondegenerate iid `{2,3}` offspring law. It nevertheless proves that no argument may assume one-level fresh-regeneration probability is pointwise increasing on every bounded-support environment as soon as `beta d>1`.

The sign reversal is exactly of the type isolated in (6.6): every fixed-child freshness factor `a_j` increases by (5.5), so the negative sign can only be produced by the beta-dependent terminal-child selection law.

---

## 8. Uniform conditional return-time and last-exit moment budget

The exact factorization also produces a useful time budget in a slightly stronger subregion. It does not prove the speed derivative sign, but it prevents the current last-exit block from carrying an uncontrolled long-time tail.

Suppose

\[
x=\beta d>2-\frac1\kappa.
\tag{8.1}
\]

Let a returning excursion start from a child `y` of `x`, and condition it on eventually hitting `x`. For a descendant `z` on that excursion, let `H(z)=P_z(T_x<infinity)`. By uniqueness of the path to `x`,

\[
H(z)=h_z H(z^*).
\tag{8.2}
\]

Under the Doob transform conditioning on `T_x<infinity`, the inward transition probability at `z` is therefore

\[
\widehat p_\leftarrow(z)
=\frac{q_{k_z}}{h_z}
=\frac{1+\beta\sum_{w:w^*=z}(1-h_w)}{1+\beta k_z}.
\tag{8.3}
\]

Using `h_w<=1/(beta d)` and `k_z<=D`,

\[
\widehat p_\leftarrow(z)
\ge
1-\frac{D/d}{1+\beta D}
=:p_*.
\tag{8.4}
\]

Write

\[
\delta:=2p_*-1
=\frac{1+\kappa x-2\kappa}{1+\kappa x}>0.
\tag{8.5}
\]

The distance to `x` under the return-conditioned law is then stochastically dominated by a nearest-neighbor walk on the nonnegative integers with inward probability `p_*`. If `T_*` is the hitting time of zero from one for that comparison walk,

\[
\boxed{R_i\preceq_{st}T_*}
\tag{8.6}
\]

for every child and every environment satisfying the support bounds.

The standard one-dimensional recurrences give

\[
E T_*=\frac1\delta,
\tag{8.7}
\]

\[
E T_*^2
=\frac1{\delta^2}
+\frac{1-\delta^2}{\delta^3}.
\tag{8.8}
\]

Also `C` in (3.9) is dominated by a geometric random variable `C_*` with

\[
P(C_*=c)=(1-r)r^c,
\qquad r:=\frac1x,
\tag{8.9}
\]

because `L<=r`.

Therefore

\[
\boxed{
\tau_x^{last}
\preceq_{st}
1+\sum_{j=1}^{C_*}(1+T_{*,j}),
}
\tag{8.10}
\]

with iid copies `T_{*,j}`.

Put

\[
A:=1+\frac1\delta,
\qquad
B:=A^2+\frac{1-\delta^2}{\delta^3}.
\tag{8.11}
\]

Then

\[
\boxed{
E[\tau_x^{last}\mid T,A_x]
\le
H_1(x,\kappa)
:=1+\frac{A}{x-1},
}
\tag{8.12}
\]

and

\[
\boxed{
E[(\tau_x^{last})^2\mid T,A_x]
\le
H_2(x,\kappa)
:=1+\frac{2A+B}{x-1}
+\frac{2A^2}{(x-1)^2}.
}
\tag{8.13}
\]

For `[2,3]`, condition (8.1) is simply

\[
\beta>\frac23.
\tag{8.14}
\]

Thus throughout the entire deterministic `[2,3]` region above `2/3`, current one-level last-exit durations have a uniform second moment, while their terminal-child selection score is exactly orthogonal to the current duration by (3.15).

---

## 9. What this does and does not solve

### New proved progress

1. **Exact last-exit factorization:** conditioned on avoiding the parent, the terminal child is independent of all returning-loop history at the current fresh vertex.
2. **Zero-lag covariance removed:** the terminal-child score has exactly zero covariance with the current one-level last-exit duration.
3. **Exact regeneration collision formula:** standard regeneration advances exactly one level with probability `Phi_x=sum pi_j(1-L)/(1-L+ell_j)`.
4. **Uniform collision bound:** the probability that standard regeneration must skip past the terminal child is `<1/(beta d)`.
5. **Physical/selection separation:** every fixed-child freshness factor increases with beta; the only possible adverse derivative comes from movement of the terminal-child law.
6. **Quenched derivative certificate:** condition (6.11) forces `Phi_x'(beta)>0` on every `[d,D]` tree. For `[2,3]`, the threshold is `beta>0.838581414884562...`.
7. **Real obstruction below the certificate:** the explicit binary/ternary descendant tree has `Phi'(0.51)<0`, proving branch selection can genuinely reverse the one-level regeneration hazard.
8. **Uniform time budget:** for `beta d>2-d/D`, return-conditioned excursions and the current last-exit block have explicit first and second moment envelopes.

### What remains open

None of these statements proves asymptotic speed monotonicity. Three debts remain:

- **annealed environment tilt:** a fresh standard regeneration vertex is sampled under a beta-dependent environment law, so pointwise quenched monotonicity of `Phi_x` does not directly average to a speed theorem;
- **collision descendants:** on `F_x^c`, the terminal child carries self-history and the next standard regeneration is deeper; (4.7) bounds the frequency of entering that channel but not its complete duration/displacement law;
- **parent-side / renewal quotient:** the eventual speed derivative still requires the standard regeneration displacement/time quotient (or the equivalent Bowditch--Tokushige covariance) with no double charging against the earlier selected-ancestor/common-spine estimates.

The important narrowing is that terminal-child selection no longer pays a same-block time covariance. Its first effect is through a **future/history channel**, and the probability of entering the immediate self-history collision channel is explicitly at most `1/(beta d)`.

---

## 10. Failed shortcut and next attack

A tempting shortcut was to prove that the one-level fresh-regeneration probability must increase whenever all physical returning-loop kernels decrease. Section 7 disproves that pointwise mechanism: terminal-child selection can reverse the sign near `beta d=1`.

The next P03-B attack should therefore preserve the decomposition (6.6) instead of discarding it. The concrete target is a two-state renewal ledger:

- state `F`: the terminal child is fresh, so the next standard regeneration is exactly one level down and its descendant environment is genuinely untouched;
- state `H`: a collision occurred, whose entrance probability is at most `L<1/(beta d)`.

Use (3.15) to remove the current-block terminal score, (6.10) to control the derivative of the `F` hazard, and the earlier common-spine/history budgets only inside `H`. The first goal is a closed inequality of the form

\[
\mathcal D_{\rm regen}
\le
\frac1{\beta d}\,\mathcal D_{\rm history}
+\text{explicit first-level selection term},
\]

with no repeated payment for the same returned excursion. If that closes for `[2,3]` below the 2025 full-speed threshold, it would be a genuinely new restricted speed interval; until then the status remains **PROVED PARTIAL**.

---

## Obligation ledger

- `R_full` (full LPP conjecture): **OPEN**, unchanged.
- `R_loop_factorization`: **CLOSED this run** by (3.9)--(3.12).
- `R_zero_lag_terminal_score`: **CLOSED this run** by (3.15).
- `R_one_level_regeneration_formula`: **CLOSED this run** by (4.4).
- `R_direct_hazard_sign_all_beta_d_gt_1`: **FALSE as a quenched mechanism**, exact obstruction (7.4).
- `R_direct_hazard_high_region`: **CLOSED this run** under explicit condition (6.11).
- `R_last_exit_time_moments`: **CLOSED this run** under `beta d>2-d/D`, by (8.10)--(8.13).
- `R_collision_history_channel`: **OPEN**; now entered with probability `<1/(beta d)` from a fresh regeneration vertex.
- `R_annealed_regeneration_quotient`: **OPEN**; next target.

`ledger_delta`: exact last-exit factorization + zero-lag score cancellation + exact regeneration-collision law + support-uniform derivative certificate + explicit quenched sign obstruction + uniform conditional time moments.