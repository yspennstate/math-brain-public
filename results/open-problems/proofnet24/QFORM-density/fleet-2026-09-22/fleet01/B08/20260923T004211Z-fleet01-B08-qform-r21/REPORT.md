SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B08, 2026-09-23T00:42:11Z.
attacking: rank-r physical cross-block L2/Plancherel smoothing; combine the rank-three case with the B08 finite-dimensional floating partition to enlarge the exact-rank-three diffuse regime.

# fleet01/B08 r21 — full physical cross-block L2 smoothing and a 2/5 exact-rank-three diffuse theorem

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** diffuse eigenvector case  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The full owner target remains open: for arbitrary finite `n`, independent real original-coordinate inputs with densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a single universal finite bound for the density of `X^T A X`, or give a valid counterexample. No moment, support, Gaussian, log-concavity, connected-support, or post-rotation independence assumption is introduced below. Continuity is stated only where Fourier inversion proves it.

This run changes mechanism from the preceding B08 ridge/near-rank-two iterations. The main analytic observation is that a **whole original-coordinate cross block of exact rank r>=3 can be paid in L2 without any leverage hypothesis at all**. Same-side quadratic terms and arbitrary outside couplings survive. Combining this with B08's finite-dimensional floating partition gives a new exact-rank-three diffuse threshold `max leverage <1/sqrt(6)` and, in particular, the clean target-level bound `<594` under `max leverage <=2/5`.

## 1. Source-valid inputs

### 1.1 Product-projection L-infinity theorem

The only external analytic input needed for the new cross-block theorem is the product-marginal estimate transferred in fleet01/B18 r20:

`yspennstate/math-open-problems@a9cecd1c7eaa605bd5d4bfd69ae9d9cb721705b7`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B18/20260923T002242Z-qform-B18-a01-r20/REPORT.md`.

It uses Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016): if `U` has `r` orthonormal columns and the original coordinates have densities at most one, then the density of `U^T X` is at most `2^(r/2)`. No moments or support assumptions occur.

The B18 report itself proves a two-full-bank theorem for exact rank three. The theorem below keeps the same L2 input but removes the requirement that the full quadratic matrix be rank three: arbitrary same-side blocks and arbitrary conditioned outside couplings are retained. What must remain exact is the physical **cross block** being paid.

### 1.2 B08 finite-dimensional floating partition

Source:

`yspennstate/math-open-problems@c37badc7438c808fa283f574d22a8cb4db87216e`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B08/20260922T144029Z-fleet01-B08-qform-r13/REPORT.md`.

If `R in R^(n x m)` has orthonormal columns and row leverage at most `delta`, there is an original-coordinate partition `I sqcup J=[n]` with

`R_I^T R_I >= alpha I_m`, `R_J^T R_J >= alpha I_m`,

where

`alpha = 1/2 - kappa_m delta`, `kappa_m=sqrt(m(m+1)/8)`.

For `m=3`, `kappa_3=sqrt(6)/2`, so `alpha>0` whenever `delta<1/sqrt(6)`.

### 1.3 Assigned partner fleet02/B08

Completed partner theorem:

`QFORM-DOUBLE-INCIDENT-RANK2-GROUPED-L3-v1`,

canonical source

