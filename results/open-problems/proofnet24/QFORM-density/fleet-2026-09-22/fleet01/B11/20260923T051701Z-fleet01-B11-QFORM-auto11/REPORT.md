SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-23T05:17:01Z.
attacking: opposite-sign pair plus an overlapping independent scalar bank: complete the scalar square first, then pay the exact rank-two Schur half-Riesz potential without rotating the product law.

# fleet01/B11 — cross-coupled scalar-bank Schur smoothing for indefinite signatures

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T051701Z-fleet01-B11-QFORM-auto11`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** essential boundedness only for the new theorem; continuity is not claimed.

## 1. Exact obligation and current boundary

The owner target remains the full arbitrary-dimensional statement: independent real inputs with density caps one, arbitrary symmetric `A` having at least three eigenvalues of modulus at least one, no moments, compact support, log-concavity, connected support, Gaussianity, or post-rotation independence.

B11 is responsible for the genuinely rotated indefinite signatures `(2,1)` and `(1,2)`, retaining the genuine rank-two opposite-sign logarithmic singularity and identifying how a third direction removes it.

The designated partner `fleet02/B11` most recently proved the disjoint-bank theorem

`||p_(P+dW^2+2rW+q)||inf <= 16 sqrt(30) L |det B|^(-1/4)|d|^(-1/2)`

when `P=U^T B U+ell^T U+c`, `U=(X1,X2)` are two independent cap-one variables, `W` is independent of them with density cap `L`, and `B` is invertible. Source:

`yspennstate/math-open-problems@f2835c54b9f384f8f83e34c46bef5c40953e32a7`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260923T042112Z-fleet02-B11-QFORM-2f47d35a/REPORT.md`.

Its explicit unpaid interface is the case where the scalar third direction has quadratic cross coupling with the opposite-sign pair. The present run pays that cross coupling exactly, without rotating the product law.

The key analytic dependency is the completed rank-two affine half-Riesz estimate

`sup_t E |U^T S U+b^T U-t|^(-1/2) <= 16 sqrt(30)|det S|^(-1/4)`      (1.1)

for two independent cap-one variables and every invertible symmetric `2x2` matrix `S`. It is the two-coordinate specialization of

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

The current pair-log theorem is also used below only at its proved scope:

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

No arbitrary-joint coarea estimate, conditional-density moment, post-rotation independence, or pointwise quadratic-phase decay is used.

## 2. Main theorem: cross-coupled scalar square plus a rank-two receiver

### Theorem 2.1 — `QFORM-CROSSCOUPLED-SCALAR-SCHUR-HALF-RIESZ-v1`

Let `U=(X1,X2)` consist of two independent real random variables with densities bounded by one. Let `W` be independent of `U` and have a density bounded by `L`. Let

`H = [[B,c],[c^T,d]]`,                                             (2.1)

where `B` is real symmetric `2x2`, `c in R^2`, `d!=0`, and `H` is invertible. For arbitrary `ell in R^2`, `r,q in R`, put

