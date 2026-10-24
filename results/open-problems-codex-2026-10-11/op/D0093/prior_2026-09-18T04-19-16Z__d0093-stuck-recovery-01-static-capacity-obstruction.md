Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime does not authenticate a GPT-6 model-family or maximum-reasoning selector, so I do not claim that configuration. **NO SOURCE-METRIC MOVEMENT: `beta_fast = 2 -> 2`; D0093 no-movement count `2 -> 3`; methods actually tried: B11 DUALIZE, B19 MAKE IT AN ALGORITHM, B20 FIND WHY THE ALGORITHM FAILS. STUCK RECOVERY 1 is triggered.**

# P13 — D0093 third research run: exact block-flow dual, online fresh tails, and the static-capacity obstruction

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Own root: `proofnet24/P13-outside-successor`.  
Canonical claim: `operations/claims/D0093.md`.  
Source: Leonardo T. Rolla, *Activated Random Walks on Z^d*, Probability Surveys 17 (2020), arXiv:1906.05037v2, Section 6.2, second Open Problem after Theorem 6.1 / equation (6.3).  
Status after this run: **OPEN / PARTIAL / STUCK RECOVERY 1**.

## 1. Continuity, exclusions, and frozen metric

The former P13 I0051 Aldous--Janson clade-covariance target remains RETIRED and was not reopened. P0082 remains handed off after its six-run rotation and was not reopened. The current exclusive P13 claim remains D0093, owned by native slot `6aa7b253b37c8191b693d8dc79298d37`.

The immediate predecessor is

`proofnet24/P13-outside-successor/runs/2026-09-18/2026-09-18T03-04-02Z__d0093-capacity-queue-reduction.md`.

The source-faithful metric remains

\[
\beta_{\rm fast}:=\inf\left\{\beta\ge0:\exists\kappa<\infty,\delta>0,
\ \mathbb P\!\left(T\le \kappa n(\log n)^\beta\right)\ge1-n^{-\delta}
\text{ for all large }n\right\},
\]

under exactly the source finite cycle, i.i.d.-Poisson initial law, symmetric nearest-neighbor jumps and fast-regime hypotheses used for (6.3). The certified source frontier is `beta_fast=2`; the requested endpoint is `0`.

The work below identifies a sharper interface and proves auxiliary lemmas, but it does not yet give a source-domain estimate with exponent below 2. Therefore

\[
\boxed{\beta_{\rm fast}:2\to2.}
\]

and the unchanged-run counter becomes three. No narrower model, different initial law, local processor, or changed metric is counted as movement.

## 2. Source/current-status reread

The required campaign/control surfaces were reread: the anchored owner directive, `operations/NEW_METHODS_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current D0093 claim, the newest P13 report, D0093 intake/attempt search surfaces, and the current ownership surface. The latest visible P14 state still does not expose a new 2026-09-18 P14 theorem requiring another directed P13 audit, so prior completed P13->P14 audits were retained rather than duplicated.

The original source was rechecked directly. It defines

\[
T=\sum_x m_{\mathbb Z_n,\eta_0}(x)
\]

as the total number of topplings. Theorem 6.1 proves, for fixed `0<zeta<1` and sufficiently large `lambda`,

\[
\mathbb P(T\le \kappa n\log^2n)\ge1-n^{-\delta},
\]

and the next explicit Open Problem asks to remove the `log^2 n` term. In the proof one chooses

\[
p:=\frac{\lambda}{1+\lambda}>\zeta'>\zeta,
\]

takes `r=floor(K log n)`, sends particles to sources by acceptable topplings, and then uses Proposition 6.5 to confine a centered pile of at most `2 zeta' r` particles in `[-r,r]` with failure probability `e^{-cr}`. The proof demands success at every source, so its union bound forces `r` to grow like `log n`.

A fresh bounded literature search on 18 September 2026 used variants of

