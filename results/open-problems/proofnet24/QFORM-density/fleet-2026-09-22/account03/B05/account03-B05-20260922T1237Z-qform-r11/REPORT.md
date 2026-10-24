# account03/B05 — coarea closure via rank-two cross-block smoothing and HLS

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `account03-B05-20260922T1237Z-qform-r11`  
**Assignment:** Quadratic coarea bound  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREMS PROVED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Target, corrections, and peer mathematics actually used

The target is the full arbitrary-law statement: for independent real `X_i` with probability densities `0<=f_i<=1`, and a real symmetric matrix `A` with at least three eigenvalues of absolute value at least one, prove a universal dimension- and law-independent essential-density bound for `Q=X^TAX`, or give a valid counterexample. Continuity is a separate stronger request.

This run preserves the three mandatory corrections: it does not use law-uniform pointwise Fresnel decay; it does not rotate to the eigenbasis and keep independence; and it does not take a spectral-fiber supremum, which can lose a factor growing with dimension.

The assigned partner is `account04/B05`. At the final source refresh there was still no completed current-QFORM report in that slot's canonical math-open-problems or shared-handoff root, so no partner theorem is fabricated. Two completed compatible results are applied directly:

1. `account02/B05`, report `proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260922T115002Z-b05-qform-9c3a2d7e/REPORT.md`, proves the coarea-to-half-Riesz lemma

   `p_Q(t) <= |a|^(-1/2) int |t-s|^(-1/2) p_R(s) ds`

   for `Q=a(X+m(Y))^2+R(Y)`, and the quantitative `L^p`, `p>2`, closure. Its first stated missing implication is precisely the generic nonzero-diagonal binary Schur residual.

2. The completed cross-block theorem in `proofnet24/QFORM-density/fleet-2026-09-22/interactive/20260922T121109Z-crossblock-and-lower-bounds/REPORT.md` proves, for a quadratic form whose original-coordinate cross block has rank `r`, the Fourier estimate

   `|phi(t)| <= (2 pi)^(r/2) |t|^(-r/2) Delta^(-1/2)`,

   where `Delta` is the product of its nonzero singular values. For `r=2` this is not integrable and therefore does not by itself give a bounded density. The first theorem below shows that the *outer square coarea* supplies exactly the missing half-order.

The current universal assembly also identifies a product-elliptic trace inequality as the major remaining coarea debt. The present results close two substantial sub-interfaces of that debt but do not establish the full trace inequality.

## 2. Rank-two cross-block plus one outer square is enough

### Theorem 2.1 — `QFORM-OUTER-SQUARE-RANK2-CROSSBLOCK-v1`

Let `X_0,X_1,...,X_m` be independent real random variables with densities bounded by one. Suppose, after conditioning on any further outside coordinates and making coordinatewise translations, a quadratic expression has the form

`Q = a (X_0 + m(X_1,...,X_m))^2 + R(X_1,...,X_m)`,  `a != 0`,

where `R` is a quadratic form in the original independent coordinates `X_1,...,X_m`.

Assume that these residual coordinates admit a disjoint partition `I union J={1,...,m}` for which the cross block `B=R[I,J]` has rank exactly two, with nonzero singular values `s_1,s_2`. Put

`Delta=s_1 s_2>0`.

Then `Q` has an essentially bounded density and

`||p_Q||_infinity <= 8 sqrt(3) |a|^(-1/2) Delta^(-1/4)`.                 (2.1)

No sign condition on `R` is required, and arbitrary quadratic terms inside `I` and inside `J` are retained.

### Proof

Apply the completed rank-two cross-block Fourier estimate to `R`. For every `t!=0`,

`|phi_R(t)| <= 2 pi |t|^(-1) Delta^(-1/2)`.

Set `D=2 pi Delta^(-1/2)`. Together with `|phi_R(t)|<=1`,

`|phi_R(t)| <= min(1,D/|t|)`.

Therefore

`int_R |phi_R(t)|^(4/3) dt`

` <= 2[ int_0^D 1 dt + D^(4/3) int_D^infinity t^(-4/3) dt ]`

