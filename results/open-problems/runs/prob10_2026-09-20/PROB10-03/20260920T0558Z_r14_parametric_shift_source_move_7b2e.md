Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not an authenticated configurable native setting. SOURCE METRIC MOVED: rigorous `kappa=-1` width `6.44702562494 -> 6.447025546689`; three attacks compared: (A) exact parametric contraction shift of the newly certified `12.75` box, (B) exact negation test for reusing that frozen box over a macroscopic density step, (C) larger-step stationary transport versus a fresh `12.33` endpoint box.**

# PROB10-03 — R14 bounded substantive iteration: parametric contraction shift

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / SOURCE OPEN / RIGOROUS UPPER ENDPOINT IMPROVED / INDEPENDENT FULL-SCOPE VALIDATION STILL PENDING**.

## 1. Contract, continuity, ownership, and consumed state

This run obeyed `operations/PROB10_2026-09-20.md`. It preserved the hourly task state and made no scheduler, notification, permission, workflow, email, Drive, or public-posting change.

Consumed before new mathematics:

- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`;
- root `POSTED.md`, blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`;
- `operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`, blob `d8fe3a276b9c59d4608a113c0d77ba5b5dc8717d`;
- preserved Campbell handoff `artifacts/prob10_2026-09-20/PROB10-03/20260919T2354Z_campbell_q18_r14_handoff.md`, retaining navigation point `3846db33296cfb6eea59ff7c488929087c7b62a2`;
- newest preceding R14 report `runs/prob10_2026-09-20/PROB10-03/20260920T0453Z_r14_no_b0_branch_adaptive_alpha_6d41.md`, blob `e0a3c850ab910e6f9312c47a16d7f99a5d7edeb8`;
- complementary NM13-07 report `proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-certified-alpha1275-contraction.md`, blob `0dfab2d6d35a8d865295efec5dcb092902732fca`;
- its executed directed-interval output `proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_alpha1275_interval_contraction.out`, blob `af96bf024333505e2f12dfcd194014bf948452b8`;
- complementary NM13-03 report `proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/2026-09-20__t03-stationary-transport-alpha1233.md`, blob `e9d006411e64e6cf38ee238aee3f1b7bd9b72ed6`;
- current primary-source scope: El Alaoui--Sellke arXiv:2010.15811; Stojnic arXiv:1306.3980 and arXiv:2312.16531; current follow-up Huang--Sellke--Sun arXiv:2608.29416.

The Campbell claim still names R14. I did not overwrite that shared claim. This is the owner-directed delimited PROB10-03 route already admitted by the immutable handoff.

## 2. Source/scope refresh and corrected entering metric

The exact source model remains

`M=floor(alpha N)`, iid `g_a~N(0,I_N)`, `||sigma||_2=sqrt(N)`,

`<g_a,sigma> >= -sqrt(N)` for every `a<=M`, fixed `alpha`, `N->infinity`.

A lower endpoint means SAT probability tends to one. An upper endpoint means SAT probability tends to zero.

The primary-source distinction remains essential:

- El Alaoui--Sellke's negative-margin construction uses conjectural FRSB/Parisi structure and outputs a feasible vector on radius `sqrt(qbar N)` with `qbar<1`; it is not the exact full-radius threshold theorem.
- Stojnic 2013 supplies rigorous negative-spherical comparison/upper-bound machinery.
- Stojnic 2023 places the negative model in stationarized fully lifted RDT and explicitly states that practical operation requires substantial numerical work.
- Huang--Sellke--Sun (submitted 29 August 2026) gives exact thresholds for a dimension-free Lipschitz algorithm class and explicitly separates this from the non-algorithmic feasible-projection problem.

A bounded 20 September 2026 primary-literature search found no later theorem plainly replacing the full-radius `kappa=-1` threshold problem. This is dated negative evidence, not a worldwide novelty certificate.

### Important consumed update

R14's previous report was stale as to the current source metric. NM13-07 has now completed the directed whole-box contraction certificate at `alpha=12.75` and its report explicitly transfers the certificate through the source-matched complete-second-lift theorem. Therefore this run enters with

