# account03/B16 r30 addendum — exact projected-crossing identity for the two-bank compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `NEW SUPPORTING IDENTITY + NEW CONTINUOUS PAID SUBBRANCH / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

This addendum was written after the required control refresh exposed the new interactive checkpoint

`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

That checkpoint proves a one-original-hub, `ell=2` projected-crossing theorem: if the hub-star row on one light bank has Euclidean norm `S`, the projected light crossing has second volume `Z_2` with every volume row marginal at most `1/2`, then the full quadratic form, with arbitrary same-side quadratic terms, hub square, affine terms and outside couplings retained, has a continuous `C_0` density satisfying

`||p_Q||_infinity <9.4 (S^2 Z_2)^(-1/6)`.                       (A.1)

The purpose of this addendum is to compute `S^2 Z_2` **exactly** in the r30 two-bank exact-rank-three packet and verify the row-marginal gate from the inherited transverse-smallness condition.

## A.1 Setup

Use the notation of `REPORT.md`:

`A=R Lambda R^T`, `R^T R=I_3`, `D=|det Lambda|>=1`,

with hub row `r_0=sqrt(h)e`, `h>63/64`, and leaves

`r_i=alpha_i e+z_i`, `z_i perpendicular e`, `||z_i||^2<1/64`.

Take the two-bank alternative from Theorem 3.1 of `REPORT.md`:

`J union K = {leaves}`, `J cap K=empty`,

`(1/4)I_2 <=G_J,G_K <=(3/4)I_2`,

where `G_B=sum_(i in B) z_i z_i^T`.

For a bank `B`, also define its full three-dimensional spectral Gram and volume

`H_B=sum_(i in B) r_i r_i^T`,
`nu_B=det H_B>=0`.                                                (A.2)

The new projected-crossing theorem will be applied with original hub `X_0`, light-row bank `J` and light-column bank `K`; the roles can then be swapped.

## A.2 The hub star on either balanced bank is quantitatively nonzero

Write

`a=e^T Lambda e`,
`g=P_(e^perp) Lambda e`.

Then

`A_00=h a`,
`A_0i=sqrt(h)(a alpha_i+g^T z_i)`.                               (A.3)

The hard branch has already paid every physical diagonal of magnitude at least `1/64`, so `|A_00|<1/64`. Since `h>63/64`,

`|a|<1/63`.                                                       (A.4)

Moreover `sigma_min(Lambda)>=1`, hence

`a^2+||g||^2=||Lambda e||^2>=1`,

so

`||g||>sqrt(1-1/63^2)>62/63`.                                   (A.5)

For either balanced bank `B`,

`sum_(i in B)(g^Tz_i)^2=g^T G_B g >=||g||^2/4`,                 (A.6)

while

`sum_(i in B)alpha_i^2 <=1-h<1/64`.                             (A.7)

Therefore, writing `S_B=||A_{0,B}||_2`, the triangle inequality in coefficient space gives

`S_B/sqrt(h)
 >= ||(g^Tz_i)_(i in B)||_2-|a| ||(alpha_i)_(i in B)||_2
 >31/63-1/504
 =247/504`.                                                      (A.8)

Since `sqrt(h)>sqrt(63)/8`,

`S_B>247 sqrt(63)/4032>31/64`.                                  (A.9)

The last strict inequality follows by squaring:

`247^2*63=3843567 >3814209=1953^2`,

and `31/64=1953/4032`.

Thus the one-hub row used below has literal singular value `S_B>31/64`; no conditional density or rotated-coordinate independence is being substituted for it.

## A.3 Exact projected-crossing determinant identity

Apply the interactive theorem with light split `I=J`, `J=K` in its notation. Put

`m=A_{0,K}`,
`S=||m||_2=S_K`,
`Pi_m=orthogonal projection onto span(m) in R^K`,

and define the projected physical crossing

`C=A_{J,K}(I-Pi_m)`.                                             (A.10)

Let

`Z_2=e_2(CC^T)`.                                                 (A.11)

### Proposition — `QFORM-EXACT-R3-PROJECTED-CROSSING-PLUECKER-v1`

If `nu_K>0`, then `C` has rank two, its normalized two-volume row marginals are all strictly smaller than `1/16`, and

`boxed:
 S_K^2 Z_2
 =D^2 h det(G_J) nu_K.`                                         (A.12)

#### Proof

For a fixed row pair `i<j` in bank `J`, denote the corresponding rows of `A_{J,K}` by `b_i,b_j`. The Gram determinant after orthogonal projection away from the nonzero row `m` satisfies the standard Schur/Gram identity

`det Gram(P_(m^perp)b_i,P_(m^perp)b_j)
 = det Gram(m,b_i,b_j)/||m||^2`.                                (A.13)

By Cauchy--Binet,

`det Gram(m,b_i,b_j)
 =sum_(T subset K, |T|=3) det A[{0,i,j},T]^2`.                  (A.14)

Exact rank three factors every cross minor:

`det A[P,T]
 =det(R_P Lambda R_T^T)
 =det Lambda det(R_P) det(R_T)`.                                (A.15)

Write `w_P=det(R_P)^2`. Combining (A.13)--(A.15), summing first over `T subset K`, then over row pairs `i<j` in `J`, gives

`Z_2
 =D^2/S_K^2
   [sum_(i<j in J) w_{0ij}]
   [sum_(|T|=3,T subset K) w_T].`                               (A.16)

The second bracket is `det H_K=nu_K` by Cauchy--Binet. Since `r_0=sqrt(h)e`,

`w_{0ij}=h det(z_i,z_j)^2`,

and another two-dimensional Cauchy--Binet identity gives

`sum_(i<j in J)w_{0ij}=h det G_J`.                              (A.17)

Equations (A.16)--(A.17) prove (A.12). In particular `Z_2>0`, so `rank C=2`.

To verify the interactive theorem's row-marginal gate without a new assumption, observe directly that the hub projection kills every longitudinal term in the row crossing:

`A_{i,K}(I-Pi_m)
 =z_i^T Lambda R_K^T(I-Pi_m)`.                                 (A.18)

Thus `C=Z_J T` for a deterministic rank-two matrix `T`, where `Z_J` has rows `z_i^T`. Since `rank C=2`, `col(C)=col(Z_J)`. For an exact-rank-two matrix, the normalized squared two-minor row marginal equals its row-space leverage. Hence

`rho_i=z_i^T G_J^(-1)z_i
 <=4||z_i||^2
 <1/16<1/2`.                                                     (A.19)

This proves every claimed gate. QED.

## A.4 New continuous paid subbranch

Substitute (A.12) into the completed projected-crossing estimate (A.1): whenever `nu_K>0`,

`||p_Q||_infinity
 <9.4 [D^2 h det(G_J) nu_K]^(-1/6)
 <=9.4 [D^2 h nu_K/16]^(-1/6).`                                (A.20)

The same statement holds with `J,K` swapped.

Consequently, if either bank satisfies

`nu_B>=2^-12`,                                                   (A.21)

then, since `D>=1` and `h>63/64`,

`boxed:
 ||p_Q||_infinity
 <9.4 [ (63/64) 2^-12 /16]^(-1/6)
 =59.8431454684... <60.`                                        (A.22)

The density is continuous and vanishes at infinity on this branch, by the cited projected-crossing theorem.

Thus after the `<81` single-pair exit in `REPORT.md`, every still-unpaid two-bank state may additionally be assumed to satisfy

`boxed: nu_J<2^-12, nu_K<2^-12.`                                (A.23)

This is substantially more specific than merely saying the leaf frame is near the hub plane.

## A.5 Geometric meaning of the survivor: two nearly exact source planes

Write the full bank Gram in the hub/transverse splitting as

`H_B=[[t_B,v_B^T],[v_B,G_B]]`,

where

`t_B=sum_(i in B)alpha_i^2`,
`v_B=sum_(i in B)alpha_i z_i`.                                  (A.24)

Because `G_B` is invertible,

`nu_B=det G_B [t_B-v_B^T G_B^(-1)v_B].`                         (A.25)

The bracket is exactly the squared Euclidean distance of the longitudinal coefficient vector `(alpha_i)_(i in B)` from the span of the two transverse coefficient rows `(z_i^(1))_(i in B),(z_i^(2))_(i in B)`.

Since `det G_B>=1/16`, (A.23) implies

`t_B-v_B^T G_B^(-1)v_B
 =nu_B/det G_B
 <16*2^-12
 =2^-8`.                                                        (A.26)

Therefore on **each** source bank there is a deterministic slope vector `q_B in R^2` such that

`sum_(i in B)(alpha_i-q_B^Tz_i)^2<1/256`.                       (A.27)

Equivalently, the genuinely unpaid packet consists of two disjoint original-coordinate banks, each carrying

- order-one diffuse negative hub-pair determinant mass;
- a well-conditioned two-dimensional transverse projection;
- but a longitudinal coefficient row lying within `1/16` in Euclidean norm of that bank's two-dimensional transverse row span.

This is the quantitative **two-slope / small-innovation** geometry anticipated by the live twist obstruction. The residual `<1/16` source innovation cannot be deleted on unbounded inputs; it must be spent by an integrated Fourier or direct small-ball argument.

## A.6 Next implication after the new owner checkpoint

The next B16 target is sharpened to

`QFORM-TWO-BANK-TWO-SLOPE-SMALL-INNOVATION-CLOSURE-v1`:

> in the exact-rank-three ultra-coloop state, close the packet where both balanced banks have longitudinal innovation norm `<1/16`, while each bank still carries more than `c_*/4` diffuse negative hub-pair determinant mass and the cross-bank bordered triple mass is at least `189D/512`.

The new projected-crossing theorem already pays any bank whose full three-volume reaches `2^-12`; the remaining proof must use the small innovation **without deleting it** and without replacing the two-dimensional product projections by arbitrary joint densities.

Full QFORM remains OPEN / NOT PROVED. Global continuity remains OPEN; continuity is proved only on the projected-crossing paid subbranch (A.22).
