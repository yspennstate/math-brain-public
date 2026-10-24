# Quadratic-form density: current research

Programme QFORM-DENSITY-3EIG-20260922. Full conjecture: OPEN / NOT PROVED by the supplied arguments.

## Urgent correction: the arbitrary-joint coarea and conditional-moment gates are false

Read [the pair-log and correction handoff](handoffs/interactive/20260922T180015Z-pair-log.md). It preserves the original conjecture and the current exclusive QFORM assignment. The proposed mathematical lemmas in the revision-2026-09-22.9 owner-message source are not automatically valid premises.

**QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1.** The claimed `||p_Q||_infinity<=K||rho||_infinity^(2/3)` for arbitrary 3D joint probability density rho is false. The indicator of `{|z|<=1/(2pi delta), 0<=x^2+y^2-z^2<=delta}` has volume one and density cap one, but Q is exactly Uniform[0,delta]. Its density is 1/delta. This remains false for smooth compactly supported joint densities. This example has DEPENDENT coordinates: it refutes the proposed general-joint lemma, not the independent-input conjecture. It invalidates that route's declaration that the unrestricted exact-rank-three case is already solved.

**QFORM-CONDITIONAL-PROJECTION-POSITIVE-MOMENT-FALSE-v1.** For 3m independent Uniform[0,1] coordinates and Y the three block-constant projections, W its orthogonal complement,

`E||p_(Y|W)||_infinity^(2/3)=m^2[Gamma(m)Gamma(4/3)/Gamma(m+1/3)]^3 ~Gamma(4/3)^3 m ->infinity`.

The exact one-block fiber identity is `integral L^alpha=m^((alpha+1)/2)Gamma(m)Gamma(alpha+1)/Gamma(m+alpha)`. Every fixed positive conditional moment below exponent two diverges in this family. It also uses a valid FULL-RANK target matrix `P1+P2-P3+(I-PY)/128`. This is a false proof interface, not a large-output-density counterexample. Do not spend runs trying to prove that universal conditional moment.

Complete elementary proofs: `yspennstate/math-open-problems@f305dcc8ae0f602f2b21ab32cf4d8ddcdcb56b92:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/CORRECTIONS.md`, read-back blob `58a3d40f3722ebebccb922616467b75cd7f06ef5`. Preserve the source owner message and historical work; mark its invalid deductions rather than editing history.

## Constructive update: logarithmic two-coordinate smoothing

Full proof: `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`. Status: complete supporting analytic argument supplied; independent review pending.

For an exact-rank-three ORIGINAL-coordinate principal block with nonzero eigenvalue magnitudes >=s, and any invertible indefinite physical pair B, set D=|det B| and kappa=sigma_min(B). The FULL ambient form, including arbitrary outside coefficients/couplings and affine terms, satisfies

`||p_Q||_infinity <=8sqrt(5)(D*kappa*s)^(-1/4)`.

Both scalar diagonals of B can be zero. The pair-density envelope is `2sqrt(2)/r +D^(-1/2)log_+(2r^2/(kappa|t-t0|))`. Averaging its moving critical value against a Schur-remainder bound `P(|R-t|<rho)<=H sqrt(rho)` gives `4sqrt(2H)(D*kappa)^(-1/4)`. Exact rank three leaves a rank-one Schur coefficient of magnitude at least s, so the preceding affine rank-one small-ball lemma applies with H=10/sqrt(s). A localized target with |Aij|>=1/2 and associated diagonals <=1/4 in magnitude has sharpened bound <35.

This does not guarantee a uniformly conditioned physical pair under the bare spectral hypothesis, nor a rank-one remainder for arbitrary higher-rank forms. It therefore does NOT solve the unrestricted rank-three or full-matrix problem. Essential boundedness is established in the stated scope; continuity is not claimed. Existing account03/B05 and account04/B11 perform the requested mathematical reviews; other workers apply the exact scope to the remaining aggregate-before-inversion problem. Full proof and finite check sources/results are together at bundle commit `2823dfbc10490eb9b1aba6837ab6c9f9a1da1ca0`.

## New synthesis: every rank-two orientation, including arbitrary affine terms

Read [the complete source-pinned handoff](handoffs/interactive/20260922T161801Z-rank-two-fusion.md). The full proof is at `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`, blob `00681629acaba8f2e04edda6c9f6b5c4f0fdafa4`. Status: complete supporting analytic arguments supplied; independent reviews pending. Full target remains OPEN.

**QFORM-RANK2-AFFINE-HALF-RIESZ-v1.** For every U with two orthonormal columns, every invertible symmetric 2x2 Lambda, arbitrary b in R^n, and independent cap-one inputs,

`sup_t E |(U^T X)^T Lambda(U^T X)+b^T X-t|^(-1/2) <=128 |det Lambda|^(-1/4)`.

No leverage assumption and no affine-in-range restriction are imposed. Both definite and indefinite signatures are included. This is a fractional-potential estimate, NOT a bounded-density assertion for rank two. For b in range(U), including b=0, the constant improves to 16sqrt(30).

The proof combines account03/B16's translated quadratic kernel with the diffuse Fourier estimate and a rank-one affine small-ball lemma. In the heavy-coordinate case the arbitrary correlated translation disappears from the quadratic part after completing the square; the remaining affine term is retained explicitly. The small nonzero residual Rayleigh coefficient cancels exactly. The beta=0 case is proved separately by affine conditioning.

**QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1.** For an ORIGINAL-coordinate principal block of exact rank three, A_II=V M V^T, V^T V=I_3, with physical a=A_ii!=0 and c_i=||v_i||^2,

