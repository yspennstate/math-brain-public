SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B13, 2026-09-24T01:46:13.729913Z.
attacking: partner r40 four-point tau rigidity on the r38 tau-clean physical e2 crossing; force a dimension-free physical star or low-score tau-clean bank, then retain pinned D5 on the same physical-crossing interface.

# account02/B13 r39 — tau-clean physical star or low-score e2 bank

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: extremal product laws / complementary constructions and source-valid counterexamples  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **new supporting theorem proved; full unrestricted QFORM remains OPEN / NOT PROVED / NOT DISPROVED; continuity remains separate.**

No moment, compact-support, connected-support, Gaussian, log-concavity, diagonal-basis, post-rotation independence, attained bathtub optimizer, common support diameter, fixed fragment count, or perturbative deletion of a coefficient-small quadratic form is used.

## 1. First unpaid implication

The first unpaid implication is now

`QFORM-LOWSCORE-PIVOT-TRIPOD-BANK-RECEIVER-v1`:

> In the hard diffuse exact-rank-two survivor, pay an actual original-coordinate cross-bank two-volume exceeding `e^2 rho^-4` whose contributing tau-clean row pairs satisfy the pivot-tripod score `q_ij q_ki q_kj <331 rho^-1`, without dividing by one individual star determinant and without imposing support/moment assumptions. The complementary branch is already a single physical-center star of the same two-volume scale. Retain the pinned `s_5=O(rho^-1)` obstruction on every physical cross cut in the general survivor. If this endpoint cannot be paid, construct a genuine bounded-finite-union product-indicator counterexample.

This is narrower than partner r40's `QFORM-TAUCLEAN-E2-WEIGHTED-4CYCLE-OR-STAR-v1`: the weighted four-cycle/star selection is discharged below, leaving only a low pivot-tripod-score bank or one physical center.

## 2. Fresh source-pinned premises

Fresh owner control remained QFORM-only, OWNER CONTROL revision `2026-09-22.15`, with no pause/stop on account02/B13. The full theorem remains open. The latest completed compatible designated-partner result is account03/B13 r40, canonical report commit

`2dc90715428202b4218a60df0d3efe79bfff4055`,

with checker output commit

`f2eb2bed996ce7dddcc5f8a7d96cd36ec33a366c`

and publication refresh commit

`2eb4f32a1015b73a18e6277dadc09e080a3d71f7`.

Its hard diffuse exact-rank-two chamber is

`A=D+U Lambda U^T`, `U^T U=I_2`, `max_i ||u_i||^2<=1/3`, `s_3(A)>=1`.      (2.1)

A physical pivot `k` satisfies `|d_k|>=1`. Put

`q_ij=det(u_i,u_j)^2`                                                (2.2)

and, for physical pairs `{a,b}` away from `k`,

`Delta_ab=det(U_[n]\\{k,a,b}^T U_[n]\\{k,a,b})`,
`tau_ab=d_k q_ab+d_a q_kb+d_b q_ka`.                               (2.3)

In the hard non-rank-one branch,

`|det Lambda|>H0 rho^(-2)`, `H0=sqrt(1536 e^2)=106.534455308869...`,
`|A_kk|<=H0 rho^(-2)`.                                               (2.4)

The grouped three-leaf supporting theorem used by r40 gives

`Delta_ab (det Lambda)^2 |tau_ab| <= C_T rho^(-5)`,
`C_T=759375/2=379687.5`.                                             (2.5)

Partner r40 also proves, after rotating only the deterministic two-dimensional coefficient basis so

`u_k=(sqrt(c),0)`, `u_i=(x_i,y_i)`, `s_i=y_i^2`, `t_i=x_i/y_i`,     (2.6)

the exact four-point identity

`G_ij+G_lm-G_il-G_jm=-2d_k(t_i-t_m)(t_j-t_l)`,
`G_ab=tau_ab/(s_a s_b)`,                                            (2.7)

whenever the four displayed `s` values are positive. Its checker records the exact algebra/constant checks as passing.

The input from my preceding account02/B13 r38, commit

`3da714c7dea66b4f81087bf9637a6eac060b5b6a`,

