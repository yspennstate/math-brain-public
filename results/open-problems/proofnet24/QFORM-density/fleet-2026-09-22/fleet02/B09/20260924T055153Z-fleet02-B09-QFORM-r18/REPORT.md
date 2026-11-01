SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B09, 2026-09-24T05:51:53Z.
attacking: the small-pair survivor by retaining one physical hub density inside mixed-hub Brascamp--Lieb, so a leverage-one hub row can be paid without conditioning away that hub and without square-root decoupling.

# fleet02/B09 r18 -- retained-hub Brascamp--Lieb and the leverage-one hub endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism / complementary constructions and source-valid obstructions  
Run: `20260924T055153Z-fleet02-B09-QFORM-r18`  
Status: **NEW SUPPORTING THEOREM / MIXED-HUB LEVERAGE ENDPOINT EXTENDED / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

All variables below are literal ORIGINAL source coordinates. Inputs are arbitrary independent real random variables with probability densities bounded by one. No moment, compact-support, connected-support, iid, Gaussian, log-concavity, diagonal-basis, or post-rotation-independence assumption is made. No small coefficient is deleted. Continuity is asserted only in the branches where the characteristic function is proved integrable.

## 1. First unpaid implication

The immediate B09 structural debt is now

`QFORM-SMALLPAIR-TO-RETAINED-HUB-FRAME-OR-GROUPEDCROSSING-v1`.

The previous source-valid obstruction showed that the bare three-large-eigenvalue hypothesis cannot force a universal physical-pair scalar/star resource: a diffuse mixed frame can stay uniformly smooth while every individual pair resource, and even the sum of the best such resources, tends to zero. Therefore pair selection must be preceded by an aggregate routing step.

This run removes a second obstruction inside that aggregate route. Pinned mixed-hub Theorem H discarded every hub density by `f_h<=1`; consequently a single physical leaf row of mixed-frame leverage greater than `1/2` blocks its Brascamp--Lieb gate. The new theorem keeps selected hub densities inside the same BL integral. Those retained densities act as extra coordinate rows in the frame and can reduce hub-direction leverage, at the cost of only part of a Fourier power. In the two-hub plus one leaf-square regime, retaining one hub can still leave an integrable power.

The remaining unpaid implication is structural rather than this analytic endpoint: from `s_3(A)>=1` and failure of the already-paid physical-pair branches, force either (i) a source-coordinate low-rank-plus-diagonal mixed packet for which the augmented retained-hub frame below has universal determinant and leaf leverage `<=1/2`, or (ii) an already-paid grouped-crossing/volume exit. General dense curvature on the same active leaf bank remains the hard routing issue.

## 2. Source theorem being extended

Use the completed pinned mixed-hub theorem from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

Its setup is a coordinate split `H union I union J`, with

`A_II = D + sum_{k=1}^r lambda_k v_k v_k^T`,                         (2.1)

where `D` is diagonal, and physical mixed rows

`rho_i=((v_1)_i,...,(v_r)_i, A_{ih}:h in H) in R^(r+|H|)`.           (2.2)

If the mixed Gram is positive definite and every normalized leaf leverage is at most `1/2`, Theorem H gives an undecoupled Fourier power `|H|+r/2`; the blocks `A_HH,A_HJ,A_IJ,A_JJ` are arbitrary. Its proof uses Fresnel linearisation, the cap-one `L^p` characteristic-function lemma, and geometric Brascamp--Lieb.

The extension below changes only one step: selected hub densities are retained rather than replaced by one.

## 3. New theorem -- retained-hub Brascamp--Lieb

### Theorem 3.1 -- `QFORM-RETAINED-HUB-BRASCAMP-LIEB-v1`

Let `H,I,J` be disjoint original-coordinate banks, let `h=|H|`, and suppose (2.1) holds with every `lambda_k!=0`. Put

`d=r+h`,

and use the mixed rows (2.2). Choose any subset `S subset H`. For each `a in S`, let `e_a in R^d` be the standard basis vector corresponding to that hub component and define the **augmented mixed Gram**

`Gbar = sum_{i in I} rho_i rho_i^T + sum_{a in S} e_a e_a^T`.         (3.1)

Assume `Gbar>0`. Define

`c_i = rho_i^T Gbar^(-1) rho_i`,                                      (3.2)

`b_a = e_a^T Gbar^(-1) e_a`,                                         (3.3)

`B = sum_{a in S} b_a`,                                               (3.4)

and suppose

`c_i <= 1/2` for every `i in I`.                                      (3.5)

Finally set

