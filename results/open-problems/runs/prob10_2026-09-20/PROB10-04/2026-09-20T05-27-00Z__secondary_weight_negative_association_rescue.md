Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# PROB10-04 run 6 — secondary-weight rescue swaps and an exact negative-association compiler

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source OPEN**.

**SOURCE-METRIC NO MOVEMENT.**  The independently verified explicit-decimal bracket used by this worker remains

`[alpha_L,alpha_U]=[3.52,4.4898]`,

so

`W_verified=alpha_U-alpha_L: 0.9698 -> 0.9698`.

This is an intentional method-change run after repeated endpoint nonmovement.  The previous `t_{r,r}` / exact-`f_{1,1,1}` rescue family is replaced by (i) an exact heterogeneous negative-association compiler, (ii) a much larger collision-free rescue family, and, most importantly, (iii) a **lexicographic secondary-weight extremal representative that unlocks one-rescue `t_{i,1}` swaps**.  At the rounded Diaz saddle the new one-rescue correction is about `1.87e-7`, roughly `53.4` times the log margin in the source's printed final bound, but this is only a local rounded-saddle diagnostic.  The refined global variational maximum has not yet been interval-certified at any lower density, so no new threshold endpoint is claimed.

## 1. Continuity, ownership, and evidence consumed

I continued only the existing scoped **cluster-aware weighted-counting / overlap-variational** claim in `operations/claims/PROB10-04.md`.  I did not take over the neighboring constructive lower-bound route and did not duplicate the interpolation worker's finite-support 1RSB trial.

Consumed repository state:

- `operations/PROB10_2026-09-20.md` @ blob `6f0fcee836d93371d43b84af1a55150fedc80779`;
- current `POSTED.md` @ blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`;
- scoped ownership `operations/claims/PROB10-04.md` @ blob `1095e6bfb106b53e810af56f2605521abb7143b4`;
- actual pre-refocus HARD7-06 handoff `runs/hard7_2026-09-18/HARD7-06/2026-09-19T23-49-30Z__handoff_to_prob10-04.md` @ blob `e59380417dc476970e22b72b66c59ffbffa4af3a`; it preserves the real `F0095` 3-colourability / binary-cascade work and is not relabeled as 3-SAT progress;
- preceding own report `runs/prob10_2026-09-20/PROB10-04/2026-09-20T04-08-00Z__diaz_rblock_rescue_transfer.md` @ blob `82d072a81db3a5033e9284d8acd6bda7818eb354`;
- neighboring cluster/interpolation report `proofnet24/NM13-13/progress-3sat/runs/2026-09-20/2026-09-20T04-07-30Z__t04_three_support_439539_rigorous_upper.md` @ blob `0dfecd71ffe7ae7c71e27b6ad1fb3b3bfd4bef74`;
- newest constructive neighbor read in this run, `proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/2026-09-20T05-29-47__t04_blocked_majority_core_and_promotion.md` @ blob `7fe7f9deae22224d234dd61a9954e53c5efe77ca`.

The immutable HARD7-06 handoff therefore already satisfies the owner requirement to preserve the actual F0095/binary-cascade target before the refocus; I did not create a duplicate handoff.

The mathematical idea was recorded before the first new checker in

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T04-48-36Z__heterogeneous_rescue_NA_idea_before_code.md`

creation commit `98e86c4eab4ca7bd2ba69bf2c81a25e712577daa`.

