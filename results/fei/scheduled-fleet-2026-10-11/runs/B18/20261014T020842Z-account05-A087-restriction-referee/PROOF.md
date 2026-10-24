# Shared controller reveal with unfinished cores (bits)

## Source-bound review: A064 additional version-2 clause

The review covers the additional exclusive-controller lift in A064-TERMINAL-CORRECTED-GLOBAL-DEBT@2, not its bundled old version-1 assertions. At a data-only query the independently reconstructed split is D_F=q[D_u-paird(m,beta)]+M+J. The scalar paird is nonnegative: it is Phi(m^2,beta^2) plus the concavity gap of phi, including zero endpoints. The positive remainder satisfies M+J<=((3+2/e)/ln2)q d+q log2(1/q)beta^2. If the prescribed own-history core potential satisfies D_u<=C d+r-E r_child, then R=sum q r+sum q log2(1/q)Var(u) obeys D_F<=(C+11/2)d_F+R-E R_child. All conditional probabilities are physical fair probabilities. Other-core queries leave the current core history and reserve unchanged, so adaptive interleaving cannot reopen it.

R is nonnegative. The least nonnegative reserve Q for a declared prefix satisfies Q=max(0,D-alpha d+E Q_child), with zero prefix leaves. Finite backward induction gives Q<=R. Separately, D_u>=0 gives E r_child<=r+C d, so actual stopped E R_sigma<=R_root+C Pi_data. This last estimate comes from the core drift and variance supermartingale, not by changing alpha to C in the lifted inequality. Root rarity funding is <=2 I_ctrl by the previously audited original-edge proof.

The rational constant guard is explicit: e>8/3 by its positive exponential series through degree three, and ln2>2(1/3+1/81)=56/81 by the positive atanh series. Thus (3+2/e)/ln2<1215/224<11/2. No floating constant estimate enters the lift.

At a complete-data frontier r=Var=0 but the actual controller entropy remains. Adding the conditional expectation of a prescribed nonnegative controller boundary reserve b is a martingale and grafts the same physical continuation: Q_full<=sum q r_root+2 I_ctrl+E b. It does not discard b or fund it with the already assigned controller account. These additional v2 assertions HOLDS without repair. Earlier bundled v1 claims are not reaccepted by this review. A064's independent review of A087's prior signed-ledger claim is consumed as a reviewer receipt, not self-review.

## A059 interleaved accounting and A091 point payment

For U=sum q[H(u)-phi(m^2)], R=sum phi(q)Var(u), a controller query changes only the selector probabilities. U has zero fair-average drift. R-E R_child=kappa=sum q Var(u) KL(P(query outcome|selector)||fair), by the definition of conditional probabilities q_branch/(2q). Hence kappa>=0 and the previously allocated R is released once. A data query gives R drift=q log2(1/q)beta^2. Exact inner empty-sector cancellation leaves D_F<=U+R-E(U_child+R_child)+(3/ln2)q beta^2. Finite telescoping on the actual interleaved tree retains both the actual terminal H-U-R and all signed controller D-kappa terms. This independently reconstructs the A059@1 equations used here; A091 already reviewed its broader finite census, which is not repeated.

A091-POINT-CONTROLLER-RESIDUAL-AND-BOUNDARY@1 is reconstructed at its stated scope: at a live point activation, B-kappa=za-2z^2+Phi((1-z)^2,z^2), z=q(1-m), a=1-m. This is nonnegative and at most b(z)=2z(1-z)+Phi((1-z)^2,z^2)<=3z. For z<=1/4 use Phi(A,B)<=B log2(e(A+B)/B), A+B<=1; the upper envelope 2(1-z)+z[2log2(1/z)+1/ln2] is increasing and at 1/4 equals 5/2+1/(4ln2)<3. For 1/4<=z<=1/2 use Phi(A,B)<=2sqrt(AB); then use symmetry for z>=1/2. With the full physical JS bound J<=2d/ln2, 0<=D-kappa<=(3+2/ln2)d. The profile identity H-U-R=Eraw(ghat^2)+sum q Var(u)H(Chat^2/q)>=0 follows by separating empty from nonempty data support. At a resolved controller leaf this is phi(m^2)<=Var(u)/ln2<=I_leaf/ln2; at an unresolved frontier it need not be small. This review accepts these explicit clauses without importing an arbitrary boundary payment.

## New one-sided controller reveal

Suppose one physical fair controller bit X kills all nonconstant selected states on one branch, leaving one constant sign there. On the other branch an arbitrary finite exclusive controller selects independent disjoint Boolean cores or constants. Further controller and core coordinates are physically disjoint from X; actual data histories and remaining selectors are used. Flip the whole output if necessary so the killed branch is +1. Write the other branch's empty-data mean profile g(z), bounded in [-1,1], and mu=E g. The actual Boolean query influence is d=(1-mu)/2 because the killed branch is constant. Every nonempty data Fourier row has equal-magnitude X amplitudes, and contributes exactly its core variance-weighted selector mass to B_X. Each corresponding selector doubles its probability on the live branch and vanishes on the killed branch, so the same sum is exactly kappa. Constant states have zero variance.

The remaining empty-data erasure is B_X-kappa=Var(g)/2+Phi((1-d)^2,d^2). Since Var(g)<=1-mu^2=4d(1-d), this is at most b(d)<=3d, and is nonnegative. Adding the full normalized physical JS gives 0<=D_X-kappa<=(3+2/ln2)d. This holds even if the live branch has arbitrarily many exclusive core states and controllers of arbitrary dimension; no private-point multiplicities are needed. It extends the point theorem to any actual one-sided controller-kill geometry. kappa is the owned release, not a new control allowance.

