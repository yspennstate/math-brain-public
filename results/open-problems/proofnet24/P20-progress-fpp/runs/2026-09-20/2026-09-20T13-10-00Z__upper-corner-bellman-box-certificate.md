Model actually run: **GPT-5.6 Sol. Reasoning effort: UNVERIFIED — no authenticated applied effort selector or GPT-6 receipt is exposed, so no stronger runtime claim is made.**

# P20 T10 — upper-corner Bellman boxes and mixed projective correctors for diagonal FPP

Date: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Controlling owner directive: `operations/PROGRESS20_2026-09-20.md`.  
Canonical parent: `operations/claims/PROB10-10.md`.  
Model: undirected nearest-neighbor first-passage percolation on `Z^2` with iid physical-edge weights `Exp(1)`.  
Status: **PARTIAL / OPEN** for the source problem. New theorem arguments in this report are **CANDIDATE_PROVED pending later independent review**. No certification, priority, or novelty claim is made.

## 1. Exact source, current target, and before/after

The exact source remains Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 4 in the limit-shape discussion: prove strict convexity for continuous passage-time distributions. The source discussion itself treats strict convexity/uniform curvature as conjectural. The repository freezes the iid `Exp(1)` undirected nearest-neighbor `Z^2` specialization.

Let `mu` be the time-constant norm and define the first same-quadrant checkpoint

`Delta_12 := 2 mu(e1)-mu(1,1) >= 0`.

The tracked source-facing quantity is the largest proved `c>=0` with `Delta_12>=c`.

- **before:** `c_*=0`;
- **after:** `c_*=0`.

Thus this run does **not** prove the axis/diagonal strict triangle inequality and does not close full strict convexity.

The bounded fresh literature recheck performed in this run found no source-matching theorem closing ordinary iid `Exp(1)` nearest-neighbor undirected `Z^2` strict convexity. Recent FPP papers returned by the search included different ambient models or different geometric questions. This is a bounded current check, not an exhaustive novelty certificate.

The demonstrated mechanism gain is separate and concrete: the continuous asynchronous min-plus Bellman certificate from the preceding P20 run can be verified over **whole profile boxes from one scalar upper-corner expectation**, with no Lipschitz interpolation loss, and its outer compactification radius can be reduced drastically by using a deterministic zero-labelled anchor instead of an `E max` over all input anchors. A second central-coordinate corrector gives an explicit exact `Gamma` reset constant and an additional box penalty. These changes turn the remaining P04 handoff into a branch-and-bound interval-enclosure problem for one scalar functional per unresolved box.

## 2. Essential state consumed and collision discipline

I consumed only the current dependencies needed for this attack:

1. `operations/PROGRESS20_2026-09-20.md` and LIVE20, which pair P20 with P04 on T10;
2. `operations/claims/PROB10-10.md` and its retained R08 failures;
3. P20's immediately preceding report
   `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T13-05-00Z__projective-minplus-corrector-compactification.md`, creation commit `0d0d6404fc95fc2f7f01ca6ebd78f50e31b6090c`;
4. the canonical same-source asynchronous-carry architecture created at commit
   `96f76b3399ffefe3178f3be0531a22e8e09dcfab`, including its explicit finite-to-infinite Bellman compiler;
5. the canonical asynchronous screen output at commit
   `c6d5dc13d7ff79b8ca555e11c308f646eaad8c06`, which is explicitly marked `NONRIGOROUS_SCREEN = True`;
6. P04's rigorous physical-edge slab / finite exponential-infection machinery, including the current T10 width-7 report at commit
   `ab1c4bd3b662dfe712acae1193e41d2f102dddb1`;
7. the displaced P20 cyclic-interval handoff and existing P26 audit state.

The canonical owner already owns the conservative upward-projection finite-state carry theorem. I do not re-claim it. P20's contribution here is a different **unrounded continuous-state verification theorem** and its exact boxwise reduction. P04 remains the natural owner of rigorous finite-block expectation evaluation and block-to-infinite-volume construction.

The retained rigorous axis lower certificate is

`mu(e1) >= b := 3002823/10000000 = 0.3002823`,

so a direct diagonal upper certificate

`mu(1,1) < 2b = 3002823/5000000 = 0.6005646`            (2.1)

would imply `Delta_12>0`. For a band longitudinal parameter `L`, the Bellman average-cost target is therefore

