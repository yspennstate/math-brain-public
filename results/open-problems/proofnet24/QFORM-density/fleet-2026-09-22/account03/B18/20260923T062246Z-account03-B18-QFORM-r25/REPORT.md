# account03/B18 r25 — MSS-paved spectral-tail exit and an affine two-plane zero-pivot transfer

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** literature-to-proof transfer  
**Run:** `20260923T062246Z-account03-B18-QFORM-r25`  
**Classification:** `TWO SUPPORTING TARGET-LEVEL BRANCHES PROVED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target, current correction boundary, and what changed

The target remains the unrestricted statement: for every dimension, every independent real coordinate family with probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite essential bound for the density of `X^T A X`, or give a target-valid counterexample. Continuity is separate.

This run does not use any of the live refuted interfaces: no independence after spectral rotation, no law-uniform pointwise quadratic-phase decay, no arbitrary-joint rank-three coarea theorem, no positive moment of a worst conditional projection-density cap, no worst-fiber supremum, and no assertion that three large eigenvalues force one uniformly good physical minor or rank-three cross cut.

Two concrete implications are proved.

1. A primary Marcus--Spielman--Srivastava partition theorem is matched exactly to the current volume-stability theorem. This yields a new full-matrix spectral-tail exit at leverage `1/18`, beyond the older `1/32` spectral-window leverage gate when the remaining spectral tail is sufficiently small.
2. The designated account04/B18 zero-pivot transfer is extended to arbitrary affine terms and applied, together with the Livshyts--Paouris--Pivovarov product-marginal theorem, to a rank-two residual source bank in a Schur-isotropic packet. This pays tilted two-plane banks, not only source-separated longitudinal/transverse banks.

Neither implication is the full theorem.

## 2. Primary-source gate ledger

### 2.1 Marcus--Spielman--Srivastava

Primary source: A. W. Marcus, D. A. Spielman, N. Srivastava, *Interlacing families II: Mixed characteristic polynomials and the Kadison--Singer problem*, Ann. Math. 182 (2015), 327--350, Corollary 1.5.

The exact statement used is:

If `u_1,...,u_m` satisfy

`sum_i u_i u_i^* = I`, `||u_i||^2 <= delta`,

then for every positive integer `r` there is a partition `S_1,...,S_r` such that

`|| sum_(i in S_j) u_i u_i^* || <= (1/sqrt(r)+sqrt(delta))^2`.

We use only `r=2`. This is a deterministic matrix theorem. It adds no probabilistic hypothesis on the input variables.

### 2.2 Livshyts--Paouris--Pivovarov

Primary source: G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889; arXiv:1507.07949.

For a product probability density with every one-dimensional factor bounded by one, every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`. We use the `k=2` case. There are no Gaussian, moment, compact-support, log-concavity, identical-law, symmetry, or smoothness assumptions.

For a non-orthonormal two-dimensional linear image `B^T X`, where `B` has full column rank, normalizing `B=Q G^(1/2)`, `Q^TQ=I_2`, gives

`||p_(B^T X)||_infinity <= 2 / sqrt(det(B^T B))`.                 (2.1)

No independence is asserted between the two projected coordinates.

### 2.3 Immediate analytic consumers

The volume-stability theorem actually used below is

`math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

It retains the full actual cross block and proves, for `M=M_0+E`,

` s_3(M_0)>=a,  max diag(P_Ran(M_0))<=1/2,  ||E||op<=a/16`

that the full quadratic-plus-affine form has a continuous density with

`||p_Q||_infinity <= 24 sqrt(3)e/(5a) < 23/a`.                    (2.2)

Its primary analytic inputs are Beckner's sharp Hausdorff--Young theorem and Lieb/Bennett--Carbery--Christ--Tao Brascamp--Lieb Gaussian extremization/finiteness. In particular, (2.2) is not a random-variable perturbation argument; arbitrary unbounded inputs are allowed.

The designated partner result is account04/B18 at

`math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.

It applies the completed zero-pivot `1+2` trace theorem to a cap-one scalar genuinely independent of a dependent two-dimensional projected vector. Its banked inequality is

`||p||_infinity <= 6 M^(2/3)|det K|^(-1/3)`                       (2.3)

when the pair has joint density cap `M` and `K` is nonsingular with zero scalar pivot. The two coordinates of the pair need not be independent.

## 3. New theorem A: MSS-paved volume-stability exit

Let `A` be real symmetric. Choose three **actual eigenpairs** with eigenvalue magnitudes at least `s>0` and write

`A = A_0 + E`,
`A_0 = U Lambda U^T`,
`U^T U=I_3`,
`min_k |lambda_k| >= s`,                                           (3.1)

where `E` is the exact remaining spectral part. Put

