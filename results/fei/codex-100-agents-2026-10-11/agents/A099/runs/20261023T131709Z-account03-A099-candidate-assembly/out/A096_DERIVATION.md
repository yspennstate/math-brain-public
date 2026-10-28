# A096 stage20: backward compression of a zero-erasure handoff

All costs are in bits, all physical cubes are uniform, and all functions below are actual Boolean functions. This is a conditional reference-accounting theorem, not a proof of FEI.

## 1. Independent reconstruction of the new depth obstruction

A085 run20261023T112613Z, PROOF sections2--5, uses h(x)=g(y), y_j=product of L disjoint physical bits. Its expansion is exactly sum_J ghat(J) product_{j in J} y_j. Squaring preserves the entire core law and every supplied lifted reference, including reference-only atoms. Consequently H(h)=H(g), I(h)=L I(g), and CE(P_h,R_lift)=CE(P_g,R). Before any of the first D queries on a path, L=D+1 leaves at least two unqueried bits in every block. A frequency and its queried-coordinate toggle cannot both be unions of these remaining blocks. Both children therefore have the same squared law, obtained by injective frequency deletion; neither the true spectral erasure nor the supplied lifted-reference occupancy KL changes. At a leaf there is still at least one bit in every block, so even adaptive branches retain the complete core law. With matched R=P, all calibration refunds are also zero. For unmatched R, finer calibrations can release existing mismatch; the source correctly excludes that credit from its zero-credit assertion. This reconstruction accepts that exact scoped theorem, not a universal cheap source or a necessary conversion.

## 2. Exact theorem: arbitrary terminal targets on an isospectral physical tree

Let f be Boolean, P its squared Fourier law, and Omega={S:P(S)>0}. Let T be ANY finite complete adaptive physical query tree such that at every internal node, for the queried coordinate j, fhat_node(V)*fhat_node(V+j)=0 for EVERY V excluding j. No coordinate is queried twice on one path. Leaves have physical reaches w_l=2^(-depth_l), summing to one; stopping early is allowed. The two child Fourier coefficients are u_V +/- v_V. The displayed hypothesis makes their squares both u_V^2+v_V^2, so (i) each queried spectral erasure is exactly zero; (ii) deletion is a bijection from occupied parent labels to occupied child labels, preserving their probabilities. Composition gives a bijection pi_l:Omega -> supp(P_l) with P_l(pi_l(S))=P(S).

Supply ANY normalized finite-CE root reference Q0 and ANY normalized finite-CE complete terminal reference Q_l for every leaf. Terminal references may be outcome-dependent, may alter the vacuum, and may put mass outside actual spectral support. Define

 q_l(S)=Q_l(pi_l(S)), G(S)=product_l q_l(S)^(w_l),
 Z=sum_{S in Omega} G(S), Rstar(S)=G(S)/Z.

Finite CE makes each q_l(S)>0, hence Z>0. Weighted AM--GM gives G(S)<=sum_l w_l q_l(S). Summing and retaining reference-only mass gives Z<=sum_l w_l sum_S q_l(S)<=1. Thus Rstar is a genuine normalized root reference, extended by zero outside Omega. No ghost mass is silently renormalized without charge: its loss is in Z.

Since log G(S)=sum_l w_l log q_l(S), the COMPLETE terminal cost has the exact identity

 sum_l w_l CE(P_l,Q_l) = CE(P,Rstar)-log2 Z.

Equivalently the signed replacement debit, including all zero erasures, is

 Delta = D(P||Rstar)-D(P||Q0)-log2 Z.                 (1)

Let Rstar_l be Rstar transported by pi_l and zero on all other leaf frequencies. A second exact identity is

 -log2 Z = sum_l w_l D(Rstar_l||Q_l) >= 0.          (2)

Indeed log(Rstar(S)/q_l(S)) averaged over l equals -log Z, pointwise in S. This proves (2), keeping all complete normalizations. Equality holds exactly when every positive-reach full Q_l equals Rstar_l. There is no assertion that Rstar is efficiently supplied or influence-priced: its definition uses the actual occupied support and all prescribed targets.

