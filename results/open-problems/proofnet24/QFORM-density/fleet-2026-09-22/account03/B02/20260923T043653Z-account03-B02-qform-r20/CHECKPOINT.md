SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T04:36:53Z.
attacking: aggregate ALL physical three-volume packets before reciprocal-minor payment by lifting the disjoint-row-basis entropy construction to the full row/column minor law; then classify the small-disjointness failure as three-row volume concentration.

# Early substantive checkpoint — global three-volume disjointness

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.

Let I,J be disjoint original-coordinate banks, M=A[I,J], and

Z=E_3(M):=e_3(M^T M)=sum_{|R|=|T|=3} det(M[R,T])^2>0.

Put

w_{R,T}=det(M[R,T])^2/Z,
mu_R=sum_T w_{R,T},

delta=P(R cap S=empty),  R,S iid~mu.

The current calculation gives the following candidate theorem, with a complete proof to be written in REPORT.md.

**QFORM-GLOBAL-VOLUME-DISJOINT-ENTROPY-L1-v1.** If delta>0, then for arbitrary within-bank quadratic phases, arbitrary outside couplings/spectrum, affine terms, and independent cap-one inputs,

|phi_Q(t)| <= min{1, e^(3/2) pi^(3/2) delta^(-1/4) Z^(-1/4)|t|^(-3/2)},

hence

||p_Q||_infinity <= 3 e delta^(-1/6) Z^(-1/6).

The density on this branch is continuous and vanishes at infinity.

Proof mechanism: condition an iid pair (R,S)~mu x mu on R cap S=empty. The first marginal nu has every row-inclusion marginal <=1/2. Lift nu to the full minor law by preserving the original conditional column law w(T|R): pi_{R,T}=nu_R w(T|R). Then

D(pi||w)=D(nu||mu)<=log(1/delta)

by data processing from the conditioned pair. The row marginal gate required by the determinant-weighted Brascamp--Lieb/Hausdorff--Young theorem is therefore retained exactly; no column triple is selected before inversion. Weighted AM--GM contributes exp(D/2) to the squared BL estimate, hence exp(D/4) to |phi| and exp(D/6) after t-integration.

There is also an exact structural complement. For a fixed row triple R,

P(S cap R=empty | R)=E_3(M[R^c,J])/Z.

Therefore

delta=E_R[E_3(M[R^c,J])/Z],

so some physical row triple R satisfies

E_3(M[R^c,J]) <= delta E_3(M).

For exact rank(M)=3, writing M=U Sigma V^T gives

E_3(M[R^c,J])/E_3(M)=det(U_{R^c}^T U_{R^c}).

Thus some unit v in R^3 obeys

||U_{R^c}v||_2^2 <= delta^(1/3),

so at least 1-delta^(1/3) of that singular-frame direction is carried by only three physical rows. This turns small delta into a quantitative localized-direction certificate rather than a failed Fourier estimate.

The identities were checked on 30 seeded random rectangular matrices: max relative Cauchy--Binet E3 error 2.68e-15; max |delta_double_sum-delta_residual_average| 3.61e-16. Exact-rank-three residual determinant ratios agreed to 1.78e-15.

Sources actually being extended/applied:
- math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba, interactive/20260923T002323Z-volume-stability/REPORT.md, q=1 fractional-volume/BL mechanism with row gates retained;
- math-open-problems@32c257209b588141fb60af698f478f1d0ad20b8a, account02/B07 QFORM-PLUCKER-ENTROPY-BL-v1, especially the conditioned-disjoint-basis entropy construction;
- previous account03/B02 fixed-three-column packet at f445f3dd7e2b845f96ac58cc4bd96f12ec7a839c.

Designated partner account04/B02 will be applied at an actual hybrid inequality in the full report; its completed zero-diagonal-triple L2 Fourier estimate is at math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7.