- `"Removing the log^2 n factor" activated random walks cycle topplings`,
- `activated random walk cycle topplings linear bound 2026`,
- `fast phase activated random walks cycle Poisson topplings`,
- `layer percolation activated random walk cycle finite odometer 2025 2026`.

It recovered Tobias Johnson--Jacob Richey (2025), *The odometer in subcritical activated random walk*, which proves stretched-exponential one-site odometer tails on `Z` for i.i.d. Bernoulli initial data; 2026 work on explosivity, self-organized criticality, and the slow phase on the ring; and the original finite-cycle work. None of the checked primary results states the exact finite-cycle Poisson `O(n)` estimate requested here. This is only bounded negative evidence. It does **not** prove worldwide openness or publication novelty.

## 3. Idea before proof/code

The previous report replaced the source's `all blocks good` event by an abstract negative-drift queue with formal local capacities. The vulnerable point was that an ARW block is not a server with a precomputed, persistent capacity: pushing extra particles through a block can wake sleepers and consume precisely the instructions that a later trap construction hoped to use.

This run therefore does three things in a different order.

1. **B11:** use the source's exact block response functions and exact directed recurrence instead of pretending the model is already a scalar queue.
2. **B19:** isolate the one circumstance in which an online processor really does regenerate independent stack tails: the vector of consumed instruction counts must be a stopping line, i.e. the algorithm may react to used instructions but may not peek at instructions it leaves unused.
3. **B20:** test the missing persistence property on the smallest ARW block. It fails on the three-instruction stack `SJJ`. Then compare that failure with Rolla's non-Markovian trap exploration and identify the one source technique that can potentially repair it: corrupted-instruction shielding and an explicit unwind/flush of abandoned trap plans.

The result is not yet the source theorem, but the old vague phrase `history-dependent distributed repair` is replaced by one exact local interface.

## 4. B11 — dualize to the source's exact flow variables

### 4.1 The scalar queue is exact in the directed model

Rolla Section 3 contains a literal Lindley recursion for the totally directed one-dimensional model. Stabilizing from left to right gives

\[
N_{i+1}=[N_i+\eta_i-Y_i]^+,
\qquad
Y_i\sim\mathrm{Bernoulli}(p),
\qquad p=\frac{\lambda}{1+\lambda},
\]

with independent increments and drift `zeta-p`. Thus the previous run's negative-drift queue is not an alien analogy: it is exactly the source dynamics in the one-sided solvable case.

What fails in the symmetric ring is not the mass-balance principle; it is the reduction to **one scalar directed flux**.

### 4.2 The correct symmetric dual is a random two-sided response map

Rolla Section 5.1 already supplies the exact language. For a fixed block `i`, add `m` particles at its source and stabilize the block. Let

\[
L_i(m),\quad R_i(m),\quad S_i(m)
\]

be the numbers leaving left, leaving right, and sleeping in the block. These entire random functions are independent from block to block. For the corresponding two-layer global system the exact flow balance is

\[
\boxed{
 m_i=R_{i-1}(m_{i-1})+L_{i+1}(m_{i+1}).
}
\tag{4.1}
\]

The conservation identity within one block is

\[
L_i(m)+R_i(m)+S_i(m)=a_i+m,
\tag{4.2}
\]

where `a_i` is its initial mass, while `S_i(m)` is bounded by the number of sites in the block.

Equation (4.1), not a scalar Lindley recursion, is the exact dual object for a symmetric block decomposition. The fast-phase question can therefore be reformulated as: construct a source-valid upper comparison for the **least nonnegative fixed point** of a two-sided random response network, together with an `O(n)` work bound.

This dualization worked: it identifies exactly what the capacity queue had suppressed. It did not by itself move `beta_fast`, because no contraction/tail theorem for the two-sided fixed point has yet been proved in the high-`lambda` source regime.

## 5. B19 — what an implementable algorithm is allowed to call `fresh`

