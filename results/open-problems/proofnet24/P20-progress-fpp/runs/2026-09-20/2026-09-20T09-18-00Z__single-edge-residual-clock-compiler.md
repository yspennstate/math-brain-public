Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# P20 T10 — single-edge exponential residual-clock compiler for finite-target Bellman curvature

Date: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.  
Canonical parent: `operations/claims/PROB10-10.md`.  
Model: undirected nearest-neighbor FPP on `Z^2` with iid physical-edge weights `Exp(1)`.  
Status: **PARTIAL / OPEN** for full strict convexity. New theorem arguments below are **CANDIDATE_PROVED pending later independent review**.

## 1. Exact source, ownership, and before/after

The source remains Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262v2, Question 4 in §2.5.1, with strict-convexity discussion in §2.8: show that if the passage-time distribution is continuous then the limit shape is strictly convex. The canonical repository specialization is iid `Exp(1)` undirected nearest-neighbor FPP on `Z^2`.

Write `mu` for the deterministic time-constant norm and

`Delta_12 := 2 mu(e1) - mu(e1+e2) >= 0`.

The source-level milestone remains the largest proved `c>=0` with `Delta_12>=c`.

- **before:** `c_*=0`;
- **after:** `c_*=0`.

So this run does **not** prove axis/diagonal strictness and does not close the ADH problem.

The demonstrated mechanism gain is nevertheless substantial:

1. the previous P20 local disagreement theorem required an entire four-edge star to remain fresh;
2. the new theorem needs only **one physical edge whose unrevealed residual clock is Exp(1)**;
3. the exact local energy modulus improves from

   `g(p)=[p+(1-p)log(1-p)]/3`

   to the sharp one-edge modulus

   `f(p)=p+(1-p)log(1-p)`;

4. consequently the small-probability quadratic constant improves from `p^2/6` to `p^2/2` when P04 can represent the charged event with one reserved residual clock;
5. exponential memorylessness makes the theorem compatible with a Dijkstra/Richardson exploration in which the candidate edge has already survived for a predictable age. A pristine untouched star is no longer required.

This directly targets the freshness obstruction in the previous P20/P04 interface.

## 2. Current repository state and failures preserved

Essential state consumed before the proof:

- `operations/PROGRESS20_2026-09-20.md` and its LIVE20 pairing `P04 <-> P20` on T10;
- `operations/claims/PROB10-10.md`;
- P20's preceding report `2026-09-20T08-12-00Z__monotone-profile-superroot-compiler.md`;
- P04's newest report `2026-09-20T08-45-54Z__moving-strip9-cone16377.md`;
- canonical owner report `runs/prob10_2026-09-20/PROB10-10/20260920T0820Z__critical-threshold-cone-163952.md`;
- R08 stuck report `runs/R08/20260916T1623Z_stuck_diagblock_4c19a7.md`.

The R08 failures remain binding:

- shared bypasses invalidate naive multiplication of local surgeries;
- positive-probability finite cylinder events can have exact finite triangle equality, so pointwise finite strictness is false;
- fixed-corner blocks did not reach the diagonal threshold;
- R07/KPZ fluctuation statements are not curvature theorems;
- directed integrable / directed-FPP comparisons do not imply the required direction-to-direction triangle defect.

The present route avoids multiplication of local surgeries. It lower-bounds a subset of the nonnegative terms in the exact finite triangle residual along the actual axis geodesic.

P04's newest independent block result is also consumed but not relabeled as P20 work. Its moving-centered length-9 three-row strip gives

`mu(e1) <= 13247968739227/22500000000000`

`       = 0.5887986106323111...`,

with explicit `O(sqrt N)` endpoint repair and a reflected strict-triangle cone whose convenient closed boundary is `|y|>=1.6377 x`. This is genuine restricted-direction progress, but its constructed strip path is not the actual axis geodesic and therefore cannot be inserted directly into the finite-target residual identity.

## 3. Exact finite-target residual retained from P20

Set

`C_n = n e1`,
`A_n = n(e1+e2)`,

and let `Gamma_n` be the a.s.-unique geodesic from `0` to `C_n`. For an oriented edge `x->y`, define

`r_A(x,y) := tau_xy + T(y,A_n) - T(x,A_n) >= 0`.

The preceding P20 report proved the samplewise identity

`D_n := T(0,C_n)+T(C_n,A_n)-T(0,A_n)`

`     = sum_{e in Gamma_n} r_A(e)`.

Translation and lattice symmetry give

`E D_n = 2 E T(0,n e1)-E T(0,n(e1+e2))`,