`delta = max_i ||u_i||_2^2`,                                      (3.2)

where `u_i^T` is row `i` of `U`, and define

`c_delta = 1/2 - sqrt(2 delta) - delta`.                           (3.3)

### Theorem A — `QFORM-MSS-VOLUME-STABILITY-1OVER18-v1`

If

`delta <= 1/18`,
`||E||op <= s c_delta/16`,                                        (3.4)

then for every independent cap-one input family, `X^T A X+b^T X+c` has a continuous density satisfying

`||p_Q||_infinity <= 24 sqrt(3)e/(5 s c_delta) < 23/(s c_delta).`  (3.5)

In particular, because `c_delta>=1/9` on this range,

`delta<=1/18`, `s>=1`, `||E||op<=1/144`

imply

`||p_Q||_infinity <= 216 sqrt(3)e/5 = 203.3943366... < 207`.       (3.6)

This is a theorem for the **full matrix `A`**, including its nonseparable spectral tail `E`.

### Proof

The rows of `U` form a Parseval frame:

`sum_i u_i u_i^T=I_3`.                                            (3.7)

Apply MSS Corollary 1.5 with `r=2`. There is a partition of the original physical coordinates into `I,J` such that

`G_I:=U_I^T U_I <= h_delta I_3`,
`G_J:=U_J^T U_J <= h_delta I_3`,
`h_delta=(1/sqrt(2)+sqrt(delta))^2`.                               (3.8)

Since `G_I+G_J=I_3`, both also satisfy

`G_I,G_J >= c_delta I_3`,                                         (3.9)

with `c_delta=1-h_delta`, exactly (3.3).

At `delta=1/18`,

`sqrt(2delta)=1/3`, `c_delta=1/9`, `delta/c_delta=1/2`.             (3.10)

The functions `c_delta` and `delta/c_delta` are respectively decreasing and increasing over the relevant interval, so for every `delta<=1/18`,

`c_delta>=1/9`, `delta/c_delta<=1/2`.                              (3.11)

Consider the rank-three spectral cross block

`M_0=A_0[I,J]=U_I Lambda U_J^T`.                                  (3.12)

Write

`U_I=Q_I G_I^(1/2)`, `U_J=Q_J G_J^(1/2)`,                         (3.13)

where `Q_I,Q_J` have orthonormal columns. The three nonzero singular values of `M_0` are therefore exactly those of

`G_I^(1/2) Lambda G_J^(1/2)`.                                     (3.14)

Equations (3.1) and (3.9) give

`s_3(M_0) >= s c_delta`.                                           (3.15)

Because `G_J` and `Lambda` are invertible, `Ran(M_0)=Ran(U_I)`. The projection onto this row-index range is

`P_I=U_I G_I^(-1) U_I^T`.                                         (3.16)

For every `i in I`,

`(P_I)_{ii}=u_i^T G_I^(-1)u_i <= ||u_i||^2/c_delta
 <= delta/c_delta <=1/2`.                                         (3.17)

The actual cross block is

`M=A[I,J]=M_0+E[I,J]`.                                             (3.18)

Coordinate compression cannot increase operator norm, so

`||E[I,J]||op <= ||E||op <= s c_delta/16`.                         (3.19)

Thus every hypothesis of (2.2) holds with `a=s c_delta`, proving (3.5). The theorem (2.2) already keeps arbitrary self-blocks, outside couplings, and affine terms, so there is no hidden separation assumption. Continuity comes from the integrable characteristic-function estimate in that theorem. QED.

### Comparison with an existing paid branch

The earlier spectral-window theorem used elsewhere in the fleet has a leverage gate `<=1/32`. Theorem A reaches leverage `1/18` when the remaining spectral tail is at most `1/144` at target scale. Hence the interval

`1/32 < delta <=1/18`

is a genuinely additional paid region under the stated tail hypothesis. No claim is made that the tail hypothesis follows from the bare three-large-eigenvalue assumption.

## 4. Affine stability of the designated partner zero-pivot theorem

Conditioning an outside source bank creates affine terms, so before applying account04/B18 we record the exact affine extension of its underlying estimate.

### Lemma B1 — affine zero-pivot `1+2`

Let `X` have a probability density at most one. Let `Y=(Y_1,Y_2)` be independent of `X` and have arbitrary joint density at most `M`. Let

`H=[[0,ell^T],[ell,B]]`

be symmetric and nonsingular. For every affine vector `q in R^3` and constant `c`,

`Z=(X,Y)^T H(X,Y)+q^T(X,Y)+c`                                    (4.1)

has a continuous density and

`||p_Z||_infinity <=6 M^(2/3)|det H|^(-1/3)`.                     (4.2)

Thus the constant in the designated partner result is unchanged by arbitrary affine terms.

### Proof

