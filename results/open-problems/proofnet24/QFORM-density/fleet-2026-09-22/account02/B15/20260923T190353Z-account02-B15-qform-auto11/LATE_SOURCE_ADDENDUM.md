# account02/B15 late-source addendum — full physical-triple receiver and optimized constant

Run `20260923T190353Z-account02-B15-qform-auto11`. Full unrestricted QFORM remains OPEN.

A later source commit landed after the main report:

`math-open-problems@9e2909942e0db085b66ce6bcefe663c879d89b44`,
`proofnet24/QFORM-density/interactive/20260923T191724Z-physical-three-core/REPORT.md`.

It proves a stronger receiver than the ruled majority-side theorem: if one **original-coordinate** principal `3x3` block `M=A_SS` satisfies `s_3(M)>=sigma>0`, then for arbitrary independent cap-one marginals, arbitrary outside coordinates/couplings, and arbitrary affine terms,

`||p_(X^T A X)||_infinity <= [3 e^(1/2) sqrt(2pi)+3sqrt(3)]/sigma <18/sigma`.

I independently checked the proof and record a small constant improvement below.

## 1. Exterior step audit

After conditioning on outside coordinates and completing the square in the three original coordinates,

`q(y)=y^T M y+c`,

with translated independent cap-one coordinate densities. For `|y|>=R`,

`|grad q(y)|=2|My|>=2 sigma R`.

Hence some original derivative satisfies

`|partial_i q|>=d:=2 sigma R/sqrt(3)`.

For fixed other two coordinates, `q` is quadratic in `y_i` and the restriction `|partial_i q|>=d` has at most two monotone branches. On each branch, inverse-function change of variables gives preimage length at most `h/d` for an interval of length `h`. Thus the two branches cost at most

`2h/d = sqrt(3) h/(sigma R)`.

Multiplying by the cap-one `i`-th density, integrating the other two probability densities, and summing over the three derivative events yields

`boxed(P(q in I, |y|>=R) <= 3sqrt(3) h/(sigma R)).`            (1)

No rotation of the product law is used.

## 2. Interior Gaussian-volume step audit

The translated joint density is pointwise at most one. On `|y|<=R`,

`1 <= e^(1/2) exp(-|y|^2/(2R^2))`.

For `G~N(0,R^2 I_3)`, diagonalization is used only inside the rotationally invariant Gaussian integral:

`|E exp(it G^T M G)|`
` = product_j (1+4 t^2 R^4 lambda_j(M)^2)^(-1/4)`
` <= (1+4t^2R^4sigma^2)^(-3/4)`.

Since

`int_R (1+u^2)^(-3/4) du <=6`, 

Fourier inversion gives

`||p_(G^T M G)||_infinity <= 3/(2pi sigma R^2)`.

Therefore

`boxed(P(q in I, |y|<=R) <= 3 e^(1/2) sqrt(2pi) R h/sigma).`   (2)

The affine completion shifts only the interval center and does not affect the estimate.

## 3. Optimizing the radius

The source sets `R=1`. But (1)-(2) hold for every `R>0`, so with

`a=3e^(1/2)sqrt(2pi)`, `b=3sqrt(3)`,

we have

`P(q in I) <= (aR+b/R) h/sigma`.

Choosing `R=sqrt(b/a)` gives

`boxed(||p_q||_infinity <= C_phys/sigma)`,

where

`C_phys = 2sqrt(ab) = 6 e^(1/4) (6pi)^(1/4) = 16.0527762227... <16.053.`   (3)

Averaging over outside coordinates preserves this bound. Thus the later physical-core theorem admits the slightly sharper universal constant `<16.053/sigma` without any new hypothesis.

The corresponding triangular owner-scale inequality is immediate:

`boxed(E (eps-|Q-y|)_+ <= C_phys eps^2/sigma)`                 (4)

whenever such a principal triple exists.

## 4. Consequence for the B15 unpaid ledger

This later theorem **removes the local minority/two-sheet gap whenever a uniformly conditioned physical principal triple is present**. In that branch one no longer needs to split the indefinite conditional law into one-sheet and two-sheet pieces at all: the exterior original-coordinate derivative estimate plus interior Gaussian volume pays the full conditional law directly, including all signs and affine shifts.

Accordingly, the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction remains important only for strategies that insist on the ruled/X-ray decomposition; it is no longer the first unpaid implication in the strong-physical-triple branch.

The first unpaid global implication is structural:

`boxed(From s_3(A)>=1, prove that either some original-coordinate 3x3 principal block has s_3>=sigma_0 universally, or one of the completed crossing/hub/volume/grouped-coordinate receivers fires with a universal bound.)`

The source itself correctly notes that `s_3(A)>=1` does not force such a physical triple: diffuse disjoint rank-one blocks can make every fixed physical `3x3` block `O(1/m)`. Thus the remaining problem is the no-strong-principal-triple regime, not rough-input limiting or continuity.

## 5. Relation to the pinned e5f theorem and this run's Fisher obstruction

The required pinned result `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` remains genuinely applied in the main report. For

`A=[[0,1,0],[1,0,0],[0,0,1]]`, `X_i~Uniform[0,1]`,

one has `Q=2X_1X_2+X_3^2>=0`, so the e5f majority one-sheet theorem pays the **entire** rough law with the sharper special-case constant

`||p_Q||_infinity <= pi sqrt(2)`

and tent bound `pi sqrt(2) eps^2`.

At the same time every H1 product approximation within joint L1 distance `eta<=1/8` of the cube has projected Fisher budget

`J_E>=3/(4eta)`.

So the regularity conclusion is now even cleaner: the rough target can be paid directly by geometry while every bounded-Fisher approximation budget fails. Continuity is neither needed nor useful for obtaining the height.

## 6. Implication ledger

- Absolute continuity remains qualitative and follows for nonconstant quadratics from coarea away from the critical subspace.
- Essential boundedness in the strong physical-triple branch is now paid directly by (1)-(3), for arbitrary rough cap-one inputs.
- Continuity is a separate conclusion; it is not used anywhere in (1)-(4).
- The Fisher and Gaussian-mixture fixed-budget classes remain non-dense at rough interval marginals, so they cannot by themselves close the unrestricted theorem by weak approximation.

This addendum supersedes only the main report's sentence identifying the minority/two-sheet term as the first unpaid local implication for a strong physical principal triple. All Fisher-closure obstructions and the pinned e5f rough witness remain valid.
