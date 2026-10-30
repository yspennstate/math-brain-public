# fleet03/B01 repeated audit — r17

Source: `yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c`
TeX blob: `c4f2a997cf336ee974e15409b5bccdd8cca039d8`
PDF SHA256: `4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423`

## Verdict
Fresh reverse-dependency and rough-law reconstruction found no fatal or constant-changing defect in Theorem 1.1. After the local repairs already documented by the fleet, the argument still yields the claimed essential density bound (270K^2/s), with arbitrary real symmetric signature and remaining spectrum, arbitrary affine terms, arbitrary dimension, and only independent original-coordinate densities bounded by (K).

The full theorem establishes essential boundedness. Continuity is proved in the integrable-Fourier/no-pivot branch only.

## Independent clause audit: Lemma 3.2, line 224
The proof takes (log p(y)) after proving (p(y)le prod_i(int h_i)^{eta_i}). Literal issue: (p(y)) can be zero, while the manuscript has not declared (log0=-infty).

Minimal repair: split the case (p(y)=0), where the desired (p(y)le e^{d/2}) is immediate; otherwise take logarithms. No constant or downstream statement changes.

This was derived directly from the pinned source before comparison. Afterward, fleet02/B12 run `20260925T070427Z-fleet02-B12-five-short-audit-r27` was consulted and independently records the same local issue as C12.

## Independent clause audit: Lemma 5.6, lines 505-509
The envelope (h(y)=6+log_+(16/|y|)) is not literally defined at (y=0), because the paper defined (log_+u) only for (u>0). The rearrangement lemma expects a function on all of (mathbb R).

Minimal repair: define (h(0)=+infty). This changes no integral, probability law, or constant.

After this repair, the displayed integral at line 507 is **arithmetically correct**:
[
int_{-delta}^{delta}!left(6+lograc{16}{|y|}ight)|y|^{-1/2},dy
=4sqrtdeltaleft(8+lograc{16}{delta}ight).
]
Indeed, the constant (6) contributes (24sqrtdelta), while the logarithmic term contributes (4sqrtdelta(log(16/delta)+2)). For (delta=1/64) this equals (4+5log2). Thus no arithmetic repair is needed at line 507.

The resulting bound
[
mathbb E|Y-b|^{-1/2}le 8+(4+5log2)=12+5log2<16
]
is valid.

After deriving this independently, fleet02/B12 r27 was compared and independently notes the same (h(0)) version issue.

## Dependency regression
- Fourier normalization, Gaussian representation, half-potential identity: PASS.
- Conditioning lemma: PASS; all conditioning remains on original coordinates.
- Singular-value/Schur chain: PASS after the local zero-padding edge-case repair already identified for Lemma 2.5.
- Brascamp--Lieb heat flow and product projection: PASS after splitting (p(y)=0) before line 224.
- Fourier-power lemma: PASS.
- Hub compiler: PASS after inserting the explicit Jensen step and establishing measurability of (xmapsto|
u_x|_2^2) via the fixed approximate-identity sequence.
- Elliptic/hyperbolic pivot lemmas: PASS after the known chart-seam, critical-level and density-version repairs.
- Concentration/log-moment/kernels/pair-half-potential: PASS after defining (h(0)=+infty); line 507 arithmetic independently confirmed.
- Random-sign fourth moment and crossing-spectrum duplication: PASS.
- No-pivot, diagonal-pivot, definite-pair and indefinite-pair terminal cases: PASS after upstream local repairs.
- General (K,s) scaling and arbitrary affine terms: PASS.

Terminal normalized bounds retain margin: no-pivot (<167), diagonal pivot (sqrt{12},77<267), definite pair (16pi<51), indefinite pair (<269).

## Remaining unchecked
Fresh rendered-PDF-versus-TeX glyph comparison remains UNCHECKED because the private PDF is unavailable to the required screenshot surface in this runtime. No render-equivalence claim is made.

Native brain status remains `WITHOUT_VERIFIED_BRAIN`.
