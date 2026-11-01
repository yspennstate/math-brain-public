# Scoped adversarial review of w468's tree calculation

Reviewer: w469, 2026-10-10. Peer files read only after the independent checkpoint INDEPENDENT.md and VERIFICATION.json were saved. w470 remains the designated independent referee. Served-model identity is unavailable; no cross-model gate is certified.

Reviewed: ~/brain_workers/w468/TREE_OBSTRUCTION.md and claims w468-C0052-L1 / L2, as read on 2026-10-10. The independent one-edge current control in VERIFICATION.json was generated before this peer read.

Verdict: KEEP the exact finite-tree formulas and the stated failure of graph-uniform LINEAR comparisons. KEEP the scope exclusion for the actual critical Z^3 problem. No proof of C0052 appears in the paired ATTEMPT.md, which still marks source recovery pending.

Independent derivation. On a finite tree, fixing a current's sources fixes the parity of every edge by the source count on either side of its cut. The conditional factorial weight then factors over the edges. On each bridge edge the two original sourced currents are even, and either's probability of being zero is s=sech(t). Their union is present with p=1-s^2. Independent bridge edges give q=p^m. Each separately augmented source cluster also has bridge-edge presence p; the two augmented clusters are independent. If the left open run covers all m edges, the probability contribution is p^m. If its first closed edge is number k+1, for k=0,...,m-1, the contribution to meeting the right run is (1-p)p^k p^(m-k)=(1-p)p^m. Sum the disjoint cases to obtain r=[1+m(1-p)]p^m. The ratio q/r tends to zero at fixed t. For the bare source cluster a bridge edge is present with 1-s; the ratio of its hit probability to the augmented one is [(1-s)/(1-s^2)]^m=(1+s)^(-m). The source-law difference and the constants are correct.

Important boundary of the conclusion: failure of a linear reverse bound is not failure of every quantitative reverse bound. On these same paths q >= (e/4) r^2, as proved in TREE_NONLINEAR.md. Therefore, a positive uniform augmented meeting probability on this family would still force a positive original meeting probability. The counterexample only rejects the graph-uniform linear shortcut, exactly as w468's scope paragraph says. A proposed Ising proof still needs an established comparison under its actual law.

The independence used here is justified by tree parity factorization. This is not an unjustified multiplication of conditional estimates. On graphs with cycles that factorization fails, so the calculation cannot be transplanted to the full Z^3 model.

## Updated original-current kernel packet

The later ATTEMPT.md from w468 (announced at 07:14 UTC) now supplies the actual subcritical endpoint mixture and explicitly isolates UCM as unproved. Scoped verdict: KEEP equations (A)-(G) as a conditional reduction under the stated subcritical current construction and switching identity. This is an author-proof audit; the designated w470 referee and served-model gates remain pending.

Independent verification of the central step: set mu(x)=G(x)/chi and average q(x,y,y+w) over independent X,W with this law. Substituting z=y+w in the original two-current identity gives -g=2 xi^(-3) sum_y E q exactly; the integrated tree-diagram upper bound makes the sum finite. Restricting y to B_floor(xi) gives -g>=2|B|xi^(-3)Q_B. With xi>=1 the stated weaker factor >=2 is valid.

For the original single-current overlap N, its positivity implies source connection in the union. Condition on Y before multiplying probabilities of the two independently sampled components. This gives m1=|B|^(-1)sum_v k(v)sum_y k(v-y), and m2=|B|^(-1)sum_(u,v)k2(u,v)sum_y k2(u-y,v-y). The shared translation Y is conditioned on; joint hits inside each component remain in k2. The diagonal is retained. No within-component independence is assumed.

Cauchy-Schwarz therefore gives Q_B>=m1^2/m2 and -g>=2|B|xi^(-3)m1^2/m2. The assumptions justify this reduction, while proving m2<=C m1^2 is exactly the missing input. A sequence-only version suffices for the source's nonzero-limsup criterion; an all-near-critical bound gives the stronger liminf conclusion. The proof correctly separates them.

The augmented one-site formula averaged over X gives k_aug(v)=G(v), and monotonicity gives k<=G. The deterministic event X=v gives k>=G(v)/chi, including v=0. Thus the chi^2 loss in the available lower first-moment bound is real. Since N is a nonnegative integer, m2>=m1; UCM together with m1>0 would require m1>=1/C. The trivial Y=0 contribution m1>=1/|B| does not provide that scale-independent occupation floor. This is a concrete necessary condition still requiring a model-specific estimate.

No algebraic counterexample was found in (A)-(G). Their explicit unproved UCM is the main obstruction. Applying the exact augmented identity as a lower bound for k, or factoring k2 into two single-hit kernels, would invalidate a future closure; neither substitution occurs in the reviewed text.

NEXT: w470 checks the reductions; derive a scale-independent lower occupation estimate for original-current k and a joint two-hit control for k2 that bounds (E)/(D)^2 after cycle-space mixing.
