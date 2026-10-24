Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-07 / T03 — pivoted x-branch nested-Schur cascade and endpoint 12.319634446193

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-07`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-03`  
Status: **PARTIAL / STRICT REVIEW-PENDING COMPUTER-ASSISTED SOURCE-BRACKET IMPROVEMENT / NEW EXACT NESTED-SCHUR REDUCTION / THIRD-FULL APPLICATION CONDITIONAL PENDING OUTWARD MOMENT ENCLOSURE**

## 0. Short handoff and exact source freeze

The source model is unchanged:

- `M=floor(alpha N)`;
- `g_1,...,g_M iid N(0,I_N)`;
- exact sphere `||sigma||_2=sqrt(N)`;
- constraints `<g_a,sigma> >= -sqrt(N)` for every `a<=M` (`kappa=-1`);
- fixed `alpha`, `N->infinity`.

No changed radius, ball relaxation, Ising restriction, radial renormalization, algorithmic-class threshold, or replica/FRSB-only number is used as a source implication.

The latest companion report

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/2026-09-20__t03-schur-branch-crossing-alpha12319634446194.md`

moved the repository-supported directed/review-pending complete-second endpoint to

`alpha_U=12.319634446194`.

My immediately preceding report

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-posgap-dimensionless-allmoment-alpha12319634446195.md`

proved a dimensionless four-overlap compiler for complete third-full lifting with prescribed `Psi_3=delta>0`, and supplied monotone outer-Gaussian endpoint/tail bounds for all five non-algebraic moment terms. At `delta=10^-3` its robust numerical waypoint is near

`alpha=12.31643335693`,

but that point remains **CONDITIONAL / NUMERICAL_ONLY** because the four-overlap root has not yet been outward enclosed.

The latest NM13-03 mechanism replaces a direct 4D Krawczyk inclusion by a 3D branch in `z=(w0,w1,x)` at fixed `m`, followed by a scalar `RH` crossing in `m`. That is a real improvement, but its 3D block still has a small singular value near `2.07e-3`. This run pivots the branch variable and then triangularizes the remaining 3D system into a nested scalar cascade.

## 1. Primary-source hypotheses and current proof status, refreshed 20 September 2026

### 1.1 El Alaoui--Sellke, arXiv:2010.15811

The paper's ambient model exactly matches the spherical geometry required here: iid standard Gaussian constraints on the radius-`sqrt(N)` sphere, with `<g_a,sigma> >= kappa sqrt(N)`. For `kappa<0`, however, the algorithm in the abstract assumes oracle access to the Parisi variational structure and outputs a feasible vector on radius `sqrt(qbar N)` with `qbar in (0,1)`; the authors expect `qbar->1` only near capacity. This is therefore not the exact full-radius threshold theorem required by T03.

### 1.2 Stojnic, arXiv:2312.16531

The paper fits the negative spherical perceptron into fully lifted RDT and states a capacity characterization through stationarized full lifting. The relevant exact hypothesis is that the non-fixed lifting coordinates solve the stationarity system before the complete-sfl expression is invoked. The paper also states that substantial numerical work is required to make the framework practically operational.

The companion checked the modulo-`m` Theorem 4 as a possible shortcut. Its one-sided inequality is of the form

`-f_sq(infty) <= max_c [dual functional]`.

A positive trial value on the right therefore does **not** imply positivity of the primal quantity on the left. This route cannot replace the missing complete stationary-root certificate for the UNSAT transfer used here.

### 1.3 Other rigorous and later work

- Montanari--Zhong--Zhou, arXiv:2110.15824: rigorous upper/lower interpolation-threshold bounds and a characterization of the linear-programming threshold, not the exact `kappa=-1` SAT/UNSAT threshold. The repository retains `alpha_L=6.30297437506` from this rigorous bracket layer.
- Annesi--Malatesta--Zamponi, arXiv:2410.06717: computes the transition under a full-RSB ansatz. It is structural guidance, not the missing rigorous exact-sphere certificate.
- Winer--Herderschee, arXiv:2503.11761: develops a jammed Parisi ansatz and matches prior threshold computations; again an ansatz-level statistical-physics calculation rather than a source-valid rigorous threshold proof.
- Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026: exactly characterizes a dimension-free-Lipschitz **algorithmic** projection-pursuit class and explicitly distinguishes the unrestricted non-algorithmic feasible-projection problem as still a major challenge.

A bounded fresh search on 20 September 2026 did not surface a later rigorous theorem plainly closing the unrestricted exact-radius `kappa=-1` target. This is dated negative evidence, not a novelty or priority certificate.

`POSTED.md` continues to exclude the owner's zero-margin/Ising perceptron work from duplicate research; it explicitly does not close the negative-margin continuous spherical target.

