# C0044 independent route, written before reading w579 or w580 proof drafts

## Statement and setup

Let the rows of a nearest-neighbor environment on Z^d be iid and strictly elliptic, d >= 3. For a fixed nonzero real direction l, set A_l = {X_n · l -> +infinity} and q_omega(x) = P_omega^x(A_l). The target is P_0(A_l) in {0,1}. The 2014 Drewitz-Ramirez survey states this as Open Question 3.2 under (E) and (IID). A September 2026 public manuscript claims a full answer, but its mathematical and formal verification are separate work.

## Route: quenched harmonic function and product ergodicity

For every strictly elliptic fixed environment, q_omega(x) > 0 at one site iff q_omega(y) > 0 at every site. Indeed, choose a finite nearest-neighbor path y to x. Its quenched probability is strictly positive, and after following it the walk has probability q_omega(x) of A_l. The event A_l ignores the finite initial path. Thus B_l = {omega: q_omega(0) > 0} is translation invariant (the starting point shifts with the environment). Under iid rows it has environment probability zero or one. Consequently P_0(A_l) > 0 implies q_omega(x) > 0 for every x in almost every environment.

Also q_omega(X_n) = P_omega^0(A_l | F_n), so it is a bounded martingale and converges to 1_{A_l} under each quenched law. This follows from the Markov property, the tail nature of A_l, and martingale convergence.

The tempting next inference is false without an additional argument: B_l having probability one does not imply q_omega(0)=1 almost surely. The martingale can have both zero and one terminal values even though its value is positive at every finite-time state. To finish this route, one would need a new theorem excluding an iid strictly elliptic environment in which q_omega(x) lies strictly between zero and one throughout the lattice. Ergodicity of the environment alone does not do this; the walk samples rows with path bias. This is the single load-bearing gap.

## Deliberate distinction from the recorded attempt

The 2026-09-07 C0044-A002 attempt isolates the planar intersection method of Zerner-Merkl. This route uses no path-intersection or planarity step. It yields a modest, rigorous all-start positivity lemma and stops at the quenched mixed-tail obstruction. It is neither a proof of C0044 nor a claim of novelty.
