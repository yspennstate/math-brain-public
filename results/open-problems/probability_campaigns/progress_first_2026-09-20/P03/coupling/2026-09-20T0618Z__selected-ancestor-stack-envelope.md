Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.

# P03-B coupling report — selected-ancestor stack envelope and a support-ratio safety criterion

**Status:** PROVED PARTIAL / NEW RESTRICTED COUPLING LEMMAS. The full Lyons–Pemantle–Peres speed-monotonicity conjecture remains unresolved. This run advances the probabilistic coupling line by controlling an *entire repeated-return stack at one outward-selected ancestor*, rather than only the first post-split step. The result is rigorous but deliberately restricted: the comparator branch is required to be fresh at each synchronized comparison. The remaining full problem is to remove that freshness restriction and sum over multiple historically selected ancestors.

**Native role:** P03-B, `6aabe777361481919c9e614646464772`, regeneration/coupling and source-valid counterexample role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`.

**Captured master before write:** `67d34b96486242fb75349d3ae745a23ba4f43616`.

**Previous own checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T0512Z__outward-selection-variance-debt.md`, creation commit `fa4bb4069fe0efe8311218b0cd6da6213a0516bb`.

**Complementary P03-A checkpoint consumed, not duplicated:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0603Z__critical-edge-speed-asymptotic.md`, creation commit `76cc4d0d07441f633977c9c2978d13fdce90d1cb`. P03-A now has a critical-edge speed asymptotic near parent bias `lambda -> E Z`; this report does not rederive its escape-probability identities.

## 1. Minimal source continuity and exact convention

Primary coupling source: Gérard Ben Arous, Alexander Fribergh and Vladas Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865, https://arxiv.org/abs/1111.5865 . The source assumes a Galton–Watson offspring variable `Z` with

\[
P(Z=0)=0,
\]

and uses **outward child bias** `beta`: at a non-root vertex with `k` children,

\[
q_k(\beta):=P_\beta(\text{parent})=\frac1{1+\beta k},
\qquad
P_\beta(\text{a specified child})=\frac\beta{1+\beta k}.
\tag{1.1}
\]

Thus increasing `beta` means stronger bias away from the root. The transient interval is `beta>1/EZ`, and the source conjecture asks that the speed `v(beta)` be increasing throughout that interval. The arXiv abstract still displays the old high-bias constant `717`; this report does not confuse that historical range with later improvements or with the full conjecture.

Bowditch--Tokushige, arXiv:1906.07913, prove differentiability in the ballistic/CLT regime and represent the derivative through a Gaussian covariance; arXiv:2006.03433 proves analyticity in the ballistic regime. These do not supply the derivative sign. The current broad primary monotonicity theorem retained by the campaign is He Song, Longmin Wang and Kainan Xiang, *Journal of Applied Probability* 62 (2025), 1044--1052, DOI `10.1017/jpr.2024.113`: in their reciprocal parent-bias parameter `lambda=1/beta`, and minimum offspring `m_1>=2`, the speed is strictly decreasing on

\[
0\le \lambda\le \frac{m_1}{1+\sqrt{1-1/m_1}}.
\tag{1.2}
\]

This is consistent with increasing speed in outward `beta`. A bounded literature refresh on 20 September 2026 did not surface a full-source resolution; this negative search is not treated as proof of worldwide openness.

The fixed full-source metric remains

`R_full: 1 -> 1`.

## 2. Inherited obstruction and target of this run

Assume in the coupling part that

\[
d\le Z\le D<\infty,\qquad \beta d>1.
\tag{2.1}
\]

Set

\[
Q:=q_Z(\beta),\qquad
\mu:=EQ,
\qquad
a:=q_d(\beta),\qquad b:=q_D(\beta).
\tag{2.2}
\]

The previous P03-B report proved that conditioning a fresh vertex to have been traversed outward tilts its degree distribution by the factor `1-Q`, and therefore lowers its expected future parent threshold by

\[
\mu-E[Q\mid\text{one outward traversal}]
=\frac{\operatorname{Var}(Q)}{1-\mu}>0
\tag{2.3}
\]

for every nonregular law. That negative selection effect survives at first order in a `beta -> beta+epsilon` derivative calculation. It also proved that the *first* selected-ancestor step cannot erase the generating `+2` favorable split.

The unresolved question was whether repeated returns to the **same** selected ancestor can accumulate enough debt to erase that `+2` credit. This report controls that whole one-ancestor stack under a clean comparator condition.

## 3. Exact outward-only posterior stack identity

Before adding return probabilities, it is useful to solve the pure degree-selection problem exactly.

For `n>=0`, define

\[
A_n:=E(1-Q)^n,
\qquad
\mu_n:=\frac{E[Q(1-Q)^n]}{A_n}.
\tag{3.1}
\]

Thus `mu_n` is the posterior mean parent threshold after observing `n` outward departures from the same initially fresh vertex, if no other information about that vertex is used. Since the likelihood `(1-Q)^n` favors small `Q`, the sequence `mu_n` is nonincreasing.

For `0<rho<=1`, put

\[
\mathcal S_\rho
:=\sum_{n\ge0}\rho^n A_n(\mu-\mu_n).
\tag{3.2}
\]

### Lemma 3.1 — exact discounted posterior-selection debt

Let

\[
G_\rho:=E\frac1{1-\rho(1-Q)}.
\tag{3.3}
\]

Then

\[
\boxed{
\mathcal S_\rho
=\frac{(1-\rho+\rho\mu)G_\rho-1}{\rho}.
}
\tag{3.4}
\]

At `rho=1`,

\[
\boxed{
\mathcal S_1
=\mu E\frac1Q-1
=\frac12E\frac{(Q-Q')^2}{QQ'},
}
\tag{3.5}
\]

where `Q'` is an independent copy of `Q`. In the present Galton–Watson parametrization,

