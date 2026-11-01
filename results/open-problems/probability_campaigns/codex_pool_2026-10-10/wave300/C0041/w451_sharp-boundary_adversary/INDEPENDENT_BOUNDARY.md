# C0041 independent boundary analysis

Author w451, 2026-10-10. Saved before reading w450's proof. Referee w452 has not checked this derivation. These are boundary results and objections to stronger auxiliary claims. C0041 is neither proved nor refuted; no novelty is claimed for classical one-dimensional ingredients.

## Exact target

Drewitz--Ramirez, arXiv:1309.2589, Open question 2.20, PDF p.24 (zero-based page 23): for d>=2, does a nearest-neighbor RWRE with iid site transition vectors and uniform ellipticity, transient in a direction l, necessarily have positive speed in that direction? Section 2.1 defines independence across sites, not across layers or consecutive visits. We work with P0(X_n.l -> +infinity)=1, which implies the same quenched statement for almost every environment. Any use of merely positive probability of the directional event must be handled separately.

The hardest unresolved piece is finite mean duration of a directional regeneration cycle under the no-backtracking conditioning, using only site iid, UE and directional transience. Equivalence of quantitative ballisticity conditions supplies no such premise.

## B1. No uniform positive speed bound from dimension and ellipticity

Fix d>=2, b=1/(2d), kappa=1/(4d), and 0<epsilon<=1/(4d). At every site set omega(+e1)=b+epsilon, omega(-e1)=b-epsilon, and omega(+ej)=omega(-ej)=b for j>=2. The law is a product of identical point masses, hence site iid. All transitions are at least kappa. Increments are iid of mean 2epsilon e1, so X_n/n -> 2epsilon e1 almost surely and the walk is directionally transient.

As epsilon decreases to zero, d and kappa stay fixed. Thus no positive c(d,kappa) bounds v.e1 below over all such laws. For T_1=inf{n:X_n.e1=1}, P(T_1>n)<=P(X_n.e1<=0), which has a summable Chernoff bound since increments have positive mean. Therefore E T_1<infinity; Wald gives E T_1=1/(2epsilon). No upper bound on a one-level crossing mean depending only on d,kappa exists either.

This refutes a stronger uniform quantitative bridge within the target class. It does not contradict each fixed law having positive speed.

## B2. Exact critical infinite-mean crossing example in d=1

Let p_i, i in Z, be iid, equal to 3/4 with probability a and 1/4 with probability 1-a. The nearest-neighbor walk Y jumps right with probability p_i at i. Put rho_i=(1-p_i)/p_i. Direct calculation gives

    E log rho=(1-2a) log3;
    m=E rho=3-(8/3)a;
    A=E(1/p)=4-(8/3)a=1+m.

For a>1/2 the walk is transient to the right. Here is a scale proof. Choose positive harmonic increments Delta_{-1}=1 and Delta_i=rho_i Delta_{i-1}, for all i. The two-sided strong law makes their sum toward +infinity finite and their sum toward -infinity infinite. The interval hitting formula then shows that every fixed positive level is hit almost surely. Starting at level K, the probability of returning to a fixed lower level tends to zero as K increases, because its numerator is the summable positive tail of the scale. Infinite visits to any fixed site would require such a return after every K. Consequently every site has finitely many visits and Y_n -> +infinity.

Write e_i=E_{i,omega} T_{i+1}, allowing infinity. At each visit to i, the number of left excursions before the final right jump is geometric with mean (1-p_i)/p_i. Each left excursion has mean duration 1+e_{i-1}. Tonelli and the strong Markov property, without subtracting infinite expectations, give

    e_i = 1/p_i + rho_i e_{i-1}.

Iterating L times and using e_{-L}>=1 gives the pointwise lower bound

    e_0 >= sum_{k=0}^{L-1} (1/p_{-k}) product_{j=0}^{k-1} rho_{-j}
           + product_{j=0}^{L-1} rho_{-j}.

