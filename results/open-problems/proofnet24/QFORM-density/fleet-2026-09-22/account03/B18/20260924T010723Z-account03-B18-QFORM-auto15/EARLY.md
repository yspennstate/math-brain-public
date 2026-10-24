SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-24T01:07:23Z.
attacking: Rudelson--Vershynin stable-rank small-ball transfer to a negative-moment cross-bank density bound, with a diffuse third spectral direction.

# Early calculation

Let X,Y be independent original-coordinate product banks with one-dimensional densities at most one, let M be a nonzero real matrix, let alpha be deterministic, and set Z=||MY+alpha||_2. Rudelson--Vershynin, *Small ball probabilities for linear images of high dimensional distributions* (IMRN 2015; arXiv:1402.4492), Corollary 8.6, gives for

r=floor(||M||_HS^2/||M||_op^2)

and every tau>0,

P(Z <= tau ||M||_op) <= (C_RV tau)^r,

where C_RV is the absolute constant in that corollary. Hence, if r>=2,

P(Z<=t) <= min(1,(C_RV t/||M||_op)^r).

With t0=||M||_op/C_RV, layer cake gives

E Z^{-1}
 = integral_0^infinity P(Z<=t) t^{-2} dt
 <= C_RV/((r-1)||M||_op)+C_RV/||M||_op
 = [C_RV r/(r-1)] ||M||_op^{-1}.

For fixed Y=y, Theorem 1.2 of the same paper gives the conditional scalar-linear density cap sqrt(2)/||My+alpha||_2. Therefore the candidate receiver is

||p_{X^T M Y+alpha^T X+G(Y)}||_infinity
 <= sqrt(2) C_RV [r/(r-1)] ||M||_op^{-1}.

This uses no moments, support, iid, log-concavity or projected-coordinate independence. The remaining work in this run is to formalize the ambient quadratic lift, stress it on a target-valid diffuse-third-direction family, and splice the designated account04/B18 theorem at an actual inequality.
