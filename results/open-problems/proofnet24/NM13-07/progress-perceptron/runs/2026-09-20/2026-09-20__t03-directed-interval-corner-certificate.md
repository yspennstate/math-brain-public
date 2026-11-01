Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-07 / T03 — directed interval quadrature and rigorous corner layer for the complete-second-lift `alpha=12.75` certificate

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-07`  
Owner policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-03` comparison / feasibility theory  
Status: **PARTIAL / SOURCE BRACKET UNCHANGED / NEW COMPUTER-ASSISTED INTERVAL CORNER CERTIFICATE**

## 1. Short handoff, exact source target, and why this run changes method

The two preceding NM13-07 T03 runs did not move the source bracket. They did, however, reduce complete second-full stationarity to two scalars `(p,B)` and then close its first Jacobian analytically through a tilted-moment compiler. The newest NM13-03 companion report subsequently proved a stationary-branch transport theorem and supported a much stronger numerical source candidate `alpha=12.33`, but correctly left it uncertified because the compact Gaussian data were not outward enclosed.

This is therefore the third consecutive NM13-07 T03 run with the same certified source metric entering the run. In accordance with the 20 September progress-first policy, I did **not** produce another symbolic derivative lemma. I executed a materially different attack: direct directed-interval enclosure of the one-dimensional Gaussian integrals, including an explicit quadrature remainder, at source-relevant parameter points.

The source model remains exactly

- `M=floor(alpha N)`;
- independent `g_a ~ N(0,I_N)`;
- `||sigma||_2=sqrt(N)` exactly;
- `<g_a,sigma> >= -sqrt(N)` for every `a<=M`;
- fixed `alpha`, `N -> infinity`.

Equivalently, with `x=sigma/sqrt(N)`, seek `x in S^{N-1}` satisfying `Gx>=-1`. No ball relaxation, smaller sphere, normalization after the fact, or replica-only endpoint is used as source progress.

## 2. Source status refresh

The primary-source hypotheses and status remain as follows.

1. **El Alaoui--Sellke, arXiv:2010.15811.** The model is precisely the iid Gaussian spherical perceptron on radius `sqrt(N)`. For `kappa<0`, their algorithm assumes oracle access to the Parisi/FRSB structure and outputs a feasible vector on radius `sqrt(qbar N)` with `qbar in (0,1)`, not a theorem at exact radius `sqrt(N)`. Their normalization therefore cannot be substituted for T03.
2. **Stojnic, arXiv:2312.16531.** The negative spherical perceptron is embedded into fully lifted / stationarized random duality theory. The paper explicitly notes that practical use of the full lift requires substantial numerical work and reports concrete finite-lift capacity values after such calculations. In this project those displayed floating-point values are not promoted to rigorous source endpoints until the stationarity and scalar Gaussian integrals are enclosed.
3. **Montanari--Zhong--Zhou, arXiv:2110.15824.** This is a rigorous source for upper/lower interpolation bounds and the linear-programming threshold; it does not identify the exact `kappa=-1` satisfiability threshold.
4. **Huang--Sellke--Sun, arXiv:2608.29416 (29 August 2026).** This gives exact *algorithmic* thresholds for a dimension-free Lipschitz algorithm class in high-dimensional projection pursuit and explicitly distinguishes the non-algorithmic feasible-projection problem as still open. It therefore does not replace the exact T03 threshold.

A bounded 20 September 2026 search did not locate a later rigorous theorem plainly replacing the exact full-radius `kappa=-1` bracket below. This is bounded negative evidence, not a worldwide priority or openness certificate. `POSTED.md` continues to distinguish the posted zero-margin / Ising perceptron work from this negative-margin continuous spherical problem.

## 3. Frozen source metric

Repository-supported rigorous bracket entering this run:

`alpha_L = 6.30297437506`,

`alpha_U = 12.78437096216`,

`W = 6.48139658710`.

