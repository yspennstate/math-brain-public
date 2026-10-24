# account03/B19 — low-offdiagonal-rank normal form and mixed coordinate/aggregate compression

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T143049Z-account03-B19-QFORM-r11b`  
**Assignment:** Universal proof assembly  
**Status:** `ESSENTIAL_STEP_APPLIED / TARGET_LEVEL_BRANCHES_PROVED / FULL_CONJECTURE_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`

## 1. Exact target and source-valid starting point

The target is unchanged: for arbitrary dimension, independent real coordinates with one-dimensional probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite essential-density bound for `Q=X^TAX`, or give a target-valid counterexample. Continuity is separate and is **not** proved in the new branches below.

Fresh owner control before publication was `yspennstate/math-research-brain@46f58fad0bc29bc323315357e8d88a7a804f72fa`, revision `2026-09-22.5`. The live correction inbox was re-read. No law-uniform scalar Fresnel decay, post-rotation independence, fiber-supremum closure, generic conditional-cap surrogate, fixed-principal-minor dichotomy, or absolute phase-Wiener claim is used.

The preceding B19 theorem left every possible counterexample in

`||H||op>1/4,  sr(H)<32`, where `H=A-diag(A)`.

This run changes mechanism: instead of another stable-rank cross-cut estimate, it uses singular-rank perturbation plus the zero diagonal of `H` to expose the first one-effective-direction normal form.

The designated partner `account04/B19` completed `QFORM-FINITE-UNION-CORE-v1` at

`yspennstate/math-open-problems@02171dc794a56c0235afb1ca394b3e614162bff4`

and proves exact equality of interval-concentration suprema between arbitrary independent cap-one densities and bounded finite-union product indicators. That theorem is applied below to an actual small-ball inequality, not merely cited.

## 2. Product finite-union transfer for a definite physical two-plane

Let `B` be a definite `2 x 2` physical principal block of `A`, and suppose

`|det B|>=delta>0`.

For a bounded finite-union product indicator law, condition on all physical coordinates outside this pair. The remaining quadratic is

`z^T B z + 2 ell^T z + c`.

Completing the square is only a deterministic translation on this two-dimensional section. For any interval `I`, the full-plane Lebesgue area of the inverse image is at most

`pi |I| / sqrt(delta)`.

Indeed, after translation and possibly replacing the quadratic by its negative, the sublevel area of a positive-definite form is `pi t/sqrt(det B)`, so a shell over an interval of length `|I|` has area at most the displayed quantity. Intersecting with the two finite-union coordinate sets can only decrease area. The remaining product factors each have total length one, hence Fubini gives

`P(Q in I) <= pi |I|/sqrt(delta)`

for every finite-union product indicator.

Now apply the **designated partner** `QFORM-FINITE-UNION-CORE-v1`: the same interval-concentration inequality holds for every admissible independent cap-one input law. Therefore the output measure is absolutely continuous and

`||p_Q||infinity <= pi/sqrt(delta)`.

This is the only extremal reduction used below; arbitrary fragment separation is retained.

## 3. New near-diagonal extension

### Theorem 3.1 — `QFORM-NEARDIAGONAL-7OVER16-v1`

Let `D=diag(A)` and `H=A-D`. If

`||H||op <= 7/16`

and `s_3(A)>=1`, then

`||p_Q||infinity <= 2 sqrt(2) pi`.

#### Proof

Singular-value perturbation gives

`s_3(D) >= s_3(A)-||H||op >= 9/16`.

Thus at least three diagonal entries of `D` have modulus at least `9/16`. Two have the same sign; call their indices `i,j`. Since `|H_ij|<=||H||op<=7/16`, the physical block

`B=[[D_ii,H_ij],[H_ij,D_jj]]`

is definite and

`|det B| >= (9/16)^2-(7/16)^2 = 1/8`.

Section 2 gives the result. QED.

Hence the previous B19 residual shrinks from `||H||op>1/4` to

`||H||op>7/16, sr(H)<32`.

## 4. Rank-one spectral truncation forced by `s_2(H)<=1/8`

Set `theta=1/8`. Suppose

`s_2(H)<=theta`.

Choose an eigenpair `(lambda,v)` with `|lambda|=s_1(H)` and `||v||_2=1`, and write

`H=lambda vv^T+R`, `||R||op<=theta`.

Because `H` has zero diagonal,

`lambda v_k^2 + R_kk =0`

for every physical coordinate `k`. Therefore

`|lambda| v_k^2 <= theta`.                                      (4.1)

Also, for `k!=l`,

`|H_kl| <= |lambda||v_kv_l|+|R_kl| <= 2theta =1/4`.            (4.2)

Now put `A_0=A-R=D+lambda vv^T`. Weyl gives

`s_3(A_0)>=1-theta=7/8`.

A rank-one perturbation can raise the singular-value counting function by at most one, equivalently

`s_3(D+lambda vv^T) <= s_2(D)`.

Thus

`s_2(D)>=7/8`.                                                   (4.3)

So there are two physical indices `p,q` with

`|D_pp|,|D_qq|>=7/8`.                                           (4.4)

## 5. Two target-level closure branches

### 5.1 Same-sign heavy diagonals

If the two entries in (4.4) have the same sign, then by (4.2)

`|det A[{p,q},{p,q}]| >= (7/8)^2-(1/4)^2 =45/64`.

The block is definite, so Section 2 gives

`||p_Q||infinity <= 8 pi/sqrt(45) <4 pi`.                       (5.1)

### 5.2 A third moderate diagonal

Assume instead `D_pp,D_qq` have opposite signs. If some third index `k` has

`|D_kk|>=1/7`,

then `D_kk` has the same sign as one of `D_pp,D_qq`. Pair it with that heavy diagonal. Again using (4.2), the corresponding definite block has

`|det B| >= (7/8)(1/7)-(1/4)^2 =1/16`.

Hence

`||p_Q||infinity <=4 pi`.                                       (5.2)

Therefore every counterexample in the `s_2(H)<=1/8` branch must satisfy, after relabelling,

`D_pp D_qq<0`,
`|D_pp|,|D_qq|>=7/8`,
`|D_kk|<1/7` for every `k notin {p,q}`.                         (5.3)

## 6. The one-effective-direction normal form

Under the unresolved conditions (5.3), `s_3(D)<1/7`. Since `s_3(D+lambda vv^T)>=7/8`, Weyl gives

`|lambda| > 7/8-1/7 =41/56`.                                  (6.1)

Combining (6.1) with the zero-diagonal identity (4.1),

`v_k^2 < (1/8)/(41/56)=7/41` for every `k`.                     (6.2)

In particular the dominant off-diagonal eigenvector is genuinely diffuse. If

`T={1,...,n}\{p,q}`, `r=||v_T||_2`,

then

`r^2 >1-2(7/41)=27/41`.                                        (6.3)

Writing `w=v_T/r`, every coefficient of this normalized outside aggregate satisfies

`w_k^2 < (7/41)/(27/41)=7/27<1/2`.                             (6.4)

Thus the unresolved one-effective branch consists of two opposite physical diagonal pivots and a quantitatively diffuse third spectral direction supported mostly on the disjoint outside coordinate bank.

## 7. New mixed coordinate/aggregate three-plane is uniformly nondegenerate

The previous statement can be strengthened to an exact geometric resource.

Let

`E=span{e_p,e_q,w}`,

where `w` is the normalized outside vector from (6.4). In the orthonormal basis `(e_p,e_q,w)`, split the compression of `A` as

`A_E=M_0+E_0`,

where, after multiplying the whole matrix by an irrelevant global sign if needed,

`M_0=diag(a,-b,0)+lambda (x,y,r)^T(x,y,r)`,

with

`a,b>=7/8`, `x=v_p`, `y=v_q`, `r^2>=27/41`,
`x^2,y^2<=7/41`, `|lambda|>=41/56`,

and

`||E_0||op <= ||R||op + ||D_T||op <1/8+1/7=15/56`.             (7.1)

### Lemma 7.1 — inverse bound for the main core

`M_0` is invertible and

`s_min(M_0)>3/10`.                                              (7.2)

#### Proof

Solving `M_0 u=z` gives the exact inverse

`M_0^{-1} =`

`[[ 1/a,   0,      -x/(ar)],`
` [ 0,    -1/b,     y/(br)],`
` [-x/(ar), y/(br), 1/(lambda r^2)+x^2/(a r^2)-y^2/(b r^2) ]]`.

The diagonal terms contribute at most `128/49` to the squared Frobenius norm. The four off-diagonal entries contribute at most

`2*(64/49)*(x^2+y^2)/r^2 <=256/189`.

Finally

`|1/(lambda r^2)+x^2/(a r^2)-y^2/(b r^2)|`
`<= [56/41+(8/7)(14/41)]/(27/41)=8/3`.

Hence

`||M_0^{-1}||F^2 <=128/49+256/189+64/9`
`=14656/1323 <100/9`.

So `||M_0^{-1}||op<10/3`, proving (7.2). QED.

By Weyl and (7.1),

`boxed: s_min(A_E) > 3/10-15/56 =9/280.`                        (7.3)

This is a cancellation-resistant three-direction resource in the **actual full matrix**, not merely in the rank-one approximation.

The third direction is a normalized linear aggregate of original coordinates disjoint from `p,q`; it is independent of `(X_p,X_q)` and, by the standard product-marginal theorem, has density at most `sqrt(2)`. Equation (6.4) records the stronger coefficient diffuseness `max w_k^2<7/27`.

What is **not** done here is to condition on coordinates orthogonal to `w`: such conditioning would silently assume a conditional density cap and is prohibited by the live corrections. The theorem therefore stops at the correct product-preserving interface.

## 8. Exact new residual after combining with the previous B19 stable-rank theorem

Any counterexample to the owner target must now satisfy all of

`||H||op>7/16`,
`sr(H)<32`,

and one of the following two mutually exhaustive mechanisms:

1. **two-offdiagonal-resource branch:** `s_2(H)>1/8`; or
2. **one-effective-direction branch:** `s_2(H)<=1/8`, together with the normal form (5.3), (6.1)--(6.4), and the actual mixed coordinate/aggregate compression (7.3).

This is a strict reduction of the prior low-stable-rank residual.

## 9. First unpaid implication

The first missing implication is now the product-preserving use of (7.3):

### `QFORM-MIXED-AGGREGATE-COMPRESSION-SPLICE-v1` — OPEN

Given two disjoint original coordinates `p,q` and a normalized linear aggregate `Z=w^T X_T` on a disjoint outside bank with `max w_k^2<7/27`, suppose the actual quadratic Hessian has smallest singular value `>9/280` on `span(e_p,e_q,w)`. Prove a universal linear small-ball estimate while retaining the full product origin of the outside bank and arbitrary quadratic/cross terms on that same bank.

It is **not** enough to rotate the outside coordinates and condition on the orthogonal complement: the conditional law of `Z` need not retain its marginal cap. The next proof must aggregate before or jointly with the curved trace, for example by a block Hausdorff--Young/coarea inequality or a bank version of the completed rank-two half-Riesz theorem.

For the complementary `s_2(H)>1/8` branch, the source-valid two-cross Schur theorem shows that a physical pivot plus two suitably diffuse cross singular directions is already analytically paid; the missing work there is a product-preserving extraction/aggregation theorem, not a new local density estimate.

## 10. Status and nonclaims

**Proved here:**

- `QFORM-NEARDIAGONAL-7OVER16-v1`, density bound `2 sqrt(2) pi`;
- same-sign and third-moderate-diagonal closures in the `s_2(H)<=1/8` branch, each with density bound at most `4 pi`;
- the one-effective-direction normal form (5.3), (6.1)--(6.4);
- the actual full-matrix mixed coordinate/aggregate compression lower bound `s_min>9/280`.

**Applied completed designated partner mathematics:** account04/B19 finite-union-core equality was used to transfer the definite-section interval inequality to all arbitrary cap-one product laws.

**Not proved:** the mixed aggregate splice, the complete `s_2(H)>1/8` extraction, the full conjecture, or global continuity.
