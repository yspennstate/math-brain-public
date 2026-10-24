SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B16, 2026-09-23T15:34:32Z.
attacking: arbitrary same-side curvature in the superdiffuse near-coloop survivor—prove a rank-two cross L^{3/2} compiler that keeps both projected pairs dependent, then identify the exact missing half-power.

# Early mathematical checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.

## First unpaid implication

The latest completed designated partner is account03/B16 r29. After its physical-diagonal and physical-pair exits, the exact-rank-three true-near-coloop survivor has c>63/64, normalized hub-star atoms <1/251, and at least 80 disjoint original-coordinate source banks. Its unpaid step is to carry non-diagonal same-side curvature jointly with those source banks without replacing a bounded two-dimensional product projection by independence or by a worst conditional cap.

The preceding account02/B16 theorem pays a rank-two original-coordinate cross cut when the curved side is diagonal. The first task here is to remove that diagonal assumption as far as possible while keeping the original product provenance.

## New borderline compiler: exact rank-two cross block with arbitrary self blocks

Condition on any outside original-coordinate set. Split the active coordinates as I disjoint union J and assume the physical cross block M=A_IJ has exact rank two,

M=U Sigma V^T,   Sigma=diag(s1,s2),   s1>=s2>0,

with U,V having orthonormal columns. Put

Z=U^T X_I,   W=V^T X_J.

The I and J source banks are independent, but neither coordinate pair Z nor W is declared internally independent. The completed two-dimensional product-projection theorem gives only

||p_Z||_infinity <=2,   ||p_W||_infinity<=2.

For each t form the complex projected densities

a_t(z)=p_Z(z) E[ exp(i t R_I(X_I)) | Z=z ],

b_t(w)=p_W(w) E[ exp(i t R_J(X_J)) | W=w ],

where R_I,R_J contain arbitrary same-side quadratic and affine terms. Then

|a_t|<=p_Z,  |b_t|<=p_W,
||a_t||_1,||b_t||_1<=1,
||a_t||_2,||b_t||_2<=sqrt(2).

The conditional characteristic function is exactly

phi(t)=int int a_t(z)b_t(w) exp(2 i t z^T Sigma w) dz dw.

With the Fourier convention hat a(xi)=int exp(i xi.z)a(z)dz, Cauchy-Schwarz in w and two-dimensional Plancherel give

|phi(t)|
 <= ||b_t||_2 [int |hat a_t(2t Sigma w)|^2 dw]^(1/2)
 <= sqrt(2) * [(2pi)^2 ||a_t||_2^2/(4 t^2 s1 s2)]^(1/2)
 <= 2pi/(|t| sqrt(s1 s2)).

Thus

boxed: |phi(t)| <= min(1, 2pi/(|t| sqrt(s1 s2))),

and consequently

boxed: int |phi(t)|^(3/2) dt <= 12pi/sqrt(s1 s2).

This is dimension-free and permits completely arbitrary same-side quadratic curvature on both source banks. It uses the two-dimensional product marginal exactly as a bounded JOINT density, never as projected independence. The exponent is borderline: rank-two cross interaction gives L^{3/2} control, not L^1.

## Fresh-square closure

If, in addition, a disjoint original-coordinate scalar Y is quadratically separated from the I union J subsystem so that after outside conditioning

Q=Q_0(X_I,X_J)+lambda Y^2+mu Y+const,

with |lambda|>0 and Y independent of the two active banks, then completing the square and the one-dimensional cap-one estimate give

int |E exp(i t(lambda Y^2+mu Y))|^3 dt <= 50pi/|lambda|.

Holder with exponents 3/2 and 3 therefore yields

boxed:
 ||p_Q||_infinity
 <= 900^(1/3) (|lambda| s1 s2)^(-1/3)
 <9.655 (|lambda| s1 s2)^(-1/3).

So arbitrary same-side curvature is not itself fatal: a nondegenerate rank-two cross source pair is only one half-power short, and one genuinely source-separated square closes the density estimate. The remaining exact-rank-three near-coloop problem is to manufacture that missing half-power from OVERLAPPING same-side curvature when no fresh square is source-separated.

## Pinned source actually used

The joint caps ||p_Z||_infinity,||p_W||_infinity<=2 are the same completed two-dimensional product-marginal input used by the ruled theorem in the required pinned package

yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837,
proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}.

This checkpoint is supporting mathematics, not a full proof and not a counterexample.