**Before:** `[6.30297437506, 12.78437096216]`, width `6.48139658710`.

**After:** `[6.30297437506, 12.78437096216]`, width `6.48139658710`.

**Source movement: none.** I do not promote `12.75`, and still less the companion numerical `12.33`, before the remaining parameter-continuum step is proved.

## 4. Consumed exact complete-second-lift reduction

Retain the already-proved notation

`q=pD^2`,

`c=(1-D^2)/(D(1-p)(1-pD^2))`,

`B=c/(4 gamma)`,

and, with

`Y=sqrt(p) z+sqrt(1-p)H-1`,

`f_{p,B}(z)=E_H exp[-B(Y_+)^2]`,

`u(z)=log f_{p,B}(z)`,

`I=E_Z u(Z)`, `I_B=partial_B I`, `K=E_Z u_z(Z)^2`,

the complete interior stationary branch is reconstructed by

`D^2=K/[-4p^2B^2I_B]`,

`alpha=-c^2/[4B^2I_B]`,

and

`H(p,B)=I-BI_B-4B^2I_B A_0(p,D)=0`,

where `A_0=T_D/c_D`. The comparison value is

`Psi=T+cI/(4B^2I_B)`.

The first-Jacobian formulas from the preceding NM13-07 report express `H_p,H_B,alpha_p,alpha_B` through the same one-dimensional moment data `I,I_B,I_BB,K,K_B,K_p`.

## 5. New computer-assisted theorem: fixed-parameter Gaussian data with explicit quadrature remainder

### Lemma NM07-T03-DIRECTED-POINT-ENCLOSURE

Fix an interior parameter point `(p,B)` in the coarse domain

`3/5 < p < 2/3`, `0 < B < 5`.

For each scalar Gaussian quantity among

`I, I_B, I_BB, K, K_B, K_p`,

the closed `J_0,...,J_4` kernel from the preceding reports gives a smooth one-dimensional integrand in `z`. On every interval `[a,b] subset [-9,9]`, two-point Gauss--Legendre has the exact remainder form

`int_a^b h(z) dz`
` = (b-a)/2 [h(m-(b-a)/(2sqrt(3)))+h(m+(b-a)/(2sqrt(3)))]`
`   + (b-a)^5 h^(4)(xi)/4320`

for some `xi in (a,b)`.

The executable artifact propagates a fourth-order Taylor jet in `z` with interval coefficients through the closed operations `exp`, `log`, `sqrt`, `Phi`, and the moment recurrence. Hence it interval-encloses `h^(4)` on each quadrature cell and therefore encloses the compact integral on `[-9,9]` without relying on a floating-point Gauss--Hermite error guess.

For the Gaussian CDF it uses the integrated alternating Taylor expansion on bounded arguments and the integration-by-parts Mills expansion in the tails, bracketing by consecutive alternating truncations. Finally it appends the already-proved full-line `|z|>9` tail budgets from the R14 companion calculation:

`Tail(I)<3.0e-16`,

`Tail(I_B)<1.2e-16`,

`Tail(I_BB)<1.4e-14`,

`Tail(K)<6.4e-14`,

`Tail(K_B)<6.4e-11`,

`Tail(K_p)<4.8e-13`.

All deterministic reconstruction after these six enclosures is performed by interval arithmetic in the exact algebraic formulas above.

This is a computer-assisted interval certificate, not a formal proof-assistant artifact and not an independent audit.

## 6. Sanity correction: shrink the old Miranda rectangle to stay inside the proved tail domain

The earlier NM13-03 numerical Miranda rectangle used

`p=p0+-0.004`, `B=B0+-0.15`

around

`p0=0.6457670646889506`, `B0=4.929229200895245`.

Its upper `B` corner is `5.079...`, outside the coarse `B<5` domain on which the inherited analytic `|z|>9` tail constants were proved. I therefore did **not** reuse that upper corner in the interval certificate.

