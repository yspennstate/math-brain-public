# Independent reconstruction of A003 stage 3

Scope: accept A003-ONCE-SLICED-MAJORITY-ERASURE@1 and A003-TWO-QUERY-ELIGIBLE-PREFIX@1 exactly as conditional on their stated actual outer influence hypotheses. This does not independently accept the B05 construction used to instantiate those hypotheses. A004 supplied no repair to either statement or proof. This is one independent review, not the two reviews required for a major universal candidate.

## 1. Independent coefficient representation and packet inequality

Put N=2r, rho=binom(N,r)/2^N. Instead of recursively generating majority coefficients, compute the coefficient of a fixed l-subset in the zero-sum boundary indicator directly:

    d_l=2^(-N) sum_j (-1)^j binom(l,j) binom(N-l,r-j).

Odd l vanish by reflection. The majority coefficient c_(l+1)=d_l: its derivative in the distinguished bit is exactly this boundary indicator. This formula is a direct signed count; the executable uses it independently of A003's recurrence and checker. The coefficient of degree t in the first slice h_sigma is c_t for odd t and sigma c_(t+1) for even t, including c_1=rho at degree zero. Thus mu=sigma rho, gamma=rho. Direct boundary probability is rho: among 2r-1 other bits the pivotal boundary is one of sums +/-1, with mass binom(2r-1,r)/2^(2r-1)=rho.

Let k be that boundary indicator. Its reflection k(-x) occupies the opposite, disjoint level. Hence <k,k(-x)>=0; reflection acts by (-1)^degree in Fourier space. Parseval gives equal even and odd Fourier energy rho/2. For a spectral edge of h with remainder degree t, the two coefficients are identical up to sign when t is even, and c_t,c_(t+2) when t is odd. The even packets cost rho in total.

Here is a separate analytic proof of Phi(a,b)<=2 sqrt(ab), in bits. By homogeneity set a=exp(t), b=exp(-t), t>=0. Half the natural-log packet is F(t)=cosh(t) ln(2cosh(t))-t sinh(t). Its derivative is cosh(t)[tanh(t)ln(2cosh(t))-t]. For t>0, define G(t)=t coth(t)-ln(2cosh(t)). Then

    G'(t)=(tanh(t)-t)/sinh(t)^2<0,   lim_(t->infinity) G(t)=0.

Therefore G(t)>0, F'(t)<0, and F(t)<=F(0)=ln2. Dividing by ln2 gives the claimed bit inequality; zero entries follow by continuity. In natural logs its constant is 2 ln2, not 2.

Multiplying the parent boundary indicator by the sum of its N coordinates gives zero pointwise. Its odd-degree-t coefficient is t c_t+(N-t)c_(t+2)=0. Consequently

    binom(N-1,t)|c_t c_(t+2)|=binom(N-1,t-1)c_t^2

for odd t. Summing gives the same even-energy rho/2 already established. The odd packet cost is at most rho. Thus B_i(h)<=2rho=2 I_i(h); r=1 gives equality, since both packets have equal squared entries. This is an all-r proof. The 64 exact Krawtchouk checks corroborate it and do not replace its quantifiers.

## 2. Arbitrary outer rest, with coherent signs preserved

For f(z,x)=A(x)+zD(x), A,D are ternary, AD=0, A^2+D^2=1. Put delta=E D^2. With fresh disjoint encoder h, F=A+hD has coefficient Ahat(T)+mu Dhat(T) at encoder empty index; every nonempty encoder index has coefficient hhat(V)Dhat(T). Therefore isolating the empty-remainder edge and using homogeneity on all other edges gives exactly

    B_i(F)=delta[B_i(h)-Phi(mu^2,gamma^2)]
           +sum_T Phi((Ahat(T)+mu Dhat(T))^2,gamma^2 Dhat(T)^2).

No balance of the physical rest is needed. Parseval and AD=0 give row totals a=1-delta+mu^2 delta and b=gamma^2 delta. Log-sum concavity bounds the collision by Phi(a,b). Since mu^2+gamma^2<=1, a+b<=1. Also Phi(a,b)<=b log2(e(a+b)/b): use a ln(1+b/a)<=b, with continuous endpoints. These facts, mu^2=gamma^2=rho^2 and physical I_i(F)=delta rho, give

    B_i(F)/(delta rho)<=2-2rho+rho log2(e/(rho^2 delta)).

delta=0 is the irrelevant case B_i=I_i=0; do not divide. The subtraction 2delta rho^2 is an exact bit-entropy credit, not a free influence payment. The all-dimensional logarithmic collision majorant is valid, but unbounded as delta->0 at fixed rho. The checker independently constructs actual composed truth tables, their spectra and physical flips for all 16 two-input Boolean outers and both slices at M=3,5,7; every remaining inner coordinate is checked. It also certifies the sharper concavity majorant by rational log intervals.

## 3. Abstract two-query prefix: all-k reconstruction

Accept only the influence-hypothesis scope: even k>=4, delta0=2^-k, p=delta0^2, s=sqrt(delta0), background influences p(1/2+delta0) on k inputs and p(1-s+delta0) on 2k inputs, selector pdelta0. The fresh block size is M=2k^2 2^(2k+4)+1=2R+1. Write W=5/2-2s+3delta0<=5/2.

The recurrence rho_R/rho_(R-1)=(2R-1)/(2R) proves rho_R^2<=1/(R+1) by induction: (4R^2-4R+1)(R+1)<=4R^3. Hence rho<delta0/(4k). Also M rho>=1 because the central binomial mass is a maximum among M masses summing to one.