The later secondary-weight insight is separately frozen in

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T05-11-00Z__secondary_weight_swap_idea.md`

creation commit `1c32914ddec432ac6fffc9c25a27a302cbfecad6`.

## 2. Source status rechecked, with model distinctions frozen

The exact target remains the owner's model: `m=floor(alpha n)` independent clauses; each clause chooses three **distinct** variables uniformly and gives them independent uniform signs.

Fresh checks in this run support the following conservative baseline.

1. Diaz--Kirousis--Mitsche--Perez-Gimenez, <https://arxiv.org/abs/0807.3600>, Theorem 1.1 proves a.a.s. UNSAT at density `4.4898` for the uniform simple proper 3-CNF model.  Their paper explicitly distinguishes Friedgut sharpness from convergence of the threshold centers.  The source's configuration calculation uses `M=23`, an interior Lagrange critical point, and the final printed bound `(1+10^-7)0.9999998965<1`.
2. Hajiaghayi--Sorkin's classical theorem gives the explicit lower endpoint `3.52`.
3. The ESA 2025 paper <https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.103> explicitly says the classical model uses independent uniform clauses and then changes the model to `k`-wise-independent clauses.  Its results are therefore not a solution of the present source problem.
4. Ding--Sly--Sun, <https://arxiv.org/abs/1411.0650>, identify the threshold for all `k>=k_0` for an absolute sufficiently large constant `k_0`; that theorem is not automatically a `k=3` result.
5. Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis, published online 27 March 2026, state that the threshold is known exactly for `k=2` and sufficiently large `k`, while the fixed-small-`k` problem remains open.  Their interpolation framework supplies a stronger symbolic 1RSB upper functional; the displayed value near `alpha≈4.267` is not promoted here as an explicit rigorous decimal without reconstructing a certified numerical evaluation.

The source simple-formula convention and the owner's independent proper-clause convention are asymptotically equivalent for this upper-bound purpose.  There are `8*C(n,3)=Theta(n^3)` signed proper clauses, while `m=Theta(n)`, so the probability that the iid model repeats a whole clause is at most

`C(m,2)/(8 C(n,3))=O(1/n)`.

Thus the `4.4898` a.a.s.-UNSAT theorem transfers to the frozen iid model.

The neighboring NM13-13 report contains a complete-looking **CANDIDATE_FULL**, not yet independently validated, argument for `4.39539`.  I record it separately and do not promote it into this worker's verified metric.  This run is research, not an audit of that interpolation proof.

## 3. Why the preceding `r`-block mechanism was quantitatively weak

The previous report used only:

- centers `t_{r,r}` with `2<=r<=23`;
- leaves exactly `f_{1,1,1}`;
- one safe anchor clause type `((1,1),(1,0))`;
- one blocker clause type `((0,1),(1,1))`;
- a concentration step that halved the available centers and leaves before the final block-avoidance estimate.

That proved a positive interior defect but did not provide a useful explicit correction to the full Diaz variational objective.

Two structural observations remove nearly all of those restrictions.

### 3.1 The collision-free leaf pool is all `f_{i,1,1}`

A false variable of class `f_{i,1,1}` has exactly one negative occurrence and that occurrence is its unique `ns1` blocker.  Flipping it from false to true can therefore hurt only that blocker; every one of its `i` positive occurrences changes from false to true and helps.

So the marked leaf pool is

`E_1 = sum_{i=1}^M f_{i,1,1}`.                              (3.1)

The old report used only the `i=1` summand.

### 3.2 Every multiply-satisfied `ps` slot is a safe center anchor

If a true center is flipped false, a `ps` occurrence can hurt only its own clause.  Whenever that clause has at least two satisfied literals before the move, another satisfied literal remains.  A selected `f_{i,1,1}` leaf cannot be the disappearing second literal: its sole negative occurrence is `ns1`, hence is the unique satisfied literal in its blocker.  Its positive occurrences only turn false-to-true.

Therefore define

`Q_safe = sum_{alpha: ps(alpha)+ns(alpha)>=2} ps(alpha)c_alpha`. (3.2)

This replaces one rare clause type by every multiply-satisfied positive slot.

### 3.3 Every negative-unique-satisfied blocker with `nu>0` supplies one canonical rescue slot

A blocking 3-clause with its unique satisfied literal of class `ns1` and at least one `nu` slot has type

`((0,1),(1,1))` or `((0,1),(0,2))`.

Choose one deterministic `nu` slot per such clause and let

`B_can` be the total number of those canonical slots.           (3.3)

One canonical slot per clause is essential: if different center copies hit different canonical slots, their associated `ns1` blocker slots are automatically distinct.

## 4. New theorem I — heterogeneous Hamming-improving rescue centers

Let a true light center have class `t_{i,j}` with `j>=2`.  Call it **completed** when

1. all its `i` `ps` copies land in `Q_safe` slots;
2. all its `j` `nu` copies land in canonical slots from `B_can`;
3. the corresponding `j` blocker `ns1` slots are occupied by copies from the leaf pool `E_1`.

### Lemma 4.1 — deterministic rescue

A simple flat-satisfying assignment maximizing the number of true light variables has no completed center `t_{i,j}` with `j>=2`.

#### Proof

Let `y` be completed, and let `x_1,...,x_j` be the false `f_{k,1,1}` leaves in the associated blocker clauses.  The canonical blocker clauses are distinct because there is one canonical `nu` slot per clause and the center copies are matched injectively.

Simultaneously flip

`y:1->0`, `x_1,...,x_j:0->1`.                               (4.1)

For each leaf, its only negative occurrence is its `ns1` blocker.  That literal becomes false, but the center's `nu` literal in the same blocker becomes true.  Every positive leaf occurrence becomes true.  The center's `nu` occurrences also become true.

A center `ps` occurrence becomes false, but it lies in a clause that had another satisfied literal.  No selected leaf can make that other literal disappear: its only disappearing literal is its `ns1`, and an `ns1` clause had no other satisfied literal before the move.  Properness prevents a second occurrence of the center variable in the same clause.  Therefore every anchor clause remains satisfied.

No other clause can lose its last satisfied literal.  The new assignment is satisfying and has `j` additional true leaves but one fewer true center, so the true-light Hamming weight increases by `j-1>0`, contradicting maximality.  QED.

Because positive unbalancing has `i>=j` on light degree classes, at `M=23` this covers

`sum_{j=2}^{23}(24-j)=253`                                  (4.2)

center classes, versus only the 22 diagonal classes of the previous report.

## 5. New theorem II — exact negative-association compiler, with no concentration loss

Fix one integer coarse Diaz type.  Write

- `P,Q` for all `ps` target slots and the safe subset `Q_safe`;
- `U,B` for all `nu` target slots and the canonical blocker subset;
- `L,E` for all `ns1` target slots and the marked `E_1` leaf source copies;
- `C_{i,j}` for the number of center source blocks of class `(i,j)`.

For a center of class `(i,j)` define

`a_i=(Q)_i/(P)_i`, `b_j=(B)_j/(U)_j`, `e_j=(E)_j/(L)_j`,     (5.1)

where `(x)_r` is the falling factorial, with the ratio set to zero if the marked pool is too small.

### Proposition 5.1

Under the independent uniform `ps`, `nu`, and `ns1` label-class bijections used in the conditional Diaz copy allocation,

`P(no center is completed)`
` <= product_{i,j} (1-a_i b_j e_j)^{C_{i,j}}`.              (5.2)

The statement holds for heterogeneous disjoint center blocks; for Lemma 4.1 one uses only `j>=2`.

#### Proof

A uniform bijection hitting a fixed marked target subset induces, on the source copies, a uniform fixed-size `0/1` sample.  Such samples are negatively associated.  Negative association is preserved under coordinatewise monotone functions on disjoint coordinate blocks; the usual product inequality applies also to nonnegative decreasing block functions (equivalently pass to the complementary fixed-size sample).

Condition first on the complete `nu` matching and let `M_0` be the centers whose entire `nu` block hits canonical blocker slots.  Because the matching is injective and there is one canonical slot per blocker clause, the associated `ns1` target blocks of different centers in `M_0` are disjoint.

Now condition on which of those `ns1` blocks are entirely hit by marked leaf copies.  If that set of centers is `J`, negative association in the independent `ps` matching gives

`P(no safe-ps completion for every c in J)`
` <= product_{c in J}(1-a_{i(c)}).`                          (5.3)

Average (5.3) over the `ns1` matching.  Its full-block leaf-hit indicators are monotone functions on disjoint coordinate blocks of a fixed-size sample, hence are negatively associated.  Therefore

`P(no completed center | nu)`
` <= product_{c in M_0}(1-a_{i(c)}e_{j(c)}).`                (5.4)

Finally average (5.4) over the `nu` matching.  The canonical-block indicators are again negatively associated, and each center of class `(i,j)` has canonical-block probability `b_j`.  Hence

`P(no completed center)`
` <= product_c (1-a_{i(c)}e_{j(c)}b_{j(c)}),`                (5.5)

which groups by class to give (5.2).  QED.

This removes the preceding run's two concentration events, half-mean losses, polynomial prefactor, and unknown minimum of large-deviation constants.

### Corollary 5.2 — explicit asymptotic Hamming-rescue correction

For a fixed interior density vector `x`, put

`q=Q/P`, `d=(B/U)(E/L)`.

For fixed bounded degrees the falling-factorial ratios converge to powers, so the relative exponential correction is explicitly

`J_res(x) = -sum_{i>=j>=2} t_{i,j}(x) log(1-q(x)^i d(x)^j).` (5.6)

Thus the source objective may be refined locally as

`F_ref(x) <= F_Diaz(x) exp(-J_res(x))`.                      (5.7)

For the simple source formulas the deterministic rescue lemma is valid.  Counting **all** motif-free configurations, including nonsimple ones, is still an upper bound on the simple satisfying representatives, so the source's subexponential simplicity correction is not endangered by using the unconditional matching count in (5.2).

## 6. Main new mechanism — secondary-weight maximality unlocks `j=1`

The Hamming argument cannot exclude `j=1`: flipping one center and one leaf preserves the number of true light variables.  Instead choose a stronger representative.

For a fixed integer `K`, among satisfying assignments first maximize true-light Hamming weight; among those maximizers, maximize

`W_K = # { true light variables of degree class (k,1) with k>K }`. (6.1)

