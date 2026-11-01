Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. GPT-6/maximum is requested only in prompt text; the exposed scheduler/runtime interface has no binding model selector, reasoning-effort selector, or authenticated effort telemetry. **No movement in the frozen metric: `S=3 -> 3`. Methods tried: B7, B18, B27.**

# HARD7-02 run 3 — full rank-marked PWIT local limit and corrected resolvent route

Status of Campbell–O'Rourke Question 1.8: **PARTIAL / source question still OPEN_BY_BOUNDED_SEARCH.** This run does not classify all properties of `theta_d` that determine `mu_{alpha,theta_d}` and therefore does not increase the frozen transformation-law count `S`. It does, however, close the main proof obligation left by run 2: the rank-marked object is not merely a depth-one heuristic. For every fixed finite exploration depth it is the exact local weak limit, and the source's diagonal argument plus the unchanged square-tail estimate upgrades this to full local operator convergence. This yields the correct type-dependent resolvent recursion and pinpoints the printed Theorem 4.8/Remark 4.9 failure for nonswap-symmetric dependence measures.

## 1. Continuity, repository state, ownership, and current-source check

I resumed the exclusive claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`

and the newest own report

`runs/hard7_2026-09-18/HARD7-02/2026-09-18T22-12-00Z__rank-marked-pwit-obstruction.md`.

The controlling files read this run were:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md` and `RESULTS.md`;
- the current claim file above;
- the newest neighboring heavy-tail report found by repository search, `research7_2026-09-17/R7-06/runs/2026-09-18/2026-09-18T212000Z__report.md`.

Repository-wide searches for `Campbell`, `O'Rourke`, the paper title, `theta_d`, `PWIT`, heavy-tailed elliptic aliases, and current claims still identify `CAMPBELL-OROURKE-2022-Q1.8` as owned only by HARD7-02. The neighboring R7-06/C0032 track is the distinct i.i.d. heavy-tailed circular-law density problem. No ownership collision, posted equivalent, or excluded personal target appeared.

### Fresh primary-source verification, 2026-09-18/19 UTC

Primary source: Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, EJP 27 (2022), paper 127, DOI `10.1214/22-EJP849`, arXiv `2010.01261v3` (revised 2022-02-02):

- https://arxiv.org/html/2010.01261v3
- https://arxiv.org/abs/2010.01261

The live arXiv HTML still states in Section 1.3, Question 1.8:

> What properties of `theta_d` determine `mu_{alpha,theta_d}`?

The same current source still prints Theorem 4.8 as convergence of the uniformly permuted matrix to the homogeneous operator on `PWIT(theta_d x m_alpha)`, and Remark 4.9 still says the theorem holds for **any** permutation sequence. The proof still uses, at its key line, the assertion that the unexplored edge vectors from every newly discovered parent have the same law as the root edge vectors. For a nonswap-symmetric atom pair this is false because the law changes according to whether the original neighbor rank lies above or below the parent rank.

A fresh bounded web search on the exact title/authors together with `Theorem 4.8`, `PWIT`, `erratum`, `correction`, `permutation`, and 2023--2026 date terms found the 2022 paper, its bibliographic pages, the later Campbell--O'Rourke Levy--Khintchine random-Laplacian paper, and unrelated later elliptic-law work, but no erratum/correction of this point and no claimed full solution of Question 1.8. This remains a bounded negative search, not a proof of worldwide novelty or openness.

## 2. Frozen source metric

The claim's fixed metric remains

`S = number of exact nontrivial transformation laws for theta_d -> mu_{alpha,theta_d}`

proved by HARD7-02 from exact finite-matrix spectral identities under Condition C2.

Before: `S=3`.

After: **`S=3` (no movement).**

Unchanged streak for this metric: **2**. This does not yet trigger Section I. The theorem below is source-relevant progress but is not counted as a fourth transformation law.

The run-2 remaining obligation was to decide whether the proposed rank-marked PWIT survives beyond depth one. It does: all fixed finite depths converge, and the local-operator upgrade follows.

