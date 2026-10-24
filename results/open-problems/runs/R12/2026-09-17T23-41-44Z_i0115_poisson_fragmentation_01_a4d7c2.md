Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or completed-run effort telemetry, so I do not claim otherwise. **NEW TARGET I0115 / metric initialized `K_explicit=1`; no source-metric movement is claimed. Methods actually used: #1 CHANGE THE CATEGORY, #18 SAY IT IN ANOTHER LANGUAGE, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

# R12 / I0115 — explicit Poisson-line fragmentation FDDs and the three-separator regularization

Repository/branch: `yspennstate/math-open-problems`, `master`.  
Deployment: `NEW-METHODS-2026-09-16`.  
Status: **OPEN / PARTIAL / first I0115 run**.  
Canonical claim: `operations/claims/I0115.md`, creation commit `8ab961339a728f0b11ee9ec8acd83edec9fbc456`.

## 1. Continuity: I0102 stays handed off

I did not reopen the Paley degree-four SOS target. The immediately preceding R12 report,

`runs/R12/2026-09-17T22-49-01Z_i0102_terminal_stuck_handoff_15_8e3a71.md`,

records the mandatory terminal I0102 handoff after the fresh reassignment reached three consecutive no-movement runs on top of the two historical stuck recoveries. Its frozen Paley metric remains `(a,C,p0)=(1/2,1,5)`, PARTIAL / SOURCE OPEN, and `next_I0102_recovery_permitted: false` for this assignment.

At run start I reread the required campaign state: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the terminal R12 handoff, the latest task-health admission material, and exact-ID ownership/history searches for candidate HARD successors. The newest coordinator screen still reports zero newly certified READY queue entries; PENDING was therefore not treated as permission to dispatch.

I then completed the missing source-scope work for I0115. Aldous's primary source, *Scale-invariant random spatial networks*, EJP 19 (2014), Section 8.1, states Open Problem 27:

> Give a construction of a SIRSN which is “mathematically natural” in some sense, e.g. in the sense that there is an explicit formula for the distribution of subnetworks `span(z1,...,zk)`.

The same paper later points to the Brownian CRT's explicit induced-subtree laws as the kind of finite-dimensional description desired. Kahn (Ann. Probab. 2016, arXiv:1503.03976) and Kendall (Ann. Probab. 2017) subsequently supplied the natural Poisson-line SIRSN construction, but the bounded current search did not recover an explicit all-`k` formula for the full spatial subnetwork laws. Aldous's current SIRSN page notes those Poisson-line developments while saying that much remains to be done. This resolves the prior R08 source-scope ambiguity sufficiently for a HARD target: R12 freezes the concrete sufficient clause “explicit full FDDs for a genuine SIRSN,” not the subjective word “natural.”

Exact-ID repository search recovered no canonical I0115 owner and no prior I0115 mathematical attempt package. I therefore created the create-only claim above before doing new mathematics.

## 2. Frozen metric

`K_explicit` is the largest integer `k >= 1` for which one **single genuine SIRSN construction** has a proved explicit full law of `span(z1,...,zj)` for every `1 <= j <= k` and every deterministic general-position point configuration, with projective consistency across `j`.

Target: `K_explicit = infinity`.

Initial certified value: `K_explicit = 1`, because the one-point subnetwork is trivial. An explicit law for an abstract partition hierarchy, a route statistic, a non-compatible pair model, or any non-SIRSN candidate does **not** move this metric. This prevents the new route below from being over-credited.

## 3. First-hour negation search: why “explicit FDD first” is hard

The source itself suggests attacking the FDDs first, rather than constructing a continuum object and only afterward asking for formulas. I therefore tried to build a projectively consistent similarity-covariant hierarchy whose finite laws are exact, then asked what prevents it from being a SIRSN.

The useful object is a marked isotropic Poisson line process. It gives a completely explicit hierarchy on every finite point configuration, but the naive one-line and two-line spatial embeddings have precise scale-critical obstructions. A three-line modification removes the local mean-length divergence but still lacks global route compatibility. This is genuine route information, not a source closure claim.

