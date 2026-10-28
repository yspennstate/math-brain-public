# Rare physical edits preserve every stopped terminal payoff

The stability estimate is uniform over adaptive physical stopping trees and every real rate in a compact interval. It strengthens root entropy/influence continuity. It does not price query-KL transactions or supply an initial arbitrary-core reference. Entropies are in bits.

## 1. Exact statement and scope

Let f,g:{-1,+1}^N->{-1,+1} differ on a fraction delta of the uniform cube, where 0<=delta<=1/16. Fix any finite Kmax>=0. A physical stopping tree queries a still-unrevealed coordinate, keeps both children at their actual probability1/2, and may stop at any node. It can adapt to earlier physical answers; it is the SAME tree for f and g. Write

    P_K(f,T)=E_leaf (H(f_leaf)-K I(f_leaf))_+,
    R_K(f)=max_T P_K(f,T),
    omega(N,delta,Kmax)=2N sqrt(delta)+h2(2sqrt(delta))+2Kmax N delta.

For EVERY such T and EVERY real K in[0,Kmax],

    |P_K(f,T)-P_K(g,T)|<=omega,
    |R_K(f)-R_K(g)|<=omega.                        (1)

An even stronger conclusion is E_leaf |(H(f_leaf)-K I(f_leaf))_+-(H(g_leaf)-K I(g_leaf))_+|<=omega. No finite grid of K or delta is used. All terms have continuous values at delta=0, and omega tends to0 there for fixed N,Kmax. The N=0 case consists of constants and both sides vanish; below assume N>=1.

## 2. Fourier probability continuity on each literal leaf

Let a,b be the normalized Fourier amplitude vectors of two restricted sign-valued functions, with conditional disagreement delta_l. Parseval gives ||a||=||b||=1 and <a,b>=1-2delta_l. Their squared Fourier laws p,q satisfy

    TV(p,q)=(1/2)sum |a_s²-b_s²|
       <=(1/2)||a-b||_2||a+b||_2
       =2sqrt(delta_l(1-delta_l))<=2sqrt(delta_l).

This estimate is valid even when delta_l is large; it is NOT assumed that the parent rare-edit bound holds conditionally. The physical leaf cylinders partition the original cube, so sum w_l delta_l=delta. Thus the mean tau of the actual leaf total variations satisfies

    tau=sum w_l TV(p_l,q_l)<=2sum w_l sqrt(delta_l)<=2sqrt(delta)<=1/2. (2)

The middle inequality is Jensen for sqrt, or Cauchy-Schwarz with sum w_l=1. Both full physical outcomes are essential to this conservation. Zero-reach leaves may be removed; no expression divides by their probability.

For distributions on at most M=2^N atoms, use maximal coupling X,Y with disagreement probability v=TV. The flag E=1[X!=Y] gives

    |H(X)-H(Y)|<=h2(v)+v log2(M-1)<=h2(v)+Nv.

Indeed H(X|Y)<=H(E)+Pr(E=1)log2(M-1), since E=0 fixes X=Y. The reverse direction is identical. With M=1 the entropy difference is0 directly. Applying this on each leaf, summing absolute differences, and using concavity of h2 gives

    sum w_l |H(f_l)-H(g_l)|<=h2(tau)+N tau
       <=h2(2sqrt(delta))+2N sqrt(delta).          (3)

The final step uses h2 increasing on[0,1/2] and (2). It does not require any individual leaf TV to be <=1/2. Coefficient zeros and deterministic leaves are included by continuity. All sums are finite, so no interchange with an infinite tree or integral is used.

## 3. Influence and stopping

For any free coordinate i in a leaf, the two edge-disagreement indicators for f_l,g_l can differ only when the functions disagree at one of the edge endpoints. Therefore

    |Inf_i(f_l)-Inf_i(g_l)|<=2delta_l,
    |I(f_l)-I(g_l)|<=2N delta_l.

Keeping all cylinders gives E_leaf |Delta I|<=2N delta. Since x->x_+ is1-Lipschitz,

    E_leaf |Delta(H-KI)_+|
      <=E_leaf |Delta H|+Kmax E_leaf |Delta I|<=omega.

This proves the stronger version of (1). To compare optimized hulls, use an optimal f-tree as a candidate g-tree and conversely. These maxima exist because the finite cube admits only finitely many deterministic physical stopping trees. Randomized policies are mixtures and obey the same estimate. Trees optimized separately for each K are allowed: the common bound is uniform over all T and K simultaneously. A policy for one function must be frozen before evaluating its paired payoff; selecting unrelated trees for the two functions would not prove pointwise policy stability.

There is also a signed cumulative-charge corollary. Let Delta H_v=H(f_v)-mean_child H(f_child), and let d_v be the physical influence of the queried coordinate. Telescoping gives

    Q_K(f,T)=sum_internal w_v (Delta H_v-K d_v)
       =H(f)-K I(f)-E_leaf[H(f_leaf)-K I(f_leaf)].

