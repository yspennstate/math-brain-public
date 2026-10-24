# account03/B20 — pivot-Schur two-direction closure inside the low-stable-rank residual

Run: `20260922T141139Z-account03-B20-QFORM-r11`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Assignment: Proof closure and keeper / SYNTHESIS  
Status: `TARGET_LEVEL_BRANCH_PROVED / FULL_CONJECTURE_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not native learned-memory ingestion.

## 1. Exact target and fresh first unpaid implication

The owner target is unchanged: for every dimension, independent real coordinates with one-dimensional probability densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove one universal essential-supremum bound for the density of `Q=X^TAX`, or produce a target-valid counterexample. Continuity is tracked separately.

The freshest complete proof-assembly report consumed before this run is account03/B19, `QFORM-LOW-STABLERANK-OFFDIAGONAL-BRIDGE-v1`, source

`yspennstate/math-open-problems@6e3c22b4fcc1038ded1aeff8d107be6a76f7df17:proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260922T140323Z-account03-B19-QFORM-r11/REPORT.md`.

It proves a continuous density bound `<70` when the physical off-diagonal part `H=A-diag(A)` has sufficiently large stable rank, and leaves the residual state

`||H||op > 1/4`, `sr(H)<32`

for a product-preserving low-effective-rank bridge. The theorem below closes a genuine branch of this residual without assuming exact rank three and without discarding arbitrary additional spectral directions.

Corrections retained: no law-uniform pointwise quadratic-phase decay; no independence after spectral rotation; no generic fiber-supremum bound; no conditional density cap after sum/difference conditioning; no single-Schur rank-two extraction; no fixed principal-block-or-rank-three-cross-cut dichotomy; no absolute phase-Wiener criterion.

## 2. Source-pinned analytic inputs

### 2.1 Regularized determinant theorem

The complete supporting proof at

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a:proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`

proves, for every original-coordinate cut with cross block `B`, the fractional estimate

`|phi(t)| <= det(I + 2 q t^2 BB^T/(pi^2 e^2))^(-1/(4q))`

when `1<=q<2` and the coordinate leverage of `range(B)` on one physical side is at most `q/2`. Its MSS argument also proves that, if the **entire range frame** of a symmetric matrix has row leverage at most `1/32`, a two-part physical partition has both frame Gramians between `7I/32` and `25I/32`.

### 2.2 Dependent square smoothing from an L3 base density

The complete account01/B11 theorem at

`yspennstate/math-open-problems@2279571f59ade7a9ec478af1e4818f6c117ac224:proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/QFORM-B11-20260922T121344Z/REPORT.md`

proves: if `R` has density `p_R` with `||p_R||_3=M`, and conditionally on `R` a real variable `V` has density cap one, then for every `d!=0`,

`||p_{R+dV^2}||infinity <= 4 |d|^(-1/2) M^(3/4)`.

### 2.3 Assigned partner account04/B20

The completed designated-partner report

`yspennstate/math-open-problems@1f85677029fc5ae27fc69b278620ae89d789efd2:proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260922T132134Z-account04-B20-QFORM-r1/REPORT.md`

proves the disjoint-aggregate hyperbolic-square theorem

`||p_T||infinity <= 4 M_Z sqrt(M_U M_V)/sqrt(|ab|)`

for

`T=2aUV+alpha(w)U+H_w(V)+b(Z+theta_w(V))^2+G(w)`,

where `U,V,Z` are independent scalar aggregates of disjoint original-coordinate blocks. Section 7 below applies this theorem to the cross-dominated branch produced by the new structural reduction.

## 3. New algebraic theorem: a scalar pivot always leaves two Schur singular directions

### Theorem `QFORM-PIVOT-SCHUR-TWO-SINGULAR-v1`

Let `A` be real symmetric with third singular value `s_3(A)>=1`. Choose an original coordinate and write

`A = [[a,b^T],[b,C]]`, `a!=0`,

and let

