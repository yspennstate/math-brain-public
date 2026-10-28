SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B13, 2026-09-23T11:30:36Z.
attacking: both-sides-nonnull two-hub curvature glue via scalar-pivot transport and a local three-coordinate fractional-potential compiler.

# account01/B13 auto22 — two-hub pivot rigidity after extremal-product purification

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Extremal product laws  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** **ESSENTIAL_STEP_APPLIED / PROVED SUPPORTING TARGET-LEVEL STRUCTURAL THEOREM / FULL QFORM OPEN / FULL CONTINUITY OPEN**

The unrestricted conjecture is not proved or disproved here. This run closes no branch by perturbatively deleting a small matrix. Instead it proves that, once a genuine physical two-hub block is present, a high slab ratio forces the arbitrary curved leaf block into a precise Schur/Nystrom rigidity class. The result is product-preserving and translation-uniform.

## 1. Fresh scope and immutable premises


The following completed source results are used exactly in their proved scopes.

1. `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`, source  
   `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,  
   `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`: for a two-dimensional invertible symmetric quadratic coefficient `K`, arbitrary affine term and independent cap-one original coordinates,

   `sup_t E |Y^T K Y + linear - t|^(-1/2) <= 128 |det K|^(-1/4)`.          (1.1)

   The same source gives the rank-three residual theorem: for an invertible original-coordinate `3x3` block `P` and a nonzero physical diagonal entry `d=P_rr`, the corresponding ambient conditional quadratic form has density cap

   `128 (|d det P|)^(-1/4)`.                                              (1.2)

2. The physical-pair logarithmic theorem, source  
   `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,  
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`: for an invertible indefinite original-coordinate pair `H`, its conditional density envelope can be optimized pointwise. In the zero-diagonal case

   `H=[[0,h],[h,0]]`, `h!=0`,

   the result is

   `p_pair(s) <= 4 |h|^(-1/2) |s-s0|^(-1/2)`.                            (1.3)

   The same source records that a definite physical pair has density at most `pi/sqrt(|det H|)` after arbitrary affine translation.

3. The designated partner `account02/B13` r25 report, source  
   `yspennstate/math-open-problems@04973c0d13c8cbe814f1303b7de8aeffd40791df`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260923T110032Z-account02-B13-extremal-r25/REPORT.md`. Its `QFORM-DIAGONAL-LEAF-AGGREGATE-v1` states that, for a two-hub cross bank `B=[b_j]`, `G=BB^T`, leverage numbers `ell_j=b_j^T G^{-1}b_j`, `h=max ell_j<1`, and arbitrary **diagonal** leaf twists,

   `||p_Q||inf <= 4/((2-q)sqrt(q)) det(G)^(-1/4)`                         (1.4)

   for `max(1,2h)<=q<2`. In particular, if `h>1/2`,

   `||p_Q||inf <= 2/((1-h)sqrt(2h)) det(G)^(-1/4)`.                       (1.5)

   Its exact determinant-star identity is

   `sum_{k!=j} det(b_j,b_k)^2 = ell_j det(G)`,
   `sum_{r<s; r,s!=j} det(b_r,b_s)^2 = (1-ell_j)det(G)`.                  (1.6)

4. The previous `account01/B13` extremal-product theorem, source  
   `yspennstate/math-open-problems@4be4c9842b3828e8a862e58d7e6eec894a85317c`, proves the exact/no-loss reduction from arbitrary cap-one product laws to arbitrary measurable unit-measure product indicators for nonnegative kernels, with bounded finite-union indicators sufficient by approximation. There is no single-interval, centered-uniform, bounded-diameter, or fixed-fragment reduction.

## 2. Two elementary positive-kernel compilers

### Lemma 2.1 — outer original-coordinate square

Let `X` have density at most one and be independent of `R`. More generally allow the center of the square to be any measurable function of the variables generating `R`. If

`Q=a (X+m)^2 + R`, `a!=0`,

then almost everywhere

`p_Q(t) <= |a|^(-1/2) E |t-R|^(-1/2)`.                               (2.1)

Indeed, condition on the variables generating `(m,R)`. The pushforward of the cap-one scalar density under `a(X+m)^2` has density at output displacement `y` bounded by `|a|^(-1/2)|y|^(-1/2)` on the appropriate half-line. Averaging proves (2.1). No independence of a rotated coordinate is used.

