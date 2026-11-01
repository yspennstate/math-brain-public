# A051: threshold witnesses, critical representatives, and limits

All functions below are actual Boolean signs on finite uniform cubes. Entropy is in bits. Write p_f(S)=fhat(S)^2, H(f)=sum p_f(S)log2(1/p_f(S)), I(f)=sum |S|p_f(S). Constants have H=I=0; never divide by their influence. For nonconstants set R(f)=H(f)/I(f), and for a fixed finite proposed C>=0 set D_C(f)=H(f)-C I(f). All the results below are analytic proofs; exact finite checks provide validation, not the all-dimensional implication. Independent review is pending.

## 1. The extremality notion

A C-witness is a Boolean f with D_C(f)>0. A dimension-critical C-witness is a C-witness with the least possible number of essential physical coordinates among all C-witnesses. A descendant-critical C-witness has no violating proper physical restriction and no violating proper disjoint tensor factor. Dimension-critical implies descendant-critical. The converse is not claimed. Essential dimension means deleting coordinates on which f is constant, not making an arbitrary invertible linear change of coordinates.

Use C-witnesses as the reduction-stable admission property. Use dimension-critical representatives only when the operation preserves minimality or after re-minimizing. Tensoring, balancing, and activation preserve or approximate witness admission as specified below; they generally do not preserve dimension-criticality. This distinction is part of the definition, rather than an unstated assumption that every reduced object is an optimizer.

Let M_n be the maximum R over nonconstant signs on n labelled coordinates, with irrelevant coordinates permitted. It exists because there are finitely many truth tables. M_n<=n 2^(n-1): cube connectedness gives at least one bichromatic edge, hence I>=2^(1-n), while H<=log2(2^n)=n. Adding irrelevant coordinates proves M_n<=M_(n+1). Thus C_*=sup_n M_n=lim_n M_n in [0,infinity]. No maximum over all dimensions is asserted. The two-bit point defect has four equal spectral masses, H=2 and I=1, so C_*>=2.

For every finite C<C_* there is a C-witness by the definition of supremum. The nonempty set of its possible essential dimensions is a subset of the positive integers, so it has a least element d_C. There are finitely many Boolean functions at that dimension; therefore a dimension-critical C-witness exists. Among these finitely many functions one may additionally maximize R or D_C if a tie-break is useful. This is an existence theorem conditional on a counterexample to the fixed constant C; it does not assume FEI fails.

If C_* is finite, take C_j=C_*-1/j for all j large enough that C_j>=0 and choose dimension-critical C_j-witnesses. Then C_j<R(f_j)<=C_*, so R(f_j) tends to C_*. If C_*=infinity, choose dimension-critical j-witnesses; their ratios tend to infinity. These are finite approximation statements with no asserted effective dimension bound. A finite dimension bound on an approximating sequence would imply attainment (choose a recurring truth table after finite enumeration); no such bound is proved.

## 2. Precisely allowed reductions

Output sign, physical coordinate permutations/flips, and addition/deletion of irrelevant variables preserve H and I. Arbitrary physical linear cube changes can preserve H while changing I and are not admitted as budget-preserving operations.

For disjoint variable sets, f(x)g(y) has fghat(S,T)=fhat(S)ghat(T). Therefore its spectral law is the product, H(fg)=H(f)+H(g), and I(fg)=I(f)+I(g). In particular D_C(fg)=D_C(f)+D_C(g). For two nonconstant factors its ratio is the influence-weighted average of their ratios. A violating product has a violating nonconstant factor. Conversely a tensor power f^tensor k preserves R and has deficit kD_C(f). A factor of a dimension-critical witness cannot be a proper nonconstant disjoint tensor factor: otherwise at least one factor is a smaller C-witness. Thus dimension-critical witnesses are tensor-indecomposable, modulo constants and irrelevant variables.

A violating restriction may be selected as a smaller witness; this preserves the threshold C, not the precise original ratio. Repeatedly select a violating proper restriction or disjoint factor, deleting irrelevant coordinates. Essential dimension strictly decreases at each substantive selection, so this procedure terminates at a descendant-critical C-witness. It need not find d_C without a global search. An arbitrary restriction is not witness-preserving: f=(1,1,1,-1) on two bits has R=2, while every one-bit restriction is constant or a character and has H=0. Consequently no assertion of criticality inheritance by descendants is valid here.

Balancing: b(x,y)=y f(x) is balanced, H(b)=H(f), I(b)=I(f)+1, and D_C(b)=D_C(f)-C. It can destroy a C-witness. Balance after tensor amplification: b_k=y product_(l=1)^k f(x^(l)) has H=kH(f), I=kI(f)+1, and D_C=kD_C(f)-C. If D_C(f)>0, any integer k>C/D_C(f) preserves admission. R(b_k) increases to R(f). The balanced supremum therefore equals C_* in the extended real sense. It does not follow that balanced witnesses have the minimal possible dimension.

For a balanced Boolean core g and A_r(z)=1_{z=(+1,...,+1)}, let p=2^-r and F=1+A_r(g-1). Direct expansion of A_r gives

H(F)=pH(g)+2rp(2-p)+h((1-p)^2),
I(F)=p(I(g)+r),  P(F=-1)=p/2,

where h(t)=t log2(1/t). Indeed the empty Fourier coefficient is 1-p; each nonempty selector-only coefficient has magnitude p; each core coefficient ghat(S), S nonempty, gives 2^r coefficients of magnitude p|ghat(S)|. These disjoint classes yield the entropy formula. Each data influence is multiplied by p; each selector influence is p because g is balanced. In particular the entropy overhead is nonnegative. At fixed r, a balanced tensor core can dominate the selector cost, but fixed r alone does not force influence to zero.

