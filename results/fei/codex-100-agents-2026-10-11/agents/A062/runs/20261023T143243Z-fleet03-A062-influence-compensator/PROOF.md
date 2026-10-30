# An affinely indecomposable bounded-influence admission obstruction

All entropies and KL divergences are in bits. This concerns the ORIGINAL actual marginal-product reference, not arbitrary references and not FEI itself.

## 1. Consume the completed history mechanism

A065 stage20 PROOF sections1-2 reconstruct A087's erasure-aware identity: if G is actual global inherited KL, L is the KL to separately transported tensor factors, and d=G-L, then mean d_child=d+E_local-E_global+O_local-O_global. In particular ordinary queries that remove reference-only cells are already covered. The one-installation potential G+L pays its declared reference policy from 2A, conditional on actually supplying original capital A. We do not repeat the completed product-history search. We strengthen the remaining source-admission obstruction beyond decomposable products and beyond vanishing influence.

## 2. Explicit Boolean family and exact product estimates

For each integer m>=8 let d=2^(1-m), L=floor(1/(md)), and N=mL. Let g_m be +1 except -1 at the zero vertex on m bits. Form F_m as the disjoint product of L copies of g_m on N bits. Finally flip F_m at the single zero vertex, obtaining f_m. No search or infinite probability space defines this family.

The point spectrum is p(empty)=(1-d)^2 and p(S)=d^2 for S nonempty. Every physical influence is d. Let epsilon=2d-d^2. Then

    I(g_m)=md,
    H(g_m)=h2(epsilon)+epsilon log2(2^m-1)<=2d(2m+1),
    TC(g_m)=m h2(d)-H(g_m)>=d(m^2-5m-2).

Here h2(x)<=x log2(1/x)+a x, a=log2(e)<2, and d<=epsilon<=2d. Tensorization gives

    15/16 <= I(F_m)=Lmd <=1,
    H(F_m)<=4+2/m<=17/4,
    TC(F_m)>= (15/16)(m-5-2/m).

Indeed md<=1/16 for m>=8 and floor(t)>=t-1. Also L>=16 and N>=128.

## 3. Single-flip perturbation with explicit proved errors

Flipping one truth value changes each physical influence by at most u=2^(1-N), because only its one incident undirected edge changes pivotality. Hence |I(f_m)-I(F_m)|<=Nu. Binary entropy continuity gives

    |M(f_m)-M(F_m)|<=N h2(u)<=Nu(N-1+a),

where M is the sum of the actual marginal entropies. This continuity inequality follows by coupling two Bernoulli variables with disagreement |s-t| and using H(X)<=H(Y)+H(X|Y)<=H(Y)+h2(|s-t|), then reversing X,Y.

Parseval gives Euclidean distance 2*2^(-N/2) between the two Fourier coefficient vectors. Cauchy-Schwarz applied to squared coefficients bounds spectral total variation by eta=2^(1-N/2). Couple the two finite spectral laws maximally; conditioning on the disagreement event proves

    |H(f_m)-H(F_m)|<=h2(eta)+eta log2(2^N-1)
       <=eta(3N/2-1+a).

The last expression is a valid upper bound because the actual total variation is <=eta and h2(x)+xN increases on [0,eta] for N>=32. For every N>=32 all THREE errors above are <1/16. To verify uniformly, use a<3/2: at N=32, Nu=32*2^-31, Nu(N+1/2)=1040*2^-31, and eta(3N/2+1/2)=(97/2)*2^-15, all <1/16. Each displayed upper bound decreases with integral N>=32 (successive polynomial ratios are smaller than 2, respectively sqrt(2) for the eta bound). The inequality a<3/2 follows from ln2=2 sum_{j>=0}(1/3)^(2j+1)/(2j+1)>2/3.

It follows that

    7/8 < I(f_m) < 17/16,
    H(f_m) < 69/16 <5,
    KL(p_fm || product_i Ber(Inf_i(f_m))) = TC(f_m)
       > (15/16)(m-5-2/m)-1/8 --> infinity.

In particular its ratio to influence is unbounded as well. Its FEI ratio stays below (69/16)/(7/8)=69/14. Thus this is explicitly NOT an FEI counterexample.

## 4. No affine product decomposition or dummy direction survives

Every sign product g(x)h(y) on two nonempty disjoint coordinate blocks has an even number of negative vertices. If their negative counts are b,c and dimensions r,s>=1, the product negative count is b*2^s+c*2^r-2bc, an even integer. This also holds if a factor is constant. The original F_m has even negative count because L>=2. Its one-vertex flip has odd negative count.

An invertible affine change of the N physical binary variables is a bijection and preserves this odd count. Therefore f_m cannot be a product across ANY nontrivial coordinate partition after ANY invertible affine change. In particular it has no affine dummy coordinate. It has no constant-minus derivative direction either: anti-periodicity would force exactly 2^(N-1) negative vertices, even for N>=2. These are finite parity certificates, not computational irreducibility guesses.

It also has FULL Fourier support: multiplication by a nonconstant Walsh character toggles an even number 2^(N-1) of truth signs, preserving odd negative count. Every Walsh numerator is therefore 2 modulo4 and cannot vanish. The trivial character has the same property. Initial source-zero rows are not responsible for this obstruction.

## 5. Universal implication and first unsupported line

An original ACTUAL MARGINAL-PRODUCT KL supplier bounded by c I, or by a constant uniform over this bounded-H bounded-I class, is false on affinely indecomposable essential Boolean cores. This strengthens A065's point-tensor supplier obstruction; tensor decomposition and small source influence are not loopholes. It does not refute a different normalized original reference, an entropy-aware stopping policy that never requires that capital, or the full FEI conjecture. The first unsupported universal line is a noncircular, influence-priced ORIGINAL NONPRODUCT reference and terminal code/owner for arbitrary cores, with the signed E/O cocycle and full H retained. More paid product-history depth cannot supply this missing initial source.

The KL lower bound concerns the ORIGINAL coordinates. We do not assert that it survives every affine change of variables; an appropriately chosen affine reference remains a possible escape. Likewise, no continuity of a reference law across the point flip is assumed: each TC is formed with its OWN actual influence marginals.
