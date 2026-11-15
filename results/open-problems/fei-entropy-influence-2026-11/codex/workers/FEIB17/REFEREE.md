# Referee report on FLOW sections 7, 9 and 10

FEIB17, 10 November 2026. Logs are base 2, entropy is in bits. The version read is the FLOW.md present at task start. The launching session owns corrections to that file; I have changed only my worker folder. Statements below are proved unless explicitly marked CHECKED or OPEN. A supremum over Boolean functions excludes constants when dividing by influence.

The requested verdicts are: (a) correct and sharp; (b) correct; (c) correct; (d) correct with the stated unoriented edge normalization; (e) soft approximation correct, raw KL identification false; (f) construction correct, exact influences and point-dependent block sizes need qualification; (g) complex obstruction correct, with corrections to adjoining prose; (h) exact witness and first bound correct, last bound false without an extra hypothesis.

## (a) One-coordinate decomposition and sharp JS constant — PROVED

Write a_T=fhat(T), b_T=fhat(T+i), m_T=a_T^2+b_T^2 and delta=Inf_i. Both restrictions are Boolean, so their spectral laws p_+=(a+b)^2 and p_-=(a-b)^2 have total mass one. Their average m is the law of U minus i. The entropy chain rule gives

    H(f)=H(m)+E_i,
    J_i=H(m)-(H(p_+)+H(p_-))/2,
    D_i=E_i+J_i.

Concavity of Shannon entropy proves J_i>=0. For a real pair let t=2ab/m and
j(t)=[(1+t)ln(1+t)+(1-t)ln(1-t)]/2. Then the pair's JS contribution is m j(t)/ln 2. Since

    atanh(t) <= t/sqrt(1-t^2),    0<=t<1,

integration gives j(t)<=1-sqrt(1-t^2). To check the derivative comparison, the derivatives of t/sqrt(1-t^2) and atanh(t) are respectively (1-t^2)^(-3/2) and (1-t^2)^(-1), and both functions start at zero. Symmetry handles negative t. Thus

    J_pair <= [m-|a^2-b^2|]/ln 2
           = (2/ln 2) min(a^2,b^2).

Summation proves J_i<=(2/ln 2)delta. The weaker intermediate inequality 1-h((1+t)/2)<=t^2 is also true: expand j(t)/ln 2 as a power series with positive coefficients and use t^(2k)<=t^2; the coefficient sum is one at t=1.

Sharpness holds within real Boolean functions, not just arbitrary real pairs. Use the bent-point family in (f), without needing majority composition. On every coefficient pair b^2/a^2 is (2^(m/2) plus or minus 1)^(-2), tending uniformly to zero. Taylor expansion j(t)=t^2/2+O(t^4) gives J_i/delta ->2/ln 2. The exact product calculations and direct truth-table checks are in exact_families.json. This also proves the degree-two homogeneity and edge formula for D_i in 7(b), by substituting eta(x)=-x log x and observing that the log of a common scale cancels.

CHECKED: audit.py transforms the actual restrictions independently of its E and J formulas. All four-variable functions, and the stated samples at n=6,7,8, pass. The numerical value of 2/ln 2 is in witnesses.json.

## (b) Paths, erasure equivalence and the two brackets — PROVED

For j different from i, Parseval applied to the two restrictions gives

    (Inf_j(f_+)+Inf_j(f_-))/2=Inf_j(f).

Consequently I(f)=delta+(I(f_+)+I(f_-))/2. The corresponding entropy equality is the definition of D_i. Induct on any finite decision tree that chooses a currently live coordinate, with each branch answer uniform and independent of previous answers. At a constant leaf both remaining H and I vanish. This proves both expected path sums, even with adaptive query order. A partial tree needs its expected leaf H and I added; a tree that reuses a fixed coordinate is not the stated decision tree on live coordinates.

