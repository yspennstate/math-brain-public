Runtime model family exposed to this session: **GPT-5.6 Sol**. Applied reasoning-effort metadata is **UNVERIFIED**; no GPT-6/maximum-effort receipt is exposed or claimed.

# P20 T10 — ancestor fixed-point Bellman certificate and subset-only Richardson ancestry recursion

Date: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Controlling directive: `operations/PROGRESS20_2026-09-20.md`.  
Canonical parent: `operations/claims/PROB10-10.md`.  
Model: nearest-neighbor **undirected** FPP on `Z^2` with iid physical-edge weights `Exp(1)`.  
Status: **PARTIAL / OPEN** for the source problem. The theorem arguments below are **CANDIDATE_PROVED pending later independent review**. No certification, novelty, or priority claim is made.

## 1. Exact source and source-facing accounting

The exact parent remains Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262. Question 4 in §2.5.1 asks:

> Show that if `F` is a continuous distribution then the limit shape is strictly convex.

Section 2.8 explicitly treats strict convexity as conjectural. The repository freezes the iid `Exp(1)`, undirected nearest-neighbor `Z^2` specialization.

Let `mu` be the deterministic time-constant norm and

`Delta_12 := 2 mu(e1)-mu(1,1) >= 0`.

The retained rigorous axis lower certificate is

`mu(e1) >= b := 3002823/10000000 = 0.3002823`,

so it is enough for the first axis/diagonal checkpoint to prove

`mu(1,1) < 2b = 3002823/5000000 = 0.6005646`.

Original-problem metric:

- **before:** largest proved `c_*` with `Delta_12 >= c_*` is `0`;
- **after:** `c_*=0`.

Thus this run does **not** prove `Delta_12>0`, and certainly does not close full strict convexity.

A bounded fresh source check on 20 September 2026 again found no source-matching unconditional resolution. Dembin--Elboim--Peled, arXiv:2204.02332, require more than 32 extreme points of the limit shape for their quantitative coalescence theorem. Jacquet's arXiv:2412.20779 proves strict unrestricted-versus-directed time constants, not this same-quadrant triangle defect. Jacquet's pattern theorem, arXiv:2310.04091, remains useful for true-geodesic geometry but likewise does not close the checkpoint. Directed integrable models are not imported as evidence for the present undirected model.

## 2. Essential continuity and recovered failures

I consumed only the dependencies needed for the new attack:

1. `operations/PROGRESS20_2026-09-20.md` and the LIVE20 pairing P20 with P04 on T10;
2. `operations/claims/PROB10-10.md`;
3. P20's preceding report `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T14-10-00Z__weighted-profile-delayed-richardson.md`;
4. the canonical owner's current asynchronous-carry compiler and source-domination report, especially `runs/prob10_2026-09-20/PROB10-10/20260920T1448Z__source-domination-pruning.md`;
5. P04's latest complete T10 report on current master, `proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T14-45-50Z__adaptive-stop234-cone1357.md`;
6. the R08 strict-gap failure history and retained axis lower certificate;
7. the displaced cyclic-interval proof only for its short preservation handoff.

The binding failures are preserved, not reset:

- shared bypasses invalidate multiplying nominally local surgery savings;
- pointwise finite-scale strict triangle saving is false on positive-probability cylinder events;
- old fixed-corner exact blocks did not reach the diagonal threshold;
- first-moment SAW/Chernoff counting has a diagonal barrier from monotone E/N paths;
- reflected-cone inequalities are compatible with the exact `l1` diamond and therefore are not source-facing progress on `Delta_12`;
- the Jacquet/Busemann true-geodesic route can collapse under flatness to near-co-calibration, leaving a global rigidity obstruction;
- sampled carry values below `0.6005646` remain screens only.

The last three P20 block runs progressively reduced the continuous-profile Bellman verification but retained the same core obstruction: certify a Bellman inequality over a large asynchronous profile state space. In accordance with the stagnation rule, this run changes the object being certified. The new theorem eliminates the profile cover entirely.

## 3. Fresh-band min-plus operator

Fix one finite diagonal band in rotated coordinates `s=x+y`, `d=x-y`, with the same finite offset index set

`D={1,...,M}`

on its left and right antidiagonal boundaries. For a realized fresh band environment `omega`, let

`d_omega(i,j)`

be the restricted passage metric from input offset `i` to output offset `j`. For a finite incoming profile `y=(y_i)`, put

`F_omega(y)_j := min_i {y_i+d_omega(i,j)}`,

`g_omega(y) := min_j F_omega(y)_j`,

`Phi_omega(y) := F_omega(y)-g_omega(y) 1`.

