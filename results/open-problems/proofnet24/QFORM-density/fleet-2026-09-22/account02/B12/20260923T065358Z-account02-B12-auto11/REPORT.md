SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B12, 2026-09-23T06:53:58Z.
attacking: thresholded original-coordinate cross certificates that survive an arbitrary full-rank dense operator-norm tail while charging arbitrary added eigenvalues only through their physical cross-cut footprint.

# account02/B12 — thresholded cross-footprint hybrid stability

Programme: QFORM-DENSITY-3EIG-20260922
Role: Additional eigenvalue control
Status: PROVED SUPPORTING THEOREM / FULL QFORM OPEN
Execution: WITHOUT_VERIFIED_BRAIN

## 0. First unpaid implication

The bare hypothesis s_3(A)>=1 still does **not** force a physical cut I|J for which either the five-volume reserve or the diffuse cross-energy gate below is uniformly quantitative. The theorem proved here starts after such a baseline cut is identified. Its new content is that this certificate survives (i) an arbitrary full-rank symmetric dense tail of small operator norm and simultaneously (ii) arbitrary signed eigenvalue replacements of unbounded magnitude, provided only that their aggregate ORIGINAL-coordinate cross footprint on the protected cut is small. Nothing here treats a small matrix as a uniformly small quadratic random variable, and no independence after rotation is used.

## 1. Source-pinned completed inputs

1. Required newest-Claude source:
   yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837,
   proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md.
   Its proved D_5 theorem says that for an ORIGINAL-coordinate cross block M=A[I,J], with

       Z_5=e_5(M^T M),

   the full ambient quadratic-plus-affine form, with arbitrary self blocks and outside couplings, satisfies

       ||p_Q||_infinity <= 5 sqrt(2e) Z_5^(-1/10),             (1.1)

   with no marginal condition.

2. Designated partner account03/B12:
   yspennstate/math-open-problems@3ea9c184594344f0d82c72c06646ad2c8291a12a,
   proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T054842Z-qform-eigenvalue-r26/REPORT.md.
   Its proved cross-energy compiler applies to the ACTUAL final cross block M. If

       S=||M||_F^2,  c=||M||_op^2,
       rho=min(max_i ||row_i(M)||_2^2, max_j ||col_j(M)||_2^2),

   and

       S>2c,   S-2c >= (9/2) rho,                              (1.2)

   then the full ambient form has a continuous density and

       ||p_Q||_infinity
       <= (9 sqrt(3)e/2) [S(S-c)(S-2c)/6]^(-1/6).              (1.3)

Both inputs retain arbitrary same-bank curvature and outside dependence in original coordinates.

## 2. New theorem

### QFORM-THRESHOLDED-CROSS-FOOTPRINT-HYBRID-v1

Let A_0=A_0^T and choose disjoint sets of ORIGINAL coordinates I,J. Put

    M_0=A_0[I,J].

Let

    A=A_0+S+T,

where S=S^T is an arbitrary spectral modification and T=T^T is an arbitrary full-rank dense perturbation satisfying

    ||T||_op <= delta.

No rank, sign, or norm bound is imposed on S. Charge it only through the protected physical cut:

    eta=||S[I,J]||_op,
    epsilon=delta+eta.                                         (2.1)

Let s_1>=s_2>=... be the singular values of M_0 and define the thresholded singular reserves

    a_j=(s_j-epsilon)_+,
    R=sum_j a_j^2.                                              (2.2)

Also define

    C=(s_1+epsilon)^2,                                         (2.3)
    r_0=max_i ||row_i(M_0)||_2^2,
    c_0=max_j ||col_j(M_0)||_2^2,
    rho_* = min{(sqrt(r_0)+epsilon)^2,
                (sqrt(c_0)+epsilon)^2}.                        (2.4)

Then either of the following final-matrix certificates is sufficient.

**Five-volume branch.** If a_5>0, then

    boxed:
    ||p_Q||_infinity
      <= 5 sqrt(2e) (a_1 a_2 a_3 a_4 a_5)^(-1/5).              (2.5)

**Collective cross-energy branch.** If

    R>2C,
    R-2C >= (9/2) rho_*,                                       (2.6)

then

    boxed:
    ||p_Q||_infinity
      <= (9 sqrt(3)e/2)
         [R(R-C)(R-2C)/6]^(-1/6).                              (2.7)

The second branch gives a continuous density by the partner theorem. The first branch inherits the Fourier inversion regularity of D_5; essential boundedness is all that is needed for the main target.

### Proof

The actual final cross block is

    M=A[I,J]=M_0+E,
    E=S[I,J]+T[I,J].                                           (2.8)

Rectangular compression cannot increase operator norm, so

    ||E||_op <= eta+delta=epsilon.                              (2.9)

By Weyl's singular-value inequality,

    s_j(M) >= (s_j(M_0)-epsilon)_+=a_j                         (2.10)

for every j. Hence, if a_5>0,

    e_5(M^T M)
      >= product_{j=1}^5 s_j(M)^2
      >= product_{j=1}^5 a_j^2.                               (2.11)

Substitution into the completed e5f D_5 inequality (1.1) proves (2.5). This is an equation-level application of the required newest-Claude source.

For the collective branch, (2.10) gives

    ||M||_F^2=sum_j s_j(M)^2 >= R.                             (2.12)

The opposite Weyl inequality gives

    ||M||_op <= s_1(M_0)+epsilon,

so the actual c satisfies c<=C. Every row of E and every column of E has Euclidean norm at most ||E||_op. Therefore

    max_i ||row_i(M)||_2 <= sqrt(r_0)+epsilon,
    max_j ||col_j(M)||_2 <= sqrt(c_0)+epsilon,                  (2.13)

