# C0041: finite trap cost versus trap frequency

Worker w444, 2026-10-10. Referee w446; adversary w445. All new lemmas below await independent review. No resolution or novelty claim for C0041.

Let omega(x), x in Z^d, be independent identically distributed probability vectors on the 2d nearest-neighbor steps. The environment is sampled once and held fixed. Assume omega(x,e) >= kappa > 0 almost surely for every allowed step. Let P_{z,omega} be the quenched law and P_z its environment average. The full target, for d >= 2 and a fixed unit vector ell, assumes P_0(X_n dot ell -> +infinity)=1 and asks for P_0(liminf (X_n dot ell)/n > 0)=1. The exact intake record is C0041, problems.jsonl line 41: Drewitz-Ramirez, Open Question 2.20, p.24, https://arxiv.org/pdf/1309.2589. The same formulation is Conjecture 1.1 of Campos-Ramirez, https://arxiv.org/html/1212.4020v3, introduction.

Prior attempt C0041-A001 (2026-09-07, attempts.jsonl line 32) combined the planar directional zero-one law with renewal structure, then stopped at regeneration-time integrability. It observed that UE finite-trap exit costs can be exponential in diameter and iid patterns can be polynomially rare at logarithmic size; it did not show that the resulting duration tail is summable. No C0041-specific record was returned by the bounded filename-only checks of the named H/I attempt directories; the Lean collection returned only the annotated ranking, not a C0041 proof. The read-only population lookup found the dated open-question card and an unverified private reduction, not a certified resolution. These bounded checks cannot certify global absence of owner work. L2/L2b below replace the prior qualitative trap-frequency discussion by an explicit estimate for a specified pattern, without pretending to cover every trap.

