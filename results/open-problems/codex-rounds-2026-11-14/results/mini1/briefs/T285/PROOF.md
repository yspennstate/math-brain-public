# An exact cubic moment for an orthonormal hard committee

Let K >= 3 be odd, d >= K, and let w_1,...,w_K be orthonormal vectors in
R^d. For X distributed as N(0,I_d), set

    G_i = <w_i,X>,    Y = sign(sum_i sign(G_i)),
    u = K^(-1/2) sum_i w_i,    S = <u,X>,
    P_0 = I_d - uu^T,    V = span(w_1,...,w_K) intersect u^perp,
    P_V = sum_i w_i w_i^T - uu^T.

The value of sign at zero is immaterial. The vector u is assumed known in the
first estimation theorem; Section 7 removes that assumption. Write

    mu = sqrt(2/pi),
    p_K = 2^(-(K-1)) binom(K-1,(K-1)/2),
    rho_K = mu(1-mu^2) p_K / sqrt(K).

## Theorem

The following identities hold exactly:

    E[YX] = mu p_K sqrt(K) u,
    E[Y(XX^T-I_d)] = 0,
    M := E[Y S ((P_0 X)(P_0 X)^T-P_0)] = -rho_K P_V.       (1)

In particular, the last matrix has K-1 negative eigenvalues, all equal to
-rho_K, and all its other eigenvalues vanish. Moreover,

    lim_{K -> infinity, K odd} K rho_K = (2/pi)(1-2/pi).   (2)

For 0 < epsilon <= 1/2 and 0 < delta < 1, put

    B = sqrt(2 log(16/(epsilon rho_K))),
    M_hat = (1/n) sum_{a=1}^n Y_a S_a 1{|S_a|<=B}
                       ((P_0 X_a)(P_0 X_a)^T-P_0).

Take the K-1 smallest-eigenvalue eigenvectors of the restriction of M_hat to
u^perp, and let P_hat be the projector onto their span. If

    n >= 32768 B^2 (epsilon rho_K)^(-2)
                    ((d-1) log(9) + log(2/delta)),         (3)

then with probability at least 1-delta,

    ||(I_d-P_V) P_hat||_op <= epsilon,
    tr(P_V P_hat)/(K-1) >= 1-epsilon^2.                   (4)

Thus this oracle-assisted estimator recovers the hidden contrast subspace using

    n = O(epsilon^(-2) K^2 (d+log(1/delta)) log(K/epsilon)).

The constants in this O bound are absolute. This is recovery of a subspace,
not identification of the individual hidden units. There is no lower bound
for general algorithms in this theorem. The clipping operation also means
the estimator is not asserted to be a polynomial of bounded degree in its data.

## 1. Boolean coefficients of majority

Let e_i = sign(G_i). These are independent uniform signs, independent of all
the magnitudes |G_i|. Write f(e)=sign(sum_i e_i), so Y=f(e).

Condition on e_2,...,e_K and let T=sum_{i=2}^K e_i, an even integer. Averaging
over e_1 gives

    E_{e_1}[f(e)e_1] = (sign(T+1)-sign(T-1))/2 = 1{T=0}.

Consequently E[f(e)e_i]=p_K for every i. Multiplying the same identity by
e_2 e_3 gives

    E[f(e)e_1 e_2 e_3] = E[e_2 e_3 1{T=0}].

Conditional on T=0, the K-1 remaining signs are exchangeable. If a is their
common pair correlation, then

    0 = E[T^2 | T=0] = (K-1)+(K-1)(K-2)a.

It follows that

    E[f(e)e_i e_j e_l] = -p_K/(K-2)                      (5)

for every three distinct indices. These arguments apply also at K=3.

## 2. The cubic Gaussian Hermite tensor

For indices a,b,c in an orthonormal coordinate system, define

    H_abc(X) = X_a X_b X_c
               -delta_ab X_c-delta_ac X_b-delta_bc X_a,
    T_abc = E[Y H_abc(X)].

For a standard normal G, integration of the Gaussian density on (0,infinity)
gives E|G|=mu and E|G|^3=2mu. Hence, in the teacher coordinates,

    T_iii = E[Y(G_i^3-3G_i)] = (2mu-3mu)p_K = -mu p_K.

For i != j, the relevant polynomial is (G_i^2-1)G_j. Since
G_i^2-1 has mean zero and is independent of every sign and the other
magnitudes,

    T_iij = 0.

For three distinct indices, independence of the magnitudes and (5) give

    T_ijl = -mu^3 p_K/(K-2).