is the actual physical tau-clean crossing. It gives a physical cut `C|C^c` of `[n]\\{k}` and good pair set

`G={E={i,j}: |tau_E|<=T rho^(-1)}`, `T=535.261618270...<536`,        (2.8)

for which, writing

`X=sum_{E subset C, E in G}q_E`,
`Y=sum_{F subset C^c, |F|=2}q_F`,                                  (2.9)

one has

`(det Lambda)^2 X Y >=(det Lambda)^2/384`.                         (2.10)

The owner-required pinned source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

Its completed unconditional fifth-volume theorem `D5` says, for every disjoint physical cross block `B=A[I,J]`,

`||p_Q||_infty <=5 sqrt(2e) e_5(B^T B)^(-1/10)`.                  (2.11)

The counterexample search reports no valid counterexample in its tested families; no numerical observation from that search is used as proof.

## 3. The r38 cut gives a uniform complement-volume floor

Cauchy-Binet for the rank-two Parseval frame gives

`sum_{|E|=2} q_E=det(U^T U)=1`.                                    (3.1)

From (2.10),

`XY>=1/384`.                                                        (3.2)

Because `X<=1` and `Y<=1`, separately

`X>=1/384`, `Y>=1/384`.                                            (3.3)

This elementary observation is useful because it removes every complementary-minor denominator on the entire row side of the selected physical cut. For every pair `P={a,b} subset C`,

`Delta_P=sum_{F subset [n]\\{k,a,b}, |F|=2}q_F`
`       >=sum_{F subset C^c, |F|=2}q_F=Y>=1/384`.                 (3.4)

Combining (3.4), (2.4), and (2.5),

`|tau_P|`
` <= C_T rho^(-5)/(Delta_P (det Lambda)^2)`
` <=384 C_T/H0^2 rho^(-1)`
` =L rho^(-1)`,                                                     (3.5)

where

`L=C_T/(4e^2)=12846.278838475346...`.                              (3.6)

Thus **every** pair inside `C` has `tau=O(rho^-1)`, not only the r38-good pairs. This is an aggregate consequence of the physical cut and is the key to applying r40's four-point identity without selecting or inverting one favorable minor.

## 4. Denominator-free score bound for two disjoint good edges

Assume first `c=||u_k||^2>0`; partner r40 already shows `c=0` forces `rho<sqrt(H0)=10.322...`, so that case is already universally paid.

Let

`E={i,j}`, `E'={l,m}`                                               (4.1)

be vertex-disjoint good pairs inside `C`. If one endpoint has `s=0`, the score defined below is zero and the desired inequality is automatic. Hence suppose all four `s` values are positive.

Multiply the exact r40 identity (2.7) by `s_i s_j s_l s_m`:

`tau_ij s_l s_m +tau_lm s_i s_j -tau_il s_j s_m -tau_jm s_i s_l`
` =-2 d_k s_i s_j s_l s_m (t_i-t_m)(t_j-t_l)`.                   (4.2)

Because the two base pairs are good,

`|tau_ij|,|tau_lm|<536 rho^(-1)`,                                 (4.3)

while (3.5) gives

`|tau_il|,|tau_jm|<=L rho^(-1)`.                                  (4.4)

Also every `s_a<=||u_a||^2<=1/3`. Since

`q_im=s_i s_m(t_i-t_m)^2`, `q_jl=s_j s_l(t_j-t_l)^2`,             (4.5)

(4.2)-(4.4) and `|d_k|>=1` imply

`sqrt(s_i s_j s_l s_m q_im q_jl)`
` <=(536+L)/(9 rho)`.                                              (4.6)

For the same four coefficient rows, the Pluecker relation gives

`p_ij p_lm-p_il p_jm+p_im p_jl=0`, `q_ab=p_ab^2`.                 (4.7)

Consequently

`max(q_il q_jm,q_im q_jl)>=q_ij q_lm/4`.                          (4.8)

Use whichever orientation of (4.2) places the larger cross matching on its right side. Define the physical pivot-transverse score

`a_E:=q_E s_i s_j`.                                                (4.9)

Then (4.6)-(4.8) prove the dimension-free pair inequality

