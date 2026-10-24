# P0104 independent route: resampling and spectral leakage

2026-10-10. Mathematical result status: self-proved lemmas, independent audit pending. P0104 is not solved. Route was recorded in APPROACH_BEFORE_PEER_PROOFS.md before reading a core-lane proof. Exact source statement is in STATEMENT_FOR_ADVERSARY.md. The campaign card also includes ADH Question 15 (positivity in a suitable dimension); that branch is not settled here.

## Prior-attempt digest and scope

The available campaign record at-p0104 in brain_bundle_C006a04.json records a structural argument: n/log n variance does not imply chi<1/2, and both a power saving and a matching lower bound are needed. C001 restates that known obstruction. The historical raw-worktree path cited by the intake script did not yield a P0104 record; targeted H/I searches did not recover a matching attempt. The annotated Lean list marks P0104 attempted_un; no formal theorem receipt is claimed. Team O's retrieved P0104 row has no holder. The core worker's initial status was source recovery; no core proof was read. A narrow route notice is being delivered through the existing mesh.

L2 is established mathematics, specifically a Bernoulli rederivation of Proposition 6 in Ahlberg-Deijfen-Sfragara, arXiv:2302.11367v2, under finite iid coordinates and square integrability. Their atomic-weight overlap convention is the intersection of all geodesics. Our L3 concerns one fixed selection after forcing an edge; no substitution of overlap conventions is made. Their variance-dependent chaos scale cannot set the missing variance exponent without additional input. The 2026 Basu-Sidoravicius-Sly paper arXiv:2604.01214v1 concerns a class of rotationally invariant Riemannian models; its abstract does not supply a theorem for our Bernoulli lattice law. Current global openness and novelty remain uncertified.

## L1: deterministic localization for positive bounded weights

Assume iid edge weights in [a,b], 0<a<=b<infinity, on nearest-neighbor Z^d. For integer n>=1 and endpoint n e1, the straight path costs at most bn. A minimizer can be chosen simple because deleting a cycle strictly reduces its weight. Every path of cost at most bn has at most floor(bn/a) edges and is contained in the l1 ball of that radius about 0. There are finitely many such simple paths, including the straight path. Their minimum equals the unrestricted passage time. This also proves existence in this special bounded-positive case. We henceforth use this finite deterministic graph.

## L2: finite-product variance identity

Let eta=(eta_1,...,eta_m) have independent Bernoulli(p) coordinates, 0<p<1, q=1-p. Let f be any real function on the finite cube. Given eta, construct eta^rho by retaining each coordinate with probability rho and otherwise drawing an independent Bernoulli(p) coordinate; the choices and replacement coordinates are mutually independent. Define delta_i f=f(eta_{-i},1)-f(eta_{-i},0). Set

R_f(rho)=p q sum_i E[delta_i f(eta) delta_i f(eta^rho)].

Use the orthonormal product basis phi_S=product_{i in S}(eta_i-p)/sqrt(pq), and write f=sum_S fhat(S) phi_S. Orthogonality follows from independent coordinates and each factor having mean zero and second moment one. The coordinate coupling has E[phi_i(eta_i)phi_i(eta_i^rho)]=rho, so the product coupling gives E[phi_A(eta)phi_B(eta^rho)]=1_{A=B} rho^|A|. This product uses an explicitly constructed independent-coordinate coupling, not a multiplication of dependent conditional bounds.

Taking the discrete gradient removes coordinate i and introduces 1/sqrt(pq). Therefore

R_f(rho)=sum_{S nonempty} |S| rho^(|S|-1) fhat(S)^2,
Var f=integral_0^1 R_f(rho) d rho,
D_f:=R_f(1)=p q sum_i E[(delta_i f)^2].

All sums are finite; the integral and termwise calculation need no limiting interchange. R_f is nonnegative and nondecreasing. This is a standard spectral/resampling identity rederived here, with no novelty claim.

## L3: geodesic forcing sandwich