## 3. Setup: the rank-marked kernel

Fix `0<alpha<2`. Let

`nu := theta_d x m_alpha`

be the regular-variation intensity on `C^2 \ {0}`, where `m_alpha` has radial density `alpha r^{-1-alpha} dr`. Let

`tau(z,w)=(w,z)`

and write `tau#nu` for its pushforward.

For `u in [0,1]`, define the type-dependent intensity kernel on

`[0,1] x (C^2\{0})`

by

`K_u(dv,dy) = 1_{v>u} dv nu(dy) + 1_{v<u} dv (tau#nu)(dy).`       (3.1)

The null diagonal `v=u` is irrelevant.

Define the **rank-marked PWIT** as follows.

1. The root type is `U_empty ~ Uniform[0,1]` for a uniform matrix root. More generally one may fix the root type equal to a deterministic `u`.
2. Conditional on a vertex `x` having type `u`, generate independently a Poisson point process
   `Xi_x={(V_xk,Y_xk)}_{k>=1}` with intensity `K_u`.
3. Order the atoms by decreasing `||Y_xk||`, write `Y_xk=(Y_xk^(1),Y_xk^(2))`, give child `xk` type `V_xk`, and set

   `A^rk_{x,xk}=Y_xk^(1),    A^rk_{xk,x}=Y_xk^(2).`          (3.2)

The offspring processes are conditionally independent from vertex to vertex, while the parent edge already present at a child is retained rather than regenerated.

Two immediate consistency facts matter.

First, for every parent type `u`, the **pair-norm** radial intensity is exactly the standard one:

`int_{0}^{1} K_u(dv,{y: ||y|| in dr}) = m_alpha(dr),`          (3.3)

because `theta_d` and `tau#theta_d` are probability measures and coordinate swap preserves the norm. Hence the ranked sequence of pair norms at every vertex has the same law as in the ordinary `PWIT(theta_d x m_alpha)`.

Second, the kernel is edge-consistent. If `u<v`, an oriented parent-to-child pair has intensity `nu(dy)`; viewed from the child back toward the parent its oriented pair is `tau y`, and the lower-rank side of `K_v` has intensity `tau#nu`. Thus the two orientations describe the same unordered heavy edge.

## 4. B27 — swap the quantifiers: a quenched-in-rank point-process theorem

Run 2 proved only the root-count limit after fixing a cap. The stronger useful statement is to fix **every** limiting parent rank first and prove the whole marked point process.

Let the original matrix labels be `1,...,n`. For `i<j`, put

`Z_ij^(n) := (X_ij,X_ji)/a_n`.

By Condition C1,

`n P(Z_12^(n) in .) -> nu(.)`                                  (4.1)

vaguely on `C^2\{0}`.

For a parent label `k`, orient every pair away from `k` by

`Y_kj^(n) = Z_kj^(n)` if `k<j`,

`Y_kj^(n) = tau Z_jk^(n)` if `j<k`.                              (4.2)

Let `F_n` be any set of labels with uniformly bounded cardinality, representing already explored vertices. Define the marked neighbor process

`Pi_n(k,F_n) = sum_{j != k, j notin F_n} delta_(j/n, Y_kj^(n)).` (4.3)

### Proposition 1 — quenched rank-marked Poisson convergence

If `k_n/n -> u`, then for every bounded-cardinality `F_n`,

`Pi_n(k_n,F_n) => PPP(K_u)`                                    (4.4)

vaguely on `[0,1] x (C^2\{0})`.

#### Proof

Take nonnegative `f in C_c([0,1] x (C^2\{0}))`. Its support in the `y` variable is bounded away from zero. By independence of the unordered matrix-edge atom pairs,

`E exp{-<f,Pi_n>}`

is the product over `j>k_n` of

`E exp{-f(j/n,Z_12^(n))}`

and over `j<k_n` of

`E exp{-f(j/n,tau Z_12^(n))}`, omitting `F_n`.

