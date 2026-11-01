# P0220: finite-determinant stationary joint law

CURRENT VERDICT: SOLVED, 2026-10-11 continuation. Historical priority unverified; not SOLVED_IN_LITERATURE.

For every finite list of stationary particle thresholds, the continuation proves an explicit finite block-determinant formula with factorial/Bessel entries. For the first k particles its dimension is at most k(k-1). It also gives a closed three-particle survival function and density. The complete theorem and proof appear below after the preserved first-attempt record, and separately in FINITE_DETERMINANT.md.

The established 1993 patience/Gamma representation is used as prior input, not claimed as a new solution. The additional answer is its finite determinant evaluation. REFEREE.md records the hostile-referee checks. Exact permutation/series checks and an independent positive growth computation pass; the general block-sign identity passes Lean kernel checking.

Two approaches considered and the chosen finite occupied-site/Eynard-Mehta construction are recorded in SECOND_ATTEMPT.md. No mathematical gap remains in the displayed finite-determinant evaluation under the established source representation. The entire probability proof is not formally verified, and historical novelty is not established.

---

# First attempt: stationary law and a continuous non-Markov obstruction

First-attempt record, 2026-10-11: verdict PARTIAL at that time. Its general-law gap is resolved by the continuation proof below. Historical novelty remains unverified.

## 1. Exact source problem and scope

David Aldous, *A one-dimensional drift-jump particle process*, posted February 2018, asks verbatim:

> Give some (fairly explicit) description of the stationary distribution.

For each integer k>=1 the state is 0<X_1<...<X_k. Every coordinate solves dX_i/dt=X_i between jumps. A rate-one Poisson point process with intensity dx dt on (0,infinity)^2 drives the jumps. At (y,t), move the closest particle strictly to the right of y to y, if there is one. These laws are consistent in k. The page states that the stationary distribution is unique. The two-sided classical Hammersley process described earlier on the page is a different process.

The primary source was fetched to source.html. The 1993 notes, Section 4.1, equations (41)-(42), PDF/printed p.37, already represent the stationary law as

    (X_1,...,X_k) =_d (Gamma(B_1),...,Gamma(B_k)),             (1)

where Gamma(n)=E_1+...+E_n, the E_j are independent Exp(1), independent of the stabilized patience-pile-top labels 1=B_1<B_2<.... Equation (45), p.39, already gives

    P(B_2=b)=(b-1)/b!, b>=2.

The notes' Section 4.2, p.39, says verbatim:

> Remark. It would be nice if the limit (Xi(∞); i = 1, . . . , k) were Markov in i, but this appears to be false.

We use (1) as established input, as authorized by the problem's caveat. Its derivation and the old k=2 formulas are NOT new solutions. Earlier internal work has substantial Plancherel/Schur/Fredholm formulas; their existence is recorded in LITERATURE.md. This attempt does not re-certify those entire packages.

The new target checked here is the precise structural assertion

    X_3 is not conditionally independent of X_1 given X_2.   (2)

In particular the stationary ordered sequence is not even a possibly inhomogeneous Markov chain in its spatial index. This is not a statement about the evolution in physical time, which is Markov by construction. It is also stronger than merely showing that the discrete labels B_i fail to be Markov: adding exponential spacings could erase some discrete dependence, so that discrete observation alone is insufficient.

## 2. Stable finite probabilities, with justification

For a finite permutation let its pile-top vector be updated by replacing the leftmost entry larger than the incoming card, or appending that card when no such entry exists. The vector is always increasing.

Deleting every card greater than c before running patience sorting does not change the final pile tops <=c. To prove this, induct on incoming cards. The current entries <=c form a prefix of the increasing vector. A card >c cannot change that prefix. A card a<=c either replaces the first larger entry within the prefix, identically in both runs, or is appended to that prefix. In the latter case it replaces a >c entry if present in the full run, or is appended to the full vector, with the same effect on its <=c prefix. This proves the induction.

Consequently, for 1<b<c the stable probability

    q_(1,b,c)=P(B_1=1,B_2=b,B_3=c)

can be calculated from a uniform permutation of precisely 1,...,c. Its final pile-top prefix must be (1,b,c). The relative order of the smallest c cards of a larger uniform permutation is uniform, and adding larger cards has the invariance just proved. Thus there is no large-n approximation in these coefficients.

We use the standard Robinson-Schensted bijection between permutations and pairs (P,Q) of standard Young tableaux of the same shape. This is classical input. The pile-top vector is the first row of P: both have exactly the same update rule on their first row, which proves this correspondence by induction on insertions. For each fixed P of shape lambda, the number of possible Q is f^lambda, the number of standard tableaux of that shape.