## 2. Source-threshold before/after — exact final bookkeeping sliver

The complete-second chart is already saturated and is not the substantive route in this run. There is nevertheless one remaining exact rational sliver inside its previously certified density band.

Entering endpoint:

`alpha_U(before)=12.319634446194`
`               =6159817223097/500000000000`.

Take

`alpha_U(after)=12.319634446193`
`              =12319634446193/1000000000000`.

The decrement from the inherited anchor `alpha_0=12.319635` is

`553807/10^12 = 5.53807e-7`,

which lies in the already directed-certified recentered range

`[4.46e-7,5.54e-7]`.

Using the inherited exact stationary-branch slope cap

`dPsi/dalpha <= 4136629/105883920`

and anchor lower bound

`Psi(alpha_0) >= 23584189005311/1090044380000000000000`,

the exact transport gives

`Psi(alpha_U(after))`
` >= 507336297612899/5770908596418480000000000000`
` = 8.791272451061869e-14 > 0`.

Thus, under the same source-matched stationarized complete-sfl transfer already used by the directed certificates, the repository-supported review-pending bracket strictly moves from

`[6.30297437506, 12.319634446194]`

to

`boxed: [6.30297437506, 12.319634446193]`,

with width

`boxed: 6.016660071133`.

The source gain is exactly `10^-12`. This is bookkeeping only. The complete-second route is exhausted and should not be mined further for decimals.

## 3. Exact theorem — nested Schur cascade

The substantive new mechanism is a general reduction of a difficult multidimensional inclusion into a sequence of one-dimensional branch certificates.

Let `F=(F_1,...,F_n)` be `C^1` on a rectangular domain, with variables ordered `x=(x_1,...,x_n)`. Let

`J_k = partial(F_1,...,F_k)/partial(x_1,...,x_k)`

be the leading `k x k` Jacobian block, and write `D_k=det J_k`, with `D_0=1`.

### Theorem NM07-T03-NESTED-SCHUR-CASCADE

Assume a branch is constructed successively as follows.

1. For every fixed `(x_2,...,x_n)` in the tail box, `F_1=0` has a unique root `x_1=phi_1(x_2,...,x_n)` in the interior of its interval.
2. After substituting `x_1=phi_1`, for every fixed `(x_3,...,x_n)`, the reduced equation `F_2=0` has a unique root `x_2=phi_2(x_3,...,x_n)`.
3. Continue inductively through stage `n-1`.
4. The final reduced scalar `f_n(x_n)` has opposite signs at the two endpoints of the final interval.

A sufficient way to certify uniqueness at each stage is to prove that the corresponding reduced derivative is bounded away from zero and that the two appropriate faces have opposite signs.

Then a full zero of `F` exists in the box. If every reduced derivative has a fixed strict sign, the full zero is unique within the nested branch tube.

Moreover, along the successively solved branch, the derivative at stage `k` is exactly

`boxed: s_k = D_k/D_{k-1}`.

Equivalently, `s_k` is the scalar Schur complement pivot obtained after eliminating the preceding `k-1` variables and residuals, and

`det DF = product_{k=1}^n s_k`.

### Proof

For `k=1`, the statement is ordinary one-dimensional implicit-function theory. Suppose stages `1,...,k-1` have been solved, yielding a `C^1` reduced branch in the remaining variables. Partition the leading `k x k` Jacobian as

`J_k = [[J_{k-1}, b],[c^T,d]]`.

Since the preceding stage derivatives are nonzero, `D_{k-1}!=0`, so `J_{k-1}` is invertible. Differentiating the first `k-1` solved equations with respect to `x_k` gives the induced response

`x'_{1:k-1} = -J_{k-1}^{-1} b`.

Therefore the derivative of the reduced `k`th equation is

`s_k = d-c^T J_{k-1}^{-1} b`.

The block determinant identity gives

`D_k = D_{k-1}(d-c^T J_{k-1}^{-1}b)`,

hence `s_k=D_k/D_{k-1}`. If `s_k` has fixed nonzero sign and the reduced residual has opposite signs on its two faces, the intermediate value theorem plus monotonicity gives a unique next-stage root. Induction constructs the branch through stage `n-1`; the final scalar sign crossing gives the full zero. Multiplying the determinant-ratio identities telescopes to `det DF=prod_k s_k`. QED.

The archived checker verifies the Schur identities symbolically for a generic `4 x 4` Jacobian before any floating calculation.

## 4. Application to the complete-third positive-gap system

Use the dimensionless prescribed-gap compiler from the preceding NM13-07 report at

`delta=10^-3`.

Instead of the companion ordering

- branch parameter `m`,
- solve `(Rratio,Rscale,RU)=0` in `(w0,w1,x)`,
- then cross `RH` in `m`,

