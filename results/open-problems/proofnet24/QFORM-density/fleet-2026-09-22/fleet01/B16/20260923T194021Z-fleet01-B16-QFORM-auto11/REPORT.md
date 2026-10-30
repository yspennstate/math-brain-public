# fleet01/B16 — crossing/Fresnel dimension trade with source provenance

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B16, 2026-09-23T19:40:21Z.
attacking: projection-product interaction at the residual shared-bank/near-coloop endpoint; trade genuine crossing rank against same-source Fresnel curvature without treating projected coordinates as independent.

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T194021Z-fleet01-B16-QFORM-auto11`  
**Assignment:** Projection-product interaction  
**Status:** `NEW SUPPORTING THEOREM + NEW TARGET-VALID FAMILY + PARTNER APPLICATION / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** proved on the new theorem's scope by an integrable characteristic-function majorant; the unrestricted continuity problem remains open.

## 1. Sources and corrections actually used

Fresh owner control keeps the unrestricted QFORM theorem open. This report uses the following pinned mathematics.

1. **Designated partner fleet02/B16 r35**, `yspennstate/math-open-problems@44d1b6391e145d4323077bbca0b16f68476df42f`, file `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260923T182948Z-fleet02-B16-QFORM-r35/REPORT.md`. It proves the rank-two-cross plus rank-one same-side Fresnel theorem and the exact one-bank innovation determinant identity.
2. **Actual product projection and twisted scalar Fourier estimates**, `yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`, file `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`: an orthonormal `k`-dimensional projection of a cap-one product law has density at most `2^(k/2)`, and for `|g|<=f`, `f` a cap-one probability density, `int |hat g|^p <=4*pi/sqrt(p)` for `p>=2`.
3. **Current B16 hard chamber**, especially fleet03/B16 r30 and its projected-crossing addendum `@0d6e70139fe0f7d8ee22cc5210efb3b8d00a0bda`, which isolates the remaining two-bank small-innovation geometry. This report does not declare that geometry closed.

The live corrections are kept throughout: no independence is inferred after rotation; a bounded joint projected density is not inserted into an arbitrary indefinite coarea integral; no normalized conditional projection-height cap is assumed; and no small random quadratic remainder is discarded merely because its coefficient vector is small.

## 2. Main theorem: crossing rank and same-side Fresnel rank trade exactly

### Theorem `QFORM-CROSS-FRESNEL-DIMENSION-TRADE-v1`

Partition the original independent cap-one coordinates into disjoint banks

`I disjoint_union J disjoint_union K`

and condition on `X_K`. Suppose the remaining real phase has the form

`Q = F(X_I)
     +2 X_I^T M X_J
     +X_J^T D X_J
     +(W^T X_J)^T Gamma (W^T X_J)
     +b^T X_J+c`,                                                (2.1)

where

- `F` is an arbitrary measurable real function of the entire `I` bank;
- `D` is diagonal in the **original J coordinates**;
- `M=U Sigma V^T` has rank `k>=1`, `U,V` have orthonormal columns, and `Sigma=diag(s_1,...,s_k)` with all `s_r>0`;
- `Gamma` is an invertible symmetric `ell x ell` matrix, `ell>=1`;
- `W` is a real `|J| x ell` matrix.

For each original source coordinate `j in J`, define the augmented row

`a_j=(s_1 V_{j1},...,s_k V_{jk},W_{j1},...,W_{j ell}) in R^(k+ell)`,

and

`G=sum_(j in J) a_j a_j^T`.                                     (2.2)

Assume `G` is positive definite and every nonzero augmented row has normalized leverage

`c_j=a_j^T G^(-1)a_j <=1/2`.                                   (2.3)

Let

`M_I=||p_(U^T X_I)||_infinity`.                                 (2.4)

Put

`alpha=k+ell/2`.                                                 (2.5)

Then for every `t!=0`,

`boxed:
 |phi_Q(t)|
 <= M_I 2^(k+ell) pi^alpha
    [|det Gamma| det G]^(-1/2)
    |t|^(-alpha).
`                                                                  (2.6)

If `alpha>1`, `Q` has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <= [alpha/(alpha-1)]
    [M_I 2^(k+ell)]^(1/alpha)
    [|det Gamma| det G]^(-1/(2alpha)).
