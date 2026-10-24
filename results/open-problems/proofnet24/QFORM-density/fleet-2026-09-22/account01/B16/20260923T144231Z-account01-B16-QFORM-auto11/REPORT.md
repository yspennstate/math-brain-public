SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-23T14:42:31Z.
attacking: the superdiffuse near-coloop source-bank compiler; build a dependence-safe three-bank nonlinear quadratic transducer and apply it to the latest account02/B16 shared-bank/log-barrier families.

# account01/B16 — disjoint scalar-bank transverse triple transducer

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: projection-product interaction  
Status: **NEW SUPPORTING THEOREM / COMPLETED PARTNER RESULT APPLIED / FULL QFORM OPEN**  
Continuity: **not proved by this run; tracked separately.**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Control and correction-aware scope

Fresh `math-research-brain` control was resolved repeatedly during the run. The last pre-publication refresh reached `630427038a786c2684403bcc612cacf3414a3046`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM remains the sole research target, and no later B16 stop was found.

The full conjecture is still open. Nothing below uses post-rotation independence, a worst conditional projection-density cap, arbitrary-joint rank-three coarea, law-uniform pointwise oscillatory decay, deletion of a small coefficient on unbounded inputs, or a bounded joint projection density as if it automatically controlled an indefinite level-set integral.

The point of this run is different: when the original product source can be separated into **three disjoint scalar banks**, the bank outputs are genuinely independent. The sharp one-dimensional product-projection theorem supplies their density caps, and only then is the nonlinear quadratic integration paid by the completed determinant-scaled physical-triple theorem.

## 2. Source-pinned inputs

### 2.1 Determinant-scaled physical triple

I use `QFORM-PHYSICAL-TRIPLE-DETERMINANT-v1`, canonical source

`yspennstate/math-open-problems@b94cc7446401c02727c42024274c002e2f4e0cab`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260922T202347Z-account03-B16-QFORM-r15/REPORT.md`.

If `Z_0,Z_1,Z_2` are independent cap-one real variables and `B` is any invertible symmetric `3 x 3` matrix, then for every affine term

`||p_(Z^T B Z + ell^T Z + c)||_infinity
 <= C_3 |det B|^(-1/3)`,                                      (2.1)

where

`C_3=16 sqrt(30) 2^(1/4)=104.21688998922089...`.              (2.2)

The theorem is sign-free and translation-uniform at the affine level.

### 2.2 Actual one-dimensional product projection

For a linear form `T=a^T X_I` in an original-coordinate product bank with `r=||a||_2>0`, the completed one-dimensional product-projection theorem gives

`||p_T||_infinity <= sqrt(2)/r`.                                (2.3)

This is used only on disjoint original-coordinate banks, so independence between the resulting scalar bank outputs is genuine source independence, not spectral independence.

### 2.3 Latest designated partner account02/B16

The newest completed designated-partner report consumed is

`yspennstate/math-open-problems@62ae6f87b26f5ed06d8a8f937a8371616511ffa9`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260923T132911Z-account02-B16-QFORM-r11/REPORT.md`.

Its first theorem studies

`Q_eta=-eta X_0^2+2 sqrt(1+eta) X_0 Y+Z^2`, `0<eta<=1`,          (2.4)

with `(Y,Z)` the balanced two-dimensional projection of one residual product bank. It proves both

`||p_(Q_eta)||_infinity
 <=3*2^(4/3)(1+eta)^(-1/3)
 <=7.55952629937`,                                               (2.5)

and a logarithmically divergent translation-uniform envelope for the direct scalar-Schur square-peel route as `eta downarrow 0`. The same partner report also records the true near-coloop shared Walsh family and the 80-bank structural endpoint from account03/B16 r29.

## 3. General three-bank theorem

### Theorem — `QFORM-DISJOINT-BANK-TRANSVERSE-TRIPLE-v1`

Let `I_0,I_1,I_2` be pairwise disjoint sets of original coordinates and let