`lambda/L < 0.6005646`.                                  (2.2)

For the screened choice `L=4`, the threshold is

`lambda_* = 4*0.6005646 = 3002823/1250000 = 2.4022584`.  (2.3)

The screen values below threshold are evidence only; this report does not convert any sampled mean into a theorem.

## 3. Binding failures preserved

The old failures remain binding and are not overwritten by this run.

1. Shared bypasses defeat naive multiplication of local surgery gains.
2. Positive-probability finite cylinder events can have exact finite triangle equality, so pointwise strict saving is false.
3. R08 fixed-corner exact blocks did not reach the needed diagonal threshold.
4. Directed integrable models and unrestricted-versus-directed strict comparisons do not prove the required undirected same-quadrant triangle defect.
5. The all-path weighted-SAW / Chernoff first-moment architecture has a diagonal barrier already exposed by the monotone E/N path family.
6. P20's Jacquet-pattern route proves linearly many true-geodesic backtracks, but under flatness their diagonal-target residual can collapse on a positive-density family; that is a co-calibration rigidity statement rather than a contradiction.
7. The preceding continuous-profile Bellman theorem compactified the state and gave a global Lipschitz net, but a brute-force tensor net in widths around 30--50 remained prohibitive and paid a deterministic interpolation margin `(1+3 kappa) delta`.

The present attack directly addresses item 7. It does not claim to solve items 1--6 by local surgery.

## 4. Recalled exact min-plus block setup

Fix one finite connected block with input and output boundaries indexed by the same finite set `D`. For a realized block environment `omega`, let

`d_omega(i,j)`

be its internal passage metric from input `i` to output `j`. For a finite input arrival vector `y`, define

`F_omega(y)_j := min_i { y_i+d_omega(i,j) }`,             (4.1)

`g_omega(y) := min_j F_omega(y)_j`,                       (4.2)

`Phi_omega(y) := F_omega(y)-g_omega(y) 1`.                (4.3)

Profiles are normalized by `min_i y_i=0`. Write

`t_first(y,omega) := min_j F_omega(y)_j = g_omega(y)`,

`t_last(y,omega) := max_j F_omega(y)_j`.                   (4.4)

The map `F_omega` is coordinatewise nondecreasing and additively homogeneous. The preceding P20 run proved projective nonexpansiveness and the exact output-span reset

`span(Phi_omega(y)) <= D_omega`,                           (4.5)

where `D_omega` is a suitable within-output-boundary diameter.

The canonical rotated diagonal-band decomposition uses disjoint physical edge sets from band to band, so after conditioning on the carried profile, the next `omega` is fresh. This is what makes a pointwise one-block Bellman inequality telescope without an independence fiction.

## 5. First new theorem: deterministic-zero-anchor drift

For the canonical rotated band of longitudinal thickness `2L`, every input offset has a fixed `2L`-edge zig-zag to the corresponding output offset, entirely inside that band. Its `2L` physical edge weights are iid `Exp(1)`.

### P20-FPP-ANCHOR-DRIFT-COMPACTIFICATION-39 — CANDIDATE_PROVED

For every fixed finite normalized input profile `y`,

`E g_omega(y) <= 2L`.                                     (5.1)

Moreover, using the fixed output-boundary chain of `W` adjacent offset links, each realized through two lattice edges,

`E span(Phi_omega(y)) <= 2W`.                              (5.2)

Consequently, for `kappa>0` and the span corrector

`h_kappa(y)=kappa span(y)`,

the Bellman residual

`B_kappa(y)`
` := E[g_omega(y)+kappa span(Phi_omega(y))]`
`    -kappa span(y)`                                      (5.3)

satisfies

`B_kappa(y) <= 2L+2 kappa W-kappa span(y)`.                (5.4)

Hence, for a proposed average block cost `lambda`, every normalized state with

`span(y) >= R_kappa(lambda)`
` := (2L+2 kappa W-lambda)/kappa`                         (5.5)

automatically satisfies `B_kappa(y)<=lambda`.

#### Proof

Fix the state `y`. Choose, deterministically from `y`, one input index `a` for which `y_a=0` (for example the least such index). This choice is made before the fresh block environment is sampled. Let `P_a` be the fixed `2L`-edge zig-zag from input `a` to the same output offset. By definition of the min-plus block passage,

