# C0044 sharp-boundary lane, w582

Exact primary-source target and current literature status are pending. The dated assignment describes directional zero-one for iid random walks in random environment in dimension at least three; it is not a proof or a current-status certificate.

## L1: the precise uniform-floor bridge

Fix a deterministic nearest-neighbor environment omega on Z^d. For a nonzero direction l let A_l be the event that X_n dot l tends to positive infinity, and let q(x)=P_x^omega(A_l). Assume inf_x q(x)=c>0. Then q(x)=1 for every starting site x.

Proof. With F_n the natural path filtration, removal of the first n steps does not change A_l. The Markov property consequently gives P_x^omega(A_l | F_n)=q(X_n). Since A_l belongs to F_infinity, Levy's upward theorem gives q(X_n) -> 1_{A_l} almost surely. Each q(X_n)>=c. The limit cannot be zero, hence A_l has probability one. This proves the claim for any x. Ellipticity is unnecessary for this particular implication.

Single hardest gap at this checkpoint: infer a path-uniform positive escape floor (or another exclusion of convergence to zero) from the exact iid environment assumptions without assuming the conclusion. A pointwise positive harmonic q is not automatically bounded away from zero on an infinite state space.

Status: elementary proved special case, independent mathematical review pending. No claim that C0044 is solved or that this lemma is novel.

## L2: exact harmonic boundary and finite-path comparison

Assume the fixed nearest-neighbor environment is elliptic, so its walk is irreducible. For any finite path x=x_0,...,x_r=y with path probability p>0, the Markov property gives q(x)>=p q(y). Apply the same argument to the complementary tail event to obtain 1-q(x)>=p(1-q(y)). Thus positivity of q, and positivity of 1-q, propagate to every starting site. Under uniform ellipticity kappa, a shortest path gives q(x)>=kappa^{|x-y|_1}q(y); the bound depends on distance.

Consequently exactly one of the following holds: q is identically zero; q is identically one; or 0<q(x)<1 at every site and inf_x q(x)=0, sup_x q(x)=1. In the third case L1 rules out a positive infimum; L1 applied to the complementary event rules out a supremum below one.

For a stationary ergodic environment law, {q(0)>0} is invariant under every spatial shift: q_{theta_z omega}(0)=q_omega(z), and the preceding positivity propagation holds pathwise. If the annealed probability alpha=E[q(0)] is positive, this event therefore has probability one. If 0<alpha<1, apply the same argument to 1-q; almost every environment is in the third alternative. Stationarity and ergodicity alone do not exclude that alternative. Given alpha>0, proving an almost-sure positive infimum of q is equivalent to proving alpha=1, so this bridge contains the unresolved conclusion unless an additional argument supplies the floor.

## CE1: explicit uniformly elliptic counterexample to the stronger floor bridge

For any d>=2, let k=x_1. Assign omega(x,+e_1)=3/8 and omega(x,-e_1)=1/8 when k>=0, and swap these two probabilities when k<0. Assign each of the other 2(d-1) steps probability 1/[4(d-1)]. Every row sums to one and every transition is at least min(1/8,1/[4(d-1)])>0.

Generate an independent Bernoulli(1/2) clock for horizontal steps. At its infinitely many ticks the first coordinate is a birth-death chain with right-jump probability 3/4 on k>=0 and 1/4 on k<0. For the constant biased chains, the probability of reaching zero from k>=1 is 3^{-k}, and from k<=-1 is 3^k. This follows from gambler's ruin on a finite interval followed by its boundary limit (or the bounded exponential harmonic function and optional stopping).

After a visit to zero there is probability (3/4)(2/3)=1/2 of taking +1 and never returning. The strong Markov property bounds the probability of at least m further returns by (1/2)^m; this is a conditional Markov argument, not an independence assumption across arbitrary regions. Hence there are finitely many visits to zero almost surely. On each possible eventual half-line the usual biased-walk strong law implies escape to the corresponding infinity; apply it after each deterministic time and take the countable intersection. Thus A_{e_1} and A_{-e_1} partition the path space up to null sets.

