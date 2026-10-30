# Affine branching from the SAME original reserve; exact nonflat tax

Finite uniform cubes, bits of entropy. Let A,B be arbitrary Boolean functions of the SAME data x. Selectors z are independent of x. Let a(z) be a0/1 indicator with probability alpha=2^-r, r>=1, and F=B+a(A-B). Set delta=Pr(A!=B), E=I(AB), K=alpha H(A)+(1-alpha)H(B), D_a=H(F)-K. All inherited core entropy stays present.

## 1. Exact arbitrary-selector collision posterior

For each data Fourier row put u=Ahat(T), b=Bhat(T), d=u-b, R=alpha u^2+(1-alpha)b^2, v=alpha(1-alpha)d^2/R if R>0. The selector-empty amplitude is b+alpha d; other amplitudes are ahat(U)d. The normalized nonempty selector spectrum is q(U)=ahat(U)^2/[alpha(1-alpha)]. Hence EXACTLY

    D_a=sum_T R h(v)+V H(q)+sum_T J_alpha(u,b),
    V=4alpha(1-alpha)delta,
    J_alpha=alpha u^2 log2(u^2/R)+(1-alpha)b^2 log2(b^2/R).

This explicitly preserves coherent amplitude addition at the empty selector sector. It is not a disjoint-input composition rule for the shared cores. Every displayed summand is nonnegative, including the convexity gap J, so D_a>=0. This posterior and nonnegativity hold for EVERY 0<alpha<1; the reciprocal-power hypothesis is needed only for the flat-point comparison. At alpha0 or1, D is0 directly. Thus arbitrary physical restrictions of a nonflat child, including ones with probability3/4, still have the required nonnegative frontier reserve without any new source admission.

If a is an affine-subspace indicator of codimension r, its Fourier support is an affine character times a size2^r row space; all nonzero amplitudes have magnitude alpha. Thus H(q)=log2(2^r-1). The exact D_a is then identical to the v8 point-selector D_r for the SAME A,B. It depends on codimension, not the position or embedding of the affine subspace.

## 2. Physical outer source admission, including TWO surviving branches

Write a=1_{Lz=c}, with L an r-by-k full-row-rank binary matrix. Let j be a physical selector coordinate whose column c_j is nonzero, and G,H the two actual restrictions of F. The XOR of the two restricted activation indicators is the indicator of an affine subspace of the remaining selectors defined by the quotient constraints modulo span(c_j). This quotient has rank r-1 and activation probability2alpha. Both child cosets survive if c_j lies in the span of the other columns; otherwise exactly one survives. Let m_j count the other columns outside {0,c_j}. The quotient has rank r-1, so m_j>=r-1. Direct physical edge counting gives

    Inf_j(F)=2alpha delta,
    I(GH)=2alpha E+4alpha m_j delta,
    B_j:=4Inf_j(F)+I(GH)=2alpha E+4alpha(m_j+2)delta
       >=2alpha E+4alpha(r+1)delta=:B_flat.

Thus the v8 bound D_r<=3B_flat proves D_a<=3B_j for ANY nonzero physical column, including a root with two surviving branches. This is ONE original ticket at the designated original root, not a sum of tickets for the branched tree.

## 3. Zero coherent price for a genuine affine fork

If both restricted cosets survive, each has codimension r on the remaining selectors, and each child has activation probability alpha. Therefore K_child=K_parent and D_child=D_parent, separately on BOTH children, with their actual changed affine targets. The coherent query debit D_parent-E D_child is exactly0. These are actual relevant physical queries: Inf_j(F)=2alpha delta can be positive. No unused account is reset or replenished.

If just one child survives, it has codimension r-1 and probability2alpha; the other selects B outright. The coherent debit is D_r-D_(r-1)/2, exactly the v8 rare-chain debit. Repeated physical restrictions therefore alternate free forks and already priced rare-chain steps. Data restrictions keep A,B arbitrary and preserve the same posterior calculation.

For ANY finite adaptive selector/data stopping tree, exact telescoping yields

    H(F_root)-E H(actual leaves)-sum_data w Delta K
       =D_root-sum_live_leaves w D_leaf <=D_root<=3B_j(root).

The account is the original3B_j, with prior signed debit retained. Its expected unspent frontier balance is the original slack3B_j-D_root plus sum_live w D. No descendant source formula replaces it. All signed inherited data-core terms and both complete actual terminals remain. After selection resolves, subsequent core queries are inherited charges. This proves the supplied-source continuation through any number of surviving affine forks, not merely a disjoint-block chain rule.

Concrete positive-old-debit control: take A=1,B=x and a=1_{z0=1 and z1 XOR z2=1}. First reveal z0. Here D_root=4-(9/8)log2(3), and the first debit is 3-(9/8)log2(3)>0. On the surviving branch, revealing z1 gives TWO surviving affine targets for z2 and has debit0. Subsequent z2 bills total1 in root reach units. The original B_z0=5/2 and original3B=15/2 stay unchanged throughout; total cost is D_root, and both final core entropies are zero. This is an actual fork AFTER a positive debit, not a dummy-variable example. The physical parity embedding has m_z0=2, so its root source is larger than the canonical r2 point source2; these must not be confused.

