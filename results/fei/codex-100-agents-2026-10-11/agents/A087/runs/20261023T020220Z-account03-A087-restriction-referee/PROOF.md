# Verdict and scope

A061-ORIGINAL-MARGINAL-ENVELOPE-ALL-HISTORIES@1 HOLDS at its stated inherited-reference, policy and ownership scope. A065-CARRIER-DATA-INTERPOSITION@1 HOLDS at its stated general invariant and finite payment/counterexample scope. The generic transfer is all-dimensional; the explicit original-owner comparison is for the field family. Neither proves full FEI. No substantive source repair is required.

All logarithms use bits. Physical inputs are independent uniform bits, queried adaptively from their actual revealed history; unrevealed inputs stay uniform. Independent policy randomness may be conditioned on first. Source/reference distributions are finite and normalized. Reference support must contain source support. On source-zero erased fibers the prescribed kernel is fair, including all reference-positive mass.

## Carrier transfer in actual physical coordinates

Let g(y) be any Boolean sign on m ordinary bits, R any such reference, L a linear parity, and c an affine bit. With fresh carrier bits u,v put

    F(u,v,y)=(-1)^((u+v+L(y)+c)*v) g(y).

Sum first over physical u in its Fourier coefficient. The sum vanishes unless v=s_u; substituting that value leaves the core coefficient at T xor s_u L and a phase of magnitude one, times1/2. Therefore

    P_F(s_u,s_v,T)=p_g(T xor s_u L)/4,
    Q_F(s_u,s_v,T)=R(T xor s_u L)/4.

The latter is the supplied reference, not a reset inferred from marginal matching. Both s_v values are retained. The four lift factors cancel in KL, giving KL(P_F||Q_F)=KL(p_g||R). This is an exact Fourier-label permutation; it makes no assertion that a general physical shear preserves influence.

For an ordinary query y_j, erase the j frequency from both P and Q. When L_j=1 the two erased terms exchange as s_u changes, leaving the same lift of p_g^{-j} and R^{-j}. The physical child is the same carrier with core g_b and c replaced by c+bL_j. Its squared law is the corresponding lift of p_{g_b}. On positive erased source rows its outcome kernel is

    k_b(T)=p_{g_b}(T)/(2p_g^{-j}(T));

on zero-source rows both the core and full lift use1/2. Thus predicted reaches coincide, as do normalized reference transports, erasure KL and outcome KL. Positive predicted reach follows because each actual child is a normalized Boolean law and the erased reference contains source support. Induction on the number of queries proves the invariant under every finite adaptive ordinary history. No ordinary bit query can break this pairing.

For a later v query, the actual children are g and a sign times chi_u chi_L g. Pair erased atoms (s_u=0,T) and (s_u=1,T xor L). Each has reference mass R(T)/2. Positive-source pairs use the two opposite deterministic outcomes; zero-source pairs retain equal fair extensions. Hence the predicted outcomes are exactly fair and O_v=0. Both actual child entropies equal H(g), and both full product-reference KLs equal TC(g): deterministic unused u and character translations do not change binary marginal entropies or joint entropy. The actual g spectrum and both full terminal bills remain; fairness of prediction is not free conversion to products.

## Exact normalized KL ledger and one marginal envelope

At any ordinary core history write p=p_g, K=KL(p||R), M=sum_j h2(Inf_j(g)) and TC=M-H. At query i let p_e,R_e be erased laws and let r_b be the reference-predicted outcome. Actual outcomes still have probability1/2. The common joint kernel and the two KL chain rules give

    K=E+O+(K_0+K_1)/2,
    E=KL(p||R)-KL(p_e||R_e)>=0,
    O=KL((1/2,1/2)||(r_0,r_1))>=0.

E is the conditional KL in each erased fiber. Every ratio is used only on a positive-source row, where its reference denominator is positive. Reference-only rows participate in r and in normalization, despite contributing no source KL. Positivity of all actual outcome reaches was established above.

For j distinct from i, physical edge counting gives Inf_j(g)=mean_b Inf_j(g_b): fixing i partitions the edges in direction j into two equal sets. Binary entropy is concave, with endpoints h2(0)=h2(1)=0. Thus

    M-mean M_child=h2(Inf_i(g))
        +sum_(j!=i)[h2(Inf_j(g))-mean h2(Inf_j(g_b))]>=0.

Set V=K+M. Combining the two formulas proves

    V-mean V_child=E+O+M-mean M_child>=O.

At stopping without conversion, V>=K. At one final carrier query and conversion, V>=TC because K>=0 and TC=M-H<=M. All potentials are nonnegative (Gibbs, binary entropy); summing the finite conditional drift inequality gives, for every admitted bounded stopping cut,

    E KL_terminal+E sum O <= K_initial+M_initial,
    E CE_terminal+E sum O <= K_initial+M_initial+E H_terminal.

Terminal KL is inherited-reference K when stopping without conversion and actual product TC at a declared carrier-conversion terminal. All such terminals stop; no intermediate reset or further postconversion transaction is included. This uses ONE M_initial, transported through its conditional drift. It never allocates a fresh M at every descendant or assumes branchwise decrease. All trees have depth at most m ordinary queries and one carrier query; no changing-dimension optional-stopping argument occurs.