so `E D_n/n -> Delta_12`.

Using the standard ADH/Alexander mean-convergence estimate, for a finite model-dependent constant `C_A`,

`E D_n <= n Delta_12 + 2 C_A sqrt(n log n)`,

hence

`n Delta_12 >= E D_n - 2 C_A sqrt(n log n)`.        (3.1)

The new local theorem below is designed to feed directly into this exact `D_n`.

## 4. One-edge Bellman threshold representation

Let `G` be a finite connected graph with positive edge weights, or a finite portion of `Z^2` large enough for the passage values under discussion. Fix an unoriented physical edge `e={x,y}` and orient it `x->y`. Remove `e` and define, for a target `Z`,

`U_Z := T^{\setminus e}(x,Z)`,
`V_Z := T^{\setminus e}(y,Z)`.

Because all weights are positive, a shortest path from `x` which uses `e` can use it only as its first edge. Thus, if `tau_e` is the edge weight,

`T(x,Z)=min(U_Z, tau_e+V_Z)`.                         (4.1)

Similarly,

`T(y,Z)=min(V_Z, tau_e+U_Z)`.                         (4.2)

Now allow the edge to have already survived a predictable age `a>=0`, so that conditionally

`tau_e = a + E`,
`E ~ Exp(1)`.

Define the residual-clock threshold

`t_Z := max(U_Z - V_Z - a, 0)`.                       (4.3)

Then, up to the zero-probability tie event, the Bellman policy toward `Z` uses the oriented edge `x->y` exactly when

`E < t_Z`.                                            (4.4)

This is the scalar threshold structure that an exponential exploration preserves even after the edge has aged.

## 5. Exact one-edge disagreement-energy theorem

Fix two targets `A,C`. Consider any event `H` which may depend arbitrarily on the fresh residual clock `E` and on the rest of the environment. Define the charged event

`D := H cap { the C-policy at x uses e and the A-policy at x does not use e }`.

After conditioning on every edge other than `e` and on the survival age `a`, put

`q := P(D | outside e, a)`.

### P20-FPP-ONE-EDGE-RESIDUAL-CLOCK-30 — CANDIDATE_PROVED

With

`f(q) := q+(1-q) log(1-q)` for `0<=q<1`, and `f(1):=1`,

one has

`boxed{ E[ r_A(x,y) 1_D | outside e, a ] >= f(q) >= q^2/2. }`     (5.1)

The event `H` may be adversarially correlated with small local gaps. No independence between `H` and the residual clock is assumed.

### Proof

Let

`d_A := U_A-V_A-a` and `t_A=max(d_A,0)`.

On the event that the A-policy does not use `e`, (4.1)--(4.2) give

`T(x,A)=U_A`,

and

`r_A(x,y)`
` = a+E + min(V_A, a+E+U_A)-U_A`
` = min(E-d_A, 2(a+E))`.

If `d_A>=0`, then on A-nonuse we have `E>d_A=t_A`, and the first term equals `E-t_A`; it is no larger than the second. Hence

`r_A(x,y)=E-t_A`.

If `d_A<0`, then `t_A=0`; the first term is `E-d_A>E` and the second is at least `2E`, so

`r_A(x,y)>=E=E-t_A`.

Therefore on `D`,

`r_A(x,y) >= E-t_A`.                                  (5.2)

The C-use / A-nonuse part of `D` forces `E` into the threshold interval `(t_A,t_C)`. In particular, for every `u>=0`,

`{D and r_A(x,y)<=u}`

is contained in

`{t_A < E <= t_A+u}`.

Since `E~Exp(1)`,

`P(D, r_A<=u | outside e,a)`
` <= exp(-t_A)(1-exp(-u))`
` <= 1-exp(-u)`.                                      (5.3)

Hence

`P(D, r_A>u | outside e,a) >= [q-(1-exp(-u))]_+`.      (5.4)

Layer cake and `L=-log(1-q)` give

`E[r_A 1_D | outside e,a]`
` >= integral_0^L [q-1+exp(-u)] du`
` = q+(1-q)log(1-q)`
` = f(q)`.                                             (5.5)

For the quadratic bound, `f(0)=0` and

`d/dq [f(q)-q^2/2] = -log(1-q)-q >=0`,

because `-log(1-q)>=q`. Thus `f(q)>=q^2/2`. QED.

### Sharpness of the local modulus

The function `f` is the sharp universal modulus for a single fresh exponential residual clock. Take `t_A=0`, `t_C=L`, let `H` be certain, and arrange the A-residual on disagreement to be exactly `E`. Then

`q=1-exp(-L)`

and