`yspennstate/math-open-problems@c248abc9be918698c6d5a68108c615ba1c4790b3`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/B08-20260922T204103Z-1dd824/REPORT.md`.

For an exact-rank-two original-coordinate cross block `C`, fixed physical incident row `j` and column `r`,

`Delta_jr(C)=sum_(k!=j,s!=r) det C[{j,k},{r,s}]^2`,

and a genuine independent outer scalar square of coefficient `a!=0`, it proves

`||p_Q||_infinity <= C_grp |a|^(-1/2) Delta_jr(C)^(-1/8)`,

where

`C_grp=(2^(4/3)+1) sqrt(3) 2^(1/4)`.

Section 5 applies this partner theorem to an explicit target-valid rank-five family. This is useful precisely where the new rank-r theorem below does not apply because the relevant cross block has rank two.

## 2. New theorem: an exact physical cross block of rank r>=3

Let `I,J,K` be disjoint original-coordinate index sets with `I union J union K=[n]`. Write the physical cross block

`B=A[I,J]`.

Let its exact rank be `r>=3`, with nonzero singular values

`s_1(B)>=...>=s_r(B)>0`,

and put

`Pi_r(B)=prod_(nu=1)^r s_nu(B)`.

### Theorem 2.1 — `QFORM-RANKR-PHYSICAL-CROSS-L2-v1`

For arbitrary independent cap-one original-coordinate laws, arbitrary real symmetric same-side blocks `A[I,I]`, `A[J,J]`, arbitrary `A[K,K]`, and arbitrary couplings to `K`, the full quadratic form

`Q=X^T A X`

has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= [2r/(r-2)] Pi_r(B)^(-1/r).
`                                                                  (2.1)

No leverage assumption on the left or right singular spaces is needed. In particular, if `r=3`,

`boxed:
 ||p_Q||_infinity <=6 [s_1(B)s_2(B)s_3(B)]^(-1/3).
`                                                                  (2.2)

Hence an exact-rank-three physical cross block with `s_3(B)>=sigma` gives

`boxed:
 ||p_Q||_infinity <=6/sigma.
`                                                                  (2.3)

### Proof

Condition on all original coordinates in `K`. The conditional laws on the disjoint banks `I` and `J` remain independent products with the same marginal density caps. All couplings through `K` become affine terms. It is therefore enough to prove a bound uniform in those affine terms.

Take a thin singular-value decomposition

`B=U Sigma V^T`,

where `U` and `V` have `r` orthonormal columns and

`Sigma=diag(s_1,...,s_r)`.

After conditioning on `K`, write the same-side phase on bank `I` as

`F_I(x_I)=x_I^T A[I,I] x_I + ell_I^T x_I`,

and similarly `F_J`. For fixed Fourier time `t`, push the complex measure

`exp(i t F_I(x_I)) prod_(i in I) f_i(x_i) dx_I`

through `x_I -> y=U^T x_I`; denote its complex density by `g_t(y)`. Disintegration and the triangle inequality give pointwise

`|g_t(y)| <= p_(U^T X_I)(y)`.

The LPP marginal theorem therefore yields

`||g_t||_2^2
 <= ||p_(U^T X_I)||_2^2
 <= ||p_(U^T X_I)||_infinity
 <=2^(r/2)`,

so

`||g_t||_2 <=2^(r/4)`.                                         (2.4)

The analogous complex pushforward `h_t(z)` on the `J` bank obeys the same estimate. Notice that **arbitrary same-side quadratic phases are already inside `g_t,h_t`**; they cost nothing in (2.4) because they have modulus one before pushforward.

With Fourier convention

`hat h(xi)=integral exp(i <xi,z>) h(z) dz`,

conditional on `X_K` we have, up to an irrelevant scalar phase,

`phi_Q(t)
 = integral g_t(y) h_t(z)
          exp(2 i t y^T Sigma z) dy dz`

` = integral g_t(y) hat h_t(2t Sigma y) dy.`                    (2.5)

Cauchy--Schwarz, a linear change of variables, and Plancherel give

`|phi_Q(t)|
 <= ||g_t||_2
    [integral |hat h_t(2t Sigma y)|^2 dy]^(1/2)`

` = ||g_t||_2 (2|t|)^(-r/2) Pi_r(B)^(-1/2)
    ||hat h_t||_2`

` = ||g_t||_2 (2|t|)^(-r/2) Pi_r(B)^(-1/2)
    (2pi)^(r/2)||h_t||_2.`                                     (2.6)

Using (2.4) on both banks, the powers `2^(r/2)` from the two L2 norms cancel the factor `2^(-r/2)` coming from the bilinear phase. Therefore, uniformly in the outside conditioning,

`|phi_Q(t)|
 <= (2pi)^(r/2) Pi_r(B)^(-1/2)|t|^(-r/2)`                     (2.7)

