SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-24T10:47:55Z.
attacking: exact zero-pivot one-anchor packets by lifting the weighted product-Fourier pair law from rank one to arbitrary finite residual rank, with an explicit rank-two target stress test.

# account03/B04 r56 — higher-rank weighted zero-pivot Fourier receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: **NEW SUPPORTING THEOREM PENDING INDEPENDENT REVIEW / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Regularity: the theorem below has an integrable characteristic-function majorant, hence gives a continuous density vanishing at infinity (`C_0`) on its stated branch. The unrestricted continuity question remains open.

Fresh control at startup was `yspennstate/math-research-brain@9009f7546727946cc924bb65ca2509a480d2637e`, OWNER CONTROL revision `2026-09-22.15`, QFORM-only. The same-hour canonical B04 login already existed and was preserved rather than duplicated. The live corrections were read before this argument. In particular, nothing below uses law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea, conditional projection caps after rotation, worst-fibre suprema, or deletion of a small nonzero random coefficient.

## 1. Source-valid input and mechanism change

The immediate B04 predecessor is

`yspennstate/math-open-problems@8943de4ce7adbeef5a110d0bf0fc634b2fce39c5`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260924T101932Z-account03-B04-QFORM-auto11-r55/REPORT.md`.

It pays an inverse-free one-hub projected-`E_2` packet, including the exact-zero scalar-pivot face, but still needs a structural projected two-volume.

The mechanism seed for the present run is the completed account02/B04 rank-one theorem

`yspennstate/math-open-problems@2311fa678098f3ac7b96e5eb3795d9def07cc2fd`,

which proves the weighted zero-pivot `J_1` receiver for a diagonal-plus-rank-one residual. The proof below lifts that product-space construction to an arbitrary exact residual rank `r>=1`. For `r=1` the constant and exponent reduce exactly to the completed account02/B04 theorem; for `r>=2` the result is genuinely new.

## 2. Main theorem — `QFORM-ZEROPIVOT-RANKR-WEIGHTED-VOLUME-v1`

Fix one literal ORIGINAL coordinate `h` and a disjoint original-coordinate bank `I`. Condition on every coordinate outside `{h} union I`. Assume

`A_hh=0`,

and that the retained principal block has an exact decomposition

`A[I,I] = D + V Lambda V^T`,                                      (2.1)

where `D` is diagonal, `V^T V=I_r`, and

`Lambda=diag(lambda_1,...,lambda_r)`, `lambda_k !=0`.             (2.2)

Put

`d=r+1`,
`a_i=A_ih`,
`z_i=(a_i, sqrt(|lambda_1|)V_i1, ..., sqrt(|lambda_r|)V_ir)
     in R^d`.                                                       (2.3)

For every physical `d`-set `P subset I`, define

`c_P = det(z_i : i in P)^2`.                                      (2.4)

Define the ordered disjoint-volume packet

`J_r(h,I)
 = sum_{|P|=|Q|=d, P cap Q=empty} c_P c_Q`.                       (2.5)

### Theorem 2.1

If `J_r(h,I)>0`, then for every admissible independent cap-one product input, with arbitrary affine terms induced by the conditioned outside coordinates, the full ambient quadratic form has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= C_r J_r(h,I)^(-1/(2(r+2))),
 C_r = 4 (r+2)/r * 2^(-2/(r+2)).`                                (2.6)

The first constants are

`C_1=3*2^(4/3)=7.559526299369239...`,
`C_2=4*sqrt(2)=5.656854249492381...`,
`C_3=5.052388555034661...`.                                      (2.7)

The estimate is determinant-homogeneous: scaling every coefficient of the quadratic form by `s` scales `J_r` by `|s|^(2(r+2))`, so the right side scales by `|s|^(-1)` as a density bound must.

## 3. Exact physical meaning of the currency

For disjoint `d`-sets `P,Q`, the diagonal matrix `D` has no `P x Q` entries. Hence the anchored physical `(r+2)x(r+2)` minor is

`M_(P,Q)=A[{h} union P, {h} union Q]
 = [[0, a_Q^T],
    [a_P, V_P Lambda V_Q^T]].`                                   (3.1)

Let `L_P=[a_P,V_P]` and `L_Q=[a_Q,V_Q]`. Factoring through the central matrix

`C_0 = [[0,1,0],
       [1,0,0],
       [0,0,Lambda]]`                                            (3.2)

(with the lower-right block of size `r`) gives

`det M_(P,Q) = - det(Lambda) det(L_P) det(L_Q)`                  (3.3)

up to the irrelevant orientation sign. Since

`c_P = |det Lambda| det(L_P)^2`,                                 (3.4)

we obtain the exact identity

`boxed: det A[{h} union P,{h} union Q]^2 = c_P c_Q.}`            (3.5)

Therefore `J_r(h,I)` is not an invented analytic norm: it is exactly the disjoint-pair portion of the one-anchor physical `(r+2)`-compound packet carried by this diagonal-plus-rank-`r` residual.

