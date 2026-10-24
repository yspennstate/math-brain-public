SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B10, 2026-09-22T19:36:53Z.
attacking: exact-rank-three heavy null row; combine the named partner's null-bank compression with a new nested-heavy pivot-or-indefinite-pair dichotomy, without conditioning away product provenance.

# account02/B10 r15 — nested-heavy null rows are already paid

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Owner control observed before publication:** revision 2026-09-22.15  
**Assignment:** Rank-three coupled case; complementary constructions/source-valid counterexamples  
**Execution:** WITHOUT_VERIFIED_BRAIN  
**Classification:** ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN

The full target remains OPEN. No projected spectral coordinates are declared independent. All density theorems below are applied only after conditioning on or regrouping genuine original independent coordinates in scopes already proved by their source reports.

## 1. First unpaid implication attacked

The latest completed named partner account03/B10 result is `QFORM-NULL-BANK-CAPONE-COMPRESSION-v1`, canonical source

`yspennstate/math-open-problems@a3dd62b198d84dc9b92653b8a9c77494fc6ed2d4`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260922T191739Z-account03-B10-QFORM-r15/REPORT.md`.

For an exact null-ray bank of spectral mass `L`, it replaces the entire bank by one genuine independent cap-one variable and rewrites the same law as an exact-rank-three Parseval form with

`q=1-L/2`, `|det Mhat|=q|det M|`, `sigma_min(Mhat)>=q sigma_min(M)`,

synthetic null-row leverage `c=L/(2-L)`, and null-row pair-determinant mass `(L/2)||Mr||^2`. In the near endpoint `L>=7/8`, this gives

`c>=7/9`, `sigma_min(Mhat)>=1/2`, `|det Mhat|>=1/2`.

Its first unpaid state allowed a second row to remain heavy after removing the null direction and then asked for overlapping-leakage aggregation. The new result below proves that **the second-heavy case is already universally paid even with complete support overlap**. Thus only the residual-diffuse overlap branch survives from that partner state.

Corrections retained: arbitrary-joint rank-three coarea is false; positive conditional projection-density moments are false; bounded conditional caps do not replace independence; pointwise law-uniform Fresnel decay and vector-fiber suprema are not used.

## 2. New matrix lemma

### Theorem 2.1 — `QFORM-NULL-ROW-NESTED-HEAVY-CLOSURE-v1`

Let

`A=U M U^T`, `U^T U=I_3`,

be an exact-rank-three form in independent cap-one physical coordinates. Put

`sigma=sigma_min(M)>0`.

Suppose physical row `i` has

`u_i=sqrt(c) r`, `|r|=1`, `c>0`, `A_ii=c r^T M r=0`.

For another physical row write

`u_j=alpha r+beta e+gamma w`

in the orthonormal spectral basis constructed below, and assume its residual leverage

`h=||(I-rr^T)u_j||^2=beta^2+gamma^2>1/2`.

Then at least one of the following holds:

1. **nonzero-pivot branch**

   `|A_jj| >= 3 sigma/8`;

2. **uniform indefinite-pair branch**

   `|A_ij| > sqrt(c) sigma/32`.

Moreover, in branch 2 under `|A_jj|<3sigma/8`, the physical pair

`B=[[0,A_ij],[A_ij,A_jj]]`

is invertible indefinite and, for every fixed lower leverage threshold `c>=c_*>0`,

`|det B| >= c_* sigma^2/1024`,

`sigma_min(B) >= k(c_*) sigma`,

where

`k(c_*)=(c_*/1024)/(sqrt(c_*)/32+3/8)`.

### Proof

Because `r^TMr=0`, the vector `Mr` is perpendicular to `r`. Put

`s=||Mr||` and `e=Mr/s`.

Since `M` is invertible, `s>0`; in fact `s>=sigma`. Complete `(r,e)` to an orthonormal spectral basis `(r,e,w)`. In this basis

`M=[[0,s,0],[s,d,g],[0,g,f]]`.                         (2.1)

Its determinant is `-s^2 f`, so `f!=0`, and direct inversion gives

`M^{-1}=[[ (g^2-df)/(s^2 f), 1/s, -g/(sf)],
          [ 1/s,                    0,       0],
          [-g/(sf),                 0,     1/f]]`.          (2.2)

Since `||M^{-1}||<=1/sigma`, every displayed entry is bounded in modulus by `1/sigma`. Hence

`s>=sigma`, `|f|>=sigma`,

`|g|<=s|f|/sigma`,

`|d|<=g^2/|f|+s^2/sigma
      <=s^2|f|/sigma^2+s^2/sigma`.                         (2.3)

Now `||u_j||^2<=1` because `U^TU=I_3`. Since `h>1/2`, this gives `|alpha|<1/sqrt(2)`. Put

`x=s|beta|`.

The physical cross coefficient is

`|A_ij|=sqrt(c)|r^T M u_j|=sqrt(c) x`.                     (2.4)

The second pivot is

`A_jj=2s alpha beta+d beta^2+2g beta gamma+f gamma^2`.      (2.5)

Assume `x<=sigma/32`. Then `beta^2<=1/1024`, and from `h>1/2`,

`gamma^2>1/2-1/1024=511/1024`.                            (2.6)

Using (2.3), `|gamma|<=1`, and `|alpha|<1/sqrt(2)`, the three error terms in (2.5) obey

`|2s alpha beta| <= sqrt(2) sigma/32`,

`|d| beta^2 <= |f|/1024+sigma/1024`,

`|2g beta gamma| <= |f|/16`.                              (2.7)

Therefore

`|A_jj|`
`>= |f|(511/1024-1/1024-1/16)`
`   -sigma(sqrt(2)/32+1/1024)`
`>= sigma(223/512-sqrt(2)/32-1/1024)`
`>3sigma/8`.                                               (2.8)

(The numerical gap is about `0.015376 sigma`.) This proves the stated dichotomy by contraposition.

In branch 2, `det B=-A_ij^2<0`. Write `a=|A_ij|` and `b=|A_jj|`. If `b<3sigma/8`, then

`a>=sqrt(c_*)sigma/32`.

For `[[0,a],[a,b]]`, the smaller singular value is

`(sqrt(b^2+4a^2)-b)/2`
`=2a^2/(sqrt(b^2+4a^2)+b)`
`>=a^2/(a+b)`.

The last expression is increasing in `a`, so substituting the lower bound on `a` and the upper bound on `b` gives exactly

`sigma_min(B)>=k(c_*)sigma`.                               (2.9)

Also `|det B|=a^2>=c_*sigma^2/1024`. QED.

## 3. Density consequence inside the exact-rank-three target

Two completed source theorems are now applied, not re-proved:

* `QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1`, source `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, proves

  `||p_Q||inf <=128[c_j |A_jj| |det M|]^(-1/4)`

  for a nonzero physical pivot, with arbitrary affine/outside terms.

