SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B17, 2026-09-22T23:29:12Z.
attacking: partial-leverage three-heavy orthogonal-frame stress families, testing whether intermediate leverage can overshoot the 3*sqrt(2) diffuse lower-bound scale and extracting the exact first correction.

# QFORM-B17 partial-leverage three-heavy barrier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `B17-20260922T232912Z-r11-partial-heavy`  
Assignment: sharp constant and witnesses  
Status: `NEW SUPPORTING THEOREM / FULL CONJECTURE OPEN`  
Execution memory: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact source-valid family

Let `sigma^2=1/12`. Fix a unit vector `u in R^3` and put

`B_u = I_3 - 2 u u^T`.

Then `B_u` is symmetric orthogonal with eigenvalues `{1,1,-1}`. Fix `0<=ell<1`. For every integer `m>=1`, use `3+3m` independent physical coordinates, all `Uniform[-1/2,1/2]`. Define a `3 x (3+3m)` synthesis matrix `C_{m,ell}` by giving it three heavy columns

`sqrt(ell)e_1, sqrt(ell)e_2, sqrt(ell)e_3`

and, for each `j=1,2,3`, `m` diffuse columns

`sqrt((1-ell)/m)e_j`.

Then

`C_{m,ell} C_{m,ell}^T = I_3`.

Hence

`A_{m,ell,u}=C_{m,ell}^T B_u C_{m,ell}`

has exact nonzero spectrum `{1,1,-1}` for every finite `m`. This is an exact instance of the owner target; no post-rotation independence is assumed.

Writing the three heavy variables as `U_1,U_2,U_3` and the diffuse bank sums as

`S_{mj}=m^(-1/2) sum_{k=1}^m X_{jk}`,

the three aggregated coordinates are

`Y_{m,ell,j}=sqrt(ell) U_j + sqrt(1-ell) S_{mj}`,

and

`Q_{m,ell,u}=Y_{m,ell}^T B_u Y_{m,ell}`.

For fixed `ell<1`, the diffuse bank local CLT gives

`Y_{m,ell} => Y_ell`,

where the coordinates of `Y_ell` are independent copies of

`Y_ell^(1)=sqrt(ell) U + sqrt(1-ell) G`,

with `U~Uniform[-1/2,1/2]` and `G~N(0,sigma^2)` independent. The weighted local-CLT/coarea argument used in the completed account04/B17 theorem applies to this Gaussian-smoothed family, so the zero-density of the finite exact witnesses converges to the zero-density of `Y_ell^T B_u Y_ell`.

## 2. Main theorem: the first heavy-leverage correction is quadratic and negative

Let `p_{ell,u}` denote the density of

`Q_{ell,u}=Y_ell^T B_u Y_ell`.

Then, uniformly in `u in S^2`, as `ell downarrow 0`,

`p_{ell,u}(0)=3sqrt(2)[1-c(u) ell^2 + O(ell^3)]`,                 (2.1)

where

`c(u)=[177-39 sum_j u_j^4]/640`                                  (2.2)

and equivalently

`c(u)=69/320 + (39/1280) sum_{i<j}(B_u)_{ij}^2`.                 (2.3)

Therefore

`69/320 <= c(u) <= 41/160`.                                      (2.4)

In particular, there is an absolute `ell_0>0` such that for every orientation `u` and every `0<ell<=ell_0`,

`p_{ell,u}(0)<3sqrt(2)`.                                          (2.5)

The important sharp-constant feature is that the deficit is **quadratic** in the total leverage of each of the three physical heavy coordinates, not linear.

## 3. Proof of the small-leverage expansion

Let `f_ell` be the one-dimensional density of `Y_ell^(1)`, and let `gamma_sigma` be the centered Gaussian density of variance `sigma^2=1/12`. Its characteristic function is

`hat f_ell(xi)=exp(-(1-ell)xi^2/24) sinc(sqrt(ell)xi/2)`.

Factor out the limiting Gaussian:

`hat f_ell(xi)=exp(-xi^2/24) M_ell(xi)`,

where

`M_ell(xi)=exp(ell xi^2/24) sinc(sqrt(ell)xi/2)`.

The exact Taylor cancellation of the variance term is

`M_ell(xi)=1-ell^2 xi^4/2880-ell^3 xi^6/181440+O(ell^4 xi^8)`      (3.1)

for fixed `xi`. For `ell<=1/2`, the residual Gaussian factor gives a uniform Gaussian Fourier majorant after finitely many derivatives, so Fourier inversion upgrades (3.1) to the weighted density expansion

`f_ell(y)=gamma_sigma(y)[1-(ell^2/20)H_4(y/sigma)]
          + O(ell^3)(1+|y|)^(-8)`,                                (3.2)

uniformly in `y`, with `H_4(z)=z^4-6z^2+3`. Indeed `sigma^(-4)=144`, and `144/2880=1/20`.

Since the coordinates of `Y_ell` are independent,

`rho_ell(y)=gamma_sigma^(3)(y)
 [1-(ell^2/20) sum_j H_4(y_j/sigma)]
 + O(ell^3)(1+|y|)^(-8)`.                                         (3.3)

