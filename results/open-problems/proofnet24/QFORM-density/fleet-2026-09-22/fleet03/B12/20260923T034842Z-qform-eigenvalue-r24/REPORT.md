SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B12, 2026-09-23T03:48:42Z.
attacking: show that one additional large eigenvalue can be reduced through at most one original-coordinate scalar Schur step before a quantitative physical-pair exit, while arbitrary dependent outside spectrum is restored with the fleet04/B12 mixed-norm shear compiler.

# fleet03/B12 r24 — one-extra-eigenvalue reduction to the low-pivot/high-leverage core

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Assignment:** Additional eigenvalue control  
**Status:** PROVED_SUPPORTING_REDUCTION / PARTNER_APPLIED / FULL_TARGET_OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN

## 1. Exact scope

Let X=(X_1,...,X_n) have independent real coordinates with probability densities bounded by one. Let A be real symmetric. Fix a scale L>0. This report proves a quantitative reduction for the class

    N_abs(A;L) := #{lambda(A): |lambda|>=L} >= 4.

All smaller and larger eigenvalues, all signs, all multiplicities, and all original-coordinate cross couplings are retained exactly. No spectral rotation is used to claim independence.

The full conjecture, whose hypothesis is only N_abs(A;1)>=3, remains OPEN.

The run consumes the following completed results at their exact scopes.

1. fleet03/B12 r21, threshold-preserving original-coordinate Schur inheritance:
   yspennstate/math-open-problems@dd754a0bfed889fd29c931b7112c8c3285fc83e8,
   proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260923T004313Z-qform-eigenvalue-r21/REPORT.md.
   A scalar physical Schur elimination loses at most one eigenvalue beyond L and does not lower the threshold L.

2. fleet03/B12 r23, one-sided scalar-Schur compiler:
   yspennstate/math-open-problems@4894ced504d555e84620c46029ed08a2af389d9f,
   proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260923T024437Z-qform-eigenvalue-r23/REPORT.md.
   If Q=a(X+m(Y))^2+R(Y) and ||p_R||_infinity<=M, then

       ||p_Q||_infinity <= 2 sqrt(M/|a|).                           (1.1)

3. fleet04/B12, mixed-norm shear compiler:
   yspennstate/math-open-problems@9ce47e2a0f2c8434d901df13a218450c2189d80e,
   proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B12/20260922T192552Z-fleet04-B12-mixed-shear-r1/REPORT.md.
   For a joint density h(u,z), M(h)=int esssup_u h(u,z) dz and arbitrary measurable psi,

       ||p_(U+psi(Z))||_infinity <= M(h).                           (1.2)

   No independence of U and Z is required.

4. fleet03/B04 r24, independently checked spectral-window ridge gate:
   yspennstate/math-open-problems@a11e719b61c4be07fae4e2dcfa4d88d31812d0d9,
   proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/B04-20260923T034739Z-r24/REPORT.md.
   At scale L, if P projects onto eigenspaces |lambda|>=L/256 and max_i P_ii<=1/20, then the form has a continuous C_0 density with

       ||p_Q||_infinity <= 98.9520900203/L < 99/L.                 (1.3)

The determinant-pair estimate used below was checked in r21: for an invertible indefinite physical 2x2 principal block B, D=|det B|, if s_3(A)>=L then

    ||p_Q||_infinity
      <= D^(-1/2) [9.2 + log_+(10000 sqrt(D)/L)].                  (1.4)

## 2. A dependence-safe definite physical-pair bound, with partner application

Let I={i,j} be two ORIGINAL coordinates and let B=A[I,I] be definite and invertible. Put D=|det B|. Condition on every outside original coordinate Z=z. The active quadratic polynomial is

    q_z(x)=x^T B x + ell(z)^T x + c(z).

Completing the square translates x but does not alter its joint density cap: because the two original inputs are independent and each density is at most one, their joint density is at most one. For positive definite B, the Lebesgue area of

    {x: a <= (x-x_0)^T B (x-x_0) <= b}

is at most pi(b-a)/sqrt(D). Reflection gives the same result for negative definite B. Hence for every z,

    ||p_(U|Z=z)||_infinity <= pi/sqrt(D),                          (2.1)

where U contains all terms involving the active pair, including the z-dependent affine terms.

Now define h(u,z)=p_Z(z)p_(U|Z=z)(u). Then

    M(h)=int p_Z(z)||p_(U|Z=z)||_infinity dz <= pi/sqrt(D).

Applying the assigned fleet04/B12 theorem (1.2) to the ACTUAL outside-only remainder psi(Z) gives

    boxed: ||p_(U+psi(Z))||_infinity <= pi/sqrt(D).                (2.2)

Thus arbitrary dependent outside quadratic spectrum of either sign and any magnitude costs exactly zero in the definite-pair branch. This is an actual use of the designated partner result, not an independence/convolution substitution.

## 3. Uniform pair exit at the numerical scale eta=0.17

Set

    eta = 0.17.                                                     (3.1)

Suppose a physical 2x2 principal block B satisfies

    |det B| >= eta^2 L^2.                                          (3.2)

If B is definite, (2.2) gives

    ||p_Q||_infinity <= pi/(eta L)
                     = 18.4799567859.../L < 99/L.                 (3.3)

If B is indefinite, put x=sqrt(D)/L>=eta. From (1.4),

    ||p_Q||_infinity
      <= L^(-1) x^(-1)[9.2+log_+(10000x)].                         (3.4)

For x>=eta>10^(-4), the bracket is 9.2+log(10000x), and the derivative of

    [9.2+log(10000x)]/x

is [1-9.2-log(10000x)]/x^2<0. Hence the worst value occurs at x=eta:

    ||p_Q||_infinity
      <= [9.2+log(1700)]/(0.17 L)
      = 97.8728442944.../L < 99/L.                                (3.5)