and the actual partner quantity rho is at most rho_*.

Under (2.6), equations (2.12)-(2.13) imply

    S_actual-2c_actual
      >= R-2C
      >= (9/2)rho_*
      >= (9/2)rho_actual,

and S_actual>2c_actual. Thus the completed account03/B12 cross-energy theorem applies to the actual final matrix. Moreover, since R>2C,

    S_actual >= R,
    S_actual-c_actual >= R-C,
    S_actual-2c_actual >= R-2C,

with all three factors positive. Substituting these deterministic lower bounds in (1.3) proves (2.7). QED.

## 3. Literal arbitrary eigenvalue replacements

Suppose now that v_1,...,v_m are orthonormal eigenvectors of A_0, with eigenvalues lambda_k, and

    S=sum_k tau_k v_k v_k^T.                                  (3.1)

Then A_0+S literally replaces lambda_k by lambda_k+tau_k. The coefficients tau_k may be arbitrarily small or large and of either sign. The theorem never charges their magnitudes separately; it charges only

    eta = || sum_k tau_k (v_k)_I (v_k)_J^T ||_op.              (3.2)

Thus huge eigenvalue changes are free whenever their aggregate physical overlap with the protected cut is small. This is a matrix-level statement in the original independent coordinates, not a rotated convolution argument.

## 4. Exact target-class family with unbounded signed eigenvalue replacement and a dense tail

Take 17 original coordinates, with

    I={1,...,8},  J={9,...,16},

and define

              [ 0      2 I_8   0 ]
    A_0   =   [ 2 I_8  0       0 ].                            (4.1)
              [ 0      0       2 ]

Its spectrum is +2 with multiplicity 9 and -2 with multiplicity 8. Let

    w=(e_1+e_9)/sqrt(2).

Both w and e_17 are +2 eigenvectors. For an arbitrary real tau, set

    alpha_tau^2 = 1/[20(1+|tau|)],
    v_tau = sqrt(1-alpha_tau^2) e_17 + alpha_tau w.             (4.2)

Then v_tau is a unit +2 eigenvector of A_0, and

    A_tau^0=A_0+tau v_tau v_tau^T                              (4.3)

literally replaces one eigenvalue +2 by 2+tau, leaving eight other +2 eigenvalues and all eight -2 eigenvalues unchanged. Hence tau may tend to +infinity or -infinity without threatening the three-large-eigenvalue hypothesis.

The cross footprint is nonzero but uniformly tiny:

    ||tau v_tau[I] v_tau[J]^T||_op
       = |tau| alpha_tau^2/2
       = |tau|/[40(1+|tau|)]
       <= 1/40.                                                (4.4)

Now add **any** symmetric dense T with

    ||T||_op <= 1/40.                                         (4.5)

Thus epsilon<=1/20. Since A_tau^0 has at least sixteen singular values exactly 2,

    s_3(A_tau^0+T) >= 2-1/40 = 79/40 >1,                      (4.6)

so every final matrix is in the exact QFORM target class.

For the protected cross block M_0=2I_8,

    a_j=2-1/20=39/20,  j=1,...,8.                             (4.7)

The required e5f D_5 branch already gives

    ||p_Q||_infinity
      <= 5 sqrt(2e)/(39/20)
      = 5.978574311787498... .                                (4.8)

The partner cross-energy branch is stronger here. We have

    R=8(39/20)^2=30.42,
    C=rho_*=(41/20)^2=4.2025,                                 (4.9)

and

    R-2C-(9/2)rho_* = 2483/800 = 3.10375 >0.                 (4.10)

Therefore (2.7) yields

    boxed:
    ||p_Q||_infinity
      <= 5.602062744709504...                                 (4.11)

uniformly for every tau in R, every independent product source with coordinate densities <=1, and every arbitrary-rank symmetric dense T obeying (4.5). The eigenvalue replacement is unbounded, signed, and has a genuinely nonzero physical cross footprint.

## 5. Why this is not the forbidden small-random-perturbation shortcut

The only uses of epsilon are the deterministic singular-value and row/column-norm inequalities (2.9)-(2.13). No estimate of |X^T T X| is made. Indeed for T=delta e_1 e_1^T and X_1 uniform on [R,R+1], an admissible cap-one law,

    X^T T X = delta X_1^2 >= delta R^2

almost surely. Small ||T||_op therefore gives no uniform probabilistic smallness on the allowed unbounded inputs. The theorem instead verifies a certificate directly on the actual final matrix.

## 6. Remaining bridge to the full target

The full QFORM conjecture remains OPEN. The first unpaid structural step is to force from s_3(A)>=1 at least one of:

* a physical cut carrying five threshold-robust singular directions;
* a cut satisfying the thresholded collective cross-energy gate (2.6);
* or an already-paid localized physical core, hub, grouped-bank, ridge, or Schur branch.

Known correction families prohibit replacing this by the assertion of one uniformly good physical minor or a universally rank-three cross cut. This report supplies stability after a viable cut exists; it does not manufacture that cut from the bare spectral hypothesis.

## 7. Source/correction boundary

Control was resolved from fresh brain main at the beginning of the invocation; OWNER CONTROL revision 2026-09-22.15 remained active. The live correction inbox was re-read immediately before publication at a later fresh main head. The proof uses none of the refuted interfaces: no pointwise law-uniform stationary phase, no arbitrary-joint coarea, no worst conditional projection-density moment, no uniformly good single minor, and no post-rotation independence.
