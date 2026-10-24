# Scoped independent reconstruction of the compatible Gibbs banks

Source: A052 stage 20261014T044609Z, WEAK_CRITICAL_PROOF.md sections1--3,
claim A052-CRITICAL-WEAK-INFLUENCE-GIBBS-BANK@1. Verdict HOLDS at the stated
new influence-localization and Gibbs/reflection/block-bank scope. Section4's
collision corollary uses an A051-authored earlier premise, so this review
does not count as an independent acceptance of that bundled full chain.

For a physical singleton, conditional entropy B_i<=h2(d_i) and the scalar
row channel estimate J_i<=kappa beta_i<=kappa d_i give R d_i<=L_i<=h2(d_i)
+kappa d_i whenever all children have ratio<=R. The strict inequality
-(1-d)ln(1-d)<d gives d_i<exp(3)2^-R for 0<d_i<1. If d_i=1, all Fourier
mass includes i, B_i=J_i=0 and physical criticality with R>0 is impossible.
For a minimal K-violation the identical step keeps D+S_i>0. No optimization
in infinite dimension is used here.

Reconstruct the bank from the normalized reference directly. Let
rho/(1-rho)=2^(lambda-K), r=-log2(1-rho). Expanding binary KL yields
h2(e)-(K-lambda)e=r-KL(e||rho). The physical decrement is sum q(h2(e)+j),
and d_i=beta_i+O_i. Subtract Kd_i and substitute this scalar identity:
D+S_i+K O_i+Lambda_i+A_i=r exactly, with no missing child or normalizer.

On a four-atom retained row, sum of the two conditional KLs equals joint
KL plus mutual information: the reference energy counts each inclusion
once; H(i|j)+H(j|i)=H(i,j)-I(i;j). If conditional inclusion p exceeds1/2,
reflecting to e=1-p changes KL by (K-lambda)(2p-1); its weighted sum is
exactly (K-lambda)O_i. This proves the compatible identity (5). Adding
the two singleton banks then leaves lambda(O_i+O_j), not K(O_i+O_j),
and produces (6). Both banks share one fixed rho; no conditional reflection
is silently treated as a global product reference.

For an a-coordinate block, expand the full product-reference KL as
a*r-B_A+(K-lambda)I_A. Substituting the exact physical child identity gives
D+S_A+G_A+lambda I_A-J_A=a*r. The source reconstructs J_A<=kappa I_A
using entropy tensorization and the elementary two-point inequality;
its derivative argument has the correct factors: natural Ent(w^2) is at
most twice the sum of squared Walsh derivatives. Thus the channel gap is
nonnegative when lambda>=kappa. Critical nonnegativity of D and S_A is
used only for proper cuts and least-essential-dimension threshold witnesses.
The tail bound is Markov's inequality applied to increasing binary KL
on e>=u>rho, with positive denominator. These identities remain signed
on arbitrary roots and do not themselves imply selected-block payment.

No source finite assertion count is adopted. The reconstruction supplies
no repair and has no contributor conflict on the new sections1--3. Existing
A053 full-scope acceptance is read as a separate source receipt, not as
a substitute for this derivation.