Every component involving a coordinate orthogonal to the teacher span is zero.
For one occurrence this follows from its zero Gaussian mean; for two or
three occurrences it follows from the centered second or third Hermite
polynomial. Thus these components specify the whole tensor.

Contract T with u in its third index and call the resulting matrix C. Its
teacher-coordinate entries are

    C_ii = -mu p_K/sqrt(K),
    C_ij = -mu^3 p_K/sqrt(K)       (i != j).              (6)

Indeed, for i != j there are K-2 distinct-index terms in the contraction,
while the repeated-index terms vanish. All entries outside the teacher
span vanish. The eigenvalue of (6) on the contrast space V is

    C_ii-C_ij = -mu(1-mu^2)p_K/sqrt(K) = -rho_K.

On the other hand, the tensor definition gives in ambient coordinates

    C = E[Y(S(XX^T-I_d)-Xu^T-uX^T)].

Multiplication on both sides by P_0 eliminates the last two terms. It also
eliminates the eigenvector u from (6). This proves the last identity in (1).

The first identity in (1) follows from E[YG_i]=mu p_K and the zero means
in all remaining coordinates. For the second identity, replace X by -X:
Y changes sign and XX^T-I_d does not. Gaussian symmetry then gives zero.

Consequently, every one-sample population moment E[a(Y)q(X)], with an
arbitrary function a on {-1,1} and a polynomial q of degree at most two,
is determined by K and u. Indeed, a(Y)=a_0+a_1Y; the a_0 part is a
Gaussian moment, while E[Y]=0, E[YX]=mu p_K sqrt(K)u, and
E[YXX^T]=0 determine the a_1 part. Thus these population moments cannot
distinguish two orthonormal committees with the same u and different V.
Equation (1) supplies such a distinguishing moment at feature degree three.
This statement concerns one-sample population moments, not the degree of
polynomials in an entire training set.

## 3. An independent calculation of the contrast eigenvalue

Take v=(w_1-w_2)/sqrt(2). Direct expansion, without Hermite contraction,
gives

    <v,Mv> = E[Y S ((G_1-G_2)^2/2-1)].

For i != j, E[Y G_j(G_i^2-1)]=0 by the centered independent magnitude
at i. For i=j,

    E[Y G_i(G_i^2-1)] = (2mu-mu)p_K = mu p_K.

It follows that

    E[Y S (G_1^2-1)] = E[Y S (G_2^2-1)] = mu p_K/sqrt(K).

Also E[Y G_1^2 G_2]=E[Y G_1 G_2^2]=mu p_K, because the squared
magnitude has mean one and is independent of all signs. For j >= 3,
E[Y G_1 G_2 G_j]=-mu^3 p_K/(K-2), by (5). Therefore

    E[Y S G_1 G_2] = (2mu p_K-mu^3 p_K)/sqrt(K),
    <v,Mv> = -mu(1-mu^2)p_K/sqrt(K).

This recovers both the sign and constant in (6) directly from raw moments.

Write K=2m+1. Stirling's limit
m!/(sqrt(2 pi m)(m/e)^m) -> 1 yields

    p_K = binom(2m,m)/4^m ~ 1/sqrt(pi m),
    sqrt(K) p_K -> sqrt(2/pi) = mu.

Substitution into K rho_K proves (2).

## 4. Finite-sample concentration

All operators in this section are restricted to H=u^perp, of dimension
m=d-1. Write Z=P_0X. Then S and Z are independent standard Gaussians
on R and H respectively. Let M_B=E[M_hat]. For any unit h in H,
g=<h,Z> is standard normal and independent of S. Since |Y|=1,

    |<h,(M-M_B)h>|
      <= E[|S|1{|S|>B}(g^2+1)]
       = 2 E[|S|1{|S|>B}] = 4 phi(B),

where phi(t)=(2 pi)^(-1/2) exp(-t^2/2). Taking a supremum gives

    ||M-M_B||_op <= 4 phi(B)
                  = epsilon rho_K/(4 sqrt(2 pi))
                  <= epsilon rho_K/4.                  (7)

For fixed unit h define

    A_h = Y S 1{|S|<=B}(g^2-1),    D_h=A_h-E[A_h].

For every integer p>=2, the Gaussian moment formula gives

    E[g^(2p)] = (2p-1)!! <= 2^p p!,
    E[|g^2-1|^p] <= E[(g^2+1)^p]
                    <= 2^(p-1)(2^p p!+1) <= 4^p p!.

Thus E|A_h|^p <= (4B)^p p!. Jensen's inequality and
|a-b|^p <= 2^(p-1)(|a|^p+|b|^p) imply

    E|D_h|^p <= (8B)^p p!.