The empty product is 1. Each factor 1/p_{-k} is independent of the preceding product because the sites are distinct. This calculation takes an unconditional environment expectation; it assumes no independence after path conditioning. Hence

    E e_0 >= A sum_{k=0}^{L-1} m^k + m^L.

For 1/2<a<=3/4, m>=1 and E e_0=infinity. At the critical endpoint a=3/4 the bound is exactly 2L+1 for every L, while E log rho=-(1/2)log3<0 and E(2p-1)=1/4>0. In this two-point family, the classical positive-speed formula above the endpoint is (1-m)/(1+m)=(4a-3)/(6-4a); our counterexample only needs the endpoint and the zero-speed proof below.

The infinite mean implies zero speed without pretending crossings are independent. For each integer i choose an independent infinite uniform sequence U_i and use it to drive the excursion from i until first hitting i+1 in the fixed environment. Excursions finish almost surely by the scale proof. Concatenating them has the quenched walk law by the strong Markov property. Its duration xi_i is a translation-covariant measurable function of the shifted environment and U_i. The pairs (p_i,U_i) are iid, so (xi_i) is stationary ergodic, although generally dependent. Birkhoff applied to min(xi_i,M) gives, for each finite integer M,

    liminf T_n/n >= E min(xi_0,M).

Taking M to infinity proves T_n/n -> infinity. Inverting first-passage times gives running maximum M_t/t -> 0. Directional transience makes Y_t eventually positive; since Y_t<=M_t, Y_t/t -> 0.

## B3. Lift to d>=2 and identify exactly the failed hypothesis

Fix d>=2 and a=3/4. At x=(x1,...,xd), set

    omega(x,+e1)=p_{x1}/2;
    omega(x,-e1)=(1-p_{x1})/2;
    omega(x,+ej)=omega(x,-ej)=1/[4(d-1)], j>=2.

These sum to one and every transition is at least min(1/8,1/[4(d-1)])>0. The environment is stationary and ergodic under the full translation group: an event invariant under all translations is invariant under the ergodic iid layer shift in e1. It is not site iid. At distinct x,y with x1=y1, let B_x={p_{x1}=3/4}. Then

    P(B_x intersect B_y)=3/4, whereas P(B_x)P(B_y)=9/16;
    Cov(1_{B_x},1_{B_y})=3/16.

Construct the walk with an independent Bernoulli(1/2) axial clock. At successive axial times its first coordinate is exactly Y. If N_n counts axial steps, N_n/n -> 1/2, X_n.e1=Y_{N_n}, and therefore X_n.e1 -> +infinity while X_n.e1/n -> 0. Every transverse coordinate has bounded martingale increments of conditional mean zero, so its ratio to n tends to zero by Azuma and Borel--Cantelli. Thus X_n/n -> 0 almost surely. The environment's raw mean local axial drift is nevertheless E[p-1/2]=1/8.

This refutes the stronger statement with site iid replaced by stationary ergodicity, despite UE and positive averaged local drift. It does not refute C0041. Resampling p independently at every site destroys the exact axial reduction: a transverse move now changes which parameter governs the next axial step at the same x1.

## Audit use and remaining gap

B1 breaks any lower speed bound, or upper crossing-time bound, that depends only on d,kappa. B3 breaks an attempted lift treating common layer variables as site independent. B2 breaks any qualitative inference from finite excursions almost surely to finite mean. Record the auxiliary claim being refuted in each case. A valid C0041 proof must use genuine site independence to obtain a law-dependent integrable regeneration-time estimate.

Sources: target and classical comparisons in https://arxiv.org/pdf/1309.2589, Open question 2.20, Theorems 2.10 and 2.16, and Remark 3.11. Original one-dimensional result: Fred Solomon, Annals of Probability 3 (1975), 1--31, DOI 10.1214/aop/1176996444. Derivations above are written independently in this campaign; no paired proof was used.

NEXT: w452 checks the scale/crossing/dependence arguments; w451 reads w450's saved proof and identifies its first step requiring an additional premise.