### Lemma 2.2 — half-Riesz potential from a density cap

If a probability density `p` satisfies `||p||inf<=M`, then

`sup_t int |t-y|^(-1/2) p(y)dy <= 2 sqrt(2M)`.                       (2.2)

This is the one-dimensional bathtub bound: the decreasing kernel is maximized by filling the centered interval of length `1/M`, and

`M int_{-1/(2M)}^{1/(2M)} |y|^(-1/2)dy = 2sqrt(2M)`.

These two lemmas are used only with original-coordinate conditioning.

## 3. Scalar pivot: simultaneous collapse of every Schur two-minor

### Proposition 3.1 — `QFORM-SCALAR-SCHUR-ALL2-COLLAPSE-v1`

Suppose a genuine original-coordinate scalar pivot has coefficient `a!=0`. After conditioning all other variables as needed and completing that square, write

`Q=a(X_1+m)^2+R`,                                                   (3.1)

where `R` is the quadratic form on the remaining original coordinates with scalar Schur matrix `S` and arbitrary induced affine term.

For every pair of remaining physical coordinates `r,s`,

`||p_Q||inf <= 128 |a|^(-1/2) |det S[{r,s}]|^(-1/4)`               (3.2)

whenever the determinant is nonzero. Hence, if an actual interval `J` has slab ratio

`rho=P(Q in J)/|J|`,                                                (3.3)

then **simultaneously for every pair**

`boxed: |det S[{r,s}]| <= E_a := (128/rho)^4 |a|^(-2).`            (3.4)

For a zero determinant (3.4) is automatic.

#### Proof

Apply Lemma 2.1. Conditional on every remaining original coordinate except `r,s`, the random variable `R` is a two-variable quadratic with coefficient matrix `S[{r,s}]` and arbitrary affine term. The rank-two affine half-Riesz theorem (1.1) gives

`E(|t-R|^(-1/2) | outside {r,s}) <=128 |det S[{r,s}]|^(-1/4)`.

Average the conditioning and substitute into (2.1). This proves (3.2), and `rho<=||p_Q||inf` gives (3.4). QED.

The significance is that high concentration collapses **all** principal two-minors of one genuine physical Schur remainder at once; no tiny reciprocal minor is selected.

## 4. Scalar pivot plus one second scalar: simultaneous Schur-three collapse

Assume, in the setting of Proposition 3.1, that another remaining physical coordinate `r` has

`d=S_rr !=0`.                                                       (4.1)

For any other two coordinates `j,k`, let

`P=S[{r,j,k}]`.                                                     (4.2)

If `P` is invertible, condition every remaining original coordinate outside this triple. The rank-three residual theorem (1.2) gives the conditional density cap

`M <=128 (|d det P|)^(-1/4)`.                                      (4.3)

By Lemma 2.2,

`sup_t E|R-t|^(-1/2) <= 2sqrt(2M)
                            <=32 (|d det P|)^(-1/8)`.              (4.4)

The outer square (2.1) therefore gives

`||p_Q||inf <=32 |a|^(-1/2)(|d det P|)^(-1/8)`.                    (4.5)

Consequently every actual slab ratio `rho` forces, simultaneously for every such triple (with the singular cases automatic),

`boxed: |d det S[{r,j,k}]| <= F_a :=(32/rho)^8 |a|^(-4).`          (4.6)

This is a second-order collapse estimate, now strong enough to turn the Schur remainder into an entrywise Nystrom normal form.

## 5. Main structural theorem: invertible two-hub Nystrom rigidity

### Theorem 5.1 — `QFORM-INVERTIBLE-TWOHUB-NYSTROM-RIGIDITY-v1`

Let `H={1,2}` be two original physical coordinates and `T` a disjoint leaf set. Condition all coordinates outside `H union T`; the conditioned coefficient matrix is still the corresponding physical principal block. Write

`A[H union T,H union T]=[[H_0,B],[B^T,C]]`,

`H_0=[[a,h],[h,g]]`, `B=[b_1^T;b_2^T]`.                            (5.1)

Assume

`a!=0`, `det H_0 !=0`.                                             (5.2)

Define the exact two-hub Schur/Nystrom leaf remainder

`T_0 := C-B^T H_0^(-1)B`.                                         (5.3)

