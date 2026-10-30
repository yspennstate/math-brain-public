# QFORM fleet02/B01 — local-L2 oscillatory replacement and a source-valid ambiguity obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control revision: `2026-09-22.5`  
Run: `20260922T130024Z-fleet02-B01-qform-r20`  
Assignment: `Oscillatory replacement`  
Status: `ESSENTIAL_STEP_APPLIED / CANDIDATE_MECHANISM_REFUTED / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source state

The target remains: for arbitrary independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite bound for the density of `Q=X^TAX`, or give a valid counterexample. No moments, log-concavity, compact support, connected support, diagonal-basis independence, or post-rotation independence are assumed.

The law-uniform pointwise Fresnel decay claim is still refuted by phase-aligned densities, so this report does not use it. The current correction inbox was reread before publication, including `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, `QFORM-TWOSHEET-XRAY-ONLY-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, and `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`.

The completed named-partner result actually applied is fleet03/B01 run `fleet03-B01-20260922T123142Z-qform-r11`, canonical report

`yspennstate/math-open-problems@d54e3a5d40a1d9837d39a1e525781fcf44ec0d9d:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260922T123142Z-qform-r11/REPORT.md`.

Its primary source theorem was also read at

`yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb:proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`.

## 2. New theorem: translation-uniform local L2 energy for one quadratic gate

Let `f` be any probability density on the real line with `0<=f<=1`, let `a!=0`, `b` be real, and define

`F(t)=int_R exp(i t (a x^2+b x)) f(x) dx`.

For every bounded frequency interval `I` of length `L`, put `s=|a|L`. Then

- if `s<1`, `int_I |F(t)|^2 dt <= L`;
- if `s>=1`,

`int_I |F(t)|^2 dt <= |a|^(-1) [8+4*pi*(1+log s)]`.        (2.1)

Consequently, for every `eta>0`,

`Leb{t in I: |F(t)|>eta}`

`<= eta^(-2) min{L, |a|^(-1)[8+4*pi*(1+log_+(|a|L))]}`.    (2.2)

This is a genuinely distributional/averaged replacement for the false pointwise estimate. It is uniform in the location of `I`, in `b`, and in the arbitrary bounded density `f`.

### Proof

Complete the square. After translating `X`, removing a harmless constant phase and reflecting the output when `a<0`, it is enough to consider `Y=|a|X^2`. Its density `g` on `(0,infinity)` obeys

`0<=g(y)<=C y^(-1/2)`, where `C=|a|^(-1/2)`, and `int g=1`.      (2.3)

Let `I` have centre `tau`. Multiplication of `g(y)` by `exp(i tau y)` merely shifts its Fourier transform, so it is enough to estimate an interval of the same length centred at zero for an amplitude `h` satisfying `|h|=g`.

Assume `s=|a|L>=1` and set `epsilon=1/L`, `M=|a|`. Split `h=h_0+h_1` with `h_0=h 1_(0,epsilon)`.

From (2.3),

`||h_0||_1 <= 2C sqrt(epsilon)`,

hence on any interval of length `L`,

`||hat h_0||_2^2 <= L ||h_0||_1^2 <= 4 C^2`.               (2.4)

For `h_1`,

`int_epsilon^M |h_1(y)|^2 dy <= C^2 int_epsilon^M dy/y = C^2 log(|a|L)`,

while on `y>M`, (2.3) gives `g(y)<=C M^(-1/2)=C^2`, and therefore

`int_M^infinity |h_1(y)|^2 dy <= C^2 int_M^infinity g(y)dy <= C^2`.    (2.5)

Thus `||h_1||_2^2<=C^2(1+log s)`. With the convention `hat h(t)=int exp(i t y)h(y)dy`, Plancherel gives

`||hat h_1||_2^2 <= 2*pi*C^2(1+log s)`.                    (2.6)

Finally `|u+v|^2<=2|u|^2+2|v|^2`, (2.4), and (2.6) yield exactly (2.1). If `s<1`, `|F|<=1` gives the first bound. Chebyshev gives (2.2). QED.

### Sharp order of the logarithm

For the admissible density `f=1_[0,1]`, `a=1`, `b=0`,

`F(t)=t^(-1/2) int_0^(sqrt(t)) exp(i u^2) du` for `t>0`.

The Fresnel integral tends to `exp(i*pi/4)*sqrt(pi)/2`, hence

`|F(t)|^2 ~ pi/(4t)` and `int_1^T |F(t)|^2 dt ~ (pi/4) log T`.

Therefore the logarithmic growth in a translation-uniform long-interval `L2` estimate cannot in general be replaced by an absolute constant.

## 3. Direct application of the named-partner result

The partner theorem gives, for a rank-two diffuse component `R` with leverage at most `1/2`, determinant scale `Delta`, and `B(U)` as in that theorem,

`int_R |phi_R(t)|^(3/2) dt <= 6*pi*B(U)*Delta^(-1/2)`.       (3.1)

The preceding fleet02/B01 run proved for an independent physical square `S=dZ^2+aZ+b`, with `d!=0`,

`int_R |phi_S(t)|^3 dt <= 16*pi/|d|`.                       (3.2)

If the product structure genuinely makes `R` and `S` independent, then Holder applied to `phi_{R+S}=phi_R phi_S` gives

`||phi_{R+S}||_1 <= (6*pi*B(U))^(2/3) (16*pi)^(1/3) (Delta |d|)^(-1/3)`.

Fourier inversion therefore gives

`||p_{R+S}||_infinity <= [576^(1/3)/2] B(U)^(2/3) (Delta |d|)^(-1/3)`

`<= 8.103 (Delta |d|)^(-1/3)`, since `B(U)<=e`.              (3.3)

This reproduces the partner's rank-two-plus-independent-square smoothing entirely on the frequency side and confirms that the averaged exponents fit exactly. The unresolved issue is not exponent arithmetic; it is how to retain enough product structure when the third large spectral direction is not a disjoint physical square.

## 4. New source-valid falsifier: absolute ambiguity-factor aggregation loses a logarithm even for a diagonal form

A natural response to the correction `QFORM-UV-CONDITIONAL-CAP-FALSE` is to square the characteristic function, keep the original-coordinate joint density, and apply Hausdorff--Young/Hölder to the resulting ambiguity factors. The following admissible family shows that the most direct absolute-value implementation cannot produce a universal constant.

For `R>e`, let

`f_R(x)=1_[1,R](x)/(x log R)`.

This is a probability density and `f_R<=1`. Let `rho_R` be the density of `X-X'` for iid `X,X'~f_R`. For `0<u<R-1`, direct integration gives the exact identity

`rho_R(u)=[log(1+u)+log(1-u/R)]/[u (log R)^2]`.             (4.1)

For `4<=u<=R/2`,

`rho_R(u) >= [log u]/[2u (log R)^2]`.                       (4.2)

For one coordinate define the ambiguity factor

`H_u(s)=int exp(i s v) f_R(v+u/2) f_R(v-u/2) dv`.

Its amplitude is bounded by one and has `L1` mass `rho_R(u)`. Hausdorff--Young therefore yields, in particular,

`||H_u||_3 <= (2*pi)^(1/3) rho_R(u)^(2/3)`.                (4.3)

For the completely harmless diagonal three-variable form

`Q=X_1^2+X_2^2+X_3^2`,

with iid `f_R`, the exact squaring identity is

`|phi_Q(t)|^2 = int_(R^3) product_{j=1}^3 H_{u_j}(2 t u_j) du_1 du_2 du_3`.  (4.4)

If one now takes absolute values, integrates in `t`, and applies three-factor Holder with exponent `3`, the resulting majorant is a constant multiple of

`J_R^3`, where `J_R=int_R rho_R(u)^(2/3) |u|^(-1/3) du`.    (4.5)

But (4.2) gives the explicit lower bound

`J_R >= 2^(-2/3) (log R)^(-4/3) * (3/5)`

`       * [(log(R/2))^(5/3)-(log 4)^(5/3)]`,               (4.6)

so `J_R` grows like a positive constant times `(log R)^(1/3)`, and the factorized absolute majorant grows like `log R`.

This does **not** say the actual diagonal form has a large density: the diagonal theorem still gives a universal bounded density. It says the proposed proof step loses a logarithm before it can see the cancellation that the true diagonal convolution has. Thus a coupled proof based on squaring may not simply take absolute values in the displacement variables and apply coordinatewise Hausdorff--Young/Hölder; it must preserve additional oscillatory cancellation or exploit a stronger product-structure identity.

The same calculation extends to any finite Holder triple `q_j>=2` with `sum 1/q_j=1`: the corresponding one-coordinate majorant scales at least as `(log R)^(1/q_j)`, so their product still carries a logarithmic loss. The symmetric `q_j=3` case above is already a complete source-valid falsifier of the natural equal-exponent implementation.

## 5. Conditional end-to-end route and first unpaid implication

A corrected Fourier route would be complete if one could do the following uniformly under the three-large-eigenvalue hypothesis:

1. extract either the partner's rank-two averaged factor plus a genuinely product-preserving third gate, or a coupled substitute with the same `L^(3/2) * L^3 -> L^1` exponent balance;
2. when using the exact squaring/ambiguity representation, retain cancellation in the displacement integration strongly enough to avoid the logarithmic loss demonstrated by (4.1)--(4.6);
3. sum the resulting frequency estimate dimension-freely and invert.

This run pays a real part of step 2 by identifying the sharp local `L2` replacement (2.1)--(2.2) and, equally importantly, shows that the naive absolute ambiguity aggregation cannot be the missing universal implication.

The first essential remaining implication is now:

**COUPLED-CANCELLATION / PRODUCT-PRESERVING-THIRD-GATE.** Prove a dimension-free estimate that couples the partner rank-two averaged theorem to a third spectral direction without post-rotation independence and without taking absolute values early enough to incur the logarithmic `f_R` loss above; or construct a genuine target counterexample.

No such implication is assumed here. The full conjecture remains OPEN and this report is not a full-proof candidate.

## 6. Provenance and integrity

Fresh owner controls were read from `yspennstate/math-research-brain` at revision `2026-09-22.5`; the pre-publication correction inbox included the five events listed in section 1. The current check-in request `QFORM-CHECKIN-20260922T120815Z` is acknowledged separately in the brain repository.

No numerical computation is used as a proof step in this report. All displayed identities and inequalities are analytic. A scoped manual privacy/secret review of this report's changed path found no credential, scheduler identifier, machine path, unrelated private data, benchmark material, email content, public-release action, paid API/model use, or workflow dispatch. Repository access here is file retrieval/transport, not authenticated native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
