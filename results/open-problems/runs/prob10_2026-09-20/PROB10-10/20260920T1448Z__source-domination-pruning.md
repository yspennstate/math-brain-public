Model requested: **GPT-6 maximum**. Applied runtime model/effort metadata is **UNVERIFIED**; this run does not claim that GPT-6 maximum was actually applied.

# PROB10-10 — quantitative source-domination pruning for asynchronous Exp(1) Bellman blocks

Status: **PARTIAL / OPEN**. Source-level metric `c_*: 0 -> 0`. No claim of full strict convexity and no claim yet that `Delta_12>0`.

## 1. Frozen source target and exact accounting

The model is unchanged throughout:

- graph: nearest-neighbor **undirected** `Z^2`;
- physical edge weights: iid `Exp(1)`;
- time constant norm: `mu` in the standard normalization;
- source: Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 4 / strict-convexity discussion.

The canonical first checkpoint remains

`Delta_12 := 2 mu(e1) - mu(1,1)`.

The retained rigorous axis lower certificate is

`mu(e1) >= b := 3002823/10000000 = 0.3002823`,

so the one-pair checkpoint would follow from

`mu(1,1) < 2b = 3002823/5000000 = 0.6005646`.

This run does **not** prove that inequality. Source-level before/after:

- before: largest proved `c_*` with `Delta_12 >= c_*` is `0`;
- after: `c_*=0`.

No directional strict-triangle range is enlarged. Full ADH strict convexity remains open in this track.

The mechanism delta is different: the current asynchronous Bellman program can now delete quantitatively dominated delayed boundary sources with a completely explicit error, reducing its finite-state dimension without recreating the old independence mistake.

## 2. Continuity, handoff, ownership, and consumed updates

The mandatory HARD7-03 predecessor handoff was already left immutably and was re-read:

- `runs/prob10_2026-09-20/PROB10-10/20260919T2321Z__handoff-hard7-03-d0025.md`, blob `1a7045aaf81930242664b944b6f0ab09f791c4c1`.

It preserves the actual D0025 / Seppalaeinen particle-system successor, including the newest four-step sign atlas and the restricted `K=2` binary-disorder plateau lower bound. Nothing in that predecessor is overwritten here.

Essential current material consumed:

- `operations/PROB10_2026-09-20.md` on current `master`;
- root `POSTED.md` on current `master` (including the 20 September posting inventory; no source-matching FPP strict-convexity result is posted there);
- `operations/claims/PROB10-10.md`, blob `6fca778a3608f973175577e9852a61dcd6754c55`;
- canonical preceding report `runs/prob10_2026-09-20/PROB10-10/20260920T1406Z__asynchronous-carry-richardson-exactification.md`, blob `4a4abf65f68f1801a96b09db881b6c1604c97bf4`, creation/readback chain ending at canonical commit `4a4a81c6078e76f6096efe0f681e7298f7b12457`;
- newest complementary P20 report found at preflight and rechecked immediately before this report: `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T14-10-00Z__weighted-profile-delayed-richardson.md`, blob `eab544da5c6652cb8dd74906576ef8c0d4d8f1ca`;
- newest P04 report found under its designated T10 progress root: `proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T09-47-23Z__width7-undirected-cone1362.md`, blob `0b14a30ca773496f6467a1ea4c770222459134d5`;
- R08 axis transition report `runs/R08/20260916T1528Z_fpp_axis_transition_3b7c92.md`;
- R08 stuck report `runs/R08/20260916T1623Z_stuck_diagblock_4c19a7.md`, blob `7bd29c35e7bed188864bd766db70d20ce46ddac6`;
- distinct R07 fluctuation/KPZ history, especially `runs/R07/2026-09-16T1525Z_kpz_deep_edges_03.md`.

The exact historical failures remain binding and are not reset: shared bypasses destroy naive multiplication of local surgery savings; pointwise finite-scale strict saving fails on positive-probability cylinder events; old fixed-corner blocks did not reach the diagonal checkpoint; the first-moment SAW/Chernoff architecture has a diagonal barrier from monotone E/N paths; and R07 fluctuation statements are not curvature theorems.