`T_j=a_j^T X_(I_j)`, `r_j=||a_j||_2>0`, `j=0,1,2`.              (3.1)

Let `W` denote all remaining original coordinates. Suppose that after conditioning on `W=w`, the entire remaining dependence factors through `T=(T_0,T_1,T_2)` as

`Q_w=T^T B T+ell(w)^T T+c(w)`,                                  (3.2)

where the symmetric `3 x 3` matrix `B` is fixed and invertible. Then

`boxed:
 ||p_Q||_infinity
 <=2 C_3 [ (r_0 r_1 r_2)^2 |det B| ]^(-1/3).`                   (3.3)

Equivalently, if one knows sharper individual density caps

`||p_(T_j)||_infinity<=K_j`,                                    (3.4)

then

`boxed:
 ||p_Q||_infinity
 <=C_3 (K_0 K_1 K_2)^(2/3) |det B|^(-1/3).`                    (3.5)

The theorem remains valid with arbitrary outside quadratic terms because after conditioning on `W` they only change `ell(w),c(w)` **provided the active-bank dependence really has the factorization (3.2)**. It does not condition inside one of the three active banks.

### Proof

The three `T_j` are independent because their source banks are disjoint. Under (3.4), put

`Z_j=K_j T_j`.                                                   (3.6)

Then the `Z_j` are independent and have density caps at most one. Writing

`D=diag(K_0^(-1),K_1^(-1),K_2^(-1))`,
`T=D Z`,                                                         (3.7)

we have

`det(D B D)=det B/(K_0 K_1 K_2)^2`.                             (3.8)

Condition on `W`, apply (2.1) uniformly over the resulting affine term, and average over `W`:

`||p_Q||_infinity
 <=C_3 |det(D B D)|^(-1/3)
 =C_3(K_0K_1K_2)^(2/3)|det B|^(-1/3)`.                          (3.9)

This proves (3.5). Using the actual projection caps `K_j<=sqrt(2)/r_j` gives

`(K_0K_1K_2)^(2/3)
 <=[(sqrt(2))^3/(r_0r_1r_2)]^(2/3)
 =2(r_0r_1r_2)^(-2/3)`,                                        (3.10)

which is (3.3). `QED`

The constant in (3.3) is

`2 C_3=208.43377997844356... <209`.                              (3.11)

### Why this is not the false joint-projection/coarea step

A cap on a dependent planar projection by itself does not pay an arbitrary indefinite quadratic trace. Here no such step occurs. The nonlinear theorem (2.1) is invoked on **three genuinely independent scalar source-bank outputs**. If two proposed scalar outputs come from the same original source bank, (3.3) cannot be used merely because their joint density is bounded.

## 4. Exact transverse determinant identity at a null or near-null first pivot

Write the active bank core in block form

`B=[[alpha,g^T],[g,C]]`,                                        (4.1)

where `g in R^2`, `C=C^T in R^(2x2)`. Assume `g!=0`, set

`n=g/||g||`,
`m=(-n_2,n_1)`,
`kappa_perp=m^T C m`.                                           (4.2)

For every symmetric `2 x 2` matrix `C`,

`g^T adj(C) g=||g||^2 kappa_perp`.                              (4.3)

Therefore

`boxed:
 det B=alpha det C-||g||^2 kappa_perp.`                         (4.4)

At the exact null pivot `alpha=0`,

`boxed: |det B|=||g||^2 |kappa_perp|.`                          (4.5)

More generally, if for some `0<=theta<1`

`|alpha det C|<=theta ||g||^2 |kappa_perp|`,                    (4.6)

then

`|det B|>=(1-theta)||g||^2|kappa_perp|`.                        (4.7)

Combining (3.5) and (4.7) gives the explicit dependence-safe near-null bank receiver

`boxed:
 ||p_Q||_infinity
 <=C_3(K_0K_1K_2)^(2/3)
   [(1-theta)||g||^2|kappa_perp|]^(-1/3).`                      (4.8)

