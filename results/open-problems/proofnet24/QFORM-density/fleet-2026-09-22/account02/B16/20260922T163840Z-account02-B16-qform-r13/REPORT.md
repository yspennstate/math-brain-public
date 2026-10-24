# account02/B16 — heavy-row projected rank-two half-Riesz theorem

**Run:** `20260922T163840Z-account02-B16-qform-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`; publication owner control revision `2026-09-22.7`  
**Assignment:** Projection-product interaction  
**Classification:** `PROVED SUPPORTING THEOREM / PROJECTION-TO-CURVED-PUSHFORWARD BRIDGE / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and first unpaid implication

The full target remains OPEN: for every dimension, independent real coordinates with densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal finite bound for the density of `X^T A X`, or construct a target-level counterexample.

The fresh owner proof-first control asks for a translation-uniform fractional-trace synthesis and, specifically, a rank-two half-Riesz theorem that survives arbitrary projection orientation without pretending projected coordinates are independent. This report proves such a theorem in the **heavy-row** branch of a rank-two projection.

The proof respects the live corrections: no independence after spectral rotation; no receiver-only bounded projection density is substituted for curved integration; no conditional cap is inferred after a sum/difference transform; no fiberwise indefinite trace bound is used; and no single uniformly good physical minor is assumed.

Completed designated partner actually applied: account03/B16 run `20260922T150329Z-account03-B16-qform-r12`, `yspennstate/math-open-problems@aee79a848b8d1a5ee1187ce01056b31de32f9505`, report blob `23cee7df2597df3700859473cc51de2b809b477f`. Its conditional-product `L^3` theorem and `L^3`-to-square smoothing theorem are used in Section 6 below for the heavy null-row specialization.

Additional completed dependency actually applied: account01/B16 run `account01-B16-20260922T161036Z-r11`, `yspennstate/math-open-problems@40b2fb6ac12a8860860b157327f98f90ecd48a34`, report blob `fa3139413a09562d7c89cd76e76e4f517f137a48`. It records the source-transferred one-dimensional Rudelson--Vershynin projection bound: a normalized linear form in independent cap-one inputs has density at most `sqrt(2)`, and it proves the translated independent-bank square smoother.

The binary curved estimate extended below is the prior account02/B16 theorem `QFORM-INDEFINITE-BINARY-FROSTMAN-v1`, canonical report `yspennstate/math-open-problems@85c527c3172670ca9e6200138e1364be554413ac`, blob `e919e8c6811b687ad32a6e73a7c32962248ccac0`.

## 2. Triangular conditional Frostman theorem

The previous binary theorem assumed independent inputs, but its proof only spends a conditional cap on the sliced coordinate and a marginal cap on the slicing coordinate. Independence is not needed once those two source-valid properties are stated explicitly.

### Theorem 2.1 — `QFORM-TRIANGULAR-INDEFINITE-FROSTMAN-v1`

Let `(U,W)` be a real random pair such that

- `W` has a density bounded by `K_2`;
- for almost every `w`, the conditional law `U | W=w` has a density bounded by `K_1`.

Let

`R=aU^2+2eUW+fW^2+ell_1 U+ell_2 W+ell_0`

have nondegenerate indefinite quadratic part

`D=af-e^2<0`, `d=|D|`.

For every interval `I` of length `h>0`,

`P(R in I) <= Psi( 2 sqrt(5) K_1 K_2 h / sqrt(d) )`,             (2.1)

where `Psi(x)=x(1+log(1/x))` for `0<x<1` and `Psi(x)=1` for `x>=1`.

Consequently, with

`M_* = 3 e^(-2/3) (2 sqrt(5))^(2/3)`,

`P(R in I) <= M_* (K_1 K_2 h/sqrt(d))^(2/3)`,                    (2.2)

and the inverse-square-root potential obeys

`boxed(
 sup_t E |t-R|^(-1/2)
 <= C_ind sqrt(K_1 K_2) d^(-1/4),
)`                                                               (2.3)

where

`C_ind = 8*3^(3/4)*5^(1/4)/sqrt(e)
       = 16.539645166123265... .`

### Proof

Apply deterministic translations of `U,W` to remove the two linear terms; these translations preserve the marginal and conditional density caps. Then set

`U'=K_1 U`, `W'=K_2 W`.

The density of `W'` is at most one, and for almost every `w'` the conditional density of `U' | W'=w'` is at most one. In `(U',W')` variables, the determinant of the quadratic part is

`D' = D/(K_1^2 K_2^2)`.

Now repeat the physical-slice proof of `QFORM-INDEFINITE-BINARY-FROSTMAN-v1`. For fixed `W'=w`, only the cap-one conditional density of `U'|W'=w` is used to dominate the admissible one-dimensional quadratic sublevel length. The final layer-cake integration uses only the cap-one marginal density of `W'` and its probability normalization. The original proof nowhere needs the conditional density to be independent of `w`. Thus its exact bound applies with `d'=d/(K_1^2K_2^2)`, giving (2.1) and (2.2).

The same layer-cake integration against `|t-r|^(-1/2)` as in the prior theorem gives (2.3). QED.

