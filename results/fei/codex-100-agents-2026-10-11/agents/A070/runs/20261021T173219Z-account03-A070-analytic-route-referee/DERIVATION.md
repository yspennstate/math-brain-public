# Referee result and a depth-free flag ledger

The A069 stage6 history theorem HOLDS at its full stated scope, without repair. The A088 conditional-flag local-price obstruction also HOLDS. The additional result below is an author proof, awaiting independent review. Full FEI is OPEN.

## 1. A069 independent reconstruction

Take four Boolean cores (a,b,-b,-a) in order c+2u, and F=q2 G where q2 is negative exactly at c=0,Z=0, |Z|=m>=1. Write rho=2^-m, t=rho^2, beta=2rho(1-rho), d=Pr(a!=b), A=(I(a)+I(b))/2. Fix one positive normalized core reference R, and carry it at every physical restriction by marginalizing the queried frequency bit. Let B=(C_R(a)+C_R(b))/2. The original five control cells and weights are retained: {c},{u},{c,u}, tails with u absent/present have weights 1/4,1/4,1/16,7/20,7/80. Each tail has 2(2^m-1) atoms. The flag probability of an empty control set is td.

Partial Parseval and the paired signs give exactly

    C = B+h2(td)+2+2(1-2d)rho
          +beta[m+log2(1-rho)+log2(20/7)],
    I = A+1+(m+1-2d)rho.

These are complete cross entropy and physical influence. The reference includes the actual core frequency, the control flag, the cell label and the complete tail atom; all positive output atoms are covered. At d=0 the empty flag has zero mass and contributes zero. Neither conditioning nor an entropy-only surrogate removes a terminal bill.

On a physical Y query the nonflag control terms average exactly. Thus Delta C=Delta B+J where J=h2(td)-E_child h2(td_child). Core influence is (Inf_i(a)+Inf_i(b))/2. This follows from averaging physical derivatives over c,u,Z, whose signs do not depend on Y. The independent checker constructs all 81 actual outputs on three private widths and all 81 query edges; complete normalized Q cross entropies agree as exact prime-log expressions, and physical edge counts agree with Fourier degrees. It imports no author helpers.

For a=Maj3,b=y0, R=(8/13,2/13,1/26,...,1/26), the 27 partial core patterns and their 27 possible queries certify Delta B<=4 Inf_i at relevant queries, Delta B<1/4 otherwise. These core statements are independent of m; irrelevant queries have J=0. For every query 0<=J<=t<=1/4 by independent thinning, so the positive query excess is <=1/4. The author's three-query allocation therefore remains valid.

At fully fixed Y terminals B=A=0, d in {0,1}. All terminals have positive influence at least 1-rho. For m=1,2 both d cases have surplus 4I-C>1, verified with rational log intervals. For m>=3, h2<=1, log2(1-rho)<=0, beta<=2rho and log2(20/7)<8/5 give

    4I-C >= 1+rho(2m+2-4d-16/5) >= 1+4rho/5 > 1.

The logarithm bound is certified by 20^5<2^8*7^5. No denominator vanishes because m>=1. The exact restriction telescope and at most three quarter-unit debits against one complete final bank prove the original >1/4 root-surplus claim. This independently accepts the original, without relying on the improvement below.

## 2. One flag charge for an arbitrary adaptive history

Let a,b be ANY Boolean functions on a finite uniform core cube. Let a physical adaptive tree query only distinct Y coordinates, with stopping decisions depending on previous physical outcomes, and hold m and the five control-cell weights fixed. For every node v let p_v be its actual probability and d_v its conditional disagreement probability. Put J_v=h2(t d_v)-E_child h2(t d_child). Then

    0 <= sum_internal p_v J_v
       = h2(t d_root)-sum_leaves p_l h2(t d_l)
       <= t h2(d_root) <= t.                         (A)

Proof: choose Y uniformly, D=1{a(Y)!=b(Y)}, and E~Bernoulli(t) independent of Y and of the physical tree. Set W=E D. The leaf transcript L is a function of Y. Conditional on the transcript at a node, Pr(W=1)=t d_v. The equality is finite entropy telescoping, or the chain rule for I(W;L). Data processing gives

    I(W;L)<=I((E,ED);L)=t I(D;L)<=t H(D).

This uses the SAME E in the representation of the whole history, not a freshly chosen independent income at each node. It also handles partial stopping and arbitrary adaptive query orders. All sums are finite. For complete Y exposure equality sharpens to h2(td_root)-d_root h2(t). Endpoints t=0,1 and d=0,1 obey the same identity with 0 log 0=0. For this physical family t>0 and t<=1/4; no conditioning on a zero-probability atom is needed.

