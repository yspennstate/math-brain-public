# P0216 — research record, 2026-10-11

## Exact source model (verified against both linked PDFs)

Let (X_i,Y_i,U_i,V_i), 1<=i<=n, be independent uniform points of [0,1]^4. Define two strict orders on the SAME label set [n] by i<P j iff X_i<X_j and Y_i<Y_j, and i<Q j iff U_i<U_j and V_i<V_j. Let C_n be the maximum cardinality of S subset [n] for which the restrictions of P and Q to S are identical. Coordinate ties have probability zero. This is NOT uniform sampling from all combinatorial posets of dimension at most two; it is the random-point model.

The target is existence and evaluation of lim E[C_n]/n^(1/3). No proof of that limit is given here. All constructions below preserve labels, and also provide lower bounds if relabelling is allowed; the exponent question cannot be the latter model because of common chains.

The original excerpt common_subs.pdf has three PDF pages, printed pages 4–6. Its printed page 4 defines identical induced substructures on the same subset of labels; printed page 5, Example 4 defines the uniform-square model and conjecture (2). The May 2001 draft notes, PDF page 1, state the same model explicitly and conjecture both mean and probability limits. The notes already outline a stronger lower bound 0.728 and upper bound 3.85. Consequently the greedy-grid bound below does NOT improve the best bound outlined in this source. The notes, PDF page 2, explicitly say no subadditive argument for existence is known, contrary to the intake hint “Subadditivity gives the exponent.” No novelty is claimed for any result here.

## 1. Exact isolated-grid lower bound, with optimization

For an integer m>=1 partition each square into m^2 equal half-open cells (assign the upper endpoints to the final cell). A label is matched if its two points lie in the same cell (r,c). Retain a matched label only if no OTHER matched label has row r or column c. Distinct retained labels occupy different rows and columns. Their x-comparison in both samples is the comparison of their columns, and their y-comparison is that of their rows; hence every ordered pair has identical comparability in the two orders. This proves deterministic feasibility, including incomparable pairs.

For each label the matching probability is m^2*(1/m^2)^2=1/m^2. Conditional on its matched cell, an independent other label conflicts with it precisely by matching in one of 2m-1 cells in the union of its row and column. Each such outcome has probability 1/m^4, and these outcomes are disjoint. Independence over labels therefore gives the EXACT expected retained count

    n/m^2 * (1 - (2m-1)/m^4)^(n-1).

For n=1 the final factor means an empty product equal to 1, even for m=1. For m=1 and n>1 the count is zero, as the formula says.

Set m=floor(a n^(1/3)), with fixed a>0 and n sufficiently large. The prefactor divided by n^(1/3) tends to a^(-2). If q_m=(2m-1)/m^4 then nq_m -> 2/a^3 and nq_m^2 ->0. The identity log(1-q)=-q+O(q^2), valid as q->0, gives

    liminf E[C_n]/n^(1/3) >= a^(-2) exp(-2/a^3).

Writing lambda=a^(-3), this is lambda^(2/3) exp(-2lambda). Its logarithmic derivative is 2/(3lambda)-2, positive below 1/3 and negative above it. Thus the best constant in this construction is (3e)^(-2/3), attained at a=3^(1/3). In particular e^(-2), obtained with a=1, is not the best constant even in the recalled construction. This does not identify the optimal common-order constant.

## 2. Greedy row-column matching improves the construction

Process labels in their fixed order. Accept label i exactly if its two points are in the same cell and both the cell's row and column have not previously been used by an accepted label. The resulting set is feasible by precisely the pairwise comparison argument in section 1. Suppose r rows and r columns remain unused. Conditional on the entire past, the next independent label is accepted with probability r^2/m^4: there are r^2 eligible matched cells, each with probability 1/m^4. After acceptance r decreases by one.

