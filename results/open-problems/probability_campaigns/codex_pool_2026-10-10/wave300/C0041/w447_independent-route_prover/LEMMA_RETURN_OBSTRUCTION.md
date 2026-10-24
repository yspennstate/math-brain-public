# First exit and total occupation remain different under the full target assumptions

Claim GO (proved special-case obstruction by w447; awaiting review).

Fix 0<kappa<1/4. On Z^2 consider the homogeneous kernel

p(+e_1)=1/4+delta, p(-e_1)=1/4-delta,
p(+e_2)=p(-e_2)=1/4,

where 0<delta<=1/4-kappa. Its environment law is a Dirac mass at that row at each site, hence is spatially iid and kappa-uniformly elliptic. Its increments are iid. The strong law gives X_n/n -> (2delta,0), so it is directionally transient and ballistic in e_1. Nevertheless

sup_{0<delta<=1/4-kappa} E_0[sum_{n>=0} 1_{X_n=0}] = infinity,

while first exit from the singleton {0} takes exactly one step for every delta. Thus no law-independent upper bound for total occupation can follow from kappa, dimension, directional transience and the singleton residence bound alone. Every individual law in this example has finite Green function: it is not a counterexample to C0041 or to finiteness under a fixed iid law.

Proof of the divergence with explicit constants. At delta=0 the transformed coordinates Y=X^(1)+X^(2), Z=X^(1)-X^(2) are independent simple symmetric walks. Consequently

P_0(X_{2n}=0) = [binom(2n,n)/4^n]^2 >= 1/(4n), n>=1.

The elementary central-binomial lower bound binom(2n,n)>=4^n/(2sqrt(n)) follows by induction from n=1, since

binom(2n+2,n+1)/binom(2n,n)=4(1-1/(2n+2))
and (1-1/(2n+2))^2 >= n/(n+1).

Every path of length 2n under p_delta has probability at least (1-4delta)^(2n) times its p_0 probability. If delta<=1/(16N) and n<=N, Bernoulli's inequality gives (1-4delta)^(2n)>=1-8delta n>=1/2. Therefore its Green function is at least

1 + (1/8) sum_{n=1}^N 1/n.

Choose delta_N=min((1/4-kappa)/2,1/(16N)); these are positive, preserve the same ellipticity lower bound, and give the divergent harmonic lower bound.

Proof of finiteness for fixed delta. For theta=(1/2)log((1/4+delta)/(1/4-delta))>0,

P_delta(X_n=0) <= E_delta exp(-theta X_n^(1))
 = [1/2+2sqrt(1/16-delta^2)]^n.

The base is strictly below one, so the Green series is finite. The obstruction is to a uniform or purely local inference, not to each law separately.

Source: owner campaign derivation, w447, 2026-10-10. Original self-contained proof, no novelty asserted.
