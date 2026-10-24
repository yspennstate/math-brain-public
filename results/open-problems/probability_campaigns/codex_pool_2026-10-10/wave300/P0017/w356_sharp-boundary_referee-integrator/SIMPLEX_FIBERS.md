# An exact isotropic-simplex obstruction to a pointwise fiber bridge

Status: proved special case by w356; independent review requested from w359, pending. This is a counterexample to a stronger auxiliary statement, not a refutation of KLS and not a novelty claim.

## Statement

For every integer n >= 2 there is a full-dimensional, centered, isotropic, uniform convex-body measure mu_n on R^n and a unit vector u such that its regular conditional laws on lines parallel to u obey

    ess sup_z C_P(mu_n(. | P_{u-perp}Y=z)) = 2(n+1)(n+2)/pi^2,
    E_z C_P(mu_n(. | P_{u-perp}Y=z)) = 12/pi^2.

Here C_P(nu) is the least coefficient in Var_nu(g) <= C_P(nu) integral |g'|^2 dnu for all Sobolev functions on the line, with derivative in Euclidean arclength. The essential supremum uses the projected probability law, so the obstruction does not depend on assigning a conditional law to a null fiber. Conditional covariance is measured in the inherited Euclidean metric; the fibers are not individually rescaled to variance one.

Consequently ambient isotropy and log-concavity do not imply a dimension-free bound on almost every fiber's Poincare constant. The averaged calculation is a fact about this example only; it is not a general averaged-fiber theorem or a bound for arbitrary gradient weights.

## Derivation

Let X be uniform on S_n={x in R^n: x_i >= 0 and sum_i x_i <= 1}. Introduce barycentric coordinate X_0=1-sum_i X_i. The vector (X_0,...,X_n) is Dirichlet(1,...,1). Direct simplex integration gives

    E X_i = 1/(n+1),
    Cov(X) = [(n+1)I - J]/[(n+1)^2(n+2)] =: Sigma,
    Sigma^{-1} = (n+1)(n+2)(I+J),

where J has every entry equal to one. Put a=(n+1)(n+2), m=E X, A=Sigma^{-1/2}, Y=A(X-m), and u=A e_1/sqrt(2a). Then A is symmetric, A^2=a(I+J), |A e_1|^2=2a, E Y=0 and Cov(Y)=I. Uniform measure on A(S_n-m) is log-concave.

The map x -> P_{u-perp}A(x-m) has kernel span(e_1). It is therefore a bijection between base coordinates (x_2,...,x_n) and projected fibers. For any base point with s=sum_{i=2}^n x_i < 1, conditioning leaves X_1 uniform on [0,T] where T=1-s=X_0+X_1. The coarea Jacobian is constant because the map is linear, so conditioning is uniform in the line's Euclidean arclength too.

In particular

    <u,Y> = sqrt(a/2) (2 X_1 + s - 1).

It is conditionally uniform on [-sqrt(a/2)T, sqrt(a/2)T], a centered interval of length L=sqrt(2a)T. Hence

    Var(<u,Y> | base) = a T^2/6,
    C_P(fiber) = L^2/pi^2 = 2a T^2/pi^2.

The last equality follows from the Neumann Wirtinger inequality on an interval; its first nonconstant cosine eigenfunction attains the bound. A separate proof is supplied below.

Since (X_0,...,X_n) is Dirichlet, T=X_0+X_1 has Beta(2,n-1) density n(n-1)t(1-t)^(n-2) for 0<t<1. Its second moment is

    E T^2 = 6/[(n+1)(n+2)] = 6/a.

This proves the stated averaged constant and E Var(<u,Y>|base)=1. For every 0<epsilon<1, P(T>1-epsilon)>0 by the displayed density. Thus ess sup T^2=1, proving the essential supremum formula on sets of positive projected measure.

For reference, P(T>q)=(1-q)^(n-1)[1+(n-1)q] for 0<q<1. Large fibers can be rare without being null.

## The interval constant, independently derived

On an interval [0,L] with uniform probability, reflect a mean-zero H^1 function evenly across both endpoints to a 2L-periodic H^1 function. Its Fourier frequencies are k*pi/L, k>=1. Parseval gives integral |g'|^2 >= (pi/L)^2 integral |g|^2. Dividing by L yields C_P <= L^2/pi^2. For g(x)=cos(pi*x/L), both integrals have the ratio L^2/pi^2, so equality holds. Translation gives the same conclusion on centered intervals.

## Exact scope of the failure

DROP the bridge: there exists a universal B such that for every isotropic log-concave mu, every unit direction u, and almost every projected z, C_P(mu on z+Ru) <= B. The simplex family forces B to grow at least as 2(n+1)(n+2)/pi^2.

KEEP the scale-correct one-dimensional conclusion: C_P(fiber)=(12/pi^2) Var(fiber) for these uniform intervals. Their covariance is not bounded by ambient covariance on each fiber, though its expectation equals one here.

No conditional probabilities are multiplied. No conclusion about a high-dimensional global gap follows merely from averaging the fiber constants. The uncontrolled dependence of a general gradient on the base, and the variance of conditional means for a general function, remain gaps in any such bridge to global Poincare.

## An explicit failure of pulling the average constant outside the energy

There is also a concrete Lipschitz test function, without a discontinuous base indicator. For an integer k >= 1 put

    f_k(Y) = T^k cos(pi X_1/T),    T=1-sum_{i=2}^n X_i,

with f_k=0 at T=0. On the simplex its partial derivatives are bounded by constants times T^(k-1), since 0<=X_1<=T; thus it is Lipschitz on the convex body. A Lipschitz extension to R^n is allowed. Each conditional mean is zero. Since A^{-1}u=e_1/sqrt(2a) and T is constant along a fiber,

    E Var(f_k | Z) = (1/2) E T^(2k),
    E |partial_u f_k|^2 = [pi^2/(4a)] E T^(2k-2),
    R(n,k) := E Var(f_k | Z) / E |partial_u f_k|^2
            = [2a/pi^2] [(2k)(2k+1)/((n+2k-1)(n+2k))].

The moment formula used here is E T^r=(r+1)! n!/(n+r)!, which follows by the same beta integral. For k=1, R=12/pi^2. For each n>=2 and k>1, R>12/pi^2; as k tends to infinity it tends to 2a/pi^2.

Therefore the purported averaging step

    E Var(f | Z) <= (E C_P(fiber)) E |partial_u f|^2

is false even for these globally Lipschitz functions and this isotropic log-concave measure. At n=100 and k=10, R/(12/pi^2)=101/2=50.5 exactly. The valid slice-by-slice inequality keeps C_P(fiber) *inside* the expectation, multiplied by that fiber's directional energy. This calculation concerns the directional energy only; the transverse part of the full gradient is essential and has not been discarded in any claimed KLS conclusion.