## Least pending booking, earlier allocations and real expenditure

The immediate extra booking required for carrier conversion is b=[TC-K]_+. For a finite declared ordinary policy class with optional stopping/conversion at every node, the least nonnegative pending booking satisfies

    B=max(b, max_admitted_i(mean B_child-E_i)).

At a terminal node the continuation maximum is omitted. This follows directly from the drift inequality for K+B: it pays O iff E+B>=mean B_child, and pays conversion iff K+B>=TC. It is a finite backward recursion. Maxima over next coordinates precede the fair average; after an outcome, branches may choose different policies. Since b<=M and mean M_child<=M, induction gives0<=B<=M. These are sufficient and necessary one-step constraints, not a new universal resource estimate.

Nested initial policy classes have B_old<=B_new<=M_initial. If theta is the earlier pending allocation for precisely that SAME original reference/class, replacing the total pending cap by Wcap consumes only Wcap-theta. A debit already paid and no longer part of that pending allocation cannot be reclaimed: it remains in the separate spent account omega. In particular, postconversion histories cannot invoke this theorem as if their old conversion were still a pending option. Its hypotheses deliberately exclude that use.

## All-field-width comparison to the actual original owner

Let q=2^l, l>=2, and choose any nontrivial additive character psi on GF(q). Define h(a,b,x)=psi(a)(1-2*1[x=ab]), on m=3l ordinary bits. Orthogonality in x first gives the coefficient of magnitude1-2/q at the psi character of a. At every nonzero x-frequency, summing in b forces a unique field value and gives magnitude2/q^2; there are(q-1)q^2 such coefficients. All others vanish. The core is balanced. The coefficient1-2/q is nonzero at every l>=2. The l=1 degeneracy is excluded and checked separately.

For this explicit field fixture set L(y) to the parity of ALL m ordinary coordinates. Every ordinary derivative then contains the independent fair v, and the u/v derivatives contain an independent fair carrier bit, so every child physical influence is1/2. Balanced h makes the selector influence1/2 as well. The selector chooses the same sheared carrier times1 or h; its original reference is uniform on its m+3 spectral bits (the actual original parent product, whose physical influences are all1/2). For the selector's normalized Bayes core references, let supp(h) denote its nonzero spectral atoms:

    R_G(T)=[1 at empty;0 on supp(h);1/2 elsewhere]/(q^3 r_G),
    R_H(T)=[0 at empty;1 on supp(h);1/2 elsewhere]/(q^3 r_H),
    r_G=1/(2q), r_H=1-r_G.

Empty is outside supp(h). The normalization follows by counting the1+(q-1)q^2 support atoms. Every reference-only atom remains. The root selector erasure credit is0, and K_root=O_selector+mean(K_G,K_H). After this actual query the G branch has constant core M=0 and B=0 for every ordinary history; the H branch has B<=M_h. Hence total original expected pending booking W_*<=M_h/2.

Physical x-direction influence is2/q. Each b-direction has two disagreement points unless a=0, giving p=2/q-2/q^2. Each a-direction similarly has p, or1-p when psi changes on that direction. Every basis direction is nonzero and multiplication by it is a bijection. Therefore in any field-coordinate basis

    M_h=2l h2(p)+l h2(2/q).

Both selector children have influence(m+2)/2 and entropies2 and2+H_h, so their actual original mean owner is

    Sbar=mean_selector(4I-H)=2m+2-H_h/2.

Since the core's spectrum has at most2^m atoms, H_h<=m and Sbar>=9l/2+2. For l>=3, p and2/q are at most1/4. Binary entropy increases on[0,1/2], and h2(1/4)=2-(3/4)log2(3)<13/16, since3^12>2^19. Consequently M_h<39l/16. The rational cap Wcap=39l/32 covers W_* and satisfies Wcap<13Sbar/48. At l=2 the explicit spectrum gives H_h=5, Sbar=23/2 and M_h<=6; Wcap=3 works since6/23<13/48 (288<299). All denominators are positive.

With a supplied genuinely available original owner and unrelated old expenditure omega<=Sbar/4, booking Wcap once leaves

    Sbar-omega-Wcap >23Sbar/48.

A smaller old nested pending allocation is already part of Wcap and is not charged again. This wider-class cap is larger than the earlier selector-then-carrier or one-data booking because it funds EVERY ordinary history, not because the older numbers were revised. Neither positivity nor availability of this family-specific original owner is assumed for arbitrary Boolean cores.

## Actual asymmetric cut and failure of tensorized reference transport

On the actual GF4 parent retain the original root uniform product reference. Query selector; stop G with its full Bayes reference; on H query ordinary direction0, then v and convert the four H terminals to products. The full512-vertex parent, all its actual restrictions and normalized references are independently reconstructed by direct character sums and physical edges.

The old H carrier-only booking b_old and new H pending booking B_new differ by

    Delta=-9/2+(3/8)log2(3)+(15/8)log2(5)>11/25.