Rotate only the two `Y` coordinates, preserving their joint density cap and scalar-versus-pair independence, so `ell=(L,0)`, `L>0`. Write the pair coordinates `(u,v)`. Nonsingularity gives

`det H=-L^2 beta`, `beta!=0`,                                     (4.3)

where `beta` is the lower-right coefficient after the rotation. A determinant-one shear in `(u,v)`, followed by a translation in the second coordinate, reduces (4.1) to

`Z=beta w^2+alpha u^2+d u+(2Lu+a)X+c_0`.                          (4.4)

The transformed pair density is still bounded by `M`. Put

`u_0=-a/(2L)`.                                                     (4.5)

For fixed `(u,w)`, linearizing in the genuinely independent scalar gives the same far-fiber estimate as in the partner proof,

`h_u(t) <= m(u)/(2L|u-u_0|)`,                                    (4.6)

where `m` is the `u`-marginal of the transformed pair density.

For fixed `(X,u)`, pushing the `w` slice through `beta w^2` and using the cap-one rearrangement

`sup_z int f(x)|z-cx|^(-1/2)dx <=2sqrt(2)|c|^(-1/2)`              (4.7)

gives

`h_u(t) <= [2M/sqrt(|beta|L)] |u-u_0|^(-1/2)`.                    (4.8)

Split at `|u-u_0|=rho`. Since `int m=1`,

`p_Z(t) <= 1/(2L rho)+8M sqrt(rho)/sqrt(|beta|L)`.                 (4.9)

Optimizing `rho` yields

`p_Z(t) <=6 M^(2/3)(|beta|L^2)^(-1/3)
          =6 M^(2/3)|det H|^(-1/3)`.                              (4.10)

For continuity, for almost every `u!=u_0` the conditional output is a convolution of `L^1` densities and is continuous; (4.6) away from `u_0` and (4.8) near it provide an integrable `u`-majorant. Dominated convergence gives a continuous unconditional density. QED.

The proof is the designated partner's proof with the dangerous fiber translated from `u=0` to `u=u_0`; no conditional-density-as-independence substitution occurs.

## 5. New theorem B: a tilted two-plane source-bank exit

Consider the exact-rank-three Schur-isotropic packet

`Q=(Y+r n X_0)^T D(Y+r n X_0)`,                                   (5.1)

where `D` is invertible symmetric, `||n||=1`,

`n^T D n=0`,                                                       (5.2)

`X_0` and every residual original coordinate are mutually independent and cap one, and

`Y=sum_j v_j X_j`, `sum_j v_j v_j^T=I_3`.                         (5.3)

Let `J` be any subset of residual **original coordinates** whose spectral rows span exactly a two-plane `E`. Condition on every residual coordinate outside `J`; this introduces only fixed translations and affine terms into the active variables.

Let `U` be an orthonormal `3x2` basis matrix for `E`, define

`G_J=U^T (sum_(j in J) v_jv_j^T) U`,
`g_J=det G_J>0`,                                                   (5.4)

and let `m` be a unit normal to `E`. Put

`theta=|n^T m|`.                                                    (5.5)

Assume `theta>0` and define the product-preserving bank currency

`Omega_J=g_J theta^2`.                                             (5.6)

By Cauchy--Binet this has the equivalent original-row formula

`Omega_J=sum_(i<j, i,j in J) det(n,v_i,v_j)^2`.                    (5.7)

### Theorem B — `QFORM-TILTED-TWOPLANE-ZEROPIVOT-BANK-v1`

Under (5.1)--(5.6), including arbitrary affine terms generated by conditioning the complementary original-coordinate bank,

`Q` has a continuous density satisfying

`||p_Q||_infinity
 <=6 * 2^(2/3) [r^2 |det D| Omega_J]^(-1/3)`.                      (5.8)

If the complete physical matrix in (5.1) has exactly three nonzero eigenvalues, each of modulus at least `s`, then

`|det D|(1+r^2)>=s^3`.                                             (5.9)

Consequently, for `r>=1`,

`||p_Q||_infinity <=12 s^(-1) Omega_J^(-1/3)`.                    (5.10)

This is a high-shear exit whenever one original-coordinate rank-two bank carries a dimension-free amount of the aggregate shear-transverse volume (5.7).

### Proof

Write the active two-dimensional projected residual variable as

`T=U^T sum_(j in J) v_jX_j`.                                      (5.11)

Its coefficient matrix `B` has `B^T B=G_J`. Normalize `B=Q G_J^(1/2)` with `Q^TQ=I_2`. LPP applied to the genuine original product bank gives

`||p_T||_infinity <=2/sqrt(g_J)`.                                  (5.12)

The scalar `X_0` is genuinely independent of the whole pair `T`; no claim is made that the two coordinates of `T` are independent.

