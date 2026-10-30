# fleet03/B09 — rank-two Schur aggregation after one physical pivot

**Run:** `20260922T134741Z-fleet03-B09-QFORM-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Bilinear block mechanism  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval/transport only.

## 1. Scope and corrections

The full target remains open: for independent real coordinates with probability densities at most one and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove one dimension- and law-independent density bound for `Q=X^TAX`, or produce a genuine target counterexample. Continuity is a separate stronger conclusion.

This report uses only original-coordinate conditioning. It does not rotate the random vector and declare spectral coordinates independent, invoke the refuted law-uniform pointwise quadratic-phase decay, use a fiber supremum, or select one tiny coordinate minor and immediately pay its reciprocal. The live corrections `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, and `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` are all respected.

The designated partner `fleet04/B09` had no completed current-QFORM handoff or research directory at the final pre-publication check, so no partner result is fabricated or awaited. I instead apply two completed compatible proof-level dependencies:

1. `QFORM-CROSSBLOCK-RANK-r-FOURIER-v1`, `yspennstate/math-open-problems@8624982153e5a2154e4ae8922d2fe4dc77080efc`, `proofnet24/QFORM-density/fleet-2026-09-22/interactive/20260922T121109Z-crossblock-and-lower-bounds/REPORT.md`;
2. fleet03/B02 `QFORM-SCHUR-2PLUS1-POTENTIAL-v1`, `yspennstate/math-open-problems@2e9ab3bfa05919cd9115fc5f6285ee0683adfb7c`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260922T130245Z-fleet03-B02-QFORM-r11/REPORT.md`.

The first gives the exact rank-two mixed-Fourier endpoint used below. The second supplies the one-dimensional square-potential estimate and shows how a physical pivot can be completed without falsely creating independence.

## 2. New theorem: rectangular rank-two Schur block is enough after one pivot

### Theorem `QFORM-SCHUR-RANK2-RECTANGULAR-v1`

Let `X_1,...,X_n` be independent real random variables with probability densities bounded by one, and let `A` be real symmetric. Choose one original coordinate `k` with

`d=A_kk != 0`.

Choose disjoint original-coordinate sets `I,J`, also disjoint from `{k}`. Put

`a=A[I,k]`, `b=A[J,k]`, `B=A[I,J]`,

and define the rectangular Schur cross block

`C = B - a b^T/d`.

Assume `C` has rank exactly two, with nonzero singular values `s_1,s_2`, and put

`Delta=s_1 s_2>0`.

No restriction is imposed on `|I|,|J|`, on the principal blocks `A[I,I],A[J,J]`, on outside coordinates, on signs, or on outside couplings. Then `Q=X^TAX` has an essentially bounded density and

`boxed( ||p_Q||_infinity <= [16/3^(1/4)] |d|^(-1/2) Delta^(-1/4). )`      (2.1)

Hence for every interval `L`,

`boxed( P{Q in L} <= [16/3^(1/4)] |d|^(-1/2) Delta^(-1/4) |L|. )`       (2.2)

This is a direct linear small-ball estimate. It has no square-root decoupling loss.

### Proof

Condition on all coordinates outside `I union J union {k}`. Write `z=X_k`, `x=X_I`, `y=X_J`. The conditional quadratic-affine polynomial is

`q(x,y,z)=q_I(x)+q_J(y)+2x^TBy+d z^2+2z(a^Tx+b^Ty+c)+c_0`,

where `q_I,q_J` are arbitrary quadratic-affine functions and `c,c_0` depend only on the conditioned outside coordinates.

Complete the square in the original physical pivot:

`q = d[z+(a^Tx+b^Ty+c)/d]^2 + R(x,y)`,                                  (2.3)

where the cross block of the residual `R` between `x` and `y` is exactly

`C=B-ab^T/d`.                                                           (2.4)

All other residual self terms are arbitrary.

Let `eta(t)=E exp(itR)` under the conditional product law of `(x,y)`. Apply the completed rank-`r` cross-block theorem with `r=2`. Its Plancherel proof itself remains valid at `r=2`; only the final `L^1_t` integration fails there. Thus

`|eta(t)| <= min(1, D/|t|)`,
`D=2 pi Delta^(-1/2)`.                                                   (2.5)

Consequently

`int_R |eta(t)|^(3/2) dt <= 6D = 12 pi Delta^(-1/2)`.                    (2.6)

Inverse Hausdorff--Young for the Fourier convention used in the source theorem gives a density `h` for `R` with

`||h||_3 <= (2pi)^(-2/3) [12pi Delta^(-1/2)]^(2/3)
          = 6^(2/3) Delta^(-1/3).`                                      (2.7)

Now return to the pivot square. Conditional on `(x,y)`, the translated physical variable `z+(a^Tx+b^Ty+c)/d` still comes from a one-dimensional density bounded by one, merely translated. Therefore the conditional density of

`d[z+(a^Tx+b^Ty+c)/d]^2`

is bounded by

`|d|^(-1/2) |v|^(-1/2)`                                                  (2.8)

on the appropriate half-line. Importantly, the singularity stays at `v=0`; its envelope is independent of the correlated shift.

Disintegration of (2.3) therefore yields, for almost every `s`,

`p_q(s) <= |d|^(-1/2) int_R h(r) |s-r|^(-1/2) dr`.                       (2.9)

For any probability density `h in L^3`, the elementary split at radius `rho` gives

`int h(r)|s-r|^(-1/2)dr
 <= 4 ||h||_3 rho^(1/6)+rho^(-1/2)`.

Optimizing at `rho^(2/3)=3/(4||h||_3)` gives

`sup_s int h(r)|s-r|^(-1/2)dr
 <= 4^(7/4) 3^(-3/4) ||h||_3^(3/4)`.                                    (2.10)

Insert (2.7). Since

`4^(7/4)3^(-3/4)[6^(2/3)]^(3/4)=16/3^(1/4)`,

(2.9) proves (2.1), uniformly in all outside conditioned values. Averaging the conditional interval inequalities proves (2.2) and therefore the unconditional essential density bound. QED.

### What was gained

The preceding fleet03/B02 theorem required two *physical* pairs and an invertible `2x2` Schur block. The present theorem allows arbitrarily large disjoint coordinate banks `I,J` and uses the product of the two nonzero singular values of their whole Schur cross operator. Thus the rank-two interaction can be aggregated before any coordinate minor is inverted.

The theorem does **not** claim continuity. The proof establishes an `L^infinity` Radon--Nikodym density through interval domination; unlike the rank-three mixed-Fourier theorem, it does not produce an `L^1` characteristic function for the full variable.

## 3. Exact-rank-three corollary: residual Pluecker aggregation after a nonisotropic pivot

The rectangular theorem becomes substantially stronger when combined with the exact geometry of a rank-three spectral frame.

Let

`A=U Lambda U^T`, `U^T U=I_3`,

with `Lambda` real symmetric invertible. Fix a physical coordinate `k`. Let `u^T` be row `k` of `U`, put

`ell=||u||^2`, `d=u^T Lambda u`,

and assume `ell>0`, `d!=0`. Let `P` be a `3x2` matrix whose columns form an orthonormal basis of `u^perp`. For every `j!=k` put

`v_j=P^T u_j in R^2`.

Then the residual rows form an exact two-frame:

`sum_{j!=k} v_j v_j^T = I_2`.                                          (3.1)

For every two-set `E` of residual physical coordinates define

`w_E=det(V_E)^2`,

where `V` has rows `v_j^T`. Cauchy--Binet gives

`sum_E w_E=1`.                                                         (3.2)

Its one-point marginals are

`sum_{E: j in E} w_E = q_j:=||v_j||^2`.                               (3.3)

Define the disjoint residual Pluecker mass

`R_2(V)=sum_{E cap F=empty} w_E w_F`.                                  (3.4)

By the union bound and (3.3),

`boxed( R_2(V) >= 1-sum_j q_j^2. )`                                   (3.5)

In particular, since `sum_j q_j=2`, if `max_j q_j<=eta<1/2`, then

`R_2(V) >= 1-2eta >0`.                                                 (3.6)

Now split the residual physical coordinates by independent auxiliary fair coins into `I` and `J`. With

`G_I=V_I^T V_I`, `G_J=V_J^T V_J`,

Cauchy--Binet gives the exact expectation

`E[det G_I det G_J]=R_2(V)/16`,                                       (3.7)

because an ordered disjoint pair of two-sets imposes four independent membership conditions. Therefore one deterministic original-coordinate cut satisfies

`det G_I det G_J >= R_2(V)/16`.                                       (3.8)

Complete the physical pivot `k`. In spectral coordinates the Schur matrix is

`H = Lambda - (Lambda u)(Lambda u)^T/d`,                               (3.9)

which annihilates `u`. On `u^perp` put

`Gamma=P^T H P`.

It is invertible, and the block determinant identity gives

`boxed( |det Gamma| = |det Lambda| ell/|d|. )`                         (3.10)

The Schur cross block between the cut residual coordinate banks is

`C=V_I Gamma V_J^T`.

Its rank is two and the product of its two nonzero singular values is exactly

`Delta(C)=|det Gamma| sqrt(det G_I det G_J)`.                          (3.11)

Using (3.8)--(3.10),

`boxed( Delta(C) >= [|det Lambda| ell/(4|d|)] sqrt(R_2(V)). )`          (3.12)

Apply Theorem 2.1. The powers of `d` partially cancel and give the explicit corollary

`boxed(
 ||p_Q||_infinity
 <= [16 sqrt(2)/3^(1/4)]
    [|d| ell |det Lambda|]^(-1/4) R_2(V)^(-1/8).
)`                                                                       (3.13)

Under the exact target-rank-three normalization `|lambda_1 lambda_2 lambda_3|>=1`,

`||p_Q||_infinity
 <= [16 sqrt(2)/3^(1/4)] (|d|ell)^(-1/4) R_2(V)^(-1/8).`               (3.14)

If only the residual leverage cap `max q_j<=eta<1/2` is recorded, (3.6) gives

`boxed(
 ||p_Q||_infinity
 <= [16 sqrt(2)/3^(1/4)] (|d|ell)^(-1/4)(1-2eta)^(-1/8).
)`                                                                       (3.15)

### Why this is a real extension of the current high-row branch

The completed large-row Schur theorem in the archive required every projected residual row to have norm at most `1/2`, i.e. `q_j<=1/4`, so that a two-dimensional Brascamp--Lieb Fourier estimate could be applied directly. The new random-cut/Schur aggregation does not require that threshold. It remains quantitative whenever the *aggregate disjoint residual Pluecker mass* is positive, and the crude leverage-only sufficient threshold expands to `q_j<1/2`.

This directly attacks the previously named `multiple projected large rows` frontier: rather than rejecting a residual two-frame as soon as one row exceeds norm `1/2`, it aggregates the two-dimensional area over disjoint residual banks and then invokes the rank-two Schur potential theorem.

## 4. Relation to the global target and remaining obstruction

This run does not prove the full conjecture.

For exact rank three, the new branch still degenerates in two identifiable configurations:

1. **isotropic pivot:** `d=u^T Lambda u` is zero or very small;
2. **near-coloop residual frame:** `R_2(V)` is zero or very small, meaning essentially every residual two-dimensional basis shares a small heavy coordinate core.

These are not bookkeeping residuals. The live coloop-bank examples show that disjoint-minor resources can genuinely vanish while the quadratic form remains uniformly smooth after product-preserving bank compression. The next B09 mechanism should therefore attack these two endpoint geometries directly, most naturally through a hyperbolic linear pivot for `d=0` and bank compression when `R_2` collapses.

For the full matrix with extra spectral directions, there is the additional cancellation problem: the actual Schur cross block of the full `A` need not equal the rank-three component's cross block. A target-level proof needs either a certificate on the actual full Schur operator or an absorption argument for the extra eigendirections.

## 5. Finite diagnostic verification

A seeded floating-point check on an `8x3` random orthonormal frame verified to machine precision:

- `V^T V=I_2` after deleting the pivot and projecting to `u^perp`;
- `sum_E w_E=1` and the one-point identities (3.3);
- the exact cut average (3.7), numerically `0.01561992392746086` versus `R_2/16=0.015619923927460873`;
- for the maximizing cut, the product of the two nonzero singular values of `V_I Gamma V_J^T` equals `|det Gamma| sqrt(det G_I det G_J)` to floating error (`2.7961687118987184` versus `2.7961687118987175`);
- the constant in (2.1) is `16/3^(1/4)=12.1573709704...`, and in (3.13) is `16sqrt(2)/3^(1/4)=17.1931189092...`.

These calculations are diagnostics only. Equations (2.1)--(3.15) are proved analytically above.

## 6. Status

- `QFORM-SCHUR-RANK2-RECTANGULAR-v1`: **PROVED supporting theorem**.
- `QFORM-RANK3-RESIDUAL-PLUECKER-SCHUR-v1`, equations (3.13)--(3.15): **PROVED in exact-rank-three scope**.
- exact designated partner `fleet04/B09`: **no completed current-programme artifact observed; not fabricated**.
- completed cross-block and Schur-potential dependencies: **APPLIED to explicit inequalities**, not merely cited.
- full QFORM target: **OPEN**.
- continuous-density conclusion for the new rank-two-Schur branch: **NOT PROVED**; only essential boundedness is claimed.
- native learned-memory receiver use: **NOT OBSERVED**; status remains `WITHOUT_VERIFIED_BRAIN`.