`alpha_L = 6.30297437506`,

`alpha_U = 12.75`,

width `6.44702562494`.

I do not attribute NM13-07's certificate to R14 and do not rewrite its files.

## 3. Attack A — exact parametric contraction shift

New proof artifact, written before the checker:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0552Z_r14_parametric_contraction_shift.md`

creation commit `bf555fe3cc81290eb48e1bb733c174abc1c86565`.

The key observation is that changing the target density in the two-scalar stationary system changes only the constant term of the second residual.

Write

`F_0(p,B)=(H(p,B), alpha(p,B)-12.75)`.

For `delta>=0`, define

`F_delta(p,B)=(H(p,B), alpha(p,B)-(12.75-delta))`
`                =F_0(p,B)+(0,delta)`.

Thus

`DF_delta=DF_0` exactly.

The NM13-07 certificate already gives on its weighted box `Q`:

`q_* <= 23849/25000 = 0.95396`,

and

`Psi >= 0.0150497744619429886066833 >0`.

Using the archived center intervals, I sharpened the center residual ceilings without recomputing any Gaussian integral:

`|H(x_c)| <= 1.214e-12`,

`|alpha(x_c)-12.75| <= 1.203e-11`.

For the same exact preconditioner and radii, the deterministic contraction estimate allows every

`delta < 45299561313/578900000000000000`
`      = 7.82510991760235...e-8`.

Choose

`delta = 78251/10^12 = 7.8251e-8`.

Exact rowwise self-map bounds are

`eta_1 <= 0.031838746032`,

`eta_2 <= 0.046039942587`,

both strictly below

`1-q_* = 0.04604`.

The second-row slack is exactly

`57413/10^12 = 5.7413e-8 >0`.

Banach contraction therefore gives a unique genuine stationary zero inside the same already-certified box for

`alpha = 12.749999921749`.

Because `Psi>0` was certified on the **entire** box, it is positive at that shifted stationary zero. The same complete-second-lift source implication used by NM13-07 then yields asymptotic UNSAT at this exact density.

Hence

`alpha_c(-1) <= 12.749999921749`.

This is a rigorous source-level improvement, not a numerical candidate.

## 4. Exact checker and executed result

Checker:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0552Z_r14_parametric_contraction_shift_checker.py`

creation commit `852d663427fe025d7cafdf543f7eda6085915353`.