Therefore

    boxed:
    any physical pair with |det B| >= 0.0289 L^2
    already gives ||p_Q||_infinity < 99/L.                         (3.6)

All signs and arbitrary outside completion are included.

## 4. Exact pivot-to-pair determinant identity

Let i be an ORIGINAL coordinate with scalar pivot

    a=A_ii !=0,

and let S be the physical Schur complement. For any remaining original coordinate j,

    det A[{i,j},{i,j}]
       = a (A_jj-A_ji^2/a)
       = a S_jj.                                                    (4.1)

This elementary identity is the key new reduction. If every physical pair of A has determinant magnitude below eta^2 L^2 and |a|>=eta L, then for every j

    |S_jj| < eta L.                                                 (4.2)

Thus one quantitative scalar pivot converts a global no-large-pair condition into a complete low-diagonal condition on the Schur remainder.

By threshold-preserving Schur inheritance, if N_abs(A;L)>=4 then

    N_abs(S;L)>=3.                                                  (4.3)

No eigenvalue-size loss occurs and all smaller eigenvalues remain in S.

## 5. Main reduction: `QFORM-FOURPLUS-ONE-PIVOT-REDUCTION-v1`

Let A satisfy N_abs(A;L)>=4. Then at least one of the following holds.

### Exit A: quantitative physical pair

There exists a physical pair with

    |det A[{i,j},{i,j}]| >= 0.0289 L^2.

Then (3.6) proves

    ||p_Q||_infinity <99/L.                                       (5.1)

### Exit B: diffuse spectral-window ridge certificate

If the spectral projection onto |lambda(A)|>=L/256 has every diagonal <=1/20, fleet03/B04 r24 gives

    ||p_Q||_infinity <99/L,                                       (5.2)

with a continuous C_0 density in this direct terminal branch.

### Reduction C: low-pivot residual after at most one scalar Schur step

Assume neither Exit A nor Exit B holds.

If every |A_ii|<0.17L, take S=A: the instance is already in the low-diagonal class.

Otherwise choose i with |a|=|A_ii|>=0.17L and form the physical scalar Schur complement S. Equations (4.2)-(4.3) give simultaneously

    N_abs(S;L)>=3,
    |S_jj|<0.17L for every remaining physical coordinate j.        (5.3)

If S has a physical pair determinant >=0.0289L^2, then the pair exit applied to S gives ||p_R||_infinity<99/L. The one-sided scalar compiler (1.1) then gives

    ||p_Q||_infinity
      <= 2 sqrt((99/L)/(0.17L))
      = 48.2639799924.../L <99/L.                                 (5.4)

If instead S satisfies the B04 spectral-window gate, exactly the same scalar lift gives (5.4), since its terminal constant is <99.

Consequently, if the original form has not already been proved to obey 99/L, it reduces after ZERO OR ONE original-coordinate scalar Schur eliminations to a remainder S satisfying all four conditions

    (i)   N_abs(S;L)>=3;
    (ii)  |S_jj|<0.17L for every physical coordinate j;
    (iii) every physical 2x2 principal determinant has magnitude <0.0289L^2;
    (iv)  the |lambda(S)|>=L/256 spectral projection has some diagonal >1/20.   (5.5)

This is a dependence-safe reduction: no rotated variable is declared independent, and no extra eigenvalue is discarded as noise.

### Interpretation

The class with at least one EXTRA large eigenvalue (four or more at scale L) is therefore no harder than the sharply localized class (5.5), up to one original-coordinate Schur step and the explicit constant 99. The arbitrary extra spectrum has been converted into one of three paid objects: a physical pair, a diffuse ridge packet, or a three-large-eigenvalue low-pivot/high-window-leverage residual.

The statement is intentionally a reduction, not a claim that class (5.5) is already solved.

## 6. General terminal-cap formulation

The same argument is reusable with any terminal theorem. Suppose a residual target at scale L has density cap B/L and choose eta so that

    eta >= 4/B,                                                    (6.1)

and both definite and indefinite physical-pair bounds at determinant eta^2L^2 are <=B/L. If A has N_abs(A;L)>=4 and a scalar pivot |a|>=eta L is taken while all original physical pair determinants are below eta^2L^2, then its Schur complement still has at least three eigenvalues beyond L and has all diagonals below eta L. Whenever that residual hits the terminal theorem, the backward scalar compiler preserves the cap B/L.

Thus a single extra substantial eigenvalue can be eliminated without accumulating a dimension-dependent or chain-length-dependent loss.

## 7. Sanity computation

The bundled checker verifies the constants in (3.3), (3.5), (5.4), the B04 terminal value, and the exact identity

    det A[{i1,i2}] = a1 a2

for sequential scalar Schur pivots on random symmetric matrices. The random check is only a sanity test; equations (4.1) and the monotonicity calculation are the proof.

## 8. Continuity and remaining debt

The B04 ridge terminal proves a continuous C_0 density. The present pair and scalar backward compilers are used only at the essential-L-infinity level, and the fleet04/B12 shear theorem gives continuity only with an additional mixed translation modulus. Therefore this run claims **essential boundedness only** for the reduction exits as assembled here; it does not prove the full continuity objective after arbitrary completion/pivot restoration.

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.** The new first unpaid implication is now the class (5.5): at least three large eigenvalues, uniformly small physical diagonals and 2x2 determinants, but a concentrated L/256 spectral window. This is precisely where grouped-bank / weighted-volume aggregation must replace reciprocal individual-minor payment.

No law-uniform pointwise van-der-Corput decay, arbitrary-joint 3D coarea, normalized worst conditional fiber, or post-rotation independence is used.