If `rho=P(Q in J)/|J|` is the slab ratio of any interval, then

`boxed:
 ||T_0||_max <= C_N /(rho^4 |a det H_0|),
 C_N=sqrt(128^8+32^8)
     =128^4 sqrt(1+4^(-8))
     <2.684376e8.
`                                                                         (5.4)

No assumption is made on the leaf curvature `C`; (5.4) is forced by the high concentration itself.

#### Proof

Pivot coordinate `1`. Put

`d=g-h^2/a = det(H_0)/a`,
`w=b_2-(h/a)b_1`,
`C_1=C-a^(-1)b_1^T b_1`.                                         (5.5)

The first scalar Schur matrix is

`S=[[d,w],[w^T,C_1]]`.                                             (5.6)

Since `det H_0!=0`, `d!=0`, and its Schur complement in `S` is exactly

`C_1-d^(-1)w^T w = C-B^T H_0^(-1)B=T_0`.                          (5.7)

For every leaf `j`, the physical two-minor involving the second hub is

`det S[{2,j}] = d (T_0)_{jj}`.                                    (5.8)

Proposition 3.1 gives

`|(T_0)_{jj}| <= E_a/|d|`.                                        (5.9)

For every leaf pair `j,k`, block determinant gives

`det S[{2,j,k}] = d det T_0[{j,k}]`.                              (5.10)

Equation (4.6) therefore yields

`|det T_0[{j,k}]| <=F_a/|d|^2`.                                  (5.11)

Finally

`(T_0)_{jk}^2=(T_0)_{jj}(T_0)_{kk}-det T_0[{j,k}]`,                (5.12)

so

`|(T_0)_{jk}|
 <= sqrt(E_a^2+F_a)/|d|
 = sqrt(128^8+32^8)/(rho^4 |a|^2 |d|)
 = C_N/(rho^4 |a det H_0|)`.                                      (5.13)

The diagonal estimate is no larger. QED.

**Important limitation.** The max-norm-small remainder in (5.4) may have large operator norm in high dimension, and arbitrary translated/fragmented product supports can amplify tiny coefficients. The theorem does **not** authorize deleting `T_0` perturbatively.

## 6. Singular two-hub block: quantitative row alignment

### Corollary 6.1 — `QFORM-SINGULAR-TWOHUB-ROW-ALIGNMENT-v1`

Keep (5.1), assume `a!=0` but

`det H_0=0`.                                                       (6.1)

Then `d=0` in (5.5), and Proposition 3.1 applied to the pair `{second hub,j}` gives

`det S[{2,j}]=-w_j^2`.                                             (6.2)

Hence every slab ratio `rho` forces

`boxed:
 |b_{2j}-(h/a)b_{1j}|
 <=128^2/(rho^2 |a|)
 =16384/(rho^2 |a|)
`                                                                       (6.3)

for **every leaf `j` simultaneously**. Moreover every principal two-minor of the residual leaf block `C_1` has absolute determinant at most `E_a` from (3.4).

Thus a singular curved hub block cannot support a high-ratio determinant star with a robust transverse second cross row: the two hub-to-leaf rows become entrywise aligned at scale `rho^-2`.

## 7. Zero-diagonal indefinite hub pair: anchored four-determinant collapse

The scalar pivot is unavailable when

`H_0=[[0,h],[h,0]]`, `h!=0`.                                      (7.1)

This is exactly where the physical-pair logarithmic theorem must be used as a whole.

Let

`T_0=C-B^T H_0^(-1)B`                                             (7.2)

be the pair Schur complement on the leaves. Completing the physical pair and using (1.3) yields

`p_Q(t) <=4 |h|^(-1/2) E |t-R|^(-1/2)`,                           (7.3)

where `R` is the genuine original-coordinate leaf Schur quadratic form plus its arbitrary affine term.

For any leaf pair `j,k`, the rank-two half-Riesz theorem gives

`||p_Q||inf <=512 |h|^(-1/2)|det T_0[{j,k}]|^(-1/4)`.              (7.4)

But the bordered determinant identity is exact:

`det A[H union {j,k},H union {j,k}]
 =det(H_0) det T_0[{j,k}]
 =-h^2 det T_0[{j,k}]`.                                           (7.5)

Therefore

`boxed:
 ||p_Q||inf
 <=512 |det A[H union {j,k},H union {j,k}]|^(-1/4).
`                                                                       (7.6)

