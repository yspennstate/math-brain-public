# Least singular value lower bound for tensorized Ginibre matrices in Lean

The preprint arXiv:2606.01664 proves that the spectral measure of a noncommutative 
polynomial evaluated in independent Ginibre matrices, converges to the limiting 
Brown measure in free probability theory. The convergence holds for polynomials of
any degree. The main component of the proof is a least singular value lower bound
for the polynomial valued Ginibre matrices shifted by a deterministic nonzero spectral
shift. Via a linearisation argument, the problem transforms to the least singular value
of tensor products of independent Ginibre matrices, where the coefficient of the tensor 
product is arbitrary. This is stated as Theorem 1.5 of arXiv:2606.01664, whose proof occupies
all of sections 3 and 4. We formalise the proof of Theorem 1.5 in this lean 4 project. 
The project also formalises other useful results in smoothed analysis and least singular
value estimates in random matrices. For example, we prove least singular value bounds for a
Ginibre matrix perturbed by an arbitrary deterministic matrix.


This Lean 4 project formalizes the square-matrix least-singular-value argument
of Sections 3 and 4 of arXiv:2606.01664 and proves the paper-facing Theorem
1.5.  The final endpoint is `GinibreLSV.Section3.theorem15`: for every
`m,n ≥ 1` it proves `Theorem15 m n`, with exponents uniform over the fixed
matrix dimensions and coefficient-dependent leading constant and threshold.
The development includes the algebraic, robust-Burnside, covariance,
conditional Gaussian, negative second-moment, and invariant-factor recursion
layers used by that theorem.

An early reusable square-Ginibre input is
`GinibreLSV.complexGinibre_leastSingularValue_smallBall`:

```text
P(s_min(G) < r / (n + 1))
  ≤ (n + 1) · gaussianPeak(1) · (2r),       r ≥ 0.
```

Thus taking `r` of order `(n + 1)⁻²` gives a genuine polynomial square bound
of the shape

```text
P(s_min(G) < (n + 1)⁻³) ≤ C / (n + 1)
```

for this unnormalized Gaussian convention. If the matrix is normalized by
`1 / sqrt(n + 1)`, the threshold rescales accordingly.

## What is formally verified

### Section 3.1 algebraic layer

- the generated coefficient algebra `alg(I, R i)`;
- equivalence between common invariant complex subspaces and submodules over
  the generated coefficient algebra;
- equivalence between family irreducibility and the absence of nonzero proper
  common invariant subspaces;
- the complex Schur lemma for the commutant of an irreducible coefficient
  action;
- the finite-dimensional complex Burnside theorem:
  irreducibility is equivalent to generating the full endomorphism algebra;
- existence of a composition filtration in finite complex dimension;
- simplicity of every successive quotient `Z_(a+1) / Z_a`;
- the bound “number of factors ≤ dimℂ Z”;
- the induced diagonal coefficient action `R_i^(a)` on every simple quotient.

### Section 3.2 and Proposition 3.2

- the Hilbert--Schmidt pairing `Tr(A† B)` on the endomorphism space;
- `Σ_R = span {R_i}` and its Hilbert--Schmidt relation space `D_R`;
- `Y(E) = span_i (R_i† E)`;
- preservation of irreducibility after taking adjoints;
- the Burnside bridge from adjoint-coefficient invariance to invariance under
  every left multiplication;
- exclusion of nonzero left ideals contained in `D_R` for a nontrivial
  irreducible action;
- Proposition 3.2: every nonzero `E ≤ D_R` satisfies `Y(E) ⊈ E`;
- the dimension surplus
  `dim(E ∩ Y(E)) + 1 ≤ dim Y(E)`;
- the degenerate zero-action identities `Σ_R = 0`, `D_R = End(Z)`, and
  `Y(E) = 0`.

### Section 4.1 and Proposition 4.1

- the compact space of norm-one orthogonal projections with range in `D`;
- continuity and strict positivity of the total leakage functional;
- the uniform robust Burnside estimate (4.8), simultaneously for every
  nonzero subspace `E ≤ D`;
- the projection-injectivity and non-strict dimension comparison used in
  Proposition 4.1;
- Lemma 4.2 with its sharp reverse-inclusion constant
  `τ / sqrt (1 - τ²)`;
- the orthogonal tube decomposition and radius estimate (4.10) from
  Lemma 4.3;
- positivity of finite covariance sums and the covariance compression
  identity (4.13);
- the Hilbert--Schmidt realization of square complex matrices and the
  rank-one operator `B ⊗ B*`;
- the matrix covariance formulas (4.15)--(4.16), including the explicit
  action `Γ_B(A) = ∑_j ⟨B_j,A⟩ B_j`;