\[
\boxed{
\mathcal S_1
=(1+\beta EZ)E\frac1{1+\beta Z}-1.
}
\tag{3.6}
\]

#### Proof

Because

\[
E[Q(1-Q)^n]=A_n-A_{n+1},
\]
we have

\[
A_n(\mu-\mu_n)=A_{n+1}-(1-\mu)A_n.
\]

Also

\[
\sum_{n\ge0}\rho^nA_n=G_\rho,
\qquad
\sum_{n\ge0}\rho^nA_{n+1}=\frac{G_\rho-1}{\rho}.
\]

Substitution gives (3.4). For `rho=1`, `G_1=E(1/Q)`, yielding the first equality in (3.5). For iid `Q,Q'`,

\[
\frac12E\left(\frac Q{Q'}+\frac{Q'}Q-2\right)
=EQ\,E\frac1Q-1,
\]

which is the second equality. Finally `1/Q=1+beta Z`, proving (3.6). QED.

### Two-point specialization

If

\[
P(Q=a)=1-\theta,\qquad P(Q=b)=\theta,
\qquad a>b,
\]
then direct simplification gives

\[
\boxed{
\mathcal S_\rho
=\frac{\rho\theta(1-\theta)(a-b)^2}
{(1-\rho+\rho a)(1-\rho+\rho b)}.
}
\tag{3.7}
\]

At `rho=1`,

\[
\boxed{
\mathcal S_1
=\theta(1-\theta)\frac{(a-b)^2}{ab}.
}
\tag{3.8}
\]

This isolates heterogeneity exactly: the pure outward-selection debt is zero on a regular tree and quadratic in the threshold separation for a near-regular two-point law.

**Scope warning.** Equations (3.4)--(3.8) are exact for outward observations with degree-independent discounting. Actual returns through a tree carry additional history. They are therefore a diagnostic and a component of the coupling proof, not by themselves a full return-stack theorem.

## 4. Uniform return bound from the minimum degree

Define

\[
r:=\frac1{\beta d}=\frac{a}{1-a}<1.
\tag{4.1}
\]

### Lemma 4.1 — a child returns to its parent with probability at most `r`