`S=C-bb^T/a`, `K=||b||_2/|a|`.

Then

`boxed: s_2(S) >= (1+K)^(-2).`                                      (3.1)

This is independent of the dimension, signs, rank of `A`, and all additional small eigenvalues.

### Proof

Put `u=b/a` and

`L=[[1,0],[u,I]]`.

The exact scalar-pivot congruence is

`A = L diag(a,S) L^T`.

Therefore

`diag(a,S)=L^(-1) A L^(-T)`.

For every invertible `P,Q`, singular values obey

`s_k(PMQ) >= s_min(P) s_k(M) s_min(Q)`.

Since `s_min(L^(-1))=1/||L||` and `||L||<=1+||u||=1+K`,

`s_3(diag(a,S)) >= s_3(A)/(1+K)^2 >= (1+K)^(-2)`.

The singular values of the block diagonal matrix are the union of the single number `|a|` and the singular values of `S`. A single scalar can account for at most one of the three singular values above the displayed threshold. Hence `S` has at least two singular values above that threshold, proving (3.1). QED.

This bypasses the refuted claim that one scalar pivot must leave a rank-two *cross block*. The conclusion is spectral for the exact Schur residual, and the next section converts it to a product-preserving physical cross block only under an explicit diffuse-range hypothesis.

## 4. New analytic theorem: two Schur singular directions plus full-range diffuseness give an L3 residual

Let `S` be any real symmetric matrix acting on the remaining original coordinates. Write

`S=U Lambda U^T`

with `U` spanning the **entire range** of `S`, `U^TU=I`, and `Lambda` invertible on that range. Suppose

`max_j ||u_j||^2 <= 1/32`                                             (4.1)

and suppose `S` has at least two singular values at least `tau>0`.

Define

`K_0 = sqrt(pi) Gamma(1/4)/Gamma(3/4)`.

### Theorem `QFORM-TWO-DIRECTION-DIFFUSE-L3-v1`

For independent cap-one original coordinates `Y`, the law of `R=Y^TSY` has an `L^3` density satisfying

`boxed: ||p_R||_3 <= [16 K_0 e/(7 sqrt(2) tau)]^(2/3).`          (4.2)

Arbitrarily many additional nonzero eigenvalues of `S`, of either sign and arbitrarily small magnitude, are allowed.

### Proof

Apply the same two-part MSS partition used in the regularized-determinant source to the entire range frame `U`. It gives a physical partition `I,J` with

`7I/32 <= U_I^T U_I, U_J^T U_J <=25I/32`.

For `B=S[I,J]=U_I Lambda U_J^T`, the singular-value comparison from that source gives

`s_j(B) >= (7/32) s_j(Lambda)`.

Thus `B` has two singular values at least

`sigma=(7/32)tau`.

Also `range(B)=range(U_I)` and its physical coordinate leverages obey

`diag P_range(B) <=1/7<1/2`.

Apply the regularized determinant theorem with `q=1` and retain only the two factors corresponding to those singular values:

`|phi_R(t)| <= (1 + 2 sigma^2 t^2/(pi^2 e^2))^(-1/2)`.          (4.3)

Raise to the `3/2` power and integrate. The classical beta integral gives

`int_R (1+s^2)^(-3/4) ds = K_0`,

hence

`int_R |phi_R(t)|^(3/2) dt <= K_0 pi e/(sqrt(2) sigma)`

` = 32 K_0 pi e/(7 sqrt(2) tau)`.                               (4.4)

With the Fourier convention `hat f(t)=int exp(itx)f(x)dx`, inverse Hausdorff--Young by interpolation gives

`||p_R||_3 <= (2pi)^(-2/3) ||phi_R||_(3/2)`.

Substitute (4.4) to obtain (4.2). Since `phi_R in L^(3/2)`, the output measure is represented by this `L^3` density. QED.

This is deliberately an `L^3`, not `L^infinity`, conclusion: two quadratic directions are the borderline regime in which a third physical square supplies the final half-order of smoothing.