- the normalized complex Gaussian realization `g_i = (x_i + I y_i)/sqrt 2`,
  its exact moments `E[g_i conj(g_j)] = δ_ij`, circularity
  `E[g_i g_j] = 0`, and mean zero;
- the real continuous-linear realization of arbitrary sums `∑ g_i e_i`,
  their Gaussian pushforward laws, and the identity between real covariance
  and one half the real part of the complex covariance;
- equality in distribution for any two proper centered complex Gaussian sums
  with the same covariance operator, even with different coefficient counts;
- the adjoint identity `L_T* = L_(T*)` for left matrix multiplication and
  both the deterministic and actual centered-Gaussian identities
  `Γ_X = ∑_i L_i Γ_B L_i*` for `X = ∑_{i,j} g_ij T_i B_j`;
- the codimension-one smallest-eigenvector removal step from Section 4.1.3;
- the exact projection-error and discarded-covariance trace identities in
  (4.14), followed by the bound by the eigenvalue threshold `τ`;
- exact additivity of successive orthogonal extraction errors;
- the consecutive inverse-power error bound (4.32);
- dimension loss by the number of removed covariance directions;
- the conditional Lemma 4.10 stopping endpoint: a positive covariance lower
  bound forces the projected profile to span the retained space and satisfy
  the paper's regularity conditions;
- the trace/average-eigenvalue argument forcing the extraction to stop;
- an explicit terminal dimension and an orthonormal batch of covariance
  eigenvectors representing the paper's dependent recursive deletion;
- persistence of every selected eigenvector through all earlier projections,
  with the required stepwise inverse-power bounds;
- the terminal Rayleigh-quotient lower bound on the retained spectral
  subspace and its transfer to the covariance of the projected profile;
- the end-to-end deterministic Lemma 4.10 endpoint: under the paper's
  threshold-sum hypotheses, the construction satisfies (4.32) and produces
  a regular profile of exactly the terminal dimension;
- monotonicity of finite conjugation sums and the covariance lower-bound
  propagation (4.17).
- the synthesis map `Ψ_E` and its SVD-defined active image `Y_σ(E)`;
- the quotient projection `P_(Y⊥)|_E` and its low-singular-value space
  `C_{τ,σ}(E)`;
- the exact complementary-space identity for the selected right singular
  vectors and the lower singular-value estimate on its orthogonal complement;
- orthogonality of the quotient-projection images of the low and complementary
  right-singular components;
- the active/inactive decomposition, with the required operator-norm bounds;
- an explicit uniform synthesis-operator bound `∑_i ‖S_i‖`;
- the quantitative leakage contradiction at the heart of Proposition 4.1;
- Proposition 4.1 itself: uniform `σ0 ∈ (0,1)` and `τ0 > 0` for which
  `dim C_{τ,σ}(E) + 1 ≤ dim Y_σ(E)` for every nonzero `E ≤ D`.
- the multidimensional shifted complex-Gaussian small-ball estimate, with
  complex dimension (rather than real dimension) in the exponent;
- the isotropic and diagonal covariance-lower-bound forms of (4.24), namely
  `(C δ² / v)^dim` when every complex-coordinate variance is at least `v`;
- invariance of that estimate under arbitrary unitary coordinates;
- the spectral square-root realization of a centered complex Gaussian for
  every positive covariance operator `Γ`, with a proof that its covariance
  is exactly `Γ`;
- the coordinate-free Loewner-order form of (4.24), including the explicit
  substitution `v = σ² / (2 N^(D+1))` from (4.23);
- the equality-in-law bridge from the original structured coefficient sum
  (4.22) to its canonical spectral Gaussian, and hence (4.24) itself for an
  arbitrary coefficient family satisfying the covariance lower bound (4.23);
- the complex-ball volumetric estimate obtained from its real Euclidean
  counterpart, including zero-dimensional subspaces;
- the product-net construction for the two components in (4.10);
- Lemma 4.3 specialized directly to the SVD-defined space `C_{τ,σ}(E)`, with
  no separate spectral or orthogonality assumptions;
- the external tube-covering estimate (4.11), with the explicit constant
  `C = 9`, specialized directly to `C_{τ,σ}(E)`;
- the internal-center tube-covering estimate (4.12), with `2C = 18`.
- the configuration-net cardinality assembled from the anchor and the
  `N - 1` tube coordinates in (4.20);
- multiplication of the independent-column bounds (4.24), the finite-net
  union bound, and the exact pre-simplified fixed-subspace estimate (4.25);
