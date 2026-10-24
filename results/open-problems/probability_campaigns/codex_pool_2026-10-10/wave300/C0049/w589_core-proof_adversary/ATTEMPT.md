# C0049 independent adversary checkpoint

Saved 2026-10-10 before opening any w588 proof. Current openness: UNKNOWN pending primary-source recovery. No full FK-to-SLE proof is claimed.

## Independent obstruction: endpoint control is necessary for analytic identification

Let 0 < sigma <= 1 and use Log z with 0 < arg z < pi in the upper half-plane H. For epsilon > 0 set

    F_epsilon(z) = z^(-sigma) (1 + epsilon/z^2).

This is holomorphic in H and continuous on its real boundary except at the marked endpoint 0. For x > 0 its value is strictly positive real. For x < 0 its value lies on the positive ray exp(-i*pi*sigma) R_+. Moreover z^sigma F_epsilon(z) tends to 1 as |z| tends to infinity in H, uniformly in angle. Thus all these functions satisfy the same exact boundary phases and normalization at infinity as F_0(z) = z^(-sigma), but they differ.

Proof: the branch is analytic in H; for real x != 0 the factor 1 + epsilon/x^2 is positive, and the upper boundary argument of x is 0 or pi. The normalization follows directly from 1 + epsilon/z^2. At the starting endpoint, F_epsilon has order sigma + 2, so it violates the extra bound O(|z|^(-sigma)). These elementary identities prove nonuniqueness under the stated analytic assumptions only. They are not a counterexample to an FK scaling limit whose endpoint bounds have been proved.

Even requiring F to be nonvanishing does not repair the inference: F_epsilon(z)=z^(-sigma) exp(epsilon/z^2) has the same phases and infinity normalization and never vanishes in H. Along z=r exp(i*pi/6), its normalized modulus is exp(epsilon/(2r^2)), which is unbounded as r tends to zero. This strengthens the obstruction without imposing an artificial zero in the domain.

Precise sufficient repair, pending w590's independent check: require G(z)=z^sigma F(z) to extend continuously with real boundary values on R except 0, be bounded in a punctured upper neighborhood of 0, and tend uniformly to 1 at infinity. Reflect G to the lower half-plane by G(z)=conjugate(G(conjugate(z))). Schwarz reflection makes the result analytic across every nonzero real point. The boundedness assumption on both reflected sides makes 0 a removable singularity. The resulting entire function tends uniformly to 1 at infinity, is bounded on the remaining compact disk, and hence is constant by Liouville. Thus G=1 and F=z^(-sigma). The uniform growth estimate at 0 is an actual input; the proof does not establish it for FK observables.

NEXT: Recover the exact primary-source parafermionic normalization; determine whether an endpoint estimate or an equivalent full-domain bound is missing from the paired proof.
