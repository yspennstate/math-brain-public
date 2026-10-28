# account01/B15 — exact product-source graph-trace formula and correction of the scalar conditional-height gate

**Run:** `20260922T190339Z-account01-B15-QFORM-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Observed owner control:** revision `2026-09-22.12`  
**Assignment:** Absolute continuity and regularity  
**Classification:** `ESSENTIAL_STEP_APPLIED / SOURCE_VALID_TRACE_REDUCTION`  
**Full target:** `OPEN_NOT_PROVED`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and corrections consumed

The target remains: for arbitrary independent real coordinates `X_i` having probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove

`P(X^T A X in I) <= C |I|`

for a single finite universal `C`, or give a genuine counterexample. Continuity of a representative is a separate stronger conclusion.

This run uses the live corrections that override older candidate language:

1. the arbitrary-joint three-dimensional coarea assertion
   `||p_(Y^T Lambda Y)||_infinity <= K ||rho_Y||_infinity^(2/3)` is false for general dependent `Y`;
2. conditioning on the whole spectral complement and paying a positive conditional-density moment is false;
3. account02/B15 r5 refutes the worst scalar-level gate `sup_b ||p_(Q3|Q'=b)||_infinity < infinity` on a genuine target;
4. account02/B15 r6 further refutes the proposed scalar-weighted repair
   `E ||rho_(123|Q')||_infinity^(2/3) <= C` on a fixed genuine target.

Accordingly, the previous account01/B15 r12 implication

`||p_Q||_infinity <= K int p_V(v)^(1/3) ||G(.,v)||_infinity^(2/3) dv`

is **withdrawn as unsupported**: its last step used the now-refuted arbitrary-joint coarea theorem after scalar conditioning had introduced dependence. The joint-density construction and exact mixture identities from r12 survive and are sharpened below.

## 2. Partner result actually applied

The named partner result used in the derivation is account02/B15 r6:

- canonical mathematics `yspennstate/math-open-problems@d00907b4362875219cc3525ceb04f90186b8c065`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T185309Z-account02-B15-qform-r6/REPORT.md`.

It gives a fixed algebraically generic target matrix and cap-one product inputs for which the scalar-conditioned positive moment diverges while the actual QFORM output remains bounded by a fixed-matrix certificate. This forces any surviving scalar-conditioning proof to retain the *translation of the conditional profile* before taking a supremum.

I also use the completed account02/B15 fixed-matrix theorem:

- `yspennstate/math-open-problems@60e7f51716e67553ce759519f9801ff3674dcce9`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T120155Z-account02-B15-qform-r1/REPORT.md`.

It proves: every nonzero quadratic form of an absolutely continuous input vector is absolutely continuous; and every fixed symmetric matrix of rank at least three has an essentially bounded output density, with a matrix-dependent principal-pivot certificate. Thus the remaining central problem is the **universal** constant; qualitative absolute continuity is already settled.

## 3. Protected-rank-three plus residual decomposition

Choose any three orthonormal eigenvectors `u_1,u_2,u_3` of `A` whose eigenvalues satisfy `|lambda_j|>=1`. Put

`U=[u_1 u_2 u_3]`, `Lambda=diag(lambda_1,lambda_2,lambda_3)`,

`B=U Lambda U^T`, `C=A-B`.

Because the selected columns are genuine eigenvectors of `A`,

`CU=0`, `U^T C=0`, `BC=CB=0`.

Define

`Y=U^T X in R^3`, `V=X^T C X`, `q(y)=y^T Lambda y`.

Then exactly

`Q=X^TAX=q(Y)+V`.

No independence between `Y` and `V` is asserted or used.

If `C=0`, this is the exact-rank-three problem and no scalar residual exists. The remainder of this report concerns the genuinely residual branch `C!=0`.

## 4. Exact joint density of `(Y,V)` with the source Jacobian retained

### Theorem 4.1 — source-valid four-dimensional pushforward

Assume `C!=0`. The random vector `(Y,V)=(U^T X,X^T C X)` has a joint density `G(y,v)` on `R^3 x R`. More precisely, writing

`F_X(x)=prod_i f_i(x_i)`,

one may take, for almost every `(y,v)`,

`G(y,v) = (1/2) int_{U^T x=y, x^T Cx=v} F_X(x)/|Cx| dH^{n-4}(x)`.

### Proof

Consider

`Phi:R^n -> R^4`, `Phi(x)=(U^T x,x^T Cx)`.

Its derivative has first three rows `u_j^T` and last row `2(Cx)^T`. Because `U^T C=0`, `Cx` is orthogonal to `range(U)`. Hence

`D Phi(x) D Phi(x)^T = diag(1,1,1,4|Cx|^2)`

and the four-dimensional normal Jacobian is exactly

`J_4 Phi(x)=2|Cx|`.

Since `C!=0`, `ker C` is a proper linear subspace and therefore has Lebesgue measure zero. Thus `Phi` has rank four almost everywhere. The coarea formula applied to the absolutely continuous source measure `F_X(x)dx` gives the displayed joint density. QED.

This identity is the key provenance statement: the scalar residual weight and the original-coordinate product density remain *inside the same curved fiber integral*. Nothing is replaced by an arbitrary dependent three-dimensional density.

## 5. Exact curved-graph trace formula

### Theorem 5.1 — translation-aware scalar-residual identity

For almost every `t`,

`p_Q(t) = int_{R^3} G(y,t-q(y)) dy`.

Equivalently, if `H(s,v)` denotes the joint density of `(S,V)` with `S=q(Y)`, then

`p_Q(t)=int_R H(t-v,v) dv`.

### Proof

For every bounded compactly supported test function `psi`,

`E psi(Q)`
`= int_{R^3} int_R psi(q(y)+v) G(y,v) dv dy`.

Set `t=q(y)+v`. For each fixed `y`, this is a unit-Jacobian translation in `v`; hence

`E psi(Q)`
`= int_R psi(t) [ int_{R^3} G(y,t-q(y)) dy ] dt`.

Since the partner theorem already supplies absolute continuity of `Q`, the bracketed function is a version of `p_Q`. QED.

Where a regular conditional density exists, the same formula reads

`p_Q(t)=int p_V(v) p_(S|V=v)(t-v) dv`.

The essential point is that the shift `t-v` remains inside the integral. Moving `sup_t` inside the scalar mixture is a lossy operation and, by the partner constructions, can be catastrophically lossy.

## 6. Application to the partner's fragmented counterexample

Account02/B15 r6 uses a fixed Hadamard-diagonalized target with spectrum `{1,2,-3,1/2}` and fragmented cap-one physical support. It proves

`E ||rho_(123|Q')||_infinity^(2/3) -> infinity`

as the number of physical fragments tends to infinity, while the same fixed target has a finite matrix-dependent output-density bound by the completed partner fixed-matrix theorem.

Thus the divergent conditional moment cannot be a necessary bridge to QFORM. The exact formula above explains the mechanism without any new hypothesis: the fragmented scalar levels move the conditional profiles to separated output translations. The full density sees

`p_Q(t)=int p_(Q')(b) p_(Q3|Q'=b)(t-b) db`,

whereas the false repair replaces each translated profile by its height and then adds all heights as though their peaks coincided.

For the preceding account02/B15 endpoint construction (r5), with `r=4-2y`, the exact scalar density satisfies

`p_(Q')(b)=r^3/(3y)`

while

`||p_(Q3|Q'=b)||_infinity >= 4/(15r^2)`.

The unavoidable product of these two *lower-bound scales* is only

`4r/(45y) -> 0`.

This does not by itself upper-bound the joint density, but it verifies quantitatively that the divergent conditional height does not force a divergent pointwise contribution after the scalar-level weight is restored. The source-valid object is the translated joint profile `H(t-b,b)`, not its conditional height alone.

## 7. Correct first unpaid implication

The previous scalar conditional-height gates should be replaced by the following exact, source-preserving trace problem:

> For every target instance and every protected triple with residual `C!=0`, prove one universal finite `C_*` such that
>
> `sup_t int_{R^3} G(y,t-y^T Lambda y) dy <= C_*`,
>
> where `G` is not arbitrary: it is the actual product-source coarea density
>
> `G(y,v)=(1/2) int_{U^T x=y, x^T Cx=v} [prod_i f_i(x_i)]/|Cx| dH^{n-4}(x)`.

Substituting the source formula gives the completely explicit curved trace

`p_Q(t)`
`= (1/2) int_{R^3} int_{U^T x=y, x^T Cx=t-y^T Lambda y}`
`      [prod_i f_i(x_i)]/|Cx| dH^{n-4}(x) dy`.

This is not claimed solved. Its value is that it preserves exactly the two pieces destroyed by the refuted reductions:

1. original-coordinate product provenance;
2. translation/packing of scalar residual levels.

Any future Brascamp--Lieb, ridge, pair-log, or grouped-coordinate estimate should be applied to this trace (or an exactly equivalent pre-normalized joint-density expression) **before** dividing by `p_V(v)` and before taking conditional suprema.

## 8. Regularity status after this run

- **Absolute continuity:** proved at much greater generality by account02/B15: any nonzero symmetric `A` and any absolutely continuous input vector suffice.
- **Bounded density for each fixed rank>=3 matrix:** proved by account02/B15 with an explicit but matrix-dependent principal-pivot constant.
- **Universal L-infinity bound:** OPEN; this is the owner target.
- **Continuous representative for every rough target law:** OPEN. The graph-trace identity alone does not supply a law-uniform translation modulus, and this report makes no continuity claim.

The full target therefore changes `OPEN -> OPEN`, but the live proof interface changes materially: the earlier weighted conditional-height moment is eliminated, and the exact product-source graph trace is the surviving scalar-residual object.

## 9. Source integrity

No rotated independence, no arbitrary-joint coarea bound, no law-uniform pointwise quadratic Fourier decay, no projection-only shortcut, and no `L^1` characteristic-function requirement are used. The partner's r6 counterexample is consumed as an actual mathematical obstruction, not merely cited. No public release or scheduler/notification/permission change is part of this scientific result.
