# One root normalizer for an arbitrary disjoint conjunction

All logarithms are base two. This is an exact supplied-reference identity, not an assumption of FEI or a universal choice of a good dictionary.

Let U_i, i=1,...,m, be nonconstant {0,1} indicators on pairwise disjoint uniform blocks, a_i=E U_i in (0,1), g_i=2U_i-1, and a=prod_i a_i. Set F=2 prod_i U_i-1 and v=4a(1-a). For each block fix any positive normalized reference q_i on its nonempty subsets. Write C_i=sum_{S nonempty} ghat_i(S)^2 log(1/q_i(S)). These references and all means are fixed before the target set.

Activate blocks independently with probabilities 1-a_i, condition the entire activation mask on being nonempty, and draw a local nonempty set from q_i in each active block. For nonempty A, J={i:A_i nonempty}, the FULL normalized output probability is

    Q(A) = [prod_{i in J}(1-a_i) q_i(A_i)
                 prod_{i notin J}a_i]/(1-a).                 (1)

Summing the local q_i and then nonempty masks gives exactly one. Every factor in (1) is paid; its negative log includes the NEGATIVE root term log(1-a). No root normalizers of different references are pooled.

Define phi(t)=4t h2(t), and C_F=sum_{A nonempty} Fhat(A)^2 log(1/Q(A)). Then

    C_F = sum_i (a/a_i) C_i
             + 4a[sum_i h2(a_i)-h2(a)],                    (2)
    I(F) = sum_i (a/a_i) I(g_i),                           (3)
    C_F + phi(a) = sum_i (a/a_i)[C_i+phi(a_i)].             (4)

Proof of every cost factor: the squared Fourier spectrum of indicator U_i, divided by a_i, is a probability measure mu_i. Its empty mass is a_i, and on nonempty sets it is ghat_i(S)^2/(4a_i). Disjointness makes mu=prod mu_i the normalized indicator-product spectrum. For nonempty A, Fhat(A)^2=4a mu(A). The local q_i length therefore has total coefficient (a/a_i) C_i: sum over the other blocks is one, and a nonempty A_i already excludes the global empty event. The unconditioned activation-mask entropy is sum_i h2(a_i). The all-inactive event has mass a and length -log a. Removing it leaves sum_i h2(a_i)+a log a. Conditioning the mask contributes (1-a)log(1-a). Multiplying by 4a gives exactly the bracket in (2). Thus the negative normalization cancels the ENTIRE global h2(a), not just an O(v) estimate. Omitting it would destroy (4). Direct pivotal counting gives (3), because a pivotal coordinate in block i changes F precisely when every other U_j is one. Equation (4) follows algebraically from (2).

## Arbitrary root activities: the exact paid mismatch

The reference may instead use ANY fixed inactive probabilities theta_i in (0,1). Put B=prod theta_i, and replace a_i by theta_i in (1), including the denominator 1-B, while leaving the local q_i unchanged. Write d(s||t)=s log(s/t)+(1-s)log((1-s)/(1-t)). Its complete cost C_theta obeys

    C_theta + phi(a)
      = sum_i (a/a_i)[C_i+phi(a_i)]
          +4a[sum_i d(a_i||theta_i)-d(a||B)].              (5)

The bracket is NONNEGATIVE, and equals (1-a) times the KL divergence between the two product activation-mask laws CONDITIONED NONEMPTY. Indeed their unconditioned KL is sum_i d(a_i||theta_i). Split its sum into the all-inactive atom and its complement. The atom contributes a log(a/B). On the complement, passing to the normalized distributions adds (1-a)log((1-B)/(1-a)). Subtracting the binary KL d(a||B) gives precisely this expression. Conditional KL is nonnegative by -ln x>=1-x summed against the first probability law. This proves both (5) and its sign without an unsupported independence step after conditioning.

The negative binary term includes the signed root contribution v log(1-B), v=4a(1-a); it cannot be discarded when assessing rare-root payment. With m=1, the WHOLE bracket is exactly zero for every theta_1, including arbitrarily rare reference activation. Thus the raw single-root rarity is completely refunded by conditioning. With multiple blocks the remaining conditional-mask KL, not the sum of unconditioned rarity costs, is the exact unpaid quantity. No uniform influence bound for arbitrary theta is asserted. The earlier A007 all-reference KL retuning obstruction is not contradicted.

## Nested conjunctions: no repeated sector tag

Consider any finite rooted tree whose internal nodes are conjunctions of their children and whose leaves are the supplied disjoint indicators. Use rule (1) at each internal node, with that node's actual mean. Let a_B=prod_{i in B}a_i be a child-subtree mean. If B is active, its inner activation probability for a particular nonempty leaf mask is prod_{i active}(1-a_i) prod_{i inactive}a_i /(1-a_B). The factor 1-a_B in the parent's activation numerator cancels its inner denominator EXACTLY. If B is inactive, its probability a_B equals the product of all inactive leaf probabilities. Induction gives precisely the flat distribution (1), for every output and every tree shape. The only remaining denominator is 1-a at the root.

Consequently (4) telescopes at all levels. More generally, for arbitrary leaf theta_i, assigning each internal inactive probability the product of its leaf theta_i makes the nested reference equal the flat theta-reference; the SAME cancellation leaves just 1-B. Formula (5) then gives the complete remaining mismatch at the root, rather than a separate header per level. If supplied leaves satisfy C_i+phi(a_i)<=K I(g_i) for one common K, then the matched reference satisfies C_F+phi(a)<=K I(F), uniformly in m and tree depth. For m=1 the identity is tautological. This removes accumulated uniform sector labels for conjunction-only nesting. Complementary OR-only nesting has the identical statement applied to 1-U_i, with phi(1-a_i). An alternating AND/OR tree changes the potential when polarity changes; no free cancellation or universal bound for such switches is asserted.

This proof does not use the actual nonempty spectral laws as q_i. Only scalar means choose the mask. The actual laws compute the code cost, just as a pivotal formula computes influence. Choosing q_i still requires a paid root reference. The condition C_i+phi(a_i)<=K I_i is stronger than C_i<=K I_i; it must never be silently substituted. A full empty/nonempty wrapper would add h2(v), also not silently free.

## Physical overlap: the exact first unsupported line

If virtual coordinates are identified by a map pi, the Fourier coefficient on physical A is the SIGNED sum of virtual coefficients over all S whose coordinate image has odd-multiplicity set A. Its square is not the pushforward of virtual coefficient squares. Thus the product spectral law used in (2) fails before any cost comparison.

An exact two-bit certificate: let U=V=OR2 on the SAME two physical variables. The actual product UV=U, so I(2UV-1)=1, whereas the false independent formula gives (3/4)*1+(3/4)*1=3/2. More strongly, first construct the genuine four-bit virtual F0=2 OR2(X) OR2(Y)-1, then identify Y=X. Its squared spectrum pushed forward by parity of coordinate identification is (1/16,5/16,5/16,5/16), indexed by empty and the three nonempty subsets. The ACTUAL physical squared spectrum is (1/4,1/4,1/4,1/4). Direct Walsh summation checks both, while signed alias sums correctly recover the physical coefficients. A normalization scalar cannot repair these nonconstant likelihood ratios.

The first unsupported universal step is to bound the signed alias/interference contribution and its reference normalization using the SAME physical influence account. The disjoint telescope gives an exact normalization target for that step, not a proof under overlap. Full FEI remains OPEN.