The absolute moment series is finite for |t|<1/(8B), which justifies
termwise expectation of the exponential series. Since E D_h=0,

    E exp(t D_h)
       <= 1 + (8Bt)^2/(1-8B|t|)
       <= exp(64 B^2 t^2/(1-8B|t|)).

For n independent copies, Chernoff's inequality, using
t=a/(128 B^2+8Ba), gives for every a>0

    P(|n^(-1) sum D_{h,j}| >= a)
       <= 2 exp(-n a^2/(256 B^2+16Ba)).                 (8)

Here t lies in (0,1/(8B)); substitution into the preceding exponent gives
exactly -n a^2/(2(128 B^2+8Ba)). Apply the same argument to -D_h
for the lower tail.

A maximal set of points on the unit sphere of H separated by more than
1/4 is a 1/4-net N. Disjoint balls of radius 1/8 about its points lie
in the ball of radius 9/8; comparison of volumes gives |N|<=9^m.
For any symmetric matrix E on H, take a unit eigenvector x with
|<x,Ex>|=||E||_op and h in N with ||x-h||<=1/4. Then

    |<x,Ex>-<h,Eh>| <= 2||E||_op ||x-h|| <= ||E||_op/2,

so ||E||_op <= 2 max_{h in N}|<h,Eh>|.

Use (8) with a=epsilon rho_K/8. Since p_K<=1, mu<1,
0<rho_K<1, and epsilon<=1/2, we have B>1 and a<=B. Hence
256 B^2+16Ba <=272 B^2. A union bound over N gives

    P(||M_hat-M_B||_op > epsilon rho_K/4)
       <= 2 exp(m log(9)-n epsilon^2 rho_K^2/(17408 B^2)).

Condition (3), with 32768>=17408, makes this at most delta.
Combining with (7), the event of probability at least 1-delta satisfies

    ||M_hat-M||_op <= eta := epsilon rho_K/2.            (9)

## 5. Recovery from the eigengap

Put r=K-1 and rho=rho_K. The matrix M=-rho P_V has r eigenvalues
-rho. The min-max principle and (9) imply that each of the r smallest
eigenvalues of M_hat is at most -rho+eta. If r<m, the remaining
eigenvalues are at least -eta, again by the min-max principle. Since
eta<=rho/4, these groups are separated. If r=m, H itself is the
desired subspace and recovery is automatic.

Let U_hat have orthonormal columns spanning the selected eigenspace,
and let Lambda be its diagonal eigenvalue matrix. Then

    M_hat U_hat = U_hat Lambda,
    (I_d-P_V) U_hat Lambda
       = (I_d-P_V)(M_hat-M) U_hat.

All selected eigenvalues have absolute value at least rho-eta. Multiplying
on the right by Lambda^(-1) yields

    ||(I_d-P_V) U_hat||_op <= eta/(rho-eta)
                         = epsilon/(2-epsilon) <= epsilon.

The same norm is ||(I_d-P_V)P_hat||_op, proving the first part of (4).
The squared Frobenius norm is at most r epsilon^2. Since

    tr(P_V P_hat) = r-||(I_d-P_V)U_hat||_F^2,

the second part follows. Equation (2) then turns (3) into the stated
asymptotic sample bound, uniformly for all odd K>=3 after enlarging an
absolute constant to cover finitely many K.

## 6. Exact variance and scope

The untruncated scalar statistic in any unit direction h perpendicular
to u has second moment

    E[(Y S ((<h,X>)^2-1))^2]
       = E[S^2] E[(g^2-1)^2] = 2.

Its mean is -rho_K ||P_V h||^2, so its variance is
2-rho_K^2 ||P_V h||^4. In a contrast direction the squared signal is
rho_K^2, of order K^(-2). This identity is a variance calculation for
this statistic, not a lower bound for algorithms using other statistics.

The exact identities require orthonormality. The first estimation theorem
assumes a known u; Section 7 supplies a quantitative perturbation argument
for estimating u. No perturbation bound for a nonidentity teacher Gram
matrix is claimed. No Bayes specialization threshold, AMP threshold, or
general low-degree bound is deduced from (1)–(4).

## 7. Removing the aggregate-direction oracle by sample splitting

The following corollary uses the same orthonormal teacher model, with no
teacher direction revealed. It recovers the contrast subspace V defined
above. Let 0<epsilon<=1/2 and 0<delta<1, write rho=rho_K and
b=mu p_K sqrt(K), and take two independent batches of sizes n_1,n_2.