An online routing stage may consume arbitrary random numbers of instructions at different sites. That does **not** automatically destroy independence of what remains. The correct condition is a stopping-line condition.

### Lemma P13-D0093-STOPPING-LINE-FRESH-TAILS-04

Let `V` be finite. At each `x in V`, let

\[
(I_{x,1},I_{x,2},\ldots)
\]

be an independent i.i.d. instruction stack with the ARW instruction law. For a deterministic vector `h=(h_x)`, let

\[
\mathcal F_h=\sigma(I_{x,j}:x\in V,\ 1\le j\le h_x).
\]

Suppose an integer-valued random vector `H=(H_x)_{x\in V}` satisfies the stopping-line property

\[
\{H=h\}\in\mathcal F_h
\quad\text{for every }h.
\tag{5.1}
\]

Then, conditionally on the stopped sigma-field, the shifted tails

\[
(I_{x,H_x+1},I_{x,H_x+2},\ldots)_{x\in V}
\]

are mutually independent, have the original stack law, and are independent of the stopped past.

#### Proof

It is enough to test a finite cylinder function `f` of the shifted tails and an event `A` in the stopped sigma-field. Decompose over the countable values of `H`:

\[
\mathbb E[1_A f(\theta_H I)]
=\sum_h\mathbb E[1_{A\cap\{H=h\}}f(\theta_h I)].
\]

By (5.1), `A cap {H=h}` is measurable with respect to `F_h`. Independence of the coordinates strictly beyond `h_x` from `F_h` gives

\[
\mathbb E[1_{A\cap\{H=h\}}f(\theta_h I)]
=\mathbb P(A\cap\{H=h\})\,\mathbb E[f(I)].
\]

Summing over `h` yields

\[
\mathbb E[1_A f(\theta_H I)]
=\mathbb P(A)\mathbb E[f(I)],
\]

which is the desired conditional independence and identical distribution. `square`

### Consequence for D0093

If a redistribution algorithm only reads an instruction when it actually topples that site, then its consumed-count vector is a stopping line and the unused tails are genuinely fresh. This means **routing first, trapping second** is probabilistically legitimate in principle.

But Rolla's Section 4 / Proposition 6.5 trap construction is deliberately non-Markovian: it explores instructions in advance and on success leaves some examined instructions unused. The source calls sites carrying such examined-but-unused instructions `corrupted`. Consequently, after a trap plan has been inspected, one may not simply invoke the fresh-tail lemma. That distinction is the heart of the present obstruction.

B19 therefore produced a valid algorithmic rule, but not yet a full processor: every retry must either avoid peeking or explicitly dispose of all corruption before claiming regeneration.

## 6. B20 — exact failure of static persistent capacity

The previous run introduced a formal random capacity `C_i`. The following smallest exact example shows why a literal pathwise persistent capacity is false.

### Proposition P13-D0093-STATIC-CAPACITY-OBSTRUCTION-05

Consider a one-site open ARW block. Both jump directions leave the block. Write `S` for a sleep instruction and `J` for a jump instruction. On the same fresh stack prefix

\[
SJJ,
\]

one active particle is stabilized as one sleeper after one instruction, whereas two active particles ignore the first sleep instruction and then both leave the block after the two jumps. Hence, on one and the same instruction field,

\[
\text{retained}(1)=1,
\qquad
\text{retained}(2)=0.
\tag{6.1}
\]

The prefix has strictly positive probability

\[
p(1-p)^2,
\qquad p=\frac{\lambda}{1+\lambda}.
\]

In fact the larger event `first instruction is S and the instruction immediately after the first later jump is another jump` has probability `p(1-p)` and gives the same non-monotonicity.

#### Proof

With one particle, the first `S` instruction is effective because the particle is alone, so it sleeps and the site is stable. With two particles, the same `S` instruction is ineffective: a sleep attempt in the presence of another active particle is instantaneously undone. The first `J` leaves one particle, and the second `J` removes the last one. This proves (6.1). `square`