`E[E 1_{E<L}] = 1-(L+1)exp(-L)=f(q)`.

Thus the factor improvement over the old four-star modulus is not merely a loose estimate.

## 6. Stopping-time / Richardson version

The theorem survives an exploration filtration.

Let `H_j` be a stopping-time history of an exponential Richardson/Dijkstra exploration. Suppose the distinct physical edge `e_j` is chosen by a rule measurable from `H_j` while it is active and its exact residual traversal clock has not been observed. Let `a_j` be its current age. By exponential memorylessness, conditional on `H_j`, the remaining clock is a fresh `Exp(1)` variable.

To avoid hiding dependence in the rest of the environment, condition further on every physical edge other than `e_j`. The previous theorem gives a conditional bound `f(q_j)` for the finer conditional charged probability `q_j`. Returning to `H_j` uses convexity:

`f''(p)=1/(1-p)>0`,

so if

`p_j := P(D_j | H_j)`,

then

`E[ r_A(e_j) 1_{D_j} | H_j]`
` >= E[f(q_j)|H_j]`
` >= f(E[q_j|H_j])`
` = f(p_j)`.                                           (6.1)

### P20-FPP-RICHARDSON-RESERVED-EDGE-31 — CANDIDATE_PROVED

An edge need not be an untouched iid `Exp(1)` edge from time zero. It is enough that at the instant it is reserved, the exploration has learned from that edge only a predictable survival age; its remaining clock can then be used with the same sharp modulus `f`.

This is the exact place where the Exp(1) law is used. It is a materially stronger fit to P04's infection-state recurrences than the previous whole-star freshness assumption.

## 7. New finite-to-infinite compiler

Return to `A_n,C_n,Gamma_n`. Let an exploration select distinct oriented physical edges `e_1,...,e_{K_n}`, with each edge satisfying the reserved residual-clock condition when selected. Let

`D_j := { e_j lies on Gamma_n oriented toward C_n, and e_j is not A_n-calibrated at its tail }`,

and

`p_j := P(D_j | H_j)`.

On `D_j`, the charged quantity `r_{A_n}(e_j)` is one of the nonnegative summands of `D_n`. Distinctness of the physical candidate edges therefore gives samplewise

`D_n >= sum_j r_{A_n}(e_j) 1_{D_j}`.                    (7.1)

Taking expectations and using (6.1):

`boxed{ E D_n >= E sum_j f(p_j) >= (1/2) E sum_j p_j^2. }`    (7.2)

Combining with (3.1) gives the new source-facing compiler

### P20-FPP-SINGLE-EDGE-SUPERROOT-COMPILER-32 — CANDIDATE_PROVED

`boxed{
 n Delta_12
 >= E sum_j f(p_j)
    - 2 C_A sqrt(n log n).
}`                                                        (7.3)

If a block proxy incurs a nonnegative expected loss `L_n`, the same argument gives

`boxed{
 n Delta_12
 >= E sum_j f(p_j)
    - E L_n
    - 2 C_A sqrt(n log n).
}`                                                        (7.4)

This is the direct P04 handoff.

### 7.1 Robust reserved edges

If `G_n` selected residual-clock edges satisfy `p_j>=p_0>0`, then

`n Delta_12 >= f(p_0) E G_n - E L_n - 2C_A sqrt(n log n)`.   (7.5)

Thus, with lower-order loss,

`E G_n = omega(sqrt(n log n))`

still suffices. Compared with the previous whole-star compiler, the coefficient is exactly three times larger for the same conditional event probability because `f=3g`.

### 7.2 Total charged-probability mass

Assume `K_n<=C n` almost surely and put

`M_n := E sum_j p_j`.

By Cauchy--Schwarz and Jensen,

`E sum_j p_j^2 >= M_n^2/(C n)`.

Therefore

`boxed{
 n Delta_12
 >= M_n^2/(2 C n)
    - E L_n
    - 2 C_A sqrt(n log n).
}`                                                        (7.6)

The previous whole-star theorem had denominator `6 C n`; the one-edge theorem improves it to `2 C n` whenever the same charged probability mass can be represented by reserved residual-clock edges.

The exponent threshold remains

`M_n >> n^(3/4)(log n)^(1/4)`

with negligible loss, but the quantitative energy constant improves by a factor of three and, more importantly, the exploration no longer has to preserve four untouched incident edges at every candidate.

## 8. Two-sided symmetric variant

There is a useful optional strengthening for future geometry. Let

`A_n^+ = n(e1+e2)`,
`A_n^- = n(e1-e2)`.

