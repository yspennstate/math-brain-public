# Individual activation eligibility and a paid later controller exposure

Uniform finite cubes, Boolean signs, and entropy/KL in bits throughout. Full FEI is OPEN. The generic entropy criterion below is universal; the original-source/reset continuation application uses the explicitly supplied point-tensor reference, not an unpriced arbitrary Boolean supplier.

## 1. Exact weakest criterion for BOTH activation children

For any Boolean core g let mu=Eg, u=|mu|, S4(g)=4I(g)-H(g), and J_s(x,z)=s on x0,g(z) on x1, s=+/-1. Define with zero-log conventions

    L(u)=[(1+u)^2 log2(1+u)+(1-u)^2 log2(1-u)
          -u^2 log2(u^2)]/2.

Its endpoints are L(0)=0,L(1)=2. Direct Fourier expansion gives the two zero-data masses (s+mu)^2/4,(s-mu)^2/4 and two copies p_g(T)/4 for each nonempty T. Summing their entropy, including the actual empty core mass mu^2, gives the EXACT identity

    H(J_s)=H(g)/2+2-L(u).

Direct pivotal probabilities give I(J_s)=(1-s*mu)/2+I(g)/2. Consequently

    S4(J_s)=S4(g)/2+L(u)-2s*mu,
    min_s S4(J_s)=S4(g)/2+L(u)-2u.             (1)

Thus BOTH actual activation children satisfy H<=4I if and only if

    S4(g)>=Theta(u):=4u-2L(u).                 (2)

This is the weakest possible additional hypothesis for that particular two-child eligibility conclusion: it is necessary and sufficient, not a claimed globally weakest FEI repair. It does not supply a source reference or price a reset. A bound H(g)<=4I(g) alone is not substituted for (2). No assertion that every Boolean core meets (2) is made.

## 2. A simple sufficient hypothesis, with a complete scalar certificate

The useful weaker-to-check condition is

    S4(g)>=1-|Eg|.                            (3)

It implies (2) because

    L(u)>=(5u-1)/2,  0<=u<=1.                (4)

Here is an analytic/exact interval proof of (4), with every seam covered. On(0,1), differentiating the displayed definition gives

    L'(u)=(1+u)log2(1+u)-(1-u)log2(1-u)-2u log2 u,
    L''(u)=log2((1-u^2)/u^2).

L' starts at0, increases to u=1/sqrt2, and then decreases to its endpoint limit2. Hence L'>=0 and L>=0. For D(u)=L(u)-(5u-1)/2 this proves D>=0 on[0,1/5].

On[1/5,3/4], the three absolute terms of L' are bounded respectively by7/4,8/5,9/2, using log2(1+u)<=1, |log2(1-u)|<=2 and |log2 u|<=3. Thus |D'|<=7/4+8/5+9/2+5/2<12. Partition this entire interval into512 adjacent rational cells of equal length11/10240. At every midpoint the exact rational32-term atanh bound for D, minus12 times the half-cell length, is strictly positive. out/SCALAR_CELLS.json records ALL endpoints, midpoint intervals and entire-cell lower bounds. code/scalar.py checks adjacency, exact first/last endpoints and every positive lower bound. This is a finite certificate of a continuum inequality, not a floating grid inference. The minimum certified middle lower bound is greater than1/50.

On[3/4,1], L''<0, so D is concave; D(3/4)>0 is separately certified and D(1)=0 exactly. Its endpoint chord is nonnegative throughout. Together the three CLOSED pieces prove(4), including u=0,1/5,3/4,1. No uncovered seam or limiting numerical estimate is used.

Combining(1),(3),(4) gives S4(J_s)>=0 for EACH sign individually. This replaces the earlier need to retain a paired-mean cancellation merely to certify terminal entropy surplus. It does not remove the need to retain the other branch's actual debt in the source account.

## 3. Every restricted point tensor satisfies the simple hypothesis

