SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B07, 2026-09-24T00:40:21Z.
attacking: the r41 dense-internal-edge survivor and the low-diagonal projected-Z2 bank — convert determinant-weighted internal edges into one literal physical rank-three crossing by a single randomized coordinate cut, without selecting or dividing by one minor.

# fleet03/B07 r42 — projected-E2 weighted internal-cut compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Run: `20260924T004021Z-fleet03-B07-qform-r42`  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
Status: **NEW DIMENSION-FREE WEIGHTED-CUT THEOREM / r41 HIGH-DIAGONAL DENSE-EDGE BRANCH CLOSED / LOW-DIAGONAL INTERNAL-CURVATURE SURVIVOR SHARPENED / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

No Gaussian, log-concavity, moment, bounded-support, connected-support, iid, diagonal-basis, or post-rotation independence assumption is used. Every bank below consists of literal original coordinates. No individual determinant or coefficient is inverted.

## 1. Fresh scope and inputs


The immediate mathematical input is my r41 report

`yspennstate/math-open-problems@56c5b07296ce6fcc66cd3795e425cfad15b27aad`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T233906Z-fleet03-B07-qform-r41/REPORT.md`.

It works with pairwise-disjoint original-coordinate banks `H,I,J`, common physical crossing

`K=A[I,J]`,

and for each anchor `h in H`

`m_h=A[h,J]`,
`C_h=K(I-P_{m_h})`,
`Z_h=e2(C_h C_h^T)`.

Here `P_{m_h}` is the orthogonal projection in coefficient space onto `span(m_h)` when `m_h!=0`, and is zero when `m_h=0`. The one-overlap diagonal packet is

`S=sum_h a_h^2 Z_h > 2/3125`,  `a_h=A_hh`.                         (1.1)

r41 already paid the star-dominant part, the at-most-two-high-diagonal part, and a genuine three-coordinate partner-core part. At scale

`d=1/64`,                                                               (1.2)

the remaining high-diagonal failure was a graph on the high-diagonal anchors with independence number at most two and every graph edge satisfying

`|A_hk|>d/12=1/768`.                                                     (1.3)

The low-diagonal survivor was

`sum_{h in H_lo} Z_h > 0.65536 = 4096/6250`,                            (1.4)

with

`|A_hh|<1/64`, `||A[h,J]||_2<1/64` for every `h in H_lo`.                (1.5)

A fresh same-hour source audit found fleet02/B07's compatible r41 handoff and canonical report

`yspennstate/math-open-problems@81d6956476fa400f61d266effb4123a42fe3185c`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260924T003945Z-fleet02-B07-qform-auto11/REPORT.md`.

It independently turns the low-diagonal bordered packet into principal third-compound mass and gives an `E3(K)` / near-rank-two `K` / diffuse-diagonal-cloud router. I use its result only as a source audit and compatibility check below; no duplicate credit is claimed for that principal-compound identity.

The analytic receiver used below is the completed marginal-free physical third-volume crossing theorem: if a literal original-coordinate cross block `M` has

`Z3=e3(MM^T)>0`,

then the full ambient quadratic form has a **continuous** density with

`||p_Q||_infinity <= C3 Z3^(-1/6)`,
`C3=3*2^(4/3)*e^(1/3)=10.5501688311648...`.                         (1.6)