For any vertex `v` and any child `w` of `v`, a `beta`-biased walk started at `w` satisfies

\[
\boxed{
P_w(T_v<\infty)\le r=\frac1{\beta d}.
}
\tag{4.2}
\]

#### Proof

Let `H_n` be distance from `v` until hitting `v`. At a vertex with `k>=d` children, the probability of decreasing `H` is

\[
q_k(\beta)\le a,
\]

and the probability of increasing it is at least `1-a`. Since `r=a/(1-a)`,

\[
q_k r^{-1}+(1-q_k)r
\le a r^{-1}+(1-a)r=1.
\]

Hence `r^{H_{n\wedge T_v}}` is a bounded supermartingale after truncation at a distant level. Optional stopping between levels `0` and `N`, followed by `N->infinity`, gives

\[
P_w(T_v<\infty)\le r^{H_0}=r.
\]

QED.

This is exactly the one-dimensional return parameter already underlying the super-regeneration construction.

## 5. New clean-stack theorem: one selected ancestor cannot accumulate arbitrary debt

Consider the following source-valid local configuration after a favorable split.

* A vertex `p` was initially fresh and, before the split, the common walk traversed it outward once. Thus its threshold `Q_p` has the outward-selected law

\[
P_{\rm out}(Q\in dq)
=\frac{1-q}{1-\mu}P(Q\in dq).
\tag{5.1}
\]

* The less-biased `beta` branch can return to `p`, depart outward again, and return repeatedly.
* At each synchronized comparison involving `p`, the `(beta+epsilon)` branch is at a fresh independent Galton–Watson vertex. This is the **clean comparator restriction** of the theorem.

Let `V` be the number of visits to `p` at which such a comparison occurs, counting the current visit. Conditional on `Q_p=q`, every *additional* visit requires an outward departure from `p`, probability `1-q`, followed by a return from the chosen child, probability at most `r` by Lemma 4.1. By the strong Markov property, at every stage

\[
P(V\ge n+1\mid Q_p=q)\le [r(1-q)]^n,
\]
so

\[
\boxed{
E[V\mid Q_p=q]\le\frac1{1-r(1-q)}.
}
\tag{5.2}
\]

Let

\[
\mu_+(\epsilon):=E q_Z(\beta+\epsilon)\le\mu.
\]

At one comparison with `p`, after averaging the fresh comparator degree, the common-uniform radial-gap increment has mean

\[
2(q-\mu_+(\epsilon)).
\]

Therefore its adverse part is bounded by `2(mu-q)_+`. Summing over the whole visit stack gives the following.

### Theorem 5.1 — full one-ancestor clean-stack envelope

Under (2.1) and the clean comparator restriction,

\[
\boxed{
E[\text{total radial-gap increment generated by the selected ancestor }p]
\ge -2\mathcal D_{\rm stack},
}
\tag{5.3}
\]

where

\[
\boxed{
\mathcal D_{\rm stack}
:=E_{\rm out}\left[
\frac{(\mu-Q)_+}{1-r(1-Q)}
\right].
}
\tag{5.4}
\]

In particular, since `b<=Q<=a`,

\[
\boxed{
\mathcal D_{\rm stack}
\le
\frac{a-b}{1-r(1-b)}.
}
\tag{5.5}
\]

Consequently, if

\[
\boxed{
\frac{a-b}{1-r(1-b)}<1,
}
\tag{5.6}
\]

then the **entire repeated-return stack at this one selected ancestor cannot erase the `+2` credit of the favorable split that created it**, within the clean comparator model.

#### Proof

Equation (5.2) and Tonelli give

\[
E_{\rm out}\sum_{j=1}^{V}(\mu-Q)_+
\le
E_{\rm out}\left[
\frac{(\mu-Q)_+}{1-r(1-Q)}
\right].
\]

At each visit the finite-`epsilon` fresh comparator has mean threshold `mu_+(epsilon)<=mu`, so replacing `mu_+` by `mu` can only enlarge the adverse bound. The common-uniform radial increment equals twice the signed threshold difference after averaging the fresh comparator degree, yielding (5.3)--(5.4). For (5.5), use

