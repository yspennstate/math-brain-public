# One affine intrusion in a bent disagreement plane

The selected-coordinate four-edge inequality holds for all six-control Boolean parents whose child disagreement is an affine two-plane with bent sign, when exactly one other parallel slice is affine and the other six are bent. This is a finite exact proof certificate, pending independent reconstruction; it does not establish full FEI.

Let F(s,t,z) have children a(t,z),a(t,z)(1-2*1_{z=0}), with t in F2^2 and z in F2^3. Normalize a(t,0)=(-1)^(t1*t2). A common character and global sign achieve this for every two-bit bent sign. Translating and invertibly linearly changing ONLY unqueried input coordinates sends an arbitrary disagreement plane to z=0. Such maps permute the selected spectral row pairs (a common character shifts their indices); hence they preserve selected erasure B_s and Inf_s. They do not preserve other physical influences and are used only for this selected-coordinate statement.

Write sigma_t=Walsh_t[a(.,0)]/2, in {+1,-1}, and H_t(z)=sigma_t Walsh_t[a(.,z)]/2. Then H_t(0)=1. A two-bit Boolean slice has either an affine spectrum (one signed 4, three zeros), or a bent spectrum (four signed 2). Thus at the one affine intrusion three H_t have value 0 and one has value +2 or -2; at every other z all four H_t have values +1 or -1. No independence between these four rows is asserted or needed for the bound.

An invertible linear z transformation fixes z=0 and sends the unique nonzero intrusion to z=1. It merely permutes Fourier indices within each row, leaving every row cost invariant. This justifies the 64 patterns per row in row_pilot.py. Put A_t(k)=Walsh_z[H_t](k)-1. The parent Fourier amplitudes, up to a row sign, are A_t(k)/16 on the absent selector and 1/16 on the present selector. Therefore Inf_s=32/256=1/8 and

256 B_s = sum_{t,k} Phi(A_t(k)^2,1),
Phi(v,1)=(v+1)log2(v+1)-v log2(v).

The exact integer census covers H(0)=1,H(1)=c,H(2..7) in {+1,-1}, for each c=0,+2,-2, with 64 cases each. Its maximum integer entropy ratios have square histograms:

c=0: {0:2,4:4,16:2}; c=+2 or -2: {4:4,16:4}.

The comparison uses P=product (A^2+1)^(A^2+1), Q=product (A^2)^(A^2), omitting zero exponents. All competitors are compared by exact cross multiplication; no logarithm is approximated. Thus three zero rows and one signed-two row cost at most

3[2 Phi(16,1)+4 Phi(4,1)] + [4 Phi(16,1)+4 Phi(4,1)]
 =10 Phi(16,1)+16 Phi(4,1)
 =170 log2(17)+80 log2(5)-768 <128.

The last strict inequality is the exact positive integer comparison 17^170*5^80<2^896. Hence B_s<1/2=4 Inf_s. Degenerate zero amplitudes contribute zero and no division by them is used. The selected influence is always positive by its four pivotal edges. This proves the scoped statement from the exhaustive row certificate, even though scalar maxima need not coexist in a Boolean parent.

The earlier all-bent class and affine-sign-on-plane class remain available at their prior scope. More affine intrusions and affine-span-three disagreement are not covered by this one-intrusion theorem. No whole-tree twelve-edit conclusion follows without treating every possible node and its full terminal cost. The data coordinate is not relabeled or charged here.


## Actual Boolean obstruction to the generic four-edge K4 inequality

The seven-intrusion scalar envelope can be attained by compatible columns. Use q(t)=t1*t2 and sigma=(1,1,1,-1). At z=1,2,3 place the affine spike in rows 1,2,3 with sign +2. At z=4,5,6,7 put it in row 0 with signs +2,+2,+2,-2. At z=0 retain q(t). In each nonzero slice define a(t,z)=sigma_row*sign*(-1)^(row dot t). Define F as above, negating exactly the changed plane in selector child 1. This is an explicit Boolean function with 64 truth values saved in out/boolean_counterexample.json.

An independent direct character-sum implementation, without the projected Walsh helper, gives 32 selected pairs with present square 1 and absent squares 4 (24 times),16 (8 times), all over denominator 256. Thus

B_s=[136 log2(17)+120 log2(5)-704]/256 > 1/2 = 4 Inf_s,

because 17^136*5^120>2^832. The positive integer slack is saved. The six physical influences are (1/8,5/16,5/16,1/2,1/2,1/2). Query coordinate 3 instead: its exact entropy-product comparison gives B_3<=4 Inf_3. The resulting children have five controls, so the previous generic five-control policy supplies a zero-bad-bill adaptive tree; the complete terminal cost and one physical data owner can still be retained. This is a refutation of a specified-coordinate intermediate lemma, not a counterexample to full FEI or to existential good-coordinate selection.

The complete 78125 scalar-row envelope pays intrusion counts 0,1,2,3,5,6, and fails at counts 4 and 7. Failure at 4 is only a relaxation obstruction; the selected seven-intrusion construction above is Boolean-certified. These statements repair the old proposed generic-four-edge route without altering the eleven-edit theorem.


## Twelve-edit critical planar nodes: the old generic local conjecture is unnecessary