Archived actual output:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0552Z_r14_parametric_contraction_shift_checker.out`

creation commit `065ce6c47c45670d3ae8621a29e81d09c644e111`.

It uses exact `Fraction` arithmetic and verifies:

- exact `q_*` and the two weighted row constants;
- `delta<delta_max`;
- both shifted self-map coordinates are strictly below `1-q_*`;
- `alpha_U_new=12.749999921749`;
- width `=6.447025546689`;
- exact source-width gain `=7.8251e-8`.

The output ends

`ALL_EXACT_PARAMETRIC_SHIFT_CHECKS_PASS`.

This exact checker is a self-check of the new rational perturbation layer. It is not an independent audit of the NM13-07 interval quadrature or of the source theorem.

## 5. Attack B — exact obstruction to the tempting frozen-box shortcut

I tested the negation: can one obtain a meaningful step such as `12.70` simply by changing the target density while keeping the certified `12.75` box, preconditioner, radii and Jacobian enclosure unchanged?

No. The exact active-row calculation proves the maximum admissible decrement under those frozen ingredients is only

`delta_max = 7.82510991760235...e-8`.

Therefore the frozen-box shortcut cannot reach even `12.7499`, let alone `12.70` or `12.33`. Any larger source movement requires a new center/radii/preconditioner or a genuine branch-continuation argument. This is a certified obstruction, not a failed floating-point search.

## 6. Attack C — compare the two serious routes toward 12.33

### C1. Stationary-branch transport

NM13-03 proves the exact branch identity

`dPsi/da=(H_p Psi_B-H_B Psi_p)/(H_p alpha_B-H_B alpha_p)`

on a nondegenerate stationary branch and numerically supports the branch to `12.33`.

The rigorous NM13-07 anchor already has

`Psi(12.75)>=0.0150497744619429886066833`.

If a directed covering proves the conservative branch bound

`dPsi/da<=0.0354`,

then positivity would automatically persist down to approximately

`12.32486512819`,

so `12.33` is safely inside the objective-positive range. This route's missing theorem is therefore branch existence/nondegeneracy plus a directed derivative enclosure, not a new variational ansatz.

### C2. Fresh endpoint box at 12.33

NM13-03 also gives a supported endpoint center

`p~=0.6644028185445602`, `B~=6.1589540518255275`,

with positive supported `Psi` and a monotone-face rectangle. A newly centered interval-Newton/contraction certificate there would avoid certifying the whole branch. It is computationally more local than C1, but it requires a fresh directed Gaussian quadrature and Jacobian enclosure rather than reuse of the `12.75` artifact.

The current iteration does not promote `12.33`; ordinary quadrature remains numerical support only.

## 7. Source metric and auxiliary movement

### Source metric

Before this run, after consuming the newer NM13-07 update:

`alpha_L = 6.30297437506`,

`alpha_U = 12.75`,

width `6.44702562494`.

After this run:

`alpha_L = 6.30297437506`,

`alpha_U = 12.749999921749`,

width `6.447025546689`.

**Rigorous source-width movement: `7.8251e-8`.**

### Auxiliary movement

1. New exact theorem `R14-T03-PARAMETRIC-CONTRACTION-SHIFT`: a whole-box contraction certificate automatically certifies a quantitative interval of nearby density targets without recomputing the Gaussian integral.
2. Exact frozen-box continuation radius: `delta_max=7.82510991760235...e-8` for the current NM13-07 preconditioner/radii/error budget.
3. Larger-step diagnosis: the `12.33` target is not presently blocked by objective positivity; it is blocked by fresh directed branch/root certification.

## 8. Remaining full-scope gap

The exact asymptotic threshold is still unknown. Status remains **OPEN / PARTIAL**.

The next high-value source-moving step should not repeat the now-exhausted frozen-box perturbation. It should take one of two materially different routes:

- **fresh endpoint certification:** recenter the directed contraction engine at the supported `alpha=12.33` root and certify root existence plus `Psi>0` on one tiny box; or
- **branch certification:** cover `[12.33,12.75]` with overlapping tiny boxes, prove determinant nonvanishing/unique continuation, and outward-enclose the transport derivative.

No smaller-radius algorithmic result, restricted overlap ansatz, simulation, replica value, or unsupported numerical stationary point is counted as an endpoint.

```yaml
ledger_delta:
  worker: "R14 / PROB10-03"
  target: "negative-margin spherical Gaussian perceptron capacity at kappa=-1"
  status: "PARTIAL / OPEN / RIGOROUS UPPER ENDPOINT IMPROVED"
  runtime:
    model: "GPT-5.6 Sol"
    reasoning: "UNVERIFIED"
    gpt6_maximum_native_setting: "not configurable/authenticated on exposed runtime"
  source_metric: "rigorous alpha_U-alpha_L"
  before:
    alpha_L: "6.30297437506"
    alpha_U: "12.75"
    width: "6.44702562494"
  after:
    alpha_L: "6.30297437506"
    alpha_U: "12.749999921749"
    width: "6.447025546689"
  source_width_gain: "0.000000078251"
  new_theorem: "R14-T03-PARAMETRIC-CONTRACTION-SHIFT"
  exact_current_box_delta_max: "7.82510991760235e-8"
  strongest_neighbor_supported_candidate_not_promoted: "12.33"
  artifacts:
    proof: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0552Z_r14_parametric_contraction_shift.md @ bf555fe3cc81290eb48e1bb733c174abc1c86565"
    checker: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0552Z_r14_parametric_contraction_shift_checker.py @ 852d663427fe025d7cafdf543f7eda6085915353"
    output: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0552Z_r14_parametric_contraction_shift_checker.out @ 065ce6c47c45670d3ae8621a29e81d09c644e111"
  remaining_gap: "fresh directed certification at a materially lower density or a rigorously covered stationary branch; exact threshold remains unknown"
```