## 4. Method #1 — CHANGE THE CATEGORY: from spatial networks to a Poisson-line fragmentation hierarchy

Let `L` be the space of unoriented affine lines in `R^2`. Parameterize a line by

`L(theta,r) = {x : x dot n_theta = r}`, `0 <= theta < pi`,

with `n_theta=(cos theta,sin theta)`. Put the invariant line measure

\[
\mu(dL)=\frac12\,d\theta\,dr.
\]

This normalization is convenient because for any two points `x,y`,

\[
\mu\{L: L\text{ separates }x\text{ and }y\}=|x-y|.
\tag{4.1}
\]

Indeed, with `v=x-y`, the allowed `r`-interval at angle `theta` has length `|v dot n_theta|`, and

\[
\frac12\int_0^\pi |v\cdot n_\theta|\,d\theta=|v|.
\]

Now let `P` be a Poisson point process on `L x (0,infinity)` with intensity

\[
\mu(dL)\,dt.
\]

For a finite deterministic configuration `z=(z_1,...,z_k)`, define `Pi_t(z)` to be the partition of `[k]` in which `i` and `j` lie in the same block iff no line with mark at most `t` separates `z_i` from `z_j`. Equivalently, the labels are grouped by the cells of the Poisson line tessellation at intensity `t`.

### Theorem R12-S1 — exact all-k fragmentation FDD

For every finite `z`:

1. `(Pi_t(z))_{t>=0}` is a finite-state continuous-time Markov chain.
2. The family is exactly projectively consistent under deletion of any subset of labels.
3. It is translation/rotation covariant, and for every `c>0`,
   \[
   (\Pi_t(cz))_{t\ge0}\ \overset d=\ (\Pi_{ct}(z))_{t\ge0}.
   \tag{4.2}
   \]
4. Its generator is explicit. If `pi` is a current partition and `Ref_L(pi)` is the partition obtained by splitting every block of `pi` according to the two open half-planes of `L`, then for `rho != pi`,
   \[
   q_{\pi\rho}(z)
   =\mu\{L:\operatorname{Ref}_L(\pi)=\rho\},
   \qquad
   q_{\pi\pi}=-\sum_{\rho\ne\pi}q_{\pi\rho}.
   \tag{4.3}
   \]
   Hence
   \[
   \Pr\{\Pi_t(z)=\rho\}
   =\bigl[e^{tQ(z)}\bigr]_{\hat 1,\rho},
   \tag{4.4}
   \]
   where `hat 1` is the one-block partition.
5. If `K=conv{z_1,...,z_k}` and `P(K)` is its perimeter (with the standard convex-geometric convention `P([x,y])=2|x-y|` for a segment), the first nontrivial split time `T_z` satisfies
   \[
   T_z\sim \operatorname{Exp}\!\left(\frac{P(K)}2\right).
   \tag{4.5}
   \]
6. For a nontrivial unordered split `A | A^c`, put `q_i(theta)=z_i dot n_theta` and
   \[
   \lambda_A(z)=\frac12\int_0^\pi
   \Bigl[
   \bigl(\min_{j\in A^c}q_j-\max_{i\in A}q_i\bigr)_+
   +
   \bigl(\min_{i\in A}q_i-\max_{j\in A^c}q_j\bigr)_+
   \Bigr]d\theta.
   \tag{4.6}
   \]
   Then
   \[
   \Pr\{\text{first split is }A|A^c\}
   =\frac{2\lambda_A(z)}{P(K)},
   \qquad
   \sum_{A|A^c}\lambda_A(z)=\frac{P(K)}2.
   \tag{4.7}
   \]

#### Proof

Projective consistency is pathwise: deleting labels from a global line tessellation simply restricts each cell-induced partition. Translation and rotation invariance follow from `mu`; under `x -> c x`, the line coordinate `r` scales by `c`, so `mu` scales by `c`, giving (4.2).