`                                                                  (2.7)

For an arbitrary cap-one product `I` bank, the actual projection theorem gives

`M_I<=2^(k/2)`,                                                  (2.8)

so (2.7) becomes

`||p_Q||_infinity
 <=[alpha/(alpha-1)]
   2^((3k/2+ell)/alpha)
   [|det Gamma| det G]^(-1/(2alpha)).`                           (2.9)

No independence is asserted among the coordinates of `U^T X_I`. The only independence used is the genuine independence of the original `I` and `J` source banks and the coordinate factorization inside the still-unprojected `J` bank.

### Proof

Push the complex measure

`exp(i t F(X_I)) dP_I`

onto the `k`-dimensional projection

`z=U^T X_I`.

Write its complex density as `A_t(z)`. Disintegration gives the pointwise domination

`|A_t(z)|<=p_(U^T X_I)(z)<=M_I`.                                (2.10)

Thus, if `Phi_J(t,z)` denotes the `J`-bank conditional oscillatory integral,

`|phi_Q(t)|<=M_I int_(R^k)|Phi_J(t,z)| dz`.                     (2.11)

This is the only use of the projected density. It is used as a linear pushforward envelope before the nonlinear source-bank integration, not as an indefinite level-set bound.

Fresnel-linearize only the rank-`ell` quadratic term in (2.1). For an invertible symmetric `Gamma`, the standard damped Fresnel identity gives, in absolute value,

`|Phi_J(t,z)|
 <=(4*pi*|t|)^(-ell/2)|det Gamma|^(-1/2)
   int_(R^ell)
   product_(j in J)
   |hat g_(j,t)(2t <Sigma V_(j,*),z>+<W_(j,*),u>)| du`,          (2.12)

where

`g_(j,t)(x)=exp(i t D_jj x^2+i t b_j x) f_j(x)`

satisfies `|g_(j,t)|<=f_j`.

Set `y=2t z`; then `dz=(2|t|)^(-k)dy`. Combining (2.11)-(2.12) gives

`|phi_Q(t)|
 <=M_I 2^(-k)(4*pi)^(-ell/2)|det Gamma|^(-1/2)
   |t|^(-k-ell/2) I_t`,                                        (2.13)

with

`I_t=int_(R^(k+ell)) product_j
     |hat g_(j,t)(<a_j,(y,u)>)| d(y,u)`.                         (2.14)

Normalize the augmented original-source row system. Put

`beta_j=G^(-1/2)a_j`, `c_j=||beta_j||^2`,
`e_j=beta_j/sqrt(c_j)`

for nonzero rows. Then

`sum_j c_j e_j e_j^T=I_(k+ell)`,
`sum_j c_j=k+ell`,                                              (2.15)

and by (2.3), `p_j=1/c_j>=2`. After the change of variables by `G^(1/2)`, geometric Brascamp--Lieb gives

`I_t
 <=det(G)^(-1/2)
   product_j [ c_j^(-1/2)
               int_R |hat g_(j,t)(s)|^(1/c_j) ds ]^(c_j).`      (2.16)

The pinned scalar twisted-Fourier estimate gives

`int |hat g_(j,t)|^(1/c_j)
 <=4*pi*sqrt(c_j)`.                                             (2.17)

Hence every bracket in (2.16) is at most `4*pi`, and (2.15) yields

`I_t<=(4*pi)^(k+ell) det(G)^(-1/2).`                            (2.18)

Substitute (2.18) into (2.13):

`2^(-k)(4*pi)^(k+ell-ell/2)
 =2^(k+ell) pi^(k+ell/2)
 =2^(k+ell) pi^alpha`,                                          (2.19)

which proves (2.6).

Together with `|phi_Q(t)|<=1`, let

`B=M_I 2^(k+ell) pi^alpha [|det Gamma|det G]^(-1/2)`.

For `alpha>1`, with `T=B^(1/alpha)`,

`int_R min(1,B|t|^(-alpha))dt
 =2T+2B int_T^infinity t^(-alpha)dt
 =2 alpha/(alpha-1) B^(1/alpha).`                               (2.20)

Fourier inversion therefore gives

`||p_Q||_infinity
 <=[alpha/(pi(alpha-1))] B^(1/alpha)`,                           (2.21)

and the factor `pi` cancels because `B^(1/alpha)` contains exactly one `pi`. This is (2.7). The same `L^1` characteristic-function majorant gives a continuous `C_0` representative. Averaging over the initially conditioned `K` bank preserves the identical density bound. QED.

## 3. Exact determinant currency: only true source innovation counts

Because `V^T V=I_k`, the augmented Gram has block form

`G=[[Sigma^2, Sigma V^T W],
    [W^T V Sigma, W^T W]].`                                    (3.1)

The Schur complement of `Sigma^2` gives the exact identity

`boxed:
 det G
 =(product_(r=1)^k s_r^2)
  det[W^T(I-VV^T)W].
