# Proofs

All logarithms are base two. Phi(a,b)=(a+b)h(b/(a+b)), with its continuous values on the axes. A minimum over coordinates excludes zero influences.

## Target-block exchange lemma — PROVED

Let f(x_B,z)=F_0(z)+g(x_B)F_1(z), with g Boolean, and target i in B. Write r=E g, c=ghat({i}). For already revealed sets R inside B minus i and S outside B, put

    a(R)=sum_{T subset R} ghat(T)^2,
    b(R)=sum_{T subset R} ghat(T+i)^2,
    u(S)=sum_{T subset S} (F0hat(T)+r F1hat(T))^2,
    v(S)=sum_{T subset S} F1hat(T)^2.

The cumulative squared masses for f are exactly

    A(R,S)=u(S)+(a(R)-r^2)v(S),   B(R,S)=b(R)v(S).

Consider adjacent steps: an inside step with increments d=(da,db), and an outside step with increments du,dv. All four increments are nonnegative. At the old inside set the outside edge has vector

    X=(du+(a-r^2)dv, b dv).

Inside then outside costs v Phi(d)+Phi(X+dv d). Outside then inside costs Phi(X)+(v+dv)Phi(d). Superadditivity gives Phi(X+dv d)>=Phi(X)+dv Phi(d). Thus moving the outside step earlier weakly decreases total cost. Repeated adjacent exchanges put every outside coordinate before every inside coordinate. The internal and external orders are preserved.

Consequently, with alpha=||F1||_2^2 and L*(g,i) the minimum over inside orders,

    L*(f,i)=alpha [L*(g,i)-Phi(r^2,c^2)]
             + min_sigma sum_k Phi(U_k,c^2 V_k),

where U_k,V_k are the martingale energy bins of F0+rF1,F1 in the outside order sigma, including k=0. This is an equality, not only an upper bound. Constants and alpha=0 have the evident limiting interpretation. No claim that all outside blocks can be kept contiguous follows just from this lemma.

## Read-once AND/OR formulas — PROVED

Fix any leaf i. At an AND node, let the target child's success probability be p, and let Q(z) be the indicator that all other children succeed. Up to output sign, f=1-2 p Q+(g-Eg)Q. For every nonempty outside spectral set the erasure pair has a common amplitude ratio: its squared endpoints are 4p^2 Qhat(T)^2 and c^2 Qhat(T)^2. Thus the entire nonempty outside portion has constant conditional inclusion probability. The empty set is its own bin. Every outside ordering therefore has its coarse entropy equal to the exact outside erasure entropy. At an OR node use failures in place of successes. The inside nonempty bins are scaled copies of the target child's bins.

Induction from a dictator, for which both costs vanish, proves L*(f,i)=E_i(f) for every leaf of every read-once AND/OR formula, allowing constants and negated literals. A realizing order visits off-path sibling subtrees before entering the child containing i, recursively. The order inside each off-path subtree is immaterial at the parent step. The exchange lemma proves this order is globally optimal.

The class is closed under restriction after simplifying constants. Since sum_i E_i<=H and the established read-once AND/OR FEI theorem gives H<=10 I, some leaf has L*<=10 Inf_i. The coefficient 10 uses Chakraborty–Kulkarni–Lokam–Saurabh, Theorem 5.11 and Remark 5.1; the source and scope are recorded in LITERATURE.md. The new ingredient here is equality of the optimized filtration cost and exact erasure, not a new proof of their entropy theorem. The XOR identity below extends equality and coefficient 10 to arbitrary read-once AND/OR/XOR/NOT formulas.

## XOR of disjoint functions — PROVED

For f=g(x)h(z), squared Fourier measures tensorize. For i in g, the exchange lemma puts z first. Its outside vector is everywhere proportional to (r^2,c^2), so the external contribution is exactly Phi(r^2,c^2). Hence L*(f,i)=L*(g,i), and Inf_i(f)=Inf_i(g). The minimum coordinate ratio is the smaller component ratio. Iterated XOR cannot increase it. Exact erasure has the same tensorization property.

## All composition blocks can be respected — PROVED

For f=F(g_1,...,g_w), let r_l=E g_l, v_l=1-r_l^2, c=ghat_j({i}) for the target block j, and

    K_A=sum_{D containing A} Fhat(D) product_{l in D minus A} r_l.

After the target-block exchange, all other blocks precede block j. A partially revealed outside block l enters the cumulative masses only through

    x_l=sum_{nonempty T subset revealed_l} ghat_l(T)^2,  0<=x_l<=v_l.

The two cumulative masses are multiaffine polynomials in the x_l, with nonnegative coefficients:

    P(x)=sum_{B subset [w] minus j} K_B^2 product_{l in B} x_l,
    Q(x)=c^2 sum_B K_{B+j}^2 product_{l in B} x_l.

