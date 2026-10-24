SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B06, 2026-09-23T23:14:42Z.
attacking: fresh-transverse curved-section payment by integrating the two-dimensional product Fourier volume before the off-fold Jacobian.

# QFORM-FRESH-TRANSVERSE-CURVED-SECTION-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T231442Z-account04-B06-QFORM-r2`  
Status: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is not proved here. This note closes the zero- and small-transverse-coefficient part of the curved-section problem whenever the transverse linear direction comes from a fresh original-coordinate bank. The level is exact, the input laws are arbitrary cap-one densities, and no conditional-density supremum is used.

## Theorem

Let the original coordinates be divided into disjoint sets (S) and (R). Let (X_S) and (X_R) denote the corresponding independent coordinate banks. Let (w,vinmathbb R^S) be orthonormal and assume the diffuse two-frame gate
[
  w_i^2+v_i^2le rac12qquad(iin S).
]
Put
[
  L=langle w,X_Sangle,qquad V=langle v,X_Sangle,
]
and let (B) be any measurable random variable determined by (X_R). Thus (B) is independent of the pair ((L,V)); no density bound for (B) is required.

For arbitrary
[
  lambda
e0,quad etainmathbb R,quad v_0,a,cinmathbb R,quad r>0,
]
consider the subprobability pushforward on the off-fold event
[
  E_r={|V-v_0|>r}
]
under
[
  (L+a, lambda(V-v_0)^2+eta B+c).
]
It has a density (g_r) satisfying
[
  oxed{ |g_r|_inftyle rac{4}{|lambda|r} }.
]
The estimate is uniform in (eta), including (eta=0), and therefore has no small-(eta) gap.

The statement remains valid after conditioning on arbitrary outside original coordinates whenever the conditioning changes only (a,c,v_0). Averaging the conditional measures preserves the same bound.

## Proof

For each cap-one coordinate density (f_i), write
[
  psi_i(t)=int_{mathbb R}e^{itx}f_i(x),dx.
]
The sharp one-dimensional input used in account01/B06 is
[
  int_{mathbb R}|psi_i(t)|^p,dtle rac{4pi}{sqrt p},
  qquad pge2. 	ag{1}
]
Apply account01/B06's translation-uniform geometric Brascamp--Lieb calculation to the two-dimensional Parseval frame (r_i=(w_i,v_i)). Since
[
  sum_{iin S}r_ir_i^	op=I_2,qquad |r_i|^2lerac12,
]
equation (1) gives the actual inequality
[
 int_{mathbb R^2}
 prod_{iin S}|psi_i(sw_i+tv_i)|,ds,dt
 le (4pi)^2. 	ag{2}
]
The left side is the (L^1)-norm of the characteristic function of ((L,V)). Fourier inversion in two dimensions therefore gives a continuous (C_0) joint density (p_{L,V}) and
[
  |p_{L,V}|_infty
  le rac{(4pi)^2}{(2pi)^2}=4. 	ag{3}
]

First set (eta=0) and omit harmless translations. On (E_r), the map
[
  (l,v)longmapsto (l,y)=(l,lambda(v-v_0)^2)
]
has at most two inverse branches. Each branch has Jacobian
[
  left|rac{dy}{dv}ight|
  =2|lambda|,|v-v_0|
  >2|lambda|r.
]
Consequently the off-fold pushforward density is
[
  h_r(l,y)=
  sum_{substack{v: lambda(v-v_0)^2=y\|v-v_0|>r}}
  rac{p_{L,V}(l,v)}
       {2|lambda|,|v-v_0|},
]
and (3) yields
[
  h_r(l,y)le
  rac{2cdot4}{2|lambda|r}
  =rac4{|lambda|r}. 	ag{4}
]

Now restore (eta B). Independence across the original-coordinate partition (Ssqcup R) is genuine. If (mu_{eta B}) is the probability law of (eta B), then addition in the second output coordinate gives
[
  g_r(l,y)=int_{mathbb R}h_r(l,y-z-c),dmu_{eta B}(z).
]
This is convolution by a probability measure in the second coordinate, so (4) implies
[
  |g_r|_inftyle|h_r|_infty
  lerac4{|lambda|r}.
]
Translations in the first output coordinate do not change the norm. This proves the theorem.

## Concrete live payment

At the standard spectral/off-fold gate
[
  |lambda|ge1,qquad r=rac1{64},
]
the theorem gives
[
  oxed{ |g_{1/64}|_inftyle256 } 	ag{5}
]
for every transverse coefficient (eta), however small, and for arbitrary fragmented or unbounded cap-one input laws.

This applies the completed account01/B06 mathematics at (2), then removes its (|eta|ge|lambda|r^2) gate whenever the transverse direction has a fresh original-coordinate bank. Compared with the exact three-bank endpoint in account01/B06, only the transverse bank must be fresh: (L) and (V) may overlap completely inside (S).

## Scope and remaining implication

The theorem closes the fresh-transverse part of
`QFORM-CURVED-SECTION-SMALL-BETA-OVERLAPPING-v1`.
It does not cover the genuinely shared-bank case in which (B) depends on the same original coordinates as ((L,V)). In that case the convolution step is unavailable, and replacing it by an arbitrary joint-density or worst-conditional-density estimate is invalid by the recorded corrections.

Thus the first remaining curved-section implication is now:

> control the off-fold map when the transverse linear statistic shares original coordinates with the curved pair, with (|eta|<|lambda|r^2), by integrating product Fourier volume and curvature jointly before inversion.

Arbitrary additional spectrum and the global reduction to this local geometry remain open.

## Sources

- Claude starting source: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.
- Completed account01/B06 curved-section theorem and scalar/BL input: `math-open-problems@3ae4b0c272e0d3c60f956c9f039bea38fc0f9077`.
- Completed account02/B06 weighted affine-fiber endpoint: `math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`.
- Corrections consumed: `QFORM-TWOSHEET-XRAY-ONLY-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-FIBERWISE-TRACE-MASS-BOUND-FALSE-v1`, and `QFORM-INDEFINITE-INNOVATION-ARBITRARY-REMAINDER-FALSE-v1`.