For a fixed finite configuration, only lines that separate at least one pair can change the partition, and their `mu`-measure is finite. Poisson independent increments therefore give a finite-state time-homogeneous Markov chain. A single arriving line deterministically applies `Ref_L`, which gives (4.3); (4.4) is the standard finite-state semigroup formula.

Before the first split, a line changes the one-block state precisely when it passes through the interior of the convex hull, up to a `mu`-null tangent set. At angle `theta` its admissible `r` interval has length

\[
\max_i q_i(\theta)-\min_i q_i(\theta).
\]

Thus its total rate is

\[
\frac12\int_0^\pi
\bigl(\max_i q_i-\min_i q_i\bigr)d\theta
=\frac{P(K)}2
\]

by Cauchy's perimeter formula, proving (4.5). A line produces the split `A|A^c` exactly when all projections of one group lie strictly below all projections of the other; the two possible side assignments give the two positive-part terms in (4.6). Apart from the null set of lines through a sample point, every first separating line induces exactly one unordered split, so summing (4.6) gives the total rate and (4.7).

This theorem supplies an **explicit, projectively consistent, similarity-covariant all-k hierarchy**. It is close in spirit to the Brownian-CRT analogy in Aldous's discussion, but it is not yet a SIRSN: it is an abstract partition genealogy, not a compatible family of finite-length planar routes. Therefore `K_explicit` stays at `1`.

## 5. Method #18 — SAY IT IN ANOTHER LANGUAGE: a sharp spatial-embedding obstruction

A first idea is to turn each separating line into a branching road. There is an immediate equivariance obstruction: there is no measurable rule `b(L) in L` depending on one affine line alone that is translation-equivariant. Indeed, if `v` is any nonzero vector parallel to `L`, then `L+v=L`; equivariance would force

\[
b(L)=b(L+v)=b(L)+v,
\]

which is impossible.

So a branch point needs at least a second geometric object. The most obvious fix is to use the intersection of the first two separating lines. That has an exact mean-length failure.

Take two endpoints at Euclidean distance `d`. The separating lines arrive as a rate-`d` Poisson process. Conditional on being separating, write a line by its crossing point `U` on the segment and its direction angle `Phi in [0,pi)`. The Crofton parameterization gives

\[
U\sim\operatorname{Unif}[0,d],
\qquad
f_\Phi(\phi)=\frac12\sin\phi,
\tag{5.1}
\]

(after rotating the segment to the x-axis), and `U` and `Phi` are independent. Thus the first two separating lines have i.i.d. `(U,Phi)` marks.

For two such lines, their intersection distance contains the factor

\[
\frac{|U_1-U_2|}{|\sin(\Phi_1-\Phi_2)|}.
\]

On the positive-probability event that both directions lie in a compact interval around `pi/2` and `|U_1-U_2|>=d/4`, the numerator and the remaining trigonometric factor are bounded below, while the density of `Phi_1-Phi_2` is bounded below near `0`. Therefore

\[
\mathbb E\frac1{|\sin(\Phi_1-\Phi_2)|}=\infty,
\tag{5.2}
\]

and the two-line intersection has infinite expected detour. So “one extra line fixes translation equivariance” is false at the precise moment required by the SIRSN finite-mean-route axiom.

A second natural fix is to decorate a separating line of mark `t` with an independent stationary one-dimensional Poisson process of portals of rate `alpha t`, the unique power-law rate compatible with the scaling `(x,t)->(cx,t/c)`. If `D` is the distance from the segment crossing to the nearest portal, then conditional on the first separation time `T=t`,

\[
\mathbb E[D\mid T=t]=\frac1{2\alpha t}.
\]

But `T~Exp(d)`, so

\[
\mathbb E D
=\int_0^\infty \frac{d e^{-dt}}{2\alpha t}\,dt
=\infty.
\tag{5.3}
\]

