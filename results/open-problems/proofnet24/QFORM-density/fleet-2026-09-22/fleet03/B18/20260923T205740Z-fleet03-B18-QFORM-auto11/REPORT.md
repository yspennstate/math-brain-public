SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B18, 2026-09-23T20:57:40Z.
attacking: literature-to-proof transfer for the exact-null-hub private bank with g_K=0 and a genuinely transverse twist ell_K; convert that twist into a rank-two original-bank cross determinant, then splice the completed fleet04/B18 N3 moderate-edge theorem.

# fleet03/B18 auto11 — private transverse-twist cross closure

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Status:** PROVED SUPPORTING TARGET-LEVEL BRANCH / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN  
**Continuity:** continuous C_0 density for the new theorem; full-target continuity remains open.  
**Execution:** WITHOUT_VERIFIED_BRAIN.

## 1. Exact theorem

Let X_0 and the original leaf coordinates X_L be mutually independent real random variables, each with a probability density bounded by one. Consider the exact-null-hub normal form

Q = 2 (X_0 + ell·X_L)(g·X_L) + d (beta·X_L)^2,                 (1)

where d is nonzero, beta·g=0, ||beta||_2=1 and gamma=||g||_2>0. Split the ORIGINAL leaf coordinates into disjoint banks L=J disjoint_union K and assume

g_K=0.                                                               (2)

Put

b = ||beta_J||_2,
rho = ||beta_K||_2,
eta = ||P_{beta_K^perp} ell_K||_2,                                  (3)

where eta is defined when rho>0. If

b rho eta >0,                                                        (4)

then Q has a continuous density vanishing at infinity and

||p_Q||_infinity
 <= 3*2^(5/6) [ |d| gamma^2 b rho eta ]^(-1/3).                     (5)

Call this `QFORM-NULLHUB-PRIVATE-TRANSVERSE-CROSS-v1`.

No moment, iid, symmetry, centering, compact-support, connected-support, smoothness, Gaussian, or log-concavity assumption is used. No rotated random coordinates are declared independent.

## 2. Primary literature transfer

The sole external anti-concentration theorem needed is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889; arXiv:1507.07949, Theorem 1.1. For a product probability density with all one-dimensional factors bounded by one, every k-dimensional orthogonal marginal has density bounded by 2^(k/2).

A full-row-rank 2 x m coefficient matrix T can be written T=G^(1/2)P with PP^T=I_2 and G=TT^T. Therefore LPP gives the exact linear-map consequence

||p_(T X)||_infinity <= 2 / sqrt(det(TT^T)).                          (6)

This is only a joint-density cap. It is not an independence statement, and it is not used as an arbitrary-joint quadratic coarea theorem.

The analytic receiver used below is the completed fleet03/B18 theorem `QFORM-RANK2-CROSS-PLUS-SCALAR-SLOPE-FRESNEL-v1`, source

math-open-problems@792c7b328e6de0e43132b2bf44e904c9ec023abd
proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B18/20260923T125902Z-fleet03-B18-QFORM-r29/REPORT.md.

Its hypotheses are three genuinely independent ORIGINAL source blocks Z,X,Y, arbitrary same-bank measurable potentials F(X),G(Y), a nonzero scalar-to-X slope c, and a rank-two X-Y cross matrix B with singular product Delta. It proves

||p||_infinity <= 3*2^(5/6) (||c||_2 Delta)^(-1/3),                 (7)

and a continuous C_0 density. Its proof applies LPP only to genuine product-source linear projections and obtains |phi(t)|=O(|t|^-3/2) from one one-dimensional and one two-dimensional Plancherel gain. Thus it is compatible with every live correction concerning pointwise quadratic-phase decay and post-rotation independence.

## 3. Exact null-hub reduction

Define the bank variables

G = g_J·X_J,
C = beta_J·X_J,
E = ell_K·X_K,
B = beta_K·X_K.                                                       (8)

Because g_K=0, equation (1) expands exactly as

Q = 2 X_0 G
    + [2(ell_J·X_J)G + d C^2]
    + d B^2
    + 2 G E + 2 d C B.                                               (9)

Set Z=X_0, X=X_J and Y=X_K. Then (9) is exactly the receiver form with

c = g_J,
F(X_J)=2(ell_J·X_J)(g_J·X_J)+d(beta_J·X_J)^2,
G_K(X_K)=d(beta_K·X_K)^2,                                            (10)

and rank-at-most-two cross matrix

M = g_J ell_K^T + d beta_J beta_K^T.                                (11)

There is no discarded term.

Since beta·g=0 and g_K=0,

<g_J,beta_J>=0.                                                       (12)

Write U=[g_J,beta_J], V=[ell_K,beta_K], and D_2=diag(1,d). Then

M = U D_2 V^T.                                                       (13)

Under (4), both U and V have column rank two, so M has rank two. QR reduction of U and V shows that the product Delta of the two nonzero singular values of M is

Delta = |det D_2| sqrt(det(U^T U) det(V^T V)).                       (14)

Now

det(U^T U)=gamma^2 b^2,                                             (15)

