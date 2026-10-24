Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise. SOURCE METRIC NO MOVEMENT: rigorous `kappa=-1` bracket width `6.48139658710 -> 6.48139658710`. This is the sixth consecutive unchanged R14 PROB10 source-metric run. Three materially different attacks: (A) complete the `B->0` deformation asymptotics and try to falsify the branch; (B) reduce ambition to an interior `alpha=12.78` certificate; (C) homogenize the affine threshold into a fixed-latitude random-cone problem. Attack A succeeds as a rigorous obstruction: the previously identified scalar boundary seed cannot satisfy full stationarity.**

# PROB10-03 — R14 bounded iteration: boundary branch obstruction, adaptive alpha, fixed-latitude cone

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / SOURCE OPEN / NEW RIGOROUS OBSTRUCTION / NO RIGOROUS ENDPOINT MOVED**.

## 1. Contract, continuity, ownership, consumed state

I read and followed the current PROB10 contract and did not change scheduler state, cadence, notification state, permissions, email, Drive, workflows, or public resources.

Consumed before the new mathematics:

- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`;
- root `POSTED.md`, blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`;
- `operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`, blob `d8fe3a276b9c59d4608a113c0d77ba5b5dc8717d`;
- the already-preserved immutable Campbell refocus handoff `artifacts/prob10_2026-09-20/PROB10-03/20260919T2354Z_campbell_q18_r14_handoff.md`, retaining owner navigation point `3846db33296cfb6eea59ff7c488929087c7b62a2` and inherited `S=5`;
- newest prior R14 PROB10 report `runs/prob10_2026-09-20/PROB10-03/20260920T0405Z_r14_tail_entropy_polar_54b2.md`, blob `9c9086d9826c36332353195f77033e00d56f654f`;
- complementary NM13-03 T03 report `proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/2026-09-20__t03-closed-kernel-miranda-alpha12p75.md`, blob `cab9e7126ca5c5c27ee8641b0448437082742bae`;
- complementary NM13-07 T03 report `proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-moment-jacobian-broad-contraction.md`;
- R14 second-order artifact `artifacts/prob10_2026-09-20/PROB10-03/20260920T0251Z_r14_second_order_moment_face_reduction.md`;
- R14 tail/sign artifact `artifacts/prob10_2026-09-20/PROB10-03/20260920T0358Z_r14_tail_entropy_polar_reduction.md`.

The canonical Campbell claim still names R14. I did **not** overwrite that shared claim. This run is the owner-directed delimited PROB10-03 route already admitted by the immutable handoff.

## 2. Frozen source problem and rigorous metric

Freeze

`M=floor(alpha N)`, `g_a iid N(0,I_N)`, `||sigma||_2=sqrt(N)`,

`<g_a,sigma> >= -sqrt(N)` for every `a<=M`, fixed `alpha`, `N->infinity`.

A lower endpoint means SAT probability tends to one. An upper endpoint means SAT probability tends to zero.

Before and after this run:

`alpha_L = 6.30297437506`,

`alpha_U = 12.78437096216`,

`W = 6.48139658710`.

No ansatz, finite mesh, ordinary floating-point solve, or smaller-radius construction is entered into this metric.

## 3. Current source/scope check

The designated source distinctions remain material.

- El Alaoui--Sellke, `https://arxiv.org/abs/2010.15811`, studies the exact Gaussian spherical model, but its abstract explicitly describes the negative-margin FRSB structure as conjectural and returns a feasible point at radius `sqrt(qbar N)` with `qbar<1`, not the full-radius threshold.
- Stojnic, `https://arxiv.org/abs/1306.3980`, remains the older rigorous negative-margin upper-bound baseline.
- Stojnic, `https://arxiv.org/abs/2312.16531`, places the problem in stationarized fully lifted RDT. Its Theorem 1 explicitly requires the non-fixed lifting parameters to solve a stationarity system before the limiting comparison formula is invoked, and the paper states that practical operation requires substantial numerical work.
- Annesi--Malatesta--Zamponi, `https://arxiv.org/abs/2410.06717`, labels its transition computation a full-RSB ansatz.
- Winer--Herderschee, `https://arxiv.org/abs/2503.11761`, develops a jammed Parisi ansatz and reports threshold agreement, not a replacement rigorous full-radius theorem of the type needed here.

A bounded current search through 20 September 2026 found no later primary theorem plainly replacing the rigorous full-radius bracket above. This is dated negative evidence, not a worldwide priority certificate.

`POSTED.md` continues to distinguish the owner's posted zero-margin/Ising perceptron work from this continuous negative-margin spherical target.

