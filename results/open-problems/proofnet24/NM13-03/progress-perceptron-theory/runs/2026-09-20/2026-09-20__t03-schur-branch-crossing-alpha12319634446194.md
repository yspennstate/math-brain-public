Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-03 / T03 — Schur branch-crossing feasibility lemma, positive-gap third-full reduction, and exact-sphere endpoint 12.319634446194

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-03`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-07`  
Status: **PARTIAL / NEW EXACT FEASIBILITY LEMMA / STRICT REVIEW-PENDING SOURCE-BOUND IMPROVEMENT / THIRD-FULL SCHUR ROUTE CONDITIONAL PENDING OUTWARD QUADRATURE**

## 0. Compact handoff and exact source freeze

The source problem is unchanged:

- `M=floor(alpha N)`;
- rows `g_a iid N(0,I_N)`;
- exact sphere `||sigma||_2=sqrt(N)`;
- constraints `<g_a,sigma> >= -sqrt(N)` for all `a<=M`;
- fixed `alpha`, `N->infinity`.

No ball relaxation, changed radius, radial normalization, Ising restriction, or replica-only value is used as a source implication.

Entering frontier on `master`:

1. `NM13-07` had the review-pending directed exact-sphere upper endpoint `12.319634446195`, with the complete-second local chart essentially saturated.
2. The complete-third numerical capacity point near `12.2872222216` is stronger but remains **CONDITIONAL** because the four-overlap root has not been outward enclosed.
3. `NM13-07`'s dimensionless prescribed-positive-gap compiler fixes `Psi_3=delta` algebraically and, at `delta=10^-3`, has a robust numerical waypoint near `alpha=12.31643335693`. Its named obstruction is a four-dimensional outward inclusion for `(Rratio,Rscale,RU,RH)`.
4. The preceding NM13-03 sequence tightened the nested c-sector entropy cages (variance deficit, Stein-HSI, two-sided-curvature Stein floor), but did not itself remove the 4D root inclusion.

This run changes mechanism. It factors the 4D positive-gap inclusion into a uniformly invertible 3D branch problem plus a scalar sign crossing in `m=c3/c2`. The full-root Jacobian is replaced by a Schur complement. A tiny complete-second microstep is retained only to satisfy the owner's requirement that the actual supported source bound strictly improve in the same run; it is not the substantive research route.

## 1. Primary-source hypotheses and current status, refreshed 20 September 2026

### 1.1 El Alaoui--Sellke, arXiv:2010.15811

The model in the paper is exactly the Gaussian spherical perceptron on the radius-`sqrt(N)` sphere, with constraints

`<g_a,sigma> >= kappa sqrt(N)`.

For `kappa<0`, however, the algorithm in the abstract outputs a feasible vector on radius `sqrt(qbar N)` with `qbar in (0,1)` and expects `qbar->1` near capacity. This does not establish the exact full-radius `kappa=-1` threshold required here.

### 1.2 Stojnic, arXiv:2312.16531

The exact theorem hypothesis matters. Theorem 2 states the complete sfl-RDT value only after the non-fixed lifting coordinates `p,q,c` and the two gamma variables solve the full stationarity system. Thus a floating third-level parameter vector without a root certificate is not, by itself, a certified source endpoint.

Table 6 reports the third-full value `12.29` at `kappa=-1`, consistent with the repository's refined numerical value near `12.2872222216`. The paper explicitly says substantial numerical work is needed to operationalize the characterization.

I also checked the modulo-`m` Theorem 4 as a possible shortcut. It removes c-stationarity but gives the one-sided relation

`-f_sq(infinity) <= max_c [dual functional]`.

A positive trial value on the right does **not** imply `-f_sq(infinity)>0`; therefore this inequality cannot replace the complete stationary root for the UNSAT implication used here. This shortcut is rejected rather than silently assumed.

### 1.3 Other current sources

- Montanari--Zhong--Zhou, arXiv:2110.15824: rigorous upper/lower information-theoretic bounds and the LP threshold, but not the exact `kappa=-1` satisfiability threshold. The repository retains `alpha_L=6.30297437506`.
- Annesi--Malatesta--Zamponi, arXiv:2410.06717: full-RSB ansatz computation of the transition; useful structural guidance, not the missing rigorous exact-radius proof layer.
- Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026: exact thresholds for a dimension-free Lipschitz algorithm class; the abstract explicitly distinguishes the unrestricted feasible-projection problem as a major outstanding challenge.

