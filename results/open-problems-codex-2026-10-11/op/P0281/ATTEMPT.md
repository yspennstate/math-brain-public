# P0281: proof by an interlacing lift

2026-10-12. This is an author-derived application of established theorems, not a theorem about the exact question found in print.

## Statement

For rate-one continuous-time TASEP with n particles initially X_i(0)=-i, indexed right to left, write p_t(x)=P(X(t)=x), extended by zero to Z^n. For every finite n>=1, every t>=0, and every a,b in Z^n, we prove

    p_t(a)p_t(b) <= p_t(floor((a+b)/2)) p_t(ceil((a+b)/2)).     (1)

Rounding is componentwise. This explicitly defined stronger lattice statement implies the requested inequality whenever the midpoint is integral. We make no assertion about real-variable extensions. Put D_i=X_i+i; its support is D_1>=...>=D_n>=0. Integer translations commute with rounding, so it suffices to prove (1) for D.

## Two established inputs

**BF:** Borodin--Ferrari, *Anisotropic growth of random surfaces in 2+1 dimensions*, arXiv:0804.3035, downloaded PDF Section 1.1, pages 3--5; Section 2.7, equation (2.101), page 37, and Proposition 2.22, page 38. Their push/block array starts from z_k^m(0)=k-m-1, has rate-one clocks at every coordinate (all parameters alpha_i=1), and satisfies z_k^m<z_k^{m-1}<=z_{k+1}^m. The left edge is step TASEP. Proposition 2.22 gives the fixed-time law as the evolved top-row distribution followed by the interlacing links. We derive its explicit mass below from their formulas.

**HKS:** Halikias--Klartag--Slomka, *Discrete variants of Brunn--Minkowski type inequalities*, arXiv:1911.04392v4, Theorem 1.2, PDF page 1; Ann. Fac. Sci. Toulouse Math. (6) 30(2), 267--279 (2021). Its lambda=1/2 case states: if nonnegative f,g,h,k on Z^r satisfy

    f(u)g(v)<=h(floor((u+v)/2))k(ceil((u+v)/2))

for all u,v, then (sum f)(sum g)<=(sum h)(sum k).

These results are used as established theorems. Neither is a paper proving this exact TASEP question.

## 1. Exact law of the lift

Change coordinates by lambda_i^m=z_{m-i+1}^m+i. The resulting nonnegative partition array satisfies

    lambda_i^{m+1} >= lambda_i^m >= lambda_{i+1}^{m+1}.        (2)

Indeed, substitute k=m-i into z_k^{m+1}<z_k^m<=z_{k+1}^{m+1}, and use integrality on the strict inequality. Initially every lambda is zero. On the left edge D_m=lambda_m^m. The required random vector is therefore a coordinate marginal, not a top-row marginal or a sum of coordinates.

For t>0, let lambda=lambda^n and l_i=lambda_i+n-i. The full array mass is

    W_t(Lambda)=e^(-nt)t^(|lambda|)
                 product_{i<j}(l_i-l_j)/product_i l_i!,      (3)

on (2), and zero elsewhere. All l_i are nonnegative and strictly decreasing.

Here is a derivation checking constants and shifts. For an ascending raw top row y, define V(y)=product_{i<j}(y_j-y_i) and C_n=product_{j=1}^{n-1}j!, with C_1=1. Its initial row is a_i=-n+i-1. BF (2.101) in the equal-alpha limit gives

    P(top=y)=V(y)/V(a) * det[q_t(y_j-a_i)]_{i,j=1}^n,
    q_t(k)=e^(-t)t^k/k! for k>=0; q_t(k)=0 for k<0.          (4)

The confluent limit of their alternant ratio is V(y)/V(a): expand alpha_i=exp(epsilon beta_i); the first nonzero alternating term uses polynomial degrees 0,...,n-1, and its factors in beta and epsilon cancel in the ratio. V(a)=C_n.

Set L_j=y_j+n. On the reachable support L_j>=0. Factor e^(-t)t^(L_j)/L_j! from column j and t^(-(i-1)) from row i in (4). The remaining entry is the falling factorial (L_j)_(i-1), which is zero when L_j<i-1 and otherwise a monic polynomial of degree i-1. Changing this monic polynomial basis to monomials is a triangular row operation with diagonal entries one. Its determinant is V(L). Thus

    det[q_t(y_j-a_i)]
       =e^(-nt)t^(sum L_j-n(n-1)/2)V(L)/product L_j!.         (5)