This is **not** a claim that no useful random service variable can exist. It rules out the naive pathwise statement `a block that can retain B particles can retain those B regardless of extra load routed through the same stack`. Any successful queue comparison must either reserve instructions from the overload routing or regenerate fresh tails after routing.

### Exact finite self-check

The finite core above was executed exactly and archived as a self-check:

- `proofnet24/P13-outside-successor/artifacts/2026-09-18/d0093_one_site_persistent_capacity_counterexample.py`
- `proofnet24/P13-outside-successor/artifacts/2026-09-18/d0093_one_site_persistent_capacity_counterexample.out`

The archived output is

```text
stack=SJJ
q=1 {'sleepers': 1, 'exits': 0, 'used': 1, 'stabilized': True}
q=2 {'sleepers': 0, 'exits': 2, 'used': 3, 'stabilized': True}
PASS: the same fresh stack traps one particle, while adding one particle destroys that trap and both particles exit.
```

This is a self-check, not an outside audit.

## 7. The promising source-native repair: flush an abandoned one-sided trap plan

The obstruction above does **not** make the route hopeless, because Rolla's own one-sided trap construction contains a mechanism designed exactly to control examined-but-unused instructions.

For the Section 4 one-sided procedure, let

\[
a_0<a_1<\cdots<a_m
\]

be successive successful traps. The source proves that all corrupted sites created by exploration `k` lie in the slab

\[
[a_{k-1}+1,a_k].
\tag{7.1}
\]

When particle `k` is actually settled, it follows its explored path to `a_k`, consumes the trap sleep instruction there, and stops. The remaining examined suffix of its exploration leads from `a_k` to the old barrier `a_{k-1}` and lies inside the slab (7.1).

### Lemma P13-D0093-ONE-SIDED-TRAP-UNWIND-06

After finitely many successful one-sided trap explorations have been replayed and the corresponding particles sleep at `a_1,...,a_m`, the trap plan can be abandoned without leaving any examined-but-unused instruction: process traps in reverse order `m,m-1,...,1`, wake/topple a particle at `a_k`, and continue along the already explored suffix until the old barrier `a_{k-1}` is reached. After the reverse sweep, every instruction that was examined by those `m` explorations has been consumed.

#### Proof

For `k=m`, the next unused instruction at `a_m` is the last jump found by the `m`-th explorer after the chosen sleep trap. Continuing along the stored suffix uses exactly the previously examined but unused instructions until `a_{m-1}` is reached. The source localization (7.1) puts this suffix in the newest slab, which is disjoint from all older corruption except at the endpoint barrier. Therefore it does not alter any still-to-be-flushed older suffix.

On reaching `a_{m-1}`, a sleeping particle there may be activated. Now repeat with one active particle at that barrier. Inductively, the `k`-th reverse step consumes every remaining examined instruction in `[a_{k-1}+1,a_k]` and touches no older slab before its endpoint. After `k=1`, every slab has been flushed. The argument only uses acceptable topplings, which are permitted for an odometer upper bound. `square`

This lemma is modest but important: a **successful** non-Markovian plan has a clean deterministic way to turn its peeks into consumed history if we later decide to sacrifice it. Once all peeks are consumed, Lemma 04 applies again to the unused tails.

I am **not** promoting this one-sided lemma to the full two-sided Proposition 6.5 processor. In the two-sided exploration, a path started at the center can visit both sides before hitting one current barrier, so the source's one-sided slab-localization must be rechecked carefully. This is now the exact technical point, rather than a generic appeal to `fresh randomness`.

## 8. Full owner-mandated STUCK report

This is the third consecutive D0093 run with `beta_fast=2`, so the stuck protocol triggers now.

### 8.1 Exact blocking formula

The previous queue route wanted fixed random capacities `C_i` and the recursion

