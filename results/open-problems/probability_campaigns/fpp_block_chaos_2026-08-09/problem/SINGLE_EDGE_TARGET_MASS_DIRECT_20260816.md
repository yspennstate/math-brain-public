# The single-edge target mass has a direct squared-influence bound

Date: 2026-08-16  
Status: exact edge-level estimate proved under a uniformly positive density;

Companions:

* `DISTINGUISHED_BLOCK_SPECTRAL_SPLIT_20260816.md`, SHA-256
  `f18916f69b7fbd24c96325ae3da9c046ba31152a893ca736fb11de737e083f0f`;
* `SINGLE_EDGE_GAP_COLLISION_20260816.md`, SHA-256
  `bc682c8ecd94a03a0662a26ddcb832e78ef4675bb70866ef6b6960d224e2a43a`.

The gap companion bounds the target mass through a larger avoidance-gap
functional.  Keeping the replacement value inside the conditional increment
gives a shorter and sharper calculation: only threshold values between the old
and replacement edge weights matter.  The robust-use tail above the weight
support never appears.

Let iid edge weights on `Z^d`, `d>=2`, have density `rho` supported on
`[a,b] subset (0,infinity)`, with

`rho(t)>=alpha>0` for almost every `t in [a,b].`              (1)

For the unique geodesic from `0` to `v`, put

`p_e=P(e belongs to gamma(0,v)).`                             (2)

The result is

`C_edge+P_edge <= (1/(4 alpha^2)) sum_e p_e^2.`              (3)

Combined with Dembin--Elboim--Peled, this gives

`C_edge+P_edge
 <=C_(d,G) ||v||^(2/(d+1)) (log ||v||)^d.`                  (4)

This is still only the pure distinguished-edge term in the spectral ledger.

## 1. Exact target-pair formula

Fix an edge `e`.  As in the gap companion, condition on all weights outside
`e` and write

`B_e=min cost of a through-e path with its copy of w_e removed,`

`C_e=min cost of a path avoiding e,       T_e=C_e-B_e.`       (5)

Positive weights let a minimizing through path be taken simple, so it uses
`e` once.  Thus the passage time, as a function of the target weight, is

`X=B_e+min{w_e,T_e}.`                                        (6)

Let `w_e'` be an independent replacement, let `X^e` be the replaced passage
time, and put

`z_e=(X^e-X)^+.`                                             (7)

For fixed target values `w,w'`, equation (6) gives the pointwise identity

`z_e=1_(w'>w) integral_w^(w') 1_(t<T_e) dt.`                 (8)

Indeed, if `w'<=w`, monotonicity makes the increment nonpositive.  If `w'>w`,
the difference `min(w',T_e)-min(w,T_e)` is exactly the length of the part of
`[w,w']` below `T_e`.

Let

`q_e(t)=P(T_e>t),`

where the probability is over the outside environment.  Conditioning on the
full distinguished pair `Y_e=(w_e,w_e')` and using Tonelli in (8) gives

`m_e(w,w'):=E[z_e|w_e=w,w_e'=w']
 =1_(w'>w) integral_w^(w') q_e(t) dt.`                       (9)

This is the exact target-main-effect kernel.  Unlike the conditional mean
avoidance gap, it integrates only inside `[a,b]`.

## 2. Conversion to squared geodesic influences

The weight is independent of the outside-measurable threshold.  Atomlessness
therefore gives

`p_e=P(w_e<T_e)=integral_a^b q_e(t) rho(t) dt.`              (10)

For `a<=w<w'<=b`, the density lower bound implies

`integral_w^(w') q_e(t) dt
 <=alpha^(-1) integral_w^(w') q_e(t)rho(t)dt
 <=alpha^(-1)p_e.`                                          (11)

Expanding the square in (9) and averaging the two iid target weights gives

`E[m_e(w_e,w_e')^2]
 =integral_a^b integral_a^b q_e(s)q_e(t)
   F(min{s,t})[1-F(max{s,t})] ds dt,`

where `F` is the weight cdf.  Since `0<=F(min{s,t})<=F(max{s,t})<=1`,

`F(min{s,t})[1-F(max{s,t})]<=1/4.`

Using this kernel bound and then (10) with `rho>=alpha`,

`E[m_e(w_e,w_e')^2]
 <=(1/4)(integral_a^b q_e(t)dt)^2
 <=p_e^2/(4 alpha^2).`                                     (12)

The distinguished-coordinate companion defines

`C_edge=sum_e(E z_e)^2,`

`P_edge=sum_e Var(E[z_e|Y_e])`

and proves the exact identity

`C_edge+P_edge=sum_e E[m_e(Y_e)^2].`                         (13)

Summing (12) proves (3).

Only finitely many summands are nonzero for fixed endpoints.  A coordinate
path costs at most `b||v||_1`, while positive lower support `a` bounds the
length and range of every geodesic deterministically.

## 3. Published influence input

Corollary 1.3 of Dembin--Elboim--Peled,
[On the influence of edges in first-passage percolation on
`Z^d`](https://arxiv.org/abs/2307.01162v2), under exactly (1), gives for
`||v||>=2`

`sum_e p_e^2
 <=C_(d,G) ||v||^(2/(d+1)) (log ||v||)^d.`                  (14)

Combining (3) and (14) proves (4).  In `d=2`,

`C_edge+P_edge<=C ||v||^(2/3)(log ||v||)^2.`                (15)

The only new step here is the direct target-pair calculation (8)--(12).  No
novelty is claimed for the published influence estimate.

## 4. Why this is sharper than the gap detour

The gap companion first bounds `z_e` by `(T_e-w_e)^+` and then controls the
conditional mean of that larger variable.  That requires paying for the tail
`T_e>b`; a local plaquette detour gives the constant
`(alpha^(-1)+2b)^2` there.  Formula (8) retains `w_e'`, so it never integrates
past `b` and gives `1/(4alpha^2)` directly.  No deterministic upper bound on
`T_e` is used.

This sharper target estimate does not solve either remaining problem:

1. with single-edge product coordinates, the outside ANOVA mass `V_z` and its
   variance-weighted revealment are still uncontrolled;
2. for the campaign's large rectangular blocks, the passage time is not a
   verbatim.

The planar rate (15) also retains logarithms and is only comparable to the
conjectural `||v||^(2/3)` variance scale.

## 5. Break-it checks

* The density inequality in (11) goes in the required direction because
  `rho>=alpha`; no density upper bound is being substituted.
* Threshold values below `a` or above `b` cause no missing term.  Equation (8)
  intersects the threshold ray with the actual replacement interval
  `[w,w'] subset [a,b]`.
* The factor `1/4` in (12) is the deterministic maximum of
  `u(1-v)` over `0<=u<=v<=1`.  The product kernel uses only independence of the
  old and replacement target weights, not independence of thresholds across
  different edges.
* Ties in (6) have zero probability in the old environment under (1).  The
  deterministic identity (8) itself remains valid at `T_e=w` or `w'` because
  endpoints have zero Lebesgue length.
* The calculation is edge-specific.  It must not be advertised as a block-gap
  estimate or as control of the full spectral ledger.

An independent proof and source audit is required before (3)--(4) are used as
a campaign dependency.
