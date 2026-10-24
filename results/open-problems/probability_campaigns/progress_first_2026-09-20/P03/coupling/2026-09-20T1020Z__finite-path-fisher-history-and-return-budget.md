Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.

# P03-B coupling report — finite-path Fisher/history decomposition and a geometric local-time budget for posterior debt

**Status:** PROVED PARTIAL / NEW PROBABILISTIC REDUCTION / RESTRICTED COMPONENT CERTIFICATES. The full Lyons–Pemantle–Peres speed-monotonicity conjecture remains open. Nothing below is represented as a new full speed-monotonicity interval.

**Native role:** P03-B, `6aabe777361481919c9e614646464772`, regeneration/coupling, posterior-history and source-valid obstruction role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`.

**Captured master immediately before write:** `585b148d30a8aef265f65c995b68313b44dc21eb`.

**Previous own checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T0904Z__annealed-score-and-continuation-energy.md`, creation commit `7a50de8fa81c3d45c28244e84d38c34f7440f378`.

**Latest complementary P03-A checkpoint consumed, not duplicated:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T1011Z__explicit-terminal-width-for-balanced-one-two-law.md`, creation commit `02259662cb172778839189975f1c6a6e7497a53d`. P03-A is working on recursive escape/speed identities and now has an explicit parent-bias terminal interval for the balanced `{1,2}` law. The present report stays on finite-path scores, hidden-degree information, return geometry and bounded-support `d>=2` families.

## 1. Minimal source continuity

Primary source: Gérard Ben Arous, Alexander Fribergh and Vladas Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865, https://arxiv.org/abs/1111.5865 . The source assumes a Galton-Watson tree without leaves,

\[
P(Z=0)=0,
\]

and uses **outward child bias** `beta`: at a non-root vertex with `k` children,

\[
q_k(\beta):=P_\beta(\text{parent}\mid k)=\frac1{1+\beta k},
\qquad
P_\beta(\text{a specified child}\mid k)=\frac\beta{1+\beta k}.
\tag{1.1}
\]

At the root all children are chosen equally. Thus increasing `beta` means stronger outward bias. The source records transience for `beta>1/EZ` and the Lyons-Pemantle-Peres conjecture that `v(beta)` is increasing throughout `(1/EZ,infinity)`. Its old arXiv theorem gives the historical high-bias cutoff and a `1/d` improvement when the minimum offspring is `d`; those are not treated here as the current frontier.

Bowditch-Tokushige, arXiv:1906.07913 / ALEA 17 (2020), prove differentiability of the parent-bias speed under an exponential offspring moment on the range in which their ballistic/CLT theorem applies and express the derivative as a covariance of a two-dimensional Gaussian limit. Their later arXiv:2006.03433 proves analyticity in the ballistic regime. These results supply differentiability/covariance machinery, not the missing sign.

The strongest broad later primary monotonicity theorem retained after a bounded 20 September 2026 source check is He Song, Longmin Wang and Kainan Xiang, *The speed of a biased walk on a Galton-Watson tree without leaves is monotonic for low values of bias*, Journal of Applied Probability 62 (2025), 1044-1052, DOI `10.1017/jpr.2024.113`. They use reciprocal **parent bias**

\[
\lambda=\beta^{-1},
\]

and, for minimum offspring `d>=2`, prove strict decrease of speed for

\[
0\le\lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\tag{1.2}
\]

This is fully consistent with increasing speed in outward `beta`; no inverse-parametrization contradiction is inferred. A bounded current search did not surface a later source-wide solution of the exact conjecture. That search miss is not a novelty certificate.

The fixed full-source status remains **OPEN**.

For the quantitative return lemmas below I use the source-valid bounded-support subfamily

\[
2\le d\le Z\le D<\infty,
\qquad \beta d>1.
\tag{1.3}
\]

The root is excluded from the local score formulas because its transition law is special. Equivalently, work on a finite root-free path segment after the root boundary has been left. Root terms can be handled separately because their transition law is `beta`-independent.

---

## 2. Inherited bottleneck from 0904Z

The preceding P03-B report integrated the hidden offspring degrees out of a finite canonical path. If a visited non-root vertex `v` has

* `N_v` departures before the finite horizon,
* `P_v` parent departures,
* `C_v` distinct children used,

then the terminal posterior mean parent threshold is

\[
M_v=M_{N_v,C_v}(\beta)
=E[q_{Z_v}(\beta)\mid\text{the canonical local path record at }v].
\tag{2.1}
\]

For a root-free canonical path `gamma`, the exact annealed path score is

\[
\boxed{
\mathcal S_T(\gamma)
:=\partial_\beta\log P_\beta(\gamma)
=\frac1\beta\sum_v\bigl(N_vM_v-P_v\bigr).
}
\tag{2.2}
\]

The problematic history factor was

\[
\sum_v N_v(M_v-\bar q),
\qquad
\bar q:=E q_Z(\beta),
\tag{2.3}
\]

because a posterior displacement at a repeatedly visited vertex is multiplied by its final local time. The previous information-energy estimate controlled posterior martingale increments but did not control this local-time multiplier.

This run closes that **single-vertex local-time factor in annealed L1/L2**, gives a new exact finite-path sign decomposition, and identifies the genuinely remaining cross-vertex covariance.

---

## 3. Exact finite-path Fisher/history decomposition

Fix a deterministic root-free horizon `T`. Let

\[
P_T:=\sum_v P_v
\tag{3.1}
\]

be the total number of parent steps, and let

\[
R_T:=|X_T|-|X_0|=T-2P_T
\tag{3.2}
\]

be the radial displacement over this segment. Define the terminal **history debt**

\[
\boxed{
D_T:=\sum_v N_v(M_v-\bar q).
}
\tag{3.3}
\]

Because `sum_v N_v=T`, (2.2) gives

\[
\beta\mathcal S_T
=T\bar q+D_T-P_T.
\tag{3.4}
\]

Substitute `P_T=T\bar q+D_T-beta S_T` into (3.2).

### Theorem 3.1 — exact score/displacement identity

For every finite canonical root-free path,

\[
\boxed{
R_T
=T(1-2\bar q)-2D_T+2\beta\mathcal S_T.
}
\tag{3.5}
\]

Since `E_beta S_T=0` for a fixed finite horizon, differentiation gives

\[
\boxed{
\frac d{d\beta}E_\beta R_T
=2\beta E_\beta[\mathcal S_T^2]
-2E_\beta[D_T\mathcal S_T].
}
\tag{3.6}
\]

Thus finite-horizon monotonicity is reduced exactly to a competition between

1. a **positive observed Fisher-information term** `2 beta E S_T^2`, and
2. one **history-selection covariance** `2 E[D_T S_T]`.

No other negative term is hidden in (3.6).

#### Proof

Equation (3.5) is the algebra above. For a finite path space, differentiation under the finite sum is immediate:

\[
\frac d{d\beta}E_\beta R_T
=E_\beta[R_T\mathcal S_T].
\]

The constant term `T(1-2 bar q)` in (3.5) contributes zero after multiplication by the score because `E S_T=0`. This leaves (3.6). QED.

### Regular-tree self-check

If `Z=d` a.s., then `M_v=bar q=q_d` and therefore `D_T=0`. Equation (3.6) becomes

\[
\frac d{d\beta}E R_T=2\beta E\mathcal S_T^2>0.
\]

For the regular tree the radial increments have parent probability `q_d`, so

\[
E\mathcal S_T^2=\frac{Tq_d(1-q_d)}{\beta^2}
\]

and hence

\[
\frac d{d\beta}E R_T
=\frac{2Td}{(1+\beta d)^2},
\]

which is exactly the derivative of `T(\beta d-1)/(\beta d+1)`. Thus (3.6) has the correct normalization and loses no factor even in the zero-disorder benchmark.

### Relation to Bowditch-Tokushige

Their derivative is ultimately a covariance obtained from the regeneration/CLT score. Equation (3.6) is a finite-path annealed identity before taking such a limit: it identifies which part of that covariance is automatically positive and isolates the only environmental-history term that can reverse the sign. Passing (3.6) itself to the infinite-time/regeneration limit still requires their type of uniform-integrability/renewal control; I do not claim that passage here.

---

## 4. Complete-data score and an exact missing-information identity

The hidden offspring counts can be retained rather than integrated out. Put

\[
Q_v:=q_{Z_v}(\beta).
\tag{4.1}
\]

For the joint law of the tree and the finite path, the complete score is

\[
\widehat{\mathcal S}_T
=\frac1\beta\sum_v(N_vQ_v-P_v).
\tag{4.2}
\]

Indeed, conditional on offspring `k`, a parent step has score

\[
-\frac{k}{1+\beta k}=-\frac{1-q_k}{\beta},
\]

while a specified child step has score

\[
\frac1\beta-\frac{k}{1+\beta k}=\frac{q_k}{\beta}.
\]

Therefore the one-step complete score increments are martingale differences under the full tree filtration. Their conditional variance is

\[
\frac{Q(1-Q)}{\beta^2}.
\tag{4.3}
\]

Conditioned on the observed canonical path, the posterior offspring counts at distinct vertices remain independent. Let

\[
V_v:=\operatorname{Var}(Q_v\mid\text{observed path}).
\tag{4.4}
\]

Then

\[
E[\widehat{\mathcal S}_T\mid\text{path}]=\mathcal S_T,
\]

and

\[
\operatorname{Var}(\widehat{\mathcal S}_T\mid\text{path})
=\frac1{\beta^2}\sum_vN_v^2V_v.
\]

### Theorem 4.1 — exact missing-information decomposition

\[
\boxed{
\beta^2E[\mathcal S_T^2]
=E\sum_{t<T}Q_{X_t}(1-Q_{X_t})
-E\sum_vN_v^2V_v.
}
\tag{4.5}
\]

The first term is the complete Fisher information. The second is exactly the information lost by not observing the offspring degrees. This identity is just the total-variance decomposition for the complete score, but the local posterior formulas from 0813Z/0904Z make its second term explicit in the present tree problem.

This is useful because the same geometric-return mechanism that controls the local-time score debt also controls the missing-information term.

---

## 5. Degree-sensitive geometric local time at one vertex

The preceding common-spine report used an escape probability based on `d-1` off-spine children. For **revisits to a single fixed vertex**, one can do better: every child can terminate future visits to that vertex.

Fix a non-root vertex `v` of degree `k` after it has been discovered. Let `N_v` be its number of departures before a deterministic horizon (or any earlier adapted truncation). The inherited deterministic hitting estimate says that, from any child of `v`,

\[
P_\beta(\text{return to }v)\le r:=\frac1{\beta d}.
\tag{5.1}
\]

This bound is quenched and survives arbitrary previous exploration because it follows from the supermartingale `r^{H_n}` for distance from `v`.

At a visit to `v`, conditional on `Z_v=k`, the walk chooses some child with probability

\[
1-q_k=\frac{\beta k}{1+\beta k}.
\]

After that child move, it never returns to `v` with probability at least `1-r`. Hence every visit has conditional probability at least

\[
\boxed{
 c_k:=(1-q_k)(1-r)
}
\tag{5.2}
\]

of being the final visit to `v`, regardless of the explored history.

Since `k>=d`,

\[
 c_k\ge c_d
=\frac{\beta d}{1+\beta d}\left(1-\frac1{\beta d}\right)
=\boxed{\frac{\beta d-1}{\beta d+1}}
=:c.
\tag{5.3}
\]

### Lemma 5.1 — geometric local-time domination

For every `n>=1`, conditional on the past immediately before discovering `v` and on `Z_v=k`,

\[
\boxed{
P(N_v\ge n\mid Z_v=k,\text{past})
\le(1-c_k)^{n-1}
\le(1-c)^{n-1}.
}
\tag{5.4}
\]

Consequently

\[
\boxed{
E[N_v\mid Z_v=k,\text{past}]\le\frac1{c_k},
}
\tag{5.5}
\]

and

\[
\boxed{
E[N_v^2\mid Z_v=k,\text{past}]
\le\frac{2-c_k}{c_k^2}.
}
\tag{5.6}
\]

This is stronger than the earlier whole-spine occupation estimate because the event only has to prevent return to one vertex, not to an entire ancestral geodesic.

---

## 6. New theorem: the local-time multiplier in the score debt is integrably controlled

Let a newly discovered vertex have fresh offspring prior. Write

\[
Q=q_Z(\beta),
\qquad
\bar q=EQ,
\qquad
\sigma_q^2=\operatorname{Var}(Q).
\tag{6.1}
\]

At the terminal finite-horizon local record let

\[
M=E[Q\mid\text{local record}],
\qquad N=N_v.
\]

The local contribution to (3.3) is

\[
A_v:=N(M-\bar q).
\tag{6.2}
\]

The discovery event of `v` is independent of its own offspring count; the degree is fresh when the vertex is first entered.

### Theorem 6.1 — weighted posterior-debt envelope

With `c_Q:=(1-Q)(1-r)`,

\[
\boxed{
E|A_v|
\le
\frac1{1-r}
E\left[\frac{|Q-\bar q|}{1-Q}\right]
\le\frac{\sigma_q}{c}.
}
\tag{6.3}
\]

Also

\[
\boxed{
E[A_v^2]
\le
E\left[(Q-\bar q)^2
\frac{2-c_Q}{c_Q^2}
\right]
\le
\sigma_q^2\frac{2-c}{c^2}.
}
\tag{6.4}
\]

#### Proof

Because `N` is measurable with the terminal local record and `M=E[Q|record]`, conditional Jensen gives

\[
N|M-\bar q|
\le N E[|Q-\bar q|\mid record].
\]

Taking expectation,

\[
E[N|M-\bar q|]
\le E[N|Q-\bar q|].
\]

Condition on `Q=q_k` and use (5.5):

\[
E[N|Q-\bar q|]
\le E\frac{|Q-\bar q|}{c_Q},
\]

which is the first inequality in (6.3). Since `c_Q>=c` and `E|Q-bar q|<=sigma_q`, the second follows.

For the square, conditional Jensen gives

\[
N^2(M-\bar q)^2
\le N^2 E[(Q-\bar q)^2\mid record].
\]

Average and use (5.6), yielding the first inequality in (6.4); then `c_Q>=c` gives the uniform bound. QED.

### Corollary 6.2 — uniform finite-horizon score-debt budget

Let `V_T^{act}` be the set of fresh non-root vertices that are both discovered and departed from before the horizon. Then `|V_T^{act}|<=T`. Applying Theorem 6.1 conditionally at each discovery gives

\[
\boxed{
E\sum_{v\in V_T^{act}}
N_v|M_v-\bar q|
\le \frac{\sigma_q}{c}T.
}
\tag{6.5}
\]

Therefore

\[
\boxed{
E|D_T|\le \frac{\sigma_q}{c}T.
}
\tag{6.6}
\]

Likewise the **diagonal L2 budget** is

\[
\boxed{
E\sum_{v\in V_T^{act}}
\bigl[N_v(M_v-\bar q)\bigr]^2
\le
\sigma_q^2\frac{2-c}{c^2}T.
}
\tag{6.7}
\]

This closes the unresolved `N_v` multiplier from 0904Z at the level of each vertex and of the aggregate absolute/diagonal budgets. No worst-pair threshold `q_d-q_D` is needed; heterogeneity enters through the actual standard deviation of `q_Z`.

---

## 7. New quantitative Fisher-information lower bound

The missing-information term in (4.5) is controlled by exactly the same local-time estimate. Since conditional variance minimizes squared error,

\[
V_v
\le E[(Q_v-\bar q)^2\mid\text{path}].
\]

Hence

\[
E[N_v^2V_v]
\le E[N_v^2(Q_v-\bar q)^2]
\le \sigma_q^2\frac{2-c}{c^2}
\]

for each fresh activated vertex, and therefore

\[
\boxed{
E\sum_vN_v^2V_v
\le
\sigma_q^2\frac{2-c}{c^2}T.
}
\tag{7.1}
\]

Put

\[
b:=q_D(\beta)=\frac1{1+\beta D}.
\tag{7.2}
\]

Because `beta d>1`, every possible `Q` lies in `(0,1/2)`, and `x(1-x)` is increasing there. Thus

\[
Q(1-Q)\ge b(1-b).
\]

Substituting into (4.5) gives:

### Theorem 7.1 — observed Fisher information survives bounded heterogeneity

\[
\boxed{
\beta^2E[\mathcal S_T^2]
\ge
T\left[
 b(1-b)
-\frac{(2-c)\sigma_q^2}{c^2}
\right].
}
\tag{7.3}
\]

Consequently the positive term in the exact derivative decomposition (3.6) obeys

\[
\boxed{
2\beta E[\mathcal S_T^2]
\ge
\frac{2T}{\beta}
\left[
 b(1-b)
-\frac{(2-c)\sigma_q^2}{c^2}
\right].
}
\tag{7.4}
\]

The bracket may be negative for a coarse parameter range, in which case (7.3) is only a vacuous lower bound; the Fisher information itself is of course nonnegative. Where the bracket is positive, (7.4) provides an explicit linear-in-time favorable budget that the history covariance in (3.6) must defeat.

This is materially sharper than saying only that the score has finite variance.

---

## 8. A second derivative-side budget: cumulative conditioned-threshold reversals

The 0813Z report proved, for a fixed local canonical history after `n` departures,

\[
\boxed{
M_n'(\beta)
=\frac1\beta\left((n+1)V_n-M_n(1-M_n)\right).
}
\tag{8.1}
\]

The adverse part is `(n+1)V_n/beta`. The geometric local-time lemma now controls its total expectation before the vertex ceases to be visited.

Let `N` be the number of departures from an activated fresh vertex. On `{N>n}`, the posterior variance satisfies

\[
V_n\le E[(Q-\bar q)^2\mid\mathcal F_n].
\]

Using (5.4),

\[
\begin{aligned}
E\sum_{n=0}^{N-1}(n+1)V_n
&\le
\sum_{n\ge0}(n+1)
E[(Q-\bar q)^2;N>n]\\
&\le
\sigma_q^2\sum_{n\ge0}(n+1)(1-c)^n\\
&=\boxed{\frac{\sigma_q^2}{c^2}}.
\end{aligned}
\tag{8.2}
\]

On the other hand, `M_n in [b,q_d] subset (0,1/2)`, so

\[
M_n(1-M_n)\ge b(1-b).
\]

Therefore:

### Theorem 8.1 — local cumulative reversal budget

For every activated fresh vertex,

\[
\boxed{
E\sum_{n=0}^{N-1}M_n'(\beta)
\le
\frac1\beta\left[
\frac{\sigma_q^2}{c^2}
-b(1-b)EN
\right]
\le
\frac1\beta\left[
\frac{\sigma_q^2}{c^2}
-b(1-b)
\right].
}
\tag{8.3}
\]

Hence the entire local-history threshold derivative has the favorable sign in expectation whenever

\[
\boxed{
\sigma_q^2<c^2b(1-b).
}
\tag{8.4}
\]

The statement is **not** a speed-monotonicity theorem: regeneration/finite-horizon rewards weight vertices and times through continuation values, and that weighting is precisely what remains in `E[D_T S_T]`. But (8.3) removes the possibility that long local histories alone produce an uncontrolled positive derivative budget once return rarity is included.

---

## 9. Exact balanced `{2,3}` component certificates

Take

\[
P(Z=2)=P(Z=3)=\frac12,
\qquad \beta>\frac12.
\tag{9.1}
\]

Then

\[
q_2=\frac1{1+2\beta},
\qquad
q_3=\frac1{1+3\beta},
\]

\[
\sigma_q^2
=\frac{(q_2-q_3)^2}{4}
=\frac{\beta^2}
{4(1+2\beta)^2(1+3\beta)^2},
\tag{9.2}
\]

and

\[
c=\frac{2\beta-1}{2\beta+1},
\qquad b=q_3.
\tag{9.3}
\]

### Local cumulative-threshold criterion

The difference appearing in (8.4) simplifies exactly to

\[
b(1-b)-\frac{\sigma_q^2}{c^2}
=\frac{\beta(48\beta^2-49\beta+12)}
{4(2\beta-1)^2(3\beta+1)^2}.
\tag{9.4}
\]

For `beta>1/2`, it is positive exactly when

\[
\boxed{
\beta>\frac{49+\sqrt{97}}{96}
=0.613008935435376\ldots
}
\tag{9.5}
\]

or, in reciprocal parent bias,

\[
\lambda<1.63129759159183\ldots .
\tag{9.6}
\]

Thus the **entire expected local conditioned-threshold derivative**, including arbitrarily many revisits to one fresh vertex, is favorable throughout this range. This is only a component certificate, not a claim that the speed is monotone out to (9.6).

### Quantitative observed-Fisher-information criterion

The bracket in (7.3) becomes

\[
b(1-b)-\frac{(2-c)\sigma_q^2}{c^2}
=\frac{\beta(96\beta^3-50\beta^2-27\beta+12)}
{4(2\beta-1)^2(2\beta+1)(3\beta+1)^2}.
\tag{9.7}
\]

Its unique root above `1/2` is

\[
\boxed{
\beta_{FI}=0.660011831964862\ldots,
\qquad
\lambda_{FI}=1.51512435318468\ldots .
}
\tag{9.8}
\]

For `beta>beta_FI`, (7.4) gives an explicit positive linear-in-`T` lower bound on the favorable Fisher term. The 2025 source-wide theorem for minimum degree two reaches only

\[
\lambda\le\frac2{1+1/\sqrt2}
=1.171572875\ldots,
\]

so these component estimates remain informative well beyond the currently published source-uniform interval. They do **not** by themselves extend that theorem because the cross-vertex history covariance in (3.6) is still uncontrolled.

---

## 10. Rigorous obstruction: information energy cannot control the score debt pathwise

The annealed bounds above genuinely need the geometric rarity of repeated returns. There is no uniform deterministic bound on the factor `N(M_N-bar q)` in terms of the static posterior-information budget alone.

Take any nondegenerate two-point offspring law supported on `{d,D}`, `d<D`. Consider a local record at one vertex consisting of `n` parent departures and no child departure from that vertex, so `C=0`. Its posterior is proportional to

\[
P(Z=k)q_k(\beta)^n.
\]

Since `q_d>q_D`,

\[
M_{n,0}\longrightarrow q_d
\qquad(n\to\infty).
\]

Therefore

\[
\boxed{
 n(M_{n,0}-\bar q)
\sim n(q_d-\bar q)\to+\infty.
}
\tag{10.1}
\]

For every finite `n`, such a repeated-return record occurs on a positive-probability finite Galton-Watson/walk cylinder: after each parent departure the parent can send the walk back to the same child before the next local parent departure. Thus the local-time multiplier can be arbitrarily large on rare valid histories even though the posterior martingale's total quadratic variation is bounded by `Var(Q)`.

This rules out the tempting mechanism

> “posterior information energy alone gives a pathwise uniform bound on the history score debt.”

The correct control must use return rarity, exactly as in Sections 5-8.

---

## 11. What remains: cross-vertex covariance, not the single-vertex return tail

The new exact derivative identity is

\[
\frac d{d\beta}E R_T
=2\beta E\mathcal S_T^2-2E[D_T\mathcal S_T].
\tag{11.1}
\]

Sections 5-8 now give:

* a geometric tail for every single-vertex local time;
* an `L1` bound on the complete history debt, `E|D_T| <= (sigma_q/c)T`;
* an `O(T)` bound on the **sum of squared vertex debts**;
* an `O(T)` bound on the exact missing Fisher information;
* an explicit local cumulative derivative criterion, with a nontrivial `{2,3}` range.

What is **not** yet controlled is the covariance

\[
\boxed{E[D_T\mathcal S_T].}
\tag{11.2}
\]

A naive Cauchy-Schwarz estimate requires an `O(T)` bound on `E D_T^2`. The diagonal estimate (6.7) does not imply that because cross-vertex posterior debts are not automatically orthogonal: the path allocation among vertices couples their local histories. A deterministic inequality replacing `D_T^2` by a universal constant times the diagonal sum is impossible on cylinders where many visited vertices all acquire posterior shifts of the same sign.

Thus the remaining probabilistic problem has narrowed to a specific **inter-vertex correlation** question.

### Next attack

There are two materially different routes, in this order:

1. **Discovery-order martingale / spine route.** Reveal offspring degrees in order of first visit and try to decompose `D_T` into a martingale transform plus a predictable revisit term. Use the single-vertex geometric bound to prove an `O(T)` variance/covariance estimate for the predictable term. The exact target is a constant `C(beta,pi)` such that

   \[
   E[D_T\mathcal S_T]
   \le C(\beta,\pi)T
   \]

   with

   \[
   C(\beta,\pi)
   <\frac1\beta\left[
   b(1-b)-\frac{(2-c)\sigma_q^2}{c^2}
   \right]
   \]

   in a genuinely new bounded-support family. Together with (7.4), that would yield a finite-horizon positive derivative margin and give a credible route to the Bowditch-Tokushige limit.

2. **Source-valid obstruction test if the martingale transform fails.** Build an exact finite cylinder with two or more historical vertices and compute the sign/magnitude of the cross-vertex term. The goal would not be to disprove speed monotonicity, but to determine whether positive same-sign inter-vertex selection is strong enough to invalidate a simple diagonal-information proof.

Finite simulation can guide which cylinder to test, but any claimed obstruction will be converted to an exact finite computation before being used.

---

## 12. Obligation ledger

* Full-source Lyons-Pemantle-Peres conjecture: **OPEN**.
* Source convention/inverse-bias normalization: **RECOVERED AND PRESERVED**.
* Strongest broad later primary range retained: Song-Wang-Xiang 2025, parent bias (1.2), `d>=2`.
* 0904Z unresolved local-time multiplier `N_v(M_v-bar q)`: **PROVED PARTIAL CONTROL** in annealed L1/L2 via Theorem 6.1.
* Finite-path derivative sign decomposition: **NEW PROVED IDENTITY**, Theorem 3.1.
* Hidden-degree missing Fisher information: **NEW EXACT IDENTITY**, Theorem 4.1.
* Single-vertex revisit tail: **NEW SHARPER FORM**, success probability `c_k=(1-q_k)(1-1/(beta d))`, uniform `c=(beta d-1)/(beta d+1)`.
* Local conditioned-threshold derivative accumulation: **NEW PROVED BUDGET**, Theorem 8.1.
* Balanced `{2,3}` local component certificate: **PROVED PARTIAL**, beta threshold `(49+sqrt(97))/96`; not a speed theorem.
* Balanced `{2,3}` positive Fisher lower-budget threshold: **PROVED PARTIAL**, beta root `0.660011831964862...`; not a speed theorem.
* Remaining obstruction: **cross-vertex covariance `E[D_T S_T]`**, not single-vertex return tails.

`R_full: 1 -> 1`.

No force-push, no peer overwrite, no public/email/Drive delivery.
