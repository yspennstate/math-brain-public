Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on H0008: `I_mf = a_hi-a_lo -> same`; this is the second consecutive unchanged H0008 run after the preceding certification movement. Methods actually used: #3 PROVE SOMETHING STRONGER, #14 FIND THE GROUP ACTING, #28 REPLACE "FOR ALL" WITH "FOR TYPICAL".**

# R14 HARD OUTSIDE — H0008 harmonic measure: a multitype PF–KL identity, equality rigidity, and the exact remaining stationarity gate

## 0. Continuity, ownership, metric, and status

This run preserves all prior R14 hard-task handoffs. I do **not** reopen the original negative-margin spherical-perceptron target, H0017, D0036, D0039, or D0034. The active exclusive R14 HARD OUTSIDE claim remains `operations/claims/H0008.md`.

The source is Achyut Kumar (2026), *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1 (17 Aug 2026), Section 12.3, open problem (6), **Boundary fluctuations**. The source asks for the multifractal spectrum of transmission-weighted flows and the harmonic measure of the failed cluster, where a dimension drop is expected.

The frozen metric is still

\[
I_{\rm mf}=a_{\rm hi}-a_{\rm lo},
\]

the exact maximal interval length certified by the 2026-09-19T04-50-17Z run for the finite-type multifractal clause. The immediately preceding H0008 run did not move it. This run attacks the remaining harmonic-measure clause and therefore does not enlarge the already maximal multifractal interval. The honest metric entry is **no movement**.

Status after this run: **PARTIAL / SOURCE OPEN**. The new theorem below reduces the general finite-type harmonic dimension-drop problem to a single stationary-environment existence/equivalence/integrability obligation and proves that, for the source offspring law, equality with full boundary dimension can occur only in the completely regular no-thinning case. I do **not** claim the remaining stationary-environment obligation is solved.

## 1. Required repository and source read