- the Proposition 4.1 dimension gain and the `δ`, `σ`, constant, and `N`
  exponent bookkeeping used in the final displayed form of (4.25).
- the Grassmannian discretization after (4.25), using fixed-rank orthogonal
  projections, an explicit internal volumetric net, deterministic transport
  of profile error/covariance/approximate-kernel conditions, and a finite
  probability union bound;
- absorption of the anchor and Grassmannian entropy by the coarse `m_Z^6`
  exponent used in (4.19).
- the finite singular-value-chain dichotomy of Fact 4.6 and the dyadic scale
  covering and tail propagation used in Fact 4.7.
- the deterministic large-gap reduction in Proposition 4.8: low-part norm
  control, residual splitting, and passage to the doubled tube radius.
- the probability assembly in (4.31): explicit doubled-radius invocation of
  (4.25), Grassmannian transport, the prescribed `δ` exponent cancellation,
  the eventual large-`N` proof of `δ ≥ y`, the concrete absorption of the
  factored post-substitution majorant into `N⁻ᴺ = exp(-N log N)`, uniformly
  over every possibly `N`-dependent scale `x ∈ (0,1]`;
- the unified large-gap-family endpoint of Proposition 4.8, the full-rank
  majorant (4.19) and endpoint of Proposition 4.5, and their composition over
  the concrete Fact 4.7 dyadic net into the Proposition 4.9 bound `N⁻ᴺ`;
- concrete definitions of `Reg(d)`, `W(d,σ)`, and `W_gap(d,x)` inside the
  ambient relation space, together with their small-residual events and the
  induced Proposition 4.9 event classification;
- an exact infimum-event interface: strict infimum events always admit an
  approximate witness, while non-strict events are converted to existential
  events only under an explicit minimum-attainment hypothesis.
- the genuine product `ℓ²` norm formula for the dual-kernel residual, its
  triangle inequality, and the lower bound transported from a regular
  approximation;
- the page-32 recursive exponents `D₁ = 1` and
  `D_{d+1} = 2 Deg_d(D_d) + 3`, including a single large-`N` threshold that
  absorbs all square-root approximation errors simultaneously;
- the final uniform exponent and the event- and measure-level reduction of
  the unit-profile bad event on `Ω_good` to the finite union of the
  Proposition 4.9 regular-profile events;
- one common large-`N` threshold for every retained dimension and every
  page-32 absorption condition, followed by the finite-sum absorption and
  final `exp(-Ω(N))` least-singular-value conclusion of Theorem 3.3.

### Square Ginibre baseline

- complex singular values and the Courant–Fischer endpoint;
- the deterministic distance-to-span reduction;
- properness of the span of the other `n` columns;
- openness and measurability of the moving-span bad event;
- a real Gaussian density/interval small-ball estimate;
- the fixed proper complex-subspace Gaussian estimate;
- product-measure conditioning after exposing one column;
- the finite union bound over all columns;
- the final square complex Ginibre lower-tail theorem above.

There are no `sorry`, `admit`, or project-defined axioms in the proof files.
The project uses ordinary mathlib classical foundations.

## Completion status

The Section 3 and Section 4 modules needed for Theorem 1.5 are connected end
to end.  This includes Fact 3.1, the negative second-moment identity,
conditional exposed-column Gaussian estimates, the Section 4 covariance
theorem, recursive invariant-factor assembly, conversion back to the literal
matrix coordinates of the paper, and absorption of the polynomial geometric
tail into `exp (-c₁ N)`.

The paper-facing endpoint is
`GinibreLSV.Section3.theorem15`.  For every `m,n ≥ 1` it proves the proposition
`Theorem15 m n`, with exponents depending only on `m,n` and with the leading
constant and large-`N` threshold allowed to depend on the fixed coefficient
matrices.  `GinibreLSV.Audit` confirms that this endpoint contains no project
axioms; the proof files contain no `sorry` or `admit`.

The development uses the harmless non-sharp Ginibre operator-norm cutoff `32`
instead of the paper's displayed `8`.  It also retains a few deliberately
coarse intermediate polynomial powers, which are absorbed by the stated
exponent slack and do not change Theorem 1.5.

## Layout

- `GinibreLSV/Deterministic.lean`: singular-value and distance-to-span geometry.
- `GinibreLSV/GaussianSmallBall.lean`: density and fixed-subspace estimates.
- `GinibreLSV/Conditioning.lean`: Tonelli/Fubini product-measure bounds.
- `GinibreLSV/Probability.lean`: distribution-free union-bound theorem.
- `GinibreLSV/Ginibre.lean`: complex Ginibre model and the final theorem.
- `GinibreLSV/Section3/Algebra.lean`: generated coefficient algebra,
  irreducibility, composition filtrations, simple quotients, and induced
  diagonal actions from Section 3.1.
