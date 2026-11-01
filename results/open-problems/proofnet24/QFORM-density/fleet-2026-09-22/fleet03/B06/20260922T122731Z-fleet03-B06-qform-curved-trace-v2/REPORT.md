# fleet03/B06 — spectral-row Schur smoothing for curved fibers

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T122731Z-fleet03-B06-qform-curved-trace-v2`  
**Assignment:** Curved fiber integration / GEOMETRY  
**Classification:** `ESSENTIAL_STEP_APPLIED`; full conjecture **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`

## 1. Exact target and corrections retained

The target is the full arbitrary-dimensional statement: for independent real `X_i` with scalar densities bounded by one and real symmetric `A` having at least three eigenvalues of absolute value at least one, prove one universal essential-density bound for `X^T A X` (or produce a genuine target counterexample).

This derivation does **not** use the refuted law-uniform pointwise quadratic oscillatory decay, does not treat rotated eigen-coordinates as independent, and does not integrate an unrestricted spectral-fiber supremum. It changes mechanism from the previous B06 ambient `(z,s)` `L^p` energy estimate to an original-coordinate Schur pivot that preserves product provenance.

The exact assigned partner is `fleet04/B06`; no completed current-QFORM artifact from that exact slot was visible at the fresh source snapshot, so no partner result is fabricated. A compatible completed fleet04 result is applied directly instead:

* `fleet04/B18`, run `20260922T113729Z-fleet04-B18-qform-r1`, proves `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`: if a base variable `R` has density at most `M`, and conditional on `R=r` the translated square variable has density at most one, then `R+aV_R^2` has density at most `2 sqrt(M/|a|)`, without requiring independence after the translation.

I also use the completed fleet01/B16 product-projection input: a two-dimensional orthogonal marginal of a coordinate-product density with scalar caps one has density at most `2` (the report cites Livshyts--Paouris--Pivovarov, arXiv:1507.07949). fleet01/B06 has meanwhile shown that an arbitrary three-dimensional density with only the corresponding X-ray cap can still concentrate on a two-sheet hyperboloid. Therefore the residual two-dimensional projection below is kept as an **actual projection of the remaining independent original coordinates**, not replaced by a generic X-ray-bounded density.

## 2. Setup: rank-three spectral truncation in original coordinates

The new theorem is first stated for a rank-three form, which is already a genuine rotated target class and is the local spectral object that a full argument must control.

Let

`A = R Lambda R^T`,

where `R` is an `n x 3` matrix with orthonormal columns and

`Lambda = diag(lambda_1,lambda_2,lambda_3)`

is nonsingular. Write the `i`th row of `R` as `v_i^T`, with

`ell_i = |v_i|^2`.

Then `sum_i v_i v_i^T = I_3` and

`Q(X)=X^TAX=(R^T X)^T Lambda (R^T X)`.

Fix an original coordinate `i` with `ell_i>0`; put `v=v_i`, `rho=|v|=sqrt(ell_i)`, and

`a = v^T Lambda v = A_ii`.

Assume `a != 0` and that the scalar pivot has a **definite spectral Schur complement**. Equivalently:

* if `Lambda` is definite, every nonzero pivot has this property;
* if `Lambda` has inertia `(2,1)`, it holds when `a<0`, the minority sign;
* if `Lambda` has inertia `(1,2)`, it holds when `a>0`, the minority sign.

The indefinite minority-sign case is the main one.

## 3. Exact spectral-row Schur identity

Let

`Z = sum_{k != i} v_k X_k`.

Then `Z` is independent of `X_i` and

`R^T X = v X_i + Z`.

Expanding and completing only the **original** scalar coordinate `X_i` gives

`Q = a ( X_i + m(Z) )^2 + D(Z)`,                                 (3.1)

where

`m(Z) = (v^T Lambda Z)/a`

and

`D(Z)= Z^T K Z`,

`K = Lambda - (Lambda v)(Lambda v)^T/a`.                         (3.2)

The matrix `K` is symmetric and `K v=0`. Let `E` be a `3 x 2` matrix whose columns form an orthonormal basis of `v^perp`, and set

