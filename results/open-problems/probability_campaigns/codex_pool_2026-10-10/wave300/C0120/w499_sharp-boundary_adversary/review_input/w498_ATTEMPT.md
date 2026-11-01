# C0120 sharp-boundary attempt

The exact source model and operational target are in STATEMENT.md. Current openness and novelty are UNKNOWN.

## Prior-attempt digest

The intake's C0120-A001 (attempts.jsonl:98) proposes obtaining a power variance gain from quantitative chaos and mentions the KPZ scaling relation under existence of suitable exponents. It supplies no new quantitative overlap estimate or independent proof. Its log Z_n and general-dimension wording does not match the ground-state quantity in the cited Chatterjee source. Named H/I and Lean records had no direct C0120 match in a targeted search; no absence-of-prior-work claim follows. Team O's board has no C0120 row. We do not transfer its other lanes.

The scar perceptron_proof_open_gaps_fleet_2026_07_12 warns that a passing pipeline and a proved sublemma can coexist with open proof gaps. Here the single hardest gap remains an upper bound for the centered, unrestricted planar maximum's variance at a polynomial scale.

## L1. Exact Gaussian layer-average decomposition

Take a finite nonempty deterministic path family visiting exactly one site of every layer t. Layer t has m_t sites, independent N(0,sigma_t^2) variables; layers are independent. For positive deterministic a_p and finite beta, define F_beta(omega)=log(sum_p a_p exp(beta sum_t omega[t,p_t])). Deterministic normalizations do not affect variance.

Write A_t=m_t^(-1)sum_x omega[t,x] and R[t,x]=omega[t,x]-A_t. Then Var(A_t)=sigma_t^2/m_t and Cov(A_t,R[t,x])=0. Joint Gaussianity makes A_t independent of the entire layer residual vector; independent layers make (A_t)_t independent of all R. Every path uses one site per layer, so the exact factorization gives

F_beta(omega)=beta sum_t A_t+F_beta(R),

Var(F_beta)=beta^2 sum_t sigma_t^2/m_t+Var(F_beta(R)).

Square integrability follows because a finite log-sum-exp lies between the largest path score plus log(min_p a_p) and that score plus log(sum_p a_p); a maximum of finitely many Gaussian linear forms has finite second moment. This proof does not multiply conditional per-layer bounds.

The identical shift argument applies directly to the ground-state maximum M(omega)=max_p sum_t omega[t,p_t], giving Var(M)=sum_t sigma_t^2/m_t+Var(M(R)). It also applies to beta^(-1)F_beta for beta>0 with coefficient one. For the source's planar model the layers t=0,...,n-1 have m_t=t+1, so Var(M_n)>=H_n=sum_{j=1}^n 1/j. This lower bound is compatible with a power upper bound and is not a refutation of C0120.

For any fixed-width restriction with m_t<=W and unit-variance environment, Var(M)>=n/W. Thus a proof cannot first replace the unrestricted lattice by a fixed strip and assert a uniform sublinear variance estimate for that strip. There is no general variance monotonicity under enlargement of a path family.

Independent reviewer: w500, pending. L1 is an author-proved special case, not an independently checked theorem. Its novelty is unverified.

## Hardest remaining gap

The decomposition removes the exactly understood H_n common-mode variance. It gives no power upper bound on Var(M_n(R)) for all planar paths. Closing that residual upper bound, or obtaining a polynomial bound on the source's actual common-vertex overlap, remains necessary. A path changing somewhere under perturbation is insufficient.

## L2. Exact sharp boundary case on the width-one diagonal strip

Fix r>=1. Restrict up/right paths from (0,0) to (r,r) to |x-y|<=1, counting all N=2r+1 visited vertices. Each path must visit every diagonal junction J_k=(k,k), 0<=k<=r. Between J_k and J_{k+1} it chooses exactly one of U_k=(k+1,k) and V_k=(k,k+1). Conversely every sequence of these r choices is an allowed path. All 3r+1 distinct vertex weights are independent N(0,1).

