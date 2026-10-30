SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B13, 2026-09-23T12:59:29Z.
attacking: low-rank off-diagonal leaf curvature by Fresnel linearization plus augmented geometric Brascamp-Lieb, extending the partner's diagonal-leaf aggregate theorem.

# fleet01/B13 auto23 — low-rank leaf-curvature augmentation

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **PROVED SUPPORTING TARGET-LEVEL THEOREMS; FULL QFORM OPEN; FULL CONTINUITY OPEN SEPARATELY**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The exact target remains: for independent real coordinates with one-dimensional probability densities bounded by one, and every real symmetric coefficient matrix with at least three eigenvalues of absolute value at least one, prove a universal essential-supremum bound for the density of the quadratic form, or give a valid counterexample. Nothing below claims that full theorem.

The point of this run is to remove a genuine obstruction in the two-hub normal form. The designated fleet02/B13 diagonal-leaf theorem pays an arbitrary-width physical two-hub bank when the leaf self-block is diagonal, but arbitrary off-diagonal leaf curvature was still unpaid. Here a low-rank off-diagonal leaf block is linearized by an exact Fresnel identity. The resulting auxiliary variables are combined with the two physical hub directions and the partner's twisted one-dimensional Fourier estimate through geometric Brascamp-Lieb. No random-variable rotation is performed.

## 1. Source inputs actually used

### 1.1 Designated partner fleet02/B13 r25

Source-pinned report:

`yspennstate/math-open-problems@04973c0d13c8cbe814f1303b7de8aeffd40791df`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260923T110032Z-fleet02-B13-extremal-r25/REPORT.md`.

Two completed pieces from that report are used.

First, in the diagonal-leaf two-hub model, if `B=[b_1 ... b_m]` has rank two, `D_B=det(BB^T)`, and

`beta_j=b_j^T(BB^T)^(-1)b_j`,

then the exact determinant-star identity is

`sum_{s!=j} det(b_j,b_s)^2 = beta_j D_B`.                         (1.1)

Second, its diffuse diagonal-leaf theorem has the exact constant

`max_j beta_j <=1/2  =>  ||p_Q||_inf <=4 D_B^(-1/4)`.             (1.2)

The new theorem below recovers (1.2) as the `k=0` member of a larger low-rank-curvature family, and (1.1) is applied later to an actual high-leverage obstruction inequality.

### 1.2 Twisted one-dimensional Fourier estimate

The partner proof uses the pinned Fourier source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

whose required estimate is the following. For every scalar cap-one density `f`, every real quadratic twist `s`, and

`g(s,tau)=int exp(i s x^2+i tau x) f(x) dx`,

one has, uniformly in `s`,

`int_R |g(s,tau)|^p d tau <=4 pi / sqrt(p),   p>=2`.              (1.3)

This is an integrated estimate, not a false pointwise stationary-phase bound.

## 2. Extremal product-law reduction retained

The completed B13 finite-mixture purification remains in force. Every cap-one probability density is an `L1` limit of finite convex mixtures of indicators of bounded finite unions of intervals of measure one; tensorization gives the same for product laws. Hence the supremum of every bounded nonnegative product-law kernel equals the supremum over unit-measure product indicators, with bounded finite unions sufficient in the supremum.

No optimizer is asserted, no centered interval is selected, and there is no dimension-free bound on support diameter or fragment count.

The theorems below are proved directly for all cap-one product densities, so the corresponding geometric product-set slab inequalities follow simply by taking indicator densities; the purification result also supplies the converse reduction whenever a strict bad slab is assumed.

## 3. Main theorem I: arbitrary diagonal twists plus rank-k off-diagonal leaf curvature

Let

`U=(U_1,U_2) in R^2`, `V=(V_1,...,V_m)`,

and `Z` be disjoint banks of original physical coordinates. All scalar coordinates are independent and each has a probability density bounded by one.

Fix a real `2xm` matrix `B`, a real `kxm` matrix `W`, and an invertible real symmetric `k x k` matrix `Lambda`, with `k>=1`. Write `b_j` for column `j` of `B` and `w_j` for column `j` of `W`. Consider

`Q = F(U,Z)
     + sum_j [d_j V_j^2 + c_j(Z)V_j]
     + 2 U^T B V
     + (W V)^T Lambda (W V)`,                                    (3.1)

where `F` is arbitrary measurable for the estimate (in the quadratic-form application it is the remaining conditioned quadratic phase), `d_j` are arbitrary real numbers, and `c_j(Z)` are arbitrary real functions of the outside coordinates.

Put

`A_* = [ B ; W ]`  (vertical concatenation),
`d = k+2`,
`G = A_* A_*^T`,                                                     (3.2)

and assume `A_*` has full row rank `d`. For column `a_j=(b_j,w_j)` define its augmented leverage

`ell_j = a_j^T G^(-1) a_j`,
`h = max_j ell_j`.                                                   (3.3)

### Theorem 3.1 — `QFORM-AUGMENTED-LOWRANK-LEAF-BL-v1`

If

`h <=1/2`,                                                           (3.4)

then `Q` has a continuous density and

`boxed:
 ||p_Q||_inf
 <= C_k [ |det Lambda| det G ]^(-1/(k+4)),
 C_k = ((k+4)/(k+2)) 2^(2(k+2)/(k+4)) <=4.