The equal-alpha interlacing link from an ascending row u of length m to a row v of length m-1 is

    Lambda_m(u,v)=(m-1)! V(v)/V(u)
                   *1{u_i<v_i<=u_{i+1}, 1<=i<m}.            (6)

This is the uniform Gelfand--Tsetlin link. It also follows directly from BF definition (2.94), its matrices on PDF page 24, and Lemma 2.13(ii), equation (2.57). For completeness the confluent calculation includes the normalization: take alpha_i=exp(epsilon beta_i) with distinct beta_i. An alternant of size m has leading term epsilon^(m(m-1)/2)V(beta_1,...,beta_m)V(u)/product_{j=0}^{m-1}j!. The ratio of the size m-1 numerator to the size m denominator therefore contributes epsilon^(-(m-1))(m-1)!V(v)/(V(u) product_{i<m}(beta_m-beta_i)). The reciprocal normalization in their link contributes product_{i<m}(1-alpha_m/alpha_i), whose leading term is epsilon^(m-1)product_{i<m}(beta_i-beta_m). Their step-function determinant equals (-1)^(m-1) times the interlacing indicator in this limit. All epsilon powers and both signs cancel, proving (6). This specifies exactly the links used in Proposition 2.22.

Multiplying (6) for m=n,...,2 gives C_n/V(y) times the full interlacing indicator. Initially the links force the unique packed lower rows, so the initial array has the Gibbs form required by Proposition 2.22. In that proposition take the top row's time interval [0,t] and every subsequent time interval zero. The fixed-time array law is therefore (4) times these links. Multiplying (5), V(y)/C_n, and C_n/V(y) yields (3), because V(L)=V(y), the descending reversal of L is l, and sum L_j-n(n-1)/2=|lambda|.

This is a probability measure: it is the law of a process with n(n+1)/2 independent rate-one clocks, hence nonexplosive. In particular its total mass is one, giving summability without a formal infinite-series identity.

The TASEP projection can also be checked directly. The left-edge coordinate z_1^m is blocked exactly when z_1^m=z_1^{m-1}-1. It is never pushed: a push increases both indices, and an incoming push to an index k=1 would require k=0. Its own unblocked clock moves it by one, possibly pushing coordinates away from the left edge. Thus the edge has exactly the n-particle TASEP generator and initial condition. Uniqueness for this bounded-rate chain identifies its law.

## 2. Rounded-midpoint inequality for the array

For valid arrays A,B, let R=floor((A+B)/2), S=ceil((A+B)/2).

**Support:** every constraint (2), and nonnegativity, is a coordinate comparison or a comparison with zero. If A_u>=A_v and B_u>=B_v, monotonicity of floor and ceiling preserves the comparison for R and S. Both are valid arrays. If an endpoint is invalid its weight is zero and the inequality is trivial.

**Factorials:** for nonnegative integers a,b set r=floor((a+b)/2), s=ceil((a+b)/2). Then r!s!<=a!b!. To prove this, assume a<=b and put k=r-a=b-s>=0. We have

    a!b!/(r!s!)=product_{j=1}^k (s+j)/(a+j)>=1,

since s>=a. The case k=0 is the empty product. Each l_i has an integer shift n-i, which commutes with rounding. Thus each reciprocal factorial factor in (3) satisfies the required product inequality.

**Differences:** fix i<j and write

    a=A_i^n-A_j^n+j-i, b=B_i^n-B_j^n+j-i,
    r=R_i^n-R_j^n+j-i, s=S_i^n-S_j^n+j-i.

All are positive integers. At every coordinate R+S=A+B, hence r+s=a+b. The quantity R_u-S_u is either zero or minus one, so |r-s|<=1. A balanced integer pair maximizes a product with fixed sum. Explicitly,

    rs-ab=((a-b)^2-(r-s)^2)/4.

If a+b is even then r=s. If it is odd then (r-s)^2=1 and a-b is an odd integer, so (a-b)^2>=1. In both cases ab<=rs. This proves the inequality for each Vandermonde factor, without incorrectly commuting subtraction with rounding.

**Time factors:** |R^n|+|S^n|=|A^n|+|B^n|, so the two products of powers of t coincide. Their e^(-nt) factors also coincide. Multiplying the positive factorial and difference inequalities proves

    W_t(A)W_t(B)<=W_t(R)W_t(S) for every A,B in Z^N,          (7)