Every satisfiable formula has such a lexicographic maximizer, and the first maximization still makes every false light variable blocked, as required by the Diaz single-flip count.

### Lemma 6.1 — secondary-improving one-rescue swap

Fix `1<=i<=K`.  Suppose a true center `y` of class `t_{i,1}` has all `i` `ps` copies in `Q_safe`, its unique `nu` copy in a canonical blocker slot, and that blocker's `ns1` slot belongs to a false leaf `x` of class `f_{k,1,1}` with `k>K`.  Then the assignment is not lexicographically maximal.

#### Proof

Flip `y:1->0` and `x:0->1`.  The clause-by-clause argument of Lemma 4.1 with one leaf shows satisfiability is preserved.  The true-light Hamming weight is unchanged.  But `y` has class `(i,1)` with `i<=K` and contributes zero to `W_K`, while after the flip the leaf has class `(k,1)` with `k>K` and contributes one.  Hence `W_K` increases, contradicting secondary maximality.  QED.

Let

`E_{>K}=sum_{k=K+1}^M f_{k,1,1}`.                            (6.2)

Applying Proposition 5.1 with one-copy `nu` and leaf blocks gives the exact finite bound

`P(no secondary-improving swap)`
` <= product_{i=1}^K (1-a_i (B/U)(E_{>K}/L))^{C_{i,1}}`.    (6.3)

