Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** Primary metric **no movement**: `L_6 >= 0 -> L_6 >= 0`; substantive auxiliary movement: exact replica-symmetric curvature `kappa_6` **UNMEASURED -> 1/11**; methods tried: **B2 / B11 / B24**.

# HARD7-06 run 1 — k=3 random-regular hypergraph 2-colorability: an exact ordinary-second-moment obstruction at d=6

Status: **PARTIAL / source conjecture remains OPEN under bounded current-status review.**

Canonical claim created create-only and read back: `operations/claims/CKS-2024-RREG-HYPER2COL-K3.md` at commit `011c41eb3c6e4145df7f8a176607166ee8a5668d`.

Exact finite-core checker: `artifacts/hard7_2026-09-18/HARD7-06/k3_overlap_curvature_exact.py`, commit `0b1be01e7c45716c39bd3763e23b61f28b622204`.

Executed exact output: `artifacts/hard7_2026-09-18/HARD7-06/k3_overlap_curvature_exact.out`, commit `d68dead0bc6f7a6c849a4e094bad27fa524e278d`, ending `ALL_EXACT_CHECKS_PASS`.

## 1. Required continuity, source and ownership checks

I read the HARD7 control file, the 16 September new-methods policy and owner directive, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md` and `RESULTS.md`, and the newest neighboring HARD7-04 and HARD7-05 reports. The neighboring runs concern heavy-tailed configuration-model GHP convergence and integrated-fBM persistence and do not overlap this CSP target.

### Random 3-SAT candidate rejected for ownership

The prompt's first candidate, the small-fixed-`k` random `k`-SAT threshold problem, is **not available**. The canonical claim `operations/claims/F0097.md` names **R03** as owner and freezes the Alan Frieze ICM 2014 problem of proving a uniform satisfiability threshold for every fixed `k>=3`, beginning with `k=3`. Recent R03 reports explicitly work on near-critical random 3-SAT. I therefore did not create an alias or duplicate assignment.

### Admitted source target

I instead admitted a distinct random-CSP threshold question from:

Evan Chang, Neel Kolhe, Youngtak Sohn, *Upper Bounds on the 2-Colorability Threshold of Random d-Regular k-Uniform Hypergraphs for k >= 3*, APPROX/RANDOM 2024, LIPIcs 317, Article 47, DOI `10.4230/LIPIcs.APPROX/RANDOM.2024.47`; full version arXiv:2308.02075.

Primary source:
https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2024.47

The source samples uniformly from `k`-uniform hypergraphs in which every vertex has degree exactly `d`. Theorem 1.1 defines an explicit `d_*(k)` and proves non-2-colorability with high probability for `d>d_*(k)`. The abstract/introduction state that this upper bound is conjectured sharp for hypergraph 2-coloring for every `k>=3`, while the corresponding matching lower bound is only known in a sufficiently-large-`k` random-regular NAE-SAT regime. For `k=3`, Proposition 1.6 and equation (1.4) locate the relevant root in `[6.74,7.5]`, and Table 1 records `ceil(d_*(3))=7`.

Thus the exact near-boundary source-valid milestone frozen here is:

> **K3D6:** For the source's uniformly random 6-regular 3-uniform hypergraph `H_{n,6,3}`, does
> `P(H_{n,6,3} is 2-colorable) -> 1` along admissible `n`?

Since `6<6.74<=d_*(3)`, K3D6 lies strictly on the conjecturally colorable side. Settling K3D6 alone is still **PARTIAL** for the full `k=3` sharpness conjecture unless the remaining lower-degree scope is covered by a rigorous reduction or existing theorem.

### Current-status screen, dated 2026-09-18

A bounded web search for the exact title/authors/arXiv ID, `random d-regular 3-uniform hypergraph 2-colorability threshold`, and `random regular 3-NAE-SAT k=3 threshold` recovered:

1. the 2024 Chang--Kolhe--Sohn paper itself, still stating small `k>=3` sharp threshold location as open and the `d_*(k)` bound as conjecturally sharp;
2. Ding--Sly--Sun, *Satisfiability Threshold for Random Regular NAE-SAT* (CMP 2016), which proves the matching threshold only for sufficiently large `k`;
3. Deshpande--Montanari--O'Donnell--Schramm--Sen, *The threshold for SDP-refutation of random regular NAE-3SAT* (2018), which is an algorithmic-refutation threshold and does **not** settle satisfiability or hypergraph 2-colorability at `d=6`;
4. adjacent 2024--2026 work on chromatic/discrepancy properties of random/regular hypergraphs, but no later theorem found in this bounded search that supplies the exact small-`k=3` matching lower bound for the source model.

Repository searches for the source title, arXiv ID `2308.02075`, authors, and model phrases returned no existing claim or active equivalent target. This is bounded negative evidence, not a proof of worldwide openness or novelty.

## 2. Frozen source metric

Let

`L_6 := sup{L in [0,1] : liminf_n P(H_{n,6,3} is 2-colorable) >= L is rigorously proved}`,

with the source's simple uniform 6-regular 3-uniform model and admissible divisibility class fixed.

Verified admission baseline: the trivial `L_6>=0`.

This run does **not** improve that probability lower bound, so the primary metric is honestly

`L_6 >= 0  ->  L_6 >= 0`.

The mathematical gain is instead an exact obstruction showing why the most obvious unweighted second-moment route fails precisely at the boundary degree `d=6`.

## 3. B2 — attack the naive lower-bound mechanism first

A standard first try for K3D6 would be to count balanced 2-colorings and apply a second moment. The source itself emphasizes that ordinary solution counts fail to concentrate in the one-step-RSB regime. Rather than assume this obstruction is already active at the first unresolved small case, I tested it exactly.

I work in the standard `d`-regular 3-uniform **configuration model** for this diagnostic. This run does **not** silently identify the configuration model with the source's simple model for a theorem-sized probability conclusion; transferring exponential second-moment asymptotics under conditioning on simplicity is left as a separate obligation. The local instability below is nevertheless exact in the configuration-model entropy problem and identifies a route that cannot establish the desired lower bound in its replica-symmetric form.

Let `sigma,tau in {0,1}^n` be two balanced colorings. On the symmetric overlap slice put

`q_00=q_11=(1+theta)/4`,
`q_01=q_10=(1-theta)/4`,

for `-1<theta<1`. Write

`a=(1+theta)/4`, `b=(1-theta)/4`,

and let

`H_q(theta)=-2a log a-2b log b`.

Then

`H_q''(0)=-1`.                                                   (1)

For the edge entropy, regard the four joint color labels as

`00, 01, 10, 11`.

An ordered triple is admissible for both colorings iff its first coordinates are not all equal and its second coordinates are not all equal. Let `N` count how many of its three joint labels lie in `{00,11}`.

The exact checker enumerates all `4^3=64` ordered triples and finds

`# {valid triples with N=0,1,2,3} = (6,12,12,6)`.              (2)