Ownership remains nonduplicating. PROB10-10 owns the source parent and the present reduction layer. P20 owns its weighted-corrector / delayed-Richardson and true-geodesic residual lanes; P04 owns its complementary finite-block upper constructions. This report consumes those results and supplies a handoff-compatible reduction rather than editing either worker's claim.

## 3. Fresh bounded source/prior-art gate

A fresh bounded search on 20 September 2026 again found no unconditional source-matching theorem proving strict convexity for ordinary iid `Exp(1)` nearest-neighbor undirected FPP on `Z^2`.

The relevant boundaries remain:

- Auffinger--Damron--Hanson, arXiv:1511.03262: source/open-problem navigation;
- Dembin--Elboim--Peled, arXiv:2204.02332: quantitative coalescence assumes more than 32 extreme points of the limit shape, so it does not supply the missing shape property in the present Exp(1) case;
- Jacquet's unrestricted-versus-directed strict comparison is not `2mu(e1)>mu(1,1)`;
- the 1+1-dimensional/simplified-model classification results returned by the current search are different models.

Thus the frozen axis/diagonal regime is still a genuinely unresolved checkpoint in the bounded search. This is negative search evidence only, not a worldwide novelty certificate.

## 4. Three materially different routes compared

The new idea was persisted **before repository certificate code** at

`artifacts/prob10_2026-09-20/PROB10-10/20260920T1448Z__idea-source-domination-pruning.md`

creation commit `3ef6f1be9081829b8bd28f76081ba80c7f25c96e`.

### A. Quantitative delayed-source domination — pursued

P20 can exactly evaluate asynchronous source activations, but the source/subset state space is huge. Delete a high activation only when a nearby source has a substantially earlier activation, and pay the deletion loss by an explicit Gamma positive-part tail along a deterministic boundary path. This is the new theorem below.

It is not the retired R08 detour route. No local saving is multiplied. Instead, one proves a **samplewise global domination of the entire arrival field** after source deletion.

### B. Full unpruned Bellman / delayed-Richardson enumeration — retained, not duplicated

The canonical carry theorem and P20 delayed-Richardson theorem are already rigorous. Their bottleneck is combinatorial state explosion at widths where the numerical carry has source-facing room. The new theorem is intended as a certified reduction layer for that existing route rather than another unpruned enumeration.

### C. True-geodesic Busemann/Jacquet residual contradiction — not duplicated

P20's actual-geodesic lane remains geometrically distinct. It forces backtracking patterns but, under a flat-face hypothesis, the finite-target residuals can collapse toward co-calibration. The remaining obstruction is global: exclude a positive-density family of near-calibrated backtracking segments. No local pattern theorem in the current history pays that step.

A one-source moving-centered undirected diagonal block is another possible finite-state attack, but no rigorous crossing certificate below `0.6005646` is currently archived; repeating progressively larger subset recursions without a state reduction would not satisfy the present contract.

## 5. New theorem: samplewise source-domination pruning

Let `G=(V,E)` be any finite graph with positive edge lengths. Let input vertices be `s_1,...,s_M`, with deterministic activation times

`y_i >= 0`.

Define the multi-source arrival field

`F(v) := min_i { y_i + T_G(s_i,v) }`.

Let `I` be a nonempty retained source set and `J` its deleted complement. Define the retained arrival field

`F_I(v) := min_{i in I} { y_i + T_G(s_i,v) }`.

For each `j in J`, choose an anchor `a(j) in I` and a deterministic path `P_j` in `G` from `s_{a(j)}` to `s_j`. Let `tau(P_j)` be its realized edge-weight sum and put

`eps_j := ( y_{a(j)} + tau(P_j) - y_j )_+`,

`eps := max_{j in J} eps_j`, with `eps=0` if `J` is empty.