`||p_Q||_infinity <=128 [c_i |a| |det M|]^(-1/4)`.

This includes arbitrary outside quadratic coefficients and cross couplings: induced original-coordinate affine terms are covered by the first theorem. The orthonormal Schur frame has exact determinant coefficient det N=c_i det M/a. For a full exact-rank-three target matrix, this implies 128/sqrt(|A_ii|).

The former account01/B10 small-Rayleigh strip INSIDE the rank-two Schur remainder is removed in this half-Riesz route. The small/zero OUTER scalar pivot and arbitrary higher-rank Schur remainders remain unresolved outside the precisely stated supporting branches above. Do not interpret the rank-two theorem as applying to every higher-rank form with two large eigenvalues.

Existing account03/B16 and account01/B10 perform the two specified independent mathematical checks and record actual results. Other B10/B11/B16/B19/B20 workers should apply the stated theorem to the remaining outer-pivot and full-matrix steps rather than duplicate the reviews. Follow the current proof-first owner request in AGENTS.md; do mathematics, not a new sign-in campaign.

## Authoritative source and exact quantifiers

Read the [owner message at its immutable source](https://github.com/yspennstate/math-research-brain/blob/0dc369ddf8b860648dd780d8f92c62994dc53ecf/scheduled_tasks/README.md). For every n, independent real X_i with probability densities f_i satisfying 0<=f_i<=1, and real symmetric A with at least three eigenvalues of absolute value>=1, prove the law of Q=X^T A X has a density p_Q with essential supremum<=C for one universal finite C, or give a valid counterexample.

The separately referenced Downloads/Quadratic_Form_Bounded_Density_Conjecture_report.md and qform/thresh.py/refine.py were not yet found in the accessible committed source directories. The owner message itself supplies the complete working statement. Do not invent contents or native-ingestion receipts.

No moments, centering, identical distributions, log-concavity, continuity or connected support are assumed for the input densities. A rotation diagonalizes A but usually makes the new coordinates dependent. The main goal is a universal density bound; continuity is an additional desired conclusion and should be stated separately.

## Decisive route corrections

**Pointwise oscillatory decay is false under the stated input assumptions.** For any frequency s>0 and small delta>0, the set {x:dist(s x^2,2pi Z)<=delta} has infinite Lebesgue measure. Choose a finite union of intervals inside it of total length1, and take its indicator as a probability density. Then Re E exp(isX^2)>=cos(delta). Therefore no uniform K|s|^-1/2 bound is possible over all densities<=1. Three independent such inputs similarly defeat the proposed universal pointwise |t|^-3/2 envelope, even for a diagonal form. This does not disprove bounded output density, nor by itself a uniform integrated Fourier bound.

**Spectral-fiber maxima can lose dimension.** For product uniforms on a cube and a two-dimensional subspace spanned by the constant directions in two blocks of m coordinates, the integral over the orthogonal complement of the supremum of the product density along a fiber equals the projected cube volume m. Thus bounding each two-dimensional spectral integral only by a fiber supremum does not yield a dimension-independent argument.

**Projection densities preserve neither independence nor finite indefinite level volumes.** A correct bounded-density projection theorem is useful, but an additional curved-measure argument is required. No characteristic-function estimate may be transferred from a decreasing rearrangement bound to a pointwise bound.

**The diagonal constant pi is not universal for the rotated problem.** The live correction inbox records an analytic lower bound C>=3sqrt(2). Continue to use pi only in its proved diagonal scope. Read every newer source-bound correction before applying an intermediate assertion.

## Proven control theorem: all diagonal forms

For Y=a(X-b)^2 with a>0 and f_X<=1, its density satisfies g_Y(y)<=1/sqrt(a y) for y>0. Two independent same-sign square terms with coefficients a,b>0 have convolution density at most pi/sqrt(ab), by the beta integral integral_0^y [u(y-u)]^-1/2 du=pi. Among three diagonal coefficients of magnitude>=1, two have the same sign. Reflection handles negative terms; convolution with all remaining independent terms cannot increase the bound. Hence every diagonal form under the target assumptions has density<=pi, for arbitrary input laws, and the argument also allows linear shifts/completing squares. This is a supporting theorem, not the general rotated result.

## Current proof routes

1. A uniform integrated characteristic-function estimate (or rearrangement/averaged estimate) may survive the pointwise counterexample. The ridge-window handoff in AGENTS.md records a complete supporting argument allowing nonseparable small tails under a spectral-window leverage condition; it does not follow from the bare three-eigenvalue hypothesis.
2. A direct small-ball inequality P(Q in[a,a+epsilon])<=C epsilon would imply the required essentially bounded density. This avoids unjustified Fourier regularity assumptions.
3. Geometric product-measure/coarea methods must keep curvature and the coordinate product structure together, rather than taking unrestricted fiber suprema or the disproved arbitrary-joint coarea and positive conditional-density-moment gates.
4. Localized/delocalized eigenvector decompositions, bilinear conditioning and a genuine averaging of coordinate minors may convert three spectral directions into a dimension-free bound. Use the new orientation-free rank-two affine half-Riesz theorem in scalar-Schur arguments and the pair-log theorem for the stated two-coordinate branches; avoid obsolete residual-Rayleigh case splits within their exact scopes.

The original uniform simulations are exploratory controls. A centered interval has not been proved extremal for arbitrary rotated indefinite forms. Rank-two opposite signs remain a mandatory logarithmic-singularity control. Source-backed derivations and subsequent corrections go into immutable reports; update claim statuses only at the scope actually established.
