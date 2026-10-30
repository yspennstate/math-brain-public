# Refinement — three essential null directions suffice

This note strengthens `REPORT.md` Theorem 4.1. The earlier four-cluster theorem remains correct, but it unnecessarily demanded light mass in both physical clusters lying on the SAME spectral null line. In the two-plane coordinates those two null lines coincide exactly with `e2`. Exploiting that shared line improves both the hypothesis and the constants.

## Theorem — `QFORM-NULL-RULING-THREE-DIRECTION-CROSSCUT-v2`

Retain the exact-rank-three two-plane setup of `REPORT.md`:

`R_S^T R_S=diag(1,rho,0)`, `R_T^T R_T=diag(0,1-rho,1)`, `m_22=0`,
`A=R M R^T`, `s=min|eig(M)|`, `tau=min(rho,1-rho)`.

Let the S null lines be

`S0={x=0}=span(e2)`, `S1={m_11 x+2m_12 y=0}`,

and the T null lines be

`T0={v=0}=span(e2)`, `T1={2m_23 u+m_33 v=0}`.

Thus `S0` and `T0` are the same spectral line, even though they consist of disjoint original-coordinate source clusters. Let nearest-null projections be as in the preceding `QFORM-NULL-RULING-L1-TO-L2-v1`, and set

`eta=eta_S+eta_T`.

Assume

`eta <= tau^2/3600`.                                                   (R.1)

Then the predecessor mass/angle lemma applies automatically. In particular:

- projected mass on `S1` is at least `rho/12` and, for its unit direction `s=(a,b,0)`, `a^2>=rho/9`;
- projected mass on `T1` is at least `(1-rho)/12` and, for its unit direction `t=(0,c,d)`, `d^2>=(1-rho)/9`;
- the combined projected mass on the shared line `E:=S0 union T0` is at least `1/12`.

Put

`gamma=tau^2/3600`, `h0=gamma/2=tau^2/7200`.                          (R.2)

Assume the projected squared mass carried by rows with ACTUAL leverage `||r_i||^2<=h0` is at least

`rho/48` on S1, `(1-rho)/48` on T1, and `1/48` on the COMBINED shared-line cluster E.    (R.3)

No separate light-mass assumption is required on S0 and T0.

Then there is an original-coordinate partition `I sqcup J` such that

`R_I^T R_I >= gamma I_3`, `R_J^T R_J >= gamma I_3`,

and every I row has range leverage at most `1/2`. Consequently Claude's completed three-volume theorem at `e5f71d79eff325201dd0274053d20268ce65b837` gives

`boxed: ||p_(X^T A X)||_infinity <= 21600 sqrt(e)/(s tau^2).`         (R.4)

The source-stability theorem at `c2414ef633b9d4b7f04a83e1aeefbe713ed82bba` further gives, for `A_full=A+H`,

`boxed: ||p_(X^T A_full X)||_infinity <82800/(s tau^2)`               (R.5)

whenever the actual cross-tail on this cut obeys `||H[I,J]||op<=s gamma/16`. The review status of (R.5) is inherited from that source.

## Proof

Select I only from light original coordinates. On S1 greedily accumulate projected squared mass until first reaching `rho/96`; on T1 use `(1-rho)/96`; on the combined shared cluster E use `1/96`. Because every selected projected weight is at most `h0`, and `h0<=tau/96`, each selected mass is at most twice its threshold. Therefore the I projected masses satisfy

`mu_s in [rho/96,rho/48]`,
`mu_t in [(1-rho)/96,(1-rho)/48]`,
`mu_e in [1/96,1/48]`.                                                (R.6)

All other original coordinates, including every heavy row, go to J. The predecessor total-mass bounds imply

`mu_s^J>=rho/16`, `mu_t^J>=(1-rho)/16`, `mu_e^J>=1/16`.               (R.7)

The projected Gram on either cut has the form

`K=mu_s ss^T + mu_e e2 e2^T + mu_t tt^T`.                             (R.8)

