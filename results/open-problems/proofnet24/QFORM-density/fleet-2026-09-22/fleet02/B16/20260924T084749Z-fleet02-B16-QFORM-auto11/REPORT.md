SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B16, 2026-09-24T08:47:49Z.
attacking: fleet03/B16 r44's shared-bank projected-square/hyperbolic gap by inserting the true dependent two-dimensional product marginal directly into the curved density integral, without projected independence or a conditional projection cap.

# fleet02/B16 — shared-bank projected square + hyperbolic receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T084749Z-fleet02-B16-QFORM-auto11`  
Role: Projection-product interaction  
Status: **NEW TARGET-LEVEL SUPPORTING THEOREM / FULL QFORM OPEN**  
Continuity of the unrestricted target: **OPEN**.

## 1. First unpaid implication

`QFORM-SHAREDBANK-NONSEPARABLE-CURVATURE-TRANSDUCER-v1`:

> The exact shared-square/hyperbolic normal form left by fleet03/B16 r44 is now paid, even with arbitrary dependence between the square projection and the overlapping hyperbolic projection. What remains is to show that the live near-coloop state either reduces source-validly to this normal form, with all other coordinates entering only through shifts/translations, or that the additional same-bank non-diagonal curvature itself supplies a previously paid Fresnel/pair/volume exit. Small nonseparable same-bank terms cannot simply be dropped for unbounded sources.

The full conjecture is not claimed.

## 2. Correction boundary and source provenance

The physical inputs are independent and each scalar density is at most one. No moments, support bounds, log-concavity, iid assumption, diagonal-basis independence, or post-rotation independence are used.

The live corrections remain binding: a bounded projected density is not projected independence; worst conditional projection caps are unavailable; arbitrary-joint coarea is false; and the fleet03/B16 mixed-norm route `int |t|^(-1/2)||G_t||_2 dt` is false. The proof below avoids all four failures. It uses a bounded **joint** density only for the actual two-dimensional projection of one original product bank, and it keeps the other scalar projection on a genuinely disjoint original-coordinate bank.