From the first batch compute

    m_hat = n_1^(-1) sum_a Y_a X_a,    v=m_hat/||m_hat||.

If m_hat=0, set v to any fixed unit vector. Define

    B_* = sqrt(2 log(32/(epsilon rho))),
    P_v = I_d-vv^T,
    N_hat = n_2^(-1) sum_a Y_a <v,X_a> 1{|<v,X_a>|<=B_*}
                         ((P_v X_a)(P_v X_a)^T-P_v),

where this sum uses only the second batch. Let P_* project onto the
K-1 smallest-eigenvalue eigenvectors of N_hat in R^d. If

    n_1 >= 19200 d/(delta b^2 epsilon^2 rho^2),           (10)
    n_2 >= 131072 B_*^2/(epsilon^2 rho^2)
                      ((d-1) log(9)+log(4/delta)),       (11)

then, with probability at least 1-delta,

    ||(I_d-P_V) P_*||_op <= epsilon,
    tr(P_V P_*)/(K-1) >= 1-epsilon^2.                   (12)

In particular, for any fixed epsilon,delta, the total sample size is
O(K^2 d log K). The estimator consists of a sample mean, a sample matrix,
and an eigendecomposition, and runs in polynomial time. It still does
not identify individual hidden units or prove a threshold lower bound.

To prove the perturbation bound, use the tensor in Section 2 and let C(a)
denote its contraction with an arbitrary vector a. For unit h,

    <h,C(a)h>
      = E[Y((<a,X>)((<h,X>)^2-1)-2<a,h><h,X>)].

Write a=t h+a_perp. With g=<h,X> and z=<a_perp,X>, the polynomial
inside this expectation is

    t(g^3-3g)+z(g^2-1).

The variables g and z are independent centered Gaussians, with variances
1 and ||a_perp||^2. The squared L^2 norm of this polynomial is

    6t^2+2||a_perp||^2 <= 6||a||^2.

Here E[(g^3-3g)^2]=15-18+9=6 and E[(g^2-1)^2]=2;
the cross term vanishes because E z=0. Cauchy–Schwarz and Y^2=1 give

    ||C(a)||_op <= sqrt(6)||a||,
    ||C(v)-C(u)||_op <= sqrt(6)||v-u||.                 (13)

For unit a put

    N(a)=E[Y<a,X>((P_a X)(P_a X)^T-P_a)]
        =P_a C(a) P_a,    P_a=I_d-aa^T.

The equality follows from the tensor formula: the two linear correction
terms vanish after projection by P_a. If eta=||v-u||, then
||P_v-P_0||_op<=2eta, by expanding vv^T-uu^T. Using (13) and
adding and subtracting P_v C(u)P_v gives

    ||N(v)-N(u)||_op
      <= sqrt(6)eta+2 sqrt(6)||P_v-P_0||_op
      <= 5 sqrt(6)eta.                                 (14)

By (1), E m_hat=bu. Also ||YX||^2=||X||^2, so independence of the
first batch gives

    E||m_hat-bu||^2 = (d-b^2)/n_1 <= d/n_1.

Set eta_0=epsilon rho/(20 sqrt(6)). Markov's inequality and (10) imply

    P(||m_hat-bu|| > b eta_0/2)
      <= 4d/(n_1 b^2 eta_0^2) <= delta/2.

On the complementary event m_hat is nonzero. The elementary inequality

    ||m_hat/||m_hat||-u|| <= 2||m_hat-bu||/b

follows by adding and subtracting m_hat/b and using the reverse triangle
inequality. Thus ||v-u||<=eta_0 and (14) gives

    ||N(v)-M||_op <= epsilon rho/4.                     (15)

Condition on the first batch. The vector v is now deterministic and the
second batch is independent. The concentration argument in Section 4
uses only that X is standard Gaussian, |Y|=1, and the projection is
orthogonal to its unit contraction vector. Thus it applies with v in
place of u, epsilon/2 in place of epsilon, and delta/2 in place of
delta, without requiring N(v) itself to be a multiple of a projector.
The chosen B_* and (11) consequently imply

    P(||N_hat-N(v)||_op > epsilon rho/4 | first batch)
      <= delta/2.                                     (16)

The matrices in this difference vanish on v, so the concentration on
v^perp also bounds their ambient operator norm. Combining (15), (16)
and the union bound gives ||N_hat-M||_op<=epsilon rho/2 with probability
at least 1-delta. The argument in Section 5 now applies in R^d to
M=-rho P_V and proves (12). Finally b -> 2/pi and K rho ->
(2/pi)(1-2/pi), proving the stated fixed-confidence sample bound.