For a uniform order, assign independent uniform labels and delete the largest first. A fixed coordinate has label p with density dp; the others alive then have independent survival probability p. Hence summing the query costs gives

    H(f)=integral_0^1 E Psi(f_rho_p) dp/p,
    I(f)=integral_0^1 E sum_alive Inf_i(f_rho_p) dp/p.

The second equality also follows directly from E sum_alive Inf_i(f_rho_p)=p I(f). These finite-polynomial integrals have no convergence issue. For example, a restriction with alive set A of size a has integrated coefficient 1/[a binom(n,a)], which reductions.py uses to check the formula without numerical quadrature.

Let C_E=sup H^-/I and c_0=2/ln 2. Chain rule in any fixed coordinate order gives

    sum_i H(U_i | U_-i) <= sum_i H(U_i | U_<i)=H(U).

Thus C_E<=C*. If C_E is finite then at every node sum_i D_i<=H^-+c_0 I<=(C_E+c_0)I, so some positive-influence coordinate has D_i/Inf_i<=C_E+c_0. Query it recursively. The path formula yields C*<=C_E+c_0. The argument also holds for extended-real suprema.

Let R=sup_f min_{i:Inf_i>0}D_i/Inf_i. A tree choosing a minimizing coordinate proves C*<=R. The weighted-average bound sum_iD_i<=H+c_0 I proves R<=C*+c_0. Both requested brackets are correct. No attainment of a supremum in unbounded dimension is needed.

CHECKED: path_census.json checks two alternating adaptive policies on all four-variable functions and the exact random-order integral on the same census. Another 400 adaptive trees and exact random-order integrals at n=4,6,7,8 are in audit_results.json and reductions.json. The comparisons between global suprema are theorems, not finite census inferences. The finite record values in 9(a) are checked in records.json; the self-composition justification for its limiting lower bound is below.

## (c) G versus erasure entropy — PROVED

On each edge with lower mass p=a^2 and upper mass q=b^2,

    Phi(p,q)=p log(1+q/p)+q log(1+p/q).

The first term is nonnegative and at most q/ln 2, using ln(1+x)<=x. These statements extend continuously when p or q is zero. Sum over all edges. The sum of upper masses is I. This proves

    G<=H^-<=G+I/ln 2.

Together with (b), G<=CI for every Boolean f is equivalent to FEI. The interpretation of the coefficient pair as the mean and one level-one coefficient of f chi_(U-i) is correct. Heavy-upper edges have only a bounded cost per upper mass; “only steep edges matter” must use the corrected constant given below, not the constant printed in 10(a).

## (d) Edge-law identity — PROVED

There is one unoriented edge e=(T,T+i) for each i not in T. For I>0 set

    P(e)=mu(T+i)/I,
    Q(e)=[mu(T)+mu(T+i)]/n.

Their masses are one: a vertex contributes its mass |U| times to the P numerator and n times to the Q numerator. P is supported inside Q. Direct substitution gives

    KL(P||Q)=log(n/I)-G/I.

Thus the displayed identity and its constant are exact. Q is the law of the unoriented edge obtained by drawing a spectral vertex and toggling a uniform coordinate. It is not solely an upward transition from the drawn vertex; that informal description in 9(d) needs qualification. Using oriented edges without adjusting Q changes the normalization.

Replacing log(1+r) by log^+(r) changes the P-average by at most one, since 0<=log(1+r)-log^+(r)<=1. The positive-log formulation is therefore equivalent up to I, not literally identical.

The symmetric ratio mu(T)/mu(T+i)=(W_(k-1)/W_k)(n-k+1)/k is correct for |T+i|=k. The following sentence, that consecutive low levels cannot both have comparable weights, is false. A symmetric threshold at n/2+(1/4)sqrt(n) has both W_0 and W_1 bounded away from zero. witnesses.json constructs this explicitly; at n=16384 it has W_0=0.14243971109411008 and W_1=0.49967303746189573. Its large influence pays for the steep singleton edges. A sparse product law is an obstruction, but the claim that it is the “only obstruction” is a heuristic, not a proved classification of laws.

