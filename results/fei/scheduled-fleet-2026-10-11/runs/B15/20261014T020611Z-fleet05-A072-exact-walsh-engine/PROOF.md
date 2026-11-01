# A bounded price for one-flip rare-bias escape

All entropy is in bits. For an actual nonconstant uniform Boolean function g, let p=P(g=-1), d_i=Inf_i(g), beta_i=ghat({i}), and E(g)=min_{d_i>0} B_i(g)/d_i, where B_i is the conditional entropy H(S_i|S_{-i}) of its squared Fourier spectrum. Assume 0<p<=delta=1/16, reorienting the output if needed. No dimension, transitivity, monotonicity or high-E hypothesis is used.

Let h be negative exactly on {0,1,2,4,8,16,32,6,17,40} in little-endian cube notation, and J(x)=-h(x xor1). Replace g by J applied to six disjoint copies, repeatedly, until the negative probability first exceeds delta. This implements one flipped block followed by an output complement. Each stage below the stopping time remains minority-oriented.

**Theorem.** This procedure stops after finitely many steps at an actual Boolean G with 1/16<P(G=-1)<1/4 and

    E(G) >= E(g) - (3/16) log2(192 e) > E(g)-111/64,
    H(G)/I(G) <= H(g)/I(g) +45/22.

The second statement is an upper cost and retains the entire initial H(g)/I(g). It is not an absolute FEI bound. A direct consequence of the first statement is

    sup_{0<p<=1/16} E(g) <= sup_{1/16<p<1/4} E(g) +(3/16)log2(192e),

where both suprema range over all actual finite-dimensional Boolean functions. Thus an absolute moderate-bias erasure-selection bound would control the rare sector with this additive constant; this implication needs only one escape per starting core.

## Gate and bias

Direct enumeration of J gives negative weight counts [0,4,10,18,15,6,1]. Thus

    sigma(p)=4p-10p^2+18p^3-19p^4+10p^5-2p^6.

For 0<p<=1/16,

    sigma/p >=4-10/16-19/16^3-2/16^5 >3,
    sigma/p <=4+p(-10+18/16+10/16^3) <4.

In particular sigma is the minority probability. Iteration must leave the interval since each step more than triples p. If p_0,...,p_{N-1} are the pre-step probabilities, then p_j<=delta*3^{-(N-1-j)}. At the last output delta<p_N<1/4. Enumeration also gives four pivotal directions at the all-zero outer input (directions 1,2,3,5); the other two are not pivotal there.

## Exact composition identities

At bias p write s_T for the normalized biased Fourier masses of J, v=4p(1-p), m=1-2p, and

    q_j=sum_{T containing j} s_T/v = P_p(j is pivotal for J), Q=sum_j q_j.

All q_j>0 since every direction is relevant and the product law has full support. For every physical inner coordinate i, with t=beta_i^2,

    Inf_{j,i}(F)=q_j d_i,
    B_{j,i}(F)=q_j B_i(g)+R_j(t),
    R_j(t)=sum_{T not containing j} Phi(s_T,t*s_{T+j}/v)-q_j Phi(m^2,t),

where Phi(a,b)=(a+b)log2(a+b)-a log2 a-b log2 b, with zero terms interpreted continuously. Here is the coefficient argument, including the exceptional empty residual. The outer centered expansion is J=sum_T c_T product_{j in T}(X_j-p), where X_j=(1-g_j)/2. In each occupied block, X_j-p has only nonempty Fourier coefficients -ghat(U)/2. Hence every physical Fourier set has a unique occupied-block pattern. For a pair of sets differing in coordinate i, all nonempty residual sets in its block inherit the corresponding inner pair with total outer weight q_j. For the empty residual the two masses instead are s_T and t*s_{T+j}/v. Replacing the inherited empty pair (m^2,t) gives exactly R_j. Homogeneity of Phi accounts for q_j. Dummy inner coordinates have t=d_i=B_i=0 and remain dummy.