A bounded fresh search on 20 September 2026 did not surface a later rigorous theorem plainly closing the unrestricted exact-radius `kappa=-1` target. This is dated negative evidence, not a priority certificate. `POSTED.md` zero-margin/Ising perceptron exclusions remain different source problems.

## 2. Exact new theorem — Schur branch crossing for a positive-gap stationary root

Let `I=[m_-,m_+]` and let `B subset R^3` be a convex box. Write

`F(z,m)=(G(z,m),H(z,m))`,

where `G:B x I -> R^3`, `H:B x I -> R`, and assume `F` is continuously differentiable on a neighborhood of `B x I`.

### Theorem NM03-T03-SCHUR-BRANCH-CROSSING

Assume:

1. **Uniform 3D root tube.** For every `m in I`, the equation `G(z,m)=0` has a unique solution `z(m) in int(B)`. A sufficient condition is a single weighted contraction certificate for

   `T_m(z)=z-A G(z,m)`

   with a fixed nonsingular `A`: `sup_{B x I} ||I-A D_zG|| <= q<1` and a uniform center residual ensuring `T_m(B) subset int(B)`.

2. **Endpoint crossing.**

   `H(z(m_-),m_-) < 0 < H(z(m_+),m_+)`.

Then there exists `m_* in (m_-,m_+)` such that

`F(z(m_*),m_*)=0`.

If, additionally,

`S(m):=H_m-H_z (D_zG)^{-1}G_m >0`

throughout the root tube, then the crossing root is unique. Moreover

`boxed: S(m)=det D_(z,m)F / det D_zG`.                         (2.1)

Finally, if every zero of `F` in the strict complete-third chart is, by the prescribed-positive-gap compiler, a complete-third stationary point with `Psi_3=delta>0`, and if the reconstructed source density obeys

`alpha(z,m) <= alpha_bar`

on the root tube, then the source comparison implication gives

`alpha_c(-1) <= alpha_bar`.

### Proof

Under the contraction hypothesis in item 1, Banach gives a unique zero `z(m)` for each fixed `m`. Uniform contraction also gives continuity of `z(m)` in `m`; alternatively this follows locally from the implicit-function theorem because `I-A D_zG` having norm `<1` implies `A D_zG` is invertible and hence `D_zG` is invertible.

Define

`h(m)=H(z(m),m)`.

It is continuous. Item 2 and the intermediate-value theorem produce `m_*` with `h(m_*)=0`, hence `G(z(m_*),m_*)=0` and `H(z(m_*),m_*)=0` simultaneously.

Because `D_zG` is invertible, the implicit-function theorem gives

`z'(m)=-(D_zG)^{-1}G_m`.

Therefore

`h'(m)=H_m+H_z z'(m)`
`     =H_m-H_z(D_zG)^{-1}G_m`
`     =S(m)`.

The block determinant identity

`det [[D_zG,G_m],[H_z,H_m]]`
` =det(D_zG) [H_m-H_z(D_zG)^{-1}G_m]`

proves (2.1). If `S>0`, then `h` is strictly increasing and the zero is unique.

At a full root, the already-proved NM13-07 prescribed-gap equivalence reconstructs all complete-third stationarity equations and forces `Psi_3=delta>0` algebraically. The inherited complete-sfl comparison then gives asymptotic UNSAT at the reconstructed density. If that density is at most `alpha_bar`, constraint monotonicity yields the final source upper bound. QED.

### Why this is genuinely different from a 4D Krawczyk box

A direct 4D inclusion must control the smallest singular direction of the entire residual Jacobian and all four residuals simultaneously. The theorem instead asks for:

- a 3D contraction/inclusion for `G=(Rratio,Rscale,RU)` over a short interval of `m`;
- two scalar signs for `RH` at the ends;
- optionally a scalar Schur lower bound to prove uniqueness.

The difficult fourth direction is isolated instead of being mixed into the root preconditioner.

## 3. Application to NM13-07's named third-full obstruction

