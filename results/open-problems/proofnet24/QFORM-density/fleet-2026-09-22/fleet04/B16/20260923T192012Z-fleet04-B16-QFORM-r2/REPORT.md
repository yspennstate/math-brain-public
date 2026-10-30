SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B16, 2026-09-23T19:20:12Z.
attacking: projection-product overlap closure on the live exact-rank-three physical-pair/three-bank packet, retaining same-bank dependence and aggregate curvature before inversion.

# fleet04/B16 r2 — physical-pair overlap receiver for the live Schur banks

Programme: QFORM-DENSITY-3EIG-20260922
Run: 20260923T192012Z-fleet04-B16-QFORM-r2
Status: ESSENTIAL_STEP_APPLIED / NEW LIVE-BRANCH RECEIVER / FULL QFORM OPEN
Regularity: continuous density on the proved branch; global continuity remains open.

## 1. Scope and source pins

The target remains the unrestricted one: independent real original-coordinate inputs with one-dimensional probability densities at most one, arbitrary finite dimension, and arbitrary real symmetric A with at least three eigenvalues of modulus at least one. No moment, support, iid, sign, exact-rank, smoothness, or post-rotation independence hypothesis is added to the target.


Three completed mathematical inputs are used at displayed equations.

1. fleet01/B16, report available at math-open-problems@bfb102a2317191969c16cf336b53ed47a8a06c6d,
   proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B16/fleet01-B16-20260923T170732Z-auto11/REPORT.md,
   theorem QFORM-CROSS2-OVERLAP-SQUARE-L1-v1. If a three-dimensional projection (Z,T) of one original source bank has joint density cap M, a two-dimensional projection W of a disjoint original source bank has joint density cap N, and

       Q = 2 Z^T Sigma W
           + lambda (T+a^T Z+u)^2
           + r(Z)+H(X_W),

   with Sigma=diag(s_1,s_2), then

       ||p_Q||_infinity
       <= C_* (MN)^(2/5)(s_1s_2)^(-2/5)|lambda|^(-1/5),       (1.1)

       C_* = 5(675/256)^(1/5)
           = 6.069917185377548... .

   The theorem permits arbitrary dependence inside (Z,T) and inside W; independence is used only between their disjoint ORIGINAL banks. It also supplies an L1 characteristic-function bound and hence continuity.

2. The actual product-projection theorem used by fleet01/B16 gives, for a three-row map L applied to a cap-one product bank,

       ||p_(LX)||_infinity
       <= 2^(3/2) / sqrt(det(LL^T)).                           (1.2)

   This is a joint-density theorem, not projected independence.

3. The live exact-rank-three packet is fleet04/B20 r11 at commit
   9d07c5d5c69c885509db66cb1093acdeff8bcb64 together with fleet04/B06 r1 at commit
   205481d65e155470ceb4eb37c1601679abbda5e0. For an indefinite physical pair I, after algebraically diagonalizing its literal 2 by 2 block,

       B = O diag(mu_1,mu_2) O^T,    D=|mu_1mu_2|,

   the completed residual coordinates have coefficient vectors g_1,g_2,h and

       D |lambda| = |det Lambda| tau,                            (1.3)

   where tau is the squared physical-pair area. In the unpaid branch tau>=1/4, the three active singular values are at least s>=1, and there are three disjoint original-coordinate banks J_b with

       W_b=||h_b||_2^2,     W_1W_2W_3>61/1728.                  (1.4)

   Thus each W_b>61/1728.

All live corrections are retained: no arbitrary-joint coarea, no conditional-density supremum, no independence after rotation, and no deletion of small quadratic leakage for unbounded inputs.

## 2. New live receiver

For one residual bank J_b define

       G_b = Gram(g_1b,g_2b,h_b).                                (2.1)

### Theorem 2.1 — QFORM-PHYSICALPAIR-BANK-OVERLAP-v1

If G_b is positive definite, then the full exact-rank-three quadratic form has a continuous density and

       ||p_Q||_infinity
       <= C_pair [D |det Lambda| tau det G_b]^(-1/5),            (2.2)

where

       C_pair = 2^(3/5) C_*
              = 9.200274035222916... .                           (2.3)

There is no leverage hypothesis on the rows of the bank.

### Proof

Condition on every original coordinate outside the literal pair I and the selected bank J_b. Put

       (W_1,W_2)^T = O^T X_I,

       Z_1=<g_1b,X_(J_b)>,
       Z_2=<g_2b,X_(J_b)>,
       T  =<h_b,X_(J_b)>.                                        (2.4)