After the first connected band every coordinate of the exact carried profile is finite almost surely. All later profiles are normalized by `min y=0`, hence `y_i>=0`.

For each output `j`, fix a measurable minimizing input at the **flat profile** `y=0`:

`I_j(omega) in argmin_i d_omega(i,j)`.

For iid continuous edge weights the minimizer is unique almost surely; the argument below does not need uniqueness because any deterministic tie rule suffices.

Define

`q_j := E[min_i d_omega(i,j)]`,

and the ancestor kernel

`K_ij := P(I_j=i)`.

Each column of `K` sums to one, so `K` is column-stochastic. Therefore `K` maps the probability simplex into itself and has at least one fixed probability vector `alpha` satisfying

`alpha_i>=0`, `sum_i alpha_i=1`, `K alpha=alpha`.

## 4. P20-FPP-ANCESTOR-FIXED-POINT-BELLMAN-45 — CANDIDATE_PROVED

### Theorem

Let `alpha` be any probability vector satisfying `K alpha=alpha`, and define the linear projective corrector

`h_alpha(y):=alpha dot y`.

Then for **every** finite incoming profile `y`,

`E[g_omega(y)+h_alpha(Phi_omega(y))]-h_alpha(y)`

` <= lambda_alpha := alpha dot q`.                              (4.1)

Consequently, for the exact unprojected asynchronous carry through iid fresh length-`L` bands,

`mu(1,1) <= lambda_alpha/L`.                                    (4.2)

Combining with the retained axis lower certificate gives

`Delta_12 >= 0.6005646-lambda_alpha/L`.                          (4.3)

Hence any rigorous finite-band certificate

`alpha dot q < 0.6005646 L`                                     (4.4)

with `K alpha=alpha` proves `Delta_12>0`.

### Proof

For every realization, every output `j`, and every finite profile `y`, the flat-profile ancestor `I_j` is an admissible competitor in the min defining `F_j(y)`. Therefore

`F_omega(y)_j`
` <= y_{I_j(omega)}+d_omega(I_j(omega),j)`
` = y_{I_j(omega)}+F_omega(0)_j`.                               (4.5)

Multiply (4.5) by `alpha_j`, sum over `j`, and take expectations. Because

`E[y_{I_j}]=sum_i K_ij y_i`,

we obtain

`E[alpha dot F_omega(y)]`
` <= alpha dot q + (K alpha) dot y`
` = alpha dot q + alpha dot y`.                                 (4.6)

Since `sum alpha_j=1`, translation covariance gives the exact identity

`g_omega(y)+h_alpha(Phi_omega(y))`
` = g_omega(y)+alpha dot(F_omega(y)-g_omega(y)1)`
` = alpha dot F_omega(y)`.                                      (4.7)

Subtract `h_alpha(y)=alpha dot y` from (4.6) and use (4.7). This proves (4.1).

For the infinite-volume transfer, use the already-proved exact asynchronous band concatenation with no projection. Let `M_j` be the accumulated minimum after band `j` and `Y_j` the normalized carried profile. Start the Bellman telescope after the first connected band. For `N>=2`, conditioning on the past and applying (4.1) gives

`E[M_N+h_alpha(Y_N)]`
` <= E[M_1+h_alpha(Y_1)] + (N-1)lambda_alpha`.                   (4.8)

Normalized profiles are nonnegative and `alpha>=0`, so `h_alpha(Y_N)>=0`. The canonical fresh terminal staircase from the minimizing output offset back to offset zero uses at most `W` fresh physical edges, hence has conditional expected cost at most `W`. Therefore

`E T(0,(NL,NL))`
` <= (N-1)lambda_alpha + E[M_1+h_alpha(Y_1)] + W`.               (4.9)

The first-band expectation is finite because the band is finite and its edges have finite mean. Divide (4.9) by `NL` and let `N->infinity`; standard `L^1` time-constant convergence gives (4.2). Equation (4.3) follows from `mu(e1)>=0.3002823`. QED.

### Why this is materially different

The preceding P20 correctors needed either a compact profile cover, upper-corner delayed-source evaluations, or a profile projection. Theorem 45 needs **none** of them. The worst incoming profile is controlled by the flat-profile ancestry kernel through the pathwise envelope (4.5). A single finite-band pair `(q,K)` certifies all continuous profiles at once.

This is also distinct from the canonical owner's tropical `k`-front idea: no `k`-subset assignment problem is used. The corrector is a linear probability weight selected by the fixed point of the flat-profile ancestor map.

## 5. Controlled-error version: an approximate ancestor fixed point is enough

