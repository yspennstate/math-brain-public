Exact obstruction to inferring full local mixing from pair decorrelation

Let H and (A_k,B_k), k in Z, be mutually independent uniform signs. Put the three variables in block k equal to A_k, B_k, H A_k B_k. Every variable is centered and every two distinct variables are independent, including two in the same block. This follows by summing over the unused independent sign, or directly enumerating their four equally likely outcomes.

But the product of the three variables in every block is H. Products in different blocks therefore have covariance one at every separation. The event that the block product is positive has probability 1/2 and is the same event in all blocks. Its event covariance is 1/4. The strong mixing coefficient between any two whole blocks equals 1/4, since 1/4 is also the universal upper bound for indicator covariance. Thus zero pair correlations do not bound dependence of arbitrary local observables.

This is a stationary discrete block process, not a Riesz gas or a claimed point-process realization. It rigorously refutes the general probabilistic step 'pair decorrelation implies strong mixing'. It does not refute any specially proved Riesz implication that uses additional hypotheses.

Measurement: verify_bridge.py enumerates the 32 states of two shared-parity blocks, checks all 15 pairs for exact independence, and computes the supremum over the complete finite block-event sigma fields. The comparison fixture uses independent parity signs and has 64 states, the same zero pair correlations, and alpha=0. Both calculations use exact integer/Fraction arithmetic.

Bounded proposed repair: proposed/bridge_hypothesis_gate.py refuses use of the decay consequence of G3 unless supplied evidence explicitly covers all local events, uniform window-size dependence, a void bound, the spatial observable and geometric hypotheses. It only checks stated hypothesis scope; it does not certify the truth of supplied evidence. On the shared-parity counterexample the naive pair-only admission rule accepts once; the proposed gate rejects it. This is a one-fixture reasoning measurement, not a claim of general recall or proof accuracy improvement. No live engine is changed.

NEXT: Preserve the distinction between particle pair correlations and full local-event mixing in theorem retrieval and all P0321 proof packets.