Let g=(-1)^q(1-2*1_Ed) be a Boolean phase on six physical controls, with q quadratic, |Ed|<=12, and selected coordinate i a nonzero polar row of q. The unedited q has 16 pivotal i-pairs and 16 nonpivotal pairs. Let R be initially pivotal pairs made nonpivotal, A initially nonpivotal pairs made pivotal, and D pairs with both endpoints edited. If the edited phase has exactly four pivotal pairs, then R-A=12 while |Ed|=R+A+2D<=12. Hence R=12,A=D=0,|Ed|=12. Every edit removes one initially pivotal pair; no other pair is touched. This uses the nonzero-polar hypothesis precisely to obtain 16 initial pivotal pairs; the counterexample's nearest twelve-edit representation has a zero selected polar row and does not contradict it.

The four surviving pivotal child vertices form a set W in the affine hyperplane P where the unedited quadratic selected derivative equals one. Suppose W is an affine two-plane. Every selected child is untouched on W, and the child sign there is quadratic, hence affine or bent. The affine-on-W case is the complete inherited quinary certificate from stage6. In the bent case, straighten ONLY the unqueried variables so that the parallel W-planes are indexed by z in F2^3. Since W lies in P, P consists of four such planes. On the four planes outside P, neither endpoint of any selected pair is edited, so the child slice is the original quadratic with the same nondegenerate two-dimensional polar form. Each is bent. Of the other four planes, one is W and is bent, so at most THREE parallel slices can be affine. The exact row-envelope certificate for intrusion counts 0,1,2,3 gives B_i<=4 Inf_i. Only selected B_i and Inf_i pass through this affine normalization; no other physical influence is transported.

Therefore every critical twelve-edit planar-disagreement polar node is paid at K4. At D>=7, the polar influence lower bound is 1/2-24/2^D>=5/16, hence good. At D6, influences above four pivotal pairs are covered by the prior five-edge odd-lattice certificate or the >=3/16 binary-entropy bound. At D<=5 use the prior generic maximum-influence physical policy. The remaining unpaid critical node has four pivotal child vertices of affine span THREE. This is the precise twelve-edit stopping gap; no generic twelve-edit theorem is asserted.

Affine terminals at <=12 edits are also paid at the unchanged K=4+2/ln2. For s>0,D>=6, the inherited sparse-mask proof gives H/I_phase<=4+2[log2(s)+log2(e)-log2(3)]/(D-log2(s)). Character multiplication cannot lower influence because each mask-coordinate influence is <=2s/2^D<1/2. The displayed ratio is <=K if ln(s)+1-ln(3)<=D-log2(s). The worst endpoint is s=12,D=6, reducing the needed strict inequality to 2 ln(2)+log2(3)<3. The prior exact exponential-series certificate gives ln(2)<7/10, while 3^5<2^8 gives log2(3)<8/5; together these prove it. s=0 is a character with zero entropy. Denominators are positive since s<=12<64<=2^D. Small terminals retain the actual five-control certificate and all shared data influence remains one.

If a finite physical restriction policy on <=12 coherent same-fiber edits encounters only planar four-edge critical nodes, the previous complete entropy/influence telescope therefore still proves H(F)<=K(I(F)-1), with zero bad-node bill and full terminal payment. This is conditional on the named geometric property at every critical node, not a proof of full FEI. The first unsupported line for the unconditional twelve-edit extension is payment or adaptive repair of affine-span-three surviving pivotal sets, from the same physical owner.


## Position-coupled refund closes the four-intrusion relaxation failure

The count-only envelope pays k=0,1,2,3,5,6, but it discards the locations of the signed-two entries. To retain this Boolean constraint, let S be the subset of seven nonzero z carrying affine slices, and let A_t be the subset at which the affine spike is in row t. These four subsets form a disjoint ordered partition of S. For each pair (S,A), maximize the scalar row cost over H(0)=1, H(z) in {+2,-2} on A, H(z)=0 on S\A, and H(z) in {+1,-1} off S. The full 5^7=78125 scalar enumeration computes all 3^7=2187 such maxima without symmetry reduction. For each S enumerate its 4^|S| ordered spike partitions and sum the four row maxima. Across all S this is another 5^7=78125 exact product comparisons. This is an upper bound for actual Boolean parents: it preserves the location and ownership of each affine spike and merely drops the sign-product compatibility of the bent columns. No independence claim is used.

Every one of the 127 sets with |S|<=6 passes. At S=all seven points, 168 of 16384 ordered partitions have an unpaid relaxed bound, one of which is realized by the explicit Boolean witness. Thus for an arbitrary affine two-plane disagreement with bent phase, B_i<=4 Inf_i whenever at least one OTHER parallel slice is bent (zero through six affine intrusions). The fully affine complement admits an actual violation. The earlier affine-on-plane phase case is separate and remains certified by the inherited quinary enumeration.

Both the Gray/Walsh nearest-quadratic scan and an independent 2097152-case XOR/bit_count calculation show that the actual witness is at Hamming distance 12 from degree<=2 phases, and distance 14 if the selected polar row must be nonzero. The first nearest quadratic has edges (2,5),(3,4) and linear mask 4. The selected-polar nearest quadratic has edges (0,5),(2,5),(3,4) and linear mask 5. Both constants are zero; complete edit vertex lists are saved in out/quadratic_distance.json. Exhausting all 15 quadratic coefficients, all 64 linear masks and both constant signs makes these finite minima certificates, not numerical optimization. The selected-polar distance-14 representation furnishes a genuine coherent-edit bad-polar-pivot obstruction; its alternative physical query remains good.

The proof uses integer arithmetic certificates and analytic reductions. Core Lean was attempted on only the two integer signs with the submitted source hash and named theorem; the wrapper returned RUNTIME_UNVERIFIED. No kernel verification, transitive-axiom audit or independent mathematical acceptance is claimed for this run.
