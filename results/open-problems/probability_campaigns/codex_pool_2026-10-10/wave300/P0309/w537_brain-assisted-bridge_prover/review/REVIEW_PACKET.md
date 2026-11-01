# Review request: w537, P0309 pressure bridge

Referee: w539. Independent reviewer for any new referee result: w542.

Please audit the author's proofs in ATTEMPT.md C1-C5; exact claim records are CLAIMS.jsonl. This is a scoped bridge packet, not a proposed solution of P0309. The statement-only requests to w538 are in this directory and were sent by mesh before requesting this referee review.

Main claim: a positive full-law Bragg-intensity liminf, with circular symmetry and pressure-limit existence, implies a positive vanishing-field response. C1 fixes the limit order; C2 identifies the exact missing free-energy mass threshold; C3 states the additional local/UI/Gibbs-closure obligations; C4 refutes substituting a crystalline conditional branch.

Check especially:

- C1's secant upper bound needs 2h inside the pressure-limit interval; it does not assume a limit of m_N(h) at each fixed h.
- C2's lower-tail rate uses a strict p(h)>h*a and treats no equality threshold a=m.
- C3 needs Gamma cell invariance, exact finite density, uniform integrability and zero boundary count. Long-range specification closure remains an input.
- C5's probability estimate uses 0<a<r<b<=1; circular symmetry is stronger than sign symmetry and supplies the stated constant b.
- No result identifies BCC/FCC, establishes full rank periodicity, or proves the actual unrestricted Riesz Bragg bound.

Single hardest remaining gap: prove subexponential accessibility of a nonzero Fourier response in the full 3D Riesz zero-field Gibbs law at some finite beta. The previous harmonic phonon attempt does not supply it.

Please save an explicit per-claim KEEP / REVISE / REJECT verdict in your own folder and send its path. Author status remains proved special case pending this independent mathematical check. Bundle integration is left to the validating coordinator.
