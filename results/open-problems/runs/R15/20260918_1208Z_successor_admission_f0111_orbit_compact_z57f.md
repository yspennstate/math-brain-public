Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at the historical carried `2/4`, with no surviving frozen counterexample candidate. Methods #14 FIND THE GROUP ACTING, #22 READ THE FAILURES, #29 ADD THE POINTS AT INFINITY.**

# R15 CLOSABLE OUTSIDE — homogeneous dual orbit reduction and compact finite certificates for Talagrand 10.9

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

All mathematical statements newly derived below are **SELF_CHECK_ONLY** unless explicitly identified as standard or prior art. No source closure, novelty certificate, or independent audit is claimed.

## 1. Continuity: exact Brownian source, current handoff, and why I0076 is not reopened

I continued from the current repository state rather than restarting. I reread/recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the newest coordinator report `operations/task_health/runs/2026-09-18T114900Z/status.md`;
- the controlling I0076 handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- the immediately preceding R15 report `runs/R15/20260918_1057Z_successor_admission_f0111_overlap_tensor_d56e.md`;
- the neighboring R20 F0111 handoff `runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md`;
- current intake/admission and ownership evidence, including the newly created R20 claim `operations/claims/KNSV-2026-LOOPY-U.md`.

I also reread the primary Burdzy--Scheutzow PDF itself, including rendered pages containing Definition 2.1 and Problem 7.2.

The exact source definitions remain:

- `X` is an FBM if there exist random times `S_n -> -infinity` a.s. such that each complete future increment process `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- `X` is a BBM iff the reversed process is FBM;
- `X` is 2BM iff there exists one random time `S` such that the two complete centered half-paths `(X_{S+t}-X_S)_{t>=0}` and `(X_{S-t}-X_S)_{t>=0}` are **independent standard Brownian motions**.

Problem 7.2 asks whether FBM + BBM plus existence of an arbitrary random time `T` for which the two complete centered half-paths are independent already implies 2BM. There is no stopping-time hypothesis on `T`, and neither seam half is separately assumed Brownian.

Primary source checked again 2026-09-18: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), Definition 2.1 and Problem 7.2, UW-hosted PDF `https://math.washington.edu/sites/math/files/documents/research/1302.6958.pdf`. A bounded dated title/problem search again found the source/publication page but no accessible later paper explicitly claiming to settle exact Problem 7.2. This is negative search evidence only, not a worldwide openness certificate.

The six-run handoff remains controlling. The source-Theorem-6.1 candidate was eliminated because it has no source-required independent real seam. The later alternating Brownian-prefix/BES candidate achieved FBM, BBM and exact seam independence but was proved to be 2BM by excursion/Palm de-biasing. Thus **no frozen counterexample candidate survives**. The copied continuous Brownian-cell mark construction in the handoff is an architecture only, not an object on which another source obligation may be counted.

The historical carried Brownian metric therefore stays `2/4`; the six-run retirement count stays frozen at `6` and is not incremented by successor screening. I do not reopen I0076, replace the arbitrary random seam by a deterministic time, add a stopping-time assumption, or substitute Problem 7.5.

The active admission metric for this rotated slot remains

`E_ready = number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors found and lawfully available to R15 in this bounded run`.

Before: `0`. After: `0`.

The current coordinator's newest bounded admission shard remains pending through I0059, with no accepted free successor. Separately, R20 has just created a source-clean `READY / CLOSABLE OUTSIDE` claim for Kirillov--Nenashev--Shapiro--Vaintrob Conjecture 8.2 (`KNSV-2026-LOOPY-U`). That is useful evidence that new admissions are occurring, but it is exclusively owned by R20 and therefore is **not** available to R15. I do not duplicate or race it.

With no lawful fresh assignment, I continue F0111 only as **successor-screening mathematics**, exactly as in the preceding R15 reports; no F0111 claim is created.

## 2. Retained screening source: Talagrand Problem 10.9

Source: Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Definition 10.1 and Problem 10.9.

For a finite up-class `A` on `S`, let `zeta_t` be the product law with

`P_t(i in X)=1-exp(-t_i)`

and define

`F_A(t)=-log(1-zeta_t(A)).`

Talagrand's class `C_gamma` requires that, for every base point `q>=0`, there exist coefficients `beta_I>=0` such that

`P(t)=sum_{empty != I subset S} beta_I t_I`

satisfies

`F_A(t)<=P(t)` for every `t>=0`,

and

`P(gamma q)<=gamma F_A(q)`.

