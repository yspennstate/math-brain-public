# account01/B01 checkpoint — zero-diagonal common-hub receivers

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T143944Z-account01-B01-qform-auto11`  
Status: substantive checkpoint; full conjecture OPEN.


The prior B01 endpoint is a common ORIGINAL-coordinate hub `h` with a leaf packet

`A[L,L]=lambda z z^T`, `b=A[L,h]`, `E=det([b,z]^T[b,z])>0`,

obtained after the diagonal leaf curvature has collapsed to zero. Outside ORIGINAL coordinates may be conditioned on; they generate only affine terms in this packet.

## 1. General nonzero-hub scalar receiver

Let `a=A_hh!=0`. Complete only the ORIGINAL scalar hub. For arbitrary conditioning-generated affine terms,

`Q = a(X_h+shift(X_L))^2 + R(X_L)`

where the quadratic part of `R` is

`B=lambda z z^T-a^{-1}bb^T`.

Since `b,z` are independent, `B` has rank two and its two nonzero eigenvalues have product

`det_2(B)=-(lambda/a) E`.

Apply the source-valid orientation-free rank-two affine half-Riesz theorem

`sup_s E |X^T B X + linear -s|^{-1/2} <=128 |det_2(B)|^{-1/4}`

from `math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For a cap-one scalar `X_h`, the conditional density of `a(X_h+t)^2` is bounded by

`|a|^{-1/2}|y|^{-1/2}`.

Therefore

`boxed: ||p_Q||_infinity <=128 (|a lambda| E)^(-1/4).`

This is essential boundedness; continuity is not asserted by this scalar-square/half-Riesz composition. Thus the exact zero-diagonal common-hub packet is analytically paid whenever the physical hub scalar is nonzero, although this certificate degenerates as `a->0`.

## 2. New translation-uniform two-bank product half-Riesz lemma

Let `Y=(Y_i)_(i in P)` and `Z=(Z_j)_(j in N)` be disjoint ORIGINAL-coordinate product banks, let `u,v` be nonzero, `c!=0`, and allow arbitrary affine vectors `d,e` and constant `gamma`. Put

`T=c(u.Y)(v.Z)+d.Y+e.Z+gamma`.

Let `C_proj` be the one-dimensional product-projection constant, so the Rogozin--Ball estimate gives `C_proj<=sqrt(2)` and

`||p_(r.X)||_infinity <= C_proj/||r||_2`.

Then

`boxed: sup_s E|T-s|^(-1/2) <=8 C_proj (|c| ||u||_2 ||v||_2)^(-1/2).`

Proof. Condition on `Y` and write `U=u.Y`. The coefficient of `Z` is `cUv+e`. If `u0=-<e,v>/(c||v||^2)`, then

`||cUv+e|| >= |c| ||v|| |U-u0|`.

A probability density with cap `M` satisfies the sharp bathtub estimate

`sup_s int |x-s|^(-1/2) f(x) dx <=2 sqrt(2M)`.

Hence, for a.e. `Y`,

`sup_s E_Z|T-s|^(-1/2) <=2 sqrt(2 C_proj) (|c| ||v||)^(-1/2)|U-u0|^(-1/2)`.

The variable `U` has density cap `C_proj/||u||`. A second use of the same bathtub estimate gives

`E|U-u0|^(-1/2)<=2 sqrt(2 C_proj/||u||)`.

Multiplying proves the displayed bound. The possible zero of the conditional coefficient occurs at one value `U=u0`, a null event; the integrable majorant handles it. No scalar quadratic oscillatory envelope is used.

## 3. Exact all-hub-leaf-minors-zero grouped endpoint

Assume in addition to the zero leaf diagonal that every physical hub-leaf `2x2` determinant vanishes:

`a lambda z_i^2-b_i^2=0` for every `i`.

Since `E>0`, necessarily `a lambda>0` and the signs `b_i/(sqrt(a lambda) z_i)` are not all equal. Split the nonzero coordinates into two nonempty ORIGINAL banks `P,N` according to signs `+,-`, and set

`U=z_P.X_P`, `V=z_N.X_N`, `r=||z_P||`, `s=||z_N||`.

Completing the physical hub, including an arbitrary affine term in `X_h`, leaves

`R=4 lambda U V + d_P.X_P+d_N.X_N+constant`.

The two-bank lemma with `c=4lambda` yields

`H_(1/2)(R) <=4 C_proj (|lambda| r s)^(-1/2)`.

Combining with the physical hub square gives

`boxed: ||p_Q||_infinity <=4 C_proj / sqrt(|a lambda| r s).`

This remains valid with arbitrary outside couplings/curvature after conditioning outside the packet.

On the three-dimensional grouped span, after harmless sign conjugations for the matrix calculation, the packet matrix is

`M=[[A,sqrt(AL)r,-sqrt(AL)s],[sqrt(AL)r,Lr^2,Lrs],[-sqrt(AL)s,Lrs,Ls^2]]`,

with `A=|a|`, `L=|lambda|`. Its inverse is exactly

`M^-1=[[0,1/(2sqrt(AL)r),-1/(2sqrt(AL)s)], [1/(2sqrt(AL)r),0,1/(2Lrs)], [-1/(2sqrt(AL)s),1/(2Lrs),0]]`.

If `sigma=min{|mu|: mu nonzero eigenvalue of M}`, then each inverse entry has modulus at most `1/sigma`, so

`sqrt(AL) r >=sigma/2`, `sqrt(AL) s>=sigma/2`,

hence `AL r s>=sigma^2/4`. Therefore

`boxed: ||p_Q||_infinity <=8 C_proj/sigma <=8 sqrt(2)/sigma.`

In particular, if this exact rank-three packet has all three eigenvalues of modulus at least one, it has a universal density bound `8sqrt(2)`.

The full conjecture is not claimed. The remaining structural issue is to route the general zero-hub or near-zero-hub survivor into this rigid grouped endpoint, the existing mixed-Fresnel/bilinear-square receivers, or another paid branch without selecting a tiny coordinate minor.