`Q = U^T B U + 2 W c^T U + d W^2 + ell^T U + 2rW + q`.            (2.2)

Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||inf
 <= 16 sqrt(30) L |d|^(-1/2) |det(B-cc^T/d)|^(-1/4)
 = 16 sqrt(30) L (|d| |det H|)^(-1/4).`                           (2.3)

If `W=sum_(j in J)b_j X_j` is a normalized linear form on a disjoint bank of original independent cap-one coordinates, `sum b_j^2=1`, then the sharp one-dimensional product-marginal estimate gives `L<=sqrt(2)`, hence

`boxed:
 ||p_Q||inf <= 16 sqrt(60) (|d| |det H|)^(-1/4).`                 (2.4)

The theorem allows arbitrary quadratic cross coupling `c` between the scalar bank and the pair. It does **not** require the scalar spectral eigenvector to be a physical coordinate axis. The only product requirement is that the scalar variable `W` itself be genuinely independent of the two receiver variables before the completion below.

### Proof

Condition on the original pair `U=u` and complete the square only in the independent scalar `W`:

`Q = d [ W + (c^T U+r)/d ]^2 + P(U)`,                             (2.5)

where

`P(U)=U^T S U + (ell-2rc/d)^T U + q-r^2/d`,

`S=B-cc^T/d`.                                                     (2.6)

Because `d!=0` and `H` is invertible, the scalar Schur determinant identity

`det H = d det S`                                                 (2.7)

shows that `S` is invertible.

The shift

`a(u)=(c^T u+r)/d`

depends on `u`; therefore `W+a(U)` is generally **not independent** of `U`. No such independence is asserted. What is retained exactly is the conditional law: because `W` was genuinely independent of `U`, conditional on `U=u` the variable `W+a(u)` has the translated density `w -> p_W(w-a(u))`, still bounded by `L`.

For fixed `u`, the pushforward of a density bounded by `L` under `z -> d z^2` has density bounded by

`L |d|^(-1/2) |y|^(-1/2)`                                       (2.8)

on the corresponding half-line. Indeed, for `d>0`,

`p_(dZ^2)(y)=[p_Z(sqrt(y/d))+p_Z(-sqrt(y/d))]/[2 sqrt(dy)]
             <= L/(sqrt(dy))`,

and reflection gives `d<0`.

Consequently Tonelli and the conditional density formula give, for almost every `t`,

`p_Q(t)
 <= L |d|^(-1/2) E |t-P(U)|^(-1/2).`                             (2.9)

The affine term in `P` is an arbitrary two-coordinate affine term, so (1.1) applies directly:

`sup_t E |t-P(U)|^(-1/2)
 <=16 sqrt(30)|det S|^(-1/4).`                                   (2.10)

Combining (2.9), (2.10), and (2.7) proves (2.3). The normalized-bank statement follows from `L<=sqrt(2)`. QED.

### Why the live conditional-cap correction is not violated

The live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` forbids replacing genuine independence by a bounded conditional density inside a hyperbolic three-variable argument. The proof above does something different: it starts with a genuinely independent scalar `W`, conditions only on the untouched product variables `U`, writes the **exact translated scalar law**, and uses its cap only inside the one-dimensional square pushforward. The shifted scalar is never declared independent of `U`, and no dependent pair is replaced by a product law.

## 3. Exact signature bookkeeping

Suppose `H` in (2.1) has inertia `(2,1)` and `d>0`. Haynsworth inertia additivity for a nonzero scalar pivot gives

`Inertia(H)=Inertia(d)+Inertia(S)`,                               (3.1)

so `S` has inertia `(1,1)`. Likewise, if `H` has inertia `(1,2)` and `d<0`, then `S` again has inertia `(1,1)`.

Thus a **majority-sign scalar pivot leaves an opposite-sign rank-two Schur receiver**. The receiver may genuinely have an unbounded logarithmic density. The third direction removes that singularity not by making the receiver density bounded, but by asking only for the receiver's finite half-order Riesz potential in (2.10).

This gives a precise sign-specific mechanism:

`rank-two saddle density ~ log(1/|t|)`

is not itself uniformly bounded, but

`sup_s E|P-s|^(-1/2) < infinity`,

and the scalar-square Jacobian contributes exactly the matching `|y|^(-1/2)` kernel. Their composition is bounded.

Reflection `H -> -H` exchanges `(2,1)` and `(1,2)` and preserves the estimate.

## 4. The mandatory rank-two logarithmic control

At the exact saddle endpoint

`B0=[[0,1],[1,0]]`

and for independent centered unit uniforms `X1,X2~Uniform[-1/2,1/2]`,

`P=2X1X2`

has density

`p_P(t)=log(1/(2|t|)),   0<|t|<1/2`.                              (4.1)

So the opposite-sign rank-two obstruction is genuine. Theorem 2.1 does not hide it. It identifies the extra square direction as the precise half-order smoother needed to integrate through that logarithmic critical value.

## 5. A genuinely rotated exact-target family and an actual partner inequality

For `0<=a<=1`, write

`sigma=sqrt(1-a^2)`

and define the reduced matrix

`H_a = [[-a,0,sigma],
       [0, 1, 0],
       [sigma,0,a]].`                                            (5.1)

The `2x2` `(1,3)` block squares to the identity, so exactly

`spec(H_a)={1,1,-1}`, `det H_a=-1`.                               (5.2)

For `m>=1`, let

`W_m=m^(-1/2) sum_(j=1)^m X_(j+2)`                               (5.3)

on a bank disjoint from `X1,X2`. If `T` has orthonormal columns `e1,e2,b_m`, then the ambient matrix

`A_(m,a)=T H_a T^T`                                               (5.4)

has the same three nonzero eigenvalues `{1,1,-1}`. Hence it lies exactly in the owner's target for every `m` and `a`, and for `0<a<1` it is genuinely rotated between the first coordinate and the diffuse bank.