Write

`h_n(v)=E[1-exp{-f(v,Z_12^(n))}],`

`h_n^tau(v)=E[1-exp{-f(v,tau Z_12^(n))}].`

Because `f` is supported on a compact set away from zero, regular variation gives

`sup_v h_n(v)=O(1/n),   sup_v h_n^tau(v)=O(1/n).`               (4.5)

For a product test function `f` replaced at first order by `phi(v) psi(y)`, (4.1) and the Riemann-sum theorem give

`sum_{j>k_n} E psi(Z_12^(n)) phi(j/n)
 -> int_u^1 int psi(y) phi(v) nu(dy) dv,`

and analogously below `u` with `tau#nu`. Finite sums of product functions are uniformly dense on the compact support of `f`; applying this to `1-e^{-f}` yields

`sum_{j>k_n} h_n(j/n) + sum_{j<k_n} h_n^tau(j/n)`

` -> int K_u(dv,dy) [1-e^{-f(v,y)}].`                           (4.6)

Removing the bounded set `F_n` changes the sum by `O(|F_n|/n)=o(1)`. Finally, (4.5) implies the sum of quadratic logarithm errors is `O(n * n^{-2})=o(1)`, so

`log E exp{-<f,Pi_n>}`

converges to minus the right-hand side of (4.6), exactly the Laplace functional of `PPP(K_u)`. This proves (4.4). `□`

This theorem contains run 2's mixed-Poisson depth-one count as the special case where the root type is random uniform and one tests an indicator approximated by continuous functions.

## 5. B7 — take the limit all the way through the source exploration

The important question is whether the rank mark persists coherently through multiple generations. It does.

For fixed integers `B,H`, use exactly the source's exploration rule: from each discovered parent, among labels not used earlier in the exploration, select the `B` edges with largest pair norm and continue to depth `H`. In addition to the edge pair, retain each selected original label divided by `n` as a type mark.

### Theorem 2 — finite-depth rank-marked network convergence

For every fixed `B,H`, the rank-marked `B`-ary depth-`H` exploration of the elliptic matrix rooted at any sequence `k_n` with `k_n/n -> u` converges jointly in distribution to the corresponding truncation of the rank-marked PWIT with root type `u` and kernel (3.1).

For a uniform independent permutation root, the same statement holds with root type `U_empty ~ Uniform[0,1]`.

#### Proof

Proceed through the source's lexicographic exploration order.

At the root, Proposition 1 gives the full marked Poisson process. Since the radial intensity is diffuse, ties among the top `B` pair norms have limiting probability zero, so selecting the top `B` atoms is a continuity point of the point-process map almost surely. Therefore the first-generation types and edge pairs converge jointly.

Suppose the exploration has been coupled through some finite number of parents. Only finitely many original labels have then been removed. For the next parent, conditional on its original rank and on all previously revealed edges, the unordered edges from it to as-yet unused labels are independent of the revealed sigma-field: every such edge corresponds to a new unordered pair of matrix indices. Its candidate process is therefore exactly of the form (4.3) with a bounded deletion set. Proposition 1 applies conditionally, with the parent type equal to the limit of its normalized rank.

The limiting offspring PPP attached to that parent is independent of the earlier limiting offspring PPPs, because the underlying unrevealed unordered edge families are disjoint. Sequential conditioning therefore gives joint convergence for all parents in the finite exploration.

The source exploration globally removes already selected labels, so an exact finite-`n` collision cannot produce two tree vertices with the same original label. Removing those finitely many labels has no limiting effect by Proposition 1. Non-tree edges among the finitely many explored vertices involve only finitely many unused unordered atom pairs. For each such fixed pair,

`||Z_ij^(n)|| -> 0` in probability,

because `a_n -> infinity`; equivalently one may use the same stochastic-domination argument as the source. Hence all non-tree edge weights converge to zero jointly.

Induction over the finite lexicographic list of vertices in `J_{B,H}` proves the theorem. `□`

