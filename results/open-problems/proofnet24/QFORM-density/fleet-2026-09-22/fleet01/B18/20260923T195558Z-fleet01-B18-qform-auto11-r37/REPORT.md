SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B18, 2026-09-23T19:55:58Z.
attacking: the fleet02/B18 low-hub equal-spectrum two-sheet stress family; exploit its normalized-Hadamard source banks and the completed scalar/dependent-pair receiver without losing original-coordinate product provenance.

# fleet01/B18 — Hadamard-bank closure of the low-hub equal-spectrum stress family

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T195558Z-fleet01-B18-qform-auto11-r37`  
Status: **PROVED SUPPORTING TARGET-VALID FAMILY CLOSURE / DESIGNATED PARTNER APPLIED; FULL QFORM OPEN**.  
Continuity: **not claimed** by the new argument; only essential boundedness is asserted.
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact partner object consumed

The newest completed fleet02/B18 report used here is

- `yspennstate/math-open-problems@c99a85972a70c210b19dd41128300ad55a9b8cb4`;
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/b18-20260923T191130Z-20b2aab6/REPORT.md`.

It constructs, for `0<eta<1/64`, an exact-rank-three target matrix with nonzero spectrum `{-1,1,1}` and a null hub, in the rigid form

`A = p n^T + n p^T + beta beta^T`,

where `(p,n,beta)` are orthonormal. Put

`c=sqrt(1-eta^2)`,
`r=(x,y,z)` in the `(n,beta,e)` coordinates of the distinguished leaf,
`z=-eta`,
`x=sqrt(1-eta^4-eta^6)-c eta`,
`y=sqrt(2 c eta x)`.

Then

`||r||^2 = 1-eta^6`,
`p=eta e_0+c e`,

and the distinguished leaf has physical diagonal zero. The residual frame is chosen explicitly as

`G=I_3-r r^T`, `H=G^(1/2)`, `R_res=W H`,

where `W` consists of the first three columns of a normalized Hadamard matrix of order `m`. This is the partner's target-valid low-hub stress completion. It is not a counterexample to QFORM.

The completed fleet02/B18 analytic receiver used below is the earlier theorem
`QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1`, source

- `yspennstate/math-open-problems@ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`;
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/20260923T013147Z-bf13c29b/REPORT.md`.

It states: if a scalar `S` of density cap `K` is genuinely independent of a pair `(C,D)` whose arbitrary joint density has cap `M`, and a symmetric three-variable quadratic matrix has zero `S^2` pivot and nonzero determinant `Delta`, then, after an orthogonal rotation inside the pair,

`||p_Q||_infinity <= 3(2 M K)^(2/3) |Delta|^(-1/3)`.              (1)

The pair coordinates need not be independent.

## 2. Primary theorem and exact hypothesis match

Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), Theorem 1.1, applies to an actual product density `prod f_i`, with every `f_i` a one-dimensional probability density and `||f_i||_infinity<=1`. For every `k`-dimensional orthogonal marginal it gives cap at most `2^(k/2)`. No moment, iid, compact-support, log-concavity, smoothness, centering or symmetry hypothesis is added.

I use it only on disjoint ORIGINAL-coordinate Hadamard banks. It supplies a joint density cap; it is never interpreted as independence after rotation.

## 3. Four exact source banks

Because the Hadamard matrix is normalized, its first column is constant and the next two columns are mutually orthogonal and orthogonal to the first. Hence their four sign patterns occur equally often. Writing

`a_st=(1,s,t)`,  `s,t in {+1,-1}`,

there are exactly `m/4` residual rows of each form

`m^(-1/2) a_st H`                                                   (2)

in `(n,beta,e)` coordinates.

For each sign bank define the ORIGINAL-coordinate aggregate

`Z_st = m^(-1/2) sum_{j in bank(st)} X_j`.                           (3)

The four `Z_st` are genuinely mutually independent, and independent of the hub and distinguished leaf, because their source sets are disjoint.

For any two distinct banks, `(2 Z_st,2 Z_uv)` is an orthogonal two-dimensional projection of their union of original input coordinates: each coefficient row has Euclidean norm one, their supports are disjoint, and hence the two rows are orthogonal. LPP therefore gives

`||p_(2Z_st,2Z_uv)||_infinity <=2`,

so by two-dimensional scaling

`||p_(Z_st,Z_uv)||_infinity <=8`.                                  (4)

This is uniform in `m` and in all admissible rough input laws. (For the endpoint where the selected union has exactly two source coordinates, the product density itself gives an even smaller cap; (4) remains valid.)

## 4. Determinant amplification from the four Walsh rays

Use active spectral coordinates `(p,n,beta)`, in which the quadratic matrix is

`D=[[0,1,0],[1,0,0],[0,0,1]]`,  `det D=-1`.                         (5)

For a residual row, the deterministic coordinate change from `(n,beta,e)` to `(p,n,beta)` is

`T=[[0,1,0],[0,0,1],[c,0,0]]`,  `det T=c`.                          (6)

Thus the effective active row multiplying `Z_st` is

`b_st=a_st H T`,                                                    (7)

while the distinguished leaf row is `u_*=r T`.

Now use the exact partner identity `||r||^2=1-eta^6`. Since

`G=I-r r^T`,

we have

`G r=eta^6 r`, `H r=eta^3 r`, `det H=eta^3`.                        (8)

Therefore for any two sign banks

`det[u_*;b_st;b_uv]
 = c det[r;a_st H;a_uv H]
 = c det[r;a_st;a_uv]`.                                             (9)

The small singular value `eta^3` of the residual Gram matrix cancels exactly: the first row contributes the reciprocal factor because `r H=eta^3 r`.

For the four vectors

`(1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1)`,

a direct exterior-frame identity gives

`sum_{unordered bank pairs} det[r;a_st;a_uv]^2
 =16 ||r||^2
 =16(1-eta^6)`.                                                     (10)

Equivalently, the six determinants are

`2(-x+y), 2(x-z), 2(y-z), -2(y+z), -2(x+z), 2(x+y)`,

whose squared sum is (10). Hence some pair of banks satisfies

`|det[u_*;b_st;b_uv]|^2
 >= (8/3)c^2(1-eta^6)
 = (8/3)(1-eta^2)(1-eta^6)`.                                       (11)

Let `B_*st,uv` be the symmetric quadratic matrix in the three retained variables `(X_*,Z_st,Z_uv)`. Since it equals `R D R^T` for the three-row matrix in (11),

`|det B_*st,uv|
 = |det R|^2 |det D|
 >= (8/3)(1-eta^2)(1-eta^6).                                       (12)

