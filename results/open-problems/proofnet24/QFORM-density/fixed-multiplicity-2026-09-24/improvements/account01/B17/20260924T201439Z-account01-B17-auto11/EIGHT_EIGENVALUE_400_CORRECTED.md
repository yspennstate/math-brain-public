# account01/B17 r11 — corrected multiplicity-eight, constant-400 replacement proof

Run: 20260924T201439Z-account01-B17-auto11
Status: NEW COMPLETE MATHEMATICAL CANDIDATE / B17 PASS.
This plain-text version supersedes only this run's earlier EIGHT_EIGENVALUE_400.md,
whose mathematical backslashes were mangled by transport serialization. The earlier
file is retained as immutable history. No mathematical assertion is changed.

## Theorem QFORM-FIXED-MULTIPLICITY-8-400-B17-v1

Let X=(X_1,...,X_n) have independent real coordinates with probability
densities bounded by K. Let A=A^T, b in R^n, c in R, and suppose

    s_8(A) >= s > 0.

Then Q = X^T A X + b^T X + c has an essentially bounded density and

    ||p_Q||_infinity <= 400 K^2 / s.

No moment, support, smoothness, Gaussianity, log-concavity, exact-rank,
diagonal-basis or leverage assumption is imposed. Global continuity is not
claimed.

The proof combines the source-pinned nine/400 package at
eeb752c8943536541b34b42b8bf48e924f4d3d2f with the robust two-anchor
collar mechanism separately reconstructed in account01/B13
(EIGHT_EIGENVALUE_REPLACEMENT.md, blob
8f792f8f80d70fd1eda26dfdabd855b9a6235e29).

## 1. Normalize and inherit the paid pivot branches

Scale to K=s=1. Use exactly the nine-paper parameters

    d = 3/40,   p = 1/400,   h = 2/25,   kappa = h^2 = 4/625.

A physical pivot is either |A_ii| >= d or a principal two-coordinate
determinant of modulus at least p.

The nine-paper pivot proofs require less spectral multiplicity than eight:

- scalar pivot: its Schur complement retains at least seven unit-scale
  eigenvalue moduli; Proposition 7.3 there needs only five. The three scalar
  branches are <280, <320 and <383;
- definite pair pivot: <80;
- indefinite pair pivot: the Schur complement retains at least six unit-scale
  directions; the logarithmic receiver needs only one. Its bound is <392.5.

Thus every pivot state is below 400 already under s_8(A)>=1.

Hence assume no pivot. Then

    |A_ii| < 3/40,
    |A_ij| < 1/11   for i != j.                                  (1.1)

## 2. The ordinary third volume either pays immediately or is small

Let V_r be the ordered disjoint minor volume from the nine paper. Since
s_8>=1 implies s_5>=1, its audited order-two spectral-to-volume proposition
gives

    V_2 >= kappa^2.                                               (2.1)

If V_3 >= kappa^3, a fair physical-coordinate cut has

    Z_3 >= kappa^3/64.

The marginal-free order-three receiver gives

    ||p_Q||_infinity <= C_3 Z_3^(-1/6) <= 25 C_3 < 375.           (2.2)

It remains to treat

    V_3 < kappa^3,    V_3/V_2 < kappa.                            (2.3)

## 3. A good two-seed forces two robust physical anchors

Sample every invertible disjoint two-seed B=A[S,T] with probability
det(B)^2/V_2, and use the audited completion

    A = D + R + E,

where D is diagonal and zero on S union T, E is zero-diagonal,

    rank(R) <= 6,    rank(R[L,L]) <= 2,

and

    E_seed ||E||_F^2 <= 9 V_3/V_2 < 9 kappa.                     (3.1)

Call a seed good when

    ||E||_F^2 <= 18 kappa.

By Markov and the strict inequality in (3.1), good seeds carry more than
half of V_2. For a good seed put

    epsilon = ||E||_F <= sqrt(18 kappa)
            = 6 sqrt(2)/25 < 17/50.                              (3.2)

Since s_8(A)>=1,

    s_8(D+R) = s_8(A-E) >= 1-epsilon.

Because rank(R)<=6,

    s_2(D) >= 1-epsilon.

Thus two coordinates H={h_1,h_2} in the seed complement L satisfy

    |D_hh| >= 1-epsilon.                                         (3.3)