On a step in block l, the edge vector is dx_l times (partial_l P,partial_l Q), which is independent of x_l. To consolidate a block l, hold the order of all other coordinates fixed and allow its total mass v_l to be allocated among the slots in that order. Costs of l-steps are linear in their allocated masses. Every other step's two masses are affine in the cumulative allocation of block l at that slot, so its Phi cost is concave in the allocation vector. Total cost is concave on the simplex of nonnegative allocations summing to v_l. At least one simplex vertex has cost no larger than the original allocation. A vertex puts all of block l in one slot, and can be implemented by its actual coordinates in any internal order.

Consolidate blocks one by one. Treat already consolidated blocks as indivisible steps, so available slots are their boundaries. The original allocation is feasible because these blocks are contiguous; the same concavity argument applies, and no prior block is split. Thus an optimum respecting every block exists. This is an existence theorem: interleaved orders can also tie.

For B subset outside blocks define

    p_B=K_B^2 product_{l in B} v_l,
    q_B=c^2 K_{B+j}^2 product_{l in B} v_l,
    alpha_j=sum_B K_{B+j}^2 product_{l in B} v_l.

Let DP(p,q) denote the subset-chain shortest path applied to these two possibly unnormalized measures on outside block patterns. The exact composition law is

    L*(f,i)=alpha_j [L*(g_j,i)-Phi(r_j^2,c^2)] + DP(p,q).

Inf_i(f)=alpha_j Inf_i(g_j). The DP has w-1 block coordinates, rather than the number of underlying variables. In particular, arbitrary fan-in symmetric AND/OR nodes admit the scalar formula below. All inequalities in the proof are non-strict and continuous, so zero coefficients and constant siblings are allowed after dropping irrelevant blocks.

## Exact AND/OR recursion — PROVED

For an AND of children, write p for the target child's success probability, alpha for the product of the other success probabilities, d=Inf_i(child), c=childhat({i}), r=1-2p, and b=1-2p alpha. If L is the child's optimal unnormalized cost, then

    L_new = alpha [L-Phi(r^2,c^2)]
            +(alpha-alpha^2) Phi(4p^2,c^2)+Phi(b^2,c^2 alpha^2).

For OR use failure probabilities. This is exact for nonidentical children as well. It agrees with the exact E recursion, hence L*-E propagates by multiplication by alpha and the normalized gap is inherited unchanged. In particular, AND_w of an identical symmetric g has F-E=L*(g,i)/d-E_i(g)/d exactly, for every w, not merely in the small examples.

## Bounded degree and sensitivity — PROVED

If deg(f)<=d, every nonzero D_i f is a nonzero polynomial of degree at most d-1, so its support has density at least 2^{-(d-1)}. The support bound follows by induction on degree, selecting a variable in a highest monomial and using the nonzero derivative on at least half of the relevant fibers. Since Boolean D_i f takes values in {0,+1,-1}, this density equals delta. Thus every order at every live coordinate has L/Inf<=d-1+log2(e). The degree class is restriction closed.

If the maximum sensitivity is at most s, consider the pivotal set of i on the other variables. At each point inside this set both i-endpoints are sensitive in i. A direction exiting this set must be sensitive at at least one endpoint, so each inside vertex has at most 2s-2 exiting directions. The cube edge-isoperimetric inequality gives log2(1/delta)<=2s-2. Consequently every order has L/Inf<=2s-2+log2(e). This class is also restriction closed.

## Adaptive input filtrations — FALSE in the naive form; a valid replacement is PROVED

For an actual adaptive tree on the input values outside i, group squared martingale increments of E_i f and D_i f by query depth and apply Phi. This need not dominate E_i(f). audit.json contains a fully specified four-variable Boolean counterexample and the two energy lists. The same root-to-leaf orthogonal decomposition preserves total energies but it mixes characters; its bins are not spectral coarse-grainings. The data-processing proof of 12(b) no longer applies. Grouping by individual tree nodes can only decrease the depth-grouped cost, so that variant fails as well.

Explicitly, use truth-table hexadecimal b6a4 (bit x=1 means f((-1)^x)=-1), with i=1 in zero-based coordinates. Reveal coordinate 0 first. If its input bit is 0, reveal 2 then 3; if its bit is 1, reveal 3 then 2. Including the root mean bin, A=(0,1/16,1/16,3/8) and B=(0,1/16,5/16,1/8). Their Phi sum is 0.7743974703476992 bits, below E_i=1 bit.

A correct input-adaptive statement is the following. Draw an independent uniform input Y, run any adaptive query policy on Y outside i, and complete its path to a permutation pi(Y). Define the cost by the spectral bins for this permutation, rather than by the actual tree's martingale increments. Then

    E_i(f)<=E_Y L_i^{pi(Y)}.