The form is

`Q_(m,a)=-aX1^2+X2^2+2 sigma X1 W_m+aW_m^2`.                      (5.5)

### 5.1 Direct application of the new cross-coupled theorem

Treat `W_m` as the scalar in Theorem 2.1. Then `d=a`,

`B=diag(-a,1)`, `c=(sigma,0)^T`,

and

`S=B-cc^T/a=diag(-1/a,1)`, `det S=-1/a`.                          (5.6)

Since `||p_(W_m)||inf<=sqrt(2)`, (2.4) gives for every `a>0`

`||p_(Q_(m,a))||inf <=16 sqrt(60) a^(-1/4).`                     (5.7)

This is already independent of `m` and is a genuine cross-coupled application. It deteriorates only at the null scalar endpoint `a=0`; the next regrouping removes even that deterioration.

### 5.2 Designated partner fleet02/B11 applied to the same family

Use the sharp scalar projection cap and put

`Z_m=sqrt(2) W_m`.

Then `Z_m` has density at most one and is independent of `X1,X2`. Rewrite (5.5) by grouping the **opposite-sign pair** as `(X1,Z_m)` and leaving the third independent square `X2^2`:

`Q_(m,a) = (X1,Z_m) B_a (X1,Z_m)^T + X2^2`,                      (5.8)

where

`B_a=[[-a, sigma/sqrt(2)],
      [sigma/sqrt(2), a/2]]`.

Exactly

`det B_a=-1/2`                                                    (5.9)

for every `a in [0,1]`. Therefore the completed designated-partner theorem `QFORM-INDEFINITE-PAIR-DIFFUSE-SQUARE-v1`, with third-square density cap `L=1` and `d=1`, gives the actual inequality

`boxed:
 ||p_(Q_(m,a))||inf
 <=16 sqrt(30) (1/2)^(-1/4)
 =16 sqrt(30) 2^(1/4)
 <104.217`                                                        (5.10)

**uniformly in both `m` and `a`, including the null limit `a=0`.**

This is not a copied citation: the partner theorem is applied to the explicit matrix (5.8), and the determinant in its hypothesis is evaluated exactly in (5.9).

At `a=0`, the pair term is `2X1W_m`. For `m=1` and centered unit uniforms it has the logarithmic singularity (4.1), while the independent `X2^2` direction makes the complete output bounded by (5.10). This is a concrete target-valid realization of the requested `rank two log + third direction` mechanism.

## 6. Mandatory newest-Claude result applied at an actual inequality

The current required Claude package is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.

Its proved ruled Theorem C states that an exact rank-three `(2,1)` form with eigenvalue magnitudes at least one has

`p_Q(t)<=pi sqrt(2)`                                               (6.1)

on the majority-sign one-sheet side `t>=0`.

The family `A_(m,a)` has exact nonzero spectrum `{1,1,-1}`, so Theorem C applies directly:

`boxed: p_(Q_(m,a))(t) <= pi sqrt(2) <4.443,  t>=0.`              (6.2)

Combining (6.2) with (5.10) gives an explicit sign splice: the ruled geometry pays the one-sheet side sharply, while the partner half-Riesz/square mechanism pays the opposite two-sheet side (indeed, it pays all `t`). This keeps the two geometrically different sides separate instead of pretending a one-sheet estimate controls both.

## 7. A correction-safe three-physical-coordinate corollary

This section is not claimed as a new primary result—the newest Claude package already supplies a stronger localized three-coordinate theorem. It is recorded because it shows how the present Schur estimate and the pair-log theorem make a completely product-preserving fallback, without the refuted arbitrary-joint coarea lemma.

Let `Y1,Y2,Y3` be independent cap-one variables and let `H` be symmetric `3x3` with

`min_j |lambda_j(H)| >= s>0`.

Then for every affine perturbation,

`||p_(Y^T H Y+ell^T Y+q)||inf <104.217/s`.                       (7.1)

Indeed, if some diagonal `|h_ii|>=s/2`, Theorem 2.1 with that original scalar gives

`16 sqrt(30)[|h_ii||det H|]^(-1/4)
 <=16 sqrt(30)2^(1/4)s^(-1)
 =104.216889... s^(-1)`.                                         (7.2)

If all three diagonals have modulus `<s/2`, then

`sum_(i<j) h_ij^2
 =[||H||_F^2-sum_i h_ii^2]/2
 >9s^2/8`,                                                       (7.3)