A completed source is fleet02/B03,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260923T184716Z-fleet02-B03-QFORM-auto11/REPORT.md`.

## 2. New fixed-oriented-edge determinant inequality

Let `h,k in H`, `h!=k`. Put

`b=A_hk`, `u=A[I,k]`.

Consider the literal cross block with row bank `{h} union I` and column bank `{k} union J`:

`M_hk = A[{h} union I, {k} union J]`.                                  (2.1)

For a fixed pair of rows `r<s` in `I`, collect only the `3x3` minors whose row triple is `{h,r,s}` and whose column triple is `{k,j,l}` with `j<l` in `J`. Their coefficients form the two-form

`Theta_rs = b k_r wedge k_s - u_r m_h wedge k_s + u_s m_h wedge k_r`,  (2.2)

where `k_r,k_s` are the corresponding rows of `K`, regarded as vectors in `R^J`.

Orthogonally project `Lambda^2(R^J)` onto `Lambda^2(m_h^perp)`. The last two terms in (2.2) vanish. Writing `c_r,c_s` for the rows of `C_h`, the first term becomes

`b c_r wedge c_s`.                                                       (2.3)

Orthogonal projection is a contraction, so

`sum_{j<l in J} det A[{h,r,s},{k,j,l}]^2
 >= b^2 ||c_r wedge c_s||^2`.                                           (2.4)

Summing in `r<s` and using the Cauchy--Binet identity for `e2(C_hC_h^T)` gives the key literal-coordinate inequality

`boxed:
 Phi_{h->k}:=sum_{r<s in I} sum_{j<l in J}
 det A[{h,r,s},{k,j,l}]^2
 >= A_hk^2 Z_h. `                                                       (2.5)

No cancellation estimate is used: the unwanted `u` terms are killed by an orthogonal exterior projection before norms are compared.

## 3. Dimension-free random-cut theorem

### Theorem 3.1 — `QFORM-PROJECTED-E2-WEIGHTED-INTERNAL-CUT-v1`

For the disjoint banks `H,I,J` and weights `Z_h` above, there exists a bipartition

`H=L disjoint_union R`                                                   (3.1)

such that the one literal physical cross block

`M=A[L union I, R union J]`                                              (3.2)

obeys

`boxed:
 e3(MM^T)
 >= (1/4) sum_{h<k in H} A_hk^2 (Z_h+Z_k). `                            (3.3)

### Proof

For a fixed cut, every oriented crossing pair `h in L`, `k in R` contributes the family of minors in (2.5). Families belonging to two different ordered pairs `(h,k)` are disjoint because the unique `H` row in the row triple is `h` and the unique `H` column in the column triple is `k`. Hence Cauchy--Binet gives

`e3(MM^T) >= sum_{h in L,k in R} A_hk^2 Z_h`.                           (3.4)

Assign every `h in H` independently to `L` or `R` with probability `1/2`. For an unordered pair `{h,k}`, the orientation `h in L,k in R` occurs with probability `1/4` and contributes `A_hk^2 Z_h`; the reverse orientation occurs with probability `1/4` and contributes `A_hk^2 Z_k`. Therefore

`E_cut [sum_{h in L,k in R} A_hk^2 Z_h]
 = (1/4) sum_{h<k} A_hk^2(Z_h+Z_k)`.                                    (3.5)

Some deterministic cut is at least its expectation. Combining (3.4)-(3.5) proves (3.3). QED.

This is exactly the requested aggregate-before-selection mechanism: all internal edges and all projected two-minor weights are averaged into one physical third-compound crossing before any coefficient is chosen.

## 4. Closing r41's high-diagonal dense-edge survivor

Return to r41's high-diagonal set `B_hi`. Define

`w_h=a_h^2 Z_h`,
`W=sum_{h in B_hi} w_h`.                                                 (4.1)

On this branch

`W >= S/4`.                                                              (4.2)

Apply the designated completed partner theorem

`fleet04/B07`,
`yspennstate/math-open-problems@dab16464e87c939cc0cf3fd01d070045290192fa`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B07/20260923T161510Z-fleet04-B07-coordinate-core-r2/REPORT.md`.

For three diagonals of magnitude at least `d`, if all three mutual off-diagonals have magnitude at most `d/12`, the partner's `r=0` coordinate-core theorem gives `s3>=3d/4`, hence the full-law essential-density bound recorded in r41. Therefore failure of that paid partner exit produces a graph `G` on `B_hi` such that

* `alpha(G)<=2`;
* every edge `{h,k}` satisfies `|A_hk|>d/12`.                            (4.3)

The following weighted argument closes this previously residual graph branch.

Set

`eta=d^2 W/4`.                                                           (4.4)

If some anchor satisfies

`a_h^4 Z_h >= eta`,                                                      (4.5)

then the completed marginal-free square-plus-`Z2` theorem used in r41 pays the full ambient law:

`||p_Q||_infinity <= 8 e^(1/4) eta^(-1/8)`.                             (4.6)

Assume no anchor satisfies (4.5). Because `|a_h|>=d`,

`w_h=a_h^2Z_h < eta/d^2 = W/4`.                                         (4.7)

Also

`Z_h = w_h/a_h^2 = w_h^2/(a_h^2 w_h) > w_h^2/eta`                       (4.8)

whenever `w_h>0`.

Now use the Caro--Wei inequality

`alpha(G) >= sum_h 1/(deg(h)+1)`.                                       (4.9)

Since `alpha(G)<=2`, Cauchy--Schwarz gives

`W^2
 <= [sum_h (deg(h)+1)w_h^2] [sum_h 1/(deg(h)+1)]
 <= 2 sum_h (deg(h)+1)w_h^2`,                                           (4.10)

so

`sum_h (deg(h)+1)w_h^2 >= W^2/2`.                                       (4.11)

Equation (4.7) implies

`sum_h w_h^2 <= (max_h w_h) W < W^2/4`.                                 (4.12)

Subtracting (4.12) from (4.11),

`sum_h deg(h) w_h^2 > W^2/4`.                                           (4.13)

Hence, by (4.8),

`sum_h deg(h) Z_h > W^2/(4 eta)`.                                       (4.14)

The weighted internal-edge quantity in Theorem 3.1 therefore satisfies

`sum_{{h,k} in E(G)} A_hk^2(Z_h+Z_k)
 > (d^2/144) sum_h deg(h)Z_h
 > d^2 W^2/(576 eta)
 = W/144`.                                                              (4.15)

Theorem 3.1 produces a literal physical crossing `M` with

`boxed: e3(MM^T) > W/576 >= S/2304. `                                   (4.16)

The marginal-free `Z3` receiver then pays the **full ambient law with a continuous density**.

Thus the entire r41 high-diagonal branch is now paid: partner physical core, square-plus-`Z2`, or a single determinant-weighted physical `Z3` cut. There is no longer an unpaid dense-edge graph.