At a fixed interior density vector the explicit exponent is

`J_K(x) = -sum_{i=1}^K t_{i,1}(x)
               log(1-q(x)^i d_K(x)),`                       (6.4)

where

`d_K=(B/U)(E_{>K}/L)`.                                      (6.5)

This is the key change of scale: (5.6) starts at order `d^2`, while the one-rescue correction (6.4) is first order in `d_K`.

## 7. Rounded source-saddle reconstruction — auxiliary only, but large enough to matter

I reconstructed the source's Appendix-B core quantities and Appendix-E critical-point formulas using the six decimal multipliers printed by Diaz et al.:

`mu_ps=1.9972796`, `mu_ns1=0.45029358`, `mu_ns2=0.33794030`,

`nu_ps=1.2782018`, `nu_ns1=0.33277280`, `nu_ns2=0.95336927`.

The reconstruction uses the source equations

`sqrt(b)=1-exp(-(3 gamma/2)b)`,                               (7.1)

`delta^b_{i,j}=2 exp(-3 gamma b)(3 gamma b/2)^{i+j}/(i!j!)` for `i>j`, with the factor one on the diagonal, and the critical-point formulas (27) for `t,f,c,ell`.

The executed diagnostic gives

`Q_safe/ell_ps = 0.7479869238144213`,