If the first-row prefix is (1,b,c) and c is the largest label, that row has exactly three boxes. Counting P and multiplying by f^lambda gives the following four probabilities:

    q_(1,2,3)=1/6;
    q_(1,3,4)=1/8;
    q_(1,2,4)=1/8;
    q_(1,3,5)=11/120.                                     (3)

Here are the complete counts. For c=3 only the one-row tableau with row (1,2,3) occurs, and there is one Q, out of 3!=6 permutations. For c=4 and either specified row (1,3,4) or (1,2,4), the shape is (3,1), and the one remaining label fixes its unique P. There are exactly three Q of shape (3,1): the lone lower cell can contain any of 2,3,4. Thus both probabilities are 3/24.

For c=5 and row (1,3,5), the only shapes are (3,2) and (3,1,1). Each has a unique P, with remaining labels 2,4 placed in increasing order. For shape (3,2), the possible sets of labels in the bottom row of Q are {2,4}, {2,5}, {3,4}, {3,5}, {4,5}; each fixes a valid tableau, and the other five two-element subsets violate a column condition. Hence f^(3,2)=5. For shape (3,1,1), choose the two labels below the initial 1 from {2,3,4,5}, in six ways; arrange them in increasing order, and put the other two in increasing order across the first row. All column and row conditions hold. Thus f^(3,1,1)=6, and the probability is (5+6)/120.

The old formula for B_2 additionally gives

    q_(1,2)=1/2, q_(1,3)=1/3.                              (4)

These could also be obtained by the same finite counting: one of two permutations and two of six permutations.

Independent exact checks enumerate all permutations of sizes <=5 using a pile-top algorithm rather than RSK. See exact_check.py and checks.json. FiniteCertificate.lean (successful check: lean_check.txt, exit 0) defines the pile-top algorithm and independently checks all six integer counts using `decide +kernel`. The use of the library's permutation enumeration relies on its established completeness and absence of repetitions on a deck of distinct labels. The rational obstruction certificates are also kernel-checked. This finite formalization does not formalize the analytic or conditional-independence arguments below.

## 3. Full gap density and justified analyticity

Write A=X_1, G=X_2-X_1, H=X_3-X_2. By (1), A=E_1 and

    G=E_2+...+E_(B_2),
    H=E_(B_2+1)+...+E_(B_3).

Since E_1 is independent of the labels and all subsequent E_j, A~Exp(1) is independent of (G,H). The same argument gives independence of X_1 from the entire vector of subsequent gaps.

Conditionally on (B_2,B_3)=(b,c), G and H are independent Gamma(b-1,1) and Gamma(c-b,1). Their shapes are positive integers. Therefore the density of (G,H), for g,h>0, is

    f(g,h)=exp(-g-h) C(g,h),
    C(g,h)=sum_(r,s>=0) q_(1,r+2,r+s+3) g^r h^s/(r! s!).   (5)

The conditional gamma densities integrate to one, the q's sum to one, and all real summands are nonnegative. Tonelli proves that (5) is a normalized density. The joint density of (A,G,H) is exp(-a) f(g,h), a>0.

Equation (5) defines an entire function of two complex variables. Indeed 0<=q<=1, so on |g|,|h|<=R the absolute sum is at most exp(2R). Each fixed mixed derivative has the same bound after shifting the factorial indices. Thus the series and its derivatives converge uniformly on compact sets, permitting termwise differentiation, evaluation at (0,0), and limits from the positive quadrant. In particular C and f extend smoothly to its boundary. Also C(g,h)>=1/6 for g,h>=0, so there are no zero-density complications.

The density of G from the old k=2 law is

    a(g)=exp(-g) F(g),
    F(g)=sum_(r>=0) [(r+1)/(r+2)!] g^r/r!.                (6)

Exactly the same compact-convergence argument applies to F, and F(g)>=1/2 for g>=0. Thus (3)-(4) imply

    C(0,0)=1/6,
    C_g(0,0)=C_h(0,0)=1/8,
    C_gh(0,0)=11/120,
    F(0)=1/2, F'(0)=1/3.                                  (7)

## 4. The consecutive gaps are dependent

If G and H were independent, their continuous joint density would satisfy

    f(g,h) f(g',h') = f(g,h') f(g',h)

almost everywhere in positive quadruples. Fubini proves the a.e. statement from density factorization. Its two sides are continuous, so the identity holds for every positive quadruple: a continuous function zero almost everywhere is identically zero. Differentiate in g' and h' and set g'=g, h'=h. This gives

    f f_gh - f_g f_h = 0

