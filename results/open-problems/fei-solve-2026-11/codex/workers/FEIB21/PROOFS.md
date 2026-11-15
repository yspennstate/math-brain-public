# FEIB21 proofs and open points

All logarithms are base two unless written ln. Entropies are in bits. A limit concerns L=w-1 tending to infinity. Write a=2^-L and lambda_L=D^2 L a. The balanced regime means lambda_L stays in a fixed compact subinterval of (0,infinity), not merely that D a is small.

## 1. Model and tensor identities — PROVED; CHECKED NUMERICALLY

The input literals z are 0/1 bits; their Walsh character is 1-2z. Put Q_z=OR of D-1 independent width-L conjunctions, so q=1-(1-a)^(D-1). Different mates have disjoint leaf variables. With N_t=product_z(1-z Q_z), beta_t=A_t N_t=product_z z(1-Q_z), M_t=N_t-beta_t, N=product_t N_t and M=product_t M_t, the indicator of no satisfied term is N when x=0 and M when x=1. For output 1-2f, g=N+M-1 and h=N-M. The sign of h changes with the convention for the root character and does not affect its squared spectrum.

In the orthonormal basis 1, chi_z, (Q-q)/sqrt(q(1-q)), chi_z(Q-q)/sqrt(q(1-q)), the coefficients of 1-zQ are (1-q/2,q/2,-sqrt(q(1-q))/2,sqrt(q(1-q))/2). Those of z(1-Q) are ((1-q)/2,-(1-q)/2,-sqrt(q(1-q))/2,sqrt(q(1-q))/2). Tensor products give the block vectors n,beta,m=n-beta. Passing from the normalized Q mode to its actual Fourier spectrum introduces the same conditional law in g and h, so it preserves the erasure entropy exactly. This is not a truth-table approximation.

Let s=(1-q/2)^L, b=((1-q)/2)^L and A=s^D. Since beta_t is a subindicator of N_t, <N_t,beta_t>=||beta_t||_2^2=b. Thus ||M_t||_2^2=<N_t,M_t>=s-b, and

    delta=Inf_root=A-(s-b)^D.

The actual empty Fourier coefficient of g is Nhat(empty)+Mhat(empty)-1; no subtraction occurs at any other Fourier coefficient.

For resampling c mates in a block, the three correlations are

    NN(c)=(1-q/2)^(L-c)(1-3q/4)^c,
    NM(c)=NN(c)-b,
    MM(c)=NN(c)-2b+b 2^-c.

They follow either by averaging the two z copies or by summing squared Fourier coefficients with those c characters absent. Tensor products give the supplied W,G formulas. Command: python3 ~/fei_solve_agent/code/tree_dnf.py selftest; saved in tree_selftest.log. The inherited process priority was nice 10; the redundant nice invocation warned because lowering relative priority was denied, but did run. Subsequent scripts measure their actual priority directly.

## 2. An explicit erasure estimate — PROVED

The proof works for d independent root blocks, not necessarily identically distributed, with L mates in each. Each block has an indicator N_t and beta_t=A_t N_t; put s_t=E N_t, b_t=E beta_t, v_t=b_t/s_t, A=product s_t, eta=sum v_t and delta=A[1-product(1-v_t)]. Assume eta<=1. Suppose the normalized squared spectrum of N_t has probability at most alpha of containing at least three mates, and that beta_t's normalized mate spectrum is uniform on subsets. Set

    gamma=2^-L [1+L+L(L-1)/2],
    eps=min(1, 2 A eta/delta [eta+d gamma+d(d-1)alpha]),
    kappa=A d alpha/delta.

Then

    |E_root/delta-2|
      <= 2 eps+(8/ln 2)sqrt(kappa)
         + eps log2(e[3+8 A/(eps delta)])
         + delta log2(e[1+delta^-2]).                         (E)

A term with eps=0 is interpreted by continuity. Constants here are conservative.

Proof. Put H_t=beta_t product_(u!=t) N_u and H=sum H_t. Under N=1 the indicators beta_t are independent Bernoulli variables of parameters v_t. If their sum is K, h=1[K>=1]N and H=KN. Consequently

    ||H-h||_2^2=A E[(K-1)^2 1[K>=1]]
                <=A E[K(K-1)]<=A eta^2,
    ||H_t||_2^2=A v_t.