\[
Q_{i+1}=(Q_i+A_i-C_i)^+.
\tag{8.1}
\]

For an actual ARW block with instruction field `I_i`, any capacity determined from a trap exploration is a function of examined instructions. If overload routing consumes `H_i` instructions before trapping, the relevant future block is instead

\[
C_i^{\rm after}=C(\theta^{H_i}I_i),
\tag{8.2}
\]

and if the trap exploration itself has peeked at instructions that remain unused, `H_i` is not a stopping line for the information already revealed. There is no justified replacement

\[
C(\theta^{H_i}I_i)\stackrel{?}{=}C(I_i)
\]

or monotone lower bound that would make (8.1) a pathwise ARW recursion. Proposition 05 gives an exact one-site witness to the underlying non-monotonicity.

The local interface actually needed is therefore:

> **Two-sided clean attempt/flush lemma.** At fixed interval scale `r`, starting with at most `2 zeta_1 r` particles at its source (`zeta<zeta_1<p`), run a source-faithful two-sided trap attempt. On success, confine and stabilize them. On failure, use acceptable topplings to consume every instruction that the failed/partial exploration examined but did not use, and return the particles to a controlled set of boundary/source locations, with a work tail on the natural `O(r^3)` scale and with the remaining stack tails forming a stopping line. The failure probability must remain `<=e^{-cr}` conditional on the past.

Without this interface, adaptive retry/cluster merging is not a proof: it silently reuses biased instruction tails.

### 8.2 Every substantive route tried so far and its precise failure

**Run 1 — B26/B18/B25.** Counterexample-first screening found no pile-size mechanism forcing `log^2 n`; polynomial functions of the Poisson loads have linear aggregate budget with arbitrarily high polynomial probability. Recounting the source proof suggested adaptive repair of only rare failed blocks. **Failure:** Proposition 6.5 starts from one centered pile, whereas merged failed regions carry distributed, history-dependent configurations.

**Run 2 — B3/B12/B30.** Proved a high-probability linear-area theorem for a cyclic negative-drift Lindley queue and identified aggregate unused capacity as the conserved quantity. The source constants give positive *mean formal service surplus* at one fixed large constant scale. **Failure:** the formal capacity was not yet realized by a genuine ARW processor; an overloaded block can consume/wake the very traps the capacity variable counted.

**Run 3 — B11/B19/B20 (this run).** Replaced the fictitious scalar block by the source's exact two-sided response functions, proved the stopping-line fresh-tail lemma for online algorithms, and found the exact one-site non-monotonicity of static service. The one-sided source trap plan can be flushed in reverse, showing how a retry could legitimately recover fresh tails. **Failure:** the corresponding clean flush-and-transfer statement has not yet been proved for the **two-sided** confinement procedure of Proposition 6.5, whose explorer can inspect both sides before choosing which barrier it reaches.

### 8.3 Missing ingredient

The missing ingredient is the two-sided clean attempt/flush lemma stated in 8.1, including a quantitative work tail and a boundary configuration that can be glued to the next block without touching a sealed neighboring trap.

A weaker `the unused tails should be fresh` assertion is not enough. The exact information filtration has to be exhibited.

### 8.4 Simplest unproved case

Take two adjacent source intervals of the source construction at a fixed large constant scale `r`. Put at most

\[
B=\lfloor2\zeta_1 r\rfloor,
\qquad \zeta<\zeta_1<p,
\]

particles at each source. Assume the first interval's two-sided trap exploration succeeds and the second one's first attempt fails.

The simplest unresolved local task is to **sacrifice the first plan, flush both explored histories, and produce by acceptable topplings a clean two-interval state from which a new joint attempt can start using untouched stopping-line tails, without letting any particle leave the two-interval repair region, and with `O(r^3)`-scale work**.

No `n`-dependent geometry is present in this case. If even this two-block interface fails, the fixed-scale queue program should be abandoned rather than patched with another global lemma.

