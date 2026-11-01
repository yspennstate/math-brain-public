Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested, but no authenticated applied model/reasoning receipt is exposed, so I do not claim GPT-6.**

# P20 T10 — finite-target HJB flatness budget and a super-root disagreement compiler

Date: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.  
Canonical parent: `operations/claims/PROB10-10.md`.  
Model: nearest-neighbor **undirected** FPP on `Z^2` with iid physical-edge weights `Exp(1)`.  
Status: **PARTIAL / OPEN** for strict convexity. The theorem arguments below are complete modulo the cited classical mean-convergence theorem and are labelled `CANDIDATE_PROVED` pending later independent review.

## 1. Exact source, ownership, and original-problem metric

The exact source remains Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262v2, Question 4 in §2.5.1: show that for a continuous passage-time distribution the limit shape is strictly convex. The canonical repository target freezes the iid `Exp(1)` undirected nearest-neighbor `Z^2` special case. Directed integrable models and sampled numerical curvature do not settle this target.

Write `mu` for the deterministic time-constant norm and

`Delta_12 := 2 mu(e1) - mu(e1+e2) >= 0`.

The frozen source milestone is

`c_* := largest rigorously proved c >= 0 with Delta_12 >= c`.

- **before:** `c_*=0`;
- **after:** `c_*=0`.

So this run does **not** close even the axis/diagonal pair. The demonstrated gain is a new finite-volume variational reduction: under the hypothetical equality `Delta_12=0`, an exact two-target HJB residual budget along the actual axis geodesic is only `O(sqrt(n log n))`. Consequently P04 no longer needs a *linear* number of robust disagreement blocks merely to refute flatness: any block theorem whose certified disagreement energy is `omega(sqrt(n log n))` already forces `Delta_12>0`.

## 2. Essential dependencies and preserved failures

I consumed only the dependencies needed for the new argument:

1. `operations/PROGRESS20_2026-09-20.md` and the LIVE20 assignment pairing P20 with P04 on T10;
2. `operations/claims/PROB10-10.md` and root `POSTED.md` exclusions;
3. P20's preceding report `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T06-25-00Z__critical-chernoff-busemann-barrier.md`;
4. P04's newest report `proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T06-53-21Z__strip7-carry-cone1702.md`, creation commit `8f5af2d652f7eb049e0103b7c45666609cc9cfa8`, blob `8b39f7418367722ec65166be82de23bd380e032d`;
5. ADH Theorem 3.33, the classical Alexander/Kesten mean-convergence bound summarized in the source.

The R08 failure history remains binding:

- local detour gains can share one bypass, so independent local savings cannot simply be multiplied;
- a uniform pointwise finite-scale strict triangle saving fails on positive-probability cylinder events;
- old fixed-corner exact blocks did not reach the axis/diagonal threshold;
- fluctuation/KPZ information is not itself curvature.

The new argument avoids the first two failures because it defines one exact global residual from two finite target value functions and then decomposes that **same** residual along the actual optimizing geodesic. No independent-surgery multiplication and no pointwise strict-saving event are assumed.

## 3. Fresh source/literature boundary

Checked 2026-09-20. The ADH arXiv record remains v2 (23 September 2016), and Question 4 is still the source statement above. The same source's Theorem 3.33 gives, under `F(0)<p_c` and a finite second moment for the minimum of `d` edge weights,

`mu(x) <= E T(0,x) <= mu(x) + C (|x| log |x|)^(1/2)`

for `|x|>1`. `Exp(1)` satisfies these hypotheses.

A bounded fresh search recovered no theorem closing the exact iid Exp(1), undirected nearest-neighbor `Z^2` strict-convexity target. Dembin--Elboim--Peled's quantitative coalescence theorem assumes more than 32 extreme points of the limit shape, so it cannot be inserted under the flat/diamond contradiction hypothesis. Jacquet's strict unrestricted-versus-directed comparison is a different inequality. Recent lower bounds on non-random fluctuations do not imply directional curvature. Search misses are bounded negative evidence only; publication novelty and exhaustive worldwide openness remain **UNVERIFIED**.

## 4. A finite two-target Bellman field

Fix `n>=2` and set

`o=(0,0)`, `b_n=(n,0)`, `A_n=(n,n)`, `C_n=(n,-n)`.

For a finite target `z`, define its exact distance cocycle

`B_z(x,y) := T(x,z)-T(y,z)`.

For every oriented nearest-neighbor edge `(x,y)`, the triangle inequality gives

`B_z(x,y) <= tau_xy`,

so the target residual

