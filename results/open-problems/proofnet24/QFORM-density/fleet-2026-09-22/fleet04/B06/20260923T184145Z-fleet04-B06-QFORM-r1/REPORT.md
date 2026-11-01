SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B06, 2026-09-23T18:41:45Z.
attacking: the live exact-rank-three three-bank/shear packet by spending all three physical curvatures on one original-coordinate bank before Fourier inversion; no fiber supremum and no rotated independence.

# fleet04/B06 — bankwise triple-curvature receiver

Run: `20260923T184145Z-fleet04-B06-QFORM-r1`

Status: `ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREM PROVED / FULL TARGET OPEN / GLOBAL CONTINUITY OPEN`

## 1. Scope and pinned inputs

The target remains the unrestricted bounded-density conjecture: independent real original coordinates with probability densities at most one, arbitrary dimension, and an arbitrary real symmetric matrix with at least three singular values at least one. No support, moment, iid, sign, or post-rotation independence assumption is introduced.

Fresh brain main was `math-research-brain@bbce6f338d76cf687cebce3528e48f4613bd24bf`. The newest checked Claude directory source is `math-open-problems@b0cbc2233369b6a3f366cf569d425f485f123e1c`; it retains the correction that an arbitrary bounded joint density does not support a three-dimensional coarea bound.

Two completed results are used at displayed inequalities.

1. fleet01/B06, commit `3ae4b0c272e0d3c60f956c9f039bea38fc0f9077`, proves the translation-uniform product Fourier/Brascamp--Lieb estimate. For a normalized tight frame in dimension three whose physical leverage scores are at most one half,

       integral_(R^3) product_k |psi_k(<rho_k,z>+c_k)| dz
       <= (4 pi)^3.                                             (1.1)

   The shifts `c_k` are arbitrary. This is the input that permits conditioning on every coordinate outside the selected physical bank without taking a worst conditional-density supremum.

2. fleet04/B20 r11, commit `9d07c5d5c69c885509db66cb1093acdeff8bcb64`, supplies the live exact-rank-three chamber. For a physical indefinite pair `I`,

       A = [[B,C],[C^T,C^T B^(-1) C + lambda h h^T]],
       D = |det B|,
       D |lambda| = |det Lambda| tau,                             (1.2)

   where `||h||=1`, `tau>=1/4`, and the three singular values of `A` are at least one. In the unpaid diffuse-normal branch it also gives disjoint banks `J1,J2,J3` with

       W_b = sum_(k in J_b) h_k^2,
       W1 W2 W3 > 61/1728.                                      (1.3)

## 2. Exact bankwise curvature representation

Diagonalize the literal two-by-two physical pair algebraically,

       B = O diag(mu_1,mu_2) O^T,

where `mu_1 mu_2 = det B < 0`. Put

       S = B^(-1) C,
       (g_1^T,g_2^T)^T = O^T S.                                 (2.1)

This is only an identity in the quadratic polynomial. No independence of the rotated pair `O^T X_I` is claimed or used.

Fix one of the original-coordinate banks `J_b` and set

       r_k = (g_1k,g_2k,h_k)^T,  k in J_b,
       G_b = sum_(k in J_b) r_k r_k^T.                            (2.2)

Condition on every coordinate outside `J_b`, including the two physical pair coordinates. The conditional quadratic polynomial in the still-independent coordinates `Y=X_(J_b)` is

       mu_1(<g_1b,Y>+xi_1)^2
       + mu_2(<g_2b,Y>+xi_2)^2
       + lambda(<h_b,Y>+xi_3)^2 + affine constant,                (2.3)

where the three centers may be arbitrarily dependent functions of the conditioned coordinates.

### Theorem 2.1 — `QFORM-BANKWISE-TRIPLE-CURVATURE-v1`

If `G_b` is invertible and every physical leverage

       ell_k = r_k^T G_b^(-1) r_k <= 1/2,                         (2.4)

