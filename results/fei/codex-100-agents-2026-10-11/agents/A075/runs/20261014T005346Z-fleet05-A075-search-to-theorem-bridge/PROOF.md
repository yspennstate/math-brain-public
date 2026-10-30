# Quantified rare-core localization with retained entropy

All cubes below are finite uniform physical cubes. Boolean outputs are signs; all entropies and logarithms are in bits. Write B_i(g)=H(S_i|S_{-i}) for its squared Fourier law, d_i=Inf_i(g), and E(g)=min_{d_i>0} B_i/d_i. The gate h is negative exactly at indices {0,1,2,4,8,16,32,6,17,40}, with a one bit representing a negative input. Six copies always have disjoint physical supports.

## 1. Exact identities, including the terminal term

Orient a core g with P(g=-1)=p, mean m=1-2p, v=1-m^2. For a selected gate input j write h=A+y_j D. In the normalized biased basis on the other five outputs let C_T=a_T+m d_T, U_T=C_T^2, D_T=d_T^2. Define phi(x,y)=(x+y)log(x+y)-x log x-y log y, with zero terms interpreted continuously. Then

    q=sum D_T=2p(1-p)^3(2-p)>0,
    R_p(t)=sum phi(U_T,tD_T)-q phi(m^2,t),
    B_(j,i)(h(g,...,g))=q B_i(g)+R_p(beta_i^2),
    Inf_(j,i)(h(g,...,g))=q d_i.                         (1)

For nonempty residual spectral sets in the selected block, both amplitudes acquire the same outer derivative multiplier, giving q times the core's pair entropy by homogeneity. For its empty residual, the amplitude without i is C_T and the amplitude with i is beta_i d_T, replacing precisely phi(m^2,beta_i^2). Other occupied blocks have normalized nonempty core spectral laws summing to one. This proves (1), including the signed empty collision. Physical edges independently give the influence identity. Matching-pair permutations/swaps make h transitive, so q,R are the same for every j. No irrelevant core coordinate becomes relevant, and every relevant one stays relevant because q>0. Complementing any entire core preserves its squared spectrum, influence and singleton squares.

Let H_p(h) be the entropy of its 64 normalized biased Fourier masses. A physical spectral set specifies its occupied blocks and the nonempty spectral set inside each. With rho the normalized nonempty law of g,

    H(g)=h2(v)+v H(rho),
    H(F)=H_p(h)+6v q H(rho)=6q H(g)+C_p,
    C_p=H_p(h)-6q h2(v),     I(F)=6q I(g).               (2)

Thus no terminal entropy is discarded. The identity does not claim that the correction has a favorable sign.

## 2. Independent acceptance of the moderate-bias premise

A084-F6-CONTINUUM-ADMISSION@1 states that for minority bias in [1/16,1/2], one common orientation for all six copies and all coordinates preserves every B_i/d_i: use the minority-negative orientation up to 7/32, and its complement above 7/32. Here is an independent reconstruction of its critical chain.

For positive D_T put u_T=U_T/D_T and lambda_T=D_T/q. The function z -> phi(exp(z),t) is convex, since its second derivative is exp(z)[ln(1+t/exp(z))-t/(exp(z)+t)]/ln2 >=0. Consequently, with G0=product u_T^lambda_T,

    R_p(t)>=q[phi(G0,t)-phi(m^2,t)].                    (3)

In particular sum D_T log(u_T/m^2)>=0 suffices for all t>=0. Necessity when m!=0 follows by dividing R(t) by t and taking t down to zero. This is an all-t analytic argument, not a scalar grid inference.

From the actual uniform Walsh coefficients of h, the raw coefficient polynomials for a selected other-input set T are

    C_T=v^(|T|/2) sum_(W superset T) hhat(W)m^(|W|-|T|),
    d_T=v^(|T|/2) sum_(W superset T+j) hhat(W)m^(|W|-|T|-1).