There are 36 valid ordered triples in total.

## 4. B11 — entropy/Legendre dualization gives an exact curvature

For a fixed symmetric overlap, maximum entropy over admissible edge patterns with the required joint-label marginals is unique by strict entropy concavity. Symmetry reduces it to a one-parameter exponential family. If `t=e^u`, the partition polynomial is exactly

`P(t)=6+12t+12t^2+6t^3 = 6(1+t)(1+t+t^2)`.                   (3)

Let

`s=(1+theta)/2`.

The required mean number of same-bit joint labels per triple is `3s`, so the saddle is determined by

`t P'(t)/P(t) = 3s`.                                           (4)

At `theta=0`, `s=1/2` and symmetry gives `t=1`, `u=0`. Under the corresponding uniform law on the 36 valid triples, the exact finite enumeration (2) yields

`E[N]=3/2`,
`E[N^2]=19/6`,
`Var(N)=11/12`.                                                (5)

Differentiate (4) in `u=log t`. Since `d E_u[N]/du = Var_u(N)`, at zero

`u'(0) = (3/2)/(11/12) = 18/11`.                              (6)

The maximum edge-pattern entropy is the Legendre transform

`H_p(theta)=log P(e^u)-3s u`.

Envelope differentiation gives

`H_p'(theta)=-(3/2)u`,

hence by (6)

`H_p''(0)=-(3/2)(18/11)=-27/11`.                              (7)

This is an exact rational identity, not floating numerics.

### The overlap rate

In the `d`-regular configuration model, the theta-dependent exponential method-of-types contribution to the second moment of balanced colorings is, up to theta-independent normalization,

`S_d(theta) = (1-d) H_q(theta) + (d/3) H_p(theta)`.            (8)

Reason: there are `exp(n H_q+o(n))` coloring pairs of joint type `q`; the `d` copies of each vertex label contribute the usual `-d H_q` stub-type entropy term; admissible triple types contribute `(d/3)H_p`; all partition normalizations independent of theta cancel when comparing overlaps. Equation (8) is only used here through overlap differences and derivatives, so no theta-independent constant is being smuggled into the conclusion.

Combining (1) and (7),

`S_d''(0) = (1-d)(-1) + (d/3)(-27/11)`
`           = (2d-11)/11`.                                   (9)

Therefore

`S_5''(0)=-1/11`,
`S_(11/2)''(0)=0`,
`S_6''(0)=+1/11`,
`S_7''(0)=+3/11`.                                             (10)

All four values are asserted and checked exactly in the archived `Fraction`-arithmetic checker.

## 5. B24 — identify the extremal-overlap obstruction

At `d=6`, equation (10) proves

`boxed(S_6''(0)=1/11>0)`.

Thus independent overlap `theta=0` is a **strict local minimum**, not a local maximum, of the symmetric-overlap contribution. Consequently there are arbitrarily small nonzero overlaps `theta` with

`S_6(theta)>S_6(0)`.                                          (11)

