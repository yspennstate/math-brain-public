# C0017 statement packet (before the proof attempt)

Recovered catalog statement (problems.jsonl, row 17, source garban_steif_noise_2012, Chapter II Section 4 p. 26): "Prove that critical bond percolation on Z^2 at p = 1/2 is conformally invariant in the scaling limit (Cardy's formula and convergence of interfaces to SLE(6)), as is known on the triangular lattice by Smirnov." This is a historical problem statement, not a current-open certificate.

Precise crossing formulation to use here: let D be a bounded simply connected Jordan domain with distinct boundary prime ends a,b,c,d in positive cyclic order, and let (D_delta,a_delta,b_delta,c_delta,d_delta) be standard inner square-lattice approximations of mesh delta with the marked boundary arcs converging. Declare each nearest-neighbor bond independently open with probability 1/2. The probability of an open connection in D_delta from the arc a_delta b_delta to the arc c_delta d_delta should converge to Cardy's value C(lambda). Here a conformal map to the upper half-plane sends (a,b,c,d) to (0,lambda,1,infinity), 0<lambda<1, and C(lambda)=Gamma(2/3)/(Gamma(1/3)Gamma(4/3))*lambda^(1/3)*2F1(1/3,2/3;4/3;lambda). Thus conformally equivalent marked domains have the same limit.

Interface component of the catalog target: in Jordan Dobrushin domains with marked a,b and the usual primal/dual boundary arcs, the critical square-bond medial exploration from a_delta to b_delta should converge in law, as an unparametrized continuous curve, to chordal SLE_6 from a to b in D. Proving one isolated crossing comparison does not by itself prove this component.

Current openness: UNKNOWN pending assessment of recent primary manuscripts; a bounded search found an October 2026 manuscript claiming square-lattice random-cluster conformal limits. No novelty claim will be made on that basis or its absence.

Independent adversary task: identify a concrete obstruction to transferring a triangular-site theorem to this square-bond statement. Read only this statement initially; w417's later proof packet will be separate.

Prover lemma boundary: w417 reserves a comparison through independent local terminal-connectivity laws, with an explicit accumulated error and a finite-network obstruction. This is distinct from deriving an additional parafermionic relation or classifying a Loewner martingale. No shared mathematical file or live store is being changed.