## 5. New target-level branch: arbitrary-matrix diffuse Schur closure

Return to the target matrix and the pivot notation of Section 3. Completing the square in the **original** coordinate gives

`Q = a (X_i + b^T Y/a)^2 + R`,

`R=Y^T S Y`.                                                            (5.1)

Because `X_i` is independent of `Y`, conditionally on any measurable function of `Y` the variable `X_i+b^TY/a` is a mixture of translations of the original `X_i` law; its conditional density cap is still one.

Combining (3.1), (4.2), and the account01/B11 dependent-square theorem yields the following.

### Theorem `QFORM-ARBITRARY-SPECTRUM-PIVOT-DIFFUSE-SCHUR-v1`

Assume the exact target spectral hypothesis `s_3(A)>=1`. For a physical pivot `a=A_ii!=0`, set

`K=||A_{i,-i}||_2/|a|`.

If the entire-range projection of its Schur residual `S` has maximum row leverage at most `1/32`, then

`boxed:
 ||p_Q||infinity
 <=16 (1+K) |a|^(-1/2) sqrt[ K_0 e/(7 sqrt(2)) ].
`                                                                      (5.2)

Only an essentially bounded density is asserted here; continuity is not proved by this square-smoothing step.

### Proof

Theorem 3 gives `tau=(1+K)^(-2)`. Theorem 4 gives

`M=||p_R||_3 <=[16K_0e/(7sqrt(2)tau)]^(2/3)`.

Account01/B11 then gives

`||p_Q||infinity <=4|a|^(-1/2)M^(3/4)`

`=16(1+K)|a|^(-1/2)sqrt[K_0e/(7sqrt(2))]`.

QED.

The notable point is scope: unlike the earlier exact-rank-three spectral-row formulas, `A` and `S` may have arbitrarily many additional nonzero spectral directions.

## 6. Large-spectral-row consequence and an explicit universal subbranch

Let

`P=1_{ {|A|>=1} }`

be the spectral projection onto all eigenvectors whose eigenvalues have modulus at least one, and put `c_i=P_ii`. Functional calculus gives the operator inequality

`A^2 >= P`.

Therefore, for every original coordinate,

`boxed: A_ii^2 + ||A_{i,-i}||_2^2 = (A^2)_ii >= c_i.`          (6.1)

If `||A_{i,-i}||<=K|A_ii|`, then (6.1) implies

`|A_ii| >= sqrt(c_i/(1+K^2))`.                                  (6.2)

Combining (5.2) and (6.2), whenever the Schur residual range is diffuse,

`boxed:
 ||p_Q||infinity
 <=16(1+K)((1+K^2)/c_i)^(1/4)
     sqrt[K_0e/(7sqrt(2))].
`                                                                      (6.3)

In particular, take `c_i>=1/64` and `K<=1`. Then

`|A_ii|>=1/sqrt(128)`, `tau>=1/4`, and

`boxed: ||p_Q||infinity <= C_*`,

`C_*=32*128^(1/4)*sqrt[K_0e/(7sqrt(2))] <130.`                  (6.4)

Thus a full-target counterexample cannot contain a coordinate carrying at least `1/64` of the large-spectral projection which is simultaneously diagonal-dominated (`||A_{i,-i}||<=|A_ii|`) and has a diffuse entire-range Schur residual.

This is a genuine branch closure inside the fresh B19 low-stable-rank residual as well: no assumption in the proof conflicts with `sr(A-diag A)<32`.

## 7. Assigned partner applied to the complementary cross-dominated branch

Suppose `c_i>=1/64` but the diagonal-dominated condition fails:

`beta:=||A_{i,-i}||_2 > |A_ii|`.

Then (6.1) gives

`beta >1/sqrt(128)`.                                                 (7.1)

Assume a product-preserving extraction produces the **exact** account04/B20 normal form with