### Theorem 5.1 — global arrival-field domination

For every realization and every vertex `v`,

`0 <= F_I(v)-F(v) <= eps`.                                      (5.1)

#### Proof

The first inequality is immediate because deleting sources only removes competitors from the minimum.

Fix `v` and choose a source attaining the original finite minimum; ties do not matter. If an attaining source `i` belongs to `I`, then the same source remains available after deletion, so

`F_I(v) <= y_i+T(s_i,v)=F(v)`,

and equality follows from `F_I>=F`.

If an attaining source is `j in J`, then the retained process can reach `s_j` through its anchor:

`F_I(s_j) <= y_{a(j)}+tau(P_j) <= y_j+eps_j`.

The FPP triangle inequality gives

`F_I(v) <= F_I(s_j)+T(s_j,v)`
`        <= y_j+eps_j+T(s_j,v)`
`        = F(v)+eps_j`
`        <= F(v)+eps`.

This proves (5.1). The concatenated walk may overlap itself or the later optimal route; positive edge lengths allow loop erasure and can only reduce its cost, so no disjointness or independence is hidden in the argument. QED.

The theorem is deterministic. Exp(1) is used only to turn its error into the explicit expectation below.

## 6. Bellman functional is 1-Lipschitz under this domination

Let `O` be the output boundary. Use the P20 weighted projective functional

`Q(z)`
` := (1-kappa-A) min_{o in O} z_o`
`    + kappa max_{o in O} z_o`
`    + sum_{o in O} alpha_o z_o`,                              (6.1)

where `kappa>=0`, `alpha_o>=0`, `A=sum alpha_o`, and `kappa+A<=1`.

All coefficients in (6.1) are nonnegative and sum to one.

### Corollary 6.1

Under the hypotheses of Theorem 5.1,

`0 <= Q(F_I|_O)-Q(F|_O) <= eps`.                                (6.2)

#### Proof

If two output vectors satisfy `z<=z'<=z+eps*1`, then their minima, maxima, and every coordinate each increase by a quantity in `[0,eps]`. Multiplying by the nonnegative coefficients in (6.1), whose sum is one, gives (6.2). Apply (5.1). QED.

This explicitly quantifies the conservatism in P20's monotone source-deletion certificate. Source deletion was already known to be safe for an upper certificate; the new information is that a suitably dominated deletion is **nearly lossless by a computable amount**.

## 7. Exact Exp(1) pruning error

Now restore iid `Exp(1)` physical edges. Suppose every chosen `P_j` is simple with `k_j` edges and

`y_j-y_{a(j)} >= R_j >= 0`.                                    (7.1)

Then

`eps_j <= (tau(P_j)-R_j)_+`.

No independence among the paths is needed, because

`max_j eps_j <= sum_j eps_j`.

For `X_k~Gamma(k,1)`, define

`psi_k(R) := E[(X_k-R)_+]`.

### Lemma 7.1 — closed positive-part formula

For integer `k>=1`,

`psi_k(R)`
` = exp(-R) sum_{r=0}^{k-1} (k-r) R^r/r!`.                       (7.2)

#### Proof

The Erlang survival function is

`P(X_k>t)=exp(-t) sum_{m=0}^{k-1} t^m/m!`.

Hence by the layer-cake formula,

`psi_k(R)=int_R^infinity P(X_k>t) dt`.

For integer `m`, repeated integration by parts gives

`int_R^infinity exp(-t)t^m/m! dt`
` = exp(-R) sum_{r=0}^m R^r/r!`.

Summing over `m=0,...,k-1`, the coefficient of `R^r/r!` appears for exactly `k-r` values of `m`. This is (7.2). QED.

### Corollary 7.2 — quantitative pruning compiler

Under (7.1),

`0 <= E Q(F_I|_O)-E Q(F|_O)`
`   <= sum_{j in J} psi_{k_j}(R_j)`.                              (7.3)

This is a finite-block, dependence-valid error. Shared path edges only create dependence between the `eps_j`; (7.3) never factors their probabilities.