throughout the positive quadrant. Substituting f=exp(-g-h) C cancels the separate exponential factors and gives C C_gh-C_g C_h=0 there. Continuity gives the same equality at the origin. But (7) gives

    C C_gh-C_g C_h at (0,0)
      = (1/6)(11/120)-(1/8)^2 = -1/2880 != 0.             (8)

This contradiction proves dependence. Equivalently the mixed log derivative is

    partial_g partial_h log f(0,0) = -1/80.

This is a local interaction in the density, not a claim that the full covariance or every correlation is negative.

## 5. A continuous-index Markov law is impossible

For 0<x<y<z, put g=y-x and h=z-y. The coordinate change (x,g,h)->(x,y,z) has determinant one. Hence the joint density of (X_1,X_2,X_3) is exp(-x) f(g,h), and that of (X_1,X_2) is exp(-x) a(g). A version of the conditional density of X_3=y+h given X_1=x,X_2=y is therefore

    R(g,h)=f(g,h)/a(g)=exp(-h) C(g,h)/F(g).                (9)

R is smooth on the closed positive quadrant and strictly positive. If X_3 were conditionally independent of X_1 given X_2, there would be a measurable conditional density K(y,h) with

    R(g,h)=K(y,h) for a.e. (y,g,h) satisfying 0<g<y,h>0.   (10)

Here the conditional density K exists because the joint and marginal laws have densities; the density exp(-(y-g))a(g) of (y,g) is everywhere positive on its domain. Thus probability-a.e. and Lebesgue-a.e. null sets agree in this assertion.

For almost every y, Fubini makes (10) hold for almost every (g,h) in (0,y)x(0,infinity). For such a y and almost every h, R(g,h) is a.e. constant as a function of g on (0,y). Its continuity makes it constant for all g in that interval. For any fixed g_1,g_2 in (0,y), continuity in h then extends R(g_1,h)=R(g_2,h) from almost every h to every h>0. There are arbitrarily large good y, since the exceptional y set has measure zero. It follows that R(g,h) is independent of g for every g,h>0. Its smooth extension consequently has R_g(0,0)=0.

However (7) and the quotient rule give

    R_g(0,0)
      = [(1/8)(1/2)-(1/6)(1/3)]/(1/2)^2
      = 1/36 > 0.                                       (11)

This contradiction proves (2). Continuity also shows the violation occurs on a positive open neighbourhood inside the support; it is not an inference from a conditioning event of probability zero.

Therefore the stationary spatial sequence (X_i) is not Markov, already at the triple (X_1,X_2,X_3). This proof allows arbitrary index-dependent transition kernels. It does not merely exclude independent or identically distributed gaps.

## 6. Hostile-referee checks and limits

- Exact hypotheses: the drift is x, not a constant; the noise is rate one per unit space-time. Source checked directly.
- Stable atoms: proved by the pile-top prefix induction, rather than assuming that later larger labels do nothing to the entire tableau.
- Finite counting: explained combinatorially via the classical RSK bijection, independently exhaustively enumerated in Python, and independently kernel-checked in Lean. Counts are exact, not Monte Carlo.
- Gamma off-by-one: the first gap has b-1 exponentials, so its density power is b-2=r; the second has c-b, so its power is c-b-1=s. The index c=r+s+3 in (5) follows exactly.
- Infinite summation: positivity gives normalization, while factorial domination separately justifies analytic derivatives. No unjustified differentiation of a merely pointwise series.
- Conditional null sets: addressed with positive densities and Fubini before using continuity; no statement is based on directly conditioning at coincident particle positions.
- Discrete-to-continuous inference: not used. The contradiction is computed in the actual continuous density.
- Markov-in-time versus Markov-in-index: explicitly distinguished.
- Independence of X_1 and gaps: follows directly from the independence of E_1; it does not imply all gaps are independent.
- Novelty: unverified. The historical notes already suspected non-Markov behavior and previous internal work proves a discrete analogue. This note supplies a continuous proof, not a claim of priority.
- Lean scope: only the finite counts and rational certificates are checked, not the full probabilistic theorem.

## 7. What remains open in this attempt

No published theorem solving the exact source question was verified. Some requested APIs were rate-limited, and the literature search is bounded; a negative search is not proof of openness.

The general tableau mixture is established prior representation, not a new answer. Earlier internal records contain candidate Schur/Fredholm and constructive partition formulas, but this attempt has not independently verified their full kernel/time-ordering identification and all-k source-matching proof. The remaining task for that route is a complete audit of those formulas against a precisely quoted published Schur-process theorem and the actual source dynamics. Merely noting that classical Hammersley processes have Poisson invariant measures is insufficient.

The result proved here rules out a useful simple route: one cannot encode this stationary particle sequence with a transition kernel depending only on the immediately preceding continuous coordinate. It supplies a rigorous structural partial result and leaves the requested new useful explicit all-k joint law unresolved in this attempt.


