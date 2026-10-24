SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B17, 2026-09-22T21:11:44Z.
attacking: exact finite-period optimization of the diffuse rotated-cube witness, including a sharp arithmetic deficit and equality classification.

# account03/B17 — exact finite-period Edgeworth witness optimizer

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260922T211144Z-account03-B17-QFORM-r17`  
Assignment: sharp constant and witnesses  
Status: `NEW SHARP SUPPORTING THEOREM / FULL CONJECTURE OPEN`  
Execution memory: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source discipline

The full target remains: for arbitrary independent real coordinates with densities at most one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a dimension-free essential-density bound for `X^T A X`, or give a valid counterexample. The continuity conclusion remains separate.

This run uses none of the refuted arbitrary-joint coarea, worst conditional-density, pointwise van-der-Corput, one-minor, or near-zero half-Riesz shortcuts. The result below is a sharp witness constraint inside the completed fixed-period uniform-cube Edgeworth family. It does not claim a full upper bound for QFORM.

Fresh control at start: `yspennstate/math-research-brain@7708818b2832fb5055d55674e596fbb93270e79b`, OWNER CONTROL revision `2026-09-22.15`, QFORM sole research target, no B17 pause/stop.

## 2. Partner theorem consumed

Designated partner `account04/B17` has now completed a current-QFORM result:

- repository/commit: `yspennstate/math-open-problems@092be154e735f99a60d80dff46b648ae7bae01b7`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260922T201827Z-account04-B17-QFORM-r2/REPORT.md`;
- theorem: for `J=diag(1,1,-1)` and any tight frame with row vectors `v_j`, if
  `s_j=v_{j1}^2+v_{j2}^2`, `t_j=v_{j3}^2`, then the first Edgeworth correction polynomial is

`E(s,t)=(57/32)s^2+(15/4)st+(3/4)t^2`,

with `sum s_j=2`, `sum t_j=1`. For the repeated frame pattern with `m` copies scaled by `m^{-1/2}` and iid `Uniform[-1/2,1/2]` physical coordinates,

`p_{Q_m}(0)=3 sqrt(2)[1-(1/(20m)) sum_j E(s_j,t_j)+O(m^{-2})]`.

The partner proved the continuous lower bound `sum E >= kappa_*/r`, where

`kappa_*=(sqrt(57/8)+sqrt(3/4))^2 = 63/8+sqrt(171/8)`.

This run solves the **finite-r minimization exactly**, including the integer arithmetic gap and all minimizers.

## 3. Exact finite-r optimization theorem

### Theorem 3.1 — exact finite-period cone-polynomial minimum

Let `r>=3`, and let nonnegative numbers `s_1,...,s_r,t_1,...,t_r` satisfy

`sum_j s_j=2`, `sum_j t_j=1`.

Put

`F_r(s,t)=sum_j [(57/32)s_j^2+(15/4)s_j t_j+(3/4)t_j^2]`.

Then

`min F_r = M_r := min_{1<=k<=r-1} [57/(8k)+3/(4(r-k))].`

Every minimizer is sign-segregated: after a permutation there is a minimizing integer `k` such that

`s_1=...=s_k=2/k`, `t_1=...=t_k=0`,

and

`s_{k+1}=...=s_r=0`, `t_{k+1}=...=t_r=1/(r-k)`.

For `r>=3`, every minimizing `k` automatically satisfies `k>=2`; hence the scalar optimum is realizable by an actual rank-three tight frame.

### Proof

Write

`a=57/32`, `b=15/4`, `c=3/4`.

The key strict inequality is

`a+c-b = -39/32 <0`.                                               (3.1)

#### Step 1: at most one mixed row at a minimizer

Suppose two distinct rows `i,j` both have positive `s` and positive `t`. Along the sum-preserving perturbation

`s_i -> s_i+eps`, `s_j -> s_j-eps`,
`t_i -> t_i-eps`, `t_j -> t_j+eps`,

the coefficient of `eps^2` in the sum of the two row energies is

`2(a+c-b)=-39/16<0`.

Hence the objective is strictly concave along the maximal feasible interval in `eps`; an interior point cannot minimize it. Moving to an endpoint kills at least one of the four positive coordinates and does not increase the objective. Therefore a global minimizer has at most one row with both `s_j,t_j>0`.

#### Step 2: a mixed row cannot coexist with an unused row

If a row `(u,v)` has `u,v>0` and another row is `(0,0)`, replace them by `(u,0)` and `(0,v)`. The pure square terms are unchanged and the positive cross cost `buv` disappears. Thus every minimizer with one mixed row uses all remaining rows as pure rows.

