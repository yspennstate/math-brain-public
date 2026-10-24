Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested, but no authenticated applied-model/reasoning-effort telemetry is exposed, so GPT-6/maximum is not claimed. SUBSTANTIVE MOVEMENT: the Lyons--Pemantle--Peres parent problem remains OPEN, but for the exact no-leaf family `P(nu=3)=1-p, P(nu=4)=p` a new mixture-localized escape-tilt criterion proves strict parent-bias decrease through `lambda=569/200=2.845` for every `p<=1/4`, and through `lambda=57/20=2.85` for every `p>=3/4`. On the new derivative segments the exact uniform margins are `-ell'_lambda >= 153509400000/49730949521317` and `>=93338400/58489590703`, respectively. No simulated sign is used.**

# NM13-05 T06 — mixture-localized branch-addition wedge for `{3,4}` offspring

Date: 2026-09-20.  
Repository: private `yspennstate/math-open-problems`, branch `master`.  
Own root: `proofnet24/NM13-05/progress-tree-speed`.  
Parent target: T06 / historical intake P0066, Lyons--Pemantle--Peres monotonicity of biased-walk speed on a supercritical Galton--Watson tree without leaves.  
Status: **PARTIAL / OPEN parent; NEW RESTRICTED THEOREM CANDIDATE pending later independent review.**

## 1. Compact handoff and exact continuity

The controlling owner instruction is `operations/PROGRESS20_2026-09-20.md`; the LIVE20 mapping assigns NM13-05 to T06 by escape-probability/regeneration coupling, complementary to P01's analytic regeneration-derivative route.

Historical P0066 remains `attempted_unsolved`. Its old route observed only that at a fixed `k`-child vertex the radial drift

`(k-lambda)/(k+lambda)`

decreases in the parent bias `lambda`. That does not control the `lambda`-dependent law of the environment seen by the walk, so the measure-change term remained unsigned. This failure is preserved.

The immediate predecessor is

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T05-25-22Z__mean-excess-escape-tilt-wedge.md`.

It extended the near-minimum-degree theorem to arbitrary finitely supported laws with small mean excess. Earlier NM13-05 work proved the branch-addition ratio for adjacent support and the parametric endpoint-defect wedge

`p<=delta or 1-p<=delta  =>  lambda<=d-delta`.

For the present `{3,4}` law and `p=1/4` or `3/4`, that wedge reaches only `lambda=11/4=2.75`.

A stronger inherited analytic adjacent-family criterion from the historical P03-A work is also consumed rather than rediscovered: for `{d,d+1}` and every mixture, exact optimization over an unrestricted tilted weight gives

`lambda a_d(lambda)<2d+1+2 sqrt(d(d+1))`.

For `d=3` its limiting root is approximately `2.8152423075`. The present run improves this **for substantial non-rare mixture ranges** by combining the dynamic sensitivity estimate with NM13-05's static branch-addition localization of the same tilted weight.

The latest complementary live P01 report consumed is

`proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T06-05-48Z__run-report.md`.

P01 now treats minimum offspring exactly one with no maximum-offspring bound. Its mechanism is an analytic covariance/compression argument. The present theorem instead keeps minimum degree three and uses a branch-addition coupling to localize the escape-tilted mixture before optimizing the derivative numerator.

The newest relevant PROB10-06 work was also checked. It records that differentiating the static branch-addition ratio in the desired direction is false in general and that a universal pathwise logarithmic-derivative ordering under branch addition is not available. Neither failed route is retried here.

`POSTED.md` / current repository search records no posted source-wide P0066 closure; restricted T06 results do not close the parent conjecture.

## 2. Frozen offspring assumptions and bias convention

Throughout this report,

`P(nu=3)=1-p,   P(nu=4)=p,   0<=p<=1`.                         (2.1)

There are no leaves and `E nu=3+p`.

Use **parent bias** `lambda`:

`P(parent | nu=k)=lambda/(lambda+k)`,
`P(each fixed child | nu=k)=1/(lambda+k)`.                      (2.2)

Larger `lambda` points toward the root, so the target derivative sign is

`ell'_lambda<0`.                                                 (2.3)

The Ben Arous--Fribergh--Sidoravicius **child bias** is reciprocal:

`beta=1/lambda`.                                                 (2.4)

Thus, wherever differentiable,

`v'(beta)=-ell'_{1/beta}/beta^2`.                               (2.5)

So every strict parent-bias derivative result below is a strict positive child-bias derivative result on the reciprocal interval.

## 3. Primary-source and current-literature recovery

Refreshed on 2026-09-20:

1. Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*. In child-bias notation its abstract proves `v(beta)` increasing for `beta>=717` on Galton--Watson trees without leaves.
2. He--Wang--Xiang, arXiv:1610.08151, later published in *Journal of Applied Probability* 62 (2025), 1044--1052. For minimum offspring `d>=2`, they prove strict parent-bias decrease for

   `0<=lambda<=d/(1+sqrt(1-1/d))`.                              (3.1)

3. Aidekon's speed representation supplies the exact effective-degree reduction used below; Bowditch--Tokushige supply differentiability/analyticity in the ballistic regime.
4. A bounded fresh search dated 2026-09-20 found the 2025 low-bias paper and the 2026 deterministic regular-tree paper, but no checked source-wide solution and no checked external theorem matching the mixture-localized `{3,4}` rectangles below. This is bounded negative evidence only, not a novelty certificate.

## 4. Parent problem before/after and source-level scope

### Parent problem

Before: **OPEN**.  
After: **OPEN**.

No theorem for every no-leaf offspring law on the full transient interval is claimed.

### Restricted-family scope before

For all `{3,4}` mixtures, the inherited exact adjacent-family criterion gives strict decrease while

`A_3(lambda)<7+4 sqrt(3)`,                                      (4.1)

where `A_3` is defined in Section 7. Its limiting root is approximately

`Lambda_all=2.8152423075...`.                                   (4.2)

This is stronger than the clean older `11/4` all-mixture corollary and is therefore the honest baseline for the two p-subranges treated below.

### Restricted-family scope after

### Theorem A — moderate lower-degree-dominant rectangle

If

`0<=p<=1/4`,                                                     (4.3)

then the parent-bias speed is strictly decreasing on

`0<=lambda<=569/200=2.845`.                                     (4.4)

Moreover, on the new derivative segment `1<=lambda<=569/200`,

`-ell'_lambda >= 153509400000/49730949521317 >0`.               (4.5)

Equivalently,

`v'(beta)>0  for  200/569<=beta<=1`.                            (4.6)

### Theorem B — moderate upper-degree-dominant rectangle

If

`3/4<=p<=1`,                                                     (4.7)

then the parent-bias speed is strictly decreasing on

`0<=lambda<=57/20=2.85`.                                        (4.8)

Moreover, on `1<=lambda<=57/20`,

`-ell'_lambda >= 93338400/58489590703 >0`.                       (4.9)

Equivalently,

`v'(beta)>0  for  20/57<=beta<=1`.                              (4.10)

Relative to the inherited all-mixture limiting endpoint (4.2), the two p-regions gain about `0.02976` and `0.03476` in parent bias, respectively. These decimal differences are context only; the theorem endpoints and margins are exact rationals.

## 5. Exact Aidekon reduction for `{3,4}`

Work on `1<=lambda<3`. Let `B` be the quenched probability of escaping to infinity before hitting the parent, and set `U=-dB/dlambda>=0`.

Conditional on current offspring count `k`, take iid copies `B_0,...,B_k` and corresponding `U_i`. Put

`S_k=sum_i B_i`,
`D_k=lambda-1+S_k`,

`c_k=E[(1/(k+1))*S_k/D_k]`,                                     (5.1)

`h_k=E[(1/(k+1))*sum_i(B_i+(lambda-1)U_i)/D_k^2]`.              (5.2)

Then `c'_k=-h_k`.

Set

`C=(1-p)c_3+p c_4`,
`theta=p c_4/C`,
`M=3+theta`.                                                      (5.3)

Aidekon's symmetrized formula reduces exactly to

`ell_lambda=(M-lambda)/(M+lambda)`,                              (5.4)

hence

`ell'_lambda=2(lambda M'-M)/(M+lambda)^2`.                       (5.5)

Also

`theta'=theta(1-theta) Delta`,                                  (5.6)

where

`Delta=h_3/c_3-h_4/c_4`.                                        (5.7)

Therefore the desired sign is equivalent to positivity of

`G:=M-lambda M'`
` =3+theta-lambda theta(1-theta)Delta`.                          (5.8)

## 6. Consumed escape-sensitivity estimate

The minimum-degree-three escape comparison used in the predecessor gives

`1-lambda/3 <= B <= 1-lambda/4`,
`0<=U<=B/(3-lambda)`.                                           (6.1)

Exactly as in the earlier `{3,4}` report, these imply

`h_3/c_3 <= 6/[(3-lambda)(9-lambda)]`,                           (6.2)

and, using `U>=0` together with the upper escape bound,

`h_4/c_4 >= 4/(16-lambda)`.                                     (6.3)

Hence

`Delta<=a_3(lambda)`,                                            (6.4)

where

`a_3(lambda):=6/[(3-lambda)(9-lambda)]-4/(16-lambda)`.          (6.5)

