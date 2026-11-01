Actual runtime model: **GPT-5.6 Sol**. Applied reasoning-effort telemetry: **UNVERIFIED**.

# T06 / NM13-05 — type-conditioned sibling-mean Jensen contraction

Status: **PARTIAL / parent OPEN; NEW RESTRICTED-FAMILY THEOREM CANDIDATES pending independent review.**

Repository: private `yspennstate/math-open-problems`, branch `master`.
Owner root: `proofnet24/NM13-05/progress-tree-speed`.
Controlling directive: `operations/PROGRESS20_2026-09-20.md` on `master`.

## 0. Compact handoff, ownership, and preserved failures

LIVE20 keeps NM13-05 on T06 by the escape-probability / regeneration-coupling route and P01 on the complementary analytic regeneration-derivative route.

The latest own substantive predecessor consumed was

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T16-20-00Z__joint-L-vector-score-secant.md`.

Its inherited restricted candidates for the adjacent no-leaf family `P(nu=3)=1-p`, `P(nu=4)=p` included

- `p>=293/500`: strict parent-bias speed decrease through `lambda=3001/1000`;
- `p>=3/5`: through `lambda=151/50=3.02`;
- `p>=2/3`: through `lambda=78/25=3.12`;
- retained earlier `p>=4/5`: through `lambda=337/100=3.37`.

That run introduced the joint type-conditioned moment `L_k=E[UB|nu=k]`, where `B` is branch escape and `U=-partial_lambda B`, and used it in both the global derivative contraction and the Aidekon score. Its named remaining loss was the replacement of the sibling escape sum `T` by the deterministic ceiling `(n-1)u_4` in every denominator.

This run executes that materially different attack immediately: it proves finite type-conditioned **upper means** for sibling escape, then conditions on sibling types and applies Jensen to the denominator kernels. Thus the current advance is not another iteration of the old `L` map with the same ceiling.

Historical P0066 is preserved as attempted-unsolved. The old fixed-degree radial drift `(k-lambda)/(k+lambda)` has the desired sign, but this does not control the `lambda`-dependent environment seen from the walk. Nothing below relabels that route as a solution.

Latest companion P01 work consumed:

`proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T16-57-25Z__run-report.md`.

P01 treats the distinct minimum-offspring-one family `P(nu=1)=1-p`, `P(nu=D)=p`, all `D>=2`, and proves a candidate through `lambda=2/3` for `p<=20119/50000=0.40238` by type-conditioned convexity in the Aidekon coefficient. The present run remains on `{3,4}` near and beyond `lambda=3`, so scope and mechanism are complementary.

`POSTED` exclusions remain respected. Repository search records no posted source-wide P0066 closure; no public action is taken here.

## 1. Frozen offspring law and bias convention

Throughout,

`P(nu=3)=1-p`, `P(nu=4)=p`, `0<=p<=1`.

There are no leaves and `E nu=3+p>1`.

Use **parent bias** `lambda`:

`P(parent | nu=k)=lambda/(lambda+k)`,
`P(each fixed child | nu=k)=1/(lambda+k)`.

Write the corresponding speed as `ell_lambda`. The outward child bias used in Ben Arous--Fribergh--Sidoravicius is exactly

`beta=1/lambda`.

Hence on differentiability intervals

`v'(beta)=-ell'_{1/beta}/beta^2`,

so `ell'_lambda<0` is equivalent to `v'(beta)>0` after reciprocal reparametrization.

Primary-source boundary refreshed in this run:

- Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, state that outward-child-bias speed `v(beta)` is increasing for `beta>=717` on Galton--Watson trees without leaves.
- He--Wang--Xiang, arXiv:1610.08151, prove strict parent-bias decrease on
  `0<=lambda<=m1/(1+sqrt(1-1/m1))` for minimum offspring `m1>=2`; the Journal of Applied Probability version was published online 2025-03-05.
- A bounded fresh 2026 search found Song--Liu's deterministic regular-tree result (published 2026-02-27), where the speed decreases monotonically with parent bias. It does not resolve the random Galton--Watson rectangles below. This is not a novelty certificate.

## 2. Inherited escape and score framework

Let `B` be the quenched branch escape probability. If the branch root has offspring `n` and iid child branch escapes `B_i`, then

`B=S/(lambda+S)`, `S=sum_i B_i`.                            (2.1)

Put

`U=-partial_lambda B>=0`.

Differentiating (2.1) gives

`U=S/(lambda+S)^2 + lambda sum_i U_i/(lambda+S)^2`.         (2.2)

For `2<=lambda<4`, the inherited deterministic type ceilings are

`u_4=(4-lambda)/4`,
`u_3=3(4-lambda)/(12+lambda)`.                              (2.3)

The first is the regular four-child escape ceiling; the second follows from `S<=3u_4` at a degree-three root. Hence

`0<B<=u_k` conditional on `nu=k`.                           (2.4)

The inherited twelve-step harmonic inverse-moment envelope gives rigorous type-conditioned lower means

`d_k <= E[B|nu=k]`, `k=3,4`.                               (2.5)

Explicitly, with `q=1-p`,

`d=1-lambda(4-p)/12`,
`M_3^(0)=1+lambda/(3d)`, `M_4^(0)=1+lambda/(4d)`,

and

`T_k(x_3,x_4)
 =1+lambda sum_{r=0}^k C(k,r)p^r q^(k-r)
       /((k-r)/x_3+r/x_4)`,                                (2.6)

one has `E[1/B|nu=k]<=M_k^(j)` for every finite iterate `M^(j+1)=T(M^(j))`; this run retains `j=12` and sets

`d_k=1/M_k^(12)`.                                           (2.7)

The inherited exact Aidekon two-state speed reduction is

`ell_lambda=(M-lambda)/(M+lambda)`, `M=3+theta`,            (2.8)

with

`theta=p c_4/(q c_3+p c_4)`.                               (2.9)

Writing `Delta=h_3/c_3-h_4/c_4`, differentiation gives

`-ell'_lambda
 =2M/(M+lambda)^2 [1-lambda g(theta) Delta]`,              (2.10)

where

`g(theta)=theta(1-theta)/(3+theta)`.                        (2.11)

The inherited quantitative branch-addition estimate gives

`c_4/c_3 >= R_*`,                                           (2.12)

`R_*=(4/5)[1+(lambda-1)/(4-lambda)
             (q d_3/(3+u_3)+p d_4/(3+u_4))]`,             (2.13)

and therefore

`theta>=theta_*:=pR_*/(q+pR_*)`.                            (2.14)

On all certified rectangles below, `theta_*>1/2`, so `g` is decreasing and `g(theta)<=g(theta_*)`.

## 3. New mechanism I: finite type-conditioned sibling-mean upper envelopes

Let

`b_k:=E[B|nu=k]`, `k=3,4`,
`m:=E B=q b_3+p b_4`.                                      (3.1)

For fixed `lambda>0`,

`f_lambda(s)=s/(lambda+s)`

is increasing and concave. Conditional on `nu=k`, Jensen applied to (2.1) gives

`b_k <= k m/(lambda+k m)`.                                 (3.2)

The deterministic ceilings (2.3) give the starting upper vector

`bar b_3^(0)=u_3`, `bar b_4^(0)=u_4`.                       (3.3)

Define for each finite `r`

`bar m^(r)=q bar b_3^(r)+p bar b_4^(r)`,                    (3.4)

`bar b_k^(r+1)=k bar m^(r)/(lambda+k bar m^(r))`.           (3.5)

### Lemma 3.1 — finite sibling-mean envelope

For every finite `r>=0`,

`BOX: b_k<=bar b_k^(r), k=3,4.`                             (3.6)

**Proof.** The case `r=0` is (2.3). If (3.6) holds at `r`, then `m<=bar m^(r)`. By (3.2) and monotonicity of `x -> kx/(lambda+kx)`,

`b_k<=k m/(lambda+k m)
    <=k bar m^(r)/(lambda+k bar m^(r))
    =bar b_k^(r+1)`.

This closes the induction. No limiting fixed point or numerical convergence assumption is used. QED.

The certificates use the finite values

`bar b_k:=bar b_k^(12)`.                                    (3.7)

This is already a mechanism-level improvement over the predecessor: sibling denominators will be charged according to rigorously bounded **mean escape by sibling type**, rather than the pathwise maximum `u_4` for every sibling.

## 4. New mechanism II: type-conditioned Jensen in the joint `UB` recursion

Retain the predecessor's genuinely joint moments

`L_k:=E[UB|nu=k]`.                                          (4.1)

The direct source in (2.2) gives the inherited lower bound

`L_k>=L_k^(0):=(1-u_k)d_k^2/lambda`.                        (4.2)

Now consider a root of degree `n in {3,4}` and one distinguished child of type `k`. Let `T` be the sum of the other `n-1` sibling escapes. From (2.2), after multiplying by `B=S/(lambda+S)`,

`UB
 =S^2/(lambda+S)^3
  +lambda S sum_i U_i/(lambda+S)^3`.                        (4.3)

For the distinguished child,

`lambda S U_i/(lambda+S)^3
 >=lambda B_i U_i/(lambda+B_i+T)^3`.                        (4.4)

Condition also on the sibling offspring types. If exactly `r` of the `n-1` siblings have type four, Lemma 3.1 gives

`E[T | sibling types]
 <=t_{n,r}:=(n-1-r)bar b_3+r bar b_4`.                      (4.5)

For fixed `B_i`, the function

`t -> (lambda+B_i+t)^(-3)`

is decreasing and strictly convex. Since the distinguished subtree is independent of its siblings,

`E_T[(lambda+B_i+T)^(-3) | sibling types]
 >=(lambda+B_i+E T)^(-3)
 >=(lambda+u_k+t_{n,r})^(-3)`.                              (4.6)

Therefore, defining

`Q_{n,k}^{mean}
 :=lambda sum_{r=0}^{n-1} C(n-1,r)p^r q^(n-1-r)
       /(lambda+u_k+t_{n,r})^3`,                            (4.7)

we get the positive two-type recursion

`L_n >= L_n^(0)
       +n sum_{k=3,4} pi_k Q_{n,k}^{mean} L_k`,             (4.8)

where `pi_3=q`, `pi_4=p`.

Starting from (4.2), define the finite iteration

`L_n^(s+1)
 =L_n^(0)+n sum_k pi_k Q_{n,k}^{mean} L_k^(s)`.             (4.9)

All coefficients are nonnegative, so induction in (4.8) yields

`BOX: L_k>=L_k^(s) for every finite s.`                     (4.10)

The checker uses `s=12`.

Relative to the predecessor, the deterministic sibling ceiling `(n-1)u_4` in the denominator has been replaced by a binomial average of type-conditioned mean ceilings `t_{n,r}`. This is a genuine strengthening of the joint-moment transfer, not a reparameterization.

## 5. New mechanism III: convex sibling averaging in both secant subtractions

The predecessor used the endpoint secant for

`x -> 1/(t+x)^2` on `0<=x<=u`:

`1/(t+x)^2
 <=1/t^2-c_u(t)x`,                                        (5.1)

where

`c_u(t)=(2t+u)/(t^2(t+u)^2)`.                              (5.2)

A direct derivative calculation gives

`c_u'(t)
 =-2(3t^2+3tu+u^2)/(t^3(t+u)^3)<0`,                       (5.3)

and, crucially for this run,

`c_u''(t)
 =6(2t+u)(2t^2+2tu+u^2)/(t^4(t+u)^4)>0`.                  (5.4)

Thus `c_u` is decreasing **and convex**.

Condition on sibling types as in Section 4. By Jensen and (4.5),

`E[c_{u_k}(a+T) | sibling types]
 >=c_{u_k}(a+E T)
 >=c_{u_k}(a+t_{n,r})`.                                    (5.5)

Define the type-averaged secant coefficient

`C_{n,k}^{mean}(a)
 :=sum_{r=0}^{n-1} C(n-1,r)p^r q^(n-1-r)
       c_{u_k}(a+t_{n,r})`.                                 (5.6)

This replaces the predecessor's single worst-case value `c_{u_k}(a+(n-1)u_4)`.

### 5.1 Improved global derivative contraction

Let

`K_j^J(a)
 =sum_{r=0}^j C(j,r)p^r q^(j-r)
    a/[a+(j-r)d_3+r d_4]^2`.                               (5.7)

The inherited reciprocal-Jensen estimate gives

`rho=q 3K_2^J(lambda)+p 4K_3^J(lambda)`.                   (5.8)

The inherited source term is

`A=q 12(4-lambda)/(12+lambda)^2+p(4-lambda)/16`.            (5.9)

Using (5.1), independence of the distinguished branch from its siblings, (5.5), and the finite lower vector `L^(12)`, the annealed derivative moment `eta=E U` satisfies

`eta<=A+rho eta-delta_mean`,                                (5.10)

where

`delta_mean
 =lambda sum_{n=3,4} pi_n n sum_{k=3,4} pi_k
     C_{n,k}^{mean}(lambda)L_k^(12)`.                       (5.11)

Hence, when `rho<1`,

`eta <= (A-delta_mean)/(1-rho)`.                            (5.12)

### 5.2 Improved Aidekon score subtraction

Put `a=lambda-1` and

`mu=q d_3+p d_4`.                                           (5.13)

For the four-branch score entering `h_3/c_3`, the distinguished branch has three siblings, so the same argument gives

`Q_score^{mean}
 =q C_{4,3}^{mean}(a)L_3^(12)
  +p C_{4,4}^{mean}(a)L_4^(12)`.                            (5.14)

The inherited score estimate therefore sharpens to

`h_3/c_3
 <=1/a+(3/mu)[eta K_3^J(a)-a Q_score^{mean}]`.              (5.15)

The degree-four lower score remains

`h_4/c_4>=4/(16-lambda)`.                                  (5.16)

Thus

`Delta<=D_mean(lambda,p)`,                                  (5.17)

with

`D_mean
 =1/(lambda-1)
  +(3/mu)[eta K_3^J(lambda-1)
          -(lambda-1)Q_score^{mean}]
  -4/(16-lambda)`.                                          (5.18)

Combining (2.10), (2.14), and (5.18), it is sufficient to prove

`BOX: lambda g(theta_*)D_mean(lambda,p)<1`.                 (5.19)

## 6. New restricted-family theorem candidates

The corrected directed outward interval checker proves four complete rectangles on the new strip starting at `lambda=2`.

### 6.1 Wider class crossing `lambda=3`

For every

`BOX: p>=7/12`,                                             (6.1)

(5.19) is certified throughout

`2<=lambda<=3001/1000=3.001`,                               (6.2)

with

`lambda g(theta_*)D_mean <999/1000`.                        (6.3)

Since `M>=3` and `M+lambda<=4+3001/1000`, (2.10) gives

`BOX: -ell'_lambda >=6000/49014001>0`.                     (6.4)

