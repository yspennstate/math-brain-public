Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.

# P03-B coupling report — exact local-history Bayes filter, sharp reversal horizon, and a regeneration-tail budget

**Status:** PROVED PARTIAL / NEW PROBABILISTIC LEMMAS / SOURCE-VALID OBSTRUCTION. The full Lyons–Pemantle–Peres speed-monotonicity conjecture remains unresolved. This run does not repeat the old high-bias proof and does not claim a new source-wide monotonicity interval. It attacks the remaining post-split self-history mechanism from the preceding P03-B report by exactly filtering the offspring degree of a repeatedly visited vertex from its local path history.

**Native role:** P03-B, `6aabe777361481919c9e614646464772`, regeneration/coupling and counterexample-search role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`.

**Captured master immediately before write:** `096cd70d196edc7013da42ad1bc10e3b6a49104b`.

**Previous own mathematical checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T0715Z__common-spine-occupation-debt.md`, creation commit `e152e40cfc696bc434ea4228bc5ccb45ed0c57be`, together with the immutable root-boundary clarification `2026-09-20T0729Z__common-spine-root-boundary-clarification.md`, creation commit `c9b2efd3cc46dc1efd7a9c7c3ca42bd3c31d7a3a`.

**Complementary P03-A work consumed, not duplicated:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0705Z__terminal-critical-monotonicity-by-normalized-contraction.md`. That line controls recursive escape/speed identities near the critical edge. The present report stays probabilistic and local-history/regeneration based.

## 1. Minimal source continuity

Primary source: Gérard Ben Arous, Alexander Fribergh and Vladas Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865, https://arxiv.org/abs/1111.5865 . The source model is a supercritical Galton–Watson tree without leaves, and at a non-root vertex with `k` children uses **outward child bias** `beta`:

\[
q_k(\beta):=P_\beta(\text{parent}\mid k)=\frac1{1+\beta k},
\qquad
P_\beta(\text{each specified child}\mid k)=\frac\beta{1+\beta k}=\beta q_k(\beta).
\tag{1.1}
\]

Thus increasing `beta` pushes outward. Bowditch--Tokushige, arXiv:1906.07913, prove differentiability in the ballistic/CLT regime and give a Gaussian-covariance derivative representation; arXiv:2006.03433 later gives analyticity in the ballistic regime. The strongest broad later monotonicity theorem retained in the campaign is He Song, Longmin Wang and Kainan Xiang, *J. Appl. Probab.* 62 (2025), 1044--1052, DOI `10.1017/jpr.2024.113`, in reciprocal parent bias `lambda=1/beta`: for minimum offspring `d>=2`, speed is strictly decreasing for

\[
0\le \lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\tag{1.2}
\]

No inverse-bias contradiction is inferred. The fixed full-source metric remains

`R_full: 1 -> 1`.

For the coupling lemmas below, as in the preceding P03-B run, assume the source-valid restricted family

\[
2\le d\le Z\le D<\infty,\qquad \beta d>1.
\tag{1.3}
\]

The post-root super-regeneration convention from the `0729Z` clarification is retained, so root boundary effects are not silently included in the non-root formulas.

## 2. Previous result and the unresolved mechanism

The preceding run proved a quenched occupation bound for any non-root ancestral geodesic `Gamma`. With

\[
r:=\frac1{\beta d},
\qquad
s:=\frac{(d-1)(\beta d-1)}{d(1+\beta d)},
\tag{2.1}
\]

if `N_Gamma` is the number of visits to `Gamma` before the relevant stopping time, then

\[
P(N_\Gamma\ge n)\le(1-s)^{n-1},
\qquad EN_\Gamma\le s^{-1}.
\tag{2.2}
\]

This controlled all reverse-mismatch debt occurring on the **pre-split common ancestral spine**. The unresolved part was post-split self-history: a branch can repeatedly revisit vertices created after the split, and the degree distribution at such a historical vertex is no longer the raw offspring law after conditioning on the local path.

A worst-pair replacement `q_d-q_D` discards almost all of that structure. The goal here is to recover it exactly.

## 3. Exact posterior law from a canonical local departure history

Fix a non-root vertex `v`. Let its offspring count be

\[
K\sim\pi,
\tag{3.1}
\]

where initially `pi` is any law supported on `{d,...,D}`. In a fresh Galton–Watson vertex one takes `pi` to be the offspring law itself.

Observe only departures **from `v`**. Canonically relabel children by order of first discovery: the first child ever used is label 1, the next previously unseen child is label 2, and so on. Suppose a finite local departure record has

* `n` total departures from `v`;
* `o` child departures and `n-o` parent departures;
* exactly `c` distinct child identities among those child departures.

Write

\[
(k)_c=k(k-1)\cdots(k-c+1),
\]

with `(k)_c=0` for `k<c`.

### Lemma 3.1 — exact local-history likelihood

For every fixed canonical equality pattern of the child labels,

\[
\boxed{
P_\beta(\text{that local record}\mid K=k)
=C_{\rm rec}\,(k)_c\,\beta^o q_k(\beta)^n,
}
\tag{3.2}
\]

where `C_rec` is independent of `k`. Consequently the posterior law of `K` given the canonical local record is

\[
\boxed{
\pi_{n,c}^{(\beta)}(k)
=
\frac{\pi(k)(k)_c(1+\beta k)^{-n}}
{\sum_j\pi(j)(j)_c(1+\beta j)^{-n}}.
}
\tag{3.3}
\]

In particular, after the equality pattern is retained, the number of parent versus child departures no longer appears separately: all `k`-dependence is carried by `n` and `c`.

#### Proof

Given `K=k`, every parent departure contributes `q_k(beta)` and every departure to one **specified** child contributes `beta q_k(beta)`. A canonical record with `c` discovered child identities can be embedded into the `k` actual child labels in exactly `(k)_c` injective ways. Therefore summing over those embeddings gives

\[
(k)_c(\beta q_k)^o q_k^{n-o}
=(k)_c\beta^o q_k^n,
\]

up to a record-dependent combinatorial factor independent of `k`. Bayes' rule gives (3.3). QED.

### Excursions outside `v` do not add hidden `K`-dependence

For the annealed Galton–Watson law, once the identity of the chosen neighboring edge is fixed, the environment in that neighboring subtree is independent of `K`. Thus finite return/non-return behavior during an excursion through a chosen child contributes a factor independent of `K`; the same is true of the parent-side environment because offspring numbers at distinct vertices are independent. The local degree information in a path can therefore be deferred to the canonical departure record above. This is the precise probabilistic sense in which (3.3) applies inside regeneration episodes.

Define the partition function and posterior parent-threshold mean

\[
Z_{n,c}(\beta):=
\sum_k\pi(k)(k)_c(1+\beta k)^{-n},
\tag{3.4}
\]

\[
\boxed{
M_{n,c}(\beta)
:=E_{\pi_{n,c}^{(\beta)}}q_K(\beta)
=\frac{Z_{n+1,c}(\beta)}{Z_{n,c}(\beta)}.
}
\tag{3.5}
\]

This ratio is the exact annealed parent-threshold seen at the next visit to `v`, given its local record.

## 4. Discovery versus reuse: an exact Bayes martingale

At a local state `(n,c)`, write under the posterior (3.3)

\[
Q:=q_K(\beta),
\qquad M:=EQ,
\qquad V:=\operatorname{Var}(Q),
\qquad \alpha_c:=1+\beta c.
\tag{4.1}
\]

The next departure from `v` is put into one of two categories:

* `R` (reuse): the parent or one of the `c` already discovered children;
* `N` (new): a child not previously used from `v`.

Given `K`,

\[
P(R\mid K)=(1+\beta c)Q=\alpha_c Q,
\tag{4.2}
\]

because the parent has probability `Q` and each known child has probability `beta Q`, while

\[
P(N\mid K)=1-\alpha_c Q.
\tag{4.3}
\]

Hence

\[
P(R)=\alpha_c M,
\qquad P(N)=1-\alpha_c M.
\tag{4.4}
\]

### Lemma 4.1 — exact posterior jumps

If `M^R` and `M^N` denote the posterior means of `Q` after the next departure category, then

\[
\boxed{
M^R=M+\frac{V}{M},
}
\tag{4.5}
\]

and, whenever `P(N)>0`,

\[
\boxed{
M^N
=M-\frac{\alpha_c V}{1-\alpha_c M}.
}
\tag{4.6}
\]

Thus reuse pushes the inferred parent threshold upward, while discovery of a new child pushes it downward. The two effects compensate exactly:

\[
\boxed{
E[M_{\rm next}\mid\mathcal F]=M.
}
\tag{4.7}
\]

#### Proof

On `R`, the posterior is tilted by `Q`, up to the constant `alpha_c`, so

\[
M^R=\frac{EQ^2}{EQ}=M+\frac VM.
\]

On `N`, the tilt is `1-alpha_c Q`, so

\[
M^N
=\frac{E[Q(1-\alpha_c Q)]}{1-\alpha_c M}
=\frac{M-\alpha_c(V+M^2)}{1-\alpha_c M}
=M-\frac{\alpha_cV}{1-\alpha_cM}.
\]

Multiplying the two increments by the probabilities in (4.4) gives `+alpha_c V` and `-alpha_c V`, proving (4.7). QED.

This corrects a conceptual weakness in a purely outward-selection picture: a repeatedly visited vertex is not monotonically tilted toward high or low degree. **Reuse and fresh-child discovery form an exact Bayesian martingale pair.**

### Lemma 4.2 — stopped information budget

Let `M_t` be this posterior-mean process along successive local departures and let `N` be any almost surely finite stopping time for the local path/excursion filtration. Put `V_t=Var(Q|F_t)` and `alpha_t=1+beta c_t`. Then

\[
\boxed{
E\sum_{t<N}
\frac{\alpha_tV_t^2}
{M_t(1-\alpha_tM_t)}
=E[M_N^2]-M_0^2
\le \operatorname{Var}(Q_0).
}
\tag{4.8}
\]

Moreover the expected accumulated **upward** posterior movement satisfies

\[
\boxed{
E\sum_{t<N}(M_{t+1}-M_t)_+
=E\sum_{t<N}\alpha_tV_t
\le\frac12\sqrt{\operatorname{Var}(Q_0)\,EN}.
}
\tag{4.9}
\]

#### Proof

By (4.5)--(4.6), the conditional second moment of the martingale increment is

\[
\alpha_tM_t\left(\frac{V_t}{M_t}\right)^2
+(1-\alpha_tM_t)
\left(\frac{\alpha_tV_t}{1-\alpha_tM_t}\right)^2
=
\frac{\alpha_tV_t^2}{M_t(1-\alpha_tM_t)}.
\]

Orthogonality of martingale differences and localization give the equality in (4.8). Since `M_N=E[Q_0|F_N]`, Jensen gives `E M_N^2<=E Q_0^2`, proving the upper bound.

For (4.9), the conditional expected positive jump is exactly `alpha_t V_t`. Write

\[
\alpha_tV_t
=
\sqrt{\frac{\alpha_tV_t^2}{M_t(1-\alpha_tM_t)}}
\sqrt{\alpha_tM_t(1-\alpha_tM_t)}.
\]

Cauchy--Schwarz over time and probability, (4.8), and `x(1-x)<=1/4` give (4.9). QED.

This is a genuine control on the history-selection mechanism: raw revisit count is replaced by posterior variance/information. It does **not** yet identify the full speed derivative because a regeneration stopping rule weights different local histories differently.

## 5. Exact derivative of the local posterior threshold

The previous martingale describes selection at fixed `beta`. For speed monotonicity we must also know how the conditioned threshold itself moves when `beta` changes.

Keep a fixed canonical local record `(n,c)` and a `beta`-independent prior `pi`. Under (3.3), let

\[
M=M_{n,c}(\beta),
\qquad V=\operatorname{Var}_{\pi_{n,c}^{(\beta)}}(Q).
\]

### Theorem 5.1 — exact derivative and selection/direct decomposition

\[
\boxed{
\frac{d}{d\beta}M_{n,c}(\beta)
=
\frac1\beta\Big((n+1)V-M(1-M)\Big).
}
\tag{5.1}
\]

The term `-M(1-M)/beta` is the direct effect of increasing outward bias. The term `(n+1)V/beta` is the adverse history-selection correction. Therefore a fixed local history can make the inferred parent threshold move in the **wrong direction** only if

\[
\boxed{
(n+1)V>M(1-M).
}
\tag{5.2}
\]

#### Proof

For `Q=q_K(beta)`,

\[
Q'=-\frac1\beta Q(1-Q).
\tag{5.3}
\]

The posterior weight in (3.3) is proportional to `Q^n` times the beta-independent factor `pi(k)(k)_c`, so its log-derivative, modulo an additive constant that disappears in covariance, is

\[
-\frac n\beta(1-Q)
\equiv \frac n\beta Q.
\]

Differentiating an expectation under a moving probability law gives

\[
M'
=E Q'+\frac n\beta\operatorname{Var}(Q)
=-\frac1\beta E[Q(1-Q)]+\frac n\beta V.
\]

Since `E[Q(1-Q)]=M-M^2-V`, (5.1) follows. QED.

This formula is distinct from P03-A's recursive escape derivative: it is a local annealed history filter for the coupling/spine mechanism.

## 6. A sharp support-uniform safe-history horizon

Put

\[
a:=q_d(\beta)=\frac1{1+\beta d},
\qquad
b:=q_D(\beta)=\frac1{1+\beta D}.
\tag{6.1}
\]

Then `b<=Q<=a`. Bhatia--Davis gives

\[
V\le(a-M)(M-b).
\tag{6.2}
\]

The ratio in (5.2) can be optimized exactly. For `M in [b,a]`,

\[
\frac{(a-M)(M-b)}{M(1-M)}
\le
\left(\sqrt{a(1-b)}-\sqrt{b(1-a)}\right)^2.
\tag{6.3}
\]

Indeed, with `t=M/(1-M)`, the left side becomes

\[
a+b-2ab-\frac{ab}{t}-(1-a)(1-b)t,
\]

whose maximum occurs at

\[
t=\sqrt{\frac{ab}{(1-a)(1-b)}}.
\]

Define the exact support heterogeneity coefficient

\[
\boxed{
\rho_{d,D}(\beta)
:=
\left(\sqrt{a(1-b)}-\sqrt{b(1-a)}\right)^2
=
\frac{\beta(\sqrt D-\sqrt d)^2}
{(1+\beta d)(1+\beta D)}.
}
\tag{6.4}
\]

### Theorem 6.1 — sharp uniform local monotonicity horizon

For **every** offspring prior supported on `{d,...,D}`, every canonical local history with `n` departures and any possible number `c` of discovered children,

\[
\boxed{
\frac{d}{d\beta}M_{n,c}(\beta)
\le
\frac{M(1-M)}\beta
\left((n+1)\rho_{d,D}(\beta)-1\right).
}
\tag{6.5}
\]

Consequently

\[
\boxed{
(n+1)\rho_{d,D}(\beta)\le1
\quad\Longrightarrow\quad
\frac{d}{d\beta}M_{n,c}(\beta)\le0
}
\tag{6.6}
\]

uniformly over the local history.

The criterion is sharp as a **uniform-over-offspring-laws** statement. If

\[
(n+1)\rho_{d,D}(\beta)>1
\tag{6.7}
\]

and `c<=d`, choose a two-point law on `{d,D}`. By varying its mixing weight, the posterior mean after the fixed `(n,c)` history can be tuned to the maximizer in (6.3); endpoint support also makes Bhatia--Davis equality exact. Hence there exists a source-valid two-point offspring law and a positive-probability local history for which

\[
\boxed{
\frac{d}{d\beta}M_{n,c}(\beta)>0.
}
\tag{6.8}
\]

Thus a proof strategy asserting that every history-conditioned parent threshold decreases with outward bias is impossible in full bounded-support generality.

### Proof of sharpness

For a law with masses `1-theta,theta` at `d,D`, the posterior odds are

\[
\frac{P(K=D\mid n,c)}{P(K=d\mid n,c)}
=
\frac\theta{1-\theta}
\frac{(D)_c}{(d)_c}
\left(\frac{q_D(\beta)}{q_d(\beta)}\right)^n.
\tag{6.9}
\]

For `c<=d`, the multiplier after `theta/(1-theta)` is finite and positive, so as `theta` runs from 0 to 1 the posterior mixing weight covers `(0,1)`. One can therefore realize the optimizing `M` in (6.3). Equations (5.1)--(6.3) then make the sign positive exactly when (6.7) holds. QED.

This is both a positive lemma and an obstruction: **short local histories are uniformly safe; sufficiently long histories can genuinely reverse the local beta-response.**

## 7. Exact bounded-support counterexample to pointwise posterior monotonicity

Take the source-valid no-leaf offspring law

\[
P(K=2)=\frac1{1000},
\qquad
P(K=30)=\frac{999}{1000},
\tag{7.1}
\]

and outward bias

\[
\beta=\frac23,
\qquad \beta d=\frac43>1.
\tag{7.2}
\]

Consider a canonical local record with

\[
n=4,\qquad c=1,
\tag{7.3}
\]

for example four departures to the same discovered child, together with any finite return cylinder needed to revisit `v`. Those return factors are independent of `K` and cancel from the local posterior.

The exact posterior calculation gives

\[
P(K=30\mid n=4,c=1)=\frac{185}{266},
\tag{7.4}
\]

\[
M_{4,1}\!\left(\frac23\right)
=\frac{457}{2793},
\qquad
V_{4,1}\!\left(\frac23\right)
=\frac{26640}{866761}.
\tag{7.5}
\]

Substitution into (5.1) yields the **exact positive derivative**

\[
\boxed{
M'_{4,1}\!\left(\frac23\right)
=\frac{65624}{2600283}>0.
}
\tag{7.6}
\]

So, on this positive-probability finite source cylinder, increasing the outward bias makes the **history-conditioned expected parent threshold increase**. This is not a counterexample to speed monotonicity. It is a rigorous counterexample to the proposed local mechanism `history-conditioned q always decreases with beta`.

The sharp-horizon coefficient here is

\[
\rho_{2,30}\!\left(\frac23\right)
=
\frac{2(\sqrt{30}-\sqrt2)^2}{147}
\approx0.2245995458,
\tag{7.7}
\]

so `1/rho≈4.45237`; the first potentially unsafe history length is indeed `n=4`.

## 8. New regeneration-tail bound for dangerous local histories

The obstruction above only appears after a vertex has accumulated enough departures. The preceding geometric spine occupation theorem therefore suppresses it.

Fix one historical non-root vertex `v` inside the post-root regeneration block. Let `N_v` be its number of departures before the block is stopped. Because visits to `v` are a subset of visits to an ancestral spine through `v`, (2.2) gives

\[
\boxed{
P(N_v>n)\le(1-s)^n,
\qquad n\ge0.
}
\tag{8.1}
\]

Assume `D>d`; the regular case has `rho=0` and no local reversal at all. Define

\[
\boxed{
L:=\left\lfloor\rho_{d,D}(\beta)^{-1}\right\rfloor.
}
\tag{8.2}
\]

By Theorem 6.1, a positive local posterior derivative is impossible before `n=L` departures. Also (6.5) and `M(1-M)<=1/4` give the pathwise bound

\[
\left[M'_{n,c}(\beta)\right]_+
\le
\frac1{4\beta}
\left[(n+1)\rho_{d,D}(\beta)-1\right]_+.
\tag{8.3}
\]

### Theorem 8.1 — fixed-vertex dangerous-history budget

For any adaptive sequence of child-discovery counts `c_n` generated by the walk,

\[
\boxed{
E\sum_{n=0}^{N_v-1}
\left[M'_{n,c_n}(\beta)\right]_+
\le
\frac{(1-s)^L}{4\beta s^2}
\Big(\rho_{d,D}(\beta)(1+Ls)-s\Big).
}
\tag{8.4}
\]

#### Proof

Use (8.1) and (8.3):

\[
E\sum_{n<N_v}[M'_{n,c_n}]_+
\le
\frac1{4\beta}
\sum_{n=L}^\infty
\big((n+1)\rho-1\big)(1-s)^n.
\]

For `t=1-s`,

\[
\sum_{n=L}^\infty(n+1)t^n
=\frac{t^L(1+Ls)}{s^2},
\qquad
\sum_{n=L}^\infty t^n=\frac{t^L}{s}.
\]

Substitution gives (8.4). QED.

The key point is qualitative as well as quantitative: for near-regular support, `rho` is quadratic in `sqrt(D)-sqrt(d)`, so `L` is large, while dangerous histories are penalized by the geometric factor `(1-s)^L`.

### Example: `{2,3}` at `beta=3/5`

Here

\[
s=\frac1{22},
\qquad
\rho=\frac{15}{154}(5-2\sqrt6)
\approx0.00983966050,
\qquad
L=101.
\tag{8.5}
\]

Thus a local beta-response reversal cannot occur until at least 101 departures from the same vertex, and

\[
P(N_v>101)\le\left(\frac{21}{22}\right)^{101}
\approx0.00910873.
\tag{8.6}
\]

The full fixed-vertex positive-derivative budget from (8.4) is approximately

\[
0.01756.
\tag{8.7}
\]

This is not a speed-monotonicity theorem, but it replaces an unstructured worst-degree history term by an explicit exponentially suppressed quantity.

## 9. Regeneration-block aggregate version

The earlier exact P03-B downcrossing-chain calculation gave, for the one-dimensional auxiliary walk with

\[
\gamma:=\frac{\beta d-1}{\beta d+1},
\tag{9.1}
\]

the exact super-regeneration-block mean

\[
\boxed{\widetilde E\tau=\gamma^{-2}.}
\tag{9.2}
\]

Before time `tau`, each tree walk can first discover at most `tau` vertices. At the discovery time of a fresh post-split vertex, its offspring law is again the original Galton–Watson offspring law, and Theorem 8.1 applies conditionally and uniformly to its later local history. Therefore, if `B_loc(beta,d,D)` denotes the right side of (8.4), the aggregate positive local-posterior-reversal budget over all newly discovered post-split vertices satisfies

\[
\boxed{
\widetilde E\,\mathcal R_{\rm post}^{\rm one\ branch}
\le \gamma^{-2} B_{\rm loc}(\beta,d,D),
}
\tag{9.3}
\]

and for both branches of the two-walk coupling,

\[
\boxed{
\widetilde E\,\mathcal R_{\rm post}^{\rm two\ branches}
\le 2\gamma^{-2} B_{\rm loc}(\beta,d,D).
}
\tag{9.4}
\]

This bound is intentionally labeled a **posterior-threshold reversal budget**, not a bound on the full derivative of speed. It controls the part of the negative mechanism caused by history-conditioned degree selection. Cross-branch synchronization and continuation-value weights remain to be inserted.

For near-regular offspring and biases not extremely close to `beta d=1`, (8.4) can be very small because the safe-history horizon is long. Conversely the exact `{2,30}` cylinder in Section 7 shows why no support-uniform argument can simply declare the posterior derivative nonpositive after arbitrarily many revisits.

## 10. What has actually moved

The previous P03-B report left **post-split self-history** as an undifferentiated obstruction. This run resolves three pieces of it rigorously:

1. **Exact local law.** The degree posterior after an arbitrary canonical local path is (3.3); it depends only on departure count `n` and distinct-child count `c`.
2. **Exact selection compensation.** Reuse and new-child discovery produce opposite posterior jumps with zero conditional mean, with the stopped information budget (4.8)--(4.9).
3. **Sharp derivative horizon.** The support coefficient `rho_{d,D}(beta)` gives the exact uniform threshold before which every local history has the correct beta-response sign; beyond that horizon, two-point offspring laws produce real finite-cylinder reversals. Combining this with the geometric spine occupation law yields the explicit tail budget (8.4).

So the headline source metric remains unchanged,

`R_full: 1 -> 1`,

but the intermediate obligation moves from

`post-split degree-selection debt = uncontrolled`

to

`local degree-selection reversal = exact Bayes filter + sharp horizon + explicit geometric tail budget`.

No simulation, solver timeout, or finite numerical experiment is being used as evidence for asymptotic speed monotonicity. The `{2,30}` calculation is an exact rational finite-cylinder obstruction to a proof mechanism only.

## 11. Remaining obstruction and next attack

The missing step is now more specific than in the `0715Z` report. A speed derivative/regeneration-gap term does not weight every local posterior state equally. It multiplies local threshold changes by a **continuation value** depending on whether the two branches return, discover fresh subtrees, or terminate the regeneration episode. The Bayes martingale cancels reuse and discovery only when their continuation weights agree.

The next attack is therefore to derive a two-vertex continuation-gap identity. At a historical vertex with posterior `(M,V,c)`, equations (4.5)--(4.6) imply that for continuation values `H_R,H_N` attached respectively to reuse and new-child discovery, the selection contribution has the exact form

\[
\boxed{
\alpha_c V\,(H_R-H_N).
}
\tag{11.1}
\]

This follows simply by weighting the two posterior jumps by (4.4). The target is to identify the relevant `H` from the regeneration-gap/score representation and bound `H_R-H_N` by the return kernel `r^h` and the exact downcrossing chain, without replacing it by the worst degree pair.

If that succeeds, (4.8) or (8.4) can control the variance factor and the continuation kernel can control the stopping asymmetry. If it fails, the right next result is a finite source-valid cylinder proving that continuation weighting, rather than local posterior selection itself, is the irreducible obstruction to this coupling architecture.

### Obligation ledger

* `SOURCE_CONVENTION`: DONE — outward `beta`; reciprocal `lambda` kept separate.
* `PRE_SPLIT_COMMON_SPINE`: PROVED PARTIAL in `0715Z`, root convention clarified in `0729Z`.
* `POST_SPLIT_LOCAL_DEGREE_FILTER`: **DONE in this run**, equations (3.3)--(3.5).
* `REUSE/DISCOVERY_SELECTION_COMPENSATION`: **DONE in this run**, equations (4.5)--(4.9).
* `UNIFORM_LOCAL_DERIVATIVE_SIGN`: **DONE up to the sharp safe-history horizon**, equations (6.4)--(6.8); impossible globally by Section 7.
* `DANGEROUS_HISTORY_TAIL`: **DONE for a fixed vertex and aggregated posterior-reversal budget**, equations (8.4), (9.3)--(9.4).
* `CONTINUATION_WEIGHT / CROSS-BRANCH SYNCHRONIZATION`: OPEN — next attack (11.1).
* `FULL LPP SPEED MONOTONICITY`: OPEN.

## 12. Delivery ledger

Intended immutable path:

`probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T0813Z__local-history-filter-and-dangerous-tail.md`

This report does not alter shared `RESULTS.md`, `QUEUE.md`, `POSTED.md`, another worker's report, a claim file, the preserved R7-01 Potts work, or P10's Potts role.

`ledger_delta`: P03-B changes from a support-uniform common-spine occupation bound with post-split self-history still uncontrolled to an exact local-history Bayes filter, an information/martingale compensation identity, the sharp support coefficient `rho_{d,D}(beta)`, a source-valid finite cylinder where local posterior beta-monotonicity genuinely reverses, and an explicit geometric regeneration-tail bound for the positive local-posterior derivative. Full speed monotonicity remains open because continuation-value/cross-branch weighting has not yet been controlled.
