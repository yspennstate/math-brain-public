# One marked source book for arbitrary shared phases under private point histories

All costs are bits and all physical signs are uniform. Let u,v be ANY Boolean phases on a common k-bit cube S, with supplied normalized positive-support finite-cost references R_u,R_v. Empty-calibrate these to squared means, retaining the nonempty conditional laws; write their resulting costs c_u,c_v and debts D_u,D_v. The calibration does not increase the supplied raw costs. Let disjoint private point indicators A_r,B_s be independent of S, and let a=2^-r,b=2^-s. Set G=1+A_r(u-1),H=1+B_s(v-1), and F a fresh fair-selector mux of G,H. Constant/failed point events and resolved selectors are allowed below.

## 1. A support-complete prescribed branch reference

Put mu=Eu. After calibrating ALL shared-only atoms, the branch reference on S and private A masks is

    Q_G(empty A,T)=Ghat(empty A,T)^2;
    Q_G(U!=empty,T=empty)=a^2(1-mu)^2;
    Q_G(U!=empty,T!=empty)=a^2 R_u(T).             (1)

The formulas apply on zero true phase coefficients too. The total nonempty phase mass of R_u is Var(u), so (1) is normalized. For a failed event use the actual point mass at empty; for a successful zero-width event use P_u. The same construction applies to H. Exact debt is

    D(P_G||Q_G)=a(1-a)D_u,
    CE_G=H(G)+a(1-a)D_u.                          (2)

The actual Fourier coefficients at each nonempty A mask are a(uhat(T)-1_{T=empty}); shared-only coefficients are a uhat(T)+(1-a)1_{T=empty}. The reference ratios in (2) are therefore R_u(T)/P_u(T) only on nonempty-A/nonempty-phase packets. There are2^r-1 nonempty masks. Every other packet is exact, giving (2).

The supplied-reference point-activation bound, already established in A095's biased activation interface (and A056's earlier disjoint one-bit proof), gives

    H(G)<=a H(u)+6r a(1-mu),
    CE_G<=a c_u+6 I_A(G).                        (3)

For (3), iterate the one-fair-control cost<=6 times its actual influence, retaining each conditional core entropy; I_A(G)=r a(1-mu). Add (2)'s retained debt a(1-a)D_u<=aD_u. This uses no new arbitrary-core FEI certificate.

To make that scalar premise self-contained, for one fair point control put t=(1-|mu|)/2. Nonempty phase packets contribute Var(u)/2=2t(1-t) to erasure; the empty packet has masses(1-t)^2,t^2. Using ln(1+x)<=x bounds its entropy by[2t^2 ln(1/t)+t^2]/ln2. Physical concavity is at most2t/ln2, by the magnitude-Hellinger inequality. One elementary proof of that inequality is d(z)<=1-sqrt(1-z^2), with d(z)=[(1+z)ln(1+z)+(1-z)ln(1-z)]/2: the derivative difference z/sqrt(1-z^2)-atanh(z) increases from0 because its derivative is(1-z^2)^(-3/2)-(1-z^2)^(-1)>=0. Apply it to each pair of squared child coefficients and sum. Hence the full decrement divided by t is at most2+(2+exp(-1/2))/ln2<6; maximize2t ln(1/t)+(1-2ln2)t at t=exp(-1/2)/2. The strict bound follows from ln2>2/3,e>9/4. Since the physical influence(1-mu)/2>=t, the one-bit6 price follows, including zero by continuity. Iteration gives(3). The fair-selector concavity bound used below is the same argument with its magnitude distance bounded by the actual sign mismatch gamma.

## 2. Compatible completion preserves the ORIGINAL phase reference

At a private point query, use the actual physical coherence kernel on positive spectral fibers. On a reference-only exclusive branch fiber with a nonempty REMAINING private point mask, use the point indicator's kernel: the passing child has probability1 and the failing child0. This rule is used in both branch and root transport. A fair extension could change the conditional phase reference on these fibers; it is not licensed as preserving prescribed R_u.

On a passing child, all remaining nonempty-private-mask reference amplitudes scale from a^2R_u(T) to(2a)^2R_u(T) after normalization/calibration. Within this complement the SAME R_u conditional law remains. Shared-only rows are recalibrated individually, including newly exposed rows. On a failed child the true private complement mass is zero and disappears by categorical calibration. The remaining unqueried failed controls are retained as physical dummy coordinates, not silently deleted. If the last private control passes, the phase is now entirely shared and its calibrated reference is P_u. The supplied c_u still remains a valid gross source allowance, rather than being assigned to another phase.

On residual reference-only shared rows choose any normalized extension; they are singleton calibrated. On selector queries use the selected-branch controller kernel. A056 v3's categorical closure proof applies with SYNCHRONIZED branch/root zero-fiber data kernels (its fair choice was one possible extension, not a prescribed-phase invariance assertion). It follows that the inherited Bayes reference, after categorical calibration at shared singletons and private branch totals, is exactly the reference rebuilt by (1) with the original R_u,R_v. No descendant chooses a fresh phase law.

Thus at every reached state with phase selection weights pi_G,pi_H (1/2,1/2 before the selector,1/0 or0/1 after), the exact root debt is

    D_state=pi_G a(1-a)D_u+pi_H b(1-b)D_v.        (4)

