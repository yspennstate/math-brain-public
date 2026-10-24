SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-23T03:17:17Z.
attacking: spectral-footprint leverage compiler for arbitrary-magnitude added eigenvalues of either sign, using the completed account02/B12 shielded rank-reserve theorem.

# account01/B12 r23 — spectral-footprint leverage compiler

## Status

PROVED_SUPPORTING_STABILITY / PARTNER_APPLIED / FULL_QFORM_OPEN / WITHOUT_VERIFIED_BRAIN.

The full target remains open: independent real inputs with densities at most one, arbitrary dimension, and a real symmetric matrix with at least three eigenvalues of absolute value at least one. This report proves a quantitative additional-eigenvalue stability theorem in a source-valid protected-cross-cut regime. It does not prove the bare three-eigenvalue hypothesis forces that regime.

Continuity is not claimed here; the result below gives essential boundedness through the completed partner theorem.

## Fresh controls and corrections

Programme: QFORM-DENSITY-3EIG-20260922, programme revision 2026-09-22.5, OWNER CONTROL revision 2026-09-22.15. Final pre-write brain main observed at 44eed49efa089550280980d59897af6afffa8f53. Live correction inbox blob remained c7000cf3822ae4935a2faf43b89ac92ea65ac0fe.

Used corrections: no post-rotation independence; no law-uniform pointwise quadratic-phase decay; no arbitrary-joint coarea bound; no normalized worst conditional-fiber cap; no one-good-minor implication. The proof works entirely with original-coordinate cross blocks and exact spectral-footprint identities.

## Completed assigned-partner theorem actually used

Latest account02/B12 handoff read before this report:

- brain handoff: scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/account02/B12/20260923T025914Z-account02-B12-qform-r24.md;
- canonical mathematics: yspennstate/math-open-problems@0d0b91b9c5b5ca41fbdc3b910bde3c3759195eb3, proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260923T025914Z-account02-B12-qform-r24/REPORT.md.

Its theorem QFORM-SHIELDED-RANK-RESERVE-TAIL-STABILITY-v1 says the following. For an ORIGINAL-coordinate cut with cross block

M = M0 + L + E,

let P be a row-side orthogonal projection satisfying max_i P_ii <= 1/2, rank(L) <= r, (I-P)L=0, and ||E||op <= delta. Define

a1 = (s_{r+1}(M0)-delta)_+,
a2 = (s_{r+2}(M0)-delta)_+,
B^2 = sum_{k>=r+3} (s_k(M0)-delta)_+^2,
epsilon0 = ||(I-P)M0||op.

If a2,B>0 and epsilon0+delta <= B/15, then the final quadratic form, with arbitrary self blocks and all other allowed couplings, satisfies

||p_Q||_infinity <= (9 sqrt(3) e / 2) (a1 a2 B)^(-1/3).                 (P)

The low-rank term L can have completely arbitrary magnitude and sign; only its rank and shielded row footprint are charged. This report translates the abstract projection P into a direct criterion on the eigenvectors of an added spectral cloud.

## 1. Exact spectral-footprint identity

Let I,J be disjoint ORIGINAL-coordinate sets defining a protected cross cut. Let

S = V Theta V^T,

where V is n x r with orthonormal columns and Theta is any real symmetric r x r matrix. In the spectral-addition application Theta is diagonal, but diagonality is not needed for the cross-block identity. The eigenvalues of Theta may have arbitrary signs and arbitrary magnitudes.

Write V_I and V_J for the row restrictions. The I-by-J cross block of S is exactly

L = V_I Theta V_J^T.                                               (1.1)

Let P be the orthogonal projection in R^I onto range(V_I). Then

rank(L) <= r,
(I-P)L = 0.                                                        (1.2)

These identities are magnitude-free: neither statement contains ||Theta||.

If V_I has full column rank, define the restricted Gram matrix

G_I = V_I^T V_I > 0.

Then

P = V_I G_I^{-1} V_I^T,                                          (1.3)