`                                                                      (3.5)

For `k=1`,

`C_1=(5/3)2^(6/5)=3.8289945166...`.                                 (3.6)

For `k=0`, deleting the rank-k term and the Fresnel step gives exactly

`||p_Q||_inf <=4 det(BB^T)^(-1/4)`,                                (3.7)

which is the diffuse branch of the designated partner theorem.

### Proof

Condition on `Z=z`. All bounds below are uniform in `z`; therefore averaging at the end is harmless. For every leaf define

`g_{j,t}(tau)
 = int exp(i t d_j v^2+i tau v) f_{V_j}(v) dv`.                    (3.8)

For `t!=0`, the exact `k`-dimensional Fresnel identity gives

`exp(i t y^T Lambda y)
 = gamma_(t,Lambda)
   int_Rk exp(-i xi^T Lambda^(-1) xi/(4t)) exp(i xi^T y) dxi`,      (3.9)

where only the modulus of the constant is needed:

`|gamma_(t,Lambda)|
 = (4 pi |t|)^(-k/2) |det Lambda|^(-1/2)`.                          (3.10)

Insert (3.9) with `y=WV`, integrate the independent leaf coordinates first, and discard only unimodular phases. The conditional characteristic function satisfies

`|phi_z(t)|
 <= (4 pi |t|)^(-k/2)|det Lambda|^(-1/2)
    int_Rk int_R2 f_U(u)
      prod_j |g_{j,t}(2t b_j dot u + xi dot w_j + t c_j(z))|
    du dxi`.                                                         (3.11)

Here `f_U(u)=f_{U_1}(u_1)f_{U_2}(u_2)<=1`; the physical hub coordinates have not been rotated.

Set

`eta=xi/(2t)`, `x=(u,eta) in R^(k+2)`.                              (3.12)

Then `dxi=(2|t|)^k deta`, and

`2t b_j dot u + xi dot w_j
 =2t a_j dot x`.                                                    (3.13)

Dropping `f_U<=1` therefore gives

`|phi_z(t)|
 <= (4 pi |t|)^(-k/2)|det Lambda|^(-1/2)(2|t|)^k I_t`,             (3.14)

where

`I_t=int_Rd prod_j |g_{j,t}(2t a_j dot x+t c_j(z))| dx`.           (3.15)

Normalize only this deterministic integral. Put

`y=G^(1/2)x`,
`r_j=G^(-1/2)a_j`,
`ell_j=||r_j||^2`,
`v_j=r_j/sqrt(ell_j)` for `ell_j>0`.                               (3.16)

Since `G=sum_j a_j a_j^T`,

`sum_j ell_j v_j v_j^T=I_d`,                                      (3.17)

and `sum_j ell_j=d`. Columns with `ell_j=0` are zero columns and contribute factors of modulus at most one, so omit them.

For each remaining `j`, define

`F_j(s)=|g_{j,t}(2t sqrt(ell_j) s+t c_j(z))|^(1/ell_j)`.           (3.18)

The hypothesis `ell_j<=1/2` makes `p_j=1/ell_j>=2`, so (1.3) yields

`int_R F_j(s) ds
 <= [1/(2|t|sqrt(ell_j))]
    [4 pi / sqrt(1/ell_j)]
 = 2 pi/|t|`.                                                       (3.19)

Geometric Brascamp-Lieb applied to (3.17) gives

`I_t
 <= det(G)^(-1/2)
    prod_j (int F_j)^(ell_j)
 <= det(G)^(-1/2) (2 pi/|t|)^d`.                                  (3.20)

Substitute `d=k+2` into (3.14):

`|phi_z(t)|
 <= K |t|^(-alpha)`,                                               (3.21)

with

`alpha=2+k/2=(k+4)/2`,                                             (3.22)

and

`K=2^(k+2) pi^(2+k/2)
   [|det Lambda| det G]^(-1/2)`.                                   (3.23)

The same estimate holds for the unconditional characteristic function, and trivially `|phi(t)|<=1`. Since `alpha>1`,

`int_R min(1,K|t|^-alpha) dt
 =2 [alpha/(alpha-1)] K^(1/alpha)`.                                (3.24)

Fourier inversion therefore gives a continuous density and

`||p_Q||_inf
 <= [alpha/(pi(alpha-1))] K^(1/alpha)`.                            (3.25)

Now `1/alpha=2/(k+4)`, and the power of `pi` in (3.23) is exactly `(k+4)/2`; hence the factor `pi` cancels. This simplifies to (3.5).

The elementary inequality `C_k<=4` follows by one-variable calculus from the displayed formula, with equality at `k=0` and limit four as `k` tends to infinity. QED.

## 4. Exact structural identity for the paid currency

The quantity in (3.5) is representation-invariant. This is important because `W^T Lambda W` has many factorizations.

Since full augmented rank implies `rank B=2`, define the orthogonal projection onto the kernel of the two hub rows by

`P = I_m - B^T(BB^T)^(-1)B`.                                      (4.1)

Block determinant / Schur complement in the Gram matrix gives

`det G
 = det(BB^T) det(W P W^T)`.                                 (4.2)

Moreover

`R_perp = P W^T Lambda W P`                                       (4.3)

has rank `k`, and its nonzero eigenvalues have product

`pdet(R_perp)
 = det(Lambda) det(W P W^T)`.                                      (4.4)

Indeed the nonzero eigenvalues of `(WP)^T Lambda (WP)` are those of `Lambda (WP)(WP)^T`.

Thus

`boxed:
 |det Lambda| det G
 = det(BB^T) |pdet(P W^T Lambda W P)|.