The single hardest remaining input in this route is integrability of a genuine regeneration-cycle duration under the no-backtracking law, using ONLY directional transience, iid and uniform ellipticity. No neighborhood-of-directions assumption, polynomial exit assumption or condition (T') may be inserted. Section 2.1 of Campos-Ramirez records the iid cycle law; its stated Theorem 2.1 additionally assumes transience in a neighborhood, so I do not cite that theorem as a proof under the full weaker target assumptions. The elementary reduction R1 below states its cycle-law inputs explicitly.

## R1: a proved conditional reduction

Suppose finite regeneration times 0 <= sigma_0 < sigma_1 < ... split a nearest-neighbor walk into iid cycles after sigma_0. Write S_i=sigma_i-sigma_{i-1}, Z_i=X_{sigma_i}-X_{sigma_{i-1}}, and suppose E[S_1] < infinity and E[Z_1 dot ell] > 0. Then X_n/n converges almost surely to E[Z_1]/E[S_1], with positive ell projection. This statement assumes the actual iid cycle law; it does not establish that law or its moment input from C0041.

Proof. |Z_i|_1 <= S_i, so all components of Z_i are integrable. The strong law gives sigma_k/k -> m=E[S_1]>0 and X_{sigma_k}/k -> E[Z_1]; the initial finite shift is negligible. Integrability also implies sum_k P(S_k > epsilon k) < infinity for every epsilon>0, by the integrated tail bound, hence S_k/k -> 0 by Borel-Cantelli. For k=N(n), the last completed cycle, N(n)/n -> 1/m and |X_n-X_{sigma_k}|_1 <= S_{k+1}=o(k). This proves the claimed limit. The missing input is E[S_1]<infinity. No speed inference follows from cycles being finite almost surely alone.

## L1: a deterministic quenched exit bound

For r >= 1 an integer and x in Z^d, let B(x,r)=x+[-r,r]^d intersect Z^d, L=2r+1, and T_B=inf{n>=0:X_n not in B}. For ANY uniformly elliptic environment, not necessarily iid, any start z in B, and p=kappa^L,

P_{z,omega}(T_B > mL) <= (1-p)^m for every integer m>=0,
E_{z,omega}[T_B] <= L/p,
E_{z,omega}[T_B^s] <= M_r(s):=2^s s! L^s kappa^{-sL} for each integer s>=1.

Proof. From every z in B, at most L consecutive +e_1 steps leave B. Their conditional quenched probability is at least kappa^L. At each deterministic block boundary, conditional on still being inside, the same bound holds. Iterating the Markov conditional bound proves the tail inequality; no independence of the block events is claimed. Summing the tail over integer times gives E[T_B]<=L/p. The tail domination is T_B <=_st L G with G geometric(p) on {1,2,...}. For t>=1, P(G>t)=(1-p)^floor(t)<=exp(-p(t-1)), so G <=_st 1+E with E exponential of rate p. Convexity gives E[(1+E)^s]<=2^{s-1}(1+s!p^{-s})<=2^s s!p^{-s}. This proves the moment bound.

## L2: frequency of fully inward-oriented boxes

Fix delta>0. Put b_1(y)=omega(y,+e_1)-omega(y,-e_1). Define A_delta(x,r) by requiring b_1(y)>=delta at every y in B(x,r) with y_1<x_1 and b_1(y)<=-delta at every y in B(x,r) with y_1>x_1. The middle hyperplane is unrestricted. This is a specific box pattern; it is not a definition of all possible traps.

Let p_+=P_env(b_1(0)>=delta), p_-=P_env(b_1(0)<=-delta), and n_r=r(2r+1)^{d-1}. Then

P_env(A_delta(x,r))=(p_+p_-)^{n_r} <= 4^{-n_r}.

Proof. Each of the two half-boxes has exactly n_r sites. The requirements concern distinct independent environment rows, so their product is legitimate. The two events at a SINGLE site are disjoint since delta>0. Thus p_++p_-<=1, and p_+p_-<=1/4. Translation invariance makes the bound uniform in x. The event may be empty for some delta or row laws; the bound still holds.

Combining this with L1 gives the environment-weighted quenched bound

E_env[1_{A_delta(x,r)} sup_{z in B(x,r)} E_{z,omega}(T_B^s)] <= M_r(s)4^{-n_r}.

For d>=2 and every fixed kappa>0 and integer s>=1, sum_{r>=1} M_r(s)4^{-n_r}<infinity. Indeed the logarithm of each term is at most log(2^s s!)+s log(2r+1)+s(2r+1)log(1/kappa)-log(4) 2^{d-1}r^d. The negative degree-d term dominates the linear and logarithmic positive terms. The corresponding argument does not establish convergence in d=1.

### L2b: holes are allowed below a half-density threshold

Let I_delta(x,r) count the sites in those two half-boxes satisfying their prescribed inward sign. There are 2n_r possible sites. For any fixed theta in (1/2,1], let A_delta,theta(x,r)={I_delta(x,r)>=2 theta n_r}. With D(theta||1/2)=theta log(2 theta)+(1-theta)log(2(1-theta)), interpreting 0 log 0 as 0,

P_env(A_delta,theta(x,r)) <= exp[-2 n_r D(theta||1/2)].

Proof. Site indicators are independent, with n_r Bernoulli(p_+) and n_r Bernoulli(p_-). For lambda>=0 and a=exp(lambda)-1, their moment generating function equals [(1+a p_+)(1+a p_-)]^{n_r}. Since p_++p_-<=1, the arithmetic-geometric mean inequality bounds this by [(1+exp(lambda))/2]^{2n_r}. Exponential Markov and the minimizer exp(lambda)=theta/(1-theta) give the assertion for theta<1; lambda -> infinity gives theta=1 and recovers L2. For theta>1/2 the divergence is strictly positive. Hence the same weighted moment series is finite in d>=2 after replacing 4^{-n_r} by this entropy bound. This conclusion allows an arbitrary set of missing inward rows, provided its fraction among the two half-boxes is less than one half.

## L3: adaptive selection without a false fresh-row assumption

Let N be a deterministic nonnegative integer. Let H be a stopping time for the walk filtration with the entire fixed environment included; let C be a Z^d-valued, F_H-measurable center. On {H<=N}, assume |C|_infinity<=N and X_H in B(C,r). Let Y be the first exit time from B(C,r) measured after H (zero on {H>N}). Then

E_0[1_{H<=N}1_{A_delta(C,r)}Y^s]
 <= M_r(s) min{1,(2N+1)^d 4^{-n_r}}.

Proof. Condition on the fixed environment and F_H. For every possible center and current site L1 bounds the conditional s-moment of Y by the SAME deterministic M_r(s). The indicator of A_delta(C,r) is measurable because the entire environment has been included. After averaging, the remaining probability is P_0(H<=N,A_delta(C,r)). It is bounded by the environment probability of the union of A_delta(x,r) over all deterministic x in [-N,N]^d. Apply a union bound and L2. Overlapping boxes and bias from adaptive selection require no independence here. If Q=P_0(.|D^ell=infinity) and q=P_0(D^ell=infinity)>0, the same nonnegative moment under Q is at most this bound divided by q, since 1_{D^ell=infinity}<=1. This last step does not invoke a strong Markov property under Q.

For a family of such (H_r,C_r), all with the SAME deterministic bound N, Tonelli gives a finite total moment sum over r>=1 when d>=2. H is a genuine stopping time. A regeneration time depends on the future, so it cannot be substituted for H without a separate argument.

The entire L3 proof also works with A_delta,theta and its entropy bound. No extra row independence is asserted after a box is selected or after conditioning on nonbacktracking.

## T1: a direct tail reduction valid even for a future-dependent time

Let tau be any positive, almost surely finite integer-valued random time for a UE walk started at 0; tau need not be a stopping time. Let Q=P_0(.|E), with q=P_0(E)>0, and define R=max_{0<=j<=tau}|X_j|_infinity. For every integer r>=1 and integer t>=0,

Q(tau>t) <= Q(R>r) + q^{-1}(1-kappa^(2r+1))^floor(t/(2r+1)).

Proof. On {tau>t,R<=r}, the path remains inside B(0,r) through time t, hence T_{B(0,r)}>t. Therefore Q(tau>t,R<=r)<=q^{-1}P_0(T_{B(0,r)}>t). Apply the uniform quenched L1 tail bound, then average. No stopping-time assertion about tau and no Markov assertion under Q is used.

Consequently, if Q(R>r)<=C exp(-a r) for a>2 log(1/kappa), then E_Q[tau]<infinity. Choose beta with 1/a<beta<1/(2 log(1/kappa)) and r=floor(beta log(t+1)) for large t. The radius term is O(t^(-a beta)), with exponent greater than 1. The exit term is at most q^{-1} exp(-c t^(1-2 beta log(1/kappa))/log(t+1)) for a c>0, hence summable. Sum the tail bound. The radius assumption is an ADDITIONAL sufficient assumption and has not been proved from directional transience; T1 does not resolve the target.

## Attempt at the missing input and the exact failure

The tempting proof is: bad regeneration delays come from inward traps; L2 makes large traps rare; L1 makes their delay at most exponential; therefore regeneration times have finite mean. L1-L3 rigorously implement the second and third steps for this particular pattern, including adaptive centers. They do not prove the first step.

There is no proved decomposition of ALL regeneration delay into these box exits with an integrable number of contributions. Irregular regions, traps with unconstrained internal rows, large wandering excursions, and repeated entries are not covered. Sending N to infinity in L3 loses its bound through the (2N+1)^d factor. The regeneration duration itself is not a stopping time, and conditioning on successful nonbacktracking tilts the cycle law. Consequently the full target remains unproved by this packet.

The exact remaining lemma is: under the original full target hypotheses, Q=P_0(.|D^ell=infinity) has E_Q[tau_1]<infinity for the standard time-valued directional regeneration construction. Equivalently, sum_{m>=0}Q(tau_1>m)<infinity. The construction must use tau_1=S_K for the first successful attempt K, not K itself. To fix it precisely, choose a>2sqrt(d), set M_0=0, S_1=inf{n>=0:X_n dot ell>=a}, R_1=S_1+D^ell composed with theta_{S_1}, and, after each finite R_j, set M_j=max_{0<=n<=R_j}X_n dot ell, S_{j+1}=inf{n>=R_j:X_n dot ell>=M_j+a}, R_{j+1}=S_{j+1}+D^ell composed with theta_{S_{j+1}}. Then K=inf{j>=1:R_j=infinity} and tau_1=S_K. This distinguishes a duration from the index of the successful trial. A quantitative classification/occupation estimate for arbitrary slow regions sufficient for the integrated duration tail is still missing. L1-L3 exclude one explicit finite-trap mechanism; T1 exposes a sufficient radius input which is stronger than anything established from the target hypotheses here.

NEXT: independently check L1-L3, then test whether an arbitrary low-escape-probability region admits a sufficiently rare certificate without assuming coherent inward drift at all sites.
