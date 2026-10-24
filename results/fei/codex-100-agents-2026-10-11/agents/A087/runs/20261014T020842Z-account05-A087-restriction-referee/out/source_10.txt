# Point-selector full stopping payment and shared-bit priority ownership

All entropy is in bits, eta(t)=t log2(1/t), eta(0)=0. Fourier normalization is uniform Parseval. Let g,h be Boolean signs on disjoint cubes, and let A be the indicator of one specified point on r fresh bits, r>=1, p=2^-r. Write mu=Eg, nu=Eh, Vg=1-mu^2, Vh=1-nu^2, t=mu-nu, m=p mu+(1-p)nu, d=(1-mu nu)/2. Define F=A g+(1-A)h. The tree queries just enough selector bits to determine A, stopping at g or h. Its actual entropy payment and influence payment are

    Pi=H(F)-p H(g)-(1-p)H(h), Q=2rp d,
    I(F)=Q+p I(g)+(1-p)I(h).

The first equality denotes the summed signed entropy increments of the physical stopping tree, not a sum of positive parts or a mismatch-KL upper bill. The second follows from selector boundary edges: the sign selector 1-2A has influence 2rp and independent children disagree with probability d. Expected terminal weights are p and 1-p. These identities remain valid for constants and d=0.

## Exact coherent spectrum and entropy

At a nonempty g-only data frequency, the empty selector coefficient is p ghat and every nonempty selector coefficient has magnitude p|ghat|. At an h-only frequency they are (1-p)hhat and p|hhat| respectively. There are 1/p-1 nonempty selector sets. Mixed private frequencies are zero. At empty data frequency, the empty selector coefficient is m and every nonempty selector coefficient has magnitude p|t|. Grouping eta terms, with no discarded empty row, gives

    Pi = 2rp [Vg+(1-p)Vh+(1-p)t^2]
       + Vh eta((1-p)^2)
       + eta(m^2)-p eta(mu^2)-(1-p)eta(nu^2)
       + p(1-p)t^2 log2(1/t^2).

The last term is zero at t=0. Thus Pi depends only on the two biases and the selector width, although all child entropies are retained. This is the block cost of the physical early-stopping tree, independent of the order of its point-test bits.

## Width-dependent upper bound

Put b=log2(e). The following elementary facts hold on [-1,1]:

    Vg+Vh+t^2=4d; |t|<=2d;
    eta((1-p)^2)<=2bp(1-p).

The absolute-value inequality follows from 1-mu nu >= |mu-nu|, equivalently (1-mu)(1+nu)>=0 or (1+mu)(1-nu)>=0. The eta bound follows from -(1-p)ln(1-p)<=p.

Let psi(x)=eta(x^2). For x nonzero, psi''(x)=-4 log2|x|-6b>=-6b. The derivative extends continuously at zero, so psi(x)+3b x^2 is convex on the entire interval. Jensen therefore gives

    psi(m)-p psi(mu)-(1-p)psi(nu)<=3b p(1-p)t^2.

Also, for 0<|t|<=1,

    t^2 log2(1/t^2)=|t| [2|t| log2(1/|t|)]
                         <=(2b/e)|t| <=(4b/e)d.

For |t|>1 the left side is negative and the same upper bound is valid. Maximizing x ln(1/x) proves the displayed scalar maximum 1/e. Combine the eta and Jensen terms as

    bp(1-p)[2Vh+3t^2] <=3bp(Vh+t^2)<=12bp d.

The leading term is at most 8rp d. Hence for every r>=1,

    Pi <= [4+(6b+2b/e)/r] Q.

For r>=2 this is at most [4+3b+b/e]Q <(71/8)Q. The final rational certificate uses b<13/9 and 1/e<3/8: ln2 >= 2/3+2/81+2/1215=842/1215>9/13, and e>1+1+1/2+1/6=8/3. Thus 4+3b+b/e<4+13/3+13/24=71/8. No floating-point constant comparison is needed.

## One-bit endpoint, independently reconstructed from A012

For r=1, the exact formula is Pi=Vg+Vh+E+J, where M=(mu^2+nu^2)/2, U=(mu+nu)^2/4, W=(mu-nu)^2/4,

    E=M h2(W/M),
    J=eta(M)-[eta(mu^2)+eta(nu^2)]/2.

All zero endpoints are continuous. The inequality h2(x)<=2sqrt(x(1-x)) gives E<=|mu^2-nu^2|/2. To check this scalar premise, the second derivative of 2sqrt(x(1-x))-h2(x) has one sign change on (0,1/2); its derivative starts positive, ends at zero from below, and its endpoint values are zero. Symmetry then proves nonnegativity.

For J, set s=|mu|, u=|nu|. The inequality

    [(1+x)ln(1+x)+(1-x)ln(1-x)]/2 <= 1-sqrt(1-x^2)

follows because the derivative difference is x/sqrt(1-x^2)-atanh(x), whose derivative is nonnegative on [0,1). Substitute x=(s^2-u^2)/(s^2+u^2). This proves J<=b(s-u)^2/2.