Our rational polynomial checker reconstructs all 32 and verifies their ratio groups by cross multiplication and their four total D weights coefficient by coefficient. Put S=m^2+2m-1, P=m^4+4m^3+2m^2-4m-11, d0=(m-1)(m+1)^3(m+3)/16, C0=SP/16, v=1-m^2. The four ratios and weights are

    u0=(C0/d0)^2,  w0=d0^2,
    uA=[(m-1)(m+1)(m+3)/S]^2,
    wA=S^2(m+1)^2[4v(m+1)^2+2v^2]/256,
    uB=[S/(m+1)]^2, wB=v^2(m+1)^4(m+3)^2/256,
    uC=(m+1)^2,
    wC=[v(m-1)^2(m+1)^4(m+3)^2+4v^2(m+1)^2S^2
         +2v^3S^2+4v^3(m+1)^4+4v^4(m+1)^2+v^5]/256.

The weights sum to q exactly. Independently computed 192-bit outward log intervals on 208 pre-frozen rational boxes prove sum w log(u/m^2)>0 throughout [9/16,7/8] and [-9/16,-1/2]. The boxes are sixteen fixed subdivisions of each source box, whose endpoints/adjacency are checked. The minimum lower endpoint is positive (display approximately 0.00113831); its exact rational value and every interval are in out/INDEPENDENT_CONTINUUM_CERTIFICATE.json. No source code or source interval verdict is imported.

For m in [-1/2,0], all u>=m^2 analytically. uC follows from 1+m>=-m; uB from |S|-|m|(1+m)=1-m>0. For uA, the difference between numerator magnitudes is 3+2m-5m^2-2m^3>=3/4. For u0, |S|>=1 and P<=-135/16, whereas |m|(1-m)(1+m)^3(m+3)<=9/4. All relevant denominators are nonzero. At m=0 the subtracted phi vanishes. Monotonicity of phi in its first argument proves the remaining domain, strictly for t>0. At t=0 reserves are exactly zero. This accepts A084@1 at its stated scope without repair or enlargement.

## 3. Rare admission: an infinite, summable error certificate

Assume 0<p<=1/16 and use the minority-negative orientation. For m in [7/8,1), every active ratio above satisfies

    u_T>=49p^2.                                        (4)

Indeed 97/64<=S<=2. The magnitude of the numerator/denominator for sqrt(uA) is at least (465/64)p>7p. For uB it is at least 97/128, whose square exceeds 49/256; uC>49p^2 immediately. For u0, q<=4p<=1/4 and |C0|=1-2 tau(p)>=29/32, where

    tau(p)=12p^2-28p^3+27p^4-12p^5+2p^6.

The event h=+1 requires at least one of the twelve unmatched input pairs to be negative, so 0<tau(p)<=12p^2. This supplies the stated bound on C0. Also 3p<=q<=4p: the lower bound follows from 2(15/16)^3(31/16)>3.

Equation (3) and monotonicity in the first argument imply

    R_p(t)>=-q t log(1/(49p^2)).                        (5)

For detail, m^2<=1 and, for a=49p^2, phi(1,t)-phi(a,t)=integral_a^1 log(1+t/x) dx <= t log(1/a), using ln(1+z)<=z. This also covers m^2<a by monotonicity. Actual Boolean singleton coefficients obey |beta_i|<=d_i and |beta_i|<=2p: the first follows from the signed derivative, the second from beta_i=-2 E[1_(g=-1) chi_i]. Therefore beta_i^2/d_i<=2p and every relevant ratio loses at most

    epsilon(p)=2p log(1/(49p^2)).                       (6)

After composing, complement the output so its minority-negative probability is p'=tau(p). This changes neither entropy nor erasure. Repetition gives p_s<=P_s, P0=1/16, P_(s+1)=tau(P_s), and p_(s+1)<=3p_s/4. tau is increasing because tau'=6q>0.