Extend to an infinite independent sequence of labels for the analysis only. Let G_r be the number of label trials while r rows remain, including the accepting trial. These waiting times, as r decreases from m to 1, are independent geometric variables on {1,2,...}, with parameter p_r=r^2/m^4. To justify independence despite random used rows: conditional on ANY realized past, the waiting-time law depends only on r, not on which rows or columns remain, and the unused future labels are independent. Successive conditional laws are therefore fixed geometric laws; iterating conditional expectations factors their joint distribution. For p=1 the geometric variable is deterministically one.

Let T_k be the number of trials required to accept k labels. Then

    T_k = sum_{r=m-k+1}^m G_r,
    E[T_k] = m^4 sum_{r=m-k+1}^m r^(-2),
    Var(T_k) = sum_r (1-p_r)/p_r^2 <= m^8 sum_r r^(-4).

For completeness, a geometric variable G with parameter p has Pr(G>t)=(1-p)^t for integers t>=0. Summing tails yields E G=1/p. Since G^2=sum_{t=0}^{G-1}(2t+1), summing the same tails gives E G^2=2(1-p)/p^2+1/p=(2-p)/p^2, and therefore Var G=(1-p)/p^2. The series identities follow by summing the geometric series and its derivative for 0<=1-p<1. Independence gives the displayed variance sum.

For fixed 0<y<1 and k=floor(ym), the Riemann sum gives

    E[T_k]/m^3 -> integral_{1-y}^1 x^(-2) dx = y/(1-y).

For sufficiently large m every r in this sum is >= (1-y)m/2. There are at most m summands, so Var(T_k)/m^6 <= 16/((1-y)^4 m) ->0. Chebyshev's inequality proves T_k/m^3 -> y/(1-y) in probability.

Now let n/m^3 ->lambda in (0,infinity), and A_n be the number accepted after n trials. Put y*=lambda/(1+lambda). For any fixed y<y*, the event A_n<floor(ym) is the event T_floor(ym)>n and its probability tends to zero by the preceding limit and strict inequality y/(1-y)<lambda. For y>y*, the event A_n>=floor(ym) similarly has probability tending to zero. Consequently A_n/m ->y* in probability. Because 0<=A_n/m<=1, convergence of expectations follows: for any epsilon>0, E|A_n/m-y*| <=epsilon+Pr(|A_n/m-y*|>epsilon), and then let epsilon decrease to zero.

With m=floor(a n^(1/3)), we obtain

    E[A_n]/n^(1/3) -> a/(1+a^3).

The derivative is (1-2a^3)/(1+a^3)^2, so its maximum for a>0 occurs at a=2^(-1/3) and equals 2^(2/3)/3, approximately 0.529133684. Thus rigorously

    liminf E[C_n]/n^(1/3) >= 2^(2/3)/3.

This is an improvement over the recalled isolated-cell bound, within the established grid method. No novelty claim is made. It determines the limit for this particular greedy algorithm, not for the largest common suborder.

## 3. Variance reduction: a mean limit suffices for a probability limit

For every n, Var(C_n)<=E C_n. This is a general deletion-certificate argument, fully proved here.

Write Z_i=(X_i,Y_i,U_i,V_i), independent for i=1,...,n, and F=C_n. Let F_i be the maximum coincidence size on all labels except i, as a function of Z_{-i}. Restricting any feasible set to labels other than i is feasible; hence 0<=F-F_i<=1. Fix an optimal feasible S (choose the lexicographically first one if a selection rule is desired). If i is outside S then F_i=F. Consequently

    sum_i (F-F_i)^2 = sum_i (F-F_i) <= |S| = F

pointwise. This proof does not assume optimal sets are unique.

Here is the independent-variable variance inequality needed to use that fact, with its proof. Let M_i=E[F|Z_1,...,Z_i], M_0=EF, and Delta_i=M_i-M_{i-1}. The increments are pairwise orthogonal in L^2 because each has conditional mean zero given the preceding sigma-field. Thus Var F=sum_i E Delta_i^2. Let B_i=E[F|Z_{-i}]. Independence and iterated integration give E[B_i|Z_1,...,Z_i]=M_{i-1}: in B_i the integration over Z_i has already been performed, and conditioning integrates the remaining future variables. Therefore Delta_i=E[F-B_i|Z_1,...,Z_i]. Conditional Jensen yields

    Var F <= sum_i E[(F-B_i)^2].