The pair variable W is independent of (Z_1,Z_2,T) because their ORIGINAL source sets are disjoint. Although O rotates the two physical coordinates, its determinant has modulus one, so the transformed pair has its true joint density

       p_W(w)=f_i((O w)_1) f_j((O w)_2),

and hence

       ||p_W||_infinity <=1.                                     (2.5)

No independence of W_1 and W_2 is claimed.

By (1.2),

       ||p_(Z_1,Z_2,T)||_infinity
       <= 2^(3/2)(det G_b)^(-1/2).                               (2.6)

Under the conditioning, the exact completed-square identity is

       Q = mu_1(W_1+Z_1+xi_1)^2
           +mu_2(W_2+Z_2+xi_2)^2
           +lambda(T+xi_3)^2 + constant,                         (2.7)

with arbitrary conditioned shifts xi_j. Expanding (2.7), reflecting one W coordinate if needed, and absorbing all pure-W terms into H and all pure-Z terms into r puts the form exactly into (1.1) with

       s_1=|mu_1|,  s_2=|mu_2|,
       M=2^(3/2)(det G_b)^(-1/2),  N=1.                          (2.8)

Therefore

       ||p_Q||_infinity
       <= C_* 2^(3/5)
          (det G_b)^(-1/5) D^(-2/5)|lambda|^(-1/5)

       = C_pair [D^2 |lambda| det G_b]^(-1/5).                   (2.9)

Using (1.3), D^2|lambda|=D|det Lambda|tau, which is (2.2). The bound is uniform in every conditioned shift. Averaging retains it. The uniform L1 characteristic-function estimate in fleet01/B16 also survives the averaging, proving continuity on this branch. QED.

This is the physical-pair specialization of fleet01/B16's rank-(3,2) compiler, but it improves its numerical factor: the generic two-dimensional projection cap 2 is replaced by the exact cap 1 of the literal two-coordinate pair.

## 3. Concrete inequality on the live three-bank packet

Let s be the least modulus of the three active eigenvalues. Then

       |det Lambda| >= s^3.                                      (3.1)

Suppose one live bank satisfies the super-volume gate

       det G_b >= W_b s^2/(64 D tau).                            (3.2)

Insert (3.1)-(3.2) into (2.2):

       D |det Lambda| tau det G_b
       >= W_b s^5/64.                                            (3.3)

Using W_b>61/1728 from (1.4),

       ||p_Q||_infinity
       < C_pair (64*1728/61)^(1/5) s^(-1)

       = 41.2552799658... s^(-1)
       <= 41.256.                                                 (3.4)

This is an actual bound on the live original-coordinate matrix. It permits arbitrary dependence among the three projections from J_b, arbitrary physical leverage in that bank, all conditioned affine shifts, and arbitrary same-bank quadratic terms already present in the exact completion.

## 4. Comparison with the bankwise Fresnel receiver

The fleet04/B06 receiver proves

       ||p_Q||_infinity
       <=12 [|det Lambda| tau det G_b]^(-1/3)                    (4.1)

when every normalized row leverage in bank b is at most 1/2. At the live gates it pays any such bank with det G_b>=W_b/64 by <232.274.

The new receiver (2.2) is complementary:

- it has no row-leverage restriction;
- it pays any bank satisfying the stronger scale-adjusted super-volume gate (3.2) by <41.256;
- it uses the curved scalar fiber jointly with the rank-two physical crossing, rather than taking a worst conditional density.

Consequently the previously stated live alternative sharpens. After the B06 and present receivers, every unpaid bank J_b must satisfy at least one of

       det G_b < W_b/64,                                        (4.2)

or

       max_k r_k^T G_b^(-1) r_k >1/2
       and
       det G_b < W_b s^2/(64 D tau).                            (4.3)

Thus an intermediate-volume bank can survive only by having a literal heavy normalized physical row, while a diffuse-leverage bank is already paid; any leverage profile with sufficiently large scale-adjusted volume is paid by the overlap theorem.

This is a genuine reduction of the hybrid chamber, not a full solution. The remaining exact-rank-three endpoint consists of shear-flat banks and heavy-row intermediate-volume banks, together with the mixed-bank consistency identity

       det(G+diag(1,1,0))=1/tau.                                (4.4)

The extension from exact rank three to arbitrary additional spectrum also remains open.

## 5. Integrity and status

The full universal QFORM density conjecture remains OPEN / NOT PROVED / NOT DISPROVED. Global continuity remains open. The result above proves continuity only on its branch.

The mathematics uses only original-source independence between the selected residual bank and the literal physical pair. It does not infer independence after O, and it uses the actual joint cap (2.5), not coordinatewise independence. No schedule, task, notification, account binding, public release, permission, paid call, or remote workflow was changed.
