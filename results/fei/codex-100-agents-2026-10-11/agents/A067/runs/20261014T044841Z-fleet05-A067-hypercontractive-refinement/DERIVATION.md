# Boolean spectral flag payment and controller-dependent branches

All entropies are bits, cubes finite and uniform, signs genuinely Boolean. Influence is ordinary physical flip probability, equivalent to Fourier degree under these hypotheses. The prior two-controller theorem was independently accepted by A088; this extension does not overwrite it.

## 1. A universal Boolean spectral-flag lemma

For ANY Boolean F on X,Z let v=Var(F), alpha=P_spectral(S_Z nonempty). Partial Parseval gives 0<=alpha<=v, and influence dominates variance. Then

    h2(alpha)<=2 I(F).                                      (1)

Proof. If v>=1/2, h2(alpha)<=1<=2v<=2I. If v<1/2, h2 is increasing on [0,1/2], so h2(alpha)<=h2(v). Let p=min(P(F=+1),P(F=-1))<=1/2. Then v=4p(1-p)<1/2 implies p<1/4. For 0<p<1/4 the function t log2(e/t) is increasing on [0,1], and v<=4p<1. Consequently

    h2(v)<=v log2(e/v)<=4p log2(e/(4p))
           <=4p log2(1/p)<=2I(F).

The penultimate inequality is e<4. The last is the Boolean set isoperimetric bound I(F)>=2p log2(1/p). Constants give zero on both sides. Thus no edit-mask ownership, fiber cap, original seed, or positive source slack is needed for (1). This is a universal Boolean estimate for a SINGLE two-cell flag; it does not pay the entropy of arbitrary control labels.

For completeness, set isoperimetry is proved by induction: split a set into child densities p0,p1; the crossing influence is at least |p0-p1|. For p=(p0+p1)/2 and t=p0/(p0+p1), the difference between target 2p log2(1/p) and averaged child bounds is 2p[1-h2(t)]<=2p|2t-1|=|p0-p1|, by h2(t)>=2min(t,1-t). Induct from the zero-dimensional set. This applies to either minority sign class.

The coefficient two in this single-flag lemma is asymptotically sharp: take the d-bit point sign, X empty and Z all bits. With delta=2^-d, alpha=4delta(1-delta) and I=2d delta. Since h2(alpha)>=alpha log2(1/alpha), its ratio to I is at least 2(1-delta)[1-log2(4(1-delta))/d], tending to two; (1) supplies the matching upper bound. This does not prove the retained 2I_X reserve is optimal for the access theorem, and it is not an FEI constant claim.

## 2. Final-output theorem: arbitrary four core branches

Let p(Z),q(Z) be two fixed subcube indicators with arbitrary fixed-coordinate sets P,Q and arbitrary compatible or incompatible assignments. Let h_00,h_10,h_01,h_11 be arbitrary Boolean signs on X. Define the ACTUAL OUTPUT

    F(x,z)=h_(p(z),q(z))(x).

There is no sparse-fiber cap. The output can be densely edited, and a source depending on both controller states is allowed. An inaccessible controller state is not counted as an actual terminal. Contract all controls outside P union Q. Write I_X,I_Z for final F, Q_access=H(F)-E_z H(F_z), and alpha=P_spectral(S_Z nonempty). Then

    Q_access <= K I_Z+2I_X,
    K=4+log2(5)+2/ln2<19/2.                                (2)

For compatible assignments K can be 6+2/ln2<9. Complete physical control reveal retains all actual terminal cores with their actual state probabilities; E_z I(F_z)=I_X. Hence if EVERY accessible h_ab has H(h_ab)<=C I(h_ab),

    H(F)<=K I_Z+(C+2)I_X<=max(K,C+2)I(F).                 (3)

Under U(h_ab)<=bI(h_ab), replace C by 2+2b. Degree at most two on actual cores gives C=4 and H(F)<=KI. Both ordinary entropy admission and U admission are actual-terminal hypotheses, not universal conclusions. Equation (3) does NOT close induction at the same C because the 2I_X reserve is retained explicitly.

## 3. One complete reference, independent of the original source

The Boolean branch expansion is

    F=h00+(h10-h00)p+(h01-h00)q
           +(h11-h10-h01+h00)pq.

Each core Fourier row lies in the real span of 1,p,q,pq, even though each branch may be an arbitrary Boolean core. Split contracted controls into R=P intersect Q, U=P minus Q, V=Q minus P. In the compatible case partition nonempty Fourier subsets by whether they meet U,V: four cells 00,10,01,11, omitting empty cells and removing S=empty from 00. In the incompatible case pq=0; split the shared-only 00 cell by parity of the intersection with the shared conflict set D, giving at most five cells. The double-private cell is still included in the complete reference even when it has zero output mass. This fixes the minor scope ambiguity noted by A088 in the prior source prose: 11 is zero only when assignments are incompatible.