so some pair has `|b|^2>=3s^2/8`. For that physical pair

`B=[[a,b],[b,c]]`, `|a|,|c|<s/2`,

one has

`D=|det B|=b^2-ac >=s^2/8`,                                      (7.4)

and, since the pair is indefinite,

`kappa=sigma_min(B)
 >= |b|-(|a|+|c|)/2
 >=( sqrt(3/8)-1/2 )s
 =((sqrt(6)-2)/4)s`.                                             (7.5)

The current pair-log theorem therefore gives

`||p||inf
 <=8sqrt(5)(D*kappa*s)^(-1/4)
 <51.962/s`,                                                      (7.6)

which is below (7.2).

Again, (7.1) is recorded as a transparent cross-check and a usable local compiler; the active full problem is not the existence of one well-conditioned physical triple, because current corrections contain explicit exact-rank-three families for which every such local triple degenerates with dimension.

## 8. What changed and what remains unpaid

The designated partner's disjoint-square theorem no longer needs the condition `c=0` when one has a genuinely independent scalar bank and the remainder after scalar Schur completion is an invertible rank-two receiver. The exact cross coupling is paid by (2.3). In signatures `(2,1)` and `(1,2)`, a majority-sign scalar pivot produces exactly the opposite-sign rank-two Schur form, so the theorem directly addresses the two-sheet/logarithmic side.

The concrete family (5.1)--(5.5) also shows a second useful mechanism: if one scalar coefficient approaches zero, regrouping the three independent physical aggregates can move the cross coupling **inside the indefinite pair**, after which the designated partner theorem gives the uniform bound (5.10). Thus an apparent near-null scalar singularity can be an artifact of the chosen completion order.

The first B11 implication still unpaid is now:

**`QFORM-PRODUCT-PRESERVING-SCALAR-BANK-EXTRACTION-v1`.** In the general no-pivot/high-leverage indefinite chamber, prove that one can either

1. extract a disjoint original-coordinate bank whose contribution to the active rank-three block is through a single scalar projection `W`, with all induced bank-linear terms aligned so that Theorem 2.1 applies and with a dimension-free Schur determinant certificate; or
2. regroup the active variables so that the designated partner pair-plus-square theorem applies as in Section 5; or
3. force one of the already-paid ruled, volume-stability, physical-pair, ridge, or finite-ray exits.

The important remaining obstruction is **not** quadratic cross coupling with an independent scalar—it is now paid. The obstruction is obtaining that scalar product provenance from an arbitrary rotated frame while retaining all light rows and arbitrary extra spectrum. If a many-coordinate bank enters through several linearly independent statistics, conditioning on the other bank statistics can make the scalar conditional density arbitrarily large; the live conditional-cap corrections forbid pretending otherwise. Likewise, small coefficients cannot be discarded on arbitrary unbounded supports.

This is also where the previous null-arc high-leverage/bank-coloop problem meets the present theorem: a successful exact one-scalar bank extraction would feed directly into (2.3); failure of such extraction must itself provide the geometric volume/pair certificate.

## 9. Verification

`VERIFY.py` and `VERIFY_OUTPUT.txt` in this directory check symbolically:

- `charpoly(H_a)=(lambda-1)^2(lambda+1)` and `det H_a=-1`;
- the regrouped partner pair has `det B_a=-1/2` for every `a`;
- the direct scalar Schur complement is `diag(-1/a,1)` and satisfies `a det S=det H_a`;
- the `tau=1/2` local fallback constants in Section 7;
- the partner-family constant `16 sqrt(30)2^(1/4)=104.216889...`.

The captured execution ends

`QFORM_B11_CROSSCOUPLED_SCHUR_CHECK_PASS`.

These checks verify algebra and constants only; they are not independent mathematical review.

## 10. Status

- New supporting theorem: `QFORM-CROSSCOUPLED-SCALAR-SCHUR-HALF-RIESZ-v1` — proved above.
- Designated partner result: actually applied at (5.10).
- Mandatory newest-Claude theorem: actually applied at (6.2).
- Rank-two opposite-sign log singularity: retained explicitly in Section 4 and at the `a=0,m=1` endpoint.
- Continuity: not proved by the new theorem.
- Full QFORM conjecture: **OPEN**.
- Independent end-to-end review of this run: **not performed / not claimed**.
- Native brain ingestion: **WITHOUT_VERIFIED_BRAIN**.
