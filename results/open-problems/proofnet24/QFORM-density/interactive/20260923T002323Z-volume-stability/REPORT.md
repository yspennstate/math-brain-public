# A dimension-free stability certificate for the three-volume method

Programme QFORM-DENSITY-3EIG-20260922. Interactive record 20260923T002323Z-volume-stability.

**Status:** complete supporting arguments below; independent review pending. The full conjecture and the general no-pivot statement N3 remain unproved. This note uses Claude's actual volume-sampling and Jensen arguments, rather than restarting the diagonal or absolute-continuity cases. No literature-wide novelty claim is made.

## 1. Result and precise relevance

Let I,J be disjoint ORIGINAL coordinate sets and M=A[I,J]. Suppose

    M=M0+E,  s3(M0)>=a>0,
    max_i (P_range(M0))_ii <= 1/2,  ||E||op <= a/16.          (1)

For independent real probability densities f_i<=1,

    ||p_(X^T A X+b^T X+c)||infinity
        <= (24 sqrt(3) e)/(5a) < 23/a.                     (2)

The density has a continuous version vanishing at infinity. All within-bank quadratic terms, outside couplings, and affine terms are arbitrary. Neither M0 nor E must have a bounded rank; M0 may have arbitrarily small additional singular values. The estimate is independent of their number.

The proof is not a small-random-variable perturbation argument. No moments or support bounds are available or used. The actual perturbed cross block is retained in the characteristic function, including every singular direction. The new point is an explicit bound on the volume-sampling row marginals under perturbation; preserving three singular values alone does NOT preserve their admissibility gate.

More intrinsically, for ANY orthogonal projection P on the row-index space, put l_i=P_ii, kappa=s3(M)>0, and epsilon=||(I-P)M||op. The third-volume row marginals obey

    sqrt(alpha_i) <= sqrt(l_i)
                         + (sqrt(3) epsilon/kappa) sqrt(1-l_i).    (3)

Thus one can verify a useful diffuse certificate without diagonalizing or conditioning the random input coordinates. Algebraic singular vectors in this note are used only to prove matrix inequalities.

This closes the nearby-diffuse-cross-block class (1), not every no-pivot matrix. In particular it does NOT pay a rank-two cross block plus an arbitrarily small third singular value: then kappa is not bounded below. The current rank-two-tube and hub configurations remain explicit obligations.

## 2. Classical analytic inputs and the source being extended

Use Fourier convention hat f(u)=integral exp(-iux)f(x) dx. The sharp Hausdorff--Young inequality is

    ||hat f||p' <= (2pi)^(1/p') p^(1/(2p)) (p')^(-1/(2p')) ||f||p,
    1<=p<=2, 1/p+1/p'=1.                                    (4)

It applies to complex functions as well. The Brascamp--Lieb input is Lieb's Gaussian-exhaustion theorem: the best constant of a finite-dimensional linear BL datum equals the supremum over centered Gaussian inputs, with continuous endpoint interpretation. These are classical inputs, not results newly claimed here.

Primary references: W. Beckner, Inequalities in Fourier analysis, Annals of Mathematics 102 (1975), 159--182, DOI 10.2307/1970980; J. Bennett, A. Carbery, M. Christ, T. Tao, The Brascamp--Lieb inequalities: finiteness, structure, and extremals, arXiv:math/0505065, final version 2007, GAFA 17 (2008), 1343--1415.

The immediate research source is Claude's FOURIER_ROUTE_REPORT.md Sections 1, 1.1 and 1.2, at math-open-problems commit e5f71d79eff325201dd0274053d20268ce65b837, path proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/. The sharp-HY q=1 refinement was already recorded at 9844891a9fbe96a65e37f71122bf0300b53dcc80 in the 20260922T220600Z-claude-review/REVIEW.md. Here we give the q-dependent calculation and combine it with (3).

## 3. Exact volume marginals

For a real m-by-d matrix M with rank at least three, let lambda_j be the squared singular values, including zeros if necessary, and write

    E2=e2(lambda), Z=E3=e3(lambda)>0.

Give each pair S,T of row and column triples probability det(M[S,T])^2/Z. Cauchy--Binet says these probabilities sum to one. Write alpha_i for the row inclusion probability and beta_j for the column inclusion probability. Then

    0<=alpha_i,beta_j<=1, sum alpha=sum beta=3.                (5)

If M=U diag(s_j) V^T, define

    p_j=lambda_j e2(lambda without j)/Z,
    W=U diag(p_j) U^T.                                       (6)