#### Step 3: reduce the one-mixed-row case to two variables

Assume one mixed row `(u,v)`, with `p` positive-only rows and `q` negative-only rows. Then `p+q=r-1`. Convexity of the pure square terms forces equalization within each pure class, so for `p,q>=1` the minimum at fixed `(u,v)` equals

`G_{p,q}(u,v)
 = a[(2-u)^2/p+u^2]
 + c[(1-v)^2/q+v^2]
 + b u v`,                                                     (3.2)

on `0<=u<=2`, `0<=v<=1`.

The Hessian determinant of (3.2) is

`D_{p,q}=-(9/(32pq)) H_{p,q}`,

where

`H_{p,q}=31pq-19p-19q-19`.                                    (3.3)

If `H_{p,q}>0`, the Hessian is indefinite, so an interior point cannot be a local minimum; the global minimum on the rectangle lies on the boundary.

If `H_{p,q}<0`, since `p,q` are positive integers, necessarily either `p=1,q<=3` or `q=1,p<=3`. The unique stationary point has

`u_* = 2(10p-19q-19)/H_{p,q}`,

`v_* = -19(p-5q+1)/H_{p,q}`.                                  (3.4)

For each of the only possible pairs

`(p,q) in {(1,1),(1,2),(1,3),(2,1),(3,1)}`,

formula (3.4) gives `v_*<0`; hence the positive-definite stationary point is infeasible. There is no integer pair with `H_{p,q}=0` (for `p=1`, `q=19/6`; for `p=2`, `q=57/43`; for `p>=3`, the only possible positive value is already nonintegral or below one). Therefore (3.2) always minimizes on its boundary.

If `p=0`, then `u=2` and

`G(v)=4a+c[(1-v)^2/q+v^2]+2bv`.

Its derivative at zero is `2b-2c/q>0`, and its derivative is increasing, so the minimum is `v=0`.

If `q=0`, then `v=1`, `p=r-1>=2`, and

`G(u)=a[(2-u)^2/p+u^2]+c+bu`.

Its derivative at zero is `b-4a/p>=b-2a=3/16>0`, and its derivative is increasing, so the minimum is `u=0`.

Thus **no minimizer contains a mixed row**.

#### Step 4: optimize the pure partition

Let exactly `k` rows carry `s` and the remaining `r-k` carry `t`. Cauchy gives

`sum s_j^2 >= 4/k`, `sum t_j^2 >= 1/(r-k)`,

with equality exactly when the active values are equal. Therefore

`F_r >= 4a/k+c/(r-k)
     =57/(8k)+3/(4(r-k))`.

Minimizing over the integer `k` proves the formula and equality classification.

Finally, `k=1` is never optimal for `r>=3`, because

`[57/8+3/(4(r-1))]-[57/16+3/(4(r-2))]
 =57/16 - 3/[4(r-1)(r-2)] >0`.

So a minimizing `k` has `k>=2`. `QED`

## 4. Exact arithmetic deficit above the continuous partner bound

Put

`A=57/8`, `B=3/4`,
`rho=sqrt(A)/(sqrt(A)+sqrt(B))=0.7550344704135897...`,
`kappa_*=(sqrt(A)+sqrt(B))^2=12.49831050222673...`.

For `x in (0,1)` one has the exact identity

`A/x+B/(1-x)-kappa_*
 = kappa_*(x-rho)^2/[x(1-x)]`.                                 (4.1)

Hence if `k_r` is any minimizing integer in Theorem 3.1,

`r M_r
 = kappa_* [1+(k_r-rho r)^2/(k_r(r-k_r))]`.                   (4.2)

Because `rho` is irrational, the bracket is **strictly larger than one for every finite integer r**. Therefore the partner's continuous coefficient `kappa_*/r` is an infimum as the pattern size grows, but it is never attained by a finite pattern.

Define the sharp finite-period Edgeworth deficit coefficient

`beta_r := r M_r/20`.

Then

`beta_r > beta_* := kappa_*/20
 = 0.6249155251113365...`                                      (4.3)

for every finite `r>=3`, with equality only in the limit along suitable integer approximations to `rho`.

Some exact values are

| r | minimizing k | M_r | beta_r |
|---:|---:|---:|---:|
| 3 | 2 | 69/16 | 0.646875 |
| 4 | 3 | 25/8 | 0.625 |
| 5 | 4 | 81/32 | 0.6328125 |
| 6 | 4 | 69/32 | 0.646875 |
| 7 | 5 | 9/5 | 0.63 |
| 8 | 6 | 25/16 | 0.625 |
| 9 | 7 | 39/28 | 0.626785714... |
| 12 | 9 | 25/24 | 0.625 |