`                                                                  (3.2)

Thus the theorem pays same-side curvature only through its genuine original-source `ell`-volume transverse to the cross right-space. Components of `W` lying in `Range(V)` create no new smoothing dimension.

For `(k,ell)=(2,1)`, (3.2) is exactly the designated partner's identity

`det G=(s_1s_2)^2||(I-VV^T)w||^2`.                              (3.3)

For the new dual case `(k,ell)=(1,2)`, with cross right vector `v`,

`det G=s^2 det[W^T(I-vv^T)W]`.                                  (3.4)

So a rank-one crossing plus a genuinely two-dimensional same-side source innovation is already enough for a bounded continuous density.

## 4. New complementary branch: rank-one crossing plus rank-two curvature

Take `(k,ell)=(1,2)`. Then `alpha=2`, and the product-projection bound `M_I<=sqrt(2)` in (2.7) gives

`boxed:
 ||p_Q||_infinity
 <=2^(11/4)[|det Gamma|det G]^(-1/4)
 =6.7271713220... [|det Gamma|det G]^(-1/4).
`                                                                  (4.1)

This is complementary to partner r35, where `(k,ell)=(2,1)` and

`||p_Q||_infinity
 <=(5/3)2^(8/5)[|det Gamma|det G]^(-1/5).`                       (4.2)

The two formulas make the smoothing trade explicit: a crossing direction contributes one full power of `|t|^-1` after the projected variable is integrated, whereas a Fresnel-linearized same-side curvature direction contributes one half power. The threshold is

`k+ell/2>1`.                                                     (4.3)

## 5. Target-valid diffuse family not covered by the partner's rank-two-cross geometry

Let `m>=8` be a Hadamard order. On one original source bank choose a normalized diffuse Walsh vector `c in R^m`. On a disjoint bank choose three orthonormal diffuse Walsh vectors

`v,w_1,w_2 in R^m`,

all with entries of modulus `m^(-1/2)`. Put `W=(w_1,w_2)` and define

`A_m=[[0, c v^T],
     [v c^T, w_1w_1^T+w_2w_2^T]].`                              (5.1)

In the carrier basis `(c,v,w_1,w_2)`, the nonzero matrix is

`[[0,1,0,0],
  [1,0,0,0],
  [0,0,1,0],
  [0,0,0,1]]`.                                                   (5.2)

Hence the nonzero spectrum is exactly

`{1,-1,1,1}`,                                                    (5.3)

so (5.1) lies in the owner's full spectral target.

For (2.1), `s=1`, `Gamma=I_2`, and the augmented rows are

`a_j=(v_j,w_1j,w_2j)`.

Since the three Walsh columns are orthonormal,

`G=I_3`,                                                         (5.4)

and every row leverage is

`c_j=3/m<=3/8<1/2`.                                             (5.5)

The `I`-bank crossing variable `c^T X_I` is a genuine normalized one-dimensional projection of an independent cap-one product bank, so the actual projection theorem gives `M_I<=sqrt(2)`. Therefore (4.1) yields, for **every** choice of independent cap-one source laws,

`boxed:
 ||p_(X^T A_m X)||_infinity <=2^(11/4)=6.7271713220...,
