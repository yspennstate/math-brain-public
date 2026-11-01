Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO SOURCE-METRIC MOVEMENT: `M_P0342 = 2/2 -> 2/2`. NEW MATHEMATICAL MOVEMENT: under the actual random `DTCS(n)` law, every boundary-invisible perturbation with any positive Hölder exponent is `o_{L^1}(1)` after `sqrt(n)` leaf-sum normalization; thus the worst-case deterministic Hölder threshold `1/2` collapses to the sharp Hölder-scale boundary `0` for this counterexample mechanism. Methods actually tried: B6, B21, B28.**

# P13 / P0342 — typical-DTCS positive-Hölder stability

Date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Native slot: `6aa7b253b37c8191b693d8dc79298d37`.  
Own root: `proofnet24/P13-outside-successor/`.

## 1. Continuity, mandatory first screen, ownership, and exclusions

This invocation continues the exclusive P13 successor `P0342`, governed by `operations/claims/P0342.md`. It does **not** reopen the retired I0051 / Aldous--Janson Open Problem 9 clade-covariance target, the completed six-unchanged-run C0021 terminal handoff, old AF4.49(ii)/PROB20-13, the DLA exponent route, P22/P23/P25, paused P17/P18, or any POSTED/INDEX exclusion.

I reread/recovered the controlling owner directive at anchor `749da260517828ed311f6f1b1af74915c054bdf3`, `operations/NEW_METHODS_2026-09-16.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md` and `QUEUE.md`, the canonical P0342 claim, the newest P13 report, the C0021 terminal handoff, current P0342 audit searches, the newest neighboring I0054 report, and targeted P0342 intake/attempt-history hits. The GitHub connector permits targeted search/fetch rather than a credible literal visual reread of every byte of every large append-only intake JSONL; I do not claim otherwise.

The mandatory I0054 screen was performed first. The source v3 still states Open Problem 18 as:

> Are there superficially different discrete models whose limit is the same `CTCS(infinity)`?

and immediately asks whether the subordinator-approximation feature can arise in another discrete tree model. The newest recovered R11 report is

`runs/R11/2026-09-19T16-40-00Z_i0054-growing-power-u051-c072-e4a7.md`.

It moves R11's own frozen author-side model-class metric `71 -> 72`, remains **PARTIAL at source/campaign level, not CLOSED**, and continues R11 ownership. P13 therefore did not touch I0054 or its claim.

The current P13 claim instead remains:

`operations/claims/P0342.md` — David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, Open Problem 12, Section 4.10.

Its frozen metric is

`M_P0342 in {0,1,2}` = the number of the `FRINGE` and `FINITE-FAILURE` obligations simultaneously established for the one fixed witness `Theta = Psi + Phi`.

Both obligations were already proved in earlier immutable P13 reports, so

`M_P0342 = 2/2 -> 2/2`.

The denominator remains frozen. The theorem below is genuine mathematical strengthening around the completed counterexample, not a third source obligation and not renewed source-metric movement.

Targeted repository search still recovers no end-to-end P0342 PASS from P26 and no end-to-end P0342 PASS from a distinct OTHER research track. Historical P12/P13 audits belong to the retired I0051 target and do not transfer. Campaign status therefore remains

`CLAIMED / METRIC-COMPLETE / SOURCE-REFUTATION-CANDIDATE / AUDITS-PENDING`.

No claim file, shared root ledger, peer file, or schedule is modified here.

## 2. Exact source scope and fresh current-literature check

The current arXiv v3 source still asks literally:

> If we know that, for a given functional `Phi`, a CLT holds for the fringe process `sum_{i=0}^{m-1} Phi(T_i)`, does the same CLT necessarily also hold for `DTCS(n)`, that is for `sum_{i=1}^n Phi(T_i^(n))`?

The nearby prose says first-order fringe convergence for “suitable functionals,” but Open Problem 12 itself does not state a Hölder, stabilization, locality-radius, or boundary-modulus assumption. P0342 therefore remains a candidate negative answer to the literal universal implication only; the theorem below studies one natural quantitative repair.

Fresh dated searches on 2026-09-19 used combinations of:

- `"Aldous Janson" "Open Problem 12" fringe CLT beta splitting`,
- `"critical beta-splitting" 2026 "Open Problem 12"`,
- `"critical beta-splitting" negative Laplace leaf height`,
- `"harmonic descent" exponential moments absorption time`, and
- `"regenerative composition" critical beta-splitting leaf height`.

