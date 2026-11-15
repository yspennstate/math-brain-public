# Referee of FLOW section 12

Source read in full: ~/fei_solve_agent/FLOW.md, as present at worker start on 10 November 2026. The verdicts distinguish displayed core statements from adjacent explanatory sentences.

| Claim | Verdict |
|---|---|
| 12(b), E_i<=L_i^pi | PROVED. This is conditional-entropy data processing for the deterministic last-position label. |
| 12(b), martingale representation | PROVED. Conditional expectation retains characters supported on the revealed set; its orthogonal increment consists exactly of characters whose last revealed member is the new coordinate. The constant bin is separate. |
| 12(b), weighted-count limit sentence | FALSE if meant as a literal limit of conditional entropies for the exact weighted sum. Superincreasing weights make that sum injective, so its conditional entropy is E_i for every such weight vector. The leading nonzero position is a further coarse-graining, giving L. This does not affect the definition or martingale identity. |
| 12(c), trivial bound | PROVED. Superadditivity gives L<=Phi(1-delta,delta)=h(delta)<=delta log2(e/delta). |
| 12(d), subset shortest path | PROVED. Each permutation gives one maximal chain, every chain gives a permutation, and the objective is the sum of its edge costs including the empty bin. Complexity is (n-1)2^(n-1) per coordinate, excluding polynomial bookkeeping. |
| 12(e), sufficient two-sequence condition | PROVED. Apply the dyadic-head lemma of 11(c), using max(M,1) to cover K=0. Here |E h|<=E|h|=delta, so B0<=delta^2 and A_total<=1. |
| 12(e), pair identities | PROVED. The identities and their two different sharing prefixes are correct; derivation below. |
| 12(f), random-order tribes estimate | GAP as written. It is explicitly a hand estimate, and the phrase "Stay is about delta^(2-t)" suppresses the contribution of the other tribes. The claimed width loss is plausible; the supplied text contains no uniform asymptotic proof. No result in this report depends on it. |
| 12(g), exact E composition formula | PROVED. Separate nonempty inside remainder from empty inside remainder and use homogeneity. Independently checked in audit.json. |
| 12(g), comparison with biased erasure | FALSE if read literally as the unnormalized last sum being at least biased erasure. With t=c^2/(1-r^2)<=1, the last sum is at most the biased erasure, by monotonicity. Its ratio to t is at least the biased erasure, by concavity/homogeneity. |
| 12(g), filtration splitting with outside first | PROVED. The formula is in PROOFS.md. The target-block exchange additionally proves that an optimal order of this form exists. |

For the pair identities, let P be the conditional-resampling operator sharing a fixed revealed set. For g=E_i f and h=D_i f, E g^2=1-delta and g^2+h^2=1 pointwise. For the prefix of length K-1,

    A_{>=K}=E g(y)^2-E g(y)g(y').

On a nonpivotal/pivotal pair the integrand contributes 1 from the first marginal; on two nonpivotal points of opposite g-signs it contributes 2; on matching nonzero signs it vanishes. Exchangeability handles the marginal form, giving exactly

    A_{>=K}=P[y pivotal, y' not pivotal]+2 P[g(y)=-g(y') !=0].

The displayed first probability can equivalently use the reversed orientation. For the prefix of length K,

    B_{<=K}=||E[h | first K]||_2^2=E h(y)h(y').

This quantity is nonnegative even when h has both signs, but it is not in general the probability of simultaneous pivotality; it is only at most that probability. Thus a bound Cross_(K-1) Stay_K<=M' delta^2 is sufficient with M=1+2M'. The two prefixes must not be identified.

An explicit counterexample to the unnormalized sentence in 12(g) is outer F(u,z)=u with a dummy z, and inner g=AND_2. Here r^2=c^2=1/4 and v=1-r^2=3/4. The last sum is Phi(1/4,1/4)=1/2 bit, while the biased outer erasure is Phi(1/4,3/4)=h(1/4), which is larger. Dividing the last sum by t=1/3 repairs the stated direction.

The filtration two-sequence constant is correct, but it is sufficient rather than necessary. Address functions already have F=0 while their M can grow. Also, the final assertion in 12(i) that section 11 proves the maximum-position witness for thresholds is a GAP in the cross-reference: section 11 proves the degree-count witness. PROOFS.md supplies a separate deterministic-tail argument for the filtration statement.

audit.json records independent truth-table checks of the entropy bounds, martingale energies, both pair identities, the shortest path against every permutation in its stated small scope, and the E composition formula. The arguments above establish the mathematical claims; the sampled checks alone do not.