\[
(\mu-Q)_+\le a-b,
\qquad
1-r(1-Q)\ge1-r(1-b).
\]

If (5.6) holds, the total expected adverse amount is strictly less than `2`, hence cannot cancel the generating `+2` split credit. QED.

## 6. Explicit support-ratio criterion

Write

\[
x:=\beta d>1,
\qquad
\kappa:=\frac Dd\ge1.
\tag{6.1}
\]

Then

\[
a=\frac1{1+x},
\qquad
b=\frac1{1+\kappa x},
\qquad
r=\frac1x.
\]

A direct simplification of the support envelope in (5.5) gives

\[
\boxed{
\frac{a-b}{1-r(1-b)}
=
\frac{(\kappa-1)x}
{(1+x)(1+\kappa x-\kappa)}.
}
\tag{6.2}
\]

The right side is `<1` exactly when

\[
\boxed{
F(x,\kappa):=
\kappa x^2-\kappa x-\kappa+2x+1>0.
}
\tag{6.3}
\]

This has two convenient consequences.

### Corollary 6.1 — support width at most a factor three

If

\[
\boxed{D\le3d,}
\tag{6.4}
\]

then (5.6) holds for **every** `beta d>1`.

Indeed `F(1,kappa)=3-kappa>=0`, while

\[
\partial_xF=2\kappa x-\kappa+2>0
\quad\text{for }x\ge1,
\]
so strict positivity holds as soon as `x>1`.

### Corollary 6.2 — sufficiently strong outward drift removes any support-ratio restriction

Let

\[
\varphi:=\frac{1+\sqrt5}{2}.
\]

If

\[
\boxed{\beta d\ge\varphi,}
\tag{6.5}
\]

then `x^2-x-1>=0`, so

\[
F(x,\kappa)=\kappa(x^2-x-1)+2x+1>0
\]

for every finite `D/d`.

For `1<x<varphi`, the exact sufficient support-ratio condition is

\[
\boxed{
\kappa<\frac{2x+1}{1+x-x^2}.
}
\tag{6.6}
\]

The threshold equals `3` at `x=1` and diverges as `x` approaches `varphi` from below.

These criteria are **not** new speed-monotonicity intervals by themselves. They prove that one specific negative mechanism — repeated visits to a single outward-selected ancestor while the other branch remains fresh — is quantitatively incapable of destroying its generating split credit.

## 7. Exact bounded-support certificate: `{2,6}`

Return to the nontrivial test family used in the preceding P03-B obstruction:

\[
P(Z=2)=P(Z=6)=\frac12.
\tag{7.1}
\]

Here `D/d=3`, so Corollary 6.1 applies throughout

\[
\boxed{\beta>\frac12.}
\tag{7.2}
\]

Thus, even arbitrarily close to the auxiliary critical line `beta d=1`, the whole clean selected-ancestor return stack cannot erase the favorable split credit.

At the previous exact test point `beta=3/5`,

\[
a=\frac5{11},
\qquad b=\frac5{23},
\qquad \mu=\frac{85}{253},
\qquad r=\frac56.
\]

The support-only envelope is

\[
\boxed{
\frac{a-b}{1-r(1-b)}=\frac{15}{22}<1.
}
\tag{7.3}
\]

Using the actual two-point law inside (5.4) is much sharper. Only the `Z=6` atom contributes to `(mu-Q)_+`, and

\[
\boxed{
\mathcal D_{\rm stack}
\le
\frac{\tfrac12(1-b)}{1-\mu}
\frac{\mu-b}{1-r(1-b)}
=\frac{45}{224}
\approx0.2008928571.
}
\tag{7.4}
\]

Hence the full one-ancestor clean stack leaves at least

\[
\boxed{
2\left(1-\frac{45}{224}\right)
=\frac{179}{112}
\approx1.598214286
}
\tag{7.5}
\]

of expected radial-gap credit from the original `+2` split, before accounting for any additional favorable events.