CHECKED: audit_results.json verifies Q normalization and the identity on the full four-variable census and the samples. Constants have I=G=0; P is undefined there and should not be introduced.

## (e) Pair form — soft approximation PROVED; unsmoothed KL equality FALSE

Put u=f_+, v=f_-, a=(uhat+vhat)/2, b=(uhat-vhat)/2. Pointwise f_1 is u on B={u!=v} and zero elsewhere; f_0 is u off B. Multiplication by 1_B is an orthogonal projection in Fourier space, with every diagonal entry E 1_B=delta. Thus the operator description is correct.

Define

    L_i=sum_T b_T^2 log(1+uhat(T)^2/b_T^2).

For real x, 1+(x-1)^2 and 1+x^2 are within a factor 3 of each other. Apply this with x=uhat/b, so a/b=x-1. The per-pair logarithms in G_i and L_i differ by at most log 3. Part (c) then proves

    |E_i-L_i| <= (log 3+1/ln 2)delta.

The requested error term is valid. In fact the factor 3 improves to gamma=(3+sqrt(5))/2: the quadratic-form ratio has eigenvalues gamma and 1/gamma. Therefore the error constant improves to log gamma+1/ln 2. audit_results.json tests both constants before using the sharpened version as a theorem. witnesses.json computes their values, respectively 3.0276575416101195 and 2.831178868150198 bits per unit influence.

The next equality in 9(b) is false. In general

    sum b^2 log(1+uhat^2/b^2)

is not within O(delta) of sum b^2 log(uhat^2/b^2), even after taking a positive part of the latter. For a concrete finite counterexample take u=1 on two remaining variables, v=-1 at (1,1) and +1 elsewhere. Then delta=1/4, b is the indicator of that point, all four b coefficients have magnitude 1/4, uhat vanishes at three of them, and a=uhat-b. Here

    E_i=(5/8)h(1/10)+3/8 >0,
    L_i=(1/16)log 17,
    KL(b^2/delta || uhat^2)=infinity.

Both E_i and L_i are finite. The raw expression delta[log(1/delta)-KL] is minus infinity. Even a positive part would give zero while, in the bent family, E_i/delta grows without bound although a single such support defect can make raw KL infinite. No truncation of an aggregate raw KL repairs the equality in general.

A correct exact replacement is

    nu=b^2/delta,
    q=(uhat^2+b^2)/(1+delta),
    L_i=delta[log((1+delta)/delta)-KL(nu||q)].

This q is a probability law dominating nu. For the original a,b pair there is an even simpler exact formula:

    m=a^2+b^2,
    G_i=delta[log(1/delta)-KL(nu||m)],
    G_i<=E_i<=G_i+delta/ln 2.

These are the corrected KL criteria for a good coordinate. The raw signed-log identity in 7(f) is valid in the extended-real sense when delta is strictly between zero and one, but its ensuing approximation to E_i and the KL “i.e.” in 7(g) do not follow. Here is also an unbounded-ratio counterexample to taking a positive part of raw KL in 7(f). Start with bent h on m bits, write s=2^(m/2), choose two points B where h=1, and flip (s-2)/2 other positive values to define u. Put v=u-2 1_B. Then delta=2/s^2 and a_empty=0, b_empty=2/s^2, so KL(b^2/delta || a^2/(1-delta)) is infinite. The change from h has squared Fourier norm at most 2/s, so at most 8s coefficients of u differ from the bent magnitude 1/s by more than 1/(2s). The b spectrum is flat on s^2/2 characters. Outside a fraction at most 16/s of those characters, |a|>=1/(4s) for s>=8, and hence E_i/delta>=G_i/delta>=(1-16/s)log(1+s^2/64), which diverges. Flipping s/2 positive values instead gives u_empty=0 and the same unbounded-ratio obstruction to raw KL in 9(b). singular_examples.json checks both versions at m=4,6,8,10,12. Mixture references avoid every support issue.