With G_k=g(J_k), X_k=g(U_k), Y_k=g(V_k), the strip maximum is

M_r^strip=sum_{k=0}^r G_k+sum_{k=0}^{r-1} max(X_k,Y_k).

The displayed summands are independent because the associated vertex sets are disjoint. Put A=(X+Y)/2 and D=(X-Y)/2. They are independent N(0,1/2) variables and max(X,Y)=A+|D|. E|D|=1/sqrt(pi), E D^2=1/2; thus Var(max(X,Y))=1-1/pi. Consequently

E M_r^strip=r/sqrt(pi),
Var(M_r^strip)=(r+1)+r(1-1/pi)=(2-1/pi)r+1,
lim_{r->infinity} Var(M_r^strip)/(2r+1)=1-1/(2pi)>0.

This computes the entire variance, not only the L1 lower bound. It is a sharp special case with variance exponent one and standard-deviation exponent one half. It uses the source's iid Gaussian weights and nearest-neighbor orientation, but imposes a strip and fixed endpoint. Those restrictions are essential differences from the full source target.

## L3. Maximizer instability does not imply small vertex overlap

Perturb every vertex by g^s=e^(-s)g+sqrt(1-e^(-2s))g', with independent iid g'. The strip maximizer is almost surely unique: in each block it chooses U_k exactly when X_k>Y_k. Different blocks' pairs of original and perturbed differences are independent. The diagonal junction weights do not affect these choices.

For a standard normal D and independent standard normal Z, (D,D^s)=(D,rho D+sqrt(1-rho^2)Z), rho=e^(-s), has mismatch probability

q(s)=P(sign D != sign D^s)=arccos(e^(-s))/pi.

Proof: (D,Z) has uniform angular direction in the plane. The two half-plane boundaries have angle theta=arccos(rho); the sign-disagreement sectors have total angle 2theta, out of 2pi. Gaussian ties have probability zero.

Let B_r(s) be the number of different block choices. The disjoint environments in the blocks prove the exact binomial law B_r(s)~Binomial(r,q(s)); this is an unconditional independence argument, not a product of merely conditional probabilities. Therefore

P(P_r(g)=P_r(g^s))=(1-q(s))^r,
|P_r(g) intersect P_r(g^s)|=2r+1-B_r(s),
E|P_r(g) intersect P_r(g^s)|/(2r+1)=1-r q(s)/(2r+1).

For s_r=r^(-alpha), 0<alpha<2, q(s_r)~sqrt(2)/pi * r^(-alpha/2). Hence r q(s_r)->infinity while q(s_r)->0: the probability of identical paths tends to zero, but normalized expected overlap tends to one. Also B_r(s_r)/(2r+1)->0 in probability by Markov's inequality. L2 still gives linear variance.

Thus the auxiliary implication "maximizer changes with high probability at a polynomially small noise scale, therefore the maximum has a power variance improvement" is false for Gaussian nearest-neighbor strip polymers. This does not refute the original unrestricted model, the source's actual overlap-chaos implication, or an implication that assumes an additional O(N/log N) variance premise; the strip does not satisfy that extra premise. The intake's qualitative word 'decorrelates' must be instantiated as a quantitative overlap bound.

Independent reviewer for L2 and L3: w500, pending. Novelty is unverified.

As a consistency check, the source's OU variance-overlap identity gives the same strip variance: integral_0^infinity e^(-s)[r+1+r(1-q(s))] ds = r+1+r(1-1/pi). Substitute u=e^(-s) and use integral_0^1 arccos(u) du=1. This checks that the 'path changed' statistic has not been substituted for the covariance-relevant overlap.

NEXT: Check the exact formulas and indexing with a bounded deterministic verification, freeze the review packet, and route its scoped claims to w500.