Conditional expectation is the best squared-error approximation by a function of Z_{-i}. More explicitly, since E[F-B_i|Z_{-i}]=0 and F_i is Z_{-i}-measurable,

    E[(F-F_i)^2] = E[(F-B_i)^2] + E[(B_i-F_i)^2].

Summing and applying the pointwise certificate inequality proves Var F<=E F. All variables are bounded by n, so every conditional expectation and L^2 step is justified.

In particular if E C_n=O(n^(1/3)), as outlined in the source, then

    E[(C_n/n^(1/3)-E C_n/n^(1/3))^2] <= E C_n/n^(2/3) = O(n^(-1/3)).

Thus any proven mean limit c immediately gives convergence in L^2 and in probability to c. Conversely, under that same upper bound, probability convergence to c implies mean convergence: the means are bounded and the above difference tends to zero in probability, so if the deterministic means failed to converge to c along a subsequence, the triangle inequality would contradict probability convergence. No upper bound with an explicit constant is newly proved in this section: the displayed implication is conditional on the O(n^(1/3)) bound. The finite variance inequality itself is unconditional.

At n=0 the maximum is zero and the variance bound is exact; at n=1 it is one and has zero variance. At n=2 a point pair is ordered in either direction with probability 1/4 each and incomparable with probability 1/2. Two independent orders coincide with probability (1/4)^2+(1/4)^2+(1/2)^2=3/8. Thus C_2=1+Bernoulli(3/8), E C_2=11/8, and Var C_2=15/64. These are same-label probabilities.

## Referee risks and remaining gap

The same-label random-point model is now verified. Feasibility requires distinct rows AND distinct columns; allowing two edges in one row invalidates the deterministic argument. Waiting times count original labels, not just the matched labels. The normalization is m^3, not m or m^2. The variance estimate is only used for fixed y<1; no unjustified uniform estimate near saturation is needed. The proof of expectation convergence uses boundedness of A_n/m, not an unproved uniform integrability statement for C_n/n^(1/3).

The unresolved question remains: prove convergence of E[C_n]/n^(1/3) and evaluate its optimal limit. Neither the greedy algorithm nor optimization of its parameter yields an upper bound with the same constant. Different coordinate-sign patterns can also agree as posets; coordinatewise sign agreement is sufficient, not necessary.

## 4. Why elementary monotonicity and concentration do not close the gap

Put a_n=E C_n. Adding one label changes the maximum by zero or one, so 0<=a_n-a_(n-1)<=1. Delete a uniformly random label from an n-label sample, independently of its coordinates. Its resulting law is that of n-1 independent labels, after an immaterial renaming. For a fixed optimal S, its restricted size is C_n-1_{I in S}. Averaging over I gives a_(n-1)>=(1-1/n)a_n. In particular a_n/n is nonincreasing.

These conditions, even together with two-sided n^(1/3) bounds, do not imply a limit at that scale. Here is an explicit counterexample to that proposed inference (NOT to P0216): b_0=0 and b_n=f(n), where

    f(x)=x^(1/3)(1+(1/10) sin(log x)), x>=1.

The derivative is x^(-2/3)[1/3+(1/10)((1/3)sin(log x)+cos(log x))]. Since the absolute oscillating term in brackets is at most sqrt(10)/30<1/3, the derivative is positive and is less than 1 for x>=1. Thus 0<b_n-b_(n-1)<1 for n>=2, and b_1-b_0=1. Moreover (f(x)/x)' is x^(-5/3)[-2/3+(1/10)(-(2/3)sin(log x)+cos(log x))], strictly negative because sqrt(13)/30<2/3. Thus b_(n-1)>=(1-1/n)b_n. Finally 0.9 n^(1/3)<=b_n<=1.1 n^(1/3), but b_n/n^(1/3) has subsequential limits 1.1 and 0.9 by rounding exp(2pi k+pi/2) and exp(2pi k+3pi/2) to integers (rounding changes their logarithms by a quantity tending to zero). This proves that the elementary expectation inequalities alone cannot establish convergence. The example is a real sequence, not the expectation of the actual poset maximum.