`                                                                      (4.5)

So Theorem 3.1 can be written without choosing a low-rank factorization:

`boxed:
 ||p_Q||_inf
 <= C_k [ det(BB^T)
          |pdet(P C_lr P)| ]^(-1/(k+4)),
`                                                                      (4.6)

where `C_lr=W^T Lambda W` is the low-rank leaf-curvature term and the compression has rank `k`.

For `k=1`, if `C_lr=sigma w w^T` with `||w||_2=1`, then

`|det Lambda| det G
 = det(BB^T) |sigma| ||P w||_2^2`.                       (4.7)

Thus the exact rank-one curvature is paid whenever it has a diffuse component transverse to the two hub cross rows.

## 5. Main theorem II: Nystrom-compatible hub curvature plus a transverse low-rank Schur remainder

The preceding theorem is strongest when no additional low-rank leaf curvature lies inside the row space of `B`. In the actual invertible-hub Schur decomposition, however, the leaf block contains the exact Nystrom term `B^T H^(-1)B`. That term can also be handled exactly rather than treated as an error.

Consider now

`Q = F(U,Z)
     + sum_j [d_j V_j^2+c_j(Z)V_j]
     +2 U^T B V
     +(BV)^T K (BV)
     +(WV)^T Lambda(WV)`,                                          (5.1)

where `K` is any invertible symmetric `2x2` matrix, `Lambda` is invertible symmetric `k x k`, `k>=1`, and the same augmented matrix `A_*=[B;W]` has full row rank `d=k+2` with maximum leverage `h<=1/2`.

### Theorem 5.1 — `QFORM-NYSTROM-LOWRANK-FRESNEL-BL-v1`

Under those hypotheses, `Q` has a continuous density satisfying

`boxed:
 ||p_Q||_inf
 <= [4(k+2)/k]
    [ |det K| |det Lambda| det(A_*A_*^T) ]^(-1/(k+2)).