Write P=A[:,T] B^(-1) A[S,:], so R[L,L]=P[L,L]. For h in H,

    |P_hh| >= 1-epsilon-d > 117/200,

while for distinct h,h' in H,

    |P_hh'| <= |A_hh'|+|E_hh'|
             < 1/11 + 17/50 = 237/550.

Therefore

    |det P[H,H]|
      > (117/200)^2 - (237/550)^2
      = 151533/968000
      > 3/20.                                                     (3.4)

The exact interpolation identity

    P[H,H] = A[H,T] B^(-1) A[S,H]

now yields

    |det A[S,H] det A[H,T]| > (3/20) |det B|.                    (3.5)

## 4. Aggregate collar mass extracts one robust literal two-anchor block

For every two-set H define

    D_H = sum_{U subset H^c, |U|=2} det A[H,U]^2.                 (4.1)

By definition of ordered V_2,

    sum_H D_H = V_2.                                             (4.2)

Assign each good seed one pair H supplied by Section 3 and let w_H be the
sum of det(B)^2 over good seeds assigned to H. Since good mass is >V_2/2,
some H_* satisfies

    w_{H_*} > D_{H_*}/2.                                         (4.3)

Squaring (3.5), summing over seeds assigned to H_*, and then dropping
disjointness in a nonnegative double sum gives

    (9/400) w_{H_*}
       < sum_assigned det A[S,H_*]^2 det A[H_*,T]^2
       <= D_{H_*}^2.

Together with (4.3),

    g := D_{H_*} > 9/800.                                        (4.4)

Let H=H_*, L=H^c, and C=A[H,L]. Cauchy-Binet gives

    g = det(C C^T).                                               (4.5)

## 5. Exact leave-one-column identity and leverage split

Put

    Q_C = C^T (C C^T)^(-1) C,    P = I-Q_C,
    q_i = (Q_C)_ii,               p_i = 1-q_i.

Since Q_C has rank two,

    sum_i q_i = 2.                                                (5.1)

Write A in block form [[B,C],[C^T,D]]. Let d_i be row i of the L by L
block D and put r_i=d_i P. Define

    W_i = sum_{T subset L\{i}, |T|=3} det A[H union {i},T]^2,
    W_dis = sum_i W_i.                                           (5.2)

The leave-one-column Cauchy-Binet identity is

    W_i = g ( p_i ||r_i||_2^2 - r_ii^2 ).                        (5.3)

Proof of (5.3): the total squared 3-minor sum of the three rows (C;d_i)
is g ||r_i||^2. The leverage of column i in their row space is
q_i+r_ii^2/||r_i||^2; deleting all minors using column i leaves (5.3).
The zero-residual case follows directly.

Set

    J = {i : q_i > 2/3},    U=L\J.

For i in U, p_i>=1/3, define

    lambda_i = r_ii/p_i,
    row_i(E) = (d_i-lambda_i e_i^T) P.

For i in J put lambda_i=0 and row_i(E)=0. Then E_ii=0 and (5.3) gives

    ||E||_F^2 <= (3/g) W_dis.                                    (5.4)

## 6. There is at most one high-leverage coordinate

For every pair {a,b} in L put

    w_ab = det(C_{a,b})^2/g.

Cauchy-Binet gives sum_{a<b} w_ab=1, and the determinantal one-point
marginals are

    q_i = sum_{b != i} w_ib.                                     (6.1)

If distinct i,j both had q_i,q_j>2/3, then

    w_ij >= q_i+q_j-1 > 1/3

and hence

    det(C_{i,j})^2 > g/3 > 3/800.                                (6.2)

But all four entries of this literal 2 by 2 cross minor are off-diagonal
entries of A, so (1.1) gives

    |det C_{i,j}| < 2/121,
    det(C_{i,j})^2 < 4/14641 < 3/800,

a contradiction. Therefore

    |J| <= 1.                                                     (6.3)

## 7. A dimension-free disjoint incident third volume is forced

Assume for contradiction

    W_dis <= g/50.                                                (7.1)

Then by (5.4),

    ||E||_F^2 <= 3/50,
    ||E|| <= ||E||_F < 49/200,                                   (7.2)

because 3/50 < (49/200)^2.

Let D_0 be diagonal with entries lambda_i on U and zero on H union J, and
set

    R = A - D_0 - (0_H direct_sum E).