`B_can/ell_nu  = 0.1278825275166306`,

`E_1/ell_ns1   = 0.00208095813522024`.                       (7.2)

For comparison, the old exact leaf pool `f_{1,1,1}` is only

`1.36156490501267e-5`,

whereas

`E_1 = 0.001116323754941311`,

an `81.99x` enlargement at the rounded saddle.

Using the exact NA compiler, the old narrow diagonal family has rounded-saddle correction

`J_old_narrow_NA ≈ 2.5286622371e-18`,

while the heterogeneous Hamming-improving family (5.6) gives

`J_res ≈ 5.3683506973e-10`,                                  (7.3)

about `2.12e8` times larger.  Even this is only about `15.3%` of the source's printed final log margin

`-log((1+10^-7)0.9999998965) ≈ 3.5000102877e-9`.

The secondary-weight route changes the picture.  Searching the finite integer thresholds `1<=K<23` at the same **rounded** source saddle gives its maximum at

`K=5`,

with

`E_{>5} ≈ 0.0005079222679878244`,

`J_5 ≈ 1.869587880794033e-7`.                                (7.4)

Hence, at the printed saddle only,

`J_5 / source_printed_log_margin ≈ 53.4166`.                 (7.5)

This is a strong mechanism signal, not a threshold theorem.  The six source multipliers are printed only to about eight significant digits, and, more importantly, once (6.4) is added the global maximizing type can move away from the old saddle.  Therefore I do **not** infer `alpha_U<4.4898` from (7.4)--(7.5).

Durable diagnostic:

- code `artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T05-16-00Z__secondary_weight_swap_saddle_diagnostic.py`, commit `c1e7000993e3910fd71f6c767c9dc5e60f54d7a6`;
- actual output `artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T05-16-30Z__secondary_weight_swap_saddle_diagnostic.out`, commit `f4020efcefe43dba2eccf45ae405d6cbbfbade72`.

The broader source-saddle reconstruction is in

- `2026-09-20T05-03-00Z__diaz_heterogeneous_rescue_saddle_diagnostic.py`, commit `9d6828e0458321bd83eddee3918ee648530489e3`;
- `2026-09-20T05-03-30Z__diaz_heterogeneous_rescue_saddle_diagnostic.out`, commit `c59afbc3e0c75251ffc80b62026e7deab4b7a93f`.

Both outputs explicitly label themselves as rounded-source diagnostics, not interval certificates.

## 8. Three materially different attacks and their outcomes

### Attack A — eliminate concentration entirely by negative association: **SUCCESS**

The previous typical-event proof was replaced by Proposition 5.1, an exact finite product bound valid for heterogeneous disjoint copy blocks.  This changes the mathematical object from a positive-but-unspecified interior defect to an explicit correction functional that can actually be inserted into a finite-dimensional optimizer.

### Attack B — change the extremal representative, not the local motif: **SUCCESS, MAIN ADVANCE**

A Hamming maximizer cannot exclude one-for-one rescue swaps.  Lexicographically maximizing the secondary degree-class weight `W_K` excludes a large family of `t_{i,1}` -> `f_{k,1,1}` swaps without changing the source model or the single-flip property.  The resulting exponent (6.4) is first-order in the blocker/leaf density and is about 53 times the source's printed final log margin at the rounded old saddle for `K=5`.

### Attack C — enlarge leaves naively to `f_{i,j,1}` with `j>1`: **NEGATION / DO NOT USE UNCHANGED**

The naive extension is false.  Such a leaf has `ns2` occurrences that turn true-to-false.  One of those can be precisely the extra satisfied literal protecting a center's nominally safe `ps` anchor clause, so simultaneous flipping can falsify the anchor.  This identifies the exact collision that the `j=1` leaf restriction avoids.

A potentially valid replacement is to use leaves whose **all** negative occurrences are blockers and rescue their full blocker bundles, or to build an alternating rescue cycle in which leaf `pu` occurrences rescue center anchors while center `nu` occurrences rescue leaf blockers.  Both require identity-preserving multi-layer matching rather than the independent marked-subset compiler.  I did not promote either to a theorem this run.