Write a=q(0). For k>=0, q(k)=1-(1-a)3^{-k}; for k<=0, q(k)=a3^k. At zero, a=(3/4)q(1)+(1/4)q(-1)=1/2+a/3, hence a=3/4. The exact probabilities are

q(k)=1-(1/4)3^{-k} for k>=0; q(k)=(3/4)3^k for k<=0.

Therefore q is strictly between zero and one at every site, q(0)=3/4, inf q=0 and sup q=1 despite uniform ellipticity. This environment is deterministic and NOT translation invariant or iid: its row changes across a fixed hyperplane. It refutes the stronger auxiliary inference 'uniform ellipticity plus pointwise positive escape probabilities implies probability one', not C0044. No novelty is claimed.

## L3: balanced projected drift gives oscillation (an actual C0044 subclass)

Fix any d>=1, l!=0, and a uniformly elliptic nearest-neighbor environment omega with kappa>0. Suppose sum_{|e|=1} omega(x,e)(e dot l)=0 at every site. For a walk starting at x, M_n=(X_n-x) dot l is a martingale with increments bounded by L=||l||_infinity>0 and conditional second moments at least v=2 kappa ||l||_2^2>0.

For a,b>0 let tau be the first time M_n<=-a or M_n>=b. The stopped square identity gives v E[tau wedge n]<=E[M_{tau wedge n}^2]<=max(a+L,b+L)^2. Monotone convergence gives E[tau]<infinity. Since the stopped M is uniformly bounded, optional stopping gives E[M_tau]=0. With p=P(M_tau>=b), the overshoot bounds give 0=E[M_tau]>=bp-(a+L)(1-p), so p<=(a+L)/(a+b+L).

The event of never hitting (-infinity,-a] forces exit through the upper endpoint for each b; the displayed bound tends to zero as b tends to infinity. Thus every fixed negative threshold is hit almost surely. Apply the same argument to -M for every positive threshold. A countable intersection over integer thresholds yields liminf M_n=-infinity and limsup M_n=+infinity almost surely. Hence both directional escape events have probability zero in this fixed environment. Any iid uniformly elliptic law supported on such rows satisfies the exact C0044 conclusion with alpha=0. No novelty is claimed.

## L4: strictly positive uniform projected drift gives escape

In a fixed nearest-neighbor environment suppose sum_e omega(x,e)(e dot l)>=delta>0 at all x. No ellipticity or independence assumption is needed. The martingale N_n=(X_n-X_0) dot l - sum_{j<n} drift_l(X_j) has differences bounded by 2L. Azuma's inequality yields P(|N_n|>=epsilon n)<=2 exp(-epsilon^2 n/(8L^2)). These probabilities are summable, so Borel-Cantelli, first for rational epsilon>0, gives N_n/n->0. Thus liminf_n (X_n dot l)/n>=delta almost surely, and P_x^omega(A_l)=1. This supplies the alpha=1 subclass even for arbitrarily small fixed positive delta. Delta=0 alone cannot replace delta>0, as L3 shows.

## Single hardest remaining gap

For general iid strictly elliptic rows with mixed projected drifts, exclude the nonconstant harmonic alternative of L2. Neither distance-dependent Harnack comparison nor spatial ergodicity supplies a path-uniform escape floor. The balanced and uniform-drift cases above close only their stated subclasses.

## Recent source gate (2026-10-10)

The official public ComparatorChallenges/DirectionalWalk.lean file exposes the intended iid, strictly elliptic d>=3 statement, but its directional_zero_one body is `by sorry` (as read from raw.githubusercontent.com/openai/math/main, line 81). This is a comparator statement with an admitted placeholder, not an accepted formal proof receipt. This observation does not refute an accompanying manuscript and does not exclude a separate full proof file. Current openness remains UNKNOWN until the actual proof and a different-model review are checked.
