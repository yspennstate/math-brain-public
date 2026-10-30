# fleet04/B20 — projection-cap hyperbolic-square closure

Run: `20260922T132134Z-fleet04-B20-QFORM-r1`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Status: `ESSENTIAL_STEP_APPLIED / FULL_CONJECTURE_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction-aware scope

The target is a universal finite (C) such that, for every dimension, every product law with one-dimensional densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one,
[
  mathbb P{X^TAXin[t,t+h]}le Ch
]
for all (tinmathbb R) and (h>0).

This report does not assume independence after a general rotation, pointwise Fresnel decay, compact support, moments, log-concavity, connected support, or a diagonal basis. It does not use a generic bounded projection density as a substitute for an indefinite level-set estimate. Instead it preserves independence by aggregating **disjoint original-coordinate blocks** and then applies a nonlinear density theorem.

The named partner `fleet01/B20` had no completed current-QFORM report located in the source snapshot, so no partner result is invented. The completed OTHER-account result actually applied is fleet01/B19's hard family, source-read at
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B19/20260922T121338Z-b19-qform-r11/REPORT.md`.
The nonlinear input is fleet02/B10's proved `QFORM-HYPERBOLIC-SQUARE-v1`, canonical report
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260922T1147Z-qform-rank3-coupled-B10-r1/REPORT.md`,
creation commit `1eba911614ef9f6683f8eacb5d6608a0f9a4b833`.

## 2. Compact conditional end-to-end chain

The present best proof assembly has already closed:

1. the full near-coordinate-diagonal basin by a definite physical pair;
2. a diffuse spectral-frame basin by integrated Fourier estimates;
3. physical triangular hyperbolic-square triples; and
4. finite-union product indicators as an exact extremal testing core.

The first hard model not covered by fixed physical triples is fleet01/B19's rank-three family
[
 A_m=Uegin{pmatrix}0&1&0\\1&0&0\\0&0&1end{pmatrix}U^T,
]
whose nonzero eigenvalues are (1,1,-1), but whose every fixed physical three-coordinate block degenerates as (m	oinfty). Product-preserving aggregation gives
[
 X^TA_mX=2X_0Y_m+Z_m^2,qquad
 Y_m=m^{-1/2}sum_{jin Y}X_j,quad
 Z_m=m^{-1/2}sum_{kin Z}X_k .
]
The remaining issue is to combine the actual projection-density theorem with the nonlinear hyperbolic-square integral without losing dependence or dimension. The theorem below does exactly that for every disjoint-block normal form.

## 3. General cap-parametric theorem

### Theorem `QFORM-AGGREGATE-HYPERBOLIC-SQUARE-v1`

Let (I,J,K,L) be pairwise disjoint sets of original coordinate indices. Put
[
 U=sum_{iin I}e_iX_i,qquad
 V=sum_{jin J}c_jX_j,qquad
 Z=sum_{kin K}d_kX_k,qquad W=(X_ell)_{ellin L}.
]
Assume (U,V,Z) have densities bounded respectively by finite constants
(M_U,M_V,M_Z). They are mutually independent and independent of (W).

Let (a,b
e0). Suppose that, conditionally on (W=w), a real random variable (T) has the form
[
 T=2aUV+alpha(w)U+H_w(V)+bigl(Z+	heta_w(V)igr)^2+G(w),
]
where (H_w,	heta_w) are arbitrary measurable functions and (alpha,G) are arbitrary measurable scalar functions. Then (T) is absolutely continuous and
[
 oxed{ |p_T|_infty
 le {4M_Zsqrt{M_UM_V}oversqrt{|ab|}} }.
]
The estimate is uniform in the outside dimension, the law of (W), and every displayed measurable shear/translation.

#### Proof

Fix (w). Translate
[
 widetilde V=V+{alpha(w)over2a}.
]
Translation preserves the density cap (M_V), independence from (U,Z), and rewrites the conditional polynomial in the same form with (alpha=0) after changing (H_w,	heta_w,G(w)).

Scale
[
 U'=M_UU,qquad V'=M_Vwidetilde V,qquad Z'=M_ZZ.
]
Each primed variable has a probability density bounded by one, and the three remain independent. After absorbing the deterministic scaling into the arbitrary functions,
[
 T
 =2a'U'V'+H'_w(V')
   +b'igl(Z'+	heta'_w(V')igr)^2+G'(w),
]
where
[
 a'={aover M_UM_V},qquad b'={bover M_Z^2}.
]
Fleet02/B10's source theorem gives
[
 |p_{Tmid W=w}|_infty
 le {4oversqrt{|a'b'|}}
 ={4M_Zsqrt{M_UM_V}oversqrt{|ab|}}.
]
This bound is independent of (w). Averaging the conditional densities therefore gives the same unconditional bound. The conditional construction also proves absolute continuity. QED.

This proof does not infer independence of spectral coordinates. It uses only the genuine independence of disjoint original-coordinate blocks.

## 4. Sharp projection insertion

Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, prove that every one-dimensional orthogonal marginal of a product probability density with one-dimensional factors bounded by one has density at most (sqrt2).

Consequently, for every nonzero coefficient vector,
[
 M_Ule{sqrt2over|e|_2},qquad
 M_Vle{sqrt2over|c|_2},qquad
 M_Zle{sqrt2over|d|_2}.
]
Inserting these **before** the nonlinear estimate gives
[
 oxed{ |p_T|_infty
 le {8over
 sqrt{|ab|},|d|_2,sqrt{|e|_2|c|_2}} }.
]
This is the requested projection-product interaction: the projection theorem supplies scalar caps, while the hyperbolic-square theorem spends them through a direct square-root-kernel integration. A bounded joint projection density by itself is never used to integrate an indefinite level set.

If one of the blocks is a single physical coordinate with its original density cap one, retain that stronger cap instead of replacing it by (sqrt2).

## 5. Actual inequality on the fleet01/B19 hard family

For the family (A_m),
[
 U=X_0,quad V=Y_m,quad Z=Z_m,quad a=b=1.
]
The coefficient vectors of (Y_m,Z_m) have Euclidean norm one. Hence
[
 M_Ule1,qquad M_Vlesqrt2,qquad M_Zlesqrt2.
]
The theorem yields
[
 oxed{ |p_{X^TA_mX}|_infty
 le4sqrt2,sqrt{sqrt2}
 =2^{11/4}<6.728 }.
]
This improves the previously recorded safe bound
(4(2sqrt2)^{3/2}=2^{17/4}<19.1)
and is uniform in (m), all admissible input laws, and all translations generated by conditioning outside coordinates.

If all three normalized variables are genuine aggregate blocks, the same calculation gives the universal normal-form cap (8/sqrt{|ab|}).

## 6. What is and is not closed

Closed here:

- arbitrary cardinalities of the three disjoint original-coordinate blocks;
- arbitrary density-(le1) product inputs;
- both signs of (a,b);
- arbitrary measurable (V)-shears and outside-conditioned translations;
- absolute continuity and an explicit essential-supremum bound;
- the full fleet01/B19 delocalized saddle family with constant (2^{11/4}).

Not closed:

- an arbitrary rank-three symmetric matrix need not admit three disjoint aggregate blocks in this triangular hyperbolic-square normal form;
- (U^2) or (UZ) terms cannot be silently absorbed by the displayed shears;
- additional spectral directions in a general matrix remain an interaction debt;
- continuity of the density is not proved by this argument.

Thus the full conjecture remains open. The sharpened first missing implication is:

`QFORM-AGGREGATE-NORMAL-FORM-EXTRACTION-v1`: in the leverage-heavy, near-isotropic minority-sign branch, either extract disjoint original-coordinate blocks with the displayed normal form and a dimension-free lower bound on
[
 |ab|,|d|_2^2|e|_2|c|_2,
]
or supply a different product-preserving aggregate mechanism that handles the residual (U^2/UZ) couplings before any reciprocal minor is paid.

## 7. Integrity and status

This is `ESSENTIAL_STEP_APPLIED`, not a full proof. No source correction is contradicted. The theorem proves an essentially bounded density at its scope; continuous density remains separate and unproved. No native brain retrieval/context use occurred, so the execution status remains `WITHOUT_VERIFIED_BRAIN`.