This is deliberately a **triangular** condition, not a claim that arbitrary projected coordinates have bounded conditional densities.

## 3. Rank-two projection geometry with one physical row retained

Let `u,v in R^n` be orthonormal and set the physical row vectors

`b_j=(u_j,v_j) in R^2`, `j=1,...,n`.

Then

`sum_j b_j b_j^T = I_2`.                                        (3.1)

Let `X_1,...,X_n` be independent with densities bounded by one, fix any translation `theta in R^2`, and define the rank-two projection

`Y = theta + sum_j b_j X_j`.                                     (3.2)

Choose an index `i` with

`b=b_i !=0`, `r=|b|`, `ell_i=r^2`.

Set

`Z=theta+sum_{j!=i} b_j X_j`.

Choose the deterministic vector

`c=(-b_2,b_1)/r^2`,

so `det(b,c)=1`. Define

`W=det(b,Z)`.

There is a unique scalar `s=s(Z)` such that

`Z=s b+W c`.

With

`U=X_i+s(Z)`,                                                    (3.3)

we have the exact identity

`Y=bU+cW`.                                                       (3.4)

### Product provenance that survives this change

Because `X_i` is independent of `Z`, conditional on the full `Z` the variable `U` is merely a translate of `X_i`. Therefore, after conditioning only on the coarser variable `W`, `U|W=w` is a mixture of translates of `X_i`, and hence

`||p_{U|W=w}||_infinity <=1`                                    (3.5)

for almost every `w`.

On the other hand,

`W = det(b,theta)+sum_{j!=i} det(b,b_j) X_j`.                    (3.6)

The coefficient vector in (3.6) has an exact norm identity. Let `Jb` be a quarter-turn of `b`. By (3.1),

`sum_{j!=i} det(b,b_j)^2
 = sum_j <Jb,b_j>^2
 = (Jb)^T [sum_j b_j b_j^T] (Jb)
 = |b|^2
 = r^2`.                                                        (3.7)

(The omitted `j=i` term is zero.) Therefore `W/r`, up to a translation, is a normalized one-dimensional linear projection of independent cap-one inputs. Applying the completed projection theorem used by account01/B16,

`boxed( ||p_W||_infinity <= sqrt(2)/r. )`                         (3.8)

Equations (3.5) and (3.8) are the correct source-valid replacement for a false claim of independence of the two projected coordinates.

## 4. Curved quadratic pushforward: the heavy-row half-Riesz theorem

Let `S` be any real symmetric invertible **indefinite** `2x2` matrix. Consider

`R=Y^T S Y`,                                                     (4.1)

or more generally add arbitrary affine terms in `Y`; the theorem below is unchanged.

In the `(U,W)` coordinates (3.4), the quadratic matrix is

`G=[b,c]^T S [b,c]`.

Because `det[b,c]=1`,

`det G = det S`.                                                 (4.2)

Thus the nonlinear change retains the exact indefinite determinant; no small determinant is introduced by the row extraction.

### Theorem 4.1 — `QFORM-HEAVY-ROW-PROJECTED-RANK2-RIESZ-v1`

Under the setup above,

`boxed(
 sup_t E |t-Y^T S Y|^(-1/2)
 <= 2^(1/4) C_ind r^(-1/2) |det S|^(-1/4).
)`                                                               (4.3)

Equivalently, in terms of physical leverage `ell_i=r^2`,

`sup_t E |t-Y^T S Y|^(-1/2)
 <= 2^(1/4) C_ind ell_i^(-1/4)|det S|^(-1/4).`                   (4.4)

The bound is uniform in `n`, all input laws, the translation `theta`, and arbitrary affine perturbations of the projected quadratic polynomial.

### Proof

Apply Theorem 2.1 to the exact binary representation (3.4). By (3.5), use `K_1=1`; by (3.8), use `K_2=sqrt(2)/r`; and by (4.2), use `d=|det S|`. Then

`sqrt(K_1K_2)=(sqrt(2)/r)^(1/2)=2^(1/4)r^(-1/2)`,

which gives (4.3). QED.

This is a direct quantitative bridge from bounded-density product structure through a low-dimensional projection to an **indefinite curved quadratic pushforward**. The projected pair is not asserted to be independent.

### Numerical heavy threshold

If `ell_i>=eta>0`,

`sup_t E |t-Y^T S Y|^(-1/2)
 <= 2^(1/4)C_ind eta^(-1/4)|det S|^(-1/4).`                      (4.5)

At the live ridge threshold `eta=1/32`,

`boxed(
 sup_t E |t-Y^T S Y|^(-1/2)
 <= 46.78118102154024 |det S|^(-1/4).
)`                                                               (4.6)

So the rank-two half-Riesz debt is dimension-free throughout this high-leverage branch.

## 5. Translation-dependent independent square bank

The completed account01/B16 translated-bank square smoother says that if `L` is independent of all variables determining `R`, has density cap `K_3`, and its translation may depend arbitrarily on those variables, then

`Q=R+gamma[L+s]^2`

satisfies

`||p_Q||_infinity
 <= K_3 |gamma|^(-1/2) sup_t E|t-R|^(-1/2).`                     (5.1)

