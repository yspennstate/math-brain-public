SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B13, 2026-09-24T05:30:36.801885Z.
attacking: a separable-perturbation rank-two half-Riesz theorem and its scalar-Schur consequence, so the partner's rough two-strip endpoint is paid whenever the physical scalar pivot is nondegenerate.

# account01/B13 — diffuse rank-two separable half-Riesz and full-diagonal scalar-Schur receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T053036Z-account01-B13-auto11`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Classification: **ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREMS PROVED**  
Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Unrestricted continuity: **OPEN**.

The proof below keeps arbitrary cap-one product laws, arbitrary support fragmentation and translations, every diagonal quadratic term, and arbitrary affine terms. It never rotates the random variables, never uses law-uniform pointwise one-dimensional quadratic decay, and never deletes a coefficient-small quadratic tail.

## 1. Extremal-product reduction retained at the correct scope

The optimizer-free reduction proved in the preceding account01/B13 report remains the admissible extremal-law interface:

`yspennstate/math-open-problems@0031d0fd7ef023c747e8177b6079742fc0f0c0f8`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260924T033304Z-account01-B13-QFORM-auto11/REPORT.md`.

For every measurable `0<=K<=1` and independent cap-one mass-one densities `f_i`, every `epsilon>0` admits bounded finite-union unit-measure sets `E_i` such that

`int K(x) prod_i 1_{E_i}(x_i) dx >= int K(x) prod_i f_i(x_i) dx-epsilon`.   (1.1)

Hence the supremum over cap-one product densities equals the supremum over bounded finite-union unit-product indicators. This is equality of suprema, not global optimizer attainment, and gives no single-interval, centered-uniform, common-diameter, or uniform-fragment-count conclusion.

For the slab kernel `K=1_{x^T A x in J}`, a witness of ratio `rho` transfers to a bounded finite-union unit-product-set witness with ratio at least `rho-delta` for arbitrary `delta>0`.

## 2. Source-pinned inputs actually used

### 2.1 Complex-amplitude separable-phase mechanism

The completed rank-r separable-phase proof is source-pinned at

`yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`

`proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`.

Its exact Fourier step works for complex product amplitudes `f_i(x) exp(i t V_i(x))`. For an orthonormal r-frame with row leverage at most `1/2`, it proves

`||hat g_t||_1 <= (2 pi)^r B(U)`,

where

`B(U)=prod_i (1-c_i)^(-(1-c_i)/2)`

and `c_i` are the row leverages. The same report derives the quadratic Fresnel estimate while retaining every separable `V_i` inside the complex amplitudes.

### 2.2 Designated partner account02/B13 r40

The newest completed compatible designated-partner report read in this run is

`yspennstate/math-open-problems@2af615c6d649e207191127733fc6dd180db14944`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260924T025738Z-account02-B13-QFORM-auto11/REPORT.md`.

Two pieces are applied below:

1. `QFORM-FINITE-CENTER-CONDITIONING-v1`: conditioning any finite set of ORIGINAL coordinates preserves the product law on the others, and some center value has slab ratio at least the original ratio; the induced change is an arbitrary affine term plus a constant.
2. `QFORM-ROWSTRIP-AGGREGATE-ENERGY-OBSTRUCTION-v1`: rowwise `O(rho^-1/6)` proximity of a rank-two carrier to one/two latent lines does **not** imply an operator-small discarded strip; the strip must remain in the phase.

The theorem proved below is designed precisely so that this rough strip and every diagonal term remain inside the exact phase.

## 3. New theorem: rank-two half-Riesz with arbitrary separable perturbations

### Theorem 3.1 — `QFORM-DIFFUSE-RANK2-SEPARABLE-HALFRIESZ-v1`

Let `X_1,...,X_n` be independent real random variables with densities `0<=f_i<=1`. Let `W` be an `n x 2` real matrix with

`W^T W=I_2`,

and row leverages

`c_i=||w_i||^2<=1/2`.

Let `M` be any invertible real symmetric `2 x 2` matrix, let `V_i:R->R` be arbitrary measurable functions finite almost surely, and define

`T=(W^T X)^T M(W^T X)+sum_i V_i(X_i)`.                         (3.1)

Then for every `a in R`,

