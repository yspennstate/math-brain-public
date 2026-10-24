SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-23T21:02:17Z.

# account01/B02 r37 — aggregate rank-two spectral-plane transfer to a physical E3 cut

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Integrated Fourier estimate  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / TARGET-WIDE FOURIER L1 OPEN_NOT_REFUTED**  
Regularity: continuous `C_0` density on every Fourier-L1 branch proved below; full-target continuity remains OPEN.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

The exact owner target remains unchanged: independent ORIGINAL real coordinates with one-dimensional probability densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No Gaussian, log-concave, moment, compact-support, connected-support, iid, diagonal-basis, post-rotation-independence, arbitrary-joint coarea, conditional-cap, fiber-supremum, one-good-minor, or small-tail-deletion assumption is introduced.

Fresh control before publication remains OWNER CONTROL revision `2026-09-22.15`, continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`, QFORM-only.

## 1. Source-pinned inputs actually used

The designated partner result used at an actual inequality is account02/B02:

`yspennstate/math-open-problems`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T200844Z-account02-B02-qform-auto11/REPORT.md`.

Its completed marginal-free physical-third-volume theorem says that for every literal ORIGINAL-coordinate cross block `N`, if

`Z_3=E_3(N):=e_3(NN^T)>0`,

then, with

`C_3=10.345084`,

`||p_Q||_infinity <= C_3 Z_3^(-1/6)`,

`int_R |phi_Q(t)| dt <= 2 pi C_3 Z_3^(-1/6)`.

The same theorem retains all same-bank quadratic terms, outside couplings, affine terms and signs, and gives a continuous density vanishing at infinity.

The preceding B02 r36 state used below is

