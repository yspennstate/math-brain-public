# account01/B12 — independent nine-direction review and multiplicity-eight transverse reserve

Run: `20260924T144749Z-account01-B12-FIXMULT-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Status: **(i) independent PASS reconstruction of the complete nine-eigenvalue theorem; (ii) new deterministic two-transverse-mode theorem and a much stronger fixed-anchor overlap-one identity at the unresolved multiplicity-eight endpoint. Multiplicity eight remains OPEN. The unrestricted three-eigenvalue conjecture remains OPEN.**

## 1. Independent review of the complete nine-eigenvalue theorem

After completing my own full 790-line baseline audit, I independently reconstructed the later grouped product-Fourier replacement proof. My verdict is **PASS** for the theorem

> If the independent real coordinates have densities bounded by `K`, `A=A^T` is arbitrary, `b,c` are arbitrary, and `s_9(A)>=s>0`, then `Q=X^TAX+b^TX+c` has an essentially bounded density satisfying
> 
> `||p_Q||_infinity <= (2010+1200 log 16) K^2/s < 5338 K^2/s`.

The no-pivot Fourier branch has a continuous `C_0` representative. Global continuity is not asserted by the pivot branches.

### 1.1 Grouped compiler check

For disjoint original-coordinate banks `H,I,J`, the proof pushes the phase-weighted `H`-law through a `k`-dimensional orthogonal projection and uses only the resulting density cap and its `L^2` norm. On the light bank it conditions on the original `I` coordinates, regularizes the complex pushforward through the `J`-linear map, expands its squared `L^2` norm with an independent `J` copy, and averages the original independent `I` coordinates **before** taking the determinant/Hölder bound. This preserves the physical product characteristic factors. No projected-coordinate independence is used.

For an `ell`-subset `T` of residual physical rows, the joint coefficient map has Gram determinant

`S^2 det(C_T C_T^T)`.

The product-projection theorem therefore gives exactly the required density Jacobian. Weighted Hölder uses exponents `1/alpha_i>=2`; the scalar Fourier-power lemma applies at precisely those exponents. The determinant geometric mean is paid by the entropy identity

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.

I re-derived the ordered-subset entropy proof. The resulting characteristic-function envelope has exponent `(k+ell)/2` with the stated constants.

### 1.2 Promotion trees check

For a literal physical crossing, heavy determinant marginals are promoted as literal original-coordinate hub rows. Exact coefficient-space Gram--Schmidt gives the identities

`||w||^2 E_2(C)=J_i`

at order three and

`||w||^2 E_1(C)=J_i`

at order two. Repeating once more terminates in exact physical rank three or rank two. Same-bank quadratic and affine phases remain in the complex pushforwards. Hence:

- order three gives a marginal-free bounded-density receiver
  `||p||_infinity <= C_3 E_3(M)^(-1/6)`,
  `C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`;
- order two gives the full half-potential receiver
  `sup_a E|Q-a|^(-1/2) <= C_2 E_2(M)^(-1/8)`,
  `C_2=8 sqrt(e) 2^(-1/8)=12.095072570796...`.

The order-two statement is correctly used only as a half-potential endpoint.

### 1.3 Assembly check

Normalize `K=s=1`.

- No pivot: the audited baseline order-three spectral-to-volume theorem requires exactly `s_9(A)>=1`, gives `V_3>=kappa^3`, and a fair physical cut gives `E_3>=4^-3 kappa^3`. The order-three receiver yields `<2371`.
- Scalar pivot: one Schur loss leaves at least eight unit-scale directions. If the remainder has a pivot, the sharpened baseline half-potential is at most `201+120 log16`; if it has no pivot, five remaining directions feed the order-two full half-potential receiver and give `<153`. The outer scalar square profile therefore yields `2010+1200 log16 <5338`.
- Definite pair: `<10pi`.
- Indefinite pair: at least one Schur direction remains and the audited hyperbolic/logarithmic branch stays `<251`.

Scaling `Y=KX`, `A -> A/s` gives exactly `K^2/s`.

Thus the complete replacement is a genuine **17 -> 9** improvement with the full arbitrary-law, arbitrary-dimension, arbitrary-sign and arbitrary-affine scope.

## 2. Review-gate evidence

I directly read two genuinely separate complete PASS reconstructions already on `master`:

1. `improvements/account01/B16/20260924T124038Z-r11/REPORT.md`, which independently reconstructs the grouped compiler, both promotion trees and the full nine-direction assembly.
2. `improvements/account01/B07/20260924T133059Z-account01-B07-fixedmult-audit-r12/NINE_EIGENVALUE_FULL_REVIEW.md`, which explicitly performs a separate full reconstruction and records PASS.

Therefore the owner's **two-separate-end-to-end-review mathematical gate has repository evidence satisfying it** for the nine-direction theorem. I do not mutate or self-award any owner-level validation, release or publication flag.

The scalar-pivot sector is already known to close under only `s_6(A)>=s` if an original-coordinate scalar pivot exists; hence the remaining threshold obstruction at eight is entirely in the no-pivot geometry.

## 3. New theorem: robust pair forces two transverse outside modes

The freshest multiplicity-eight collar reduction provides a literal pair `H={h_1,h_2}` for which

`C=A[H,H^c]`

has row rank two and, in the terminal normalized branch,

`D_H:=det(CC^T)>=D_0=0.3649442658827020...`.

The next statement is deterministic and in fact needs only `rank C=2` and the spectral hypothesis.

### Theorem `QFORM-S8-ROBUST-PAIR-TWO-TRANSVERSE-MODES-v1`

Let `A=A^T`, let `H` be any two-set, and write

`A = [[K,C],[C^T,B]]`

relative to `H union H^c`. If `s_8(A)>=s>0`, then

`boxed: s_4(B)>=s.`                                             (3.1)

If `C` has row rank two and

`P_C=C^T(CC^T)^(-1)C`

is the orthogonal projection in `R^(H^c)` onto the row space of `C`, then

`boxed: s_2(B(I-P_C))>=s,`                                      (3.2)

and hence

`boxed: ||B(I-P_C)||_F^2>=2s^2.`                               (3.3)

#### Proof

Let

`A_0=diag(0_H,B)`.

Then

`A-A_0=[[K,C],[C^T,0]]`

is the sum of

`[[K,C],[0,0]]`

and

`[[0,0],[C^T,0]]`.

The first has rank at most two because only the two `H` rows are nonzero; the second has rank at most two because only the two `H` columns are nonzero. Thus

`rank(A-A_0)<=4`.

The audited rank-perturbation lemma gives

`s_8(A)<=s_4(A_0)=s_4(B)`,

which proves (3.1).

Next `rank(BP_C)<=rank P_C=2` and

`B=B(I-P_C)+BP_C`.

Applying the same rank-perturbation lemma with rank loss two gives

`s_4(B)<=s_2(B(I-P_C))`,

proving (3.2). At least two singular values of `B(I-P_C)` are therefore at least `s`, which gives (3.3). QED.

### Interpretation

The unresolved `s_8` robust-pair collar does **not** consist merely of a two-dimensional random slope with a potentially singular two-by-two self-block. The outside principal matrix has at least four unit spectral directions, and after deleting the entire two-dimensional coefficient row space already consumed by the robust pair, **two unit transverse singular modes necessarily survive**.

This is exactly the deterministic reserve one would want for a `(k,ell)=(2,1)` grouped Fourier receiver. What is still missing is a product-preserving conversion of this global transverse reserve into a literal physical split while retaining the robust pair's two-dimensional slope.

## 4. Exact fixed-anchor overlap-one identity

The same theorem yields a quantitatively much stronger version of the overlap-one currency in the terminal `s_8` collar.

Keep a rank-two pair `H` and define, for every `i in H^c`, the three-row matrix

`M_i = A[H union {i}, H^c]`.

Write `b_i` for row `i` of `B`. By the Gram determinant / Schur-complement identity,

`det(M_i M_i^T)
 = det(CC^T) ||b_i(I-P_C)||^2
 = D_H ||b_i(I-P_C)||^2.`                                      (4.1)

Cauchy--Binet gives

`det(M_iM_i^T)=sum_{U subset H^c, |U|=3} det A[H union {i},U]^2.`

Summing in `i` therefore gives the exact identity

`boxed:
 sum_i sum_{|U|=3} det A[H union {i},U]^2
 = D_H ||B(I-P_C)||_F^2.`                                      (4.2)

Split the right-hand Cauchy--Binet sum according to whether `i in U`. Define the fixed-anchor overlap-one mass

`Omega_H^(1)
 := sum_{i in H^c}
    sum_{U subset H^c, |U|=3, i in U}
       det A[H union {i},U]^2.`                                 (4.3)

The complementary terms `i notin U` are disjoint `3x3` minors, hence form a sub-sum of `V_3(A)`. Combining (3.3) and (4.2),

`boxed:
 Omega_H^(1) >= 2s^2 D_H - V_3(A).`                             (4.4)

This is exact except for the final omission of nonnegative disjoint minors.

### Terminal normalized consequence

In the only unpaid no-pivot multiplicity-eight collar, `s=1`, the robust-anchor theorem gives

`D_H>=D_0=0.3649442658827020...`,

while the already-paid alternative is `V_3>=kappa^3`; hence in the survivor we have `V_3<kappa^3`, `kappa=1/6400`. Therefore

`boxed:
 Omega_H^(1)
 > 2D_0-kappa^3
 > 0.729888531761.`                                             (4.5)

This is a dimension-free order-one amount of shared-anchor third-minor mass attached to **one literal physical pair H**. It is far stronger numerically than merely knowing a tiny aggregate overlap mass somewhere in the matrix.

The identity also explains why the ordinary disjoint order-three receiver can fail at eight: the transverse exterior mass can concentrate precisely in minors whose row and column triples share the coordinate `i`.

## 5. Fixed-anchor three-role entropy has no cardinality loss

For completeness, put determinant-squared probability weights on the nonzero packets `(i,U)` in (4.3), with `U={i,j,k}`. Independently order `j,k`. Let `alpha_l` be the expected number of appearances of physical coordinate `l` among the three roles `(i,j,k)`, so `sum_l alpha_l=3`. Entropy subadditivity and concavity, exactly as in the existing five-role theorem, give

`boxed:
 H(w)+sum_l alpha_l log alpha_l
 <=3 log3-log2=log(27/2).`                                      (5.1)

Thus neither packet cardinality nor Shannon entropy is an obstruction to aggregating the strong mass (4.5). The remaining obstruction is analytic: the shared coordinate `i` appears simultaneously as a physical row variable and a column variable, so it cannot simply be placed into two independent banks.

## 6. Precise remaining multiplicity-eight gap

The current endpoint can now be stated more sharply.

In the only unpaid normalized no-pivot `s_8` state, there is one literal pair `H` such that

- `det(A[H,H^c]A[H,H^c]^T)>=0.3649442658827020...`;
- the entire two-dimensional anchor self-block may be zero, rank one, or arbitrarily close to singular;
- `s_2(B(I-P_C))>=1` and `||B(I-P_C)||_F^2>=2`;
- the fixed-anchor overlap-one third-minor mass is `>0.729888531761`;
- packet entropy is dimension-free by (5.1);
- the robust two-anchor Plancherel estimate already gives every finite `L^r` norm and an `h log(1/h)` small-ball bound uniformly through `det K=0`.

What is **not** yet proved is the endpoint upgrade from this shared-coordinate structure to `L^infinity`. A complete `s_8` theorem needs a product-preserving shared-anchor receiver that consumes the overlap coordinate before destructive absolute values are taken, or an equivalent physical-split theorem that converts the two transverse modes in (3.2) into at least one additional independent smoothing channel while retaining a quantitative rank-two anchor slope.

A general orthogonal projection onto `row(C)^perp` is not enough: rotating the outside product coordinates destroys independence, so (3.2) cannot be fed directly into the grouped compiler.

Accordingly, **multiplicity nine is the lowest complete theorem established here; multiplicity eight remains open.**

## Dependency map

This improvement uses only:

- the independently audited baseline rank-perturbation lemma;
- the completed nine-direction grouped Fourier compiler and order-two/order-three promotion receivers;
- the existing robust-pair extraction at multiplicity eight for the numerical lower bound `D_0`;
- elementary Gram determinant, Cauchy--Binet and entropy identities for Sections 3–5.

No numerical experiment is used as proof. No matrix/input/affine hypothesis has been weakened.