`boxed: E |T-a|^(-1/2) <=4 sqrt(2 B(W)) |det M|^(-1/4)}`          (3.2)

and therefore, since `B(W)<=e`,

`boxed: sup_a E |T-a|^(-1/2) <=4 sqrt(2e) |det M|^(-1/4).}`       (3.3)

This is a fractional-potential theorem, not a bounded-density assertion for rank two. Arbitrary diagonal quadratic terms and arbitrary affine terms are included through the `V_i`.

#### Proof

For each fixed real `t`, put

`h_{i,t}(x)=f_i(x) exp(i t V_i(x))`.                               (3.4)

Then `||h_{i,t}||_p=||f_i||_p<=1` for all `p>=1`. Push the complex product measure with density `prod_i h_{i,t}` forward under `x -> W^T x`, obtaining an L1 complex density `g_t` with `||g_t||_1<=1`. Exactly as in the source-pinned separable-phase proof, geometric rank-one Brascamp--Lieb and sharp Hausdorff--Young give

`||hat g_t||_1 <=(2 pi)^2 B(W)`.                                  (3.5)

The quadratic Fresnel inversion in dimension two therefore gives, for `t!=0`,

`|phi_T(t)| <= pi B(W) |det M|^(-1/2) |t|^(-1)`.                 (3.6)

The actual characteristic function also satisfies `|phi_T(t)|<=1`. Put

`K=pi B(W) |det M|^(-1/2)`.                                      (3.7)

Then

`|phi_T(t)|<=min(1,K/|t|)`.                                       (3.8)

For `epsilon>0`, define the positive regularized half-Riesz kernel

`k_epsilon(x)=sqrt(2/pi) int_0^infinity exp(-epsilon s) cos(sx) s^(-1/2) ds`.

Using the Gamma integral,

`k_epsilon(x)=sqrt(2) Re (epsilon-i x)^(-1/2)>=0`,                 (3.9)

and for every `x!=0`,

`k_epsilon(x)->|x|^(-1/2)` as `epsilon downarrow0`.                (3.10)

Because `s^(-1/2) min(1,K/s)` is integrable on `(0,infinity)`, Fubini is justified and

`E k_epsilon(T-a)`
` <=sqrt(2/pi) int_0^infinity s^(-1/2) |phi_T(s)| ds`
` <=sqrt(2/pi) int_0^infinity s^(-1/2) min(1,K/s) ds`.             (3.11)

Split at `s=K`:

`int_0^infinity s^(-1/2) min(1,K/s) ds`
`=2 sqrt(K)+2 sqrt(K)=4 sqrt(K)`.                                 (3.12)

Fatou's lemma, using positivity in (3.9), gives

`E|T-a|^(-1/2)`
` <=4 sqrt(2/pi) sqrt(K)`
` =4 sqrt(2 B(W)) |det M|^(-1/4)`.                               (3.13)

(The same finite bound forces `P(T=a)=0`, so the possible value at `x=0` causes no issue.) This proves (3.2).

Finally, the inequality

`-(1-c) log(1-c)<=c`, `0<=c<1`,                                   (3.14)

and `sum_i c_i=2` give

`log B(W)<=1`, hence `B(W)<=e`. This proves (3.3). `QED`

### Invariant nonorthonormal form

Let `Z` be any full-column-rank `n x 2` matrix and put

`G=Z^T Z`,
`ell_i=z_i^T G^(-1) z_i`.                                        (3.15)

If `max_i ell_i<=1/2`, then with `W=Z G^(-1/2)` and

`M=G^(1/2) Lambda G^(1/2)`                                       (3.16)

we have `W^T W=I_2`, row leverages `ell_i`, and

`det M=det(G) det(Lambda)`.                                       (3.17)

Thus

`boxed: sup_a E |(Z^T X)^T Lambda(Z^T X)+sum_i V_i(X_i)-a|^(-1/2)`
` <=4 sqrt(2e) |det(G) det(Lambda)|^(-1/4).}`                     (3.18)

This form is useful after partner finite-center conditioning, where the remaining coefficient columns need not stay orthonormal.

## 4. New scalar-Schur receiver retaining the full diagonal residual

### Theorem 4.1 — `QFORM-DIAG-RANK2-DIFFUSE-SCHUR-SEPARABLE-v1`

