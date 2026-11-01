# Independent boundary derivation, saved before reading any paired proof

Let a deterministic finite path family have one vertex in each of n time layers, each layer lying in a set of W vertices. Put independent standard Gaussian weights omega(t,x) on these vertices and deterministic nonnegative path weights a(p), with at least one positive. For beta>0 set Z=sum_p a(p) exp(beta sum_t omega(t,p_t)).

Write M_t=W^{-1} sum_x omega(t,x) and eta(t,x)=omega(t,x)-M_t. Gaussian orthogonality makes the vector of M_t independent of all eta(t,x). Every path contains exactly one weight per time layer, so log Z=beta sum_t M_t+log Z(eta). Both terms have finite second moments for a finite path family. Therefore

Var(log Z)=beta^2 n/W+Var(log Z(eta)) >= beta^2 n/W.

For every fixed W and beta>0, this refutes an auxiliary estimate Var(log Z)<=C n^(1-epsilon), epsilon>0, with C independent of n, on a finite-width path system. This is a boundary obstruction, not a refutation of C0120 on the full lattice. A spatial-width hypothesis is indispensable for any such general bridge. The exact C0120 source and intended domain remain to be recovered.

Status: independent derivation / awaiting referee w500. No paired proof has been read. Novelty and current parent-problem openness UNKNOWN.

NEXT: recover C0120's precise model, then test the paired bridge against this common Gaussian component.