`                                                                      (5.2)

For `k=1`,

`boxed:
 ||p_Q||_inf
 <=12 [ |det K| |det Lambda| det(A_*A_*^T) ]^(-1/3).
`                                                                      (5.3)

The exponent mechanism is exact: for `k=0` the same computation gives only `|phi(t)|=O(|t|^-1)`, the nonintegrable rank-two boundary. Adding one transverse low-rank curvature direction changes the exponent to `3/2`, exactly crossing into `L1(dt)`.

### Proof

Condition on `Z=z` and use the same leaf transforms (3.8). Apply the Fresnel identity simultaneously to the two-dimensional form `(BV)^T K(BV)` and to `(WV)^T Lambda(WV)`. Let `xi in R^2` and `eta in R^k` be the corresponding auxiliary variables. The combined prefactor has modulus

`(4 pi |t|)^(-(k+2)/2)
 |det K det Lambda|^(-1/2)`.                                       (5.4)

After integrating the independent leaves, the `j`-th transform is evaluated at

`2t b_j dot u + xi dot b_j + eta dot w_j+t c_j(z)`.               (5.5)

Now use the exact translation

`s=xi+2t u`.                                                        (5.6)

For every fixed physical `u`, `dxi=ds`, and the product of leaf-transform moduli depends on `(s,eta)` but no longer on `u`. After absolute values, the Fresnel kernels are unimodular. Therefore the physical hub density is used through its mass, not through a rotation:

`int_R2 f_U(u) du=1`.                                              (5.7)

Consequently

`|phi_z(t)|
 <=(4 pi |t|)^(-d/2)|det K det Lambda|^(-1/2)
   J_t`,                                                           (5.8)

where

`J_t=int_Rd prod_j
 |g_{j,t}(a_j dot x+t c_j(z))| dx`,
`x=(s,eta)`.                                                       (5.9)

Normalize by `G=A_*A_*^T` as before. Define

`F_j(r)=|g_{j,t}(sqrt(ell_j) r+t c_j(z))|^(1/ell_j)`.             (5.10)

Now (1.3) gives

`int F_j(r) dr
 <= [1/sqrt(ell_j)] [4 pi sqrt(ell_j)]
 =4 pi`.                                                           (5.11)

Geometric Brascamp-Lieb therefore yields

`J_t <=det(G)^(-1/2)(4 pi)^d`.                                    (5.12)

Thus

`|phi(t)|
 <=K_0 |t|^-alpha`,
`alpha=d/2=(k+2)/2`,                                               (5.13)

with

`K_0=(4 pi)^(d/2)
     [|det K det Lambda| det G]^(-1/2)`.                           (5.14)

Since `k>=1`, `alpha>1`. Inserting `min(1,K_0|t|^-alpha)` into Fourier inversion gives

`||p_Q||_inf
 <=[alpha/(pi(alpha-1))]K_0^(1/alpha)`.                            (5.15)

Because `K_0^(1/alpha)=4 pi [|det K det Lambda|det G]^(-1/d)` and `alpha/(alpha-1)=d/(d-2)=(k+2)/k`, this is exactly (5.2). QED.

## 6. Schur-form corollary

Take an invertible original-coordinate hub pair `H0=A[H,H]` and write the selected hub/leaf block as

`[ H0   B
  B^T   C ]`.                                                      (6.1)

Its Schur remainder is

`T=C-B^T H0^(-1)B`.                                                (6.2)

Suppose for some diagonal matrix `D0` one has an exact decomposition

`T=D0+W^T Lambda W`,                                               (6.3)

with `Lambda` invertible `k x k`, `k>=1`, and the augmented matrix `[B;W]` has full row rank `k+2` and maximum leverage at most `1/2`.

Then Theorem 5.1 applies with

`K=H0^(-1)`,                                                       (6.4)

so

`boxed:
 ||p_Q||_inf
 <=[4(k+2)/k]
   [ |det Lambda| det([B;W][B;W]^T) / |det H0| ]^(-1/(k+2)).