Thus the simplest scale-covariant independent-portal repair also fails at a logarithmic critical divergence.

These are exact analytic obstructions; no finite checker is relevant.

## 6. Method #23 — DO WHAT THE PROPOSER DID NOT EXPECT: three separators, not one

The divergences above suggest not trying to make the first separator carry all spatial information. The first **three** separating lines are already enough to regularize both the angular and scale-critical local geometry.

Let `L_1,L_2,L_3` be the first three separating lines for a pair `x,y`, ordered by their Poisson marks. Their spatial marks `(U_i,Phi_i)` are i.i.d. with (5.1), independently of the arrival times. Define

\[
S=\max_{1\le i<j\le3}|\sin(\Phi_i-\Phi_j)|,
\]

choose a pair `(i_*,j_*)` attaining the maximum (ties have probability zero), and let `H(x,y)` be the intersection of `L_{i_*}` and `L_{j_*}`.

### Theorem R12-S2 — three-separator finite-mean hub

The map `(x,y,P) -> H(x,y)` is translation-, rotation-, and scale-covariant in distribution, has an explicit finite-dimensional law, and

\[
\boxed{
\mathbb E\bigl[|x-H|+|H-y|\bigr]
\le 2|x-y|\left(3+\frac{\pi^2}{8}\right)<\infty.
}
\tag{6.1}
\]

Moreover the analogous construction from only the first two separating lines has infinite expected detour; three is the first value for which this angular regularization works.

#### Proof

The conditional direction density in (5.1) is bounded by `1/2`. Put `delta=arcsin(epsilon)`. If `S<=epsilon`, then after fixing `Phi_1`, both `Phi_2` and `Phi_3` must lie within projective angular distance `delta` of `Phi_1`. The relevant set has total length `2 delta`, hence conditional probability at most `delta` for each direction. Therefore

\[
\Pr(S\le\epsilon)\le (\arcsin\epsilon)^2.
\tag{6.2}
\]

Since `S<=1`,

\[
\begin{aligned}
\mathbb E[S^{-1}]
&=1+\int_1^\infty \Pr(S<t^{-1})\,dt\\
&\le 1+\int_1^2 1\,dt
+\int_2^\infty \frac{\pi^2}{4t^2}\,dt\\
&=2+\frac{\pi^2}{8},
\end{aligned}
\tag{6.3}
\]

where `arcsin u <= (pi/2)u` was used for `u<=1/2`.

Two lines crossing the segment at points at most `d=|x-y|` apart have intersection at distance at most `d/S` along either selected line from its segment crossing. Hence

\[
|x-H|+|H-y|\le 2d(1+S^{-1}).
\]

Taking expectations and applying (6.3) gives (6.1).

For two lines, on an interior angle interval where `f_Phi` is bounded below, the difference angle has positive density at zero, so the integral of `1/|sin difference|` diverges logarithmically. Restricting simultaneously to `|U_1-U_2|>=d/4` gives the claimed infinite expected detour.

### What this actually accomplishes

R12-S2 removes two concrete local obstructions simultaneously:

- one affine line cannot carry a translation-equivariant branch point;
- two random separating lines have an infinite-angle detour;
- three lines give a canonical similarity-covariant pair hub with finite expected stretch.

But `R(x,y)=x-H(x,y)-y` is **not** yet a SIRSN route system. Pair-specific hubs do not automatically satisfy Aldous's route-compatibility condition: two routes can meet twice without being forced to coincide between the meetings, and deletion/projective consistency of full spatial subnetworks is not established. Therefore I do not move `K_explicit`.

The important new route is to combine the all-k Poisson fragmentation genealogy R12-S1 with a **shared three-separator decoration at the level of global genealogy nodes**, rather than choosing `H(x,y)` independently for each pair. If that can be done while retaining the finite-mean bound (6.1), the remaining source obligations become finite local-length / compatibility / major-road-intensity estimates rather than an unknown FDD law.

