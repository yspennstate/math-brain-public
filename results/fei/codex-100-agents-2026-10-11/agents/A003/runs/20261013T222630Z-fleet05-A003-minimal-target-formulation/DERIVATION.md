# First two majority queries: inherited erasure and an actual-history prefix

All entropies are bits. Phi(a,b)=(a+b)log2(a+b)-a log2(a)-b log2(b), with continuous zero conventions. Physical inputs are uniform after every actual restriction.

## 1. The sliced-majority lemma

Let g=Majority_(2r+1), r>=1, rho=binom(2r,r)/4^r. Fix its first physical bit to sigma, and call the remaining 2r-input sign h_sigma. Every remaining coordinate i has mean mu=sigma rho, singleton coefficient gamma=rho and influence d=rho. Then

    B_i(h_sigma)<=2rho,

with equality for r=1. This is an all-dimensional inherited-erasure estimate, not a bound assumed for arbitrary inner functions.

Proof: write c_l for the permutation-invariant degree-l Fourier coefficient of g. Only odd l occur. The derivative in the fixed coordinate is the indicator that its 2r other inputs sum to zero; its even-degree coefficients are c_(l+1). Since the product of this indicator and the sum of those inputs is identically zero, its degree-t coefficient for odd t gives

    t c_t+(2r-t)c_(t+2)=0.                         (1)

On the slice, the degree-t coefficient is c_t for odd t and sigma c_(t+1) for even t. For a remaining coordinate, group its spectral erasure packets by remainder size t in {0,...,2r-1}. The even-t packets have both squared entries c_(t+1)^2 and thus cost 2c_(t+1)^2. The odd-t packets have entries c_t^2,c_(t+2)^2.

Put E=sum_(even t) binom(2r-1,t)c_(t+1)^2. The physical derivative of h_sigma is the indicator of one of the two boundary levels (sum of 2r-1 remaining inputs equals +1 or -1). It has mass rho, and its reflected boundary indicator has disjoint support. Consequently its even and odd Fourier parts both have energy rho/2: reflection gives zero inner product, so E=rho/2. This also proves d=rho; the zero-frequency mean and singleton follow directly by conditioning the odd parent (its degree-two coefficient is zero).

For nonnegative a,b, Phi(a,b)<=2sqrt(ab). Here is an elementary proof rather than a floating sign test. Set z=|a-b|/(a+b). The desired inequality is h2((1+z)/2)<=sqrt(1-z^2). The derivative of their difference has the sign of R(z)-ln2, where R(z)=sqrt(1-z^2)atanh(z)/z. R decreases strictly from 1 to 0, since R'(z)=[z-atanh(z)]/[z^2 sqrt(1-z^2)]<0. The difference therefore first increases and then decreases, and vanishes at both endpoints. Boundaries follow by continuity.

By (1), binom(2r-1,t)|c_t c_(t+2)|=binom(2r-1,t-1)c_t^2 for odd t. Summing gives exactly E. Thus the even packets cost 2E=rho and the odd packets cost at most 2E=rho. This proves the lemma. No FEI hypothesis is used.

## 2. Coherent composition and the signed credit

Let A,D be the split of an arbitrary actual Boolean outer sign in one coordinate: AD=0, A^2+D^2=1, delta=E D^2. For a fresh encoder h with mean mu, singleton gamma and inner influence d, the exact interface, independently read from A026 section 2, is

 B_i(A+hD)=delta[B_i(h)-Phi(mu^2,gamma^2)]
              +sum_T Phi((Ahat(T)+mu Dhat(T))^2,gamma^2 Dhat(T)^2). (2)

This follows by isolating the encoder's empty remainder packet and using homogeneity on every nonempty remainder. It preserves the signs in Ahat+mu Dhat. Parseval and AD=0 give sum(Ahat+mu Dhat)^2=1-delta+mu^2 delta. Concavity bounds the last sum by Phi(1-delta+mu^2 delta,gamma^2 delta), or by gamma^2 delta log2(e/(gamma^2 delta)) when mu^2+gamma^2<=1.

For a once-sliced odd majority, mu^2=gamma^2=rho^2, d=rho, so (1)-(2) yield the universal actual-rest bound

 B_i(A+h_sigma D)/(delta rho)
       <=2-2rho+rho log2(e/(rho^2 delta)).           (3)

The sharper form retains Phi(1-delta+rho^2 delta,rho^2 delta)/(delta rho) in place of the logarithmic term. The negative 2rho is an actual empty-row credit; it is not silently discarded. For an intact majority the corresponding bound has only the logarithmic term (A026 section 1). delta=0 means an irrelevant bit and is omitted.

This is NOT a universal coordinate price: delta can be arbitrarily small. It closes the inherited slice term; the arbitrary-outer collision term remains.