## 8. Ordered boundary greedy compression

In the rotated diagonal slab, index an input antidiagonal boundary consecutively by `0,...,M-1`. Consecutive boundary sources are joined inside the first interior layer by a two-edge zig-zag; therefore sources `q` indices apart admit a deterministic simple boundary-chain path with at most `2q` physical edges.

Fix integers `q>=1` and a gap `R>0`. Process sources in nondecreasing activation time. Retain a source unless an already-retained source `a` lies within index distance `q` and satisfies

`y_i-y_a >= R`.

If such an anchor exists, delete `i` and record that retained anchor.

### Corollary 8.1 — greedy `q,R` skeleton

The resulting retained set `I` has both properties:

1. every deleted source has a **retained** anchor at distance at most `q` and activation advantage at least `R`;
2. if two retained sources lie within distance `q`, their activation times differ by less than `R`.

Moreover, for the functional (6.1),

`0 <= E Q_I-E Q_full <= |J| psi_{2q}(R) <= M psi_{2q}(R)`.         (8.1)

#### Proof

Property 1 is built into the processing rule and remains valid because anchors are never deleted after being retained. For property 2, take retained `a,b` with `y_a<=y_b` and distance at most `q`. Source `a` was processed no later than `b`. If `y_b-y_a>=R`, source `b` would have been deleted using `a`, contradiction. The input-boundary chain gives a simple path of at most `2q` Exp(1) edges. Gamma variables are stochastically increasing in their integer shape, so Corollary 7.2 gives (8.1). QED.

This converts an arbitrary continuous activation profile into a skeleton whose nearby retained labels cannot have large jumps, while giving an explicit price for all removed peaks.

## 9. Exact width-48 numerical certificate — rigorous auxiliary delta

P20's current hard core uses `W=48`, hence `M=49` input labels, and its source-facing example uses `L=4` with Bellman threshold

`lambda_* = 4*0.6005646`
`         = 3002823/1250000`
`         = 2.4022584`.                                         (9.1)

The executed exact checker is

`artifacts/prob10_2026-09-20/PROB10-10/20260920T1448Z__source_domination_tail_exact.py`

creation commit `192ea8326a069bc6cad7d7e7ab1506f785ed5925`.

Executed output is

`artifacts/prob10_2026-09-20/PROB10-10/20260920T1448Z__source_domination_tail_exact.out`

creation commit `6df9b7bf98117367cc120593908338789b2bbcd5`.

The checker uses `Fraction` arithmetic for every sign. To upper-bound `exp(-R)`, it uses

`exp(R) > sum_{n=0}^{180} R^n/n!`,

so the reciprocal of that exact rational partial sum is a rigorous upper bound. It verifies:

- `M psi_8(35) < 1/1,500,000`, with exact-upper decimal `6.0167643558936115436995646000593459...e-7`;
- `M psi_12(40) < 1/200,000`;
- `M psi_16(50) < 1/2,000,000`;
- `M psi_20(57) < 1/2,000,000`.

Thus, for example, **all** sources that are at least `35` later than a retained source within four boundary indices can be removed simultaneously, even in the worst case of 49 deletions, while increasing the P20 block functional in expectation by less than

`6.666666666666666...e-7`.                                      (9.2)

For scale comparison only, the optional reserved target

`lambda_* - 1/1,500,000`
` = 18016933/7500000`
` = 2.402257733333333...`                                       (9.3)

is also checked exactly. This reserve is **not required** for correctness: because deleting sources increases `Q`, an exact pruned certificate below `lambda_*` is already a valid upper certificate for the full block. Equation (9.2) says additionally that the pruning itself cannot consume more than a microscopic amount of margin.

The output ends

`ALL_EXACT_CHECKS_PASS = True`.

## 10. Negation-first test: deletion is not free

The same exact checker records a deterministic finite counterexample to the stronger false statement that a delayed source can simply be removed with zero loss.