then the full form has a continuous density and

       ||p_Q||_infinity
       <= 12 [D |lambda| det G_b]^(-1/3)
       = 12 [|det Lambda| tau det G_b]^(-1/3).                    (2.5)

Proof. Apply damped Fresnel linearization to all three squares in (2.3) before taking absolute values. After normalizing the rows by `G_b^(-1/2)`, fleet01/B06 estimate (1.1) applies at the actual integral

       integral_(R^3) product_(k in J_b)
       |psi_k(<r_k,u>+c_k)| du
       <= (4 pi)^3 / sqrt(det G_b).                               (2.6)

Thus

       |phi_Q(t)| <= min(1,K_b |t|^(-3/2)),
       K_b = (4 pi)^(3/2)
             [|mu_1 mu_2 lambda| det G_b]^(-1/2).                 (2.7)

The conditioning weights are probability weights and remain inside the expectation; the bound is uniform only because the shifts in (2.6) are harmless. Finally

       integral_R min(1,K |t|^(-3/2)) dt = 6 K^(2/3),             (2.8)

and Fourier inversion gives (2.5). The integrable characteristic function also gives the stated branchwise continuity. QED.

This is aggregate curvature before inversion: the singular `|t|^(-3/2)` factor is paid against the complete three-dimensional product Fourier volume. There is no supremum over a curved fiber.

## 3. Concrete application to the live three-bank packet

Since all singular values are at least one and `tau>=1/4`, (1.2) gives

       D |lambda| = |det Lambda| tau >= 1/4.                      (3.1)

Also (1.3), together with `W_b<=1`, implies separately

       W_b > 61/1728  for b=1,2,3.                                (3.2)

Therefore, if any one bank obeys the diffuse triple-frame gate (2.4) and the aggregate transversality gate

       det G_b >= W_b/64,                                        (3.3)

then

       ||p_Q||_infinity
       < 12 [61/(4*1728*64)]^(-1/3)
       = 232.2732529465... .                                     (3.4)

This is a real bound on the live original-coordinate matrix, not a model family. It retains the same-bank shear projections `g_1b,g_2b` that prevented use of the mere joint cap for `(H_1,H_2,H_3)`.

## 4. Sharpened unpaid state

Consequently the exact-rank-three diffuse-normal survivor is now restricted as follows. For every one of its three disjoint banks, at least one of these holds:

1. a physical coordinate carries more than one half of that bank's normalized three-curvature leverage;
2. the bank is quantitatively shear-flat:

       det Gram(g_1b,g_2b,h_b) < ||h_b||^2/64.                    (4.1)

The second alternative has the exact geometric factorization

       det Gram(g_1b,g_2b,h_b)
       = det Gram(g_1b,g_2b)
         dist(h_b,span{g_1b,g_2b})^2.                             (4.2)

Thus the remaining hybrid is no longer an unstructured moving ridge. On each bank it has either a literal heavy physical hub or a quantified collapse of shear area times normal distance. This is the appropriate input for the heavy-hub receivers and for a grouped descent along the nearly common shear plane.

For reference, the global three-form Gram matrix satisfies the exact consistency identity

       det(G + diag(1,1,0)) = 1/tau,                              (4.3)

where `G=sum_b G_b`. Indeed the three linear forms consisting of the two completed pair coordinates and `h^T Z` represent the exact rank-three matrix by congruence; comparing products of its nonzero eigenvalues gives (4.3). This prevents treating all shear-flat alternatives as zero information: their mixed-bank curvature is constrained by the original physical pair.

The next implication is to combine (4.1)--(4.3) with a heavy-hub receiver or a mixed-bank version of (2.6), without replacing the three banks by an arbitrary joint density. Extension to arbitrary additional spectrum also remains open.

## 5. Status

This closes the aggregate-transverse/diffuse-leverage portion of the live three-bank/shear packet with the explicit cap `232.274`. It does not prove or disprove the full universal conjecture. No target counterexample is produced. Global continuity remains open; continuity is proved only on the branch covered by Theorem 2.1.
