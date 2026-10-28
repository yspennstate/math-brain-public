SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B19, 2026-09-24T03:13:36Z.
attacking: the partner-r47 ultra-thin physical rank-two frontier after the pure-bilinear subcase — derive a curvature-robust fractional smoothing estimate and isolate the remaining third-resource upgrade.

# account02/B19 auto11 — curvature-robust rank-two fractional smoothing

Status: **ESSENTIAL STEP APPLIED / FULL QFORM OPEN / CONTINUITY OPEN**.

The exact owner target remains: independent real coordinates with densities bounded by one, arbitrary real symmetric A with at least three eigenvalues of modulus at least one, and a universal essential-density bound for X^TAX. No moment, support, log-concavity, iid, diagonal-basis or post-rotation-independence hypothesis is used below. Continuity is kept separate.

## 1. Source-pinned graph used in this run


The required pinned mathematical source was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

The specific completed inputs used below are its Theorem-D decoupling/volume-sampling proof, its D' Jensen extension, and Lemma 4.1 converting Fourier decay into fractional potentials. The present theorem is the k=2 version of exactly that argument, with q=2; it is written out so no unproved interpolation is hidden.

Newest completed designated partner consumed before this report was account03/B19 r47,

`yspennstate/math-open-problems@1a64d8ce29d893fd99b9af8dac5a63e359a9cc08`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260924T020346Z-account03-B19-QFORM-r47/REPORT.md`.

Its large-leaf-curvature endpoint gives either a paid physical E3 exit or an actual literal leaf cut N=A[R,C] lying within Frobenius distance 2^-16 of rank at most two. In the multiplicatively rank-two branch the **actual** N satisfies

sigma_1(N) sigma_2(N) > gamma_0 := 28159/(4194304 sqrt(2))
= 0.004747252428873060... .                                    (1.1)

All same-bank curvature and all outside couplings remain live there.

## 2. New theorem: physical rank-two crossing gives H_alpha for every alpha<1/2

Let I,J be disjoint sets of original coordinates and put M=A[I,J]. Define

Z_2 := e_2(M^T M)
    = sum_{|S|=|T|=2} det(M[S,T])^2.                              (2.1)

No rank-exactness assumption is made. Let

H_alpha(Q) := sup_s E |Q-s|^{-alpha},  0<alpha<1.                 (2.2)

### Theorem `QFORM-PHYSICAL-R2-FRACTIONAL-SMOOTHING-v1`

If Z_2>0, then for every real t,

|phi_Q(t)| <= min{1,
 (2 e pi^2)^(1/4) Z_2^(-1/8) |t|^(-1/2)}.                       (2.3)

Consequently, for every 0<alpha<1/2,

H_alpha(Q)
 <= [c_alpha/(alpha(1/2-alpha))]
    (2 e pi^2)^(alpha/2) Z_2^(-alpha/4),                         (2.4)

where

c_alpha = 2^(1-alpha) Gamma((1-alpha)/2)
          /(2 sqrt(pi) Gamma(alpha/2)).                          (2.5)

In particular

H_{1/4}(Q)
 <= C_{R2} Z_2^(-1/16),
C_{R2}=16 c_{1/4}(2e pi^2)^(1/8)
      =3.929131770449763... .                                    (2.6)

If sigma_1>=sigma_2 are the two largest singular values of M, then Z_2>=sigma_1^2 sigma_2^2, hence

boxed:
H_{1/4}(Q)
 <=3.92913177045 (sigma_1 sigma_2)^(-1/8).                       (2.7)

The theorem retains arbitrary A[I,I], A[J,J], all outside blocks and couplings, arbitrary affine terms, all signs, all further singular values and all extra spectrum. The only independence used is independence of disjoint original-coordinate product banks.

### Proof of (2.3)

Repeat the completed source Theorem-D Weyl differencing on the literal physical cut I|J. Condition on all coordinates outside I union J. Cauchy-Schwarz in X_I gives

|phi_Q(t)|^2 <= E_W F(W),                                       (2.8)

where W=X_J-X'_J has independent coordinates with densities
f_j * f~_j <=1 and

F(W)=prod_{i in I} |psi_i(2t(MW)_i)|.                           (2.9)

The same-bank quadratic blocks and all affine terms are phases and disappear at this step exactly as in the pinned source.

Use two-volume sampling weights

w_{S,T}=det(M[S,T])^2/Z_2,
|S|=|T|=2,                                                       (2.10)

and their row/column marginals alpha_i,beta_j. Necessarily

0<=alpha_i,beta_j<=1,
sum_i alpha_i=sum_j beta_j=2.                                   (2.11)

Unlike the k=3 density theorem, no small-marginal hypothesis is needed for the fractional conclusion. Since 0<=F<=1,

E F <= (E F^2)^(1/2).                                          (2.12)

Apply exactly the D' Brascamp-Lieb calculation to F^q with k=2 and q=2. The source L^p characteristic-function lemma is legal because q/alpha_i>=2 for every i. The Gaussian determinant computation gives

E F^2
 <= e^(2/2) (2pi)^2 2^(-2/2)
    |t|^-2 Z_2^-1/2
 = 2 e pi^2 |t|^-2 Z_2^-1/2.                                  (2.13)

Combining (2.8),(2.12),(2.13),

|phi_Q(t)|^2
 <= (2e pi^2)^(1/2)|t|^-1 Z_2^-1/4,                           (2.14)

which is (2.3) after taking a square root and intersecting with the trivial bound one.

### Proof of (2.4)

The pinned source Lemma 4.1 says that if

|phi(t)|<=min(1,B|t|^-b), b>alpha,

then

H_alpha <= c_alpha [2b/(alpha(b-alpha))] B^(alpha/b).           (2.15)

Insert b=1/2 and

B=(2e pi^2)^(1/4) Z_2^-1/8.                                   (2.16)

Since 2b=1, (2.15) is exactly (2.4). Taking alpha=1/4 gives (2.6), and Cauchy-Binet gives (2.7). QED.

## 3. Equation-level application to partner r47

In partner r47's strong physical-rank-two branch, (1.1) and (2.7) give for the **full ambient quadratic law**, without removing its same-bank leaf curvature or its 2^-16 coefficient tail,

boxed:
H_{1/4}(Q)
 < 3.92913177045 gamma_0^(-1/8)
 = 7.66904530231.                                                (3.1)

Equivalently every interval K of length delta obeys

P{Q in K}
 <= H_{1/4}(Q) (delta/2)^(1/4)
 < 6.44887270314 delta^(1/4).                                   (3.2)

This is the first source-valid smoothing statement on the entire r47 multiplicative-rank-two frontier that is simultaneously:

* insensitive to arbitrary same-bank curvature;
* insensitive to outside couplings and affine terms;
* valid for the actual N, including its nonzero tail;
* free of post-rotation independence;
* free of any physical-minor selection claim.

It does **not** by itself give L^infinity: the exponent 1/2 in (2.3) yields H_alpha only for alpha<1/2. A receiver must spend a genuinely additional source before the endpoint density follows.

## 4. A paid exact-rank-two diagonal-curvature subchamber

The same pinned Fresnel machinery pays a useful strict subcase and identifies what the missing same-bank obstruction actually is.

Assume M has exact rank two,

M=sigma_1 u_1v_1^T + sigma_2 u_2v_2^T,
P=sigma_1sigma_2>0,                                             (4.1)

and on L=I union J the whole self-curvature outside the crossing is physical-diagonal:

A[L,L]=D_L + [[0,M],[M^T,0]],                                  (4.2)

D_L diagonal. Outside L all coefficients may be arbitrary. Suppose the left and right singular two-frames are physically diffuse:

max_{i in I}(u_1(i)^2+u_2(i)^2)<=1/2,
max_{j in J}(v_1(j)^2+v_2(j)^2)<=1/2.                           (4.3)

### Theorem `QFORM-EXACTR2-DIAGONALCURVATURE-R4-FRESNEL-EXIT-v1`

Under (4.1)-(4.3),

boxed: ||p_Q||_infinity <= 8 P^(-1/2).                          (4.4)

Proof. The symmetric crossing has the orthonormal four-frame

w_{k,+}=(u_k,v_k)/sqrt2,
w_{k,-}=(u_k,-v_k)/sqrt2,

with coefficients +sigma_k,-sigma_k. Its physical row leverage is exactly the quantity in (4.3). The Fresnel linearisation and Brascamp-Lieb proof of source Theorem F is dimension-free in the number r of Fresnel modes; applying the same proof with r=4 and source bank L gives

|phi_Q(t)| <= (4pi)^2 P^-1 |t|^-2.                              (4.5)

Here the four-frame Gram is I_4 and the residual LxL block is the diagonal D_L. Fourier inversion using min(1,C|t|^-2) with C=(4pi)^2/P gives

||p_Q||_infinity
 <=(2pi)^-1 * 4 sqrt(C)
 =8 P^-1/2.                                                      (4.6)

No outside block was removed. QED.

At the partner scale P>gamma_0, this exact-rank-two diagonal-curvature subchamber is therefore paid by

boxed: ||p_Q||_infinity < 116.109785917.                         (4.7)

This theorem deliberately does not treat the actual r47 2^-16 tail as zero, and it does not treat arbitrary off-diagonal same-bank curvature as diagonal. Those are precisely the forbidden perturbative shortcuts.

## 5. Updated source-pinned proof graph

The compatible active graph after this run is:

1. Full target -> principal-minimal ORIGINAL-coordinate target by the completed same-constant descent.
2. Existing scalar/pair/triple, physical E3/E5, Fresnel/H, ridge/window, grouped and exact-pair exits are paid in their recorded scopes.
3. In the exact singular-pair/macroscopic-overlap branch, account01/B09 either pays directly or forces |tau|<1/8, s>2, ||D||op>7/8.
4. Partner account03/B19 r47 converts that large-leaf chamber into either:
   (a) E3>=2^-64, already paid by <13741; or
   (b) a literal strong multiplicative-rank-two leaf crossing satisfying (1.1); or
   (c) the giant near-rank-one / aligned low-rank carrier frontier.
5. This run upgrades branch 4(b), with **no curvature restriction**, to the full ambient fractional estimate (3.1)-(3.2). It also completely pays the exact-rank-two diagonal-self-curvature diffuse-frame subchamber by (4.4).
6. Branch 4(c), the rank<=9 third-mode skeleton, arbitrary-extra-spectrum closure, and unrestricted continuity remain open.

The first compatible unpaid implication is therefore sharpened to

`QFORM-R47-R2-HALFPOTENTIAL-UPGRADE-OR-GIANTR1/R9-PAYMENT-v1`:

Starting from either

(A) a literal physical crossing with sigma_1sigma_2>=gamma_0 and the now-proved universal H_alpha control for every alpha<1/2, but with arbitrary same-bank curvature; or

(B) the aligned giant-near-rank-one / rank<=9 third-resource carrier from the existing compiler,

produce a universal L^infinity output bound while retaining every coefficient, all original-product provenance, arbitrary signs/affine terms and extra spectrum. In branch (A), a successful receiver must supply a genuinely additional half-level of smoothing: simply rerunning two-volume decoupling cannot cross alpha=1/2, and replacing same-bank curvature by a diagonal or dropping the nonzero cross tail is not valid.

## 6. What is and is not proved

The new fractional theorem is unconditional in its stated physical-cross-block scope and is applied to a real current partner obstruction at equation level. The rank-four Fresnel theorem is a separate exact subbranch. Neither is a full proof of QFORM. No counterexample to the exact target is produced. Continuity of the unrestricted target remains open. The required two independent end-to-end reviews do not exist.
