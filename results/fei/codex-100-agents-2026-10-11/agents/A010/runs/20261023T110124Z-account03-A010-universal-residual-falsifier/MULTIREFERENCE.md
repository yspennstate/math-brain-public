# An exponential reference budget still fails

All logarithms are base two. Define U(X) as the AND of r=2^w disjoint width-w OR clauses, V(Y)=1-U(-Y) on an independent clone, and F=2UV-1. For every integer w>=64, consider any fixed normalized mixture containing at most floor(2^(w/4)) ORIGINAL complete positive-prime queues of F, and any finite or countable collection of its original complete negative-prime queues. Each queue has its own arbitrary positive feasible packing vector, arbitrary allowed ordered covers, its own original root normalizer and its full finite successful output law. Then

    C_mix(F)/I(F) > w/2592,

uniformly over every such choice. In particular the infimum over this entire bounded representation class diverges. Optimizing the posterior over reference names AND actual runs is already included in the mixture output law. Nevertheless H(F)<8I(F). This is a coding-route obstruction, not an FEI disproof, and it does not refute unrestricted representations or unrestricted positive-reference mixtures.

## Source-bound input

A008-RARE-CHILD-MOMENT-AND-FIXED-POLARITY-MIXTURE-OBSTRUCTION@1, hash 8665cf2638011cb0dffa64b7c0cad0b347746eeb92dc2541e4bbc262ce55e6e5, proves the marked-tree lemma and the actual family identities. REVIEW_A008.md reconstructs its complete proof without repairs. We use the lemma: for total marked packing weight t, total root activity A0, z>=1 with zt,zA0<=1/16,

    E[1_success z^(R-1+M)] <=16/19.

Here M counts every marked child visit, including repetitions; R counts all initial roots. The original conditioned law and all finite successful runs are retained.

## Simultaneous good clauses

Let L>=1 be the actual number of positive references. For positive reference ell, let t_(ell,D) sum the packing weights of prime names using Y clause D. Every positive prime consists of one X-transversal and one whole Y clause. The packing rows in any fixed X clause imply

    sum_D t_(ell,D) <= w.

Thus fewer than r/(2L) clauses have t_(ell,D)>2Lw/r. The union of bad clauses over all L references has size less than r/2. There are at least r/2 common good clauses D, simultaneously for every positive reference; this is a union bound on the full predetermined dictionaries, not an A-dependent choice of weights.

Every positive prime has rarity pi=2^-(r+w), hence A0_ell<=pi*w<=w/r. On a common good D define

    z_ell=1/[16(t_(ell,D)+A0_ell)] >= r/(48Lw)=Z.

Whenever Z>=1 this satisfies the marked-tree hypotheses. For a target A contained in one X clause C and one common good Y clause D, with kX selected X coordinates and kY selected Y coordinates, every successful positive run satisfies kX<=R+M_D. A new X_C coordinate beyond those supplied by roots must be reached across a Y_D attachment, whose child prime has clause name D. Markov's inequality on the FULL marked-tree moment gives

    Q_(+,ell)(A) <= Z^(-(kX-1)).

For every negative reference, without any restriction on its weights/orders or on D, the induced target has one X component and kY separate Y components. The necessary-root product bound gives

    Q_-(A) <= 2^(-(r-1)kY).

These bounds hold on the SAME target sector for ALL summands, so any normalized finite/countable mixture obeys their maximum. No union bound over negative references is required, and there is no factor L in output mass. In particular reference priors may be unequal or zero, but must be fixed before sampling A. A mixture with no positive references satisfies the negative bound alone, using all clauses D.

## General budget tradeoff and all-size specialization

Let a=ceil(w/2)-1, and assume Z>=1. On the sector kX>=ceil(w/2), kY>=1, the cost per target is at least

    B=min{a log2[r/(48Lw)], r-1}.

Every such target has actual Fourier mass 4r^-4 p^(4(r-1)), p=1-1/r. There are r choices of C, at least r/2 common good D, at least r/2 central nonempty X subsets and r-1>=r/2 nonempty Y subsets. Thus the sector has total mass at least (1/2)p^(4(r-1))>1/162. Physical pivotal counting gives I(F)=2w p^(r-1)<2w. Consequently

    C_mix(F)/I(F) > B/(324w)              (when B>0).

For w>=64, (48w)^4<=2^w. At w=64 the inequality is integer arithmetic; the ratio grows because 2w^4>(w+1)^4 for w>=64 (expand the difference, or use (1+1/w)^4<2). Hence 48w<=2^(w/4). If L<=2^(w/4), then Z>=2^(w/2), a>=w/4, and r-1>=w^2/8, so B>=w^2/8. This proves the displayed w/2592 bound. The last exponential-versus-square inequality follows at w=64 and increases by induction, since 2(w^2+8)> (w+1)^2+8 for w>=3.

The choice of common good clauses may depend on the entire fixed representation, but their Fourier masses and the lower bound do not. Taking the infimum over all such representations therefore preserves the inequality. This is the exact quantifier needed to distinguish a variational obstruction from the failure of a chosen vector.

Explicitly, on a fixed target A, assign each actual pair (reference ell, successful run h) its joint mass alpha_ell*q_ell(h). Their sum is Q_mix(A). If Q_mix(A)>0, normalizing those masses gives a probability rho_A. The relative-entropy form of the posterior objective is -log2 Q_mix(A)+KL(eta_A||rho_A); its infimum is exactly -log2 Q_mix(A). This definition also avoids subtracting two infinite entropies on countable run spaces. When Q_mix(A)=0 the cost is infinite. Consequently neither selecting another posterior nor retaining only some admissible runs can lower the full-law optimum established here. The outer variational infimum over the stated fixed references/vectors/orders/priors is separately covered by the uniform common-sector bound.

## Boundary of the conclusion

The allowed positive-reference budget grows exponentially in w, so any fixed budget or budget polynomial in w is eventually included. This does not mean an arbitrary polynomial in physical dimension n=2w*2^w. The proof offers no diverging bound once L is comparable to r/(48w): the common-good-clause estimate then stops forcing a rare child label. An unrestricted mixture can specialize dictionaries by clause and must be evaluated separately with its actual reference-name payment. No claim that such a mixture succeeds is made. Nonprime gates, a shared clause tag transmitted once per spectral set, and general joint-set codes are outside the refuted class. This explicit boundary is the first unsupported universal line, rather than evidence against FEI.