## 4. Exact price of breaking Fourier flatness

For ANY selector indicator a with alpha=2^-r, compare with an r-bit point indicator p_r and write s=1-2a, s_flat=1-2p_r. They have equal empty Fourier amplitude and equal total nonempty spectral mass4alpha(1-alpha). Their normalized nonempty spectra have entropies H(q) and log2(2^r-1). Consequently, exactly,

    D_a=D_flat+delta[H(s)-H(s_flat)].                 (*)

The tax is nonnegative. Indeed |ahat(U)|<=alpha, so q(U)<=alpha/(1-alpha), whence H(q)>=log2((1-alpha)/alpha). Equality requires a flat nonempty selector spectrum. Thus affine forks are free precisely because no new selector spectral entropy is created; a general nonflat selector incurs the explicit positive tax in (*).

If a complete supplied selector FEI bound H(s)<=C_s I(s) is available, the tax is at most C_s delta I(s)=C_s I_selectors(F). This is a CONDITIONAL transfer, not a proof of universal selector FEI and not admission to an already diminished ancestor bank. The source3B_j admission above uses affine geometry and is not asserted for arbitrary nonflat selectors.

Nonflat control: choose a to indicate the four vertices of weight<=1 in F2^3, so s is a majority phase up to sign, alpha=1/2, H(s)=2 (FOUR squared Fourier atoms1/4); the point reference has H(s_flat)=0. With A=1,B=x, delta=1/2, D_flat=2, so the actual nonflat overhead is3 and the additional tax is1. An affine-free-fork assertion for this changed profile would therefore omit a positive bill.

## 4b. A genuine nonflat continuation paid from ORIGINAL surplus

Let a_child have probability p=2^-r, phase s=1-2a_child, and introduce ONE fresh outer fair bit t. Activate A only if t=1 and a_child=1, otherwise select B. The initial alpha=p/2. The ACTUAL original outer ticket is

    B_original=p E+4p delta+delta I(s).

The flat point comparison has B_flat=p E+2p(r+2)delta. Their difference is exactly delta[I(s)-2rp], a physical selector surplus. The same row-entropy calculation, now for the selector phase itself, gives

    H(1-2*1_{t=1}a_child)-H(point_phase_(r+1))
      =(H(s)-H(point_phase_r))/2.

Therefore the total coherent overhead is D_flat_(r+1)+delta[H(s)-H(point_phase_r)]/2. If the COMPLETE supplied selector satisfies the precise surplus criterion

    H(s)-H(point_phase_r)<=6[I(s)-2rp],               (S)

then total overhead<=3B_flat+3delta[I(s)-2rp]=3B_original. This is admission to the ORIGINAL larger physical account, not a new ticket after the old debit. The initial account includes that surplus exactly once. The outer coherent debit equals the corresponding flat outer debit: the parent tax is exactly the reach-weighted child tax, so they cancel in that first decrement. Both inherited A,B bills remain present.

Unconditional genuine nonflat example for ALL Boolean A,B: a_child=weight<=1 on3 bits (balanced majority phase). Here p=1/2,r=1,H(s)=2,I(s)=3/2,point_phase_1 has H=0 and I=1. Criterion(S) reads2<=3, leaving original slack at least delta/2 after the nonflat tax is allocated. For A=1,B=x the actual B_original=9/4, initial3B=27/4, total D=9/2-(9/8)log2(3), first old debit=3-(9/8)log2(3)>0, and the reached nonflat child bill is3/2 in root reach units, including tax1/2. Both complete final cores have entropy0. The extra selector energy was present at the ORIGINAL root; no reserve is renewed.

This pays a necessary nonflat child after a positive debit, beyond the free affine fork. Criterion(S) is NOT asserted for arbitrary selectors. Its all-dimensional universal version would require further mathematics; a complete supplied selector FEI bound alone is not silently substituted for this sharper surplus admission.

## 5. Universal boundary

v9 closes the second-surviving-branch step for all affine activations and the genuine nonflat majority continuation after actual old debit, with the SAME original allowance and arbitrary shared cores. The exact new line for an arbitrary selector is the tax delta[H(s)-H(s_flat)] and its ORIGINAL physical surplus admission(S). Criterion(S) is supplied, not universal. Claiming it unconditionally is the first unsupported universal line. Arbitrary core A,B entropies remain unpaid. NEXT must pay a necessary nonflat child OUTSIDE the sufficient surplus criterion from the SAME actual remaining ORIGINAL account after the old prefix debit, using the full existing slack and both terminal bills, or certify that admission fails. Physical data telescopes are already covered; another free affine fork does not address the universal obstruction. Full FEI remains OPEN.
