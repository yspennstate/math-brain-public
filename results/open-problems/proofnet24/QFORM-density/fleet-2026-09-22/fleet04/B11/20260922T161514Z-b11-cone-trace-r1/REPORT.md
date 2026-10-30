# QFORM B11 — exact cone-trace interface for indefinite rank three

**Run:** `20260922T161514Z-b11-cone-trace-r1`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.5`  
**Status:** `ESSENTIAL_STEP_APPLIED / PRECISE_MISSING_FACTOR_IDENTIFIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## Target and scope

The full target asks for a universal bound on the density of (X^TAX) for independent cap-one coordinates and a symmetric matrix with at least three eigenvalues of modulus at least one. This note treats the genuinely indefinite spectral signature ((+,+,-)); ((+,-,-)) follows by negation. It does not rotate the input law and then assume independence.

## 1. Exact cone-trace formula

Let (Z=(U,V,W)) have an arbitrary probability density (g) on (mathbb R^3), and put
[
q(U,V,W)=U^2+V^2-W^2.
]
Using cylindrical coordinates (U=rcos	heta,V=rsin	heta), coarea (equivalently the delta-function identity) gives, for almost every (y),
[
oxed{
p_q(y)=rac12int_{{w:w^2+y>0}}int_0^{2pi}
g!left(sqrt{w^2+y}cos	heta,sqrt{w^2+y}sin	heta,wight)
,d	heta,dw .
}
]
Indeed (du,dv=r,dr,d	heta), and
[
int_0^infty delta(r^2-w^2-y)r,dr
=rac12mathbf 1_{{w^2+y>0}}.
]
Thus the precise geometric quantity needed in spectral coordinates is not (|g|_infty), but the uniform quadratic cone-trace norm
[
mathcal T(g):=sup_yrac12int_{{w:w^2+y>0}}int_0^{2pi}
g(sqrt{w^2+y},e_	heta,w),d	heta,dw .
]
The desired density bound is exactly (|p_q|_infty=mathcal T(g)).

## 2. Quantitative no-go for a projection-cap-only proof

A bounded three-dimensional density does not control this trace. Fix (Rge1), set
[
delta_R=rac1{6pi R^2},
]
and let (g_R=mathbf 1_{E_R}), where in cylindrical coordinates
[
E_R={Rle wle2R,quad 0le	heta<2pi,quad |r-w|ledelta_R}.
]
Then
[
|E_R|
=int_R^{2R}int_0^{2pi}int_{w-delta_R}^{w+delta_R}r,dr,d	heta,dw
=6pidelta_RR^2=1.
]
Hence (g_R) is a probability density with (|g_R|_infty=1). But the entire cone segment (r=w, Rle wle2R) lies in (E_R), so the exact formula gives
[
oxed{p_{q,R}(0)=pi R.}
]
Therefore
[
sup_{substack{gge0, int g=1\ |g|_inftyle1}}
|p_{U^2+V^2-W^2}|_infty=infty.
]

This is not a counterexample to QFORM: (g_R) is an arbitrary joint density and has not been shown to be a three-dimensional projection of an independent cap-one product law. It is a sharp obstruction to the invalid implication “bounded spectral projection density implies bounded indefinite quadratic pushforward.” The missing factor is exactly product-provenance control of (mathcal T(g)), or an equivalent weighted X-ray/cone-trace estimate.

The geometry also identifies why the rank-two logarithm survives: at (y=0), the level surface is a noncompact cone, and cap-one mass can occupy a normal tube of thickness (R^{-2}) along a cone segment of length (R), keeping total volume one while making the trace grow linearly.

## 3. Actual application of fleet01/B11

The newest completed assigned partner theorem (fleet01/B11, canonical commit `aff1f42f4b68ea31eec27673e7d56b5370f6dec3`) proves:

If (S) is independent of ((V,W)), (|f_S|_inftyle M), the pair has joint density (h) with (|h|_inftyle K), and (a,b
e0), then
[
Y=2aSW+bV^2
]
has a bounded continuous density satisfying
[
oxed{|p_Y|_inftyle
6(MK)^{2/3}|a|^{-2/3}|b|^{-1/3}.}
]

This theorem is precisely a product-provenance estimate for the null-coordinate version of the cone trace. In the canonical exact-rank-three null-heavy case
[
Q=2Z_1Z_3+Z_2^2,
]
if a physical Parseval row is exactly ((1,0,0)), then (Z_1=X_i) is genuinely independent of ((Z_2,Z_3)). The two-dimensional projection theorem used by fleet01/B11 gives (Kle e), while (Mle1). Therefore
[
oxed{|p_Q|_inftyle6e^{2/3}<11.687,}
]
and the density is continuous. Negating (Q) gives the dual ((+,-,-)) branch.

The important distinction is exact: the partner estimate controls (mathcal T(g)) because the spectral density retains an original-coordinate factorization. The example (g_R) shows that replacing that factorization by (|g|_inftyle e) would be invalid.

## 4. Precise remaining implication

For a general rotated target, let (g) be the genuine three-dimensional spectral projection of the original independent product law. Known projection estimates control (|g|_infty), but Section 2 proves this is insufficient. The remaining indefinite-signature obligation is therefore

[
oxed{	ext{`QFORM-PRODUCT-CONE-TRACE-v1': }quad
mathcal T(g)le C
	ext{ for genuine spectral projections }g,}
]
or a substitute estimate that uses the same product provenance and survives arbitrary extra spectral directions.

In the null-heavy coordinates (2Z_1Z_3+Z_2^2), this becomes the overlapping-support compiler already isolated by fleet01/B11: when no original coordinate separates (Z_1) from ((Z_2,Z_3)), extract enough aggregate independence, shear determinant, or regularized-minor payment to control the weighted (1/|Z_3|) fiber integral. Conditional density caps alone do not supply this.

## 5. Regularity

The partner-separated branch above has a continuous density. The cone-trace identity by itself yields only an almost-everywhere density formula and no continuity. Full target-level continuity remains separate and open outside branches covered by existing regularity theorems.

## 6. Corrections respected

No pointwise law-uniform quadratic Fourier decay is used. No rotated spectral coordinates are declared independent. No bounded-projection theorem is promoted to an indefinite pushforward theorem. No moment, compact-support, connected-support, Gaussian, or log-concavity assumption is added. The example is explicitly labeled a mechanism counterexample, not a QFORM counterexample.