These are genuinely different mechanisms, not three parameter tweaks of the preceding `r`-block calculation.

## 9. Exact tests actually executed

The proof is on the page; the finite computations below are self-checks, not independent audits.

### 9.1 Heterogeneous three-layer NA model

Executed

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T04-56-00Z__heterogeneous_rescue_NA_exact.py`

creation commit `802dc8a21e72520d1e0fb7343a9be46be3d3fa95`.

Archived stdout

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T04-56-30Z__heterogeneous_rescue_NA_exact.out`

creation commit `a922dd8ab0f1eb1665108b90a326fcf87e6b0d03`.

It exhaustively enumerates the `ps` marked subset, full `nu` permutation, and `ns1` marked subset in eight heterogeneous small cases.  Every exact rational comparison satisfies (5.2), and output ends

`ALL_EXACT_NA_RESCUE_CHECKS_PASS = True`.

### 9.2 One-rescue secondary-swap specialization

Executed

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T05-22-00Z__secondary_swap_exact.py`

creation commit `edb2125edb44e007823ca62f2c80b9be5f330170`.

Archived stdout

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T05-22-30Z__secondary_swap_exact.out`

creation commit `ce1b6fc10c1b8fabdf17807f6c1b1b467b06d746`.

It exhaustively checks four `j=1` cases, including heterogeneous `i=1,2` centers.  Output ends

`ALL_EXACT_SECONDARY_SWAP_CHECKS_PASS = True`.

## 10. Before / after ledger

### Source-level verified explicit-decimal metric

- lower endpoint: `3.52 -> 3.52`;
- upper endpoint used by this worker: `4.4898 -> 4.4898`;
- width: `0.9698 -> 0.9698`;
- limiting `k=3` threshold existence / identification: **OPEN**.

### Neighboring internal candidate, kept separate

- NM13-13 currently records a `4.39539` upper endpoint as `CANDIDATE_FULL` pending independent validation;
- this run neither audits nor promotes it.

### Auxiliary mechanism progress

Before:

- deterministic completed-center theorem only for 22 diagonal classes `t_{r,r}`;
- exact leaf class only `f_{1,1,1}`;
- one safe-anchor type and one blocker type;
- concentration/half-mean losses before block avoidance;
- no mechanism at all for `j=1` centers.

After:

- 253 Hamming-improving light center classes `t_{i,j}`, `i>=j>=2`, covered by the same deterministic rescue argument;
- all `f_{i,1,1}` leaves covered;
- all multiply-satisfied `ps` anchors and both canonical negative-blocker types covered;
- exact finite NA compiler (5.2), with no concentration constants;
- explicit Hamming-rescue correction functional (5.6);
- a new lexicographic extremal theorem for one-rescue `t_{i,1}` centers, with explicit functional (6.4);
- rounded old-saddle `K=5` diagnostic `J_5≈1.8696e-7`, versus source printed log margin `≈3.5000e-9`.

The last number is **auxiliary numerical evidence**, not a certified endpoint movement.

## 11. Precise remaining full-scope gap

The local counting obstruction is no longer the bottleneck.  The exact remaining lemma for this route is:

> **Global refined Diaz optimization.**  Reconstruct the `M=23` source feasible polytope and objective with outward interval arithmetic, incorporate `J_K(x)` (preferably start with `K=5`), and certify
> `sup_x B_gamma(x) F_gamma(x) exp(-J_K(x)) < 1`
> for one explicit `gamma<4.4898`, including all boundary / heavy-variable / source-continuity error terms.

The old maximizer may move toward a region with a weaker swap penalty, so the large local ratio (7.5) does not pay this obligation.  Another local rescue checker would now be low-value work.

If the independent audit process first validates the neighboring `4.39539` interpolation theorem, this Diaz continuation should not chase a weaker decimal merely for ledger movement.  Its mathematically distinct value would then be either (a) a genuinely competitive globally certified endpoint from the secondary-weight correction, or (b) porting the secondary extremal constraint into a different cluster functional with a proved coupling.  Until one of those happens, PROB10-04 remains **PARTIAL / OPEN**.