Let

`A=D+U Lambda U^T`,
`U^T U=I_2`,                                                       (4.1)

where `D=diag(d_1,...,d_n)` and `Lambda` is invertible symmetric. Assume

`max_i c_i<=1/3`, `c_i=||u_i||^2`.                                (4.2)

Allow also an arbitrary affine term `b^T x+beta`. Choose a physical coordinate `k`, and write

`d=d_k`, `u=u_k`, `c=||u||^2`,
`a=A_kk=d+u^T Lambda u`.                                          (4.3)

Assume `d!=0` and `a!=0`. Then the quadratic-affine polynomial

`Q(X)=X^T A X+b^T X+beta`                                         (4.4)

has a bounded density satisfying

`boxed: ||p_Q||_infinity`
` <=4 sqrt(2e) [(1-c)|a d det Lambda|]^(-1/4).}`                  (4.5)

Every diagonal coefficient in `D`, including an arbitrarily large and arbitrarily distributed residual diagonal bank, is retained exactly.

#### Proof

Write `Y=X_{-k}` and `U_0=U_{-k}`. The `k`-cross vector is

`q=U_0 Lambda u`.                                                  (4.6)

Completing the square in the ORIGINAL independent coordinate `X_k` gives

`Q=a (X_k+m(Y))^2+R(Y)`,                                          (4.7)

where the shift `m(Y)` is affine in `Y` and

`R(Y)=Y^T S Y+tilde b^T Y+tilde beta`,                            (4.8)

with the exact scalar Schur matrix

`S=D_0+U_0 C U_0^T`,
`C=Lambda-Lambda u u^T Lambda/a`.                                 (4.9)

Because `X_k` is independent of `Y` and its density is at most one, translation by `m(Y)` does not change that cap. The density of `a(Z+m)^2` is bounded by

`|a|^(-1/2) |s|^(-1/2)`                                          (4.10)

at signed displacement `s`. Hence

`p_Q(t)<=|a|^(-1/2) E|R-t|^(-1/2)`.                              (4.11)

Now

`G=U_0^T U_0=I_2-u u^T`,                                         (4.12)

so `det G=1-c>0`. Put

`W=U_0 G^(-1/2)`,
`M=G^(1/2) C G^(1/2)`.                                            (4.13)

Then `W^T W=I_2`. Matrix determinant lemma gives

`det C=det Lambda (1-u^T Lambda u/a)`
`     =det Lambda * d/a`,                                         (4.14)

hence

`boxed: det M=(1-c) d det Lambda/a.}`                             (4.15)

For every remaining row `i`, its leverage in `W` is

`tilde c_i=u_i^T G^(-1)u_i`
` <=c_i/(1-c)`                                                     (4.16)

by Sherman--Morrison and Cauchy--Schwarz. Under (4.2), `c_i<=1/3` and `c<=1/3`, so

`tilde c_i<=1/2`.                                                   (4.17)

Equation (4.8) is exactly

`R(Y)=sum_{i!=k} d_i Y_i^2 +(W^T Y)^T M(W^T Y)+linear+constant`.   (4.18)

Apply Theorem 3.1 with the separable functions

`V_i(y)=d_i y^2+tilde b_i y`.                                      (4.19)

Therefore

`E|R-t|^(-1/2)<=4 sqrt(2e)|det M|^(-1/4)`.                       (4.20)

Combining (4.11), (4.15), and (4.20) gives

`|a|^(-1/2)|det M|^(-1/4)`
`=[(1-c)|a d det Lambda|]^(-1/4)`,                                (4.21)

which is (4.5). `QED`

## 5. Target-level consequence in the hard exact-rank-two chamber

Assume now the exact target-side chamber

`A=D+U Lambda U^T`, `U^T U=I_2`, `max_i c_i<=1/3`, `s_3(A)>=1`.   (5.1)

Because `rank(U Lambda U^T)<=2`, the singular-value rank inequality gives

`s_3(A)<=s_1(D)=max_i |d_i|`.                                     (5.2)

Thus some physical `k` has

`|d_k|>=1`.                                                        (5.3)

If its actual scalar pivot `a=A_kk` is nonzero, Theorem 4.1 gives, for every interval slab witness of ratio

`rho=P(Q in J)/|J|`,                                               (5.4)