` = 8D`.

With the Fourier convention `hat f(t)=int exp(ity) f(y)dy`, inverse Hausdorff--Young gives

`||p_R||_4 <= (2 pi)^(-3/4) ||phi_R||_(4/3)`

` <= (2 pi)^(-3/4) (8D)^(3/4)`

` = 2^(9/4) Delta^(-3/8)`.                                               (2.2)

Now apply the `account02/B05` coarea-to-Riesz lemma to the independent scalar `X_0`. Its `p=4` Riesz estimate has `p'=4/3` and

`C_4=[2/(1-p'/2)]^(1/p')=6^(3/4)`.

Hence

`||p_Q||_infinity`

` <= |a|^(-1/2) * 2 ( C_4 ||p_R||_4 )^(2/3)`

` <= |a|^(-1/2) * 2 [6^(3/4) 2^(9/4) Delta^(-3/8)]^(2/3)`

` = 8 sqrt(3) |a|^(-1/2) Delta^(-1/4)`.

This is (2.1). Every use of independence is in the original coordinate partition: `X_0`, `X_I`, and `X_J` are disjoint original-coordinate blocks. QED.

### Why this is a genuine threshold improvement

A rank-two cross block alone gives only `|t|^-1`, the known nonintegrable endpoint. The outer square converts the resulting residual `L^4` estimate into an `L^infinity` density bound through the half-Riesz kernel. Thus one does **not** need a rank-three cross block once a genuine independent outer quadratic coordinate is available.

## 3. Application to the localized rank-three spectral-Schur branch

Use the notation of the completed `account03/B19` spectral-Schur decomposition. For a rank-three form

`A_0=R Lambda R^T`,  `R^T R=I_3`,

choose a physical coordinate row `v`, put

`c=|v|^2`,  `a=v^T Lambda v`,

and complete the square in that physical input. The exact residual is rank two and has signed pseudodeterminant

`pdet(T)=c det(Lambda)/a`.                                                (3.1)

Let `U` be an orthonormal two-column spectral frame for the residual matrix on the remaining physical coordinates. Suppose there is a partition of those coordinates such that

`U_I^T U_I >= alpha I_2`,  `U_J^T U_J >= alpha I_2`.                    (3.2)

If the two nonzero residual eigenvalues are `theta_1,theta_2`, the corresponding residual cross block has rank two and

`Delta = |theta_1 theta_2| sqrt(det(U_I^T U_I) det(U_J^T U_J))`

`      >= alpha^2 |pdet(T)|`

`      = alpha^2 c |det Lambda|/|a|`.                                   (3.3)

Theorem 2.1 therefore yields

`||p_Q||_infinity`

` <= 8 sqrt(3) alpha^(-1/2) (|a| c |det Lambda|)^(-1/4)`.               (3.4)

This applies to the indefinite majority-pivot case as well as the definite case; only rank two and (3.2) matter.

### A concrete diffuse-residual closure

If every residual row leverage satisfies

`max_j ||u_j||^2 <= 1/8`,                                                (3.5)

then a Bernoulli partition gives (3.2) with `alpha=1/4`. Indeed, for

`D_0=sum_j (epsilon_j-1/2)u_j u_j^T`,

`E ||D_0||_F^2 = (1/4) sum_j ||u_j||^4 <= (1/4)(1/8) sum_j||u_j||^2 = 1/16`,

because the total leverage of a two-frame is `2`. Hence some partition has `||D_0||_op<=1/4`, so both covariance halves are at least `I_2/4`.

Consequently

`||p_Q||_infinity <= 16 sqrt(3) (|a| c |det Lambda|)^(-1/4)`.            (3.6)

For example, in the localized rank-three branch `c>1/2`, `|det Lambda|>=1`, and a non-near-isotropic pivot `|a|>=1/2`, (3.6) gives the explicit universal bound

`||p_Q||_infinity <= 16 sqrt(6)`.                                        (3.7)

