SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-23T14:58:43Z.
attacking: QFORM-STAR4-THIRD-SPECTRAL-RESOURCE-ROUTING-v1 — force the third singular resource in the aligned STAR4 survivor into either a bounded-rank aligned skeleton or a quantitative original-coordinate self-bank off-diagonal packet.

# account03/B19 r36 — the third spectral resource cannot disappear into the aligned rank-two approximation

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Universal proof assembly / SYNTHESIS  
Status: **NEW TARGET-LEVEL STRUCTURAL DICHOTOMY / ESSENTIAL STEP APPLIED / FULL TARGET OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: not asserted by the new deterministic routing lemma; full-target continuity remains OPEN.

The unrestricted theorem is still OPEN. No Gaussian, moment, compact-support, connected-support, log-concavity, diagonal-basis or post-rotation-independence hypothesis is introduced. The argument below is deterministic matrix analysis on the actual physical-coordinate coefficient matrix, so it is valid for every admissible product input law and every sign pattern. Repeated singular values cause no problem: choose any top-two singular subspaces.

## 1. Sources actually consumed

Fresh owner control at the start of this run was `yspennstate/math-research-brain@0ca160119f6385f92605c6b5b61ea31d854880ab`, OWNER CONTROL revision `2026-09-22.15`.

The immediate B19 predecessor is

`yspennstate/math-open-problems@55fbef3fbe63cb7335851d9772449daac0ed67cf`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T142823Z-account03-B19-QFORM-r35/REPORT.md`.

It proved that the aligned null-hub + two-star + rank-two-cross packet alone is not an L-infinity receiver: an exact rank-two product-law family has logarithmically unbounded output density. Thus a genuine third spectral resource must be spent.

The quantitative STAR4 input and selected-volume identity are from account01/B19,

`yspennstate/math-open-problems@dc25fccd11312d65d1eae4b8efc947cf4bd475db`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/account01-B19-20260923T134858Z-auto11/REPORT.md`.