## 7. Current-status / prior-art boundary

The primary source is Aldous, EJP 2014 Open Problem 27. Later work that must not be re-claimed:

- Jonas Kahn, *Improper Poisson line process as SIRSN in any dimension*, Ann. Probab. 44 (2016), proves the speed-marked Poisson-line geodesic network is a SIRSN and proves finite expected geodesic length and finite long-distance-network intensity.
- Wilfrid Kendall, *From random lines to metric spaces*, Ann. Probab. 45 (2017), develops the planar Poisson-line metric and geodesic structure.
- Kendall, *Rayleigh Random Flights on the Poisson line SIRSN*, EJP 25 (2020), studies local geodesic dynamics but does not supply the source-requested explicit all-k full subnetwork law in the bounded search performed here.

The invariant-line/Crofton identities and the existence of Poisson-line SIRSNs are standard prior art. I make **no novelty claim** for R12-S1/S2 at publication level before a much deeper search; their role here is to identify a new constructive route and an exact threshold between two-line and three-line local embeddings.

## 8. Status and next route

`K_explicit` remains `1`. Source status: **OPEN / PARTIAL**. Outside audits: `0/2`. No checker was manufactured because both new claims are symbolic all-configuration analytic statements, not finite enumerations.

The exact remaining construction problem for this route is:

\[
\boxed{
\text{decorate the projectively consistent Poisson-line partition genealogy by shared planar branch points so that}\
\text{(i) route compatibility holds pathwise, (ii) }\mathbb E D_1<\infty,\text{ and (iii) }p(1)<\infty.
}
\]

The next nonrepeating Section-B moves are **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #12 FIND WHAT IS CONSERVED, #19 MAKE IT AN ALGORITHM**. Concretely: introduce an `m`-separator node decoration and determine the exact smallest `m` for each SIRSN axiom; search for a deletion-consistent invariant of the line genealogy; and compile the shared-node construction as an explicit recursive algorithm whose failure point is mechanically identifiable.

## 9. Model / scheduler configuration status

The configuration issue remains unchanged. The exposed task-control surface provides prompt/title/schedule/timing/enablement fields but no binding model-family selector, reasoning-effort selector, guaranteed-duration field, or authenticated completed-run model/effort telemetry. GPT-6 / maximum is therefore prompt-only here. Changing that requires an authorized product/workspace control exposing those fields or platform support. A native task that returns `You cannot modify this task` must be handled from its authorized owning context or through platform support, not by duplicating it or bypassing permissions.

No scheduler state, email, Drive, public posting, purchase, permission, workflow, shared-root file, or peer-track file was changed.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R12
  predecessor:
    target_id: I0102
    status: PARTIAL_OPEN_TERMINAL_HANDOFF
    metric: "(a,C,p0)=(1/2,1,5)"
    reopened: false
  target_id: I0115
  source: "David Aldous, Scale-invariant random spatial networks (EJP 2014), Open Problem 27"
  category: HARD_OUTSIDE
  claim_path: operations/claims/I0115.md
  claim_commit: 8ab961339a728f0b11ee9ec8acd83edec9fbc456
  metric_name: K_explicit
  metric_definition: "largest k with explicit full span(z1,...,zj) laws for all j<=k in one genuine SIRSN"
  before: UNMEASURED_NEW_TARGET
  after: 1
  source_movement_claimed: false
  status: OPEN_PARTIAL
  methods: [1, 18, 23]
  new_results:
    - R12-S1_exact_projectively_consistent_Poisson_line_fragmentation_generator_and_first_split_law
    - R12-S2_three_separator_similarity_covariant_pair_hub_with_finite_mean_stretch
    - two_separator_angular_divergence
    - scale_covariant_independent_portal_log_divergence
  finite_core: none
  audits_other_tracks: 0
  next_methods: [5, 12, 19]
  next_obligation: "shared genealogy-node planar decoration with pathwise compatibility, finite mean route length, and finite p(1)"
```