## 8. Exact interior witness, separate from the boundary proof

To test the boundary-to-interior argument independently, interior_check.py computes bounds using rational arithmetic and only degree-two polynomials. Additional finite permutation counts give q_(1,2,5)=11/120 and q_(1,4,5)=1/20. Consequently

    C_2(g,h)=1/6+(g+h)/8+g^2/40+11gh/120+11h^2/240,
    F_2(g)=1/2+g/3+g^2/16.

Because every q<=1, the omitted terms satisfy, for 0<=u=g+h<4,

    0<=C-C_2<=u^3/[6(1-u/4)],
    0<=F-F_2<=g^3/[6(1-g/4)].

Indeed the total-degree-n envelope for C is u^n/n!, by the binomial formula, and the ratio of successive terms starting with n=3 is at most u/4. The same proof applies to F. Positivity therefore bounds C/F between C_2/(F_2+tail_F) and (C_2+tail_C)/F_2.

At h=1/100, the exact bounds give

    g=1/100: 0.3361207147... <= C/F <= 0.3361234886...,
    g=1/50:  0.3363961631... <= C/F <= 0.3364060010....

The exact rational intervals, not these rounded displays, are in interior_check.json. The second interval lies strictly above the first. Since the common factor exp(-h) in R is positive, the conditional density of X_3 at 1.01 given X_2=1 differs between X_1=0.99 and X_1=0.98. Smoothness extends that discrepancy into neighbourhoods of these points. This is a rational-tail certified interior check of the analytic argument, not a simulation.


---

# Continuation: complete joint-law theorem and proof

# A finite determinant for every stationary joint law in P0220

2026-10-11 continuation. This is a source-specific composition of classical RSK and finite nonintersecting-path determinant algebra. It does not claim historical novelty for that machinery. The mathematical statement is stronger than the old rank representation: it evaluates every stationary joint survival probability by one ordinary finite matrix determinant, with factorial/Bessel entries and dimension bounded in terms of the number and indices of the requested particles.

## 1. Statement

Use exactly the source dynamics: dX_i/dt=X_i between rate-one space-time Poisson left jumps to the nearest particle on the right. Let (X_i) be its stationary ordered sequence. For any finite list of indices k>=1 and thresholds t>=0, the following recipe computes

    S=P(X_k>t for every listed (t,k)).

Discard t=0 (all coordinates are strictly positive), and at each repeated positive t retain the smallest index. If no observations remain, S=1. Otherwise order them as

    0<t_1<...<t_r=T,

with corresponding indices k_a. Replace k_a by min_{b>=a} k_b. This changes no event: the auxiliary first-row length is nondecreasing, so a later smaller width bound implies the earlier larger bound. Put

    m_a=k_a-1, d=m_r.

The m_a are now nondecreasing. If d=0, S=exp(-T). If d>=1, define the finite marker list

    J={(t_a,x): a<r, x=0,...,d-m_a-1},

where an empty range contributes no markers. Order markers by time, with any fixed order within a time. Let q=|J|, and write its entries (s_alpha,x_alpha). For nonnegative u and integers y,x>=0 put

    p_u(y,x)=u^(y-x)/(y-x)! if y>=x, and 0 otherwise,

with p_0(y,x)=1_{y=x}. Set b_i=i for i=0,...,d-1, and define

    E_u(a,b)=sum_{n>=max(0,b-a)} u^n/[n! (a+n-b)!].       (1)

This entire scalar function is explicit; for u>0,

    E_u(a,b)=u^((b-a)/2) I_(a-b)(2 sqrt(u)),

where I_-j=I_j. Formula (1), not a singular power expression, defines the u=0 value.

Form the matrices

    A_ij=E_T(b_i,b_j),
    F_i,alpha=p_(s_alpha)(x_alpha,b_i),
    G_alpha,j=E_(T-s_alpha)(x_alpha,b_j),
    Q_alpha,beta=1_(s_alpha<s_beta)
                   p_(s_beta-s_alpha)(x_beta,x_alpha).   (2)

Then the claimed exact formula is

    S=exp(-T) det M,
    M=[[ A, F ], [ -G, -Q ]].                            (3)

The determinant has size d+q<=r d. The empty-marker case is just exp(-T) det A. For the first k particles and arbitrary nonnegative thresholds, r<=k and d<=k-1, so a matrix of size at most k(k-1) suffices. No inverse, contour prescription, infinite spatial determinant, or tableau enumeration appears in the final evaluation formula.

This supplies all joint survival functions, hence the full stationary joint law. Indeed probabilities of arbitrary axis-aligned rectangles follow by inclusion-exclusion on these survival events. Such rectangles generate the Borel sigma-algebra. The formula therefore determines the law, not merely its scalar marginals.

