# HARD7-05 route note — edge-smoothed AR comparator and Gaussian Volterra reduction

New-method route recorded before building the exact finite checker.

The previous checkpoint compared the sampled `H=1/4` Lamperti process directly to an AR(1) covariance `rho^k`. That is wasteful: matching the relatively large one-step source covariance forces every later comparator covariance to stay unnecessarily large.

Use instead a latent stationary AR(1) chain `U_j` with correlation parameter `r`, and define

`Y_j=(U_j+U_{j-1})/sqrt(2(1+r))`.

Then

`Cov(Y_0,Y_k)=((1+r)/2) r^(k-1),  k>=1`.

For the source grid `q=exp(-Delta/4)`, take `q=r=4/5`. The comparator covariances are `C_1=9/10`, `C_2=18/25`, and `C_k=(9/10)(4/5)^(k-1)` thereafter. The inherited exact source covariance formula can test lags 1 and 2 directly. Since `q^3=64/125<r0=287831/500000`, every lag `k>=3` lies in the already certified cone `R(q^k)<=q^k`, while `C_k/q^k=9/8`. Thus only two new exact inequalities are needed for an all-lag Slepian comparison.

The persistence problem for this comparator has a second representation. Let

`(T_r f)(x)=int_{y<-x} k_r(x,y) f(y) phi(dy)`

with `k_r` the Mehler kernel relative to standard Gaussian measure. Reflect `y=-v` and define the triangular Gaussian operator

`(A_a g)(x)=int_{v>x} k_a(x,v) g(v) phi(dv)`.

Then `T_r=A_{-r} R`, where `R g(v)=g(-v)`, and reflection gives `R A_{-r} R=A_{-r}^*`. Hence

`T_r^2=A_{-r} A_{-r}^*`,

so the comparator persistence eigenvalue is exactly the singular norm `lambda_edge(r)=||A_{-r}||` once positivity of `T_r^2` identifies the Perron root. At `r=0`, the Gaussian quantile map `u=Phi(x)` sends `A_0` to the classical Volterra operator `g -> int_u^1 g(v)dv`, whose norm is exactly `2/pi`. This deforms the comparator into a weighted/Gaussian Volterra norm problem instead of another killed-halfline AR eigenproblem.

A second exact route comes from even trace powers. For `n>=2`,

`tr(T_r^n)=(1-r^n)^(-1) P_loop(X_i+X_{i+1}<0 for every i mod n)`,

where the normalized Gaussian loop has cyclic covariance

`C_d=(r^d+r^(n-d))/(1-r^n)`.

For `n=8`, `r=4/5`, this reduces the next useful norm upper bound to one explicit seven-dimensional Gaussian cone probability (the eight edge sums have one alternating linear dependence). A rigorous upper certificate for that finite cone could move the frozen source bracket without discretizing the original continuous path.

Section-B routes for this run:

- **B6 (deform to a solvable point):** deform the edge comparator to `r=0`, where it is exactly the Volterra operator with norm `2/pi`.
- **B21 (ask who else has this shape):** identify the persistence transfer operator with a Gaussian-copula deformation of a triangular Volterra operator rather than a standard killed AR operator.
- **B29 (add points at infinity):** test positive Schur weights for the triangular operator. A one-parameter exponential/quadratic weight makes the tail supremum finite but remains too loose to improve the current source bound; this failure points to either a richer subinvariant weight or an even-trace cone certificate.

No numerical spectral estimate in this route note is a theorem or a source-metric movement. The next finite checker will certify only the two new covariance inequalities and the exact `n=8` loop covariance algebra.