Every row outside J lies in the direct sum of the two physical H-coordinate
directions and the two-dimensional row space of C. Each row in J contributes
at most one extra row direction. Hence

    rank(R) <= 4+|J| <= 5.                                       (7.3)

After restriction to U by U, every row lies in the restricted row space of
C, so

    rank(R[U,U]) <= 2.                                           (7.4)

By (7.2) and s_8(A)>=1,

    s_8(D_0+R) >= 3/4.

Using (7.3),

    s_{4-|J|}(D_0) >= 3/4.

Since |J|<=1, at least three coordinates I subset U satisfy
|lambda_i|>=3/4. For i in I,

    |R_ii| >= 3/4-d = 27/40.

For distinct i,j in I,

    |R_ij| < 1/11 + 49/200 = 739/2200.

Thus each row of R[I,I] has off-diagonal absolute sum less than

    2*(739/2200) = 739/1100 < 27/40,

with exact margin 7/2200. Strict diagonal dominance makes R[I,I]
invertible, contradicting (7.4). Hence

    W_dis > g/50 > 9/40000.                                      (7.5)

## 8. Pay the disjoint incident volume by the audited grouped compiler

Randomly partition L=I union J'. Each packet counted by W_dis contains four
distinct L-coordinates (one distinguished row coordinate and three column
coordinates), so with probability 1/16 it lands with the row in I and all
three columns in J'. Therefore some cut has

    W(I,J') >= W_dis/16.                                         (8.1)

Retain the two literal coordinates in H as hubs. Let S^2 be the two-row
Gram determinant of their crossing block to J'. Project each residual I-row
orthogonally off those two hub rows and let

    Z = sum_i ||c_i||^2.

Cauchy-Binet gives exactly

    W(I,J') = S^2 Z.                                             (8.2)

If all residual row marginals are at most 1/2, the audited grouped lemma
with k=2, ell=1 gives

    |phi_Q(t)| <= min(1,
       pi^(3/2) 2^(1/4) e W(I,J')^(-1/4) |t|^(-3/2)),

hence

    ||p_Q||_infinity
       <= 3*2^(1/6)*e^(2/3)*W(I,J')^(-1/6).                      (8.3)

If one residual row has marginal >1/2, retain that literal original
coordinate as a third hub. The terminal three-hub lemma has Gram determinant
>W(I,J')/2 and gives a smaller coefficient than the right side of (8.3)
after the factor 2^(1/6).

Combining both branches with (8.1),

    ||p_Q||_infinity
       <= 3*2^(5/6)*e^(2/3)*W_dis^(-1/6).                        (8.4)

Using (7.5), e<3, 2^(5/6)<2 and (40000/9)^(1/6)<5,

    ||p_Q||_infinity < 90                                        (8.5)

in the terminal no-pivot branch.

## 9. Assemble the theorem

Every normalized s_8(A)>=1 state is in one of the following branches:

1. scalar pivot: <383;
2. definite pair pivot: <80;
3. indefinite pair pivot: <392.5;
4. no pivot and V_3>=kappa^3: <375;
5. no pivot and V_3<kappa^3: <90.

Therefore ||p_Q||_infinity <400.

For general K,s, put Y=KX and apply the normalized theorem to A/s. Since

    Q=(s/K^2) Q_tilde,

density scaling gives

    ||p_Q||_infinity <= 400 K^2/s.

All conditioning and hub promotion is in original independent coordinates.
The projections P,Q_C are deterministic coefficient-space algebra only. No
post-rotation independence is invoked. Essential boundedness is proved;
global continuity is not asserted.

## 10. Audit/review status and lower frontier

I independently re-derived every step above, including two-anchor extraction,
the leave-one-column identity, the high-leverage exclusion and the rank
contradiction. The proof is compatible with all QFORM correction events read
in this run.

The B13 report cited at the start is a genuinely separate complete
reconstruction of the multiplicity-eight mechanism, with different pivot
thresholds and constant 6010. This B17 proof supplies a second end-to-end
reconstruction of the structural chain and sharpens the constant. This is not
formal proof-assistant verification or journal peer review.

Multiplicity seven remains open in this route. At s_7, the rank-six two-seed
completion forces only one large completed diagonal coordinate, so the
two-anchor conversion above fails. The remaining object is a genuine
one-shared-coordinate overlap packet; the current grouped q=3 compiler cannot
be applied by pretending that shared coordinate occurs in two independent
banks.
