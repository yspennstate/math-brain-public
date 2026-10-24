# Physical restriction of information projections

All entropies use bits. f is a Boolean sign on a finite uniform cube. Fix one physical coordinate i, write a_T=fhat(T), b_T=fhat(T+i), q_T=a_T^2+b_T^2, and p_y(T)=(a_T+y b_T)^2 for y=+-1. Each child is normalized and (p_++p_-)/2=q. All zeros are interpreted on their actual supports.

Let d_j=Inf_j(f), d_j^y=Inf_j(f_y), B=H_P(S_i|S_-i), J=H(q)-(H(p_+)+H(p_-))/2, D_H=H(f)-E_y H(f_y)=B+J, and
G=sum_{j!=i}[h2(d_j)-E_y h2(d_j^y)]. Each summand is nonnegative because d_j=E_y d_j^y. Let K(f)=D(P_f||product_j Bern(d_j))=sum_j h2(d_j)-H(f).

## Exact product projection balance

Subtract the entropy formulas directly, retaining the actual signed children:

    E_y K(f_y)-K(f) = B+J-h2(d_i)-G.                    (1)

Equivalently K(f)-E K(f_y)+D_H=h2(d_i)+G. This is a compensated identity, not monotonicity. Erasing i first gives K(q)=K(f)-h2(d_i)+B. The common fixed residual product reference R has the parent residual marginals, so

    E D(p_y||R)=K(q)+J,
    E D(p_y||R_y)=E D(p_y||R)-G,                      (2)

where R_y is the newly optimized child product. The last equality follows by expanding log(R_y/R): its expectation is exactly the sum of marginal KLs E sum_j D(Bern(d_j^y)||Bern(d_j))=G. Thus G is the exact reset saving in the fixed-reference comparison; it is not a free additional entropy rebate.

In the B08 lead's notation, Gamma_i=G and I_h=I_P(S_i;S_-i)=h2(d_i)-B, so (1) reads TC(f)=I_h-JS_i+Gamma_i+E TC(f_y). For an adaptive finite fair tree this telescopes exactly to sum_h w_h I_h+sum_h w_h Gamma_h+E_leaf TC=TC(root)+sum_h w_h JS_h. TC does not have to decrease at each node. If the two child squared spectra agree, then JS_i=Gamma_i=0 and TC(f)-TC(child)=I_h>=0. Conversely JS_i=0 forces equal child spectra by the equality case in Gibbs, and hence Gamma_i=0. This is the exact isospectral equality interface; TC itself is constant only if I_h also vanishes.

## Bayes-compatible reference transport

On q_T>0 use the function-specific kernel k(y|T)=p_y(T)/(2q_T); extend it by k=1/2 on q_T=0. Apply this SAME kernel to q and R. Under P the outcome Y is fair. Let Q_Y be its reference outcome law and Q_y the Bayes-predicted residual reference. D_out=D(Bern(1/2)||Q_Y) and delta_y=E_{p_y}log2(Q_y/R_y). The KL chain rule with a common kernel proves

    K(q)=D_out+E D(p_y||Q_y),
    E delta_y = D_out+J-G.                           (3)

This supplies the explicit signed reset term in A037's ledger, with zero channel injection. Terms supported only under Q are handled by the declared zero-fiber extension. Reference probabilities on P-supported atoms remain positive after deterministic marginal coordinates are removed. Arbitrary extensions affect D_out and delta separately but not their difference J-G. No phase-blind spectral channel is claimed.

## Occupancy projection and the second reset

For v=P_f(S!=empty)>0, let r_j=d_j/v and let Q_r maximize entropy on nonempty subsets with marginals r. Set M(empty)=1-v and M(S)=v Q_r(S). Let E(f)=H(M)=h2(v)+v Hmax(r), A(f)=v K_occ(f)=E(f)-H(f), and Delta(f)=sum_j h2(d_j)-E(f). Constants have A=Delta=E=0. Then

    K=A+Delta,
    E_y A(f_y)-A(f)=D_H+E_y E(f_y)-E(f),
    E_y Delta(f_y)-Delta(f)=-h2(d_i)-G-[E_y E(f_y)-E(f)]. (4)

For interior feasible r with sum r>1, c is the unique positive solution 1-c=product_j(1-c r_j), theta_j=c r_j, and

    Hmax(r)=log2(c)-sum_j[r_j log2(theta_j)+(1-r_j)log2(1-theta_j)].

This is proved by conditioning independent Bernoulli(theta_j) on nonempty and observing that log Q_r is affine in the indicators. Gibbs proves maximality. If sum r=1 the law is the uniquely determined singleton law; forced-one coordinates use c=1 and forced-zero coordinates are omitted. This also independently reconstructs A038's normalization identity: log(M/R) is affine on the nonempty support and fixed on the empty atom, so D(P||R)=D(P||M)+D(M||R).

## Both signs occur, even for actual Boolean functions

For f(x)=(-1)^{sum_{a<b} x_a x_b} on four binary coordinates, the alternating adjacency matrix of K4 is nonsingular over F2. Translation orthogonality, or a direct sixteen-value Walsh transform, gives all sixteen squared Fourier coefficients 1/16. Thus K(f)=K_occ(f)=Delta(f)=0. Restrict any coordinate. Each triangle quadratic child has four squared coefficients 1/4, on an odd or even parity class of the three residual coordinates, and every residual marginal is 1/2. Consequently K(f_y)=1 for BOTH children: E Kchild-Kparent=1. For the odd child v=1 and H=2. The uniform law on the six sets of size one or two has marginals 1/2 and entropy log2(6)>2, so K_occ(odd child)>=log2(3/2)>0. Occupancy credit therefore also increases from zero. No use of numerical roots is needed for these strict signs.