### Why this directly repairs the false line in the printed proof

The source proof asserts, for every newly explored parent `v`, that its unexplored edge-vector family has the same distribution as a root family of iid `theta_d`-oriented pairs. The correct replacement is:

- conditional on the parent's normalized original rank `u`, upper-rank neighbors converge with intensity `nu`;
- lower-rank neighbors converge with intensity `tau#nu`;
- the neighbor rank `v` must remain as a mark;
- after finite deletions, the same kernel `K_u` remains.

Thus the missing state variable is exactly one scalar type `u in [0,1]`.

## 6. Full local-operator convergence, not only finite-depth convergence

The finite-depth theorem is enough to repeat the source's diagonal argument, because the tail estimate used after its finite-network convergence is unchanged.

### Theorem 3 — corrected Theorem 4.8

Let `P_n` be uniform random permutation matrices independent of the elliptic matrix `A_n`, under the source's Condition C1/C2 regime. Then

`(P_n A_n P_n^T, 1) => (A^rk, empty)`                           (6.1)

in the source's local-operator sense, where `A^rk` is the rank-marked operator (3.2) with uniform root type.

More strongly, if a deterministic sequence of roots has original ranks `k_n/n -> u`, its local limit is the rank-marked operator with root type fixed to `u`.

#### Proof

For every fixed `B,H`, Theorem 2 gives convergence of the finite explored network. Apply Skorokhod representation separately on a countable diagonal family and choose `B_n,H_n -> infinity` slowly enough that every fixed finite collection of tree matrix entries converges almost surely after the corresponding random relabeling, exactly as in the source.

It remains to upgrade entrywise convergence on finitely supported vectors to strong `ell^2` convergence of each column. This is precisely the point of the source's order-statistic tail estimate. That estimate depends only on the norms of the unordered pair variables. But coordinate swap leaves the pair norm unchanged, and for every original row the variables

`||(X_kj,X_jk)||, j != k,`

are iid with the same law, regardless of whether `j<k` or `j>k`. Consequently the uniform square-tail estimate used in the source is literally unchanged for the rank-marked exploration. Each matrix coordinate is bounded by the pair norm, so the same tail control gives

`sup_n sum_{i>=m} |<delta_{u_i}, phi_n^w>|^2 -> 0`

as `m->infinity` for every finitely supported basis vector `delta_w` after the diagonal coupling.

On the limit side, (3.3) shows that the ranked pair norms at every typed vertex have exactly the same Poisson radial law as in the ordinary PWIT. In particular they are square summable for `alpha<2`. Therefore the limiting columns lie in `ell^2`, and finite-coordinate convergence plus the uniform tail estimate yields strong convergence on every finitely supported vector. This is the source's Definition 4.4 local convergence. `□`

### Corollary 4 — exact scope of the printed homogeneous PWIT theorem

If

`tau#theta_d = theta_d`,                                        (6.2)

then `tau#nu=nu`, and (3.1) collapses to

`K_u(dv,dy)=dv nu(dy)`

for every `u`. The type marks become probabilistically irrelevant after projection, so `A^rk` reduces to the ordinary homogeneous `PWIT(theta_d x m_alpha)` operator. Thus the printed Theorem 4.8 is recovered under swap symmetry.

If `tau#theta_d != theta_d`, run 2 already supplied an explicit C2 family for which the homogeneous theorem fails at depth one. Theorem 3 gives the corrected replacement at all depths.

### Corollary 5 — corrected form of Remark 4.9

For a deterministic permutation sequence whose root original rank satisfies

`pi_n(1)/n -> u`,                                               (6.3)

the local limit is the typed operator with root type `u`, not a universal root-independent homogeneous PWIT.

Hence identity-root permutations (`u=0`) and reversing-root permutations (`u=1`) have limiting offspring intensities `nu` and `tau#nu`, respectively. They can project to the same homogeneous oriented PWIT only when the relevant swap asymmetry disappears. This classifies the permutation-sequence dependence at the root-type level instead of only giving a counterexample.