Put

`A_3(lambda):=lambda a_3(lambda)`.                               (6.6)

Then from (5.8),

`G>=F_lambda(theta)`                                             (6.7)

with

`F_lambda(theta):=3+theta-A_3(lambda) theta(1-theta)`.           (6.8)

## 7. New ingredient: localize the dangerous tilted weight before optimizing

The inherited NM13-05 branch-addition coupling proves

`4/5 <= t:=c_4/c_3 <=1`.                                        (7.1)

For completeness, the mechanism is the concavity of

`phi(s)=s/(lambda-1+s)`

for `lambda>1`: adding a fifth iid escape branch gives the lower ratio `4/5`, while averaging all five leave-one-out four-branch sums gives the upper ratio `1`.

Because

`theta=p t/(1-p+p t)`,                                           (7.2)

(7.1) gives the exact static localization

`BOX: 4p/(5-p) <= theta <=p`.                                   (7.3)

The previous all-mixture optimization discarded p and minimized over every `theta in [0,1]`. The present run keeps (7.3).

Define

`K(theta):=(3+theta)/[theta(1-theta)]`,  0<theta<1.             (7.4)

Then `F_lambda(theta)>0` exactly when

`A_3(lambda)<K(theta)`.                                          (7.5)

A direct derivative calculation gives

`sign K'(theta)=sign(theta^2+6 theta-3)`,                        (7.6)

so the unique minimizer is

`theta_*:=2 sqrt(3)-3=0.4641016...`,                             (7.7)

with

`K(theta_*)=7+4 sqrt(3)`.                                       (7.8)

Let

`p_*:=5 theta_*/(4+theta_*)=0.5198152...`.                       (7.9)

Then the exact p-localized threshold is

`K_p := min_{theta in [4p/(5-p),p]} K(theta)`

and hence

`K_p = K(p)`                          if `0<p<=theta_*`,
`K_p = 7+4 sqrt(3)`                   if `theta_*<=p<=p_*`,
`K_p = K(4p/(5-p))`                   if `p_*<=p<1`.             (7.10)

Thus:

### Proposition 7.1 — mixture-localized derivative criterion

For the exact law (2.1), if `1<=lambda<3` and

`A_3(lambda)<K_p`,                                               (7.11)

then `ell'_lambda<0`.

This is strictly stronger than the inherited all-mixture criterion except on the narrow central p-band `[theta_*,p_*]` where the branch-addition interval still contains the global dangerous weight.

This is the demonstrated mechanism gain of the run: **the static escape coupling identifies where the bias-dependent effective offspring weight is allowed to live, and only then is the dynamic derivative numerator optimized.** It is neither a simulation nor P01's support-wide covariance route.

## 8. Monotonicity of the sensitivity budget

To certify closed lambda intervals it suffices to check their right endpoint because `A_3(lambda)` is strictly increasing on `[1,3)`.

Indeed

`d/dlambda [6lambda/((3-lambda)(9-lambda))]`
` =6(27-lambda^2)/[(3-lambda)^2(9-lambda)^2]`,                  (8.1)

and

`d/dlambda [4lambda/(16-lambda)]`
` =64/(16-lambda)^2`.                                           (8.2)

For `1<=lambda<3`,

`6(27-lambda^2)/[(3-lambda)^2(9-lambda)^2] >= 27/64`,           (8.3)

while

`64/(16-lambda)^2 <=64/169`.                                    (8.4)

Therefore

`A_3'(lambda)>=27/64-64/169=467/10816>0`.                        (8.5)

## 9. Proof of Theorem A: `p<=1/4`

Since

`1/4<theta_*`,                                                   (9.1)

`K` is decreasing throughout the allowed low-p tilted interval. Thus for every `p<=1/4`, (7.3) implies

`K(theta)>=K(1/4)=52/3`.                                        (9.2)

At

`L_-=569/200`,                                                   (9.3)

the exact checker gives

`A_3(L_-)=1709592364/100401591`,                                (9.4)

and

`52/3-A_3(L_-)=10233960/33467197>0`.                            (9.5)

By Section 8 this inequality holds for every `1<=lambda<=L_-`; hence Proposition 7.1 gives strict derivative negativity on that whole interval.

For the explicit uniform margin, `theta<=1/4`, and because `A_3(L_-)>2`, the quadratic (6.8) is decreasing on `[0,1/4]`. Therefore

`G>=F_{L_-}(1/4)=3837735/66934394`.                              (9.6)

Also

`M+lambda<=13/4+569/200=1219/200`.                              (9.7)

Substituting into (5.5) yields exactly

`-ell'_lambda`
` >=153509400000/49730949521317>0`.                             (9.8)

