# A sharp Boolean exceptional-row price

The exceptional entropy row has a sharp price strictly between 2 and 9/4 times physical influence. This replaces A075's sufficient price 2/ln(2) and rational reserve 3. It reduces a supplied bank; it does not fund its initialization. Entropy is in bits.

## 1. Exact object and analytic boundary reduction

Set eta(u)=-u log2(u), with eta(0)=0, and

    L(x,y)=eta(x²)+eta(y²)-[eta((x+y)²)+eta((x-y)²)]/2.

The expression is defined on all real x,y even when a squared argument exceeds 1. It is nonnegative, even separately in x,y, symmetric, and homogeneous of degree two. Nonnegativity follows by splitting it into the nonnegative binary mixing entropy Phi(x²,y²) and the concavity gap of eta at (x+y)²,(x-y)². Homogeneity holds because all scaling-log terms cancel.

For x,y>0 away from x=y,

    partial_x partial_y L(x,y)=2 log2((x+y)/|x-y|) >=0.

Integrating in y from 0, where partial_x L(x,0)=0, proves partial_x L(x,y)>=0. The logarithmic singularity at y=x is integrable (the integral of |ln u| on (0,epsilon) is finite), and the original first derivative is continuous there because u ln|u| tends to zero. This justifies crossing that line without an unjustified derivative bound. Continuity extends coordinatewise monotonicity to both axes.

For any Boolean g and physical coordinate i, write mu=E g, t=ghat({i}), d=Inf_i(g), b=|t|. The conditional means mu+t,mu-t lie in [-1,1]; hence |mu|+b<=1. The signed Boolean derivative has absolute mean d, so b<=d. Monotonicity yields

    L(mu,t)<=L(1-b,b)=ell(b).

If b=0 the row is exactly zero, including when d>0. No division by d or b is needed on that face. For b>0 a bound ell(b)<=lambda*b implies L(mu,t)<=lambda*d. All physical Boolean biases are covered by the full real interval b in [0,1].

## 2. A unique maximum, rather than a grid

On [0,1],

    ell(b)=eta((1-b)²)+eta(b²)-eta((1-2b)²)/2.