They recovered, among other items:

1. Aldous--Pittel, *The Critical Beta-splitting Random Tree I: Heights and Related Results* (Ann. Appl. Probab. 35 (2025)), with the exact edge-height Laplace recurrence used below;
2. Aldous--Janson Part III on the exchangeable-partition/fringe representation and Part IV on Mellin analysis of leaf height;
3. Brandenberger--Chin--Mossel (arXiv:2505.24821) on harmonic-descent rates and fixed-clade CLTs;
4. Iksanov--Nikitin--Yakymiv (2026) on balls-in-boxes/regenerative-composition CLTs for critical beta-splitting leaf heights;
5. Chorbadzhiyska--Minchev--Savov (arXiv:2608.18320, 18 August 2026) on fragmentation and beta-splitting asymptotics; and
6. Heng Ma (arXiv:2609.14329 and 2609.14325, 13 September 2026), including the resolution of the distinct discrete-height Open Problem 4 and fragmentation/clade-count dynamics.

No checked primary source in this bounded search explicitly announces a resolution of exact Open Problem 12. I also did not locate an explicit statement of the boundary-stability theorem below. This is **bounded negative evidence only**. In particular, sharper published lower-tail or large-deviation estimates for leaf height may imply the negative-Laplace estimate below as a corollary; I make no novelty or priority claim for that estimate or for the theorem built from it.

## 3. Idea-before-proof receipt and the three methods

Before writing the proof, I committed

`proofnet24/P13-outside-successor/artifacts/2026-09-19/2026-09-19T17-12-54Z__p0342_b6_b21_b28_typical-holder-idea.md`

at commit `8c4a80b1834af49d8fc812ca34ce62be987f249c` and read it back at that exact commit; verified blob `3699d37da03defe8b87f7e0567250359efbd6f54`.

The methods differ from the preceding B1/B13/B30 triple.

**B28 — REPLACE “FOR ALL” WITH “FOR TYPICAL”.** The previous theorem optimized over every deterministic full binary tree and found the sharp worst-case Hölder threshold `beta=1/2`. Here I instead average over the actual `DTCS(n)` tree. The relevant geometric quantity becomes the negative exponential moment of a uniformly sampled leaf depth.

**B6 — DEFORM TO A POINT YOU CAN SOLVE.** Set the Laplace parameter to the fixed negative value `u=-beta log 2` and deform the exact Aldous--Pittel recurrence against the trial supersolution `n^{-a}`. This succeeds for every `a<1`, which is much stronger than the `a>1/2` needed for `sqrt(n)` stability.

**B21 — ASK WHO ELSE HAS THIS SHAPE.** The harmonic-descent, Mellin, regenerative-composition and fragmentation literature supplies the exact recurrence and much sharper height asymptotics, but the bounded search did not expose the precise boundary-invisible perturbation theorem. This method was useful for locating the right recurrence and for limiting the claim: the recurrence argument below is elementary relative to that literature, and no novelty claim is made.

No new checker is warranted. The new claims are analytic and are proved completely below; there is no new finite enumeration. The historical P0342 exact checker remains a P13 self-check only.

## 4. Setup: boundary-invisible Hölder perturbations

Use the same local metric convention as the previous P0342 reports. For two leaf-rooted ordered trees `S,T`, let

`d_loc(S,T)=2^{-R(S,T)}`

up to the source-equivalent harmless one-radius convention, where `R` is the largest radius on which their rooted induced neighborhoods agree.

Call a functional `g` **boundary-invisible** if

`g(T)=0`

for every infinite one-ended fringe tree in the source state space.

Assume `g` is Hölder of exponent `beta>0`:

`|g(S)-g(T)| <= C d_loc(S,T)^beta`.

Let `T^(n)` be `DTCS(n)`. For leaf `i`, write `d_i` for its graph distance from the original phylogenetic root and `T_i^(n)` for the tree rerooted at that leaf.

As in the preceding deterministic theorem, extend `T_i^(n)` beyond its old root by an infinite binary spine, adding arbitrary finite sibling branches so the result is a valid infinite one-ended binary fringe tree; call it `T_hat_i`. The finite and infinite rerootings agree until the old root. With the conservative one-radius convention,