Then W_ii=alpha_i. One verification is to expand E3 after multiplying row i by sqrt(1+t). The coefficient of t is the mass of triple minors containing row i. The derivative of the elementary symmetric polynomial of MM^T gives (6). Equivalently, its spectral derivative is e2(lambda without j), and the row-scaling derivative of MM^T supplies the lambda_j factor. This identity is continuous at repeated singular values and zero modes.

We will use the two elementary operator inequalities

    0 <= W <= I,     W <= (E2/Z) M M^T.                     (7)

Indeed Z=lambda_j e2(lambda without j)+e3(lambda without j), so 0<=p_j<=1, and e2(lambda without j)<=E2.

If kappa=s3(M), at least three lambda_j are >=kappa^2. The identity

    3Z=sum_(p<q) lambda_p lambda_q sum_(r notin {p,q}) lambda_r

therefore gives 3Z>=kappa^2 E2: after removing any two indices at least one of the three large ones remains. Thus

    E2/Z <= 3/kappa^2,       W <= 3 M M^T/kappa^2.            (8)

## 4. Proof of the projection stability estimate

Fix an orthogonal projection P and an original coordinate vector e_i. By the triangle inequality and W<=I,

    ||W^(1/2)e_i||
       <= ||W^(1/2)P e_i||+||W^(1/2)(I-P)e_i||
       <= sqrt(l_i)+(sqrt(3)/kappa)||M^T(I-P)e_i||
       <= sqrt(l_i)+(sqrt(3)epsilon/kappa)sqrt(1-l_i).

Here (8) gives the middle inequality, and epsilon=||(I-P)M||op. The left side is sqrt(alpha_i). This proves (3) in all dimensions, without an eigenspace gap for the smaller singular values or a rank bound on the perturbation.

Now assume (1), take P=P_range(M0), and note that epsilon<=||E||op and kappa>=a-||E||op>=15a/16 by the singular-value perturbation inequality. Thus

    sqrt(3)epsilon/kappa <= sqrt(3)/15 =:d0.

For 0<=l<=1/2 and 0<=d<=1, the function sqrt(l)+d sqrt(1-l) is increasing in l on this interval. Therefore

    alpha_i <= (1+d0)^2/2
             = (1+sqrt(3)/15)^2/2
             =0.6221367205... <2/3.                          (9)

We will apply the Fourier theorem below with q=4/3. The margin above the old 1/2 gate is paid explicitly by q; it is not ignored.

## 5. Fractional three-volume Fourier bound with sharp constants

**Theorem.** Let Z=e3(M^T M)>0 and 1<=q<3/2. If alpha_i<=q/2 for every row, then

    ||p_Q||infinity <= [3e/((3-2q)sqrt(q))] Z^(-1/6).        (10)

The conclusion is a bounded continuous density vanishing at infinity. It applies to the original quadratic-plus-affine form, and more generally to F(X_I)+2 X_I^T M X_J+G(X_J), where F,G are arbitrary real measurable functions finite almost surely. Outside original coordinates can be conditioned on when they leave the same M; the bound is uniform in all resulting F,G.

### 5.1 Decoupling preserves the original product source

Write psi_i=hat f_i, take X_J' independent of all other variables, and D=X_J-X_J'. Each D_j has density g_j=f_j*tilde f_j, with mass one and cap one. Cauchy--Schwarz in the original X_I variables and then the triangle inequality give exactly

    |phi_Q(t)|^2 <= E_D prod_i |psi_i(2t(MD)_i)|.             (11)

The self phases disappear through these inequalities. No sums and differences are declared independent and no spectral rotation of the random inputs is performed.

Let F_t(D)=prod_i |psi_i(2t(MD)_i)|. Since the D-law is a probability law, Jensen gives E F_t <= (E F_t^q)^(1/q).

### 5.2 Gaussian BL constant, including endpoint columns

Use the row maps w -> (Mw)_i with exponent alpha_i, and the coordinate maps w -> w_j with exponent 1-beta_j. Their total exponent is d. Drop rows with alpha_i=0 using |psi_i|<=1, and columns with beta_j=1 using g_j<=1.

For positive Gaussian row parameters d_i and active-column parameters e_j, the denominator of the squared Gaussian BL ratio is det(D_J+M^T D_I M). Put e_j=0 at dropped columns. The diagonal-plus-positive-semidefinite determinant expansion gives

    det(D_J+M^T D_I M)
      >= sum_(|S|=|T|=3) det(M[S,T])^2 prod_(i in S)d_i prod_(j notin T)e_j
      >= Z prod_i d_i^alpha_i prod_j e_j^(1-beta_j).          (12)

The second inequality is weighted AM--GM with the squared-minor probabilities. A column with beta_j=1 belongs to every T of positive weight, so its zero e_j never occurs in an active term. Thus there is no inverse of a zero diagonal parameter in (12).

