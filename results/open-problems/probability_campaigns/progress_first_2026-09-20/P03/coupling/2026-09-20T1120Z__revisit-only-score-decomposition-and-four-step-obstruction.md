Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.

# P03-B coupling report — exact revisit-only derivative decomposition, return-odds contraction, and the first adverse cross-history expectation

**Status:** PROVED PARTIAL / NEW PROBABILISTIC REDUCTION / EXACT SOURCE-VALID OBSTRUCTION. The full Lyons–Pemantle–Peres speed-monotonicity conjecture remains open. No finite-horizon calculation below is represented as asymptotic speed monotonicity or as a counterexample to it.

**Native role:** P03-B, `6aabe777361481919c9e614646464772`, regeneration/coupling, spine comparison and source-valid counterexample role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`.

**Captured master immediately before write:** `e77bd5f95849d2916b884a33fe92648fcde579cb`.

**Previous own checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T1020Z__finite-path-fisher-history-and-return-budget.md`.

**Latest complementary P03-A checkpoint consumed, not duplicated:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T1106Z__uniform-explicit-terminal-strip-for-all-one-two-mixtures.md`, creation commit `c7233ae9abadfd8fca0970561e6ab96b9103c758`. P03-A has now made its terminal critical-edge theorem explicit uniformly over every nondegenerate `{1,2}` mixture. This report stays on the distinct observed-score / revisit / regeneration side and bounded-support `d>=2` test families.

## 1. Minimal source continuity

Primary source: Gérard Ben Arous, Alexander Fribergh and Vladas Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865, https://arxiv.org/abs/1111.5865 . The tree has no leaves, `P(Z=0)=0`, and at a non-root vertex with `k` children the source uses **outward child bias** `beta`:

\[
q_k(\beta):=P_\beta(\text{parent}\mid k)=\frac1{1+\beta k},
\qquad
P_\beta(\text{a specified child}\mid k)=\frac\beta{1+\beta k}.
\tag{1.1}
\]

At the root a child is chosen uniformly, independently of `beta`. Thus larger `beta` means stronger outward bias. The full conjecture asks that the speed be increasing throughout the transient interval `beta>1/EZ`.

Bowditch–Tokushige, arXiv:1906.07913 / ALEA 17 (2020), prove differentiability in the ballistic/CLT regime and express the derivative through a two-dimensional Gaussian covariance; arXiv:2006.03433 proves analyticity in the ballistic regime. These are regularity/covariance tools, not a sign theorem.

The strongest broad later primary monotonicity theorem retained after the current bounded source check is He Song, Longmin Wang and Kainan Xiang, *The speed of a biased walk on a Galton–Watson tree without leaves is monotonic for low values of bias*, Journal of Applied Probability 62 (2025), 1044–1052, DOI `10.1017/jpr.2024.113`. Their parameter is reciprocal **parent bias** `lambda=1/beta`; for minimum offspring `d>=2` they prove strict decrease of speed for

\[
0\le \lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\tag{1.2}
\]

No inverse-parametrization contradiction is inferred. The full-source status remains **OPEN**.

For the quantitative revisit statements below I work in the source-valid bounded-support family

\[
2\le d\le Z\le D<\infty,
\qquad \beta d>1.
\tag{1.3}
\]

The finite-path identities themselves only require a no-leaf offspring law and exclude the root from the local score because the root transition is `beta`-independent.

---

## 2. Inherited exact objects

Let

\[
Q_v:=q_{Z_v}(\beta),
\qquad \mu:=E Q_v.
\tag{2.1}
\]

Fix a deterministic finite horizon `T`, and let `G_t` be the annealed canonical path filtration immediately before transition `t`. If the current non-root vertex `v=X_t` has already made `j-1` departures, write

\[
M_t:=E[Q_v\mid G_t],
\qquad
V_t:=\operatorname{Var}(Q_v\mid G_t),
\qquad
j_t:=j.
\tag{2.2}
\]

Let `I_t=1` when transition `t` goes to the parent and `I_t=0` otherwise. After observing transition `t`, let

\[
\Delta M_t:=M_v(j)-M_v(j-1).
\tag{2.3}
\]

At discovery, `M_v(0)=mu`. The previous report proved that the terminal observed path score and history debt are

\[
\mathcal S_T
=\frac1\beta\sum_v\bigl(N_vM_v(N_v)-P_v\bigr),
\tag{2.4}
\]

and

\[
D_T:=\sum_vN_v\bigl(M_v(N_v)-\mu\bigr).
\tag{2.5}
\]

It also proved

\[
\frac d{d\beta}E_\beta R_T
=2\beta E_\beta\mathcal S_T^2
-2E_\beta[D_T\mathcal S_T],
\tag{2.6}
\]

for a root-free segment, with the root contributing no score when one starts from the source root.

The unresolved issue was the apparently global covariance `E[D_T S_T]`. The main result below shows that most of that covariance cancels exactly: the only genuinely nonlocal term is carried by **revisit departures**.

---

## 3. Exact local score increment

For one vertex, after `j` departures and `P_j` parent departures, (2.4) gives the local score

\[
\mathcal S_{v,j}=\frac{jM_v(j)-P_j}{\beta}.
\]

Therefore the increment at its `j`-th departure is exactly

\[
\boxed{
\beta\,\Delta\mathcal S_t
=j_t\Delta M_t+M_t-I_t.
}
\tag{3.1}
\]

Both summands are martingale differences under the observed filtration:

\[
E[\Delta M_t\mid G_t]=0,
\qquad
E[M_t-I_t\mid G_t]=0.
\tag{3.2}
\]

The second identity uses `P(I_t=1|G_t)=M_t`.

There is also an exact covariance identity which does not require enumerating parent / known-child / new-child categories.

### Lemma 3.1 — posterior innovation versus radial Bernoulli innovation

\[
\boxed{
E[\Delta M_t(M_t-I_t)\mid G_t]=-V_t.
}
\tag{3.3}
\]

#### Proof

Put `M_t^+=M_t+Delta M_t=E[Q_v|G_{t+1}]`. Because `I_t` is `G_{t+1}`-measurable,

\[
E[M_t^+I_t\mid G_t]
=E[Q_vI_t\mid G_t]
=E[Q_v^2\mid G_t].
\]

Also `E[M_t^+|G_t]=M_t` and `E[I_t|G_t]=M_t`. Hence

\[
E[\Delta M_t(I_t-M_t)\mid G_t]
=E[Q_v^2\mid G_t]-M_t^2
=V_t,
\]

which is (3.3). QED.

If

\[
W_t:=E[(\Delta M_t)^2\mid G_t],
\tag{3.4}
\]

then (3.1) and (3.3) give

\[
E[(\beta\Delta\mathcal S_t)^2\mid G_t]
=j_t^2W_t-2j_tV_t+M_t(1-M_t).
\tag{3.5}
\]

The important point is that the `W_t` term will cancel completely from the speed derivative.

---

## 4. Abel decomposition of the history debt

At a fixed vertex with terminal local time `N`,

\[
N(M_N-\mu)=N\sum_{j=1}^N\Delta M_j.
\]

Abel summation gives the exact identity

\[
\boxed{
N(M_N-\mu)
=\sum_{j=1}^Nj\Delta M_j
+\sum_{j=1}^{N-1}(M_j-\mu).
}
\tag{4.1}
\]

Indeed the coefficient of `Delta M_i` on the right is `i+(N-i)=N`.

Define globally

\[
K_T:=\sum_{t<T:X_t\ne e}j_t\Delta M_t,
\tag{4.2}
\]

and the **predictable revisit debt**

\[
\boxed{
B_T:=\sum_{t<T:X_t\ne e,\ j_t\ge2}(M_t-\mu).
}
\tag{4.3}
\]

Then

\[
\boxed{D_T=K_T+B_T.}
\tag{4.4}
\]

On the other hand, summing (3.1) gives

\[
\boxed{
\beta\mathcal S_T=K_T+C_T,
\qquad
C_T:=\sum_{t<T:X_t\ne e}(M_t-I_t).
}
\tag{4.5}
\]

`K_T` and `C_T` are martingales. All nonmartingale history allocation is now isolated in `B_T`, and `B_T` is supported only on second and later departures from a vertex.

---

## 5. Main theorem: all first-visit cross-history terms cancel

Because martingale increments at distinct times are orthogonal, Lemma 3.1 implies

\[
\beta E[K_T\mathcal S_T]
=E\sum_{t<T:X_t\ne e}
\left(j_t^2W_t-j_tV_t\right).
\tag{5.1}
\]

Similarly, (3.5) gives

\[
\beta^2E[\mathcal S_T^2]
=E\sum_{t<T:X_t\ne e}
\left(j_t^2W_t-2j_tV_t+M_t(1-M_t)\right).
\tag{5.2}
\]

Substitute `D_T=K_T+B_T` into (2.6). The `j_t^2W_t` terms cancel exactly.

### Theorem 5.1 — revisit-only derivative decomposition

For every deterministic finite horizon, with root transitions omitted from the score,

\[
\boxed{
\frac d{d\beta}E_\beta R_T
=
\frac{2}{\beta}
E\sum_{t<T:X_t\ne e}
\bigl[M_t(1-M_t)-j_tV_t\bigr]
-2E[B_T\mathcal S_T].
}
\tag{5.3}
\]

Moreover, because the summand in `B_T` is `G_t`-measurable and all score increments from time `t` onward have conditional mean zero,

\[
\boxed{
E[B_T\mathcal S_T]
=
E\sum_{t<T:X_t\ne e,\ j_t\ge2}
(M_t-\mu)\,\mathcal S_t^{-},
}
\tag{5.4}
\]

where `S_t^-` is the cumulative observed score strictly before transition `t`.

Thus **every genuinely cross-vertex / cross-excursion contribution to the derivative is gated by a revisit**. A first departure from a fresh vertex contributes only through the local posterior term in the first sum of (5.3).

This is substantially sharper than the previous formulation in terms of the terminal covariance `E[D_T S_T]`.

### Link to the previous local derivative formula

The 0813Z/0904Z calculations gave, after `n` previous local departures,

\[
M_{n,c}'(\beta)
=
\frac1\beta\left((n+1)V-M(1-M)\right).
\tag{5.5}
\]

At the next departure `j=n+1`, the local term in (5.3) is therefore exactly

\[
\frac2\beta[M(1-M)-jV]
=-2M_{n,c}'(\beta).
\tag{5.6}
\]

Hence the finite-horizon derivative has the clean interpretation

\[
\boxed{
\frac d{d\beta}E R_T
=-2E\sum_t M_t'(\beta)
-2E[B_T\mathcal S_T].
}
\tag{5.7}
\]

The first term is the already-controlled local posterior response; the second is the **only remaining history-transport term**.

In particular, the previous support coefficient

\[
\rho_{d,D}(\beta)
=
\frac{\beta(\sqrt D-\sqrt d)^2}
{(1+\beta d)(1+\beta D)}
\tag{5.8}
\]

continues to imply that local terms are favorable whenever `j_t rho <=1`. Long local histories are geometrically rare by the earlier single-vertex escape bound. What remains is no longer a generic inter-vertex covariance; it is specifically a **score carried across an excursion and paid only when the vertex is revisited**.

---

## 6. New quenched return lemma: child-to-parent return odds contract with outward bias

The remaining term in (5.4) is organized by excursions between consecutive departures from the same vertex. For descendant excursions there is a useful exact monotonicity law.

Fix a deterministic rooted tree and a non-root vertex `x`. Let

\[
h_x(\beta):=P_\beta^x(T_{x^*}<\infty)
\tag{6.1}
\]

be the probability ever to hit the parent. If `x` has children `x_1,...,x_k`, first-step decomposition gives

\[
\boxed{
 h_x(\beta)
=\frac1{1+\beta\sum_{i=1}^k(1-h_{x_i}(\beta))}.
}
\tag{6.2}
\]

To justify this on an infinite tree, first impose an absorbing failure boundary at generation `n`, use (6.2) on the finite truncation, and let `n` increase. The finite probabilities increase to the eventual parent-hitting probability.

Induction on a finite truncation shows every `h_x^{(n)}(beta)` is decreasing in `beta`. Passing to the limit preserves monotonicity. More is true: since the child return probabilities decrease, the quantity

\[
S_x(\beta):=\sum_i(1-h_{x_i}(\beta))
\]

is increasing. Hence for `beta_2>beta_1`,

\[
\boxed{
\frac{h_x(\beta_2)}{1-h_x(\beta_2)}
\le
\frac{\beta_1}{\beta_2}
\frac{h_x(\beta_1)}{1-h_x(\beta_1)}.
}
\tag{6.3}
\]

So the **return odds**, not merely the return probability, contract at least by the inverse bias ratio. Where a derivative exists this implies

\[
\frac d{d\beta}
\log\frac{h_x}{1-h_x}
\le -\frac1\beta.
\tag{6.4}
\]

This is a quenched statement and does not use the Galton–Watson law beyond providing the tree. It complements the previously proved crude bound `h_x<=1/(beta d)`: the old bound controls magnitude, while (6.3) controls how descendant-return propensity changes with the bias.

This is precisely the sign information needed when (5.4) is decomposed into return excursions: a successful excursion through a child becomes less likely as outward bias rises. Parent-side excursions remain the harder selected-history channel.

---

## 7. The tempting sign conjecture for the revisit term is false

Theorem 5.1 raises a natural hope:

> perhaps `E[B_T S_T] <= 0` always, so the revisit-history term can simply be discarded in a lower bound.

That hope is false even in a bounded-support, no-leaf Galton–Watson family. The failure occurs at the **first horizon at which the revisit term can exist**.

Start the source walk at the root. Root transitions are `beta`-independent and contribute no score. For `T<=3` transitions, no non-root vertex can both be departed from and then be departed from again, so

\[
B_T=0.
\tag{7.1}
\]

At `T=4`, there are exactly two prefix mechanisms that put the walk at a non-root vertex `v` for its second departure:

1. `root -> v -> root -> v`;
2. `root -> v -> new child w -> v`.

Everything can therefore be integrated exactly for an arbitrary no-leaf offspring law.

Put

\[
Q=q_Z(\beta),
\qquad
\mu=EQ,
\qquad
V=\operatorname{Var}(Q),
\qquad
\eta=E\frac1Z.
\tag{7.2}
\]

After the first departure from a fresh vertex, the posterior mean is

\[
\boxed{
M_R=\mu+\frac V\mu
}
\tag{7.3}
\]

if that departure is to the parent (equivalently a reuse event at `c=0`), while an outward departure to a newly discovered child gives

\[
\boxed{
M_N=\mu-\frac V{1-\mu}.
}
\tag{7.4}
\]

### Theorem 7.1 — exact first nonzero revisit-score expectation

For the four-transition walk started at the source root,

\[
\boxed{
E[B_4\mathcal S_4]
=
\frac V\beta
\left[
\eta(M_R-1)
-
\mu(M_N+M_R-1)
\right].
}
\tag{7.5}
\]

#### Proof

For the parent-return prefix `root -> v -> root -> v`, the prefix probability is `mu eta`: the first departure from `v` is to its parent with annealed probability `mu`, and on the next root departure the root chooses the already discovered child `v` with probability `E[1/Z]=eta`. At the second departure from `v`,

\[
B\text{-increment}=M_R-\mu=\frac V\mu,
\]

while the score accumulated before that departure is

\[
\mathcal S^-=rac{M_R-1}{\beta}.
\]

Its contribution to `E[B S]` is therefore

\[
\frac V\beta\eta(M_R-1).
\]

For the child-return prefix `root -> v -> w -> v`, the first outward move from fresh `v` has probability `1-mu`, and fresh `w` immediately returns to its parent with probability `mu`. At the second departure from `v`,

\[
B\text{-increment}=M_N-\mu=-\frac V{1-\mu},
\]

and the predeparture score is

\[
\mathcal S^-=rac{M_N+M_R-1}{\beta}.
\]

Multiplying by the prefix probability `(1-mu)mu` gives

\[
-\frac V\beta\mu(M_N+M_R-1).
\]

Adding the two prefixes proves (7.5). The fourth transition itself does not contribute because its score increment has conditional mean zero against the predictable `B` increment. QED.

---

## 8. Exact bounded-support adverse example

Take the source-valid family

\[
\boxed{
P(Z=2)=\frac1{1000},
\qquad
P(Z=30)=\frac{999}{1000},
\qquad
\beta=\frac23.
}
\tag{8.1}
\]

It has no leaves, bounded support and `beta d=4/3>1`. Exact arithmetic gives

\[
\mu=\frac6{125},
\qquad
V=\frac{111}{765625},
\qquad
\eta=\frac{169}{5000},
\tag{8.2}
\]

and

\[
M_R=\frac5{98},
\qquad
M_N=\frac{279}{5831}.
\tag{8.3}
\]

The bracket in (7.5) is

\[
\eta(M_R-1)-\mu(M_N+M_R-1)
=
\frac{651837}{58310000}>0.
\tag{8.4}
\]

Therefore

\[
\boxed{
E[B_4\mathcal S_4]
=
\frac{217061721}{89287187500000}
>0.
}
\tag{8.5}
\]

This is an **overall exact expectation**, not merely a positive-probability cylinder. It proves that the remaining revisit-history term in Theorem 5.1 can genuinely be adverse.

For orientation only, the exact four-step displacement derivative in this same example is still positive:

\[
\frac d{d\beta}E R_4
=
\frac{37216832523}{93789062500}
>0.
\tag{8.6}
\]

Thus (8.5) is not evidence against speed monotonicity. It is a rigorous obstruction to the proof mechanism that simply declares the revisit-score covariance nonpositive.

The mechanism is also transparent in (7.5). The parent-return route is favorable because `M_R-1<0`. The child-return route becomes adverse when

\[
M_N+M_R-1<0,
\]

which is typical at small `mu`; its weight is `mu`, whereas the root same-child return route is weighted by `eta=E[1/Z]`. A highly skewed large-degree law can therefore make the adverse child-return channel dominate.

---

## 9. What changed mathematically

The preceding report left the entire quantity `E[D_T S_T]` as an inter-vertex covariance. This run replaces it by a much narrower structure:

\[
\boxed{
\text{derivative}
=
\text{sum of local posterior-response margins}
-
2\times\text{revisit-only score transport}.
}
\]

The local posterior-update variance cancels exactly. First departures carry no nonlocal debt. The only cross-history term is a predictable posterior displacement paid on a later revisit, multiplied by score accumulated before that revisit.

Two additional facts now constrain that term:

* descendant-to-parent return odds contract monotonically with outward bias by (6.3);
* nevertheless the total revisit-score expectation need not have the favorable sign, and (8.5) is the earliest exact source-valid obstruction.

So the next proof cannot be a global sign argument. It must compare the **magnitude** of the adverse return channels with the local margin in (5.3).

---

## 10. Next attack

The next P03-B attack is an excursion-by-excursion charging theorem for (5.4).

For each revisit departure from `v`, assign it to the immediately preceding departure from `v` and the intervening excursion. Split excursions into:

1. **descendant excursions** `v -> child -> ... -> v`; and
2. **parent-side excursions** `v -> parent -> ... -> v`.

For descendant excursions, use (6.3) together with the earlier uniform return bound `h<=1/(beta d)` to control both the return probability and its bias response. The exact four-step formula says this channel can be adverse after a *new-child* posterior drop, so the target is a quantitative charge, not a sign claim.

For parent-side excursions, reuse the selected-ancestor stack and common-spine occupation bounds from the 0512Z–0715Z P03-B reports. Those bounds were designed precisely for historical parent-side returns and do not require pretending that the comparator branch is always fresh.

The concrete target is an inequality of the form

\[
E[B_T\mathcal S_T]
\le
E\sum_t \Gamma_t
\bigl[M_t(1-M_t)-j_tV_t\bigr],
\qquad \sup \Gamma_t<\frac1\beta,
\]

on a nontrivial bounded-support family. By (5.3), that would give a positive finite-horizon derivative margin and a clean object to transport through the Bowditch–Tokushige regeneration limit.

If this charge fails even for `{2,3}`, the fallback is now sharply defined: compute the exact excursion kernel under the reversible downcrossing chain from 032221Z and identify which return channel consumes the margin. No return to admission screens or repeated high-bias ranges is needed.

---

## 11. Obligation ledger

* Full-source Lyons–Pemantle–Peres conjecture: **OPEN**.
* Source outward-bias convention and reciprocal later literature: **PRESERVED**.
* P03-A latest 1106Z analytic result: **CONSUMED, NOT DUPLICATED**.
* Previous terminal covariance `E[D_T S_T]`: **STRICTLY REDUCED** to a revisit-only predictable covariance by Theorem 5.1.
* Local posterior-update variance `W_t`: **CANCELS EXACTLY** from the derivative.
* First departures from fresh vertices: **NO NONLOCAL HISTORY TERM** in Theorem 5.1.
* Child-to-parent return response: **NEW QUENCHED ODDS CONTRACTION**, (6.3).
* Universal sign conjecture `E[B_T S_T]<=0`: **FALSE**.
* Earliest adverse full expectation: **EXACTLY CERTIFIED AT T=4** by (7.5)–(8.5) in a bounded-support no-leaf family.
* Asymptotic speed monotonicity: **NOT CLAIMED** from finite horizons.
* Next bottleneck: **quantitative excursion charging of revisit-only score transport**.

`R_full: 1 -> 1`.

No force-push, no peer/historical overwrite, no public/email/Drive delivery.
