Actual runtime model: **GPT-5.6 Sol**. Applied reasoning-effort telemetry: **UNVERIFIED**.

# T06 / NM13-05 — two-type joint `UB` recursion plus score-level secant subtraction

Status: **PARTIAL / parent OPEN; NEW RESTRICTED-FAMILY THEOREM CANDIDATES pending independent review.**

Repository: private `yspennstate/math-open-problems`, branch `master`.
Owner root: `proofnet24/NM13-05/progress-tree-speed`.
Controlling directive: `operations/PROGRESS20_2026-09-20.md` on `master`.

## 0. Compact handoff, ownership, and preserved failed route

LIVE20 keeps NM13-05 on T06 by the escape-probability / regeneration-coupling route and P01 on the complementary analytic regeneration-derivative route. The latest own substantive predecessor consumed was

`2026-09-20T15-22-30Z__joint-own-B-secant-contraction.md`.

It proved, for the adjacent no-leaf family `P(nu=3)=1-p`, `P(nu=4)=p`, the restricted candidates

- `p>=59/100`: strict parent-bias speed decrease through `lambda=3001/1000`;
- `p>=2/3`: through `lambda=623/200`;
- `p>=4/5`: through `lambda=337/100`.

An earlier retained theorem gives `p>=3/4` through `lambda=651/200`.

The predecessor's new mechanism was an own-`B` secant subtraction in the scalar derivative-moment contraction. Its named next route was a two-type derivative-moment vector. This run first checks that the naive vector alone gives **no improvement**: if `eta_k=E[U|nu=k]`, dropping the distinguished child's own `B` gives

`eta_3 <= A_3 + 3 K_2(lambda) [(1-p)eta_3+p eta_4] - delta_3`,

`eta_4 <= A_4 + 4 K_3(lambda) [(1-p)eta_3+p eta_4] - delta_4`.

Averaging with weights `1-p,p` collapses exactly to the predecessor's scalar inequality. The coefficient matrix is rank one at this level. I therefore did **not** spend the run iterating that no-gain vector; instead I retained the genuinely joint moment `E[UB|nu=k]` and fed it into two different parts of the proof.

Historical P0066 is preserved as attempted-unsolved. Its fixed-degree local drift `(k-lambda)/(k+lambda)` has the desired derivative sign, but this does not control the `lambda`-dependent environment seen from the walk. Nothing here relabels that failed route as a solution.

Latest companion P01 work consumed: `proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T15-57-21Z__run-report.md`. P01 now treats the distinct minimum-offspring-one family `P(nu=1)=1-p`, `P(nu=D)=p`, all `D>=2`, proving a candidate through `lambda=2/3` for `p<=792847/2000000`. There is no parameter/mechanism duplication with the present `{3,4}` near-`lambda=3` escape route.

## 1. Frozen assumptions and bias convention

Throughout this report,

`P(nu=3)=1-p`, `P(nu=4)=p`, `0<=p<=1`.

There are no leaves and the mean offspring is `3+p>1`. Parent bias is `lambda`:

`P(parent | nu=k)=lambda/(lambda+k)`,
`P(each fixed child | nu=k)=1/(lambda+k)`.

Write the parent-bias speed as `ell_lambda`. The outward child bias is exactly

`beta=1/lambda`.

Thus on differentiability intervals

`v'(beta)=-ell'_{1/beta}/beta^2`,

so `ell'_lambda<0` is equivalent to `v'(beta)>0` under reciprocal reparametrization.

Primary-source boundary refreshed on 2026-09-20:

- Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, prove outward-child-bias speed increasing for `beta>=717` on Galton--Watson trees without leaves.
- He--Wang--Xiang, arXiv:1610.08151, prove strict parent-bias decrease on
  `0<=lambda<=m1/(1+sqrt(1-1/m1))` for minimum offspring `m1>=2`; the Journal of Applied Probability version was published online 2025-03-05.
- A bounded fresh literature search also found the 2026 deterministic regular-tree monotonicity paper of Song--Liu. I found no checked source in that bounded search identical to the random `{3,4}` rectangles below. This is **not** a novelty certificate.

`POSTED` exclusions remain respected; no public-posting action was taken and no source-wide P0066 solution is claimed.