`d_loc(T_i^(n), T_hat_i) <= 2^{1-d_i}`.

Since `g(T_hat_i)=0`, Hölder continuity gives the pointwise deterministic bound

`|g(T_i^(n))| <= C 2^beta 2^{-beta d_i}`.                                           (4.1)

Thus the entire problem reduces to the negative exponential moment of a uniformly random leaf height.

## 5. Exact edge-height recurrence

Let `L_n` be the edge-height of a uniformly chosen leaf of `DTCS(n)`, and put

`f_n(u)=E[e^{u L_n}]`.

For completeness, the recurrence can be recovered directly from the source split rule. A size-`n` clade has oriented split-size probability

`q(n,k)= n / [2 H_{n-1} k(n-k)]`,

with `H_m=sum_{j=1}^m 1/j`. If a leaf is uniform, the probability that its child clade after the root split has size `k` is the sum of the two orientations:

`P(K_n=k)=2 q(n,k) (k/n)=1/[H_{n-1}(n-k)]`,      `1<=k<n`.                         (5.1)

Therefore

`L_n = 1 + L_{K_n}`

in distribution with the recursive copy conditionally independent below the chosen child, and hence, for every real `u`,

`f_1(u)=1`,

`f_n(u)= e^u/H_{n-1} * sum_{k=1}^{n-1} f_k(u)/(n-k)`,      `n>=2`.                (5.2)

This is the exact Aldous--Pittel recurrence.

## 6. B6 power barrier for every fixed negative Laplace parameter

### Proposition 1 — near-`n^{-1}` decay of fixed negative exponential moments

Fix `u<0`. For every `a` with `0<a<1`, there is a finite constant `C(u,a)` such that

`f_n(u) <= C(u,a) n^{-a}`                                                       (6.1)

for every `n>=1`.

Equivalently, for every `beta>0` and every `a<1`,

`E[2^{-beta L_n}] = O_{beta,a}(n^{-a})`.                                         (6.2)

#### Proof

Write `c=e^u`, so `0<c<1`. Suppose inductively that

`f_k(u) <= C k^{-a}`

for all `k<n`. By (5.2),

`f_n(u) <= C c/H_{n-1} * sum_{k=1}^{n-1} k^{-a}/(n-k)`.                         (6.3)

Thus it suffices, for large `n`, to show

`R_n(a):= c n^a/H_{n-1} * sum_{k=1}^{n-1} k^{-a}/(n-k) <= 1`.                   (6.4)

Set `j=n-k`. Then

`n^a sum_{k=1}^{n-1} k^{-a}/(n-k)
 = sum_{j=1}^{n-1} (1-j/n)^{-a}/j
 = H_{n-1} + D_n(a)`,                                                           (6.5)

where

`D_n(a)=sum_{j=1}^{n-1} [(1-j/n)^{-a}-1]/j >=0`.

I claim

`D_n(a)=O_a(1)`.                                                                (6.6)

Split at `j=n/2`.

For `j<=n/2`, the derivative of `(1-x)^{-a}` is bounded on `[0,1/2]`, so by the mean value theorem

`(1-j/n)^{-a}-1 <= C_a j/n`.

After division by `j`, each summand is at most `C_a/n`, and this half contributes `O_a(1)`.

For `j>n/2`, put `r=n-j`, so `1<=r<n/2`. Since `1/j<=2/n`,

`[(1-j/n)^{-a}-1]/j
 <= (n/r)^a * 2/n
 = 2 n^{a-1} r^{-a}`.

Because `a<1`,

`sum_{r<=n/2} r^{-a} = O_a(n^{1-a})`,

so the second half also contributes `O_a(1)`. This proves (6.6).

Combining (6.4)--(6.6),

`R_n(a)=c [1+O_a(1/H_{n-1})] -> c < 1`.                                         (6.7)

Hence there is `N=N(u,a)` such that `R_n(a)<=1` for every `n>=N`. Choose

`C >= max_{1<=m<N} m^a f_m(u)`.

Then the desired bound holds for the finite base range and (6.3)--(6.7) propagate it inductively for all `n>=N`. This proves (6.1). Substituting `u=-beta log 2` gives (6.2). `square`

### Comment on strength and limitations

The proof gives every exponent `a<1`, but does not assert a sharp asymptotic for `f_n(u)`. The constant can deteriorate badly as `u` approaches zero or `a` approaches one. This is entirely sufficient for the present `sqrt(n)` application.