Atomwise closure: a nonempty remaining owner-point mask has equal parent coefficients a uhat(T) on its queried-bit pair, giving kernel(1,0); the chosen zero-mass extension is also(1,0). Its inherited reference is2a^2R_u(T) on the passing outcome, uniformly proportional to the declared4a^2R_u(T) complement. An unrelated branch has queried-coordinate coefficient0 and uses kernel(1/2,1/2), including reference-only rows. Newly shared rows are singletons calibrated to their true mass. These exhaust the root cells. On a failing outcome the owner's true complement has mass0; on a selector query exclusive owner fibers select their owner. Category normalization consequently gives exactly(1) at each child, including failed and zero-width states. Induction proves all-history closure independently of finite checks.

At an A query the expected KL release is pi_G a^2D_u; at B it is pi_H b^2D_v; at a selector query it is0. These releases equal conditional erasure KL plus outcome KL plus mean categorical savings for the inherited reference. All physical outcomes remain fair even when reference outcomes do not. This is a quantified fixed-seed history theorem, not a generic reset credit.

## 3. Price the shared collision from one original core mark

Consume A028@5's fair-selector boundary specialization, independently reproduced here: with gamma=P(G!=H),

    Pi=H(F)-[H(G)+H(H)]/2 <=(3/ln2)gamma+I(GH)/2. (5)

Indeed the physical selector erasure is<=h2(gamma), its concavity gap<=2gamma/ln2, and cube edge isoperimetry gives gamma log2(1/gamma)<=I(GH)/2. These are the full shared rows; a mean-only branch mismatch would be wrong.

Because A,B are private independent control blocks, multiplication by the OTHER Boolean branch leaves each private edge unchanged. Therefore

    [I_A(GH)+I_B(GH)]/2=I_private(F).

On each SHARED data coordinate, Inf_i(GH)<=a Inf_i(u)+b Inf_i(v). Consequently

    I_shared(GH)/2<=I_core(F),
    I_core(F)=(a I(u)+b I(v))/2.                  (6)

Mark this ONE unit of actual source core influence to pay the shared part of(5); the private part costs one additional private-control unit. Combining(3),(5),(6), exact terminal debt transfer and3/ln2<7 gives

    CE(F,Q)<=w_u c_u+w_v c_v+I_core(F)+7I_control(F), (7)

where w_u=a/2,w_v=b/2 and I_control includes private point and fresh selector influences. Once the selector is resolved, (3) gives the same bound with pi equal0/1; the unused one-unit core mark remains explicit. Failed point events contribute zero phase weight. No phase dimension, spectral norm, derivative gap, rarity or agreement assumption occurs.

If c_u<=C_u I(u),c_v<=C_v I(v), choose K=max(C_u+1,C_v+1,7). The ACTUAL root surplus has the certified lower bound

    K I(F)-CE(F,Q)
       >=w_u[(K-1)I(u)-c_u]+w_v[(K-1)I(v)-c_v]
                                      +(K-7)I_control(F)>=0. (8)

The one-unit mark is taken from unused supplied-source surplus, not borrowed from an unrelated terminal. The full source-reference bills occur in(7) once. This root entropy-rate corollary is a composition application; the new work is preserving these very references and owners below actual weak private queries.

## 4. Complete signed stopped history with no renewed bank

Allow ANY finite adaptive tree querying private point controls and the selector in any order, with arbitrary stopping; NEVER query the shared phase coordinates in this theorem. Actual phase weights w_u=pi_G a,w_v=pi_H b are conditional probabilities of fixed original control events, hence harmonic on the tree. The original phase costs, phase influences and remaining source surpluses in(8) are therefore harmonic, not reissued root budgets. The actual control-block influence obeys its ordinary telescope. Formula(1) remains the carried reference at each node by Section2, so(7),(8) hold at the ACTUAL terminals, with both core bills retained.

Define the explicit unused BOOK, with the same original c_u,c_v,

    L_state=w_u c_u+w_v c_v+I_core+7I_control-CE_state>=0. (9)

All terms in this book have been bounded independently in(3)-(7). For every stopped private-control history T,

    CE_root=7 Pi_control+E CE_leaf+E L_leaf-L_root.      (10)

This follows by subtracting the actual CE from the harmonic core-bill/mark plus telescoping control budget; it keeps the SIGNED child-refund term rather than asserting a false local7Influence rule. The same initial book is used on every branch. In particular E CE_leaf<=K E I_leaf, and the nonnegative source-surplus part of(8) remains in expectation with its ORIGINAL weights. Large local entropy/query ratios are allowed and are represented by the actual child-book difference, not clipped or charged to a fresh selector bank. Equation(10) is an exact signed ledger; its new content is the independently proved nonnegative fixed-seed book and its hereditary reference realization.

## 5. What remains

A shared PHASE-coordinate query changes u,v themselves. It can destroy the old phase-reference conditional law or change its certified c/I ratio, so (7)-(10) are not licensed by assigning fresh c_u,c_v to the reached phases. The first unsupported universal line is paying that actual shared-core exposure from the SAME unused source surplus and all incoming reference normalizers, with both nonconstant children retained. General original phase references still need influence-paid certificates. The theorem moves the private rare/rare collision ownership problem to this explicit shared-core boundary; it does not solve full FEI or all-node signed drift.