Thus the current pure-rank-three obstruction narrows further: a majority-sign pivot is no longer difficult merely because its residual is indefinite. If its rank-two residual frame is diffuse and the pivot is quantitatively away from zero, it is closed. The remaining pure-rank-three debt is concentrated residual leverage and/or a near-isotropic pivot, exactly where the known cross-energy lower bound must be aggregated without selecting a tiny physical minor.

## 4. The generic three-coordinate Schur residual is closed by recursive coarea + HLS

This section directly pays the missing implication stated in the completed `account02/B05` report.

Let a nonsingular physical principal block be

`B=[[a,d,e],[d,b,f],[e,f,c]]`,

and suppose `a!=0`. After conditioning on all outside coordinates, an affine term in the selected three variables is removed by the coordinatewise translation `(1/2)B^{-1} ell`, preserving independence and all density caps. Completing the square in the first coordinate gives

`x^T B x`

` = a (x+(d/a)y+(e/a)z)^2 + beta y^2 + 2 gamma yz + delta z^2`,           (4.1)

where

`beta=b-d^2/a`, `gamma=f-de/a`, `delta=c-e^2/a`,

and

`det B = a (beta delta-gamma^2)`.                                        (4.2)

Because `B` is nonsingular, the binary Schur complement is nonsingular.

### Lemma 4.1 — square laws in `L^(4/3)`

If `Z` has density bounded by one and `kappa!=0`, then

`||p_{kappa Z^2}||_(4/3) <= (3^(3/4)/sqrt(2)) |kappa|^(-1/4)`.           (4.3)

Proof. Put `h(r)=f_Z(r)+f_Z(-r)` on `r>0`. Then `0<=h<=2`, `int h=1`, and

`p_{Z^2}(y)=h(sqrt y)/(2 sqrt y)`.

For `1<q<2`,

`||p_{Z^2}||_q^q=2^(1-q) int_0^infinity h(r)^q r^(1-q) dr`.

By rearrangement/bathtub, the right side is maximized by `h=2 1_[0,1/2]`, giving

`||p_{Z^2}||_q^q <= 2^(q-1)/(2-q)`.

At `q=4/3` this is `3*2^(-2/3)`, and scaling by `kappa` gives (4.3). QED.

### Theorem 4.2 — `QFORM-GENERIC-SCHUR-HLS-v1`

Assume `beta!=0` in (4.1), and put

`kappa=delta-gamma^2/beta=(beta delta-gamma^2)/beta`.

Let `C_HLS` denote any valid one-dimensional Hardy--Littlewood--Sobolev constant for

`|| |.|^(-1/2) * g ||_4 <= C_HLS ||g||_(4/3)`.                          (4.4)

Then the full conditioned three-coordinate form, and hence the original form after mixing over outside coordinates, satisfies

`||p_Q||_infinity`

` <= 6*2^(1/6) C_HLS^(2/3)
       |a|^(-1/2) |beta|^(-1/3) |kappa|^(-1/6)`                         (4.5)

` = 6*2^(1/6) C_HLS^(2/3)
       [ |a| |ab-d^2| |det B| ]^(-1/6)`.                                (4.6)

Proof. Rewrite the residual as

`R=beta (Y+(gamma/beta)Z)^2 + kappa Z^2`.

Apply the peer coarea lemma *again*, now conditioning on the original coordinate `Z`. The translated variable `Y+(gamma/beta)Z` need not be independent of `Z`; conditional on `Z=z` it is merely a translate of the original `Y` density and therefore still has density at most one. Consequently

`p_R(s) <= |beta|^(-1/2)
            int |s-u|^(-1/2) p_{kappa Z^2}(u) du`.

By (4.3)-(4.4),

`||p_R||_4 <= C_HLS (3^(3/4)/sqrt(2))
               |beta|^(-1/2)|kappa|^(-1/4)`.                            (4.7)

Apply the outer peer coarea lemma with its `p=4` estimate. Since `C_4=6^(3/4)`,

`||p_Q||_infinity
 <= |a|^(-1/2) 2 (C_4 ||p_R||_4)^(2/3)`,

which simplifies to (4.5). Using (4.2) and `beta=(ab-d^2)/a` gives (4.6). No shear is interpreted as an independence-preserving change of variables; the only shifts are inside conditional one-coordinate laws. QED.

