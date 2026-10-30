# QFORM coordinate-minor selection: finite heavy-core determinant factorization

Run: `a01-b07-20260922T170700Z-qform-r13`  
Worker: fleet01/B07  
Status: **ESSENTIAL_STEP_APPLIED / FULL TARGET OPEN**  
Execution label: `WITHOUT_VERIFIED_BRAIN`

## 1. Target and conditional end-to-end argument

The target remains: for independent real coordinates with densities bounded by one and every real symmetric matrix A having at least three eigenvalues of modulus at least one, prove a universal L-infinity density bound for X^T A X (with continuity recorded separately), or give a valid counterexample.

A current structural reduction from fleet03/B07 (`QFORM-THIRD-COMPOUND-OVERLAP-REDUCTION-v1`, math-open-problems commit `685929d9daee92a164dbf6ba6f9305d2e6550826`) says that the spectral hypothesis forces one of four constant third-compound banks O0/O1/O2/O3. The O0 diffuse ridge subbranch is already paid by `QFORM-RIDGE-DENSITY-v1`. The assigned partner fleet02/B07 (`QFORM-Q0-RIDGE-FOUR-HEAVY-DPP-v1`, commit `059c2aefcc283898976e9e207fcc01049b85fb97`) sharpens the unpaid O0 branch: after calibrating the ridge kernel to effective dimension three, either the q=6/5 ridge condition pays the density directly, or the set of rows with ridge leverage >3/5 has at most four original coordinates.

This report attacks exactly that finite-heavy-core branch. The new result is that **one fixed inclusion/exclusion pattern on those at most four coordinates retains a fixed fraction of the entire regularized determinant, and the retained determinant factors exactly into a physical finite-core Gram determinant times a projected residual regularized determinant.** Thus determinant weight is not lost when conditioning/peeling the heavy rows. The first remaining analytic task is a product-law payment of this finite-core/residual factor (and the corresponding O1/O2/O3 packets), not another search for one large principal minor.

No full QFORM proof is claimed here. The new lemmas are structural. Continuity is not proved by them; continuity remains available only on the already-paid ridge/diffuse branches.

## 2. Partner result actually consumed

The designated partner fleet02/B07 r12 proves the following applicable branch. For a physical cross block B, set

L = gamma^{-2} B B^T,  K = L(I+L)^{-1}.

On the calibrated high-leverage O0 branch one may take `tr K = 3` (or the rank-three gamma -> 0 limiting interpretation). If all diagonal ridge leverages satisfy K_ii <= 3/5, the partner applies the completed ridge theorem with q=6/5 and closes that branch. Otherwise

H := {i : K_ii > 3/5}

has cardinality at most four, simply because sum_i K_ii=3.

Everything below starts from this exact partner state and derives a new quantitative invariant for it.

## 3. New theorem: fixed heavy-pattern determinant payment

### Theorem 3.1 (`QFORM-RIDGE-HEAVY-CORE-SCHUR-FACTOR-v1`)

Let B be any real m by n matrix and gamma>0. Put

L = gamma^{-2} B B^T,
K = L(I+L)^{-1},
D = det(I+L).

Assume `tr K=3` and define

H = {i : K_ii > 3/5},   C = H^c.

Then |H|<=4 and there exists a subset T of H such that

(3.1)  W_T := sum_{R subset C} det L[T union R, T union R] >= D/16.

If T is nonempty, the inequality W_T>0 forces B_T to have full row rank. With

P_T^perp = I - B_T^T (B_T B_T^T)^{-1} B_T

(the orthogonal projection in the column space onto the orthogonal complement of the span of the rows in T), one has the exact factorization

(3.2)  W_T
       = gamma^{-2|T|} det(B_T B_T^T)
         det(I_C + gamma^{-2} B_C P_T^perp B_C^T).

For T=empty set, the first factor is interpreted as one and P_T^perp=I.

Moreover

(3.3)  D >= e^3,

and hence the selected pattern satisfies the dimension-free multiplicative inequality

(3.4)  gamma^{-2|T|} det(B_T B_T^T)
       det(I_C + gamma^{-2} B_C P_T^perp B_C^T)
       >= e^3/16 > 1.2553.

This is a determinant-weight statement about original physical rows. No row-space rotation of the independent variables is performed.

### Proof

Because L is positive semidefinite, the principal-minor expansion gives

D = det(I+L) = sum_{S subset [m]} det L[S,S].

Partition all subsets S according to the pattern T=S intersect H. There are at most 2^{|H|}<=16 patterns, so some T obeys (3.1).

If det L[T,T]=0, the Gram vectors indexed by T are linearly dependent. Every larger Gram family containing T remains dependent, so every determinant in W_T vanishes. Thus W_T>0 implies det L[T,T]>0 whenever T is nonempty.

Fix such a T. For R subset C, the block determinant identity gives

det L[T union R,T union R]
 = det L[T,T] det M_T[R,R],

where

M_T = L[C,C] - L[C,T] L[T,T]^{-1} L[T,C].