and for each original coordinate i in I, writing v_i^T for row i of V,

P_ii = v_i^T G_I^{-1} v_i.                                       (1.4)

Thus the exact row-leverage condition required by the partner theorem is

max_{i in I} v_i^T G_I^{-1} v_i <= 1/2.                          (1.5)

If V_I is rank deficient, the same statement holds with P the projection onto range(V_I), equivalently with the Moore-Penrose inverse in (1.3); the effective rank is then smaller than r and only helps.

### Proof

Equation (1.1) is block restriction of V Theta V^T. Every column of L belongs to range(V_I), proving (1.2). For full-column-rank V_I, (1.3) is the standard orthogonal-projection formula, and taking its diagonal gives (1.4). QED.

## 2. Spectral-footprint leverage compiler

### Theorem 2.1 — QFORM-SPECTRAL-FOOTPRINT-LEVERAGE-COMPILER-v1

Let the cross block of a baseline symmetric quadratic form across an original-coordinate cut I|J be M0. Add an arbitrary spectral cloud S=V Theta V^T of rank at most r and an arbitrary symmetric dense perturbation T with ||T||op <= delta. Let E=T[I,J]. Let P be the projection onto range(V_I).

Assume

max_i P_ii <= 1/2.                                                (2.1)

Define

a1=(s_{r+1}(M0)-delta)_+,
a2=(s_{r+2}(M0)-delta)_+,
B^2=sum_{k>=r+3}(s_k(M0)-delta)_+^2,
epsilon0=||(I-P)M0||op.                                         (2.2)

If a2,B>0 and

epsilon0+delta <= B/15,                                         (2.3)

then the full final quadratic form satisfies

boxed( ||p_Q||_infinity <= (9 sqrt(3)e/2)(a1 a2 B)^(-1/3) ).     (2.4)

The bound is completely independent of ||Theta||op. Hence all eigenvalues represented by Theta may be arbitrarily small, arbitrarily large, positive, negative, or sign-changing.

### Proof

The cross block of the full perturbation is L+E with L=V_I Theta V_J^T. By (1.2), rank L<=r and (I-P)L=0. Since E is a submatrix of T,

||E||op <= ||T||op <= delta.                                    (2.5)

Condition (2.1) is exactly the partner theorem's leverage hypothesis. The quantities in (2.2) and condition (2.3) are exactly the partner theorem's remaining hypotheses. Applying account02/B12 r24 theorem (P) gives (2.4) directly. QED.

This is a genuine use of the assigned partner theorem at the final density inequality, not a citation-only dependency.

## 3. A simpler eigenvector criterion

The exact leverage in (1.5) can be bounded without forming P explicitly.

### Corollary 3.1

Suppose

G_I = V_I^T V_I >= gamma I_r                                 (3.1)

for some gamma>0, and the global row energies on I satisfy

max_{i in I} ||v_i||_2^2 <= gamma/2.                            (3.2)

Then max_i P_ii<=1/2, so Theorem 2.1 applies.

### Proof

From G_I^{-1} <= gamma^{-1} I,

P_ii = v_i^T G_I^{-1} v_i <= ||v_i||^2/gamma <= 1/2.            (3.3)

QED.

Thus a spectral cloud whose eigenspace remains quantitatively spread after restriction to I is free in amplitude and sign. The relevant quantity is not the size of its eigenvalues but the coordinate leverage of its physical footprint.

An incoherence form is immediate: if max_i ||v_i||^2 <= mu r/n and G_I>=gamma I, then (2.1) follows whenever mu r/n <= gamma/2.

## 4. Exact stress family with arbitrary eigenvalue changes

This section applies the theorem to an explicit family and obtains a numerical density inequality.

Take r=100 and split 800 original coordinates into I and J of size 400 each. Let

M0 = 2 I_400,
A0 = [ 0   M0 ; M0   0 ].                                      (4.1)

Hence A0 has eigenvalues +2 and -2, each with multiplicity 400.

