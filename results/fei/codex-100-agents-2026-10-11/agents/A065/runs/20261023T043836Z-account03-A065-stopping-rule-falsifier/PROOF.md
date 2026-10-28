# A carrier reset after an arbitrary ordinary prefix, paid by the original cap

Units are bits. Every tree is finite; each physical coordinate is revealed at most once. The physical filtration has fair outcomes, regardless of reference predictions. References are normalized and support the actual squared Fourier law. Source-zero rows of every coherent kernel are extended fairly. There is one original expected reserve; no bank is renewed at a descendant. Full terminal entropy remains explicit.

## 1. Two transport envelopes

For an actual Boolean core g and supporting reference R, let p be its squared Fourier law, K=KL(p||R), M=sum_j h2(Inf_j(g)), and TC=M-H(g). On query i, erase its spectral indicator. Positive-source erased rows use kernel k_b(T)=p_(g_b)(T)/(2p^(-i)(T)); zero-source rows use k_b=1/2. Set r_b=sum R^(-i) k_b and normalize R_b=R^(-i) k_b/r_b. Each r_b>0: a positive atom in the normalized actual child spectrum has a positive parent erased source atom and supporting reference atom. Both KL chain rules give

    K=E+O+mean_b K_b,
    E=KL(p||R)-KL(p^(-i)||R^(-i))>=0,
    O=KL((1/2,1/2)||r)>=0.

Erasure conditional KL proves E>=0, retaining every reference-only row. For j!=i, partitioning physical j-edges by bit i proves d_j(g)=mean_b d_j(g_b). Concavity of binary entropy, including endpoints, gives M>=mean_b M_b. Consequently, for a=1 or 2,

    (K+aM)-mean_b(K_b+aM_b)=E+O+a(M-mean_b M_b)>=O.       (1)

These potentials belong to a single original allocation. They are not fresh capacities issued to children. At an inherited stop the full KL is K. At a final product conversion-and-stop it is the actual TC, which is at most M and hence at most K+M. Thus K+M pays all physical query outcome KLs and both kinds of final stop from any supplied entry reference. The nonnegativity of TC also follows from TC=KL(p||the actual product of its marginals), with deterministic marginals included.

## 2. Preserve the carrier until the chosen reset

Use fresh carrier coordinates u,v and C_g=(-1)^((u+v+L(y)+c)v)g(y), where L is any parity of ordinary core coordinates and c is an affine bit. A lifted reference has spectral law Q(s_u,s_v,T)=R(T xor s_u L)/4. The actual law has the same form with p in place of R. Therefore the actual lifted KL is exactly the core K.

For an ordinary physical query j, the two erased core terms are swapped when s_u changes and L_j=1; their sum is unchanged. Thus the normalized reference kernel and both predicted outcomes are exactly those of the core query, also on zero-source rows, and each child reference is again the lift of R_b. The child affine bit is c+bL_j. This proves by finite induction the lift identity for every adaptive ordinary prefix; the policy may depend on all preceding physical outcomes. K,E,O and their chain are exactly the core quantities throughout that prefix.

When fresh v is queried, its erased spectral rows occur in complementary pairs with equal lifted reference mass. The positive-source coherent kernels are complementary on each pair; reference-only pairs have fair kernels. Hence r=(1/2,1/2), O_v=0. Erasure loses no source/reference likelihood information, so E_v=0. Each actual child is g or a signed character multiple of g, with a deterministic surviving u indicator. Each PRE-reset child has inherited KL exactly K; each has H(g), marginal entropy M(g), and actual product KL TC(g). Character multiplication just complements the relevant spectral indicators. This establishes all carrier boundary claims without discarding u or reference-only mass.

## 3. An adaptive prefix followed by one actual intermediate reset

Admit the following policy. Before consuming either carrier coordinate, reveal any finite adaptive sequence of ordinary coordinates, or stop and retain inherited KL. At any such history the policy may query v, stop in either inherited child, convert-and-stop, or ACTUALLY replace both references by their actual marginal products and continue. After that replacement, admit any adaptive PHYSICAL continuation, including u and all surviving ordinary coordinates, followed by an inherited-reference stop or one final product conversion-and-stop. No second intermediate reset is admitted. Randomization is handled by conditioning on its policy seed.