`boxed: sqrt(a_E a_E') <=K rho^(-1) for every disjoint good E,E'`, (4.10)

where the safe explicit constant is

`K=2(536+L)/9=2973.839741883410...<2974`.                          (4.11)

If an endpoint has `s=0`, its score is zero, so (4.10) remains valid without a separate nondegeneracy assumption.

A useful immediate interpretation is that the high-score graph

`H={E subset C: E good, a_E>K/rho}`                                (4.12)

has matching number at most one. Hence its edge family is a star or a triangle (or smaller). This is already a finite-center conclusion, but the weighted theorem below is stronger because it preserves a fixed positive fraction of the actual cross two-volume.

## 5. Main theorem — physical star or low-score e2 bank

### Theorem `QFORM-TAUCLEAN-PHYSICAL-STAR-OR-LOWSCORE-E2-v1`

Under (2.1)-(2.10) and the hard branch (2.4), there is the r38 physical cut `C|C^c` for which one of the following alternatives holds.

**Star alternative.** There is a physical coordinate `h in C` such that

`Z_star:=sum_{E subset C, E good, h in E}`
`          sum_{F subset C^c, |F|=2} det A[E,F]^2`
`       >e^2 rho^(-4)`.                                           (5.1)

**Low-score-bank alternative.** There is a set `L0` of good physical pairs `E={i,j} subset C` such that every `E in L0` satisfies

`q_E s_i s_j<=K/rho<2974/rho`                                     (5.2)

and

`Z_low:=sum_{E in L0}sum_{F subset C^c, |F|=2}det A[E,F]^2`
`      >e^2 rho^(-4)`.                                             (5.3)

Moreover, since `q_ki=c s_i`, every low-score pair obeys the pivot-tripod inequality

`boxed: q_ij q_ki q_kj <= c^2 K/rho <= K/(9rho)<331/rho`.         (5.4)

### Proof

Normalize the r38-good pair weights on `C`:

`p_E=q_E/X`.                                                       (5.5)

For a physical vertex `v in C`, let

`r_v=sum_{E good, E subset C, v in E}p_E`.                         (5.6)

Every edge contributes to two marginals, so

`sum_v r_v=2`.                                                     (5.7)

If some `r_h>=1/4`, then the good q-mass of the star at `h` is at least `X/4`.

Otherwise `max_v r_v<1/4`. Sample two independent good edges `E,E'` with law `p`. A union bound over their common endpoint gives

`P(E cap E' nonempty)<=sum_v r_v^2`
`                    <=(max_v r_v) sum_v r_v<1/2`.                (5.8)

Hence the ordered q-weight of vertex-disjoint good pairs exceeds `X^2/2`.

Let

`L0={E good, E subset C: a_E<=K/rho}`.                             (5.9)

By (4.10), two edges outside `L0` cannot be disjoint. Thus every ordered disjoint pair has at least one member in `L0`. Its total ordered q-weight is at most

`2X sum_{E in L0}q_E`.                                             (5.10)

Together with the lower bound `X^2/2`, this gives

`sum_{E in L0}q_E>=X/4`.                                          (5.11)

So in all cases there is either a star subset or a low-score subset of the good row pairs carrying q-mass at least `X/4`.

For disjoint physical pairs `E subset C`, `F subset C^c`, the diagonal part of `A` vanishes across the cut and

`det A[E,F]^2=(det Lambda)^2 q_E q_F`.                             (5.12)

Therefore either selected subset has physical two-volume at least

`(det Lambda)^2 (X/4)Y`
` =(det Lambda)^2 XY/4`
` >=(det Lambda)^2/1536`
` >e^2 rho^(-4)`,                                                  (5.13)

using (2.10) and `(det Lambda)^2>1536 e^2 rho^-4`. This proves (5.1) or (5.3). Finally (5.4) follows from `q_ki=c s_i`, `q_kj=c s_j`, (5.2), and `c<=1/3`. QED.

The constants are deliberately not optimized. The structural point is that the positive aggregate r38 crossing cannot evade r40's four-point rigidity by spreading mass over infinitely many tiny pairs: either a fixed physical center captures a slab-scale two-volume, or a fixed positive two-volume survives on a bank where every row pair has quantitatively tiny simultaneous transversality to the pivot.