We bound its least eigenvalue without a determinant/trace loss. Let L have rows `sqrt(mu_s)s^T`, `sqrt(mu_e)e2^T`, `sqrt(mu_t)t^T`, so `K=L^T L`. For `y=Lx`,

`x_2=y_2/sqrt(mu_e)`,
`x_1=(y_1/sqrt(mu_s)-b x_2)/a`,
`x_3=(y_3/sqrt(mu_t)-c x_2)/d`.

Hence

`||x||^2 <= A1 y_1^2 + A2 y_2^2 + A3 y_3^2`,                         (R.9)

with

`A1<=2/(mu_s a^2)`, `A3<=2/(mu_t d^2)`,
`A2<=(1+2/a^2+2/d^2)/mu_e`.                                          (R.10)

For I, (R.6) and the angle bounds give

`A1,A3 <=1728/tau^2`,
`A2 <=96[1+18/rho+18/(1-rho)]
    <=96(1+36/tau)
    <=1800/tau^2`,                                                    (R.11)

where the last inequality holds for `0<tau<=1/2`. Thus

`K_I >= (tau^2/1800) I_3`.                                           (R.12)

For J, (R.7) gives

`A1,A3<=288/tau^2`,
`A2<=16(1+36/tau)<=300/tau^2`,                                       (R.13)

so

`K_J >= (tau^2/300) I_3`.                                            (R.14)

The actual/projected Gram error on either cut is at most `eta`. By (R.1),

`G_I>=tau^2/1800 I-eta I >=gamma I`,
`G_J>=tau^2/300 I-eta I >=gamma I`.                                  (R.15)

Every I row is light, so `r_i^T G_I^{-1}r_i<=h0/gamma=1/2`.

For the ACTUAL cross block `C=A[I,J]=R_I M R_J^T`, exactly as in `REPORT.md`,

`Z=e_3(C^T C)=det(M)^2 det(G_I)det(G_J)>=s^6 gamma^6`,                (R.16)

and the rank-three volume row marginal is `r_i^T G_I^{-1}r_i<=1/2`. Claude Theorem D therefore gives

`||p_Q||inf<=6sqrt(e)Z^(-1/6)<=6sqrt(e)/(s gamma)
            =21600sqrt(e)/(s tau^2)`,

which is (R.4). Also `s_3(C)>=s gamma`; the current matrix-stability theorem yields (R.5).

## Sharpened failure classification

Define the heavy set `H={i:||r_i||^2>h0}`. Since the total frame leverage is three,

`|H| < 3/h0 =21600/tau^2`.                                           (R.17)

If (R.3) fails, then H carries projected mass more than `tau/16` on at least one of the THREE essential null directions `S1`, `T1`, or the combined shared line E. Indeed the relevant total masses are at least `rho/12`, `(1-rho)/12`, and `1/12`, while the allowed light masses are `rho/48`, `(1-rho)/48`, and `1/48`.

Thus the remaining B11 branch is now more precise than in `REPORT.md`: a bounded-cardinality heavy-spike set carries macroscopic mass on one essential null direction. The two shared-line source clusters need not be treated separately. The next unpaid implication is

`QFORM-NULL-RULING-FINITE-SPIKE-INTERPOLATION-v2`:

use those finitely many heavy ORIGINAL coordinates jointly with the residual light banks through a source-preserving hub/pair/Schur receiver, or force an already-paid pivot/pair/volume exit. Near-zero nonzero pivots may not be replaced by exact zero.

## Sign and logarithmic interpretation

The sign-specific splice is unchanged: for signature `(+, +, -)`, the pinned ruled theorem gives `p_Q(t)<=pi sqrt(2)/s` only on `t>=0`; reflection handles the majority-sign half-line of `(+, -, -)`. The opposite two-sheet side in this branch is paid by (R.4).

The rank-two saddle remains genuinely logarithmic (`p_(2XY)(t)=log(1/(2|t|))` for centered unit uniforms). The three essential null directions above create a genuine third singular direction in the ACTUAL original-coordinate cross block, so Claude's decoupling estimate gains the integrable `|t|^(-3/2)` decay rather than the rank-two `|t|^(-1)` endpoint. No rotated-coordinate independence is used.
