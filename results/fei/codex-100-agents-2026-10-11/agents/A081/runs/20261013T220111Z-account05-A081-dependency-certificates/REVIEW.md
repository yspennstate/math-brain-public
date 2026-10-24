# Independent reconstruction and exact scope verdicts

All Boolean functions below are signs on finite uniform physical cubes. Entropies, cross-entropies and KL divergences use bits. References are subprobabilities on the entire remaining subset space, positive on true support. A081 supplies no repair to A097 transfer v1 or A090 parity-tail v1; the verdicts below are independent scoped reviews. Formal coefficient checking, floating-screen contracts, and finite censuses are not used to prove these results.

## A097 compatible-reference transfer v1: HOLDS

At one actual physical block node A, let m=2^|A|, C the remaining coordinates, a(U,T) the parent Fourier coefficients, and b(y,T) the coefficients after assigning A=y. Character orthogonality gives q(T)=sum_U a(U,T)^2=(1/m)sum_y b(y,T)^2. Each P_y(T)=b(y,T)^2 is normalized because the restricted function is Boolean. For q(T)>0 put theta(U|T)=a(U,T)^2/q(T). Given fixed child references Q_y, put r(T)=(1/m)sum_y Q_y(T), and Q(U,T)=theta(U|T)r(T). At q(T)=0 choose a probability kernel theta, for example the point mass U=empty. Its choice affects only zero true atoms. Then sum Q=average_y sum Q_y<=1 and Q is positive on every positive parent atom.

Here is a joint-law proof independent of any entropy induction. Define p(y,T)=P_y(T)/m and t(y,T)=Q_y(T)/m. The true/reference T marginals are q,r; their normalized physical posteriors are k_P=P_y/(mq), k_Q=Q_y/(mr) on positive true fibers. Factor their likelihood ratio p/t=(q/r)(k_P/k_Q). Multiplying by p and summing yields

    average_y D(P_y||Q_y)=D(q||r)+kappa,
    kappa=sum_T q(T) D(k_P(.|T)||k_Q(.|T))>=0.

The parent shares theta with Q, so D(P||Q)=D(q||r). This computation retains every subprobability normalizer. Generalized D(P||Q) is nonnegative: adjoin a failure atom to Q, with true mass zero, then apply the ordinary Gibbs inequality. No false assertion that Q has mass one is needed.

Let B=H(P)-H(q), J=H(q)-average_y H(P_y). Since CE=H+D, subtraction gives exactly

    CE(P,Q)=B+J-kappa+average_y CE(P_y,Q_y).

On any finite adaptive tree, each block depends only on revealed physical history; its actual branch probability is 1/m. Iterating this equality gives the stated CE telescope, and iterating the divergence equality gives

    K_tree=average_leaf D(P_l||Q_l)-D(P_root||Q_root)
          <=average_leaf D(P_l||Q_l).

For the history-posterior interpretation, generate the joint law by choosing a physical branch y, sampling its recursively generated child spectral law, and then sampling removed labels U through theta(U|T). Its root marginal is exactly P by the orthogonality identity. Repeat using the fixed Q_l at the leaves. In the likelihood ratio of the resulting (full spectral set, transcript), all physical branch factors and theta factors cancel. The joint divergence is therefore the average terminal divergence. Applying its ordinary conditional chain rule over the full spectral marginal identifies K_tree with the claimed history-posterior divergence, also for subprobabilities completed by a failure atom. The unused reference failure probability is never assigned positive true mass.

The physical channel constant needs its own proof. For nonnegative numbers a,b under a fair two-point measure, Ent(g^2)<=E(g-g_flip)^2/2. By homogeneity take b=1,a=t. The difference multiplied by two is

    F(t)=(t^2+1)ln((t^2+1)/2)-2t^2 ln t+(t-1)^2.