for `t!=0`. Averaging over `X_K` preserves (2.7). Together with `|phi_Q(t)|<=1`, set

`K_r=(2pi)^(r/2) Pi_r(B)^(-1/2)`.

Since `r>2`,

`integral_R min(1,K_r |t|^(-r/2)) dt`

` = [2r/(r-2)] K_r^(2/r)`

` = [4pi r/(r-2)] Pi_r(B)^(-1/r).`                             (2.8)

Fourier inversion now yields a continuous density vanishing at infinity, and multiplication by `(2pi)^(-1)` in (2.8) gives exactly (2.1). QED.

### Scope guard

The exact-rank requirement in Theorem 2.1 is substantive. If a cross block has three large singular values but also arbitrarily tiny additional nonzero singular values, (2.1) spends the product of **all** nonzero singular values and can become useless. One may not simply delete those tiny modes under the owner hypotheses: the correction record contains explicit phase-aligned bounded-density examples showing there is no law-uniform coefficient-perturbation modulus. The existing ridge theorems address top singular directions only by paying additional leverage/effective-dimension hypotheses. Bridging these two mechanisms is now the key unpaid diffuse implication.

## 3. Main B08 application: exact rank three with leverage below 1/sqrt(6)

Consider now an exact-rank-three target

`A=R Lambda R^T`,

where `R^T R=I_3` and every eigenvalue of `Lambda` has modulus at least one. Let

`delta=max_i ||r_i||^2`

be the maximum physical leverage of the rank-three spectral subspace.

### Theorem 3.1 — `QFORM-RANK3-FLOATING-CROSS-L2-v1`

If

`delta<1/sqrt(6)`,

then `Q=X^TAX` has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= 12/(1-sqrt(6) delta).
`                                                                  (3.1)

This uses no moment, support, sign, iid, smoothness, or post-rotation independence assumption.

### Proof

Apply the B08 finite-dimensional floating partition with `m=3`. There is an original-coordinate cut `I sqcup J` such that

`G_I=R_I^T R_I >= alpha I_3`,
`G_J=R_J^T R_J >= alpha I_3`,

where

`alpha=1/2-(sqrt(6)/2)delta>0`.                                 (3.2)

The physical cross block is

`B=A[I,J]=R_I Lambda R_J^T`.

Since both Grams are positive definite and `Lambda` is invertible, `rank(B)=3`. Write

`R_I=W_I G_I^(1/2)`, `R_J=W_J G_J^(1/2)`

with `W_I,W_J` column isometries. The three nonzero singular values of `B` are those of

`G_I^(1/2) Lambda G_J^(1/2)`.

Consequently

`Pi_3(B)
 = |det Lambda| sqrt(det G_I det G_J)
 >= alpha^3`,                                                   (3.3)

because `|det Lambda|>=1` and both determinants are at least `alpha^3`.

Apply Theorem 2.1 at `r=3`:

`||p_Q||_infinity <=6 Pi_3(B)^(-1/3)<=6/alpha`.

Substitute (3.2) to obtain (3.1). QED.

### Clean numerical corollary: leverage 2/5

Since

`2/5 <1/sqrt(6)`,

if

`max_i ||r_i||^2 <=2/5`,

then

`alpha >=1/2-sqrt(6)/5=(5-2sqrt(6))/10`,

and therefore

`boxed:
 ||p_Q||_infinity
 <= 60/(5-2sqrt(6))
 =300+120sqrt(6)
 <594.