## 3. Extension from one to two queries per block

Use the outer influence hypotheses of A026-INTACT-ENCODER-BIASED-PREFIX v1: even k>=4, delta0=2^-k, p=delta0^2, s=sqrt(delta0); k backgrounds have influence p u with u=1/2+delta0, 2k backgrounds have influence p A0 with A0=1-s+delta0, and selector y has influence p delta0. Let W=u+2A0<=5/2. Enlarge the fresh encoder to

 R=k^2 2^(2k+4), M=2R+1, rho=binom(2R,R)/4^R<delta0/(4k).

The binomial recurrence bound rho<=1/sqrt(R+1) and M rho>=1 are reconstructed in A026 section 3. Consider any adaptive actual history querying at most two bits per block, never y. A block's output mean after zero, one, or two queries is respectively 0, +/-rho, or 0 or +/-2rho. The final assertion follows from the conditional means of the two children of a once-sliced majority, whose next singleton is rho. Twice-sliced remaining-bit influences are rho times either 2R/(2R-1) or 2(R-1)/(2R-1); direct boundary binomial counts prove this. Hence every residual inner influence is at most t rho, t=1+1/(M-2).

The density of the induced independent outer outputs relative to uniform lies between (1-2rho)^(3k) and (1+2rho)^(3k). Put eta=6k rho<3delta0/2<=3/32. All outer derivative masses are between (1-eta) times their original values and their original values/(1-eta). In a block eligible for its first or second query, inner influence is exactly rho, and delta>=29p/64>p/4.

The intact collision term and the second-query collision term in (3) are at most

 rho log2(4e/(p rho^2))
 <delta0/(4k)[4k+2log2(4k)+2+log2(e)]
 <=delta0/(4k)[6k+11/2] <=59/512=:Kc.             (4)

Here x log2(4e/(p x^2)) is increasing on this interval, log2(4k)<=k+1, and log2(e)<3/2. Therefore a first query costs <Kc and a second query costs <2+Kc-2rho, both divided by its actual influence.

Half-average eligibility: relevant residual dimension D>=3k(M-2)+1. Total influence is at most p/(1-eta)[t M rho kW+delta0]. Each candidate first/second bit has influence >=rho p(1-eta)/2. It suffices that

 (D/M)(1-eta)^2>t kW+delta0/(M rho).

Use (1-eta)^2>=1-2eta>1-3delta0, D/M>=3k(1-2/M), and M rho>=1. Subtracting the right bound leaves at least

 k[1/2+2s-12delta0]-6k/M-(5/2)k/(M-2)-delta0.

The bracket is >=1/4 on delta0 in [0,1/16] by concavity and endpoint values. Since M>=128, this is >k/8-delta0>0. Thus EVERY eligible first/second bit is in G_(1/2), with the actual relevant residual dimension, at every such history. The ratio of any background influence to the selector is <=t (rho/delta0)/(1-eta)^2<1, and all influences are <1/4. None of these statements claims an erasure lower bound for the selector away from the root.

## 4. Payment and full-law normalization

Let S1,S2 be the expected sums of queried-coordinate influences over first and second queries respectively. Exact physical telescoping gives S1+S2=I(root)-E I(leaf). The proof pays

 sum_nodes w B_query <=Kc(S1+S2)+(2-2rho)S2,
 H(root)<=E H(leaf)+(Kc+2/ln2)(S1+S2)+(2-2rho)S2.  (5)

In particular Cprefix=2+59/512+2/ln2 suffices per consumed influence. Every terminal entropy is retained, including when all 3k blocks have been queried twice. This extends A026's maximum prefix length from 3k to 6k, with the enlarged encoder stated explicitly rather than asserting the original size works.

For every actual descendant law P with empty mass a, v=1-a, R=P/v on nonempty sets, the normalization used is exactly A004 section 4:

 B(P)=v B(R)+T0(P), DTC(P)=h2(v)+v DTC(R)-T0(P),
 T0(P)=sum_i Phi(a,P_{i}).

These terms are preserved by the checker. No Boolean property is applied to R, and no conditional DTC is substituted for full-law DTC.

## 5. First unsupported line and smallest next target

An arbitrary seed has no dimension-independent lower bound on delta, so (3) alone does not prove C018. After two queries in every block, a third query uses a twice-sliced majority whose inherited erasure is not paid by the once-slice lemma. Terminal outer-core entropy also remains. The smallest next scoped target is a uniform bound on B_i(h_(sigma1,sigma2))/I_i(h_(sigma1,sigma2)) for the two-query majority slices, coupled with their signed empty-row subtraction and actual density/eligibility; the genuinely universal unpaid lemma is a common-budget bound on the coherent collision term for arbitrary outer delta, retaining terminal entropy. Neither is asserted here.