`g_omega(y) <= weight(P_a)`.                              (5.6)

The path contains `2L` distinct physical edges, each of mean one, so taking expectation gives (5.1). The crucial point is that no maximum over all possible zero anchors is taken: the Bellman inequality is pointwise in a fixed state `y`.

For (5.2), any two output offsets can be connected along the fixed output-boundary chain. Across all `W` adjacent offset links the chain uses `2W` distinct physical edges. Therefore samplewise

`span(Phi_omega(y)) <= S_W`,                              (5.7)

where `S_W` is the total chain cost. Since `E S_W=2W`, (5.2) follows. Substitute (5.1)--(5.2) into (5.3) to get (5.4), and rearrange for (5.5). QED.

### Demonstrated gain over the preceding compactification

The preceding report used the crude uniform variable

`H_omega=max_i min_j d_omega(i,j)`

and the bound `E H_omega<=2L |D|`. For the canonical even-width profile with offsets `-W,-W+2,...,W`, `|D|=W+1`. The deterministic-zero-anchor theorem replaces that factor `W+1` by `1`.

At `L=4`, `W=48` and target `lambda_*=3002823/1250000`, the new outer radii are:

- `kappa=1`:
  `R=126997177/1250000 = 101.5977416`,
  versus the previous crude `485.5977416`;
- `kappa=1/2`:
  `R=66997177/625000 = 107.1954832`,
  versus `875.1954832`;
- `kappa=1/4`:
  `R=36997177/312500 = 118.3909664`,
  versus `1654.3909664`;
- `kappa=1/10`:
  `R=18997177/125000 = 151.977416`,
  versus `3991.977416`.

These are analytic certificate-domain reductions, not sampled curvature.

## 6. Second new theorem: a central-coordinate mixed corrector

Assume `W` is even, so the output offset set has a central offset `c=0`. Fix parameters

`kappa>=0`, `eta>=0`, `kappa+eta<=1`.                      (6.1)

Define the normalized corrector

`h_{kappa,eta}(y) := kappa span(y)+eta y_c`.                (6.2)

Since

`span(Phi)=t_last-t_first`,

`Phi_c=F_c-t_first`,                                      (6.3)

we have the exact scalar identity

`g+h(Phi)`
` = (1-kappa-eta)t_first + kappa t_last + eta F_c`
` =: Q_{kappa,eta}(y,omega)`.                             (6.4)

All three maps `t_first=min_j F_j`, `t_last=max_j F_j`, and `F_c` are coordinatewise nondecreasing in `y`. Because all coefficients in (6.4) are nonnegative,

`y<=z coordinatewise  ==>  Q_{kappa,eta}(y,omega)`
`                           <=Q_{kappa,eta}(z,omega)`       (6.5)

samplewise.

We now obtain an exact central reset constant.

Let the fixed output-boundary chain be split at the central offset. The left half contains `W/2` offset links and therefore `W` distinct physical edges; so does the right half. Let their total costs be `X` and `Y`. Then

`X,Y iid Gamma(W,1)`.                                     (6.6)

For every state and environment, if `k` is any output minimizing `F`, then

`Phi_c = F_c-F_k <= chain_distance(k,c) <= max(X,Y)`.       (6.7)

Thus

`E Phi_c <= M_W := E max(X,Y)`.                           (6.8)

### Exact evaluation of `M_W`

Let `S=X+Y` and `U=X/S`. The beta-gamma factorization gives `E S=2W`, `U~Beta(W,W)`, and independence. Also

`|X-Y|=S |2U-1|`.                                        (6.9)

A direct integral evaluates

`E|2U-1|`
` = (2/B(W,W)) int_{1/2}^1 (2u-1)u^{W-1}(1-u)^{W-1} du`
` = 2/[W 4^W B(W,W)]`
` = binom(2W,W)/4^W`.                                    (6.10)

Indeed `(2u-1)u^{W-1}(1-u)^{W-1}=-(1/W)d[u^W(1-u)^W]/du` on `[1/2,1]`. Therefore

`E|X-Y|=2W binom(2W,W)/4^W`,                              (6.11)

and

`M_W = W + W binom(2W,W)/4^W`.                            (6.12)

### P20-FPP-MIXED-CENTRAL-CORRECTOR-40 — CANDIDATE_PROVED