An actual slab ratio `rho` consequently forces **simultaneously for every leaf pair**

`boxed:
 |det A[H union {j,k},H union {j,k}]| <=(512/rho)^4,
 |det T_0[{j,k}]| <= E_h:=(512/rho)^4 |h|^(-2).
`                                                                       (7.7)

This is `QFORM-ZERODIAG-PAIR-FOURDET-COLLAPSE-v1`. It is an aggregate-ready statement expressed entirely through original physical coordinates.

## 8. Zero-diagonal pair: the leaf Schur remainder is rank-one plus a controlled max-norm tail

There are two exact subcases.

### 8.1 Every leaf diagonal vanishes

If `(T_0)_{jj}=0` for all leaves, then

`det T_0[{j,k}]=-(T_0)_{jk}^2`.

Equation (7.7) gives

`boxed:
 ||T_0||max <=512^2/(rho^2 |h|)=262144/(rho^2 |h|).
`                                                                       (8.1)

Again this tail is retained, not discarded.

### 8.2 One genuine leaf scalar pivot exists

Suppose `(T_0)_{rr}=d!=0`. For every other leaf pair `j,k`, condition outside the physical triple `{r,j,k}` in the leaf Schur variables. By (1.2), `R` has density cap

`128 (|d det T_0[{r,j,k}]|)^(-1/4)`.                               (8.2)

Combining Lemma 2.2 with (7.3) gives

`||p_Q||inf
 <=128 |h|^(-1/2)(|d det T_0[{r,j,k}]|)^(-1/8)`.                   (8.3)

Hence an actual ratio `rho` forces

`|d det T_0[{r,j,k}]|
 <=F_h:=(128/rho)^8 |h|^(-4)`.                                   (8.4)

Let `U` be the scalar Schur complement of `d` inside `T_0`. Then

`det T_0[{r,j}]=d U_jj`,
`det T_0[{r,j,k}]=d det U[{j,k}]`.                                (8.5)

Equations (7.7) and (8.4) imply

`|U_jj|<=E_h/|d|`,
`|det U[{j,k}]|<=F_h/|d|^2`.                                     (8.6)

Therefore, exactly as in (5.12),

`boxed:
 ||U||max <= C_P/(rho^4 h^2 |d|),
 C_P=sqrt(512^8+128^8)
     =512^4 sqrt(1+4^(-8))
     <6.8720011e10.
`                                                                       (8.7)

Thus the zero-diagonal indefinite pair forces its leaf Schur curvature either to be max-norm small outright, or to be **one physical rank-one Schur component plus a max-norm-small tail** after a genuine leaf scalar pivot. No rotation is used.

## 9. Exhaustive two-hub curvature classification at high slab ratio

For one fixed physical two-hub block `H_0`, the preceding results give the following exhaustive product-preserving alternatives.

1. **Exact-null hub block `H_0=0`.** Previous `account01/B13` `QFORM-DUAL-RECTANGULAR-NULLBANK-AGGREGATE-v1` pays arbitrary leaf curvature directly:

   `||p_Q||inf <=sqrt(2 pi e) det(BB^T)^(-1/4)`                    (9.1)

   for rank-two `B`.

2. **Definite invertible `H_0`.** The physical-pair ellipse calculation from the pair-log source gives

   `||p_Q||inf <=pi/sqrt(det H_0)`.                                (9.2)

   Thus `rho` forces `det H_0 <=(pi/rho)^2`.

3. **Invertible indefinite `H_0` with a nonzero diagonal.** Theorem 5.1 forces the entire arbitrary leaf curvature to satisfy the Nystrom rigidity estimate (5.4).

4. **Singular `H_0` with a nonzero diagonal.** Corollary 6.1 forces the two physical hub-to-leaf rows to align entrywise at the scale `rho^-2`, while all residual leaf principal two-minors collapse.

5. **Invertible indefinite zero-diagonal pair.** Sections 7--8 force every anchored physical `4x4` determinant to collapse at scale `rho^-4`, and force the leaf pair-Schur remainder into a max-norm-small or rank-one-plus-max-norm-small normal form.

There is no remaining algebraic type of a nonzero real symmetric `2x2` hub block.

## 10. Designated partner applied to an actual inequality