It is symmetric about 1/2; ell(0)=ell(1)=0 and ell(1/2)=1. On (0,1/2),

    ell'(b)=4[(1-b)ln(1-b)-b ln b-(1-2b)ln(1-2b)]/ln2,
    ell''(b)=4 log2((1-2b)²/[b(1-b)]),
    ell'''(b)=-4/[ln2*b(1-b)(1-2b)]<0.

Every denominator is strictly positive on this open interval. The balanced endpoint is evaluated by continuity from the original formula, never by inserting zero into a logarithm. The second derivative has its unique zero at alpha=(1-1/sqrt(5))/2, by solving (1-2b)²=b(1-b). The derivative ell' tends to zero at both ends and is strictly positive in between: it first increases and then decreases. Thus ell increases on [0,1/2].

Define N(b)=b ell'(b)-ell(b). Then N'=b ell'', N(0+)=0 and N(1/2-)=-1. It increases strictly until alpha and decreases strictly afterwards. There is exactly one beta in (alpha,1/2) with N(beta)=0. Hence ell(b)/b has exactly one maximum on (0,1/2]. Symmetry implies ell(b)/b<=ell(1-b)/(1-b) for b>1/2; the strict global maximum is therefore

    lambda_row=ell(beta)/beta.

The continuous extension of ell(b)/b at zero is zero, since ell'(0+)=0. The value at one is zero. ROOT.json contains strict rational signs N(a)>0>N(c), isolating beta. Monotonicity of ell gives the rigorous enclosure ell(a)/c<=lambda_row<=ell(c)/a. Exact rational logarithm bounds certify 2<lambda_row<9/4. The root isolation is the only numerical component, and its signs are certified. It covers every real parameter through the preceding proof.

The coefficient is sharp for the exceptional row over actual finite Boolean functions. For every dyadic b in [0,1], take a coordinate i, set g=+1 on its positive branch, and on its negative branch set g=-1 on a fraction b of an independent finite cube. Then mu=1-b and t=d=b. Dyadic b approximate beta, so every smaller coefficient fails for some actual Boolean g. This is not a sharpness assertion about the full composition drift, whose subtracted rows may lower its optimum.

## 3. Independently reconstructed composition identity

Let F=h(g_1,...,g_r) for any Boolean gate and disjoint uniform Boolean physical cores. Keep the partition fixed, including under restrictions. Let q_j be the true pivotal probability of gate input j under the other output laws and C=H(F)-sum_j q_j H(g_j).

For a query i in block j write h=A+z_j D and take Fourier transforms of A(g_-j),D(g_-j) on the other physical blocks. Every full row with nonempty remaining block-j frequency is Dhat(W) times the corresponding g_j row. Its complete entropy decrement is L, and homogeneity plus Parseval sums its scale factors to q_j=E D². The exceptional rows are (Ahat(W)+mu Dhat(W),t Dhat(W)). The probabilities q_k for k!=j have conserved conditional mean because they are affine in the output law of g_j; q_j is unchanged. Subtracting the complete full and inner entropy decrements gives

    mean C_child-C_parent
      =q_j L(mu,t)-sum_W L(Ahat(W)+mu Dhat(W),t Dhat(W))
      <=lambda_row*q_j*Inf_i(g_j)
      =lambda_row*Inf_i(F).

This reconstructs A075-WHOLE-ROW-SIGNED-COMPOSITION-DRIFT@1 unchanged; its 2/ln2 and rational 3 conclusions remain true. The smaller coefficient here is a separate extension, not independent acceptance of our extension. Zero pivotal probability, constant cores and dummy coordinates cause no division and are included.

## 4. All real rates and supplied credits

For each fixed real K>=0 let rho_K(g) be the full finite physical stopping hull of (H(g)-K I(g))_+. For kappa=lambda_row, or the certified rational 9/4, put

    U_K=C+kappa I(F)+sum_j q_j rho_K(g_j).

Influence telescopes by Inf_i(F), so C+kappa I is superharmonic under every physical query. It vanishes at full revelation; finite backward induction gives nonnegativity. Each weighted inner hull term is superharmonic by unchanged q_j for its own query and conserved conditional mean for other queries. Finally C+sum q_j rho_K(g_j)>=H(F)-K I(F). Thus U_K is nonnegative and majorizes the full stopping payoff at every actual restriction.

Given ACTUALLY supplied credit a>=U_K(parent), choose a_b=U_K(child_b)+a-mean U_K(children). These nonnegative child credits have mean a and dominate their required banks. Nonnegative original credit labels use the kernel a_b/a when a>0, with the zero case handled directly. The nonnegative booked debit is d_b=K I(F_b)-H(F_b)+a_b (this sign is essential). Old signed debit labels and the new query charge have total T=mean d_b; for T>0 use kernel d_b/T, otherwise retain cancelling signed labels with kernel 1. Both full children and old stopped siblings remain present. No original owner is charged twice.

Against the source rational-3 envelope, the new rational envelope is smaller by exactly (3/4)I(F) at every state; its conditional mean release is (3/4)Inf_i(F). This is a reduction in required headroom. It is not new income from a spent owner. The sharp scalar coefficient is smaller still. All real surplus credits D>=0 are covered by adding the same D to child credits; no bias grid or credit grid is used.

## 5. The remaining initial-price obstruction

Since H is a nonnegative superharmonic majorant of the payoff, 0<=rho_K(g)<=H(g). Also rho_K(g)>=H(g)-K I(g), so sigma=H-rho_K lies in [0,K I]. Exactly as in A089's all-partition diagnosis,

    U_K=H(F)+kappa I(F)-sum_j q_j sigma(g_j),
    H(F)+(kappa-K)I(F)<=U_K<=H(F)+kappa I(F).

This holds for every fixed disjoint partition, even one selected separately for each F. Consequently, at fixed K and kappa, a dimension-independent influence price for U_K is equivalent to full FEI. The constant reduction above does not establish that initial price. Full FEI remains OPEN. The next unpaid line is an ORIGINAL unused O(I) source for an arbitrary indecomposable core, or a well-founded source-price descent that genuinely avoids this sandwich.
