SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-23T04:59:48Z.
attacking: close the two-coordinate approximate-cocircuit branch by replacing the failed balanced inclusion/exclusion law with an exact two-bank capped Pluecker law.

# account03/B16 r26 — two-bank cocircuit Fresnel closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `NEW SUPPORTING THEOREM / STRICTER EXACT-RANK-THREE REDUCTION / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** proved on the new paid branch; global continuity remains open.

## 1. Target, control, and source boundary

The owner target remains the unrestricted statement: for every finite `n`, independent real original-coordinate variables `X_k` with probability densities `0<=f_k<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has a density with one universal finite `L^infinity` bound, or give a valid counterexample. No moment, compact-support, connected-support, log-concavity, Gaussianity, or spectral-coordinate independence assumption is made.

Fresh owner control was read from `yspennstate/math-research-brain@8be2516e16b25148c91fe571f08dbf44cc2eedfe`; OWNER CONTROL is revision `2026-09-22.15`, QFORM only. The live correction inbox was reread. In particular, this report does not use arbitrary-joint 3D coarea, conditional projection-height moments, worst-fiber suprema, small-coefficient deletion, or law-uniform pointwise one-dimensional van der Corput decay.

The immediate B16 predecessor is

`yspennstate/math-open-problems@ed79d5f9d8a99c466397114723e3695d49bf9044`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260923T035222Z-account03-B16-QFORM-r25/REPORT.md`.

Its exact-rank-three notation is retained. Write

`A=R Lambda R^T`, `R^T R=I_3`, `D:=|det Lambda|>=1`,

and fix an original coordinate `i` with

`r_i=sqrt(c)e`, `0<c<1`, `a:=1-c`.

For `k!=i`, decompose only the deterministic coefficient rows

`r_k=s_k e+w_k`, `w_k perpendicular e`, `h_k=||w_k||^2`.

Then Parseval gives

`sum_(k!=i) s_k^2=a`,
`sum_(k!=i) s_k w_k=0`,
`sum_(k!=i) w_k w_k^T=I_2`.                                    (1.1)

No random variable has been rotated.

The completed analytic input used below is account01/B18 `QFORM-FRESNEL-CAPPED-BASIS-WEIGHTS-v1`, canonical source

`yspennstate/math-open-problems@8c04ccbc1f032d1a82ad505223f08e3c344bde74`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/20260922T225705Z-qform-B18-a01-r19/REPORT.md`.

For the rank-three coefficient frame, if `w=(w_S)` is any probability law on nonsingular physical three-element bases and every coordinate marginal

`alpha_k=P_w(k in S)`

satisfies `alpha_k<=1/2`, then the original-product quadratic form has a continuous density with

`||p_Q||_infinity <=3e (D Z_w)^(-1/3)`,                         (1.2)

where

`Z_w=exp(H(w)+sum_S w_S log det(R_S)^2)`.                       (1.3)

This theorem operates directly on the original product characteristic function through Hausdorff--Young and Brascamp--Lieb, so it is compatible with the live corrections.

## 2. The hard branch inherited from r24-r25

The r24 residual chamber has a dominant physical row with

`c>c_*:=643/7936>1/64`.                                        (2.1)

The designated partner account04/B16 is already source-valid here. Its theorem `QFORM-RULED-PLUECKER-ENDPOINT-v1`, canonical source

`yspennstate/math-open-problems@b111363ff02b67015d14db35482e0150591744cd`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260922T231542Z-account04-B16-QFORM-r1/REPORT.md`,

proves for the disjoint-Pluecker probability `d`

`||p_Q||_infinity <=12 D^(-1/3)d^(-1/6)`.                      (2.2)

Hence at the actual branch threshold

`d>=1/64  =>  ||p_Q||_infinity<=24`.                            (2.3)

This is the equation-level application of the designated partner result in this run. We therefore work only in the complementary `d<1/64` branch.

R24 further proves that if any residual transverse leverage satisfies `h_k>=1/64`, then