If mu nu>=0, Vg+Vh<=4d, |s^2-u^2|/2<=2d, and (s-u)^2<=2d. The last two inequalities follow by maximizing the corresponding convex quadratics on the unit square, or directly factoring endpoint expressions. Therefore Pi<=(6+b)d. If mu nu<0, E<=M and J<=M, while Vg+Vh=2-2M, so Pi<=2<=4d. If d=0 the functions are equal constants and Pi=0. Since Q=d when r=1, the one-bit bound is <(67/9)Q, hence below 71Q/8. This reconstructs only A012's disjoint-private entropy mux subclaim; no blanket reference or grammar review is claimed.

Consequently every point-selector block satisfies Pi<=(71/8)Q<9Q when Q>0. Supplying H(g)<=L_g I(g), H(h)<=L_h I(h) pays the complete path plus terminal allowance at rate max(71/8,L_g,L_h). Arbitrary cores without terminal certificates retain their full weighted entropies.

## Optional complete spectral reference for the selector block

There is also a compatible normalized output reference, without keeping the physical transcript. Given normalized core references positive on target support, first calibrate their empty masses to mu^2,nu^2, preserving conditional nonempty laws. KL disintegration shows this lowers terminal CE. Denote the calibrated references by Rg,Rh. Give the empty data row its TRUE masses m^2 at empty selector and p^2t^2 at every nonempty selector. For a g-only nonempty data frequency T give every selector sector p^2 Rg(T). For an h-only nonempty frequency give empty selector (1-p)^2 Rh(T) and each nonempty selector p^2 Rh(T). Mixed private frequencies have zero mass. These are a single reference, fixed from the instance before spectral sampling.

Total mass is pVg+(1-p)Vh+m^2+p(1-p)t^2=1. Sectorwise probability ratios show exactly

    D(P_F||R_F)=p D(P_g||Rg)+(1-p)D(P_h||Rh),
    CE_F=p CE_g_cal+(1-p)CE_h_cal+Pi.

This is the rare-point-selector extension of A012's one-bit calibrated construction. It proves the same 71/8 selector overhead for complete ideal spectral references with terminal reference deficits retained. It does not pay integer prefix rounding or transcript decoding. The algebra here is analytic; the executed finite job checks the true-spectrum entropy specialization, not arbitrary supplied reference laws. No extra reference enumeration was run.

## Same-orientation priority pair sharing one physical control bit

Let z be fresh, A and B be point indicators on r and s disjoint private control cubes, and g,h have disjoint private data cubes, independent also of all controls. When z is favorable, output g if A, else h if B, else +1; when z is unfavorable output +1. Thus

    H_B=1+B(h-1), T=A g+(1-A)H_B, F=1+1_{z favorable}(T-1).

This is the first-event-priority convention. It differs from multiplying two potentially simultaneous core activations. Put p=2^-r, q=2^-s, a=1-mu, c=1-nu. Terminal weights are wg=p/2, wh=(1-p)q/2. The physical tree queries z once, then A, then B only after A fails. Its disjoint physical influence accounts are

    Qz=[p a+(1-p)q c]/2,
    QA=rp[1-mu(1-q c)], QB=sq c,
    Qctrl=Qz+QA/2+(1-p)QB/2,
    I(F)=Qctrl+wg I(g)+wh I(h).

Equivalently,

    Qctrl=N+p q c(r mu-s-1)/2,
    N=(r+1)p a/2+(s+1)q c/2.

This independently matches A091's signed same-orientation ownership correction. The correction can have either sign; nominal event budgets N are not used as the funding account.

The actual full tree entropy bill is

    H(F)-wg H(g)-wh H(h)
      = [H(F)-H(T)/2]
        +[H(T)-p H(g)-(1-p)H(H_B)]/2
        +(1-p)[H(H_B)-q H(h)]/2.

The first and last terms have rate6 by A028 v2 point-activation transport. The middle is the new point-selector block with disjoint children g and H_B, rate71/8. Therefore

    H(F)-wg H(g)-wh H(h) <= (71/8)Qctrl.

With any explicitly certified terminal FEI constants Lg,Lh, the FULL expected signed path cost plus weighted terminal allowance is <=max(71/8,Lg,Lh)I(F). This pays the one shared control bit exactly once. It works for arbitrary widths and all biases. For r or s=0, eliminate that constant selector; remaining activation cases are already covered at rate6.

## Honest boundary

This is an actual entropy partition bill. It does not pay sums of clipped positive increments, mismatch-KL plus linear upper charges, physical transcript entropy, or C020 reference coding without further proof. Disjoint private data is essential: for overlapping cores Pr(g!=h) need not equal (1-mu nu)/2 and nonempty rows can collide. The first unsupported extension is a uniform point-selector Pi<=K*2rp*Pr(g!=h) with shared data and terminal costs retained. Arbitrary selector substitution is also unpaid; choosing opposite constant children recovers the selector's FEI question. The universal stopping/admission and full FEI remain open.