## 2. Inherited escape envelopes

Let `B` be the quenched branch escape probability. With iid child copies `B_i`,

`B=S/(lambda+S)`, `S=sum_i B_i`.

Let `U=-partial_lambda B>=0`. Then exactly

`U=S/(lambda+S)^2 + lambda sum_i U_i/(lambda+S)^2`.          (2.1)

The twelve-step harmonic inverse-moment envelope from the predecessor is retained. Put `q=1-p`,

`d=1-lambda(4-p)/12`,

`M_3^(0)=1+lambda/(3d)`, `M_4^(0)=1+lambda/(4d)`,

and, for `k=3,4`,

`T_k(x3,x4)=1+lambda sum_{r=0}^k C(k,r)p^r q^(k-r) /
                    ((k-r)/x3+r/x4)`.

Define `M^(j+1)=T(M^(j))`. Joint concavity and monotonicity of the harmonic mean imply, for every finite `j`,

`E[1/B | nu=k] <= M_k^(j)`.

This run continues to use `j=12` and defines

`d_k:=1/M_k^(12) <= E[B|nu=k]`.                              (2.2)

The deterministic type ceilings are

`u_4=(4-lambda)/4`,
`u_3=3(4-lambda)/(12+lambda)`,                               (2.3)

so `0<B<=u_k` conditional on `nu=k`.

## 3. New joint moment and a positive two-type recursion

Define the genuinely joint type-conditioned moment

`L_k:=E[U B | nu=k]`, `k=3,4`.                              (3.1)

The predecessor used only the source-term lower bound. From (2.1),

`U >= B(1-B)/lambda`,

hence, using `B<=u_k`, Jensen, and (2.2),

`L_k >= L_k^(0):=(1-u_k)d_k^2/lambda`.                       (3.2)

The new gain comes from retaining the descendants in `UB`. Multiplying (2.1) by `B=S/(lambda+S)` gives

`UB=S^2/(lambda+S)^3 + lambda S sum_i U_i/(lambda+S)^3`.     (3.3)

At a root of degree `n in {3,4}`, condition one distinguished child to have type `k`. Since

`S>=B_i`,
`S<=u_k+(n-1)u_4`,

we obtain the pointwise lower bound

`lambda S U_i/(lambda+S)^3
 >= lambda B_i U_i/[lambda+u_k+(n-1)u_4]^3`.                 (3.4)

Therefore the true vector `L=(L_3,L_4)` satisfies

`L_n >= L_n^(0)
       + n sum_{k=3,4} pi_k Q_{n,k} L_k`,                    (3.5)

where

`pi_3=q`, `pi_4=p`,
`Q_{n,k}=lambda/[lambda+u_k+(n-1)u_4]^3`.                   (3.6)

Starting from (3.2), define the finite positive iteration

`L_n^(r+1)=L_n^(0)+n sum_k pi_k Q_{n,k} L_k^(r)`.            (3.7)

Because every coefficient is nonnegative, induction in (3.5) gives the rigorous finite-depth statement

`BOX: L_k >= L_k^(r) for every finite r.`                    (3.8)

No convergence or fixed-point assumption is used. The certificates below take `r=12`.

This is the first demonstrated mechanism gain of the run: the old lower bound used only the direct source in `U`; (3.7) also recycles a rigorously controlled amount of the descendants' joint `UB` mass.

## 4. First use of `L^(12)`: stronger derivative-moment contraction

For `0<=b<=u`, the convex function `f_t(b)=1/(t+b)^2` obeys the endpoint secant inequality

`f_t(b) <= f_t(0)-c_u(t)b`,

where

`c_u(t)=(2t+u)/(t^2(t+u)^2)`                                (4.1)

and `c_u(t)` decreases in `t`.

At a root of degree `n`, write `T` for the sibling escape sum of a distinguished child. Then

`T<=(n-1)u_4`.

Conditioning on distinguished child type `k`, multiplying the secant by `lambda U`, and using the independence of the distinguished subtree from its siblings gives

`E[lambda U/(lambda+T+B)^2 | k]
 <= E[lambda/(lambda+T)^2] E[U|k]
    -lambda c_{u_k}(lambda+(n-1)u_4) L_k`.                  (4.2)