`||p_Q||_infinity<865`.                                         (2.4)

Thus the only branch relevant below has

`h_k<1/64` for every `k!=i`.                                    (2.5)

R24-r25 also prove that the balanced duplicated-slice gate

`h_k+s_k^2/(2a)<=1/2 for all k!=i`                              (2.6)

is paid by a continuous-density Fresnel estimate. If (2.6) fails at a unique possible coordinate `j`, then

`h:=h_j<1/64`,
`s^2/a>1-2h>31/32`,                                             (2.7)

and the natural Pluecker basis law places more than `63/64` of its mass on bases containing exactly one of `{i,j}`. The prior report identified this as an approximate two-element cocircuit but did not yet pay it.

The purpose of this run is to pay that entire gate-failure branch whenever the hub is not itself a near-coloop, i.e. whenever

`a=1-c>=1/64`.                                                   (2.8)

## 3. Exact one-of-two Pluecker bank ledger

For every physical basis `S`, put

`v_S=det(R_S)^2`.

Because `R^T R=I_3`, Cauchy--Binet gives `sum_S v_S=1`.

Fix a gate-failing `j` as in (2.7) and put `K={1,...,n}\{i,j}`. Define the two disjoint basis banks

`B_i={S: i in S, j notin S}`,
`B_j={S: j in S, i notin S}`.                                  (3.1)

Let

`P_i=sum_(S in B_i) v_S`,
`P_j=sum_(S in B_j) v_S`.                                      (3.2)

R25's one-row inclusion identities give exactly

`P_i=c(1-h)`,                                                    (3.3)

and, writing

`q=h+s^2/a`,                                                     (3.4)

`P_j=s^2+a h=a q`.                                               (3.5)

The gate failure `h+s^2/(2a)>1/2` is equivalent to

`q>1-h`.                                                         (3.6)

Under (2.1), (2.5), and (2.8), therefore

`P_i> (1/64)(63/64)=63/4096`,                                  (3.7)

`P_j> (1/64)(63/64)=63/4096`.                                  (3.8)

These lower bounds are deterministic and dimension-free.

## 4. New basis law: half of each cocircuit bank

Define a probability law `w` on bases by

`w_S=v_S/(2P_i)` for `S in B_i`,
`w_S=v_S/(2P_j)` for `S in B_j`,
`w_S=0` otherwise.                                               (4.1)

Thus each bank has `w`-mass exactly `1/2`, and immediately

`alpha_i=alpha_j=1/2`.                                          (4.2)

The essential point is that every remaining coordinate has much smaller marginal under this law.

### Lemma 4.1 — `QFORM-COCIRCUIT-TWOBANK-MARGINALS-v1`

Under (2.5), (2.7), and (2.8), for every `k in K`,

`P_w(k in S)<13891/249984<0.056<1/2`.                           (4.3)

#### Proof: the `i`-bank

On a basis `{i,k,l}` with `k,l in K`,

`det(r_i,r_k,r_l)^2=c det(w_k,w_l)^2`.                           (4.4)

The transverse Gram matrix of the rows in `K` is

`G_i=sum_(k in K) w_k w_k^T=I_2-w_jw_j^T`.                      (4.5)

Its smallest eigenvalue is `1-h>63/64`. The standard two-dimensional Cauchy--Binet inclusion identity therefore gives the conditional bank marginal

`beta_k:=P_v(k in S | S in B_i)=w_k^T G_i^(-1)w_k`.             (4.6)

Hence

`beta_k<=h_k/(1-h)<(1/64)/(63/64)=1/63`.                        (4.7)

#### Proof: the `j`-bank

Put

`m=||r_j||^2=s^2+h`,
`u=r_j/sqrt(m)`,
`P=I_3-u u^T`,
`q_k=P r_k` for `k in K`.                                      (4.8)

All `q_k` lie in the two-dimensional plane `u^perp`. Since `P r_j=0`, their Gram matrix is, on `u^perp`,