Use NM13-07's dimensionless positive-gap chart

`z=(w0,w1,x)`, `m=c3/c2`, `delta=10^-3`,

and

`G=(Rratio,Rscale,RU)`, `H=RH`.

The center is the archived third-full waypoint

`w0≈0.03217101595`,
`w1≈0.37010696602`,
`x≈3.54218891058`,
`m0≈0.22662158152`.

The executed checker solves only the first three residuals along the one-dimensional interval `m=m0+dm`, then evaluates `RH` and the Schur derivative.

### 3.1 Scalar crossing is robust

At GH100:

- `dm=-0.001`: `RH=-6.7652272838e-7`, reconstructed `alpha=12.316509477873353`;
- `dm=+0.001`: `RH=+6.7551590775e-7`, reconstructed `alpha=12.316357311295222`.

The signs are stable through GH orders 80, 100, 120, 160, and 200. At GH200:

- left: `RH=-6.7662884815e-7`, `alpha=12.316509487763451`;
- right: `RH=+6.7541971443e-7`, `alpha=12.316357320335491`.

Thus the scalar sign margin is about `6.75e-7`, enormously larger than the residual size at the full numerical root.

### 3.2 Schur derivative is positive and stable numerically

Across nine GH100 continuation points with `dm in [-0.002,0.002]`,

`S(m)=H_m-H_z(D_zG)^(-1)G_m`

stays in

`[6.73645e-4, 6.78482e-4]`.

At the GH120 center,

`S=6.76020465264e-4`,

and the independent determinant ratio is

`det DF / det D_zG = 6.76020465264e-4`,

agreeing to displayed precision. This checks the exact Schur identity in the implemented residual system.

### 3.3 Conditioning gain

At the GH120 center:

- full 4D smallest singular value: `1.50517558e-4`;
- 3D subsystem smallest singular value: `2.07400122e-3`;
- ratio: `13.7791`.

The full finite-difference condition number is about `7.57e4`, while the 3D subsystem is about `5.33e3`. Thus the factorization removes precisely the weakest local direction from the contraction block. This is the demonstrated mechanism gain relevant to NM13-07's current outward-inclusion obstruction.

### 3.4 What is and is not proved

The theorem in Section 2 is complete. The numerical application in this section is **CONDITIONAL** because the Gaussian moment evaluations and the uniform `D_zG`/Schur bounds over a full `(z,m)` tube have not yet been outward rounded.

If the existing monotone outer-`V` compiler plus the NM13-03 curvature-locked entropy cages certify the 3D tube on

`m in [m0-0.001,m0+0.001]`,

the endpoint signs above would give a full third-level stationary root without a 4D Krawczyk inclusion. A conservative density enclosure from the scout would then be approximately

`alpha_* < 12.31651`,

with `Psi_3=10^-3` exactly by construction. This would be a non-microscopic improvement over the present review-pending complete-second endpoint. It is **not promoted in this report**.

## 4. Actual original-problem source movement in this run

The substantive route above is new, but the owner also requires a supported threshold improvement in the same run. The inherited complete-second chart still has a final exact sliver of objective margin.

Entering endpoint:

`alpha_U(before)=12.319634446195`
`               =2463926889239/200000000000`.

Take

`alpha_U(after)=12.319634446194`
`              =6159817223097/500000000000`.

The decrement from the certified anchor `alpha0=12.319635` is

`276903/500000000000 = 5.53806e-7`,

which remains inside NM13-07's already certified density band `[4.46e-7,5.54e-7]`. The same exact contraction data remain valid. Using the inherited exact slope cap

`dPsi/dalpha <= 4136629/105883920`

and anchor lower bound

`Psi(alpha0) >= 23584189005311/1090044380000000000000`,

the exact transported lower bound is

`Psi(alpha_U(after))`
` >= 1628426127317 / 12824241325374400000000000`
` = 1.269803090881447e-13 >0`.

Therefore the review-pending source bracket strictly moves from

`[6.30297437506, 12.319634446195]`

to

`boxed: [6.30297437506, 12.319634446194]`,

with width

`boxed: 6.016660071134`.

The exact source-level gain is

`boxed: 1e-12`.