This is enough to kill the naive replica-symmetric second-moment plan: an unweighted balanced-coloring count cannot be controlled by declaring independent pairs to be the dominant overlap saddle. Correlated pairs are already exponentially favored at the variational level.

The exact formula (9) says more: the local stability boundary of this naive symmetric-overlap saddle is

`d_RS = 11/2`.                                                 (12)

Hence **`d=6` is the first integer degree at which the independent-overlap saddle becomes locally unstable**. This is structurally well aligned with the source problem: the first near-threshold small-`k` degree is also exactly where the elementary unweighted second moment changes local type.

I make no novelty claim for (9)--(12). Replica-symmetry instability phenomena are standard in the random-CSP literature, and this particular rational curvature may be implicit in prior moment calculations. What is new for this track is the exact source-matched obstruction and its verified finite core. A dedicated prior-art search is still required before treating the calculation itself as publishable.

## 6. What was and was not proved

**Proved in this run:**

- the finite pattern counts `(6,12,12,6)` for the symmetric two-color overlap in 3-uniform NAE constraints;
- the exact entropy curvature `H_p''(0)=-27/11`;
- the exact configuration-model symmetric-overlap curvature
  `S_d''(0)=(2d-11)/11`;
- in particular `S_6''(0)=1/11>0`, so the replica-symmetric independent-overlap saddle is locally unstable at `d=6` for the ordinary unweighted balanced-coloring second-moment variational problem.

**Not proved:**

- `L_6>0`, let alone `L_6=1`;
- 2-colorability of the source's simple random 6-regular 3-uniform hypergraph;
- a conditioning-on-simplicity transfer theorem for the full second-moment asymptotics;
- sharpness of `d_*(3)`;
- novelty of the exact curvature identity.

This is therefore **PARTIAL** and is not a refutation of the source conjecture. It refutes only the naive route in which ordinary balanced colorings are expected to have an independent-overlap-dominated second moment.

## 7. The route this points to

The obstruction is informative because it specifies what a successful lower-bound object must change. The source's large-`k` relatives succeed by counting or weighting **clusters**, not raw solutions. At `d=6`, any useful reweighting should remove the positive `+1/11` overlap curvature and restore a locally concave independent/cluster-overlap saddle.

A concrete next target is therefore to define a one-parameter cluster/frozen-variable reweighting `Z_lambda` for `k=3,d=6`, derive its two-replica overlap Hessian at the source's BP fixed point, and ask whether some source-natural `lambda` makes the corresponding curvature nonpositive while retaining a positive first-moment exponent. This is a quantitative gateway to a true second-moment lower bound rather than another checker-only exercise.

The next run should not reuse B2/B11/B24. Proposed next methods: **B1** (change category to the factor-tree/cluster message model), **B6** (deform from a solvable reweighting or lower degree while following the Hessian), and **B20** (identify exactly why the cluster-weight algorithm fails if the Hessian remains positive).

## 8. Scheduler/model capability note

The requested GPT-6/maximum setting is still not exposed as a scheduler model or reasoning selector in this environment. This run actually identifies as **GPT-5.6 Sol**; reasoning-effort telemetry is not exposed, so it is **UNVERIFIED**. No claim is made that an hour of uninterrupted execution occurred.

The older historical statement that some scheduler IDs once rejected modification is repository history, not a fresh modification test in this research run. No scheduler was modified.

## 9. Structured ledger delta

```yaml
ledger_delta:
  track: HARD7-06
  source: "Chang-Kolhe-Sohn, APPROX/RANDOM 2024, sharpness of d_*(k) for random regular hypergraph 2-coloring"
  canonical_claim: operations/claims/CKS-2024-RREG-HYPER2COL-K3.md
  source_scope: "k=3 sharpness, boundary milestone d=6"
  status_before: ADMISSION_PENDING
  status_after: PARTIAL
  primary_metric: "L_6 = largest proved liminf colorability-probability lower bound in source simple model"
  metric_before: ">=0"
  metric_after: ">=0"
  movement: no_movement_primary_metric
  auxiliary_metric: "kappa_6 = S_6''(0) for symmetric ordinary balanced-coloring configuration-model overlap rate"
  auxiliary_before: UNMEASURED
  auxiliary_after: "1/11"
  methods_tried: [2, 11, 24]
  exact_artifact: artifacts/hard7_2026-09-18/HARD7-06/k3_overlap_curvature_exact.py
  exact_output: artifacts/hard7_2026-09-18/HARD7-06/k3_overlap_curvature_exact.out
  exact_output_status: ALL_EXACT_CHECKS_PASS
  theorem_claims_new: 1
  source_closed: false
  independent_audits: 0
  unchanged_primary_runs: 1
  remaining_obligation: "Prove a nontrivial source-simple-model lower bound at k=3,d=6, ultimately L_6=1; ordinary unweighted RS second moment is locally unstable."
  next_methods: [1, 6, 20]
```