`G_j=sum_(k in K) q_kq_k^T
    =I_(u^perp)-q_iq_i^T`.                                     (4.9)

Now

`||q_i||^2
 =c-<r_i,r_j>^2/m
 =c-cs^2/m
 =c h/m`,                                                       (4.10)

so

`lambda_min(G_j)=1-c h/m`.                                     (4.11)

Gate failure and `h<1/64` imply

`s^2/a>1-2h>31/32`,                                             (4.12)

hence

`m=s^2+h>(31/32)a+h`.                                           (4.13)

Using `a>=1/64`, `c<=1`, and `h<1/64`,

`c h/m
 < h/[(31/32)a+h]
 <= (1/64)/(31/2048+1/64)
 =32/63`.                                                        (4.14)

Therefore

`lambda_min(G_j)>31/63`.                                       (4.15)

For the `j`-bank the two-dimensional Cauchy--Binet inclusion identity gives

`gamma_k:=P_v(k in S | S in B_j)=q_k^T G_j^(-1)q_k`.            (4.16)

Also, by (1.1) and (4.12),

`sum_(k in K) s_k^2=a-s^2<2ah<a/32`,                           (4.17)

so each

`||r_k||^2=s_k^2+h_k<a/32+1/64<=3/64`.                         (4.18)

Since `||q_k||<=||r_k||`, (4.15)-(4.18) yield

`gamma_k<(63/31)(3/64)=189/1984`.                              (4.19)

Finally the law (4.1) mixes the two conditional banks equally, so

`alpha_k=(beta_k+gamma_k)/2
 <(1/2)(1/63+189/1984)
 =13891/249984
 <1/2`.                                                          (4.20)

QED.

## 5. Exact determinant-entropy score and density bound

### Theorem 5.1 — `QFORM-TWO-BANK-COCIRCUIT-FRESNEL-v1`

Assume exact rank three, `D=|det Lambda|>=1`, and the hypotheses

`c>=1/64`, `a=1-c>=1/64`,
`h_k<1/64` for all `k!=i`,                                      (5.1)

with a duplicated-gate failure at `j`,

`h_j+s_j^2/(2a)>1/2`.                                           (5.2)

Then for arbitrary independent original-coordinate densities bounded by one, and also after arbitrary affine perturbations of the quadratic form, the law has a continuous `C_0` density satisfying

`boxed: ||p_Q||_infinity <27.`                                  (5.3)

More precisely,

`||p_Q||_infinity
 <=3e (2048/63)^(1/3) D^(-1/3)
 =26.0262863804... D^(-1/3).`                                  (5.4)

#### Proof

Lemma 4.1 and (4.2) show that every coordinate marginal of the basis law (4.1) is at most `1/2`. It remains only to compute its determinant-entropy score.

On `B_i`, `v_S/w_S=2P_i`; on `B_j`, `v_S/w_S=2P_j`. Since the two banks each carry `w`-mass `1/2`,

`log Z_w
 =sum_S w_S log(v_S/w_S)
 =(1/2)log(2P_i)+(1/2)log(2P_j)`,                               (5.5)

hence

`Z_w=2 sqrt(P_iP_j)`.                                           (5.6)

By (3.7)-(3.8),

`Z_w>2(63/4096)=63/2048`.                                      (5.7)

Apply the completed capped-basis Fresnel theorem (1.2):

`||p_Q||_infinity
 <=3e(D Z_w)^(-1/3)
 <3e (2048/63)^(1/3)D^(-1/3)
 <27D^(-1/3)
 <=27`.                                                          (5.8)

The same source theorem gives a continuous `C_0` representative because its characteristic-function majorant is integrable. QED.

### What changed relative to r25