## 4. Product-space law and the half-marginal threshold

Write `J=J_r(h,I)>0` and put a probability law on ordered disjoint `d`-set pairs by

`mu(P,Q)=c_P c_Q/J`.                                              (4.1)

Let `w` be the first marginal and

`alpha_i = P_w(i in P)`.                                         (4.2)

The law `mu` is symmetric under `(P,Q)<->(Q,P)`. Because `P cap Q=empty`,

`2 alpha_i
 = E_mu[1_(i in P)+1_(i in Q)] <=1`,                            (4.3)

so every physical row marginal obeys the exact product-Fourier threshold

`boxed: alpha_i<=1/2.`                                            (4.4)

Also `sum_i alpha_i=d`.

Define the determinant-entropy currency

`G(w)=exp(sum_P w_P log c_P + H(w)).`                             (4.5)

Since `H(mu)<=H(P)+H(Q)=2H(w)` while

`H(mu)=log J -2 sum_P w_P log c_P`,                              (4.6)

we get

`boxed: G(w)>=sqrt(J).}`                                          (4.7)

This aggregation occurs before any reciprocal minor is paid.

## 5. Fourier proof and explicit constant

After the outside conditioning, diagonal curvature and affine terms on each original coordinate `X_i`, `i in I`, are absorbed into scalar phase twists

`g_i(x)=exp(i t D_ii x^2+i ell_i x) f_i(x)`,

so `|g_i|<=f_i`, `||g_i||_1=1`, `||g_i||_infinity<=1`.

The zero hub contributes the linear phase

`2t X_h sum_i a_i X_i`.

Integrating the literal hub by the change of variable `y=2tX_h` uses only `f_h<=1` and contributes

`(2|t|)^(-1)`.                                                     (5.1)

For each nonzero rank direction, use the exact Fresnel representation of

`exp(i t lambda_k <v_k,X_I>^2)`.

Taking absolute values only after this identity contributes

`(4 pi |t lambda_k|)^(-1/2)`                                    (5.2)

and introduces one deterministic Fourier variable. After all `r` linearisations the remaining integral is `d=r+1` dimensional and has the Brascamp--Lieb form

`int_(R^d) prod_i |hat(g_i)(<rho_i,u>+s_i)| du`,                  (5.3)

where `rho_i=(a_i,V_i1,...,V_ir)`. For the physical law `w` above, Cauchy--Binet plus weighted AM-GM gives

`det(sum_i d_i rho_i rho_i^T)
 >= G_rho(w) prod_i d_i^(alpha_i)`.                              (5.4)

The cap-one Hausdorff--Young/rearrangement bound used in the completed rank-one source gives, because `alpha_i<=1/2`,

`||hat(g_i)||_(1/alpha_i)
 <= (4 pi sqrt(alpha_i))^(alpha_i).`                             (5.5)

The `alpha_i` powers cancel the Gaussian Brascamp--Lieb factors, and since `sum alpha_i=d`,

`(5.3) <= (4 pi)^d G_rho(w)^(-1/2).`                             (5.6)

Scaling the `r` rank coordinates by `sqrt(|lambda_k|)` gives

`G(w)=|det Lambda| G_rho(w)`.                                    (5.7)

Thus all `lambda_k` prefactors cancel exactly and

`|phi_Q(t)|
 <= min{1,
    (1/2)(4 pi)^((r+2)/2) G(w)^(-1/2)
    |t|^(-(r+2)/2)}.`                                           (5.8)

Put

`beta=(r+2)/2>1`,
`K=(1/2)(4 pi)^beta G(w)^(-1/2)`.                               (5.9)

Exact integration gives

`int_R min(1,K|t|^-beta) dt
 = 2 beta/(beta-1) K^(1/beta).`                                 (5.10)

Fourier inversion therefore yields

`||p_Q||_infinity
 <= [beta/(pi(beta-1))] K^(1/beta)
 = 4(r+2)/r * 2^(-2/(r+2)) G(w)^(-1/(r+2)).`                   (5.11)

Finally (4.7) gives (2.6). Since beta>1, the majorant is integrable and Fourier inversion gives a continuous density vanishing at infinity. No scalar pointwise quadratic-phase decay was used. QED.

### Regression check at rank one

For `r=1`, (2.6) becomes

`||p_Q||_infinity
 <=3*2^(4/3) J_1(h,I)^(-1/6)`,                                  (5.12)

exactly the completed account02/B04 weighted zero-pivot theorem. This is an internal consistency check on both the exponent and the constants.

## 6. New rank-two target branch, strictly beyond diagonal plus rank one

Take one physical hub `h` and residual coordinates indexed by `i=1,...,6`. Define

`A_hh=0`,
`A_hi=A_ih=i^2`,
`A_ij=2 delta_ij + 1 + i j` for `1<=i,j<=6`.                     (6.1)

The residual principal block is

`R=2I + 1 1^T + w w^T`, `w=(1,2,3,4,5,6)^T`,                    (6.2)