Let

`K_j^J(a)=sum_{r=0}^j C(j,r)p^r q^(j-r)
          a/[a+(j-r)d_3+r d_4]^2`.                          (4.3)

The inherited reciprocal-Jensen sibling bound gives the first term in (4.2). Averaging (2.1) over root type therefore yields

`eta:=E U <= A+rho eta-delta_12`,                            (4.4)

with

`rho=q 3 K_2^J(lambda)+p 4 K_3^J(lambda)`,                  (4.5)

`A=q 12(4-lambda)/(12+lambda)^2 + p(4-lambda)/16`,           (4.6)

and the improved subtraction

`delta_12
 =lambda sum_{n=3,4} pi_n n sum_{k=3,4} pi_k
   c_{u_k}(lambda+(n-1)u_4) L_k^(12)`.                      (4.7)

Hence whenever `rho<1`,

`eta <= (A-delta_12)/(1-rho)`.                              (4.8)

The predecessor had exactly the same form but with `L_k^(0)` in (4.7). Since (3.7) is positive, this is a strict mechanism-level strengthening whenever a descendant term is nonzero.

## 5. Second use of `L^(12)`: a new score-level subtraction

The same joint information also sharpens the Aidekon escape score itself rather than only the global `eta` bound.

Put `a=lambda-1`. For current offspring three there are four branch variables and

`h_3/c_3
 =[ E(S/(a+S)^2)+a E(sum_i U_i/(a+S)^2) ]
   / E[S/(a+S)]`.                                           (5.1)

The escape-only part is at most `1/a`. Also `S<=4u_4=4-lambda`, so

`a+S<=3`,
`E[S/(a+S)] >= E S/3 >=4 mu/3`,                             (5.2)

where

`mu=q d_3+p d_4`.                                           (5.3)

For the derivative part, condition on one distinguished branch. Its three siblings satisfy `T<=3u_4`, hence

`a+T <= a+3u_4 = 2+lambda/4`.                               (5.4)

Applying the same secant before averaging gives

`a E[U/(a+T+B)^2 | k]
 <= E[a/(a+T)^2] E[U|k]
    -a c_{u_k}(2+lambda/4) L_k`.                            (5.5)

After type averaging and the reciprocal-Jensen sibling bound,

`h_3/c_3
 <=1/a + (3/mu)[ eta K_3^J(a)-a Q_score ]`,                 (5.6)

where

`Q_score=q c_{u_3}(2+lambda/4)L_3^(12)
        +p c_{u_4}(2+lambda/4)L_4^(12)`.                    (5.7)

The inherited lower score on degree four remains

`h_4/c_4 >=4/(16-lambda)`.                                  (5.8)

Thus

`Delta:=h_3/c_3-h_4/c_4 <= D_12(lambda,p)`,                 (5.9)

where

`D_12
 =1/(lambda-1)
  +(3/mu)[eta K_3^J(lambda-1)-(lambda-1)Q_score]
  -4/(16-lambda)`.                                          (5.10)

This score-level subtraction is new in this run. It uses the same joint `UB` lower vector a second time, directly in the environment-change score.

## 6. Speed reduction and branch-addition localization

For the `{3,4}` law, the inherited exact Aidekon two-state reduction is

`ell_lambda=(M-lambda)/(M+lambda)`, `M=3+theta`,             (6.1)

where

`theta=p c_4/[q c_3+p c_4]`.                                (6.2)

Differentiation gives

`-ell'_lambda
 =2M/(M+lambda)^2 [1-lambda g(theta) Delta]`,               (6.3)

with

`g(theta)=theta(1-theta)/(3+theta)`.                         (6.4)

The inherited quantitative branch-addition lower bound is

`c_4/c_3 >= R_*`,                                           (6.5)

`R_*=(4/5)[1+(lambda-1)/(4-lambda)
             (q d_3/(3+u_3)+p d_4/(3+u_4))]`.              (6.6)

Therefore

`theta>=theta_*:=pR_*/(q+pR_*)`.                            (6.7)

