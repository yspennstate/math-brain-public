# P0003 boundary audit, 2026-10-10

## Exact assigned target and related route

[Grimmett Question 2.2](https://arxiv.org/pdf/2205.07318) asks about a uniform **n-step** SAW from the origin of the infinite hexagonal lattice, with a free endpoint, suitably rescaled as n grows. The source leaves the scale, SLE geometry/stopping rule, parametrization, and topology unspecified. This is P0003.

The **related chordal route** samples boundary-to-boundary SAWs in a domain with critical fugacity z_c = (2+sqrt(2))^(-1/2), and conjectures convergence to chordal SLE(8/3) as mesh tends to zero [BDGS Conjecture 1.5 and Section 3.3](https://arxiv.org/html/1206.2092). Conditioning on exact length gives a uniform law within a fixed domain and fixed endpoints, but no proved transfer to Grimmett's infinite-lattice, free-endpoint fixed-length model is supplied. The counterexample below audits a finite-volume property of this related route.

## Sharp auxiliary counterexample: domain Markov is insufficient

Take honeycomb subgraphs (H_\delta\) inside a fixed rectangle, with (N_\delta\le C\delta^{-2}\) vertices and boundary endpoints. Select a simple lattice corridor path (P_\delta\) converging to a deterministic simple arc. Let (z_c=(2+\sqrt2)^{-1/2}\), and give each edge on (P_\delta\) weight (z_c\); give every other edge weight (z_c e^{-\delta^{-4}}\). Give a path the product of its edge weights and normalize over all endpoint-to-endpoint SAWs.

For any prefix with positive probability, the prefix product is common to every continuation. Removing its earlier vertices leaves precisely the admissible continuations, with the same product weights. Thus the exact finite-domain Markov property holds.

Every other path has an edge outside (P_\delta\), because the subgraph made of (P_\delta\)'s edges is a path and has one endpoint-to-endpoint simple path. Since (z_c<1\), any other path's weight is at most (e^{-\delta^{-4}}\). There are at most (3^{N_\delta+1}\) SAWs in a graph of maximum degree three. The selected path has at most (N_\delta-1\) edges and weight at least (z_c^{N_\delta}\). Consequently

\[
\mathbb P_\delta(\omega\ne P_\delta)\le 3^{N_\delta+1}z_c^{-N_\delta}e^{-\delta^{-4}}=\exp[-\delta^{-4}+O(\delta^{-2})]\longrightarrow0.
\]

Hence the scaling law is the deterministic arc, not SLE(8/3). This is a counterexample to a domain-Markov-to-SLE bridge. It changes the model by using edge-dependent factors; the original P0003 conjecture remains untouched.

## Hardest open piece

For the actual uniform fixed-length free-endpoint SAW, first specify and justify a scaling and candidate limiting curve law. Prove tightness and identify all subsequential limits. A chordal route also needs quantitative crossing and multi-arm control, a conformal martingale or restriction law, and a justified transfer from its variable-length fixed-endpoint ensemble to the assigned model. The local parafermionic relation alone does not close any of these steps.
