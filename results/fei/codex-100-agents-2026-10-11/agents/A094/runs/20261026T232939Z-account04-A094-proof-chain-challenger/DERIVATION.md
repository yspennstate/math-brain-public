# A094 stage21: one-selector reconstruction and the query-contraction boundary

All logarithms are base 2. The FEI conjecture remains open. This audit distinguishes an actual transaction bill from a terminal functional, even when both contain signed reset terms.

## 1. Full physical-query ledger

Fix one Boolean target on one finite cube. At a node v, P_v is its actual Fourier probability law and Q_v is the current covering subprobability reference. Define CE(P,Q)=-sum P log Q and D=CE-H, retaining scalar mass penalties. A physical query produces both true children and the actual inherited references Q^inh_vb. Write

 delta_v=lambda_v[D(P_v||Q_v)-(D(P_v0||Q^inh_v0)+D(P_v1||Q^inh_v1))/2].

For the inherited model convention in the sources, delta_v>=0. A prescribed child reference R_vb incurs actual signed charge

 e_vb=(lambda_v/2)[CE(P_vb,R_vb)-CE(P_vb,Q^inh_vb)].

The complete inherited query release is lambda_v[H(P_v)-avg_b H(P_vb)]+delta_v. Sum releases and actual conversions over a finite adaptive tree. Every interior CE cancels, leaving the exact identity

 CE_root+sum e_vb = H(P_root)+sum delta_v+sum_leaf lambda_v D(P_v||R_v).

All child references, including reference mass on true-zero atoms, are retained. No entropy monotonicity is needed for this telescoping identity; it is finite algebra. It applies to subprobability references as well as normalized ones. The target is FIXED during the tree; a target-changing edit is a separate transaction and cannot be identified with a same-target reset.

Consequently A011 DERIVATION equation (6) correctly DEFINES a terminal functional L=H_root+E D_terminal. Its identification with root CE plus actual signed resets omits sum delta_v. This is an ERROR in that identification, and a GAP in interpreting its functional bound as payment of the entire physical transaction bill. It does not refute A011's terminal-functional inequality, constants, cylinder partition identity, or full FEI. Source v5's exact statement defines L as the functional, so its numerical assertion is not declared false here.

## 2. Exact witness inside A011's allowed family

Take the one-bit dictator g(x)=(-1)^x (so g(0)=1), a=1, b>=12 untouched padding bits, n=a+b, epsilon=2^-n, one fresh fair control w. Its supplied original reference is P_g itself, mass one, c=0 and C0=0. The actual target is F=g-2 indicator(x=0,padding=0,w=0). This is A011's M=1,r1=1 construction; the global edit probability is epsilon/2, hence its actual first floor has beta=3epsilon.

There is one source mask with A=1 and 2^n-1 masks with A=0. Group these by exact multiplicity. Parent data marginal is q(A)=(A-epsilon)^2+epsilon^2. Parent data reference is R(A)=(A^2+3epsilon^2)/(1+3epsilon), lifted by the TRUE selector kernel. On exposing w, P_clean(A)=A^2 and P_edit(A)=(A-2epsilon)^2. The raw inherited child reference is R(A)P_child(A)/q(A); its normalizer is Z_child. Exactly Z_clean+Z_edit=2 and

 Z_clean=(1+3epsilon^2)/[(1+3epsilon)(1-2epsilon+2epsilon^2)] < 1.

The strict inequality follows because denominator minus numerator equals epsilon(1-7epsilon+6epsilon^2)=epsilon(1-epsilon)(1-6epsilon)>0 for 0<epsilon<1/6. Both normalizers are positive by cover. Thus

 1-Z_clean Z_edit=(1-Z_clean)^2>0,
 delta=-log(Z_clean Z_edit)/2>0.

At the clean leaf A011 prescribes P_g; at the edited leaf its r_local=0 first floor is (P_g+6epsilon Uniform)/(1+6epsilon). These are EXACTLY the current v5 prescription, with all zero-fiber model mass retained. Whatever those actual signed conversion values are, the full bill differs from A011's L by this strictly positive delta. The example respects b>=12, nonconstant source, finite covering initial reference, one nonempty global control block, actual edit point, and an allowed physical tree. It isolates the missing term without extrapolating a generic dictator test beyond its hypotheses. The exact checks use b=12,13; the displayed factorization proves the all-b assertion analytically.

The full-tree implication is especially clear: at constant leaves with normalized scalar references, terminal divergence is zero. L=H_root then follows by definition, whereas a full transaction bill can still contain positive query contractions. A bound on L alone cannot silently erase these charges.

## 3. Independent reconstruction of A086's one-selector upper price

