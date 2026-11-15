# Containment, cancellation, and the logarithmic loss

Worker FEIB08. All logarithms in our identities and numerical calculations are base 2, except the explicitly named natural logarithm L. Parameter constants transcribed from KKLMS use that paper's natural-log convention; conversion changes only absolute constants. Truth-table bit x set means f(x)=-1. Constants denoted C can change from one inequality to another. This document gives a proof skeleton of the cited paper, and separate complete proofs of the elementary reductions and obstructions used here. It does not prove FEI or FMEI.

## 1. Normalization and what the three theorems actually say

Write a_S=hat f(S), mu(S)=a_S^2, up(R)=sum_{S superset R}mu(S), I=sum_S |S|mu(S), and v=1-mu(empty). K=I/v for a nonconstant Boolean function. Put c_R=D_R f, alpha(R)=E|c_R|, and p(R)=Pr(c_R !=0).

The paper is [Kelman, Kindler, Lifshitz, Minzer, Safra, Towards a Proof of the Fourier–Entropy Conjecture?, arXiv:1911.10579v2](https://arxiv.org/html/1911.10579). It uses {0,1}-valued functions and natural logarithms. For b=(1-f)/2, nonempty Fourier coefficients, derivatives, and generalized influences are respectively -a_S/2, -c_R/2, and up(R)/4. Both the Fourier-energy influence from Definition 2.3 and variance scale by 1/4, so K is invariant. The introductory combinatorial influence has a different factor, explicitly noted before Definition 2.3; its effect is absorbed in absolute constants here. Its generalized influence is exactly our up after this scaling. Its block-intersection quantity in section 5 is a different, sharper object, defined below.

In our normalization, with changes to absolute constants, the introductions's statements are:

* Theorem 1.1: some nonempty S with |S|<=10K satisfies |a_S|>=sqrt(v) 2^(-C|S|log(1+K)).
* Theorem 1.2: for every eta>0 there is C_eta such that sum_{|a_S|<=2^(-C_eta K log(1+K))}mu(S)<=eta v. A constant factor in the coefficient threshold is absorbed in C_eta when changing normalization.
* Theorem 1.3: H_{<=D}=sum_{|S|<=D}mu(S)log(1/mu(S)) <= C sum_{|S|<=D}|S|log(|S|+1)mu(S)+CI.

Theorems 1.2 and 1.3 are concentration and entropy statements. They are not themselves stated as bounds on up(R). That distinction matters when tracing the loss.

## 2. Dependency skeleton of KKLMS

The following is the dependency list for sections 2–7.3. Earlier versions of the argument in sections 4 and 5 are included so that the difference between the first subset count and the final proof is visible. Section 7.4's symmetry application is not needed here.

For a real g, let up_g(R)=sum_{S superset R}hat g(S)^2 and I(f,g)=sum_i sqrt(up_f({i})up_g({i})). Let L(f,g)=(sum_S |a_S hat g(S)|^(4/3))^(3/4), restricted to the relevant degree band. A band (alpha,d) means alpha d<=|S|<=d on the Fourier support of g.

| Paper statement | What is controlled in our notation | Role |
|---|---|---|
| Fact 2.1 | Inner products are sums of products of Fourier coefficients | Parseval/Plancherel |
| Definition 2.3, Fact 2.4 | sum_{|R|<=r}up_{f<=d}(R)<=2d^r ||f||_2^2 | First, expensive count of generalized influences |
| Definition 2.5, Lemma 2.6 | E_z I(f restricted to J,g restricted to J)<=sum_{i in J}sqrt(up_f(i)up_g(i)) | Cross-influence survives restrictions; summing disjoint live blocks pays only once |
| Lemma 2.7 | E_z hat(g restricted to J)(T)^2=sum_{U:U intersection J=T}hat g(U)^2 | Exact intersection masses, not just up(T) |
| Theorem 2.8 | ||h||_q<=(q-1)^(degree(h)/2)||h||_2, q>=2 | Hypercontractive price for restoring information from restrictions |
| Lemma 3.3 | Pr[a block intersection has relative error >epsilon]<=2 exp(-epsilon^2 |S|/(3m)) | Binomial concentration; union over m blocks |
| Corollary 3.4 | Some m-block partition preserves at least 1-2m exp(-epsilon^2 alpha d/(3m)) of sum |a_S hat g(S)| in well-sized intersections | Deterministic partition after averaging |
| Lemma 3.5 | E max_T h_T^2<=3^q max_T ||h_T||_2 (sum_T ||h_T||_2^2)^(1/2) | Exchange maximum and expectation, with degree q in outside variables |
| Lemma 4.3 | <f,g><=(d/delta)^d max|a_S hat g(S)|+2 delta^(1/8)3^(d/4) I(f,g) | KKL base case: high-influence coordinates counted; other coordinates use Holder and hypercontractivity |
| Theorem 4.1, equation (4) | <f,g><=C1 max|a_S hat g(S)|+C2 I(f,g)+C3||f||_2||g||_2 | First multiscale induction using up(R) |
| Corollary 4.2 | Replaces the recurrence by C1=delta^(-2^(O(1/epsilon))d) and small C2,C3, requiring delta<=2^(-4d^epsilon) | First explicit parameter choice |
| Lemma 5.1 | E(sum_T |h_T h'_T|^(4/3))^(3/4)<=3^q max_T(||h_T||_2||h'_T||_2)^(1/4)(sum||h_T||_2^2 sum||h'_T||_2^2)^(3/8) | Uses both restricted functions to improve the exponent in the induction |
| Lemma 5.3 | Same as Lemma 4.3, with first term (d/delta)^(d/4)L(f,g) | Holder replaces maximum by a 4/3 norm |
| Theorem 5.2, equation (8) | <f,g><=C1 L(f,g)+C2 I(f,g)+C3||f||_2||g||_2; C1=2^k(2/delta_k)^((1+epsilon)d_k/(4d_{k-1})) | Uses exact intersections, deleting the d_k^((1+epsilon)d_k) loss of Theorem 4.1 |
| Corollary 5.4 | <f,g><=delta^(-6d)||f||_2^(3/4)||g||_2^(3/4)max|a_S hat g(S)|^(1/4)+delta^(1/16)I(f,g)+delta||f||||g|| | Still needs d^epsilon>=100 log d/(alpha epsilon), delta<=2^(-16d^epsilon/epsilon) |
| Fact 6.1 | C(d,r)>=[16 sqrt(r)]^(-1)d^d/((d-r)^(d-r)r^r) | Stirling lower bound |
| Fact 6.2 | Pr[every one of d/r blocks meets S in exactly r points]>=[16 sqrt(r)]^(-d/r) | Exact occupancy replaces high-probability concentration at small degrees |
| Corollary 6.3 | Some partition retains this fraction of correlation on exact-size intersections | Averaging the preceding occupancy bound |
| Lemma 6.4, equation (12) | A three-term correlation estimate on homogeneous degree 10^k, with a ten-block recursive degree reduction | Boosted small-degree base case; extra polynomial losses permitted |
| Corollary 6.5 | <f,g><=eta^(-30e')L(f,g)+eta^(1/16)I(f,g)+eta||f||||g|| for homogeneous e', a power of 10, eta<=10^(-320 sqrt(e')) | Packages the boosted base case |
| Theorem 6.6, equation (15) | Same three-term band estimate as Theorem 5.2, but with the boosted base case | Connects small-degree and large-degree recursions |
| Corollary 6.7 | <f,g><=delta^(-100000d)||f||^(3/4)||g||^(3/4)max|a_S hat g(S)|^(1/4)+delta^c I(f,g)+delta||f||||g||, delta<=d^(-96000/sqrt(alpha)) | Final usable technical estimate; c is a positive absolute constant |
| Section 7.1, equation (16) | Bounds correlation with each coefficient-size bin, hence its spectral mass | Theorem 1.3 |
| Section 7.2 | Rebins using log(1+K), then uses degree Markov | Theorem 1.1 |
| Section 7.3, equation (17) | Entropy Markov on low degrees and degree Markov on high degrees | Theorem 1.2 |

Here is enough of the argument to reconstruct the recurrences, rather than treating the table as a list of black boxes.

The base case splits coordinates at up_{f<=d}(i)>=delta. There are at most d/delta such coordinates. Characters involving only these coordinates are counted, and each remaining character is assigned to at least one small-influence coordinate. For such a coordinate, Holder gives ||D_i f||_{4/3}||D_i g||_4. Since D_i f takes values in {-1,0,1}, ||D_i f||_{4/3}=up(i)^(3/4); hypercontractivity bounds the other factor. Combining this with a Cauchy–Schwarz bound on the low-degree derivative gives the delta^(1/8) factor in Lemma 4.3. Lemma 5.3 changes only the large-coordinate part, using Holder on the finite set of coefficients.

For a reduction from d_j to d_{j-1}, choose about (1+epsilon)d_j/d_{j-1} blocks. Keep only characters with all intersection sizes in the prescribed smaller band. Corollary 3.4 loses at most half the correlation. Theorem 4.1 calls a generalized influence large using up_g(R), bounds the number of such R by 2d_j^(d_{j-1})/delta_j, and counts the products of block choices. This is where a literal d_j^(O(d_j)) count occurs in the first proof.

Theorem 5.2 repairs that count. For a fixed live block J define

    j_J^g(T) = sum_{U: U intersection J=T}hat g(U)^2.

For each J, sum_T j_J^g(T)=||g||_2^2. Call T large if j_J^g(T)>=delta_j||g||_2^2 or j_J^f(T)>=delta_j||f||_2^2. There are at most 2/delta_j possibilities per block. The all-large characters number at most the product of these counts, giving (2/delta_j)^(m/4) L(f,g) by Holder. A support or degree restriction can make the map into the Cartesian product only injective; the inequality still holds. The paper sometimes calls it a bijection, which is unnecessary.

For the remaining characters, select a block with a small intersection mass and apply the induction hypothesis after fixing the outside variables. There are three resulting terms. Lemma 2.6 sums the cross-influence term over disjoint blocks without an extra m. Cauchy–Schwarz handles the product-of-norms term, with m copies. Lemma 5.1 handles the Fourier 4/3 term: outside hypercontractivity and j_J^f(T),j_J^g(T)<=delta_j times squared norms give an error at most 3^(d_j)delta_j^(1/4)||f||||g||. Thus equation (11) has the recurrence

    small-part <= m C1(j-1) 3^(d_j)delta_j^(1/4)||f||||g||
                  + C2(j-1) I(f,g) + m C3(j-1)||f||||g||.

This explains both the improved first coefficient and the pressure to make the next threshold very small.

Section 6's boosted base case continues reduction after the Chernoff-based method reaches polylogarithmic degree. For a degree-d character, exact occupancy into d/r blocks has probability d!/(r!^(d/r)(d/r)^d). Facts 6.1–6.2 lower bound this probability, and Corollary 6.3 selects a partition. Lemma 6.4 applies ten-block reductions to homogeneous degrees 10^j and the same large/small intersection split. Its C2 and C3 accumulate the exact-occupancy losses; the small number of remaining scales allows them to be absorbed by eta<=10^(-320 sqrt(e')). Corollary 6.5 packages this induction. The base of Theorem 6.6 selects a homogeneous component, selects characters meeting a random block in one point, and replaces each selected coordinate by a parity on new coordinates to pad the degree to a power of ten. This is addition modulo 2 in the paper's input convention; ordinary real addition would not preserve Booleanity. Norms stay fixed and cross-influence grows by at most the padding factor. The inductive step then repeats Theorem 5.2.

For Corollary 6.7 use e'=d_1=(1000/alpha)(log d)^2, double subsequent d_j, take epsilon=1/log d, eta=delta, delta_2=delta^(1600d_1), and delta_{j+1}=delta_j^(2(1+epsilon)^2). These choices turn C1 into delta^(-O(d)), C2 into delta^c and C3 into delta. The threshold delta<=d^(-O(1/sqrt(alpha))) meets the boosted-base and accumulated-error requirements. Finite small degrees, for which the displayed d_1 exceeds d, can be handled by the original base estimate with enlarged absolute constants.

There is a printed exponent mismatch: the statement of Corollary 6.7 has delta^(1/16), but its C2 calculation gives delta^(1/32) (PDF pp. 29–30, physical pages 29–30; HTML lines 839 and 861). The skeleton uses c>0. Changing the fixed powers in section 7's choice of delta accommodates c=1/32; none of the asymptotic conclusions here requires the disputed exponent. This is a proof-skeleton audit, not an independently checked verification of every numerical constant in sections 4–6.

## 3. Precisely where the logarithm appears

For a fixed degree d, Corollary 6.7 already contains the decisive tradeoff:

    delta <= d^(-A),       first amplification = delta^(-B d).

At the largest allowed delta this amplification is 2^(AB d log d). Thus the correlation estimate becomes informative for coefficient magnitudes at scale 2^(-O(d log d)), rather than 2^(-O(d)). This is a parameter-range loss, with the small-threshold requirements coming from degree reduction and error absorption. It is not an identity involving a harmonic sum.

Section 7.1 makes it explicit. Its line defining delta immediately before equation (16), PDF p. 31 / physical page 31, uses

    delta(d,k)=2^(-32k)d^(-100000).

Consequently

    log(delta^(-100000d))=100000d(32k+100000 log d).

The coefficient bins must compensate this d log d term. For safety with the exponent mismatch above, replace 32k by 128k and enlarge the fixed power of d; the same calculation applies. Take bins with coefficients between sqrt(v)2^(-C(k+1)d log(d+1)) and sqrt(v)2^(-Ckd log(d+1)), and let g_{d,k} be the matching Fourier projection of f. Its correlation with f is exactly its mass. The first term of Corollary 6.7 contains max|a_S hat g(S)|^(1/4)<=v^(1/4)2^(-Ckd log(d+1)/2). Sufficiently large C absorbs delta^(-100000d). The other terms use I(f,g)<=I because g is a Fourier projection. With slightly enlarged fixed powers the resulting bin mass is at most C'2^(-k)d^(-10)I.

The k>=1 bins contribute O(I) entropy: sum_{d,k}2^(-k)d^(-10)(k+1)d log(d+1) converges. The k=0 bins leave

    O(sum_d d log(d+1) W_d)+v log(1/v).

The variance term and the empty coefficient cost are O(I), by edge isoperimetry (and elementary endpoint estimates). This proves the stated shape of Theorem 1.3. Notice that the log is already present at a single degree; summing the degrees is not its first cause.

For Theorem 1.1 use D=10K, log(1+K) in the bins, and delta=2^(-256k)d^(-100000)K^(-16), as in section 7.2, again with larger constants if using c=1/32. The sum of bad-bin masses is a fixed fraction of v. Degree Markov leaves a positive part of v in degrees at most 10K, so at least one good nonempty coefficient remains. For Theorem 1.2 choose D=2K/eta. The weight above D is <=eta v/2. Theorem 1.3 bounds entropy below D by O_eta(I log(1+K)); dividing by the requested coefficient surprise threshold bounds the small-coefficient mass there by eta v/2.

FLOW section 3 is partly right about a failed method, but wrong about the final proof. Section 4.1 footnote 4 of KKLMS explicitly says that naively substituting order-r derivatives counts U by C(|U|,r). Fact 2.4 and the first proof really do incur this cost. Section 5 replaces it by exact intersections j_J, with total budget one per block. I found no occurrence of FLOW's u1 budget or its harmonic sum in the proof of Theorems 1.1–1.3. The final log is the tradeoff above. It is not justified to identify either proposed budget as its exact source.

## 4. Elementary identities, their attribution, and one sharpening

The identities in this section are proved here from definitions. The source concordance below distinguishes them from nearby published statements; I did not find these exact named splits in the portions of the papers read.

For mu(S)>0 set

    c1(S)=log(1/alpha(S)),
    gamma(S)=log(alpha(S)/|a_S|),
    cp(S)=log(1/p(S)),
    cm(S)=log(p(S)/alpha(S)).

All are nonnegative. Their sum satisfies c1=cp+cm and log(1/mu)=2(c1+gamma). At the empty set alpha=p=1. For nonempty S of size r, c_S is an average of 2^r signs with a nonempty parity, hence c_S lies in 2^(1-r)Z and |c_S|<=1. Therefore

    2^(1-r)p(S) <= alpha(S) <= p(S),
    0 <= cm(S) <= r-1.

Writing M=E_mu cm gives the sharper exact split

    H = 2P + 2M + 2Gamma,
    0 <= M <= I-v,
    H = 2A1 + 2Gamma,
    2P+2Gamma <= H <= 2P+2Gamma+2(I-v).

This improves FLOW's sufficient upper estimate with 3I to 2(I-v). AND functions attain the magnitude bound termwise, so its coefficient cannot be decreased by this pointwise argument. Since every term is nonnegative, FEI implies P,Gamma<=H/2<=CI/2. Conversely bounds P<=C_P I and Gamma<=C_G I imply H<=(2C_P+2C_G+2)I. This proves the equivalence claimed in FLOW; no cancellation between the two nonnegative parts is being assumed.

For completeness, up<=alpha<=sqrt(up) gives A1<=A<=2A1, while Q=E_mu log(up/alpha^2) satisfies 2A1=A+Q and B=Q+2Gamma. Cauchy–Schwarz on the support gives alpha^2<=p up, hence P<=Q. Combining up<=alpha and alpha>=2^(1-r)p gives Q<=P+I-v. These establish all of FLOW section 1(a)–(d).

To verify the level form, fix d with W_d>0 and apply Jensen to the probability weights mu(S)/W_d on |S|=d:

    sum_{|S|=d}mu(S)log(up(S)/mu(S))
      <= W_d log(sum_{|S|=d,mu(S)>0}up(S)/W_d)
      <= W_d log(M_d/W_d),
    M_d=sum_{|R|=d}up(R)=sum_U mu(U)C(|U|,d).

The second inequality can itself lose mass from sets with zero Fourier coefficient. Equality holds for symmetric functions when the relevant level is nonzero, because up and mu are constant there. This is a general log-sum/Jensen inequality, with no Booleanity needed. Combining the granularity inequality |a_S|<=2^(r-1)up(S) with mu=a_S^2 gives A<=B+2I-2v and hence H<=2 sum_d W_d log(M_d/W_d)+2I-2v.

For FLOW section 1(e), let F={z:c_S(z)!=0}. Edge isoperimetry gives at least |F|log(2^m/|F|) edges crossing F to its complement in the m-dimensional outside cube. Such an edge in direction j has D_j c_S !=0. Count each crossing edge among the 2^(m-1) edges in its direction. This yields 2p(S)log(1/p(S))<=sum_{j outside S}p(S+j). The factor 2 comes from converting edges to their endpoint density. No claim about interior nonzero differences is needed.

## 5. Chain flow, Talagrand, and the level-one bound

For R of size r, m(R)=sum_{U superset R}mu(U)/C(|U|,r). It is the probability that the first r entries of a uniformly ordered spectral sample form R. Thus sum_{|R|=r}m(R)=Pr(|U|>=r), and summing r>=0 gives I+1. Telescope log alpha along each such chain, starting from alpha(empty)=1, then average the last coordinate of R uniformly. This proves the chain formula in FLOW section 2, including its coefficient 1/r.

Here is a full proof of the advertised generalized Talagrand estimate. Put g=D_R f and L=ln(||g||_2/||g||_1). For a nonzero g and r>=1, the beta integral gives

    m(R)=r integral_0^1 (1-t)^(r-1)||T_sqrt(t)g||_2^2 dt.

Indeed the Fourier term indexed U contributes r integral_0^1 t^(|U|-r)(1-t)^(r-1)dt=1/C(|U|,r). Hypercontractivity gives ||T_sqrt(t)g||_2<=||g||_{1+t}. Interpolating L1 and L2 with exponent theta=(1-t)/(1+t) gives

    ||g||_{1+t}^2 <= ||g||_2^2 exp(-2theta L)
                        <= up(R) exp(-(1-t)L).

The integral is at most up(R), by direct contraction, and at most

    up(R) r integral_0^infinity s^(r-1)e^(-Ls)ds
      =up(R) r!/L^r.

Take the smaller bound. If L=0, use m<=up. If g=0, both sides are zero. This proof works for real-valued g and does not use derivative granularity. At r=1 for Boolean f, ||D_i f||_1=||D_i f||_2^2=Inf_i, so L=(1/2)ln(1/Inf_i) and m(i)<=2 Inf_i/ln(1/Inf_i), with m<=Inf_i also available.

A complete level-one proof with an explicit constant follows. Let a_i=Inf_i>0 and ell_i=log(1/a_i). Since D_i f is {0,1,-1}-valued, hypercontractivity at rho=1/sqrt(3) implies

    sum_{U contains i,|U|<=k}mu(U)
       <=3^(k-1)||T_(1/sqrt(3))D_i f||_2^2
       <=3^(k-1)a_i^(3/2).

Set K0=4log(3). For every nonempty S,

    max_{i in S}ell_i <= K0|S| + sum_{i in S:ell_i>K0|S|}ell_i.

For fixed i the event on the right has |S|<ell_i/K0, so the low-degree bound makes its spectral probability at most a_i^(5/4). Since sup_{0<a<=1}a^(1/4)log(1/a)=4/(e ln 2), averaging gives

    E_mu[log(1/min_{i in S}Inf_i); S nonempty]
       <=(4log(3)+4/(e ln2)) I.

The constant is evaluated by the command recorded in RESULTS.md. Empty S contributes zero, and zero-influence coordinates never occur in the spectral sample. This is an elementary consequence of hypercontractivity; I did not locate this exact expected-minimum statement in the listed papers.

## 6. The E,D potential tree

Fix a coordinate order and split g into a=E_i g and d=D_i g. Energy conservation gives ||g||_2^2=||a||_2^2+||d||_2^2. For any functional N positive on nonzero nodes, put F_N(g)=||g||_2^2 log N(g). At this node the displayed edge cost is

    F_N(g)-F_N(a)-F_N(d).

Summing over the full tree telescopes. Leaves are constants a_S and root f has norm 1. If N(f)=1 and N(c)=|c|, the result is -sum_S mu(S)log|a_S|=H/2. Each leaf with index S passes through |S| derivative edges, so the sum of derivative-child energies over all nodes equals I. Zero-energy nodes are omitted. This proves FLOW section 4's main formula for each fixed order.

There is one correction to its explanatory sentence: the usual entropy chain rule is N=||g||_2. The weighted geometric mean of the spectral coefficient magnitudes generally has N(f)=2^(-H/2), so it does not satisfy the stipulated root normalization. For a general N, the telescoped answer is H/2+log N(f), not H/2. In particular that geometric-mean choice gives zero. This does not invalidate the formulas for L1, Lp, or L-infinity norms.

The local obstruction can be made exact. For g=a+bx with a=1, 0<b<1, N=L-infinity, the root norm is 1+b and the E-child contributes log(1+b), whereas the derivative energy is b^2. The ratio log(1+b)/b^2 tends to infinity. These nodes are real-valued; one must not silently claim they are arbitrary Boolean roots.

## 7. Boolean obstructions to deleting the local loss

The chosen directly testable steps are Lemmas 3.5 and 5.1. They are used in the degree-reduction recurrence that eventually forces the threshold tradeoff. To keep the test within actual Boolean restrictions, use g=f, h'=h, a nonempty proper live block J, and retained level r>=1. Define

    E2=max_T E_z h_T(z)^2,       Z=sum_T E_z h_T(z)^2,
    X=E_z max_T h_T(z)^2,
    Y=E_z (sum_T |h_T(z)|^(8/3))^(3/4),  |T|=r.

The tested published bounds are X<=3^q sqrt(E2 Z) and Y<=3^q E2^(1/4)Z^(3/4), where q is the actual maximum outside degree of h_T. The deletion proposals replace 3^q by a universal constant. Tests with h'=h are a subcase of the full two-function lemma, sufficient to refute such a deletion.

Exhaustive enumeration and an independent direct-sum check are in data/exact4.json and data/independent_audit.json. Both maxima without 3^q occur first at truth table 0x001b, live mask 0x6, r=1. Its two retained coefficient functions take values (-1,0), (0,-1), (0,0), (0,0) across the four outside assignments. Thus E2=1/4, Z=1/2, X=Y=1/2, giving ratios sqrt(2) and 2^(1/4). These are exact radicals. This example has q=2.

There is also an analytic check of both exhaustive maxima. If there are l coefficient functions and m outside assignments, then X<=Z and E2>=Z/l give X/sqrt(E2 Z)<=sqrt(l). Also E2>=X/m and Z>=X give the bound sqrt(m). For p=4/3 and nonnegative vectors w_z=(h_T(z)^2)_T, (sum_z ||w_z||_p)^p<=m^(p-1)sum_z||w_z||_p^p<=m^(p-1)||sum_z w_z||_p^p. Consequently Y<=m^(1/4)||E_z w_z||_p<=m^(1/4)E2^(1/4)Z^(3/4). The bound l^(1/4) follows instead from Y<=Z and E2>=Z/l. On four variables, l=C(|J|,r) and m=2^(4-|J|), so min(l,m)<=2 for every tested J,r. Thus the two universal upper bounds are sqrt(2) and 2^(1/4), exactly achieved by the stored witness. This proof does not depend on floating-point comparisons.

An unbounded Boolean family makes the issue decisive. Let k address bits select one of 2^k independent data bits, f(z,y)=y_z. Retain all data bits and fix z. Then h_{i}(z)=1_{z=i}, so

    X=Y=Z=1,    E2=2^(-k),    q=k,
    X/sqrt(E2 Z)=2^(k/2),
    Y/(E2^(1/4)Z^(3/4))=2^(k/4).

All these h_i take only values 0 and 1, so they already have the strongest order-one derivative granularity. The original f is Boolean, so its Fourier coefficients satisfy sum_S a_S a_{S xor T}=0 for every nonempty T. The full k-address spectrum has exactly 4^k nonzero coefficients of magnitude 2^(-k), supported on one data bit and any subset of the address bits. Therefore H=Hinf=2k, I=1+k/2. This family obstructs an exponential-to-constant improvement of these restriction lemmas even under the full Boolean convolution constraints. It does not obstruct FEI; H/I stays bounded.

Likewise parity on n variables gives sum_{|R|=r}up(R)=C(n,r) and sum_{r>=1}sum_{|R|=r}u1(R)=n H_n. Its budgets divided by I=n are C(n,r)/n and H_n. These equalities are Boolean and exact. Neither a constant budget for all r-subsets nor deletion of the harmonic overcount can follow from granularity or f^2=1 alone. Parity has zero entropy, so these are obstructions to proposed accounting steps, not lower bounds on the FEI constant.

No test or argument here proves that every use of granularity or Booleanity must fail to remove the final KKLMS logarithm. That would be a much stronger claim. The rigorous conclusion is that the particular local deletions above fail, while the final entropy bound may still be improved by a different global argument.

## 8. Tribes really makes the FLOW level estimate lose a logarithm

This is a separate obstruction, to treating FLOW's level Jensen right side as O(I). Let tribes have width w, t=round((ln2)2^w), p=2^(-w), n=wt, and f=2 product_j(1-AND_j)-1. Changing the global sign has no spectral effect. Write Q(z)=(1-p)^2+p^2((1+z)^w-1). Exact generating functions are

    W(z)=mu(empty)+4[Q(z)^t-Q(0)^t],
    M_d=[z^d]W(1+z).

For d>0 this is 4[z^d][(1-p)^2+p^2((2+z)^w-1)]^t. The script tribes_levels.py computes both polynomials with integers over denominator 2^(2wt). Thus no truth table on n=3195 variables is allocated. I=2tw p(1-p)^(t-1) and the entropy can independently be evaluated by counting how many tribes the spectral set touches.

Here is a proof that J=sum_d W_d log(M_d/W_d)=Theta(I log I), although H=O(I). Set a=number of touched tribes. For a>=1 its spectral mass is

    4(1-p)^t Pr[Bin(t,p)=a],

and, conditional on the touched blocks, each selected subset in a block is uniform among the 2^w-1 nonempty subsets. In particular Pr[a=1] is bounded below by a positive constant, and the weight of degrees d in [w/3,2w/3] is bounded below. Also I=Theta(w).

For such a d take a=floor(w/log w). For all sufficiently large w, Bin(t,p) has probability at least exp(-C a log(a+1))>=exp(-C'w) at a. This follows directly from its binomial formula, t p bounded above and below and a<<sqrt(t). With at least constant conditional probability, the total degree is at least aw/4: the size of each nonempty uniform subset stochastically dominates Bin(w,1/2), and Chebyshev or a binomial tail bound applies to their sum. For sufficiently large w, aw/4>=d. Hence

    M_d=E C(|U|,d) >= exp(-C'w) C(floor(aw/4),d).

Using C(K,d)>=(K/d)^d yields

    log M_d >= d(log w-log log w-O(1))-O(w).

Summing over the constant spectral mass in the displayed degree interval gives J=Omega(w log w). Here -log W_d>=0, so it can only help the lower bound.

For the matching upper bound choose z=1/w. Then W(1+1/w) stays bounded: Q(1+1/w)=1+O(p), since (2+1/w)^w=O(2^w), and t=Theta(1/p). Nonnegative coefficients give M_d<=C w^d. Thus

    J<=I log w+H(W)+O(1)=O(I log w).

The last equality can use OWZ Theorem 5, H(W)<=3I, or the elementary entropy bound H(W)<=log(1+I)+O(1+I) from comparison with a geometric distribution. Finally the same touched-block formula gives H=4I(1+o(1)): its coefficient surprise is 2aw-2(t-a)log(1-p)-2, whose leading average is 2w E_mu a=4I(1+o(1)). This proves the claimed separation.

The log loss in this FLOW estimate is Jensen's removal of within-level structure. Tribes has Booleanity and exact granularity throughout. Consequently a universal estimate J<=CI is false. This fact must be kept distinct from the source of the final KKLMS log and from the true conjecture B<=CI.

## 9. FMEI: exact equivalent splits and the limits of the support version

All minima below are over mu(S)>0. The pointwise identities give

    Hinf=2 min_S[c1(S)+gamma(S)]
        =2 min_S[cp(S)+cm(S)+gamma(S)]
        =min_S[log(1/up(S))+log(up(S)/mu(S))].

Thus FMEI is equivalent, up to factors in a universal constant, to a joint witness S for which alpha(S)>=2^(-CI) and |a_S|/alpha(S)>=2^(-CI). Equivalently there is one S with up(S)>=2^(-CI) and mu(S)/up(S)>=2^(-CI). Both conditions must refer to the same witness. Each pair's sum is precisely the coefficient surprise, so the implications follow by adding nonnegative costs; no probabilistic inference is needed.

Replacing alpha by support probability p discards cm and is not an equivalent pointwise split. In fact the joint condition p(S)=1 and gamma(S)=0 always has a witness: take an inclusion-maximal S in the Fourier support. D_S f is then the nonzero constant a_S. This condition by itself has no content. The exact support version must retain cm(S), or a sufficient degree penalty (|S|-1)_+ by granularity. FMEI implies the existence of small cp+gamma, but the reverse estimate without cm is unavailable and the proposed condition is tautological. A degree-penalized sufficient condition should not be advertised as equivalent to FMEI without a separate argument controlling the witness degree.

There is also no fixed-order Renyi gap hiding here. For q>1 and pmax=max mu,

    pmax^q <= sum mu^q <= pmax^(q-1),
    Hinf <= H_q <= q/(q-1) Hinf.

So H_q<=CI for any fixed q>1 is equivalent to FMEI up to constants. In split notation sum mu^q=E_mu 2^(-2(q-1)(c1+gamma)), giving an exact exponential-moment formulation, not a stronger intermediate conjecture. ACKSW Corollary 4.6 provides nearby Renyi bounds; it does not identify a strict gap.

A positive fixed amount of good spectral mass already reaches FEI. Suppose some universal C and epsilon>0 give, for every Boolean f,

    Pr_{S~mu}[c1(S)+gamma(S)<=CI]>=epsilon.

FEI implies this by Markov (with, for example, a larger C and epsilon=1/2). Conversely apply the assertion to the product F_m of m independent copies of f. Its influence is mI; its spectral measure is the product of m copies of mu; alpha and |a| multiply, hence c1+gamma adds. The ordinary law of large numbers makes the probability in the displayed assertion tend to zero if E_mu(c1+gamma)=H/2>CI. Therefore H<=2CI. This proves equivalence to FEI. The same argument works with simultaneous bounds on c1 and gamma, after adding them.

The conclusions proved here are an exact joint-witness characterization of FMEI, and a joint positive-mass characterization of FEI. No strictly intermediate universal statement is proved. Pointwise Hinf<=H and examples of distributions with different entropies do not establish a strict implication between the two open Boolean-function conjectures.

## 10. Source concordance for FLOW

The phrase “not found” means not found in the portions actually read, listed in REPORT.md. It is not a priority or novelty claim.

| FLOW item | Exact statement located? | Nearest published statement actually read |
|---|---|---|
| 1(a) H=2A1+2Gamma; FEI iff P and Gamma are O(I) | Not found in the papers read | KKLMS Definition 2.3 identifies up; KMS Proposition 3.1 gives integer-valued Fourier granularity; the split and implication are proved in section 4 above |
| 1(b)–(d), including Q,P comparisons | Not found in the papers read | Same granularity input; Cauchy–Schwarz on the derivative support; full derivation above |
| 1(e), support isoperimetry | Not found in this derivative-support notation | Shalev section 2.2, Lemma 12 and the edge-isoperimetric theorem cited there; direct boundary counting above |
| 1(f), B<=sum W_d log(M_d/W_d) | Not found in this exact form | KMS Claim 4.1 is coordinate entropy subadditivity H<=sum_i h(Inf_i); OWZ section 3 equation (1) is the symmetric-level entropy formula, and Theorem 5 is H(W)<=3I; neither is the displayed containment-moment bound |
| 2, exact chain flow m(R) | Not found in the papers read | KKLMS section 4.1 footnote 4 and Fact 2.4 concern the unweighted subset count; they do not give this normalized chain flow |
| 2, m(R)<=up(R)min(1,r!/L^r) | Exact per-R constant-one version not found | Talagrand L1/L2 inequality, as stated in Tanguy Theorem 3; Tanguy Theorem 4 gives a summed second-order version with a squared (1+L) denominator plus lower-order terms; our beta-integral proof is a direct hypercontractive consequence |
| 2, hypercontractive low-distance statement | Standard immediate consequence, not a separately numbered result found | KKLMS Theorem 2.8 / the noise-operator form of hypercontractivity, applied to D_R f |
| 2, expected log inverse minimum individual influence | Exact statement not found | KKLMS section 4.1's KKL calculation before equation (3), and Theorem 2.8; explicit proof in section 5 above |
| 4, arbitrary norm potential on the E,D tree | Exact arbitrary-functional formula not found | Han Lemma 3.1 and equations (3.1)–(3.4) track moments of restricted Fourier coefficients; this is related restriction machinery, not this norm potential |

Other candidate references read were [CKLS, Upper Bounds on Fourier Entropy, ECCC TR13-052 revision 2](https://eccc.weizmann.ac.il/report/2013/052/revision/2/download/), sections 1 and 6: Theorem 6.2 is a degree-(1+delta) moment bound with a dimension-dependent additive term, and Corollary 6.3 uses first and second sensitivity moments. They do not state the FLOW level bound. [Shalev, arXiv:1806.03646](https://arxiv.org/html/1806.03646), Lemma 1 and Theorems 2–9, concerns weak FEI, extremal classes, spectral norm, and decision trees. [ACKSW, arXiv:1809.09819](https://arxiv.org/html/1809.09819), Theorems 3.1–3.2, 4.2 and Corollary 4.6, supplies certificate and min-/Renyi-entropy bounds. [Han, arXiv:2312.08271](https://arxiv.org/html/2312.08271), Theorem 1, gives H<=C I+C' sum_i Inf_i log(1/Inf_i); it does not prove FEI or the containment/cancellation components.

KMS is [A Note on the Entropy/Influence Conjecture, arXiv:1105.2651](https://arxiv.org/html/1105.2651). OWZ is [The Fourier Entropy–Influence Conjecture for Certain Classes of Boolean Functions, author PDF](https://www.cs.cmu.edu/afs/cs/Web/People/jswright/papers/fei.pdf). Tanguy is [Talagrand inequality at second order and application to Boolean analysis, arXiv:1801.08931v3](https://arxiv.org/html/1801.08931). The older title “at higher order” belongs to an earlier version; the current version's principal discrete result is second order.