For a single reserved edge, conditional on the outside environment, each target's use/nonuse decision is a threshold in the same residual exponential variable. If the `C_n` policy uses the edge but at least one of the two symmetric target policies does not, let `t_min` be the smaller of their two thresholds. Then on that union event

`r_{A_n^+}(e)+r_{A_n^-}(e) >= E-t_min`.

Exactly the same layer-cake argument yields the modulus `f(p)` for the **union disagreement event**. This does not close the geometry, but it lets a future P04 separator use whichever of the NE or SE targets first breaks calibration without paying an additional local union-bound constant.

No source-level claim is made from this variant because a lower bound on the corresponding union probability along the actual axis geodesic is still missing.

## 9. Why this is a real P04 coordination gain

P04's finite strip computations are already formulated as exponential infection recurrences over reachable infected sets. Its newest strip-9 proof also enforces disjoint physical-edge ownership across blocks. The previous P20 interface asked P04 to preserve a whole fresh four-edge star at a path-relevant candidate. That requirement is unnecessarily rigid.

The new sufficient architecture is:

1. expose a Dijkstra/Richardson frontier inside a block;
2. before a chosen active physical edge fires, reserve it using a rule that depends only on the explored history and its survival age, not on its hidden residual clock;
3. continue the exploration and let the eventual visit/noncalibration event depend arbitrarily on that residual clock;
4. charge the event through `f(p_j)` by (6.1);
5. arrange distinct physical-edge ownership across blocks and control the proxy/interface loss as `L_n`.

If a two-target P04 extension can retain the same `O(sqrt n)` scale for its endpoint/interface correction, that scale is lower order than the existing `sqrt(n log n)` Alexander budget. **This sentence is conditional:** the current P04 `O(sqrt N)` correction belongs to its constructed moving-strip path and has not yet been proved to equal the loss `L_n` for the actual-geodesic two-target proxy.

Thus the concrete next P04 question is no longer “can an entire untouched star be hidden?” but the weaker question:

> Can each of `O(n)` disjoint physical slabs reserve one active edge whose conditional probability of becoming an axis-geodesic, diagonal-noncalibrated edge has enough aggregate mass to beat the super-root threshold?

## 10. Residual obstruction and honest failure statement

The run removes the **freshness** obstruction but not the **path-unavoidability / ancestry-mass** obstruction.

Even in a Richardson exploration, a reserved active boundary edge may have tiny conditional probability of lying on the eventual parent chain from `0` to `C_n`. The theorem proves a sharp energetic price *given* the conditional charged probability `p_j`; it does not prove that the aggregate

`M_n=E sum_j p_j`

is super-root.

The old shared-bypass failure therefore survives in a more precise form: the actual axis geodesic might route its ancestry through a small subset of frontier edges on which the NE target remains calibrated, while many spatially available disagreement edges never enter `Gamma_n`. Spatial disagreement density alone is still insufficient.

No current unconditional coalescence theorem found in the bounded literature check removes this. Dembin--Elboim--Peled's quantitative geodesic-coalescence/BKS theorem assumes more than 32 extreme points of the limit shape; under the flat-face contradiction that hypothesis cannot be imported. Jacquet's unrestricted-versus-directed strict inequality is again a different comparison.

## 11. Next attack

The next nonredundant attack is an **ancestral-mass frontier lemma** for the actual reverse Richardson tree of `C_n`.

Work in P04-style disjoint physical slabs. At a stopping frontier, reserve a bounded set of active edges before their residual clocks fire. For each reserved edge `e`, track

`a_e = P(e becomes the parent-chain crossing used by Gamma_n | frontier history)`

and the conditional probability that the `A_n` threshold lies below the `C_n` threshold. The target lemma is a dichotomy:

1. either a positive fraction of slabs carry enough joint ancestry/noncalibration mass that the sum of the resulting `p_j` exceeds `n^(3/4)(log n)^(1/4)` by a diverging factor, and (7.6) proves `Delta_12>0`;
2. or the two target continuation profiles are nearly translate-equivalent on most path-relevant frontier mass, in which case propagate that near-translation across slabs and compare with their incompatible terminal boundary data.

This is materially different from trying another untouched-star construction or improving the local constant. The local constant and memoryless conditioning are now explicit; the only unpaid quantity is the path-relevant ancestry mass.

## 12. Supplementary executed sanity artifact

The theorem is proved analytically above. A small executed checker was nevertheless archived to falsify algebraic mistakes and compare the old/new local moduli:

`proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T09-18-00Z__single_edge_residual_clock_sanity.py`

creation commit `54b6874977e6e0d9712985bd70ddbbedc9a4afdf`.