Take two sources `a,i`, activation times `y_a=0`, `y_i=35`; a realized anchor-to-`i` path of cost `36`; a continuation from `i` to one output of cost `1`; and a separate `a`-to-output route of cost `100`. Then

`F_full(o)=min(100,35+1)=36`,

while after deleting `i`,

`F_I(o)=min(100,36+1)=37`.

The source-domination error is

`eps_i=(0+36-35)_+=1`,

and the deletion loss is exactly `1`. The output therefore records

`ZERO_LOSS_DELETION_FALSE = True`

and

`TOY_DELAY_BOUND_ATTAINED = True`.

Because iid Exp(1) has positive density on every positive interval, neighborhoods of such a realized configuration have positive probability. The paid Gamma tail is not cosmetic; some quantitative error is genuinely necessary if one wants to know how conservative pruning is.

## 11. Combination with the already-proved finite-to-infinite compiler

The canonical 14:06Z report already proved the asynchronous-carry Bellman compiler. If a projected Bellman supersolution has block constant `lambda`, then for every number `N` of length-`L` bands,

`E T(0,(NL,NL))/(NL)`
` <= lambda/L + [h(Y_0)-inf h+W]/(LN)`,                           (11.1)

and consequently

`mu(1,1) <= lambda/L`.                                           (11.2)

The present theorem changes only how the finite Bellman expectation can be certified. For every profile box, one may greedily prune dominated high inputs, evaluate the smaller delayed-Richardson problem, and use

`Q_full <= Q_pruned`                                             (11.3)

for the rigorous one-sided Bellman bound. Equation (8.1) quantifies how much slack that reduction can lose.

Therefore the complete finite-to-infinite error remains explicit and unchanged: the term in (11.1). There is no new unpaid mixing, stationarity, or source-reset error.

If a finite cover of the projected profile core can now certify

`lambda < 4*0.6005646 = 2.4022584`                               (11.4)

for `L=4`, then (11.2) plus the retained axis lower bound proves `Delta_12>0`. That would still be only a one-pair **PARTIAL** result.

## 12. Before/after ledger

### Source-level

`c_*: 0 -> 0` for `Delta_12>=c_*`.

No global or restricted new strict-convexity direction is claimed.

### Rigorous mechanism delta

Before: high asynchronous sources could be deleted one-sidedly, but there was no quantitative theorem saying how much Bellman margin this could destroy.

After: Theorem 5.1 and Corollaries 7.2/8.1 give a samplewise global domination and exact Exp(1) pruning loss

`sum psi_k(R)`

without independence assumptions. For the active width-48 example, a `q=4,R=35` greedy deletion has worst-case expectation loss below `1/1,500,000`.

### Auxiliary/computational delta

The exact tail certificate and zero-loss counterexample were executed and archived. They are checks of the finite reduction, not sampled curvature and not source closure.

## 13. Remaining full-scope gap and next exact obligation

The immediate source-facing obligation is unchanged:

`Delta_12>0`, equivalently here it is sufficient to certify `mu(1,1)<0.6005646`.

The cleanest next block obligation is now narrower than in the preceding run:

1. apply the `q,R` skeleton to the width-48 projected profile core;
2. use P20's delayed-Richardson recursion only on the retained sources / unresolved smooth skeletons;
3. certify the weighted-corrector Bellman inequality at common `lambda<2.4022584` over the complete finite cover;
4. retain the exact finite-to-infinite correction (11.1).

The difficult residual profiles are those with no large locally dominated peaks: their retained labels vary by less than `R` over `q`-neighborhoods, so state explosion is no longer caused by arbitrarily high isolated activations. That is the precise new reduction. It does not yet prove that the remaining smooth-profile core is small enough to enumerate or that its Bellman residual is below threshold.

The Busemann/Jacquet alternative still has a different unpaid global rigidity step. Full strict convexity requires all noncollinear boundary directions even after the axis/diagonal checkpoint is solved, and source closure would additionally require independent validation under the repository contract.