## 2. Source matching: what is inherited and what is proved

The established historical input is Aldous-Diaconis (1993), Section 4.1, equations (41)-(42), p.37:

    (X_1,...,X_k) =_d (Gamma(B_1),...,Gamma(B_k)),          (4)

with independent rate-one Poisson arrival times Gamma and stabilized patience-pile tops B. This input is not presented as newly solved work.

For a uniform permutation of n letters, patience-pile tops equal the first row of the RSK insertion tableau P, by induction on the update of that row. The RSK bijection gives, for every standard tableau U of shape lambda,

    P(P=U)=P(Q=U)=f^lambda/n!,                           (5)

because each partner tableau has f^lambda possibilities. Hence the entire vector of first-row labels has the same distribution in P and the recording tableau Q, not just its length.

Deleting input labels above n leaves the pile-top prefix <=n unchanged. Here is the prefix induction. At every stage the pile tops are increasing, so tops <=n form a prefix. An incoming card >n cannot replace a member of that prefix. An incoming card c<=n either replaces the first larger member of that prefix, identically in the full and restricted runs, or extends that prefix by one. In the latter case, in the full run it replaces a larger top outside the prefix if present, or appends at the end; both actions extend the <=n prefix in exactly the same way as the restricted run. Starting with the empty vector proves the assertion. Thus (5) is compatible with the stabilized B labels at every finite cutoff. An infinite recording tableau built from iid continuous uniform inputs has these finite-cutoff distributions. If Lambda_n is its shape after n entries, the label of its j-th first-row box is

    H_j=inf{n:(Lambda_n)_1>=j}.

Every H_j is finite almost surely. For a proof, split the iid input sequence into disjoint blocks of length j. Each block is strictly increasing with probability 1/j!, independently of the other blocks. Almost surely some block is increasing, since (1-1/j!)^M tends to zero. It yields an increasing subsequence of length j, and the RSK first-row/LIS theorem makes the first-row length at least j. Taking countably many j is harmless.

The law of the first k labels in B consequently equals that of (H_1,...,H_k). Poissonizing with the independent arrival process in (4) gives

    (X_1,...,X_k) =_d (tau_1,...,tau_k),
    tau_j=inf{t:(Lambda(t))_1>=j}, Lambda(t)=Lambda_(N(t)), (6)

with N a rate-one Poisson process. Therefore

    {X_k>t for all observations}
       =_d {(Lambda(t))_1<k for all observations}.        (7)

There are no atoms at deterministic positive times: every finite H_j is a discrete index independent of continuous arrival times. The strict inequalities in (7) are therefore valid; directly they follow from the definition of hitting times as well.

For nested shapes lambda^0=empty subset ... subset lambda^r at the observation times, let n_a=|lambda^a| and h_a=n_a-n_(a-1). The exact compressed path weight is

    exp(-T) [f^(lambda^r)/n_r!]
        product_a [ f^(lambda^a/lambda^(a-1))
                     (t_a-t_(a-1))^h_a/h_a! ].         (8)

Proof: the independent Poisson interval counts have probability exp(-T) product Delta_a^h_a/h_a!. Conditional on their total n_r and the input relative order, Q is a tableau U with probability f^(lambda^r)/n_r! by (5). The number of such U whose shapes at the selected label cutoffs are the prescribed shapes is the product of their skew-tableau counts: each interval is filled with its consecutive block of labels, and these fillings concatenate uniquely. Multiplying proves (8). This derivation does not require an unproved Markov assertion for a compressed hitting-time sequence.

Transpose every shape. Transposition preserves both ordinary and skew standard-tableau counts by transposing the filling, and the old first-row cap becomes a row-count cap. Write mu^a=(lambda^a)' . The final constraint is length(mu^r)<=d, and all earlier mu^a are contained in mu^r, so they also have at most d rows. This is why a finite d-particle construction represents the desired event exactly, rather than approximately. It is a subprobability ensemble, not an alternative normalized law substituted for (8).

## 3. Skew-tableau weights as finite particle minors

Encode a partition mu of length <=d by the d distinct nonnegative positions

    mu_i+d-i, i=1,...,d,

written in increasing order. The empty partition has positions b_i=i, i=0,...,d-1. Conversely any d distinct nonnegative positions determines exactly one such partition: subtract the staircase after sorting in decreasing order. Distinctness and nonnegativity ensure all resulting parts are nonnegative and nonincreasing.

For partitions lambda subset mu with position sets X,Y, respectively, the identity is

    det[p_u(y_i,x_j)]_(i,j=1)^d
       = f^(mu/lambda) u^(|mu|-|lambda|)/(|mu|-|lambda|)!. (9)