The accepted A067 cell proof, independently reconstructed by A088, gives: row squared amplitudes are constant in every occupied cell, and for each cell C,

    log2 |C|<=2 E_(S uniform C)|S|.

Unrestricted blocks have fair occupancy and matching degree/entropy; nonempty conditioning reduces entropy and raises degree. Shared conflict-parity cells are affine parity subspaces (one fixed bit if |D|=1); removing the empty subset from the even cell also decreases entropy and raises degree. Thus the bound covers every cell, including singleton and zero-dimensional block limits.

Set M to the number of nonempty cells, R_tail(S)=1/(M|C(S)|), R_full(empty)=1-alpha, R_full(S)=alpha R_tail(S). R_tail covers ALL nonempty subsets, not a selected support; R_full is one complete normalized output reference, the same in every core Fourier row. If the contracted block or alpha is zero, handle trivial access or continuity separately. The density, empty atom and label weights are all selected from the FINAL OUTPUT, not the ancestral seed or masks. Gibbs' inequality and actual flatness yield

    B_Z:=H(S_Z|S_X)<=h2(alpha)+alpha log2 M+2I_Z.

Alpha<=I_Z is now the trivial spectral degree bound, which holds for all normalized functions. Applying the NEW Boolean flag lemma (1) gives

    B_Z<=(4+log2 M)I_Z+2I_X.                              (4)

The exact restriction identity Q_access=B_Z+J_Z and tensorized real two-point channel bound J_Z<=2I_Z/ln2 prove (2). More explicitly, the complete joint reference is R_joint(T,S)=P_final(S_X=T) R_full(S). It covers the entire actual final spectrum and has cross entropy H(S_X)+E[-log2 R_full(S_Z)]. The same identity gives H(S_X)=E_z H(F_z)+J_Z; hence this whole reference cost is bounded by E_z H(F_z)+K I_Z+2I_X, not merely its conditional fragment. Zero-mass core rows need no conditional cost. Choosing the actual core marginal does not admit it for free: its full entropy is converted to the explicitly retained actual terminal bill plus the paid channel. This separates the dimension-free real channel fragment from the Boolean flag improvement. The proof's first genuinely Boolean line is the bias/variance relation v=4p(1-p) and the set-boundary influence bound in Section 1; arbitrary real Parseval laws do not have them.

## 4. Fully exposed cancellations: final reference instead of ancestral bills

A070's original four-bit witness has q=(1-c)/2+(1+c)uv/2, source g=q*y, and final F=y. Under its two event indicators p=1{c=+,u=+}, q_event=1{c=+,v=+}, both source and output are controller-state functions. The NEW theorem applies despite full exposure. Its final alpha=I_Z=Q_access=0; it retains H(y)=0 and I_X=1. There is no attempt to make the negative ancestral conversion term nonnegative.

A070's newer unequal-width family has q1=1-2p, q2=1-2q_event, source g=q1*h(Y), final F=q2*h(Y), with private U={u}, V of width t and h a point sign on t core bits. The ancestral bill [7I(g)+12I(q1q2)]/I(F) diverges, whereas the final-output cell reference remains bounded by (2) with the actual h or -h terminals retained. The source is fully exposed to the first private controller, and no residual privacy condition is imposed here. This is an alternative final reference for this controller-algebra scope, NOT a proof that arbitrary control-dependent sources are paid and NOT a bound on the invalid ancestral bill.

Equivalently, start from ANY four Boolean source branches s_ab(X), then multiply by any sign-valued function of p,q,X. The product has four actual Boolean branches and is covered by (2)-(3). This is the promised common-reference transfer with source dependence on both controllers. If the multiplier's core dependence changes terminal entropy, its resulting branches must be certified; the original source core certificates cannot be silently carried over.

## 5. Sharp scope guards and remaining bridge

The flag lemma does not hold for general normalized real outputs. Let u=(4095+128z)/4097, so its two squared Fourier masses are 1-beta,beta with beta=16384/16785409<1/1024. Then h2(alpha)/I=h2(beta)/beta>log2(1/beta)>10>2. This is an exact rational normalized-real counterexample to (1), not a Boolean FEI counterexample. With X empty and p=1{z=+}, q=1{z=-}, it lies in the same two-controller REAL span and its real access exceeds even K I_Z. Thus the new unconditional no-cap access theorem is genuinely Boolean, not just the general real flat-cell inequality.

The cell restriction is substantive. Arbitrary control-dependent seeds need not be functions of the two fixed event states, so flatness/reference Section 3 can fail. An arbitrary F can be expanded using exponentially many indicator controllers, but then log M is not a universal constant. No such extension is asserted.

First unsupported universal line: either pay the retained 2I_X access reserve from a genuinely UNUSED certified child surplus, or supply a common final reference for general controller dependence whose whole cost and actual terminal debt fit one physical influence account. A bare H(child)<=C I(child) gives (3), with C+2, and cannot certify a same-C universal induction. New global retained-core KL or shadow accounts are needed; their loss-only bounds do not by themselves supply this surplus.