Define

`B_{kappa,eta}(y)`
` := E Q_{kappa,eta}(y,omega)`
`    -kappa span(y)-eta y_c`.                              (6.13)

Then for every finite normalized profile,

`B_{kappa,eta}(y)`
` <= 2L + 2 kappa W + eta M_W`
`    -kappa span(y)-eta y_c`.                              (6.14)

For `W=48`,

`M_48`
` = 64247422146097977376474165077`
`   /1237940039285380274899124224`
` = 51.89865430250223...`.                                (6.15)

#### Proof

From (6.4), equivalently from `g+h(Phi)`, use the anchor bound `E g<=2L`, the span reset `E span Phi<=2W`, and (6.8). Subtract `h(y)` to obtain (6.14). Equation (6.15) is (6.12) evaluated at `W=48`. QED.

The parameter `eta` is not asserted to improve every state. It gives a useful extra coercive penalty precisely on boxes whose central coordinate is already large, while consuming only `eta` of the nonnegative `t_first` coefficient. The safe condition `kappa+eta<=1` is essential.

## 7. Main new theorem: exact upper-corner certification of a continuous profile box

This is the principal verification gain of the run.

Fix an anchor index `a`. Let lower and upper vectors `ell,u` satisfy

`0=ell_a=u_a`,

`0<=ell_i<=u_i` for every `i`.                             (7.1)

Define the anchored continuous box

`C(ell,u;a)`
` := { y : y_a=0 and ell_i<=y_i<=u_i for every i }`.       (7.2)

Every state in this box is normalized because all coordinates are nonnegative and coordinate `a` is zero.

### P20-FPP-UPPER-CORNER-BOX-CERTIFICATE-41 — CANDIDATE_PROVED

For `kappa,eta>=0`, `kappa+eta<=1`,

`sup_{y in C(ell,u;a)} B_{kappa,eta}(y)`
` <= E Q_{kappa,eta}(u,omega)`
`    -kappa max_i ell_i - eta ell_c`.                      (7.3)

Consequently, if a rigorous one-block computation proves the single scalar inequality

`E Q_{kappa,eta}(u,omega)`
` <= lambda + kappa max_i ell_i + eta ell_c`,              (7.4)

then

`B_{kappa,eta}(y)<=lambda`                                (7.5)

for **every continuous profile** in the entire box.

#### Proof

For any `y in C(ell,u;a)`, we have `y<=u` coordinatewise. By the samplewise monotonicity (6.5),

`Q_{kappa,eta}(y,omega)<=Q_{kappa,eta}(u,omega)`.           (7.6)

Taking expectations preserves the inequality. Because `y_a=0` and `y_i>=ell_i`,

`span(y)=max_i y_i >= max_i ell_i`,                        (7.7)

and

`y_c>=ell_c`.                                              (7.8)

Subtract `kappa span(y)+eta y_c` from the expectation bound and use (7.7)--(7.8). This gives (7.3), and (7.4) implies (7.5). QED.

### Why this is stronger than the previous finite-net interpolation theorem

The preceding P20 run proved that a sup-norm `delta`-net controls the Bellman residual with deterministic margin `(1+3 kappa)delta`. The upper-corner theorem has **no interpolation margin at all**. One rigorous scalar expectation at the box's upper corner certifies an uncountable set of profiles.

The verification can therefore be adaptive:

1. fix an anchor and start from a coarse box covering the compact nonnegative profile region;
2. apply the outer drift theorem (5.4) or mixed drift (6.14) first;
3. for a remaining box, rigorously upper-enclose only
   `E Q_{kappa,eta}(u,omega)` at its upper corner;
4. accept the whole box if (7.4) holds;
5. otherwise split the box and repeat.

No projected transition kernel and no tensor grid are logically required.

## 8. Finite-to-infinite compiler and direct source implication

The canonical asynchronous-band compiler and the previous P20 report supply the exact telescoping step. For completeness, the relevant implication is restated here.

Suppose a corrector `h` bounded below and a number `lambda` satisfy, for every finite normalized post-first-band profile,

`E[g_omega(y)+h(Phi_omega(y))]-h(y)<=lambda`.              (8.1)