## 4. Attack A — the `B->0` fallback is impossible for full stationarity

New proof artifact:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0453Z_r14_boundary_no_branch_latitude.md`

creation commit `c28f3772b056bc629f80805140bd0d2debf17a70`.

The previous R14 boundary analysis found a unique scalar `p_*` forced by the `D^2` reconstruction if a stationary branch had

`B->0`, `D->1`, `p->p_* in (0,1)`.

That was only one stationarity equation. This run evaluates the remaining residual at the same boundary and proves the two necessary conditions are incompatible.

Let

`u(x)=(x-1)_+`, `mu_1=E u(G)^2`,

`r_p(Z)=E[(sqrt(p)Z+sqrt(1-p)H-1)_+ | Z]`,

and

`V_p=E Var((sqrt(p)Z+sqrt(1-p)H-1)_+^2 | Z)`.

### New theorem

There is **no** sequence of complete-second-lift stationary points `(p_n,B_n,D_n)` with

`B_n->0`, `D_n->1`, `p_n->p_0 in (0,1)`.

The proof has two independent boundary equations.

First, the exact reconstruction

`D^2=K/[-4p^2B^2I_B]`

and dominated convergence give

`E[r_{p_0}^2]=p_0 mu_1`.                                       (4.1)

Using the Hermite weights of `u`, this equation has a unique interior root. The exact Mills-ratio certificate in this run sharpens its location to

`0<p_*<1/4`.                                                     (4.2)

Second, with `A_0=T_D/c_D`, symbolic algebra gives

`lim_{D->1} A_0(p,D)=(1-p^2)/4`.

Since

`d/dB(I-BI_B)=-B I_BB`,

`I_B(p,0)=-mu_1`, and `I_BB(p,0)=V_p`, the remaining stationary residual satisfies

`H/B^2 -> mu_1(1-p^2)-V_p/2`.

Hence full stationarity would additionally require

`V_{p_*}=2mu_1(1-p_*^2)`.                                     (4.3)

Write `phi=phi(1)`, `Q=P(G>1)`, `r=Q/phi`. The exact finite certificate proves

`13/20<r<33/50`.

For `W=(G-1)_+^2`,

`mu_1=2Q-phi=phi(2r-1)`,

`E W^2=10Q-6phi=phi(10r-6)`.

The upper Mills bound is exactly enough to give

`E W^2 < (15/8)mu_1`.

Since `V_p<=E W^2` and `p_*<1/4`,

`V_{p_*} < (15/8)mu_1 < 2mu_1(1-p_*^2)`,

contradicting (4.3).

Thus the earlier `B=0` scalar seed is **not false**, but it is only a necessary seed for the `D` equation and cannot launch a complete stationary branch. This closes that fallback route rigorously rather than spending another run perturbing it.

## 5. Exact finite checker

Checker:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0453Z_r14_boundary_no_branch_checker.py`

creation commit `22a37cfc46324e1f8aea050b8d977a31c0f2c64d`.

