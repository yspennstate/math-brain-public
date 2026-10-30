# Independent reconstruction of the selected deep physical policy

The A061 deep-policy theorem holds at its stated scope. The source is the A061 run dated 2026-10-27 04:47:53Z, PROOF sections 1--5 and 8, claim A061-DEEP-SELECTED-DATA-RESET-SHARP-SQRT-BOUNDARY@1. This is an independent analytic reconstruction, with separate finite validation. It is not a proof of full FEI and is not Lean-checked.

1. All cubes and trees are finite, outputs are signs, and units are bits. Put d_s=2^(1-s), p_s=1-2 1_{0^s}, h_s=H(p_s), b_s=s h2(d_s). For s=1 both entropies vanish. Direct characters give squared mass (1-d_s)^2 at the empty set and d_s^2 at each nonempty set. Every physical coordinate has influence d_s; its two children, each of physical probability 1/2, are a constant and p_(s-1), up to a translation or sign. Every reached history is a cylinder, so another block's adaptive query order does not alter these conditional probabilities.

2. Fix 1<=r<=m. A live block is queried until it dies or has r coordinates left; only at that boundary may its exact reference be installed as its coordinate-marginal product, after which that block is frozen. Before installation its full cross entropy is h_s; afterward its full cross entropy is b_r, with H=h_r and KL=b_r-h_r separately retained. A deterministic spectral marginal is a point mass. No 0/0 expression or discarded reference row is required.

The local potential is v_s=max(h_s,2^(r-s)b_r), with dead potential zero and installed potential b_r. For a general Boolean physical query, grouping its Fourier coefficients as a_T,b_T gives normalized child laws (a_T+b_T)^2 and (a_T-b_T)^2. Their average is a_T^2+b_T^2. Entropy concavity and the chain rule therefore give h_s>=h_(s-1)/2. For s>r,

    E[v_child | past] = max(h_(s-1)/2,2^(r-s)b_r) <= v_s.

The maximum is taken inside the conditional expectation through the actual two-child expression; it is not moved past a general random variable. At installation subadditivity gives b_r>=h_r and the potential stays b_r. Thus it dominates the complete current cross entropy at every declared node.

3. The tensor reference comprises exact spectra on live factors, installed full marginal products on frozen factors, and deterministic atoms on dead factors. An actual query acts only on an exact-reference factor. Coherent transport of the exact source predicts both physical outcomes with probability 1/2 and yields the actual child spectrum. The other tensor factors and all their reference atoms remain. Consequently actual outcome KL is zero, including after installations in other blocks. This argument would not justify querying a frozen factor; that action is excluded.

Add the local potentials. It is a nonnegative supermartingale for every predictable interleaving and every finite stopping cut. Summing conditional drops proves the stopped expected full cross entropy bound directly, without any unbounded stopping or limit exchange. A consumed old debit is not part of the remaining potential; funding requires S-old_debit at least the initial potential.

4. For N=2^(m-1) identical blocks, g_m=product p_m, I(g_m)=m and H(g_m)=N h_m. The root sum is

    N max(h_m,2^(r-m)b_r) = max(H(g_m),K_r),
    K_r=2^(r-1)b_r=r h2(d_r)/d_r.

Immediate stopping demands H(g_m). Completion of all declared blocks demands K_r: each survives with probability 2^(r-m), irrespective of interleaving, and the expected completed H and KL are respectively N 2^(r-m)h_r and N 2^(r-m)(b_r-h_r). These two lower bounds match the supermartingale upper bound. This proves exact least expected capital for EVERY adapted cut in the declared class, rather than only for the last cut. The equality pulling N through the maximum uses identical block parameters. Heterogeneous blocks require the sum of their separate maxima and cannot silently use just a maximum of two total endpoints.

For the bent-mask source (-1)^(uv)g_m, a first v query releases two entropy bits and leaves g_m or its u-character multiple with the same data law. Exact capital is max(H(g_m)+2,K_r). Both physical children have the same complete cost. The extra character is retained, with zero entropy and no promised new source.

5. For rare activation Z=1+A_t(g_m-1), let delta=2^-t and mu=Eg_m=(1-d_m)^N, a=1-mu. Query activation controls before any data. The inactive child is an actual constant and the active child is the same activated source with one fewer control. At l remaining controls use

    w_l=max(H(Z_l),2^-l max(H(g_m),K_r)).