On every certified rectangle the checker verifies `theta_*>1/2`, where `g` is decreasing. Combining (4.8), (5.10), and (6.7), it is sufficient to prove

`BOX: lambda g(theta_*) D_12(lambda,p)<1`.                  (6.8)

## 7. New restricted theorem candidates

A directed outward interval certificate establishes four rectangles on the new high-bias strip beginning at `lambda=2`.

### 7.1 Wider class crossing `lambda=3`

For every

`BOX: p>=293/500=0.586`,                                    (7.1)

(6.8) is certified for

`2<=lambda<=3001/1000=3.001`,                               (7.2)

with the stronger certified product inequality

`lambda g(theta_*)D_12 <9999/10000`.                        (7.3)

Since `M>=3`, `M+lambda<=4+3001/1000`, (6.3) gives the uniform derivative margin

`BOX: -ell'_lambda >=600/49014001>0`.                       (7.4)

The immediate predecessor required `p>=59/100=0.59` for the same crossing endpoint. The crossing class is therefore widened by exactly

`59/100-293/500=1/250=0.004`.                               (7.5)

### 7.2 Deeper crossing for `p>=3/5`

For every `p>=3/5`, strict derivative negativity is certified on

`2<=lambda<=151/50=3.02`,                                   (7.6)

with product `<999/1000` and hence

`BOX: -ell'_lambda >=5/41067>0`.                            (7.7)

The inherited `p>=59/100` theorem already gave this subclass through `3.001`; the new source-level endpoint gain for `p>=3/5` is therefore exactly

`151/50-3001/1000=19/1000`.                                 (7.8)

### 7.3 Deeper crossing for `p>=2/3`

For every `p>=2/3`, strict derivative negativity is certified on

`2<=lambda<=78/25=3.12`,                                    (7.9)

with product `<199/200` and

`BOX: -ell'_lambda >=75/126736>0`.                          (7.10)

The immediate predecessor endpoint was `623/200=3.115`, so the exact gain is

`78/25-623/200=1/200`.                                      (7.11)

### 7.4 A broader upper-tail region than the `p>=4/5` theorem

For every `p>=3/4`, strict derivative negativity is certified on

`2<=lambda<=409/125=3.272`,                                 (7.12)

with product `<999/1000` and

`BOX: -ell'_lambda >=125/1101708>0`.                        (7.13)

The retained pre-predecessor `p>=3/4` endpoint was `651/200=3.255`, so the source-level gain is exactly

`409/125-651/200=17/1000`.                                  (7.14)

These are derivative-positive child-bias regions under `beta=1/lambda`: on the genuinely new high-bias portions, `v'(beta)>0` for, respectively,

`1000/3001 <= beta <=1/2`,
`50/151 <= beta <=1/2`,
`25/78 <= beta <=1/2`,
`125/409 <= beta <=1/2`.

## 8. Why the displayed parent-bias theorems run from zero

The new joint-moment machinery is used only for `lambda>=2`. The inherited exact all-mixture `{3,4}` escape-tilt theorem proves strict parent-bias decrease for every `p in [0,1]` from `lambda=1` through the exact root of its all-mixture criterion, approximately `2.8152423075`, and therefore overlaps every new strip above.

Below that, He--Wang--Xiang cover

`0<=lambda<=3/(1+sqrt(2/3))`

for minimum offspring three. The two inherited intervals overlap. Consequently each restricted theorem candidate in Section 7 is connected all the way from `lambda=0` to its displayed endpoint; no gap is filled by simulation.

## 9. Rigorous computational certificate

Checker:

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T16-20-00Z__joint-L-vector-score-secant-check.cpp`

created at commit

`451d28209363e7b25503a980090256472dd94231`.

Actual stdout:

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T16-20-00Z__joint-L-vector-score-secant-check.out`

created at commit

`8d4b540706ca73e137aabfad3904316af6ce44fd`.

The checker uses outward `nextafter` interval operations, compiles with

`-O2 -std=c++17 -frounding-math -ffp-contract=off`,

outward-rounds all rational theorem endpoints before subdivision, and accepts a box only after an interval enclosure proves the target product and `rho<0.99`. It is an enclosure proof over complete rectangles, not a grid or speed simulation.

Actual certified summaries:

