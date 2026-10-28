SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-23T03:37:53Z.
attacking: recolor an exact rank-one low-cross survivor using two diffuse child curvature banks; prove a third-volume exit or a localized bicolop certificate, and test robustness to the partner near-rank-one tube.

# B08 report — rank-one recoloring converts bilateral child curvature into 3-volume

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / REFUTED_NAIVE_NEAR-RANK1_STABILITY`.
Full unrestricted QFORM target: OPEN.
Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source-valid inputs

The target is unchanged: independent original coordinates with arbitrary real probability densities bounded by one, arbitrary real symmetric A, and at least three eigenvalues of modulus at least one. No moments, compact support, log-concavity, Gaussianity, connected support, or independence after spectral rotation is used.


Completed inputs actually used at equations:

1. Designated partner account02/B08, `QFORM-DIFFUSE-HYBRID-VOLUME-TAIL-LADDER-v1`, canonical source `yspennstate/math-open-problems@31212dc0982ef58cdae6fc12c9354599a663fad6`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T020620Z-account02-B08-QFORM-auto11/REPORT.md`. At selected-three leverage at most 1/48 it reduces the k=2 branch to a paid branch, a bicolop anchor, a very tight rank-two tube, or a rank-one Frobenius tube. Its rank-one tube contains the exact rank-one endpoint addressed below.
2. The preceding account01/B08 bilateral-curvature theorem, `yspennstate/math-open-problems@9534b12fbf558d1b6c82db1bc55068afd764fcce`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B08/20260923T030529Z-account01-B08-QFORM-auto11/REPORT.md`. In the partner rank-one tube it gives two strong actual child eigenvalues on each physical bank.
3. The sharp fractional three-volume theorem in `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, path `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`: for an original-coordinate cross block M with third-volume row marginals alpha_i <= q/2, 1<=q<3/2,

   ||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] e_3(M^T M)^(-1/6),

with a continuous C_0 density, while arbitrary same-bank quadratic terms, outside couplings and affine terms are retained.

## 2. A sharp 4-by-4 algebraic core

Write E_3(T)=e_3(T^T T)=||wedge^3 T||_HS^2, equivalently the sum of the squares of all 3-by-3 minors of T.

### Lemma 2.1 — `QFORM-RANK1-BLOCK-IDENTITY-E3-7OVER2-v1`

For arbitrary real 2-by-2 matrices U,V of rank at most one,

    N = [[I_2, U],
         [V,   I_2]]

satisfies

    E_3(N) >= 7/2.                                             (2.1)

The constant 7/2 is sharp.

#### Proof

Blockwise left/right orthogonal transformations preserve the singular values of N and can put

    U = s e_1 e_1^T,  s>=0,
    V = t v w^T,      t>=0,

where v,w are unit vectors. Write x=<v,e_1>, y=<w,e_1>. Direct expansion of the sixteen 3-by-3 cofactors gives the exact identity

    E_3(N)
      = 4+s^2+t^2+s^2 t^2(x^2+y^2)-4stxy.                    (2.2)

If xy<=0, the last term is nonnegative and (2.1) is immediate. If xy>=0, set a=st and z=xy in [0,1]. Since x^2+y^2>=2xy=2z and s^2+t^2>=2st=2a,

    E_3(N)-4 >= 2a+2a^2 z-4az.

For a>=2 the right side is minimized at z=0 and is at least 4. For 0<=a<=2 it is minimized at z=1, giving

    E_3(N)-4 >= 2a^2-2a = 2(a-1/2)^2-1/2 >= -1/2.

Thus E_3(N)>=7/2. Equality occurs for s=t=1/sqrt(2), v=w=e_1, where the singular values are 1+1/sqrt(2),1,1,1-1/sqrt(2), and E_3=7/2. QED.

### Lemma 2.2 — conditioned diagonal blocks

Let C,D be 2-by-2 invertible matrices with

    s_min(C), s_min(D) >= c>0,

and let U,V have rank at most one. Then

    M_4 = [[C,U],[V,D]]

satisfies

    E_3(M_4) >= (7/2)c^6.                                    (2.3)

Indeed,

    M_4 = diag(C,D) [[I,C^{-1}U],[D^{-1}V,I]].

The second factor is covered by Lemma 2.1, and the least singular value of wedge^3 diag(C,D) is at least c^3. Hence

    ||wedge^3 M_4||_HS >= c^3 ||wedge^3 N||_HS.

### Lemma 2.3 — rectangular version

Let C and D be arbitrary rectangular matrices with s_2(C),s_2(D)>=c, and let U,V be conforming matrices of rank at most one. Then for

    M = [[C,U],[V,D]]                                        (2.4)

one still has

    E_3(M) >= (7/2)c^6.                                      (2.5)

Choose the top two left/right singular vectors of C and D and compress (2.4) to the corresponding 4-by-4 block. The diagonal compressed blocks have least singular value at least c, while the two off-diagonal compressed blocks still have rank at most one. Lemma 2.2 applies. Orthogonal compression is contractive on the Hilbert-Schmidt norm of wedge^3, so the full E_3 is at least the compressed E_3. QED.