`                                                                      (6.5)

Using (4.5), this becomes the factorization-free identity

`boxed:
 ||p_Q||_inf
 <=[4(k+2)/k]
   [ det(BB^T)
     |pdet(P(T-D0)P)|
     / |det H0| ]^(-1/(k+2)).
`                                                                      (6.6)

For an exact rank-one Schur correction

`T-D0=sigma w w^T`, `||w||=1`,                                    (6.7)

with `Pw!=0`,

`boxed:
 ||p_Q||_inf
 <=12
 [ det(BB^T)|sigma| ||P w||^2 / |det H0| ]^(-1/3),
`                                                                      (6.8)

provided the three-row augmented leverage is at most `1/2`.

This is a new paid endpoint for the Nystrom normal form. It retains the exact Nystrom curvature and arbitrary diagonal Schur curvature; neither is perturbatively discarded.

## 7. High-leverage obstruction and direct application of the designated partner

The leverage hypothesis itself has an exact physical meaning. Let

`P_B=B^T(BB^T)^(-1)B`,
`P=I-P_B`,
`Y=WP`.                                                            (7.1)

Since the row space of `[B;W]` is the orthogonal direct sum of `row(B)` and `row(Y)`, its orthogonal projection is

`P_* = P_B + P_Y`,
`P_Y=Y^T(YY^T)^(-1)Y`.                                             (7.2)

Therefore

`ell_j = beta_j + tau_j`,                                         (7.3)

where

`beta_j=(P_B)_{jj}`

is exactly the partner's two-hub leverage, and

`tau_j=(P_Y)_{jj}`                                                 (7.4)

is the leverage of the transverse low-rank curvature bank.

Suppose a slab ratio `rho` in the model of Theorem 5.1 is larger than the paid bound. Then the theorem forces

`max_j ell_j>1/2`.                                                 (7.5)

Choose `j_*` with `ell_(j_*)>1/2`. By (7.3),

`beta_(j_*)>1/4  OR  tau_(j_*)>1/4`.                              (7.6)

The first branch is where the designated fleet02/B13 result is applied to an actual inequality. Its exact identity (1.1) gives

`boxed:
 beta_(j_*)>1/4
 => sum_{s!=j_*} det(b_(j_*),b_s)^2
    > (1/4) det(BB^T).
`                                                                      (7.7)

Thus more than one quarter of the entire physical two-hub cross-area is forced onto the single original leaf `j_*`.

The second branch has a completely parallel exact curvature-volume statement. By Cauchy-Binet,

`D_Y=det(YY^T)
 =sum_{|S|=k} det(Y[:,S])^2`.                                      (7.8)

Deleting column `j` and using the matrix determinant lemma shows

`sum_{S: |S|=k, j in S} det(Y[:,S])^2
 =tau_j D_Y`.                                                      (7.9)

Hence

`boxed:
 tau_(j_*)>1/4
 => sum_{S contains j_*} det(Y[:,S])^2
    >(1/4) det(YY^T).
