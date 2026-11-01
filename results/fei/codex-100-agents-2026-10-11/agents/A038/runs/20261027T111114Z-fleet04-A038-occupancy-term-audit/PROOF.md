# V4 has exactly the universal strength of FEI

All entropies are in bits. Let f be Boolean on a finite uniform cube. Let H(f) be the entropy of its squared Walsh coefficients and I(f) its total influence. For a fresh physical coordinate i put

    e_i(f)=H(f)-(H(f_i=+1)+H(f_i=-1))/2,
    d_i(f)=Inf_i(f),  delta_i(f)=e_i(f)-4d_i(f).

For any finite adaptive tree querying each physical coordinate at most once per path, use its actual uniform-input reach weights w_v. Define V4(f) as the maximum of sum_v w_v [delta_i(v)(f_v)]_+ over these trees, including stopping trees. There are finitely many such trees. Constants have H=I=V4=0. Queries of dummy coordinates are permitted and harmless.

## 1. The missing sign

Fix i and write f(x,y)=a(y)+x b(y). Its two restrictions are g=a+b and h=a-b, both Boolean. For every residual Fourier set T set u_T=ahat(T), v_T=bhat(T), and q_T=u_T^2+v_T^2. Parseval gives sum q_T=1. The full squared spectrum has masses u_T^2 and v_T^2 at T and T union {i}; the slice squared spectra are P_g(T)=(u_T+v_T)^2 and P_h(T)=(u_T-v_T)^2. Each slice law is normalized, and (P_g+P_h)/2=q.

Use 0 log 0=0 and omit q_T=0 fibers. The entropy chain rule gives

    H(f)=H(q)+B_i,
    B_i=sum_T q_T h2(v_T^2/q_T)>=0.

Concavity of Shannon entropy gives the Jensen-Shannon divergence

    JS_i=H(q)-(H(g)+H(h))/2>=0.

Therefore e_i=B_i+JS_i>=0 at EVERY physical query. No coordinate-selection hypothesis, balancedness, independence between slices, occupancy reference, child surplus assumption, or FEI hypothesis is used. This is a direct finite calculation; no limit or exchange of infinite sums occurs. Booleanity is used to normalize both child squared spectra under the actual fair physical weights.

## 2. All trees and boundary leaves

Because d_i>=0 and e_i>=0,

    0 <= [e_i-4d_i]_+ <= e_i.

Entropy telescoping on a stopped tree gives sum_v w_v e_i=H(f)-E H(f_leaf)<=H(f). Thus every tree has positive-deficit cost at most H(f), even when its leaves have nonzero entropy. Maximizing proves

    [H(f)-4I(f)]_+ <= V4(f) <= H(f).                 (1)

For the lower inequality, complete any tree to singleton input leaves. Those leaves are constants. Physical influence conservation gives I(f)=d_i+(I(g)+I(h))/2, hence sum_v w_v d_i=I(f) for any complete tree. Its signed deficit sum is H(f)-4I(f); its positive sum is at least that and at least zero. Completion never lowers a positive-cost sum. This also proves that a complete tree attains V4.

At n=0 all terms vanish. If d_i=0 then f is independent of i, g=h=f with i removed, and e_i=0. If q_T=0 its entropy contribution is zero. Constants and characters have V4=0. No quotient by influence is needed anywhere in (1).

For any lambda>=0, the identical proof gives [H-lambda I]_+<=V_lambda<=H. The nonnegative lambda hypothesis is essential for the upper argument: a one-bit character has e=0,d=1, and V_lambda=-lambda>0=H when lambda<0.

## 3. Exact capped-drop complement

The scalar identity [e-4d]_+=e-min(e,4d) gives, for every complete tree T,

    cost_V(T)=H(f)-sum_v w_v min(e_i(v),4d_i(v)).

Consequently

    V4(f)=H(f)-W4(f),
    W4(f)=min_complete_T sum_v w_v min(e_i(v),4d_i(v)),
    0<=W4(f)<=4I(f).

Both V4 and W4 have exact finite Bellman recursions, with maxima and minima respectively. This supplies a second derivation of (1) and a separate finite-check implementation. An optimized V4 bound still needs the whole unpaid entropy: the complement W4 is already at most 4I.

## 4. Universal quantifiers and correction of the earlier scope

If a finite absolute C satisfies H(f)<=C I(f) for EVERY finite-dimensional Boolean f, then V4(f)<=C I(f) for all the same f by the upper inequality of (1). Conversely, if a finite absolute K satisfies V4(f)<=K I(f) for every such f, then H(f)<=4I(f)+V4(f)<=(4+K)I(f). The constants are dimension independent and the zero-influence constant case is already covered.

Thus existence of a universal V4/I bound is EQUIVALENT to full FEI, with constants C -> K=C and K -> C=K+4. In particular, an actual Boolean family with unbounded V4/I necessarily has unbounded H/I, since V4<=H. A single violation of a proposed numerical constant is insufficient. An unbounded family of costs from specified actual trees would suffice as well, since every such cost is at most V4 and hence at most H. All values must refer to actual Boolean functions and physical weights.

The previous stage11 report says, 'An obstruction to this stronger target alone would not refute FEI.' For the precise V4 defined there, that sentence is false if 'obstruction' means a rigorous unbounded-ratio Boolean family. Failure of a single proposed constant K, an upper surrogate, or a local helper remains insufficient to refute FEI. This correction does not alter any earlier reset bill or source-owner ledger.

## 5. Occupancy account remains separate

The archived source-exact occupancy candidate is K_occ=D(P^+||Q_r)=Hmax(r)-H(P^+), where P^+ is the ACTUAL NONEMPTY spectrum and Q_r is its matched-marginal maximum-entropy law on nonempty subsets. If mu=sum r_i=1 it is the singleton law; otherwise its conditional-product parameter c>0 solves 1-c=product_i(1-c r_i). It is not full-spectrum total correlation. For the proposed Gibbs prices, its unpaid target is K_occ>=[Hmax(r)+a_q-sum r_i a_i]_+. No new lower bound for that target is asserted here. V4 came from the already authorized stopping-payment supplier audit; (1) proves why that supplier has full-FEI strength rather than bypassing the occupancy debt.

## 6. Exact first unsupported line

There exists K<infinity, independent of n and f, with V4(f)<=K I(f). Equivalently, H(f)-W4(f)<=K I(f). Neither the sign identity, the Bellman recursion, the finite census nor the previous tensor theorem proves that line. Full FEI remains OPEN. The next useful work must supply a quantitative Boolean inequality beyond entropy concavity, rather than try to distinguish the universal strengths of V4 and H.

Rung: analytical proof with exact finite implementation checks; independent external review pending. The finite census certifies only its declared finite domain. No Lean certification of the Shannon or all-tree theorem is claimed.
