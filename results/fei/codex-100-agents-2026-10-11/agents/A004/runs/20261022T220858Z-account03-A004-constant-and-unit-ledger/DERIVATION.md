# Same ancestor account through a full-support nonflat reset

The full FEI conjecture remains open. The result here is a reference accounting lemma and its application to the saved neutral AND3/Maj3 fixture. All entropies, cross-entropies and divergences use base two; all spectra include the empty set.

## 1. The local identity with the actual phases

Let g be any Boolean sign on a finite uniform cube and query physical coordinate i. For each residual Fourier index T write a=ghat(T), b=ghat(T+i). Its actual child masses are p_+(T)=(a+b)^2 and p_-(T)=(a-b)^2. Thus their arithmetic mean is m(T)=a^2+b^2, the marginal of the parent spectrum P after erasing i. This is an amplitude identity, not conditioning of the parent squared spectrum.

Let R be any normalized reference law on parent Fourier sets satisfying P<<R. Write r(T)=R(T)+R(T+i), and use this SAME marginal reference in both children. All child supports lie inside the support of r. Put

    C(P,R) = -sum P log2 R = H(P)+D(P||R),
    c_i(P,R) = D(P||R)-D(m||r).

The chain rule gives c_i as a sum, with weights m(T), of binary conditional KL divergences. Hence c_i>=0. A zero-mass pair contributes zero; division occurs only for m>0, when r>0. Terms with P>0 have R>0. No support limit or interchange of infinite sums is used.

Since cross-entropy is linear in its first argument,

    [C(p_+,r)+C(p_-,r)]/2 = C(m,r).

Also B_i(P)=H(P)-H(m). Subtracting the two cross-entropies proves the exact identity

    B_i(P) + [C(p_+,r)+C(p_-,r)]/2
      = C(P,R)-c_i(P,R).                                  (1)

Nonnegative conditional KL is the refund in this reference ledger. In the actual-root case R=P, c_i=0 at that first query, even when the children have positive KL relative to m. That child KL is precisely their Jensen-Shannon divergence. This cancels the JS term lost by replacing child entropy with cross-entropy; it must not be charged a second time.

## 2. A prescribed multiplicative reset

At a reached node replace an inherited normalized reference r by a normalized Q with Q>=alpha*r on the whole support of the node's actual law p, where 0<alpha<=1. The exact signed reset cost is

    e(p;r,Q)=C(p,Q)-C(p,r)=sum p log2(r/Q).

It can be negative. Pointwise domination proves e<=log2(1/alpha). For the explicit prescription Q=(1-t)r+tU, with U uniform on ALL remaining Fourier sets and 0<t<1, alpha=1-t; Q has full support. This is a specified transformation of the inherited reference, not the unspecified existence of a favorable reference. It still depends on that inherited law.

The condition is sharp when the reset price must hold independently of the Boolean node: for FIXED normalized r,Q with Q positive on support(r),

    sup_{Boolean g: P_g << r} e(P_g;r,Q)
      = log2 max_{T:r(T)>0} r(T)/Q(T).                    (sharp)

The upper bound is the maximum of a linear expectation. A Boolean character g=chi_T has spectrum concentrated on any chosen T, so a maximizing atom attains it. If Q vanishes at an r-positive atom, the corresponding character has infinite reset cost. Thus a cap b for EVERY Boolean g with this fixed reference is equivalent to Q(T)>=2^(-b)r(T) at every r-positive atom. This necessity has fixed-reference quantifiers; it does not allow varying g while insisting that r was produced by that g's particular ancestor. It is a constant/unit guard for reference-only claims, not a refutation of a correlation-aware payment.

Iterating (1) through ANY finite adaptive restriction tree, including arbitrary stopping, gives

    W + sum_leaves reach*C(p_leaf,R_leaf)
      + sum_queried_nodes reach*c_i
      = C(P_root,R_root) + sum_resets reach*e.              (2)