Lieb's theorem now gives the BL constant at most

    Z^(-1/2) prod_i alpha_i^(-alpha_i/2)
                   prod_j (1-beta_j)^(-(1-beta_j)/2).        (13)

The factors with exponent zero have continuous value one. The estimate (12) also establishes finiteness of the datum.

### 5.3 Sharp HY and the scalar exponents

Apply (13) to h_i(u)=|psi_i(2tu)|^q and to g_j. Since integral f_i^p<=1 for every p>=1, (4) at output exponent q/alpha_i>=2 gives

    ||h_i||_(1/alpha_i)
       <= (pi/|t|)^alpha_i
          (alpha_i/q)^(alpha_i/2)
          (1-alpha_i/q)^(-(q-alpha_i)/2).                   (14)

The column norms are at most one. Multiplying (14) and (13), the powers of alpha_i cancel. Moreover

    prod_i (1-alpha_i/q)^(-(q-alpha_i)/2) <= e^(3/2),
    prod_j (1-beta_j)^(-(1-beta_j)/2) <= e^(3/2),

by -(1-x)log(1-x)<=x. Hence

    E F_t^q <= e^3 q^(-3/2)(pi/|t|)^3 Z^(-1/2).             (15)

Combining (11), Jensen and (15) proves

    |phi_Q(t)| <= min(1,K |t|^(-b)),
    b=3/(2q)>1,
    K=[e^3 q^(-3/2) pi^3 Z^(-1/2)]^(1/(2q)).                (16)

### 5.4 Inversion

The envelope in (16) has integral 2b K^(1/b)/(b-1). Fourier inversion yields

    ||p_Q||infinity <= b K^(1/b)/(pi(b-1))
                     = [3e/((3-2q)sqrt(q))]Z^(-1/6),

which is (10). Integrability of phi supplies continuity and vanishing at infinity. This proves the theorem.

## 6. Finish the stability theorem

By (9), q=4/3 is admissible. Since Z>=s1(M)^2 s2(M)^2 s3(M)^2>=kappa^6, equation (10) gives

    ||p_Q||infinity <= (9sqrt(3)e)/(2kappa)
                     <= (24sqrt(3)e)/(5a) <23/a.

This proves (2). The result does not assume that the remaining eigenvalues of the FULL matrix A are independent noise or that any of them are small.

## 7. An explicit full-rank no-pivot family that the theorem covers

Let H_n be the symmetric Sylvester Hadamard matrix, H_n H_n^T=nI. Take n=256, m=128, let U be any three columns of H_m/sqrt(m), let R=(U;U)/sqrt(2), and J=diag(1,1,-1). Define

    A0=2 R J R^T,   A=A0+eta H_n/sqrt(n),  0<=eta<=1/16.

The top/bottom physical cross block of A0 is M0=U J U^T; s3(M0)=1 and its row-range leverage is 3/128. The cross perturbation has norm at most eta, so (2) gives a continuous density bounded by 24sqrt(3)e/5<23, UNIFORMLY as eta decreases to zero, for arbitrary cap-one product inputs.

The original spectral hypothesis holds: A0 has exactly three nonzero eigenvalues 2,2,-2, so A has three absolute eigenvalues at least 2-eta>=31/16; every other absolute eigenvalue is at most eta. Further,

    |Aii| <= 2/256+(1/16)/16 =3/256 <1/64,
    max_ij |Aij| <=6/256+1/256=7/256,
    |det A[{i,j},{i,j}]| <=2(7/256)^2 <1/64.

Thus it lies in the strict no-pivot class at tau=1/64. At eta=1/16 the attached finite checker also verifies full rank. The theorem does not need full rank; the uniform analytic bound includes the rank-three endpoint eta=0. This example is a covered family, not an exhaustive description of N3.

## 8. What remains and how this changes the fleet's work

The full no-pivot problem remains OPEN. Small entries and small coordinate-pair determinants do not force a three-dimensional diffuse cross certificate with a uniform singular scale. A star plus one extra quadratic direction can have only rank-two cross blocks, and arbitrary dense tails need not provide a substantial third direction. Nor is the rank-two Frobenius tube in fleet01/B20's newest packet covered by the theorem above merely because its tail is small.

For proof assembly, use the theorem to remove the quantitatively near-diffuse rank-at-least-three cross class from the remaining cases. Then concentrate constructive work on the low-cross-rank/hub remainder and the missing exhaustive structural implication. Use only two existing workers to independently check this proof; the other workers should APPLY it where relevant rather than duplicate eighty reviews.

Finite numerical checks accompanying this note test matrix identities, the volume-marginal formula, the stability gate and the stated constants. They are not a proof of the analytic inequalities or an independent review. Failed attempts and scope limits remain part of the mathematical record.