Summing over all R subset C and using the principal-minor expansion again gives

W_T = det L[T,T] det(I_C+M_T).

Now write L=gamma^{-2}BB^T. Direct substitution yields

M_T = gamma^{-2} B_C
      [I - B_T^T(B_TB_T^T)^{-1}B_T]
      B_C^T
    = gamma^{-2} B_C P_T^perp B_C^T,

and

det L[T,T] = gamma^{-2|T|} det(B_TB_T^T).

This proves (3.2).

For (3.3), let kappa_j in [0,1) be the eigenvalues of K. Since L and K have the same eigenvectors and kappa_j=lambda_j(L)/(1+lambda_j(L)),

log D = sum_j log(1+lambda_j(L))
      = sum_j -log(1-kappa_j)
      >= sum_j kappa_j
      = tr K = 3.

Exponentiating and combining with (3.1) gives (3.4). QED.

### Interpretation

The unpaid O0 heavy branch no longer consists merely of “at most four bad rows.” A fixed physical occupancy pattern on those rows retains at least 1/16 of the *whole* regularized determinant. After that pattern is fixed, the determinant resource splits multiplicatively into

1. a finite physical core with at most four rows, measured by the aggregate row-volume `det(B_TB_T^T)`, and
2. the residual cross block after orthogonally removing exactly the row-space directions already paid by the core.

There is no reciprocal selection of one tiny coordinate minor. If the finite core determinant is small, the projected residual determinant must compensate, and conversely.

## 4. Exact deletion identity for an arbitrary heavy set

The same algebra yields an exact set-valued extension of the previous one-row deletion formula.

### Lemma 4.1 (`QFORM-RIDGE-SET-DELETION-v1`)

For any G subset [m], let C=G^c. Then

(4.1) det(I+L[C,C]) / det(I+L) = det(I-K[G,G]).

Equivalently, for the L-ensemble probability law

P(Y=S)=det L[S,S]/det(I+L),

(4.2) P(Y intersect G = empty set)=det(I-K[G,G]).

For |G|=1 this reduces to `D_{-i}=D(1-K_ii)`. For a group of heavy rows it records exactly how much regularized determinant survives simultaneous conditioning/deletion; no product of single-row lower bounds is required.

Proof: either apply the Schur determinant formula to I+L, or use the standard principal-minor expansion on C and the identity I-K=(I+L)^{-1}. Jacobi's complementary-minor identity gives (4.1).

## 5. New third-order ridge packet: 0+3 / 1+2 / 2+1 / 3+0

The all-size determinant factorization above has a third-compound companion which is closer to the original coordinate-minor assignment.

### Lemma 5.1 (`QFORM-RIDGE-THIRD-PACKET-v1`)

Let K be any positive semidefinite contraction with tr K=3, and let H={i:K_ii>3/5}. Then

(5.1) e_3(K) = sum_{|S|=3} det K[S,S] >= 1.

Consequently, after splitting the sum by r=|S intersect H|, one of the following holds:

- r=0: `sum_{S subset C, |S|=3} det K_S >= 1/4`;
- r=1: for some i in H,
  `sum_{R subset C, |R|=2} det K_{ {i} union R } >= 1/16`;
- r=2: for some pair P subset H,
  `sum_{j in C} det K_{P union {j}} >= 1/24`;
- r=3: for some triple T subset H, `det K_T >= 1/16`.

Thus the calibrated heavy branch contains a constant **aggregate** third-order determinant packet with at most four possible physical heavy coordinates.

### Proof of e_3(K)>=1

Let kappa_1,...,kappa_N be the eigenvalues of K. They lie in [0,1] and sum to 3. Fix all but two values a,b. Writing E_1,E_2,E_3 for the elementary symmetric polynomials of the remaining values,

e_3 = ab E_1 + (a+b)E_2 + E_3.

At fixed a+b, the coefficient of ab is E_1>=0. Therefore e_3 cannot increase when (a,b) is pushed to an endpoint of the square [0,1]^2 while preserving a+b: replace it by (a+b,0) if a+b<=1 and by (1,a+b-1) if a+b>=1. Iterating leaves all coordinates at 0 or 1; since the sum is the integer 3, the endpoint is exactly three ones and the rest zeros. There e_3=1. Hence (5.1).

The four packet bounds follow by pigeonhole over r=0,1,2,3 and then over at most |H|<=4 choices of the heavy part.

Remark: with `Z=B(gamma^2 I+B^TB)^{-1/2}`, K=ZZ^T, so each `det K_S` is itself the exact sum of squares of all |S|-minors of Z with row set S. This is a regularized determinant bank, not one selected minor.

## 6. Second new refinement: pin the partner Pluecker packet to a full-A physical core

The earlier fleet02/B07 result `QFORM-PLUCKER-STRATUM-COLLAR-v1` (commit `55751ad6d9915a2600d42385d41388c900d29a26`) supplies, on its localized selected-three-eigenspace branch, a physical set J with 1<=|J|<=3 and a nonempty T subset J such that