For a width-r>=2 point sign, defect d=2^-r, mean1-2d, and influence2rd, the nonempty entropy is8(r-1)d(1-d). Empty entropy is at most4d(1-d)/ln2<6d(1-d), because ln2>2/3. Therefore

    S4(point)>2d+(8r-2)d^2 >=2d=1-|E point|.

A width-one surviving point is a signed character: S4=4>=1. Constants have S4=0 and absolute mean1. A restriction of a signed disjoint point tensor is a product of these factors. Entropy and influence add, absolute means multiply, and sum_j(1-u_j)>=1-product_j u_j for0<=u_j<=1. Hence(3) holds for EVERY physical data restriction, including zero means, constants and irrelevant coordinates. In particular every remaining activation terminal individually has S4>=0.

This is the application-specific additional hypothesis that repairs the attempted arbitrary selected controller continuation. The exact test(2) admits any other Boolean core that satisfies it; the simpler test(3) is sufficient and restriction-stable for the entire point-tensor family. Arbitrary Boolean cores and unrelated non-point reset profiles are not admitted for free.

Additional exact scope: code/audit.py checks(3) for ALL256 truth tables on three bits by direct character sums and direct physical pivots, including embeddings of every smaller function. A tensor of arbitrary disjoint factors using at most three bits therefore satisfies(3), as does every physical data restriction, by the same additive-surplus/multiplicative-mean argument. Its activation terminals and selected-x children have nonnegative surplus. This is an entropy eligibility statement only: no occupancy-shape monotonicity, initial supplier price, or free reference reset for these arbitrary non-point factors is asserted.

## 4. Reconstruct the already-paid inherited-reference input

Use A050's ORIGINAL1/8 correlated complete reference Q for F_h: x0 is the a-character, x1b0 is+1, x1b1 is h, with any finite heterogeneous disjoint point tensor h of widths>=2. Query b, retain b0, take any finite adaptive data prefix in b1, and expose a at selected frontier leaves, retaining BOTH signs and all complements. Make the first full1/7 activation reset as specified in A073-ACTIVATION-NONEMPTY-OCCUPANCY-REFRESH@1. No earlier canonical reference is converted to Q for free.

Let A0=D(P_F||Q),M0=4I(F)-CE(P_F,Q). The original point supplier gives M0>1+2Pr(h=-1)+sum_j d_j/4. The first reset's ACTUAL weighted increment sigma1<=T1<=sum d_j(1-d_j)log2(7/6)<sum d_j/4, since7^4<2*6^4. Thus M0-sigma1>1, with sigma1 still explicitly booked. No later source bank is created.

Here is the critical later-reset argument, reconstructed from A073. Starting from a fresh activation reference, on each NONEMPTY data row the two x copies are equal and data transport updates their common profile by the pure-core coherent kernel, up to a single common normalization. Consequently their conditional law given nonempty data is a product of the actual transported block references conditioned on at least one occupied block. The two exceptional vacuum masses need not match the actual source; they are retained, not reset for free. Sequential transport is used, not the false cumulative-erasure shortcut.

In a surviving block, full/ordinary nonempty ratio evolves as R'=(1+R)/2. After any surviving data prefix from last fresh defect v to current defect d,

    R_old=1+(1-v)/(6d) >= R_fresh=1+(1-d)/(6d)>=1.

The actual conditional nonempty block spectrum is uniform on N=2^k-1 points. Its cross-entropy against relative full weight R is Phi_N(R)=log2(N-1+R)-log2(R)/N, increasing for R>=1. Given the vector of occupied blocks, conditional product structure therefore gives

    CE(P_core^+,Q_old^+)-CE(P_core^+,Q_fresh^+)
      = D(P_occupied^+||Q_old,occupied^+)
        +E sum_occupied [Phi_N(R_old)-Phi_N(R_fresh)] >=0. (5)

Here the fresh occupancy law matches the ACTUAL one; this is why its entropy cancels and the first term is a KL. Characters have N=1 and zero shape cost; constant blocks are unoccupied. Global occupied/vacuum KL and the conditional two-vacuum-row KL are additional nonnegative terms. Thus every later full1/7 activation refresh costs<=0, regardless of width/load or divergent finite data history. Repetition renews only this structural reference form; it renews NO budget. This accepts the conditional later-reset clause of A073 unchanged; as original-supplier contributor A050 does not call this an independent review of the entire upstream chain.