For non-contained shapes the determinant is zero.

Here is a finite algebraic proof, avoiding unquoted Schur-process conventions. Fix L at least the greatest position in both X and Y. On the vector space with basis e_0,...,e_L, let R e_x=e_(x+1) for x<L and R e_L=0. Then exp(uR) has entries p_u(y,x), since R^n shifts the index n places. On its d-th exterior power, let D act by the sum of R on each tensor factor. The differential equation for the exterior action gives

    wedge^d exp(uR)=exp(uD).

To verify this identity, differentiate the wedge of d evolving vectors: the product rule places R in each factor in turn, which is exactly D; at u=0 the action is the identity. Both sides solve this finite-dimensional constant-coefficient ODE, whose unique solution is its convergent exponential series.

In the ordered wedge basis e_(x_1) wedge ... wedge e_(x_d), a summand of D either increments one position by one while preserving strict order, or gives zero because two positions coincide (or it attempts to leave L). No permutation of surviving factors is needed, so every legal move has coefficient +1. Legal moves correspond exactly to adding one box to the partition. Thus the (Y,X) coefficient of D^n is the number of legal n-step paths of box additions. Every such path is equivalent to a standard filling of mu/lambda: label the box added at step j by j. Conversely a standard filling gives that legal addition order. All paths have exactly n=|mu|-|lambda| moves, since each move increases the sum of coordinates by one. If containment fails no such path exists. The coefficient of exp(uD) is therefore the right side of (9).

The coefficient of wedge^d exp(uR) in the same ordered wedge basis is the determinant on the left, by multilinearity and antisymmetry. This proves (9). The cutoff L does not change the conclusion: legal right-moving paths ending in Y never visit a larger position than max Y.

In particular the terminal factor f^mu/|mu|! in (8) is

    det[p_1(y_i,b_j)],                                  (10)

and each transition factor in (8) is the corresponding minor (9). Using increasing rather than decreasing positions reverses both row and column orders in these square minors, producing no determinant sign change.

## 4. Why row-count constraints are finitely many occupations

For a partition mu with at most d rows, length(mu)<=m is equivalent to its last d-m parts being zero. In particle coordinates this is equivalent to occupation of every site

    0,1,...,d-m-1.                                      (11)

The forward implication is immediate from the zero parts. Conversely these are the lowest possible d-m positions in a distinct nonnegative configuration, so if all are occupied they must be its lowest d-m positions. The corresponding last parts of mu are zero. This proves both directions and explains every marker in J.

After transposition, (7) is therefore exactly the final d-row restriction and the required occupations at the finitely many earlier markers. Simultaneous markers at different sites are genuine multiple occupations by different particles; they must not be treated as alternative possibilities.

## 5. Finite cutoff generating function and Cauchy-Binet

Fix L>=d-1 and allow positions only in {0,...,L}. Markers already lie below d and so lie within this cutoff. Give each marker alpha a variable z_alpha. At time s_alpha multiply the weight by 1+z_alpha if its site is occupied. The resulting path generating polynomial is obtained by multiplying, at each checkpoint, the diagonal one-particle operator whose value at site x is 1+z_(t,x) for listed sites and 1 at all other sites.

For a particle configuration the determinant of this diagonal restriction is the product of these factors over its occupied sites. Consequently repeated finite Cauchy-Binet applied to all time layers and the terminal matrix (10) gives the unnormalized generating polynomial

    D_L(z)=det A_L(z).                                  (12)

Explicitly, the sum on the other side of Cauchy-Binet runs over d-element subsets of {0,...,L} at every layer, in their fixed increasing order. Its factors are exactly the minors in (8)-(10), times the checkpoint occupation factors. There is no d! overcounting because each subset is summed once. Equation (8) supplies the overall probability factor exp(-T), outside (12).

The one-particle semigroup satisfies

    sum_y p_v(z,y) p_u(y,x)=p_(u+v)(z,x).                (13)

Proof: for z>=x it is the binomial identity

    sum_(j=0)^(z-x) v^(z-x-j) u^j/[(z-x-j)! j!]
       =(u+v)^(z-x)/(z-x)!,

and all terms vanish for z<x. At the finite cutoff (13) is still exact whenever both endpoints lie in {0,...,L}: all intermediate right-moving positions are between them.

Expand the diagonal checkpoint products in (12) and use (13) to combine unselected intervals. A path selected at markers alpha_1,...,alpha_l has strictly increasing marker times: a one-particle path cannot occupy two different sites at one time, and each checkpoint factor is linear in its site's variable. The resulting matrix is exactly

    A_L(z)=A_L+F Z (I-Q Z)^(-1) G_L,                    (14)