`r_z(x,y) := tau_xy-B_z(x,y) = tau_xy+T(y,z)-T(x,z)`

is nonnegative.

Average the two opposing target cocycles:

`bar B_n := (B_{A_n}+B_{C_n})/2`,

and define the mixed residual

`q_n(x,y) := tau_xy-bar B_n(x,y) >= 0`.

Equivalently, with

`H_n(x):=[T(x,A_n)+T(x,C_n)]/2`,

we have the discrete HJB form

`q_n(x,y)=tau_xy+H_n(y)-H_n(x)`.

Define its path metric

`Q_n(x,y):=inf_gamma sum_{e in gamma} q_n(e)`.

### P20-FPP-FINITE-SYMMETRIC-HJB-25 — CANDIDATE_PROVED

For every `x,y`, samplewise,

`Q_n(x,y)=T(x,y)-bar B_n(x,y)`.

In particular,

`E Q_n(o,b_n)=2 h(n e1)-h(n(e1+e2))`,

where `h(x):=E T(0,x)`. Hence

`lim_{n->infinity} E Q_n(o,b_n)/n = Delta_12`.

#### Proof

For any path `gamma:x=x_0,...,x_k=y`, cocycle telescoping gives

`sum_i q_n(x_i,x_{i+1}) = sum_i tau_{x_i x_{i+1}} - bar B_n(x,y)`.

The second term is path-independent, so taking the infimum over paths gives

`Q_n(x,y)=T(x,y)-bar B_n(x,y)`.

For `x=o,y=b_n`, translation and lattice reflection give

`E B_{A_n}(o,b_n)
 = E T(o,A_n)-E T(b_n,A_n)
 = h(n(e1+e2))-h(ne1)`

and the same identity for `C_n`. Therefore

`E Q_n(o,b_n)
 = h(ne1)-[h(n(e1+e2))-h(ne1)]
 = 2h(ne1)-h(n(e1+e2))`.

Divide by `n` and use convergence of expected passage times to `mu`. QED.

This is a finite-volume Busemann/HJB object: no subsequential reconstructed Busemann limit and no coupling of two infinite-volume cocycles is required.

## 5. The Alexander flatness budget

Let

`a:=mu(e1)` and `d:=mu(e1+e2)`.

ADH Theorem 3.33 applies to Exp(1), so there is a finite distribution-dependent constant `C_A` such that for all sufficiently large `n`,

`0 <= h(ne1)-na <= C_A sqrt(n log n)`.

Also `h(n(e1+e2)) >= n d`, since the time constant is the infimum/asymptotic lower envelope of the expected metric.

Combining with the identity above gives

`E Q_n(o,b_n)
 = 2h(ne1)-h(n(e1+e2))
 <= n(2a-d)+2 C_A sqrt(n log n)`.

Thus:

### P20-FPP-ALEXANDER-FLATNESS-BUDGET-26 — CANDIDATE_PROVED

For all sufficiently large `n`,

`n Delta_12 >= E Q_n(o,b_n)-2 C_A sqrt(n log n)`.

In particular, under the contradiction hypothesis `Delta_12=0`,

`E Q_n(o,b_n) <= 2 C_A sqrt(n log n)`.

This is the main mechanism gain of the run. Previous P20 compilers sought a *linear* positive residual density directly. For the binary question `Delta_12>0`, that is unnecessarily strong: a super-`sqrt(n log n)` lower bound on this exact finite residual already contradicts flatness.

## 6. Local HJB curvature on the actual axis geodesic

Because Exp(1) is continuous, finite geodesics are unique almost surely. Let `Gamma_n` be the unique geodesic from `o` to `b_n`. Define the local mixed Bellman slack

`kappa_n(x):=min_{y~x} q_n(x,y) >= 0`.

Each single-target value function satisfies the Bellman equation

`min_{y~x} r_{A_n}(x,y)=0`,
`min_{y~x} r_{C_n}(x,y)=0`.

Moreover, away from its target, the zero-residual neighbor is exactly the first edge of the unique geodesic to that target. Since

`q_n=(r_{A_n}+r_{C_n})/2`,

we have the exact policy interpretation:

`kappa_n(x)=0`

if and only if the unique geodesics from `x` to `A_n` and from `x` to `C_n` have the same first edge. If those first-edge policies disagree, then `kappa_n(x)>0`.

The ordinary `T`-geodesic `Gamma_n` is also a `q_n`-geodesic because every path's `q_n`-cost differs from its passage time by the same endpoint cocycle. Therefore

`Q_n(o,b_n)=sum_{(x,y) in Gamma_n} q_n(x,y)`.