The sufficient-set condition in 9(b) survives. Let nu(Q)>=1-epsilon, mu_u(Q)<=C delta and epsilon<=c/log(1/delta). Concavity of log gives

    L_Q <= delta nu(Q) log(1+mu_u(Q)/(delta nu(Q)))=O(delta),
    L_Qc <= delta epsilon log(1+1/(delta epsilon))=O(delta).

Handle delta>=1/2 by E_i<=h(delta)<=2delta. Thus L_i and then E_i are O(delta). The incorrect raw KL argument should be replaced by this calculation. If u is a character and delta tends to zero, all nonexceptional pairs have a=-b; their erasure is exactly 2b^2. The exceptional coefficient contributes O(delta^2 log(1/delta)), so E_i=2delta+O(delta^2 log(1/delta)) as claimed.

## (f) Bent of majorities with one point replaced — PROVED with corrected influences

Use bits y in {0,1}^m, m even, h(y)=(-1)^(sum y_(2j-1)y_(2j)), and replace the all-zero point by a fresh coordinate z. Let d=2^-m, s=2^(m/2), and let each y_j be a balanced odd majority on r fresh bits. On the outer cube

    f_0=h-1_[y=0],    f_1=1_[y=0],
    a_A=hhat(A)-d,    b_A=d.

Bentness gives hhat(A)=plus or minus 1/s. There are N_+=(2^m+s)/2 plus signs and N_-=(2^m-s)/2 minus signs, since sum_A hhat(A)=h(0)=1. Hence

    a_A^2/b_A^2=(s-1)^2 or (s+1)^2.

Balanced composition preserves these ratios. A Fourier set meets exactly the outer blocks belonging to A; because the majorities have zero mean, no other outer character contributes to that same set. The total squared product weight over each block expansion is one. Define F(r)=(1+r)h(1/(1+r)). Exactly,

    E_z/d = 2^-m [N_+ F((s-1)^2)+N_- F((s+1)^2)].

This is m+log_2(e)+O(2^-m), in particular m+O(1). No huge truth table is used to obtain it.

The influence printed in 9(c) omits a real change at the replaced point. Every original h direction is nonpivotal along the all-zero edge. Replacing its one endpoint by a random z adds d, so every outer y_j has influence 1/2+d, exactly. For other choices of the replaced point the influence can be 1/2-d instead, depending on that edge. Each inner bit therefore has influence

    (1/2+d) c_r,    c_r=binom(r-1,(r-1)/2)/2^(r-1),

whereas Inf_z=d. The fresh coordinate is uniquely most influential if and only if (1/2+d)c_r<d for this chosen point. The asymptotic threshold in FLOW neglects the d term and cannot be used as a finite sufficient condition.

Exact results from exact_families.json:

| m | least odd r | variables mr+1 | E_z/Inf_z | D_z/Inf_z |
|---|---:|---:|---:|---:|
| 2 | 7 | 15 | 2.672488983973203 | 4.867668746754797 |
| 4 | 53 | 213 | 5.224357932670612 | 8.030013847484557 |
| 6 | 695 | 4171 | 7.386758947438571 | 10.255970235276205 |

The script uses exact rational binomial probabilities to prove strictness, and verifies failure at r-2. For m=4, r=41 is not sufficient for this point. FLOW leaves x* unspecified: r=41 does work at the all-one bit point, where every replaced edge was pivotal and the outer influences are 1/2-d. Thus its finite number needs a point specification rather than being false for every choice of x*. The alternative point thresholds are also recorded in exact_families.json. Direct outer truth-table transforms at m=2,4,6 reproduce the product formula and outer influences independently.

The block coordinates remain uniformly good. Let gamma=1/2+d be an outer block influence and c=c_r. Odd majority has only odd-degree Fourier support. For an inner coordinate the only pairs with both endpoints nonzero have that block empty at the lower endpoint and a singleton at the upper endpoint. Jensen therefore gives

    E_inner/Inf_inner <= c[log(1+(1-gamma)/(c^2 gamma))+1/ln 2].