Instead define the narrower valid rectangle

`R0=[p0-0.0015,p0+0.0015] x [B0-0.055,B0+0.055]`.

Its entire `B` range lies below `5`, and all three certified points below lie inside the inherited tail theorem's parameter domain.

This correction is important: a certificate with a tail theorem used outside its hypotheses would not be source-valid.

## 7. Executed enclosures

The center was evaluated with 600 quadrature cells. The resulting intervals include

`H(p0,B0) in [-2.4401135048e-6, 2.4403352384e-6]`,

`alpha(p0,B0) in [12.749975514266, 12.750024384877]`,

`Psi(p0,B0) in [0.0151967288870, 0.0152052545199]`,

`H_B(p0,B0) in [0.000435681454, 0.000440131227]`,

`alpha_p(p0,B0) in [26.83310339, 26.83823530]`.

Thus the comparison value is rigorously positive at the fixed center, and the two desired monotonicity signs hold at the center itself.

At the **lower-left** corner of `R0`,

`p=0.6442670646889507`, `B=4.874229200895245`,

the interval computation proves

`H in [1.1913691974e-5, 1.6547584846e-5] > 0`,

`alpha in [12.758988783600, 12.759035884411] > 12.75`,

`Psi in [0.015514683775, 0.015522874556] > 0`,

`H_B in [0.000440239019,0.000444508865] > 0`,

`alpha_p in [26.90408480,26.90894362] > 0`.

At the **upper-right** corner,

`p=0.6472670646889506`, `B=4.9842292008952445`,

the interval computation proves

`H in [-1.7307553160e-5,-1.2167005088e-5] < 0`,

`alpha in [12.741709181890,12.741759895537] < 12.75`,

`Psi in [0.014904859511,0.014913734435] > 0`,

`H_B in [0.000431080712,0.000435718906] > 0`,

`alpha_p in [26.76502737,26.77044825] > 0`.

The executable ends respectively

`CENTER_RIGOROUS_PASS`,

`LOWER_LEFT_VALID_RIGOROUS_PASS`,

`UPPER_RIGHT_VALID_RIGOROUS_PASS`.

These are substantially stronger than the prior ordinary floating-point corner scans: the two decisive corner sign pairs required by the monotone-face/Poincare--Miranda route are now outward enclosed at a rectangle satisfying the inherited tail hypotheses.

## 8. Why this does not yet move `alpha_U`

The exact monotone-face lemma used by the companion theory requires enough continuum control to extend the corner signs to all four faces; a sufficient condition is

`H_B>0` and `alpha_p>0`

throughout the relevant rectangle (indeed it is enough to prove the corresponding signs on the two `p`-faces and two `B`-faces). This run certifies those derivative signs at the center and the two decisive corners only.

A deliberately attempted naive interval evaluation with `(p,B)` replaced by the whole rectangle was decisively unusable: dependency/wrapping inflated the reconstructed `D,H,alpha` ranges to the point that `H` and its derivatives spanned both signs. This reproduces, in an executable way, the R14 diagnosis that ordinary product intervals destroy the correlations in the reconstructed stationary variables.

Therefore I do **not** infer a root merely from three points, and I do **not** claim the strict source endpoint `12.75` yet.

## 9. Mechanism movement versus source movement

### Original T03 threshold

Before: `[6.30297437506,12.78437096216]`, width `6.48139658710`.

After: `[6.30297437506,12.78437096216]`, width `6.48139658710`.

Movement: **none**.

### Demonstrated mechanism gain

Before this run, every complete-second-lift source candidate (`12.75`, and the companion transport candidate `12.33`) ultimately rested on ordinary quadrature at the point/corner layer; even the correct topological lemmas still lacked outward scalar Gaussian data.

After this run:

1. the compact one-dimensional Gaussian point evaluation has a reusable interval/Taylor quadrature engine with explicit fourth-derivative remainder;
2. `Psi>0` at the `12.75` center is outward enclosed;
3. a tail-domain-valid rectangle `R0` has the **two decisive corner pairs** outward certified with comfortable strict signs;
4. the remaining source-moving obligation is localized to **parameter-continuum correlation control**, not scalar Gaussian quadrature at isolated points.

This is a genuine proof-mechanism advance but not a threshold-bracket advance.

## 10. Residual obstruction and next attack

The next attack should preserve correlations in `(p,B)` rather than widen ordinary interval products. The most direct route is:

1. use the already-proved `J_0,...,J_6` second-order compiler to build a centered Taylor/affine model for `H_B` and `alpha_p` on the four faces of `R0`;
2. cover each face by small cells, evaluate the center data with the present fixed-point interval integrator, and bound the cell remainder from the explicit second derivatives rather than re-evaluating all reconstructed variables as unrelated intervals;
3. once the face monotonicity signs are enclosed, combine them with the two corner certificates above and the monotone-face lemma to obtain an actual `H=0`, `alpha=12.75` stationary point;
4. certify `Psi>0` on the resulting root box. The present center/corner margins are of order `1.5e-2`, so a relatively coarse rigorous Lipschitz bound should suffice once root localization is available.

A naive whole-box interval pass is now recorded as a failed recovery route and should not be repeated. The Taylor/affine face enclosure is materially different because it keeps first-order parameter correlations instead of discarding them.

## 11. Essential artifacts

Executed source:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_interval_gauss_fixedpoint.py`

current creation/update commit: `b3690166497969b4e4e3a7bee5280c2773b25c98`.

Archived executed output:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_interval_gauss_fixedpoint.out`

current creation/update commit: `9aff7dbaa5c0a06451ac1abee30d3faf59082e3a`.

No peer file, shared root ledger, schedule, permission, workflow, email, Drive object, paid resource, or public resource was modified.

```yaml
ledger_delta:
  worker: NM13-07
  parent: T03
  target: "negative spherical Gaussian perceptron, kappa=-1, exact radius sqrt(N)"
  status: "PARTIAL / SOURCE OPEN / NEW INTERVAL CORNER CERTIFICATE"
  runtime:
    model: "GPT-5.6 Sol"
    reasoning: "UNVERIFIED"
  source_metric: "rigorous whp threshold bracket width alpha_U-alpha_L"
  certified_before:
    alpha_L: "6.30297437506"
    alpha_U: "12.78437096216"
    width: "6.48139658710"
  certified_after:
    alpha_L: "6.30297437506"
    alpha_U: "12.78437096216"
    width: "6.48139658710"
    movement: "none"
  consecutive_own_source_metric_unchanged_runs: 3
  materially_different_attack_this_run: "directed interval Gaussian quadrature with explicit GL2 fourth-derivative remainder and analytic tails"
  mechanism_gain:
    center_Psi_lower: "0.015196728887035582"
    lower_left_H_lower: "1.191369197355185e-05"
    lower_left_alpha_lower: "12.758988783600488"
    upper_right_H_upper: "-1.2167005088136219e-05"
    upper_right_alpha_upper: "12.74175989553676"
    rectangle: "p0+-0.0015, B0+-0.055; entire B-range below 5"
  failed_route:
    naive_whole_parameter_box_intervals: "dependency/wrapping destroys signs; do not repeat"
  residual_obstruction: "rigorous parameter-continuum enclosure of H_B>0 and alpha_p>0 on the relevant faces, followed by Psi positivity on the true root box"
  next_attack: "facewise Taylor/affine enclosure using exact J0..J6 second derivatives plus fixed-point interval anchors"
  artifacts:
    code: "proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_interval_gauss_fixedpoint.py @ b3690166497969b4e4e3a7bee5280c2773b25c98"
    output: "proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_interval_gauss_fixedpoint.out @ 9aff7dbaa5c0a06451ac1abee30d3faf59082e3a"
```