The designated partner theorem used at an actual inequality in Section 6 is account04/B19,

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260922T222052Z-account04-B19-QFORM-r2/REPORT.md`.

## 2. Exact aligned survivor entering this run

Fix the live no-pivot scale

`tau=2^-20`.

The current STAR4 quantitative-rank-two branch has a literal physical partition

`{h} disjoint_union J disjoint_union K`

of all coordinates, with

`u=A[J,h]`, `v=A[K,h]`, `N=A[J,K]`.

Write the singular values of `N` as `s_1>=s_2>=...` and put `x_r=s_r^2`,

`E=||N||_F^2`.

The source gives

`||u||^2>beta`, `||v||^2>beta`,

`beta=(1/12800-tau-2tau^2)/2
      =0.0000385856619323021732270717620849609375...`,          (2.1)

`E>E0=(1-tau)^2/4
      =0.24999952316306917055...`,                              (2.2)

`x_1+x_2+x_3+x_4>(63/64)E`,                                    (2.3)

and in the R2 branch

`s_2>s_1/16`,                                                   (2.4)

`rho:=s_1s_2>rho_*:=63(1-tau)^2/16384
                    =0.0038452075095882221056...`.              (2.5)

Let `P_2,Q_2` be any top-two left/right singular projections and let

`d_J^2=||(I-P_2)u||^2`, `d_K^2=||(I-Q_2)v||^2`.                 (2.6)

For the literal hub-bordered selected-volume currency, account01/B19 proves

`Gamma_J >= x_1x_2 d_J^2 + x_2x_3 ||P_2u||^2`,                 (2.7)

and symmetrically

`Gamma_K >= x_1x_2 d_K^2 + x_2x_3 ||Q_2v||^2`.                 (2.8)

The live selected-volume threshold is

`G_* = rho_*^2 beta/4
     =1.4262824133284200881e-10`.                               (2.9)

This run concerns the true aligned survivor in which neither the selected-volume Fourier payment nor the incident selected-volume anchor occurs. In that survivor

`Gamma_J<=G_*`, `Gamma_K<=G_*`.                                 (2.10)

Indeed, if (say) `Gamma_J>G_*`, then either all normalized physical-row inclusion probabilities are at most `1/2`, in which case the completed fractional selected-volume theorem pays the form, or one row carries more than half the selected volume, which is exactly the anchor alternative. Thus failure of both exits forces (2.10).

## 3. New quantitative sharpening: the aligned approximation is genuinely close in operator norm

First, (2.3)-(2.4) give an absolute lower bound for `x_2`. Since

`x_1<256x_2`, `x_3<=x_2`, `x_4<=x_2`,                           (3.1)

we have

`(63/64)E < x_1+x_2+x_3+x_4 <259x_2`.

Using `E>E0`,

`boxed:
 x_2 > 63 E0/(64*259) = (64/259) rho_*
     =0.0009501671066163946516... .`                            (3.2)

Next (2.7), (2.10), and `x_1x_2=rho^2>rho_*^2` imply

`d_J^2 < G_*/rho_*^2 = beta/4`,                                 (3.3)

and identically

`d_K^2 < beta/4`.                                                (3.4)

Hence

`||P_2u||^2>3beta/4`, `||Q_2v||^2>3beta/4`.                     (3.5)

Putting (3.2), (3.5) into the second term of (2.7) gives

`G_* >= Gamma_J > x_2 x_3 (3beta/4)`,

so

`boxed:
 x_3 < 4G_*/(3 beta x_2)
     < (259/192) rho_*
     =0.0051870247134549454446... .`                            (3.6)

This is substantially stronger than merely saying that the Frobenius tail is a small fraction of `E`: the first omitted cross singular value is now absolutely small at the fixed live constants.

## 4. Third-resource carrier dichotomy

Let `N_2=P_2NQ_2` be the top-two SVD truncation, and set

`u_2=P_2u`, `v_2=Q_2v`.

Write the physical self blocks

`B=A[J,J]`, `C=A[K,K]`, `a=A_hh`.

Define the **aligned skeleton**

`S = [[a, u_2^T, v_2^T],
      [u_2, 0,     N_2 ],
      [v_2, N_2^T, 0   ]]`,                                    (4.1)

and the self-bank matrix

`T = diag(0,B,C)`.                                               (4.2)

Then

`A=S+T+R`,                                                       (4.3)

where `R` contains only the two star misalignments and the cross tail `N-N_2`.

The star-error matrix has operator norm exactly at most

`sqrt(d_J^2+d_K^2)<sqrt(beta/2)`,                                (4.4)

while the symmetric cross-tail matrix has operator norm

`||N-N_2||_op=s_3=sqrt(x_3)`.                                   (4.5)

Therefore (3.6) gives

`boxed:
 ||R||_op < epsilon_*
 :=sqrt(beta/2)+sqrt((259/192)rho_*)
 =0.07641336241474038218... .`                                  (4.6)

Moreover `S` acts on

`span{e_h} + Ran(P_2) + Ran(Q_2)`,

so

`rank(S)<=5`.                                                    (4.7)

### Theorem 4.1 — `QFORM-STAR4-THIRD-RESOURCE-CARRIER-DICHOTOMY-v1`

In the aligned survivor (2.1)-(2.10), at least one of the following holds.

**(I) Aligned finite-rank carrier:**

`boxed: s_3(S)>=1/4, rank(S)<=5.}`                               (4.8)

Thus the missing third spectral direction is quantitatively present already in the explicit `1+2+2` aligned skeleton.

**(II) Original-coordinate self-bank carrier:** one of `B,C` satisfies

`boxed: ||B||_op>0.673586637585...}`                             (4.9)

(or the same statement for `C`). Since strict N3 gives every physical diagonal magnitude `<tau`, the winning bank has off-diagonal energy

`F_B:=sum_(i!=j) B_ij^2
     =||B-diag(B)||_F^2
     >0.4537176735697731.`                                      (4.10)

Furthermore that bank admits a literal original-coordinate bipartition `D_1 disjoint_union D_2` such that

`boxed:
 ||B[D_1,D_2]||_F^2>0.11342941839244327.}`                      (4.11)

#### Proof

The full target hypothesis implies

`s_3(A)>=1`,                                                     (4.12)

because at least three eigenvalues of the symmetric matrix have modulus at least one.

If (4.8) fails, Eckart--Young supplies a rank-at-most-two matrix `S_2` with

`||S-S_2||_op=s_3(S)<1/4`.                                      (4.13)

Again by Eckart--Young and (4.12), every rank-at-most-two approximation to `A` is at operator distance at least one. Hence, using (4.3),

`1 <= ||A-S_2||_op
   <= ||T||_op+||R||_op+||S-S_2||_op
   < ||T||_op+epsilon_*+1/4`.

Thus

`||T||_op>3/4-epsilon_*
          =0.6735866375852596... .`                              (4.14)

Since `||T||_op=max(||B||_op,||C||_op)`, one self bank obeys (4.9).

For that bank, `||diag(B)||_op<tau`; therefore

`||B-diag(B)||_op
 >=||B||_op-||diag(B)||_op
 >0.6735856839109432... .`                                      (4.15)

Frobenius norm dominates operator norm, which gives (4.10).

Finally color every coordinate of the winning bank independently into `D_1,D_2` with probability `1/2`. For each unordered off-diagonal edge `{i,j}`, its squared coefficient contributes to `||B[D_1,D_2]||_F^2` exactly when the endpoints receive opposite colors, an event of probability `1/2`. Since

`F_B=2 sum_(i<j)B_ij^2`,

we get

`E ||B[D_1,D_2]||_F^2 = F_B/4`.                                 (4.16)

Some deterministic bipartition therefore realizes at least this value, proving (4.11). QED.

The theorem is sign-free. It also includes the exact-rank-two cross endpoint `x_3=0`, where the cross-tail contribution in (4.6) vanishes. Repeated singular values are handled by fixing any top-two singular projection; every displayed exterior inequality remains valid.

## 5. What this actually buys in the end-to-end proof

The r35 obstruction showed that the local aligned rank-two bicore can remain logarithmically singular if the third spectral resource is ignored. Theorem 4.1 proves that in a **full target** matrix the third resource cannot hide arbitrarily weakly around that obstruction.

After the already-paid diffuse-window, D5 and selected-volume exits, the aligned R2 survivor now has only two mechanisms:

1. a quantitative third singular direction in an explicit rank-at-most-five aligned `1+2+2` skeleton; or
2. a quantitative off-diagonal packet inside one original-coordinate self bank, with total off-diagonal energy `>0.4537` and an actual disjoint physical cut of cross Frobenius square `>0.1134`.

This is a real strengthening over the predecessor's statement `s_3(A-diag A)>=1-tau`: it locates the third resource relative to the already-existing bicore rather than merely asserting global off-diagonal spectral energy.

It does **not** yet prove an L-infinity bound on either new carrier. In branch (II), the existing source-disjoint weighted-Fourier theorem cannot be invoked automatically because the new packet lies inside `J` or `K` and hence overlaps the active rank-two bicore; its cross couplings cannot be deleted. In branch (I), the five-dimensional skeleton is a deterministic grouped object, but the two-dimensional singular-coordinate groups are projections of product banks, not independent scalar coordinates. Treating them as independent would violate the live rotation correction.

Thus the first remaining implication is now the narrower

`QFORM-ALIGNED-SKELETON-OR-SELFPAIR-PAYMENT-v1`:

> pay either (I) the `s_3(S)>=1/4`, rank-at-most-five grouped `1+2+2` skeleton while retaining arbitrary same-bank physical curvature, or (II) the overlapping self-bank cut with cross Frobenius square `>0.113429`, jointly with the old rank-two `J-K` bicore, without requiring source-disjointness or deleting couplings.

A natural next mechanism is a coupled weighted-Fourier estimate in which the old rank-two `1/|t|` bicore factor and the new overlapping self-bank off-diagonal packet are integrated before absolute-value separation. The disjoint-packet theorem already proves this when the third packet is genuinely source-disjoint; the present theorem isolates precisely the extra overlap that must be handled.

## 6. Designated partner account04/B19 applied at an actual inequality

The completed partner theorem `QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1` proves, in its residual-diffuse exact-rank-three null-coloop normal form and for `0<D_res<=1`,

`||p_Q||_infinity <34 sqrt(log(e/D_res)).`                       (6.1)

On the actual proof-graph range

`e^-8<=D_res<=1`,                                                (6.2)

`log(e/D_res)<=9`, hence

`boxed: ||p_Q||_infinity <34*3=102.`                             (6.3)

This is an equation-level use of the designated partner result. I do not extend it to a near-coloop, to a non-diffuse residual, or to the overlapping STAR4 carrier above. The same partner source separately records the exact singular endpoint `<5.844` and the `D_res>=1` branch `<11.748`.

## 7. Compact conditional proof assembly and status

The strongest current assembly remains conditional rather than complete: the strict-N3 reduction, spectral-window diffuse exit, D5 exit, STAR4 compiler and selected-volume payment reduce the R2 aligned chamber to Theorem 4.1. The predecessor proves that no theorem using only the two-channel aligned bicore can close the chamber. The new theorem now forces the indispensable third resource into one of two quantitative, product-coordinate-aware carriers (4.8) or (4.10)-(4.11).

The unrestricted QFORM theorem is **OPEN / NOT PROVED / NOT DISPROVED**. Global continuous density is also **OPEN**. The new result is deterministic and therefore makes no continuity claim by itself. No full candidate is ready for the required two independent end-to-end reviews.

The accompanying `CHECK.py` evaluates the exact live constants and asserts

`x_2>(64/259)rho_*`,
`x_3<(259/192)rho_*`,
`epsilon_*<0.077`,
`F_B>0.453`,
`||B[D_1,D_2]||_F^2>0.113`,

ending with `QFORM_B19_R36_THIRD_RESOURCE_ROUTING_CHECK_PASS`.
