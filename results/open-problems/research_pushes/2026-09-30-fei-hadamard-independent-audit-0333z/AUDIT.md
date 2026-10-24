# Independent audit: Hadamard sign-rounding control-influence obstruction

Audit date: 2026-09-30 UTC. Classical FEI remains OPEN.

## Verdict and pinned scope

The analytic conclusions in Theorems 2.1–2.3 and Section 3 of the [audited report](https://github.com/yspennstate/math-open-problems/blob/c4d07e6e2280aa54c767512540d143f930154d3c/research_pushes/2026-09-30-fei-hadamard-rounding-0330z/REPORT.md) are sound under the independent, uniform, disjoint-input hypotheses. This is an independent mathematical review with finite cross-checks, not a formal proof certification, novelty certificate, or proof of full classical FEI.

One concrete defect was found in the pinned verification output: ordinary float conversion of narrow rational intervals does not preserve enclosure. It affects the displayed JSON interval endpoints, not the exact rational acceptance checks or analytic theorems. The author and coordinating researcher were notified; the final repair at `67c4459ae0e8ae85a228c7a5c2629f003910139b` was independently rerun and verified under both binary64 and exact-decimal interpretations (Section 8). This audit preserves the original source files unchanged and reports the pinned defect even if a later commit fixes it.

Audited source commit: `c4d07e6e2280aa54c767512540d143f930154d3c` in `yspennstate/math-open-problems`.

## 1. Hypotheses and influence convention

Use the uniform sign cube and disagreement influence `Inf_j f = Pr[f(Y) != f(Y with coordinate j flipped)]`. The required hypotheses are:

- `L` is a positive integer admitting a real orthogonal matrix `R` with all entries of magnitude `1/sqrt(L)`
- `W` has Euclidean norm one almost surely and is independent of the independent uniform sign vector `xi`
- The control signs `Y` are independent uniform signs, independent of all coefficient data
- The threshold uses one fixed tie convention, here `sign(0)=+1`
- The physical control realization uses disjoint parity blocks of positive integer length `r`, independent of the data
- For the explicit multilayer application, `L` is a power of two and `k` is a positive integer; data layers have mutually disjoint coordinates

The proof is conditional on every fixed `W`, so no distributional assumption on earlier layers beyond independence of the final random sign layer is needed. Independence cannot be dropped: choosing `W(xi)=Diag(xi) R^T e_1` makes `v=e_1` always, hence total control influence one, contradicting the growing bound for large `L`. Flatness also matters; an arbitrary orthogonal matrix such as the identity need not flatten a sparse vector.

The edge case `L=1` is valid for the abstract theorems. The spectral count in Section 3 presupposes positive-length control blocks; empty parity blocks would not yield distinct indexed monomials. The asymptotic example has `d>=2`, hence `k>=1`.

## 2. Threshold identity, ties, and the constant

Fix a real unit vector `v` and write `Z=sum_j v_j Y_j`, `f=sign(Z)`. Conditional on all coordinates except `j`, the two endpoint values have difference in `{0,2}` if `v_j>0`, and in `{0,-2}` if `v_j<0`. Thus

`E[Y_j f] = sign(v_j) Inf_j f`.

If `v_j=0`, both the correlation and influence are zero. A constant tie choice preserves these monotonicity statements even when one endpoint is exactly zero. Also `fZ=|Z|` at all inputs, including ties. Therefore

`sum_j |v_j| Inf_j f = E|Z|`.

The moments are `E Z^2=1` and `E Z^4=3-2 sum_j v_j^4<=3`. Hölder with exponents `3/2` and `3`, applied to `|Z|^(2/3)|Z|^(4/3)`, gives

`1 <= (E|Z|)^(2/3) (E Z^4)^(1/3)`.

Consequently `E|Z|>=1/sqrt(3)`, and hence

`sum_j Inf_j f >= 1/(sqrt(3) ||v||_infinity)`.

Now condition on arbitrary fixed `W`. For each coordinate of `v=R Diag(xi)W`, the moment-generating function is bounded by

`product_a cosh(t R_ja W_a) <= exp(t^2 sum_a R_ja^2 W_a^2/2) = exp(t^2/(2L))`.

Chernoff and the union bound yield

`Pr[||v||_infinity > u | W] <= 2L exp(-L u^2/2)`.

At `u=sqrt(2 ln(4L)/L)`, the right side is `1/2`. On the complementary event, the pointwise influence lower bound is at least `sqrt(L/ln(4L))/sqrt(6)`. Multiplying by probability at least `1/2` proves the exact reported constant:

`E_(W,xi) sum_j Inf_j f >= (1/(2 sqrt(6))) sqrt(L/ln(4L))`.

No independence between different coordinates of `v` is used. Averaging over `W` loses no additional constant. Every physical bit in parity block `j` flips exactly `Y_j` and leaves the other controls and data unchanged, so the physical control influence is exactly `r` times this expectation. Additional data-coordinate influence is nonnegative.

The same identity holds for the constant convention `sign(0)=-1`; the report needs only its stated `+1` convention. Arbitrary input-dependent tie assignments are outside this argument.

## 3. One-hot criterion and exact conditional probability

The square of the unit-norm linear form is

`(sum_j v_j Y_j)^2 = 1 + 2 sum_(j<ell) v_j v_ell Y_j Y_ell`.

The degree-two control characters are distinct and linearly independent. Pointwise Booleanity is therefore equivalent to every pairwise product vanishing. Unit norm leaves exactly one nonzero coordinate, equal to `+1` or `-1`.

For fixed `W`, the equation `R Diag(xi)W=+/- e_j` is equivalent to `Diag(xi)W=+/-R^T e_j`. Every target coordinate has magnitude `1/sqrt(L)`, so `W` must have all those magnitudes. If it does, all its coordinates are nonzero, and each of the `2L` distinct signed columns of `R^T` gives exactly one sign assignment. Orthogonality ensures these targets are distinct. Thus the conditional probability is exactly `2L/2^L` for flat-magnitude `W`, and zero otherwise, including the valid `L=1,2` edge cases.

This is a full pointwise-Booleanity calculation, not a replacement of Booleanity by a second-moment identity.

## 4. Fixed-W scalar conditional-mean lift

For `G(xi,Y)=sum_j (R Diag(xi)W)_j Y_j`, maximizing over `Y` gives `max_Y |G|=||v||_1`, so the supremum is over both `xi` and `Y`. The upper bound is `sqrt(L)` by unit norm and Cauchy–Schwarz.

For each row, `E_xi v_j^2=1/L` and `E_xi v_j^4<=3/L^2`. The same Hölder calculation gives `E_xi |v_j|>=1/sqrt(3L)`. Summing and taking a maximum gives `||G||_infinity>=sqrt(L/3)`.

Every conditional expectation of a `+/-1` variable lies in `[-1,1]`. Hence an exact representation `E_A B(xi,Y,A)=lambda G(xi,Y)` at every input necessarily satisfies `|lambda| ||G||_infinity<=1`, proving `|lambda|<=sqrt(3/L)`. This is a necessary scalar-amplitude restriction only. It provides no universal lower bound on auxiliary-variable influence and does not exclude different representations.

## 5. Multilayer support and asymptotic comparison

Each multiplication by the unnormalized Hadamard matrix multiplies squared Euclidean norm by `L`; sign diagonals preserve it. Starting with the all-ones vector of squared norm `L`, the `k`-layer numerator has squared norm `L^(k+1)` at every data input. The reported normalization is correct.

The explicit earlier-layer vector is

`W=L^(-k/2) H Diag(x^(2)) ... H Diag(x^(k)) 1`,

with the product empty when `k=1`. It has unit norm and is independent of `xi=x^(1)`. Thus the abstract theorem applies for every number of earlier layers, without a limiting or mixing assumption.

In the unrounded real polynomial, each tuple `(j,a_1,...,a_k)` selects a distinct nonempty control block and one variable from each disjoint data layer. There can be no collisions or cancellations between these monomials. There are `L^(k+1)` coefficients, each of magnitude `L^(-(k+1)/2)`, all at degree `r+k`. Parseval therefore gives norm one, spectral entropy `(k+1) log_2 L`, and real Dirichlet energy `r+k`.

For `r=ceil(d/2)`, `k=floor(d/2)`, and largest power of two `L<3^r`, we have `3^r/2<=L<3^r` and `ln(4L)<=r ln(12)` for `r>=1`. The reported lower bound therefore implies the explicit sufficient inequality

`I(F) >= [1/(4 sqrt(6 ln(12)))] sqrt(d) 3^(d/4)` for every `d>=2`.

This verifies the claimed exponential comparison, while the unrounded entropy is `Theta(d^2)` and its real energy is `d`. The phrase “whose influence is much larger” in the report should be understood in this asymptotic degree split, not for every tiny configuration: for example `L=2,k=3,r=1`, the unrounded function is already Boolean and both total energies are four.

[Slote, Section 4](https://arxiv.org/html/2608.01424#S4) uses an anticommuting Pauli core and commuting Hadamard-generated suffixes. Anticommutation cancels cross terms when squaring the quantum operator. The report accurately retains the suffix formula while analyzing a different, explicitly classical independent-parity control realization. This audit verifies that particular replacement; it gives no obstruction to all possible classicalizations and no rounded-family entropy bound.

## 6. Reproduction and independently executed checks

The remote pinned `verify.py` SHA-256 is `be681c36a14690e9f68cae925519923a2ec6ed4aff62764c2a88f9c243c0836a`. Replaying it in an isolated directory reproduced the pinned `verification.json` byte for byte; its SHA-256 is `c423310cbf9973066bdcd813f569a5606b83e1a7f419150b7dc9f0aec8cf2c3c`. All ten author configurations passed.

The separate `independent_check.py` executes 110 fixed coefficient-vector cases, covering `L=1,2,4,8`, sparse, flat, unequal, signed, and zero-containing vectors. It exhausts `217736` pairs `(xi,Y)` for each of two constant tie conventions. It verifies integer norm and fourth-moment identities, exact rational correlation/influence identities, the pointwise influence lower bound, conditional one-hot counts, the averaged lower bound, and both fixed-W supremum estimates. These finite checks supplement the all-dimension analytic proof above; they do not establish it by extrapolation.

`independent_results.json` stores exact rational witnesses for the pinned display defect. Reproduce from this audit directory with `python independent_check.py`; `source/verify.py` is the unchanged pinned checker copy.

## 7. Pinned interval-serialization defect

The source function `encl(bounds)` returns `[float(lower),float(upper)]`. The rational endpoints are much closer together than one binary64 spacing, so both can round to the same float outside the true enclosure:

- At `L=2`, both saved endpoints `0.04007486224691565` exceed the exact rational upper endpoint of the squared analytic lower-bound interval
- At `L=4`, both saved endpoints `0.06011229337037347` fall below the exact rational lower endpoint
- At `L=8`, both saved endpoints `0.09617966939259756` exceed the exact rational upper endpoint

These are exact comparisons using `Fraction.from_float`, not a high-precision numerical guess. The rational log-series construction and the internal inequality `24 I_control^2 ln_lower(4L)>=r^2 L` are sound. The defect is the final presentation as a certified interval.

A suitable repair is to store numerator/denominator endpoint pairs, or verify the direction of each float conversion with exact fractions and move outward using `math.nextafter` when necessary. Regenerate the output and its script hash after repair. The issue does not change the theorem, but rounded display pairs must not be described as rigorous enclosures before correction.

## 8. Final repair verification

The intermediate repair `ada352231ccb4f37bf8faa54112a07e2213bd399` correctly enclosed values when JSON numbers were parsed as binary64, but 7 of 20 Hadamard interval pairs still failed as exact decimal literals. For example, the literal upper endpoint `0.04007486224691565` is below the exact rational lower bound for `L=2`, despite its binary64 value being above the exact value. This remaining representation issue was reported immediately.

The final [repair commit](https://github.com/yspennstate/math-open-problems/commit/67c4459ae0e8ae85a228c7a5c2629f003910139b) checks both `Fraction.from_float(endpoint)` and `Fraction(str(endpoint))`, stepping outward until both meanings enclose the rational interval. Its regression cases include exact binary representations of `0.1` and midpoint values between binary and decimal meanings.

The final Hadamard checker was fetched from that immutable commit and rerun in isolation. The generated output matched the committed output byte for byte. The independent checker also intercepted all 20 emitted interval pairs and verified exact containment under both meanings. All passed; the regenerated configuration results matched the final output exactly.

- Final checker SHA-256: `0ed03f4178cdc5d5e3d483fa292c4d3a62c8e6367884b8b78a1e7a9e816d5fe1`
- Final output SHA-256: `291f188b7b4c0779d473f8fe7f9463425890dd11a432f7b88af23c983971d668`
- Final source copies are in `final/`; original pinned copies are in `source/`

The Hadamard export issue is resolved at the final commit. This audit does not independently rerun the two other packages modified by that repair; their verification belongs to their respective audits. No analytic result changed.

## Boundary

No novelty search, formal verification, complete proof of classical FEI, or universal classicalization obstruction is claimed. No author files, public repositories, repository visibility, or merge state were changed by this audit.