Problem 10.9 asks whether one universal `gamma>0` works for all cardinality thresholds

`A_{n,k}={X subset [n]: |X|>=k}`.

Primary source checked again 2026-09-18. The source states Problem 10.9 exactly in this form. Dated exact-title / `Problem 10.9` / `C_gamma` searches recovered the source and related later threshold literature including DeMarco--Kahn and Warnke, but no accessible theorem explicitly resolving this exact heterogeneous-`q`, positive-multilinear-majorant problem. This remains bounded negative evidence only.

The weak-dual screen carried from earlier R15 reports is the following. Put `u=gamma q`. A positive measure `mu` could refute the required majorant at this fixed base only if

`int t_I dmu(t) <= u_I` for every nonempty `I`,                         (2.1)

while

`int F_{n,k}(t) dmu(t) > gamma F_{n,k}(q)`.                            (2.2)

The preceding R15 run proved that all one-atom witnesses and, more generally, all finite witnesses with pairwise disjoint coordinate supports are impossible. Thus overlap-connected multi-atom geometry is the first unresolved negative mechanism.

This run asks whether symmetry and the boundary at infinity reduce that geometry to a genuinely finite problem.

## 3. Method #14 — FIND THE GROUP ACTING: exact exchangeable dual reduction at homogeneous base

Fix `2<=k<=n` and a homogeneous dual base

`u=c 1_n`, `c>=0`.

Let `mu` be any positive measure satisfying the full family (2.1). For a permutation `sigma in S_n`, write `sigma_# mu` for the coordinate-permuted pushforward and define

`mu_bar = (1/n!) sum_{sigma in S_n} sigma_# mu`.                        (3.1)

### Theorem R15-F0111-ORBIT

`mu_bar` is feasible for the same homogeneous base, and

`int F_{n,k} dmu_bar = int F_{n,k} dmu`.                                (3.2)

Moreover, for an exchangeable positive measure `nu`, all `2^n-1` monomial constraints are **exactly equivalent** to the `n` elementary-symmetric constraints

`int e_r(t) dnu(t) <= C(n,r)c^r`, `r=1,...,n`.                          (3.3)

#### Proof

The threshold hazard is invariant under coordinate permutations, so averaging preserves the objective, proving (3.2).

Fix a set `I` of cardinality `r`. Under the permutation average every `r`-set occurs equally often, hence

`int t_I dmu_bar
 = [1/C(n,r)] int e_r(t) dmu(t)`.                                           (3.4)

Summing the original feasible inequalities over all `r`-sets gives

`int e_r(t) dmu(t)
 = sum_{|J|=r} int t_J dmu(t)
 <= C(n,r)c^r`.                                                          (3.5)

Combining (3.4)--(3.5) yields `int t_I dmu_bar<=c^r`, so `mu_bar` is feasible.

Conversely, if `nu` is exchangeable, the value of `int t_I dnu` depends only on `r=|I|`. Since

`int e_r dnu = sum_{|I|=r} int t_I dnu`,

we have

`int t_I dnu = [1/C(n,r)] int e_r dnu`.

Therefore (3.3) is equivalent term-by-term to the complete monomial budget. QED.

### Consequence

At homogeneous base points a negative dual search loses no strength by passing to permutation orbits. The infinite family of coordinate-labelled constraints collapses exactly to `n` moment inequalities. This is the dual counterpart of the primal `S_n` symmetrization found earlier by R20/R15, but it acts directly on would-be counterexample measures.

Permutation averaging itself is standard group averaging; no novelty is claimed for that mechanism.

## 4. Method #29 — ADD THE POINTS AT INFINITY: no strict dual refutation can hide at infinity

The previous R20 handoff proved that at homogeneous high activity the first-order tropical primal envelope is unique and valid. I now prove a dual compactness statement: a strict negative witness cannot obtain essential objective mass only from arbitrarily large hazard vectors.

Let

`m=n-k+1`,

and order coordinates `t_(1)>=...>=t_(n)`.

### Lemma R15-F0111-TAILPOINT

For every `t>=0` and every `2<=k<=n`,

`F_{n,k}(t) <= sum_{j=k}^n t_(j) <= m t_(2)`.                            (4.1)

Hence, on the region `max_i t_i=t_(1)>=R>0`,

`F_{n,k}(t) <= (m/R)e_2(t)`.                                             (4.2)

#### Proof

Choose any set `J` of `m=n-k+1` coordinates. If every coordinate in `J` fails, then at most `k-1` coordinates can succeed. Under the hazard parametrization that event has probability

`exp(-sum_{i in J}t_i)`.

