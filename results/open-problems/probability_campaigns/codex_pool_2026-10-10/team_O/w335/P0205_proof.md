# P0205: an exact complete-Cayley family

Label: proof of a special family, pending independent w347 audit. This is not a claim that every question in the original source is solved.

Let G be any group of order n >= 2, e its identity, and 0 < alpha <= 1. Let P(x,x)=1-alpha and P(x,y)=alpha/(n-1) for y != x. Let T be independent with P(T=k)=p(1-p)^k for k >= 0, where 0 < p < 1. Start P at e. Write u for the uniform law, b=1-alpha*n/(n-1), and a=p/(1-(1-p)*b). The geometric-time target is mu=u+a*(delta_e-u). In particular mu(e)=(1+(n-1)*a)/n and mu(y)=(1-a)/n for y != e.

Form the ordinary Metropolis kernel M using P as proposal and target mu. With tau(K)=1/(1-lambda_2(K)), its exact relaxation time is

    tau(M) = (n-1)/(alpha*n) * (1+(n-1)*a)
           = tau(P) * (1+(n-1)*p/(1-(1-p)*b)).

Proof. P acts as the scalar b on the space orthogonal to constants. Summing p*sum_k (1-p)^k P^k gives the displayed target. Every proposal from a nonidentity state is accepted. From e to any other state, its probability is alpha/(n-1) times r=(1-a)/(1+(n-1)*a). Thus the two-state radial lump has rates alpha*r and alpha/(n-1), and nonconstant eigenvalue 1-alpha*r-alpha/(n-1). The n-2 contrasts between nonidentity states have eigenvalue b. Since 0<a<1 and r<1, the radial eigenvalue is at least b and is lambda_2. Its gap is alpha*(r+1/(n-1))=alpha*n/((n-1)*(1+(n-1)*a)). Inversion proves the formula, including n=2 where the contrast subspace is empty.

Consequences. Since da/dp=(1-b)/(1-b+b*p)^2>0, tau(M) is strictly increasing in the stopping parameter p. Equivalently it is strictly decreasing as the mean geometric time (1-p)/p increases; these are different parametrisations. If alpha=1/2, P and M are lazy, and the spectral-gap and absolute-gap conventions agree. For fixed alpha,p, the ratio tau(M)/tau(P) diverges linearly in n, with ratio/n -> p/(alpha+(1-alpha)*p). In particular alpha=p=1/2 gives ratio/n -> 2/3. This refutes a bound on this ratio depending only on p and the base relaxation time, with no restriction on group order or proposal degree. Degree grows as n-1; this calculation does not settle a fixed-degree variant.

Prior source quoted: the existing attempt card says "The literal monotonicity direction is refuted under the standard spectral-gap relaxation convention" and covers n=2. The present calculation generalises that family to all n and keeps the geometric convention explicit.

Checks to run: geometric resolvent equation, stochastic rows, detailed balance, radial and contrast eigenvectors, ordering of eigenvalues, positive derivative, and the lazy large-n ratio. The checks use exact rational arithmetic where possible.