- `p>=293/500`, `L=3001/1000`: 12,243 visited boxes, worst certified product upper endpoint `0.9998995062810897`, max depth 33.
- `p>=3/5`, `L=151/50`: 10,151 boxes, worst product `0.9989980450464776`, max depth 30.
- `p>=2/3`, `L=78/25`: 7,085 boxes, worst product `0.99499993548833754`, max depth 28.
- `p>=3/4`, `L=409/125`: 6,757 boxes, worst product `0.99899572247379853`, max depth 31.

All four runs end

`ALL_RIGOROUS_INTERVAL_CHECKS_PASS`.

The decimal outputs are diagnostics only; theorem acceptance uses the outward interval comparisons against rationally specified thresholds.

## 10. Parent scope versus demonstrated mechanism gain

### Parent problem

`OPEN -> OPEN`.

No source-wide Lyons--Pemantle--Peres solution is claimed.

### Restricted source-level scope gains

- crossing threshold at endpoint `3.001`: `p>=0.59` -> `p>=0.586`;
- `p>=0.6` endpoint: inherited `3.001` -> `3.02`;
- `p>=2/3` endpoint: `3.115` -> `3.12`;
- `p>=3/4` endpoint: `3.255` -> `3.272`.

These baselines are inherited proved/candidate scopes in the NM13-05 run history; no unknown baseline is treated as zero.

### Demonstrated mechanism gains

1. The naive two-type `eta_3,eta_4` vector was proved to collapse to the old scalar contraction, preventing a false claim of progress from mere reparameterization.
2. The new positive affine recursion (3.7) gives finite-depth rigorous lower bounds on the joint moments `E[UB|nu=3]` and `E[UB|nu=4]`, recycling descendant joint mass rather than only the source term.
3. Those joint lower bounds strengthen the global derivative-moment contraction via (4.7).
4. Independently, the same joint lower bounds produce the new score-level subtraction (5.6)--(5.10) inside `h_3/c_3` itself.
5. The combination is what yields the widened/deeper certified rectangles above.

## 11. Residual obstruction and next materially different attack

The remaining loss is now identifiable. In (3.4) I used only `S>=B_i` and the crude deterministic upper ceiling

`S<=u_k+(n-1)u_4`.

Thus the joint recursion retains `UB` correlation but still discards the siblings' actual escape mass in the denominator. Repeating more finite iterations of exactly the same map will eventually give diminishing returns.

The next nonredundant attack should therefore retain one sibling statistic jointly with `UB`, for example a two-type lower recursion for

`E[UB/(lambda+T+B)^r | nu=k]`

or a regeneration-block formulation that conditions on the sibling escape sum `T`. Either would attack the denominator loss directly rather than only increasing the iteration count of (3.7).

## 12. `ledger_delta`

```yaml
ledger_delta:
  task: T06
  owner: NM13-05
  parent_problem_before: OPEN
  parent_problem_after: OPEN
  offspring_law:
    P_nu_3: 1-p
    P_nu_4: p
    leaves: false
  bias_convention:
    parent: lambda
    child_outward: beta=1/lambda
  restricted_scope_before:
    cross_lambda_3_001: p>=59/100
    p_ge_3_5_endpoint: 3001/1000
    p_ge_2_3_endpoint: 623/200
    p_ge_3_4_endpoint: 651/200
  restricted_scope_after:
    cross_lambda_3_001: p>=293/500
    p_ge_3_5_endpoint: 151/50
    p_ge_2_3_endpoint: 78/25
    p_ge_3_4_endpoint: 409/125
  new_mechanism:
    - finite positive two-type recursion for L_k=E[UB|nu=k]
    - strengthened own-B derivative contraction using L_k^(12)
    - new score-level own-B secant subtraction in h_3/c_3
  failed_route_preserved:
    - P0066 fixed-degree drift sign does not control environment law
    - naive eta_3/eta_4 vector collapses to the predecessor scalar inequality
  proof_status: restricted theorem candidates pending independent review
  simulated_speed_signs_used: false
  checker_commit: 451d28209363e7b25503a980090256472dd94231
  checker_output_commit: 8d4b540706ca73e137aabfad3904316af6ce44fd
```