`                                                                  (3.4)

The density is continuous and vanishes at infinity.

This is a substantial enlargement of the previous B08 leverage-only exact-rank-three diffuse certificate. It also exceeds the `1/7` threshold from B08 r17, but the scopes must not be conflated: r17 tolerated an arbitrary nonseparable low-spectrum tail below `1/64`, whereas (3.1) assumes the **full matrix is exact rank three**. The gain comes from replacing ridge-leverage payment by whole-bank L2 payment once no extra cross singular directions are present.

## 4. Collision-entropy refinement and the localized complement

The fresh fleet01/B18 theorem gives a second, differently shaped diffuse certificate. For the exact rank-three Parseval frame define

`c_i=||r_i||^2`, `S_2=sum_i c_i^2`.

B18's volume-basis collision theorem proves

`S_2 <=1-eta
 => ||p_Q||_infinity <=12 eta^(-1/6)`,                          (4.1)

with continuity. This can pay frames with one leverage larger than `1/2` when the remaining determinant mass is sufficiently diffuse.

A simple max-leverage corollary is

`S_2 <= delta sum_i c_i =3delta`.

Thus, for `delta<1/3`,

`boxed:
 ||p_Q||_infinity <=12(1-3delta)^(-1/6).
`                                                                  (4.2)

For example, `delta<=1/4` gives

`||p_Q||_infinity <=12*4^(1/6)=15.1190525987...`.                (4.3)

For `delta<1/3`, (4.2) is much sharper numerically than (3.1); Theorem 3.1 is important because it keeps paying the previously uncovered range

`1/3 <= delta <1/sqrt(6)=0.408248...`.

The two criteria are not redundant: (4.1) is global collision diffuseness and can allow a single leverage far above `1/sqrt(6)`, while (3.1) is a deterministic max-row condition.

### Fixed-scale localized remainder after the new theorem

The exact row identity also makes the complement precise. If Theorem 3.1 fails because

`delta>=1/sqrt(6)`,

choose a physical row `i` with leverage

`c_i>=1/sqrt(6)`.

Put

`a=A_ii`, `b=A[i,-i]`.

Since `A=R Lambda R^T`,

`a^2+||b||_2^2=(A^2)_ii=r_i^T Lambda^2 r_i >=||r_i||^2=c_i`.    (4.4)

The completed rank-three affine half-Riesz theorem

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`

already gives, for every nonzero diagonal pivot,

`||p_Q||_infinity <=128/sqrt(|A_ii|)`.                          (4.5)

Hence if `|a|>=1/8`, the branch is paid by

`||p_Q||_infinity <=256sqrt(2)<363`.                            (4.6)

If instead `|a|<1/8`, (4.4) forces the genuine physical hub certificate

`boxed:
 ||A[i,-i]||_2^2
 >1/sqrt(6)-1/64,
`

so

`boxed:
 ||A[i,-i]||_2>0.6265965930... .
`                                                                  (4.7)

Thus, for exact rank three, the new diffuse theorem reduces the unpaid max-leverage complement to a **fixed-scale near-null physical hub**: leverage at least `1/sqrt(6)`, diagonal smaller than `1/8`, and cross-row norm larger than `0.6265`. This is considerably narrower than a generic localized-eigenvector statement and is an appropriate input for the fleet's pivot/hub/grouped-determinant mechanisms.

The exact null-coloop endpoint is known to be paid when the leverage is exactly one and the diagonal is exactly zero: fleet01/B19, canonical

`yspennstate/math-open-problems@09bb706f11ea00995a61f0c7323bf67997c65932`,

proves `||p_Q||_infinity<11.687` there. This does **not** pay the whole near-null hub region (4.7), so no full exact-rank-three closure is claimed here.

## 5. Assigned partner fleet02/B08 applied to a rank-two cross-block family

Theorem 2.1 deliberately starts at cross rank three. The designated partner theorem pays a complementary rank-two configuration.

Let `U in R^(m x 2)` satisfy `U^T U=I_2`, put

`P=U U^T`,

and define the target matrix on one scalar coordinate and two `m`-coordinate banks by

`A_U = [1] direct_sum [[0,P],[P,0]].`                           (5.1)

The spectrum contains

`1,+1,+1,-1,-1`,

so (5.1) satisfies the owner's three-large-eigenvalue target. Let `u_j` be row `j` of `U` and set

`h_j=||u_j||^2`.

The left-right physical cross block is the exact-rank-two matrix `C=P`. For two-element row and column sets, Cauchy--Binet gives

`det P[{j,k},{j,s}]
 = det U[{j,k}] det U[{j,s}]`.                                 (5.2)

