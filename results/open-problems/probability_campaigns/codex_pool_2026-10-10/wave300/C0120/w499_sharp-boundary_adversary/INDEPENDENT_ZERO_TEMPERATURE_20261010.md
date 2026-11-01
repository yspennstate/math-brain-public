# Independent extension to the ground-state functional

This derivation is saved before reading w498's proof. For a nonempty deterministic finite path family P, with each p choosing exactly one site p_t from each finite time layer V_t, let omega(t,x) be independent N(0,1) and c(p) be deterministic real offsets. Define L=max_{p in P}(c(p)+sum_t omega(t,p_t)). Put m_t=|V_t|, M_t=m_t^{-1} sum_{x in V_t} omega(t,x), and eta(t,x)=omega(t,x)-M_t.

The vectors (M_t)_t and (eta(t,x))_{t,x} are independent: their cross-covariances vanish, and they are jointly Gaussian. The M_t are mutually independent with Var(M_t)=1/m_t. Since every p takes one site in every layer,

L(omega)=sum_t M_t+L(eta).

L and L(eta) have finite second moments because they are maxima of finitely many Gaussian linear forms plus finite deterministic offsets. Independence gives the exact identity

Var L=sum_t 1/m_t+Var L(eta) >= sum_t 1/m_t.

For normalized positive-temperature free energy F_beta=beta^{-1}log(sum_p a(p) exp(beta sum_t omega(t,p_t))), deterministic a(p)>=0 not all zero and fixed beta>0, the same variance identity holds with F_beta in place of L. For unnormalized log Z the floor is beta^2 sum_t 1/m_t. Changing normalizations must preserve this beta^2 factor.

On a strip with m_t<=W this gives Var L>=n/W. Consequently no C n^(1-epsilon), with C finite and epsilon>0 fixed independent of n, holds uniformly on a fixed-width strip. If the width W_n varies with n, that bound requires W_n>=(1/C)n^epsilon; this is only necessary, not sufficient.

For a one-dimensional nearest-neighbor walk from the origin, the reachable sites at time t are {-t,-t+2,...,t}, hence m_t=t+1. With visited weighted layers t=0,...,n-1 the floor is H_n; with t=1,...,n it is H_{n+1}-1. The precise source convention remains to be checked. These logarithmic lower bounds are compatible with every conjectured n^(1-epsilon) upper bound for 0<epsilon<1 and do not solve or refute the parent problem.

Single hardest open piece: control the variance of the residual functional on the full lattice by a power of n below one. The common-mode decomposition gives no such upper bound.

Status: author proof / referee w500 pending; current openness and novelty UNKNOWN.
NEXT: check the 2008 path and energy convention; audit w498's exact bridge on its stated domain.
