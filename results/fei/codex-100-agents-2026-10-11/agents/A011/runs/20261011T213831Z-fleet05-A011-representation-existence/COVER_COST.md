# Complete joint cost

For a fixed selector tree and fixed leaf codebooks, transmit the physical
leaf word, the leaf's spectral witness, then one selector-frequency bit
per queried coordinate on that path. The length at leaf ell is
2 d_ell + L_leaf. The true recursive witness law has fair physical child
choices, so its expected cost is 2D + sum p_ell c_ell.

| Obligation | Complete payment |
|---|---|
| Root/used gate label | Leaf path: d_ell bits, expected D; paid once |
| Gate existence | Explicit C_ell AND [g_ell=1] cover; cells partition selectors |
| Support dictionary | Fixed tree identifies all queried coordinates and leaf support |
| Coordinate order/rank | Known root-to-leaf order; no rank is omitted from a varying dictionary |
| Selector Fourier subset | d_ell binary membership choices; expected D |
| Data Fourier subset | Complete leaf code, expected sum p_ell c_ell |
| Attachments/children | Fixed tree dictionary; no runtime forest/child label choice |
| Global normalizer | Kraft sum <=1 exactly; no scaling/conditioning penalty |
| Duplicate witnesses | Retained in true joint law; output decoder sums their masses |
| Posterior entropy | H(S)=H(W)-H(W|S); no equality to mixture entropy is assumed |
| Empty output | Included by decoder; no separate h2(variance) is silently discarded |
| Parameter prior | One fixed codebook per represented function; no mixture prior |

Every static dictionary is fixed before the spectral set is sampled, as in
the campaign's existing references. This is an expected whole-set code,
not a claim that the function description itself has length O(I).

The true law is sampled using exact signed Fourier coefficients of actual
children. At a queried coordinate, q_T=(u_T^2+v_T^2)/2 and
theta_T=(u_T-v_T)^2/(4q_T). These coefficients can be obtained by finite
truth-table enumeration. No polynomial-time construction is asserted.
The code length does not require transmitting theta or an adaptive prior.

Alternatively push Kraft weights through the decoder:
Q(S)=sum_{w: decode(w)=S} 2^{-L(w)}. Then sum Q<=1 and
-log2 Q(decode(w))<=L(w) for every witness. Therefore the complete
cross-entropy payment E[-log2 Q(S)] is at most the same joint cost.
This supplies a reference-law handoff independently of Shannon's
prefix-code inequality.

For character leaves the leaf code has length zero, the selector/data
decoder always has a nonempty data set, and the Kraft sum is exactly one.
Influence payment requires B>=beta D and gives 2D<=4 I_sel/beta.
For general coded leaves, I_sel>=gamma D and c_leaf<=K I(leaf) give
max(2/gamma,K) I(F). Selector and data influence are spent separately once.

The original Proposition 5.5 queue is not this codebook. No bound on its
variational minimum has been established here. Distinct character cells
alone are already the affine-selector baseline and are not counted as
new mathematics; the repeated-label case retains coherent collisions.
