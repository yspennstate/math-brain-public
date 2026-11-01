# F0118 — working notes, 12 October 2026

## Exact question
Fix the same b-ary tree, integer 2 <= q < r, and 0 < lambda < 1.
Let M_q = lambda I + (1-lambda)J/q. Does reconstruction for M_q imply reconstruction for M_r?
The restriction lambda < 1 follows from the source's ergodicity assumption; lambda is the eigenvalue itself, not its absolute value. Mossel defines it as the eigenvalue having second largest absolute value, so positivity selects the ferromagnetic case.

## A. Proved finite special case: one-generation pairwise TV is monotone in q
This is a finite-depth statement, not a proof of the conjecture.

Take any b >= 1 and compare root labels 1 and 2. Put c=(1-lambda)/q, p=lambda+c, and z=1-lambda-2c. A boundary word with counts N_1,N_2 has likelihood ratio (p/c)^(N_1-N_2) under the two root laws. Since p>c>0, the positive part of the likelihood difference is exactly the event N_1>N_2. Swapping labels 1 and 2 gives

    TV_q(b,1) = P_1(N_1>N_2) - P_1(N_1<N_2).

Under root 1 the difference is S_b, the sum of b independent steps taking +1,-1,0 with probabilities p,c,z. Thus TV_q=E sign(S_b), with sign(0)=0.

Fix lambda and view this polynomial as a function F_b(c) on 0 <= c <= (1-lambda)/2. Differentiating each of the b factors of the step distribution (derivatives +1,+1,-2 for +1,-1,0) gives, including at the endpoints by polynomial continuity,

    F_b'(c) = b E[sign(S_(b-1)+1)+sign(S_(b-1)-1)-2sign(S_(b-1))]
            = b[P(S_(b-1)=-1)-P(S_(b-1)=1)].

The discrete second difference of sign is +1 at -1, -1 at +1 and zero at every other integer. For b>=2, enumerate words with k minus steps and k+1 plus steps. Swapping plus and minus and subtracting their probabilities yields

    F_b'(c) = -b lambda sum_{k=0}^{floor((b-2)/2)}
      (b-1)! / ((k+1)! k! (b-2-2k)!)
      * [c(lambda+c)]^k * (1-lambda-2c)^(b-2-2k) <= 0.

For b=1 the derivative is zero and F_1=lambda. Increasing integer q decreases c, proving the claimed TV monotonicity for every b. For b=2, F_2=lambda(2-lambda-2c). For b>=2 and c>0 the derivative is strictly negative: if b is even the final summand has zero exponent of z and is positive, and if b is odd the k=0 term is positive whenever z>0. For odd b and q=2, z=0 can make the endpoint derivative vanish; integrating across a nonempty interval to q>2 still gives strict increase. Hence pairwise TV is strictly increasing in integer q for b>=2.

What prevents induction: at depth two the independent children contribute q-dimensional random likelihood vectors rather than iid three-valued steps. Their laws change with q. The derivative identity above does not compare those laws. Monotonicity at every fixed depth, if proved, would settle the question by taking limits, but only depth one is proved here.

## A2. Proved finite special case: depth two on the binary tree

For every integer q>=2 and fixed 0<lambda<1, pairwise root TV at depth two on the binary tree is strictly increasing in q. Here is a full computation with its sign choices justified.

Write l=lambda and c=(1-l)/q. For a child subtree containing two observed leaves, set

    A=c(l^2+3lc+qc^2), B=c^2(3l+qc), u=l^2(l+2c), v=l^2 c.

These are actual probabilities, not unnormalized posteriors. If the leaves have the same label x, integrating out the child state gives likelihood A+u when the root label equals x and A otherwise. Indeed, with a=l+c, this integration is c[a^2+(q-1)c^2]+l[a^2 if root=x else c^2]. If the two leaf labels are distinct x,y, the likelihood is B+v when root is x or y and B otherwise; the corresponding integration is c[2ac+(q-2)c^2]+l[ac if root in {x,y} else c^2].

For testing root 1 against 2 there are seven categories of ordered leaf pairs:

| category | root-1 likelihood | root-2 likelihood | multiplicity |
|---|---|---|---|
| E1: both 1 | A+u | A | 1 |
| E2: both 2 | A | A+u | 1 |
| E0: both same other label | A | A | q-2 |
| D12: distinct 1 and 2 | B+v | B+v | 2 |
| D1: 1 and an other label | B+v | B | 2(q-2) |
| D2: 2 and an other label | B | B+v | 2(q-2) |
| D0: two distinct other labels | B | B | (q-2)(q-3) |