### Numerical specialization

Using `S>2/3125`, `d=1/64`:

`W>S/4>1/6250`,

`eta=d^2 W/4 > 1/102400000 = 9.765625e-9`.                              (4.17)

The square-plus-`Z2` branch gives

`boxed: ||p_Q||_infinity < 103.027012.`                                  (4.18)

If it fails, (4.16) gives

`e3(MM^T)>1/3600000`,                                                    (4.19)

hence

`boxed: ||p_Q||_infinity < 130.610020`,                                  (4.20)

with continuity on this `Z3` exit. The partner three-coordinate core still has the weaker numerical bound `<1283.393677` from r41, so the whole high-diagonal branch is nevertheless uniformly paid.

## 5. New sharpening of the low-diagonal survivor

Apply Theorem 3.1 directly to the r41 low-diagonal bank `H_lo`. Put

`E_H := sum_{h<k in H_lo} A_hk^2(Z_h+Z_k)`.                              (5.1)

If

`E_H >= 1/12500`,                                                        (5.2)

then one physical cut has

`e3(MM^T)>=E_H/4 >=1/50000`,                                             (5.3)

and therefore the full ambient law has a continuous density satisfying

`boxed: ||p_Q||_infinity <= C3*50000^(1/6)
                         <64.035541. `                                   (5.4)

Assume instead

`E_H<1/12500`.                                                           (5.5)

For each anchor let

`r_h^2=sum_{k in H_lo, k!=h} A_hk^2`.                                   (5.6)

Then exactly

`E_H=sum_h Z_h r_h^2`.                                                   (5.7)

Let

`G0={h in H_lo: r_h<1/64}`.                                             (5.8)

The complementary anchors have `r_h^2>=1/4096`, so from (5.5)

`sum_{h notin G0} Z_h
 <=4096 E_H
 <4096/12500
 =0.32768`.                                                             (5.9)

Combining this with (1.4),

`boxed:
 sum_{h in G0} Z_h >0.32768. `                                          (5.10)

Every anchor in this surviving bank simultaneously obeys

`|A_hh|<1/64`,
`||A[h,J]||_2<1/64`,
`||A[h,H_lo\{h}]||_2<1/64`.                                             (5.11)

Thus a failure of the new continuous-density exit does not merely say that the average internal curvature is small: **at least half of the projected-`Z2` mass is carried by anchors whose entire internal star inside the low-diagonal bank has l2 norm below the same `1/64` scale as their diagonal and `J`-star.**

This is compatible with, and sharper on same-bank curvature than, the same-hour fleet02/B07 diffuse-diagonal-cloud stress test. That stress has zero internal edges, so it correctly survives (5.11); no bounded-cardinality core is inferred.

## 6. Why the proof is safe against the live corrections

* No rotated coordinate is declared independent.
* No pointwise quadratic-phase decay is used.
* No conditional density cap after a sum/difference transformation is used.
* No unrestricted joint-coarea estimate is used.
* No fiber supremum is integrated over a growing-dimensional complement.
* No individual principal/cross minor is inverted.
* All determinant mass is accumulated as literal Cauchy--Binet `e3` mass of one original-coordinate cross block before the analytic receiver is invoked.
* The same-bank tail is retained; Section 5 records the exact residual instead of deleting it.

## 7. Regression checks

A deterministic checker accompanies this report. It tests:

1. the fixed-oriented-edge inequality (2.5) by direct enumeration of all relevant `3x3` minors;
2. Theorem 3.1 by exhaustive enumeration of all cuts for small random finite symmetric matrices;
3. the weighted Caro--Wei consequence (4.13) on finite graphs with independence number at most two;
4. all numerical constants in Sections 4--5.

Finite computations are regression evidence only. The proof is Sections 2--5.

## 8. Remaining first implication

The r41 **high-diagonal** one-overlap diagonal-volume branch is now fully paid.

The surviving low-diagonal branch has been reduced further to a bank `G0` carrying projected mass

`sum_{h in G0} Z_h >0.32768`                                             (8.1)

with all three physical local quantities in (5.11) below `1/64`. Combining this with fleet02/B07's same-hour router, the sharp next debt is

`QFORM-R2-CARRIER-PLUS-LOWDIAG-LOWINTERNAL-CLOUD-RECEIVER-v1`:

pay a common physical crossing that is either already `Z3`-paid or quantitatively near rank two, together with a diffuse cloud of literal anchors having tiny diagonal, tiny `J`-star, and tiny same-bank internal l2 star, while retaining the nonzero crossing tail, arbitrary couplings through `I`/outside coordinates, and all extra spectrum.

The separate r40 skew-mismatch packet `sum_h ||m_h||^2 W(h)>2/3125`, the overlap-2 packets, and the principal-triple residual remain distinct debts.

Full QFORM remains **OPEN / not proved / not disproved**. Full-target continuity remains **OPEN**. Continuity is proved only on the physical-`Z3` exits in this report; the partner physical-core and square-plus-`Z2` gates provide essential boundedness in their stated scopes.