where Z=diag(z_alpha), A_L and G_L are the sums in (2) with terminal y<=L. F and Q need no truncation. To see every term, expand the inverse as the finite sum

    (I-QZ)^(-1)=I+QZ+...+(QZ)^(q-1),

since Q is strictly upper triangular when markers are ordered by time. The entry F_i,alpha z_alpha supplies the initial segment to the first selected marker; every Q_alpha,beta z_beta supplies the next segment; G_L supplies the final segment and terminal weight. These are precisely all subsets of selected checkpoints on a single path, with no repeated or same-time transition. Thus (14) is an equality of finite polynomial matrices.

The coefficient of product_alpha z_alpha in exp(-T) D_L(z) is the probability weight of exactly the event that all markers are occupied and the path remains within the terminal-position cutoff. Each factor is 1+z rather than z: configurations with all occupations contribute coefficient 1, irrespective of other positions.

## 6. Extracting that coefficient: audited signs

A_L is invertible for T>0. Indeed

    (diag(T^b_i) A_L)_ij
       =sum_(y=0)^L T^y/[(y-b_i)! (y-b_j)!],             (15)

with negative factorial terms zero. This is the Gram matrix of d real vectors. They are linearly independent, since their values at y=0,...,d-1 form a triangular matrix with nonzero diagonal. Hence it is positive definite for L>=d-1, and A_L is invertible. We only need this fact inside the proof, not for evaluating (3).

The elementary determinant identity det(I+UV)=det(I+VU), applied to (14), gives

    D_L(z)
      =det A_L det[I+(I-QZ)^(-1) G_L A_L^(-1) F Z]
      =det A_L det[I+(G_L A_L^(-1)F-Q) Z].              (16)

For completeness det(I+UV)=det(I+VU) follows by evaluating the determinant of the same block matrix [[I,U],[-V,I]] using either diagonal block as the Schur-complement pivot. In the second line of (16), multiply inside the determinant by I-QZ; its determinant is 1 because it is upper triangular with diagonal 1. This also proves the equality at the level of formal polynomials, rather than making assumptions about numerical variable values.

By column multilinearity, the coefficient of the product of all variables in det(I+KZ) is det K: choose the K column in every column; any identity column omits that column's variable. Thus the desired coefficient in (16) is

    det A_L det(G_L A_L^(-1)F-Q)
       =det [[A_L,F],[-G_L,-Q]].                       (17)

The last equality is the Schur-complement identity: the lower-right complement is -Q-(-G_L)A_L^(-1)F=G_L A_L^(-1)F-Q. There is no extra (-1)^q. GeneralBlockCertificate.lean formalizes this identity for arbitrary finite dimensions over a commutative ring and an invertible A; its successful kernel check is recorded separately. This formalization checks the general block signs, not the complete probabilistic proof.

## 7. Removing the finite cutoff

The left side of (17), multiplied by exp(-T), is a nonnegative subevent weight from (8). Increasing L increases the allowed terminal position sets. Monotone rightward paths have all earlier positions bounded by their terminal maximum, so this cutoff removes exactly paths whose final maximum position exceeds L. Every finite partition path has finite final positions. Monotone convergence therefore makes these probabilities increase to the desired event in (7).

Meanwhile the entries of A_L and G_L converge absolutely to A and G in (2). For E_u(a,b), the ratio of successive nonzero terms is

    u/[(n+1)(a+n+1-b)],

which tends to zero; convergence is uniform for u in a compact set. There are only finitely many entries. Polynomial continuity of a finite determinant hence makes the right side of (17) tend to det M. This proves (3) without any infinite determinant, trace-class hypothesis, or kernel convention.

When d=0, the final partition is empty. Box count is nondecreasing, so all earlier partitions are empty as well. The event is exactly N(T)=0 with probability exp(-T). Zero times and repeated times were handled before constructing the matrix. Equalities in time after merging never enter a falsely ordered Q connection. These arguments cover all boundary cases of the statement.

## 8. Useful closed three-particle consequence

For 0<=s<=t<=u and u>s, put a=u-s, b=u-t. Then

    P(X_1>s,X_2>t,X_3>u)
      =exp(-u) [ I_0(2 sqrt(a)) I_0(2 sqrt(b))
                  -sqrt(b/a) I_1(2 sqrt(a)) I_1(2 sqrt(b)) ]. (18)