`B = E^T K E`.                                                    (3.3)

By inertia additivity, `B` is definite under the stated pivot hypothesis.

There is an exact determinant identity

`det B = rho^2 det(Lambda)/a`.                                   (3.4)

To prove it, use the orthonormal basis `(e,E)` with `e=v/rho`. In that basis write

`Lambda = [[a/rho^2, b^T],[b,C]]`.

The restriction of `K` to `v^perp` is precisely the Schur complement

`B = C - b b^T/(a/rho^2)`.

Therefore

`det Lambda = (a/rho^2) det B`,

which is (3.4). In particular

`|det B| = ell_i |det Lambda|/|a|`.                              (3.5)

This identity is the curved-fiber determinant payment; no physical `3 x 3` minor is selected.

## 4. The residual fiber is still an exact product projection

Because `K` is symmetric with kernel containing `v`, it factors as

`K = E B E^T`.

Hence

`D(Z) = xi^T B xi`,

where

`xi = E^T Z = sum_{k != i} E^T v_k X_k`.                         (4.1)

Define the `(n-1) x 2` matrix `W` by rows

`w_k^T = v_k^T E`, `k != i`.

Then

`W^T W`
`= E^T (sum_{k != i} v_k v_k^T) E`
`= E^T (I_3 - v v^T) E`
`= I_2`,                                                         (4.2)

since `E^T v=0`.

Thus `xi=W^T X_{-i}` is literally a two-dimensional orthogonal projection of the remaining independent original coordinates. This is the key product-provenance fact that the generic X-ray counterexample does not possess.

By the valid two-dimensional product-marginal theorem used in fleet01/B16,

`||g_xi||_infinity <= 2`.                                        (4.3)

For a definite `2 x 2` matrix `B`, elliptic coarea now gives the density of `D=xi^T B xi` (or of `-D` when `B<0`) the uniform bound

`M := ||p_D||_infinity <= 2 pi / sqrt(|det B|)`.                  (4.4)

Using (3.5),

`M <= 2 pi sqrt(|a|) / ( sqrt(ell_i) sqrt(|det Lambda|) ).`       (4.5)

No support, moment, continuity, connectedness, or coordinate-eigenvector alignment assumption has been added.

## 5. Apply the compatible fleet04 square-smoothing theorem

Equation (3.1) has the exact form needed by fleet04/B18.

Condition on the value `D(Z)=r`. The random shift `m(Z)` may still depend on the remaining information in `Z`, but `X_i` is independent of the whole vector `Z`. Therefore the conditional law of

`V_r = X_i + m(Z)`

is a mixture of translates of the scalar law of `X_i`; its conditional density is still bounded by one. This is exactly why the dependent version of square smoothing, rather than an independence-based convolution claim, is required.

Applying `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1` with base-density bound (4.5) yields

`||p_Q||_infinity <= 2 sqrt(M/|a|)`

and hence

`boxed{
 ||p_Q||_infinity
 <= 2 sqrt(2 pi) /
    ( ell_i |det Lambda| |a| )^(1/4).
}`                                                               (5.1)

Since `a=A_ii`, this can also be written

`boxed{
 ||p_Q||_infinity
 <= 2 sqrt(2 pi) /
    ( ell_i |lambda_1 lambda_2 lambda_3| |A_ii| )^(1/4).
}`                                                               (5.2)

### Theorem — `QFORM-SPECTRAL-ROW-SCHUR-SMOOTHING-v1`

For every rank-three real symmetric form `A=R Lambda R^T` and every product input with independent scalar densities bounded by one, if one original-coordinate scalar pivot `A_ii` leaves a definite spectral Schur complement, then `Q=X^TAX` has an essentially bounded density satisfying (5.2).

For an indefinite rank-three form of inertia `(2,1)` or `(1,2)`, every original coordinate whose diagonal entry has the minority sign is therefore fully paid at **all output levels**, including the two-sheet side that the generic X-ray-only argument cannot control.

If moreover all three nonzero eigenvalues satisfy `|lambda_j|>=1`, then

`||p_Q||_infinity <= 2 sqrt(2 pi)/(ell_i |A_ii|)^(1/4)`.          (5.3)