The distinguished scalar pivot is exactly zero because the partner construction has `A_**=0`.

## 5. Conditioning is legitimate and affine terms do not matter

Condition on the hub and on all original coordinates belonging to the two unselected Hadamard banks. The selected variables are still:

- the original distinguished scalar `X_*`, density cap `K=1`;
- the selected pair `(Z_st,Z_uv)`, independent of `X_*`, with joint cap `M<=8` by (4).

Every conditioned cross term becomes only an affine term in the selected triple. Because (12) makes the retained three-variable quadratic matrix invertible, a deterministic translation by `(1/2)B_*st,uv^(-1)` times the affine coefficient removes those linear terms. Such deterministic translations preserve the scalar-versus-pair independence and all density caps, and do not change the zero quadratic pivot or determinant. Thus the fleet02/B18 receiver (1) applies uniformly in the conditioning.

Substituting `K=1`, `M=8`, and (12),

`||p_Q||_infinity
 <= 3*16^(2/3) * [(8/3)(1-eta^2)(1-eta^6)]^(-1/3).`                 (13)

For the partner stress range `0<eta<1/64`, the right side is strictly below its endpoint value

`3*16^(2/3) * [(8/3)(1-1/64^2)(1-1/64^6)]^(-1/3)
 = 13.7376889776911...`.                                            (14)

Averaging the uniform conditional density bound gives the same bound unconditionally.

### Theorem `QFORM-EQUAL-SPECTRUM-LOWHUB-HADAMARD-CLOSURE-v1`

For every normalized-Hadamard residual completion in the fleet02/B18 low-hub stress construction, every `0<eta<1/64`, and arbitrary independent original-coordinate input densities bounded by one,

`boxed: ||p_(X^T A X)||_infinity < 13.738.`                          (15)

The physical matrix has exact nonzero spectrum `{-1,1,1}`, so this is a genuine target-valid family. The result is whole-line; it includes the previously difficult minority-sign/two-sheet side.

## 6. What this proves and what it does not

The partner's newest low-hub stress family demonstrates a real failure of several local compilers as `h=eta^2 ->0`. The calculation above shows that the stress is nevertheless uniformly paid once its actual normalized-Hadamard product-source geometry is used: two of the four independent source banks and the null distinguished leaf always carry a determinant of constant size after aggregation.

Thus this explicit stress family is removed as a density obstruction. The remaining low-hub debt is more precise: **arbitrary residual source geometry** need not come with four exact equal Walsh banks. A full proof still needs either a product-preserving bank extraction that recovers a determinant like (12), or another receiver that handles the non-bank low-hub two-sheet configuration. This report does not establish such a decomposition for arbitrary `A`, does not touch arbitrary extra spectrum, and does not prove the full conjecture.

Continuity is kept separate. The scalar/dependent-pair weak-L^(3/2) argument proves essential boundedness; I do not promote it to a continuous representative here.

## 7. Correction audit

No arbitrary-joint coarea bound, conditional-cap-as-independence step, post-rotation independence, pointwise universal quadratic-phase decay, perturbative deletion of a small coefficient, fixed universally good physical minor, or interval-to-Borel transfer is used. The only random independence invoked is between disjoint sets of ORIGINAL coordinates.

Primary literature used: Livshyts--Paouris--Pivovarov, arXiv:1507.07949 / Israel J. Math. 216 (2016), Theorem 1.1. The theorem's product-density hypotheses exactly match the bank sources here.

Privacy/source check before publication: changed files contain only mathematical formulas, public bibliographic data, repository-internal source pins and nonsecret run metadata; no credentials, signed URLs, personal data or unrelated private material. No public-release or permission action was taken.