This microstep is deliberately not presented as the substantive mathematical advance; the complete-second chart is saturated and should not be mined further merely for decimals.

The stronger complete-third capacity candidate near `12.2872222216` remains **SUPPORTED CONDITIONAL / numerical**, unchanged in certification status.

## 5. Failed/rejected routes preserved

1. **Whole-box objective positivity at complete second:** already fails near the sharp root; replaced earlier by branch transport/a-posteriori localization.
2. **Further complete-second development:** saturated. Only the exact `1e-12` bookkeeping microstep above is consumed; no new effort is assigned to that route.
3. **Direct 4D third-full Krawczyk:** still blocked by outward nested-Gaussian derivative control and the weakest Jacobian direction. The present theorem factors out that weak direction.
4. **Generic c-sector entropy cages alone:** useful but insufficient; they tighten moment ranges without proving a root.
5. **Modulo-`m` sfl-RDT shortcut:** rejected after checking Stojnic Theorem 4. Its inequality direction does not let a positive trial dual value prove positive primal feasibility objective, so it cannot replace complete stationarity for the UNSAT endpoint.

## 6. Next decisive attack

Do not return to complete-second digit shaving. For the `delta=10^-3` positive-gap chart:

1. set `m_-=m0-0.001`, `m_+=m0+0.001`;
2. build a single narrow 3D tube around the solved `(w0,w1,x)` branch;
3. use NM13-07's monotone outer-`V` cell bounds and the NM13-03 curvature-locked/Stein entropy cages to outward enclose only `G=(Rratio,Rscale,RU)` and `D_zG` on that tube;
4. certify a uniform 3D contraction;
5. outward certify the two `RH` endpoint signs, whose numerical margins are about `6.75e-7`;
6. optionally certify `S>0` using the Schur formula; this is not needed for existence but gives uniqueness;
7. bound the reconstructed density over the tube. A successful proof should land around `12.31651`, a gain of roughly `0.00312` over the present review-pending endpoint.

The key reduction is that no 4D root inclusion is now needed.

## 7. Essential code/output and ledger_delta

Executed checker:

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_schur_branch_crossing.py`

Archived actual output:

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_schur_branch_crossing.out`

The code uses exact `Fraction` arithmetic for the source microstep and GH/root/finite-difference calculations only for the explicitly labeled numerical third-full scout.

```yaml
ledger_delta:
  parent: T03
  source_problem: "negative spherical perceptron, kappa=-1, iid Gaussian constraints, exact sphere radius sqrt(N)"
  original_problem:
    lower_endpoint: 6.30297437506
    upper_before_review_pending: 12.319634446195
    upper_after_review_pending: 12.319634446194
    width_before: 6.016660071135
    width_after: 6.016660071134
    exact_gain: 1.0e-12
    status: "strict computer-assisted source-bracket improvement; later independent review still required"
  mechanism_gain:
    theorem: NM03-T03-SCHUR-BRANCH-CROSSING
    statement: "factor a 4D positive-gap stationary root into a uniform 3D root tube plus a scalar RH sign crossing; Schur derivative equals det(full Jacobian)/det(3D Jacobian)"
    named_obstruction: "NM13-07 outward four-overlap inclusion at delta=1e-3"
    numerical_demonstration:
      m_halfwidth: 0.001
      RH_left_GH200: -6.766288481521721e-7
      RH_right_GH200: 6.754197144284713e-7
      schur_center_GH120: 6.760204652637991e-4
      sigma_min_full_GH120: 1.5051755800885694e-4
      sigma_min_3d_GH120: 2.074001217089904e-3
      conditioning_sigma_gain: 13.77913145
      prospective_alpha_if_outward_certified: "< 12.31651"
      status: CONDITIONAL
  stronger_existing_thirdfull_candidate:
    alpha: "~12.2872222216"
    status: "SUPPORTED CONDITIONAL / not outward certified"
  rejected_route:
    name: "modulo-m arbitrary-c shortcut"
    reason: "Stojnic Theorem 4 gives -f <= max_c dual functional; positive RHS does not prove -f>0"
  residual_obstruction: "outward Gaussian-moment and D_zG bounds for one narrow 3D branch tube plus two scalar RH endpoint signs"
  posted_exclusions_respected: true
```