Let Omega_t consist of Fourier sets having at least three mates in block t and fewer than three in every other block; these sets are disjoint. Under H_t's normalized squared spectrum, failure to belong to Omega_t has probability at most gamma+(d-1)alpha, by tensor independence and the union bound. If Omega is their union, Cauchy-Schwarz over the d summands and ||x+y||^2<=2||x||^2+2||y||^2 give

    ||1_(Omega complement) hhat||_2^2
       <=2A eta^2+2d A eta[gamma+(d-1)alpha] <=eps delta.

(The final cap at delta is valid independently.) Also

    ||1_Omega Nhat||_2^2<=A d alpha=kappa delta.

Omega excludes the empty Fourier set. On it ghat=2Nhat-hhat. For fixed b, the derivative in u of Phi(u^2,b^2) has magnitude

    2|u| log2(1+b^2/u^2) <=(4/ln 2)|b|,

because ln(1+x^2)<=2x. Integrating from u=-b to u=ghat and using Cauchy-Schwarz therefore gives

    |sum_Omega Phi(ghat^2,hhat^2)-2 sum_Omega hhat^2|
       <=(8/ln 2)delta sqrt(kappa).

For nonempty coefficients in the complement, ghat^2<=(2|Nhat|+|hhat|)^2<=8Nhat^2+2hhat^2. Their total p mass is at most 8A+2eps delta, and their total q mass at most eps delta. Superadditivity of Phi and

    Phi(P,Q)<=Q log2(e[1+P/Q])

give the third term in (E). At the actual empty coefficient, monotonicity gives hhat(empty)=E h=delta, since h is a nonnegative pivotal indicator. Its contribution is at most Phi(1,delta^2), giving the fourth term. The omitted q mass changes 2delta by at most 2eps delta. Combining the lower and upper estimates proves (E).

For the supplied identical-block tree,

    rho=q/(4-2q),    alpha=binom(L,3) rho^3,

since the mate characters under N_t's squared spectrum are independent Bernoulli(rho); the third factorial moment bounds their upper tail. The beta spectrum on mates is exactly uniform. Thus every parameter in (E) is explicit.

If lambda_L lies in [lambda_-,lambda_+], then q<=Da, Lq<=lambda_+/D, eta~Da, delta~A Da and A~exp(-lambda_L/2). Direct substitution yields

    eps=O_(lambda_+)(L/D), kappa=O_(lambda_+)(L/D),
    E_root/delta=2+O_(lambda_-,lambda_+)(sqrt(L/D)+L^2/D).

The explicit finite error is (E); the asymptotic O constants are not optimized. In particular the limit is exactly 2, not an approximate numerical constant. Finite ratios need not be >=2.

## 3. Extension to acyclic term hypergraphs — PROVED

Let f be a monotone, uniform width-w DNF whose bipartite incidence graph (variables versus terms) is a forest. Let every variable have degree at most D, and L=w-1>=3. Assume D^2 L 2^-L<=Lambda for a fixed finite Lambda. Then, uniformly over the size of the forest and every live coordinate i,

    E_i/Inf_i <= 2+o_L(1).

An explicit coefficient is 2 plus the right-hand error of (E), with the quantities below. In particular, whenever that explicit error is <=1, the coefficient is 3. This is an erasure theorem; it does not by itself give FEI by restriction induction, because general restrictions need not preserve uniform width or the displayed parameter bound. No claim of a new FEI class is made.

Proof. Delete i and its incident terms. Acyclicity separates the branches rooted at their dL mates. Within a mate branch, avoidance of all terms takes the form R_j(1-z_j Q_j), where R_j is the indicator that every term not using z_j fails, and Q_j is the OR of the residual conjunctions of the at most D-1 terms using z_j. All residual conjunctions have width L. R_j is decreasing and Q_j increasing. Harris's inequality gives

    q_j=P[Q_j=1 | R_j=1]<=P[Q_j=1]<=(D-1)2^-L=:q_*.

Acyclicity makes different branches independent. For one branch write r_j=P[R_j=1]. Its N squared norm is r_j(1-q_j/2), and its zN squared norm and cross inner product are r_j(1-q_j)/2. Its normalized N spectral probability of including z_j is q_j/(4-2q_j); under z_j N it is exactly 1/2. Tensor over the L mates and then the d incident terms. Hence

    v_t=a product_(j in t) (1-q_j)/(1-q_j/2),
    a [(1-q_*)/(1-q_*/2)]^L <=v_t<=a,
    alpha=binom(L,3)[q_* /(4-2q_*)]^3.