Condition on the past in each successive physically disjoint band and sum (8.1). The first band, whose initial vector includes infinities, is handled separately; one connected band makes all relevant output labels finite. The terminal offset is repaired by a fresh staircase using at most `W` new mean-one edges. Those first/last contributions are `O(1)` with the block dimensions fixed. Dividing by `NL` and taking `N->infinity` gives

`mu(1,1)<=lambda/L`.                                      (8.2)

Therefore the upper-corner theorem has the source-facing compiler

`finite box cover + rigorous scalar corner enclosures`
`with lambda/L < 0.6005646`
` ==> mu(1,1)<0.6005646`
` ==> Delta_12>0`.                                         (8.3)

This would be only a restricted-direction PARTIAL result for ADH Question 4, not full strict convexity.

## 9. P04 coordination: the remaining rigorous computation is scalar

P04's useful contribution here is its exact finite exponential-infection / physical-edge block machinery, not its reflected opposite-cone inequality. The same-quadrant target requires a diagonal asynchronous block certificate.

For a fixed upper-corner profile `u`, P04 need only enclose the scalar

`E[(1-kappa-eta)t_first(u)`
`   +kappa t_last(u)+eta F_c(u)]`.                         (9.1)

This is materially less information than a complete projected Markov transition kernel. For `Exp(1)` edge weights, a rigorous implementation can use a Richardson/Dijkstra exponential-race recursion with deterministic source activation offsets. A tail-safe interval version must keep every approximation one-sided; e.g. finite truncations cannot silently round an exponential edge downward.

The best current canonical numerical screens are explicitly nonrigorous. They report, for example, projected `L=4,W=48,eps=0.05,H=5`, a sampled block rate around `0.595220618068`, below `0.6005646`, and unprojected widths `30--40` also screen below the threshold. These values are **not used as proof**. They only indicate that a rigorous interval budget of order several `10^{-3}` per lattice unit may plausibly exist.

The new upper-corner theorem improves the certification budget in two ways:

- outer-state certification now starts near projective span `~10^2` rather than `~10^3--10^4` for several useful `kappa` choices at `W=48`;
- interior verification has no `(1+3 kappa)delta` interpolation tax.

This is the precise P20 handoff to P04.

## 10. Executed exact sanity check

I added and executed a supplementary exact-rational checker:

`proofnet24/P20-progress-fpp/artifacts/2026-09-20/`
`2026-09-20T13-09-30Z__mixed-corrector-box-sanity.py`

creation commit

`008d6e2e9b40b18211e51157ce75dbdb854b7eb8`.

It builds four deterministic finite rational-weight undirected block environments, computes their exact input/output passage matrices, and checks with `fractions.Fraction`:

1. coordinatewise monotonicity of the mixed scalar score;
2. the upper-corner whole-box inequality on exact profile grids;
3. exact samplewise output-span and weighted-chain reset inequalities.

The executed output is archived at

`proofnet24/P20-progress-fpp/artifacts/2026-09-20/`
`2026-09-20T13-09-30Z__mixed-corrector-box-sanity.out`

creation commit

`f58ef6193319bd49ccf0f67589fae0d0166b5690`.

It records

`environments = 4`,
`profiles = 2101`,
`monotonicity_checks = 3000`,
`boxes = 20`,
`box_profile_checks = 1620`,
`reset_checks = 648`,

and terminates

`ALL_EXACT_FRACTION_CHECKS_PASS`.

The checker is supplementary finite sanity evidence only. It is not an asymptotic FPP proof, is not sampled numerical curvature, and does not certify the missing one-block `Exp(1)` expectations at the widths needed for (8.3).

## 11. Honest obstruction and failure report

The local/projective geometry is no longer the principal obstruction in this route. The remaining hard step is computational-but-rigorous:

> obtain certified **upper** enclosures of the one-band expectation (9.1) on enough adaptively selected upper corners to cover the compact profile region, with total error small enough to achieve `lambda/L<0.6005646`.

At widths around `30--48`, direct enumeration of every profile is impossible. The new box theorem removes the need to do so, but the block environment itself is still large, and `t_last` is a max of dependent first-passage labels. A rigorous interval Richardson recursion must control exponential tails, deterministic source activation offsets, and branching without losing the several-milliths margin suggested by screens.

No theorem in this report shows that such an enclosure will succeed. If the rigorous interval bounds land above threshold, that is a genuine failure of this quantitative route rather than evidence of curvature.