use the pivoted ordering

**residuals** `(Rscale, RU, Rratio, RH)`,

**variables** `(w0, w1, m, x)`.

The nested program is therefore:

1. solve `Rscale=0` in `w0`;
2. on that branch solve `RU=0` in `w1`;
3. on that branch solve `Rratio=0` in `m`;
4. cross `RH=0` in the remaining scalar `x`.

At a full zero, the already proved positive-gap compiler reconstructs all complete-third stationarity equations and forces

`Psi_3=10^-3`

**exactly**. Thus the only remaining proof obligation is an outward branch/root certificate plus an outward source-density bound; objective positivity itself is algebraic.

## 5. Decisive conditioning calculation — why this pivot matters

All numbers in this section are **NUMERICAL_ONLY** Gauss--Hermite scouts, not directed proof claims.

At the archived `delta=10^-3` waypoint, GH160 gives for the companion 3D `m`-branch block

`smallest singular value = 0.0020740007270`,

`condition number = 5326.95`.

For the new fixed-`x` 3D block in `(w0,w1,m)`,

`smallest singular value = 0.0081933049563`,

`condition number = 1389.60`.

Hence the smallest singular value is larger by a factor

`3.95048`,

and the condition number is smaller by a factor

`3.83344`.

This is the demonstrated mechanism gain: the pivot removes most of the weak direction from the part that must be certified uniformly, before any interval preconditioning is attempted.

The four nested Schur pivots at the center are approximately

`s_1=-1.29777`,

`s_2=+3.06972e-2`,

`s_3=+1.47292e-1`,

`s_4=-1.55156e-4`.

Thus the weak direction is isolated in the **last scalar crossing**, where interval wrapping is least damaging.

## 6. Broad x-branch scout and robust sign margins

I solved the first three equations at nine values

`x=x_0+dx`, `dx in {-0.2,-0.15,...,0.2}`,

using GH160, and evaluated all four Schur pivots. Over this whole numerical sweep:

`-2.20119 < s_1 < -0.61240`,

`0.0250404 < s_2 < 0.0370707`,

`0.0840127 < s_3 < 0.205490`,

`-2.56622e-4 < s_4 < -1.16899e-4`.

The first 3D block retains

`smallest singular value >= 0.00337639`

through the sweep, with condition number at most about `1864`.

Most importantly, the final scalar residual crosses with a substantial margin:

at `dx=-0.2`,

`RH = +3.91165e-5`, `alpha = 12.31196366071`;

at `dx=+0.2`,

`RH = -2.67439e-5`, `alpha = 12.31940667954`.

These endpoint signs remain stable when the entire solve is repeated independently at GH orders `80,100,120,160,200`. The smaller absolute endpoint margin is about `2.67e-5`, roughly forty times larger than the companion `m0 +/- 0.001` scalar-crossing margin near `6.75e-7`.

The reconstructed density is numerically increasing across the swept x-branch; the finite-difference derivative remains positive and is at least about `0.0128`. I do **not** promote that derivative sign: it is only a scout. A directed proof can instead bound `alpha` directly on the certified branch tube.

The full numerical root remains near

`alpha=12.31643335693`,

and remains **CONDITIONAL / NUMERICAL_ONLY**.

## 7. What the pivot buys for the actual outward proof

A direct four-dimensional Krawczyk certificate couples the weakest direction to every moment/Jacobian interval. The companion Schur route improved that to a 3D inclusion plus one scalar crossing. The present cascade goes further:

- stage 1 needs only a sign-separated `partial Rscale/partial w0` and two `w0` faces;
- stage 2 needs only the first scalar Schur pivot for `RU` after eliminating `w0`;
- stage 3 needs only the next scalar Schur pivot for `Rratio` after eliminating `(w0,w1)`;
- stage 4 needs only two `RH` endpoint signs in `x`, with optional `s_4<0` for uniqueness.

Every stage can use the already proved NM13-07 monotone outer-`V` cell/tail bounds, while the c-sector pieces can additionally intersect NM13-03's variance-deficit / curvature / Stein-HSI cages. The important point is that the interval task is now **triangular**: one does not need an outward inverse of the full 4D Jacobian, and the smallest direction is tested only as a scalar sign.

A conservative numerical target for the first directed cascade is

`alpha_bar=12.31950`.

The GH80--GH200 right-end values are all below `12.319407`, leaving roughly `9.3e-5` of density slack to absorb directed quadrature and tube width. If the cascade and an outward tube bound `alpha<12.31950` are proved, the source endpoint would improve from `12.319634446193` by more than `1.34e-4`. This is **PROSPECTIVE, NOT PROMOTED**.

## 8. Failed/rejected routes preserved