Conversely the three-bit point defect f=1-2*1_{x=0} has K=2-(9/8)log2(3)>0, since 3^9<2^16. Its two children are a constant and a two-bit point defect, both with K=0. Hence neither direction of unconditional product-KL monotonicity holds. Delta also increases from zero on the K4 example: for the odd child the unconstrained product at marginals 1/2 places positive mass on empty, and strict entropy maximality on the full cube implies Hmax(r)<3, so Delta=3-Hmax(r)>0; the other child has Delta>=0.

The three-bit triangle quadratic itself supplies the opposite sign for BOTH occupancy KL and Delta. Its nonempty odd-parity law has K_occ>=log2(3/2)>0 and Delta=3-Hmax(1/2,1/2,1/2)>0. Restricting any coordinate leaves a two-bit bent law, uniform on all four subsets. Its conditional nonempty law is uniform on the three nonempty subsets and equals its own maximum-entropy projection; thus both child K_occ and child Delta vanish. These counterexamples prove the absence of either monotonic direction for all three accounts.

## All-dimensional local correction obstruction

For the m-bit point defect, m>=3, put a=2^(1-m). All coordinate influences equal a, P(empty)=(1-a)^2, and P(nonempty S)=a^2. The conditional nonempty law is uniform, so K_occ=0 and Delta=K exactly. Querying any coordinate produces a constant child and the (m-1)-bit point defect, with active probability 1/2. From (1),

    Delta_m-(1/2)Delta_{m-1}
      =h2(a)+(m-1)[h2(a)-(1/2)h2(2a)]-[H_m-(1/2)H_{m-1}]. (5)

The exact entropy is H_m=-2(1-a)^2 log2(1-a)+2a(2-a)(m-1). Elementary Taylor expansions with remainder O(a^2) give

    H_m-(1/2)H_{m-1}=4a+O(m a^2),
    [Delta_m-(1/2)Delta_{m-1}]/a
       =2m-6+log2(e)+O(m a) -> infinity.             (6)

Thus no finite C bounds the absolute expected single-step Delta change by C times physically removed influence. This is a reference-transfer obstruction, not a FEI counterexample. In the Bayes ledger, delta_bar-D_out=J-G and G/a=(m-1)+O(m a); the mutual information J<=D_H=O(a), so the signed combination (delta_bar-D_out)/a also tends to minus infinity. A corrected ledger must carry these state-dependent terms; an O(Inf_i) replacement is impossible.

Here the asymptotic has an explicit error certificate. For 0<a<=1/2, the series -(1-a)ln(1-a)=a-sum_{l>=2}a^l/[l(l-1)] gives |h2(a)-a(log2(1/a)+log2(e))|<=a^2/ln2. Also | -2(1-a)^2 log2(1-a)-2a/ln2 |<=4a^2/ln2. Apply these at a and 2a (m>=3). The resulting remainder in (6) is at most [6m-4+(3m+10)/ln2]a <=(12m+16)a, using ln2>1/2. This proves the all-m divergence with a proved error, independently of finite numerical enclosures.

The late-arriving B08 lead asks whether Gamma_i<=c Inf_i or Gamma_i<=c(JS_i+Inf_i) can hold for a finite universal c. Both are refuted by this SAME physical point-defect split: Gamma_i/a=(m-1)+O(m a), with an explicit error <=3(m-1)a/ln2; JS_i<=D_H and D_H/a<=4+(6m+20)a. Thus Gamma_i/(JS_i+Inf_i)>=[(m-1)-6(m-1)a]/[5+(6m+20)a] tends to infinity. This is a nonlocal reference-reset obstruction, not a repetition of the previously refuted variance-refund helper. All coordinates of this family have the same obstruction, so existential coordinate selection does not save either Gamma helper. The true entropy decrement remains O(Inf_i) on this family.

## Sparse activated bent-defect application

Let k>=4 be even, delta=2^-k, b(x)=(-1)^{x1x2+...+x(k-1)xk}, b'=b-2*1_{x=0}. Let j(y,x) choose b,b' fairly, and put F_r(z,y,x)=1+1_{z=0}(j-1), p=2^-r. Its mean m=2^(-k/2)-delta. Its core influences are alpha_data=1/2+delta and alpha_selector=delta. Its control influences are p(1-m). For either selector-first child replace the core with b or b': means 2^(-k/2), 2^(-k/2)-2delta, and data influences 1/2, 1/2+2delta.

For any of these cores g with mean m and influence vector alpha, the activated state has

    v=1-[1-p(1-m)]^2,
    d_data=p alpha, d_control=p(1-m),
    H=eta([1-p(1-m)]^2)+(2^r-1)eta(p^2(1-m)^2)
         +2^r sum_{T!=empty} eta(p^2 ghat(T)^2),

where eta(t)=-t log2 t. These exact rational spectral classes and the above positive-root formula compute E, A and Delta without enumerating the control cube. Control-first steps have a constant inactive child and F_{r-1} as active child. Selector-first steps have activated b,b' children. Equations (1)-(4) therefore give both complete signed transfer ledgers. Weighted control-first sums telescope to the retained terminal core quantities, with visit weight 2^-t at depth t; the selector query is charged only once on surviving paths. Computation validates these identities and encloses actual Delta transfers, but does not prove a new uniform influence bound for arbitrary witness generators.

First unsupported universal line: bounding the complete residual erasure/terminal cost after the signed Delta and Bayes reset transfers, without importing a new root reference budget or paying the same child slack twice. Algebraic compensation and projection optimality alone do not supply that bound.