After conditioning the complementary residual coordinates, the active quadratic coefficient matrix in `(X_0,T)` is

`K=[rn,U]^T D [rn,U]`.                                             (5.13)

Equation (5.2) gives the required zero scalar pivot. Moreover

`|det K|=r^2 |det[n,U]|^2 |det D|
          =r^2 theta^2 |det D|`.                                  (5.14)

Since `theta>0`, `K` is nonsingular. Apply Lemma B1, equivalently the affine-stable form of the designated account04/B18 estimate, with `M=2/sqrt(g_J)`. This gives

`||p_Q||_infinity
 <=6 (2/sqrt(g_J))^(2/3)
       (r^2 theta^2 |det D|)^(-1/3)`,                              (5.15)

which is exactly (5.8).

The estimate is uniform in all conditioned values. Mixing the conditional densities preserves the `L^infinity` bound. Their continuity plus the uniform bound gives unconditional continuity by dominated convergence.

For an exact-rank-three physical matrix, the coefficient-row Gram is `I_3+r^2nn^T`; the product of the three nonzero physical eigenvalue magnitudes therefore equals

`|det D| det(I_3+r^2nn^T)=|det D|(1+r^2)`.                         (5.16)

This proves (5.9). If `r>=1`, then

`r^2 |det D| >= s^3 r^2/(1+r^2) >=s^3/2`.                         (5.17)

Substitution into (5.8) yields (5.10). QED.

### Why this is stronger than source separation

The two-plane `E` need not equal `n^perp`; it may contain a substantial longitudinal component. The conditioned complement need not be parallel to `n` either. What is preserved is only genuine source independence between the physical scalar `X_0` and the whole two-dimensional bank. This is exactly the independence hypothesis of the designated partner theorem and no more.

## 6. Exact target-valid tilted-plane stress family

Take

`n=e_1`,
`v_1=(e_1+e_2)/sqrt(2)`,
`v_2=e_3`,
`v_3=(e_1-e_2)/sqrt(2)`.                                         (6.1)

These three residual rows are an orthonormal basis, so (5.3) holds. Use the active bank `J={1,2}` and condition coordinate `3`. Then

`E=span(v_1,e_3)`, `g_J=1`, `theta=1/sqrt(2)`, `Omega_J=1/2`.      (6.2)

For every `r>=1`, set

`D_r=[[0,(1+r^2)^(-1/2),0],
      [(1+r^2)^(-1/2),0,0],
      [0,0,1]]`.                                                    (6.3)

The nonzero physical spectrum of the four-coordinate matrix is exactly

`{-1,1,1}`                                                        (6.4)

for every `r`: indeed conjugating `D_r` by `(I+r^2e_1e_1^T)^(1/2)` gives the fixed matrix `[[0,1,0],[1,0,0],[0,0,1]]`.

Theorem B gives

`||p_Q||_infinity <=12 ((1+r^2)/r^2)^(1/3)`.                      (6.5)

Thus the bound is at most

`12*2^(1/3)=15.1190525987...`                                     (6.6)

for all `r>=1`, and tends to `12` as `r` tends to infinity. The active plane is tilted relative to `n`, so this is not the earlier longitudinal-versus-transverse source-separated packet.

## 7. Non-transfers checked

A focused literature check did not justify replacing the hypotheses above by standard Hanson--Wright, Carbery--Wright, or Gaussian quadratic-form density estimates: those require subgaussian/Bernstein, log-concave/Gaussian, or similarly stronger distributional assumptions absent from the owner target. They are therefore not used.

Likewise LPP is used only to obtain a genuine marginal-density cap for a specified original-product projection. It is not promoted to independence of projected coordinates and is not treated as an arbitrary-joint indefinite quadratic pushforward theorem.

## 8. Remaining debt

The full QFORM conjecture remains **OPEN / NOT PROVED** and global continuity remains open.

Theorem A removes a larger diffuse three-eigenvector/small-spectral-tail region, but it does not show that every target matrix has such a diffuse top-three subspace or such a small tail.

Theorem B removes high-shear packets with a quantitatively useful **rank-two source bank**. It does not solve the genuinely non-source-separated high-shear state in which every product-preserving bank carrying substantial transverse volume also has full latent rank three. That is still the exact place where a bounded joint projection density, a worst conditional cap, or a fixed physical pair cannot be substituted for the missing product provenance.

The most useful next implication for B18 is therefore one of:

1. find a primary theorem giving a product-valid trace estimate for the full-rank three-dimensional projected bank in the zero-pivot Schur-isotropic packet, or
2. combine the current volume-stability/tail certificate with a structural theorem that forces the remaining high-leverage/low-tail matrices into an already-paid hub, pair, or rank-two-bank exit.

No external novelty claim is made for either theorem in this report.