1. **Complete-second decimal continuation:** exhausted. The `10^-12` source move in Section 2 is the final bookkeeping use of that chart, not a research route.
2. **Direct 4D third-full Krawczyk:** still mathematically valid but inefficient because the full Jacobian's weakest direction contaminates every enclosure.
3. **Companion fixed-m 3D branch:** a material improvement, but its branch block remains about four times worse conditioned than the new fixed-x block. It is retained as a fallback/cross-check.
4. **Modulo-m sfl-RDT shortcut:** rejected because Stojnic's one-sided Theorem 4 inequality has the wrong implication direction for certifying UNSAT from a positive trial value.
5. **Replica/full-RSB/jammed-Parisi values alone:** not source-valid rigorous closure for the exact-radius target.

## 9. Residual obstruction and next decisive attack

The new exact nested-Schur theorem is complete; the third-full application is still **CONDITIONAL** because its Gaussian moment and derivative evaluations have not yet been outward rounded on the entire nested branch tube.

Next attack, without returning to complete-second polishing:

1. Take `x in [x_0-0.2,x_0+0.2]` at `delta=10^-3`.
2. Use the monotone outer-`V` endpoint/tail compiler to outward enclose `Rscale` and `partial Rscale/partial w0`; certify a unique `w0` branch.
3. On that tube, outward enclose the two-by-two Schur pivot `s_2`; certify the `RU` crossing in `w1`.
4. Outward enclose `s_3`; certify the `Rratio` crossing in `m`.
5. Outward certify `RH(x_-) > 0 > RH(x_+)`; optionally prove `s_4<0` for uniqueness.
6. Directly outward bound reconstructed `alpha` on the final tube by `<12.31950`. This avoids needing a separate proof of `d alpha/dx>0`.
7. Once the robust `delta=10^-3` waypoint is certified, continue the same cascade toward the stronger NM13-03 conditional capacity branch near `12.2872222216`.

The numerics indicate that the new pivot is substantially less sensitive to wrapping than either the original 4D inclusion or the fixed-m 3D branch. The remaining work is a directed one-dimensional/nested-moment certificate, not a new conceptual stationarity reduction.

## 10. Executed artifacts and sanity checks

Created and executed:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_pivoted_x_schur_cascade.py`

creation commit:

`db8cae0055512e3991eb0aa407f73509857a5c18`

and archived output:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_pivoted_x_schur_cascade.out`

creation commit:

`b26d70c5a6655f9010fdd5f4e326b913e234c5e0`.

The exact section checks the rational source microstep and symbolic Schur determinant identities. The numerical section checks conditioning, the broad x-branch pivot signs, the final scalar crossing, and independent GH80--GH200 endpoint stability. It ends

`ALL_EXACT_AND_NUMERICAL_CASCADE_CHECKS_PASS`.

The distinction is essential: the exact rational/symbolic claims are proof ingredients; ordinary Gauss--Hermite values are **NUMERICAL_ONLY** and are not promoted to a source theorem.

## 11. ledger_delta

```yaml
ledger_delta:
  target: T03_negative_spherical_perceptron_kappa_minus_1_exact_sphere
  source_model_changed: false
  source_bracket_before:
    lower: 6.30297437506
    upper: 12.319634446194
    width: 6.016660071134
  source_bracket_after:
    lower: 6.30297437506
    upper: 12.319634446193
    width: 6.016660071133
  source_gain_upper: 1.0e-12
  source_status: review_pending_directed_computer_assisted
  mechanism_gain:
    theorem: NM07-T03-NESTED-SCHUR-CASCADE
    third_full_order:
      residuals: [Rscale, RU, Rratio, RH]
      variables: [w0, w1, m, x]
    center_sigma_min_gain_vs_companion_3d: 3.95048
    center_condition_number_improvement: 3.83344
    endpoint_RH_margin_min_numerical: 2.674e-5
    prospective_alpha_bar_if_directed: 12.31950
    prospective_gain_not_promoted: 1.34446e-4
  complete_third_candidate:
    alpha: 12.31643335693
    psi3: 1.0e-3
    status: CONDITIONAL_NUMERICAL_ONLY
  stronger_companion_capacity_candidate:
    alpha_approx: 12.2872222216
    status: CONDITIONAL_NUMERICAL_ONLY
  residual_obstruction: outward_nested_scalar_branch_and_moment_enclosure
  next_attack: directed_x_branch_nested_schur_cascade_with_monotone_outer_cells_and_entropy_cages
  failed_routes_preserved:
    - complete_second_decimal_mining_saturated
    - direct_4d_krawczyk_weak_direction
    - modulo_m_inequality_wrong_implication_direction
  historical_or_peer_overwrite: false
  public_posting: false
  email_or_drive: false
  paid_compute: false
  schedule_or_access_change: false
```
