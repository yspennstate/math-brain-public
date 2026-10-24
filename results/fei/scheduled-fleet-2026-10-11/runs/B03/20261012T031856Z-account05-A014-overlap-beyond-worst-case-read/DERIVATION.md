# A014 stage 2: generic interference and dilute bounded intersections

Units bits, uniform +/-1 cube, monotone positive conjunctions. No full FEI claim.

## Arbitrary-union Lemma I (no geometric assumptions)
Let d=d_j f=sum_l u_l+r, alpha=||d||_2^2>0, E any residual Fourier event and eta>0. Young's inequality and Parseval give

    alpha nu_j(E) <= (1+eta)[sum_l ||P_E u_l||_2^2
                       +sum_{l!=m}<P_E u_l,P_E u_m>]
                       +(1+1/eta)||P_E r||_2^2.

The cross sum has its actual sign; it cannot be silently deleted. The same inequality holds with P_E replaced by the square root of any nonnegative Fourier multiplier, in particular a rank/rarity cost. No Booleanity of u_l or disjoint-support assumption is required. This is a source-complete extension of the prior ideal-piece repair, not a mass-only K_eff argument.

## Complete dilute-intersection theorem
Let H be a nonempty hypergraph of distinct nonempty edges R_l, with |R_l|=w_l<=W, |R_l intersect R_m|<=t for l!=m, t>=1. Let f be the Boolean OR of AND(R_l), and define

    p_l=2^(-w_l), mu=sum_l p_l, theta=2^t mu, Q=2sum_l w_l p_l.

If theta W<=1/16, then H(f)<71 I(f), regardless of maximum read, edge number, or ambient dimension. The hypothesis is physical incidence/activation data and does not use H(f) or assume FEI. It applies after a single common coordinate orientation as well. It does not cover arbitrary mixed-polarity DNFs or all dense linear hypergraphs.

### Physical residual and influence
At j let u_jl=indicator(all other points of edge l positive), for incident l, and S_j=sum_l u_jl. Let B_j be the event that a nonincident edge is true. Then d_j f=indicator(S_j>0)indicator(not B_j), r_j=d_j f-S_j. Put a_j=sum_{l containing j}2p_l and mu_non=mu-a_j/2.

Pair intersections among residual incident edges have size <=t-1, so

    C_j=E[S_j(S_j-1)]<=2^(t-1)a_j^2.

For an incident residual conjunction and a nonincident full conjunction, overlap <=t yields

    E[S_j indicator(B_j)]<=2^t a_j mu_non.

Pointwise, (S_j-d_j f)^2<=S_j(S_j-1)+S_j indicator(B_j). Consequently

    ||r_j||_2^2 <= 2^(t-1)a_j^2+2^t a_j mu_non=theta a_j.

Also indicator(S>0)>=S-S(S-1)/2 and removing B costs at most E[S indicator(B)], hence

    alpha_j=Inf_j(f)>=a_j-(1/2)C_j-E[S_j indicator(B_j)]
                         >=(1-theta)a_j.

Summing gives I>=(1-theta)Q. These estimates hold even when the lower bound is negative outside the theorem's regime.

### Ideal spectral cross mass
Every u_jl has Fourier coefficient 2p_l on each subset of R_l minus j, and zero elsewhere. Thus all ideal Fourier cross terms are nonnegative. Their total mass is C_j (by Parseval). The previous bound gives C_j<=theta a_j. The frequency-wise cross mass is retained, not replaced by an assertion of Fourier orthogonality when t>1.

### Owner assignment and rank payment
For each nonempty Fourier set A contained in one or more edges, assign all its coordinates to a single containing gate minimizing the sum of its rank/rarity costs G_jl(A). The minimizing gate is independent of j. Otherwise use any deterministic partition into incident gates and its source-component forest. Any such partition admits the original queue witness; coordinatewise rank minimization is not necessary when the rank expectation is paid directly as below.

Let Gmax=W+(6/5)log2 W <=(11/5)W. A nonempty Fourier set is good if contained in some edge, bad otherwise. At a good A all derivatives' ideal squared diagonal mass sum_l (2p_l)^2 1[A subset R_l] is the same for every j in A. The one-owner sum of G costs is at most its average over owners, using these diagonal weights. Therefore the total ideal diagonal rank bill is bounded by

    E0 Q, E0=(24/5)[log2(sqrt(2e)+2^(3/5))+log2 e]<108/5.

This uses the published signed rank/rarity piece tail, applied to each actual conjunction derivative u_jl. At bad A all ideal amplitudes vanish. Apply Lemma I with eta=1 and the assigned nonnegative G multiplier: the actual rank bill R satisfies

    R<=2E0 Q+2Gmax sum_j C_j+2Gmax sum_j ||r_j||^2
      <=[2E0+(44/5)theta W]Q.

The average-owner argument is for the SUM over j, not an unsupported coordinatewise comparison. It works for unequal gate widths because each ideal gate coefficient is 2p_l for every contained j.

### Weighted queue: labels, subsets, root normalization
Choose each root l independently with odds p_l (global lambda=1), and at a child attachment coordinate j choose gate l with probability p_l/sum_{m containing j}p_m. All other queue choices are exactly the source queue: subset weights, sizes, child counts and multisets. Root normalization is

    Lambda=sum_l log2(1+p_l)<=mu log2 e.

Dense root rarity and all subset rank terms are paid exactly as in the original forest proof. A child label costs

    log2(sum_{m containing j}p_m/p_l)<=w_l<=W,

since mu<1. A good set uses one root, zero children, and zero subset congestion, so its additional label/subset bill is ZERO (its gate identity is paid through root rarity, not omitted). A bad set's child bill is <=W|A| and its subset bill <=(6/5)|A|log2 N<=(6/5)W|A|, because mu=sum p_l>=N2^(-W) and mu<1 imply N<2^W.