Entropy concavity again gives H(Z_l)>=H(Z_(l-1))/2. Hence w_l dominates its expected successor and joins the block potential at l=0. The exact least root cost is max(H(Z),delta K_r), by immediate stopping and completion. Nonconstant active terminals retain H and KL. The entropy floor cannot be erased by taking Q=P.

Direct Fourier coefficients are 1-delta a at the empty set, -delta a for nonempty pure-control sets, and delta ghat(S) for every nonempty data set and every control set. Since 0<a<1 and every point_m coefficient is nonzero for m>=2, the support is full. Each data influence is positive and each control influence is delta a, giving I(Z)=delta(m+ta). In a putative nontrivial disjoint sign-product factorization, setting any control inactive makes Z constant; the factor without that control would have to be constant on all its coordinates. Relevance of every coordinate rules this out. This proves physical tensor indecomposability; it says nothing about general affine factorizations.

6. Write phi(x)=-x log2 x and A(x)=-2(1-x)^2 log2(1-x), continuously at endpoints. Summing the three spectral sectors gives exactly

    H(Z)=A(delta a)+delta H(g_m)-delta phi(mu^2)
         +2t delta(1-mu^2)+(2^t-1)phi(delta^2 a^2).

Since 1-mu^2+a^2=2a, dropping only negative terms yields

    H(Z)<=delta H(g_m)+4t delta a
          +2delta a^2 log2(1/a)+A(delta a).

The elementary bound -ln(1-x)<=x/(1-x), with continuous endpoints separately treated, gives A(x)<=2x/ln2. Also -a ln a<=1. For points H(g_m)<=4m: the nonempty sector contributes 2(m-1)(2d_m-d_m^2), and A(d_m)<3d_m, using ln2>2/3. Thus H(Z)<=4I(Z)+4delta a/ln2<4I(Z)+6delta a<=7I(Z), because m>=2 and a<1. No denominator vanishes in this argument: activation has delta a in (0,1), and the r=1 endpoint is evaluated directly.

7. Binary entropy gives r(r-1)<=K_r<=r(r-1+1/ln2)<r(r+1/2). Thus if r<=floor(sqrt(m)), delta K_r<2delta m<=2I(Z). ONE original S=8I(Z), after an arbitrary already-consumed debit at most I(Z), covers the exact capital <=7I(Z). It does not issue fresh influence credit at descendants. For t<=beta m, the lower ratio delta K_r/I(Z)>=r(r-1)/((1+beta)m) and the upper bounds prove capital=O(I) if and only if r=O(sqrt(m)). Without bounded t/m this necessity does not follow; the source does not assert it.

8. The proof uses every substantive admission: fixed r boundary, frozen installed factors, controls first, literal disjoint point factors, exact initial references, finite fair predictable trees, explicit entropy source price, and the old-debit bound. Removing any of these needs a new argument. In particular, immediate root stopping already costs H(g) for an arbitrary replacement core g, so the potential construction alone cannot influence-price that core without solving an FEI-strength problem. The earlier ALL-product-stop obstruction remains intact: resetting at r=m costs K_m of quadratic order, while this selected rule reaches r of square-root order.

No unsupported line remains in this scoped reconstruction. The first unpaid universal line is an ORIGINAL O(I) source, or a useful entropy-decaying compatible selected policy, for arbitrary indecomposable Boolean cores, retaining old bills, actual physical-query KL and BOTH full terminal terms. Independent full-chain review is assigned to A094; A061/A064/A065 are the immediate consumers.

9. An exact heterogeneous-cut guard uses the actual source p4(x)p3(y), with common boundary r=3. Its immediate full bill is h4+h3. Completing both blocks gives expected bill (3/2)b3: the four-bit block survives to three bits with probability 1/2, and the three-bit block installs immediately. Instead install only the three-bit block and stop, retaining the untouched four-bit factor. This actual intermediate bill is h4+b3. Here

    h3=4-(9/8)log2(3), b3=6-(9/4)log2(3),
    h4=45/32+(49/64)log2(64/49).

The intermediate-minus-root gap b3-h3=2-(9/8)log2(3)>1/5 follows from 3^5=243<256=2^8. Also 3^9=19683>16384=2^14 implies b3<5/2, while 64^4>2*49^4 implies h4>409/256. Therefore the intermediate-minus-completed gap h4-b3/2>89/256>1/5. These are exact integer sign certificates. Both actual children of a subsequent first-block query carry the same frozen three-bit product reference and its full KL; the independent full-atom checker verifies that transport as well. This guard rules out the heterogeneous endpoint-max extrapolation, not A061's identical-block formula. Its independent review is pending.