Other connected components contribute a common independent avoidance factor to N and M. Absorb it into A; all estimates in section 2 still hold, since A/delta=1/[1-product(1-v_t)]. The empty-coefficient term is uniformly small: delta<=eta<=Da, and x log2(e[1+x^-2]) tends to zero with x. Also eta>=d a exp(-O(L q_*)), so A d alpha/delta=O(alpha/a). As D^2 L a<=Lambda, all the errors in (E) tend to zero uniformly. The same proof covers arbitrary branch functions R_j,Q_j satisfying these independence and conditional-probability assumptions.

The target class of all linear hypergraphs is larger: deleting i can leave branches joined by cycles. Pairwise intersections of at most one variable do not supply tensor independence. No step above proves the claimed uniform coefficient for that class.

## 4. A controlled single-active-block law — PROVED

This section concerns the identical-block tree, and the mate spectral marginal. Put delta0=A eta with eta=D b/s, v=b/s, rho=q/(4-2q). Define Q0 as the sum of the squared spectra of H_t, marginalized over all leaves. It has mass delta0. Under Q0/delta0: choose one block uniformly; its L mate indicators are independent fair bits, and all other mate indicators are independent Bernoulli(rho). This is an actual positive mixture.

For the four-mode vectors in section 1, sum |nhat betahat| per mate is (1-q^2)/2. Thus the absolute Fourier overlap of the block vectors is ell=((1-q^2)/2)^L. The L1 distance between the actual h squared spectrum and Q0 (before or after any statistic) is at most

    e=A eta sqrt(eta)[1+sqrt(1+eta)]
        +A D(D-1)(ell/s)^2.                                (TV)

Indeed ||h-H||<=sqrt(A) eta, ||h||<=sqrt(A eta), ||H||<=sqrt(A(eta+eta^2)); multiply the first bound by the sum of the latter two to compare hhat^2 with Hhat^2. The remaining cross terms of Hhat^2 have total absolute mass at most sum_(t!=u) ||Hthat Huhat||_1=A D(D-1)(ell/s)^2, by tensorization. This proves (TV). In either scaling used below, e/delta=O(sqrt(eta)+eta), and tends to zero exponentially in L, up to polynomial factors.