The rank-three cone coarea integral at zero is absolutely convergent against this weighted remainder. Choose an orthogonal matrix `O` whose third row is `u^T`; then

`B_u=O^T diag(1,1,-1) O`.

Parametrize the cone by

`y=O^T(r cos theta, r sin theta, epsilon r)`,

with `r>0`, `0<=theta<2pi`, and `epsilon in {+1,-1}`. Since `B_u^2=I`, each nappe contributes

`dH^2/|2B_u y| = (1/2) dr dtheta`.

The Gaussian term gives exactly

`p_{0,u}(0)=1/(2^(3/2)sigma^2)=3sqrt(2)`.                          (3.4)

Normalize the Gaussian cone measure. Put `q=r/sigma`; then

`E q^2=1/2`, `E q^4=3/4`.

If

`a_j=(O^T(cos theta,sin theta,epsilon))_j`

and `x_j=u_j^2`, the exact angular/sign averages are

`E a_j^2=(1+x_j)/2`,

`E a_j^4=(3+18x_j-13x_j^2)/8`.

Hence

`E H_4(q a_j)=(57+6x_j-39x_j^2)/32`,

and summing over `j` gives

`E sum_j H_4(q a_j)=[177-39 sum_j u_j^4]/32`.                     (3.5)

Multiplying (3.5) by the Edgeworth coefficient `1/20` in (3.3) proves (2.1)-(2.2). Formula (2.3) follows from

`sum_{i<j}(B_u)_{ij}^2=2(1-sum_j u_j^4)`,

and (2.4) follows from `1/3<=sum_j u_j^4<=1`.

The remainder in (3.3) is uniform in `u`: orthogonal rotations preserve `|y|`, the cone factor is scale-invariant, and `S^2` is compact. Since the coefficient has the uniform lower bound `69/320`, (2.5) follows.

## 4. Application of the completed designated partner result

The completed partner `account03/B17` theorem is:

`yspennstate/math-open-problems@63f692146f592bc250af369056573dc5e3720a8e`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260922T221945Z-account03-B17-QFORM-r19/REPORT.md`.

It proves for the pure three-bank uniform CLT witness

`p(0)=3sqrt(2)[1-c(u)/m+O_u(m^-2)]`

with exactly the same `c(u)` in (2.2). The reason the same coefficient appears here is structural rather than numerical: the normalized bank characteristic function has

`[sinc(xi/(2sqrt(m)))]^m
 = exp(-xi^2/24)[1-xi^4/(2880m)+O(m^-2)]`,

whereas the present partial-heavy Gaussian completion has

`hat f_ell(xi)
 = exp(-xi^2/24)[1-ell^2 xi^4/2880+O(ell^3)]`.

Thus `ell^2` replaces `1/m` at the first non-Gaussian order. I have rederived the cone contraction above rather than merely relabelling the partner coefficient.

The underlying completed weighted local Edgeworth/coarea theorem used by the partner is:

`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260922T211900Z-account04-B17-QFORM-r3/REPORT.md`.

## 5. Exact fully coupled witness and proof-mechanism consequence

Take the partner's exact rational orientation

`u_10=(10,10,49)/51`.

Every entry of `B_{u_10}` is nonzero, and

`c(u_10)=53990741/240540480
        =0.22445594604284486...`.

Therefore the fully coupled partial-heavy family satisfies

`p_{ell,u_10}(0)
 =3sqrt(2)[1-(53990741/240540480)ell^2+O(ell^3)]`.                 (5.1)

This gives a concrete source-valid stress constraint on any proposed sharp proof: **qualitative nonzero physical heavy leverage cannot be charged a fixed or linear density penalty near the diffuse obstruction.** Even with three genuine heavy physical coordinates and every effective bank coupling nonzero, the central density stays within `O(ell^2)` of `3sqrt(2)`.

Equivalently, any argument whose sharp branch would force a deficit `>=c ell` merely from the presence of three leverage-`ell` physical coordinates is false on this family for all sufficiently small `ell`.

This complements the designated partner's newest `QFORM-RARE-FRAGMENT-FIRST-ORDER-BARRIER-v1`: remote `m^-2` fragments make the first finite-bank deficit more negative, while a local contiguous heavy component has no linear effect at all and begins only at order `ell^2`.

## 6. Scope and next implication

This theorem does **not** prove that `3sqrt(2)` is the universal sharp constant, and it does not exclude an off-zero overshoot for the partial-heavy family. It proves only the exact central asymptotic and the source-valid finite-matrix approximation.

The next nonredundant witness question is therefore sharper: determine the global output maximum for intermediate `ell`, especially for genuinely non-collinear/fully coupled orientations, or exhibit a finite/mesoscopic off-zero overshoot. If no such overshoot exists, a uniform global no-escape theorem for the partial-heavy family would bridge the diffuse and saturated endpoint exclusions already proved by B17.

No refuted arbitrary-joint coarea, post-rotation independence, conditional-density cap, pointwise oscillatory decay, or single-minor extraction is used here.