R25 balanced **all** bases containing `i` against all bases excluding `i`. Gate failure made the second physical coordinate `j` exceed the Hausdorff--Young marginal cap `1/2`. The new law discards the very small `both present` and `both absent` banks and balances only the two large XOR banks. This forces `alpha_i=alpha_j=1/2` exactly. The remaining marginals stay far below `1/2` because the `i`-bank sees the diffuse transverse frame `I_2-w_jw_j^T`, while the `j`-bank sees the quotient frame `I_(u^perp)-q_iq_i^T`, whose smallest eigenvalue remains uniformly positive as long as `a>=1/64`.

No conditional density or rotated independence is introduced; the only rotation is deterministic coefficient-space bookkeeping inside the basis determinant calculation.

## 6. Consequence for the r24/r25 residual chamber

Combine the source-valid exits already proved in r24-r25 with Theorem 5.1.

1. If `d>=1/64`, the designated partner account04/B16 gives `||p_Q||_infinity<=24` by (2.3).
2. If some `h_k>=1/64`, r24 gives `||p_Q||_infinity<865`.
3. If all `h_k<1/64`, `a>=1/64`, and the duplicated gate passes, r24 gives a continuous bounded-density branch (`<18.7` with its r23 constants).
4. If all `h_k<1/64`, `a>=1/64`, and the duplicated gate fails, Theorem 5.1 now gives the continuous bound `<27`.

Therefore the former two-source leakage alternative is completely removed whenever `a>=1/64`.

### Corollary 6.1 — `QFORM-R23-ONE-COLOOP-REDUCTION-v1`

Inside the exact-rank-three r23 dominant-star residual chamber, after the already-paid partner and transverse-pair exits, **the only B16 branch not paid by the r24-r26 projection-product compiler is**

`boxed: c>63/64.`                                                (6.1)

Equivalently, the remaining physical hub is a genuine near-coloop: more than `98.4%` of one Euclidean spectral direction lies on one original coordinate. The separate arbitrary-additional-spectrum problem is still open and is not touched by this exact-rank-three reduction.

This is a strict improvement over r24-r25, where a second almost-collinear source coordinate remained as an additional unpaid alternative.

## 7. First remaining implication

The next B16 target is now sharply one-dimensional in its geometric defect:

`QFORM-NEAR-COLOOP-UNIFORM-TRANSITION-v1`.

In exact rank three, close the near-coloop collar

`c>63/64`,

while retaining the original-coordinate product source and the small but nonzero residual longitudinal mass `a=1-c`. The bound must remain uniform as `a->0`; one may not delete the residual coefficient, replace the near-coloop by an exact coloop, or take a worst conditional projection-density slice. The likely useful inputs are the exact null-coloop product theorem at the endpoint, the nonzero scalar-pivot half-Riesz theorem away from the null coefficient, and the robust two-dimensional transverse projection frame. A valid bridge has to fuse those estimates before taking any reciprocal power that blows up in `a`.

Even after exact rank three is closed, arbitrary additional spectrum remains a separate full-target interaction debt. Hence this report does not claim the owner's full conjecture.

## 8. Finite exact checks

A companion verifier records only rational inequalities used above. Its checked outputs are

`beta_upper=1/63`,
`gamma_upper=189/1984`,
`alpha_rest_upper=13891/249984=0.0555675563...<1/2`,
`Z_lower=63/2048`,
`3e(2048/63)^(1/3)=26.02628638047539...<27`.

No Monte Carlo or histogram is used as evidence.

## 9. Status

- New theorem: `QFORM-TWO-BANK-COCIRCUIT-FRESNEL-v1` — proved on the stated exact-rank-three branch.
- New reduction: `QFORM-R23-ONE-COLOOP-REDUCTION-v1` — proved from the existing r24-r25 exits plus the new theorem.
- Designated partner actually applied: account04/B16 `QFORM-RULED-PLUECKER-ENDPOINT-v1`, giving the explicit `d>=1/64 => ||p_Q||_infinity<=24` exit.
- Continuity: proved on the new two-bank branch; not global.
- Full owner target: `OPEN / NOT PROVED`.
- Native brain ingestion: `WITHOUT_VERIFIED_BRAIN`; authenticated repository retrieval is not native learned-memory receiver use.