The sum of (6) is bounded uniformly over every starting rare core and every depth. Its initial term is at most 4/(7e ln2)<9/28, since e>8/3 and ln2>2/3. epsilon increases below 1/(7e)>1/21>3/64, using e<3. P1<3/64, so terms s=1,...,4 are at most epsilon(P_s). The exact polynomial iteration proves P5<2^-21. Subsequently p_s<=2^-21 4^-(s-5), because 12p_s<1/4. Using epsilon(p)<=4p log(1/p) and monotonicity of p log(1/p) there, the remaining sum is at most

    4*2^-21 sum_(j>=0) 4^-j(21+2j)=260/(9*2^19).

The exact 192-bit/80-term logarithm certificate gives

    kappa=9/28+upper(sum_(s=1)^4 epsilon(P_s))
                   +260/(9*2^19)<0.914<1.              (7)

The exact rational kappa is stored in out/INFINITE_LOSS_CERTIFICATE.json; the decimal is only a display. Its positive gap to one is certified. Thus E at every rare depth is at least its starting value minus kappa, including every relevant physical coordinate. This is a proved all-depth bound, not absence of finite failures.

## 4. Every actual core reaches the rare band

Under the moderate policy of Section 2, the minority update is tau(p) for p<=7/32 and b(p)=p^4(3-2p^2) for p>7/32. These follow by enumerating the negative set: alpha(p)=P(h=-1)=(1-p)^4(1+4p-2p^2), tau=1-alpha, and alpha(1-p)=b(p). For the first interval tau(7/32)<3/8<1/2; for the second b(p)<=b(1/2)=5/32<7/32. Thus these are indeed minority updates.

On (0,7/32], tau is strictly convex since

    tau''=12(1-p)^2(2-10p+5p^2)>0,

and the last factor at 7/32 is 53/1024. Hence tau(p)/p is strictly increasing. Exact endpoint inequalities tau(1/16)<1/16 and tau(7/32)>7/32 give a unique fixed point p* in (1/16,7/32). The fixed-point equation divided by p is

    2p^5-12p^4+27p^3-28p^2+12p-1=0.

The rational root theorem restricts rational roots to +/-1,+/-1/2, all outside this interval. Therefore p* is irrational. Every actual uniform Boolean bias, before and after finite composition, is dyadic and cannot equal p*.

Below p*, iterates decrease to zero and hence enter p<1/16 in finite time. Above p*, iterates increase until they cross 7/32 in finite time: otherwise their limit would be a fixed point at least their starting value. The crossing value is <=tau(7/32)<3/8, and one complemented step gives b(p)<=b(3/8)=7047/131072<1/16. An initial p>7/32 first maps to <=5/32 and the same argument applies. Once rare, the policy stays rare. Moderate steps lose no coordinate ratio by the independently accepted premise. There is no uniform bound on the number of moderate steps asserted; a dyadic bias can lie close to p*.

## 5. Retained rare-tail entropy and one normalized budget

Write h(x)=x log(1/x). For a full outer subset T of size k let a_T be its raw biased multilinear derivative coefficient, so its Fourier mass is v^k a_T^2, |a_T|<=1, and the six singleton coefficients equal -q. Expansion of (2), with sum |T| mass =6v q, cancels every log(v) term exactly:

    C_p=h(P_empty)+sum_(T nonempty) v^|T| a_T^2 log(1/a_T^2)
                        -6q h(1-v).                   (8)

Here P_empty=(1-2tau)^2. On the rare band 1-P_empty<=48p^2, so h(P_empty)<=72p^2 using 1/ln2<3/2. The singleton sum is at most 384p^3(2log(1/p)-4)<=96p^2: x log(1/x) is increasing on x<=1/16, q^2<=(4p)^2<=1/16, and p(2log(1/p)-4)<=1/4 on this band. For the k>=2 terms, x log(1/x)<=1/(e ln2)<9/16 and

    sum_(k=2)^6 binom(6,k) v^k <=(5385/256)v^2.