The immediate predecessor required `p>=293/500` for the same endpoint. The certified class crossing `lambda=3` therefore widens by exactly

`293/500-7/12=1/375`.                                       (6.5)

### 6.2 Deeper endpoint for `p>=3/5`

For every

`BOX: p>=3/5`,                                              (6.6)

(5.19) is certified on

`2<=lambda<=3023/1000=3.023`,                               (6.7)

with product `<997/1000`, hence

`BOX: -ell'_lambda >=2000/5480281>0`.                      (6.8)

The predecessor endpoint was `151/50=3.02`, so the source-level endpoint gain is

`3023/1000-151/50=3/1000`.                                  (6.9)

### 6.3 Deeper endpoint for `p>=2/3`

For every

`BOX: p>=2/3`,                                              (6.10)

(5.19) is certified on

`2<=lambda<=25/8=3.125`,                                    (6.11)

with product `<999/1000`, hence

`BOX: -ell'_lambda >=16/135375>0`.                         (6.12)

The predecessor endpoint was `78/25=3.12`, so the exact endpoint gain is

`25/8-78/25=1/200`.                                         (6.13)

### 6.4 Deeper endpoint for `p>=4/5`

For every

`BOX: p>=4/5`,                                              (6.14)

(5.19) is certified on

`2<=lambda<=3377/1000=3.377`,                               (6.15)