Exact stationary vectors are unnecessary for a rigorous numerical certificate.

Let `alpha` be any probability vector and set

`r := K alpha-alpha`,

`epsilon := (1/2)||r||_1`.

Because the columns of `K` sum to one and `sum alpha=1`,

`sum_i r_i=0`.                                                   (5.1)

For a normalized profile `min y=0`,

`r dot y <= epsilon span(y)`.                                    (5.2)

Indeed the total positive mass of the zero-sum vector `r` is exactly `epsilon`, every positive-coordinate contribution is at most `epsilon max y`, and the negative coordinates can only reduce the scalar product.

The same envelope proof as above gives

`E[alpha dot F(y)]-alpha dot y`
` <= alpha dot q + r dot y`
` <= alpha dot q + epsilon span(y)`.                             (5.3)

Now use the augmented corrector

`h(y):=alpha dot y + epsilon span(y)`.                            (5.4)

The output-span reset from the fixed two-edge output-boundary chain gives

`E span(Phi_omega(y)) <= 2W`                                    (5.5)

uniformly in `y`: if `j_*` minimizes the output profile, then each other output label is at most the label at `j_*` plus the passage cost along the output chain; traversing the entire chain uses `W` independent two-edge links of mean two, so the span is bounded by their total cost.

Combining (5.3)--(5.5),

`E[g(y)+h(Phi(y))]-h(y)`
` <= alpha dot q + epsilon E span(Phi(y))`
` <= alpha dot q + 2W epsilon`
` = alpha dot q + W ||K alpha-alpha||_1`.                        (5.6)

This proves the following robust certificate.

### P20-FPP-APPROX-ANCESTOR-EIGENVECTOR-46 — CANDIDATE_PROVED

For every probability vector `alpha`,

`mu(1,1)`
` <= [alpha dot q + W ||K alpha-alpha||_1]/L`.                   (5.7)

Consequently

`Delta_12`
` >= 0.6005646`
`    -[alpha dot q + W ||K alpha-alpha||_1]/L`.                  (5.8)

Thus interval arithmetic may certify only

- upper bounds `q_j <= qbar_j`, and
- a rigorous residual bound `||K alpha-alpha||_1 <= R`

for a rational probability vector `alpha`. It then suffices to check the scalar inequality

`sum_j alpha_j qbar_j + W R < 0.6005646 L`.                      (5.9)

This is the controlled-error source compiler. There is no profile discretization error; all finite approximation is exposed in `qbar` and `R`.

## 6. P20-FPP-SUBSET-ANCESTRY-RICHARDSON-47 — CANDIDATE_PROVED

The remaining finite computation can also be reduced substantially. A naive exact evaluator would carry the initial-source label of every infected vertex. That is unnecessary.

Let `G=(V,E)` be one finite band. Simultaneously infect all input vertices at time zero. For an infected set `S`, let `b(S)` be the number of physical edges with exactly one endpoint in `S`. Under iid `Exp(1)`, memorylessness implies that the next boundary edge is uniform among those `b(S)` edges and the holding time has mean `1/b(S)`.

For an output vertex `j`, define `q_j(S)` to be its expected remaining infection time. Then

`q_j(S)=0` if `j in S`,                                         (6.1)

and otherwise

`q_j(S)`
` = 1/b(S) + (1/b(S))`
`   sum_{(x,v): x in S, v notin S, {x,v} in E} q_j(S union {v}).` (6.2)

This is the standard subset Richardson recursion.

For ancestry, attach an arbitrary real scalar `z_x` to each currently infected vertex `x in S`. Whenever an infection crosses `x->v`, let the newly infected vertex copy the parent's scalar:

`z_v:=z_x`.                                                      (6.3)

The infection dynamics are independent of these scalar values. Therefore the expected scalar eventually inherited by output `j` is a linear function

`A_{S,j}(z)=sum_{x in S} H_{S,j}(x) z_x`.                        (6.4)

If `j in S`,

`H_{S,j}=e_j`.                                                   (6.5)

If `j notin S`, condition on the first firing boundary edge `x->v`. Let `H_child` be the coefficient vector at `S union {v}`. Since the child's scalar satisfies `z_v=z_x`, substitute the child coefficient of `v` into the coefficient of `x`. Explicitly, define

`(R_{x,v} h)(u)=h(u)+1{u=x}h(v)`, for `u in S`.                  (6.6)

Then

`H_{S,j}`
` = (1/b(S))`
`   sum_{(x,v) in boundary(S)} R_{x,v} H_{S union {v},j}.`        (6.7)

Every transition strictly enlarges `S`, so (6.1)--(6.7) form a finite acyclic recursion indexed **only by infected subsets**. Starting from the initial input set `S_0`,

