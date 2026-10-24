SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-23T21:30:06Z.
attacking: the indefinite near-null two-hub collar; convert partner r44's anchored third-curvature bank into an ORIGINAL-coordinate cross-volume that can be spent before any hyperbolic fiber supremum.

# Early calculation: anchored-K wedge currency survives the first physical square peel

Full QFORM remains OPEN. The first unpaid implication is `QFORM-INDEFINITE-NEARNULL-ANCHORED-K-RECEIVER-v1` from account03/B06 r44.

Write the literal original-coordinate matrix on physical hubs X,Y and environment Z as

A = [[a,b,alpha^T],[b,d,beta^T],[alpha,beta,C]],  a != 0.

After completing only the ORIGINAL coordinate X, set

  delta = d-b^2/a,
  gamma = beta-(b/a)alpha,
  R = C-alpha alpha^T/a.

The remaining quadratic matrix on (Y,Z) is

  S1 = [[delta,gamma^T],[gamma,R]].

For H=[[a,b],[b,d]], E=[alpha^T;beta^T], partner r44's exact anchored bank is

  K_H = det(H) C-E^T adj(H) E.

Direct expansion gives the key identity

  K_H = a(delta R-gamma gamma^T).                                    (E1)

Now choose disjoint environment index sets U,V. For u in U and v<w in V,

  det [[gamma_v,gamma_w],[R_uv,R_uw]]
   = (gamma_v (K_H)_{uw}-gamma_w (K_H)_{uv})/det(H).                (E2)

Define the aggregate anchored wedge currency

  W_{U,V} = sum_{u in U} sum_{v<w in V}
              (gamma_v (K_H)_{uw}-gamma_w (K_H)_{uv})^2.

Let M be the cross block of S1 with row bank {Y} union U and column bank V. Cauchy-Binet then gives

  e_2(M^T M) >= W_{U,V}/|det H|^2.                                  (E3)

This is source-preserving: every index is an original independent coordinate, no spectral rotation is used, and all other entries of S1 remain present.

Apply the completed square-peel identity from the pinned Fourier route,

  D(Q) <= |a|^{-1/2} H_{1/2}(R1),

where R1 is the full Schur-complement polynomial on (Y,Z). Applying the row-gate-free E2 half-Riesz compiler to M yields

  H_{1/2}(R1) <= 8 e^{1/4} e_2(M^T M)^(-1/8).

Combining with (E3):

  ||p_Q||_infty
   <= 8 e^{1/4} |a|^{-1/2}|det H|^{1/4} W_{U,V}^{-1/8}.             (E4)

This is determinant-FAVORABLE rather than determinant-singular: for fixed anchored wedge currency it improves as det(H)->0. The only way this receiver can collapse at the exact rank-one endpoint is algebraically forced. Indeed when H has rank one with this pivot a != 0, delta=0 and (E1) gives

  K_H=-a gamma gamma^T,

so every K_H row is parallel to gamma and W_{U,V}=0 for every U,V. Thus the remaining near-null branch is precisely an ALIGNMENT branch, not an arbitrary-curvature branch.

Pinned-result application at an actual equation: on the diffuse natural-two-volume row arm for M, Theorem D_k of `FOURIER_ROUTE_REPORT.md` at k=2,q=1 gives

  |phi_{R1}(t)| <= min(1,2 pi sqrt(e) e_2(M^T M)^(-1/4)|t|^-1),

which converts to the displayed half-Riesz bound. Heavy-row failure is handled by the already-completed account02/B06 aggregate transfer, without selecting or inverting an individual 2x2 minor.

Next: prove a quantitative compiler from failure of every W_{U,V} gate to near-rank-one alignment of K_H with gamma gamma^T, then combine that aligned branch with r43/r44's exact-null innovation receiver. The r44 logarithmic counterexample has K_H=0 and therefore lies exactly in this aligned-collapse locus; it does not contradict (E4).