The root signed difference and mean absolute leaf signed difference are each bounded by omega, so EVERY common tree and EVERY K in[0,Kmax] satisfy |Q_K(f,T)-Q_K(g,T)|<=2omega. Thus actual integrated entropy-minus-pivotal-influence charges survive the perturbation uniformly too. This is the telescoped physical charge, not a reference projection or query-KL fee.

## 4. Universal rare-edit approximation, including adaptive policies

Take ANY finite n-bit Boolean seed f, pad it by spectators to N bits, and flip precisely the radius-one ball around the origin. This is A080's actual composition-prime construction F_N=f_padded*b_N. Its exact disagreement fraction is delta_N=(N+1)2^-N, independent of the seed signs. For N>=max(n+2,7), delta_N<=1/16. The source composition-prime property is separately source-bound; no primeness hypothesis is needed for Sections1-3.

Padding leaves R_K unchanged: a dummy query has identical children, so randomizing or querying dummies cannot improve a finite maximization. Hence for every fixed finite Kmax,

    sup_(K in[0,Kmax]) |R_K(F_N)-R_K(f)| <=omega(N,delta_N,Kmax)->0. (4)

The same modulus compares the payoff of EVERY physical stopping policy on the padded pair, not just optimal values. To prove the limit explicitly, put s=2sqrt(delta_N)<=1/2. The elementary bound h2(s)<=s log2(e/s), ln2>2/3, and log2(1/s)<=N/2 imply

    omega(N,delta_N,Kmax)
      <=3(N+1)^(3/2)2^(-N/2)+2Kmax N(N+1)2^-N ->0.          (5)

Each polynomial times a geometric decay tends to zero, for example by taking consecutive-term ratios, eventually bounded below1. The estimate also covers ALL real edit budgets delta in[0,delta_N], since the defining omega is increasing on[0,1/16]. This includes the zero-budget face without assigning any positive-reach cost to an unreachable branch.

## 5. What this does not transfer

The compared functional is the original stopped terminal payoff. Initial signed-bank source prices, current-reference normalizers, projection fees, query-KL charges, and separately renewed owner labels are not parts of P_K and are not bounded by (1). No continuity claim for such a transaction ledger is made. In particular closeness of terminal payoffs does not license deleting the query-KL terms identified by A094/A011.

The exact first unpaid universal line remains: supply an INITIAL O(I) bank/reference for an arbitrary retained Boolean core from the SAME unused original physical influence, or a well-founded decreasing-price construction that actually pays the necessary histories. The preceding stability theorem says that restricting attention to arbitrarily close rare prime perturbations does not simplify that terminal stopping problem: all its policy payoffs survive uniformly. It is neither a proof of FEI nor a divergent Boolean H/I family.

The complete sufficient stopped alternative is explicit: for some ONE finite K, prove R_K(F)=0 for every composition-prime F. Equation(4) then gives R_K(f)=0 for every Boolean f. Stopping at the root yields (H(f)-K I(f))_+<=R_K(f)=0, hence full FEI with constant K. The continuity result strengthens this reduction to every common policy and every compact real rate interval; it does not establish the premise. This is a stopped alternative to the GU route, not a claim that FEI implies GU.

## 6. GU guard: normalized real spectra do not inherit this modulus

The private owner order singles out U(p)=sum_S p(S)log2(pi_p(S)/p(S)), pi_p(S)=sum_(T containing S)p(T). The preceding entropy proof does not establish continuity of U on growing cubes. Here is an exact obstruction to substituting it.

On 2m coordinates, m>=4, let M=binom(2m,m), let p be uniform on the middle layer, and put q=(1-tau)p+tau delta_top for any real tau in[0,1/16]. Since the middle layer is an antichain, U(p)=0. For each middle-layer set, pi_q=(1-tau)/M+tau; the top atom contributes zero. Consequently

    TV(p,q)=tau,
    U(q)=(1-tau)log2(1+M tau/(1-tau)),
    H(q)-H(p)=h2(tau)-tau log2 M.

All zero terms at tau=0 have their continuous values. At tau=2^-m, the largest binomial coefficient is at least the average of the 2m+1 coefficients, so M>=4^m/(2m+1), and

    U(q)>=(1-2^-m)[m-log2(2m+1)] ->infinity,
    |H(q)-H(p)|<=h2(2^-m)+2m*2^-m ->0.

Thus no universal C bounds |Delta U| by C[N TV+h2(TV)] on normalized real spectra. The nonnegative-amplitude inverse Fourier FUNCTIONS used here are NOT Boolean: their values at the all-positive input are sqrt(M)>1 for p and sqrt(M(1-tau))+sqrt(tau)>1 for q. This tests the actual displayed real functions, not every possible choice of Fourier phases; no Boolean realization of the laws is supplied or used. They are explicit normalized REAL-function laws, not an FEI or Boolean-GU counterfamily. An argument that uses only Parseval, squared-law coupling and entropy continuity cannot bridge this gap; it must use further exact Boolean structure or a separately paid U transaction. This guard names the precise first unsupported GU transfer rather than asserting it.