- `GinibreLSV/Section3/Burnside.lean`: complex Schur lemma and the
  finite-dimensional Burnside theorem used in Proposition 3.2.
- `GinibreLSV/Section3/Proposition32.lean`: Hilbert--Schmidt coefficient and
  relation spaces, adjoint Burnside, left-ideal exclusion, and Proposition
  3.2 with its dimension surplus.
- `GinibreLSV/Section4/RobustBurnside.lean`: compact projection parameter
  space and the uniform robust Burnside/leakage estimate (4.8).
- `GinibreLSV/Section4/SubspaceGeometry.lean`: Lemma 4.2, the dimension
  comparison in Proposition 4.1, and the decomposition (4.10) in Lemma 4.3.
- `GinibreLSV/Section4/Covariance.lean`: covariance positivity, compression,
  and Loewner lower-bound propagation (4.17).
- `GinibreLSV/Section4/MatrixCovariance.lean`: the Hilbert--Schmidt matrix
  model, equations (4.15)--(4.16), left-multiplication adjoints, and the
  concrete product-matrix covariance identity.
- `GinibreLSV/Section4/ComplexGaussianCovariance.lean`: normalized standard
  complex Gaussian coefficients, covariance and pseudo-covariance identities,
  real Gaussian pushforward laws, uniqueness from complex covariance, and the
  product-matrix specialization after (4.16).
- `GinibreLSV/Section4/GaussianAntiConcentration.lean`: real product-Gaussian
  coordinate boxes, shifted and scaled complex small-ball estimates, and the
  isotropic, diagonal, unitary, and arbitrary positive-covariance spectral
  forms of (4.24), including the scale inherited from (4.23) and the
  equality-in-law transfer to arbitrary structured coefficient sums.
- `GinibreLSV/Section4/ActiveCovariance.lean`: the synthesis/analysis adjoint
  identity, the active-space Gram lower bound, and the abstract propagated
  covariance estimate underlying (4.23).
- `GinibreLSV/Section4/ActiveExtraction.lean`: the smallest covariance
  eigenvector removal, codimension-one retained space, and trace-error
  estimate (4.14).
- `GinibreLSV/Section4/ProfileRegularization.lean`: the orthogonal extraction
  iteration, accumulated error (4.32), dimension bookkeeping, and conditional
  regularity endpoint of Lemma 4.10.
- `GinibreLSV/Section4/ExtractionStopping.lean`: the trace-based forced
  stopping argument and concrete spectral construction of all successive
  covariance-eigenvector removals.
- `GinibreLSV/Section4/Lemma410.lean`: the terminal Rayleigh lower bound,
  covariance-compression bridge, and end-to-end deterministic Lemma 4.10
  regular-profile theorem.
- `GinibreLSV/Section4/Proposition41.lean`: SVD spectral spaces, synthesis and
  quotient maps, complementary-space spectral and image-orthogonality
  theorems, the active/inactive leakage bound, and Proposition 4.1.
- `GinibreLSV/Section4/TubeCovering.lean`: complex volumetric ball nets,
  the SVD-specialized Lemma 4.3 decomposition, product tube nets, and the
  covering estimates (4.11)--(4.12).
- `GinibreLSV/Section4/NetUnionBound.lean`: the product configuration net,
  independent-column small-ball product, finite union bound, and the
  fixed-subspace probability estimate and exponent reductions in (4.25).
- `GinibreLSV/Section4/GrassmannianNet.lean`: explicit internal projection
  nets, profile/covariance/kernel stability, and the simultaneous-subspace
  finite-union step following (4.25).
- `GinibreLSV/Section4/SingularValueGaps.lean`: the gap dichotomy of Fact 4.6
  and the finite dyadic discretization underlying Fact 4.7.
- `GinibreLSV/Section4/Proposition48Reduction.lean`: the deterministic
  low/high singular-part and tube reduction surrounding (4.28)--(4.30).
- `GinibreLSV/Section4/Equation431.lean`: the doubled-radius use of (4.25),
  Grassmannian probability assembly (4.31), exponent identities, the
  `N⁻ᴺ = exp(-N log N)` absorption, and the final finite dyadic union
  architecture of Proposition 4.9.
- `GinibreLSV/Section4/Proposition48.lean`: the real prescribed residual
  scale, the uniform eventual `(4.30)` comparison `y ≤ δ`, and the
  simultaneous dyadic-family probability endpoint of Proposition 4.8.