The same unique occupied-pattern argument, or entropy chain rule for the nonempty normalized inner spectrum rho, gives

    H(F)=H_p(J)+v Q H(rho)=Q H(g)+C,
    C=H_p(J)-Q h2(v),    I(F)=Q I(g).

In particular C is signed; no terminal term or initial entropy is discarded.

## Summable erasure loss

Since Phi>=0, R_j(t)>=-q_j Phi(m^2,t). Parseval gives m^2+t<=1, and for x+y<=1,

    Phi(x,y)<= y log2(1/y)+y log2(e),

because x ln(1+y/x)<=y. Also |beta_i|<=d_i from the conditional derivative formula and |beta_i|<=2p from beta_i=-2 E[1_{g=-1} chi_i]. Thus, writing b=|beta_i|>0,

    Phi(m^2,b^2)/d_i <= b log2(e/b^2)
                               <=2p log2(e/(4p^2))=:L(p).

The last function of b is increasing on 0<b<=1/8: its derivative has sign -1-2 ln b>0. If b=0 the loss is zero. Consequently E(F)>=E(g)-L(p), uniformly across ALL blocks and physical coordinates. L is increasing throughout the rare band. The reverse geometric bound therefore yields

    sum_j L(p_j) <= sum_{k>=0} 2delta*3^{-k}
                  [log2(e/(4delta^2))+2k log2 3]
                =3delta log2(3e/(4delta^2))=(3/16)log2(192e).

For the rational bound, ln2>2/3 follows from the first positive term of its atanh series; hence log2 e<3/2. Also 3^4<2^7 implies log2 192<31/4. Their sum times3/16 is111/64, strictly.

## Summable normalized entropy cost

The outer spectral random set has marginals vq_j, so subadditivity gives H_p(J)<=sum_j h2(vq_j). The scalar inequality

    h2(vq)<=q h2(v)+v h2(q),  0<=v,q<=1,

follows because the right side minus left side vanishes at q=0,1 and has second derivative -v(1-v)/[ln2(1-q)(1-vq)]<=0 in the interior. Therefore C<=v sum_j h2(q_j).

For each j, at the dominant all-zero assignment of the OTHER five bits its pivotal status is fixed. A union bound gives min(q_j,1-q_j)<=5p. Since 5p<=5/16<1/2,

    h2(q_j)<=h2(5p)<=5p log2(e/(5p)).

The four dominant pivotal directions satisfy q_j>=(1-p)^5>=1-5p, giving Q>=4(1-5p)>=11/4. Since v<=4p,

    C<=120p^2 log2(e/(5p)).

For completeness the uniform edge isoperimetric estimate I(g)>=2p log2(1/p) follows by entropy tensorization of 1_A, A={g=-1}. The tensorized left side is Ent(1_A)=p log2(1/p). In a two-point fiber, Ent_i(1_A)=1/2 if the fiber crosses A and zero otherwise. Averaging and summing is I(g)/2. Tensorization here follows inductively from the entropy chain rule and convexity of Ent under averaging (equivalently the log-sum inequality). It applies to indicators including fibers that vanish, by continuity.

Combining these facts and e<5 gives

    C/(Q I(g)) <= (240/11)p * log2(e/(5p))/log2(1/p)
               <= (240/11)p.

The ratio identity is EXACT at every stage:

    H(F)/I(F)=H(g)/I(g)+C/(Q I(g)).

It telescopes with the complete starting ratio and all signed C terms. Since sum_j p_j<=3delta/2=3/32, the total upper cost is45/22. This completes the theorem.

## First unsupported universal line

Neither theorem bounds E(g) or H(g)/I(g) absolutely. The missing line is an absolute admission/exposure bound for the resulting moderate-bias core, with any subsequent return/escape costs charged to a finite global budget. Repeated arbitrary excursions could incur unboundedly many copies of these constants. A composition level is not a physical restriction query, and this proof makes no once-spent restriction influence claim.