At every nonterminal vertex of `Gamma_n`, its selected outgoing edge has `q_n`-cost at least `kappa_n(x)`. Hence samplewise

`sum_{x in Gamma_n minus {b_n}} kappa_n(x) <= Q_n(o,b_n)`.

For `lambda>0`, let

`N_n(lambda):=#{x in Gamma_n minus {b_n}: kappa_n(x)>=lambda}`.

Then

`lambda N_n(lambda) <= Q_n(o,b_n)`.

Together with the Alexander budget this proves:

### P20-FPP-ROBUST-DISAGREEMENT-COMPILER-27 — CANDIDATE_PROVED

For every fixed `lambda>0` and all sufficiently large `n`,

`Delta_12 >= [lambda E N_n(lambda)]/n - 2 C_A sqrt(log n / n)`.

More generally, the same inequality holds with any deterministic `lambda_n>0` in place of `lambda`.

Consequently, if for some sequence `lambda_n>0`,

`lambda_n E N_n(lambda_n) / sqrt(n log n) -> infinity`,

then `Delta_12>0`.

Under the hypothetical flatness `Delta_12=0`, every fixed robust threshold obeys the quantitative avoidance law

`E N_n(lambda) <= (2 C_A/lambda) sqrt(n log n)`.

So flatness forces the axis geodesic to avoid all but `O(sqrt(n log n))` vertices where the opposing finite-target Bellman policies disagree by a fixed positive HJB margin.

## 7. Controlled-error handoff to P04

P04's newest seven-column carry-lane report gives an exact dependence-controlled block concatenation with disjoint physical-edge ownership and only a one-time endpoint repair. It also improves its restricted reflected cone to slope `851/500=1.702` and the exact axis upper bound to

`mu(e1) <= a_7 = 0.6049757734885347...`.

Those are genuine T10 advances, but the reflected-cone inequality itself is compatible with a diamond norm and therefore does not settle `Delta_12`.

The finite-HJB compiler above gives P04 a different block target. In a block decomposition of the actual `o`-to-`b_n` geodesic, suppose P04 can identify `G_n` visited blocks and certify a deterministic per-good-block mixed-HJB contribution `lambda_n`, with a total block/interface loss `E_n>=0`, such that samplewise or in expectation

`Q_n(o,b_n) >= lambda_n G_n - E_n`.

Then

`Delta_12 >= [lambda_n E G_n - E E_n]/n
             - 2 C_A sqrt(log n/n)`.

Therefore there are two useful modes:

1. **Strictness-only / contradiction mode.** It is enough that

   `lambda_n E G_n - E E_n = omega(sqrt(n log n))`.

   This already rules out `Delta_12=0`, even if `G_n/n -> 0`.

2. **Quantitative-defect mode.** If

   `liminf [lambda_n E G_n - E E_n]/n = eta>0`,

   then `Delta_12>=eta`.

The first mode is the new relaxation. P04 need not immediately prove positive-density disagreement. Any rigorously transferred `n^(1/2+epsilon)` number of fixed-size robust disagreement blocks, or a weaker count compensated by larger certified HJB margins, is enough for strictness.

The seven-column physical-edge-band architecture is well suited to this because it already solves the bookkeeping problem of dependence across adjacent blocks. What remains is mathematical rather than administrative: carry **two** boundary value profiles, for `A_n` and `C_n`, and lower-bound how often their Bellman minimizers separate on blocks actually visited by the axis geodesic.

## 8. A failed route diagnosed this run

I also tested the tempting infinite-volume shortcut: under `Delta_12=0`, take reconstructed Busemann fields with NE and SE supporting slopes, average them, and try to use positive stationary policy-disagreement density to force positive axis residual speed.

This does **not** by itself close the problem. A geodesic is selected adaptively and can in principle shadow a common calibrated `e1`-directed interface while avoiding most disagreement sites. Current unconditional bigeodesic/coalescence results do not exclude such an axis-boundary ray under a hypothetical flat face. Thus stationary spatial positivity of a local Busemann gap is not a pathwise lower bound. This is another form of the old shared-bypass obstruction.

The finite-target theorem above keeps the useful HJB curvature idea while replacing the unjustified density step by an exact budget on the **actual optimizing path**. It exposes the precise contradiction target: prove more than `sqrt(n log n)` robust opposing-policy energy along that path.

## 9. Supplementary exact sanity artifact

I executed an exact-rational finite-graph checker for the algebraic core. On a 45-vertex undirected rational-weight rectangle with opposing targets, it verifies:

- every oriented mixed residual `q` is nonnegative;
- the mixed residual path metric equals `T-bar B` exactly;
- the ordinary passage-time geodesic has total `q`-cost exactly `Q`;
- the sum of local `kappa` values along that geodesic is at most `Q`;
- `kappa=0` if and only if the two target first-step policies agree, at every checked nonterminal vertex.

The output ends

`P20-T10-FINITE-HJB-BUDGET-SANITY: ALL_EXACT_CHECKS_PASS`.

This is supplementary falsification/sanity evidence only, not an asymptotic FPP proof.

Artifacts:

- `proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T07-12-00Z__finite_hjb_budget_sanity.py` @ creation commit `411c00a1d17536a9482b550fb0971cd2c03364eb`;
- `proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T07-12-00Z__finite_hjb_budget_sanity.out` @ creation commit `17b3ce1e7ae4774b1eb65788bce1c511d96ffbb0`.

## 10. Residual obstruction and next attack

The residual obstruction is now narrower than in the preceding P20 runs:

> prove a super-`sqrt(n log n)` lower bound for the robust two-target HJB disagreement energy encountered by the **actual axis geodesic**, with block/interface losses smaller than that gain.

A linear-density theorem is sufficient but no longer necessary.

The next attack should use P04's disjoint seven-column physical-edge bands but enlarge the carried state from one lane label to a pair of normalized continuation profiles `(u^+,u^-)` for the opposing finite targets. In each visited band, reserve enough unrevealed physical edges to test whether the two Bellman minimizers separate. The first quantitative objective is deliberately weaker than positive density:

`E[number of lambda-robust disagreement bands] >= n^(1/2+epsilon)`

for some fixed `lambda,epsilon>0`, or any equivalent estimate whose total certified HJB energy dominates `sqrt(n log n)`. If that fails because the two profiles become near-translates, the failure should be converted into a deterministic profile-coalescence statement and propagated to the incompatible upper/lower terminal boundary data.

This is materially different from another Chernoff-cone refinement: the outer-cone constants are no longer the bottleneck.

## 11. Short cyclic-interval handoff

The displaced P20 cyclic-interval work remains preserved and is not reopened here. The source-literal proof candidate `P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01` and its finite sanity artifact remain on record. P26's full-proof/source-quantifier audit `P26-AUDIT-P20-CI241-SEMICIRCLE-MAJORITY-41` remains PASS; the last recovered certification state still lacked the second genuinely distinct non-P20/non-P26 audit. No completed certification, public posting, or publication-novelty claim is implied. This run spent no research effort waiting for that audit.

## 12. ledger_delta

```text
P20 | T10 Exp(1) undirected Z2 FPP strict convexity | full source OPEN -> OPEN/PARTIAL; axis/diagonal c_* 0 -> 0 | NEW CANDIDATE_PROVED P20-FPP-FINITE-SYMMETRIC-HJB-25: exact opposing-target mixed residual Q_n has E Q_n=2h(ne1)-h(n(1,1)) and Q_n/n -> Delta_12 | NEW CANDIDATE_PROVED P20-FPP-ALEXANDER-FLATNESS-BUDGET-26: Delta_12 >= E Q_n/n - 2 C_A sqrt(log n/n), hence flatness forces E Q_n=O(sqrt(n log n)) | NEW CANDIDATE_PROVED P20-FPP-ROBUST-DISAGREEMENT-COMPILER-27: Delta_12 >= lambda E N_n(lambda)/n - 2 C_A sqrt(log n/n); any certified HJB disagreement energy omega(sqrt(n log n)) rules out flatness | mechanism gain: P04 strictness target relaxed from linear robust-disagreement density to super-root total disagreement energy, while linear density still gives an explicit positive defect | newest P04 input: strip7 carry-lane report @ 8f5af2d652f7eb049e0103b7c45666609cc9cfa8, axis upper 0.6049757734885347 and reflected cone slope 851/500 retained as complementary restricted progress | exact sanity PASS artifacts @ 411c00a1d17536a9482b550fb0971cd2c03364eb + 17b3ce1e7ae4774b1eb65788bce1c511d96ffbb0 | residual obstruction: super-root robust opposing-policy energy along adaptive axis geodesic | next: two-profile reserved-edge extension of P04 seven-column bands, or profile-near-translate propagation if disagreement count fails | cyclic interval proof preserved; P26 PASS; second distinct audit last known missing; no closure claim | shared POSTED/RESULTS/QUEUE and canonical claim untouched
```

No historical or peer file was overwritten. No shared claim/POSTED ledger, email, Drive object, public post, workflow, permission, paid compute, access setting, or schedule was changed.

END OF P20 FPP RUN REPORT