Writing the minority-sign Rayleigh margin as

`eta_i = |A_ii|/ell_i`,

(5.3) becomes

`||p_Q||_infinity <= 2 sqrt(2 pi)/( sqrt(ell_i) eta_i^(1/4) ).`   (5.4)

Thus a row with leverage `ell_i>=kappa` and minority-sign margin `eta_i>=tau` costs at most

`2 sqrt(2 pi) kappa^(-1/2) tau^(-1/4)`.                          (5.5)

The two exact losses are now visible: vanishing physical leverage and approach to the spectral light cone.

## 6. Why this is not the previous physical-minor theorem

fleet04/B18 proves a scalar-pivot theorem when a **selected physical three-coordinate principal block** has definite `2 x 2` Schur complement, with its constant governed by that physical block determinant. The present theorem is different: after selecting only one physical coordinate, the other two curved directions are aggregated across **all remaining coordinates** by (4.2). The determinant payment is the spectral identity

`|det B| = ell_i |det Lambda|/|A_ii|`,

not a selected physical minor.

This is useful precisely in delocalized eigenframes where every bounded-size physical compression can be tiny. It also directly answers the fleet01/B06 warning that a generic X-ray cap is insufficient: we never discard the fact that the residual two-dimensional law is an exact orthogonal projection of an independent-coordinate product law.

## 7. Boundary / failed stronger closure

The theorem does **not** prove the full owner target.

1. In signature `(2,1)`, a form may have every physical diagonal `A_ii` of the majority sign; fleet04/B18 already records an explicit Hadamard-type `3 x 3` example. Then no minority-sign scalar pivot exists, and the residual Schur form is indefinite rather than elliptic. The generic `L^infinity` cap on its two-dimensional marginal cannot by itself control an indefinite quadratic pushforward because hyperbolic strips have unbounded area.
2. Even when a rank-three spectral truncation is paid, a general higher-rank ambient matrix has additional spectral terms correlated with the selected triple. They cannot simply be convolved away or conditioned out while retaining independence of the selected spectral coordinates.
3. The quantitative bound degenerates as `ell_i ->0` or as `A_ii/ell_i ->0`; these are genuine diffuse/light-cone regimes requiring a different mechanism, not a bookkeeping defect.

So the attempted stronger shortcut “one original scalar pivot always closes rank-three rotation” is false. The repaired universal statement is exactly the definite-Schur branch (5.1).

## 8. First unpaid implication and next mechanism

For rank-exactly-three indefinite forms, the surviving local branch is now sharply characterized:

> all available high-leverage original-coordinate pivots are majority-sign or arbitrarily close to the spectral light cone.

The next B06 implication is `QFORM-MAJORITY-PIVOT-HYPERBOLIC-RESIDUAL-v1`: retain the exact product representation (4.1), but replace elliptic coarea by a product-sensitive estimate for the **indefinite** residual Schur form before applying the third square. A successful estimate must exploit more than a generic two-dimensional density or X-ray cap; fleet01/B06's shell construction explains why.

For the full higher-rank target, the next additional debt is to show how one paid rank-three spectral block survives the correlated remaining spectral contribution without pretending it is independent noise.

**Full QFORM conjecture: OPEN / NOT PROVED.**

## 9. Dependency ledger

* Fresh owner control: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`.
* Applied compatible fleet04 result: `fleet04/B18`, run `20260922T113729Z-fleet04-B18-qform-r1`, theorem `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`.
* Applied product-projection result: fleet01/B16, run `qform-20260922T114042Z-fleet01-B16-r11`, two-dimensional marginal/X-ray cap for true product projections.
* Adversarial information-loss check: fleet01/B06, run `20260922T120617Z-a01-b06-qform-r11`, `QFORM-TWOSHEET-XRAY-ONLY-FALSE-v1`.
* Exact assigned partner `fleet04/B06`: no completed current-QFORM artifact visible at the source snapshot; no result or PASS fabricated.
* Corrections retained: pointwise oscillatory decay false; unrestricted fiber-sup dimension loss; rotations destroy coordinate independence; cross-minor-alone route false.
