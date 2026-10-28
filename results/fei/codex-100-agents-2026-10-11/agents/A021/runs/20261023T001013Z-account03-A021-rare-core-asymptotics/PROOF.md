# A nonflat data query retains the original complete reference and old reserve

Full FEI is OPEN. All probabilities are physical uniform-cube probabilities; entropy and cross-entropy are in bits. Let g on three bits be -1 at000 and+1 elsewhere. For integer t>=2 set k=3t, delta=2^-k, b=g tensor t, and F(x,z)=b(x)(1-2*1_(x=v)*A(z)). The control indicator A is arbitrary Boolean on an independent finite uniform cube; alpha=EA, a=1-2A. Fix ANY original data coordinate i. No controller bit is queried here.

The ORIGINAL positive data reference is Q=P_b, the product of q=(9/16,1/16,...,1/16). Let R be the ORIGINAL controller spectral marginal of F: R(empty)=1-V, R(T)=delta*ahat(T)^2 for nonempty T, V=4delta alpha(1-alpha). Root joint reference is Q(S)R(T). A zero R row has zero Fourier mass in BOTH query children and is omitted, not filled or reset. Put L=delta H(a), C0=CE_(Q R)(P_F), and let old booked U satisfy0<=U<=t/64.

## 1. Review consumed and mechanism changed

A025 run20261022T231646Z proves, for any finite shared-data physical controller, the exact signed history identity S_T+E_T=S_0+2Pi_D+10Pi_C-L_0+L_T, and certifies its source admission on the old quadratic bent family. It follows directly by expanding entropy/influence definitions and IT_0-IT_T=Pi_D; L_T>=0 is the sum of remaining one-bit entropy decrements. The identity and its71/78 admission are reconstructed at that scope. It closes A021's prior all-prefix NEXT. It does not pay external reference conversions. This stage therefore consumes A022 run20261021T213608Z's nonflat source and its original-Q/t64 NEXT.

## 2. A sharper charge from the SAME original seed

A022's exact signed spectrum gives

 C0 = H(b)+L+kV+phi(1-V)-delta phi((1-2alpha)^2)+4delta alpha J_b(v),
 I_data(F)=3t/4+2delta alpha s_b(v),
 H(b)=t[4-(9/8)log2(3)].

The joint KL D0=D(P_F||Q R) remains explicit: H(F)=C0-D0. Both J and the signed neighbor count s are tensor-additive. On one block, writing l=log2(3), the local pairs (J,s) are (-7l/4,-3) at000; (5l/4,1) at Hamming weight1; and (5l/4,3) at weights2,3. Consequently the SAME vertex obeys

 4J_g-8s_g <=24-7l <118/9.

This uses l>14/9 and l<8/5, both proved by3^9>2^14 and3^5<2^8. The nonzero-vertex alternatives are smaller. Thus keeping the signed terms together, rather than maximizing J and -s separately,

 C0-L-4I_data(F)
 < -3t/4+delta alpha[(226/9)t+6]
 <= -(179/576)t < -t/4.                         (1)

Here V<=4delta alpha, phi(1-V)<=cV, c=log2(e)<3/2, t>=2 and delta<=1/64. All negative phi terms were dropped only in this upper estimate. This is an improved estimate of the ORIGINAL source charge, not new credit from a child. Its original bank is still4I(b)-H(b)-U; the surgery costs and old U are paid from that same quantity. In particular B0=4I_data(F)+L-C0-U>=t/4-U. A022's t/64 reserve remains booked and is not reissued.

## 3. A prescribed positive child reference

Permute blocks/coordinates so i is the first bit of one block. Let Qrest be the ORIGINAL product reference on all other blocks. The inherited projection Qminus has local probabilities(5/8,1/8,1/8,1/8). Define the following concrete conversion at the actual physical query:

 outcome0: Q0=(1/4,1/4,1/4,1/4) tensor Qrest;
 outcome1: Q1=(13/16,1/16,1/16,1/16) tensor Qrest.

Pass the SAME R to BOTH children, including its original empty atom and every nonempty row. Do not replace it by either child's controller marginal. Both data references are normalized and strictly positive. Let C1=(CE_(Q0 R)(P_F|i=0)+CE_(Q1 R)(P_F|i=1))/2. Every full child joint KL D_b=D(P_F|i=b || Q_b R) is retained, so Hchild_b=Cchild_b-D_b.