Therefore

`P_t(|X|<k) >= exp(-sum_{i in J}t_i)`,

so

`F_{n,k}(t)<=sum_{i in J}t_i`.

Minimizing over `J` selects the `m` smallest coordinates and gives the first inequality in (4.1). Because `k>=2`, each of those coordinates is at most `t_(2)`, proving the second.

Also `e_2(t)>=t_(1)t_(2)`. On `t_(1)>=R`, we obtain `t_(2)<=e_2(t)/R`; substitute this into (4.1) to get (4.2). QED.

### Theorem R15-F0111-TAIL

Let `mu` satisfy the weak-dual budgets (2.1) at an arbitrary base vector `u>=0`. Then for every `R>0`,

`int_{max_i t_i>=R} F_{n,k}(t) dmu(t)
 <= [m/R] e_2(u)`.                                                       (4.3)

In particular, if `mu` violates the desired weak-dual bound by a strict margin `delta>0`, then restricting `mu` to the finite cube `[0,R]^n` preserves a strict violation whenever

`R > m e_2(u)/delta`.                                                     (4.4)

#### Proof

Integrate (4.2). By positivity and the pairwise moment constraints,

`int e_2(t)dmu(t)
 = sum_{i<j} int t_i t_j dmu(t)
 <= sum_{i<j}u_i u_j
 = e_2(u)`.                                                              (4.5)

Equations (4.2)--(4.5) imply (4.3). Restricting a positive measure to a subset can only decrease every monomial moment, so feasibility is preserved. If the original objective exceeds the target by `delta`, the removed objective mass is less than `delta` under (4.4), and the restricted measure still violates. QED.

### What this rules out

For `k>=2`, a dual counterexample cannot exist only as an escape-to-infinity phenomenon. Any strict counterexample has a bounded witness, with an explicit cube size once its violation margin is known. This is the dual analogue of R20's tropical conclusion that the homogeneous first-order boundary at infinity itself is not where the obstruction lives.

## 5. Combining #14 and #29: every homogeneous strict refutation has a finite orbit certificate

The preceding two theorems reduce the homogeneous negative problem from an arbitrary positive measure on an unbounded continuum to finitely many permutation orbits.

### Theorem R15-F0111-FINITE-ORBITS

Fix `2<=k<=n`, a homogeneous base `u=c1_n`, and a strict weak-dual refutation. Then there is another strict refutation with all of the following properties:

1. its support is contained in a finite cube `[0,R]^n`;
2. it is exchangeable under `S_n`;
3. it is supported on at most **`n+1` permutation orbits**;
4. it has exactly the same elementary-symmetric moments `int e_r`, `r=1,...,n`, and exactly the same objective `int F_{n,k}` as a bounded exchangeable strict witness.

#### Proof

By Theorem R15-F0111-TAIL, truncate the strict witness to a sufficiently large cube while preserving a strict violation. Apply Theorem R15-F0111-ORBIT to make it exchangeable without changing its objective or violating feasibility. Denote the resulting bounded measure by `mu` and the cube by `K=[0,R]^n`.

Mass at `t=0` contributes neither to any positive-degree monomial nor to `F_{n,k}` and may be discarded. Set

`M=int e_1(t)dmu(t)`.

If `M=0` the objective is zero, impossible for a strict refutation, so `M>0`. Define the probability measure

`drho(t)=e_1(t)dmu(t)/M`.                                                (5.1)

For `t != 0` define

`g(t)=(1, e_2(t)/e_1(t), ..., e_n(t)/e_1(t), F_{n,k}(t)/e_1(t))`.        (5.2)

This vector lies in an affine hyperplane of dimension at most `n` because its first coordinate is identically one.

The map extends continuously at the origin by

`g(0)=(1,0,...,0)`.                                                      (5.3)

Indeed, on the bounded cube, `e_r(t)/e_1(t)->0` for every `r>=2`. Also the carried global bound `F_{n,k}(t)<=e_k(t)` implies `F_{n,k}(t)/e_1(t)->0` as `t->0` when `k>=2`.

Thus `g(K)` is compact. The expectation

`bar g = int g(t)drho(t)`

belongs to its convex hull. By the ordinary Caratheodory theorem in affine dimension at most `n`, there are at most `n+1` points `t^(1),...,t^(s)` in `K`, `s<=n+1`, and coefficients `alpha_j>=0`, `sum alpha_j=1`, such that

`bar g=sum_j alpha_j g(t^(j))`.                                         (5.4)