Thus same-side curvature **parallel to the hub-coupling direction** and the mixed entry of `C` disappear from the determinant at the exact null pivot. Only curvature transverse to the hub cross vector matters. This is the bank-level algebraic reason the scalar-pivot singularity can be artificial.

## 5. Latest partner log-barrier family: a second, source-first uniform proof

Take the partner family (2.4). Split the balanced residual signs into their two original-coordinate source banks and define normalized sums

`Z_+=sqrt(2/m) sum_(epsilon_j=+1) X_j`,
`Z_-=sqrt(2/m) sum_(epsilon_j=-1) X_j`.                         (5.1)

The variables

`X_0, Z_+, Z_-`                                                  (5.2)

are genuinely independent. The coefficient vectors in (5.1) have Euclidean norm one, so

`||p_(Z_+)||_infinity, ||p_(Z_-)||_infinity<=sqrt(2)`,           (5.3)

while `||p_(X_0)||_infinity<=1`.

The partner projections satisfy

`Y=(Z_++Z_-)/sqrt(2)`,
`Z=(Z_+-Z_-)/sqrt(2)`.                                          (5.4)

Hence (2.4) becomes a quadratic form in the three independent bank variables with matrix

`B_eta=[[-eta, sqrt(1+eta)/sqrt(2), sqrt(1+eta)/sqrt(2)],
        [sqrt(1+eta)/sqrt(2), 1/2,-1/2],
        [sqrt(1+eta)/sqrt(2),-1/2, 1/2]].`                       (5.5)

Here the lower `2 x 2` block has determinant zero. Its transverse curvature relative to the hub vector is exactly one, while

`||g||^2=1+eta`.                                                 (5.6)

Therefore (4.4) gives the exact cancellation

`boxed: det B_eta=-(1+eta).`                                    (5.7)

No reciprocal power of the small scalar pivot `eta` appears. Applying (3.5) with caps `(1,sqrt(2),sqrt(2))` gives the alternate bound

`boxed:
 ||p_(Q_eta)||_infinity
 <=C_3 2^(2/3)(1+eta)^(-1/3)
 =165.43400080174334...(1+eta)^(-1/3).`                         (5.8)

This is much weaker numerically than the partner's mixed-Fresnel bound (2.5), but it is structurally useful: the very same family for which direct scalar Schur peeling has a logarithmically divergent translation-uniform envelope is uniformly paid by **source-bank splitting followed by nonlinear determinant integration**.

### Completed partner result applied to an actual higher-rank inequality

Use the sharper partner inequality (2.5). If `W=Z_out^T C_out Z_out` is **any** quadratic form in additional independent cap-one original coordinates disjoint from the partner family, of arbitrary dimension, rank, and signature, then

`p_(Q_eta+W)=p_(Q_eta)*mu_W`,                                    (5.9)

and Young's inequality yields the actual target-level extension

`boxed:
 ||p_(Q_eta+W)||_infinity
 <=3*2^(4/3)(1+eta)^(-1/3)
 <=7.55952629937.`                                               (5.10)

The full coefficient matrix is a block direct sum and therefore retains the partner core's three eigenvalues of modulus at least one.

## 6. True near-coloop shared Walsh family: transverse curvature survives bank conditioning

Now take the partner's fully shared Walsh family

`Q=2(sqrt(c)X_0+sqrt(a)L)U+T^2`,
`0<a<1/64`, `c=1-a`,                                              (6.1)

with all four sign pairs `(epsilon,tau)` represented equally. Use the partner's normalized sign-class source variables

`Z_(sigma,tau)=(2/sqrt(m)) sum_{j:(epsilon_j,tau_j)=(sigma,tau)} X_j`, (6.2)

which are mutually independent and each have density cap at most `sqrt(2)`.

Condition on the two `epsilon=-1` source classes `Z_-+ , Z_--`. The only remaining active source variables are

