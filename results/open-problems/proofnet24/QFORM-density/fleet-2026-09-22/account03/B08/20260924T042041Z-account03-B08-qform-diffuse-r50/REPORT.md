SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-24T04:20:41Z.
attacking: the diffuse top-three frame by a sharper physical Bernoulli half-cut, then spend the resulting literal third-compound crossing before routing a large complementary spectrum to the ridge window.

# account03/B08 r50 — diffuse top-three frame: 3/8 half-cut + third-compound crossing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case / quantitative inequalities and rigorous computations  
Status: **NEW SUPPORTING DIFFUSE-TO-LOCALIZED ROUTER / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture remains **OPEN**. The result below sharpens the current diffuse-top-three bridge: under maximum top-three row leverage `<=1/48`, either the full quadratic form already has a continuous density bounded by `<197.779/L`, or an ORIGINAL physical coordinate carries a scalar/star witness `>0.00062475 L`. No moments, compact support, log-concavity, connected support, Gaussianity, post-rotation independence, arbitrary-joint coarea bound, or law-uniform pointwise quadratic-phase decay is used.

## 1. Fresh source boundary

Startup owner control was resolved from `yspennstate/math-research-brain` main at `1f4eb28d496430030c36c4b097d410c69381397f`; the prepublication control refresh was `c2cf502ba91445ad3119cfb9991131ec7d32d725`. OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, with no pause or reassignment of account03/B08.

The arbitrary-rank crossing input is the reviewed source

`yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

For the zero-hub third-compound specialization and its canonical physical-row promotion, I use and recheck the source theorem

`QFORM-THIRDCOMPOUND-CROSS-PROMOTION-v1`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260923T194715Z-account01-B04-QFORM-auto11-r18/REPORT.md`,

whose stated consequence for an original-coordinate crossing `B` is

`||p_Q||_infinity <= 6^(4/3) e_3(BB^T)^(-1/6)`,                 (1.1)

with `p_Q in C_0(R)`, while retaining arbitrary same-bank quadratic/measurable phases. Its promotion step is product-safe: a heavy canonical compound row is moved as an ORIGINAL scalar coordinate into the hub; the exact currency recursion is

`S_+^2 Z_(ell-1)^+ = alpha_h S^2 Z_ell`.                         (1.2)

Thus no row-marginal gate is assumed below.

The designated partner is account04/B08 r2,

`QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260923T212412Z-account04-B08-QFORM-r2/REPORT.md`.

If an ORIGINAL-coordinate deletion child `C` has three eigenvalues of modulus at least `m` and the physical projection onto `|lambda(C)|>=m/64` has maximum diagonal `<=1/32`, it gives

`||p_Q||_infinity <= C_R/m <64/m`, `p_Q in C_0`,                (1.3)

where

`C_R=288 sqrt(3e)/13=63.26405187778285...`.                     (1.4)

The live correction inbox was reread before publication. No challenged pointwise or conditional-density shortcut is used.

## 2. A sharper physical half-cut for a diffuse three-frame

Let `U in R^(n x 3)` have orthonormal columns, and write its physical rows as `u_i^T`. Put

`mu=max_i ||u_i||_2^2`.                                          (2.1)

Choose independent Bernoulli variables `xi_i in {0,1}` with probability `1/2`, and set

`G=sum_i xi_i u_i u_i^T=U_S^T U_S`,                              (2.2)

where `S={i:xi_i=1}` and `T=S^c`. Since `sum_i u_i u_i^T=I_3`,

`E G=I_3/2`.                                                     (2.3)

The centered summands are independent and have mean zero. Therefore

`E ||G-I_3/2||_F^2`
` = (1/4) sum_i ||u_i u_i^T||_F^2`
` = (1/4) sum_i ||u_i||_2^4`
` <= (mu/4) sum_i ||u_i||_2^2`
` =3mu/4`.                                                       (2.4)

Hence at least one ACTUAL original-coordinate partition satisfies

`||G-I_3/2||_op <= ||G-I_3/2||_F <= sqrt(3mu)/2`.                (2.5)