## 3. Recoloring theorem: diffuse 3-volume exit or a localized bicolop

Suppose an ORIGINAL-coordinate partition is I union J and the cross block B=A[I,J] has exact rank at most one. Split each bank again,

    I=I_+ union I_-,   J=J_+ union J_-,

and define the two within-child cross blocks

    C=A[I_+,I_-],  D=A[J_+,J_-].

Assume

    s_2(C), s_2(D) >= c>0.                                  (3.1)

Recolor the physical coordinates as

    K=I_+ union J_+,    L=I_- union J_-.

The actual K-by-L cross block of A is

    M=A[K,L]
      = [[C,                 B[I_+,J_-]],
         [B[J_+,I_-]^T,      D            ]].                (3.2)

Because B has rank at most one, both off-diagonal blocks in (3.2) have rank at most one. Lemma 2.3 therefore gives

    Z:=e_3(M^T M) >= (7/2)c^6.                              (3.3)

Let w_{S,T}=det(M[S,T])^2/Z be the third-volume sampling law, with row and column marginals alpha_i and beta_j.

### Theorem 3.1 — `QFORM-RANK1-RECOLORING-PAID-OR-BICOLOP-v1`

Under (3.1), exactly one of the following conclusions is forced (the two alternatives may overlap at non-strict endpoints):

**Diffuse volume exit.** If max_i alpha_i<=2/3 or max_j beta_j<=2/3, then the full ambient quadratic form has a continuous C_0 density and

    ||p_Q||_infinity
      <= (9 sqrt(3)e/2) Z^(-1/6)
      <= C_rec/c,                                             (3.4)

where

    C_rec=(9 sqrt(3)e/2)(7/2)^(-1/6)
         =17.1945025411191....

To prove this, use q=4/3 in the completed fractional three-volume theorem. If the column marginal is the good one, apply the same theorem to M^T, i.e. swap the two physical sides. No random-coordinate rotation is performed.

**Localized third-volume bicolop.** Otherwise choose a physical row i and column j with alpha_i>2/3 and beta_j>2/3. Under w,

    P(i in S and j in T)
       >= alpha_i+beta_j-1 >1/3.

Hence the double-incident physical 3-minor bank obeys

    W_ij^(3)
      := sum_{S contains i, T contains j} det(M[S,T])^2
      > Z/3
      >= (7/6)c^6.                                           (3.5)

This is a genuinely localized physical certificate produced by failure of the diffuse volume gate. Thus exact rank-one coupling cannot erase two independent rank-two child cross resources: after recoloring, they become either a paid rank-three volume or a quantitatively large physical bicolop.

All of (3.2)-(3.5) are statements about original-coordinate blocks of the ACTUAL matrix A. Arbitrary same-side blocks, outside coordinates/couplings, and all unused spectral directions remain in the ambient form.

## 4. Elementary second-stage diffuse splitter for a two-eigenvalue child

The preceding theorem needs an actual physical split with s_2(C)>=c. Here is a moment-free sufficient condition that retains a genuine spectral tail rather than deleting it.

### Lemma 4.1 — rank-two frame split

Let R be m-by-2 with R^T R=I_2 and row leverage

    mu=max_i ||r_i||^2 <1/2.

There is a physical partition +,- such that both restricted Gram matrices obey

    R_+^T R_+, R_-^T R_- >= alpha I_2,
    alpha=(1-sqrt(2mu))/2.                                  (4.1)

Proof: choose independent random signs eps_i and S=sum eps_i r_i r_i^T. Then

    E||S||_F^2=sum_i ||r_i||^4 <= mu sum_i||r_i||^2=2mu.

Some signing satisfies ||S||_op<=||S||_F<=sqrt(2mu). Since R_+^TR_+=(I+S)/2 and R_-^TR_-=(I-S)/2, (4.1) follows.

### Corollary 4.2 — retain an arbitrary small spectral tail

Let a symmetric child matrix be

    H=R Lambda R^T+E,

where R^TR=I_2, min |lambda_k(Lambda)|>=kappa, max row leverage<=mu<1/2, and ||E||_op<=eta. The partition in Lemma 4.1 satisfies

    s_2(H[+,-]) >= alpha kappa-eta.                          (4.2)

Indeed the rank-two spectral cross block has second singular value at least sqrt(alpha)*kappa*sqrt(alpha)=alpha kappa, and the ACTUAL tail block E[+,-] has operator norm at most eta. Thus the tail is retained in the true cross block and paid by singular-value perturbation; it is not treated as a small random quadratic perturbation.

Applying Corollary 4.2 independently to the two physical children in Section 3 gives Theorem 3.1 with

    c=alpha kappa-eta>0.                                    (4.3)

This is a concrete second-stage diffuse-to-volume transducer.

## 5. Actual application of the designated partner result

