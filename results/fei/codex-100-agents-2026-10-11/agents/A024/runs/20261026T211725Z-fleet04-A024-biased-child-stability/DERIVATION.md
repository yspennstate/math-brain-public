# Endpoint-aware payment for the actual binary activation

All logarithms are base two. Physical coordinates have the uniform product law. Put e(s)=-s log2(s), with e(0)=0, and L(a,b)=e(a²)+e(b²)-e(a²+b²). Let w,h be arbitrary Boolean functions on DISJOINT finite coordinate blocks, F=1-(1-w)(1-h)/2, t=Pr(w=-1), r=Pr(h=-1). No bounded-degree or two-flat hypothesis is needed below.

## 1. Scalar estimate, with endpoints

The retained exact activation identity for a physical query i in w is

    B_i(F)=r B_i(w)+R_r(a,b),  Inf_i(F)=r d,
    R_r(a,b)=L(1-r+ra,rb)+r(1-r)L(1-a,b)-r L(a,b),

where a=Ew, b=(Ew_0-Ew_1)/2 and d=Inf_i(w). In particular |a|<=1 and |b|<=d. The subtraction of the empty-sector term is retained. Fair physical restrictions preserve uniformity of all unqueried coordinates; r,t are output probabilities, not changed physical input biases.

Write c=1-r and k=2/ln(2). The function x -> L(x,b) is even, nondecreasing for x>=0, and k|b|-Lipschitz on the real line. Indeed, away from zero its derivative is

    2x ln(1+b²/x²)/ln(2).

For s>=0, ln(1+s²)<=s: the difference s-ln(1+s²) vanishes at zero and has derivative (s-1)²/(1+s²)>=0. This bounds the derivative; it extends continuously as zero at x=0. Also L(x,b)<=2|xb|, as established in v5. No division by b or r is used when either is zero; treat those cases directly.

If a>=0, Lipschitz continuity gives

    L(c+ra,rb)<=r²L(a,b)+k cr |b|.

Consequently

    R_r <= rc [L(1-a,b)-L(a,b)+k|b|]
        <= (2+k)rc|b|,

using L>=0, 0<=a<=1, and L(1-a,b)<=2(1-a)|b|.

If a=-u<=0 and c-ru>=0, monotonicity and the same inequalities give

    L(c-ru,rb)<=L(c,rb)<=2cr|b|,
    cL(1+u,b)-L(u,b)
       =c[L(1+u,b)-L(u,b)]-rL(u,b)<=ck|b|.

Thus again R_r<=(2+k)rc|b|. If instead c-ru<0, then |c-ru|<=ru, so L(c-ru,rb)<=r²L(u,b), and

    R_r<=rc[L(1+u,b)-L(u,b)]<=krc|b|.

These three cases include a=0 and c-ru=0. At r=0 or r=1 the original expression is zero. We obtain, for all r in [0,1], |a|<=1 and all real b,

    R_r(a,b) <= (2+2/ln2)r(1-r)|b| <= 5r(1-r)d.       (1)

The last rational constant is valid because ln2>2/3 (e.g. integrate the geometric series for 2 atanh(1/3); its first positive term is 2/3). Only the last comparison to d requires an actual Boolean physical derivative. Negative R is allowed. No finite grid is used to prove (1).

## 2. An original interaction reserve, not a renewed reserve

Define the nonnegative actual-state potential

    Xi(w,h)=5[r(1-r) I(w)+t(1-t) I(h)].                 (2)

For a physical query in w, r and I(h) are unchanged, I(w)=d+avg I(w_b), and t_b=t plus or minus b/2. Hence

    Xi(w,h)-avg Xi(w_b,h)
      =5[r(1-r)d + b² I(h)/4] >= max(R_r(a,b),0).      (3)

The h-query identity is obtained by exchanging the two blocks. Disjointness ensures the untouched block really stays fixed even under an adaptive history. Both children and their true reaches are retained. Equation (3) applies to ANY partial adaptive physical tree, including irrelevant queries, constant children and deterministic gates.

Let D_v denote the nonnegative left side in (3), R_v the actual signed activation remainder for the queried block, and ell_v=D_v-max(R_v,0)>=0. Multiplying by actual reach probabilities and telescoping gives the EXACT account

    sum_internal p_v max(R_v,0)
      + sum_terminal p_l Xi(w_l,h_l)
      + sum_internal p_v ell_v = Xi(w_root,h_root).    (4)

For any old debit U, U appears unchanged on both sides after adding it. If an ORIGINAL available balance M has M-U-other_due>=Xi(root), the same account pays every continuation without renewal and leaves every terminal reserve in (4). It does not prove that a previously depleted bank has this capacity. Constant gate outputs have Xi=0; full actual terminal functions can still have nonzero entropy (for example w=-1 leaves F=h), and their ENTIRE entropy, erasure, reference and KL liabilities remain in other_due or the inner accounts. They cannot be removed by Xi=0.

This improves the inherited sufficient universal reserve6I(F): Xi<=5I(F), because I(F)=rI(w)+tI(h). More precisely Xi/I(F) is at most5 max(1-r,1-t) whenever I(F)>0. Small r alone does not make the normalized price small; r approaching1 suppresses only the w-query bill. Thus neither rarity nor variance alone has been used to pay the missing logarithm.

For threshold K and a w-query with B_i(w)<=K d, the actual excess obeys B_i(F)-K Inf_i(F)<=R_v. Equation (4) therefore pays all positive lifted K-excess on queries selected by a hereditary inner K-policy, even with adaptive interleavings. It prices erasure EXCESS, not the whole odd-face debit at every bad node; that conversion still needs a separately justified localization ledger.

## 3. Normalization, limits, and exact remaining gap

Corrected biased FEI+ is sum over nonempty S of p_mu(S) log2(product_{j in S}(1-mu_j²)/p_mu(S)). Its numerator has INPUT variances only. Contract deterministic children before using normalized bases. Equation (1) avoids every variance denominator and all logarithms of means, so it is uniform at deterministic and near-dictator limits. The exact mismatch/KL rebate in prior accounts is not replaced or dropped. No theorem about the percolation spectral law is used here.

This extends the v6 candidate's binary activation transport and gives its K10 two-flat inner policies an explicit original reserve (2) for lifted positive K10 erasure excess. It reduces the separately established zero-bad-debit continuation from K16 to K15, but does not make an old K10 odd-face debit disappear. The first unsupported line is M-U-other_due>=Xi(root) for the SAME already depleted arbitrary-core original bank, together with a justified conversion from paid positive erasure excess to the requested full localized odd-face debit. The existence and influence price of arbitrary inner policies also remain open. Full FEI remains OPEN; this is an all-dimensional author proof with finite exact checks, pending independent reconstruction and formal admission.