If C_j>=0 has total mass C*, define T_C(Q)=sum_j Q_j log2(1+C_j/Q_j). Concavity, monotonicity and subadditivity in Q imply

    |T_C(Q)-T_C(Q')| <=e log2(1+C*/e)

whenever ||Q-Q'||_1<=e. To check subadditivity, differentiate x log(1+c/x); its derivative decreases, so adding y costs at most the value at y. Apply this coordinatewise to Q<=Q'+|Q-Q'|, and use Jensen for the final sum. This estimate is independent of the number of cells.

## 5. The one-mate witness — PROVED growth; constant offset CHECKED NUMERICALLY

Orient the order backwards: the first mate in this order is the last revealed. In round robin let a cell have its selected mate in block t (1<=t<=D), round k (1<=k<=L), position M=(k-1)D+t. Let C be the N squared-spectrum marginal mass and Q0 the law in section 4. Direct independent Bernoulli counting gives

    C_(k,t)=A rho(1-rho)^(M-1),
    Q0_(k,t)=A v [2^-k(1-rho)^(M-k)
        +rho sum_(u!=t) 2^-m_u (1-rho)^(M-1-m_u)],

where m_u=k for u<t, m_u=k-1 for u>t. The no-mate cell has Q0_empty=delta0 a (1-rho)^((D-1)L), and C_empty=A(1-rho)^(DL). These formulas sum to delta0 and A respectively.

For every nonempty mate cell the leaf coefficient vectors satisfy g=2N-h. If C and Q are their squared norms, the g squared norm lies between (2sqrt(C)-sqrt(Q))^2 and (2sqrt(C)+sqrt(Q))^2. The scalar estimate

    |Phi(P,Q)-Q log2(1+C/Q)|<=10 Q                         (S)

holds throughout this interval. Proof: for C/Q>=4 the ratio P/Q lies in [C/Q,9C/Q], and Phi(P,Q)/Q lies between log2(1+P/Q) and that number plus log2 e. For C/Q<1/16, P/Q<=9/4. On the intervening interval P/Q<=25 and log2(1+C/Q)<=log2 5; these bounds give a discrepancy less than 10. Thus no cancellation of the N and h vectors invalidates (S).

Set u=min(delta,delta0 a+e). Comparing with Q0 by (TV), and separating the no-mate cell (which also contains the actual constant character), yields the explicit error bound

    |L_mates^1 - T_C(Q0)|
       <=10 delta+e log2(1+A/e)
           +Phi(1,u)+u log2(1+A/u).                        (L1)

Here T_C(Q0) is the explicit finite double sum just displayed, including its no-mate cell. It can be computed without any unknown constants.

In the balanced regime v~a, rho~Da/4, D rho=O(1/L), L rho=o(1). The noise part of Q0_(k,t) divided by its active-block part is at most

    2 D rho (1-rho)^(-L).

Consequently C_(k,t)/Q0_(k,t) is between fixed positive multiples (depending only on lambda_+) of D 2^k, uniformly in k,t once L is large. The Q0/delta0 expectation of k is bounded: the active contribution is dominated by 2^-k/D, and the noise contribution by that same bound times 2D rho(1-rho)^(-L). Use sum 2^-k=1 and sum k2^-k=2. The missing no-mate probability is at most a, so its omission costs at most a log D. It follows that T_C(Q0)/delta0=log D+O_(lambda_+)(1). Also delta0/delta=1+O(eta), e/delta=O(sqrt(eta)+eta), and all additional terms in (L1), divided by delta, are O(1). Therefore

    L_mates^1/Inf_root=log2 D+O_(lambda_-,lambda_+)(1).

The explicit finite error is (L1). Numerical results suggest the sharper offset limit 2+log2 e, but that sharper statement is not needed or asserted as proved here.

## 6. The two-mate witness — PROVED boundedness; candidate limit HEURISTIC

Let

    F4=5 log2(5)-4,
    c0=rho^2/[v(1-rho)^2],
    B=min(1,(L+1)a+(7/2)(D-1)rho).

Then the following finite upper bound is explicit:

    L_mates^2/delta <= F4
       +(delta0/delta)[4+log2(1+4c0)
          +B log2(1+4(A+1)/(delta0 B))]
       +(e/delta)log2(1+4(A+1)/e).                          (L2)

Proof. For every mate-window cell, including the empty one, the actual g norm is at most 2sqrt(C)+sqrt(Q)+1[cell empty]. Squaring and using Cauchy-Schwarz gives P<=16(C+1[cell empty])+4Q. Since Phi(P,Q)/Q=F(P/Q), where F'(x)=log2(1+1/x)<=1/(x ln 2),

    Phi(P,Q)<=F4 Q+Q log2(1+4(C+1[cell empty])/Q).

Replace Q by Q0 in the second term using (TV). Split Q0 according to whether both selected mates belong to the chosen active block. Subadditivity of T permits this split without revealing the hidden block in the actual statistic.

If both selected mates are active and the second is in round k>=2, their Q0 component has mass A v 2^-k(1-rho)^(M-k). The N mass of that cell is A rho^2(1-rho)^(M-2), so C/Q_good<=c0 2^k. There are k-1 possible first active rounds. Hence the good contribution divided by delta0 is at most

    sum_(k>=2) (k-1)2^-k log2(1+4c0 2^k)
       <=4+log2(1+4c0),

using sum (k-1)2^-k=1 and sum k(k-1)2^-k=4.

For the bad part, the active block has fewer than two selected mates with probability (L+1)a. Otherwise a background mate must precede the second active mate. Extend fair active bits to infinitely many rounds. Their second success has mean round 4. Averaging the active block position over t, the expected number of other-block positions before this second success is (7/2)(D-1). A union bound on their Bernoulli(rho) selections bounds the remaining bad probability by (7/2)(D-1)rho. Thus bad mass is <=delta0 B. Jensen with total C+1 mass at most A+1 gives its term in (L2).

If lambda_L tends to lambda in (0,infinity), B~7lambda/(8L), c0~lambda/(16L), and log2(1/delta0)=L/2+O(log L). The terms involving e vanish. Thus (L2) proves O(1), and specifically

    limsup L_mates^2/delta <= F4+4+7lambda/16.

The coefficient is loose. A sharper calculation suggests

    L_mates^2/delta -> 2+7lambda/16.                       (H2; HEURISTIC)

Reason: the all-active pair cells have C/Q_good->0 at each fixed round and contribute 2. A single background mate among the last two has probability 7lambda/(8L)+O(1/L^2); its pair usually uses different blocks, where P/Q is of order D. Its entropy cost is that probability times log2 D. Two background mates have probability O(1/L^2) and vanish after multiplication by log D. A uniform tail argument giving the exact limit has not been completed here. tensor_asymptotics.json tests this calculation far beyond the initial table; the approach is slow, so finite data do not certify H2.

## 7. Full windows, mate windows, and the whole-neighborhood witness — PROVED

A full last-r statistic, with leaves revealed before all mates, determines the mate-only last-r statistic. Thus E<=L_full^r<=L_mates^r. They differ only on the event that fewer than r mates occur. Under Q0 this event has probability at most a sum_(j<r) binom(L,j), since it forces the active block to have fewer than r mates. Under the actual q law its mass is at most

    u_r=min(delta,delta0 a sum_(j<r)binom(L,j)+e).

The difference of the two unnormalized conditional entropies is at most Phi(1,u_r). In either scaling discussed here, for fixed r this divided by delta tends to zero. Therefore (L1) proves the full one-window growth, and (L2) proves the full two-window boundedness in the balanced regime. The supplied code's mates-only convention changes neither conclusion; the finite quantities are not exactly equal.

The statistic T intersection B, for B consisting of all root mates, has normalized conditional entropy tending to 2 in both scalings. The proof of section 2 works after summing Fourier coefficients over leaves: Omega depends only on mate inclusion, ||g|| and ||h|| in each nonempty mate cell obey | ||g||-||h|| |<=2||N||, and the same derivative estimate applies to these norms. The empty mate cell contains nonempty leaf characters as well as the actual constant character. Consequently use (E) with its final empty-character term replaced by Phi(1,u_1)/delta. This still tends to zero in the two scalings here. This gives a tested and proved replacement for the fixed window on this model: keep the entire incident neighborhood.

## 8. Every fixed mate window fails in an unbalanced tree regime — PROVED

Fix c>0 and choose integers D with D^2 2^-L ->c. Thus lambda_L~cL, rather than bounded lambda_L. Then at the root

    E_root/delta ->2,

but for every fixed positive integer r,

    liminf_(L->infinity) min_(mate orders pi)
       L_root,mates^(pi,r) / [delta log2 D]
       >= (1/8) P[Poisson(c/4)>=r] >0.                    (W)

The same lower bound holds for full windows among orders putting all leaves first and mates last. The minimum over arbitrary leaf/mate interleavings or over all coordinates is not covered.

Erasure proof: q~c/D, v~a~c/D^2, eta~c/D, L=O(log D). In (E), gamma=O(L^2/D^2), alpha=O(L^3/D^3), eps=O(L^3/D), kappa=O(L^3/D), and every error tends to zero, including the empty-character term. Also (TV) has e/delta->0. These estimates do not require A bounded below: A cancels in every ratio except the harmless empty-character term.

Window proof, uniformly in the mate order. Consider its first D positions, meaning nearest the revelation end. Let k_t be the number from block t; sum k_t=D. At least half the blocks have k_t<=2. Under Q0 choose the active block among these (probability at least 1/2), and require none of its prefix mates selected (probability at least 1/4). On the remaining prefix positions the background marks are independent Bernoulli(rho), with (D-k_t)rho->c/4. Therefore the probability of at least r background marks while no active mate appears is at least (1/8)P[Poisson(c/4)>=r]-o(1), uniformly in the order. The expected number of pairs of background marks in the same block is at most rho^2 L D/2=o(1), since each k_t<=L. Except for this vanishing event, the last r selected mates are in r distinct blocks and all occur in the first D positions. (TV) transfers this probability to the actual normalized q law.

It remains to show that every such observed cell is expensive even though its origin is hidden. For a cell, let C be its N squared mass. In block t let k be its prefix count and j in {0,1} its required selected-mate count. Its N, N-beta cross and beta squared masses, divided by the block N mass, are respectively 1,

    x_t=0 if j=1, else v(1-rho)^(-k),
    y_t=v 2^-k /[rho^j(1-rho)^(k-j)].

Since k<=L, Lrho->0 and exactly r blocks have j=1,

    X=sum x_t=O(c/D), Y=sum y_t=O((r+c)/D),
    NM_cell/C=product(1-x_t),
    MM_cell/C=product(1-2x_t+y_t).

For nonnegative small x,y,

    q_cell/C=1+product(1-2x+y)-2product(1-x)
       <=exp(Y)Y+exp(2X)X^2=O_(r,c)(1/D).

To verify the quadratic term, apply Taylor's formula to F(t)=product(1-t x_t) on [0,2]; |F''(t)|<=exp(2X)X^2. Adding the y factors changes the product by at most exp(Y)Y, by telescoping, since 0<=1-2x_t<=1. For all sufficiently large L, the displayed upper bound can be replaced by 16(r+c+1)/D.

There is a mate in the cell, so the output constant contributes nothing. The p mass is C+MM_cell+2NM_cell>=C for large L. Consequently

    Phi(p_cell,q_cell)>=q_cell[log2 D-log2(16(r+c+1))].

Sum over the prefix cells established above to obtain (W). This completes the proof for every mate order, not just round robin or contiguous blocks.

This is not a refutation of the universal minimum-coordinate conjecture. In fact the finite tree family is ruled out as such a counterexample. A fresh leaf in an attached term has L-1 other fresh leaves that occur nowhere else. Place these private mates last. Whenever the spectral set contains one of them, Nhat is zero and ghat=-hhat, so every corresponding last-one bin costs exactly twice its q mass. On the remaining event the q mass is delta_leaf 2^(-(L-1)), since the derivative factors as the conjunction of those private mates times a function of the other variables. Therefore

    L_leaf^1/delta_leaf <=2+Phi(1,delta_leaf 2^(-(L-1)))/delta_leaf.

For the supplied tree let m=D+DL(D-1) be its number of terms. Harris positive association of the decreasing term-failure events gives A_leaf>= (1-a/2)^(m-1). The shortest-term lower bound proved independently in section 12 gives delta_leaf>=a[1-L(D-1)a] A_leaf. In the scaling D^2 a->c, log2(1/delta_leaf)=O_c(L), so the extra term above is O_c(L 2^-L). Section 12 also bounds every coordinate's erasure ratio below by 2-o(1). Consequently the minimum over all coordinates and all orders of the one-element witness in this finite tree family tends to 2. Every larger fixed window has the same bounded minimum. Regularizing the tree to remove private boundary variables and controlling all interleavings at interior coordinates are separate unresolved steps.

## 9. Exact optimization of any finite window — PROVED

Use the reverse revelation order, and let R be the prefix already visited. When a new j is visited, a size-r observed window is first completed precisely when its other r-1 members form K subset R. The corresponding cell is

    T intersection (R+{j})=K+{j}.

Its mass depends only on R and j, not on the earlier ordering within R. Every size-r window appears exactly once this way. Sets of size less than r contribute their exact-coefficient entropy independently of order. Let avoid_p(A)=sum_(T misses A) p(T), and similarly for q. For J=K+{j}, inclusion-exclusion gives the cell mass

    p_J(R+{j})=sum_(B subset J) (-1)^(r-|B|) avoid_p((R+{j}) minus B).

Thus the minimum is a shortest path on subsets:

    dp(empty)=sum_(|T|<r)Phi(p(T),q(T)),
    dp(R+{j})=min(dp(R+{j}),dp(R)
        +sum_(K subset R, |K|=r-1)Phi(p_(K+j)(R+j),q_(K+j)(R+j))).

window_search.py implements this recurrence and verifies selected optimal orders by direct spectral binning. windows_validate.json also compares it with every permutation on small random truth tables, independently of the recurrence. The scope of finite minima and symmetry representatives is recorded per case in windows_scan.json.

## 10. A neighborhood that must grow on PM towers — PROVED formula; CHECKED numerical values

Use the balanced monotone 18-input PM host of FEIB19. Its core influence is a0=57/256 (verified directly from ../FEIB16/pm_record_spectrum.npy). Follow an all-core leaf path. At total depth t its influence is a0^t. Keep all the other input variables of the bottom k-level subtree as the observed neighborhood B, and forget all outside variables. Let R_k be that subtree's exact normalized erasure ratio. Then

    H(1[i in U] | U intersection B)/Inf_i
      = R_k+Phi(1-alpha,alpha d_k^2)/(alpha d_k),
    d_k=a0^k, alpha=a0^(t-k).                             (PMB)

Proof. Write the full composition as F0(Z)+g(Y)F1(Z), where g is the balanced bottom subtree. The empty inner Fourier coefficient is zero, so after summing squared coefficients over Z, the p marginal on Y minus i is (1-alpha)1_empty+alpha p_inner, and q is alpha q_inner. Also alpha=||F1||^2 and the inner singleton coefficient is d_k, by monotonicity. The empty p_inner coefficient is zero. Nonempty bins contribute alpha times the inner erasure; its empty bin contributes zero. The displayed extra term is the entire empty observed-neighborhood cell. This proves (PMB).

For fixed k and t tending to infinity the extra term is

    d_k[(t-k)log2(1/a0)+2log2(1/d_k)+log2 e+o(1)],

so every such fixed-bottom-depth neighborhood fails. Conversely take k=min(t,ceil(2 log(t)/log(1/a0))) (and k>=1). Then d_k<=t^-2 and t d_k tends to zero. FEIB19's fixed-gate tower argument bounds R_k, so this growing neighborhood has a bounded ratio, approaching the all-core erasure limit. extra_checks.json independently computes R_k using grouped exact dyadic gate masses and high-precision scalar Phi, and checks against the all-core states in FEIB19/pm.json. The minimum over all PM path types can differ slightly from the all-core erasure; the check compares like with like.

For this tower, the optimized one-element filtration already stays bounded by the prior exact composition theorem. A large fixed local block can therefore be worse than a carefully ordered one-element statistic. The tree example and PM example require different structure; neither suggests that a single fixed-radius neighborhood is universally sufficient.

## 11. The largest-influence coordinate need not be good — PROVED; CHECKED NUMERICALLY

Let k be even, B(y) a bent Boolean function on k bits (for example the sign of the sum mod 2 of disjoint pair products), and a=2^-k. Replace its value at one point y* by a fresh root x:

    f(x,y)=B(y) for y!=y*, and f(x,y*)=x.

At the root, h=1[y=y*], delta=a, and hhat(T)^2=a^2 for all T. The g coefficients have magnitudes between sqrt(a)-a and sqrt(a)+a. Since Phi(p,q)/q=log2(p/q)+log2 e+O(q/p) when p/q tends to infinity,

    E_root/delta=k+log2 e+O(sqrt(a)).                       (MAX)

Now replace each y_j by a disjoint balanced depth-d MAJ3 tower. Its leaf influence is 2^-d. The root's influence and erasure ratio are unchanged: because the inner gates are balanced, each spectral set of outer y variables expands into disjoint nonempty-block supports; within each expanded support p and q have the same conditional distribution. Phi is homogeneous, so summing those conditional probabilities preserves erasure exactly. A new leaf has influence Inf_(y_j)(f) 2^-d<=2^-d. Choose d=k+1. Then every other influence is strictly below a, while (MAX) diverges. The root is the unique largest-influence coordinate and is not good with any universal coefficient.

extra_checks.json verifies preservation using complete truth tables with the two-bit bent gate and MAJ3 depths zero, one and two. The 19-variable example already has a unique maximum at the root. The unbounded conclusion is the symbolic bent-family argument, not that finite numerical example. This refutes the general maximal-influence proposal in FLOW 7(i); it does not refute a smallest-ratio choice or the largest-weight theorem for linear thresholds.

## 12. Linear hypergraphs without branch independence — PROVED

This strengthens section 3 and closes its cycle gap in the parameter range stated below. It does not require an acyclic incidence graph.

Let f be a monotone uniform width-w DNF, every pair of terms sharing at most one variable, with maximum variable degree D. Set L=w-1, a=2^-L. Fix a live coordinate i of degree d. For an integer k with 1<=k<=L, put

    gamma_k=a sum_(j<k) binom(L,j),
    theta=1-L(D-1)a-(d-1)a/2,
    alpha_k=binom(L,k) 2^(binom(k,2)-2k) [(D-1)a]^k
                /[1-k(D-1)a/2],
    eps=min(1,d gamma_k),  kappa=alpha_k/(a theta).

Assume theta>0, k(D-1)a<2, and d a<=1/4. Then

    |E_i/Inf_i-2| <= 2eps+(8/ln 2)sqrt(kappa)
       +eps log2(e[3+8/(eps d a theta)])
       +d a log2(e[1+(d a)^-2]).                          (LIN)

This is a numerical certificate with no hidden constants. A zero eps term is interpreted by continuity. In particular its upper coefficient is 2 plus the right side, and if that side is <=1 the coefficient is 3.

Corollary. Fix any epsilon>0. For monotone uniform width-w linear DNFs with

    D<=2^((1-epsilon)(w-1)),

uniformly over their size and every live coordinate,

    E_i/Inf_i=2+o_(w->infinity)(1).

Indeed take a fixed k>1/epsilon (and then L>=k). eps is at most a fixed polynomial in L times 2^(-epsilon L), while kappa is at most a fixed polynomial in L times 2^((1-k epsilon)L); all terms in (LIN) tend to zero. Thus coefficient 3 applies eventually, with the threshold certified by (LIN). More generally the explicit certificate applies to any parameters for which its right side is small. Mere D 2^-w ->0, without a rate, is not covered by this corollary.

Proof, step 1: normalize by the no-background probability. Let N be the indicator that every term not containing i fails. Let A_t be the conjunction of the L mates in the t-th term through i. These mate sets are disjoint by linearity. Then

    M=N product_t(1-A_t), h=N-M=N 1[OR_t A_t], g=N+M-1.

Put A=E N. For one incident term t let R be the indicator that all background terms not meeting its mate set fail. Every remaining background term meets that set in exactly one mate; after fixing all its mates to 1 it has L other literals. Conditional on R=1, the probability that any such remaining term fires is at most L(D-1)a. This uses Harris's inequality: an increasing event and a decreasing event have nonpositive covariance under the product measure. R depends only on variables outside the chosen mate set. Hence

    P[A_t,N] >= a P[R](1-L(D-1)a)
                >=a A(1-L(D-1)a).

For distinct incident terms s,t, A_s A_t is increasing and N decreasing, so

    P[A_s A_t | N=1] <=P[A_s A_t]=a^2.

Bonferroni therefore gives

    delta/A=P[OR_t A_t | N=1]>=d a theta.

The corresponding upper bound is delta/A<=d a, again by Harris and a union bound. In particular delta<=d a.

Step 2: derivative spectrum is dense in an incident term. Partition the pivotal points according to their first satisfied A_t, and write h=sum_t h_t for the disjoint nonnegative pieces. Each h_t is supported on the subcube fixing the t-th L mates to 1, so h_t=A_t Psi_t on the remaining variables. Its squared Fourier law is uniform on those mates, independently of the other variables. Let Omega consist of Fourier sets containing at least k mates of at least one incident term. For every h_t, the normalized squared mass outside Omega is <=gamma_k. Cauchy-Schwarz pointwise across the d summands and Parseval, followed by disjointness of their physical supports, give

    sum_(T outside Omega) hhat(T)^2
       <=d sum_t sum_(T outside Omega) hthat(T)^2
       <=d gamma_k sum_t ||h_t||^2=d gamma_k delta.

No tensor independence among branches was used.

Step 3: background high-mate mass. Fix k distinct mates J from one incident term. No background term can contain two variables of J, by linearity with that incident term. Thus, with all other variables fixed,

    N=R product_(j in J)(1-z_j Q_j),

where R avoids all background terms containing no member of J, and Q_j is the OR of at most D-1 width-L residual conjunctions, depending on no z variable in J. Walsh differentiation gives exactly

    ||D_J N||_2^2=4^-k P[R=1, Q_j=1 for every j in J].

The event intersect_j{Q_j=1} is increasing and R decreasing. Expand that event by choosing one residual term for each j. The chosen background terms are all distinct, and any two residual variable sets intersect in at most one variable. Their union has size at least kL-binom(k,2): adding the pairwise-overlap subtraction is a valid lower bound even if three or more sets share a point. Therefore

    P[all Q_j=1 | R=1]
       <=P[all Q_j=1]<=(D-1)^k 2^binom(k,2) a^k.

Also A=E N>=P[R](1-k(D-1)a/2), by a union bound over the random z_j and the conditional activation probabilities. Hence

    ||D_J N||_2^2/A
       <=2^(binom(k,2)-2k) [(D-1)a]^k/[1-k(D-1)a/2].

Summing over k-subsets of a mate block bounds the squared spectral mass containing at least k of its mates; sum over the d incident blocks to obtain

    sum_(T in Omega) Nhat(T)^2 <=A d alpha_k
                                <=delta alpha_k/(a theta).

Step 4: entropy. Omega excludes the actual empty Fourier set. On it ghat=2Nhat-hhat, so the derivative estimate of section 2 gives discrepancy at most (8/ln 2)delta sqrt(kappa) from 2 times its h mass. The q mass outside is <=eps delta. For nonempty coefficients there, p<=8Nhat^2+2hhat^2, so its entropy is at most

    eps delta log2(e[3+8A/(eps delta)])
       <=eps delta log2(e[3+8/(eps d a theta)]).

At the actual empty coefficient hhat(empty)=delta. Its cost is <=delta^2 log2(e[1+delta^-2]); because delta<=d a<=1/4, x log2(e[1+x^-2]) is increasing on this interval, giving the last term in (LIN). Adding the missing 2eps delta proves the theorem.

For completeness, Harris's inequality used here follows by induction on independent bits. In one bit, the covariance of functions F,G is p(1-p)(F(1)-F(0))(G(1)-G(0)), nonnegative when both are increasing. Conditional covariance plus the covariance of conditional means proves the increasing/increasing statement by induction. Replace G by -G to obtain the increasing/decreasing version. Thus no assumption about correlations inside the conditioned zero set was introduced.

## 13. The universal statement and next lemma — HEURISTIC / OPEN

The final one-page statement is BELIEF.md. It retains the averaged deletion-cost form of FEI, rejects a maximal-influence rule, and identifies a mixed-width high-mate separation lemma as the first concrete next target. No universal fixed-window theorem or counterexample is asserted.