## 6. Extremal product laws — transfer without a global optimizer

The optimizer-free product-law reduction remains at exactly its valid scope. For every bounded nonnegative slab kernel `K`, the cap-one product supremum can be approximated by products of unit-measure indicators, and strict witnesses can be approximated by bounded finite unions. At the elementary transfer level, if marginal densities `f_i,g_i` have unit mass,

`||prod_i f_i-prod_i g_i||_1 <=sum_i ||f_i-g_i||_1`.              (6.1)

Thus a strict bad slab for arbitrary independent cap-one densities transfers with arbitrarily small loss to a bounded-finite-union product-indicator witness after finite-mixture expansion. Nothing asserts that the optimizing sets are intervals, centered, bounded with a uniform diameter, or bounded in fragment count. Separated/unbounded original supports remain admissible in the limiting problem.

The theorem in Section 5 is coefficient-only and therefore survives this approximation unchanged. In particular, any counterexample sought at this endpoint may be sought through such finite-union product witnesses only in the approximation sense; there is still no attained global bathtub optimizer assumption.

## 7. Required pinned Fourier result applied to the surviving obstruction

Apply the owner-pinned unconditional D5 theorem (2.11) to an arbitrary physical cross block `B=A[I,J]` in any target-class slab witness of ratio `rho`. Rearranging gives

`e_5(B^T B)<=(5 sqrt(2e)/rho)^10`.                                (7.1)

Since

`e_5(B^T B)>=s_1(B)^2...s_5(B)^2>=s_5(B)^10`,                    (7.2)

we get the concrete universal physical-cut obstruction

`boxed: s_5(A[I,J])<=5 sqrt(2e)/rho`
`                    =11.6582199079856.../rho`.                   (7.3)

This is a genuine inequality on every physical cross cut. In the exact `D+U Lambda U^T` chamber used in Sections 3-5, all such off-diagonal cross blocks have rank at most two and D5 is identically blind; the new star/low-score theorem attacks exactly that endpoint. In a general high-density survivor, however, (7.3) says any extra cross interaction attached to either branch can have at most four singular directions above the same `O(rho^-1)` scale. The tail is **not** discarded as a random quadratic perturbation on rough/unbounded inputs; (7.3) is retained only as a spectral obstruction.

This meets the owner requirement to apply a completed result from the pinned Claude/Fourier source to an actual surviving obstruction.

## 8. Exact remaining gap

The weighted four-cycle/star problem posed by partner r40 is now replaced by one explicit analytic endpoint. In the star branch (5.1), a single original coordinate anchors an `e_2`-mass `>e^2 rho^-4`, so the configuration routes into the existing finite-center/hub family. The genuinely new unresolved branch is (5.2)-(5.4): an actual physical crossing carries `>e^2 rho^-4` of squared two-minor mass, all its row pairs are tau-clean, yet each has very small triple product with the two pivot spokes.

A closure theorem must consume this aggregate low-score currency without selecting one favorable pair and dividing by `q_ki q_kj`. Equivalently, it must show that such a bank either becomes product-payable through a diffuse/hub Fourier receiver, collapses the rank-two coefficient frame toward one projective direction after finitely many physical deletions, or produces a valid finite-union product-indicator counterexample. No such theorem is claimed here.

## 9. Deterministic checks

A symbolic expansion of r40's four-point cross-difference after multiplying denominators gives residual zero. The recorded arithmetic checks are

`L=12846.278838475346...`,
`K=2973.839741883410...`,
`K/9=330.426637987046...`,
`5 sqrt(2e)=11.658219907985622...`.

The physical branch normalization was also checked:

`(det Lambda)^2 XY/4 >=(det Lambda)^2/1536 >e^2 rho^-4`.

The saved `CHECK_OUTPUT.txt` records these values. No benchmark, Monte Carlo, or numerical counterexample claim is used.

## 10. Status

Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Global continuity remains OPEN. The new theorem is a supporting exact structural reduction in the diffuse exact-rank-two hard chamber. It preserves arbitrary fragmented cap-one product inputs and original-coordinate provenance throughout.