All seven categories are disjoint and exhaust the q^2 possibilities. At q=2 the last three categories and E0 are empty; their listed multiplicities vanish. At q=3 D0 is empty. Let m=2(q-2) and let Z be the total likelihood of all neutral categories under either root:

    Z=(q-2)A+[(q-2)(q-3)+2]B+2v.

The nonneutral likelihood ratios are R_E=(A+u)/A, its reciprocal, R_D=(B+v)/B and its reciprocal. Since A,B,u,v>0, R_D>1, and

    uB-vA = l^2 c^2 [2l^2+(q+3)lc+qc^2] > 0,

we have R_E>R_D>1. Thus every absolute value in the root likelihood difference for the two child subtrees has a determined sign, independent of q and l. Pairing positive and negative symmetric categories gives the exact TV polynomial

    F(q,l)=u(2A+u)+m^2 v(2B+v)
          +4m uB+2m uv+2(u+mv)Z.

For completeness the contributions are: E1/E1 and E2/E2 together give u(2A+u); D1/D1 and D2/D2 give m^2 v(2B+v); mixed E and D with the same sign give 2m(uB+vA+uv); mixed E and D with opposite signs give 2m(uB-vA); neutral against E or D in either ordering gives 2(u+mv)Z. Opposite E pairs, opposite D pairs, and pairs of neutral categories give zero. This accounts for every pair of categories and the factor 1/2 in TV.

Substitute c=(1-l)/q into this displayed F and differentiate in continuous q, holding l fixed. To verify the derivative's sign without numerical estimates, put q=t+2 and l=a/(a+1), with t>=0 and a>0. Expansion and collecting terms gives

    (partial F/partial q)(t+2,a/(a+1))
      = 2a^2 [(a^3+6a^2+18a+6)t^2
               +(4a^3+22a^2+2a)t
               +4a^3+20a^2+22a+6]
        / [(a+1)^6(t+2)^4] > 0.

This algebraic identity follows by substitution into the preceding explicit polynomial, and `depth_two_symbolic.py` checks it using exact polynomial arithmetic. The denominator and all numerator terms are nonnegative, with a strictly positive constant term. Every 0<l<1 is represented by a=l/(1-l)>0. Hence F is strictly increasing over real q>=2 as a rational extension, and in particular across its integer alphabet sizes. Noninteger category multiplicities are not interpreted as probabilities; the rational extension is used only to compare integer values by integration of its positive derivative.

This proof extends the finite-depth result to a nontrivial tree with hidden branching vertices, but does not extend to depth three or to an infinite-depth reconstruction comparison. No novelty claim is made.

## B. Independent stochastic recoloring is possible only for divisible alphabets
Let K be an r by q stochastic matrix, applied to all vertices using independent auxiliary randomness, independent of the broadcast. Assume a uniform root for the r-process and require the resulting process to have exactly the uniform-root q-Potts law at the same lambda. This restricted simulation is possible if and only if q divides r.

The output marginal being uniform requires sum_x K(x,a)=r/q. The input parent-child joint law is lambda delta_xy/r+(1-lambda)/r^2. Independence of the two recolorings then gives output edge law

    lambda (K^T K)(a,d)/r + (1-lambda)/q^2.

Equating this to the desired law lambda delta_ad/q+(1-lambda)/q^2 and dividing by lambda>0 shows K^T K=(r/q)I. For a != d, sum_x K(x,a)K(x,d)=0. All summands are nonnegative, so every product is zero. Each row has at most one positive entry, and its sum is 1, so that entry is 1. K is a deterministic partition map. Its column sums count the fibers, and each is r/q; hence q divides r. This argument uses only one edge and is stronger than assuming a pointwise Markov intertwining condition.

Conversely a partition into q equal blocks sends a reset-uniform draw to a reset-uniform block and a copy edge to a copy edge. Conditional child distributions depend only on the parent's block; conditional independence of children is retained because their conditional block probabilities do not depend on the hidden within-block label. Thus it gives exactly the q-Potts broadcast on the whole tree.

For such a map f, choose i,j in different blocks a,d. The pushforwards of the level-n laws conditional on root i,j are the q-state laws conditional on a,d. Data processing for TV gives TV_r(i,j;n)>=TV_q(a,d;n). Taking limits proves the divisible case of the conjecture. By symmetry all distinct root pairs of a symmetric channel have the same TV. This is the source's known special case, not a novelty claim.