Let e_v=Delta B_v-K Inf_i(v). Since J_v>=0,

    sum p_v (Delta C_v-K Inf_i(v))_+
       <= sum p_v (e_v)_+ + t h2(d_root).             (B)

Equation (B) removes a depth multiplier from the FLAG part only. It does not prove a bound for the positive core-reference excess. The signed sum retains exactly

    K I_root-C_root
      = sum_leaves p_l(K I_l-C_l)
          -sum_internal p_v(e_v+J_v).               (C)

Both full terminal bills and any prior debits remain in (C). A bank already spent outside this subtree cannot be counted again. This is the precise universal unpaid line: pay the cumulative positive core-reference excess, or justify its signed cancellation against exclusively unused descendant surplus, for a supplied common reference on arbitrary Boolean cores.

## 3. Stronger scoped consequence, all m>=1

For the fixed majority/literal cores, A_root=5/4 and B_root=15/4+log2(13/16). Full physical core exposure gives B_leaf=A_leaf=0, irrespective of adaptive query order. Hence

    sum p_v e_v = B_root-4 A_root = -5/4+log2(13/16).

By (A), the total flag refund is <=1/4. Since (13/16)^4<1/2 (integer comparison 2*13^4<16^4), log2(13/16)<-1/4. Thus the total SIGNED excess is <-5/4. The same final terminals each have surplus>1, so (C) yields

    4I(F)-C_Q(F)>9/4, for every m>=1.

This improves A069's conservative >1/4 guarantee using signed cancellation and ONE terminal bank. The constants differ because the earlier argument discarded positive query prices and charged each of three queries separately; the present argument retains all signed core prices and telescopes the single flag. It does not assert a >9/4 unused bank at every partial child after unrelated spending. All 12 complete adaptive trees for each m=1,2,3 verify the exact flag, signed excess and terminal identities. The proof for all m is the analytic boundary argument above, not extrapolation from these 36 trees.

## 4. A088 conditional-flag obstruction independently checked

For m>=2 define b(Y)=(-1)^(sum Y_(2j-1)Y_(2j)), on 2m bits, and G=b+1{w=0,Y=0}(z-1). Let delta=2^-(2m+1), A=2^-m. Direct tensor Walsh calculation gives each core row u_T=1{w absent} sigma_T A-delta and v_T=delta. Thus I_z=delta. Rows with w present contribute exactly delta to H(V|T). Rows without w have q_T=u_T^2+delta^2>delta^2*2^(2m+1), since delta/A<=1/8. Their entropy contribution is at least delta(2m+1)/2 by h2(p)>=p log2(1/p). Consequently

    H(V|T)/I_z >= m+3/2.

The physical parent P=(-1)^(cw+sum Ypair products)+1{c=w=0,Y=0}(z-1) restricts at c=0 to G; the independent checker verifies this exact reachability. Physical influences sum to m+(2m+2)delta: each Y coordinate gains delta at the edited vertex, and w,z each have influence delta. H<=2m+2 yields H/I<=3. For m=2,3 direct spectra, physical counts and certified conditional entropies verify all formulas. This accepts the full analytic family, not just two cases. It refutes isolated conditional flag payment by K I_z, not FEI, weighted selection or signed unused child payment.

## 5. Booleanity and cyclic-law scope guards

The abstract thinning and entropy-telescoping lemma is a probability identity and does NOT use Booleanity. The physical identification d=Pr(a!=b) and empty-control mass=td uses (a-b)^2/4=1{a!=b}, which is Boolean. Physical pivotal influence and the claimed complete reference payment also use actual signs and the paired sum-zero structure. Arbitrary four Boolean cores do not have that structure. Arbitrary normalized real spectra cannot inherit a paid core-reference bank: psi_n=n^-1/2 sum x_i has H=log2 n and I=1, with nonzero two-coordinate coefficient 2/n in psi_n^2. These nonlinear Boolean identities cannot be replaced by normalization.

The historical cyclic-law certificate Addendum 11.51 remains unavailable as a source-complete witness. No new cyclic reproduction or acceptance is asserted. The present flag lemma needs no cyclic independence; the SAME auxiliary gate and the full physical transcript supply its joint law explicitly. A hypothetical arbitrary probability-law payment of the missing core excess still fails the singleton-spectrum guard. Padding and point edits do not break (A), but can change the reference bank: no edit-stability of that unpaid bank is inferred.