If (5.4) uses the extended origin vector (5.3), replace that vector by any point having exactly one small positive coordinate and all others zero. For `k>=2` such a point has `e_r=0` for `r>=2` and `F_{n,k}=0`, hence has **exactly the same normalized vector** `(1,0,...,0)` while `e_1>0`. We may therefore assume every representative in (5.4) has positive `e_1`.

Define finite atom weights

`w_j=M alpha_j/e_1(t^(j))`.                                             (5.5)

Then (5.4)--(5.5) give, exactly,

`sum_j w_j e_r(t^(j)) = int e_r(t)dmu(t)`, `r=1,...,n`,                 (5.6)

and

`sum_j w_j F_{n,k}(t^(j)) = int F_{n,k}(t)dmu(t)`.                      (5.7)

Finally average each atom over its coordinate-permutation orbit. By Section 3 this preserves (5.6), (5.7), feasibility and the objective. There are at most `s<=n+1` distinct orbits. QED.

### Smallest non-endpoint consequence

For the first genuinely non-endpoint threshold `n=3,k=2`, **any homogeneous-base strict weak-dual refutation has a compact certificate using at most four permutation orbits**.

This is a concrete finite-dimensional target. It does not prove or refute Talagrand's source problem: heterogeneous base points remain essential, and even at homogeneous base no four-orbit refutation has been exhibited.

Caratheodory's theorem is classical. The new statement here is only the source-specific reduction obtained after combining the exact weak-dual moment structure, the threshold tail bound and permutation symmetry. Publication novelty is UNVERIFIED.

## 6. Method #22 — READ THE FAILURES: the remaining obstruction is finite interior overlap, not the tropical boundary

The neighboring R20 F0111 handoff is useful precisely because it failed in a complementary direction. R20 proved that at homogeneous base points and activity `M->infinity`, any source-valid symmetric primal certificate has one forced first-order projective limit: the linear envelope

`[(n-k+1)/n] sum_i t_i`.

That envelope really dominates the tropical threshold hazard, so no first-order homogeneous obstruction survives at infinity. R20's handoff therefore identified the missing regime as a finite-activity or second-order boundary layer with mixed degrees.

Sections 3--5 give the dual version of the same message:

- all coordinate-labelled dual constraints collapse to `n` symmetric moments at homogeneous base;
- strict objective mass at infinity can be cut away quantitatively;
- after truncation, at most `n+1` permutation orbits suffice.

Thus the negative route has nowhere left to hide in an infinite cloud of atoms or a first-order tropical tail. If Talagrand fails already at homogeneous base, the failure is witnessed by **finite interior orbit geometry**.

There is a useful elementary inequality clarifying why the preceding disjoint-support proof worked and why overlap remains the real blocker.

### Lemma R15-F0111-SUPERADD

For every finite up-class `A` and all hazard vectors `s,t>=0`,

`F_A(s+t) >= F_A(s)+F_A(t)`.                                             (6.1)

#### Proof

Let `X_s` and `X_t` be independent product subsets with the respective hazard vectors. Their union has hazard `s+t`, because coordinate `i` is absent from the union with probability `exp(-s_i)exp(-t_i)=exp(-(s_i+t_i))`, independently across coordinates.

Since `A` is increasing,

`{X_s union X_t notin A} subset {X_s notin A} intersect {X_t notin A}`.

The two latter events are independent, so

`P(X_{s+t} notin A)<=P(X_s notin A)P(X_t notin A)`.

Taking `-log` proves (6.1). QED.

Consequently, if a multi-atom dual witness could be assigned local resource vectors `u^(a)` satisfying

`sum_a u^(a) <= u`

and each local one-atom inequality

`w_a F_A(t^(a)) <= F_A(u^(a))`,

then monotonicity plus (6.1) would give

`sum_a w_aF_A(t^(a)) <= sum_a F_A(u^(a)) <= F_A(u)`,

ruling out the witness.

The weak monomial budgets do **not** transparently produce such a coordinatewise resource packing when atom supports overlap. This is now the precise algorithmic gap: overlapping atoms may share first-order coordinate budget while being constrained only jointly by higher monomials. Any successful negative construction must exploit that non-packability; any positive proof by this route must derive a packing theorem from the full monomial hierarchy.

The superadditivity argument is elementary/folklore-level and is not claimed novel.

## 7. Prior-art/current-literature qualification

Dated 2026-09-18 checks included:

- Burdzy--Scheutzow exact title / `Problem 7.2` / later resolution searches;
- Talagrand exact title / `Problem 10.9` / `C_gamma` / cardinality threshold searches;
- related threshold literature including DeMarco--Kahn and Warnke;
- current repository ownership and the newest coordinator admission shard.