For bad A, ideal S_jhat(A minus j)=0, so

    E_p[|A|indicator(bad)]<=sum_j||r_j||^2<=theta Q.

Thus L+S <=(11/5)theta W Q. This is the requested improvement of all three read sources, not just the rank term.

The completed queue/Gibbs bound is

    H(f)<=h2(v)+vLambda+K0 I+L+S+R,
    K0=120/11+3+2log2 3+log2(6e)<22.

Here h2(v)<=2I. Also v<=4mu, so vLambda<=4mu^2 log2 e<6mu^2. Q>=2mu (all edges nonempty), giving vLambda/I<3mu/(1-theta). In total,

    H/I <24+[2E0+11theta W+3mu]/(1-theta).

Since theta W<=1/16, theta<=1/16 and mu<=1/32 (t>=1), the right side is less than

    24+[216/5+11/16+3/32]*(16/15)=53185/750<71.

The final displayed rational value must be rechecked by the exact checker; the expression, rather than an unchecked decimal, governs the theorem. All root normalization is multiplied by the actual nonempty spectral mass v.

## Unbounded-read family
For any prime q>=19, points are (x,y) over F_q and gates are the q^2 nonvertical affine lines y=ax+b. Each gate has width q, any pair intersects in <=1 point, and each point belongs to q gates. Therefore max read q tends to infinity, while theta W=2q^3 2^(-q)<=1/16. The condition follows for every integer q>=18 from 2*18^3/2^18<1/16 and ((q+1)/q)^3/2<1. This is an example of the general theorem, not a repetition of the lead's projective-plane computation. The original source bound is 41+7log2 q, whereas the generic sparse-intersection theorem gives 71.

## First unsupported line
No argument establishes the complete queue payment when 2^t mu W is unbounded. In that region the ideal derivatives can have residual norm much larger than actual influence. An O(t) replacement for exponential intersection multiplicity is also unproved. The lead's PP complete proof cannot be accepted from its CLAIMS file alone: its referenced REPORT/Lemmas O and G were not persisted in the read-only lead run, although the generic interference and scalar certificates can be reconstructed independently.

## Density obstruction and a local blocking-factor repair

For m disjoint width-w clauses and a coordinate j of the first clause, let p=2^(-w), a=2p, C=indicator(all other clauses false). Then alpha_j=a(1-p)^(m-1), whereas the unconditioned ideal u_j has mass a and its residual r_j=d_jf-u_j has squared norm a[1-(1-p)^(m-1)]. Thus

    ||r_j||^2/alpha_j=(1-p)^(-(m-1))-1 -> infinity.

These are linear hypergraphs of read one, already FEI-certified by C003. Hence the raw global residual mechanism cannot prove the unrestricted target, even in an established class. It is a route obstruction, not an FEI counterexample.

There is an exact repair at the rank level for arbitrary positive AND unions. At j set V_j=union of residual supports R_l minus j of all incident gates. Let D_j be the nonincident gates disjoint from V_j, and C_j=indicator(all gates in D_j false), with c_j=E C_j>0. C_j depends only outside V_j. Let N_j be the remaining nonincident gates, mu_near_j=sum_{l in N_j}p_l. Set

    a_j=sum_incident 2p_l,
    X_j=2^(t-1)[a_j^2-sum_incident(2p_l)^2]/a_j,
    theta_j=X_j+2^t mu_near_j,
    U_jl=C_j indicator(all residual points of incident gate l positive).

For a_j=0 omit j. Let S_j=sum_l U_jl and rloc_j=d_jf-S_j. The exact local estimates are

    sum_l ||U_jl||^2=c_j a_j,
    Ccross_j=sum_{l!=m}<U_jl,U_jm><=c_j a_j X_j,
    ||rloc_j||^2<=c_j a_j theta_j,
    alpha_j>=(1-theta_j)c_j a_j.

The blocking bound uses E[C_j indicator(A_l)indicator(B_m)]<=c_j (2p_l)2^t p_m. After fixing A_l, the remaining physical input is still a product measure; C_j is decreasing and B_m increasing. Their covariance is nonpositive. This correlation fact follows by induction from the conditional covariance formula: the last one-bit covariance is p(1-p)(g_1-g_0)(h_1-h_0)<=0, and the conditional lower-dimensional covariances have the same sign. Thus this application does not rely on an unproved independence assertion under conditioning.

All U_jl share the same outside factor C_j. Their Fourier cross terms at each index are nonnegative: outside amplitude appears squared, and local positive-conjunction amplitudes have a common sign. The source rank/rarity tails still apply to U_jl because it is a signed support-subfunction of the corresponding gate derivative. For the coordinatewise minimum G_j (the original C003 assignment), Lemma I gives

    E_nu_j G_j <= [2E0+4 theta_j Gmax_j]/(1-theta_j),
    Gmax_j<=W_j+(6/5)log2 W_j<=(11/5)W_j,

where W_j is maximum incident gate width. Therefore theta_j W_j<=1/16 at every relevant j suffices for total rank/rarity R<(140/3)I<47I, regardless of GLOBAL mu. On disjoint clauses theta_j=0, the conditioned remainder is identically zero and alpha_j=c_j a_j, exactly cancelling global false-event rarity.

This local rank estimate uses coordinatewise minimizing assignment; the complete dilute theorem above uses a single whole-set owner. They cannot be interchanged without checking the label and subset bills. The first missing line for the unrestricted class is a full whole-set code paying the outside-factor spectrum and shared blocking once. The local ideal repair is a concrete next mechanism for that gap, not a completed unrestricted linear-hypergraph theorem.