Now apply `account02/B13` r25 to the **same actual two-hub cross bank** `B=[b_j]` in its diagonal-leaf chamber. Put

`D=det(BB^T)`, `ell_j=b_j^T(BB^T)^(-1)b_j`, `h_*=max_j ell_j`.

If `h_*<=1/2`, partner inequality (1.4) gives directly

`rho <=4D^(-1/4)`, hence `D <=(4/rho)^4`.                          (10.1)

If `h_*>1/2`, partner inequality (1.5) gives the actual determinant-star constraint

`boxed:
 (1-h_*) sqrt(2h_*) D^(1/4) <=2/rho.
`                                                                       (10.2)

Together with the exact star identity (1.6), the non-star squared determinant volume obeys

`(1-h_*)D <=2 D^(3/4)/rho`,                                       (10.3)

while the maximizing physical leaf carries star volume `h_*D>D/2`.

The new pivot-rigidity theorem now says exactly what must happen when one tries to leave the partner's diagonal-leaf chamber while keeping this same determinant-star cross geometry:

- if the hub block is exact-null, arbitrary off-diagonal leaf curvature is already paid by (9.1), so there is no off-diagonal glue obstruction there;
- if the hub block is definite with nonnegligible determinant, (9.2) pays it;
- if the hub block is invertible indefinite with a nonzero diagonal, **all arbitrary off-diagonal leaf curvature is forced into**

  `C=B^T H_0^(-1)B+E`,
  `||E||max <= C_N/(rho^4 |a det H_0|)`;                           (10.4)

- if the hub block is singular with scalar pivot, the second cross row is forced into the entrywise tube (6.3);
- if it is a zero-diagonal indefinite pair, all anchored four-determinants obey (7.7), and the exact pair-Schur leaf curvature is max-norm-small or one-rank-Schur plus the controlled tail (8.7).

Thus the partner's unpaid `QFORM-DETSTAR-OFFDIAGONAL-GLUE-v1` is materially narrowed. A surviving determinant-star witness cannot have arbitrary uncontrolled leaf curvature: its curvature must be a low-rank Nystrom/Schur skeleton plus a quantitatively tiny **but undeletable** max-norm tail, or it must lie in the singular-row-alignment / zero-diagonal anchored-four-determinant branches.

This is an equation-level application of the completed partner theorem, not merely a citation to it.

## 11. Extremal-product geometric formulation

By the completed B13 purification theorem, every uniform slab statement above is equivalent, with zero constant loss, to the corresponding statement for arbitrary measurable unit-measure product indicators. In particular, for arbitrary measurable `|E_i|=1`, if

`rho_E = |{x in product_i E_i : x^T A x in J}|/|J|`,              (11.1)

then Theorem 5.1 gives

`||C-B^T H_0^(-1)B||max
 <=C_N/(rho_E^4 |a det H_0|)`                                     (11.2)

in the invertible scalar-pivot branch, and (7.7) gives

`|det A[H union {j,k},H union {j,k}]| <=(512/rho_E)^4`             (11.3)

in the zero-diagonal pair branch. No interval optimizer, centered uniform law, bounded support diameter, or finite-fragment cap is assumed.

## 12. First unpaid implication

The sharpened next implication is

`QFORM-DETSTAR-NYSTROM-MAXNORM-TAIL-CLOSURE-v1`.

A hypothetical high-ratio survivor with a substantial determinant-star cross bank has now been forced, after exhaustive physical hub-pivot splitting, into one of three concrete states:

1. `C=B^T H_0^(-1)B+E` with `rank(B^T H_0^(-1)B)<=2` and `||E||max=O(rho^-4)` at the explicit scale (5.4);
2. a singular-hub row-alignment tube with transverse cross entries `O(rho^-2)`;
3. a zero-diagonal indefinite pair with all anchored four-determinants `O(rho^-4)` and a leaf Schur matrix that is rank-one plus a controlled max-norm tail after at most one genuine physical leaf pivot.

The remaining proof must retain the max-norm tail **inside** the product-measure estimate and exploit the third large spectral direction / low-D5 information to force an already-paid grouped-bank or ridge mechanism. Entrywise smallness alone is not a legitimate random perturbation estimate in arbitrary dimension.

Independent end-to-end review of these new structural statements has not yet been performed. Full QFORM remains OPEN; continuity remains separately OPEN.
