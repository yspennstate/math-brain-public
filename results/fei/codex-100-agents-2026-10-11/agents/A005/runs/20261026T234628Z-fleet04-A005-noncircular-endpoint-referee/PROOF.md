# Child deficits must be measured against the original influence

All entropies are in bits. Let f be a nonconstant Boolean function with n>=2 relevant physical coordinates. Fix K>=0 and write D=H(f)-K I(f). For each i let f_i^+,f_i^- be its complete physical children, and let a(g) be the minimum physical influence over invertible affine input maps and output characters. Define

    s_i = average_b [K I(f_i^b)-H(f_i^b)],
    t_i = average_b [I(f_i^b)-a(f_i^b)],
    s_i* = s_i-K t_i,
    N* = sum_i max(-s_i*,0).

The average is uniform, including constant children. No spectral components or discarded rows enter these quantities. t_i>=0 since the identity map is permitted. Let B_i=H(S_i|S_{-i}) for the squared Fourier law, J_i=H(f)-average_b H(f_i^b)-B_i, and T=H(f)-sum_i B_i, the dual total correlation. Then

    T+(n-1)D+sum_i s_i*+K sum_i t_i = sum_i J_i.             (1)

Consequently, with c=2/ln(2),

    N* >= (n-1)D+T+K sum_i t_i-c I(f).                     (2)

This is a lower bound on necessary negative reserve, not a payment theorem. Its right side can be negative.

In fact, if P*=sum_i max(s_i*,0), then N*=(n-1)D+T+K sum_i t_i-sum_i J_i+P* exactly. The branch-resolved debt sum_i average_b max(H(f_i^b)-K a(f_i^b),0) is at least N* by convexity, so (2) also lower-bounds that stronger quantity.

Proof. Physical restriction gives average_b I(f_i^b)=I(f)-Inf_i(f). The entropy restriction identity gives s_i=K I(f)-K Inf_i(f)-H(f)+B_i+J_i. Sum over i, use sum_i Inf_i=I, and substitute s_i*=s_i-K t_i to obtain (1). The standard Boolean row inequality J_i<=c Inf_i gives sum J_i<=c I. Since N*>=-sum s_i*, (2) follows. T>=0 follows from the chain rule: conditioning S_i on all other coordinates decreases entropy relative to conditioning only on preceding coordinates. All sums are finite. Relevant n excludes artificial dummy inflation, though (1) itself also holds with dummies.

In particular, put eta=N*/(n I(f)). Division is legitimate because f is nonconstant. Then

    H(f)/I(f) <= K + [c+n eta]/(n-1),                      (3)

with the stronger bound retaining T and the affine release term in (2). Thus a sequence with relevant n tending to infinity and N*=o(n I) has limsup H/I<=K. More quantitatively, a ratio limit R>K forces liminf N*/(n I)>=(R-K). Any proposed same-K arbitrary-seed embedding into this normalized near-critical endpoint is impossible for a seed of ratio R>K. This is conditional on that seed; it asserts no FEI counterexample exists. A ratio-preserving embedding that does not grow relevant dimension is not excluded by this limit argument.

The ingredients that could fail are the restriction sign, the use of a complete Boolean child, the affine-release sign, the nonzero denominator I, and the relevant-dimension limit. The finite validation includes constants (identity only), n=1 (identity only), dummy coordinates, K=0 and positive/zero/negative reserves. The ratio conclusion uses n>=2 and I>0; K>=0 is needed when dropping K sum t_i. An arbitrary probability law cannot replace Boolean restriction: J_i<=c Inf_i is specifically the Boolean two-child row bound C005, independently derived by B17 in the board's packet-scalar entry. No infinite sum or integral is interchanged.

The normalization matters. The old rare-core examples can have every displayed negative reserve tending to zero in absolute value while retaining positive normalized debt. Absolute smallness is therefore not a substitute for (3)'s hypothesis. This conclusion uses the previously established embeddings only for interpretation, not to prove (1)--(3).

# Scoped independent review of A052's rank rigidity

Source: A052 stage11 REPORT.md, derivation items 1--4 and claim A052's corresponding CLAIMS.json. Its claim is conditional on gamma=2^(1-d)-4 delta>=0 and m=K gamma-1>0. The proof can be reconstructed through the annihilator of support differences: the constant-derivative subspace has codimension r; a basis has at least r directions outside it; on those directions the centered cost rises by at least gamma. Outside-coset spectral mass is preserved by convolution with the phase, so entropy rises by at most r. Hence H(g)-K I(g)<=H(f)-K a(f)-m r. Comparing with a competitor within epsilon gives m r<=epsilon. epsilon<m excludes r>=1, and a one-point Fourier support phase is a signed character. At epsilon=m the strict exclusion is not available. gamma>=0 is used when replacing the number of active basis directions by r; m>0 is used in division. Affine input maps preserve entropy and polynomial degree. Constants and output characters have r=0 and cause no zero-influence division. This accepts the analytic corollary at that scope, not the giant certificate or the entire embedding chain. Finite checks are recorded separately; independent review of the new normalized-deficit consequence remains pending.

# First unpaid universal line

Exact nonnegative optimized complete-child reserves imply N*=0, but (2) only bounds a possible positive gap by c/(n-1); it does not exclude that vanishing-gap regime. Nor does it select or pay an original pair. One must still prove that a genuine least-dimensional positive K witness has an original proper pair whose complete mixed-row entropy cost and phase price, together with old debits, are funded from the same nonnegative child reserves and unused independent quotient-rank release. No reset, new owner, or replacement of a full child by a component is licensed by (1).