`K_ij = H_{S_0,j}(s_i)`.                                        (6.8)

All coefficients and all `q_j` are rational because the recursion uses only integer boundary counts and rational averaging.

### Proof

Equations (6.1)--(6.2) are the usual exponential-race conditioning. For (6.4), future infection-edge choices do not depend on `z`, and the scalar at every future vertex is always copied from exactly one current scalar, so the expected terminal scalar is linear. At a first jump `x->v`, the child continuation is linear in the enlarged scalar vector, and (6.3) identifies the new coordinate with the parent's coordinate; this is exactly substitution (6.6). Averaging the child functional over the uniform boundary-edge race gives (6.7). Backward induction on `|V\S|` proves all claims. QED.

### Why this matters computationally

The preliminary same-run checker that explicitly stored source labels required

- 69 labelled states for `L=1,W=2`;
- 4,053 labelled states for `L=1,W=4`.

The subset-only recursion computes the **same exact** `q`, `K`, `alpha`, and `lambda` using only

- 17 subset states for `L=1,W=2`;
- 217 subset states for `L=1,W=4`.

So the ancestry information does not multiply the state space by the number of label assignments. The finite computation is now on the same infected-set DAG as the ordinary Richardson expectation, with additional linear coefficients propagated over that DAG.

This is the key P04 coordination gain: P04 already has a dependence-valid exponential infection-set recursion and exact upward rounding architecture. To use Theorem 46 it need not certify a continuous profile, delayed-source family, or labelled-infection state. It only has to propagate first-hit times and the linear ancestry coefficients on its existing subset/frontier state representation.

## 7. Executed exact sanity check

The primary checker is

`proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T15-38-56Z__subset-ancestry-exact-sanity.py`

creation commit `32c67bd7ee91e02d9d63ff86d129fbd2369c052a`.

Its archived output is

`proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T15-38-56Z__subset-ancestry-exact-sanity.out`

creation commit `59f266f83aa08766b4936ed09502605fa858da18`.

It uses exact `Fraction` arithmetic throughout and ends

`ALL_EXACT_CHECKS_PASS = True`.

For `L=1,W=2`, it obtains

`q=(53/36, 11/12, 53/36)`,

`K = [[17/36,1/4,1/36],`
`     [1/2,  1/2,1/2 ],`
`     [1/36,1/4,17/36]]`,

`alpha=(1/4,1/2,1/4)`,

`K alpha=alpha`, and

`lambda=43/36`.

For `L=1,W=4`, it obtains the exact stationary vector

`alpha=(35359/290152, 1/4, 37179/145076, 1/4, 35359/290152)`

and

`lambda=5456065/5222736 = 1.044675625955438...`,

again with exact `K alpha=alpha` and exact unit column sums.

These values are only finite sanity checks; they are far above the source threshold at `L=1` and are **not** presented as curvature evidence. Their purpose is to verify the algebra and the subset-state compression.

A preliminary explicit-label checker is also preserved immutably at commits

`d0e586b834734480880a03023aa18dd4c833a7b7`

(code) and

`32c831b728e297f90221e6fa3c5f0e095372be44`

(output). It computes the same exact matrices, providing an independent same-run check of the subset substitution recursion. It is superseded computationally, not overwritten.

## 8. Coordination with P04's current transfer

P04's latest complete report proves an adaptive fresh-column Richardson stopping policy with random horizontal advance `D in {2,3,4}` and the explicit finite-to-infinite estimate

`E T(0,n e1)`
` <= (16139/31250)n`
`    + sqrt((2334416160657687/10^15) ceil((n-3)/2)) + 3`,

hence `mu(e1)<=0.516448`. This is a valid dependence-controlled renewal transfer, although its reflected-cone consequences remain compatible with the `l1` diamond and therefore do not move `c_*`.

The relevant P04 technology for the present theorem is not that reflected cone; it is the exact finite Richardson recursion, physical-edge freshness, and upward rational rounding. Theorem 47 fits that machinery directly.

A concrete shared finite target is now:

1. choose a diagonal band `(L,W)`;
2. run the simultaneous-source subset Richardson recursion to obtain rigorous upper intervals `q_j<=qbar_j` and ancestry-coefficient intervals sufficient to bound `R>=||K alpha-alpha||_1` for a rational `alpha`;
3. certify

   `sum alpha_j qbar_j + W R < 0.6005646 L`;

4. invoke Theorem 46 plus the exact asynchronous block-to-infinite-volume transfer.

This target is strictly smaller than the preceding P20/P04 task of certifying a Bellman inequality over a continuous asynchronous profile core.

