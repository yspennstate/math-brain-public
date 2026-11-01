# A070 stage9: independent order-theorem review and the real-spectrum boundary

All logarithms are base two. Boolean means values exactly in {-1,1}; restrictions are physical uniform-cube restrictions. This note independently reviews A069-SHARP-INHERITED-CORE-ORDER-COMPARISON@1 unchanged, and adds a real-normalization diagnostic. Neither result proves FEI.

## 1. Independent reconstruction of the supplied-source theorem

For a finite Boolean pair a,b, let P=(ahat^2+bhat^2)/2 and J=(I(a)+I(b))/2. Supply one normalized nonnegative reference R dominating P; zero reference cells are allowed only when the actual mass is zero. Define B=CE(P,R). At every physical restriction inherit R by frequency marginalization, without reset. At a query i write D=B_parent-(B_child+ + B_child-)/2 and j=(Inf_i(a)+Inf_i(b))/2. Query every remaining coordinate on every branch, even after the outputs become constant. Choices may depend on the physical history and an independent original random seed. Every expectation retains both children with physical probabilities.

Write the two parent Fourier coefficients above an erased set T as alpha_T,beta_T. The child coefficients are alpha_T+beta_T and alpha_T-beta_T, so their mean squared mass is alpha_T^2+beta_T^2. Thus D equals the sum, for each member of the pair and each T, of its parent squared masses times log((R_T+R_Ti)/R_T) or log((R_T+R_Ti)/R_Ti), with the pair factor 1/2. Each summand is nonnegative. If an inherited child has positive squared mass at T then at least one parent coefficient was nonzero; domination implies R_T+R_Ti>0. Support domination is therefore hereditary, including when R has zero cells. No entropy or CE is silently discarded at a constant-output interior node.

At complete exposure the inherited reference has the single atom 1, hence terminal CE is exactly zero. Telescoping with actual physical reach weights w gives sum wD=B. Boolean Fourier energy is pivotal influence, so the restriction identity I_parent=j+mean I_child gives sum wj=J. These equalities remain true for adaptive coordinate choices; condition on the independent seed to include random choices.

Define V_T=sum w(D-4j)_+ and A_T=sum w min(D,4j). Pointwise D=(D-4j)_++min(D,4j), with 0<=min(D,4j)<=4j. Therefore V_T=B-A_T, 0<=A_T<=4J, max(0,B-4J)<=V_T<=B, and |V_T-V_U|<=4J for any two complete trees with the SAME supplied R. This proof reconstructs the abstract theorem directly, without the source's code or wrapper lemma. It supplies no budget for B.

## 2. Sharpness, zero-support issue, and source-payment equivalence

Take a=b=x on two bits x,z, epsilon=2^-k and R=(epsilon,1,15-2epsilon,epsilon)/16 in mask order empty,x,z,xz. For x first, D_root=log(1+epsilon), j_root=1 and its excess is zero; the remaining irrelevant z query pays CE 4-log(1+epsilon), so V_xz=4-log(1+epsilon). For z first, the root has zero influence and D=log(1+epsilon); the subsequent x query has D=4-log(1+epsilon)<4 and zero positive excess. Hence V_zx=log(1+epsilon). The difference tends to 4J=4. For k>=2 the SAME 5/8 allowance pays the latter order and fails the former. This is a reference-invoice example on actual Boolean functions, not an entropy-influence counterexample.

For constant pairs J=0 but a strictly positive nondegenerate reference gives B=-log R(empty)>0; mandatory complete exposure then gives V=B. Thus universal V<=KJ cannot require strictly positive reference mass everywhere. Nonnegative references dominating P are the correct scope. For a diagonal pair f and any supplied dominating reference, Gibbs yields H(f)<=B=V+A<=V+4I(f). A universal selected-tree payment V<=KI therefore implies FEI with C=K+4.

Conversely, assuming Boolean FEI(C), choose R=P for any pair. Then B=H(P)=[H(Pa)+H(Pb)]/2+JS(Pa,Pb). The elementary binary-source decomposition into common mass and disjoint remainders gives JS<=TV(Pa,Pb). Since both laws have their distinguished empty atom, TV<=max(Pa(nonempty),Pb(nonempty))<=Ia+Ib=2J. Thus B<=(C+2)J and V_T<=B for EVERY tree. The diagonal improves to V_T<=CI. Constant pairs use their actual point-mass reference. These implications preserve the source's exact stated scope and establish source-payment equivalence, not FEI itself.

The finite Bellman min/max recurrence is immediate from the actual current state (restricted pair, inherited R, remaining coordinates): at nonterminal states take min/max over fresh queried coordinates of the local positive excess plus the mean of the two child values. Terminal value is zero only at complete exposure. The recurrence does not prove an influence-priced supersolution. Wrapper applications retain their original product-reference hypotheses and must actually pay any extra 4J from the SAME original unused capacity. The independently reviewed older private lemma is not repaired or broadened here.

## 3. What is and is not Boolean in this proof