* `QFORM-RANK3-INDEFINITE-PAIR-PIVOT-v1`, source `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`, proves for an invertible indefinite physical pair

  `||p_Q||inf <=8sqrt(5)(D*kappa*sigma)^(-1/4)`,

  where `D=|det B|` and `kappa=sigma_min(B)`.

Because the row `j` in Theorem 2.1 has full leverage `c_j>=h>1/2`, the pivot branch gives

`||p_Q||inf <=128[(1/2)(3sigma/8)|det M|]^(-1/4).`          (3.1)

In the pair branch, Theorem 2.1 gives

`||p_Q||inf`
`<=8sqrt(5)[(c_*/1024) k(c_*) sigma^4]^(-1/4).`             (3.2)

These are uniform constants whenever `c_*`, `sigma`, and `|det M|` have fixed positive lower bounds.

For the **original exact-rank-three target** with all three nonzero eigenvalue magnitudes at least one, take `sigma>=1`, `|det M|>=1`. If the null row has leverage `c>=1/12` and a residual-heavy row exists, then `c_*=1/12`; (3.1) is `<195` and (3.2) is `<1562`. Thus this whole nested-heavy zero-pivot branch is target-level closed by an explicit universal constant.

## 4. Direct application of the named partner result

Now apply account03/B10 r15 exactly in its near-endpoint state `L>=7/8`. Its product-preserving compression yields

`c>=7/9`, `sigma>=1/2`, `|det Mhat|>=1/2`.

If any complementary physical row has residual leverage `h>1/2`, Theorem 2.1 applies with `c_*=7/9`.

The pivot branch (3.1) is then

`||p_Q||inf <=128(3/64)^(-1/4) <276`.                      (4.1)

For the pair branch,

`k(7/9)=7/[96(36+sqrt(7))] >0.0018867`,

and (3.2), with `sigma>=1/2`, gives

`||p_Q||inf <1035`.                                        (4.2)

Hence the partner's compressed near-endpoint **nested-heavy overlap branch is completely paid**, without support separation and without selecting a third determinant atom. No conditional-density surrogate is used.

This is the named-partner application required by the assignment: account03/B10's null-bank compression supplies the genuine independent synthetic coordinate and the quantitative `(c,sigma,det)` lower bounds; the new dichotomy then feeds those exact numbers into two completed density inequalities.

## 5. What remains after the new closure

For a compressed heavy null row, the overlap problem may now be restricted to the **residual-diffuse** case

`||(I-rr^T)u_j||^2 <=1/2 for every complementary physical row j`. (5.1)

The coefficient vectors in `r^perp` form an exact two-dimensional Parseval frame, so (5.1) is precisely the regime where its transverse two-dimensional projection is diffuse. The remaining problem is not a missing large local minor: it is to combine that diffuse transverse product projection with the heavy null hyperbolic coordinate before the logarithmic singularity is paid.

The first unpaid implication is therefore

**`QFORM-NULLROW-RESIDUAL-DIFFUSE-OVERLAP-v1`**: prove a universal density bound for the exact-rank-three heavy-null state in which every residual leverage is at most one half, retaining the orthogonality of the leakage coefficient vector to the two-dimensional residual Parseval frame and avoiding any positive conditional-profile-height moment.

A separate still-open bridge is the genuinely **near-zero but nonzero** outer physical pivot. The live correction `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1` prevents treating that case as a trivial perturbation of the exact-null theorem.

Thus the full QFORM conjecture, and even unrestricted arbitrary-orientation exact rank three, remain OPEN.

## 6. Exact checks

A deterministic algebra/stress checker accompanies this report. It verifies the constant arithmetic and tests the implication

`x<=sigma/32 => |A_jj|>=3sigma/8`

on 196,398 admissible randomly generated null-basis instances after filtering for positive spectral scale; no failure was observed. This is diagnostic only. The proof of Theorem 2.1 is the exact inverse-matrix calculation above, not finite sampling.

## 7. Source status

Fresh protected control before publication remained QFORM-only. The latest live correction inbox was re-read before this write. No source-backed correction found there challenges the partner compression, the rank-two affine/rank-three pivot theorem, or the exact-rank-three pair-log theorem used above. The current newly observed decoupled-L3 correction concerns a different Fourier/decoupling interface and is not used here.

No moments, support regularity, log-concavity, Gaussianity, rotation-independence, or conditional cap assumptions are introduced. Essential boundedness is the only regularity conclusion in the new branch; continuity is not proved here.