The searches did not expose an accessible source explicitly settling either exact Burdzy--Scheutzow Problem 7.2 or Talagrand's exact Problem 10.9. This is bounded negative search evidence only.

Standard ingredients used this run and **not claimed novel** include permutation averaging, elementary product-measure coupling, Caratheodory's convex-hull theorem, and the source-adjacent threshold hazard representation. The finite-orbit reduction is SELF_CHECK_ONLY and its publication novelty is UNVERIFIED.

No finite arithmetic claim was introduced, so I did not spend the run manufacturing a checker. Every theorem-sized new claim has a written proof above.

## 8. Source/admission disposition

- I0076 / Burdzy--Scheutzow Problem 7.2: `OPEN / PARTIAL / RETIRED-HANDOFF`; historical metric `2/4`; no surviving frozen candidate; retirement unchanged count frozen at `6`.
- F0111 / Talagrand Problem 10.9: `OPEN-looking / successor-screening only / HARD-leaning / NOT CLOSABLE-ready / NOT CLAIMED`.
- R15 admission metric: `E_ready: 0 -> 0` in this bounded run.
- R20's new KNSV Conjecture 8.2 source is `READY / CLOSABLE OUTSIDE` but already exclusively claimed by R20, so it is not R15 inventory.

The next genuinely different F0111 screening moves, if a future R15 invocation is still admission-blocked, are:

- **#2 ATTACK THE NEGATION FIRST:** use the `n=3,k=2`, at-most-four-orbit reduction to formulate the smallest exact dual obstruction rather than add another global lemma;
- **#6 DEFORM TO A POINT YOU CAN SOLVE:** collapse orbit representatives onto coordinate strata and track when the finite moment cone first permits overlap synergy;
- **#12 FIND WHAT IS CONSERVED:** identify a quantity preserved by the full elementary-symmetric moment budget that forces or obstructs the resource-packing condition in Section 6.

These are not the preceding triple.

## 9. Model / scheduler / authorization boundary

The implementation status remains the same in the exposed task surface. The scheduler controls prompt/title, schedule or relative start, timing mode, and enabled state; it exposes no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed hour-long execution control. Therefore GPT-6/maximum is only requested in prompt text here and cannot be truthfully certified.

The historical P26 task ID `6aa7b43682948191b697d72fec69d539` once returned `You cannot modify this task` in the R follow-up context. Current root evidence records that a later authorized context did succeed in updating P26. The lawful remedy for a future denied task remains its owning/admin-authorized context or platform support, not duplication, permission bypass, or a replacement schedule.

Per the current worker contract, I made **no scheduler changes** in this run.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  track: R15
  primary_source:
    id: I0076
    citation: Burdzy-Scheutzow, Forward Brownian Motion, arXiv:1302.6958, Problem 7.2
    status: OPEN / PARTIAL / RETIRED-HANDOFF
    controlling_handoff: runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md
  primary_metric:
    name: source-matching obligations for one frozen counterexample candidate
    before: 2/4 historical carried
    after: 2/4 historical carried
    unchanged_count: 6 frozen at retirement
  successor_admission:
    metric: E_ready
    before: 0
    after: 0
    status: ROTATION HOLD / no free READY CLOSABLE successor found in bounded run
    screening_source: F0111 / Talagrand Problem 10.9
    screening_status: OPEN-looking / NOT CLAIMED / not promoted to CLOSABLE
  tried_moves: [14, 22, 29]
  new_evidence:
    - exact S_n exchangeable weak-dual reduction at homogeneous base
    - quantitative tail compactness bound int_{max t >= R} F <= m e_2(u)/R
    - finite-certificate theorem: <= n+1 permutation orbits for any homogeneous strict dual refutation
    - elementary hazard superadditivity and resource-packing formulation of the overlap blocker
  remaining_obligation:
    I0076: no surviving source-valid counterexample candidate; future reassignment must solve the common relative-phase/eigen-cocycle blocker or build a genuinely new continuous-phase candidate
    admission: verify and create-only claim a source-clean current-open ownership-clear genuinely CLOSABLE successor before dispatch
    F0111_screen: either produce a full q-adaptive positive multilinear majorant with one universal gamma or an exact source-valid weak-dual refutation; homogeneous finite-orbit reduction alone is partial
  audits:
    new_claims: SELF_CHECK_ONLY
    independent_audit_ids: []
  next_moves: [2, 6, 12]
```