## 7. Self-adjointness transfers to the rank-marked operator

A possible concern is that introducing types could break the source's essential-self-adjointness argument for the bipartization. It does not.

For each typed vertex, define exactly as in the source

`T_x(k)=sum_{j>k} ||Y_xj||^2`

and the first index after which this tail is at most a fixed `kappa`. By (3.3), the ordered norm process has **exactly** the same law at every vertex as the source's ordinary PWIT norm process. The offspring PPPs are independent between vertices, and the norm law is independent of the type. Therefore the stopping indices used in the source's red/green Galton-Watson construction are iid with the same distribution as before.

Choosing `kappa` so that their mean is below one and repeating the source's finite-connected-set construction gives the same Corollary-4.2 criterion. Consequently the bipartization of `A^rk` is almost surely self-adjoint for every `z`.

No new numerical or finite certificate is needed here: this is a theorem-sized transfer and the complete reason the transfer works is the exact radial identity (3.3).

## 8. B18 — say the source problem in the right language: a continuum-type resolvent recursion

The homogeneous scalar distributional recursion in the printed paper loses the rank state. The corrected object is a **family** of root resolvents indexed by `u in [0,1]`.

Let

`R_u(U) = [[a_u,b_u],[b'_u,c_u]]`

be the root resolvent block of the bipartized rank-marked operator with root type fixed to `u`. For an atom `(v,y)` of `Xi_u`, with `y=(y_1,y_2)`, let `R_v^(atom)(U)` be an independent copy of the cavity resolvent at child type `v`. Then Proposition 4.3 applied to the rank-marked tree gives the exact continuum-type recursion

`R_u(U)  =d  -[ U + sum_{(v,y) in Xi_u}`

`   [[0,y_1],[bar(y_2),0]] R_v^(atom)(U) [[0,y_2],[bar(y_1),0]] ]^{-1}.`   (8.1)

The PPP `Xi_u` has intensity `K_u` from (3.1). Equation (8.1) is the corrected analogue of the source's homogeneous recursion: `theta_d` enters separately on the half-space `v>u`, while `tau#theta_d` enters on `v<u`. The child type is then fed recursively into `R_v`. The shared latent rank that produced the mixed-Poisson obstruction in run 2 is therefore not a nuisance to average away; it is the state variable of a multitype recursive distributional equation.

For the uniform matrix root, the symmetrized singular-value Stieltjes transform is represented by

`m_checknu(z,eta) = (1/2) int_0^1 E[a_u(z,eta)+c_u(z,eta)] du.`   (8.2)

Indeed the finite-matrix identity is the normalized trace average over original ranks, the uniform permutation makes the root rank asymptotically Lebesgue, Theorem 3 supplies resolvent convergence, and the source's bounded resolvent estimates justify taking expectations. Matrix-level concentration is unchanged. Formula (8.2), rather than a single homogeneous root law, is the natural repaired input to the Hermitization argument.

This does **not** by itself solve Question 1.8. It does make the dependence question substantially sharper:

> Which invariants of `theta_d` leave the continuum family `(Law(R_u))_{u in [0,1]}` — and hence the integrated root transform (8.2) — unchanged?

The three exact run-1 symmetries act on this typed equation, but the equation also makes clear why replacing `theta_d` by the arithmetic swap average need not be valid: for each fixed `u`, all descendants share recursively generated rank types, so averaging the intensity before solving the nonlinear recursion is not the same operation as averaging the resulting law.

## 9. Method outcomes