Before research I recovered or targeted-read:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/claims/H0008.md`;
- `probability_1000_intake_H_20260914/problems.jsonl`, including H0003–H0011 around the same Kumar source family;
- the newest R14 H0008 report `runs/R14/2026-09-19T05-52-24Z_h0008_type_lumpability_harmonic_slice_6d2f.md` and the preceding zero-temperature certification report;
- neighboring same-source ownership/history by scoped searches, including H0003 and H0005.

The canonical H0008 claim is still R14-owned, HARD OUTSIDE, SOURCE-OPEN. No release, reassignment, POSTED exclusion, or competing H0008 owner was found.

Fresh primary checks on 19 September 2026:

- source: https://arxiv.org/abs/2608.15987 — still v1, submitted 17 Aug 2026;
- exact open-problem text: https://arxiv.org/html/2608.15987v1, Section 12.3, item (6), still explicitly asks for the multifractal spectrum and harmonic measure/dimension drop;
- companion: https://arxiv.org/abs/2608.21125 — still v1, submitted 21 Aug 2026, and concerns front propagation plus the continuous-type limit theory, not closure of H0008.

A bounded current search did not recover a later primary paper explicitly resolving H0008. That is bounded negative evidence, not a novelty certificate.

## 2. Source finite-type branching law and harmonic recursion

Under the source front-decoupling reduction, away from the exceptional root generation the failed genealogy is a finite-type Galton–Watson process on a finite type set `D`. Write

\[
q_j>0,\qquad \sum_j q_j=1,
\]

and let `nu` be the common forward potential-child count with

\[
m_*:=\mathbb E\nu=\frac{g''(1)}{g'(1)}.
\]

A failed parent of type `i` generates, for each of its `nu` potential children independently, a type `j` with probability `q_j`, followed by a successful failure transmission with probability `p_{ij}`. The source assumes uniform ellipticity, so in the finite-type regime

\[
p_{ij}>0.
\]

The failed-child mean matrix is

\[
M_{ij}=m_*q_jp_{ij}.
\tag{2.1}
\]

Assume throughout this run that `M` is irreducible and supercritical,

\[
\rho:=\rho(M)>1.
\]

The source finite-variance hypothesis gives the multitype Kesten–Stigum input needed below: with a positive right Perron vector `r`, the weighted population martingale has an a.s. limit positive exactly on survival under the usual `N log N` condition (the source itself records this in Appendix C).

For simple random walk on a surviving failed tree, let `B(T)` be the probability that a walk started at the root never hits an added parent. If `T_u` are the child descendant trees and `B_u=B(T_u)`, the exact electrical recursion recovered in the earlier R14 run is

\[
B(T)=\frac{\sum_u B_u}{1+\sum_u B_u},
\tag{2.2}
\]

and the harmonic split among infinite child subtrees is

\[
H_T(u)=\frac{B_u}{\sum_v B_v}.
\tag{2.3}
\]

The hard point is that the law of `B_u` depends on the inherited type and on the full descendant tree.

## 3. Method #3 — prove something stronger: a multitype PF–KL identity for *any* stationary consistent flow

The right comparison object is not equal splitting. It is the Perron/Kesten–Stigum limit-uniform flow on the multitype tree.

Let

\[
\mathcal W(T)
:=\lim_{n\to\infty}\rho^{-n}
\sum_{|v|=n}r_{\tau(v)},
\tag{3.1}
\]

where `tau(v)` is the type of `v`. Use the unnormalised convention above, so

\[
\mathbb E_i\mathcal W=r_i
\]

and, on every realised tree where the limits exist,

\[
\mathcal W(T)=\frac1\rho\sum_{u\text{ child of root}}\mathcal W(T_u).
\tag{3.2}
\]

Under the Kesten–Stigum hypotheses, `mathcal W(T)>0` exactly on survival. Define the PF limit-uniform local split

\[
U_T(u):=rac{\mathcal W(T_u)}{\rho\,\mathcal W(T)}
\tag{3.3}
\]

on surviving child subtrees and `0` on extinct ones. Equation (3.2) makes `U_T` a probability vector. Iteration gives the cylinder formula

\[
U_T([v])=
\frac{\mathcal W(T_v)}{\rho^{|v|}\mathcal W(T)}.
\tag{3.4}
\]

### Theorem R14-H0008-06A (PF–KL identity for a stationary multitype flow)

Let `Theta` be any consistent boundary flow rule on surviving typed trees, with local child split `theta_T(u)`. Suppose there is a probability law `mu` on surviving rooted typed trees such that:

1. `mu` is stationary and ergodic for the `Theta` descendant shift
   \[
   (K_\Theta f)(T)=\sum_u\theta_T(u)f(T_u);
   \]
2. `mu` is equivalent to the original finite-type GW law conditioned on survival if a source-a.s. conclusion is desired;
3. `log mathcal W` and the one-step entropy/KL quantities below are integrable.

Then `Theta_T` is exact-dimensional for `mu`-a.e. tree and

\[
\boxed{
\dim_H\Theta_T
=
\log\rho
-
\int D_{\rm KL}(\theta_T\Vert U_T)\,\mu(dT).
}
\tag{3.5}
\]

In particular,

\[
\dim_H\Theta_T\le\log\rho,
\tag{3.6}
\]

with strict inequality whenever `theta_T != U_T` on a set of positive `mu`-measure.

#### Proof

Because `Theta` is consistent, for a `Theta_T`-sampled ray `xi=(xi_1,xi_2,...)`, if `T_k` denotes the descendant tree rooted at `xi_k`, then

\[
-\log\Theta_T([\xi|n])
=
\sum_{k=0}^{n-1}
-\log\theta_{T_k}(\xi_{k+1}).
\tag{3.7}
\]

The stationary law `mu(dT)Theta_T(dxi)` on tree-ray pairs is shift invariant, and by ergodicity plus the integrability assumption, Birkhoff gives

\[
-\frac1n\log\Theta_T([\xi|n])
\longrightarrow
h_\Theta
:=
\int\Big[-\sum_u\theta_T(u)\log\theta_T(u)\Big]\,\mu(dT)
\tag{3.8}
\]

for almost every tree-ray pair. Hence the flow is exact-dimensional and its boundary dimension is `h_Theta` in the generation metric.

Now compute the cross-entropy against the PF flow. From (3.3), for every child with `theta_T(u)>0`,

\[
\log\frac1{U_T(u)}
=
\log\rho+\log\mathcal W(T)-\log\mathcal W(T_u).
\tag{3.9}
\]

Therefore

\[
\begin{aligned}
&\int\sum_u\theta_T(u)
  \log\frac1{U_T(u)}\,\mu(dT)\\
&=\log\rho
 +\int\log\mathcal W(T)\,d\mu
 -\int\sum_u\theta_T(u)\log\mathcal W(T_u)\,d\mu.
\end{aligned}
\tag{3.10}
\]

Stationarity of `mu` makes the last two terms cancel exactly:

\[
\int\sum_u\theta_T(u)\log\mathcal W(T_u)\,d\mu
=
\int\log\mathcal W(T)\,d\mu.
\tag{3.11}
\]

So the averaged cross-entropy is exactly `log rho`. Pointwise,

\[
D_{\rm KL}(\theta_T\Vert U_T)
=
\sum_u\theta_T(u)\log\frac{\theta_T(u)}{U_T(u)}
=
\sum_u\theta_T(u)\log\frac1{U_T(u)}
-
\Big[-\sum_u\theta_T(u)\log\theta_T(u)\Big].
\tag{3.12}
\]

Integrating (3.12), using (3.10)–(3.11), yields

\[
h_\Theta
=
\log\rho-
\int D_{\rm KL}(\theta_T\Vert U_T)\,d\mu.
\]

This is (3.5). Non-negativity and the equality condition for KL divergence give (3.6) and the strictness criterion. `square`

### Why this is stronger than the previous slice

The theorem does not assume one type, equal weighted row sums, type lumpability, reversibility, or any special formula for the harmonic conductance. It applies to **any** finite-type branching law and **any** consistent flow once the correct stationary descendant-environment law exists. The harmonic problem is therefore reduced to constructing one stationary law rather than estimating the Hausdorff dimension directly.

The identity is also quantitative: the exact dimension deficit is the mean one-step information divergence from the PF limit-uniform flow.

I do **not** claim the abstract entropy comparison mechanism as wholly new. It is the multitype PF form of the Lyons–Pemantle–Peres consistent-flow/entropy argument. The source-specialized form (3.5) and the equality classification in the next section were not located in the bounded search; novelty remains **UNVERIFIED**.

## 4. Source-specific equality rigidity: harmonic flow can equal PF-uniform only for a regular no-thinning tree

The PF–KL identity will give strict source dimension drop as soon as two things are known:

- an appropriate harmonic-shift stationary law equivalent to the source GW law;
- the harmonic split is not PF-uniform except in the trivial equality class.

The second item can be proved completely from the source reproduction law.

### Theorem R14-H0008-06B (rigidity of `H=U` for the source offspring law)

Assume the source finite-type law (2.1), with finite type set, `q_j>0`, `p_{ij}>0`, irreducible `M`, `rho>1`, and Kesten–Stigum positivity of `mathcal W` on survival. Then

\[
H_T=U_T
\quad\text{for GW-a.e. surviving tree}
\tag{4.1}
\]

holds **if and only if** there is an integer `k>=2` such that

\[
\boxed{
\nu\equiv k
\quad\text{and}\quad
p_{ij}=1\ \text{for every }i,j.
}
\tag{4.2}
\]

Thus, except for the deterministic `k`-ary untyped failed tree (random type labels are harmless), the harmonic split differs from the PF limit-uniform split on a positive-probability set.

#### Proof

For a surviving type-`j` descendant tree set

\[
R_j(T):=\frac{B(T)}{\mathcal W(T)}\in(0,\infty).
\tag{4.3}
\]

First show each `R_j` is deterministic. Since `rho>1` while every transmission probability is at most one, `m_*=E nu>1`; hence `P(nu>=2)>0`. Fix any parent type `i` and child type `j`. A potential child is a transmitted type-`j` child whose descendant process survives with probability

\[
t_{ij}:=q_jp_{ij}s_j>0,
\]

where `s_j>0` is the survival probability from type `j` (positivity for all types follows from irreducibility and supercriticality). Conditional on an event `nu>=2`, there is positive probability of two such surviving type-`j` children.

On that event the two child subtrees, conditioned on type `j` and survival, are independent copies of the same survival-conditioned law. Equality of the local harmonic and PF splits implies

\[
\frac{B(T_{u_1})}{\mathcal W(T_{u_1})}
=
\frac{B(T_{u_2})}{\mathcal W(T_{u_2})}.
\tag{4.4}
\]

Two independent copies of a positive random variable being equal almost surely forces that variable to be constant. Hence

\[
R_j\equiv c_j
\tag{4.5}
\]

under the type-`j` survival law. Repeating the same co-occurrence argument with one surviving type-`j` child and one surviving type-`ell` child gives `c_j=c_ell`. Because all `q_jp_{ij}s_j` are positive, there is one common constant `c>0` such that

\[
B(T)=c\,\mathcal W(T)
\quad\text{on survival, for every root type.}
\tag{4.6}
\]

Use the two exact recursions. By (3.2),

\[
\sum_u\mathcal W(T_u)=\rho\mathcal W(T).
\]

By (2.2) and (4.6), on survival,

\[
c\mathcal W(T)
=
\frac{c\rho\mathcal W(T)}{1+c\rho\mathcal W(T)}.
\tag{4.7}
\]

Since `c mathcal W(T)>0`, division gives

\[
\mathcal W(T)
=
\frac{\rho-1}{c\rho}
=:w_*
\tag{4.8}
\]

on every surviving subtree, independently of its type.

Let `N_infty` be the number of children whose failed descendant subtree survives. Extinct children have `mathcal W=0`, while every surviving child has the same value `w_*`. Equation (3.2) and (4.8) therefore give

\[
w_*
=
\frac{N_{\infty}w_*}{\rho},
\]

so

\[
N_{\infty}=\rho
\tag{4.9}
\]

almost surely on survival. Hence `rho=k` is an integer at least two.

Now use the special source thinning law. For a parent of type `i`, one potential child produces an **infinite failed child** with probability

\[
a_i:=\sum_j q_jp_{ij}s_j.
\tag{4.10}
\]

Conditional on `nu`, different potential children are independent, so

\[
N_{\infty}\mid\nu\sim\operatorname{Bin}(\nu,a_i).
\tag{4.11}
\]

By (4.9), conditional on root survival, `N_infty` is the point mass at `k>=2`. Equivalently its unconditional support is contained in `{0,k}`. If `0<a_i<1`, then

\[
\mathbb P(N_{\infty}=1)
=
\mathbb E\big[\nu a_i(1-a_i)^{\nu-1};\nu\ge1\big]>0,
\tag{4.12}
\]

contradicting that support. Thus `a_i=1` for every type `i`. Since `q_j>0`, `p_{ij}\le1`, and `s_j\le1`, the convex combination (4.10) can equal one only if

\[
p_{ij}=1\quad\text{and}\quad s_j=1
\tag{4.13}
\]

for every `i,j`. With survival certain and every transmission successful, `N_infty=nu`; (4.9) now gives

\[
\nu\equiv k.
\]

This proves necessity.

Conversely, if `nu=k` deterministically and all `p_{ij}=1`, the untyped failed genealogy is the deterministic `k`-ary tree. Both harmonic measure and the PF limit-uniform flow split every vertex equally among its `k` children, so `H_T=U_T` identically. `square`

### Corollary R14-H0008-06C (conditional complete finite-type dimension drop)

Suppose in addition that the harmonic descendant shift admits an ergodic stationary probability `mu_H` equivalent to the source finite-type GW law conditioned on survival, with the integrability assumptions of Theorem 06A. Then

\[
\boxed{
\dim_H(\mathrm{HARM}_T)
=
\log\rho
-
\mathbb E_{\mu_H}
D_{\rm KL}(H_T\Vert U_T).
}
\tag{4.14}
\]

If the source law is not the regular no-thinning case (4.2), Theorem 06B and equivalence imply the KL term is positive on a set of positive `mu_H`-measure, hence

\[
\boxed{
\dim_H(\mathrm{HARM}_T)<\log\rho
=\dim_H\partial S.
}
\tag{4.15}
\]

Thus the source's expected finite-type dimension drop is now reduced to one precise analytic obligation:

\[
\boxed{
\texttt{HARM-STATIONARY-MTGW: construct }\mu_H\sim\mathbb P(\cdot\mid\mathrm{survival})
\texttt{ stationary/ergodic for the harmonic descendant shift, with the needed }L^1\texttt{ bounds.}
}
\tag{4.16}
\]

No separate geometric dimension estimate remains after (4.16).

## 5. Method #14 — find the group acting: symmetry gives an automatic quotient and a larger solved source family

The preceding R14 run proved an exact type-lumpability criterion. A natural group action produces such lumpability automatically.

### Proposition R14-H0008-06D (orbit lumpability)

Let a group `G` act on the finite type set `D`. Assume the source parameters are equivariant:

\[
q_{g j}=q_j,
\qquad
p_{g i,g j}=p_{ij}
\tag{5.1}
\]

for all `g in G` and `i,j in D`. Partition `D` into `G`-orbits. Then this orbit partition satisfies the exact lumpability criterion from the preceding run.

#### Proof

For an orbit block `C_B`, define

\[
c_{iB}=\sum_{j\in C_B}q_jp_{ij}.
\]

If `i'=g i`, then because `g` permutes the orbit `C_B`, substituting `j=gk` gives