For that same partition, because `U_T^T U_T=I_3-G`,

`boxed:
 U_S^T U_S >= a_mu I_3,
 U_T^T U_T >= a_mu I_3,
 a_mu=(1-sqrt(3mu))/2.
`                                                                  (2.6)

At the live diffuse gate `mu<=1/48`,

`boxed: a_mu>=3/8.`                                               (2.7)

This strengthens the earlier `1/4` balanced-half-cut constant and needs only the second-moment identity (2.4).

## 3. Spend the literal crossing while the fourth spectrum is moderate

Let `A=A^T` satisfy

`s_3(A)>=L>0`.                                                    (3.1)

Choose eigenvectors for its three largest absolute eigenvalues and write

`A=A_3+E=U Lambda U^T+E`,
`min_j |lambda_j|>=L`, `||E||op=s_4(A)`.                         (3.2)

Assume the selected frame is diffuse:

`mu=max_i ||U_{i,*}||^2<=1/48`.                                  (3.3)

Use the physical partition from Section 2. Its top-three crossing is

`B_0=A_3[S,T]=U_S Lambda U_T^T`.                                 (3.4)

Both `U_S` and `U_T` have least singular value at least `sqrt(a_mu)`, hence

`boxed: s_3(B_0)>=a_mu L>=3L/8.`                                 (3.5)

The ACTUAL crossing of the full matrix is

`B=A[S,T]=B_0+E[S,T]`.                                           (3.6)

A coordinate compression cannot increase operator norm, so if

`s_4(A)<=eta L`, `0<eta<a_mu`,                                   (3.7)

then Weyl gives

`boxed: s_3(B)>=(a_mu-eta)L.`                                    (3.8)

Consequently

`e_3(BB^T)>=s_1(B)^2 s_2(B)^2 s_3(B)^2`
`             >=(a_mu-eta)^6 L^6`.                              (3.9)

Apply (1.1) to this LITERAL original-coordinate crossing, retaining the full same-bank blocks `A[S,S]` and `A[T,T]`. We obtain

`boxed:
 ||p_Q||_infinity
 <= 6^(4/3)/((a_mu-eta)L),
 p_Q in C_0(R).
`                                                                  (3.10)

The complementary spectrum is never treated as a small random variable; only its deterministic cross-block operator norm enters Weyl.

## 4. Large fourth spectrum: ridge payment or physical localization

Suppose instead

`s_4(A)>eta L`.                                                   (4.1)

Then at least four eigenvalues have modulus `>eta L`. Let

`P_eta=1_{|A|>=eta L/64}`.                                       (4.2)

If

`max_k (P_eta)_kk<=1/32`,                                        (4.3)

the reviewed affine-uniform ridge-window theorem at scale `eta L` gives

`boxed:
 ||p_Q||_infinity <= C_R/(eta L),
 p_Q in C_0(R).
`                                                                  (4.4)

If (4.3) fails, choose an ORIGINAL physical coordinate `k` with `(P_eta)_kk>1/32`. Spectral energy gives

`||Ae_k||_2^2>(eta L/64)^2/32`,                                  (4.5)

so

`||Ae_k||_2>eta L/(256 sqrt2)`.                                  (4.6)

Since

`||Ae_k||_2^2=|A_kk|^2+||A[k,-k]||_2^2`,                         (4.7)

we obtain the concrete localized witness

`boxed:
 max{|A_kk|,||A[k,-k]||_2}>eta L/512.
`                                                                  (4.8)

## 5. Optimized live constants

At `mu=1/48`, put

`a=3/8`,
`C_X=6^(4/3)=10.902723556992836...`.                             (5.1)

Balance the two paid constants in (3.10) and (4.4):

`C_X/(a-eta)=C_R/eta`.                                           (5.2)

The optimizer is

`eta_* = C_R a/(C_R+C_X)`
`      =0.31987395050000694...`.                                 (5.3)

Both paid branches are then bounded by

`C_*=(C_R+C_X)/a`
`   =197.7780678260685...`.                                      (5.4)

Therefore:

### Theorem `QFORM-DIFFUSE-TOP3-THIRDCOMPOUND-RIDGE-ROUTER-v1`

If `s_3(A)>=L` and the three leading absolute-eigenvalue eigenvectors satisfy

`max_i ||U_{i,*}||^2<=1/48`,                                    (5.5)

then either

`boxed:
 p_Q in C_0(R),
 ||p_Q||_infinity <197.779/L,
`                                                                  (5.6)

or there is an ORIGINAL physical coordinate `k` satisfying

`boxed:
 max{|A_kk|,||A[k,-k]||_2}
 >0.0006247538095703261 L.
`                                                                  (5.7)

This improves the preceding diffuse-to-localized bridge's `<4049/L` paid constant and `L/32768` localized witness, and it enlarges the directly paid crossing regime from a tiny `s_4` perturbation to `s_4<=0.31987 L`.

## 6. Designated account04/B08 partner applied at an actual inequality

The r49 deletion-spill lemma proved, for any ORIGINAL coordinate `i` whose top-three leverage is `p_i`, and its literal deletion child `C_i=A[-i,-i]`,

`s_3(C_i)>=(1-p_i)L-s_4(A)`.                                     (6.1)

On the small-fourth-spectrum branch `s_4(A)<=eta_* L`, every coordinate in the diffuse frame obeys `p_i<=1/48`, hence

`boxed:
 s_3(C_i)>=m_*L,
 m_*:=47/48-eta_*=0.6592927161666597... .
`                                                                  (6.2)

Apply the designated account04/B08 theorem (1.3) to this ACTUAL deletion child. If its physical spectral projection onto

`|lambda(C_i)|>=m_*L/64`                                         (6.3)

has maximum diagonal `<=1/32`, then

`boxed:
 ||p_Q||_infinity
 <= C_R/(m_*L)
 <95.958/L,
 p_Q in C_0(R).
`                                                                  (6.4)

If that child window is not diffuse, choose its high-leverage physical coordinate `j`. The same spectral-energy calculation inside the literal child gives the parent witness

`boxed:
 max{|A_jj|,||A[j,-j]||_2}
 >m_*L/512
 =0.0012876810862630073... L.
`                                                                  (6.5)

Thus the partner theorem is not merely cited: it is applied at the forced child scale (6.2). It gives an independently structured `<95.958/L` payment or a stronger localized witness inside the small-`s_4` regime. The third-compound route (3.10) remains useful because it pays that regime unconditionally, without requiring a diffuse child window.

## 7. Regression computation

A deterministic `192 x 3` tight physical frame with 64 repeated rows in each spectral direction has row leverage `mu=1/64`. For this frame

`(1/4) sum_i ||u_i||^4 =3mu/4=0.01171875`,                       (7.1)

so the inequality in (2.4) is attained exactly. Taking 32 rows from each block gives `U_S^T U_S=I/2` exactly. Twenty-five seeded symmetric-tail tests with operator norm below `eta_* L` produced zero violations of the Weyl lower bound (3.8); the minimum observed slack was `0.003179462736150662`. These checks are regression evidence only; Sections 2--6 are analytic.

## 8. Remaining implication

The diffuse eigenvector branch is now reduced more sharply to the physical localized-row compiler:

`QFORM-LOCALIZED-ROW-PLUS-THREE-SPECTRAL-DIRECTIONS-COMPILER-v2`.

Starting from

`max{|A_kk|,||A[k,-k]||_2}>0.00062475 L`                         (8.1)

and the original `s_3(A)>=L`, produce a universal density bound while retaining arbitrary signs, arbitrary complementary spectrum and all original-coordinate product structure. A lone scalar/star witness is not itself enough; current corrections rule out several one-pivot/one-star shortcuts. The new account02/B01 heavy-star edge/tail half-Riesz theorem can consume a localized star when a second independent star tail is quantitatively present, so the next useful split is almost-single-edge versus nontrivial edge-tail currency.

Full unrestricted QFORM and the global continuous-density conclusion remain **OPEN**. The paid r50 branches are `C_0`.
