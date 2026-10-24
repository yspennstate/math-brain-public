# P0321 statement packet (send before proof)

Date: 2026-10-10. Author: w540. Independent adversary: w541. Referee: w542.

The dated ranking row is tier 5, P0321, "Existence of a hexatic phase for two-dimensional Riesz gases", status unsolved. This is a historical label, not a current-status certificate.

Primary source recovered: Mathieu Lewin, *Coulomb and Riesz gases: The known and the unknown*, arXiv:2202.09240v2, section VI.2, https://arxiv.org/html/2202.09240v2#S6.SS2 . Its qualitative hexatic criterion combines rapidly decreasing positional correlations with slower sixfold bond-orientation correlations. It discusses numerical evidence for s=0 and s=1, as well as short-range exponents. This paragraph is a physical prediction, not a quantified theorem or a complete definition of its observables. The exact short excerpt is recorded once in SOURCE_STATUS.json.

Model convention for a proposed precise subtarget: classical points in R^2 at density rho=1, interaction V_1(x)=1/|x|, beta in a nonempty open interval of positive inverse temperatures. Finite-volume energies include a neutralizing uniform background; an infinite state must be identified by a specified thermodynamic limiting construction and equilibrium specification. No bare infinite sum of pair energies is used. The logarithmic s=0 case and all-exponent statements are outside the first subtarget.

The recovered canonical card gives the full campaign formulation: "Prove or refute the intermediate hexatic phase predicted in two-dimensional Riesz-gas phase diagrams, distinguished by orientational order and absence of crystalline positional order." Card logical ID: math:probability.core:open-problem-p0321-existence-of-a-hexatic-phase-for-two-dimensional-riesz-gases. Its source locator is Lewin 2022, Section VI.B, PDF 66-67; the verified HTML counterpart is VI.2. The PDF page locator itself was not independently checked. The card explicitly labels current status unverified.

The source does not give fully quantified phase observables. The following is a *chosen sufficient, narrower subtarget*, not an assertion that the source states this exact proposition. It makes the classical s=1 route reviewable.

Take square boxes Lambda_L, N=L^2 integer, density-one background, and the canonical Gibbs law proportional to exp(-beta H_L) dx_1...dx_N/N!, where

    H_L=sum_{i<j}1/|x_i-x_j| - sum_i integral_{Lambda_L}1/|x_i-y|dy
                         + (1/2) integral_{Lambda_L x Lambda_L}1/|x-y|dxdy.

The self energies are excluded in the particle sum. A limiting state must come from bulk local limits of these laws (spatially averaged bulk centers are allowed), have intensity one, and satisfy a stated jellium equilibrium specification. Existence of thermodynamics alone is not this last identification.

For a simple, locally finite configuration in general position with finite positive Delaunay degrees, define at each particle x

    psi_6(x)=(1/deg(x)) sum_{y Delaunay-neighbor of x} exp(6 i arg(y-x)).

Require these geometric conditions almost surely. Suppose the stationary limit has a positive pair density rho^(2)(0,x) and well-defined two-point Palm laws. Define the angularly averaged bond correlation C_6(r) as the average over directions u of E^{0,ru}[psi_6(0) conjugate(psi_6(ru))]. Define D(r) as the directional average of |rho^(2)(0,ru)-1|. An explicit sufficient phase criterion is: for each beta in a nonempty open interval I, there are eta(beta) in (0,2), delta(beta)>0, r_0, and finite positive c,C such that for every r>=r_0,

    c r^(-eta) <= |C_6(r)| <= C r^(-eta),     D(r) <= C r^(-2-delta).

The first quantity tends to zero but is not integrable against r dr; the second is integrable at infinity. This chosen criterion permits summable algebraic density tails. It is stronger and more specific than the source's qualitative wording; no equivalence with every possible notion of hexatic order is claimed. No universal exponent or exponential decay of all density correlations is imposed.

Reserved lemma boundary: quantitative transfer of algebraic sixfold vertex correlations from a screened angular effective field to a microscopic bond observable. A scale-independent additive error by itself cannot establish a lower bound at arbitrarily large separation. Errors vanishing with volume at each fixed separation can instead disappear when the thermodynamic limit is taken first. The proof attempt specifies both this iterated limit and a uniform scale-decaying error criterion. It does not infer defect proliferation from spin waves. Narrow claim receipt: clm-787096d890, resource topic:P0321:connected-cumulant-transfer.

Hardest input anticipated: a volume-uniform microscopic effective-field/defect estimate on an actual nonempty beta interval that has a nonzero bond amplitude, allows dislocation screening, controls disclinations, and has errors below the algebraic correlation scale. This is unproved. Current openness is UNKNOWN pending local solved/retired checks and a bounded primary-literature search; no novelty claim is made.

Current source-check outcome: openness remains UNKNOWN. The exported problem/attempt cards and a bounded primary-literature search supply no solved/retired certificate, and the search is not exhaustive.

NEXT: Check L1-L3/C1-C2 independently; then attempt a microscopic anchored connected-defect estimate compatible with the specified Palm bond observable.