m_T(J) := sum_{|R|=3, R intersect J=T} det(U_R)^2 >= 1/8,

where U consists of the selected three orthonormal large-eigenvalue eigenvectors.

The previous B07 run transferred this packet through A^2 without loss. Here is a sharper fixed-core form.

### Theorem 6.1 (`QFORM-FIXED-CORE-COMPOUND-SLICE-v1`)

On that localized partner branch, there exists T' subset J such that

(6.1) sum_{|R|=|K|=3,
          R intersect J=T,
          K intersect J=T'} det A[R,K]^2 >= 1/64.

Furthermore, after also splitting by h=|R intersect K|, one fixed h in {0,1,2,3} carries at least 1/256.

### Proof

Let P=UU^T. Since the three selected eigenvalues have modulus at least one,

A^2 - P is positive semidefinite.

For every physical triple R,

det((A^2)[R,R])
 = det(A[R,:] A[R,:]^T)
 = sum_{|K|=3} det A[R,K]^2
 >= det(P[R,R])
 = det(U_R)^2.

Sum over R with R intersect J=T. The result is at least m_T(J)>=1/8. Partition the column triples K by the pattern T'=K intersect J. There are at most 2^{|J|}<=8 patterns. One therefore carries at least 1/64. Splitting that packet into four possible overlap values h loses at most another factor four. QED.

This is stronger than an overlap-only coloring: both the row and column incidence with the same physical core J (of size at most three) are now fixed. It survives the full-spectrum cancellation example A=I_4-J_4/3 because it uses row-volume before selecting columns.

## 7. Exact polynomial object for the two-shared-coordinate bank

The h=2 bank has a useful division-free identity. Fix a physical pair S, put C=S^c and H=A[S,S]. Define

C_S(i,j) = det A[S union {i}, S union {j}],  i,j in C.

Then

(7.1) C_S = det(H) A[C,C] - A[C,S] adj(H) A[S,C].

When H is invertible this is `det(H)` times the Schur complement, but (7.1) remains valid when H is singular and therefore does not introduce the forbidden reciprocal of a tiny principal pivot.

For the cancellation stress matrix A=I_4-J_4/3 and S={1,2},

H = [[2/3,-1/3],[-1/3,2/3]],
C_S = [[0,-1/3],[-1/3,0]].

Thus all 3x3 principal minors vanish while the two-shared-coordinate bordered-minor bank remains nonzero. This is exactly why the next payment should be formulated for the polynomial bank C_S rather than by dividing through det H first.

## 8. First essential missing implication after this run

A useful target-level closure can now be stated without selecting one small minor.

**`QFORM-FINITE-CORE-DETERMINANT-PAYMENT-v1` (OPEN):** Starting from either

(a) the calibrated O0 factor (3.4) with |T|<=4, or
(b) the full-A fixed-core third-compound packet (6.1) with |J|<=3,

prove a universal density/small-ball estimate directly under the original product law, allowing arbitrary self blocks, outside couplings, additional eigenvalues and all signs. In the h=2 subcase the payment must use the division-free bordered matrix (7.1), or an equivalent product-preserving identity, so that a tiny/singular physical pivot never appears in a denominator.

If this lemma is proved together with the analogous finite-core payments for all O1/O2/O3 packet patterns, the existing third-compound reduction plus the already-paid diffuse ridge branch gives the full theorem. The current conditional-projection-density shortcut is not used; the live correction and fleet02/B07 r12 counterexample show that shortcut is false.

## 9. Exact checks

Exact rational checks used in this run:

1. For

B = [[1,2,0,1],
     [0,1,1,2],
     [2,0,1,1],
     [1,1,2,0],
     [2,1,0,1]], gamma=1,

`D=det(I+BB^T)=1455`. For G={0,2}, `det(I+L[G^c,G^c])=208`, and exactly

`det(I-K[G,G])=208/1455`.

The four occupancy-pattern determinant weights are

empty: 208, {0}: 376, {2}: 376, {0,2}: 495,

which sum exactly to 1455. For T={0,2},

`det L_T=27`, `det(I+M_T)=55/3`, product=495.

The Schur residual M_T equals exactly `B_C P_T^perp B_C^T`.

2. For the symmetric integer test matrix

A = [[3,1,2,0,1],
     [1,2,1,1,0],
     [2,1,4,2,1],
     [0,1,2,3,1],
     [1,0,1,1,2]],

with S={0,1}, both sides of (7.1) equal

[[13,9,2],[9,12,6],[2,6,8]].

These finite exact checks validate the algebraic identities only; they are not evidence for the universal density conjecture.

## 10. Outcome

Outcome label: **ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN**.

New proved content: a dimension-free fixed-pattern factorization of the full ridge determinant on the <=4-row heavy core; a constant third-order ridge packet; a fixed-core refinement of the partner Pluecker packet in the full matrix; and a division-free bordered-minor identity isolating the h=2 payment object.

Not proved: a universal payment of the finite-core determinant factor under arbitrary cap-one product laws, the O1/O2/O3 analytic payments, the full L-infinity theorem, or global continuity.