Because gamma>=1/2, c log(1+2/c^2) is bounded uniformly for 0<c<=1. Add the JS bound for D_inner. Thus the example refutes choosing the largest influence, while leaving cheap block coordinates available.

## (g) Complex unimodular example and marginal proxy — PROVED

For f(x)=product_j(sqrt(1-p)+i sqrt(p)x_j), every value has modulus one. Its Fourier coefficient at S is (i sqrt(p))^|S| sqrt(1-p)^(n-|S|), so mu is the Bernoulli-p product law. Consequently

    I=np,    H=H^-=n h(p),    G=np log(1/p).

H/I=h(p)/p tends to infinity as p tends to zero. Restricting one variable changes only a unit complex phase, so J_i=0 and D_i=E_i=h(p). The real-Boolean relations f_0 f_1=0 and f_0^2+f_1^2=1 fail. The correct unimodular relations involve conjugates and Re(f_0 conjugate(f_1))=0. The derivative is supported everywhere instead of on a set of density its squared norm. extra_checks.json checks actual complex truth tables at n=4,6,7,8; exact_families.json records the analytic product statistics.

For any real Boolean function, E_i<=h(Inf_i) and J_i<=c_0 Inf_i prove

    H<=K+c_0 I,

with K as in 9(e). Thus calling K an upper bound on H-c_0 I is correct, though the clearer inequality is the one just written.

The tribes proxy really has the stated linear-in-width loss, for both query policies; it is not evidence that E_i itself has that loss. Here is a proof. Let beta=2^-w, q=1-beta and s beta bounded above and below. Since delta log(1/delta)<=h(delta)<=delta log(1/delta)+delta/ln 2, it suffices to average pivotality-weighted log(1/delta).

For the greedy policy, index the current tribe by t and the number of remaining bits in it by l. Its influence is 2^(-(l-1))q^(t-1). The probability of reaching that position is q^(s-t)2^(-(w-l)). Their product is 2^(-(w-1))q^(s-1), independent of t,l. Thus the pivotality-weighted average logarithm is exactly

    (w-1)/2 + (s-1)log(1/q)/2.

The marginal proxy divided by I differs from this by between zero and 1/ln 2. This is w/2+O(1).

For uniform random order at survival probability p, condition on a fixed bit's pivotality weight. The expected number of live siblings in its own tribe is (w-1)p: each sibling is alive with conditional probability p. Every other tribe contributes a conditional log cost at most beta/(q ln 2), since x log(1/x)<=(1-x)/ln 2 and its averaged unsatisfied probability is q. Using E sum_alive Inf_i=pI and integrating dp gives

    (w-1)/2 <= K/I
               <= (w-1)/2+(s-1)beta/(q ln 2)+1/ln 2.

Again K=(w/2+O(1))I on balanced tribes. The exact greedy recursion and numerical values are in exact_families.json.

## (h) Block witnesses — corrected theorem PROVED

Let A=I_N=P[U meets N], delta=Inf_i, eta=P[i in U,U misses N]. Conditioning on the two-cell statistic gives exactly

    H(U_i | 1[U_-i meets N])
      = A h((delta-eta)/A)+(1-A)h(eta/(1-A)).

Cells of mass zero contribute zero. Data processing gives E_i no larger than this. Moreover (1-A)h(eta/(1-A))<=h(eta): for fixed eta, t h(eta/t) increases with t on eta<=t<=1. Thus the first inequality printed in 10(d) is correct.

The next inequality is false without an extra hypothesis. A nondegenerate Boolean counterexample is f(x_i,y)=x_i AND_4(y), with AND taking signs and N one y coordinate. Then

    delta=1,    A=1/8,    eta=7/8,    E_i=0,

whereas the claimed last right side is -0.1263823551335972 bits. Every variable is relevant. reductions.json obtains these values from a direct transform. N empty, or an irrelevant N, also makes the displayed logarithm undefined.