For t>=1, F'(t)=2t[1-1/t-ln(2t^2/(t^2+1))]. The bracket vanishes at one and its derivative is (t-1)^2/[t^2(t^2+1)]>=0. Thus F>=0; t<1 follows from F(t)=t^2 F(1/t), with zero endpoints by continuity. Conditional entropy tensorization over independent fair coordinates proves the cube version: normalize g^2 to a density, express its entropy using conditional densities in coordinate order, and use convexity of relative entropy to bound each ordered conditional term by the corresponding fully conditioned two-point term. Apply it to g(y)=|b(y,T)|/sqrt(q(T)), then multiply by q(T) and sum T. Magnitude differences are bounded by signed differences; Parseval on C gives J<=2 I_A/ln2. This proof requires the physical block, not an arbitrary spectral relabeling.

Finally, physical edge counting gives I(parent)=I_A(parent)+average_y I(child), hence I(root)=I_removed+average_leaf I(leaf). If the separate hypotheses B_tree-K_tree<=K I_removed and CE_l<=C_leaf I_l hold, the full CE telescope gives CE_root<=max(K+2/ln2,C_leaf) I_root and Gibbs gives H<=CE. These hypotheses remain explicit universal unpaid leaves. A097's conditional theorem never asserts their existence.

Two sharp bookkeeping checks: Q_l=P_l makes all references true and every kappa zero; scaling every fixed leaf reference by the same lambda in (0,1] scales every lifted reference by lambda, leaves all physical posterior kernels and kappas unchanged, and increases both root and averaged terminal CE by log2(1/lambda). Uniform reference mass loss cannot create free payment. History-dependent leaf mass loss can alter kappa, but its entire terminal CE and the above slack ceiling remain mandatory.

## A090 parity-tail completeness v1: HOLDS

For any actual seed f on n bits, m independent copies, and ell>=2 fresh physical parity coordinates Z, let h=chi_Z product_j f_j. Its Fourier law is the product seed law with all of Z deterministically present. Hence B(h)=mB(f), I(h)=mI(f)+ell, its mean and all singleton coefficients vanish, and each Z-coordinate has zero erasure. Activate at the zero vertex of k fresh controls: F=1+A_k(h-1), q=2^-k. Direct character expansion gives a_F(empty,empty)=1-q, a_F(empty,U)=-q for nonempty control U, and a_F(S,U)=q a_h(S) for nonempty core S and every control U.

At an original data coordinate, phi(x,y)=(x+y)h2(y/(x+y)) is homogeneous. Summing the 2^k control slices therefore multiplies the seed edge cost by q. There is no singleton correction because a_h(i)=0, so B_data(F)=qmB(f). Every nonzero-cost data edge retains all ell parity coordinates at its lower endpoint. Removing any one parity coordinate destroys occupied core support; its exceptional empty row is also separated by at least two parity coordinates. Thus B_z(F)=0 while Inf_z(F)=q>0.

For a given control coordinate, each occupied nonempty core frequency contributes equal adjacent masses q^2 a_h(S)^2, whose summed phi is q. These edges have lower size at least ell. Empty-core lower control subsets of size r>=ell contribute phi(q^2,q^2)=2q^2, with binomial(k-1,r) choices per control. Therefore, exactly,

    R_geell(F)=qmB(f)+kq+2kq^2 sum_(r=ell..k-1) binomial(k-1,r).

For ell=2 the binomial sum is 2^(k-1)-k; for k=1 both expressions are zero. For any parity count ell>=2 the tail starting at level two is consequently

    R_ge2(F)=qmB(f)+2kq(1-kq).

Influence is q[mI(f)+ell+k], directly from the active-core edges and the balanced core's minority probability one half. The parity bits have positive influence, so the selectable min ratio is exactly zero. This distinguishes aggregate hardness from selected-coordinate hardness without any asymptotics.

To prove the complete cutoff supremum independently, for any finite-valued nonnegative s=o(N), put sbar(N)=max_(1<=j<=N) s(j). This is nondecreasing and o(N): split at a fixed finite index after which s(j)<=epsilon j. For a fixed nonconstant n-bit seed and fixed ell choose

    k_m=ceil(sbar(2mn)+log2(3mn))+1.