For a previously paid prefix, let rho>0 be the GLOBAL physical reach of this subtree root. Let W contain every prior debit and all complementary complete terminals, excluding ONLY rho*CE(P,Q0), let A be the ORIGINAL global allowance, and let U=A-W-rho*CE(P,Q0) be its actual unused amount. The handoff is affordable at that SAME account if and only if rho*Delta<=U. At unit reach this is Delta<=U. For disjoint frontier roots the exact joint test is sum_v rho_v*Delta_v<=U, with every complementary terminal still in W. Equations (1)--(2) give the test. Neither source mismatch D(P||Q0), old releases, nor U may be issued a second time. Arbitrary intervening reference changes telescope into this same complete signed bill; ordinary inherited references are one permissible implementation.

If Q0=P, Delta=D(P||Rstar)+sum_l w_l D(Rstar_l||Q_l)>=0, and it is zero iff EVERY full terminal reference is already its actual P_l. Thus a zero-credit matched history supplies no free different target. Conversely a history alone does not force a conversion: carrying P forward is admissible. A universal proposal must specify why its target is needed and exhibit either this SAME original unused payer or a cheap initial source. The theorem moves the entire obligation back to its true ancestor and separates the target-disagreement liability; it does not discharge it.

## 3. Actual Boolean witness: effective ancestor KL is zero, yet the bill is positive

Take f=-1 at truth indices0 and7 on three bits and +1 elsewhere. Direct Walsh expansion is

 f=(1-x1*x2-x1*x3-x2*x3)/2.

Thus P is uniform on Omega={empty,12,13,23}; H=2 and I=3/2. Query x1. No occupied adjacent pair exists, both children have uniform four-atom spectra, and with Q0=P all current erasure/occupancy/calibration refunds are zero. At the plus leaf prescribe probabilities (3,3,1,1)/8 on the transported root labels; at the minus leaf prescribe (1,1,3,3)/8. These are complete normalized references with finite CE and both full terminals are kept.

For EVERY root atom G(S)=sqrt(3)/8, so Z=sqrt(3)/2 and Rstar=P. Nevertheless

 Delta=-log2 Z=(1/2)log2(4/3)>0.

The exact sign is the integer inequality4>3. Root effective-reference KL alone is zero and misses the entire bill. This refutes only normalization-free geometric compression / free adaptive target selection, not FEI. The targets are prescribed to test accounting; no assertion that an FEI construction intrinsically requires this pair is made.

## 4. Relation to current source-bound progress

A097's two nonempty phase bins, A003's reference-singleton discrepancy and A004's occupancy credit fund changes outside this matched nullspace. They are not contradicted. A085 already proves the arbitrary-depth/core isometry; the new delta here is arbitrary complete outcome-dependent target compression, its exact nonnegative normalizer/disagreement term, and a Boolean zero-effective-KL counterexample to omitting that term. A090's no-reset deferral remains valid. A094's enlarged original allowance is a possible payer only after its compatible model/policy is actually identified; its numerical reserve is not imported into this unrelated tree.

The first unsupported universal line remains: supply an influence-priced initial reference for arbitrary cores, or name a necessary compatible target conversion and prove (1)<=the ACTUAL unused original U after all prior debits. A geometrically averaged reference does not bypass that line because its construction has no price bound and (2) need not vanish.

## Universal bridge

This stage advances C024 history transfer and C020 whole-reference accounting inside C019: every finite isospectral query history with arbitrary full terminal targets is exactly an ancestor reference conversion PLUS the explicitly priced geometric-normalizer/disagreement bill, with all old debits and both signed terminals retained. It supplies zero improvement to a universal FEI constant. The next shortest route is to demand a specified useful target and its actual original payer, or directly price the arbitrary-core source; searching deeper for local phase energy cannot evade A085's all-depth obstruction, and dropping the new normalizer is refuted by the four-atom Boolean witness.
