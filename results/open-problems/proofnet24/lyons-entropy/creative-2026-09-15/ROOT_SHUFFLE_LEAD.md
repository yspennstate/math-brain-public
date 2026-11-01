# Three-site spectral interpolation as a fixed random shuffle

Date: 2026-09-15. Root research lead, not an agent execution. The representation below is proved; the requested entropy conclusion for general shuffles is an open obligation in this note. No historical priority is asserted.

## Exact representation

Fix a unitary 3-by-3 matrix U and let K=U diag(p_1,p_2,p_3) U*. Draw independent Bernoulli variables Z_i with parameters p_i, then draw a coordinate permutation Pi independently from a fixed law. There exists a law of Pi depending only on U such that

\[
X=\Pi\{i:Z_i=1\}
\quad\hbox{has exactly the occupation DPP law }P_K
\tag{1}
\]

for every p in [0,1]^3.

**Proof.** The matrix B_ji=|U_ji|^2 is doubly stochastic. It is a convex combination of permutation matrices, so choose Pi with P(Pi(i)=j)=B_ji. One elementary proof of this decomposition repeatedly extracts a positive permutation from the support (Hall's condition follows from the row and column sums), subtracts the minimum selected entry times its permutation matrix, and normalizes the residual; at least one support entry disappears each time, so the process terminates.

The spectral DPP construction first chooses the independent set of eigenmodes S={i:Z_i=1}, then samples the projection law with probabilities |det U_(T,S)|^2 for |T|=|S|. When |S|=1 these probabilities are B_ji, matching Pi. When |S|=2, write S^c={i}, T^c={j}. The complementary-minor identity for a unitary matrix gives

\[
|\det U_{T,S}|^2=|U_{ji}|^2=B_{ji}.
\]

But Pi(S)=T exactly when Pi(i)=j, so the same permutation law works. Empty and full S are deterministic. Mixing over all eigenmode choices proves (1).

The phenomenon is special to dimension at most three: in larger dimension the squared two-by-two unitary minors are additional data, generally not specified by the one-site matrix B.

## A concrete remaining entropy problem

For a fixed probability law nu on the six permutations, define

\[
\mathcal H_\nu(p)=H\left(\Pi_\nu(Z_1,Z_2,Z_3)\right).
\]

If this function is concave on [0,1]^3 for every nu, it would prove Lyons concavity for every commuting three-site pair in a fixed occupation basis. It would be enough to establish the assertion for the unistochastic B arising from a unitary U. The identity permutation gives ordinary product entropy. Uniform permutation gives the weighted count entropy being developed in C075. Neither case proves arbitrary nu by convex mixing: concavity of entropy as a function of the **output law** does not imply concavity in these nonlinear Bernoulli parameters after mixing distinct channels.

This is a constructive, finite alternative target for the commuting-kernel assignment C069. An exact rational shuffle obstruction outside the unistochastic class would only obstruct the strengthened shuffle conjecture; a physical unitary and positive curvature would be needed for a Lyons counterexample. Even a proof for all commuting pairs would not by itself control noncommuting affine kernel lines.