Archived executed output:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0453Z_r14_boundary_no_branch_checker.out`

creation commit `3ac9c837f48eca78674f3a40af507a97d26c39ca`.

The finite core is exact rational/SymPy arithmetic. It verifies:

- `A_0 -> (1-p^2)/4`;
- the rational Mills sandwich `13/20<r<33/50` using 400 right-endpoint cells and `(1-a/1000)^1000<e^{-a}`;
- the `p_*<1/4` Hermite inequality;
- the fourth-moment incompatibility;
- the frozen source bracket arithmetic.

The archived output ends `ALL_EXACT_CHECKS_PASS`. It was read back from its exact creation commit. This is a self-check, not an independent audit.

## 6. Attack B — smaller first endpoint movement at `alpha=12.78`

Since the boundary route is dead, I tested whether the interior certificate should first aim for a smaller rigorous improvement rather than `12.75`.

Using the already-proved closed one-dimensional kernel and exact two-scalar reconstruction, an ordinary numerical scout gives at `alpha=12.78`

`p ~= 0.6445929558545802`,

`B ~= 4.8607761199420505`,

`D ~= 0.6609587800306822`,

`Psi ~= 0.016259103550683496 >0`.

This is **NUMERICAL ONLY**. If outward-certified, it would improve the upper endpoint by only

`0.00437096216`,

but the larger objective margin and freedom to take a very small Newton/Kantorovich box may make the finite enclosure easier than the stronger `12.75` target. No endpoint is promoted here: the same directed compact-integral certification remains mandatory.

## 7. Attack C — exact fixed-latitude homogenization

As a category change, write `x=sigma/sqrt(N)` and set

`y=(x,1)/sqrt(2) in S^N`, `h_a=(g_a,1)`.

Then exactly

`||x||=1`, `g_a dot x>=-1 for all a`

if and only if

`y in S^N`, `y_{N+1}=1/sqrt(2)`, `h_a dot y>=0 for all a`.

Thus SAT is a **random homogeneous-cone intersection with one fixed latitude**.

This is not directly Wendel/Cover: `h_a=(g_a,1)` is neither centrally symmetric nor rotationally invariant in `R^{N+1}`, and the witness is restricted to one latitude. The reformulation therefore identifies a precise rank-one anisotropy rather than pretending the negative offset disappeared. It is a possible future conic/intrinsic-volume route, not a source endpoint.

## 8. Source metric versus mechanism movement

### Source metric

Before:

`alpha_L=6.30297437506`, `alpha_U=12.78437096216`, width `6.48139658710`.

After:

`alpha_L=6.30297437506`, `alpha_U=12.78437096216`, width `6.48139658710`.

**Movement: none.**

### Auxiliary movement

1. `B->0, D->1` continuation: **plausible fallback -> rigorously impossible for complete second-full stationarity**.
2. The old boundary scalar root: **necessary `D`-equation seed -> certified not to satisfy the second stationarity equation**.
3. Interior upper route: `12.75` remains the stronger candidate; `12.78` is recorded as a smaller potentially easier first rigorous movement, but is numerical-only.
4. Direct geometry: affine constraints -> exact fixed-latitude homogeneous-cone formulation with explicit rank-one anisotropy.

## 9. Remaining full-scope gap

The source-moving obligation remains an interior certificate:

1. directed compact evaluation of the closed one-dimensional Gaussian moment formulas on a small `(p,B)` box;
2. append the already-proved outer tails;
3. certify either a Newton/Kantorovich Jacobian enclosure or the monotone-face signs;
4. certify `Psi>0` at the true stationary root;
5. only then invoke the stationarized complete-second-lift source implication and move `alpha_U`.

The `B->0,D->1` route should not be revisited unless the limiting scaling itself changes. A future run should either attempt the smaller `12.78` rigorous box first or use the latitude-cone formulation with a genuinely rank-one-aware conic comparison; another perturbation of the now-excluded boundary branch would violate the changed-method contract.

Status remains **OPEN / PARTIAL**. No exact capacity, publication novelty, or independent validation is claimed.

```yaml
ledger_delta:
  worker: "R14 / PROB10-03"
  target: "negative-margin spherical Gaussian perceptron capacity at kappa=-1"
  status: "PARTIAL / OPEN"
  runtime:
    model: "GPT-5.6 Sol"
    reasoning: "UNVERIFIED"
    requested_gpt6_maximum_native_setting: "not configurable on exposed native scheduler surface"
  source_metric: "rigorous whp threshold bracket width alpha_U-alpha_L"
  before:
    alpha_L: "6.30297437506"
    alpha_U: "12.78437096216"
    width: "6.48139658710"
  after:
    alpha_L: "6.30297437506"
    alpha_U: "12.78437096216"
    width: "6.48139658710"
  source_movement: "none"
  unchanged_run_count_for_current_PROB10_refocus: 6
  obstruction_after_repeated_unchanged_runs: "the B->0,D->1 candidate satisfies a necessary D-equation at p_*, but the remaining H=0 equation would require V_p*=2 mu_1(1-p_*^2), contradicted by exact Mills/Hermite moment bounds"
  new_theorems:
    - "R14-T03-NO-B0-FULL-STATIONARY-BRANCH"
    - "R14-T03-FIXED-LATITUDE-HOMOGENIZATION (exact reformulation; no novelty claim)"
  numerical_only_candidate:
    alpha: "12.78"
    p: "0.6445929558545802"
    B: "4.8607761199420505"
    D: "0.6609587800306822"
    Psi: "0.016259103550683496"
    potential_upper_improvement_if_certified: "0.00437096216"
  artifacts:
    proof: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0453Z_r14_boundary_no_branch_latitude.md @ c28f3772b056bc629f80805140bd0d2debf17a70"
    checker: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0453Z_r14_boundary_no_branch_checker.py @ 22a37cfc46324e1f8aea050b8d977a31c0f2c64d"
    output: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0453Z_r14_boundary_no_branch_checker.out @ 3ac9c837f48eca78674f3a40af507a97d26c39ca"
  scheduler_changes: "none"
  external_actions: "GitHub authorized writes only; no email/Drive/public posting/permissions/workflow execution"
```