with product `<995/1000`, hence

`BOX: -ell'_lambda >=10000/18140043>0`.                    (6.16)

The retained earlier endpoint for this subclass was `337/100=3.37`, so the exact endpoint gain is

`3377/1000-337/100=7/1000`.                                 (6.17)

All four high-bias strips overlap the inherited all-mixture `{3,4}` escape-tilt theorem, which reaches past `lambda=2` (indeed to the previously certified root approximately `2.8152423075`). That inherited theorem in turn overlaps the He--Wang--Xiang low-parent-bias theorem. Hence each displayed restricted candidate stitches to a connected monotonicity interval from `lambda=0` to its stated endpoint.

In reciprocal child-bias notation, the directly new derivative-positive strips include

- `p>=7/12`: `1000/3001 <= beta <= 1/2`;
- `p>=3/5`: `1000/3023 <= beta <= 1/2`;
- `p>=2/3`: `8/25 <= beta <= 1/2`;
- `p>=4/5`: `1000/3377 <= beta <= 1/2`.

These are restricted-family candidates only. The parent conjecture remains open.

## 7. Essential rigorous computation and soundness correction

The relied-upon checker is

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T17-22-49Z__sibling-mean-type-jensen-rigorous-check.cpp`.

Actual stdout is

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T17-22-49Z__sibling-mean-type-jensen-rigorous-check.out`.