Let U=I_100 and define V in R^(800 x 100) by eight identical 100x100 blocks,

V = (1/sqrt(8)) [U;U;U;U;U;U;U;U].                             (4.2)

The columns of V are orthonormal. Let I consist of the first four blocks and J the last four. Then

V_I^T V_I = (1/2) I_100,                                       (4.3)

and every row of V_I has squared norm 1/8. Therefore

P_ii = (1/8)/(1/2) = 1/4 < 1/2.                                (4.4)

Moreover A0 V = 2V, so the columns of V are actual +2 eigenvectors of A0. For arbitrary real numbers theta_1,...,theta_100, let

Theta=diag(theta_1,...,theta_100),
A=A0+V Theta V^T+T,                                             (4.5)

where T is any symmetric matrix with ||T||op<=0.01.

Before T is added, (4.5) literally changes 100 eigenvalues 2 to 2+theta_j; every theta_j is unrestricted and can be huge positive, huge negative, small, or chosen to cross zero. The remaining 300 positive eigenvalues +2 and all 400 negative eigenvalues -2 are untouched. After T, Weyl still leaves at least 700 eigenvalues of magnitude at least 1.99, so this is safely inside the target class for every choice of the theta_j.

For the I|J cross block, r=100, delta=0.01, and every singular value of M0 equals 2. Hence

a1=a2=1.99,
B=1.99 sqrt(298)=34.3527262382...,
epsilon0=||(I-P)2I_400||op=2.                                  (4.6)

The gate is satisfied because

epsilon0+delta=2.01 < B/15=2.2901817492....                    (4.7)

Applying the account02/B12 r24 inequality through Theorem 2.1 gives the actual bound

||p_{X^T A X}||_infinity
 <= (9 sqrt(3)e/2)[1.99^2*(1.99 sqrt(298))]^(-1/3)
 = 4.1195062803....                                             (4.8)

Therefore

boxed( ||p_{X^T A X}||_infinity < 4.120 )                       (4.9)

uniformly over all 100 arbitrary spectral parameters theta_j and the entire dense symmetric operator-norm-0.01 tail T.

This is a concrete dependence-safe additional-eigenvalue theorem: one hundred eigenvalues are changed by arbitrary amounts and signs, yet the density constant does not depend on their magnitudes.

## 5. What this pays and what it does not

Paid here:

1. The abstract shield projection in account02/B12 r24 is converted into a direct exact formula in terms of the physical restrictions of the added eigenspace.
2. Arbitrarily many added eigenvalues up to a rank budget r can have arbitrary signs and magnitudes when their I-side footprint has leverage <=1/2 and the baseline cross block has the partner theorem's r-direction reserve.
3. An arbitrary-rank dense tail is simultaneously allowed through one operator-norm charge delta.
4. The explicit family (4.5) gives a uniform density bound <4.120 while 100 genuine eigenvalues vary arbitrarily.

Still unpaid for the full conjecture:

The bare hypothesis s_3(A)>=1 supplies only three globally large singular/eigen directions and does not automatically provide the r+3 cross-singular reserve required when an arbitrary rank-r spectral cloud is spent by rank. Nor does it automatically produce a protected cut with the leverage and leakage conditions (2.1)-(2.3). The remaining structural task is to show that a target matrix either yields such a shielded diffuse-footprint cut, or exits through one of the already-paid localized physical-pair/triple, hub, ridge, grouped-bank, or scalar-Schur branches. In the high-leverage alternative, one should exploit the concentrated original-coordinate footprint rather than rotate it away.

This report does not claim a full solution and does not claim continuity.

## Integrity

No Gaussianity, log-concavity, moment, compact-support, connected-support, diagonal-basis independence, pointwise van-der-Corput decay, arbitrary-joint coarea, or Monte Carlo inference is used. All spectral rotations appear only in deterministic matrix identities; probabilistic conditioning remains in original coordinates through the source partner theorem.