`X_0, Z_++, Z_+-`,                                                 (6.3)

still genuinely independent. In these variables the conditional quadratic block has

`g=(sqrt(c)/2,sqrt(c)/2)`                                        (6.4)

and leaf matrix

`C_a=[[sqrt(a)/2+1/4, sqrt(a)/2-1/4],
     [sqrt(a)/2-1/4, sqrt(a)/2+1/4]].`                           (6.5)

The hub pivot is zero. The direction perpendicular to `g` is `(1,-1)/sqrt(2)`, and

`kappa_perp=1/2`,
`||g||^2=c/2`.                                                    (6.6)

Hence the entire longitudinal same-side curvature `sqrt(a)` cancels from the determinant:

`boxed: det B=-c/4.`                                             (6.7)

Applying (3.5) with caps `(1,sqrt(2),sqrt(2))` gives

`||p_Q||_infinity
 <=C_3 2^(2/3)(c/4)^(-1/3)
 =C_3 2^(4/3)c^(-1/3).`                                         (6.8)

Since `c>63/64`,

`boxed: ||p_Q||_infinity<263.993<264.`                           (6.9)

The designated partner's source-plane/source-line compiler is far sharper on this exact family (`<27.015`), but (6.7) is a useful new structural certificate: after conditioning whole source classes, the zero-pivot determinant is controlled purely by hub cross mass times transverse curvature, uniformly as `a downarrow0`. This is another explicit aggregate-before-inversion mechanism.

## 7. Connection to the 80-bank superdiffuse endpoint

The newest account03/B16 structural compiler leaves, after paid pivot/pair exits, 80 disjoint normalized star banks `Y_k` with

`||p_(Y_k)||_infinity<=sqrt(2)`,
`sigma_k^2:=sum_(j in B_k)A_0j^2
 >4031/(4096*120)`,                                               (7.1)

so

`sigma_k>0.0905598724`.                                          (7.2)

The theorem above now completely pays the following subbranch of that endpoint. If, after conditioning the other original source banks, two selected banks `k,l` have **all their active dependence factor through the scalar star aggregates** `Y_k,Y_l`, then the conditional core is

`[[A_00, sigma_k,sigma_l],
 [sigma_k, *, *],
 [sigma_l, *, *]].`                                              (7.3)

Let `kappa_perp` be the leaf curvature transverse to `(sigma_k,sigma_l)`. Whenever

`|A_00 det C|
 <=theta (sigma_k^2+sigma_l^2)|kappa_perp|`, `theta<1`,           (7.4)

(4.8) gives an immediate universal bound. In particular at the exact null physical pivot, any uniform `|kappa_perp|>=kappa_0>0` gives

`||p_Q||_infinity
 <=C_3 2^(2/3)
   [(sigma_k^2+sigma_l^2)kappa_0]^(-1/3)
 <652 kappa_0^(-1/3).`                                           (7.5)

The numerical inequality uses (7.1) twice.

This does **not** close the full 80-bank endpoint because a generic superdiffuse bank can carry additional independent spectral linear forms; one may not condition those away while keeping the scalar star aggregate at its marginal density cap. The latest account02/B16 correction and partner analysis make exactly this distinction.

## 8. Sharpened remaining implication

The remaining B16 debt is now

`QFORM-SUPERDIFFUSE-FULLRANK-BANK-TRANSDUCER-v1`:

> In the true near-coloop 80-bank survivor, either extract two banks whose full active dependence collapses to the scalar-bank form paid by Sections 3--4, or a source-plane/source-line form paid by the partner compiler, or prove a new source-preserving receiver for the residual case in which several banks each retain genuinely rank-two/rank-three same-side curvature.

The present run closes the scalar-bank/null-transverse part and exhibits exact determinant cancellation on both the partner log-barrier family and the fully shared Walsh family. It does not prove that an arbitrary superdiffuse survivor must contain such a scalar-factor pair. The full conjecture and global continuity remain open.