The physical query influence is d=1/4+2delta alpha sigma, where sigma=b(v)b(v xor e_i) is-1 exactly when the local vertex is000 or e_i. Because only the logarithmic cost of the queried block changes, the original controller-reference cost and every Qrest cost cancel IN EXPECTATION, without an independence assertion about the edited spectrum. Direct Fourier marginal calculation gives

 drop := C0-C1 = 1+G+delta alpha w,
 G=(1/2)log2(13)-(9/8)log2(3),

 w=-7log2(3)                    if v_local=000;
 w= 5log2(3)                    if v_i=0 and v_local!=000;
 w= 5log2(3)-3log2(13)          if v_i=1.           (2)

To verify every factor, the edited root local empty mass is9/16+7delta/2 at000, or9/16-5delta/2 otherwise. The edited physical outcome has density eta=2delta. Outcome0's local code length is always2. In outcome1 an edited constant seed has local masses(1-3eta,eta,eta,eta), so its extra code length is3eta log2(13), with physical reach1/2. This supplies the3delta log2(13) in(2). All unused block costs are left intact.

Define the REFERENCE-CAPACITY loss, not the entropy decrement,

 ell_i=4d-drop=-G+delta alpha(8sigma-w).

The largest coefficient is K=8-5log2(3)+3log2(13). Exact rational logarithm bounds below certify

 ell_i <1/8 for ALL t>=2;
 ell_i <0 for ALL t>=3.                            (3)

For example use19/12<log2(3)<127/80 and37/10<log2(13)<89/24. The associated integer-power inequalities are checked exactly. They give G>41/640, K<269/24; then ell_i<269/1536-41/640<1/8 for t>=2, and ell_i<269/12288-41/640<0 for t>=3. Each other local case has a smaller coefficient, and alpha in[0,1] cannot worsen the positive endpoint.

## 4. Both terminal bills, old debit and source reserve stay present

Ordinary influence telescoping gives I_data,children=I_data(F)-d. With the SAME original L and old U, the converted child bank is EXACTLY

 B1=4I_data,children+L-C1-U = B0-ell_i.

By(1),(3), B1>=t/4-U-1/8>=11t/64, since U<=t/64 and t>=2. Thus the original t/64 reserve remains unused, with at least10t/64 additional unbooked reference capacity. Neither a new source reference on Qrest nor a new R was admitted. At t>=3 this particular data step even increases the complete reference capacity before any new booking. Both physical outcomes and both complete CE/KL terminal expressions are in the formula; no rare branch is discarded.

The ACTUAL entropy decrement D_i is different:

 D_i=drop+(D_0child+D_1child)/2-D0.                  (4)

Consequently B1+(D_0child+D_1child)/2+(4d-D_i)=B0+D0. This is the exact signed history account. It retains the physical query debit, parent reference mismatch and both child KLs. Equation(3) MUST NOT be renamed D_i<=4d. Already the unedited g block has D_i/d=12-(9/2)log2(3)>4. The new result pays one prescribed inherited-reference conversion and certifies both resulting complete reference debts from the SAME source. It is not an all-coordinate entropy induction or a universal FEI proof.

## 5. Why positivity and prescribed conversion matter

Replacing Q1 by the unsmoothed constant-child seed spectrum is invalid. If A is identically1 and v_i=1, an actual edited child has strictly positive local nonempty mass eta=2delta. A point-mass seed reference assigns that mass zero probability, so its cross-entropy is infinite. The positive reference above is part of the theorem, not a harmless notation change.

All calculations include alpha=0,1, arbitrary control dimensions and arbitrary v. R(empty)>0 because V<=delta<1. At nonempty rows R(T)=0 forces ahat(T)=0 and hence both child Fourier rows are zero. No denominator involving a seed coefficient or alpha is canceled. All sums are finite and no limits are interchanged.

First unsupported universal line: under repeated mixed queries, supply positive normalized child references whose ACTUAL conversion loss can be paid from one remaining source account without restoring Qrest, R, U or the reserve. Our bound uses the special three-bit log kernel and a single untouched block. Queries after that block's first exposure, controller-reference changes and arbitrary nonflat cores need a new estimate. The source-scale signed history identity survives, but does not itself price these conversions.