Build/run command:

`g++ -O2 -std=c++17 -frounding-math -ffp-contract=off ...rigorous-check.cpp -o sibling_mean_check_rig && ./sibling_mean_check_rig`.

The code uses IEEE-754 interval operations with `nextafter` after every elementary arithmetic operation. Each rational theorem boundary is expanded outward (`p_0` downward, `lambda` endpoint upward), and each comparison threshold is moved downward. Adaptive bisection covers the entire outer parameter rectangle; there is no grid acceptance criterion and no simulated speed sign.

The corrected checker also represents the exact inherited factor `4/5` as the outward interval `divi(point(4),point(5))`. An earlier exploratory checker archived at the same timestamp used the binary point literal `.8`; because binary `.8` is not exact, that exploratory file is **not relied upon**. The corrected checker was rerun from scratch and all four modes pass.

Actual corrected output summary:

- `p>=7/12`, `lambda<=3001/1000`: 34,637 boxes visited, worst certified product upper bound `0.99899641696310248`;
- `p>=3/5`, `lambda<=3023/1000`: 31,873 boxes, worst product `0.99699392358328331`;
- `p>=2/3`, `lambda<=25/8`: 29,007 boxes, worst product `0.99899989885533402`;
- `p>=4/5`, `lambda<=3377/1000`: 19,589 boxes, worst product `0.99499766786019972`.

