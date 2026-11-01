# Independent reconstruction of A066 source payment v4

All costs below are bits. Reviewed source: A066 run20261023T113807Z, DERIVATION.md and claim A066-NONFLAT-DATA-RELEASE-AND-SOURCE-PAYMENT@4, statement hash3d140b42344fef85bd4ed28b9a5fe58a976d1b24e505ec59be908102d235c802. No repair is supplied. This review addresses the supplied-source theorem; it supplies no arbitrary-core reference or FEI proof.

## Probability and group reconstruction

For M=Maj3 its four nonzero squared coefficients, at masks W={1,2,4,7}, are1/4. Product multiplication on disjoint physical blocks gives P_F=delta_{t,x} tensor Uniform_W tensor P_g. Hence H_F=2+H_g and I_F=7/2+I_g. For the prescribed original reference delta_{t,x} tensor q tensor Q_g with q=(1-3epsilon,epsilon,epsilon,epsilon) on W, the FULL CE is C_g+c, with epsilon=2^(-3K) and c=9K/4-log2(1-3epsilon)/4. This statement retains every Q_g ghost. Since1/2<1-3epsilon<1, 9K/4<c<9K/4+1/4 for all integerK>=4.

The frequency map with columns2,4,7 has table(0,2,4,6,7,5,3,1). It preserves XOR, fixes0, and its fourth power is the identity. It cycles W. Thus it is an invertible linear map on F2^3 and is realized by inverse-transpose physical input change. There is no assertion that it preserves every coordinate influence, nor is that needed: the operation changes only the reference at the SAME actual function. Squared-spectrum invariance of the actual Maj factor is what licenses the refund.

Both t and x are present in every ACTUAL occupied label. Deleting either frequency is therefore a bijection on actual support, independently of the physical query sign. It is also a bijection on the supplied reference support, including Q_g-only labels. Consequently complete source CE is unchanged by either literal projection, all actual erasure and outcome KL releases are zero, and both complete children remain. The queried singleton Fourier coefficient is zero because E(M*g)=0; every coefficient pair that differs only in the queried private bit has one zero member. Thus the singleton energy, ALL nonempty phase-bin energies, true entropy decrement and vacuum calibration refund are zero. Zero means persist after both queries.

## Original account and the exact scope of necessity

Write B_g=K I_g-C_g>=0, A=K(I_g+7/2), and permanently withhold tau=B_g+1/4. This is A066's supplied original quota and declared old liability, not a renewed descendant price. After charging the first actual t invoiceK,

    S_t=A-K-(C_g+c)-tau=5K/2-c-1/4,

which lies strictly between K/4-1/2 and K/4-1/4. Retaining the literal reference while paying x would leave

    S_raw=3K/2-c-1/4<-3K/4-1/4<0.

Thus a change or another legitimate payer is NECESSARY for THIS prescribed two-query, fixed-invoice policy with THIS original profile and tau. This is not an intrinsic lower bound forcing every FEI proof to make this conversion. In particular it is permissible to choose a different initially priced source in another argument; the theorem does not forbid that.

At the actual already-paid t frontier, average the CURRENT reference over the four powers of the displayed map. Each image has identical full CE against the actual invariant spectrum; convexity of -log shows the average cannot increase it. Here direct summation shows its majority factor becomes Uniform_W, while Q_g is unchanged, so the refund is exactly c-2. Apply that refund BEFORE x, giving

    S_mid=5K/2-9/4>0,
    S_final=3K/2-9/4>=15/4.

All four signed terminal branches have complete bill C_g+2. The equality

    2K+(C_g+2)+(K I_g-C_g+1/4)+(3K/2-9/4)
      =K(I_g+7/2)

reconstructs every original debit and remainder without approximation. Off-path bills may be excluded only if the displayed A really is the available original quota after they are withheld; no off-path reserve is assumed. At K4,g=1 the five-bit witness has A14,tau1/4 and final15/4. A066's bounds for c and the positive intermediate bank follow directly from4093<4096<2*4093.

## General orbit defect and semigroup clauses

Let P_G and Q_G be orbit averages, with Q positive on the union of actual orbit supports. The full signed change is sum P log2(Q/Q_G). Adding and subtracting P_G gives exactly -R_G+T_G, with R_G=sum P_G log2(Q_G/Q)>=0 by Jensen at invariant P_G and T_G=sum(P-P_G)log2(Q/Q_G). No sign is assigned to T_G. The actual dictator supported at mask1 costs -log2(1-3epsilon)<1 before averaging and exactly2 after, so a source-only orbit argument fails: the increase is>1. The normalizations and finite-cost hypothesis are essential.

For a finite Fourier spectrum, each nonempty term in the stated heat integral is a constant multiple of exp(-2s|S|); integration yields p(S)ln(1/p(S))/2. Finite summation proves both endpoint integrability and2K_heat=ln2 H-b_empty. Here all physical means vanish, so b_empty=0, entropy is unchanged and no positive heat dissipation pays the reference change. The refund is a complete CE change, with natural-log cost ln2*(c-2). These clauses reconstruct without a repair.

## Validation and formal boundary

code/check.py is a separate direct Walsh/physical-edge/current-reference implementation. It proposes144 fixtures over24 frozen cores, three integer rates and two references; only inputs satisfying the supplied CE<=K I premise are admitted. Both branches after each actual query and complete ghost-bearing references are checked. The finite instances corroborate the all-dimensional proof above; they do not prove its universal quantifiers.

code/Orbit.lean contains only the finite C4/XOR structure certificate, since conflating a support permutation with a physical linear symmetry would invalidate the source-refund argument. out/LEAN_RESULT.json records whether its EXACT target was kernel checked or admission held it. No analytic CE, convexity, account, heat or full FEI theorem is claimed formalized. Compiler success is accepted only with the target theorem and its transitive axioms reported by the checker.

First unsupported universal line: find useful actual orbits and bound their noninvariant defect T_G by the SAME original unused allowance plus legitimate R_G, or supply a complete influence-priced reference for every Boolean core. A066 closes the invariant supplied-source example only. A096's geometric ancestor compression also retains a potentially positive normalizer; it cannot make the missing general payment free.