## 7. B28 theorem — the random DTCS threshold collapses from `1/2` to `0`

### Theorem 2 — positive-Hölder boundary stability in actual `DTCS(n)`

Let `g` be boundary-invisible and Hölder of any exponent `beta>0`. Then

`(1/sqrt(n)) sum_{i=1}^n |g(T_i^(n))| -> 0` in `L^1`,                            (7.1)

and therefore

`(1/sqrt(n)) sum_{i=1}^n g(T_i^(n)) -> 0` in `L^1` and in probability.          (7.2)

The same is true after centering the finite sum by its expectation.

#### Proof

Conditional on the realized finite tree, a uniformly selected leaf has height distributed as the empirical depth distribution. Hence

`(1/n) sum_{i=1}^n 2^{-beta d_i}
 = E[2^{-beta L_n} | T^(n)]`.                                                    (7.3)

Using (4.1), then taking expectation,

`E[(1/sqrt(n)) sum_i |g(T_i^(n))|]
 <= C 2^beta sqrt(n) E[2^{-beta L_n}]`.                                         (7.4)

Choose any fixed `a` with `1/2<a<1`. Proposition 1 gives

`E[(1/sqrt(n)) sum_i |g(T_i^(n))|]
 <= C' n^{1/2-a} -> 0`.                                                         (7.5)

This proves (7.1), hence (7.2). For the centered sum, use

`E|S_n-E S_n| <= E|S_n| + |E S_n| <= 2E|S_n|`

with `S_n=sum_i g(T_i^(n))`. `square`

This is substantially stronger than the preceding **uniform-over-all-trees** theorem. There the deterministic Kraft extremal family showed that `beta>1/2` is necessary and sufficient for worst-case `sqrt(n)` negligibility. Under the actual random `DTCS(n)` law, every `beta>0` suffices.

The mechanism is geometric: a worst-case balanced tree has all leaf depths only `Theta(log n)`, whereas a typical critical-beta-splitting leaf has height of order `log^2 n`; fixed negative exponential moments are consequently crushed faster than `n^{-a}` for every fixed `a<1` by the exact recurrence.

## 8. Source-relevant corollary for the P0342 architecture

The earlier P13 report proved that the local size-three orientation mark `Psi` has the same positive-variance Gaussian limit in the fringe process and in finite `DTCS(n)`:

`N(0, 3/(2 pi^2))`.

Let `g` be any boundary-invisible positive-Hölder perturbation and define

`Theta_g = Psi + g`.

On the infinite fringe process, `g` vanishes identically, so the fringe sums of `Theta_g` equal those of `Psi` exactly. On finite `DTCS(n)`, Theorem 2 gives

`n^{-1/2} sum_i [Theta_g(T_i^(n))-Psi(T_i^(n))] -> 0`

in probability, and the centered version also tends to zero. Slutsky's theorem therefore yields:

### Corollary 3

For every boundary-invisible Hölder perturbation of any positive exponent,

`Theta_g = Psi + g`

has the **same** `N(0,3/(2 pi^2))` `sqrt(n)` limit in finite `DTCS(n)` as in the stationary fringe process. In particular, no P0342 counterexample can be produced from the already-good local mark `Psi` by adding a boundary-invisible perturbation with positive Hölder exponent.

This is a source-relevant obstruction to the counterexample mechanism, not a proof of a strengthened Open Problem 12 for all Hölder functionals. A general Hölder functional need not decompose into a baseline with a known matching finite/fringe CLT plus a boundary-invisible perturbation.

## 9. Sharpness in the Hölder scale: mere continuity can fail

The current P0342 counterexample uses exactly a boundary-invisible global perturbation `Phi` that is continuous in the source-relevant local topology but, as proved in the preceding P13 regularity report, is **not Hölder of any positive exponent**. Along comb trees its finite-to-infinite discrepancy decays only polynomially in the visible root distance while the local metric decays exponentially.

That same `Phi`, added to `Psi`, already satisfies the positive-variance fringe CLT and destroys the finite transfer. Therefore, within this explicit boundary-invisible perturbation architecture, Theorem 2 is sharp in the Hölder exponent scale:

- every `beta>0` is stable under the actual `DTCS(n)` law;
- exponent `0` / mere continuity is not sufficient.