`                                                                  (5.6)

and the density is continuous and vanishes at infinity.

No projected coordinates on the `J` bank are called independent. The proof linearizes the two same-bank curvature directions while the original `J` coordinates are still factorized.

This family is structurally complementary to the partner's `{1,1,1,-1,-1}` rank-two-cross/rank-one-square Walsh family: here the literal cross block has rank one, so a rank-two-cross theorem cannot be invoked, but two genuine same-bank curvature innovations supply the missing smoothing.

## 6. Completed designated-partner result applied to an actual target inequality

The designated partner r35 theorem applies to the Walsh construction with two orthonormal cross columns `C=(c_1,c_2)` on one bank, `V=(v_1,v_2)` on the other, and a third orthonormal source direction `w` on the receiver bank. It has

`s_1=s_2=1`, `Gamma=(1)`, `G=I_3`,                              (6.1)

so the completed partner result gives

`||p_Q||_infinity
 <=(5/3)2^(8/5)
 =5.0523885550346606... .`                                      (6.2)

Now make a genuinely nontrivial target extension allowed by the partner theorem: for any real `theta`, add the arbitrary same-side quadratic term `theta(c_1^T X_I)^2` on the **crossing-side source bank**. The carrier matrix becomes, after ordering `(c_1,v_1,c_2,v_2,w)`,

`diag_blocks( [[theta,1],[1,0]], [[0,1],[1,0]], [1] ).`          (6.3)

Its eigenvalues are

`(theta+sqrt(theta^2+4))/2`,
`(theta-sqrt(theta^2+4))/2`,
`1,-1,1`.                                                        (6.4)

For every real `theta`, at least one eigenvalue of the first pair has modulus at least one, while the last three already have moduli exactly one. Thus every matrix (6.3) remains inside the full QFORM target. Because r35 allows an arbitrary `I`-side quadratic function without changing the Fourier estimate, its completed theorem gives the actual inequality

`boxed:
 ||p_(Q+theta(c_1^T X_I)^2)||_infinity
 <=5.0523885550346606...
 for every theta in R.
`                                                                  (6.5)

This is an application of the partner result to a target-valid one-parameter family, not merely a citation. The extension is not a convolution argument: the added quadratic uses the same original source bank that participates in the crossing.

As a numerical branch consequence of the exact partner formula, whenever its one-bank innovation currency satisfies

`s_1 s_2 delta >=2^-10`,                                        (6.6)

one immediately has

`||p_Q||_infinity
 <=(5/3)2^(8/5)(2^-10)^(-2/5)
 =16*(5/3)2^(8/5)
 =80.8382168806...<81.`                                         (6.7)

The point of (6.7) is that the partner theorem converts a concrete source-innovation threshold directly into a universal target density inequality.

## 7. What this does and does not close

The theorem unifies and extends the partner mechanism: crossing rank `k` and same-bank Fresnel rank `ell` can be traded whenever `k+ell/2>1`, with the exact source determinant (3.2) and every row-leverage gate retained. It proves a new rank-one-cross/rank-two-curvature target family with universal continuous density bound `<6.728`, and it recovers the partner's `(2,1)` constant exactly.

It does **not** close the current fleet03/B16 r30 two-bank small-innovation survivor. In that survivor, arbitrary same-bank non-diagonal curvature remains, and neither bank is yet known to admit a representation (2.1) with a uniformly nondegenerate transverse innovation determinant. Equation (3.2) shows why merely saying the source innovation is small cannot help: if the curvature columns collapse into the cross right-space, the BL determinant really degenerates. Those small components also cannot be deleted on unbounded inputs.

The next precise B16 implication is therefore:

`QFORM-TWO-BANK-CURVATURE-DIMENSION-EXTRACTION-v1`:

> In the exact-rank-three ultra-coloop two-bank packet, prove that either one orientation admits a `(k,ell)` source decomposition with `k+ell/2>1`, row leverages at most `1/2`, and `|det Gamma|det G` bounded below universally, or identify a source-preserving joint receiver for the residual case in which every such augmented innovation determinant degenerates.

A useful special target is the dual `(k,ell)=(1,2)` branch (4.1): if the remaining order-one cross/hyperbolic currency forces two same-side curvature directions transverse to one crossing direction, the punctured small-innovation chamber is paid without a conditional projection-height bound.

Full unrestricted QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity remains open; continuity is proved only in the theorem's stated branch.