Failure mode checked: M_r K=K M_q merely requires uniform column average, and does not imply a broadcast simulation. For example K(x,a)=1/q intertwines but independent recoloring makes the entire output iid uniform; its edge covariance is zero, not lambda. Shared or correlated recolorings, and boundary maps depending on many vertices, are outside this obstruction.

The intake's 9 September 2026 attempt already identified this obstruction by a stronger pointwise condition. The edge-law calculation above supplies a proof under the weaker assumption of equality in distribution alone.

## C. Universal necessary and sufficient bounds (complete elementary proofs)

### Necessary: b lambda > 1
Generate each edge independently by copying the parent with probability lambda and otherwise resetting to an independent uniform label. The vertices connected to the root by copy edges form a Galton-Watson tree with Binomial(b,lambda) offspring. Couple broadcasts with root i and j by using the same copy indicators and the same reset labels. Every vertex outside the root's copy cluster has identical labels in the two broadcasts: the first reset along its path removes the root dependence. Therefore

    TV(P_i^n,P_j^n) <= s_n,

where s_n is the probability of a copy path reaching level n. Starting with s_0=1, independence of the b child clusters gives

    s_(n+1)=1-(1-lambda s_n)^b.

These survival events are decreasing, so s_n decreases to s>=0. If b lambda<1, the union bound gives s_n<=(b lambda)^n, hence s=0. If b lambda=1, b>=2 because 0<lambda<1. For s>0 and 0<lambda s<1, the strict union bound 1-(1-lambda s)^b < b lambda s=s contradicts the fixed-point equation obtained by continuity. Thus s=0 also at equality. Reconstruction is impossible whenever b lambda<=1. On the b=1 path it is impossible for every admissible lambda; directly M_q^n=lambda^n I+(1-lambda^n)J/q gives pairwise TV=lambda^n.

### Sufficient: b lambda^2 > 1
Let the root be uniform. Choose a real function f on the q labels with uniform mean 0 and uniform second moment 1, e.g. f(1)=sqrt(q-1), f(i)=-1/sqrt(q-1) for i!=1. Then M_q f=lambda f. Let F_n contain labels up to level n and put

    Z_n=(b lambda)^(-n) sum_{v in L_n} f(sigma_v).

Conditioning on F_n proves E[Z_(n+1)|F_n]=Z_n, so Z_n is a martingale with Z_0=f(root). The innovations of distinct children are conditionally independent, with zero conditional mean. Every vertex has the uniform marginal, so the unconditional mean of Var(f(child)|parent) is

    E f(child)^2 - E[lambda f(parent)]^2 = 1-lambda^2.

Consequently

    E[(Z_(n+1)-Z_n)^2]=(1-lambda^2)(b lambda^2)^(-(n+1)).

Martingale increments are orthogonal: if k<l, condition on F_l to see E[(Z_(k+1)-Z_k)(Z_(l+1)-Z_l)]=0; they are also orthogonal to Z_0. Therefore, writing R=b lambda^2>1,

    E Z_n^2=1+(1-lambda^2)sum_{k=1}^n R^(-k)
           <= C=1+(1-lambda^2)/(R-1).

Also E[Z_n|root]=f(root), by iterating the single-edge mean relation. Hence E[f(root)Z_n]=1. Write h_n=E[f(root)|sigma_n]. Z_n is measurable from sigma_n alone, so E[h_n Z_n]=1 and Cauchy-Schwarz gives E h_n^2>=1/C.

To connect this directly to reconstruction, let P_i^n be the level-n law given root i, and let Pbar^n=q^(-1)sum_i P_i^n. The joint law of (root,sigma_n) has TV distance from the product of its marginals

    D_n=(1/q)sum_i TV(P_i^n,Pbar^n).

If all pairwise root TVs tended to zero, the triangle inequality and convexity of TV would give D_n->0. For posterior probabilities p_i(y), the function h_n(y)=sum_i f(i)(p_i(y)-1/q) satisfies

    E|h_n| <= ||f||_infinity E sum_i |p_i-1/q| = 2||f||_infinity D_n.

Since |h_n|<=||f||_infinity, E h_n^2<=2||f||_infinity^2 D_n. This contradicts its positive lower bound. Thus reconstruction holds. In fact Z_n depends only on the census, giving census reconstruction by the identical argument with the census in place of sigma_n. These are known bounds, re-proved here to isolate the difficult range.

