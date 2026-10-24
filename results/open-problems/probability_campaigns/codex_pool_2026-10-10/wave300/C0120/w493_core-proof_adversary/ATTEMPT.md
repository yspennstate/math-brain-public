# C0120 independent derivation (saved before reading w492's proof)

Author: w493. Date: 2026-10-10. Referee: w494 (pending). Current openness: UNKNOWN. Parent problem: NOT SOLVED. Requested settings are not a served-model receipt.

The primary source is Chatterjee, arXiv:0810.4221v2 (16 December 2008), Section 8, Theorem 8.1, and Section 12(3), printed page 59. Its model has independent standard Gaussian vertex weights on the first quadrant of Z^2. A path has n vertices, starts at the origin, and moves right or up. The endpoint is unrestricted. Write M_n=max_p sum_{v in p} g_v; its negative is the minimum energy. The source's variance bound is C n/log n. The exact historical question says: "Improve the fluctuation exponent in directed polymers."

Important scope correction: the cited source concerns the Gaussian ground state M_n in 1+1 dimensions. The intake's Var(log Z_n), arbitrary weights, and general dimension are extensions of that question, not the model or theorem stated at that locator. A precise power target in the source model is: there exist delta in (0,1) and finite C, independent of n, such that Var(M_n)<=C n^(1-delta) for all n>=2. We do not assert a uniform constant over temperatures, dimensions, or weight laws. A separate finite-temperature quantity is F_{n,beta}=log(sum_p exp(beta sum_{v in p}g_v)) for fixed beta>0; none of the following proves its power upper bound.

## Independent layer-mean obstruction

Let L_i={(x,y):x+y=i,x,y>=0}, for 0<=i<n, so |L_i|=i+1. Put A_i=(i+1)^(-1) sum_{v in L_i}g_v and r_v=g_v-A_i. The finite Gaussian vector (A_i)_i is independent of the vector r: within a layer Cov(A_i,r_v)=1/(i+1)-1/(i+1)=0, and different layers are independent. The residual covariance is singular, which is harmless for Gaussian independence.

Every admissible path uses exactly one vertex from each L_i. Therefore, with S_n=sum_i A_i,

M_n(g)=S_n+M_n(r).

The summands are independent and square integrable (the maximum is over finitely many Gaussian path sums). Consequently

Var(M_n)=H_n+Var(M_n(r)) >= H_n, where H_n=sum_{j=1}^n 1/j.

For fixed beta>0, the same argument factors every Gibbs weight by exp(beta S_n), giving Var(F_{n,beta})=beta^2 H_n+Var(F_{n,beta}(r)). Deterministic partition-function normalizations do not alter this identity. These are finite-n identities, not asymptotic heuristics. They permit a power upper bound with delta<1; they refute a bounded-variance claim for this model and show that layer-wide perturbations need not move the maximizing path at all.

## Gaussian overlap and its unavoidable floor

Let g_t=e^(-t)g+sqrt(1-e^(-2t))g' with an independent Gaussian g'. The maximizing path P_n(g) is unique almost surely: different paths have a difference of sums with positive Gaussian variance, and there are finitely many paths. Set U_v(g)=1{v in P_n(g)} and R_n(t)=E sum_v U_v(g)U_v(g_t).

The weak gradient of the Lipschitz function M_n is U almost everywhere. For the stationary Gaussian Ornstein-Uhlenbeck semigroup P_t, the gradient commutation formula is grad(P_t f)=e^(-t)P_t grad(f). Integrating the derivative of E[f P_t f] from zero to infinity, first for smooth approximations and then by Gaussian Sobolev convergence, gives

Var(M_n)=integral_0^infinity e^(-t) R_n(t) dt.

For each v, E[U_v P_t U_v]=||P_{t/2}U_v||_2^2. Semigroup contraction makes R_n(t) nonincreasing; preservation of the mean and Jensen give E[U_v P_t U_v]>= (E U_v)^2. Summing the identity sum_{v in L_i}E U_v=1 and applying Cauchy-Schwarz within each layer yields

R_n(t)>=B_n:=sum_v(E U_v)^2>=H_n for every t>=0.

In the independent-environment limit t->infinity, R_n(t)->B_n. Thus an estimate R_n(t)<=C_n exp(-c_n t) with finite C_n and c_n>0 for all t is false even for this exact source model. Subtracting the first Gaussian-chaos floor B_n can repair that formulation, but then an upper bound for B_n must also be proved; a bound only on the centered overlap is insufficient for the variance target. This is an obstruction to a proof step, not a disproof of C0120.

## An exact n=2 witness inside the source model

There are two paths, sharing the origin and choosing (1,0) or (0,1). Write their weights g_0,g_1,g_2. Then M_2=g_0+max(g_1,g_2). With D=g_1-g_2 and its coupled D_t, Corr(D,D_t)=e^(-t). A rotationally symmetric two-dimensional standard Gaussian gives P(sign D=sign D_t)=1/2+arcsin(e^(-t))/pi. Hence

R_2(t)=3/2+arcsin(e^(-t))/pi, and Var(M_2)=2-1/pi.

In particular R_2(t)>=3/2 for all t, tends to 3/2 rather than zero, and integrates against e^(-t) to 2-1/pi. Directly, max(g_1,g_2)=(g_1+g_2)/2+|g_1-g_2|/2; the mean and difference are independent, and Var(|N(0,2)|)=2(1-2/pi), proving the same variance. At n=1 the path is deterministic and R_1(t)=Var(M_1)=1. These boundary cases include the origin explicitly.

## The single hardest missing input and a proved reduction

For this lane the missing lemma is quantitative chaos at a polynomial time: find fixed a,b>0 and finite C such that R_n(n^(-a))<=C n^(1-b), uniformly for n>=2. Constants must concern this one fixed model; this is not an available theorem.

If that lemma holds, monotonicity, R_n(t)<=n, and the overlap identity imply

Var(M_n)<=n(1-exp(-n^(-a)))+exp(-n^(-a))R_n(n^(-a))<=n^(1-a)+C n^(1-b).

Thus delta=min(a,b) gives a power improvement. Conversely, if Var(M_n)<=C n^(1-delta) for some delta>0, monotonicity implies (1-exp(-t))R_n(t)<=Var(M_n). At t=n^(-delta/2)<=1, 1-exp(-t)>=t/2, so R_n(t)<=2C n^(1-delta/2). This proves equivalence of existence of a power variance gain and existence of some polynomial-time polynomial-overlap gain, with a stated exponent loss. It does not supply either gain.

## Attempt at the missing lemma and why it stops

The historical C n/log n variance theorem gives only R_n(t)<=C n/((1-exp(-t))log n). At t=n^(-a) this is of order n^(1+a)/log n, so the trivial bound R_n(t)<=n is eventually stronger. The qualitative chaos theorem at a time of order 1/sqrt(log n) does not give a polynomial rate by replacing its time with n^(-a).

The attempted shortcut was to use annealed one-layer symmetry as if choices in different layers were independent, or as if annealed path marginals were the simple-walk heat kernel. The first does not follow from separate layer bounds, and the second requires a proof for the optimizing/Gibbs path. The exact n=2 witness already shows persistent overlap between noisy environments; conditioning on the whole maximizing path also reveals inequalities involving all layers, so independent raw layer weights do not become independent conditional choices. No product estimate is used. The saved Bernoulli witness in CLAIMS.jsonl identifies the minimal filtration requirement for any proposed product step.

NEXT: Read w492's statement-only route and candidate proof, then audit its claimed polynomial-time overlap estimate against the origin, layer-mean floor, and conditioning requirements; request w494's independent check of the finite-n identities.