Every mode also certifies `rho<0.99`; stdout ends

`ALL_RIGOROUS_INTERVAL_CHECKS_PASS`.

The printed decimal extrema are diagnostics only. The logical acceptance test is the outward interval comparison against the stated rational thresholds.

Local pre-upload SHA256 values for the corrected artifacts were

`82565e27683b20e10e9d059aa3a96b1de619768ed9ce92b42844f0b9fb3e01b7`  checker,

`9b93f61b2c420b5c7e783f903987a146f633d6fccdf8208ca2bdceda0f6f5c49`  stdout.

## 8. Parent scope versus mechanism gain

### Parent-problem scope

Before this run: **OPEN**, with the inherited `{3,4}` restricted candidates listed in Section 0.

After this run: **OPEN**. No source-wide LPP monotonicity theorem is claimed.

Source-level restricted gains proved here are exactly:

- crossing-class threshold `293/500 -> 7/12` at endpoint `3.001`, a width gain `1/375`;
- `p>=3/5` endpoint `3.02 -> 3.023`, gain `3/1000`;
- `p>=2/3` endpoint `3.12 -> 3.125`, gain `1/200`;
- `p>=4/5` endpoint `3.37 -> 3.377`, gain `7/1000`.

No unknown baseline is treated as zero.

### Demonstrated mechanism gain