The Busemann/Jacquet residual route remains preserved as a separate fallback: under flatness it forces positive-density true-geodesic backtracks to be nearly co-calibrated for the diagonal target. The upper-corner min-plus theorem may later help encode that rigidity, but no such synthesis is claimed here.

## 12. Next attack

The next attack is an **interval Richardson branch-and-bound certificate** built around Theorem 41, not a denser global grid.

1. Start with `L=4` and widths `W=30,40,48`, because the existing screens separate the obviously too-narrow regime from widths with apparent slack.
2. Choose a small family of `(kappa,eta)` correctors; begin with `eta=0` and then use the central term only on boxes with large central lower coordinate.
3. Cover normalized profiles anchor-by-anchor; discard boxes immediately using (5.4)/(6.14).
4. At each unresolved box evaluate a rigorous upper interval for the scalar score (9.1) at the upper corner only.
5. Split the coordinate contributing most to the interval excess; exploit reflection symmetry before splitting.
6. Preserve a complete one-sided error ledger for exponential tails and rational/interval arithmetic.
7. Stop the route honestly if the certified bound cannot beat `0.6005646`; do not replace the missing proof by the sampled screen.

This attack is materially narrower than the preceding continuous-net proposal: it has no tensor-net requirement and no deterministic interpolation loss.

## 13. Short cyclic-interval handoff

The displaced P20 cyclic-interval proof remains preserved and is not reopened in this run. The source-literal candidate

`P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01`

remains on record together with its existing exact sanity artifact. P26's full-proof/source-quantifier audit remains **PASS**; the last recovered certification gate is still one genuinely independent audit out of the requested two. No completed certification or novelty claim is implied, and no research effort in this run was spent waiting for the second audit.

## 14. Original-problem / mechanism ledger

### Original problem

`Delta_12 >= c_*`:

- before: `c_*=0`;
- after: `c_*=0`.

Full ADH continuous-law strict convexity: **OPEN**.  
Exp(1) full strict convexity: **OPEN**.  
Axis/diagonal strictness: **OPEN**.

### Demonstrated mechanism gains

1. `P20-FPP-ANCHOR-DRIFT-COMPACTIFICATION-39 = CANDIDATE_PROVED`:
   replaces the crude `E H<=2L(W+1)` input-reset cost by pointwise `E g(y)<=2L`; at `L=4,W=48` this shrinks outer projective radii by factors ranging from roughly `4.8` to `26` in the displayed `kappa` examples.
2. `P20-FPP-MIXED-CENTRAL-CORRECTOR-40 = CANDIDATE_PROVED`:
   adds a central-coordinate penalty with exact reset
   `M_W=W+W binom(2W,W)/4^W`.
3. `P20-FPP-UPPER-CORNER-BOX-CERTIFICATE-41 = CANDIDATE_PROVED`:
   a single rigorous scalar expectation at a box upper corner certifies every continuous profile in that box, with **zero interpolation margin**.
4. P04 handoff is now a scalar interval expectation / branch-and-bound problem rather than full profile-transition enumeration.

### Residual obstruction

Rigorous finite-block interval evaluation at useful widths has not yet been completed tightly enough to certify `lambda/L<0.6005646`.

## 15. ledger_delta

```text
P20 | T10 iid Exp(1) undirected Z2 FPP strict convexity | source c_*: 0 -> 0; full source OPEN -> OPEN/PARTIAL | NEW CANDIDATE_PROVED 39 deterministic-zero-anchor drift: E g(y)<=2L and B_kappa<=2L+2kappa W-kappa span(y), sharply shrinking compactification radius | NEW CANDIDATE_PROVED 40 mixed central corrector h=kappa span+eta y_c with exact Gamma reset M_W=W+W*C(2W,W)/4^W | NEW CANDIDATE_PROVED 41 exact upper-corner profile-box Bellman certificate, eliminating prior (1+3kappa)delta interpolation loss | P04 handoff: rigorously upper-enclose one scalar E[(1-kappa-eta)t_first+kappa t_last+eta F_c] per unresolved upper corner; target lambda/L<0.6005646 | exact rational sanity checker/output archived; not asymptotic proof | cyclic candidate preserved, P26 audit PASS, independent gate remains 1/2 | residual: rigorous interval Richardson enclosure at W~30-48
```

END OF P20 FPP RUN REPORT