The required pinned package `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` was reread at `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Two completed ingredients are used at actual inequalities below: the bounded two-dimensional product-projection marginal, and the ruled one-sheet theorem `p(s)<=pi sqrt(2)` for a three-eigenvalue indefinite form on its majority-sign side.

The latest completed partner report consumed is fleet03/B16 r44, `20260924T082444Z-fleet03-B16-QFORM-auto11-r2`. Its theorem pays three **disjoint** projected banks, but explicitly leaves `QFORM-SHAREDBANK-PROJECTEDSQUARE-HYPERBOLIC-PREABSOLUTE-v1` when the projected square and one hyperbolic factor use the same original coordinates. The theorem below pays that exact overlap normal form.

## 3. Main curved receiver

### Theorem 3.1 — `QFORM-SHAREDBANK-PROJECTEDSQUARE-HYPERBOLIC-CURVEDCAP-v1`

Let `(S,U)` have an arbitrary joint probability density `rho` on `R^2` satisfying

`||rho||_infinity <= M`,

and let `V` be independent of the pair `(S,U)`, with scalar density `f` satisfying

`||f||_infinity <= N`.

For real `a,b` with `ab !=0`, and arbitrary deterministic shifts `d,alpha,beta,r0`, put

`Q = a(S+d)^2 + 2b(U+alpha)(V+beta) + r0`.                    (3.1)

Then `Q` has an essentially bounded density and

`boxed: ||p_Q||_infinity <= 6 (MN)^(2/3) (|a| b^2)^(-1/3).`  (3.2)

No independence between `S` and `U` is assumed or inferred. Continuity is not asserted by this argument.

### Proof

Translate `S,U,V` and the output, so it suffices to treat zero shifts. Let

`m(u)=int_R rho(s,u) ds`.

For `u !=0`, conditioning on `(S,U)` and changing variables in `V` gives, for a.e. output `q`,

`p_Q(q)
 = int_R [1/(2|bu|)] int_R rho(s,u)
        f((q-a s^2)/(2bu)) ds du.`                            (3.3)

The set `u=0` is null because `U` has a density. Write the inner integral as `J_q(u)`. There are two complementary bounds.

First, using only `f<=N`,

`J_q(u) <= N m(u).`                                           (3.4)

Second, use the actual joint cap `rho<=M` before integrating the curved square:

`J_q(u)
 <= M int_R f((q-a s^2)/(2bu)) ds.`                           (3.5)

For arbitrary nonzero `c`, the substitution `y=|a|s^2` and then `v=(q-sign(a)y)/c` gives

`int_R f((q-a s^2)/c) ds
 <= sqrt(|c|/|a|)
    sup_z int_R f(v)|v-z|^(-1/2) dv.`                         (3.6)

Among probability densities bounded by `N`, the decreasing half-potential is maximized by height `N` on the centered interval of length `1/N`; hence

`sup_z int f(v)|v-z|^(-1/2)dv <=2 sqrt(2N).`                  (3.7)

Taking `c=2bu` in (3.6),

`J_q(u) <=4M sqrt(N |b u|/|a|).`                              (3.8)

Put

`A=N/(2|b|)`,
`B=2M sqrt(N/(|ab|)).`

Equations (3.3), (3.4), (3.8) yield

`p_Q(q)
 <= int_R min( A m(u)/|u|, B/|u|^(1/2) ) du.`                 (3.9)

For any `R>0`, use the second term on `|u|<=R` and the first term outside. Since `int m=1`,

`p_Q(q) <=4B sqrt(R)+A/R.`                                    (3.10)

The minimum occurs at

`sqrt(R)=(A/(2B))^(1/3)`

and equals

`3*2^(2/3) A^(1/3) B^(2/3)
 =6(MN)^(2/3)(|a|b^2)^(-1/3).`                               (3.11)

This is uniform in `q`. QED.

The point of (3.9) is the exact interface: near `u=0`, where the hyperbolic Jacobian `1/|u|` would give a logarithm, the **joint planar cap** is spent through the square and changes the singularity to `|u|^(-1/2)`, which is locally integrable. Away from zero, only probability normalization is used. No conditional density of `S` given `U` is formed.

## 4. Product-projection corollary

Let `I,J` be disjoint sets of original physical coordinates. On `I`, put

`S=r^T X_I`, `U=u^T X_I`,

and define

`G = [[||r||^2, <r,u>], [<r,u>, ||u||^2]]`.

Assume `G>0`. On the disjoint bank `J`, put

`V=v^T X_J`, `tau=||v||_2>0`.

The completed two-dimensional product-projection theorem gives the legitimate **joint** marginal bound

`boxed: ||p_(S,U)||_infinity <=2 det(G)^(-1/2).`               (4.1)

This does not say that `S,U` are independent. The one-dimensional bounded-density projection theorem gives

`boxed: ||p_V||_infinity <=sqrt(2)/tau.`                       (4.2)

Since the source banks `I,J` are disjoint, the vector `(S,U)` and the scalar `V` are genuinely independent source objects. Substituting (4.1),(4.2) into Theorem 3.1 yields

`boxed:
 ||p_Q||_infinity
 <=12 [ |a| b^2 det(G) tau^2 ]^(-1/3).`                       (4.3)

This is the determinant-homogeneous replacement requested by partner r44.

The same estimate remains valid after conditioning on any further disjoint original-coordinate bank `W`, with arbitrary `W`-dependent shifts `d(W),alpha(W),beta(W)` and an arbitrary additive translation `R(W)`, because (4.1),(4.2) are unchanged and the conditional bound is uniform.

## 5. Exact-rank-three target consequence

Let the full quadratic core be

`A = a rr^T + b(uv^T+vu^T)`,                                 (5.1)

where `r,u` are supported on `I`, `v` is supported on the disjoint bank `J`, `G>0`, and `v!=0`. In the three-column representation `R=[r,u,v]`,

`A=R Lambda R^T`,

with

`Lambda=[[a,0,0],[0,0,b],[0,b,0]].`

Because the columns are independent,

`pdet(A)=det(R^T R) det(Lambda)
       =-a b^2 det(G) tau^2.`                                 (5.2)

Thus if this exact-rank-three core satisfies the owner target, i.e. all three nonzero eigenvalues have modulus at least one, then

`|a|b^2 det(G)tau^2
 = product_{k=1}^3 |lambda_k(A)| >=1.`                         (5.3)

Equation (4.3) therefore gives the target-level universal bound

`boxed: ||p_(X^T A X)||_infinity <=12.`                        (5.4)

This is a strict theorem for an exact-rank-three shared-bank class under the full arbitrary-source hypotheses.

## 6. Fully delocalized strict target witness

Take even `m>=4`. On one `m`-coordinate original product bank choose the orthonormal flat sign vectors

`r=m^(-1/2)(1,...,1)`,
`u=m^(-1/2)(1,...,1,-1,...,-1)`

with equal plus/minus halves. On a disjoint `m`-coordinate bank take

`v=m^(-1/2)(1,...,1)`.

Set

`S=r^T X_I`, `U=u^T X_I`, `V=v^T X_J`,
`Q_m=S^2+2UV`.                                                (6.1)

In the orthonormal carrier `(r,u,v)`, the nonzero matrix is

`[[1,0,0],[0,0,1],[0,1,0]]`,

so

`boxed: spec_nonzero(A_m)={1,1,-1}.`                           (6.2)

Every member is therefore a strict owner-target instance. The square and one hyperbolic factor **share the same physical bank**; `S` and `U` need not be independent. Nevertheless (5.4) gives

`boxed: ||p_(Q_m)||_infinity <=12`                             (6.3)

for every choice of the independent cap-one physical source laws, uniformly in `m`.

All physical coefficients have magnitude at most `1/m`; for an `I-J` physical pair the nonzero principal `2x2` determinant has magnitude `1/m^2`. Thus reciprocal payment to any fixed physical coefficient/minor deteriorates with `m`, while the source-aggregated curved receiver remains constant. This is a real aggregation-before-reciprocal-payment obstruction, not a QFORM counterexample.

A deterministic check gave nonzero spectrum `[-1,1,1]` for `m=4,8,16,64`, `det G=1`, and maximum overlap leverage `2/m`; `CHECK_OUTPUT.txt` records the values.

## 7. Required pinned result applied to an actual curved inequality

The same family has signature `(+, +, -)`. The completed ruled one-sheet theorem in the pinned `COUNTEREXAMPLE_SEARCH.md` applies directly to the physical product source and gives

`boxed: p_(Q_m)(s) <= pi sqrt(2)
       =4.442882938158366...  for a.e. s>=0.`                  (7.1)

This theorem uses two-dimensional product marginals along the rulings; it never declares the spectral coordinates independent. Equation (7.1) is sharper on the one-sheet side, while the new curved receiver (6.3) supplies full-line control, including the two-sheet side that the ruled theorem leaves open.

The pinned twisted-characteristic-function estimate was also applied in the earlier calculation `CALC.md`: if the shared overlap frame additionally has every normalized row leverage at most `1/2`, Fresnel linearisation plus geometric Brascamp-Lieb improves (4.3) to

`||p_Q||_infinity
 <=12*2^(-1/3)
    [|a|b^2 det(G)tau^2]^(-1/3)`,                             (7.2)

so an exact target core in that diffuse subcase has density `<9.525`. The no-leverage theorem (4.3) is the main result because it pays the actual r44 overlap interface without a diffuse-frame assumption.

## 8. Relation to fleet03/B16 r44

Partner r44 proves, for three disjoint source banks, a projected-square plus hyperbolic estimate `<10.938` in the normalized exact target. It explicitly states that its conditional convolution fails when the square projection and one hyperbolic factor overlap.

Theorem 3.1 replaces that failed convolution by the curved split (3.9). It requires no independence inside the overlapping pair and no conditional projection cap. Therefore the exact r44 next implication

`QFORM-SHAREDBANK-PROJECTEDSQUARE-HYPERBOLIC-PREABSOLUTE-v1`

is paid whenever the live form has exactly the source-valid normal form (3.1)/(5.1). The dependence barrier itself is no longer the debt.

What remains is structural: the general near-coloop survivor may contain non-diagonal same-bank quadratic curvature beyond the single projected square, or cross terms that prevent partitioning the sources into one dependent planar block and one genuinely disjoint scalar block. Those terms must be retained and converted into a Fresnel/pair/cross-volume resource, not treated as small errors.

## 9. Scope audit

Proved here: a distribution-free curved receiver for an arbitrary bounded dependent planar density times an independent bounded scalar density; the product-projection corollary; the exact-rank-three target bound `12`; a fully delocalized strict-target witness; and the sharper diffuse Fourier subcase.

Not proved: the unrestricted QFORM conjecture, a structural theorem reducing every near-coloop survivor to (3.1), any universal conditional projection cap, projected independence, or continuity for Theorem 3.1 under arbitrary rough densities.

The theorem is consistent with the live arbitrary-joint coarea counterexamples because it uses a genuine product separation between the two-dimensional source object `(S,U)` and the scalar source object `V`, plus the special parabolic-hyperbolic algebra. It does not assert that a generic bounded three-dimensional density has a bounded quadratic trace.