`                                                                      (7.10)

Therefore the only unpaid leverage branch in the low-rank Schur chamber is a **single physical leaf star**: the same leaf carries more than one quarter of either the two-hub determinant area or the transverse Schur-curvature `k`-volume.

Equivalently, if every physical leaf satisfies simultaneously

`beta_j<=1/4` and `tau_j<=1/4`,                                    (7.11)

then `ell_j<=1/2` for every `j` and the Nystrom/low-rank branch is completely paid by (6.6).

## 8. Geometric product-set version

For arbitrary measurable sets `E_i` with `|E_i|=1`, use the indicator densities `1_(E_i)`. The preceding theorems give, for every interval `J`,

`|{x in prod_i E_i : Q(x) in J}|
 <= C_k [|det Lambda|det G]^(-1/(k+4)) |J|`                        (8.1)

under Theorem 3.1, and

`|{x in prod_i E_i : Q(x) in J}|
 <= [4(k+2)/k]
    [|det K det Lambda|det G]^(-1/(k+2)) |J|`                     (8.2)

under Theorem 5.1.

No component of any `E_i` is assumed to be an interval, centered, bounded in diameter, or bounded in fragment count.

## 9. Relation to the current fleet obstruction

The previous fleet01/B13 run proved that in an invertible physical hub chamber a high slab ratio forces the leaf Schur remainder into an explicit Nystrom skeleton plus a max-norm-small residual. The newest fleet02/B13 Schur-crosscut handoff further shows that this residual retains a strong physical cross cut and has a low-cross-rank-or-third-volume-bi-hub dichotomy.

The present theorem pays an exact low-rank endpoint of that obstruction:

* if the Schur remainder is diagonal plus rank `k>=1`, and its new directions are diffuse after orthogonalization against the two hub rows, the entire branch is bounded by (6.6);
* if this fails only because augmented leverage exceeds one half, one original coordinate carries a quantitative determinant/curvature star by (7.7) or (7.10).

Thus an exact low-rank Schur residual is no longer an unrestricted obstruction. The survivor is localized to one physical leaf, or else the residual must contain genuinely higher-rank/non-low-rank structure that cannot be represented as diagonal plus a fixed low-rank correction.

This does not yet control an arbitrary max-norm-small high-dimensional residual: entrywise smallness still cannot be treated as a law-uniform perturbation. It also does not turn the partner's cutwise `s_5=O(rho^-1)` information into a global exact low-rank decomposition. Those are the remaining gaps.

## 10. First unpaid implication

`QFORM-AUGMENTED-STAR-OR-HIGH-RANK-SCHUR-CLOSURE-v1`:

> Starting from the partner's strong Schur cross cut and the fleet01 Nystrom max-norm rigidity, show that either the Schur residual globally admits a diagonal-plus-low-rank representation to which (6.6) applies, or the cutwise residual necessarily produces enough disjoint higher exterior volume to trigger the already-paid D5 / grouped-bank mechanisms. In the high augmented-leverage case, use the single physical star (7.7)/(7.10) as the next genuine pivot rather than deleting the small tail.

Full QFORM remains OPEN. Independent end-to-end review of the new theorems has not yet been performed.

## 11. Correction compliance

This report does not use any law-uniform pointwise quadratic oscillatory decay, does not rotate the independent random variables and then call them independent, does not use projection density alone to control an indefinite pushforward, does not invoke the refuted arbitrary-joint coarea lemma, does not assume a conditional density cap after a sum/difference change, does not localize product indicators to a fixed number of intervals, and does not delete a small max-norm matrix perturbatively. The only changes of variables are deterministic integration variables inside Fourier/Fresnel integrals.