On the finite graph, let tau_e=a+(b-a)eta_e and Delta=b-a>0. Choose a minimizer gamma deterministically among ties. For each e fix all other edges and let gamma_e^0,gamma_e^1 be chosen minimizers when eta_e is respectively forced to 0 and 1. Then

Delta 1_{e in gamma_e^1} <= delta_e T <= Delta 1_{e in gamma_e^0}.

Monotonicity and using the low-environment minimizer as a competitor give 0<=delta_e T<=Delta. If the chosen low minimizer avoids e, it has the same cost in the high environment, so delta_e T=0. If the chosen high minimizer contains e, lowering e reduces that path's cost by Delta; since it was a minimizer in the high environment, T_low<=T_high-Delta, and hence delta_e T=Delta. These arguments remain valid with ties.

Writing H and L for the numbers of high and low edges on the chosen unforced minimizer, independence of eta_e from eta_{-e} gives

q Delta^2 E H <= D_T <= p Delta^2 E L <= p Delta^2 (b/a)n.

For example, sum_e P(e in gamma_e^1)=E H/p: conditioned on eta_e=1, the unforced environment and its deterministic choice are exactly the forced-high environment. This conditioning equality is the required justification.

## L4: linear resampling energy for an explicit planar law

Choose a=1,b=2,p=99/100,q=1/100. All minimizers have length between n and 2n. A simple path of length ell has distinct edges. The probability it has fewer than ell/4 high edges is at most 2^ell q^(3ell/4), by summing over choices of at least 3ell/4 low edges. There are at most 4*3^(ell-1) simple paths of length ell from 0. With r=6 q^(3/4)=3/(5 sqrt(10))<1/5, a union bound over ell>=n gives

P(exists such bad simple path of length >=n) <= (4/3) r^n/(1-r) < 1/3.

On the complement every minimizer has at least n/4 high edges. Consequently E H >= n/6, and L3 yields, for every n>=1,

n/600 <= D_n <= (99/50)n.

This is a proved special-law energy estimate, not a power-law variance estimate. The elementary path-counting proof is deliberately restricted to q=1/100. No assumption of curvature, independent geodesics, or block decorrelation is used.

## L5: an exact reduction and the single hardest gap

For this special law, define the size-biased spectral distribution nu_n(S)=|S| That_n(S)^2/D_n on nonempty subsets of the deterministic finite edge set, and K=|S|. Then

Var T_n = D_n E_{nu_n}[1/K].

Together with L4, the desired Var T_n=n^(2/3+o(1)) is equivalent to

GAP G1: E_{nu_n}[1/K]=n^(-1/3+o(1)).

This is not proved. It needs quantitative control of low-degree spectral mass, not merely a typical spectral scale. A sufficient stronger hypothesis is: constants c,C,epsilon>0 and a_0 in (0,1] exist with R_n(1-t)>=c n for 0<=t<=a_0 n^(-1/3), and R_n(1-t)<=C n(1+t n^(1/3))^(-1-epsilon) for 0<=t<=1. Integrating gives c a_0 n^(2/3)<=Var T_n<=(C/epsilon)n^(2/3). None of those correlation hypotheses is established by this packet.

## A failed shortcut with an exact obstruction

A claim that K/n^(1/3) converges in probability to 1 would not suffice for G1. Let nu_n put mass epsilon_n=n^(-1/4) at K=1 and mass 1-epsilon_n at K=ceil(n^(1/3)). Then K/n^(1/3)->1 in probability, but E[1/K]>=n^(-1/4), larger than n^(-1/3). These are abstract spectral distributions, not asserted to be realizable by FPP. They demonstrate why a typical-scale argument must separately bound the small-degree tail.

## Next concrete proof step

Estimate F_n(k)=nu_n(K<=k) for 1<=k<=n^(1/3). The exact identity E[1/K]=1/(m+1)+sum_{k=1}^m F_n(k)/(k(k+1)) identifies the needed weighted small-degree bound. Start with the first-level term pq sum_e (E delta_e T_n)^2 and determine whether a primary theorem supplies a usable uniform directional estimate. Do not infer the missing bound from qualitative chaos or from n/log n variance.