The ordinary query's E is exactly0. The stopped cut has full mean terminal entropy11/4. Keeping the stopped G KL and all four H terminal product KLs, its exact old-booking shortfall is Delta/2>11/50. This is an actual expected cut, not just a rare branch price. The original Sbar is23/2 by direct edges and spectra. The updated TOTAL expected booking is B_new/2<Sbar/50; retain old unrelated quarter expenditure and top up only the difference from old W. Both complete terminals survive. At GF8 the declared small-depth bookings vanish. The source's exact all-optional-stop depth-two maxima are independently recovered as47/32-(3/8)log2(7) at l2 and0 at l3, below Sbar/25, with second topup below Sbar/50.

The new reference-based cut cannot be tensor-amplified using an unproved product-kernel assumption. The original GF4 parent has400 nonzero spectral atoms among512, so its independent uniform reference places25/32 on actual source support. For a second module, the globally prescribed kernel is fair whenever that other module lies off source support, rather than applying the local coherent kernel in the first module. The first selector prediction on two modules is therefore

    (25/32)(1/8)+(7/32)(1/2)=53/256 !=1/8.

This proves failure of naive reference transport factorization, without a large product enumeration. It does not affect ordinary entropy/influence additivity or the earlier A062/A065 entropy-only product obstruction, which did not use this reference kernel.

## New extension: every physical continuation after the selector

The proof of V=K+M above does not require a carrier when M is computed on ALL actual remaining coordinates. For any finite Boolean g and source-supporting inherited R, take M_full=sum h2(Inf_j(g)) over its entire remaining physical cube. The same edge conservation and KL chain prove that K+M_full pays every adaptive physical query and any stopping cut with a single final conversion to actual products. This includes carrier-coordinate queries, with no pairing assumption. It still excludes a conversion followed by further queries. Gibbs and H>=0 guarantee every terminal inequality, including deterministic coordinate endpoints.

Apply this universal envelope to each actual selector child of the field fixture. All m+2 child physical influences are1/2, so each M_full=m+2. Allocate ONE expected root pending cap

    W_all=m+2=3l+2.

The root potential is K_root+W_all; after its selector query use K_child+M_full(child), and use that same full marginal potential through every later physical history. The selector's KL chain pays its actual O, and all subsequent drift inequalities hold even after consuming u or v. The initial selector is fixed (or the root may stop with its original reference); arbitrary first root coordinates are not added to this class. At later cuts keep inherited KL, or convert once to actual products and stop, retaining full H+TC. Any previously allocated nested pending booking is included in W_all once; unrelated consumed debits remain in omega.

For l>=3, Sbar>=9l/2+2 gives

    (5/7)Sbar-W_all >= (3l-8)/14 >=1/14>0.

At l=2 the exact Sbar=23/2 gives (5/7)Sbar-W_all=3/14>0. Hence W_all<5Sbar/7 for EVERY l>=2. With the SAME supplied original owner and omega<=Sbar/4,

    Sbar-omega-W_all >Sbar/28.

This is a new conditional all-width extension of the reviewed carrier-preserving result: every physical continuation is paid, not just ordinary core histories. Its cap is deliberately larger and its remaining guaranteed owner smaller, because the policy class is larger. It does not revise the23/48 remainder for the narrower class or the earlier finite1/20 interface on a different family. The constant original owner is family-specific; the envelope theorem itself is universal but is not an influence-scale bound.

The new written corollary is author-checked, awaiting independent review by A061/A064/A094. A separately frozen check exhausts all16 two-bit functions, three inherited references and all physical stopping policies for the generic full envelope; this is a small exhaustive boundary control, not the proof for all dimensions. Exact owner guards and the actual GF4 child full marginal value8 are rechecked separately. No new field width is searched.

## Verification and remaining universal line

Frozen tests cover all16 two-bit sign cores, three references (uniform, nonmatching full support and actual spectrum), all four ordinary parity masks and both affine phases, with every ordinary history. The main field certificate uses l2/l3 and the complete depth-two adaptive maximum with optional stops; no dimension escalation or symmetry quotient occurs. A separate actual GF4 parent checks the asymmetric cut, prescribed second proper ordinary query and both carrier terminals. Exact prime-log identities establish chain equations; rational logarithm enclosures establish strict signs. The mathematical argument, not finite enumeration, proves all-width and all-history statements.

The universal gap is influence-scale funding of a source-dependent pending reserve for arbitrary Boolean cores. For point defects f_n=1-2*1[x=0], every influence is d=2^(1-n) and M/I=h2(d)/d>=n-1. Thus no universal M<=C I can close it. All physical continuations of the supplied field source are now paid up to ONE final conversion, including carrier consumption, so neither ordinary depth extensions nor a separate carrier-breaking query alone address the remaining gap. The next action is one actual INTERMEDIATE reference reset followed by a further query, with its complete signed booking charged to the SAME remaining original capacity after old debits and without reusing the full-M envelope. Both actual terminals and original reference provenance must be retained. Full FEI remains OPEN.