Then k_m=o(m), eventually ell+k_m<=mn, N_m=mn+ell+k_m<=2mn, and mI(f)+ell+k_m<=3mn. Thus 0<I(F_m)<=2^-sbar(N_m)<=2^-s(N_m). Since k_m/m->0, the data contribution alone implies liminf R_geell(F_m)/I(F_m)>=B(f)/I(f). Conversely R_geell<=B always, so the restricted supremum is at most K_E. Taking every actual seed proves equality in the extended reals, including infinite K_E by arbitrarily large finite seed ratios. No finiteness or optimal seed is assumed. The source's exact formulas and scope survive unchanged.

The A099 low-influence v2 claim follows from the same construction or from R_geell<=B and this equality; the C_FEI comparison uses the conditional erasure bridge reconstructed next. Its source 522cb5... hash is the canonical JSON hash of statement plus hypotheses; A090's ea6312... is SHA256 of the identical statement alone. Both are valid, differently typed receipts. We preserve both rather than changing the source version or treating the source as corrupted.

For completeness, the conditional erasure bridge is not an assumed FEI endpoint. For a random spectral binary vector, conditioning reduces entropy; summing H(S_i|S_-i)<=H(S_i|S_1,...,S_(i-1)) proves B<=H. Conversely, ASSUME B(g)<=K I(g) for every dimension and every actual Boolean g. The singleton identity D_i=B_i+JS_i and the independently proved scalar bound JS_i<=2 Inf_i/ln2 give sum_i D_i<=(K+2/ln2)I. If I>0, at least one relevant i has D_i<=(K+2/ln2)Inf_i. The exact physical identity I=Inf_i+average I(child), followed by dimension induction starting with constants H=I=0, yields H<=(K+2/ln2)I. The reverse implication FEI(C)=>B<=CI uses B<=H. No all-dimensional payment is proved or presumed outside the antecedent of this implication.

## Debt sign and boundary: scoped acceptance only

Write D=H(parent)-average H(child), d=queried influence. For Q=CI-H, direct conservation gives Q_parent-average Q_child=Cd-D. Inserting this in the debt requirement D<=Cd+Q_parent-average Q_child is equivalent to D<=Cd. Parent/child FEI certificates alone give no such local inequality. On f=(-1,1,1,1), C=2, H=2,I=1,d=1/2, the two children have H=0 and averaged I=1/2. All three satisfy H<=2I, but Q_parent=0, averaged Q_child=1, and the proposed debt RHS is zero while D=2. This independently confirms the sign clause of A064 v1, not all clauses of its compound theorem.

The correct finite-tree boundary implication, also reconstructed here, is: D_v<=Cd_v+Q_v-average Q_child, Q_root<=K I_removed, and average(H_leaf-Q_leaf)<=L average I_leaf imply H_root<=max(C+K,L)I_root. Sum weighted inequalities and keep the terminal Q and H terms. Q=H_v-average(H_terminal|v) has drift D, zero terminal values, and is nonnegative because each block decrement B+J is nonnegative. Its universal initial-resource and terminal-cost bounds are still assumptions. Calling this exact identity a payment proof would hide the whole missing theorem.

## Executed certificates and unresolved line

The independent checker uses direct character sums, physical edge counts and exact Fraction/prime-log dictionaries; no upstream helper is imported. It passed 7,318 assertions on 312 tree/reference cases and 176 actual parity-tensor activations, plus the two-bit sign witness, in 3.54 seconds. Pilot passed 700 assertions. Nonzero credits occurred in 96 cases and nonzero retained terminal entropy in eight. Every log-identity check cancels exact prime coefficients. Finite tests support the implementation; the preceding proofs establish the arbitrary finite-dimensional statements.

The first unsupported universal line is the existence of one finite K and one allowed tree/reference construction for every Boolean f with B_tree-K_tree<=K I_removed and all complete terminal costs paid by their unreused terminal influence. Equivalently, the live C018 assembly still has no all-dimensional R_ge2<=KI proof. A090's equality proves that fixed low-layer deletion and sublinear influence cutoffs retain the full optimal aggregate debt. No universal FEI constant was improved.