The canonical owner's newest source-domination pruning theorem is valuable for delayed high sources, but it does not directly simplify the present **flat simultaneous-source** block because all activation times are equal. The subset-ancestry recursion is the appropriate reduction for this attack.

## 9. Residual obstruction and honest failure report

The source-facing inequality is not yet certified. The unresolved quantity is now finite and explicit:

`Lambda(L,W,alpha)`
` := [alpha dot q + W ||K alpha-alpha||_1]/L`.                   (9.1)

We need one rigorous finite band with

`Lambda(L,W,alpha) < 0.6005646`.                                 (9.2)

The exact subset recursion still grows exponentially with the number of vertices if implemented as a raw infected-set table. An attempted brute-force extension during this run exceeded the interactive execution budget before reaching a source-relevant block. I do **not** use any partial output from that interrupted computation.

Thus the remaining obstruction is no longer a continuous Bellman state space or a Busemann path-unavoidability theorem. It is **frontier compression / rigorous interval evaluation of one simultaneous-source subset process** at a useful diagonal width and length.

No sampled numerical curvature, directed-integrable input, or interrupted calculation is promoted to a theorem.

## 10. Next attack

The next attack is a frontier/pathwidth compression of (6.1)--(6.7), preserving only the infected frontier and the linear ancestry transfer needed for `K alpha`, rather than the full infected subset. The target should be a rational/interval certificate of (9.2), not another Monte Carlo screen.

Two implementation features should be exploited:

- **approximate fixed point instead of exact eigenvector:** Theorem 46 converts all ancestry approximation into the explicit penalty `W||K alpha-alpha||_1`, so interval arithmetic can stop once the total error budget is safely below the source margin;
- **P04 first-hit freshness:** if a fixed-length band remains too large, introduce stopping only at a fresh antidiagonal first hit, exactly as P04 does for its axis renewal, and formulate the ancestor kernel for the resulting semi-Markov block together with a Dinkelbach transformed cost. The first attempt should remain fixed-length because its Bellman theorem is already complete.

If this frontier-compressed simultaneous-source recovery also fails twice, the unresolved scope should switch away from this block lane while preserving Theorems 45--47 for future reuse.

## 11. Short cyclic-interval handoff

The displaced source `FOKAM-BITJOKA-2026-CYCLIC-INTERVAL` remains preserved and untouched. The source-literal proof candidate

`P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01`

remains on record. P26's full-proof/source-quantifier audit remains

`PASS_FULL_MATHEMATICAL_PROOF / SOURCE_LITERAL_CONJECTURE_2_41 / SOURCE_QUANTIFIERS_PASS`,

with the second genuinely distinct audit still pending in the last recovered state. No completed certification, prior-art clearance, or posting claim is implied. This run spent no mathematical effort waiting for that audit.

## 12. ledger_delta

### Original problem

- target: `Delta_12=2mu(e1)-mu(1,1)`;
- rigorous lower bound before: `c_*=0`;
- rigorous lower bound after: `c_*=0`;
- full ADH strict convexity: **OPEN**.

### Demonstrated mechanism gain

- before: rigorous diagonal Bellman certification required control of a continuous carried profile, reduced only to boxes/delayed-source expectations;
- after: a flat-profile ancestor kernel `(q,K)` yields a global all-profile Bellman supersolution through `K alpha=alpha`;
- robust error compiler:

  `mu(1,1) <= [alpha dot q + W||K alpha-alpha||_1]/L`;

- finite evaluator improvement: ancestry is propagated on the ordinary infected-subset Richardson DAG, not a source-labelled state space;
- exact sanity state counts improve from `69 -> 17` at `L=1,W=2` and `4053 -> 217` at `L=1,W=4` while reproducing identical exact `q,K,alpha,lambda`.

### Residual obstruction

Produce a source-relevant rigorous finite-band interval certificate with

`alpha dot q + W||K alpha-alpha||_1 < 0.6005646 L`.

### Next attack

Frontier/pathwidth-compressed subset Richardson ancestry recursion, with interval `q` and eigen-residual certification; if needed afterward, combine with P04-style fresh first-hit stopping.

### Persistence

Primary exact checker creation commit: `32c67bd7ee91e02d9d63ff86d129fbd2369c052a`.  
Primary exact output creation commit: `59f266f83aa08766b4936ed09502605fa858da18`.  
Preliminary explicit-label checker/output commits: `d0e586b834734480880a03023aa18dd4c833a7b7`, `32c831b728e297f90221e6fa3c5f0e095372be44`.

END OF P20 FPP RUN REPORT