This should not be overread as a complete characterization of all possible regularity assumptions that repair Open Problem 12. It says exactly that **positive Hölder control rules out the existing global-boundary escape mechanism**, while continuity alone does not.

## 10. B21 comparison with nearby literature

Aldous--Pittel already emphasize recursive inequalities and Laplace transforms for leaf-height asymptotics. Aldous--Janson Part IV obtains sharper Mellin-based height estimates; Iksanov and collaborators obtain regenerative-composition/balls-in-boxes descriptions and joint CLTs; Chorbadzhiyska--Minchev--Savov give fragmentation/subordinator asymptotics across the beta-splitting family; Brandenberger--Chin--Mossel analyze rates for harmonic-descent recurrences.

The present proof is intentionally elementary relative to those results: it needs only the exact fixed-negative-parameter recurrence and a power supersolution. A sharper lower-tail theorem in that literature may subsume Proposition 1. The bounded search did not find the exact statement “every boundary-invisible positive-Hölder perturbation is `o_{L^1}(sqrt(n))` in DTCS leaf sums,” but absence from this search is not evidence of novelty.

B21 therefore **worked as a method-selection and claim-limiting route**, not as a novelty certificate. It located the correct recurrence and shows that the new theorem belongs naturally to existing harmonic-descent/height technology.

## 11. What moved, what did not, and next research question

Source metric:

`M_P0342: 2/2 -> 2/2` — **no source-metric movement**.

Mathematical scope did move. The previous deterministic theorem had the exact worst-case stability boundary `beta=1/2`; the present theorem proves that on the actual random source model the boundary-invisible Hölder threshold is `beta=0` in the sense above. It also proves a near-`n^{-1}` fixed-negative-Laplace power barrier directly from the source recurrence.

The strongest next source-relevant regularity question is no longer whether Hölder continuity blocks this P0342 mechanism; it does. The next useful target is to identify the weakest **non-Hölder** modulus `omega` for which

`sqrt(n) E[omega(2^{-L_n})] -> 0`,

and compare that exact typical-DTCS criterion against the known continuous counterexample modulus. That would refine the gap between positive Hölder regularity and mere continuity without changing the frozen source metric.

No finite checker was manufactured because no finite enumeration claim moved. The theorem-sized claims are proved on the page.

## 12. Delivery and structured ledger delta

Idea-before-proof artifact:

`proofnet24/P13-outside-successor/artifacts/2026-09-19/2026-09-19T17-12-54Z__p0342_b6_b21_b28_typical-holder-idea.md`

creation commit `8c4a80b1834af49d8fc812ca34ce62be987f249c`, verified read-back blob `3699d37da03defe8b87f7e0567250359efbd6f54`.

This report is immutable under the P13 root. It does not update root `RESULTS.md`, `QUEUE.md`, any peer file, or any canonical claim.

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  target: P0342
  source: Aldous-Janson arXiv:2303.02529v3 Open Problem 12
  lane: CLOSABLE_OUTSIDE
  metric_name: M_P0342
  metric_domain: fixed single witness Theta=Psi+Phi; obligations [FRINGE, FINITE-FAILURE]
  before: 2/2
  after: 2/2
  source_metric_movement: false
  mathematical_movement: true
  new_result: >-
    For every boundary-invisible beta-Hölder perturbation g with beta>0,
    n^{-1/2} sum_i |g(T_i^(n))| -> 0 in L1 under DTCS(n). Equivalently,
    the existing boundary-invisible counterexample mechanism cannot work inside any
    positive Hölder class. The fixed-negative leaf-height Laplace moment obeys
    E[exp(u L_n)] = O_{u,a}(n^{-a}) for every u<0 and every a<1.
  methods: [B6, B21, B28]
  status: CLAIMED_METRIC_COMPLETE_SOURCE_REFUTATION_CANDIDATE_AUDITS_PENDING
  p26_end_to_end_audit: not_recovered
  distinct_other_end_to_end_audit: not_recovered
  self_check: none_new_analytic_proof_on_page
  prior_art: bounded_negative_only_no_novelty_claim
  peer_edits: none
  shared_root_edits: none
  scheduler_changes: none
```

No email/Gmail, Drive, public posting, paid compute, credential or permission change, force-push, workflow execution, external contact, or scheduler modification was performed.