This follows pointwise in the sampled permutation from 12(b). It also bounds D_i after adding (2/ln 2)Inf_i. Adaptivity of this independent order sampling cannot beat the best deterministic permutation. A separate valid spectral-adaptive statement lets a decision tree query membership bits of T=U minus i; its leaf is a statistic of T, and its conditional entropy bounds E_i by data processing. These statements distinguish input values from spectral membership.

## Limits of the class conclusions

PROVED: width-one monotone DNFs and read-once DNFs of any width have coefficient 10 by the AND/OR result above. OPEN: all monotone width-w DNFs with overlap, with a width-only filtration coefficient. OPEN: arbitrary expected-depth-d trees with a coefficient depending only on d. A class defined only by the expected depth of a supplied tree is not restriction closed with the same parameter: a rare branch can contain an arbitrarily deep hard subtree. A maximum-depth-d tree has degree at most d and is covered by the degree bound.

OPEN: FWC for arbitrary read-once majority/threshold formulas, with one constant uniform in depth and unbounded fan-in. The exact composition theorem reduces numerical optimization to gate-size DPs; the known FEI composition theorem alone does not bound this stronger witness. Regular fixed-gate towers and the numerical scopes are treated in FAMILIES.md. Section 11's proved level-witness result does not logically establish a bound for a maximum-position witness; the two statistics do not refine each other. Its assertion about decreasing-weight filtration orders requires its own argument or a separate partial-refresh inequality.

## Linear threshold functions: a deterministic-tail proof — PROVED

Take a coordinate of largest weight a>0, make the function monotone by input negations, remove zero weights and perturb the threshold to avoid ties while preserving the truth table. Write h=1[|s|<a] and g=sgn(s)1[|s|>a]. Reveal the other coordinates in any fixed order. For the tail before reveal K, let sigma_old^2 be the sum of squared unrevealed weights; after reveal K let sigma_new^2 be the corresponding sum. Every weight is at most a, hence sigma_old^2<=sigma_new^2+a^2.

Conditioned on any prefix, the tail is a symmetric Rademacher sum U with steps at most a and variance sigma^2. FLOW Lemma 11(j) gives

    P[U>t+a] <= (16/3)(1+sigma/a) P[|U-t|<=a],  t>=0.

Its proof uses bounded-step overshoot, Levy's maximal inequality, Chebyshev, and the interval comparison 11(i). It is independent of how the prefix was chosen; here the prefix is fixed rather than adaptively chosen. Conditional crossing has probability at most 2 P[U>a+|A|], where A is the prefix sum minus the threshold. Averaging the window probability over A is delta. Therefore

    Cross_(K-1) <= (32/3)(1+sigma_old/a) delta.

For a tail with standard deviation sigma, Berry–Esseen with universal constant at most 1 gives concentration in every interval of length 2a at most (2/sqrt(2pi)+2)a/sigma<=3a/sigma, since sum w_j^3<=a sigma^2. Use the bound 1 when sigma=0. Conditional independence of the two tails gives

    Stay_K <= delta min(1,3a/sigma_new).

For x=sigma_new/a, the product of the two displayed factors is bounded by

    (32/3)(1+sqrt(1+x^2)) min(1,3/x)
      <=(32/3)(2+x)min(1,3/x)<=160/3.

Thus Cross_(K-1) Stay_K<=(160/3)delta^2 and the pair identities imply A_{>=K}B_{<=K}<=(323/3)delta^2. Section 12(e) now gives the explicit filtration coefficient

    C_LTF = 1/ln(2)+4+2 log2(1+2*(323/3)).

This proves FWC for all linear threshold functions, in fact with every order at the largest-weight coordinate. The class is restriction closed. This coefficient is deliberately conservative. constants.json evaluates it; no optimized constant is claimed. Berry–Esseen is used in its independent, not necessarily identically distributed, form; primary references are recorded in LITERATURE.md.

## A general reveal rule — PROVED bound; CHECKED quality only

At the current revealed set R, for each remaining j form its two-component mass increment d_j and the still unrevealed mass vector t-d_j. Choose j minimizing Phi(d_j)+Phi(t-d_j), breaking ties by coordinate index. Repeat, evaluate the resulting L, and choose the live target i minimizing L/Inf_i. This is the deterministic greedy rule implemented in search.py. Each step refines the two-bin spectral partition, so its final cost is between E_i and h(Inf_i). It has no proved absolute approximation ratio. policy.json compares it with the exact shortest path on the supplied small families and stored hill-search examples. The tree-distance order is exact on read-once AND/OR/XOR/NOT formulas; on a general truth table this greedy rule is only a heuristic.

## Fixed balanced monotone gate towers have bounded witnesses — PROVED

