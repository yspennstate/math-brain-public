# One original account through every private-query product reset

Author proof, independent review pending. Bits throughout. This is a scoped C024/C019 accounting theorem, not FEI.

## Actual branch information and spectral erasure

At a Boolean query i write p for the parent squared Fourier law, q for its erased law, and p_y for the two child laws. Then q=(p_0+p_1)/2. Couple a fair PHYSICAL branch Y with a remaining spectral set T by P(Y=y,T)=p_y(T)/2. Its actual revealed information is J=I(Y;T)=H(q)-(H(p_0)+H(p_1))/2. By contrast spectral erasure is B=H_p(S_i|T). The exact entropy drop is B+J. Neither quantity is the entropy of the physical branch (which is one bit).

For any normalized supporting reference Q, erase it to Qbar, and apply the SAME kernel k_y(T)=p_y(T)/(2q(T)), extended fairly where q=0. Let pi_y=sum Qbar(T)k_y(T), and Q_y=Qbar k_y/pi_y. Put K=KL(p||Q), E=K-KL(q||Qbar)>=0, O=KL(fair||pi)>=0 and K_y=KL(p_y||Q_y). Two finite KL chain rules give

    K = E + O + mean K_y.                                  (1)

O is reference outcome mismatch, not physical information J. No mass with positive source is divided by zero, since Q supports p and every child law is normalized. The fair source-zero extension is also applied to Q.

For a product reference equal to the actual parent marginals, K=TC(p). Define

    Gamma=sum_(j!=i) [h2(d_j)-mean h2(d_{j,y})]>=0.

The spectator influence identities give d_j=mean d_{j,y}. Thus mean TC(p_y)-TC(p)=-Gamma-h2(d_i)+B+J. For this particular product reference the erased reference is the product of spectator marginals. The exact conditional chain gives

    E=h2(d_i)-B=I_p(S_i;T),
    sigma=mean TC(p_y)-mean K_y
         =J+O-Gamma.                                       (2)

Here sigma is the signed cost of an ACTUALLY exercised reset to the child products. Replacing E by B gives the wrong reset bill. Equation (2) follows directly from (1); all entropies of complete child laws remain present.

## Boolean fixture and a uniform frontier bound

Let w>=14 and let u,v be disjoint blocks of w fair bits. Set p_w(u)=1-2*1[u=0], h=p_w(u)p_w(v). On independent control bits x,a,b set F=-1 on x=0,a=1, F=h on x=b=1, and F=+1 otherwise. Query a first. The children are G and -chi_x G, with G=1 except G=h when x=b=1 and chi_x=(-1)^x. Use ANY original normalized reference supporting the spectrum of F, in particular its prescribed nonempty occupancy reference. Its actual initial KL A is retained; its admission is a hypothesis, not an influence-paid claim.

Put delta=2^-w and t=Pr(h=-1)=2delta(1-delta). The untwisted G has control influences t/2 each, and 2w data influences delta/2 each. Hence its sum of marginal entropies is

    M=2h2(t/2)+2w h2(delta/2)
      < U_w=(w^2+(9/2)w+3)/2^w.                           (3)

For 0<p<=1/2, h2(p)<=p(log2(1/p)+log2(e))<p(log2(1/p)+3/2). Also t/2<=delta and h2 is increasing there. This proves (3). The elementary bound log2(e)<3/2 follows from ln2>2/3 by its positive atanh series.

Allow arbitrary adaptive distinct PRIVATE data queries, always retaining x,b. At a stopping frontier untwist the a=1 lineage by chi_x. For each original coordinate j define D_j to be its current influence, or zero if it has already been queried. Restricting a different coordinate preserves influence in physical expectation, and querying j removes it; consequently E D_j<=d_j(G). Jensen's inequality and monotonicity of h2 up to 1/2 imply

    E sum_j h2(D_j) <= sum_j h2(d_j(G))=M.                 (4)