A valid universal replacement is

    E_i <= (delta-eta)log(e A/(delta-eta))
           +eta log(e(1-A)/eta)
        <= delta log(e(A+eta)/delta)+eta log(e/eta).

The first follows by expanding both binary entropies and using ln(1+x)<=x. For the second, first bound the two-cell expression by A h((delta-eta)/A)+h(eta), use A+eta>=delta, and use monotonicity of t log(e(A+eta)/t) for 0<=t<=delta. The original last formula is valid under the additional hypothesis delta<=A, by the same monotonicity argument with A instead of A+eta.

The sufficiency assertion survives: if A<=C delta and eta<=delta/log(1/delta) for small delta, then A+eta<=(C+1)delta and eta log(e/eta)=O(delta). For delta>=1/2 use E_i<=1<=2delta.

For tribes with N the other bits of the tribe, the exact values are

    eta=2 beta delta,    A=2(1-2 beta)delta,

where beta=2^-w. These satisfy the criterion at large width. In the special width-two case A=delta. The general uniform tribes assertion D_i=O(delta), including arbitrarily biased tribe counts, follows instead from the exact pair formula in the next subsection.

The majority sentence has a second quantitative error: I_N has order sqrt(|N|/n), not |N|/sqrt(n), when 1<<|N|<<n. Indeed for k=|N|, let q_k(s)=P[sum of k signs=s]. Then

    eta=E_{S_(n-1-k)} q_k(-S)^2,
    I_N=E_{S_(n-k)} [1-(E_{S_k} sign(S+S_k))^2].

Stirling's formula and the local central limit estimate give

    eta/Inf_i ~ 1/sqrt(pi k),
    I_N ~ (2 sqrt(2)/pi)sqrt(k/n).

For the second constant, integrate 1-(2 Phi(t)-1)^2; its integral is 4/sqrt(pi). Dominated convergence follows by the binomial Gaussian tail bound. These estimates imply k of order at least log^2 n for the stated eta threshold, and I_N/Inf_i of order sqrt(k), which is still unbounded. Thus the qualitative conclusion about this block witness is correct. Exact binomial sums for several n,k are in witnesses.json.

## Remaining displayed claims in sections 7, 9 and 10

The following completes the line-by-line pass beyond the requested eight letters.

7(a): P<=B follows from (E g)^2<=P[g!=0] E g^2. Its conditional-moment expression is exact on positive spectral mass. To justify FEI iff B<=CI, use Boolean derivative granularity: for nonempty S, |fhat(S)|<=2^(|S|-1)up(S). Hence A<=B+2(I-Var), and H=A+B<=2B+2(I-Var). All zero-mass terms are omitted. This also handles biased empty terms correctly.

7(f), 7(g): the raw signed-log divergence identity has the endpoint/support qualifications explained in (e). Replace the proposed good-coordinate raw KL criterion by the exact mixture criterion there. The existence-of-good-coordinate equivalence itself is correct: convert E to D with the JS bound and use paths. E_i<=h(delta)<=delta log(e/delta) is correct.

7(g), extremizers: on finitely many n-variable truth tables a maximizer exists. For every i,

    D_i >= C_(n-1)delta+(C_n-C_(n-1))I >= C_(n-1)delta.

Together with D_i<=delta[log(1/delta)+3/ln 2] this proves the printed influence ceiling, with 4.33 a rounded value of 3/ln 2. The claim about every sequence of counterexamples having no cheap coordinate is too broad. If any bad sequence exists, XOR with a fresh dictator supplies a coordinate of influence one and D_i=0 while retaining unbounded H/I after first arranging I>=1 by tensor copies. The conclusion about small influences and no uniformly cheap coordinate applies to an appropriate extremizing or restriction-critical sequence, not to arbitrary examples. No actual counterexample to FEI is asserted here.