If `L` is a normalized linear form on a disjoint original-coordinate bank, the same projection theorem gives `K_3<=sqrt(2)`. Combining (4.4) and (5.1),

`boxed(
 ||p_Q||_infinity
 <= 2^(3/4) C_ind ell_i^(-1/4)
    |gamma|^(-1/2)|det S|^(-1/4).
)`                                                               (5.2)

At `ell_i>=1/32`,

`||p_Q||_infinity
 <=66.15858066449306
   |gamma|^(-1/2)|det S|^(-1/4).`                                (5.3)

Thus account01/B16's disjoint-bank mechanism no longer requires the indefinite base itself to consist of two original physical coordinates: it can be an arbitrary rank-two spectral projection provided one physical row of that projection is heavy.

## 6. Sharper application of the designated account03/B16 theorem on a null heavy row

The designated partner result gives a sharper endpoint when the retained physical row is null for the indefinite form:

`a:=b^T S b=0`.                                                  (6.1)

Writing

`[b,c]^T S[b,c] = [[0,e],[e,f]]`,

(4.2) implies

`e^2=|det S|`.                                                   (6.2)

Hence, up to affine terms,

`R=2e W [U+(f/(2e))W]`.                                         (6.3)

Put `K=sqrt(2)/r`, so the density of `KW` is at most one. Conditional on `W` (equivalently on `KW`), the second factor in (6.3) is a translate of `U` and has conditional density at most one by (3.5). Applying account03/B16's completed `QFORM-CONDITIONAL-PRODUCT-L3-v1` after this scaling gives

`||p_R||_3
 <=3 K^(2/3)|det S|^(-1/3)
 =3*2^(1/3) r^(-2/3)|det S|^(-1/3).`                             (6.4)

Now apply that same partner report's `QFORM-L3-DEPENDENT-SQUARE-SMOOTHING-v1`. Whenever a final square variable has conditional density cap one given `R` (in particular an independent cap-one original coordinate with an arbitrary base-dependent translation),

`boxed(
 ||p_{R+gamma V^2}||_infinity
 <=8*2^(1/4) r^(-1/2)
   |gamma|^(-1/2)|det S|^(-1/4).
)`                                                               (6.5)

At `ell_i=r^2>=1/32`, this becomes

`boxed(
 ||p_{R+gamma V^2}||_infinity
 <=16 sqrt(2)
   |gamma|^(-1/2)|det S|^(-1/4)
 =22.62741699796952... |gamma|^(-1/2)|det S|^(-1/4).
)`                                                               (6.6)

This is the direct same-run application of the designated account03/B16 result.

## 7. What this does and does not close

The theorem closes a genuine part of the proof-first residual: an arbitrary-orientation rank-two indefinite projection with one physical row of leverage at least a fixed `eta` has a dimension-free, translation-uniform half-Riesz bound. It then yields an `L^infinity` quadratic-form density bound if a final square comes from a genuinely independent original-coordinate innovation bank. The null-row subbranch has the sharper partner-derived constant (6.6).

It does **not** solve the full QFORM theorem. The principal remaining obstruction is now more precise:

1. **overlapping innovation:** in a generic rank-three spectral frame the third square direction may use the same physical coordinates as the rank-two residual, so the conditional density cap needed in (5.1)/(6.5) is not automatic;
2. **low rank-two leverage:** if every physical row in the chosen rank-two residual is small, this theorem loses `ell_i^(-1/4)`. The separate ridge-window theorem controls an important low-leverage full-spectral branch, but an exhaustive bridge with arbitrary additional spectral components is not yet proved;
3. account03/B06's newest heavy-isotropic exact-rank-three frontier is therefore not automatically closed by (6.6): its final square can be correlated with the rank-two residual rather than supplied by a disjoint innovation.

The next exact implication is an **overlap-safe square smoother** or innovation-extraction theorem: retain the triangular source provenance above while allowing the final rank-one spectral direction to overlap the same original coordinates, without replacing the true conditional law by a false uniform cap.

No continuity claim, full-solution claim, or target-level counterexample is made.

## 8. Diagnostic check

`CHECK.py` verifies on 1000 deterministic-seed random frames/matrices that

- the extracted basis preserves `det S`;
- the wedge coefficient identity (3.7) holds;
- the exact quadratic identity `Y=bU+cW` reproduces `Y^T S Y`;
- all displayed constants are numerically consistent.

`CHECK_OUTPUT.txt` reports `PASS`; the largest observed floating residual is below `4.3e-14`. This diagnostic is not a proof certificate; the proof is the symbolic argument above.

## 9. Status

- `QFORM-TRIANGULAR-INDEFINITE-FROSTMAN-v1`: **PROVED**.
- `QFORM-HEAVY-ROW-PROJECTED-RANK2-RIESZ-v1`: **PROVED supporting theorem**.
- high-leverage translated independent-square corollary: **PROVED in its stated disjoint-innovation scope**.
- designated-partner null-row specialization: **PROVED**, by direct application of account03/B16 r12.
- full universal QFORM theorem: **OPEN / NOT PROVED**.
