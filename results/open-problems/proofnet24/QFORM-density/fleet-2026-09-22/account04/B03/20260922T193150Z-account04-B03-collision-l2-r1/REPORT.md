# QFORM-COLLISION-L2-COMPILER-v1

## Status

**ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN.** This report proves a dependence-safe integrated time estimate with linear collision small-ball scaling. It does not prove the target one-copy density bound, and it explains precisely why an independent-copy estimate alone cannot do so.

## Target

Let (X_i) be independent real random variables with densities at most one and let (Q=X^TAX), where (A) has at least three eigenvalues of absolute value at least one. The target is a universal bound on the density of (Q).

## 1. Exact independent-copy geometry

Let (X') be an independent copy and put
[
U=X-X',qquad V=X+X'.
]
Then
[
Q(X)-Q(X')=U^TAV.
]
The pairs ((U_i,V_i)) are independent across (i), but (U_i) and (V_i) are dependent. Their joint density is
[
h_i(u,v)=rac12 f_i!left(rac{v+u}{2}ight)
                  f_i!left(rac{v-u}{2}ight).
]
All arguments below preserve this dependence; no sum/difference independence is asserted.

## 2. Partner input

Account01/B03, run `account01-B03-20260922T185132Z-r14`, canonical report
`yspennstate/math-open-problems@cd628bcb117fb633c47261a3fbb9d1504a8b1b1b`, proves the following. If (Z) has density cap (M), (Z') is an independent copy, and
[
psi_a(t)=mathbb E e^{itaZ^2},
]
then
[
int_{mathbb R}|t|^{-1/2}|psi_a(t)|^2,dt
le sqrt{2pi},C_{m sq},M,|a|^{-1/2},
]
where
[
C_{m sq}=1+4sqrt2+8left(lograc32+rac12log3ight)
=14.2950242690ldots.
]
Its proof works directly with
[
|Z^2-Z'^2|=|(Z-Z')(Z+Z')|
]
and therefore retains the dependence between sum and difference.

## 3. New two-square time-integral compiler

Let (Y=aZ^2+bW^2), where (Z,W) are independent and have density caps (M_Z,M_W). Then
[
phi_Y(t)=psi_a(t)psi_b(t).
]
Since (|phi_Y|le1),
[
int_{mathbb R}|phi_Y(t)|^2dt
le int_{mathbb R}|psi_a(t)psi_b(t)|dt.
]
Cauchy--Schwarz, with the half-Riesz weight split exactly between the two factors, gives
[
egin{aligned}
int |psi_apsi_b|
&=int
 igl(|t|^{-1/2}|psi_a|^2igr)^{1/2}
 igl(|t|^{-1/2}|psi_b|^2igr)^{1/2},dt\
&le
left(int |t|^{-1/2}|psi_a|^2dtight)^{1/2}
left(int |t|^{-1/2}|psi_b|^2dtight)^{1/2}.
end{aligned}
]
Applying the partner theorem yields
[
oxed{
int_{mathbb R}|phi_Y(t)|^2dt
le sqrt{2pi},C_{m sq},
sqrt{M_ZM_W},|ab|^{-1/4}.
}
]
This is a full-time, not truncated, estimate. It is valid for either signs of (a,b).

By Plancherel, (Y) has an (L^2) density (p_Y) satisfying
[
oxed{
|p_Y|_2^2
le rac{C_{m sq}}{sqrt{2pi}},
sqrt{M_ZM_W},|ab|^{-1/4}.
}
]
Numerically (C_{m sq}/sqrt{2pi}=5.7026ldots).

## 4. Linear collision small-ball estimate

Let (Y') be an independent copy of (Y). For every (arepsilon>0),
[
egin{aligned}
Pr(|Y-Y'|learepsilon)
&=int p_Y(x)int_{x-arepsilon}^{x+arepsilon}p_Y(y),dy,dx\
&le 2arepsilon|p_Y|_2^2.
end{aligned}
]
Consequently
[
oxed{
Pr(|Y-Y'|learepsilon)
le
rac{2C_{m sq}}{sqrt{2pi}},
sqrt{M_ZM_W},|ab|^{-1/4},arepsilon.
}
]
The explicit constant is (2C_{m sq}/sqrt{2pi}=11.4052ldots).

This is the requested recovery of linear small-ball scaling at the independent-copy level. It is obtained without falsely separating (Z-Z') from (Z+Z').

## 5. Exact limitation of the independent-copy route

For a general probability density (p),
[
Pr(|Y-Y'|learepsilon)le2arepsilon|p|_2^2.
]
Conversely, dividing by (2arepsilon) and taking (arepsilondownarrow0) recovers (|p|_2^2) at Lebesgue points. Thus uniform linear collision control is fundamentally an (L^2)-density certificate.

It does not imply an (L^infty) bound. For example, take a probability density consisting of a spike of height (N) and width (N^{-3}), plus a disjoint bounded block carrying the remaining mass. Then
[
|p_N|_infty=N,qquad
|p_N|_2^2le 2
]
for all sufficiently large (N). Hence the collision estimate stays uniformly linear while the essential supremum diverges.

Therefore the missing factor in a full B03 proof is now precise: one needs a structural upgrade from collision (L^2) control to one-copy (L^infty) control. In the separated three-square branch, account01/B03 supplies that upgrade by convolving the two-square half-Riesz bound with a third independent square. For a genuinely rotated quadratic form, the third direction is dependent after rotation, so the required upgrade must retain product provenance rather than invoke independent convolution.

## 6. Relation to the full target

This report proves neither the unrestricted universal density bound nor continuity. It establishes:

1. a dependence-safe full-time estimate for two independent square directions;
2. an explicit linear independent-copy small-ball estimate;
3. a sharp functional-analytic diagnosis of the remaining gap.

The current structural debt is to show that the third large spectral direction converts the (L^2) collision certificate into an (L^infty) one-copy certificate despite rotation-induced dependence, or to find a counterexample.

## Source and control notes

Partner source: account01/B03 `account01-B03-20260922T185132Z-r14`, handoff blob `b5c844b18102d59b8a6b55036745958b744eb4a3`.

The phase-aligned fragmented-support correction is respected: no pointwise van-der-Corput decay is used. Repeated eigenvalues are not treated as degeneracy. No Gaussian, log-concave, moment, compact-support, or diagonal-basis assumption is introduced into the full target.

Execution status: `WITHOUT_VERIFIED_BRAIN`.