Before v use the potential P=K+2M(core). Its drift pays O by (1). Immediately after revealing v and BEFORE changing references, use the SAME potential K+2M. Both child K and M are unchanged, so drift is zero and every before-reset cut retains its full inherited KL. At the actual reference replacement, use

    P_after=TC(g)+M(g)=2M(g)-H(g)<=K+2M(g).              (2)

The first M in (2) accounts for the actual reset terminal KL TC=M-H; the second accounts for the already allocated continuation envelope. Nothing is rebooked at this descendant. A stop immediately after conversion retains TC. After replacement transport P=K_current+M_current by (1) with a=1. At any later stop retain K_current or TC_current. All potentials are nonnegative and the compensated potential P_current+sum O is a supermartingale under the fair physical filtration, including the cut between the carrier query and reference replacement.

Therefore from a supplied lifted entry law,

    E T_terminal+E sum O <= K_entry+2M(g_entry),         (3)
    E[H_terminal+T_terminal]+E sum O
       <= K_entry+2M(g_entry)+E H_terminal.              (4)

T is the FULL actual inherited KL or actual product TC appropriate to the stop. The full terminal entropy in (4) is present on both sides; (3) is not an entropy-free terminal argument or an FEI theorem. The potential also allows final carrier conversion with no continuation as a special case.

## 4. The field fixture: the old original cap already suffices

Use the existing field selector fixture: l>=2, q=2^l, m=3l, h(a,b,x)=psi(a)(1-2*1[x=ab]) over GF(q), nontrivial additive psi, all-core parity carrier, and selector choosing C_1 or C_h. Keep the ORIGINAL uniform product spectral reference and its actual Bayes descendants; do not reset after the selector. The established field construction gives

    r_G=1/(2q), r_H=1-r_G,
    K_G=2l-1, K_H=m-H_h+log2 r_H,
    K_root=O_selector+(K_G+K_H)/2,
    Sbar=2m+2-H_h/2.

The selector erasure credit is zero, and all reference-only mass remains. Apply (3) with M(1)=0 and M(h)=M_h. The root expected reserve for the NEW prefix policy is at most M_h: use K_G in G and K_H+2M_h in H, with their true physical weights 1/2 each. Thus

    E T_terminal+E sum_all_queries O <= K_root+M_h.      (5)

This is an expected-root allocation and MAY allocate more than the old uniform per-branch cap to the H branch. It is not a claim that each branch is bounded by the same old conditional W. The bank is an original expected owner, not a pathwise bound.

Physical edge counting gives p=2/q-2/q^2 and

    M_h=2l*h2(p)+l*h2(2/q).

For a/b directions, an edge changes the defect at two points except in the zero multiplier slice, giving p or its complement according to psi. For x directions it gives 2/q. Entropy ignores complementation. These formulas hold in any field-coordinate basis. For l=2, M_h<=6<8=m+2. For l>=3, p,2/q<=1/4, so M_h<39l/16<3l+2: h2(1/4)=2-(3/4)log2 3<13/16 follows from the exact integer sign 3^12>2^19. Consequently the OLD ORIGINAL expected cap W=m+2 pays (5) at every width, and the additional owner allocation is ZERO if W was already reserved for this admitted policy. If only a nested pending booking theta<=W was reserved, top up ONCE by W-theta; already consumed transactions stay in unrelated omega and are not refunded.

Keep old unrelated consumption 0<=omega<=Sbar/4. The field entropy satisfies H_h<=m, and H_h=5 for l=2. For l>=3,

    (5/7)Sbar-W >=(3l-8)/14>0;

at l=2 the difference is 3/14. Therefore W<(5/7)Sbar and Sbar-omega-W>Sbar/28, with precisely the SAME original owner. One could reserve the smaller M_h for this specific policy, but the statement retains the already allocated W and does not reclaim its slack.

## 5. Scope, review and the first unsupported line