where N=n(n+1)/2 and weights outside the support are zero.

## 3. Marginalization and conclusion

Permute the array coordinates to put d=(lambda_1^1,...,lambda_n^n) first and denote the remaining coordinates by u in Z^(N-n). Coordinate permutations commute with rounding. For any fixed d,e in Z^n define

    f(u)=W_t(d,u), g(u)=W_t(e,u),
    h(u)=W_t(floor((d+e)/2),u),
    k(u)=W_t(ceil((d+e)/2),u).

For every u,v, (7) gives precisely the premise of HKS Theorem 1.2 at parameter 1/2. Every slice is summable since W_t is a probability mass function. Its conclusion is

    P(D=d)P(D=e)<=P(D=floor((d+e)/2))P(D=ceil((d+e)/2)).      (8)

This uses only coordinate marginalization; arbitrary linear projections are not asserted to preserve the inequality. If using a finite-support formulation of HKS, truncate all four slices to the same box [-M,M]^(N-n). The box is closed under both rounded midpoints, so the premise still holds. Monotone convergence proves (8) for the full slices. For n=1 there are no hidden coordinates and (8) is (7).

Translate D_i=X_i+i to prove (1). At t=0 the law is a point mass; a positive left side forces both endpoints to be the initial configuration, proving (1) there as well. This establishes every quantifier in the stated problem.

## 4. Referee audit and checks

* **Model:** the left edge, not the right (PushASEP) edge, is used. Its generator was checked directly.
* **Law:** the top-row law has two Vandermonde factors; the links cancel one, leaving (3). Formula (5) checks the factorial shifts and time powers. No identification of a Schur top row with the TASEP vector is assumed.
* **Rounding:** every support constraint is preserved. The difference-factor proof handles the possible parity mismatch between coordinates explicitly.
* **Marginals:** the diagonal is a coordinate selection. Infinite sums are summable and can be handled by boxes; t=0 is separate.
* **Exact finite checks:** structural_checks.py checks (7) with exact rational weights at t=1 (dropping e^(-n)): n=2, cap 6, 3570 pairs; n=3, cap 3, 6328 pairs; n=4, cap 2, 8001 pairs. Every check passed. These corroborate the algebra, not replace the proof.
* **Numerical caution:** the sparse matrix exponential in search_midpoints.py uses absolute tolerances and produced apparent failures at tiny tail probabilities. Three were rechecked using 90-digit positive uniformization, retaining 140 terms. Their midpoint ratios became 1.0343944873, 1.0831133273, 1.1392316090; they are not counterexamples. Other un-rechecked tiny-mass negatives in numerics.json are unreliable. These calculations are numerical evidence, not interval certificates.
* **Independent representation check:** structural_checks.py sums the n=3 array law at t=0.5 through top coordinate 20 and compares 77 edge states with a separately built TASEP generator. Maximum relative discrepancy is 4.54e-8 among probabilities above 1e-12, consistent with floating-point absolute error. Further high-precision comparison is recorded separately.
* **Lean scope:** Midpoint.lean checks integer balancing, rounded differences, and support constraints using kernel-checked tactics. The corrected run passed, exit code 0, recorded in lean_check_2.txt. All three printed axiom lists contain only propext, Classical.choice, and Quot.sound, with no sorryAx. No native_decide is used. It does not formalize BF, HKS, or the stochastic proof. The initial failed encoding run is preserved as lean_check.txt.

There is no remaining mathematical gap in the target proof beyond reliance on the two explicitly stated established theorems. The literature search is bounded and rate-limited, so novelty is not certified.

## Research artifacts and remaining gap

Scripts: fetch.py, followup.py, structural_sources.py, latest_search.py, locate_followup.py, record_literature.py reproduce the web checks; search_midpoints.py, tail_recheck.py, structural_checks.py, representation_check.py reproduce the computations. Every artifact is in this problem folder.

The high-precision representation check at n=3,t=0.5 compares six states: (0,0,0), (1,0,0), (1,1,0), (1,1,1), (4,2,1), (6,3,0). Array sums through top coordinate 40 agree with independently uniformized TASEP at relative errors between 3.4e-61 and 3.3e-56. These finite positive sums are corroborating numerical checks; they are not used to prove equality.

Mathematical remaining gap: none for the stipulated finite-particle integral-midpoint assertion, using BF Proposition 2.22 and HKS Theorem 1.2 as established inputs. Formal-verification scope and bounded-literature limitations are stated above.
