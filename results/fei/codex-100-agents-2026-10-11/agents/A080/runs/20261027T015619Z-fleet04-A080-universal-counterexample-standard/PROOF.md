# Arbitrary Boolean spectra survive composition-prime perturbation

Work in bits 0,1 with signs in {-1,+1}; all physical bits are uniform. H is Shannon entropy in bits of the complete squared normalized Fourier law; I is total physical influence. A composition-prime function has, for every block A with 2<=|A|<=N-1, at least three distinct rows in its A versus complement truth matrix. Thus no proper nonsingleton block can be replaced by one Boolean summary, even with all outside coordinates raw.

## Exact construction and three-row proof

Given ANY Boolean seed g on n bits and k>=2 fresh bits, with N=n+k>=3 z, put N=n+k and

    F(x,z)=g(x) b_N(x,z),  b_N=-1 on the Hamming ball of radius one about zero, +1 elsewhere.

Only N+1 physical inputs are changed. Fix a proper block A of size at least two and its nonempty complement B. If A contains two fresh bits, take A assignments of weights zero, one, two using only these fresh bits, with all original A bits zero. The seed row on B is identical in all three cases. The ball multiplier rows are negative respectively on B weights <=1, on B=0, and nowhere. They are three distinct rows for EVERY nonempty B, including |B|=1.

If B contains at least two fresh bits, the following second argument applies. Choose A assignments of weights zero, one and two. Fix all original B bits at zero and vary only its fresh bits. The seed values on these restricted rows are arbitrary scalar signs. The three multiplier rows are the radius-one ball, the point defect, and the constant row on at least two bits. They are pairwise unequal even up to a global sign: radius-one and point rows agree at zero and differ at weight one; the ball has both signs because weight two exists; the point has both signs. Therefore multiplying by arbitrary scalar signs still leaves three distinct restricted rows, hence three distinct full rows. The only remaining case has k=2 with one fresh bit in each block. A contains an original coordinate i. Fix every other coordinate at zero and use its fresh bit a for four A rows (i,a)=00,01,10,11. In the two columns given by the fresh bit of B, these rows are s0(-1,-1), s0(-1,+1), s1(-1,+1), s1(+1,+1), where s0,s1 are the corresponding seed signs. If s0=s1 the two constant rows and a mixed row are distinct. If s0=-s1 the two middle mixed rows and a constant row are distinct. These are all possibilities. This proves composition-primality for every seed, with no assumption on its own decomposition or coordinate relevance. Every coordinate of F is relevant: an irrelevant coordinate would allow a two-coordinate block containing it to have at most two rows, contradicting the conclusion (N>=3).

A block admits a scalar Boolean summary if and only if its truth matrix has at most two distinct rows. Necessity is pigeonhole; sufficiency labels its row types by two signs. In any disjoint single-output Boolean-core representation on proper physical blocks, every block of F must consequently be a singleton.

## Uniform perturbation estimates

For arbitrary Boolean f,h differing on physical probability epsilon in dimension N, Parseval gives ||fhat-hhat||_2=2 sqrt(epsilon). Cauchy-Schwarz gives total variation d of their squared Fourier laws at most 2 sqrt(epsilon), since ||fhat+hhat||_2<=2. The probability coupling that matches the common masses has mismatch probability d. Conditional on a mismatch there are at most 2^N-1 possible alternate atoms, so the entropy chain rule in both directions gives

    |H(f)-H(h)| <= h2(d)+d log2(2^N-1) <= h2(d)+Nd.

This is proved for finite laws and needs no limiting interchange. For each physical coordinate an edge can change its disagreement status only if one endpoint lies in the edit set. Hence |Inf_i(f)-Inf_i(h)|<=2 epsilon and |I(f)-I(h)|<=2N epsilon. No new variable is omitted.

For the construction, epsilon=(N+1)2^-N, h is g padded by spectators, and H(h)=H(g), I(h)=I(g). For N>=6, N+1<=2^(N/2): it holds at N=6 and the consecutive ratio (N+2)/(N+1)<=8/7<sqrt(2) proves induction. Therefore d<=delta=2^(1-N/4). Choose n>=1,m>=1 and N=8(n+m+2). Then delta<=1/2. Since -(1-t)ln(1-t)<=t and ln2>=1/2 (integrate 1/u on [1,2]), h2(delta)<=delta log2(1/delta)+2delta. Thus monotonicity of h2(t)+Nt for t<=1/2 yields

    |H(F)-H(g)| <= 2N delta =4N 2^(-N/4).

The same bound controls |I(F)-I(g)|, since epsilon<=delta. A nonconstant n-bit seed has a disagreeing edge, whence I(g)>=2^(1-n). Write s=n+m>=2. Division by I(g) bounds either error by

    2N 2^(n-N/4)=16(s+2)2^(-n-2m-4) <=2^-m,

because s+2<=2^s for integers s>=2 (equality at two; induction). Thus

    R(F) >= (R(g)-2^-m)/(1+2^-m),  R=H/I.

If the lower-bound numerator is negative the ratio inequality follows from R(F)>=0; otherwise division uses I(F)<=I(g)(1+2^-m) with nonnegative numerator. F is an actual finite Boolean function, not an abstract spectral law. The construction depends on the seed dimension and the requested accuracy index m; this dependency is explicit and permitted. For a fixed seed, the entropy and influence errors tend to zero as m grows and I(g)>0, so R(F)->R(g). For a hypothetical sequence g_m with R(g_m)->infinity the displayed lower bound proves R(F_m)->infinity. This reduction does not supply such seeds.

## Exact universal consequence for proper-partition banks

Let C_* be the supremum of H/I over all finite nonconstant Boolean functions of dimension at least two (one-bit functions have H=0), in the extended nonnegative reals, and C_prime the same supremum over composition-prime functions. Subclass inclusion gives C_prime<=C_*; approximation of each fixed seed by the construction gives C_prime>=R(g), so C_prime=C_*, including the infinite case.

Fix K>=0 and real kappa. For a proper disjoint Boolean-core representation P define the specific signed bank

    A(P)=C(P)+kappa I(F)+sum_j q_j R_K(g_j),
    C(P)=H(F)-sum_j q_j H(g_j),

where q_j are the actual outer pivotal probabilities and R_K are TRUE full physical stopping deficit hulls. Singleton nonconstant cores and all their restrictions have H=R_K=0; constants likewise. Therefore every proper representation of each composition-prime F has EXACTLY A(P)=H(F)+kappa I(F), independently of K. For arbitrary F the singleton representation always supplies this value, so

    sup_F inf_(proper P) A(P)/I(F) = C_*+kappa.

This equality concerns the optimized specific bank at one initial state; it creates no new owner credit and asserts no history renewal. In particular a universal optimized proper-partition bound A<=L I exists iff full FEI holds, and its best price is exactly the optimal FEI constant plus kappa. A whole-domain core, overlapping inputs, or multiple-bit summaries are different hypotheses and are not ruled out by the three-row proof.

## First unsupported line and proof rung

The all-dimensional construction, continuity proof and exact supremum consequence are an analytic proof subject to independent review. Exact finite validation and a formal-check receipt are recorded separately. Full FEI remains OPEN: the missing step is an ORIGINAL dimension-independent entropy/source payment on these composition-prime functions, or actual seed functions with H/I unbounded. Tiny edits force primality and do not create divergent ratios from bounded-ratio seeds.