### The zero-Schur-diagonal branch has an elementary sharper bound

If `beta=0`, nonsingularity forces `gamma!=0`, while `delta` is arbitrary. Then

`R=2 gamma YZ + delta Z^2`.

Condition on `Z=z`. The conditional density of `R` is a probability density capped by

`M_z=(2|gamma z|)^(-1)`.

For any probability density `h<=M`, the bathtub principle gives

`sup_t int |t-s|^(-1/2) h(s) ds <= 2 sqrt(2M)`.

Hence, conditionally on `Z=z`, the half-Riesz potential is at most

`2/sqrt(|gamma z|)`.

For every density `f_Z<=1`, another bathtub bound gives

`E |Z|^(-1/2) <= int_{-1/2}^{1/2}|z|^(-1/2)dz = 2 sqrt(2)`.

Therefore

`||p_Q||_infinity <= 4 sqrt(2) / sqrt(|a gamma|)`.                       (4.8)

This improves the constant in the former exact-product residual branch and, importantly, permits arbitrary `delta`; thus *every* nonsingular binary Schur residual following a nonzero physical diagonal pivot is now closed quantitatively.

If a nonsingular `3x3` block has all three diagonal entries zero, the existing zero-diagonal-pair theorem applies instead. Thus the former `account02/B05` “generic localized Schur-residual” gap is no longer an independent local obstruction.

The classical Hardy--Littlewood--Sobolev theorem used in (4.4) is the one-dimensional fractional-integration mapping `I_(1/2):L^(4/3)(R)->L^4(R)`. Only finiteness of its universal constant is needed here.

## 5. What remains unpaid

These results do **not** prove the full owner target. They expose the next missing factor more sharply.

1. A fixed nonsingular physical `3x3` block is qualitatively bounded by earlier work, and Section 4 now gives a direct product-aware coarea proof through every binary Schur signature. But the global hypothesis “three eigenvalues of `A` have modulus at least one” does not force one physical `3x3` principal block with a dimension-free lower bound on the flag quantity in (4.6).

2. In exact rank three, Section 3 closes the localized-pivot branch whenever the residual rank-two spectral frame admits a quantitatively balanced original-coordinate partition. The first remaining pure-rank-three implication is therefore:

   **`QFORM-RANK2-RESIDUAL-LOCALIZED-AGGREGATION-v1` (OPEN):** when a heavy original row is chosen and the resulting indefinite rank-two residual frame itself has a row of leverage `>1/8` (or the outer pivot is near isotropic), aggregate its distributed cross energy / physical minors into either a balanced rank-two cross block or a product-aware coarea estimate without paying the smallest individual coordinate minor.

3. Even after exact rank three is closed, arbitrary additional small spectral directions remain a separate interaction/truncation debt. The separable-phase diffuse theorem handles coordinate-separable perturbations but not a general nonseparable spectral remainder.

So the precise remaining difficulty is no longer “generic binary Schur coarea.” It is **minor/partition aggregation under localization**, followed by the independent extra-spectrum interaction problem.

## 6. Status

**Proved in this run:**

- `QFORM-OUTER-SQUARE-RANK2-CROSSBLOCK-v1`, bound `8 sqrt(3)|a|^(-1/2)Delta^(-1/4)`;
- the residual-frame diffuse specialization (3.6), including the explicit `16 sqrt(6)` closure under `c>1/2`, `|a|>=1/2`, `max residual leverage<=1/8`;
- `QFORM-GENERIC-SCHUR-HLS-v1`, closing every nonsingular nonzero-diagonal binary Schur residual after a physical pivot;
- the sharper zero-Schur-diagonal estimate (4.8).

**Not proved:** the full universal theorem, the residual-localized aggregation implication, the arbitrary extra-spectrum interaction theorem, or universal continuity in the remaining branches.

**Assigned-partner status:** no completed current-QFORM `account04/B05` artifact was visible at final refresh, so no claim of applying it is made. Completed compatible `account02/B05` coarea mathematics and the current cross-block theorem were applied line-by-line.