This uses monotonicity only at E D_j<=d_j(G)<=1/2, not at each individual random D_j. It holds on EVERY finite adaptive frontier, separately in each a lineage and hence globally. Character translation preserves entropy, total correlation and marginal entropy. Nonnegative TC<=sum h2(D_j) therefore gives E TC<=M. Subfrontiers have the same upper bound by completion and nonnegativity.

For every restricted h, I_x(G)=I_b(G)=Pr(h=-1)/2 and I_data(G)=I(h)/4. Thus I(-chi_x G)=1+I(h)/4>=1. At every allowed frontier the a=1 conditional mean surplus satisfies

    E[4I-H | a=1] >=4-M>2.                               (5)

Reserve ONE GLOBAL bit from this original lineage (which has physical reach 1/2), and carry that SAME allocation, in expectation, through every cut. This is an expected-frontier certificate, not a branchwise certificate. No new descendant bank is opened. A prior global quarter-bit debit against it is part of the hypothesis and stays booked.

## Actual resets, original owner, complete ledger

Immediately after querying a, actually replace both inherited references by the actual products. Put T_0=mean TC there, K_0=mean inherited KL, and sigma_0=T_0-K_0. By (1), A=E_a+O_a+K_0. The uncovered first conversion after releasing E_a is

    D_0=sigma_0-E_a=O_a+T_0-A=T_0-K_0-E_a<=T_0<=M.

For every subsequent private query, ACTUALLY use the current product as the incoming reference, transport it by the common kernel, retain both outcomes, and ACTUALLY replace both resulting references by their actual products. Stop anywhere, including constants and characters. At query depth d let sigma_d be the physical-reach sum of the local signed reset costs. Even charging positive local costs separately,

    sum_(nodes at depth d) reach * [sigma_node]_+
       <= sum_(nodes at depth d) reach * mean TC_child <= M. (6)

The first inequality only discards nonnegative inherited KL; it does not identify branch information with spectral erasure. Frontier completion proves the last inequality even with adaptive stopping. There are at most 2w private query depths. Therefore the SAME original bank pays the quarter-bit prior and all reset withdrawals with total at most

    1/4+[D_0]_+ +sum_private_nodes reach*[sigma_node]_+
       <1/4+(2w+1)U_w.

Let N(w)=(2w+1)(2w^2+9w+6). Then (2w+1)U_w=N(w)/2^(w+1). For w>=14 this decreases: 2N(w)-N(w+1)=4w^3+8w^2-31w-39>0, as is immediate at 14 and from its forward difference 12w^2+28w-19>0 thereafter. At w=14 the value is 3799/8192<1/2. The original unused balance is consequently

    >3/4-3799/8192=2345/8192>9/32.                        (7)

For complete accounting, let E_later denote the reached sum of later erasure KLs, O_all all outcome KLs, and T_L the final product KL. Exact telescoping, retaining signed resets, yields

    A+D_0+sum_private_nodes reach*sigma_node
       =O_all+E T_L+E_later.                             (8)

The charged positive withdrawals dominate its left side. Adding E H_L on both sides preserves BOTH full terminal cross entropies. E_later is an unspent release, not an extra charge or a new owner. Initial A remains supplied; (7) pays only the specified extra conversion withdrawals and the prior quarter, not an arbitrary upstream source cost. Querying a private bit of the first factor while the second is untouched gives two unequal nonconstant Boolean children: one core is p_w(v), the other p_(w-1)(u')p_w(v). Thus this result includes the mixed-child query missing from the previous one-defect/delayed-reset theorem, and does not replace actual resets by terminal diagnostics.

## Honest boundary

This closes all private-query product-reset histories for this equal-width two-factor family with the stated original account. It does not close arbitrary reference-profile edits, arbitrary Boolean cores, controller queries, or FEI. The first unsupported universal line is a dimension-free summable bound replacing (4)-(6) when the core has no small marginal-entropy frontier bound. NEXT: expose x after an already paid mixed data prefix, with the original bank diminished by the actual signed history, and test whether one remaining unused lineage allocation pays the true controller/reset bill while both full terminals and A remain retained.