This closes A064's named next target for ANY ordinary prefix, not just one query, before the first carrier/product intermediate reset. It includes inherited stops, the pre-reset boundary and all post-reset physical continuation. It preserves A061's ordinary/carrier terminal policy as a subclass. It does NOT assert union with A064's separate mode that permits arbitrary physical queries BEFORE deciding whether to reset: querying u earlier may destroy the fresh-carrier interface. A064's old union theorem remains valid at its own original scope. The new expected branch allocation is not its uniform per-branch allocation. No unproved union of policy classes or hidden rebudgeting at a reached descendant is used.

A064's unchanged stage18 theorem was reconstructed here through a different potential derivation: its general envelope is (1) with a=1; at its immediate carrier switch the signed H-branch debit is 2M_h-m-log2(r_H)<m+1<W, since M_h<=m and r_H>=7/8. Both pre-reset child KLs equal K_H and its boundary potential max(K_H,2M_h-H_h) is at most K_H+W. Its G debit is negative, original mode A uses K+W, and original owner arithmetic is exactly as above. No repair of that theorem was supplied. The theorem-level reconstruction HOLDS at its original scope. Since A065 contributed earlier carrier-history inputs, this is NOT an independent acceptance of the entire dependency chain and cannot supply one of two independent full-chain reviews.

The first unsupported UNIVERSAL line is an eligible unused influence-scale original owner for the signed pending reserve at arbitrary sparse non-carrier histories. Even the coarse 2M envelope fails to be influence-scale: for f_n=1-2*1[x=0], with d=2^(1-n), M/I=h2(d)/d>=n-1. Nor does this stage pay a second intermediate reset or a reset after an earlier carrier query. These are mechanism boundaries, not Boolean FEI counterexamples. The exact adaptive stopping reserve and the full source-supporting inherited reference must be retained when testing such a mixed query next. Independent review of this new prefix extension remains pending.

## 6. Independent reconstruction of the field identities used in section 4

Identify additive characters with the field through its nondegenerate trace pairing and write psi(a)=chi(t a), t!=0. The Fourier coefficient of the defect term psi(a)1[x=ab] at (alpha,beta,gamma) is q^(-3) sum_(a,b) chi((t+alpha)a+beta b+gamma ab). If gamma=0 this is 1/q only at (alpha,beta)=(t,0), otherwise zero. If gamma!=0, sum over b first: only a=beta/gamma survives, giving coefficient q^(-2) chi((t+alpha)beta/gamma). Hence h has one Fourier coefficient 1-2/q at (t,0,0), and q^2 coefficients of magnitude 2/q^2 for each nonzero gamma. The empty coefficient is zero, including q=4. Squaring gives the stated spectrum and normalization. Its entropy is at most log2(q^3)=m. At q=4 there is one atom1/4 and48 atoms1/64, so H_h=1/2+48*(6/64)=5.

The fresh carrier has uniform four-atom spectrum before the stated parity shear; that shear maps the core spectral indicator by T -> T xor s_u L. It therefore adds exactly2 to H. Its u,v influences are1/2. Each masked ordinary direction has influence1/2 by averaging v=0,1, since the parity factor switches whether the core edge agrees. Both children have all influences1/2. Selector influence equals Pr[h=-1]=1/2 since h is balanced. Thus the original product reference really is uniform, and the source Sbar formula follows from the actual child influences and entropies.

The G and H spectra have disjoint supports (the empty core atom is not in supp h). Parent selector Fourier coefficients are (Ghat+Hhat)/2 and (Ghat-Hhat)/2; disjointness makes the two squared entries equal on every positive erased row. This proves E_selector=0 with the uniform reference. The coherent outcome kernel selects G on its support, H on its support and is fair elsewhere. With N_h=1+(q-1)q^2, the G predicted reach is 1/q^3+(1-(1+N_h)/q^3)/2=1/(2q). Normalization gives precisely R_G,R_H and K_G,K_H in section4. The same disjointness gives H_parent=4+H_h/2 and K_root=m-1-H_h/2, consistent with the exact chain. All identities used for the original field account have now been reconstructed without assuming an unreviewed all-width numerical survey.