`alpha = h + r/2 - B`.                                                (3.6)

If `alpha>1`, then the full ambient quadratic form, with arbitrary blocks `A_HH,A_HJ,A_IJ,A_JJ` and arbitrary affine terms, has an integrable characteristic function and a continuous density. For every `t!=0`,

`boxed:`
`|phi_Q(t)| <= K |t|^(-alpha)`,                                      (3.7)

where

`K = [prod_{a in S} b_a^(-b_a/2)]`
`    * 2^(-h+B) (4 pi)^alpha`
`    * [prod_{k=1}^r |lambda_k|]^(-1/2)`
`    * det(Gbar)^(-1/2).`                                             (3.8)

Consequently

`boxed:`
`||p_Q||_infinity <= alpha/[pi(alpha-1)] * K^(1/alpha).`              (3.9)

Equivalently,

`||p_Q||_infinity`
` <= 4 alpha/(alpha-1) 2^((-h+B)/alpha)`
`    [prod_{a in S} b_a^(-b_a/2)]^(1/alpha)`
`    [det(Gbar) prod_k |lambda_k|]^(-1/(2alpha)).`                    (3.10)

The identical coefficient bounds `P(Q in L)/|L|` for every interval `L`.

When `S` is empty, `B=0`, `Gbar` is the original mixed Gram, and (3.7) is exactly the pinned Theorem-H power/counting formula. Thus this is a literal extension of that mechanism, not a separate decoupling argument.

## 4. Proof

Condition on the outside bank `X_J`. All `J`-dependence becomes an affine tilt or a hub-only phase; the quadratic part on `I` is still (2.1). For fixed hub coordinates `x_H`, write the `I`-expectation as `Phi_I`. Taking absolute values only after the `I`-expectation gives

`|phi_Q(t)|`
` <= int_{R^h} prod_{a in H} f_a(x_a)`
`       |Phi_I(t;2 A_IH x_H + fixed)| dx_H`.                          (4.1)

Apply the pinned Fresnel linearisation to the rank-`r` part of (2.1). For the diagonal twist and affine terms define complex one-coordinate densities `g_i` with `|g_i|<=f_i`. After the change

`y=2t x_H`,                                                             (4.2)

one obtains

`|phi_Q(t)|`
` <= (2|t|)^(-h) prod_k (4 pi |t lambda_k|)^(-1/2)`
`    * int_{R^d} prod_{i in I} |hat g_i(<rho_i,z>+s_i)|`
`      prod_{a in H} f_a(y_a/(2t)) dz`.                               (4.3)

For hubs `a notin S`, use only `f_a<=1`. The factors with `a in S` are retained.

Now change variables `z=Gbar^(-1/2)w`. Put

`u_i=Gbar^(-1/2)rho_i/sqrt(c_i)`,
`v_a=Gbar^(-1/2)e_a/sqrt(b_a)`                                        (4.4)

for nonzero weights. From (3.1),

`sum_i c_i u_i u_i^T + sum_{a in S} b_a v_a v_a^T = I_d`.            (4.5)

Also every `b_a<=1`: after whitening, deleting one summand leaves a positive semidefinite matrix, so `I_d-b_a v_a v_a^T>=0`.

Apply geometric Brascamp--Lieb to (4.3). For a leaf row with `c_i>0`, write

`|hat g_i(s_i+sqrt(c_i)s)| = F_i(s)^(c_i)`,

`F_i(s)=|hat g_i(s_i+sqrt(c_i)s)|^(1/c_i)`.                           (4.6)

Because `c_i<=1/2`, the pinned cap-one Fourier lemma applies with `p=1/c_i>=2`:

`int |hat g_i(xi)|^(1/c_i) dxi <= 4 pi sqrt(c_i)`.                    (4.7)

Therefore

`int F_i <= c_i^(-1/2) * 4 pi sqrt(c_i) = 4 pi`.                     (4.8)

Translations `s_i` do not matter. Rows with `c_i=0` have `rho_i=0` and their Fourier factors are at most one.

For a retained hub, write

`f_a(sqrt(b_a)s/(2t)) = H_a(s)^(b_a)`,

`H_a(s)=f_a(sqrt(b_a)s/(2t))^(1/b_a)`.                               (4.9)

Since `b_a<=1`, `1/b_a>=1`, and `0<=f_a<=1`,

`int H_a(s) ds`
` = 2|t| b_a^(-1/2) int f_a(x)^(1/b_a) dx`
` <= 2|t| b_a^(-1/2).`                                               (4.10)

Brascamp--Lieb, (4.8), and (4.10) give