## Completed checks

checks.py exhaustively examined all 16^3=4096 independent cell-pair sequences with m=2,n=3. The greedy count distribution is (27/64,549/1024,43/1024) on counts 0,1,2 and exactly equals the finite pure-death transition recursion with acceptance probability (m-k)^2/m^4. The isolated construction mean is exactly 507/1024, equal to its formula. Every ordered pair of accepted labels passed the cell-comparison feasibility test.

The same script simulated the EXACT geometric waiting-time representation, seed 216, 300 runs for each m=20,100,500,2000 with n=2m^3. Means of A_n/m were 0.67900,0.66650,0.66687,0.66643; standard errors were 0.00420,0.00197,0.00088,0.00043. The asymptotic prediction is 2/3. Large n values here do not require generating n labels: geometric skips give O(m) work per repetition and constant auxiliary space. These are checks of the proved algorithm limit, not estimates of the optimal c.

exact_posets.py enumerated pairs of coordinate rank permutations and grouped by their induced labeled orders, then weighted pairs of those orders by representation multiplicities. The total weights are (n!)^4. For n=1,2,3,4 the exact means are 1,11/8,65/36,2467/1152. Histograms and floating variances are in exact_posets.json; all deletion-certificate inequalities were checked pointwise for every pair of induced orders. Memory stays far below 1 GB.

GridAgreement.lean formalizes strict-comparison agreement from distinct ordered bins and conjunction of coordinate comparisons. This is deliberately only the deterministic algebraic portion, with Nat ranks. It does not formalize probability, limits, the variance bound, or the open conjecture. On 2026-10-11, `lake env lean ~/brain_workers/TRIO_1011/op/P0216/GridAgreement.lean`, run from ~/lean_verify, acquired a shared slot after 461 seconds and completed with exit code 0 and no diagnostic output. There is no sorry or native_decide. This uses kernel-checked omega proof generation, not a native computation oracle. See lean_check.json for the checked file hash.

## 5. Further serious attempt (2026-10-11)

The full mathematics and referee audit are in CONTINUATION.md. Two previously untried approaches were written down: balanced-permutation collision enumeration, and Poissonized geometric concatenation. The former was pursued through an exact graph-orientation reduction and a rigorously audited Gallai modular-decomposition encoding.

New proved result: if p_k denotes the probability that two k-label orders are identical, then

    1/(k!)^2 <= p_k <= 4 exp(2sqrt(32k))/(k!)^2.

Thus (p_k(k!)^2)^(1/k)->1, proving beta=1 in Aldous–Brightwell's collision Subproblem 4. The full finite encoding, weighted-tree coefficient bound, and established structural-theorem hypotheses are written out in CONTINUATION.md. Applying a convex binomial-moment bound and a subsequence argument gives

    limsup E C_n/n^(1/3) <= K = exp(r*)/(r*)^(2/3)
       = 2.668162063280738...,
    log(1-r*)=-3r*, r* in (2/3,1).

The exact implicit K is the proved bound; its displayed decimal is a numerical evaluation. This improves the draft's outlined beta<=3 upper constant 3.85 by proving the beta=1 premise of its conditional 2.67 calculation. No novelty claim is made. The full optimal-mean limit's existence and value remain unproved; K is not identified as that limit.

Further referee check: for the unweighted count N_k of agreeing k-subsets, its normalized second moment grows exponentially at k~a n^(1/3) for every fixed a>=12/5. The proof in CONTINUATION.md uses pairs overlapping in 4k/5 labels and the exact positive exponent [log(250000)-12]/5. Therefore the direct Paley–Zygmund bound on this count tends to zero before reaching the upper constant K. This is a method obstruction, not a bound showing C_n is smaller than 2.4 n^(1/3). An exact formal-series identity for collision counts is also derived in CONTINUATION.md, with coefficients independently checked through n=16.