Thus the four-row pattern is already extremely close to the continuous optimum, but still has the exact arithmetic gap

`beta_4-beta_* = 8.44748886635e-5...`.

## 5. Application to the designated partner's Edgeworth theorem

The account04/B17 expansion gives, for every fixed tight-frame pattern of size `r`, repeated `m` times,

`p_{Q_m}(0)
 =3 sqrt(2)[1-(1/(20m)) F_r+O(m^{-2})]`.

Applying Theorem 3.1 produces the **sharp finite-r first-order upper envelope**

`p_{Q_m}(0)
 <=3 sqrt(2)[1-M_r/(20m)+O(m^{-2})]`.

With total physical dimension `n=rm`, this is

`p_{Q_m}(0)
 <=3 sqrt(2)[1-beta_r/n+O(n^{-2})]`,                           (5.1)

where `beta_r` is exactly (4.3). The coefficient cannot be improved uniformly within the partner's fixed-r family, because the minimizing sign-segregated tight frames below attain `F_r=M_r` exactly.

This is stronger than merely saying sign mixing has a positive penalty: it proves that **for every finite period, all first-order optimizers are sign-segregated and the remaining deficit is an explicit integer-allocation penalty**. A genuinely sign-mixing physical row can never be a finite-period first-order optimizer.

## 6. Exact optimal rotated stress frame for r=4

For `r=4`, the exact optimizer has `k=3`. Take the four frame rows

`v_1=sqrt(2/3)(1,0,0)`,
`v_2=sqrt(2/3)(-1/2,sqrt(3)/2,0)`,
`v_3=sqrt(2/3)(-1/2,-sqrt(3)/2,0)`,
`v_4=(0,0,1)`.

Then `sum_j v_j v_j^T=I_3`. With `J=diag(1,1,-1)`, the base physical matrix is

`A_0 = V J V^T
 = [[ 2/3,-1/3,-1/3, 0],
    [-1/3, 2/3,-1/3, 0],
    [-1/3,-1/3, 2/3, 0],
    [ 0,    0,    0,  -1]]`,

which has exact nonzero spectrum `{1,1,-1}`. It is non-diagonal in the independent physical coordinates. Repeating each row `m` times at scale `m^{-1/2}` gives the partner's target-admissible `4m`-dimensional rotated cube family.

For this frame,

`F_4=3*(57/32)*(2/3)^2+3/4=25/8`,

so

`p_{Q_m}(0)
 =3 sqrt(2)[1-5/(32m)+O(m^{-2})]
 =3 sqrt(2)[1-5/(8n)+O(n^{-2})]`.                              (6.1)

Thus `5/8=0.625` is the exact best first-order coefficient for every four-row periodic pattern, only `8.44749e-5` above the global continuous-pattern infimum.

## 7. Target-level implication

This does **not** improve the established universal lower bound `C>=3sqrt(2)` and does not prove that `3sqrt(2)` is the sharp QFORM constant. It closes a sharper witness mechanism:

- every fixed-period iid uniform-cube frame approaches `3sqrt(2)` from below at first order;
- the optimal finite-period architecture is completely classified and sign-segregated;
- mixed-sign physical rows are never first-order optimal, even when integer row-count effects are included;
- no finite period attains the asymptotic continuous optimum exactly; the only remaining way to remove the arithmetic deficit inside this mechanism is to let the frame pattern size itself grow.

Therefore a witness above `3sqrt(2)`, if one exists, must leave this exact first-order periodic uniform-cube mechanism: e.g. growing/nonperiodic frame geometry with nonuniform density-one supports, mesoscopic leverage, or a genuinely non-Edgeworth local concentration mechanism.

The full essential-density conjecture remains `OPEN / NOT PROVED`; full-target continuity remains `OPEN`.

## 8. Computation check

An exact-rational checker in this run directory verifies:

- `a+c-b=-39/32`;
- the positive-definite one-mixed Hessian cases are only `(1,1),(1,2),(1,3),(2,1),(3,1)`, and their stationary `v_*` values are negative;
- the exact `M_r` and `beta_r` table above;
- `M_4=25/8`, `beta_4=5/8`;
- the four-row frame satisfies `V^T V=I_3` and has physical spectrum `{1,1,-1,0}`.

No histogram or Monte Carlo inference is used.