7(h): the uncomposed bent-point example follows from (f). Global input parity f(-x)=plus or minus f(x) makes spectral degree parity fixed, so U_-i determines U_i and E_i=0. For a bent function each pair has a^2=b^2, E_i=J_i=1 and D_i=2, hence Psi=2n=4I. For an address function, selector coordinates have D_i=2 and data coordinates D_i=0, hence Psi=2a when a denotes the number of address bits. records.json checks a=1,2,3.

For AND_n every nonempty mass is q=4^(1-n), and mu(empty)=(1-2^(1-n))^2. Each coordinate has

    E_i=Phi(mu(empty),q)+(2^(n-1)-1)2q,

and D_i=O(2^-n) follows by adding the JS terms; the exceptional pair is O(n4^-n), all remaining pairs cost 4q each. This also proves H^-/I ->2, as used in PROOFS.md.

For tribes define beta=2^-w, q=1-beta, delta=2 beta q^(s-1), eta=2 beta delta and mu0=(2q^s-1)^2. The exact erasure formula is

    E_i=2(delta-eta)+(eta-delta^2)F((q/beta)^2)+Phi(mu0,delta^2),
    F(r)=(1+r)h(1/(1+r)).

The first term is at most 2delta. The next divided by delta is at most 2 beta[2log(1/beta)+1/ln 2], uniformly bounded. Since mu0+delta^2<=1, the last term is at most delta^2[2log(1/delta)+1/ln 2]=O(delta). Thus D_i=O(delta) uniformly over width and number of tribes. extra_checks.json independently verifies the formula on small tribes.

7(i): the largest-influence conjecture is false by (f). The finite best-coordinate maximum and witness appear in records.json; no finite census establishes a universal bound.

9(a): the R bracket is proved in (b). The balanced perfect-matching-plus-coins function reconstructed in records.py has H/(I-1) given in records.json; record_precision.json independently recomputes it with an integer transform and 80-digit Decimal logarithms. If balanced g has H=h and I=j>1, iterated self-composition has influence j^k and entropy h(1+j+...+j^(k-1)); this follows by expanding disjoint balanced blocks and applying the entropy chain rule. The ratio tends to h/(j-1), verifying the stated lower bound on C* and R. The four-decimal 4.8677 and the tribes value 5.997 are finite checks, not exact constants; records.json retains more digits.

10(a): the edge identity and C_E bracket are correct. The line Phi(p,q)<=(c+1)q when q>=2^-c p is false. At c=0 and p=q>0 its two sides are 2q and q. The exact best constant under this condition is

    Phi(p,q) <= [log(1+2^c)+2^c log(1+2^-c)]q.

The ratio Phi(r,1) is increasing in r=p/q, which proves the assertion. A simpler valid constant for c>=0 is c+1+1/ln 2. The printed c+1 bound is valid for the G summand alone. The numerical lower bound on C_E follows from C_E>=C*-2/ln 2 and the checked self-composition lower bound above.

10(b): the vertex identity is correct if rho_i uses symmetric difference for all i, then sums only i not in T. Terms with zero lower mass contribute zero to G and are omitted. Let A be the mu-average number of supported upper neighbours and M=sum_{supported bottom edges}mu(top)<=I. Concavity gives G<=M log(1+A/M)<=I log(1+A/I). This proves the support-degree implication. The informal descriptions of good and bad vertices are heuristics, not pointwise criteria. Many tiny neighbours can have small or large total cost depending on their combined mass. The precise sufficient statement is the average supported-up-degree bound just proved.

10(c): conditioning on a statistic can only increase conditional entropy, proving the witness bound. For a probability pi, the linear statistic E_pi chi_T includes point-mass parity and subcube-uniform miss indicators exactly. Orthogonality gives sum_T fhat(T)^2 chi_T(z)=E_x f(x)f(xz). These identities and their interpretation are correct.

CHECKED scope and reproducibility: audit_results.json, reductions.json, exact_families.json, witnesses.json, extra_checks.json and records.json. None of the calculations is a proof of FEI. The only external theorem comparison used in this project is stated precisely in PROOFS.md, with its primary-source link.
