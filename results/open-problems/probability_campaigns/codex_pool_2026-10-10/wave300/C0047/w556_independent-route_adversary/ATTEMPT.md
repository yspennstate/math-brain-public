# C0047 independent approach, recorded before reading w555's proof

2026-10-10. Worker w556, adversary lane; referee w557.

For a fixed infinite locally finite Cayley graph G, let tau_p(x,y) be the probability that x and y belong to the same Bernoulli bond cluster. Seek p>p_c such that the positive kernel T_p=(tau_p(x,y)) is bounded on l2(V). Under uniqueness with theta(p)>0, positive association should force tau_p(x,y)>=theta(p)^2 uniformly. Testing the kernel on normalized indicators of larger finite sets then contradicts boundedness. This uses the dependence of infinite-cluster membership correctly through FKG; no multiplication of conditional row estimates is allowed.

The unresolved mathematical step is existence of a bounded-operator parameter strictly above p_c for every nonamenable Cayley graph. A spectral estimate valid only below p_c, a change of generating set, or exponential decay with an insufficient growth exponent does not settle that step. This is a proposed route, not a proof of the Benjamini-Schramm conjecture. First recover exact source statements and previous approaches; then derive a finite certificate and attack the paired proof without changing methods to match it.

Peer proof read: NO at this checkpoint. Primary-source verification: pending. Current openness: UNKNOWN pending a recent primary-source check. Served model: not independently evidenced by the requested settings.

## Independent derivation S1: a finite witness against uniqueness

Let G be infinite, connected, locally finite and vertex-transitive. Use iid Bernoulli bond percolation at p and write theta=P_p(|C(o)|=infinity)>0. Suppose there is almost surely exactly one infinite cluster. The events I_x={|C(x)|=infinity} are increasing; Harris positive association, justified by decreasing finite-radius approximations, gives P_p(I_x intersect I_y)>=theta^2. On I_x intersect I_y uniqueness forces x connected to y. Thus tau_p(x,y)>=theta^2 for all x,y.

For any nonempty finite S, put f_S=1_S/sqrt(|S|). Its l2 norm is one, and <f_S,T_p f_S>=|S|^{-1} sum_{x,y in S} tau_p(x,y)>=|S| theta^2. This contradicts a finite operator bound M by choosing |S|>M/theta^2. No independence of infinite-cluster memberships is asserted: FKG supplies an inequality, not an equality.

For 0<=q<=p, monotone coupling gives 0<=T_q<=T_p entrywise and hence boundedness of T_q whenever T_p is bounded (apply the bound to |f|). Consequently, if p>p_c and T_p is bounded, no q<=p has a unique infinite cluster: theta(q)=0 excludes any infinite cluster, and theta(q)>0 invokes the preceding obstruction. Therefore p_u>=p>p_c directly from the infimum definition. This argument does not need uniqueness monotonicity as an additional hidden premise.

This is an independent rederivation of an established implication, not a new theorem or a resolution of C0047. The 2020 Hutchcroft paper explicitly distinguishes the operator condition from the Benjamini-Schramm conjecture. Its 2020 open-status language cannot establish October 2026 status; a September 2026 public preprint makes a stronger claim and needs a separate audit.

## Independent obstruction S2: square-summable rows need not bound an operator

On the transitive set Z define K(i,j)=(1+|i-j|)^(-3/4). It is symmetric, translation invariant, nonnegative, and K(i,i)=1. Each row has squared l2 norm

  1+2 sum_{m>=1}(1+m)^(-3/2) <= 1+2 integral_1^infinity x^(-3/2) dx = 5.

For S_n={1,...,n}, however, <f_{S_n},K f_{S_n}>=1+2 sum_{m=1}^{n-1}(1-m/n)(1+m)^(-3/4)>=n(1+n)^(-3/4), which tends to infinity. Thus the operator is unbounded. Checking every delta-function column gives only a necessary condition for operator boundedness; a uniform bound for every finite-support input is the missing premise.

The example is positive semidefinite as well: let T have Gamma(3/4,rate=1) distribution, set R=exp(-T), and conditionally on R perform iid bond percolation on Z with edge probability R. The averaged connection kernel is E[R^{|i-j|}]=(1+|i-j|)^(-3/4). For every realized partition, sum_{i,j} a_i a_j 1_{i connected j}=sum_clusters (sum_{i in cluster} a_i)^2>=0 for finite-support real a. Averaging proves the asserted positivity.

Scope boundary: the mixture is neither iid Bernoulli at a fixed parameter nor an ergodic percolation law; Z is amenable. It refutes the generic functional-analytic implication even under positivity and transitivity. It is not a counterexample to the parent conjecture, nor to a claim that uses an additional proved iid or nonamenable estimate. w557 must check the derivation independently.

## The single remaining hard piece

On the original fixed Cayley graph, derive an operator estimate at some p>p_c from nonamenability, uniformly over every finite-support l2 input. If an argument only estimates a root row, proves a bound below p_c, assumes critical mean-field behavior, or replaces the generating set, that implication remains unproved. New claimed literature may discharge it, but title, hash and comparator scope alone do not.