- `GinibreLSV/Section4/Proposition45.lean`: the full-rank majorant (4.19),
  its comparison with (4.31), and the uniform full-rank event endpoint of
  Proposition 4.5.
- `GinibreLSV/Section4/Proposition49.lean`: absorption of the full-rank and
  dyadic case multiplicity using the spare probability exponent, composition
  of the Proposition 4.5 and 4.8 endpoints, and specialization to the concrete
  dyadic net from Fact 4.7.
- `GinibreLSV/Section4/ProfileEvents.lean`: Definition 4.4's ambient-space
  regularity class, the concrete `W(d,σ)` and `W_gap(d,x)` spectral classes,
  infimum/existential event bridges, and the regular-profile Proposition 4.9
  endpoint.
- `GinibreLSV/Section4/DualKernelOperator.lean`: the structured dual kernel
  map `D_a` from (3.7)/(4.18), its ambient relation-space restriction, exact
  coordinate residual, Proposition 4.5/4.8 full-rank and gap events, and the
  concrete regular-profile event classification and Proposition 4.9
  `N⁻ᴺ` probability endpoint.
- `GinibreLSV/Section4/RegularityCompactness.lean`: compactness of the regular
  profile class over each fixed span `E`, its exact identification with
  `Reg(finrank E)` constrained by `Span(B)=E`, and minimum attainment for the
  paper's non-strict dual-kernel infimum event.
- `GinibreLSV/Section4/VaryingRegularityCompactness.lean`: compactness of the
  fixed-rank Grassmannian incidence space, exact recovery of the whole
  varying-span `Reg(d)` as its profile projection, and global minimum
  attainment for the paper's non-strict infimum event.
- `GinibreLSV/Section4/MatrixDualKernel.lean`: the exact Hilbert--Schmidt
  matrix realization of `Σ_R`, `D_R`, `D_R^N`, and `D_a`, including the
  coordinate action by left multiplication with `R_ℓᴴ`, concrete
  full-rank/gap events, and the matrix-level Proposition 4.9 endpoint.
- `GinibreLSV/Section4/GoodOperatorNorm.lean`: the good event (4.5) using
  Euclidean matrix operator norms and the non-sharp absolute cutoff `32`,
  automatic uniform control of `Ψ_E`,
  measurability, the finite union bound for its complement, and the bridge
  from the paper's unnormalized restricted probability `P_{Ω_good}` to full
  probability, including Proposition 4.9 directly in the restricted notation
  and the exact matrix coefficient action `B ↦ R_ℓᴴ B`.
- `GinibreLSV/Section4/GinibreOperatorNorm.lean`: scalar extension from real
  to complex matrices without operator-norm loss, reduction to two real
  matrix tails, standard Gaussian product-space independence and subgaussian
  instances, and the fixed-`N` normalized complex Ginibre operator-norm tail.
- `GinibreLSV/Section4/KernelPerturbation.lean`: explicit norm estimates
  converting Lemma 4.10's squared profile distance into a dual-kernel
  residual perturbation on `Ω_good`.
- `GinibreLSV/Section4/Theorem33Assembly.lean`: the recursive regularity
  exponents from page 32, uniform absorption of the approximation error
  (also with one extra factor of `N`), the final global exponent, and the
  event/measure-level assembly of Lemma 4.10 with the Proposition 4.9
  regular-profile events.
- `GinibreLSV/Section4/AmbientLemma410.lean`: transport of profile energy,
  squared distance, span dimension, and covariance regularity through a
  subspace embedding, yielding Lemma 4.10 and the page-32 reduction directly
  inside an arbitrary ambient relation space such as `D_R`.
- `GinibreLSV/Section4/LeastSingularBridge.lean`: the exact Hilbert direct-sum
  unit sphere, its compactness and nonemptiness for `D_R ≠ 0`, the variational
  least singular value of `D_a`, equality of its non-strict bad event with the
  unit-profile residual event, and the final restricted/unrestricted measure
  bridges to Proposition 4.9 and the operator-norm tails, including a concrete
  fixed-`N` matrix theorem for `D_a : D_R^N → End(Z)^(N-1)`, a unified
  large-`N` threshold, and the final `exp(-Ω(N))` probability endpoint.
- `GinibreLSV/Audit.lean`: `#print axioms` checks for the key endpoints.
- `PAPER_REVISIONS.md`: small optional technical clarifications suggested by
  the Lean formalization; no major revision has been identified.

## Build

The project targets Lean `v4.32.0` and depends on mathlib plus
`YuanheZ/lean-stat-learning-theory` at its matching `v4.32.0` tag.

```bash
lake update
lake build
lake build GinibreLSV.Audit
```