## 5. Expose x AFTER the paid repeated resets

At ANY selected active activation frontier leaves, query x once and retain BOTH children. No alignment between the selection rule and the sign or core mean is required. The x0 child is the constant s; the x1 child is the actual current core g. Both have nonnegative S4. Every unselected activation leaf also has nonnegative S4 by sections1-3. Continuing data-only histories in the exposed pure cores preserves their point-tensor certificates, and continuing permitted histories in unexposed activation branches preserves theirs. Thus this controller exposure may be interposed anywhere after the first reset, with arbitrary later1/7 activation refreshes before it and arbitrary selections in the two sign trees. The retained b0 still contributes exactly one to the global weighted surplus, so S=E S4>=1.

There is also a PAID fresh pure-core reference after this x exposure. On nonempty data rows, erasing x and taking x1 has coherent kernel p_g(T)/(2*(p_g(T)/2))=1. Thus the inherited x1 reference conditional on nonempty data is exactly the same Q_old^+ as before x. Its vacuum mass rho may change; it is not assumed correct. Reset the FULL core child to the prescribed fresh product1/7 reference. With v=Var(g), the complete old-minus-fresh cross-entropy is

    D(Ber(v)||Ber(rho))
      +v[CE(P_core^+,Q_old^+)-CE(P_core^+,Q_fresh^+)] >=0, (6)

using(5). Standard zero-source-weight conventions handle v=0,1. This is the entire actual signed conversion, including the vacuum mismatch, not only a conditional-profile bill. The constant x0 sibling retains its full inherited reference and terminal bill. In this supplied family supports match and the coherent channel yields its exact constant law. After the pure-core refresh, any finite adaptive fresh-data tree and further same1/7 pure-core refreshes have nonpositive prices by the blockwise version of the same KL/shape decomposition. No extra first-reset charge is erased.

If the immediate pure-core refresh is deferred, the same conditional-profile induction still applies: for a nonempty remaining data frequency T, both parent rows T and T+j are nonempty, so pure-core data transport updates their product profile up to one common scalar. The arbitrary global vacuum row does not feed these rows. Equation(6) therefore pays a later fresh core reset as well. The finite checker uses the immediate-refresh policy; this deferred-refresh option follows from the displayed nonempty-row induction, not an additional finite extrapolation.

## 6. Complete original-bank payment and scope

Let sigma_later sum ALL actual weighted activation and pure-core reset increments after the first, including those after x. By(5)-(6), sigma_later<=0. Let e=H0-EHleaf-4(I0-EIleaf), S=E(4Ileaf-Hleaf), and sigma_total=sigma1+sigma_later. Actual coherent transport at every physical query, with reference's own branch normalizers and fair fallback on erased source-zero rows, gives

    A0+sigma_total = all reached erasure/outcome KL
                    + COMPLETE final terminal reference KL.

Exact entropy/influence algebra therefore gives

    S-[A0+e+sigma_total]_+ = min(S,M0-sigma_total)>=1.

Subtract the SAME one eligible old booking0<=omega<=1/4 to retain>=3/4 at SAME rate4. Both original sign trees, every x0 sibling, b0, the first sigma1, all signed query credits and terminal entropy/KL remain. This does not establish payment under separately clipped bills or under an arbitrary newly chosen reference.

The earlier second1/11 budget and width/load restrictions are not falsified: A073 supplied a stronger conditional-profile sign theorem, and the present individual-surplus certificate adds a previously unproved selected x/query/reset continuation. The result is all-width/all-load for the specified initial point-tensor supplier. Universally, the first unpaid line is still a complete correlated source with influence-linear price for arbitrary Boolean cores. Beyond this family, the exact entropy test(2) is available, but a positive non-point reset still needs payment from the actual unused original bank. That is the next interface, not another free renewal or an assertion of full FEI.