Archived output:

`proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T09-18-00Z__single_edge_residual_clock_sanity.out`

creation commit `4f6f65ca3afa7b88ceda8f3b98d67f762c76dc21`.

It checks the calculus identity behind `f(p)>=p^2/2`, several shifted residual-clock intervals, and the exact factor-three comparison `f=3g`. The output ends

`P20-T10-SINGLE-EDGE-RESIDUAL-CLOCK-SANITY: ALL_CHECKS_PASS`.

This artifact is supplementary only. It is not numerical curvature and is not used in place of the proof.

## 13. Fresh bounded literature boundary

Checked 2026-09-20:

- ADH arXiv:1511.03262 remains the exact source. The survey states Question 4 in §2.5.1 and treats strict convexity as conjectural in §2.8.
- Dembin--Elboim--Peled, *Coalescence of Geodesics and the BKS Midpoint Problem in Planar First-Passage Percolation* (GAFA 2024; arXiv:2204.02332), prove their quantitative coalescence/BKS theorem under the extra assumption that the limit shape has more than 32 extreme points.
- Jacquet, arXiv:2412.20779, proves strict inequality between unrestricted and directed FPP time constants; it does not imply `Delta_12>0`.
- Recent fluctuation/nonrandom-fluctuation papers found by bounded search do not supply the path-conditioned two-target ancestry estimate required by Section 11.

No bounded search result was treated as an exhaustive novelty certificate. Publication novelty remains **UNVERIFIED**.

## 14. Cyclic-interval handoff preserved

P20's displaced Fokam--Bitjoka cyclic-interval package is preserved unchanged and was not used as a waiting task in this run.

Canonical source claim: `operations/claims/FOKAM-BITJOKA-2026-CYCLIC-INTERVAL.md` at `d1b8c8755617cbaef9b06c2eab2694bea0382258`.

The source-literal proof candidate `P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01` remains intact. The exact finite sanity artifact remains supplementary. P26 audit `P26-AUDIT-P20-CI241-SEMICIRCLE-MAJORITY-41` remains `PASS_FULL_MATHEMATICAL_PROOF / SOURCE_LITERAL_CONJECTURE_2_41 / SOURCE_QUANTIFIERS_PASS`, with the last recovered independent-audit gate `1/2` and the second distinct audit still missing. No completed certification, posting, or novelty claim is implied.

No run time was spent waiting for that audit.

## 15. Original-problem metric versus mechanism metric

**Original problem:**

`c_* : 0 -> 0` for `Delta_12>=c`.

**Mechanism movement:**

- required local freshness: whole four-edge star -> one active residual exponential clock;
- local disagreement modulus: `g(p)=f(p)/3 -> f(p)`;
- small-`p` energy: `p^2/6 -> p^2/2`;
- `O(n)`-candidate mass compiler denominator: `6 C n -> 2 C n`;
- compatibility: pristine-star exposure -> stopping-time Richardson/Dijkstra reservation after arbitrary predictable aging.

These are demonstrated reductions toward the source target, but they are not themselves strict convexity.

## 16. ledger_delta

`P20 T10 | source ADH_Q4::Exp1_Z2_undirected | full metric c_*: 0 -> 0 | status PARTIAL/OPEN | new candidate theorem P20-FPP-ONE-EDGE-RESIDUAL-CLOCK-30: one residual Exp clock gives sharp f(p)=p+(1-p)log(1-p) disagreement energy >=p^2/2 | new candidate theorem P20-FPP-RICHARDSON-RESERVED-EDGE-31: stopping-time active-edge memorylessness preserves same modulus | new candidate theorem P20-FPP-SINGLE-EDGE-SUPERROOT-COMPILER-32: n Delta_12 >= E sum f(p_j)-E L_n-2 C_A sqrt(n log n), and if K_n<=Cn then >=M_n^2/(2Cn)-E L_n-2 C_A sqrt(n log n) | P04 latest consumed: strip9 axis cap 0.5887986106323111 and reflected closed cone 1.6377 | residual obstruction: prove super-root path-relevant ancestry/noncalibration mass, not local strictness | next attack: bounded-frontier Richardson ancestral-mass/near-translation dichotomy | cyclic-interval handoff preserved, audit gate last known 1/2, no certification claim | novelty UNVERIFIED`.

No shared `RESULTS.md`, `QUEUE.md`, or `POSTED.md` file was edited. No peer/historical file was overwritten. No email, Drive, public posting, paid compute, workflow execution, access change, or schedule change was performed.

END OF P20 FPP RUN REPORT