### Consequences
The conjecture holds for every q,r when b lambda^2>1, since the conclusion holds without using the premise; it holds vacuously when b lambda<=1. For q=2, the verified binary threshold (Mossel's Theorem 3.1, PDF p.4) gives b lambda^2>1 from reconstruction, and the preceding sufficient bound gives reconstruction for every r>2. This last implication uses the cited binary theorem, not a new proof of its necessity.

The genuinely unresolved range after these bounds is

    b>=2, q>=3, q<r, q does not divide r, 1/b < lambda <= 1/sqrt(b).

The upper endpoint is deliberately included: the binary critical result cannot simply be transplanted to every q.

### Additional implication of a verified later large-degree theorem
For q=3 or q=4, there is a b0 such that the conjecture holds for all b>=b0 and all r>q. This is a derived special case of Mossel–Sly–Sohn, Theorem 1.12, not the full conjecture and not a new threshold theorem. To check its assumptions for regular trees, one can use the real-d offspring family with support {floor(d),ceil(d)} and weights chosen to have mean d. For d>1, 1/2<=X_d/d<=2, so K(theta)<=exp(2theta)<infinity, and Assumption 1.11 holds with C1=1/2,C2=2 with probability one. At integer d=b the family is deterministic and its tree is exactly T_b. The theorem therefore rules out reconstruction for q=3,4 and b>=b0 when b lambda^2<=1. Reconstruction for these q's forces b lambda^2>1, and the sufficient bound above gives reconstruction for every r. The existence of b0 is all that is used; no numerical b0 is claimed.

A further lead discovered through GitHub is OpenAI's 5 October 2026 four-state threshold manuscript, whose Theorem 1.1 states non-reconstruction for q=4 at b lambda^2<=1 for every integer b>=2. Taken with the sufficient bound, this would remove the large-degree restriction in the q1=4 implication. It is recorded as a literature lead with its exact scope in LITERATURE.md; its sizeable exact-arithmetic certificates have not been independently re-run in this attempt. It does not settle q1=3 at small degree or arbitrary nondivisible q1>=5.

### Critical boundary when the target alphabet has at least five states
For b>=2 and r>=5, Sly's verified Theorem 1.2 (PDF p.4) states that the positive r-state reconstruction threshold lambda_+(r,b) is strictly below b^(-1/2). Hence at lambda=b^(-1/2) the r-state process reconstructs, independently of the source alphabet. This proves the conjecture at that boundary for every r>=5. It is a consequence of a published threshold theorem and not a claim of a general monotonicity theorem in print. In the remaining range with r>=5, the upper inequality can therefore be made strict: 1/b<lambda<1/sqrt(b).

## D. Exact experiments and verification

`finite_checks.py` enumerates all leaf configurations by integer likelihood vectors. For lambda=L/D, every edge numerator is D-L off-diagonal and Lq+D-L on the diagonal; the edge denominator is Dq. At depth n with E=sum_(j=1)^n b^j edges, every boundary likelihood has common denominator (Dq)^E. Recursive multiplication and summation integrate out all internal labels. The script verifies that each root-conditioned law sums to 1 before computing pairwise TV exactly as sum_y |l_1(y)-l_2(y)|/[2(Dq)^E].

For b=2, all adjacent-q comparisons passed for lambda in {1/5,2/5,1/2,3/5,4/5}, depth 1 with q=2,...,10, depth 2 with q=2,...,8, and depth 3 with q=2,3,4: 95 exact laws and 80 adjacent comparisons. Examples at lambda=1/2:

| q | depth 1 TV | depth 2 TV | depth 3 TV |
|---|---|---|---|
| 2 | 1/2 | 11/32 | 1963/8192 |
| 3 | 7/12 | 703/1728 | 380861/1327104 |
| 4 | 5/8 | 113/256 | 166177/524288 |

The script additionally checks the derivative polynomial exactly with SymPy for b=1,...,8. These computations support the stronger finite-depth comparison conjecture but prove no infinite-depth threshold. The posterior L2 entries in `finite_results.json` are floating-point auxiliary statistics and have no certified asymptotic meaning.

`FiniteAlgebra.lean` formalizes the discrete second-difference identity of the integer sign function, the scalar implication x*x=x -> x=0 or x=1 over the reals, and the fact that a row summing to 1 with all distinct cross products zero has every entry 0 or 1. It also checks the mixed-ratio identity uB-vA used at depth two and strict positivity of the transformed derivative numerator. These are key algebraic steps; the probabilistic proofs, full derivative rational identity, and full monotonicity conjecture are not formalized. Check outcome is recorded in `lean_check.log`.

## E. Hostile-referee audit

1. **Eigenvalue sign:** source defines an eigenvalue ordered by modulus; the positive hypothesis does not allow antiferromagnetic channels. Section 2 and equation (8) checked directly.
2. **Uniform root:** symmetric channels have uniform stationary measure; source Proposition 2.1 permits using this measure for reconstruction. The joint-TV argument above is also explicit.
3. **Star derivative:** varying c holds lambda fixed, and changes neutral mass by -2 dc. Missing this term would give a false comparison. The full three-term derivative and its integer sign identity were checked symbolically and are formalized separately.
4. **Neutral symbols:** at depth one only counts of labels 1 and 2 matter to their likelihood ratio, so merging all q-2 other labels is justified. This simplification is not asserted at greater depth.
5. **Finite vs asymptotic:** positive TV at finitely many depths says nothing about a positive limiting TV. No finite enumeration is promoted to a threshold result.
6. **Recoloring scope:** the obstruction requires the same fixed K at each vertex and independent auxiliary randomness. It rules out this method, not the conjecture or all couplings. Intertwining is not substituted for equality of the output broadcast law.
7. **Criticality:** copy-cluster extinction at b lambda=1 was proved rather than inferred from subcritical bounds. Census results alone do not decide b lambda^2=1.
8. **Second moment:** conditional child independence is used only after conditioning on all parent labels; averaging each conditional variance gives 1-lambda^2 under stationarity. The common random parent creates no additional innovation covariance.
9. **Literature status:** no retrieved theorem asserts the full comparison for arbitrary pairs of finite alphabets. Rate-limited services prevent an exhaustive citation check. Asymptotic and large-degree results are leads only.

## Remaining gap
Need a comparison at arbitrarily large depths, or of nontrivial limiting posterior distributions, for cases outside all the preceding special cases. With r>=5, the uncovered nonlinear range is 1/b<lambda<1/sqrt(b), q>=3, q<r, q not dividing r; for q=3,4 only degrees below the large-degree theorem's bound are uncovered. For target r=4, the remaining source q is 3 and the upper boundary lambda=1/sqrt(b) is still included at small degree in our independently supported reductions. The October 2026 all-degree four-state threshold lead supplies further special-case information if accepted, but never an arbitrary-alphabet comparison. Finite-depth enumeration is not an asymptotic certificate. No proof or counterexample to the full conjecture has been obtained.

Final Lean result: `lake env lean` from `~/lean_verify` exited 0 for the complete `FiniteAlgebra.lean` file. All five algebraic theorems are kernel-checked, with no sorry or native_decide. The first two runs exposed only missing imports (Omega and Finset.mul_sum); both imports were corrected before the successful run. This does not formalize the full probabilistic statements.

## Second attempt, requested before closure (12 October 2026)

The complete second attempt is in [SECOND_ATTEMPT.md](SECOND_ATTEMPT.md). Two untried approaches were written down: binary Blackwell/convex-order comparison through copy-cluster coloring, and posterior population dynamics with a certification step. The first was pursued.

New proved special case: the full binary root experiment is monotone in Blackwell order across integer alphabet sizes for any finite number of independent two-leaf branches, with a fixed parent-to-child parameter alpha and a fixed leaf-pair parameter beta per branch, allowed to differ between branches. This strengthens the original depth-two binary-tree TV theorem and is proved using an explicit stop-loss derivative and a finite convex-order/garbling construction.

Two stronger-method statements were disproved with exact certificates: (i) arbitrary q-independent rooted-partition coloring need not be Blackwell monotone (q=4 to 5, payoff difference -167/5032800); (ii) pairwise binary Blackwell order of symmetric q=3 experiments is not preserved by a common Potts edge of eigenvalue 1/2 (payoff difference -19/750). Neither is a counterexample to F0118. The first prior is not a tree copy-cluster law; the second consists of generic symmetric experiments, not asserted to be generated by pure tree broadcasts. Both still have the expected nonnegative total-variation comparison.

Exact independent validation checked 63 branch laws, 54 branch comparisons, one heterogeneous three-branch comparison, and both auxiliary counterexamples. A separate true-tree search checked 43 complete finite Blackwell comparisons with no failure. Lean kernel checked four new algebraic identities. These results and their limitations are recorded in the second-attempt report and new claim rows.

The remaining infinite-depth gap is unchanged in scope, with a sharper methodological requirement: a comparison must track the complete q-state conditional experiment or an additional invariant of the actually BP-generated class; generic pairwise Blackwell order does not close under an edge. Full F0118 remains unproved, no counterexample obtained. Second-attempt verdict: PARTIAL.