`yspennstate/math-open-problems@8a41226468b3a1236efa704c7442d95a997b13a0`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B02/20260923T202254Z-account01-B02-qform-auto11-r36/REPORT.md`.

Its live strong-cut collar has a literal physical cross block `M` with

`E:=||M||_F^2 > E_0:=11907/16384`,

and, after the fifth-volume exit at parameter `delta=2^-19`, the survivor obeys

`T_2:=sum_{r>=3} x_r < delta E`,

where `x_r=s_r(M)^2`.  The relative-second-scale subbranch is `x_2>=E/64`.

For comparison, account02/B07 recently proved a one-coordinate nonexact-rank-two transfer by moving a physical coordinate across a cut. The theorem below aggregates the entire family before reciprocal payment and therefore gives a dimension-free Frobenius collar when all such transfers fail.

## 2. Main theorem: aggregate spectral-plane transfer

Let `[n]=L disjoint_union R` be any ORIGINAL-coordinate cut and

`M=A[L,R]`.

Write an SVD only as a deterministic coefficient identity,

`M=sum_a sqrt(x_a) u_a v_a^T`,

with `x_1>=x_2>=...>=0` and physical-coordinate left singular vectors `u_a`. Assume `x_2>0`. For each physical `i in L`, put

`ell_i=u_1(i)^2+u_2(i)^2`.

If `ell_i<1`, let `hat u_a` denote restriction to `L\{i}`, put

`c_i=A[L\{i},{i}]`,

and define

`d_i=dist(c_i, span{hat u_1,hat u_2}).`

When `ell_i=1`, define the weighted quantity `(1-ell_i)d_i^2` to be zero. Set

`W_L=sum_{i in L}(1-ell_i)d_i^2.`

### Theorem 2.1 — `QFORM-RANK2-SPECTRALPLANE-AGGREGATE-TRANSFER-L1-v1`

There exists a literal ORIGINAL-coordinate cut `S|T` for which

`boxed: E_3(A[S,T]) >= (27/256) x_1 x_2 W_L.`                     (2.1)

Consequently, whenever `W_L>0`, the full ambient quadratic form satisfies

`boxed:
 ||p_Q||_infinity
 <= C_3 (27/256)^(-1/6) (x_1x_2W_L)^(-1/6)
 <15.051 (x_1x_2W_L)^(-1/6),`                                    (2.2)

and

`boxed:
 int_R |phi_Q(t)|dt
 <=2pi C_3 (27/256)^(-1/6)(x_1x_2W_L)^(-1/6)
 <94.565 (x_1x_2W_L)^(-1/6).`                                    (2.3)

The transpose gives the identical theorem for the right top-two singular plane, with an aggregate `W_R` built from the physical self-columns in the `R` bank.

### Proof

For one `i`, define the complete squared third-minor extension mass

`F_i=sum_{S subset L\{i}, |S|=3}
       sum_{T subset R, |T|=2}
       det A[S,T union {i}]^2.`                                  (2.4)

Right-multiply only the `R` coefficient columns of `[M_hat_i,c_i]` by the deterministic orthogonal right-singular basis of `M`, extending it by the identity on `c_i`. This is solely a Cauchy--Binet computation of a Gram invariant; it does NOT rotate the random variables and no independence is asserted after it.

Exterior Cauchy--Binet gives the exact decomposition

`F_i=sum_{a<b} x_a x_b ||hat u_a wedge hat u_b wedge c_i||^2.`    (2.5)

Keep only the nonnegative `(a,b)=(1,2)` term. Since `u_1,u_2` were orthonormal before deleting coordinate `i`,

`||hat u_1 wedge hat u_2||^2
 =(1-u_1(i)^2)(1-u_2(i)^2)-u_1(i)^2u_2(i)^2
 =1-ell_i.`                                                       (2.6)

The Gram base-height identity therefore yields

`||hat u_1 wedge hat u_2 wedge c_i||^2
 =(1-ell_i)d_i^2`,                                                (2.7)

and hence

`boxed: F_i >= x_1x_2(1-ell_i)d_i^2.`                            (2.8)

Now retain every original coordinate of `R` on the receiver side and independently move each coordinate of `L` to the receiver side with probability `p=1/4`. Let `I` be the moved set, so the resulting physical cross block is

`N_I=A[L\I,R union I].`

A fixed minor from (2.4), with source triple `S` and unique moved column `i`, occurs in `N_I` whenever

`i in I` and `S cap I=emptyset`.

Its probability is exactly

`p(1-p)^3=(1/4)(3/4)^3=27/256.`                                  (2.9)

The packets indexed by different `i` are disjoint because `i` is the unique `L`-coordinate in the column triple. Therefore linearity of expectation and (2.8) give

`E_I E_3(N_I)
 >=(27/256) sum_i F_i
 >=(27/256)x_1x_2 W_L.`                                          (2.10)

Some actual original-coordinate cut realizes at least the mean, proving (2.1). Equations (2.2)-(2.3) are the direct application of the completed designated account02/B02 theorem to that literal cut. QED.

### Why this is useful

The theorem does not select a single reciprocal minor. It aggregates every transverse self-column defect first and only then invokes the marginal-free physical-E3 receiver. Thus a diffuse family of individually tiny defects cannot survive at fixed total energy.

It also keeps the entire nonzero higher-singular-value tail in `M`: the SVD is used only inside a deterministic nonnegative exterior-volume identity.

## 3. Application to the live strong-cut near-rank-two collar

Return to the r36 strong cut. Take

`delta=2^-19`, `zeta=2^-30`.

Assume the D5 exit has failed and we are in the relative-second-scale branch

`T_2<delta E`, `x_2>=E/64`.

Because `x_1+x_2=E-T_2` and `x_1>=x_2`, concavity of `y(1-delta-y)` on the allowed interval gives

`P:=x_1x_2
 >=P_0:=(1/64)(63/64-delta)E_0^2
 =0.00812352625896906...`.                                      (3.1)

### 3.1 First universal Fourier-L1 exit

If

`E_3(M)>=zeta`,

then the designated partner theorem gives immediately

`boxed: ||p_Q||_infinity <331.043,`                               (3.2)

`boxed: int_R |phi_Q(t)|dt <2080.01.`                             (3.3)

This branch has a continuous `C_0` density.

If this exit fails, then the literal positive term `x_1x_2T_2` in `E_3(M)` gives

`T_2 < zeta/P
 <=T_0:=zeta/P_0
 =1.1464511160867112e-7.`                                        (3.4)

Thus the best rank-two approximation `M_2` obeys

`||M-M_2||_F < sqrt(T_0)=0.0003385928404568991...`.               (3.5)

### 3.2 Aggregate transverse exits on both physical banks

Apply Theorem 2.1 on the left. If its produced cut has third volume at least `zeta`, then (3.2)-(3.3) again pay the branch. Hence an unpaid state must obey

`W_L < (256/27) zeta/P
 <=W_0:= (256/27)zeta/P_0
 =1.0870055026599928e-6.`                                        (3.6)

Apply the transpose theorem to the right bank as well:

`W_R<W_0.`                                                        (3.7)

Let

`H_L={i in L: ell_i>3/4}`.

Since `sum_i ell_i=2`,

`|H_L|<=2.`                                                       (3.8)

On `J_L=L\H_L`, `1-ell_i>=1/4`, so (3.6) gives the dimension-free aggregate collar

`sum_{i in J_L} d_i^2 <4W_0.`                                    (3.9)

The same statement holds on the right.

## 4. Failure of all Fourier exits forces a global diagonal + rank-20 + tiny-Frobenius decomposition

This section is deterministic coefficient geometry; no term is deleted from the random quadratic form.

For each `i in J_L`, choose `v_i in U:=span{u_1,u_2}` whose restriction to `L\{i}` realizes the distance `d_i`. This lift exists because `ell_i<1`, so restriction of the two-plane remains two-dimensional. Let `L_0` be the matrix whose `i`th column is `v_i` for `i in J_L`, and zero for `i in H_L`. Then

`rank L_0<=2`,

and

`S_L=(L_0+L_0^T)/2`

has rank at most four.

Write `C_L=A[L,L]`. For distinct `i,j in J_L`, put

`q_{ji}=A_{ji}-v_i(j)`.

Then

`A_{ij}-(S_L)_{ij}=(q_{ij}+q_{ji})/2`,

and the elementary inequality `(a+b)^2/2<=a^2+b^2` yields

`sum_{i!=j in J_L}|A_{ij}-(S_L)_{ij}|^2
 <=sum_{i in J_L} d_i^2
 <4W_0.`                                                         (4.1)

Let `P_H` be coordinate projection onto `H_L`, `Q_H=I-P_H`, and set

`M_L=C_L-S_L`,

`R_H=P_H M_L+Q_H M_L P_H`.

This exactly absorbs every entry touching `H_L` and

`rank R_H<=2|H_L|<=4.`                                           (4.2)

Put

`N_L=Q_HM_LQ_H`, `D_L=diag N_L`, `E_L=N_L-D_L`.

Then

`boxed:
 A[L,L]=D_L+R_L+E_L,
 rank R_L<=8,
 ||E_L||_F^2<4W_0,`                                              (4.3)

where `R_L=S_L+R_H`. Hence

`||E_L||_F<2sqrt(W_0)=0.0020851911208903543...`.                 (4.4)

Repeating the same construction on `R` gives

`A[R,R]=D_R+R_R+E_R`,
`rank R_R<=8`,
`||E_R||_F^2<4W_0.`                                              (4.5)

Finally write

`M=M_2+E_M`, `rank M_2<=2`, `||E_M||_F^2=T_2<T_0`.

Combining the two banks and the crossing gives the exact global decomposition

`boxed: A=D+R_0+E_0,`                                             (4.6)

where

`D=diag(D_L,D_R)` is diagonal in the ORIGINAL coordinates,

`boxed: rank R_0<=8+8+4=20,`                                     (4.7)

and, by Frobenius orthogonality of the block supports,

`||E_0||_F^2
 =||E_L||_F^2+||E_R||_F^2+2||E_M||_F^2
 <8W_0+2T_0.`                                                     (4.8)

Numerically,

`boxed: ||E_0||_F<0.002987529789725499.`                          (4.9)

This is the principal new structural consequence of the integrated-Fourier attack: in the relative-second-scale near-rank-two strong-cut chamber, either a universal Fourier-L1 estimate has already fired, or the *entire original matrix* is trapped inside a dimension-free Frobenius tube around `diagonal + rank <=20`.

No claim is made that the small Frobenius tail is a small random quadratic perturbation; the live corrections forbid that inference on unbounded product laws.

## 5. Optional bounded-density exit from many residual diagonal pivots

This section uses the already-proved physical coordinate-core theorem of account04/B07:

if an actual `r+3` coordinate principal block decomposes as `D+R+E`, with `|D_ii|>=d`, `rank R<=r`, and `max|E_ij|<=eps`, then

`s_3 >= d-(r+3)eps`

and, if positive,

`||p_Q||_infinity <= 2sqrt(6pi(r+3))/(d-(r+3)eps)`.

Apply it to (4.6) with `r=20`, `eps=||E_0||_F<0.00298753`, and `d=1/8`. If there are at least 23 physical coordinates with

`|D_ii|>=1/8`,

then a 23-coordinate physical principal core satisfies

`s_3>1/8-23(0.00298753)>0.0562868`,

so

`boxed: ||p_Q||_infinity<740.`                                    (5.1)

This branch proves essential boundedness but, unlike the Fourier branches, I do not record continuity from this step alone.

If (5.1) does not fire, at most 22 diagonal entries of `D` have magnitude at least `1/8`. Absorb those entries into the low-rank carrier. Then

`A=R_42+D_small+E_0`,

with

`rank R_42<=42`, `||D_small||_op<1/8`.

Since the exact target gives `s_3(A)>=1`, singular-value perturbation forces

`boxed: s_3(R_42)>1-1/8-0.00298753>0.87201247.`                   (5.2)

Thus every still-unpaid state in this chamber has been reduced to a fixed-rank (`<=42`) symmetric carrier with three singular values bounded below by `0.872`, plus a small ORIGINAL-coordinate diagonal term and a retained Frobenius tail below `0.00299`.

## 6. Status and next unpaid implication

The full QFORM conjecture remains **OPEN**. The full continuity statement remains **OPEN**. I found no exact-target counterexample to the stronger target-wide statement

`int_R |E exp(it X^TAX)| dt <= C`.

That stronger criterion therefore remains **OPEN_NOT_REFUTED**.

The first unpaid B02 interface is now

`QFORM-RANK42-CARRIER-SMALLDIAG-FROBENIUS-TAIL-RECEIVER-v1`:

> In the strong-cut relative-second-scale chamber, exploit the fixed-rank carrier `R_42`, with `s_3(R_42)>0.872`, while retaining the original-coordinate diagonal and Frobenius tails exactly. Either build an integrated-Fourier/grouped-bank receiver for this finite-rank carrier-plus-tail structure, or obtain a direct bounded-density estimate. Do not discard the tail and do not rotate the product law into carrier eigen-coordinates.

The complementary `x_2<E/64` near-rank-one chamber retains the separate r36 three-bank/internal-cross routing and is not claimed closed by the present theorem.

## 7. Arithmetic summary

Using `C_3=10.345084`,

`(256/27)^(1/6)=1.4548315146289619`,

so Theorem 2.1 has density coefficient `15.05035422468384` and Fourier-L1 coefficient `94.56416453238171`.

For the live collar,

`E_0=0.72674560546875`,
`P_0=0.00812352625896906`,
`zeta=9.313225746154785e-10`,
`T_0=1.1464511160867112e-7`,
`W_0=1.0870055026599928e-6`,
`||E_0||_F<0.002987529789725499`.

At `zeta`, the designated partner theorem gives density `<331.042688` and Fourier integral `<2080.002554`.
