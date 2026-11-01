# Individual-core mixtures fail on two intersecting cores

All costs and entropies are in bits. For each integer r>=4, use independent physical bits z0,z1,z2 and r private width-two blocks X_j, Y_j on each side. Let

    T_r = product_j OR(z0,z1,X_j) * product_j OR(z1,z2,Y_j),
    f_r = 2T_r-1.

There are 4r+3 physical variables. The supplied clause supports have the two intersecting nonnested cores K1={z0,z1}, K2={z1,z2}. Every local support has width four. Let Q_r be EXACTLY A006's normalized actual-anchor/local-mask physical-union reference on these 2r supports, with local t=1/16, empty probability p=15/16 and probability c=1/240 for EACH nonempty local mask. Its full output mass includes all actual anchors and all compatible allocations.

Consider the ENTIRE reference class

    R = alpha Q_r + (1-alpha) nu,  0<=alpha<=1,

where nu is any probability law supported on nonempty subsets of K1 OR nonempty subsets of K2. Thus nu includes arbitrary fixed mixtures, priors and internal laws for individual-core dictionaries, including the global intersection {z1}. All choices precede the Fourier target. No branch jointly using both cores is allowed in this specified class. Then

    inf_R C_R(f_r)/I(f_r) > (2r-1)/2592 -> infinity,
    whereas H(f_r)/I(f_r) < 11.

The first infimum includes every such core law, every mixing prior and the optimal posterior over branch names, actual anchors and local-mask allocations. This refutes an individual-core augmentation of the supplied clause reference, not arbitrary representations, retuned clause laws, joint-core dictionaries or FEI. A006 normalization/disjoint payment and A008's ONE-common-coordinate repair remain true.

## 1. Exact actual Boolean spectrum and physical influence

Put A=product_j OR(X_j), B=product_j OR(Y_j), a=(3/4)^r. Distributivity gives the exact Boolean identity

    T_r = z1 OR [(z0 OR A)(z2 OR B)].

The two indicators S=z0 OR A and its independent clone have mean s=(1+a)/2. For the outer-pair Fourier set E={z0,z2}, averaging the middle bit contributes one half, while each outer coordinate has indicator coefficient magnitude (1-a)/2. The sign conversion contributes two. Therefore

    |fhat_r(E)|=(1-a)^2/4,  P_r(E)=(1-a)^4/16.       (1)

Direct pivotal counting for S gives I(2S-1)=1-a+(2r/3)a: the outer bit is pivotal when A=0; a private bit additionally needs the outer bit zero. The middle bit of f_r is pivotal with probability1-s^2. Conditional on it being zero, each S influence is gated by the other indicator's probability s. Thus

    I(f_r)=1-s^2+s[1-a+(2r/3)a]
           =5/4-a/2-3a^2/4+(r/3)a(1+a).             (2)

For r>=4, a<=81/256<1/3 and r*a<=81/64, since the adjacent ratio of r(3/4)^r is3(r+1)/(4r)<=15/16 from r=4 onward. Expanding (2) as

    5/4 + a(r/3-1/2) + a^2(r/3-3/4)

shows I>5/4; alternatively dropping its two negative terms gives I<5/4+9/16=29/16<2. Equation(1) gives P_r(E)>1/81. These are true PHYSICAL influences, not clone substitutions for the shared variables.

## 2. FULL original anchor/allocation output mass

To output exactly E, every mask in the first group must be empty or {z0}, and every mask in the second group must be empty or {z2}. Any other mask contains a forbidden physical coordinate and cannot be part of this output; unions cannot cancel it. Put b=p+c=113/120 and rho=2r*t=r/8.

For one group the unweighted mass of tuples selecting its outer coordinate is b^r-p^r. The corresponding occupation-weighted mass is r*c*b^(r-1). To select both outer coordinates, sum the occupation from either group, retaining all tuples and all active anchors. Thus

    Q_r(E)= [2r*c*b^(r-1)(b^r-p^r)]/rho
           =(1/15)b^(r-1)(b^r-p^r)
           < b^(2r-1).                              (3)

This is an EXACT full output probability, not one selected subfamily. Its numerator counts every compatible (anchor,tuple) pair once; the rho is the single original global normalizer of this new sampler. There is no root reset, missing allocation entropy or extra shuffle multiplicity.

The integer certificate 2*113^16<120^16 proves log2(120/113)>1/16, so (3) implies

    -log2 Q_r(E) > (2r-1)/16.                        (4)

## 3. Infimum over ALL individual-core repairs

E is a subset of neither K1 nor K2. Therefore EVERY admissible core law has nu(E)=0, independently of how it distributes mass within its core. Every allowed mixture obeys

    R(E)=alpha Q_r(E)<=Q_r(E).

All other nonempty output costs are nonnegative because R is a probability law. Equations(1)--(4) and I<2 give, uniformly in alpha and nu,

    C_R/I >= [P_r(E)/I] log2(1/R(E))
           > (2r-1)/(81*32)=(2r-1)/2592.

If alpha=0 the relevant cost is infinite; alpha=1 is feasible and has finite full-support cost, so the specified variational class is nonempty and meaningful. Optimizing posteriors cannot help: on each target the complete joint actual-run law gives -log R plus a nonnegative KL divergence. This identity may be expressed directly as relative entropy on countable run spaces, avoiding an undefined infinity-minus-infinity entropy subtraction. Taking the outer infimum over ALL priors/core distributions preserves the uniform strict lower bound (a uniform stronger bound is given by the exact P_r(E), I and Q_r(E), so strictness is not lost under infimum).

## 4. Direct entropy bound: not an FEI counterexample

For any indicator W of mean q on private coordinates, let nu_W be its squared Fourier spectrum normalized by q, and G=2(z OR W)-1 on an independent bit z. Expanding the two z sectors gives the exact identity

    H(G)=2q H(nu_W)+2(1-q)h2(q).                    (5)

For the indicator A above, nu_A is the product of r local distributions with probabilities3/4,1/12,1/12,1/12. Each has entropy strictly less than2, so H(nu_A)<2r. Hence for g_S=2S-1, (5) gives H(g_S)<4ra+2.

The normalized squared indicator spectrum of S has empty probability s. Its nonempty conditional entropy is the same as that of g_S; writing v_S=4s(1-s),

    H(nu_S)=h2(s)+[H(g_S)-h2(v_S)]/(4s)
            <=1+H(g_S)/(4s).

The two S factors in W=S_1*S_2 are physically independent, so nu_W=nu_S tensor nu_S and its mean is s^2. Applying (5) to the middle bit gives

    H(f_r)=4s^2 H(nu_S)+2(1-s^2)h2(s^2)
           <=6+H(g_S)<8+4ra<=209/16.

Together with I>5/4 this gives H/I<209/20<11, without assuming FEI or borrowing H to price a reference.

## 5. Exact scope and remaining universal line

The obstruction survives the variational infimum over all individual-core dictionary laws/priors, not merely a bad choice of those laws. It DOES depend on the original local width-four clause-mask probabilities being fixed, and it excludes dictionaries outputting subsets spanning both cores. JOINT_CORE_REPAIR.md proves that one fixed uniform dictionary on all three public core coordinates repairs this family at complete cost<24I. Thus the broader representation infimum containing that joint dictionary is bounded, while the individual-core-only infimum diverges. Factored core formula codes and retuned local laws are not evaluated here. The first unpaid universal line is influence payment of joint combinations of arbitrarily large intersecting cores, with their selector and allocation posteriors retained. Merely adding every individual visible core to the old sampler does not close that line.
