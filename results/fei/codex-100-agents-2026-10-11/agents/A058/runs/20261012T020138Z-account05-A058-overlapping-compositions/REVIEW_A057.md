# Independent review of A057-CAPPED-RECENTERED-ACTIVATION-TREE-BANK@1

Source: A057 run 20261012T003930Z-account05-A057-coherent-restriction-remainder, PROOF.md and CLAIMS.json. Earlier A057 v1 claims were already independently reviewed by A059/A087 and are not reopened. This is a review of the new capped-bank price, not a third broad candidate. Reviewer A058 supplied no source repair and has no author contribution to the reviewed version.

## Analytic reconstruction

I reconstruct the state price as the minimum of two branches, and use only its second branch for the bound. Let p=2^-r, m be the actual restricted core mean, v=1-m^2, t=beta^2, d the physical influence. Set c=1/ln2 and c0=2/(e ln2). Then

M(v)=Phi((1-p+pm)^2,p^2v)+p(1-p)Phi((1-m)^2,v).

The exact physical positive-sector formula is B_i(activated core)=p[B_i(core)-Phi(m^2,t)]+M(t). The negative empty-core pair is essential; finite replay uses the actual physical Fourier transform, not the induced-output gate alone.

The packet estimate Phi(s^2,t^2)<=2st is valid: at z=t/s<=1 the derivative of its natural-unit ratio has sign (z^2-1)ln(1+z^2)-z^2ln(z^2), nonnegative by ln(1+z^2)<=z^2 and -ln(z^2)>=1-z^2. The ratio increases to ln2 at z=1. The second scalar estimate Phi(A,B)<=B log2(e(A+B)/B) follows from A ln(1+B/A)<=B. Both cover zero limits.

The shifted row satisfies (1-p+pm)^2+p^2v=1-2p(1-p)(1-m)<=1. Therefore the second cap branch is at most

4p(1-p)d + p^2(2r+c)t + p t log2(1/t).

Here the coefficient 4 uses t/sqrt(v)<=|beta|<=d and 1-m<=2. The potentially dangerous variance logs have been combined before an inequality:

p^2t log2(1/v)+pt log2(v/t)=pt log2(1/t)+p(1-p)t log2(v).

The last term is nonpositive. Moreover t log2(1/t)<=c0|beta|<=c0 d, and t<=d. Weighting along any actual core-query prefix gives

C_prefix <= [4p(1-p)+cp^2+c0p] Pi_I +2rp^2 V_drop.

This uses two separate exact telescopes: sum w d=Pi_I and sum w beta^2=Var(root)-E Var(leaf). It does not spend terminal influence repeatedly. At complete core leaves, V_drop<=2a, a=1-Eu, and p<=1/2. Thus C_prefix<= (4+c0)pI(u)+2rp a. The control suffix occurs as an r-bit point defect with probability a/2. Its local erasure/queried-influence ratio is at most

2(1-delta)+delta(2l+c)<=3, delta=2^-l, l=s-1>=1;

the last step uses 2l/2^l<=1 and c<2. The one-bit endpoint has zero erasure. Suffix influence is exactly rp a, so its erasure is at most 3rp a. This reconstructs the claimed complete bound (4+c0)p I(u)+5rp a <= (4+c0)I(activation), since c0>1. An explicit rational check is e<11/4, ln2<7/10, hence e ln2<77/40<2.

All prices and cancellation are in bits. A scalar estimate in natural units would miss a factor ln2. The theorem deliberately leaves the nonempty inner decrement, arbitrary pH(u), and partial-tree terminal entropy unpaid. It cannot be extended to reused controls without reconstructing M and its reserve ownership.

## Review verdict

The analytic argument HOLDS at its stated scope; the reviewer has supplied no mathematical repair. Acceptance is contingent only on the source-defined scope, not on a universal stopping-tree payment. The fresh actual-activation replay specified in out/REVIEW_FROZEN_SPEC.json is recorded separately in out/review_results.json before final status is written. No adoption in shared registries or a second complete-chain full-FEI review is claimed.