and by the definition of eta,

det(V^T V)
 = ||ell_K||^2 rho^2 - <ell_K,beta_K>^2
 = rho^2 eta^2.                                                      (16)

Therefore

Delta = |d| gamma b rho eta.                                        (17)

Also ||c||=||g_J||=gamma. Substituting (17) into (7) proves (5). Since the receiver has phi in L^1, the output density has a continuous C_0 representative. QED.

## 4. Why this closes a real branch

The preceding fleet03/B18 run r34 paid the exact aligned private-bank endpoint ell_K parallel beta_K by a random-centre square smoother. The present theorem pays the complementary genuinely transverse case eta>0 with an explicit quantitative currency.

It is important that (5) is not perturbative near eta=0. The constant diverges as eta decreases to zero, while r34 pays the exact eta=0 endpoint by a different mechanism. For arbitrary rough input laws one may not delete a small nonzero transverse twist. Thus the still-unpaid local collar is the genuinely near-parallel regime 0<eta<<1 when no other compiler exit applies.

Inside the target-normalized exact-rank-three moderate/high-shear null-hub compiler, the fleet identity is

|d| gamma^2 = h D,    h>=1/5,    D>=1.                              (18)

Hence (5) gives

||p_Q||_infinity
 <= 3*2^(5/6) [ (b rho eta)/5 ]^(-1/3).                             (19)

The completed designated-partner fleet04/B18 r4 theorem states that inside N3(1/64), any heavy witness q_i>1/2 with |g_i|>=1/64 obeys

||p_Q||_infinity < 64.1795826152.                                   (20)

Matching (19) to the partner benchmark shows that the private-transverse exit also gives at most the same 64.1795826152 bound whenever

b rho eta >= 0.0028888041046934566.                                 (21)

Thus a surviving N3 exact-null state must fail the partner moderate-edge exit and, whenever a g-zero private bank is available, must also have very small private-transverse currency unless another completed exit applies.

## 5. Literal target-valid N3 family and partner application

The partner theorem is applied here at an actual target-normalized family, not merely quoted abstractly.

Take one hub coordinate X_0; one leaf G with g_G=1 and beta_G=0; 64 J-bank beta coordinates and 64 K-bank beta coordinates, each with beta coefficient 1/sqrt(128); and one additional K-bank coordinate E with ell_E=1 and beta_E=0. All other ell coefficients vanish. Set d=1.

Then

gamma=1,
b=rho=1/sqrt(2),
eta=1,
q_G=1.                                                              (22)

Every physical diagonal is either zero or 1/128, hence this family lies in N3(1/64). The active aggregate quadratic form is

Q = 2 (X_0+E) G + BETA^2,                                           (23)

where BETA is the normalized beta projection. On the orthonormal aggregate basis (X_0,G,E,BETA), the matrix is

[[0,1,0,0],
 [1,0,1,0],
 [0,1,0,0],
 [0,0,0,1]].                                                        (24)

Its spectrum is

{-sqrt(2),0,1,sqrt(2)},                                              (25)

so it has exactly three eigenvalues of modulus at least one. Here D=2, h=1/2 and hD=1, so the fleet04/B18 r4 hypotheses are satisfied. Its heavy witness G has q_G=1 and |g_G|=1>=1/64. Therefore the designated partner theorem gives the actual inequality

||p_Q||_infinity < 64.1795826152.                                   (26)

The new theorem is much sharper on the same family:

||p_Q||_infinity
 <= 3*2^(5/6) (1/2)^(-1/3)
 = 3*2^(7/6)
 = 6.734772289856238... .                                           (27)

The density in (27) is continuous C_0.

## 6. Literature scope and correction discipline

LPP is used only for bounded densities of linear projections of original-coordinate product laws. A rotation is never used to create independent eigen-coordinates. The theorem does not invoke a law-uniform pointwise van-der-Corput estimate. It does not infer an indefinite quadratic pushforward bound from a projection cap alone; the nonlinear step is the already-proved Plancherel/Fresnel receiver. No fixed uniformly good physical minor is asserted.

Banks--Garza Vargas--Kulkarni--Srivastava already contain anti-concentration results for pure two-bank bilinear/affine subcases, so no novelty claim is made for that narrow literature scope. The present implication retains arbitrary same-bank quadratic potentials through (10), and this report makes no external novelty claim.

## 7. Remaining implication

The unrestricted QFORM conjecture remains OPEN / NOT PROVED, and full-target continuity remains open. This run closes the exact g_K=0, b rho eta>0 private-transverse branch. Together with r34 it pays exact alignment and quantitatively transverse misalignment, but not uniformly the punctured near-parallel collar 0<eta<<1. More globally, the bare hypothesis s_3(A)>=1 still does not force this source split, and arbitrary additional spectrum remains part of the assembly problem.

A useful next mechanism is a nonperturbative interpolation that retains the small transverse term 2(g_J·X_J)(P_{beta_K^perp}ell_K·X_K) exactly while spending the private square, rather than deleting the transverse term or assuming moments.