Moreover, because `U^T U=I_2`,

`sum_(k!=j) det U[{j,k}]^2
 = ||u_j||^2=h_j`.                                             (5.3)

Therefore the partner's whole incident bank is exactly

`boxed:
 Delta_jj(P)=h_j^2.
`                                                                  (5.4)

Apply fleet02/B08 `QFORM-DOUBLE-INCIDENT-RANK2-GROUPED-L3-v1` with the genuine outer scalar-square coefficient `a=1`. For arbitrary independent cap-one laws,

`boxed:
 ||p_(X^T A_U X)||_infinity
 <= C_grp h_j^(-1/4),
`                                                                  (5.5)

where `C_grp=(2^(4/3)+1)sqrt(3)2^(1/4)=7.2500551088...`.

In particular, if this rank-two projection has any physical leverage `h_j>=1/3`, then

`boxed:
 ||p_(X^T A_U X)||_infinity
 <= C_grp 3^(1/4)
 =9.5416091213... <9.542.
`                                                                  (5.6)

This is an actual target-level inequality from the assigned partner theorem. It pays the **whole incident determinant bank before taking a negative power** and does not select one small physical minor. Continuity is not asserted from the partner endpoint; (5.5)-(5.6) are essential `L^infinity` bounds.

The family (5.1) is also a useful control for the division of labor: the new L2 theorem cannot be invoked because the natural cross block has rank two, while the grouped rank-two theorem pays it uniformly once an incident leverage resource is present.

## 6. First unpaid implication after this run

### `QFORM-TRUNCATED-CROSS-L2-OR-LOWRANK-ROUTING-v1` — OPEN

Theorem 2.1 pays a true physical cross block of exact rank `r>=3` by its full singular-value product. For the unrestricted owner target, a useful cut can instead have

- three macroscopically large singular values, but
- additional arbitrarily tiny nonzero singular values.

The full product `Pi_r(B)` then degenerates even though the top three directions are excellent. The live corrections forbid deleting the tiny modes by a law-uniform coefficient perturbation argument. The one-scale ridge machinery avoids paying tiny modes, but only by imposing leverage/effective-dimension conditions.

The next B08 theorem should therefore do one of two things:

1. prove a **truncated L2/Plancherel estimate** depending only on three robust singular directions while keeping the remaining bilinear modes and same-side phases inside the original product structure; or
2. prove a structural routing theorem saying that failure of such a truncated estimate forces a fixed-scale localized hub / rank-two grouped-bank certificate already paid by the partner and pivot machinery.

For exact rank three, the new theorem already gives the clean exhaustive first split: `delta<1/sqrt(6)` is continuously paid, while its complement contains a physical coordinate satisfying either the paid diagonal bound (4.6) or the fixed-scale near-null hub certificate (4.7).

## 7. Correction audit

This report does **not** use:

- pointwise law-uniform van-der-Corput decay;
- independence after spectral rotation;
- an arbitrary-joint three-dimensional coarea inequality;
- a positive conditional projection-density moment;
- a naive fiber supremum;
- a largest-minor selection;
- deletion of a small coefficient matrix under unrestricted supports.

The proof works with disjoint **original-coordinate banks**. Rotations occur only inside deterministic singular subspaces used as linear projection maps; the product law is never claimed to remain independent there. Same-side phases are retained before pushforward and bounded in L2 by domination by the positive projection density.

## 8. Status

Proved in this run:

- `QFORM-RANKR-PHYSICAL-CROSS-L2-v1`, equation (2.1), with continuous `C_0` density;
- `QFORM-RANK3-FLOATING-CROSS-L2-v1`, equation (3.1);
- the clean exact-rank-three corollary `max leverage<=2/5 => ||p_Q||_infinity<594`, continuously;
- the fixed-scale localized complement (4.7);
- the literal fleet02/B08 grouped-rank-two application (5.5)-(5.6), essential boundedness only.

The unrestricted QFORM conjecture remains **OPEN**. Two independent existing-worker end-to-end reviews of the full target are not present, and no full-solution claim is made.