so it is diagonal plus exact rank two. It is positive definite with `R>=2I`. Interlacing with this `6x6` principal block gives the six largest eigenvalues of the full `7x7` matrix at least `2`. The Schur complement of `R` is

`-a^T R^(-1)a<0`,                                                 (6.3)

so the full matrix is nevertheless indefinite. All off-diagonal physical coefficients are nonzero. Thus this is a genuinely non-diagonal, genuinely indefinite owner-target matrix.

Here

`z_i=(i^2,1,i)`.                                                   (6.4)

Every triple determinant is the Vandermonde product

`det(z_i,z_j,z_k)
 = +/- (j-i)(k-i)(k-j)`.                                         (6.5)

Summing over ordered disjoint triples gives exactly

`boxed: J_2(h,I)=331904.}`                                       (6.6)

The rank-two theorem therefore gives

`boxed:
 ||p_(X^T A X)||_infinity
 <=4 sqrt(2) * 331904^(-1/8)
 =1.154644864670688... .}`                                       (6.7)

The density is continuous and in `C_0` for every admissible independent cap-one product law.

This example is genuinely outside the rank-one residual theorem. If its off-diagonal residual were representable by one rank-one outer product, the tetrad identity would hold. Instead

`(1+1*2)(1+3*4)=3*13=39`,

while

`(1+1*3)(1+2*4)=4*9=36`.                                        (6.8)

So no change of the residual diagonal can reduce (6.2) to diagonal plus rank one.

The deterministic checker verifies all anchored minor identities (3.5) on this matrix, the exact value (6.6), the tetrad obstruction, and the numerical constant. No Monte Carlo evidence is used.

## 7. Designated partner account04/B04 applied to a new actual inequality

The newest completed designated partner remains account04/B04 r2,

`yspennstate/math-open-problems@4a54666abf2316bb79b939cef3ea940605a0af57`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B04/20260924T001353Z-account04-B04-QFORM-r2/REPORT.md`.

Its entropy branch is applied here to a new literal dense `6x4` cross block

`M = [[5,3,3,4],
      [3,5,5,3],
      [1,2,4,5],
      [1,2,1,4],
      [5,4,5,5],
      [3,4,1,2]].`                                               (7.1)

For the second physical row `i=2` (zero-based row index one), exact fourth-volume enumeration gives

`E_4(M)=165775`,
`H_i=137045`,
`rho_i=27409/33155`,                                             (7.2)

and the largest anchored conditional row marginal is

`beta_*=90786/137045 < 2/3`.                                     (7.3)

Thus the partner's entropy-payment branch applies with

`q=2 beta_*=181572/137045`,
`||m_i||_2^2=68`,
`G_i>=H_i/68`.                                                    (7.4)

Its actual same-matrix inequality is therefore

`boxed:
 ||p_Q||_infinity
 <= [3e/((3-2q)sqrt(q))] (137045/68)^(-1/6)
 =5.692467732262831... .}`                                       (7.5)

This partner branch has a continuous `C_0` density.

To verify that (7.5) lies inside the owner target rather than being only an abstract block calculation, take the pure-cross symmetric matrix

`A_dagger=[[0,M],[M^T,0]].`                                      (7.6)

The leading principal minors of `M^T M-I_4` are exactly

`69, 681, 8451, 107715`,                                         (7.7)

so `M^T M-I_4` is positive definite by Sylvester. Hence all four singular values of `M` exceed one, and `A_dagger` has eight eigenvalues of modulus greater than one, with both signs. Every entry of the physical cross block is nonzero. This is an equation-level use of the designated partner theorem on a strict target matrix, not a generic restatement of its branch condition.

## 8. Boundary and next implication

This theorem does **not** solve the unrestricted QFORM conjecture. Its structural hypothesis is exact: the zero-pivot residual principal block must be diagonal plus finite rank `r`, and `J_r(h,I)` must be positive. In particular, the live correction forbidding deletion of a merely small nonzero quadratic term is respected; this report makes no perturbative claim from `A_hh=0` to `|A_hh|<<1`.

What the theorem changes is the finite-rank zero-pivot endpoint. A residual rank two, three, or higher is no longer required to collapse to rank one before the weighted Fourier/entropy mechanism can be used. The next B04 debt is therefore

`QFORM-OVERLAP1-RESIDUAL-LOWRANK-OR-PROJECTED-E2-v1`:

from a surviving localized one-anchor packet, force either (i) an exact/structurally isolated diagonal-plus-rank-`r` residual bank with target-scale `J_r`, now paid by Theorem 2.1, or (ii) a genuinely second-exterior projected packet paid by r55 / critical-`E_2` / ridge / grouped-crossing machinery, while retaining any nonzero residual tail rather than deleting it.

Full QFORM remains OPEN. Full-target continuity remains OPEN separately. Execution remains `WITHOUT_VERIFIED_BRAIN`; repository retrieval/writeback is not authenticated native brain receiver use. No scheduler state, task identity, email/push notification, public release, paid model/API call, or cross-account authentication state was changed.
