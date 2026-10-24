# A closed-walk proof for Stieltjes odds matrices

Root creative derivation, 15 September 2026. This is supporting research, not one of the 100 worker assignments. The theorem is a restricted result; no historical priority is claimed.

## Statement

Let L be a real symmetric positive definite matrix with nonpositive off-diagonal entries (a Stieltjes matrix). Set f(S)=-log det L_S, with det L_empty=1. For every Hermitian positive contraction K, the canonical exterior Hessian of F_f(K)=E_K f(X) is positive semidefinite. In particular

q_f(K;u,v)=D²F_f(K)[uu*,vv*]>=0

for arbitrary complex u,v. The same statement holds if a diagonal unitary conjugation turns L into a Stieltjes matrix.

Consequently, at every strict marginal kernel K whose odds L=K(I-K)^(-1) is of this form, the actual Shannon entropy Hessian is nonpositive in every direction with at most one positive and one negative eigenvalue. The statement does not cover arbitrary higher-rank directions or arbitrary odds matrices.

## Closed-walk expansion

Write D=diag(L_ii)>0 and L=D^(1/2)(I-C)D^(1/2), where C is real symmetric, entrywise nonnegative and has zero diagonal. Positive definiteness gives lambda_max(C)<1. For every real vector z, |z^T C z|<=|z|^T C |z|<=lambda_max(C)||z||². Thus the spectral radius rho(C)=lambda_max(C)<1. The same bound holds on every principal submatrix.

It follows from the scalar logarithm series on the eigenvalues that

f(S)=-sum_{i in S}log D_ii + sum_{k>=1} tr(C_S^k)/k.

Every summand in tr(C_S^k) is the nonnegative weight of a closed walk of length k whose visited vertices belong to S. Group the walks by their exact nonempty visited set T. This gives

f(S)=-sum_{i in S}log D_ii + sum_{T subset S, |T|>=2} w_T,

where

w_T=sum_{k>=2} (1/k) sum_{closed walks of length k with visited set exactly T} product of their edge weights >=0.

The series is finite in total mass: sum_T w_T=sum_{k>=1} tr(C^k)/k=-log det(I-C)<infinity. This also follows from absolute convergence of the matrix logarithm series. There are only finitely many sets T, so regrouping is legitimate. Singleton weights vanish because C has zero diagonal.

The DPP inclusion identity now yields the exact finite representation

F_f(K)=-sum_i K_ii log D_ii + sum_{|T|>=2} w_T det K_T.

The first term is affine. Each coefficient of a principal determinant is nonnegative.

## Positivity of the exterior Hessian

For strict positive K_T, differentiation in rank-one directions gives

D²det K_T[uu*,vv*]=det K_T [(u_T* K_T^(-1) u_T)(v_T* K_T^(-1) v_T)-|u_T* K_T^(-1) v_T|²]>=0.

More strongly, its canonical exterior operator is the embedding of det(K_T) wedge²(K_T^(-1)), which is positive semidefinite. This is the determinant-cofactor operator identity, not an inference from tests on real decomposable forms. For singular positive semidefinite K_T, take a positive definite approximation and use polynomial continuity of the cofactors. Thus every summand has positive semidefinite canonical exterior Hessian, and so does their nonnegative finite combination. This proves the stated theorem, including boundary K.

Diagonal unitary conjugation does not change any principal determinant of L, hence it does not change f. The gauge extension follows.

## Entropy consequence and limitation

At a strict physical base K, freeze f(S)=-log p_S(K). This differs from -log det L_S by a constant, which has zero Hessian under expectation. For A=alpha uu* - beta vv*, alpha,beta>=0, rank-one affinity of every DPP atom gives

D²H(K)[A,A] = -sum_S (Dp_S(K)[A])²/p_S(K) - 2 alpha beta q_f(K;u,v) <=0.

This applies in every finite dimension. If an affine segment has rank-two indefinite direction and every interior odds matrix satisfies the theorem's hypothesis, entropy is concave along that segment by integration; endpoint limits follow from continuity when available.

The proof supplies a different sufficient class from C005's signed-rank-one odds formula. It fails for general complex L because closed-walk products can have negative real contributions, and a positive definite matrix need not have a nonnegative normalized closed-walk expansion. No step here proves full exterior positivity for arbitrary log-determinant weights, nor the full Lyons conjecture.