After zero, one or two physical queries the encoder mean is respectively 0, sigma rho, or (sigma1+sigma2)rho. For two queries, the remaining coordinate's derivative probability is 2(R-1)rho/(2R-1) if the signs agree, and 2Rrho/(2R-1) if they disagree. These follow directly from binom(2R-2,R-2) and binom(2R-2,R-1) boundary counts. Thus every residual inner influence is <=t rho, t=1+1/(M-2). A first/second candidate still has influence exactly rho.

Every reached history has at most 3k output biases, each of magnitude <=2rho. Their joint density against uniform lies in [(1-2rho)^(3k),(1+2rho)^(3k)]. With eta=6k rho<3delta0/2<=3/32, Bernoulli and the geometric majorant bound this by [1-eta,1/(1-eta)]. Outer derivative events do not depend on their own output, so the same comparison applies to every actual derivative mass, including touched blocks. In particular candidate delta>=p(1-eta)/2>29p/64>p/4.

The collision price is at most rho log2(4e/(p rho^2)). On the interval rho<delta0/(4k), its derivative is positive (4e/(p rho^2)>e^2). Evaluation at that endpoint gives

    delta0/(4k)[4k+2log2(4k)+2+log2(e)]
    <=delta0/(4k)[6k+11/2]<=59/512.

Here 4k<=2^(k+1) holds for k>=4 by induction, and log2(e)<3/2 follows from ln2>2/3 by its positive atanh expansion. The final bound is maximized at k=4 because 2^-k[6+11/(2k)] decreases with k. A first query is priced <59/512; a second <2-2rho+59/512. Both use the actual physical influence delta rho.

All residual coordinates are relevant: these large encoders have nonzero boundary probability even after two queries, and induced output distributions have full support. Relevant dimension D>=3k(M-2)+1. Total influence is <=p[t M rho kW+delta0]/(1-eta), while each candidate is >=rho p(1-eta)/2. Half-average eligibility follows if (D/M)(1-eta)^2>t kW+delta0/(M rho). Its difference is bounded below by

    k[1/2+2s-12delta0]-6k/M-(5/2)k/(M-2)-delta0.

The bracket is concave on [0,1/16] and its endpoint values are 1/2,1/4, so it is >=1/4. Since M>=128, 6/M+(5/2)/(M-2)<1/8, leaving >k/8-delta0>0. Thus every candidate is eligible at every such history. Background/selector ratio <=t(rho/delta0)/(1-eta)^2<1, and all influences are <1/4. These are influence statements; no child selector erasure lower bound is inferred.

For the actual adaptive prefix, let S1,S2 be expected spent influence by query number within a block. Physical telescoping gives S1+S2=I_root-E I_leaf. The JS bound costs at most (2/ln2)(S1+S2). Summing the two erasure prices therefore gives exactly A003's claimed terminal-inclusive bound. The instantiated B05 family and its old root bad-selector claim are not needed for this abstract proof and are outside this acceptance.

## 4. Signed terminal ledger and units

For ANY actual physical binary-query stopping tree, let E_B and E_JS be the expected sums of queried erasure and JS. Then

    H_root=E H_leaf+E_B+E_JS,
    I_root=E I_leaf+S,
    K I_root-H_root=E(K I_leaf-H_leaf)+K S-E_B-E_JS.

These are finite-tree identities. Every leaf's full law P has v=1-P_empty and R its nonempty conditional law, when v>0. The terminal contribution is exactly

    H_leaf=h2(v)+v H(R).

Equivalently B_leaf=vB(R)+T0 and DTC_leaf=h2(v)+vDTC(R)-T0, where T0=sum_i Phi(P_empty,P_singleton_i); T0 cancels only when both components use the same leaf law and weight. At v=0 the terminal entropy is zero; R is omitted. These are A004's previous correction applied to the new descendants, not a newly claimed universal estimate. The 16 actual adaptive four-query trees on two Maj3 blocks check all these identities on 496 nodes, including constants, dictators, parity and point-defect/bent outers. These tests do not assert the special outer influence hypotheses for those small examples.

Bit constants: B_slice<=2rho; second-query signed credit 2rho^2 delta; collision Kc=59/512; JS price 2/ln2; total prefix Cbit=2+59/512+2/ln2<5.001. In natural logs these are 2ln2 rho, 2ln2 rho^2 delta, 59ln2/512, 2, and Cnat=2+(2+59/512)ln2. Do not change physical pivotal influence when converting log units. If an indicator's unnormalized Fourier Dirichlet energy replaces sign pivotal influence, multiply the corresponding RHS coefficient by four; its spectral masses are not a normalized probability law without further conversion.

At a constant all terms vanish. The r=1 slice saturates B=2 I. Dictator/parity spectral laws have B=H=0 and may still consume physical influence in a tree. Nearly constant outer seeds are covered by the exact coherent interface; its delta-dependent logarithm remains visible. The normalization does not grant a fixed universal coordinate price.

## 5. First unsupported universal line

Neither the negative empty-row credit nor the cancellation of T0 proves that the arbitrary outer collision or E(K I_leaf-H_leaf) can be paid by one finite, dimension-independent K. A universal refund must retain the actual signed Ahat+mu Dhat collision and terminal core entropy on the same physical influence budget. This is the first unsupported line, before claiming C018/C019 or full FEI. No assertion about an unbounded Boolean H/I family is made.