For arbitrary real g, use its UNNORMALIZED squared Fourier masses under each physical restriction and spectral energy J(g)=sum_S |S| ghat(S)^2. The coefficient erasure identity, nonnegative CE decrement, hereditary support, zero terminal CE, both telescopes, Bellman decomposition and order bound of Section1 all remain valid, with J replacing ordinary pivotal influence. Squared masses are homogeneous; no division by the child norm is permitted in these identities. A real function's indicator that changing a bit changes its value is generally not its derivative's squared energy.

Booleanity guarantees that EVERY physical restriction has squared norm one and that E[((f(x)-f(x^i))/2)^2]=Pr[f(x)!=f(x^i)]. It is indispensable for simultaneously interpreting all restricted squared spectra as normalized laws and the spectral energy as ordinary pivotal influence. Having root norm one guarantees neither fact. In fact, norm one at every full singleton restriction is exactly g(x)^2=1 at every point, hence exactly Booleanity for real g. All the homogeneous order algebra can therefore be true without containing the Boolean input that a universal payment theorem needs.

An equivalent exact Boolean constraint is the Fourier convolution identity sum_S fhat(S) fhat(S symmetric_difference T)=1 when T is empty and 0 otherwise. A source-payment proof must exploit some consequence that excludes the real adversaries below; merely reusing coefficient erasure and complete-tree telescoping cannot do so.

## 4. Exact two-bit failure of child renormalization

Let g(x,y)=(2+x+2y)/3. Its Fourier coefficients are (2/3,1/3,2/3,0) and its squared root spectrum is (4/9,1/9,4/9,0), of total mass one. Query x. The two actual child squared spectra are (1,4/9) and (1/9,4/9), of total masses 13/9 and 5/9. Their homogeneous average is the erased root spectrum (5/9,4/9), as required.

Artificially normalizing each child instead gives (9/13,4/13) and (1/5,4/5), whose mean is (29/65,36/65), different from (5/9,4/9). Set q=1/4096 and supply the strictly positive normalized root reference R=(4(1-q)/5,(1-q)/5,q/2,q/2). Its inherited reference is (1-q,q). With h=h2(1/5), the correct homogeneous decrement is D_hom=(5/9)h+4/9>0. The artificial normalized-child decrement is

D_norm=D_hom+(64/585) log(q/(1-q))=D_hom-(64/585)log(4095)<0.

The checker verifies every rational spectrum, both exact prime-log identities, and strict interval signs. This refutes a normalized-real extension obtained by renormalizing physical children. It does NOT refute A069's Boolean theorem or its homogeneous real algebra. The false line is replacing the mean homogeneous child mass by the mean separately normalized child law.

## 5. An unbounded real-source obstruction, for every complete order

For n>=2 let g_n=(x_1+...+x_n)/sqrt(n). Its root squared spectrum is uniform on n singletons, its entropy is log n and spectral energy J=1. It is real, not Boolean. For every normalized reference R dominating that root spectrum, B>=log n by Gibbs. Section1's HOMOGENEOUS telescope gives V_T=B-A_T>=log n-4 for EVERY complete physical query tree, however selected or randomized. Thus no finite universal bound V_T<=KJ can follow from root normalization plus homogeneous erasure/telescoping alone. The ordinary change-indicator pivotal sum of g_n is n; it must not be confused with J=1. This family supplies no Boolean disproof.

For a concrete exact finite certificate take R equal to the root singleton spectrum. At depth d and physical prefix sum s, the unnormalized child spectrum has empty mass s^2/n and one mass 1/n on each remaining singleton; its norm is (s^2+n-d)/n. The inherited reference has empty mass d/n and each remaining singleton 1/n. Direct CE subtraction gives D(0,0)=0 and, for d>0,

D(d,s)=(s^2/n)log((d+1)/d)+(1/n)log(d+1), j=1/n.

The depth/prefix-sum state has weight binomial(d,(d+s)/2)/2^d. Adaptive choices of a fresh coordinate leave independent fair physical signs and the same remaining coefficients; thus the aggregation is valid for any order. Exact prime-log sums verify sum wD=log n, sum wj=1, and log n-4<=sum w(D-4/n)_+<=log n for the frozen explicit dimensions 2,4,8,16,32,64. The proof for all n is the telescope, not extrapolation from these six cases.

## 6. Review verdict and honest universal gap

A069-SHARP-INHERITED-CORE-ORDER-COMPARISON@1 HOLDS at its FULL supplied-source scope, including sharp constant, nonnegative reference remedy, complete adaptive/random trees, Bellman recursion and the FEI-equivalence qualification. No substantive repair has been supplied to that claim. The independent exact checker uses our own integer Walsh/physical restriction implementation and a different combined pair/reference representation, with all 256 ordered two-bit Boolean pairs, three reference choices and both complete orders.

First unsupported universal line: construct a Boolean-specific original influence-priced source and prove a once-owned bound for its actual positive projected-core invoice, including required conversions and all previously booked charges. Neither order comparison, real-normalization failure nor arbitrary source selection pays that line. The new real controls eliminate a false extension and identify necessary leverage; they do not close the universal payment problem. Original cyclic-law counterexamples remain binding; this stage introduces no spectral-to-physical transport, conditional-law reset, cyclic transfer or fresh budget and does not claim a new replay of their source-incomplete addenda.