- **B7 TAKE THE LIMIT.** **Succeeded.** The rank-mixed depth-one law from run 2 extends to every fixed `B,H`, then through the source's unchanged square-tail/diagonal argument to full local operator convergence. The key invariant is that pair norms are unaffected by orientation swap.
- **B18 SAY IT IN ANOTHER LANGUAGE.** **Succeeded.** The correct object is a continuum-type Poisson branching kernel `K_u` and a family of resolvent laws `R_u`, not one homogeneous PWIT recursion. This yields the explicit corrected recursion (8.1) and averaged transform (8.2).
- **B27 SWAP THE QUANTIFIERS.** **Succeeded.** Instead of averaging over a uniform root first, Proposition 1 and Theorem 3 hold for **every fixed limiting root rank** `u`. The uniform-root theorem is then the mixture over `u`. This also gives the precise corrected content of the source's overly strong “any permutation sequence” Remark 4.9.

No checker was manufactured merely to certify that the run executed. The new claims are theorem-sized and are proved on the page. There is no finite exhaustive claim requiring an exact-arithmetic artifact in this run.

## 10. What this changes for Question 1.8

Run 1 showed that the map `theta_d -> mu_{alpha,theta_d}` has exact swap, common-phase, and conjugation symmetries. Run 2 showed that the printed homogeneous PWIT loses a rank variable for nonswap-symmetric `theta_d`. This run proves the corrected all-depth object and supplies the exact recursive language in which the source question should be attacked.

A particularly important consequence is negative methodological information: a proof that first replaces `theta_d` by

`(theta_d + tau#theta_d)/2`

at the local-tree intensity level is generally unjustified. The correct local law is a **mixture of type-conditioned Poisson laws**, not a Poisson law with the averaged intensity, and the nonlinear resolvent recursion propagates the type.

The source question itself remains open because it is still unknown whether the *integrated* spectral output (8.2), after solving the typed recursion and then Hermitizing, forgets some or all of this extra type information.

## 11. Next obstruction and next methods

The next source-matching fork is now precise.

Let `theta^sym=(theta+tau#theta)/2`. Decide whether

`mu_{alpha,theta} = mu_{alpha,theta^sym}`                         (11.1)

holds for every C2-admissible `theta`, despite the fact that the local operators are different.

A useful way to attack (11.1) is not to simulate eigenvalues, but to find the first analytic coefficient of the large-`|eta|` expansion of the integrated typed resolvent (8.2) that distinguishes `theta` from `theta^sym`, or else prove all such coefficients depend only on the symmetrization. Because second moments diverge in the heavy-tail regime, this likely requires bounded resolvent observables or fractional transforms rather than raw moments.

Use a new triple next run; suggested candidates are **B5** (interpolate `theta_t=(1-t)theta+t theta^sym` and differentiate the typed recursion), **B11** (dualize the resolvent fixed point into a functional equation for its Laplace/Fourier transform), and **B23** (assume the opposite of the source's apparent geometric intuition and actively search for a nonswap family whose integrated transform is nevertheless identical).

## 12. Capability statement requested by owner

The exposed automation update schema still offers title, prompt, schedule/timing mode, enablement, and related scheduling fields, but **no model selector and no reasoning-effort selector**. Therefore GPT-6/maximum remains a prompt request only; this run actually identifies as GPT-5.6 Sol with reasoning level UNVERIFIED.

This HARD7-02 run did not probe or modify any other schedule, because the task explicitly forbids modifying/creating other schedules. Repository policy records historical native modification failures for P26/P01/P03 (`You cannot modify this task`) and also records that P26 later succeeded from a different authorized context. The legitimate workaround is to use the authorized account/workspace context that owns the task or platform support; do not bypass the denial and do not create a duplicate schedule.

## 13. Ledger delta

```yaml
track: HARD7-02
source: Campbell-O'Rourke 2022 Question 1.8
claim: operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md
status: PARTIAL
frozen_metric: S
before: 3
after: 3
movement: no movement
unchanged_streak: 2
methods: [B7, B18, B27]
new_result: corrected rank-marked PWIT local operator limit for all fixed root-rank types and uniform-root mixture; continuum-type resolvent recursion
source_question_closed: false
checker: none; theorem-sized proof on page
next_obligation: decide whether full limiting ESD is invariant under swap-symmetrization theta -> (theta+tau#theta)/2
```