For u=s, interpret the value as exp(-u). To derive it, X_1>s means no Poisson arrivals before s in (6); the independent remaining input starts from the empty tableau. The factor is exp(-s), and it remains to evaluate X_2>t-s, X_3>u-s in a fresh growth process. Here d=2 and the sole marker is (t-s,0), except the degenerate boundary handled by continuity. F=(1,0)^T. Expanding the 3-by-3 block determinant along this column gives

    A_11 G_00-A_10 G_01
      =I_0(2 sqrt(a)) I_0(2 sqrt(b))
         -sqrt(b/a) I_1(2 sqrt(a)) I_1(2 sqrt(b)).

The overall factor exp(-s)exp(-a)=exp(-u) proves (18). If t=s, the expression reduces to exp(-u)[I_0^2-I_1^2] at a; if t=u it reduces to exp(-u)I_0(2 sqrt(a)). These match respectively the third-particle scalar law and the known first-two law. Arbitrary unordered thresholds are already covered by (3); (18) is the concise ordered-threshold special case.

## 9. Validation, novelty, and exact scope

The historical representation (4) is explicitly credited as prior input and is not itself a claimed solution. The actual additional answer is the finite evaluation formula (3), and the Bessel-product triple law (18), derived above with a complete source-matching chain. Classical RSK, exterior-power determinant algebra, Cauchy-Binet and Eynard-Mehta ideas are not new. No publication was verified to state the complete source-specific result, so this is not a SOLVED_IN_LITERATURE claim. Historical priority of the composition is unverified.

Exact checks in finite_block_check.py compare all Taylor coefficients through degree 7 after simultaneous scaling of observation times by a variable v. The determinant coefficients are computed by rational power-series Gaussian elimination. Independent coefficients come from exhaustive permutations of sizes <=7 and all Poisson interval-count compositions. The independent check uses LIS of chronological input prefixes, not the determinant's transpose or skew-tableau formula. Fifteen cases pass, including scalar marginals, repeated and unordered constraints, nonmonotone row caps, fractional times, the d=0 boundary, and a 14-by-14 determinant for five particles. See finite_block_checks.json. Such finite checks are evidence against sign/time mistakes, not substitutes for Sections 2-7.

A separate positive finite-state growth computation in positive_growth_check.py propagates the central-measure transition f^nu/((n+1)f^mu), using integer hook dimensions, and kills paths at each row-count constraint. It retains total size <=32. The analytic omitted-mass bound is P(Pois(T)>32), because every discarded path has larger final box count. Seven 55-digit numerical checks agree with the determinant within that tail, including a five-coordinate event and redundant constraints. See positive_growth_checks.json. These are high-precision numerical checks with an analytic truncation bound, not interval-certified roundoff proofs. No determinant or skew-tableau minor is used in that positive computation.

The exact checker additionally leaves nonmonotone constraints unreduced in its independent permutation branch, so it also tests the suffix-minimum preprocessing. A general Lean block-sign check is recorded in general_block_lean.txt. The mathematical proof of (3) does not depend on the numerical checks.


## 10. Closed three-coordinate density and a second finite check

Define the entire functions

    L_j(v)=sum_(n>=0) v^n/[n! (n+j)!], j>=0,

so L_j(v)=v^(-j/2) I_j(2 sqrt(v)) for v>0, and L_j(0)=1/j!. Let 0<x<y<z, a=z-x and b=z-y. Differentiating (18) gives the explicit joint density

    p_3(x,y,z)=exp(-z) {
       L_1(a)[L_1(b)-L_2(b)]
       +[L_3(a)-L_2(a)]L_0(b) }.                       (19)

Here is the derivative calculation in full. The bracket in (18) is

    Phi(a,b)=L_0(a)L_0(b)-b L_1(a)L_1(b).

Termwise differentiation, justified by the factorial series, gives L_j'=L_(j+1) and L_1(b)+b L_2(b)=L_0(b). Hence

    Phi_b=L_0(a)L_1(b)-L_1(a)L_0(b),
    Phi_ab=L_1(a)L_1(b)-L_2(a)L_0(b).

Because a=z-x and b=z-y, the density is -partial_x partial_y partial_z [exp(-z)Phi(a,b)], equal to

    exp(-z) [Phi_ab-Phi_aab-Phi_abb].

Differentiating the preceding expression for Phi_ab and cancelling the opposite L_2(a)L_1(b) terms yields exactly (19). Existence and continuity of the density also follow from the historical independent-gamma mixture, so using the survival derivative introduces no distributional boundary term on the strict ordered support.

For g=y-x, h=z-y, substitute a=g+h,b=h. triple_density_check.py expands the brace in (19) through total degree four and compares all fifteen coefficients with independently enumerated permutation probabilities q_(1,r+2,r+s+3)/(r!s!), through permutation size seven. All checks pass; see triple_density_checks.json. At g=h=0 this brace gives 1/6, and its first derivatives give 1/8,1/8, consistent with the earlier non-Markov proof.