An explicit simultaneous scaling is k=m^2, g_m=y f^tensor k, r=m, p=2^-m. Then

I(F_m)=2^-m(m^2 I(f)+1+m) -> 0,
P(F_m=-1)=2^(-m-1) -> 0,
R(F_m) >= m^2 H(f)/(m^2 I(f)+1+m) -> R(f).

The matching upper limit follows by dividing the exact entropy formula by p: the overhead is 2m(2-p)+h((1-p)^2)/p, and h((1-p)^2)/p is bounded for m>=1 and tends to 2/ln2. Hence R(F_m) -> R(f). For a C-witness, m^2D_C(f)>C(m+1) suffices to retain D_C(F_m)>0; both rarity bounds can be met by increasing m. Given any epsilon,delta>0, the supremum of R among 0<I<=epsilon and P(F=-1)<=delta equals C_*. This recovers the published activation-equivalence baseline with an explicit sequence; it is not claimed as a new class theorem.

These sparse representatives are not critical representatives: fixing all selector bits to +1 gives g_m, and for sufficiently large m the displayed tensor-balancing inequality makes g_m a smaller C-witness. They also converge to 1 in L2 because E(F_m-1)^2=4P(F_m=-1). Since R(F_m)->R(f)>0 for the two-bit seed, extending R(1)=0 does not make R continuous. Compactness in L2 alone cannot justify optimizing the ratio or retaining extremality at a constant limit. This does not prove nonattainment of C_*; it identifies why this suggested argument is invalid.

## 3. Exact structural consequence of minimality

Let f be a dimension-critical C-witness. For any nonempty block A of essential coordinates (including the full block), let f_a be its physical restrictions, uniform over a, and I_A=sum_(i in A)Inf_i(f). Every f_a has smaller essential dimension, so D_C(f_a)<=0, including constants. Set L_A=H(f)-E_a H(f_a). Averaging physical j-edge indicators for j not in A gives

I(f)=I_A+E_a I(f_a),
D_C(f)=E_a D_C(f_a)+L_A-C I_A.

Therefore

L_A-C I_A >= D_C(f)>0.                         (3.1)

This uses minimality exactly at E D_C(f_a)<=0. It does not use a component-pruning inequality or treat components as physical restrictions.

For completeness derive the information terms. Write Z for the full spectral random subset. For T subset A^c, let v_T(a)=E_y f(a,y)chi_T(y); q_a(T)=v_T(a)^2 is the actual child spectrum. Parseval in a gives q(T)=E_a q_a(T)=sum_(U subset A)fhat(U union T)^2, precisely the Z_(A^c) marginal. In the experiment where a is uniform and T has conditional law q_a, put

M_A=H(Z_A | Z_(A^c)), J_A=I(a;T).

The entropy chain rule yields H(f)=H(q)+M_A, E H(f_a)=H(q)-J_A, hence L_A=M_A+J_A. Both terms are nonnegative. Equation (3.1) becomes

M_A+J_A >= C I_A+D_C(f).                       (3.2)

For a singleton, J_A is the Jensen-Shannon divergence between the two child squared spectra. The source ERASURE_REDUCTION section 2 further proves J_i<=(2/ln2)min(Inf_i,1-Inf_i). If that optional baseline is used, (3.2) forces

H(Z_i | Z_-i) >= C Inf_i+D_C(f)-(2/ln2)min(Inf_i,1-Inf_i).

This sharper necessary condition is conditional only on that already source-complete scalar baseline, not on B09's pending biased theorem. Summing yields B(f)>=C I(f)+d_C D_C(f)-(2/ln2)sum_i min(Inf_i,1-Inf_i). It is a necessary condition for critical witnesses, not an influence-paid bound on B.

For any finite adaptive physical restriction tree, at internal node v reveal a nonempty block A_v, write pi_v for its actual reach probability, L_v for its entropy decrement, and d_v for its erased influence. Applying the deficit identity at each node and canceling child terms proves

D_C(f)=sum_internal pi_v(L_v-C d_v)+sum_leaves pi_l D_C(f_l).

The corresponding two separate telescopes are H(f)=sum pi_v L_v+E H(f_leaf) and I(f)=sum pi_v d_v+E I(f_leaf). If the root is dimension-critical and every leaf is a proper restriction, all leaf deficits are <=0 and the internal sum is at least D_C(f)>0. No descendant-criticality is assumed, and influence is spent exactly once. The case of a tree stopping at the root has no proper-leaf conclusion.

## 4. What this closes and what remains

This proves the packet's existence/minimal-counterexample requirement, gives threshold-safe tensor/balancing/activation ledgers, and supplies all-block criticality inequalities for A052. It does not prove FEI, a uniform dimension bound, optimizer attainment, connectedness, component entropy subadditivity, or a payment of (3.2). Connected-component removals and point surgery require separate lemmas; neither is an admitted reduction here. The raw-indicator criticality in ADDENDUM_11_26 is a different ratio/adjusted orientation, and cannot be substituted for ordinary sign H/I. The nine-bit component obstruction in ADDENDUM_11_44 remains applicable to raw component entropy; the present proof never invokes that false inequality.

The first unproved downstream implication is: exclude dimension-critical C-witnesses for one finite absolute C, by showing that at least one allowed restriction has L_A<=C I_A, or by another structural contradiction. The required finite C is not produced. No source-complete unreviewed claim beyond the two bundled claims is opened.
