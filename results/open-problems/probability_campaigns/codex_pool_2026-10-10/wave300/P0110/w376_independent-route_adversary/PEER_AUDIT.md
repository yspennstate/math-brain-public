# w375 independent audit, P0110

Artifact read: ~/brain_workers/w375/APPROACH_PRECOMMIT.md, 2026-10-10. The w376 independent oscillating-scale derivation was already saved in ATTEMPT.md before this artifact was opened. The snapshot receipt will bind the file read.

Verdict: KEEP the finite axial exact-directed-reduction obstruction, within its stated scope. This is an independent audit of the original mathematical argument, not a review of another review. Required referee w377 remains separate.

For a law with positive masses p_low,p_high in two disjoint intervals with upper low bound a_plus strictly below lower high bound b_minus, choose an integer n satisfying n*b_minus>(n+2)*a_plus. A coordinate-monotone nearest-neighbor path from 0 to n*e1 must use only n positive e1 steps, so there is exactly one such path. On the event that its n edges are high and the n+2 height-one detour edges are low, the unrestricted passage time is strictly smaller than the directed passage time. The high and low edge sets are deterministic, internally distinct, and disjoint from each other. The iid probability product p_high^n*p_low^(n+2) is therefore valid without any path-selection conditioning. Unspecified paths can only lower the unrestricted minimum, preserving the strict comparison.

Separately checked witness: Uniform[1,2], low interval [1,5/4], high interval [7/4,2], n=6. Directed lower cost is 21/2, detour upper cost is 10, strict gap is 1/2, and event probability is 4^(-14)=1/268435456. For this choice n=6 is the smallest strictly valid positive integer. These are exact bounds, not simulation.

Limits: a positive-probability finite obstruction does not disprove asymptotic coupling, equality of exponents, or a KPZ relation. The axial uniqueness argument does not extend to endpoints with two positive coordinates: many coordinate-monotone paths then exist. Any extension must control every directed competitor, not just a single high path. That extension belongs to w375's lane; w376 has not duplicated it.

## Full proof audit, subsequently available

Original source: ~/brain_workers/w375/PROVED_LEMMAS.md, L1-L4, and STATEMENT_FOR_ADVERSARY.md. The review applies only to those numbered lemmas, not to later additions. Snapshot receipts are separate from proof validation.

L1: KEEP, as above.

L2: KEEP the linear axial separation. For block starts j(k+1), the detour uses columns j(k+1) through j(k+1)+k; the following single axial connector separates those from the next detour's start column. Both alternatives and all connectors in different blocks use disjoint deterministic edge sets. Hence the selected block costs are iid despite minimization within each block. The selected paths remain self-avoiding because their horizontal coordinate ranges are disjoint except at adjacent connector endpoints. The identity E min(S,H)=k*mu-E(S-H)_+ gives the claimed mean saving. Boundedness gives integrability; the strong law applies to the iid block costs. The remainder costs at most k*R. No conditional row probabilities are multiplied here. The expectation and limsup bounds have the same positive saving delta/(k+1).

L3: KEEP the finite diagonal obstruction. There are k(k+1) horizontal high edges and k^2 vertical high edges, totaling 2k^2+k. The low set contains k right-column vertical edges, k horizontal edges at y=-1, and two external vertical edges, totaling 2k+2. All sets are disjoint. Every monotone path stays in the square and uses k high horizontal edges plus k vertical edges of weight at least ell. The external detour cost is at most (2k+2)*a; the stipulated inequality is exactly the strict comparison. A monotone path in higher dimensions cannot add other coordinates and return to zero. The lemma controls all directed competitors, so the nonaxial caveat about a single high path does not defeat this actual proof.

L4: KEEP the sharp finite axial threshold. Outside one null event, all countably many edges are in [r,R]. The parity/minimal-length argument gives at least n+2 edges for a nonaxial path. At the non-strict threshold the passage times agree, but geodesic uniqueness is not asserted. Above it, eta=M/(4n+4) gives a strict detour gap M/2; the essential endpoint definition ensures both interval probabilities are positive. This addresses boundary ties correctly.

Scope refinement for L2: its final caveat permits a different coupling, but a different coupling ALONE cannot yield an o(n) raw approximation. Marginals already have separated linear limits. For c=delta/(k+1) and 0<epsilon<c/2, any coupling satisfies P((T_dir-T)/n>=c-2epsilon)->1 by the two marginal bounds and a union bound. This independently derived consequence is detailed in ATTEMPT.md and awaits w377. Recentring or changing models can still leave a centered universality-class question open. The requested target remains unproved.

The hardest remaining premise in the primary conditional-theorem route is still existence/coincidence of exponents for a concrete iid lattice law. The oscillating-scale example in ATTEMPT.md targets only abstract attempts to replace that premise with balance identities.
