# P0017: independent boundary derivation

2026-10-10, w355. Sections 1-5 were saved before reading any paired w354 proof. Referee w356 subsequently independently kept C001 and C002; exact verdicts are preserved in REFEREE_VERDICTS.jsonl. No novelty or full-KLS proof claim.

## 1. Exact target and scope

For all dimensions and all centered isotropic log-concave probability measures, seek a universal upper bound on C_P in Var(f) <= C_P integral |grad f|^2. This is the precise primary formulation in [Bizeul--Klartag--Lehec, Theorem 1.1 and equations (5)-(6)](https://arxiv.org/html/2610.05474v1). Their October 4 preprint claims the full result; the September ranking does not certify current openness. Full proof validity is outside this boundary derivation. For arbitrary covariance, the bound scales with its operator norm.

The auxiliary bridge tested here is stronger: global isotropy is alleged to give a universal almost-everywhere bound on the Poincare constant, or covariance operator norm, of one-dimensional orthogonal conditional slices. That bridge is false. This does not refute P0017 or the October paper.

## 2. Isotropic regular simplex, with normalization checked explicitly

Fix n >= 2. Let H={x in R^(n+1): sum_i x_i=0}, with its induced Euclidean metric (so H is isometric to R^n). Put a=sqrt((n+1)(n+2)), m=(1/(n+1),...,1/(n+1)), and v_i=a(e_i-m), i=0,...,n. Let X be uniform on K=conv{v_0,...,v_n}. This is a full-dimensional log-concave measure on H. Write X=a(lambda-m), where lambda is uniform on {lambda_i>=0, sum lambda_i=1}, equivalently Dirichlet(1,...,1).

The simplex moment identity, proved by iterated integration of monomials, is
E product_i lambda_i^(k_i) = n! product_i k_i! / (n+sum_i k_i)!
for nonnegative integers k_i. In particular E lambda_i=1/(n+1) and E lambda_i lambda_j=(1+1_{i=j})/((n+1)(n+2)). Therefore E X=0 and E XX^T=I-J/(n+1), the orthogonal projector onto H. Restricted to H the covariance is the identity. Every edge has squared length L^2=2(n+1)(n+2).

## 3. Disintegration into edge-parallel fibers

Take u=(e_0-e_1)/sqrt(2), T=<X,u>=a(lambda_0-lambda_1)/sqrt(2), and Y=X-Tu. The projected vertices v_0 and v_1 coincide; the other n-1 projected vertices and this common projection are affinely independent in H intersect u-perp. Thus Y determines lambda_2,...,lambda_n and S=lambda_0+lambda_1=1-sum_{i=2}^n lambda_i. S is an affine function of Y.

For almost every Y with S=s>0, the conditional law of T is uniform on [-Ls/2,Ls/2]. Indeed the original density is constant, the projection/coarea Jacobian is constant, and lambda_0 ranges uniformly over [0,s] with lambda_1=s-lambda_0. Integrating the remaining simplex coordinates gives S density n(n-1)s(1-s)^(n-2), 0<s<1 (Beta(2,n-1)). In particular for 0<delta<1,
P(S>1-delta)=delta^(n-1)[n-(n-1)delta]>0.
No assertion depends on a boundary slice of zero marginal probability.

## 4. Exact conditional constants and the quantifier obstruction

A uniform interval of length ell has variance ell^2/12 and Poincare constant ell^2/pi^2. The latter follows from the Neumann Fourier expansion: on a centered interval the first nonconstant mode is sin(pi t/ell), with eigenvalue pi^2/ell^2, and every higher mode has a larger eigenvalue. Its Cheeger constant in the boundary/min(mass,1-mass) convention is 2/ell: a midpoint cut attains it, while a one-dimensional set of mass at most 1/2 must pay at least one boundary point of density 1/ell.

Consequently
Var(T|Y)=((n+1)(n+2)/6)S^2,
C_P(T|Y)=(2(n+1)(n+2)/pi^2)S^2,
h(T|Y)=2/(LS).
Their exact extremes are
ess sup Var(T|Y)=(n+1)(n+2)/6,
ess sup C_P(T|Y)=2(n+1)(n+2)/pi^2,
ess inf h(T|Y)=sqrt(2/((n+1)(n+2))).
For fixed delta the same orders hold on S>1-delta, a set of strictly positive marginal probability. Thus global isotropy cannot imply a dimension-free bound on all conditional variances or Poincare constants, nor a universal positive lower bound on all conditional Cheeger constants.

Yet E S^2=6/((n+1)(n+2)), so
E Var(T|Y)=1 and E C_P(T|Y)=12/pi^2.
Also E[T|Y]=0. The law of total variance is exactly satisfied. Each individual fiber obeys the dimension-free covariance-scaled identity C_P=(12/pi^2)Var; the missing premise is control of the conditional covariance in the original metric, not failure of the one-dimensional inequality.

## 5. Averaging the constants alone does not fix the bridge

An averaged conditional constant cannot simply be multiplied by an unrelated averaged directional energy. Let 0<b<1, phi(s)=(s-b)_+^2, and f(X)=T phi(S). The function is continuously differentiable on K; S is affine and constant in direction u. Therefore E[f|Y]=0, partial_u f=phi(S), and
E Var(f|Y)/E |partial_u f|^2
=((n+1)(n+2)/6) E[S^2 phi(S)^2]/E[phi(S)^2]
> ((n+1)(n+2)/6)b^2.
The denominator is positive because P(S>b)>0. For b=1/2 this ratio exceeds (n+1)(n+2)/24, while E C_P(T|Y)=12/pi^2 is independent of n. Hence even an integrated conditional-variance inequality with universal C and ONLY directional-u energy is false. Transverse derivatives of phi(S) belong to the full gradient and are deliberately absent from this auxiliary bridge; this example makes no assertion that the full Poincare inequality fails.

The valid slice inequality retains its weight:
E Var(f|Y) <= E[C_P(T|Y) E(|partial_u f|^2|Y)].
To recover a universal bound on the right, a proposed proof must control this weighted integral for every f, and must separately bound Var(E[f|Y]) with the transverse energy and any derivative-of-conditioning terms. Neither E C_P=O(1) nor E conditional covariance <= I justifies factorization or an essential-supremum bound.

Verification completed: 5,898 exact checks passed, and w356 independently checked both special-case proofs. W354_AUDIT.md records the completed paired-proof audit.

NEXT: Retain the conditional constant inside its energy-weighted integral when considering a full-gradient continuation; merge the checked boundary into the triad packet.