## New controller reveal between two independent branches

Suppose the two actual Boolean X-children F_0,F_1 depend on disjoint physical blocks, each with an exclusive independent-core controller on its own private controls. In particular no core label occurs on both branches. Both controller mean profiles g_0,g_1 depend on disjoint private controls; put mu_b=E g_b and v_b=Var(g_b). Physical child independence gives d=(1-mu_0 mu_1)/2. All nonempty core sectors again contribute B_X=kappa before accounting for the mean profiles, because each core selector is confined to one X branch.

Disjoint private-control Fourier supports give the exact residual

B_X-kappa=(v_0+v_1)/2+Phi(((mu_0+mu_1)/2)^2,((mu_0-mu_1)/2)^2).

The bound Phi(a^2,b^2)<=2|ab| in bits implies this is <=1-(mu_0^2+mu_1^2)/2+|mu_0^2-mu_1^2|/2=1-min(mu_0^2,mu_1^2)<=2(1-mu_0 mu_1)=4d. To justify the last step, let t=min(|mu_0|,|mu_1|); mu_0 mu_1<=t and 1-t^2<=2(1-t). Consequently 0<=D_X-kappa<=(4+2/ln2)d. No branch's control influence is duplicated. This accepts biased/constant endpoints and zero influence by direct formulas.

The scalar packet inequality used above has an elementary proof. By homogeneity set the amplitudes to 1,z, 0<=z<=1. The derivative of [(1+z^2)ln(1+z^2)-z^2 ln(z^2)]/(2z) has numerator (z^2-1)ln(1+z^2)-z^2 ln(z^2)>=0, using ln(1+x)<=x and -ln x>=1-x. Its maximum at z=1 is ln2. Divide by ln2 and scale back. The full physical JS bound is reconstructed by d(t)<=1-sqrt(1-t^2), with d'(t)=atanh(t)<=t/sqrt(1-t^2); differentiation of the difference proves this from zero. These scalar proofs close the constants without floating approximation.

## Priority application and the exact remaining line

For the priority two-core gate from the previous stage, the shared X bit in same orientation has a constant killed branch, so its residual costs at most (3+2/ln2)d. Opposite orientation has two independent private branch functions, so it costs at most (4+2/ln2)d. Both conclusions hold after any data-only partial exposure and after private-coordinate restrictions that preserve the respective geometry. Thus the first unresolved shared-control reveal is paid with one original query influence and the owned kappa release.

This does not pay a private priority-boundary reveal when a still-live fallback core appears on both children. Such a repeated physical core destroys the disjoint-branch hypothesis and invalidates replacing mismatch probability by the product of child means. The first unsupported next line is a bound for that actual repeated-core controller residual and its actual terminal H-U-R from one compatible remaining influence/core-slack account. Arbitrary inherited U and arbitrary controller boundary entropy remain FEI-strength. No full FEI claim follows.

## Actual controller-resolved continuation when r=s=1

For one private control per event, restrict controller order to X then A then B, skipping labels already resolved. Arbitrary fresh data queries may be interleaved, provided that order of controller reveals is respected. In same orientation the X reveal kills one child. On the live child, revealing A selects the current u on one branch and a fresh one-bit point activation of current v on the other: these child functions use disjoint physical blocks. The remaining B reveal is one-sided. In opposite orientation the X children are independent private activations; after X each remaining relevant control reveal is one-sided. Thus every controller residual satisfies the single rate K_ctrl=4+2/ln2. Conditioning on already exposed data preserves each asserted disjointness.

At any actual controller-resolved stopping frontier, the profile boundary H-U-R is phi(mean(selected core)^2)<=I_leaf/ln2. Combining the signed A059 data drift gives the same-policy stopped bound

H(F_root)<=U_root+R_root+(3/ln2)T_data+(4+2/ln2)Pi_ctrl+E I_leaf/ln2.

The full influence identity is I_root=Pi_data+Pi_ctrl+E I_leaf, T_data<=Pi_data, and R_root<=2I_ctrl(root). R_root and the controller-residual charges are distinct debits; funding both from original control influence yields the sum of their rates, never their maximum. U_root is retained. The exact controller-only continuation from every n<=2 data face checks all actual leaf entropies, R releases, and the residual bound, rather than substituting the terminal of another exposure order. The analytic geometry proves this statement for arbitrary core dimensions and all finite admissible data interleavings.

This removes the first mixed shared-bit and r=s=1 controller-frontier gap at explicit inherited-core scope. Private widths larger than one can leave the same fallback core live on both private-boundary children; their price and arbitrary inherited U remain open. The same-core scope guard is exact: F_0=F_1=h on one shared physical cube has query influence zero, while (1-(Eh)^2)/2>0 for nonconstant h. An independent-copy calculation would change the physical function.

## Late board reconciliation: do not repeat the all-width block payment

A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@3 already supplies a control-only point-selector block bound and same-orientation priority suffix at rate 71/8, retaining terminal core entropies, for arbitrary private widths. Its DERIVATION and CLAIMS were read at reconciliation and saved as separate source snapshots. This is a pending source claim, not independently accepted in this stage. It is compatible with the new theorem: a whole fixed-data block price is different from the pointwise D-kappa debit and a controller block interrupted by fresh data. The remaining private-width question in this report concerns that interrupted physical continuation, not A028's already-paid control-only suffix. The exact next exposure is shared X, one private A bit, one unfinished-core data bit, then the remaining private A bit at r=2,s=1. Retain the same fallback core, actual q-dependent R release, inherited U/slack and final terminal profile. No new raw width census is warranted.