`int ... dz`
` <= det(Gbar)^(-1/2)`
`    (4 pi)^(sum_i c_i)`
`    (2|t|)^B prod_{a in S} b_a^(-b_a/2).`                            (4.11)

Taking traces in (4.5),

`sum_i c_i = d-B = r+h-B`.                                            (4.12)

Substituting (4.11)-(4.12) into (4.3) yields exactly (3.7)-(3.8), with Fourier exponent

`h-B+r/2 = alpha`.                                                     (4.13)

No Cauchy--Schwarz/Weyl differencing or probability squaring occurs.

If `alpha>1`, combine (3.7) with `|phi_Q|<=1`. With `T=K^(1/alpha)`,

`int_R min(1,K|t|^(-alpha)) dt`
` = 2 alpha/(alpha-1) K^(1/alpha).`                                   (4.14)

Fourier inversion gives (3.9); `phi_Q in L^1` gives the continuous density. This proves the theorem. `square`

## 5. Exact leverage-one hub-coloop corollary

The simplest genuinely new endpoint occurs for two hubs and one dense leaf square: `h=2,r=1`. Suppose the unaugmented mixed Gram is `I_3` and one physical leaf row is exactly one hub basis vector, say

`rho_0=e_U`.                                                           (5.1)

Then its original mixed leverage is **one**, so pinned Theorem H cannot use the full leaf bank. Retain the density of that same physical hub `U`, i.e. `S={U}`. Then

`Gbar=I_3+e_Ue_U^T`,
`det Gbar=2`,
`b_U=1/2`,
`alpha=2`,                                                             (5.2)

and the former coloop row now has augmented leverage exactly `1/2`. Thus a leverage-one obstruction in a pure hub direction can be paid without deleting the physical row and without reciprocal minor selection. The cost is only half a Fourier power: the original formal exponent `5/2` becomes the still-integrable exponent `2`.

For `lambda=1`, (3.7) becomes

`|phi_Q(t)| <= 2^(9/4) pi^2 |t|^(-2)`,                               (5.3)

and therefore

`boxed: ||p_Q||_infinity <= 2^(17/8) = 4.362030930661031... .`        (5.4)

## 6. Actual source-coordinate target family with dense same-side coupling

Let `m=2^k>=8`. On a literal leaf bank `T` of size `m`, choose two flat orthonormal Walsh vectors `d,q`. Add one literal leaf coordinate `Y_0`, and let `U,V` be two literal hubs. Define

`Q_m`
` = 2 U Y_0`
`   + 2 V <d,Y_T>`
`   + <q,Y_T>^2`.                                                      (6.1)

The same-side leaf block `q q^T` is dense on `T` in the original coordinates. Arbitrary diagonal terms on the active leaf bank and arbitrary additional blocks/couplings on a disjoint conditioned bank may be retained within Theorem 3.1's scope.

### 6.1 Owner-target spectrum

The five vectors/coordinates

`U, Y_0, V, d, q`                                                      (6.2)

are orthonormal at the coefficient-space level, and the active matrix is

`[[0,1],[1,0]] direct_sum [[0,1],[1,0]] direct_sum [1]`.              (6.3)

Hence

`spec_nonzero(A_m)={-1,-1,1,1,1}`.                                   (6.4)

This is a genuine owner-target family for every `m`. Moreover any full matrix having this as a principal block still has at least three eigenvalues of modulus at least one by interlacing.

### 6.2 Why the original full-frame Theorem-H gate fails

Take `I={Y_0} union T`, `H={U,V}`, `r=1`, `v_1=q`. The mixed rows, in the order `(q,U,V)`, are

`rho_0=(0,1,0)`,
`rho_i=(q_i,0,d_i)` for `i in T`.                                     (6.5)

Because `q,d` are orthonormal,

`G=sum_i rho_i rho_i^T=I_3`.                                         (6.6)

Thus the physical row `0` has normalized leverage

`rho_0^T G^(-1)rho_0=1`,                                             (6.7)

maximally outside the pinned `<=1/2` gate. Conditioning away `Y_0` removes the entire `U` direction from this two-hub mixed frame.

### 6.3 New retained-hub estimate

Retain the density of hub `U`. Then

`Gbar=diag(1,2,1)`, `b_U=1/2`, `det Gbar=2`.                          (6.8)

The row `0` leverage becomes `1/2`. Every row on `T` has augmented leverage

`q_i^2+d_i^2=2/m<=1/4`                                                (6.9)

for `m>=8`. Therefore Theorem 3.1 applies and gives (5.3)-(5.4):