The previous proof replaced every sibling escape sum by its pathwise maximum. This run proves finite type-conditioned upper means `bar b_3,bar b_4`, conditions on the sibling type pattern, and uses convexity twice:

1. convexity of `(lambda+B+T)^(-3)` strengthens the positive recursion for the joint moment `E[UB|nu=k]`;
2. convexity of the secant coefficient `c_u(a+T)` strengthens both the global derivative contraction and the Aidekon score subtraction.

The new parameter rectangles above demonstrate that this mechanism transfers to the parent target rather than merely improving an auxiliary constant.

## 9. Residual obstruction and next nonredundant attack

The new argument retains sibling **type and first mean**, but still Jensen-collapses all within-type sibling randomness. The remaining denominator loss is therefore no longer the pathwise ceiling; it is the omission of a second sibling statistic after conditioning on types.

Further iteration of the same first-mean map is a diminishing-return variant, not the next preferred route.

The next materially distinct attack is to carry a second sibling statistic into the joint kernel. One concrete route is a two-type second-moment recursion for `E[B^2|nu=k]`, followed by a rigorous quadratic lower support for the convex kernels

`(lambda+B+T)^(-3)` and `c_u(a+T)`

around the conditional mean. Equivalently, define mixed denominator moments such as

`J_k^{(r)}=E[UB/(lambda+B+T)^r | nu=k]`

with the sibling type pattern retained, rather than Jensenizing `T` to one number. Either route would use information that the present first-mean certificate necessarily discards.

## 10. ledger_delta

```yaml
ledger_delta:
  track: NM13-05
  parent: T06_Lyons_Pemantle_Peres_GW_speed_monotonicity
  source_id: P0066
  parent_before: OPEN
  parent_after: OPEN
  offspring_law:
    P_nu_3: 1-p
    P_nu_4: p
    leaves: false
  bias_convention:
    parent_bias: lambda
    child_bias: beta=1/lambda
  predecessor:
    report: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T16-20-00Z__joint-L-vector-score-secant.md
    crossing: p>=293/500, lambda<=3001/1000
    p_ge_3_5: lambda<=151/50
    p_ge_2_3: lambda<=78/25
    retained_p_ge_4_5: lambda<=337/100
  new_restricted_candidates:
    - p: ">=7/12"
      lambda: "<=3001/1000"
      high_strip_derivative_margin: ">=6000/49014001"
      gain: "crossing threshold 293/500 -> 7/12, width 1/375"
    - p: ">=3/5"
      lambda: "<=3023/1000"
      high_strip_derivative_margin: ">=2000/5480281"
      gain: "endpoint +3/1000"
    - p: ">=2/3"
      lambda: "<=25/8"
      high_strip_derivative_margin: ">=16/135375"
      gain: "endpoint +1/200"
    - p: ">=4/5"
      lambda: "<=3377/1000"
      high_strip_derivative_margin: ">=10000/18140043"
      gain: "endpoint +7/1000"
  mechanism:
    - finite type-conditioned escape-mean upper iteration
    - sibling-type-conditioned Jensen for joint UB recursion
    - convex sibling-mean Jensen for secant coefficients in eta and score
  rigorous_checker:
    source: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T17-22-49Z__sibling-mean-type-jensen-rigorous-check.cpp
    output: proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T17-22-49Z__sibling-mean-type-jensen-rigorous-check.out
    result: ALL_RIGOROUS_INTERVAL_CHECKS_PASS
    exploratory_checker_at_same_timestamp: NOT_RELIED_UPON_due_to_binary_point_literal_for_4_over_5
  failed_route_preserved:
    P0066_fixed_degree_drift: insufficient_to_control_environment_law
  companion:
    P01: minimum-offspring-one analytic Aidekon route, latest p<=20119/50000 through lambda=2/3
  status: PARTIAL_RESTRICTED_THEOREM_CANDIDATES_PENDING_INDEPENDENT_REVIEW
  next_attack: type-conditioned second sibling moment or mixed denominator-moment recursion retaining within-type T variability
```