Finally, He--Wang--Xiang's published interval for minimum degree three extends past `lambda=1`, so stitching proves strict monotonicity on all of `[0,L_-]`.

## 10. Proof of Theorem B: `p>=3/4`

From (7.3),

`theta>=4p/(5-p)>=12/17`.                                       (10.1)

Since `12/17>theta_*`, `K` is increasing throughout this allowed high-p interval. Thus

`K(theta)>=K(12/17)=357/20`.                                    (10.2)

At

`L_+=57/20`,                                                     (10.3)

the exact value is

`A_3(L_+)=190532/10783`,                                        (10.4)

and

`357/20-A_3(L_+)=38891/215660>0`.                               (10.5)

Again Section 8 promotes this endpoint inequality to the whole interval `[1,L_+]`.

For the uniform derivative margin, on `theta>=12/17>1/2`,

`dF/dtheta =1+A_3(lambda)(2theta-1)>0`,                           (10.6)

so the minimum occurs at `theta=12/17`. Hence

`G>=F_{L_+}(12/17)=116673/3116287`.                             (10.7)

With

`M+lambda<=4+57/20=137/20`,                                     (10.8)

(5.5) gives

`-ell'_lambda`
` >=93338400/58489590703>0`.                                    (10.9)

The published low-bias theorem again covers the lower lambda segment, completing strict monotonicity on `[0,L_+]`.

## 11. Exact checker and what it does not prove

The executed exact-rational checker is

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T06-22-00Z__mixture-localized-adjacent-check.py`.

Its archived actual output is

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T06-22-00Z__mixture-localized-adjacent-check.out`.

The output ends

`ALL_EXACT_CHECKS_PASS`.

The checker verifies the rational endpoint inequalities, exact margins, and the positive lower bound `467/10816` used in the monotonicity proof. The displayed decimal `2.8152423075...` for the inherited all-mixture root is context only and is not used as a theorem certificate.

## 12. Residual obstruction and next materially different attack

The parent remains open. In particular, this proof still stops before the minimum-degree boundary `lambda=3`, because its escape-elasticity input contains the minimum-degree singularity inherited from `U/B<=1/(3-lambda)`.

Two failed routes are preserved and not silently retried:

1. differentiating the static branch-addition ratio to force an elasticity order is invalid in general;
2. a universal pathwise logarithmic-derivative order under branch addition is unavailable (an exact admissible-envelope counterexample is already recorded by PROB10-06).

The next genuinely different escape/regeneration attack should therefore use the inverse-escape moment that remains finite past the minimum-degree point for nontrivial mixtures and convert it into an **occupation-weighted regeneration score**, rather than another pointwise `1/(3-lambda)` estimate. A successful version must control the derivative cost only on regeneration blocks that actually see degree-three vertices.

## 13. ledger_delta

```yaml
ledger_delta:
  worker: NM13-05
  target: T06
  source_id: P0066
  parent_problem: Lyons-Pemantle-Peres biased-walk speed monotonicity
  parent_status_before: OPEN
  parent_status_after: OPEN
  offspring_class: "P(nu=3)=1-p, P(nu=4)=p"
  bias_convention: "parent lambda; child beta=1/lambda"
  metric: "certified strict-parent-bias derivative endpoint by p-region"
  before:
    inherited_all_mixture_criterion: "A_3(lambda)<7+4*sqrt(3)"
    inherited_limiting_endpoint_decimal_context: 2.8152423075
  after:
    p_in_0_to_1_over_4:
      lambda_endpoint: "569/200"
      beta_derivative_interval: "200/569 <= beta <= 1"
      uniform_minus_ell_prime_margin: "153509400000/49730949521317"
    p_in_3_over_4_to_1:
      lambda_endpoint: "57/20"
      beta_derivative_interval: "20/57 <= beta <= 1"
      uniform_minus_ell_prime_margin: "93338400/58489590703"
  demonstrated_mechanism_gain: "combine branch-addition localization 4p/(5-p)<=theta<=p with the dynamic adjacent escape-sensitivity bound before optimizing the derivative numerator"
  simulations_used_for_claim: false
  exact_checker: "2026-09-20T06-22-00Z__mixture-localized-adjacent-check.py"
  exact_output: "2026-09-20T06-22-00Z__mixture-localized-adjacent-check.out"
  result_label: PARTIAL_CANDIDATE_RESTRICTED
  unchanged_substantive_runs: 0
  failed_recoveries: 0
  residual_obstruction: "minimum-degree pointwise escape-elasticity singularity at lambda=3"
  next_attack: "occupation-weighted regeneration derivative using inverse-escape moments, not pointwise branch-elasticity ordering"
```