\[
\begin{aligned}
c_{i'B}
&=\sum_{j\in C_B}q_jp_{g i,j}
=\sum_{k\in C_B}q_{gk}p_{g i,gk}\\
&=\sum_{k\in C_B}q_kp_{ik}
=c_{iB}.
\end{aligned}
\]

Thus aggregate failed-child block probabilities are constant inside each parent orbit, which is exactly the necessary-and-sufficient lumpability condition already proved. `square`

If the group action is transitive, there is only one orbit. The type-erased failed genealogy is therefore an ordinary one-type Galton–Watson tree even when the matrix `(p_ij)` is highly nonconstant. The classical Lyons–Pemantle–Peres dimension-drop theorem then proves the source harmonic clause on this whole transitive-symmetry family, except for the deterministic regular equality case.

This is useful because it identifies a structural reason for one-type reduction that is broader and easier to check than entrywise equality of transmissions.

## 6. Method #28 — replace "for all" with "for typical": why the stationary harmonic-ray law is the right remaining object

Theorem 06A deliberately avoids controlling every tree and every boundary ray. Hausdorff dimension of a flow only requires the logarithmic cylinder law along a **typical ray**. Once a stationary harmonic-ray environment is available, Birkhoff converts that typical-ray problem into the one-step entropy/KL identity (3.5).

I also tested whether stationarity could simply be avoided by taking empirical measures along a single harmonic ray. In a bounded-offspring version, the space of rooted finite-type trees with a marked ray is compact. For a harmonic ray with descendant environments `T_0,T_1,...`, any weak subsequential limit of

\[
\frac1N\sum_{n=0}^{N-1}\delta_{(T_n,\text{shifted ray})}
\tag{6.1}
\]

is shift-invariant, because for every bounded continuous test function `f`,

\[
\frac1N\sum_{n=0}^{N-1}
\big(f\circ S-f\big)(S^n x)
=
\frac{f(S^N x)-f(x)}N\to0.
\tag{6.2}
\]

This is not enough. Such a subsequential stationary law may be **singular** with respect to the original GW law, and weak convergence alone does not preserve the `log mathcal W` integrability needed for the coboundary cancellation (3.11). Therefore empirical stationarity by compactness does not by itself transfer an exact-dimensional result back to almost every source tree.

This failure is informative rather than bookkeeping: the missing theorem must supply **absolute continuity/equivalence and integrability**, not merely some invariant probability measure.

## 7. Prior art and exact novelty boundary

The strongest nearby literature found in this run is:

1. **Lyons–Pemantle–Peres**, one-type Galton–Watson consistent-flow/harmonic dimension theory. The source itself cites their 1996 biased-random-walk paper for the expected dimension-drop phenomenon.
2. **Pierre Rousselin**, arXiv:1708.06965 / EJP 2018, *Invariant Measures, Hausdorff Dimension and Dimension Drop of some Harmonic Measures on Galton-Watson Trees*: explicit invariant measures for classes of flow rules on one-type marked GW trees.
3. **Pierre Rousselin**, arXiv:1711.07920, *Dimension Drop for Transient Random Walks on Galton-Watson Trees in Random Environments*: constructs an invariant law for the forward environment at exit times that is absolutely continuous with respect to the one-type GW/tree-path law and proves dimension drop.
4. **Serdar Altok**, arXiv:1307.5962, *Unimodularity for multi-type Galton-Watson trees*: necessary/sufficient conditions and explicit reversible measures for simple random walk on finite-type MGW-related rooted trees.
5. **Amir Dembo and Nike Sun**, arXiv:1011.4056, *Central limit theorem for biased random walk on multi-type Galton-Watson trees*: finite-type MGW transience/recurrence and an explicit reversing measure for the environment seen from the particle at the **critical bias**, with multitype conductance estimates.

The distinction matters. Altok gives a reversible **vertex-time** environment for simple random walk in a multitype setting; Dembo–Sun's explicit reversing measure is constructed for their critical-bias program. H0008 needs a stationary law for the **forward exit/harmonic descendant chain** in the transient simple-random-walk regime on the failed MGW tree, equivalent to the survival-conditioned failed-tree law. Rousselin constructs precisely that kind of exit-time object in the one-type setting, but the bounded search did not locate a published finite-type analogue directly supplying (4.16).

Searches included variants of:

- `multitype Galton-Watson harmonic measure dimension stationary flow rule`;
- `consistent flow rule multitype Galton-Watson`;
- `finite type Galton-Watson harmonic measure dimension drop multitype`;
- `harmonic flow multitype Galton-Watson invariant measure`.

Failure to locate a paper is not proof of novelty. The PF–KL identity may be regarded as a natural multitype transcription of classical entropy machinery; I record it as a new **route/result inside this campaign**, with external novelty **UNVERIFIED**.

## 8. What moved mathematically, what did not, and the next obligation

The frozen quantity does not move:

\[
I_{\rm mf}:a_{\rm hi}-a_{\rm lo}\longrightarrow a_{\rm hi}-a_{\rm lo}.
\]

This is the **second** consecutive unchanged H0008 metric run since the zero-temperature run certified the exact full value.

The harmonic-measure frontier does move conceptually and theoremically:

- the multitype dimension comparison is now an exact KL identity, not an analogy;
- strictness is reduced to `H != U` plus a stationary equivalent environment law;
- for the source multinomial-thinning offspring law, `H=U` is now completely classified and occurs only when `nu` is deterministic and every transmission probability equals one;
- transitive type symmetry automatically collapses the problem to the classical one-type theorem;
- the exact unsolved gate is (4.16), not the dimension estimate itself.

No checker-only artifact is created: the new claims are theorem-sized and their proofs are written above rather than encoded as finite arithmetic.

### Next fresh methods if H0008 remains active

Use a nonrepeating triple:

- **#9 RANDOMIZE** — construct the harmonic stationary law by an explicit marked-spine or two-sided regeneration/Palm randomisation, modeled on Rousselin but carrying the finite type;
- **#16 COMPUTE EVERY SMALL CASE** — solve the invariant-density equation exactly for two-type finite-support offspring laws to guess the correct general Radon–Nikodym factor and type stationary weights;
- **#27 SWAP THE QUANTIFIERS** — instead of constructing one universal closed-form density first, prove that for every source parameter point the harmonic kernel admits an equivalent stationary law, then identify the density afterward.

If the next run also has no frozen-metric movement, it will be the third consecutive unchanged run; under the owner protocol, the **following** invocation must be the Section-I thinking-only stuck recovery rather than another ordinary lemma run.

## 9. Structured `ledger_delta`

```yaml
ledger_delta:
  worker: R14
  allocation: HARD_OUTSIDE
  active_target: H0008
  source: "Achyut Kumar, arXiv:2608.15987v1, Section 12.3 open problem (6), Boundary fluctuations"
  source_status: OPEN
  owner: R14
  metric:
    name: I_mf
    before: "a_hi-a_lo"
    after: "a_hi-a_lo"
    movement: false
    unchanged_streak_after_last_movement: 2
  methods_used: [3, 14, 28]
  new_results:
    - id: R14-H0008-06A
      status: PROVED_INTERNAL
      statement: "For any finite-type consistent flow with an equivalent stationary ergodic descendant-environment law, dim(flow)=log rho - E KL(local flow || PF limit-uniform flow)."
    - id: R14-H0008-06B
      status: PROVED_INTERNAL
      statement: "For the source multinomial-thinning offspring law with q_j,p_ij>0, harmonic local flow equals PF limit-uniform flow a.s. iff nu is deterministic k>=2 and all p_ij=1."
    - id: R14-H0008-06C
      status: PARTIAL_SOURCE
      statement: "Conditional on an equivalent integrable harmonic-shift stationary law, the general finite-type source harmonic measure has strict dimension drop outside the deterministic regular no-thinning case."
    - id: R14-H0008-06D
      status: PROVED_INTERNAL
      statement: "Any type-symmetry group preserving q and p makes its orbit partition exactly lumpable; a transitive action reduces the failed genealogy to one type."
  remaining_obligation: "HARM-STATIONARY-MTGW: construct an ergodic harmonic descendant-shift stationary law equivalent to survival-conditioned source MGW, with log-W/entropy integrability; then 06A+06B give the source dimension drop."
  novelty: UNVERIFIED
  closure: false
  next_methods: [9, 16, 27]
```

## 10. Model / reasoning control and the historical P26 modification issue

The exposed task-control surface in this runtime still has fields for prompt/title, schedule or relative start, timing mode, enabled state, and notifications, but **no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated completed-run model telemetry**. Therefore GPT-6/maximum remains a prompt request rather than a verified execution setting here. I have stated the actual available model identity at the top of this report and left reasoning as UNVERIFIED.

The repository ledger also records that the historical P26 `You cannot modify this task` error was authorization-context dependent and that P26 was later successfully updated from another authorized context. The legitimate workaround for any still-denied task is therefore an owner/admin-authorized context or platform support, not a duplicate job or permission bypass.

No scheduler, permission, workflow, email, Drive, public-posting, purchase, or shared-root state was changed in this run.