- `U=X_i`, so `M_U<=1`;
- `V=sum_{j in J} c_jX_j` on a disjoint block and `||c||_2>=theta beta` for some `theta>0`;
- `Z=sum_{k in K} d_kX_k` on another disjoint block;
- bilinear term `2UV`;
- square coefficient `gamma!=0`, with `kappa:=|gamma| ||d||_2^2`;
- all remaining terms lying in the measurable shears/outside conditioning allowed by the partner theorem.

The sharp one-dimensional product marginal bound gives

`M_V<=sqrt(2)/||c||`, `M_Z<=sqrt(2)/||d||`.

The assigned partner theorem therefore yields the **actual density inequality**

`||p_Q||infinity
 <= 2^(11/4)/[ ||d|| sqrt(|gamma|) sqrt(||c||) ]`

` <= 2^(11/4)/sqrt(theta beta kappa)`

` < 2^(9/2)/sqrt(theta kappa)`.                                    (7.2)

The last step is exactly (7.1). Thus, in the cross-dominated large-spectral-row branch, it is enough for the still-unpaid aggregate extraction to retain a fixed fraction `theta` of the pivot cross-row norm and a fixed effective square strength `kappa`; account04/B20 then closes the probability law with a dimension-free constant.

Equation (7.2) is not an assertion that such an extraction always exists. It identifies the precise dimension-free currency that the current low-stable-rank bridge must produce. No transformed-coordinate independence is assumed.

## 8. Sharpened residual after this run

Combine the fresh B19 stable-rank reduction with Sections 5--7. Any still-unresolved full-target configuration must lie in the B19 residual

`||A-diag(A)||op>1/4`, `sr(A-diag(A))<32`,

and, in addition, must evade the new pivot-Schur closure. Taking the concrete thresholds above, at least one of the following mechanisms must persist:

1. **large-eigenspace diffuse / small-spectrum-heavy:** every coordinate has `P_ii<1/64`, so any physical heavy leverage comes from spectral directions with modulus below one;
2. **cross-dominated large-spectral rows:** for each coordinate with `P_ii>=1/64` used as a pivot, `||A_{i,-i}||>|A_ii|`, and the product-preserving aggregate-square extraction of Section 7 is not yet available with uniform `(theta,kappa)`;
3. **Schur-range localization:** a coordinate has `P_ii>=1/64` and `||A_{i,-i}||<=|A_ii|`, but the entire-range projection of its exact Schur residual contains a row leverage greater than `1/32`.

This is strictly narrower than the bare low-stable-rank off-diagonal residual. In particular, arbitrary additional small eigenvalues are no longer an interaction debt in the diagonal-dominated/diffuse-Schur branch; they are retained by the regularized determinant proof.

A natural next implication is `QFORM-LOW-SR-CROSS-OR-LOCALIZED-SCHUR-v2`: in the residual stable-rank state, aggregate either branch 2 into the account04/B20 disjoint hyperbolic-square normal form with uniform `(theta,kappa)`, or iterate branch 3 through a bounded heavy-coordinate core without paying one reciprocal tiny minor. Branch 1 needs a separate argument showing that large-eigenspace diffuseness plus small-spectrum physical localization is harmless or itself supplies a product-preserving cross block.

## 9. Status and continuity

Proved this run:

- `QFORM-PIVOT-SCHUR-TWO-SINGULAR-v1`;
- `QFORM-TWO-DIRECTION-DIFFUSE-L3-v1`;
- `QFORM-ARBITRARY-SPECTRUM-PIVOT-DIFFUSE-SCHUR-v1`;
- the explicit `C_*<130` large-spectral-row subbranch;
- the partner-applied cross-dominated inequality (7.2).

Not proved: the full low-stable-rank residual, hence not the full QFORM conjecture. The new pivot branch proves an essentially bounded density. The partner branch also proves only essential boundedness at this scope. No new continuity claim is made for either branch.

Full conjecture status: `OPEN / NOT PROVED / NOT DISPROVED`.