This is an exact rational certificate, not a simulation. It also shows why the previous one-step negative cylinder was not yet the right scale: in this family the selected ancestor can be locally adverse, but the entire repeated-return stack at that ancestor is still far too small to reverse the original split under fresh comparison.

## 8. What changed mathematically

### Previous result

The preceding P03-B run identified an `O(epsilon)` negative outward-selection variance debt at the first selected ancestor and proved only one-step safety.

### New theorem / bound

This run proves:

1. the exact posterior-stack identity (3.4)--(3.8), reducing pure repeated outward selection to the heterogeneity functional `EQ * E(1/Q)-1`;
2. the uniform tree return bound `P(child returns to parent)<=1/(beta d)` by a radial supermartingale;
3. the full one-selected-ancestor clean-stack bound (5.3)--(5.5);
4. an explicit support-ratio safety region (6.3)--(6.6);
5. in particular, **all bounded-support laws with `D<=3d` satisfy clean one-ancestor stack safety for every `beta d>1`**;
6. for `{2,6}` at `beta=3/5`, the exact clean-stack debt envelope is `45/224`, leaving at least `179/112` of the split's expected radial-gap credit.

The full-source metric remains unchanged because the comparator-freshness assumption is not yet justified globally.

## 9. Remaining obstruction

The next obstruction is now narrower than in the previous report.

A real post-split coupling block does not keep one branch fresh forever. The `(beta+epsilon)` branch can itself revisit previously exposed vertices, while the `beta` branch may move through a **stack of several selected ancestors**. Therefore the missing global step is not control of repeated returns to one ancestor; that piece is now bounded. The missing object is a two-sided history process carrying

\[
(\text{selected-threshold posterior on the lower branch},
\text{selected-threshold posterior on the higher branch}).
\]

The exact downcrossing chain from `2026-09-20T032221Z__exact-backstep-law-and-backstep-only-debt.md` supplies the natural return clock. The posterior identity (3.4) supplies the exact degree-selection cost when return thinning is degree-independent. The remaining question is how much additional tilt is created by revisiting already explored child subtrees.

## 10. Next attack

The next P03-B run should avoid another local one-step estimate and attack the two-sided history directly:

1. Define for each active ancestor its posterior threshold `M_h=E[Q | local traversal history h]` and prove a recursion when one more outward-return cycle is appended.
2. Couple that recursion to the reversible downcrossing chain `D_j`. The target inequality is a blockwise budget

\[
E\sum_{\text{selected ancestors }a}
\frac{(M_{\rm fresh}-M_a)_+}
{1-r(1-M_a)}<1
\]

in a nontrivial support family, first `{2,6}` or `{2,3}`.
3. If the two-sided history process violates this budget, extract an exact finite-depth cylinder proving that **multi-ancestor selection**, rather than single-ancestor recurrence, is the genuine obstruction. That would justify a clean pivot to the Bowditch--Tokushige covariance/spine representation.

No simulation result will be treated as proof of speed monotonicity.

## 11. Obligation ledger

| Obligation | Before | After this run |
|---|---|---|
| exact source bias convention | proved | unchanged |
| current broad published monotonicity range | checked | refreshed 2026-09-20 |
| pointwise local derivative positivity | rigorously false | unchanged |
| first selected-ancestor debt | exact one-step formula | strengthened to full one-ancestor clean-stack envelope |
| repeated outward-selection posterior | qualitative | exact transform identity (3.4) |
| tree return kernel | auxiliary one-dimensional heuristic | rigorous `<=1/(beta d)` tree bound |
| `{2,6}`, `beta=3/5` | first-step negative cylinder | whole clean selected-ancestor stack debt `<=45/224<1` |
| multi-ancestor/two-sided history | open | now isolated as principal coupling obstruction |
| full-source monotonicity | open | open |

**Stagnation:** no. The full-source metric is unchanged, but the previous one-step safety statement has been replaced by an infinite-return-stack theorem on a source-valid restricted configuration, and the unresolved mechanism is strictly narrower.