In account02/B08's k=2 rank-one-tube branch at selected-three leverage <=1/48, put

    rho=sqrt(3/5),
    beta=(3/16)rho L.

At the exact-rank-one endpoint of that partner survivor, the preceding account01/B08 bilateral-curvature theorem gives TWO actual eigenvalues on EACH child of modulus larger than

    kappa_* L,
    kappa_* = sqrt(3/5)-3/128
            =0.751159169241483....                          (5.1)

Now impose only the following second-stage diffuse spectral-window condition on each child: use those two actual child eigenvectors as R, assume their row leverage is at most mu, and assume the remaining child spectral operator norm is at most eta. Then Lemma 4.1 and Corollary 4.2 give physical child splits with

    c=[(1-sqrt(2mu))/2] kappa_* L-eta.                      (5.2)

Whenever c>0, Theorem 3.1 gives the ACTUAL full-form implication

    ||p_Q||_infinity <=17.1945025411191/c                    (5.3)

with a continuous C_0 density, OR a recolored physical double-incident 3-volume bank

    W_ij^(3) > (7/6)c^6.                                    (5.4)

For the clean values

    mu<=1/32,   eta<=L/64,

one has alpha=3/8 and

    c >= [ (3/8)(sqrt(3/5)-3/128)-1/64 ]L
      =0.266059688465556... L.

Therefore the partner exact-rank-one endpoint plus this second-stage diffuse condition satisfies

    boxed( ||p_Q||_infinity <64.627/L )                      (5.5)

with continuous C_0 density, OR else

    boxed( W_ij^(3)>0.000413829321503891 L^6 ).              (5.6)

This is the requested quantitative join: a partner low-cross-rank survivor is either paid by a new diffuse volume cut or converted into a localized physical bicolop currency. It does not claim that the second-stage child window condition is automatic.

## 6. Exact obstruction: the near-rank-one tube is NOT a perturbative corollary

A tempting but false next step would be to replace `rank B<=1` in Section 3 by `dist_F(B,rank<=1)<=epsilon` and assert a positive E_3 floor depending only on c and epsilon. The following target-valid family shows that no such continuity statement is available without controlling the conditioning/scale of the rank-one core.

Take four physical groups I_+,I_-,J_+,J_-, each of size two. Let the child internal cross blocks be

    C=D=I_2,

so c=1. Given epsilon>0, put R=1/epsilon and define a rank-one outer block B_0=a b^T with restrictions arranged so that

    B_0[I_+,J_-]=R e_1e_1^T,
    B_0[I_-,J_+]=R e_2e_2^T.

(For example choose a_+=sqrt(R)e_1, a_-=sqrt(R)e_2, b_+=sqrt(R)e_2, b_-=sqrt(R)e_1.) Add an outer-block perturbation E_B supported only on those two subblocks:

    E_B[I_+,J_-]=epsilon e_2e_2^T,
    E_B[I_-,J_+]=epsilon e_1e_1^T.

Then

    dist_F(B_0+E_B, rank<=1) <= ||E_B||_F=sqrt(2)epsilon.     (6.1)

After the same recoloring as Section 3, the actual cross block is

    M_epsilon=[[I_2, diag(R,epsilon)],
               [diag(epsilon,R), I_2]].                     (6.2)

But the product of the lower-left and upper-right off-diagonal blocks is exactly I_2 because R epsilon=1. The Schur complement of the upper-left I_2 therefore vanishes:

    rank M_epsilon=2,
    E_3(M_epsilon)=0.                                       (6.3)

This can be embedded in a symmetric target-valid A by taking each child principal block to be [[0,I_2],[I_2,0]] and the outer block to be B_0+E_B. The 4-by-4 child principal block has eigenvalues 1,1,-1,-1, so Cauchy interlacing guarantees the full symmetric matrix has at least four eigenvalues of modulus at least one. Thus (6.1)-(6.3) refute only the proposed perturbative recoloring step, not QFORM.

This obstruction is directly relevant to the partner's genuine rank-one FROBENIUS tube: even an arbitrarily thin tube may contain matrices for which the recolored 3-volume vanishes if the rank-one core is badly conditioned/large. One must either preserve the exact rank-one factor structurally, use a scale-sensitive condition, or route the badly conditioned core to a hub/pair mechanism.

## 7. What remains

The first unpaid implication for this B08 route is now

`QFORM-NEARRANK1-RECOLOR-OR-HUB-v1`:

Starting from the account02/B08 rank-one Frobenius tube, prove a scale-sensitive alternative that either

1. controls the rank-one core sufficiently to make the recolored third-volume stable and invoke Theorem 3.1, or
2. converts the ill-conditioned/large-core case into an already-payable physical hub/pair or grouped-coordinate certificate.

The explicit family in Section 6 shows that a scale-free perturbative E_3 argument cannot do this. The exact-rank-one endpoint and the second-stage diffuse child-window subcase are now quantitatively classified. The unrestricted conjecture remains OPEN; continuity is proved only on the paid branch (3.4)/(5.5), not on the bicolop branch.