### 8.5 Nearest solved analogue

There are two source-native analogues, and they fit together.

1. **Directed Section 3:** exact reflected queue
   \[
   N_{i+1}=[N_i+\eta_i-Y_i]^+,
   \]
   with negative drift when `zeta<p`. This is the desired mass-flow logic with no backtracking ambiguity.
2. **One-sided Section 4:** the trap construction deliberately places all corrupted instructions behind successive barriers. That is precisely what makes Lemma 06 possible. Proposition 6.5 imports this architecture into a two-sided confinement argument, but the clean retry interface was never needed in the published proof because the proof simply declares failure.

### 8.6 Exactly one recovery choice

**RECOVERY CHOICE: PORT THE ANALOGOUS TECHNIQUE.**

The next recovery episode will port Section 4's corrupted-site shielding/unwind mechanism into the two-sided Proposition 6.5 setting and decide the two-block case above. It will not return to the abstract static-capacity queue until that interface is actually proved.

Next planned method triple: **B6** (deform the one-sided shield to two barriers), **B16** (exactly enumerate/check the smallest finite barrier histories to catch a false unwind rule), and **B25** (count revealed versus consumed instructions two ways to prove or refute a clean stopping line).

## 9. Literature/status limitations

The recent Johnson--Richey odometer theorem is a genuine change in the surrounding literature, but it is for subcritical ARW on `Z` with i.i.d. Bernoulli data; it does not by itself imply the finite-cycle i.i.d.-Poisson high-probability `O(n)` total-toppling bound. The 2026 slow-phase ring paper treats the opposite high-density/slow regime. The 2026 explosivity and self-organized-criticality results likewise do not state this source estimate.

Therefore the status remains **OPEN / PARTIAL** in the repository sense. The dated searches above are bounded negative evidence, not a novelty certificate.

## 10. P14 directed-audit duty

P13's secondary directed audit duty remains P14. No new P14 theorem was found on the current 2026-09-18 surface that requires repeating already completed component audits. I did not manufacture an audit artifact.

## 11. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  target: D0093
  category: CLOSABLE_OUTSIDE
  canonical_claim: operations/claims/D0093.md
  metric: beta_fast
  metric_domain: exact finite-cycle iid-Poisson symmetric-ARW fast-regime source scope
  before: 2
  after: 2
  movement: false
  unchanged_count_before: 2
  unchanged_count_after: 3
  stuck_episode: 1
  stuck_recovery: PORT_ANALOGOUS_TECHNIQUE
  methods_tried: [B11, B19, B20]
  mathematical_status: OPEN_PARTIAL
  new_results:
    - P13-D0093-STOPPING-LINE-FRESH-TAILS-04
    - P13-D0093-STATIC-CAPACITY-OBSTRUCTION-05
    - P13-D0093-ONE-SIDED-TRAP-UNWIND-06
  finite_self_check:
    script: proofnet24/P13-outside-successor/artifacts/2026-09-18/d0093_one_site_persistent_capacity_counterexample.py
    output: proofnet24/P13-outside-successor/artifacts/2026-09-18/d0093_one_site_persistent_capacity_counterexample.out
    verdict: PASS_SELF_CHECK
  exact_remaining_obstruction: two-sided clean attempt/flush plus two-block transfer interface
  next_methods: [B6, B16, B25]
  p26_end_to_end_audit: missing
  distinct_other_end_to_end_audit: missing
  closure_authorized: false
  retired_i0051_reopened: false
  handed_off_p0082_reopened: false
  shared_root_ledgers_modified: false
  peer_files_modified: false
```

## 12. Delivery boundaries

Only P13's own immutable report and the warranted exact self-check artifacts were written. No shared root ledger, historical report, peer file, claim ownership file, schedule, workflow, public post, email/Gmail item, Drive item, credential, or permission was changed.