Consequently their sum is <=(48465/256)p^2. All those terms are nonnegative. The negative last term of (8) is bounded in magnitude by 6q v/ln2<=144p^2. Thus

    -144p^2<=C_p<=360p^2.                              (9)

Let the rare tail start at g0, and r_s=I(g_s)/p_s. Poincare gives r0>=4(1-p0)>=15/4. Equations (2) and q>=3p, tau<=12p^2 give r_(s+1)>=(3/2)r_s. Hence

    C_(p_s)/(6q_s I(g_s)) <= (16/3)(2/3)^s,
    C_(p_s)/(6q_s I(g_s)) >= -(8/5)(2/3)^s.

For the lower estimate use C>=-6q h(1-v)>=-6q v/ln2, which is sharper after normalization. Telescoping the EXACT quotient identity from (2) proves, for every finite rare depth d,

    H(g0)/I(g0)-24/5 <= H(g_d)/I(g_d)
                         <=H(g0)/I(g0)+16.             (10)

The complete initial ratio is retained. Each level correction is counted once; its upper envelope is 16 times the probability weight (1/3)(2/3)^s. This is a composition ledger, not a physical restriction stopping-tree payment. The finite moderate prefix retains its exact (2) terms but no uniform bound on their total correction is asserted.

Since p_s->0 and 6q_s<=24p_s, influence eventually contracts by at least 1/2 per step and tends to zero. The depth has finite dimension at every step. No infinite Boolean function is required.

## 6. Universal localization and exact remaining line

For every nonconstant Boolean g and positive delta,eta, there exists a finite iterated, oriented h-composition F of disjoint copies of g with minority probability <=delta, total influence <=eta, and

    E(F)>=E(g)-kappa.                                  (11)

Proof: the finite moderate prefix preserves each ratio, and the rare tail eventually achieves both smallness requirements with total loss at most (7). Thus for any fixed positive delta,eta, if M(delta,eta) is the supremum of E over actual nonconstant Boolean cores satisfying those bounds, then

    sup_g E(g)-kappa <= M(delta,eta) <= sup_g E(g),

in the extended-real sense. In particular boundedness of selectable erasure is equivalent to boundedness on arbitrarily rare, arbitrarily small-influence actual cores, with explicit additive loss <0.914.

For completeness, this is a quantified reduction of full FEI. A global selectable bound K lets every nonconstant restriction choose i with B_i<=K Inf_i. The exact restriction identity is H(f)-average H(children)=B_i+JS_i, with JS_i<=(2/ln2)Inf_i, and I(f)-average I(children)=Inf_i. To verify the scalar JS bound, set z=2ab/(a^2+b^2) for a spectral pair. The binary entropy deficit obeys 1-h2((1+z)/2)<=[1-sqrt(1-z^2)]/ln2: for z>=0 its derivative comparison follows from atanh(z)<=z/sqrt(1-z^2), and both start at zero; evenness covers z<0. Multiplication by a^2+b^2 gives <=(2/ln2)min(a^2,b^2)<=(2/ln2)b^2. Summing gives the bound. Recursing to constant leaves and telescoping uses every removed influence once, yielding H<=(K+2/ln2)I. Conversely E I<=sum_i B_i<=H by the entropy chain rule and conditioning monotonicity. FEI with constant C therefore bounds E by C. A finite bound M(delta,eta) implies full FEI with constant M(delta,eta)+kappa+2/ln2.

No bound on M(delta,eta) is proved here. The exact first unsupported universal line is: every arbitrary-dimensional rare, small-influence actual Boolean core has a dimension-independent E bound (or admits an independently paid alternative extraction). The localization removes the dimension cutoff and the iteration-bias closure obstruction; it does not exclude the hard rare cores. The moderate-prefix entropy bill is also not uniformly paid. No absence of finite search failures is used as a theorem.