`boxed:`
`||p_(Q_m)||_infinity <= 2^(17/8) < 4.363`,                           (6.10)

`boxed:`
`P(Q_m in L) <= 2^(17/8)|L|`                                         (6.11)

for every interval `L` and every admissible independent cap-one source law. The density is continuous in this branch.

## 7. Required direct application of the pinned result

The pinned theorem is also applied directly, without the new extension, to a real inequality on the same source family. Condition on the literal pair `(U,Y_0)`. The remaining form on `(V,Y_T)` is

`2 V <d,Y_T> + <q,Y_T>^2 + affine/constant terms`.                    (7.1)

Use pinned Theorem H with one hub, one leaf square, mixed rows `(q_i,d_i)`, Gram `I_2`, and leverage `2/m<=1/2`. Its Fourier bound is

`|phi(t)| <= (1/2)(4 pi)^(3/2)|t|^(-3/2)`.                           (7.2)

Integrating `min(1,K|t|^(-3/2))` gives

`boxed:`
`||p_(Q_m)||_infinity <= 12*2^(-2/3) = 7.559526299369238... .`        (7.3)

This is already a linear interval bound and retains the dense same-side square. The new retained-hub theorem uses the extra physical hub smoothing that (7.1) discards and improves this concrete inequality from `7.560` to `4.363`.

## 8. Latest designated partner applied to an actual inequality

The latest completed fleet03/B09 result is r44,

`yspennstate/math-open-problems@1d81e62c818d6b592a6a6da78870f12f533d615a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260924T044555Z-fleet03-B09-QFORM-r44/REPORT.md`.

Its theorem `QFORM-INDEFINITEPAIR-SCHURSTAR-UNIFORM-v1` says that for a literal invertible indefinite pair with

`D=|det B|`, `kappa=sigma_min(B)`,                                    (8.1)

and an exact Schur remainder containing one literal scalar with nonzero star row `m`,

`||p_Q||_infinity`
` <= 14.4199290072 [D kappa ||m||_2]^(-1/4)`,                         (8.2)

uniformly through a zero or nonzero scalar Schur coefficient.

Apply it to the literal pair `(U,Y_0)` in (6.1):

`B=[[0,1],[1,0]]`, so `D=kappa=1`.                                   (8.3)

That pair is uncoupled from `V`, while `V` retains the exact star `d` into `T`, hence the post-completion star norm is `||m||=||d||=1`; the dense phase `<q,Y_T>^2` remains inside the arbitrary same-bank term. Therefore r44 gives the genuine target inequality

`boxed:`
`||p_(Q_m)||_infinity <= 14.4199290072`,                              (8.4)

with the same coefficient multiplying interval length. This checks the pair endpoint on the same physical example. The retained-hub BL estimate (6.10) is stronger because it spends the pair/hub smoothing and the leaf-square smoothing jointly before any physical pair is completed.

## 9. What this changes structurally

There are now two complementary B09 obstructions to pair-first proof architecture.

First, the preceding diffuse family shows that all physical-pair scalar/star resources may vanish with dimension while an ordinary diffuse mixed frame has a universal bound. Second, the present family shows that even the mixed-frame leverage gate itself can fail maximally (`leverage=1`) for a physical row that is purely a hub coloop; retaining the associated hub density repairs that endpoint and still leaves an integrable `t^-2` envelope.

Thus a structural compiler should not insist on either a large physical pair or a fully diffuse leaf-only mixed frame. It may route hub-heavy rows into **retained hub-density rows** of the Brascamp--Lieb datum. Quantitatively, the relevant currency is the augmented Gram (3.1), the leaf leverages (3.2), and the surviving exponent `alpha=h+r/2-B`, not solely a physical determinant or the unaugmented leverage.

The still-unpaid difficulty is to force a universal-scale augmented packet from an arbitrary matrix with `s_3(A)>=1` while preserving arbitrary same-bank curvature. Small Frobenius/operator norm of a leftover quadratic block is not a probabilistically small perturbation under arbitrary unbounded cap-one laws, so that route remains forbidden.

## 10. Counterexample status

The required pinned counterexample search reports no valid counterexample to the unrestricted conjecture, and the current master continuation of that source still reports none. This run found no QFORM counterexample. The construction (6.1) is instead a source-valid obstruction to the narrower claim that the pinned mixed-hub theorem's original leaf-leverage gate is analytically final.

Full QFORM remains OPEN. Full-target continuity remains OPEN; continuity is proved here only for Theorem 3.1 branches with `alpha>1`.