Take ANY Boolean source on a>=0 bits, including constants; normalize its value at the edited point to 1 by global sign. There are m>=8 untouched padding bits, epsilon=2^(-a-m), u=2^-m, and M=1/epsilon full data masks. The edited child has coefficients A-2epsilon. Prescribe

 T(A)=(A^2+6epsilon^2)/(1+6epsilon).

This is the complete normalized reference (P_g,embedded+6epsilon Uniform)/(1+6epsilon); it covers every full data mask. For the N nonzero original coefficients, Parseval gives sum A^2=1 and the Boolean integer Walsh lattice gives |A|>=2^-a (a deliberately weak bound, also valid at a=0). Therefore sum A^-2<=2^(2a)N and N<=2^a.

The numerator of p_edit-T is epsilon[6A^2-(4+24epsilon)A-2epsilon+24epsilon^2]. Minkowski in the weighted l2 norm, denominator A^2+6epsilon^2>=A^2, and |-2+24epsilon|<=2 give an old-support chi-square square root at most

 epsilon[6+(4+24epsilon)sqrt(N)+2epsilon( sum A^-2 )^(1/2)]/sqrt(1+6epsilon)
 <=epsilon sqrt(N)(10+24epsilon+2u)<11epsilon sqrt(N).

The zero-source masks contribute at most (2/3)epsilon to chi-square: their exact difference numerator is epsilon^2(-2+24epsilon), and there are M-N of them. Hence chi-square<121N epsilon^2+(2/3)epsilon. Jensen for log gives D_bits<=log2(1+chi-square)<=chi-square/ln2, and 1/ln2<3/2. Thus

 D(P_edit||T)<[1+(363/2)u]epsilon<2epsilon, since u<=1/256.

All canceled denominators are positive. N>=1 by Parseval; the a=0 and constant endpoints are included. The complete finite-cost incoming child reference may have ANY mass in (0,1]. Its CE is at least H(P_edit), so its signed conversion to T is <=D(P_edit||T). Multiplying by actual child reach lambda/2 proves positive booking <lambda epsilon. On the clean child P_g is a normalized true law and costs H(P_g), so its actual signed conversion is <=0. The latter credit is not refunded in the positive-booking bound.

For an actual parent exact-source floor, every q(A)>0. Its actual inherited child is normalized using Z_child; normalizers are not replaced by 1. The checker explicitly constructs both full inherited models, including all true-zero atoms and scalar half-mass tests. This also exposes the positive contraction from section 2.

## 4. Owner and full-chain scope

Append ONE selector exposure at edited-source depth d<=a of the already accepted source-first chain. The previous entry and source-floor upper costs are each <lambda_initial epsilon_initial, because reach halves while local epsilon doubles. The selector adds one such term. Total new positive bookings <(d+2)lambda_initial epsilon_initial. For nonconstant g, a>=1, edge isoperimetry gives I_g>=a/2^(a-1), so (a+2)2^-a<=3I_g/2. With u<=1/256 the total is <=3I_g/512 at root reach one. The prior supplied-root residual >=7I_g/8 therefore retains >445I_g/512. This uses the ORIGINAL supplied reference and full compatible old U; it produces no new source certificate.

In the actual original-rate4 A095/A086 two-reset h4*h2 history, current child00 has reach1/4, source -h4 on four bits, epsilon=2^(-m-4). Entry, up to four source floors and the selector together cost <6*(1/4)*2^(-m-4)<=6/16384. Subtract from the previously audited original remaining >3/256 to obtain >93/8192. ALL old p1,p2, unchanged full siblings and actual query releases remain. This reconstructs A086's named selector claim without supplying a repair. The root allowance dependency was authored by A094 in an earlier stage; that contribution conflict is disclosed for the corollary. The standalone all-source selector estimate and the actual rate4 consequence are independently reconstructed here using prior fully audited dependencies.

## 5. Checks that could fail and the remaining line

The independent checker tests signed Walsh coefficients, constants/a0, all labelled sources through three bits, mass-one and half-mass parents, a four-bit -h4 embedding, true reference cover, exact dummy multiplicities, both inherited normalizers, chi-square bounds, actual signed charges, and both complete terminal CEs. Sign decisions use rigorous rational log intervals. Identity interval overlap is a diagnostic; the algebra above establishes equality. The A011 witness also has the exact rational certificate Z_clean Z_edit<1, so its sign does not depend on a floating entropy difference.

A086's one-selector result HOLDS at its conditional scope. A011's functional-to-transaction identification has the precise missing term sum delta_v; complete-policy payment is NOT independently accepted. A011/A086 should either explicitly book and pay that term from the SAME unused original account or state only the terminal-functional result. No repair or upper estimate for arbitrary-policy accumulated contractions is supplied here. The universal initial O(I_g) source is still unpaid under either interpretation; full FEI remains OPEN.