Let a fixed balanced monotone gate have live influences alpha_j, all below 1. Write a=max_j alpha_j<1. At a target leaf the inner singleton coefficient equals its influence d. Block composition adds

    DP(p,d^2 q)/(alpha_j d)

to the normalized inner witness, with the fixed gate's outside edge measures p,q. For any fixed outside order let its bin masses be A_k,B_k, so sum B_k=alpha_j. Since

    Phi(A,d^2 B)<=d^2 B [2log2(1/d)+log2(1+A/B)+1/ln(2)],

the increment is at most d[2log2(1/d)+C_j], where

    C_j=1/ln(2)+sum_k B_k log2(1+A_k/B_k)/alpha_j.

The optimum is at most that fixed-order value. Along a depth-t path d<=a^(t-1). For sufficiently large t, x log(1/x) is increasing on [0,a^(t-1)]. Hence all path tails are bounded by a convergent series. All finite-depth minima are nondecreasing, because every extension adds a nonnegative cost. They converge to a finite limit, with the following enclosure after depth q whenever a^q<=1/e:

    remaining <= a^q {2log2(1/a)[q/(1-a)+a/(1-a)^2]+max_j C_j/(1-a)}.

The same upper bound covers exact erasure because E<=L binwise and the exact edge formula has the analogous positive increments. The PM path dynamic program retains a minimum for each number of core choices, since d depends only on that number and the depth; this computes the minimum over all coordinate type words, not just the all-core path. pm.json records both the finite minimum and its analytic tail bound. native_audit.json independently verifies the all-core minimizing candidate's outside DPs in long double.

For any balanced transitive monotone fixed gate, alpha_j=alpha and every leaf is equivalent. Jensen gives the simpler fixed-order constant C<=log2(1/alpha)+1/ln(2), since sum A=1-alpha and sum B=alpha. This applies to odd majority and the Fano gate. Thus their growth in depth is O(1), with a tail of order q alpha^q. This statement concerns these fixed regular towers; their full restriction closures are larger classes.

## The large erasure/filtration gap — PROVED exact recursion, CHECKED numerical limit

Let the seven variables be the nonzero points of F_2^3, and take the DNF whose terms are its seven lines {a,b,a+b}. Any two lines intersect. Every two-coloring has a monochromatic line: a line-free subset has at most four points, and a line-free four-set is an affine plane whose complement is a line. Thus exactly one color contains a line. The Boolean output is odd under simultaneous input negation. Its coordinate influence is exactly 9/32 (integer Fourier/direct truth-table checks), and its optimized filtration cost is computed by the six-coordinate DP.

Every recursive composition of this gate is still odd and transitive. Therefore E_i=0 at every coordinate, while its F ratio is the positive scalar tower series from the preceding theorem. The exact series is specified by the finite base spectrum and the DP recurrence; final_checks.json evaluates it at 90 decimal digits through depth 40 and bounds the remaining tail. The limit is approximately 4.601671597979309 bits per unit influence. Hence the optimized-filtration-minus-erasure gap can exceed four even in an odd monotone transitive family; this construction has bounded, rather than divergent, gap.

## Other structural growth statements — PROVED

Uniform bent spectra give F=2, since every bin has equal p and q masses and Inf_i=1/2. For the complete quadratic on odd n>=3, the spectrum is uniform on an affine parity hyperplane. The empty and first-position bins are pure, while every later bin has equal endpoint masses. Thus E_i=0 and F=2-2^(3-n), tending to 2. If r truth-table values of an even-dimensional bent function are changed, every influence remains at least 1/2-2r/2^n, because each changed vertex touches one i-edge. For r=o(2^n), the trivial entropy bound yields F<=2+o(1). These sparse quadratic corrections therefore cannot refute FWC.

For an address gate, reveal address coordinates before other data blocks and leave the target data block last. The q support has no other data block, while p requires one, so every bin is pure and a data coordinate has L=0. Iterating balanced address gates retains a data-path coordinate of zero cost. Disjoint XOR inherits the smaller component F. AND/OR of copies of a fixed inner function inherits its normalized L-E gap exactly; its extra terms in the scalar recursion have finite limits as the copy count tends to infinity. In particular AND_w of MAJ_r has gap precisely the one-gate majority filtration ratio for every w. Pure read-once AND/OR/XOR/NOT families have growth O(1), bounded by 10 even when widths and depths vary.

For the other projective-plane/Steiner DNFs, overlapping cyclic DNFs and threshold-density random DNFs, the computed tables are finite exact optimizations (with floating logarithms). No uniform boundedness or divergent asymptotic is proved. The general influence granularity gives only O(n) as n grows. For arbitrary invertible linear changes of variables the entropy is preserved, but neither influences nor F are invariant; the scans are finite checks rather than asymptotic claims.