Here W is the reach-weighted sum of actual erasures. Queries marginalize the current reference; resets replace it and are booked once. The tree retains both physical outcomes, whose probabilities are 1/2. The reference may depend on earlier outcomes. Finite-tree induction proves (2); randomized policies follow by averaging their fixed random seeds. There is no separately asserted nonnegative allocation in every child.

If reset nodes form an antichain, their reaches sum to at most one. Therefore one such frontier of t-resets costs at most log2(1/(1-t)), irrespective of the later query schedule. More generally use the actual sum of reach-weighted log prices; a new reset is never free merely because it has a new child label. In nats this price is -ln(1-t), and the ENTIRE equation (2) is multiplied by ln(2).

Boundary checks matter. For t=0 there is no reset, no strict full-support conclusion, and zero cost. For t=1 the finite domination price is unavailable (a finite cube still has finite uniform cross-entropy). Reversing the domination direction gives no claimed bound: a dictator's one occupied spectral atom against the uniform two-atom law costs one bit, larger than log2(8/7).

## 3. The original neutral six-bit AND3 account

On binary data y in {0,1}^6 let b(y)=+1 exactly when y0=y1=y2=0; otherwise b=-1. Let c equal b except c(0)=-1. On three fresh binary encoder bits put h(x)=+1 when at most one encoder bit equals 1, and h=-1 otherwise. Let F(x,y)=b(y) when h=+1 and c(y) when h=-1. This is the same actual nine-bit table as A001's source; encoder bits occupy physical indices 0,1,2 and data bits 3,...,8.

Both terminal core influences are 3/4. Hence the ORIGINAL rate-four account is 4*(I(b)+I(c))/2=3. The original escrow T0=[H(b)+H(c)]/2 and surplus S4=3-T0 are unchanged. The independently checked root spectrum has H(F) in (2444203,2444204)/10^6 bits, and 3-H(F)>555796/10^6. A001's all-actual-history conclusion follows directly by taking actual entropies and nonnegative JS at each query, so its declared scope HOLDS without a repair. An exhaustive re-enumeration of its 59,049 local pairs is unnecessary for this independent reconstruction.

Now query data y3 (physical index 6), an originally dummy coordinate of b that is active after the point edit. Both actual child functions are nonconstant. Start with R_root=P_F, marginalize it to r, and prescribe in BOTH children Q=7r/8+U/8 on all 256 residual Fourier sets. This is normalized, positive everywhere, and nonflat because r is nonflat. Keep BOTH complete child cross-entropies. Every subsequent physical query uses the current reference's marginal in both outcomes; no further reset occurs. Equation (2) yields, for every adaptive stopped continuation,

    W + expected COMPLETE terminal cross-entropy
      <= H(F)+log2(8/7)
      < 3-363150/10^6.                                   (3)

The same statement holds for one t=1/8 reset frontier anywhere in any adaptive physical history. To retain a nonflat reference at a specific frontier node one must check that its inherited reference is nonflat; (3) itself does not require nonflatness. Constants and fully restricted leaves are allowed. A constant leaf's nonzero cross-entropy against its incoming reference is retained until further marginalization or an explicitly paid reset; it is not replaced by zero entropy.

The old admission debit H(F)-T0 stays booked: the account is

    S4 -(H(F)-T0) -sum reach*e +sum reach*c_i,

with its full terminal escrow retained by (2). No descendant 4I-H reserve is added. In ordinary entropy units, the guaranteed new margin is 3-H(F)-log2(8/7); the checker also records the larger exact margin for the specified y3 reset using its actual signed cost.

## 4. Exact unpaid line

Equation (3) is a scoped reference continuation theorem, not universal FEI. Its root account has been separately paid only for this fixed fixture. The explicit reset is controlled by the INHERITED reference; it does not establish that an independently prescribed canonical or source-compressed reference dominates that law at a comparable price. The remaining universal line is to construct and fund such references, including any accumulated reach-weighted reset excess, for arbitrary Boolean roots from O(I) without using their unknown entropy as an allowance. The sharp domination estimate is useful for checking that line, but supplies no proof of it.