`rho<=4 sqrt(2e)[(1-c_k)|A_kk d_k det Lambda|]^(-1/4)`.           (5.5)

Equivalently,

`boxed: (1-c_k)|A_kk d_k det Lambda| <=1024 e^2 rho^(-4).}`        (5.6)

Since `1-c_k>=2/3` and `|d_k|>=1`,

`boxed: |A_kk det Lambda| <=1536 e^2 rho^(-4)}`                   (5.7)

with

`4 sqrt(2e)=9.326575926388497...`,
`1024 e^2=7566.393445304985...`,
`1536 e^2=11349.590167957478...`.                                 (5.8)

The important advance over the earlier scalar-pivot formula is scope: (5.5)-(5.7) now retain **all** of `D_{-k}` and arbitrary affine terms inside the rank-two half-Riesz estimate. No diagonal tail or rough strip is suppressed.

Hence every hypothetical sequence in this exact diffuse rank-two chamber with `rho->infinity` must enter the quantitative pivot-degenerate set

`|A_kk det Lambda|=O(rho^-4)`                                      (5.9)

for every chosen `|d_k|>=1` pivot to which (5.5) is applied. If `|det Lambda|` stays bounded below, the actual physical scalar pivot must collapse as `O(rho^-4)`; if `|A_kk|` stays bounded below, the latent rank-two determinant must collapse as `O(rho^-4)`.

## 6. Actual application of account02/B13 r40

Partner r40 isolates `QFORM-CENTERFREE-TWOSTRIP-DIAGONAL-BANK-RECEIVER-v1` and proves that the `O(rho^-1/6)` strip cannot be discarded in operator norm. Theorem 4.1 pays a large part of precisely that obstruction **without replacing either strip by its central line**:

- the entire exact rank-two carrier `U Lambda U^T` remains in the phase;
- the entire arbitrary diagonal `D` remains in the separable functions;
- any affine term created by partner `QFORM-FINITE-CENTER-CONDITIONING-v1` is also allowed.

More invariantly, after conditioning a finite original-coordinate center set `E`, write the remaining rank-two carrier as

`Z Lambda Z^T`, `G=Z^T Z`, `Lambda_B=G^(1/2)Lambda G^(1/2)`.       (6.1)

If `G` is nonsingular, the normalized row leverages

`ell_i=z_i^T G^(-1)z_i`                                           (6.2)

remain at most `1/3`, and the conditioned slice contains a physical pivot `k` with `d_k!=0` and `a_k!=0`, then the same proof gives the actual conditional slab inequality

`boxed: rho <=4 sqrt(2e)`
` *[(1-ell_k)|a_k d_k det(Lambda_B)|]^(-1/4).}`                   (6.3)

Partner finite-center conditioning preserves the slab ratio, so (6.3) is a genuine inequality for the partner slice, not only a formal matrix identity.

Therefore the partner's center-free two-strip receiver is no longer needed in any conditioned subbranch satisfying the nondegeneracy in (6.3). A remaining high-ratio survivor must instead exhibit at least one of the following concrete failures:

1. the normalized post-conditioning rank-two carrier becomes leverage-heavy (`max ell_i>1/3`);
2. its coefficient Gram `G` becomes singular/nearly singular;
3. every usable physical diagonal pivot is removed or has `a_k=0`;
4. the determinant product in (6.3) is `O(rho^-4)`.

This is the promised application of a completed partner result to an actual inequality.

## 7. What remains open

The first unpaid implication is now

`QFORM-PIVOT-DEGENERATE-DIAG-RANK2-GLUE-v1`:

> Close the exact diffuse diagonal-plus-rank-two chamber when the physical scalar pivot cancels (`A_kk=0` or quantitatively `|A_kk det Lambda|=O(rho^-4)`), including the tiny-`det Lambda` branch; or route it into an already-paid grouped/high-cardinality bank receiver. Then extend the same receiver beyond the exact-rank-two skeleton while retaining the known nonseparable tail.

This run does **not** prove the unrestricted three-eigenvalue conjecture. In particular, a coefficient-small rank-one/two tail cannot be deleted under arbitrary remote fragmented supports, and finite-center conditioning can make normalized leverages heavy. Continuity remains a separate stronger conclusion.
